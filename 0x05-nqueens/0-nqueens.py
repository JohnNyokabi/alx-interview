#!/usr/bin/env python3
"""program that solves the N queens chessboard problem"""
import sys


def is_safe(board, row, col, N):
    """
    Check if there is a queen in the same column,
    upper-left diagonal and upper-right diagonals.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def nqueens_helper(board, row, N, result):
    """
    helper function that ensures the board
    is in the required format
    """
    if row == N:
        soln = [[i, j] for i in range(N) for j in range(N) if board[i][j] == 1]
        result.append(soln)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            nqueens_helper(board, row + 1, N, result)
            board[row][col] = 0


def nqueens(N):
    """method of placing N non-attacking queens on an N×N chessboard"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    nqueens_helper(board, 0, N, result)

    for solution in result:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
