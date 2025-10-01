#!/usr/bin/python3
#Write a program to find the minimum and maximum number in a list, L.

str = input("Enter numbers separated by space: ")
numbers = str.split()
L = []
for i in numbers:
    L.append(float(i))

minimum = L[0]
maximum = L[0]
for num in L:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num
print("Minimum:", minimum)
print("Maximum:", maximum)
