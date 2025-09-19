#!/usr/bin/python3
#this is a program to calculate the principle and simple interest


p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
amt = p + si
print(f'Simple Interest: {si:f} ')
print(f'The total amount is : {amt:f}')
print("SIMPLE INTEREST IS: ", si)
