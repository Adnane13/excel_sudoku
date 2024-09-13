import random

class SudokuGenerator:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]

    def is_valid(self, board, row, col, num):
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True  # Solved!
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0
        return False

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def generate_full_solution(self):
        self.solve(self.board)
        return self.board

    def remove_numbers(self, board, num_holes=40):
        while num_holes > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            while board[row][col] == 0:  # Find a non-empty cell
                row, col = random.randint(0, 8), random.randint(0, 8)
            board[row][col] = 0
            num_holes -= 1
        return board

    def generate_puzzle(self):
        full_solution = self.generate_full_solution()
        puzzle = [row[:] for row in full_solution]  # Deep copy
        self.remove_numbers(puzzle)
        return puzzle, full_solution

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

if __name__ == "__main__":
    sudoku = SudokuGenerator()

    # Generate puzzle and solution
    puzzle, solution = sudoku.generate_puzzle()

    print("Generated Puzzle:")
    print_board(puzzle)
    print("\nSolution:")
    print_board(solution)
