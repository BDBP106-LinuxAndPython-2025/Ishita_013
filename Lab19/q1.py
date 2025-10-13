#!/usr/bin/python3
#Write a program to convert temperature in Celsius to Fahrenheit using map function.

def fahrenheit(celsius):
    return celsius * 9 / 5 + 32
celsius = [65, 76, 35, 43]
f = list(map(fahrenheit, celsius))
print (f)


