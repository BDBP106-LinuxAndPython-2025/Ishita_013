#!/usr/bin/python3
import numpy as np
"""Explore the set_printoptions() function to print a 3x3 matrix containing random
numbers up to 3 decimal places."""
# Create random 3x3 matrix
mat = np.random.random((3, 3))
rounded_matrix = np.round(mat, 3)

print("Original Matrix:\n", mat)
print("New matrix with rounded values is: \n", rounded_matrix)

