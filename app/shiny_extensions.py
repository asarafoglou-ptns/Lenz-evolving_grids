import shiny
from htmltools import TagAttrValue, TagChild, tags
# noinspection PyProtectedMember
from shiny._namespaces import resolve_id


def unstyled_input_action_button(
        _id: str,
        label: TagChild,
        *args,
        **kwargs: TagAttrValue,
):
    """
    Because shiny doesn't allow this, I had to find a hacky way to set class-names
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