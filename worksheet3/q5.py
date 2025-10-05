#!/usr/bin/python
""" Write functions to add and subtract two matrices of m× n. Below these two functions, create two example matrices that have the same dimensions (rows and columns) and
therefore correctly does the addition and subtraction Also come up with an example where the addition and subtraction are not defined, and hence the runtime errors show
up."""

def add_matrices(a, b):
    ans = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        ans.append(row)
    print (ans)


def subtract_matrices(a, b):
    ans = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
        ans.append(row)
        print (ans)


mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]
mat2 = [
    [7, 8, 9],
    [10, 11, 12]
]

add_matrices(mat1, mat2)
subtract_matrices(mat1, mat2)