import numpy as np

# Initial Sudoku grid (0 represents empty cells)
sudoku_grid = np.array([
    [0, 0, 7,  0, 0, 0,  4, 0, 8],
    [0, 3, 2,  0, 6, 0,  1, 0, 0],
    [0, 0, 0,  0, 0, 9,  7, 0, 0],

    [4, 1, 3,  0, 0, 2,  0, 0, 6],
    [0, 0, 9,  0, 7, 6,  0, 0, 0],
    [0, 0, 0,  0, 0, 5,  8, 0, 4],

    [0, 0, 0,  0, 4, 0,  0, 1, 0],
    [0, 6, 5,  0, 0, 0,  0, 0, 3],
    [0, 0, 4,  2, 0, 0,  0, 0, 0]
])

# Function to check if placing a number is valid
def is_valid(grid, row, col, num):
    # Check the row
    if num in grid[row]:
        return False
    # Check the column
    if num in grid[:, col]:
        return False
    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in grid[start_row:start_row + 3, start_col:start_col + 3]:
        return False
    return True

# Function to solve the Sudoku puzzle
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try all numbers from 1 to 9
                    if is_valid(grid, row, col, num):
                        grid[row, col] = num  # Place the number
                        if solve_sudoku(grid):
                            return True
                        grid[row, col] = 0  # Reset if not valid
                return False
    return True

# Solve the Sudoku puzzle
solved = solve_sudoku(sudoku_grid)

# Output the solved grid
sudoku_grid if solved else "No solution found"
if solved:
    print (sudoku_grid)
