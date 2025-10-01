#!/usr/bin/python3
#Write a script to find the highest frequency character in a string, S.
S = input("Enter string: ")
freq = {}
for i in S:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
max_char = None
max_freq = 0
for char in freq:
    if freq[char] > max_freq:
        max_char = char
        max_freq = freq[char]
print(max_char)
