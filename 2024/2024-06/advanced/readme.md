# Challenge: Sudoku Solver

**Description:**

Write a program that solves a given 9x9 Sudoku puzzle. The program should take a 2D list representing the puzzle as input and fill in the missing numbers. Sudoku puzzles follow these rules:
1. Each row must contain the numbers 1-9 without repetition.
2. Each column must contain the numbers 1-9 without repetition.
3. Each of the nine 3x3 subgrids must contain the numbers 1-9 without repetition.

**Example Input:**

[
[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]
]


**Example Output:**

[
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]
]


**Hint:** Use a backtracking algorithm to try filling numbers in the empty cells and backtrack if a number violates the Sudoku rules.

---

# Bonus Challenge: N-Queens Problem

**Description:**

Extend your Sudoku solver by solving the N-Queens problem for an `n x n` chessboard. The N-Queens problem is to place `n` queens on an `n x n` chessboard such that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.

**Example Input:**

4


**Example Output:**

[
[".", "Q", ".", "."],
[".", ".", ".", "Q"],
["Q", ".", ".", "."],
[".", ".", "Q", "."]
]


**Hint:** Use a backtracking algorithm to place queens on the board one by one and check for conflicts.

---


