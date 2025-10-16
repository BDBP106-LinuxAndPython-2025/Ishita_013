#!/usr/bin/python3
#Write a python script that lists out each line of a file prefixed with its line number.

f = open('example.txt', 'r+')
line_number = 1
for line in f:
    print(f"{line_number}: {line.rstrip()}")
    line_number += 1
f.close()
