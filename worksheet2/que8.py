#!/usr/bin/python3
#Write a program to find the sum and average of numbers in a list, L.
str = input("Enter numbers separated by space: ")
number = str.split()
L = []
for i in number:
    L.append(float(i))

sum = 0
for num in L:
    sum += num
average = sum/ len(L)
print("Sum:", sum)
print("Average:", average)
