#!/usr/bin/python3
"""Rotate nxn 2D matrixs by 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """rotates 2D matrix by 90 degrees"""
    n = len(matrix[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
