#!/usr/bin/python3
"""We know how to reverse the elements in a 1D array- a[::-1].
How would you reverse the rows in a 2D array?
How would you reverse the columns in a 2D array?"""
import numpy as np
arr1 = np.arange(9).reshape(3,3)
# Reverse the array
rev_arr = arr1[::-1]
# Reverse the rows
reverse_rows = arr1[::-1, :]
"""reverses the rows as the splitting is done as 
arr[row_slice[start:stop:step], column_slice[start:stop:step]
Here therefore the column does not change while the row is reversed.
Similarly we do for column as well"""

# Reverse the columns (left to right)
reverse_columns = arr1[:, ::-1]
#the rows remain the same and the columns are reversed using slicing

print("Original Array:\n", arr1)
print("\nReversed Array:\n", rev_arr)
print("\nReversed Rows:\n", reverse_rows)
print("\nReversed Columns:\n", reverse_columns)
