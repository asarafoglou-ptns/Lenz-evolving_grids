import asyncio

from pathlib import Path
from typing import List
from htmltools import Tag

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

from app.grid_functions import Grid, create_grid, toggle_at_position
from app.logic_functions import create_new_generation
from app.shiny_extensions import (register_dynamic_events,
                                           session_is_active,
                                           unstyled_input_action_button)


def create_grid_ui(grid: Grid) -> Tag:
    """
    creates the grid for playing the Game of Life, including all the buttons, which
    can later be displayed in the UI
    :param grid: grid to turn into the game board
    :return: grid in a grid container
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    # here I collect all the rows that should be created
    rows = []
    for row_idx in range(0, n_rows):
        # every row, however also needs some columns. These are created here
        cols = []
        for col_idx in range(0, n_cols):
            # the value of the grid cell at that position (can be either 1 or 0)
            selected = grid[row_idx][col_idx]
            button_class = "grid-button action-button "
            # if the value of a cell is 1, it is coloured to mark it as an
            # alive cell
            if selected == 1:
                button_class += "live-cell"
            # button ID consisting of its row and col
            btn_id = f"btn_{row_idx}_{col_idx}"
            cols.append(
                ui.tags.div(
                    {"class": "grid-column"},
                    # unstyled input button because shiny buttons can't be
                    # styled to look like I want them to look
                    unstyled_input_action_button(
                        btn_id, " ", {"class": button_class}
                    ),
                )
            )

        # after I created all the columns which should be in one row ...
        rows.append(
            # ... I create a new row and add all the columns as children of
            # said row
            ui.tags.div({"class": "grid-row"}, *cols)
        )
        # This gets repeated until all the rows which should be created, have
        # been created

    # return the finished grid and put it inside a grid-container
    return ui.tags.div({"class": "grid-container"}, *rows)


def create_btn_id_list(dynamic_grid: reactive.Value[Grid]) -> List[str]:
    """
    Creates a list with all button_ids in a dynamic_grid
    :param dynamic_grid: The reactive grid containing button information.
    :return: List of button IDs.
    """
    buttons_list = []

    for row_idx, row in enumerate(dynamic_grid._value):
        for col_idx, _ in enumerate(row):
            buttons_list.append(f"btn_{row_idx}_{col_idx}")

    return buttons_list


async def update_board(
        session: Session,
        shiny_input: Inputs,
        is_simulation_running: reactive.Value[bool],
        dynamic_grid: reactive.Value[Grid],
):
    """
    updates the board every 1/(2*n) seconds so that it depicts the new
    generation of alive cells
    """
    # function is active as long as the session is active (as long as the
    # website is open)
    while session_is_active(session):
        # watches if the simulation is running (every 0.1 seconds)
        # noinspection PyProtectedMember
        if not is_simulation_running._value:
            await asyncio.sleep(0.1)
            continue
        # if the simulation is running [is_simulation_running == TRUE], the grid is updated
        # noinspection PyProtectedMember
        old_generation = dynamic_grid._value
        new_generation = create_new_generation(old_generation)

        # if the old generation is the same as the new generation we know that
        # we got stuck and there is no need to simulate anymore.
        if old_generation == new_generation:
            is_simulation_running.set(False)
            ui.notification_show("The game has reached a state of equilibrium.")
            await reactive.flush()
            continue

        dynamic_grid.set(new_generation)
        # notify shiny that a value has changed
        await reactive.flush()
        # then the function sleeps for 1/(2*n) seconds
        # noinspection PyProtectedMember
        await asyncio.sleep(1 / (2 * shiny_input.speed_slider._value))


# UI ----
app_ui = ui.page_bootstrap(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", href="/ui.css"),
    ),
    # header
    ui.tags.div(
        {"class": "coloured-background"},
        # heading
        ui.tags.p({"class": "heading"}, "Evolving Grids"),
        # subheading
        ui.tags.p({"class": "small-text"}, "A Shiny App by Sarah Lenz"),
    ),
    ui.tags.div(
        {"class": "padded"},
        # Description of the Game
        ui.tags.div(
            ui.tags.p({"class": "bold"},
                      "What is Evolving Grids?"),
            ui.tags.p(
                "Evolving Grids is a Python app that allows you to play ",
                ui.tags.b("Conway's Game of Life"),
                " on your laptop. Conway's Game of Life is a simple "
                "simulation that doesn't require active participation. Instead, "
                "you set up an initial configuration of 'alive' and 'dead' cells on "
                "a grid and then observe how they evolve over generations based on "
                "a set of rules.",
                ui.tags.br(),
                ui.tags.br(),
                "Those rules are:",
                ui.tags.br(),
                "1. From one generation to the next, alive cells with 2-3 alive "
                "neighbours stay alive.",
                ui.tags.br(),
                "2. Alive cells with more than 3 alive neighbours die due to overpopulation.",
                ui.tags.br(),
                "3. Dead cells with exactly 3 neighbours come to live through reproduction.",
                ui.tags.br()
            ),
        ),
        # Instructions for how to play the game
        ui.tags.div(
            ui.tags.p({"class": "bold"}, "How to play"),
            ui.tags.p(
                "To play the game, you have to ",
                ui.tags.b("bring cells alive"),
                " by clicking on the grid. Alive cells are marked in orange. By "
                "clicking on the same cell a second time, you kill the cell. ",
                ui.tags.b("Click 'Start'"),
                "to start the simulation and 'Pause' to halt it. You can ",
                ui.tags.b("adjust the speed"),
                " of the simulation using the slider in the control panel "
                "(please note: the larger the grid, the slower the"
                " possible max speed). You can also ",
                ui.tags.b("adjust the size of the grid"),
                ". Clicking on 'Reset' returns the grid to its initial "
                "blank state, but keeps your settings for the size of the grid."
            ),
        ),
        # div with control panel and grid
        ui.tags.div(
            {"class": "side-by-side"},
            # control panel
            ui.tags.div(
                {"class": "control-panel padded"},
                ui.tags.p({"class": "bold"}, "Controls"),
                # div with start/pause and reset button
                ui.tags.div(
                    {"class": "action-buttons"},
                    # start/pause button
                    ui.input_action_button(
                        "toggle_button",
                        ui.output_ui("start_pause_button_text")
                    ),
                    # that calls a function on the server (the button is
                    # displayed based on that function)
                    # reset button
                    ui.input_action_button("reset_button", "Reset"),
                ),
                # div with slider to adjust simulation speed
                ui.tags.div(
                    {"class": "bold"},
                    ui.input_slider(
                        "speed_slider",
                        "Simulation speed",
                        1,
                        10,
                        1,
                        ticks=False,
                    ),
                ),
                # div with controls for adjusting the size of the grid
                ui.tags.div(
                    ui.tags.p({"class": "bold"}, "Grid size"),
                    ui.input_numeric(
                        "grid_rows", "Rows:", min=5, max=35, value=15
                    ),
                    ui.input_numeric(
                        "grid_cols", "Columns:", min=5, max=50,
                        value=15
                    ),
                    ui.input_action_button("submit_grid_size",
                                           "Set grid size"),
                ),
            ),
            # grid
            ui.output_ui("grid"),
        ),
    ),
)


# Server ----
def server(shiny_input: Inputs, output: Outputs, session: Session):
    # variables and reactive values ---
    # here, I create a grid with reactive values
    # noinspection PyProtectedMember
    dynamic_grid = reactive.Value(
        create_grid(shiny_input.grid_rows._value, shiny_input.grid_cols._value)
    )
    # here, I create a reactive value for the button to check if the simulation
    # is currently running
    is_simulation_running = reactive.Value(False)

    # here, I create a dynamic list of all the buttons in the dynamic_grid that
    # I can use to register clicks on all buttons. It's a reactive value because
    # the size of the grid can be adjusted, so the buttons in the grid change.
    buttons = reactive.Value(create_btn_id_list(dynamic_grid))

    # periodically check if the simulation is running and if yes, update the
    # board. unfortunately this is the only way to do that in shiny, because
    # async timers/threading is not supported
    asyncio.create_task(
        update_board(session, shiny_input, is_simulation_running, dynamic_grid)
    )

    # grid ---
    # register which button has been clicked
    @register_dynamic_events(shiny_input, buttons)
    def button_clicked(button_id: str, _: int):
        """
        registers which button in the grid is clicked and toggles its value
        :param button_id: id of a button with the format btn_row_col
        :param _: the index of the event in the event_list
        """

        # the format of the button_id is the following btn_row_col
        # therefore we split this id at "btn_", and select the first index,
        # which is only row_col. If we split that again at "_" we get the
        # row_idx and the col_idx as string
        [row_idx, col_idx] = button_id.split("btn_")[1].split("_")
        # convert said row_idx and col_idx to number to be able to use it as
        # index
        row_idx = int(row_idx)
        col_idx = int(col_idx)

        # toggle the value of the grid cell at the determined position. If the
        # value was 0 before, we put in a 1, otherwise we put a 0
        dynamic_grid.set(
            toggle_at_position(dynamic_grid.get(), row_idx, col_idx)
        )

    # show alive cells
    @output
    @render.ui
    def grid():
        """
        renders the grid (after values have been toggled by clicking on them)
        :return: the adapted/updated grid
        """
        return create_grid_ui(dynamic_grid())

    # adjust grid size
    @reactive.Effect
    @reactive.event(shiny_input.submit_grid_size)
    def set_grid_size():
        """
        sets grid size to the dimensions specified in the corresponding ui.input_numeric fields and stops
        ongoing simulations
        :return: None
        """
        # get the value entered for the number of rows
        grid_rows = shiny_input.grid_rows.get()
        # notification if the value entered for grid_rows is not a numeric value
        if not isinstance(grid_rows, int):
            ui.notification_show("Number of rows has to be a numeric value.")
            return
        # notification if the value entered for grid_rows is outside the
        # possible range
        if not 5 <= grid_rows <= 35:
            ui.notification_show("Number of rows has to be between 5 and 35.")
            return
        # get the value entered for the number of columns
        grid_cols = shiny_input.grid_cols.get()
        # notification if the value entered for grid_cols is not a numeric value
        if not isinstance(grid_cols, int):
            ui.notification_show("Number of columns has to be a numeric value.")
            return
        # notification if the value entered for grid_cols is outside the
        # possible range
        if not 5 <= grid_cols <= 50:
            ui.notification_show(
                "Number of columns has to be between 5 and 50."
            )
            return
        # stop a possibly ongoing simulation when a new grid size is set
        is_simulation_running.set(False)
        # set the new grid size
        dynamic_grid.set(create_grid(grid_rows, grid_cols))
        # update dynamic list of buttons in the grid
        buttons.set(create_btn_id_list(dynamic_grid))

    # reset grid
    @reactive.Effect
    @reactive.event(shiny_input.reset_button)
    def reset_grid():
        """
        this function resets the grid to its original blank state
        :return: None
        """
        dynamic_grid.set(
            create_grid(
                shiny_input.grid_rows.get(), shiny_input.grid_cols.get()
            )
        )
        is_simulation_running.set(False)

    # start/pause button ---
    @reactive.Effect
    @reactive.event(shiny_input.toggle_button)
    def on_button_click():
        """
        whenever the button is clicked, the value of is_simulation_running is
        changed from True to False or the other way around, depending on the
        current value.
        """
        is_simulation_running.set(not is_simulation_running.get())

    @output
    @render.ui()
    def start_pause_button_text():
        """
        Displays the inscription of the button reactively, depending on the
        value of is_simulation_running. When is_simulation_running is 'True',
        the button will read 'Pause', if is_simulation_running is 'False',
        it will read 'Start'.
        :return: the button with its changed inscription
        """
        return ui.tags.span("Pause" if is_simulation_running() else "Start")


# Combine into a shiny app ---
static_files_dir = Path(__file__).parent / "static"
app = App(app_ui, server, static_assets=static_files_dir)
