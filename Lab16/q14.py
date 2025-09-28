#a program to remove all occurrences of an element from a list, L.

L = input("Enter a set of numbers").split()
for i in range(len(L)):
    L[i] = int(L[i])

el = int(input("Element to remove: "))

newlist = []
for num in L:
    if num != el:
        newlist.append(num)

print(newlist)
