#!/usr/bin/python3
"""Write a program to concatenate a list of strings to make a
 sentence using reduce function."""

from functools import reduce

l = ["today","is","a","nice","day"]
sentence = reduce(lambda x, y: x + " " + y, l)
print(sentence)
