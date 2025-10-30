#!/usr/bin/python3
"""Thinking along the same lines of the above question, how will you swap two columns in
a 2D array? Define a 3x3 matrix with random values, and swap first and second columns
in this array."""
import numpy as np
# Create a 3x3 array with random integers from 1 to 9
matrix = np.random.randint(1, 10, (3, 3))

# Use advanced indexing to swap columns
matrix_swapped = matrix.copy()
matrix_swapped[:, [0, 1]] = matrix_swapped[:, [1, 0]]
#the ros remain the same while the column 0 and 1 are exchanged with each other

print("Original Matrix:\n", matrix)
print("\nMatrix after swapping first and second columns:\n", matrix_swapped)
