#!/usr/bin/python3
"""Write a program to extract all vowels
in a given string using list comprehension."""

str = "pythonandlinux"
vowels = [ch for ch in str if ch in 'aeiou']
print(vowels)
