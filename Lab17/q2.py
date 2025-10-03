#!/usr/bin/python
#Write a program to sum all the values of a dictionary.

def sumofval(**x):
    total = 0
    for value in x.values():
        total = total + value
    print(total)

sumofval(a=1, b=2, c=4)
