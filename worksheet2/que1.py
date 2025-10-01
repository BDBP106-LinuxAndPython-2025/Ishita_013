#!/usr/bin/python3
#Write a script to find the sum of squares of first N numbers

N = int(input("Enter N: "))
sum=sum(i**2 for i in range(1, N+1))
print(sum)

