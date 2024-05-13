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