'''Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:

code:
'''

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def is_valid(board, row, col, num):
            # Check if num is not in the current row
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Check if num is not in the current column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check if num is not in the 3x3 subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False

            return True

        def backtrack(board):
            # Try to find an empty cell
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        # Try numbers 1-9
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                # Recursively try to solve the rest of the board
                                if backtrack(board):
                                    return True
                                # Backtrack if no valid solution found
                                board[i][j] = '.'
                        return False
            return True  # All cells are filled correctly
        
        backtrack(board)

# Example usage
solution = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution.solveSudoku(board)

# Printing the solved board
for row in board:
    print(row)
