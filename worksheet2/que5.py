#!/usr/bin/python3
#Write a script to find the first occurrence of a character, c, in a string S.
S = input("Enter string: ")
c = input("Enter character to search: ")
count = -1
for i in range(len(S)):
    if S[i] == c:
        count = i
        break
print(count)               #returns -1 if the character is not found
