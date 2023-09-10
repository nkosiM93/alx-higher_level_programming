#!/usr/bin/python3
"""
    Module contains a function that divides a matrix
"""


def matrix_divided(matrix, div):
    """ Function divides all elements of a matrix by div"""

    newList = []
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    for r in range(len(matrix)):
        if r + 1 >= len(matrix):
            break
        if len(matrix[r]) != len(matrix[r + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    rows = len(matrix)

    for i in range(rows):
        inner = []
        for j in range(len(matrix[i])):
            inner.append(round(matrix[i][j] / div, 2))
        newList.append(inner)
    return newList
