#Write a program to find the even numbers in a list, L.

L = input("Enter a set of numbers: ").split()
for i in range(len(L)):
    L[i] = int(L[i])

even = []
for num in L:
    if num % 2 == 0:
        even.append(num)

print(even)
