#!/usr/bin/python3
"""Write a program to find the sum of all the elements in a list using lambda and reduce
functions."""
from functools import reduce
l = [2, 4, 6]
sum = reduce(lambda x, y: x + y, l)
print(sum)  #output should be 12
