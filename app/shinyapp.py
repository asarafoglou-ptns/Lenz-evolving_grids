import asyncio

from pathlib import Path
from typing import List
from htmltools import Tag

from shiny import App, Inputs, Outputs, Session, reactive, render, ui

from app.grid_functions import Grid
from app.shiny_extensions import (session_is_active,
                                 unstyled_input_action_button)


# functions ----
def create_grid_ui(grid: Grid) -> Tag:
    """
    creates the grid for actually playing the Game of Life, including all the
    buttons
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
    Creates a list with all button_ids in the dynamic_grid.
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

    # here, I create a dynamic list of all the buttons in the dynamic_grid that
    # I can use to register clicks on all buttons. It's a reactive value because
    # the size of the grid can be adjusted, so the buttons in the grid change.
    buttons = reactive.Value(create_btn_id_list(dynamic_grid))

    # grid ---
    # show alive cells
    @output
    @render.ui
    def grid():
        """
        renders the grid (after values have been toggled by clicking on them)
        :return: the adapted/updated grid
        """
        return create_grid_ui(dynamic_grid())





# Combine into a shiny app ----
static_files_dir = Path(__file__).parent / "static"
app = App(app_ui, server, static_assets=static_files_dir)