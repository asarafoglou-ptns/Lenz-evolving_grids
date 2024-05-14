# this file contains functions which check how many live neighbours a cell has and
# then initiate the according action (keep the cell alive, bring it alive or let it die
# according to the game rules)

from app.grid_functions import Grid, copy_grid


def is_valid_pos(row, column, nrows, ncols) -> bool:
    """
    function checks whether a position is a valid position in an array (e.g.,
    position [-1,-1] would not be valid because it's outside the bounds of the
    array)
    :param row: row in array
    :param column: column in array
    :param nrows: number of rows in array
    :param ncols: number of columns in array
    :return: True if the position is valid; False if the position is not valid.
    """
    # the position is valid if the following is the case
    # 1. 'row' is not smaller than 0 and not bigger than the total number of
    #    rows in the grid
    # and
    # 2. 'column' is not smaller than 0 and not bigger than the total number of
    #    columns in the grid
    return 0 <= row < nrows and 0 <= column < ncols


def get_number_of_adjacent_live_cells(
        grid: Grid, row_idx: int, col_idx: int
) -> int:
    """
    returns the number of alive cells that are adjacent to a specific cell
    :param grid: array in which the number of alive neighbours of the cells
                 should be checked
    :param row & col_idx: indicate the position of the cell in the array for
                          which we want to get the number of alive neighbours
    :return: number of alive cells that are adjacent to the cell indicated by
             row_idx & column_idx
    """
    # Size of given 2d array
    nrows = len(grid)
    ncols = len(grid[0])

    # Initialising a vector array
    # where adjacent live cells will be stored
    number_live_cells = 0

    # checking all (valid) adjacent positions for alive cells
    # if a neighbouring cell is alive, the count of alive cells increases by 1
    if is_valid_pos(row_idx - 1, col_idx - 1, nrows, ncols):
        if grid[row_idx - 1][col_idx - 1] == 1:
            number_live_cells += 1
    if is_valid_pos(row_idx - 1, col_idx, nrows, ncols):
        if grid[row_idx - 1][col_idx] == 1:
            number_live_cells += 1
    if is_valid_pos(row_idx - 1, col_idx + 1, nrows, ncols):
        if grid[row_idx - 1][col_idx + 1] == 1:
            number_live_cells += 1
    if is_valid_pos(row_idx, col_idx - 1, nrows, ncols):
        if grid[row_idx][col_idx - 1] == 1:
            number_live_cells += 1
    if is_valid_pos(row_idx, col_idx + 1, nrows, ncols):
        if grid[row_idx][col_idx + 1] == 1:
            number_live_cells += 1
    if is_valid_pos(row_idx + 1, col_idx - 1, nrows, ncols):
        if grid[row_idx + 1][col_idx - 1] == 1:
            number_live_cells += 1
    if is_valid_pos(row_idx + 1, col_idx, nrows, ncols):
        if grid[row_idx + 1][col_idx] == 1:
            number_live_cells += 1
    if is_valid_pos(row_idx + 1, col_idx + 1, nrows, ncols):
        if grid[row_idx + 1][col_idx + 1] == 1:
            number_live_cells += 1

    # return number of alive cells around a specific cell
    return number_live_cells


def create_new_generation(grid: Grid) -> Grid:
    """
    determines which cells in an array live or die from one generation to the
    next, based on their number of alive neighbours
    :param grid: array with alive and dead cells, for which the next generation
                 should be determined
    :return: array with values indicating which cells survive/come alive/die in
             the new generation
    """
    # first, I make a copy of the grid that holds the 'old generation'
    array_copy = copy_grid(grid)
    # get number of alive neighbours for each cell in the grid with the old
    # generation
    for row_idx, row in enumerate(grid):
        for col_idx, cell_value in enumerate(row):
            alive = get_number_of_adjacent_live_cells(grid, row_idx, col_idx)
            # Apply the rules to keep cells alive, bring them alive, or kill
            # cells to generate the new generation.
            # The new generation of alive and dead cells is stored in the copy
            # of the original grid.
            if cell_value == 1:
                # Kill cell if number of alive neighbours is < 2.
                if alive < 2:
                    array_copy[row_idx][col_idx] = 0
                # Keep cell alive if number of alive cells is 2 or 3.
                elif 2 <= alive <= 3:
                    array_copy[row_idx][col_idx] = 1
                # Kill cell if number of alive neighbours is > 3.
                else:
                    array_copy[row_idx][col_idx] = 0
            else:
                # Bring cell alive if the number of neighbours == 3.
                if alive == 3:
                    array_copy[row_idx][col_idx] = 1

    return array_copy
