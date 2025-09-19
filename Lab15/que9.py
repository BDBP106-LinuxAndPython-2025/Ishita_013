#!/usr/bin/python
#a program to reverse a number and print the reversed number.

num = int(input("Enter a number: "))
temp = 0
while num > 0:
    temp = num % 10
    print("Reverse=" , temp)
    num //=10
