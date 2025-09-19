#!/usr/bin/python
# a program to print the sum of the digits in a number.
n = int(input("Number: "))
total = 0
while n > 0:
    total = total + n % 10
    n //= 10
print("Sum:", total)
