from typing import List


Grid = List[List[int]]

def create_grid(nrow: int, ncol: int) -> Grid:
    """
    creates an array filled with 0s with the specified dimensions
    :param nrow: number of rows
    :param ncol: number of columns
    :return: array of the given dimensions
    """
    return [[0 for _ in range(ncol)] for _ in range(nrow)]


def copy_grid(grid: Grid) -> Grid:
    """
    creates a copy of a given grid
    :param grid: the grid that should be copied
    :return: copy of the grid
    """
    return [row[:] for row in grid]


def toggle_at_position(grid: Grid, row: int, col: int) -> Grid:
    """
    toggles the value at a specific position in an array from 0 to 1 or from 1
    to 0
    :param grid: array filled with 0s and 1s
    :param row & col: indicate position of the value in array that should be
                      toggled
    :return None
    """
    grid_copy = copy_grid(grid)
    if grid_copy[row][col] == 0:
        grid_copy[row][col] = 1
    else:
        grid_copy[row][col] = 0
    return grid_copy