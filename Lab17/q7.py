#!/usr/bin/python
""" Write a program with a function to find whether a given triangle with sides a, b, c is
isosceles, scalene or equilateral triangle, also provide a test case output from the program.
"""
def triangle(a, b, c):
    if a == b == c:
        print("Triangle is equilateral")
    elif a == b or a == c or b == c:
        print("Triangle is isosceles")
    else:
        print("Triangle is scalene ")

triangle(1, 2, 3)
triangle(5, 5, 6)
triangle(7, 7, 7)

