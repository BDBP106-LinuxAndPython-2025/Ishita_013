#a program to print the duplicate elements in a list, L.
L = input("Enter a set of numbers: ").split()
for i in range(len(L)):
    L[i] = int(L[i])

d = []
for num in L:
    if L.count(num) > 1 and num not in d:
        d.append(num)

print(d)
