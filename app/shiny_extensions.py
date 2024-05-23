import shiny

from htmltools import TagAttrValue, TagChild, tags
from typing import List, Callable, Any, TypeVar
from starlette.websockets import WebSocketState
from shiny import Session, Inputs, reactive

# noinspection PyProtectedMember
from shiny._namespaces import resolve_id
# noinspection PyProtectedMember
from shiny._connection import StarletteConnection


def unstyled_input_action_button(
        _id: str,
        label: TagChild,
        *args,
        **kwargs: TagAttrValue,
):
    """
    Because shiny doesn't allow this, I had to find a way to set class-names
    on buttons. This function mimics the way shiny input_action_buttons are
    created, BUT still allows you to attach custom classes to it.
    ! Make sure that you pass the "action-button" to it, otherwise shiny will
    not be able to detect that the button is indeed an action button.
    :param _id: The id of the button
    :param label: The label of the button
    :return: a shiny button
    """
    return tags.button(
        label,
        id=resolve_id(_id),
        type="button",
        *args,
        **kwargs,
    )


# noinspection PyProtectedMember
def session_is_active(session: Session) -> bool:
    """
    This is a hack to check if the session is still active.
    Because shiny doesn't provide a way to check this, we have to use
    a private attribute of the session object.
    :param session: The shiny session
    :return: True if the session is still active, False otherwise
    """
    return (
            cast(StarletteConnection, session._conn).conn.client_state
            == WebSocketState.CONNECTED
    )


def register_dynamic_events(
        shiny_input: Inputs, event_list: List[str] | reactive.Value[List[str]]
) -> Callable:
    """
    Shiny does not allow the registration of events to dynamic html (for example
    a list of buttons which can get longer and shorter). Therefore, I had to
    create a workaround which allows to do that.
    :param shiny_input: The shiny input of the server
    :param event_list: A list of events that should be subscribed to (can be a
                       reactive value with a str list if the events that should
                       be subscribed to change
    """

    def decorator(func):
        # keep track of the effects in case we have to unsubscribe from events
        registered_effects: List[reactive.Effect] = []

        def register_for_events(events: List[Any]):
            # actually register to the events
            def register_for_event(index: int, e: str):
                @reactive.Effect
                @reactive.event(shiny_input[e])
                def wrapper():
                    func(e, index)

                return wrapper

            # for each event register the event and then save the effect, so we
            # can discard it later
            for idx, item in enumerate(events):
                effect: shiny.reactive.Effect_ = register_for_event(idx, item)
                registered_effects.append(effect)

        def re_register_for_event():
            # unsubscribe from the events and then re-subscribe
            for effect in registered_effects:
                effect.destroy()

            registered_effects.clear()
            # noinspection PyProtectedMember
            register_for_events(event_list._value)

        nonlocal event_list
        # if the events are an event list then we also need to subscribe to
        # changes in addition to just registering the events
        if isinstance(event_list, reactive.Value):
            on_value_change(event_list, lambda _: re_register_for_event())
            # noinspection PyProtectedMember
            register_for_events(event_list._value)
        else:
            register_for_events(event_list)

    return decorator


T = TypeVar("T")


def on_value_change(
        val: reactive.Value[T], value_changed: Callable[[T], Any]
) -> None:
    """
    registers an onChange callback which gets called every time the reactive
    value changes
    :param val: The reactive value that should be monitored
    :param value_changed: The callback which should be executed
    """

    def wrap(fun: Callable[[T], Any]):
        def _rerun(value: T):
            fun(value)
            # call in 10ms, because otherwise there will be some weird behaviour
            threading.Timer(0.01, value_changed, args=(value,)).start()

        return _rerun

    # monkey patch the set method
    val.set = wrap(val.set)


# noinspection PyProtectedMember
def session_is_active(session: Session) -> bool:
    """
    This is a hack to check if the session is still active.
    Because shiny doesn't expose a way to check this, we have to use
    a private attribute of the session object.
    :param session: The shiny session
    :return: True if the session is still active, False otherwise
    """
    return (
            cast(StarletteConnection, session._conn).conn.client_state
            == WebSocketState.CONNECTED
    )
