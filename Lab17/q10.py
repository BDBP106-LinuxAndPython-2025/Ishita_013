#!/usr/bin/python
"""Write a function called nextPrime that finds and returns the first prime number larger
than some integer, n. The value of n will be passed to the function as its only parameter.
The main program should read an integer from the user and display the first prime
number larger than the entered value."""

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nextPrime(n):
    next = n + 1
    while True:
        if is_prime(next):
            return next
        next += 1


n = int(input("Enter an integer: "))
print("The first prime number larger than", n, "is", nextPrime(n))


