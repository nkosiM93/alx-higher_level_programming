#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

'''matrix = [
    [1, 2, 3],
    [4, 5, 6]
]'''

rows = 3
cols = 4

matrix = [[None for _ in range(cols)] for _ in range(rows)]

print(matrix_divided(matrix, 3))
print(matrix)
