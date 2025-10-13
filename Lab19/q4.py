#!/usr/bin/python3
"""Write a program to filter out the odd elements of the
Fibonacci series for the first n terms."""
"""what are fibonacci numbers -a sequence of numbers where each number 
is the sum of the two preceding ones, starting with 0 and 1. The sequence
begins as 0, 1, 1, 2, 3, 5, 8, 13, and continues infinitely"""

#long form
def fibonacci(n):
    fib = [0,1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

n = int(input("Enter a value:"))
result = fibonacci(n)
odd = list(filter(lambda x: x % 2 == 1, result))
print(odd)

#lsit comprehension form
n = 5
even_fib = (all(lambda n: (lambda a=0, b=1: [a for _ in range(n) if (a := (a + b - (b := a))) % 2 == 0]))(n))
print(list(even_fib))
