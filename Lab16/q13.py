#a program to extract elements of a list, if it occurs more than k times.

L = input("Enter a set of numbers: ").split()
for i in range(len(L)):
    L[i] = int(L[i])

k = int(input("Enter k: "))
el=[]
for num in set(L):
    if L.count(num) > k:
        el.append(num)

print(el)
