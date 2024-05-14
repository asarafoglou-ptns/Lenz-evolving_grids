from app.grid_functions import Grid
from app.shiny_extensions import unstyled_input_action_button

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