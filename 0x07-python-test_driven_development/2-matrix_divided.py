#!/usr/bin/python3
"""
    Module houses a function that divides all elements of a
    matrix
    """


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div"""

    result = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    for e, row in enumerate(matrix):
        if e > 0 and not len(matrix[e]) == len(matrix[e-1]):
            raise TypeError("Each row of the matrix must"
                            " have the same size")
        for j in range(len(row)):
            if not isinstance(row[j], (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    result = [[round((row[i] / div), 2) for i in range(len(row))]
              for row in matrix]
    return result
