#!/usr/bin/python3
"""
2D Matrix Rotation Module

This module contains a function to rotate a 2D matrix 90 degrees clockwise
in place.

Example:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_2d_matrix(matrix)
    # matrix becomes:
    # [
    #     [7, 4, 1],
    #     [8, 5, 2],
    #     [9, 6, 3]
    # ]
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate. The matrix must
                                      be square (n x n).

    Raises:
        ValueError: If the input is not a list of lists or if the matrix is
                    not square.
    """
    # Validate the input
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise ValueError("Input must be a 2D list of integers.")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Matrix must be square (n x n).")

    # Rotate the matrix in place
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Perform a 4-way element swap
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
