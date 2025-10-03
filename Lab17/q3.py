#!/usr/bin/python
#Write a program to find the maximum and minimum values of a dictionary.

def maxmin(**x):
        values = x.values()
        maxval = max(values)       #max and min are iterable and not the integer values of the dictionary
        minval = min(values)
        print("Maximum is:", maxval, "Minimum is:", minval)

maxmin(a=1, b=2, c=4)