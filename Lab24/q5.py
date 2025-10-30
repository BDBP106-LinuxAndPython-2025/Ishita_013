#!/usr/bin/python3
"""You are given two 1D arrays. Write a function to create a new array that contains the
maximum of the respective elements in the two arrays. For example, if a=[1,2] and
b=[0,5] then the new array will be c=[1,5]."""
import numpy as np

a = np.array([1, 2])
b = np.array([0, 5])

# Use np.maximum for element-wise comparison
c = np.maximum(a, b)

print("Array a:", a)
print("Array b:", b)
print("New array with maximum rows and columns", c)
