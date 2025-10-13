#!/usr/bin/python3

#Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.
a = []
for i in range(1, 51):   # creates [1, 2, ..., 50]
    a.append(i)
#a = [i for i in range(1,50)]
print("List a :", a)
sum = 0
for num in a:
    sum += num
print("The sum of digits from 1-50 in the list a is:", sum)

#in list comprehension form
#here we use the walrus operator -> :=
asum = 0
[asum:=asum+i for i in range(1, 51)]
#last element is the sum of all elements in a new list
print(asum)

#b Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
#first we define a function to check if the number is prime or not
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

b = [i for i in range(1, 51) if is_prime(i)]
print("List b:" , b)
#can also be done as: b = [num for num in range(2,51) if all(num%i!=0 for i in range(2, num)]
#this is the actual list comprehension form and not by creating a function as that is just partially list comprehension





#Using a do loop structure, collect all the common numbers in a and b into a new list c.
c = []
for num in a:
    if num in b:
        c.append(num)       # If present in both, add to c
print("The intersection of list a and b is:", c)
