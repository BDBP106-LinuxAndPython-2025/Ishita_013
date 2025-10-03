#!/usr/bin/python
""" Write a program to interchange the even and odd components of an input list. The list
can contain any type of variables. Output the result for the following example:
[23,32,33,44,’BDBH101’,’hello’,’python’, 15, 1e-10, True,’hit’]
"""
l = [23,32,33,44,"BDBH101","hello","python", 15, 1e-10, True,"hit"]
print("Original list:")
print(l)
newl = []
for i in range (0,len(l)-1,2):
   newl.append(l[i+1])
   newl.append(l[i])
print("New list:")
print(newl)
