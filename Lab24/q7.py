#!/usr/bin/python3
"""Explore the set_printoptions() function to pretty-print a numpy array by suppressing
the scientific notation (like 1e10)."""
import numpy as np
# Create array with very small floating-point values
arr = np.random.random((3, 3)) * 1e-5

# Use set_printoptions to suppress scientific notation
np.set_printoptions(suppress=True, precision=8)

print("Pretty printed array :\n", arr)
