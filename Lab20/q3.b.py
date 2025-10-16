#!/usr/bin/python3
"""  in a new program, read in the matrix of strings in the above file as a 2D array
of list of lists. The number of rows and columns are not known in advance. Make
sure your code can figure out how many rows and columns are there in this input.
Name this list as grid and print this 2D list. Name this program as ”Q3 b.py”. In
this same program, print a list that contains lists of columns of the above matrix.
For example, the first column will be grouped into a list [A,E,I] and so on. Next,
print a list that prints the diagonal elements read in one direction. For example,
some of the elements in this list will be [‘A’],[‘B’,‘E’],[’C’,‘F’,‘I’] and so on."""


f = open("stringmatrix.dat", "r")   # Open the file for reading
lines = f.readlines()
f.close()                           # Close the file after reading

# matrix into a 2D list
grid = [line.strip().split() for line in lines]
print("2D grid:", grid)

# Columns as separate lists
num_cols = len(grid[0])
columns = [[row[j] for row in grid] for j in range(num_cols)]
print("Columns:", columns)

# Major diagonal
diagonal = [grid[i][i] for i in range(min(len(grid), num_cols))]
print("Diagonal:", diagonal)
