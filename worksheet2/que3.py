#!/usr/bin/python3
#Write a script that computes the number of 1s in a binary representation of a decimal number, N.

N = int(input("Enter number: "))
binary= (bin(N))
print(binary)
one = binary.count('1')
print("Number of ones: ", one)
