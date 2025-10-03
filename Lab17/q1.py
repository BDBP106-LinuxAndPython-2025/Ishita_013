#!/usr/bin/python
#Write a program to iterate over a dictionary and print the key-value pairs.
def iterfnc(**x):
    for key , value in x.items():
        print(key, value)

iterfnc(x=4, y=5)