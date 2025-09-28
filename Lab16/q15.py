#a program to extract words from a string list, L whose first character is k.

L = input("Enter words or string : ").split()
k = input("Enter character to be counted: ")

word = []
for i in L:
    if i.startswith(k):
        word.append(i)

print(word)
