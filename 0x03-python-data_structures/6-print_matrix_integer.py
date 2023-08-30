#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        [[print("{:d}".format(row[i]), end=' ' if i != len(row) - 1 else '\n')
            for i in range(len(row))] for row in matrix]
    else:
        print()
