#!/usr/bin/python
"""Write a program with a function to calculate the area of a triangle using the formula,
where a, b, c are sides of the triangle, also providing a test case output from the program
Area=ps(s − a)(s − b)(s − c) where 2s = a + b + c."""

import math

def area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print (area)

area(5, 5, 5)
