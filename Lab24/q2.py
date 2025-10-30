#!/usr/bin/python3
#(i) Create a 1D array from 0 to 9.
import numpy as np
import math
a = np.arange(10)
print(a)
#Create a boolean array of size 3x3.
bool_arr = np.full((3,3), True, dtype=bool)
print(bool_arr)
"""(3)Using syntax from list comprehension, create an array that satisfies the condition.
For example,
arr = np.arange(10)
arr = arr[ arr%2 == 1 ]"""
a = np.array([x for x in range(10) if x % 2 == 0])
print(a)
#for prime numbers
p = np.array([x for x in range(1,51) if x % 2 == math.sqrt(x)])
print(p)
#(4)Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print
#the two arrays.
rando = np.random.randint(0, 100, 20)
re_arr = rando.reshape(4,5)
print(re_arr)
"""(5)Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has
only 1s. Then stack the two arrays horizontally."""
a = np.arange(10)
b = np.ones(10, dtype=int)
stacked = np.hstack((a, b))
print(stacked)
stacked2 = np.vstack((a, b))
print(stacked2)

"""(6)Define two 1D arrays, where array a has list of first 100 numbers, and b has first
100 prime numbers. Obtain a new array that is the intersection of these two
arrays (Hint: use np.intersect1d())"""
a100 = np.arange(1, 101)
# Find first 100 primes with sqrt loop
prime_list = []
num = 2
while len(prime_list) < 100:
    if all(num % k != 0 for k in range(2, int(num**0.5)+1)):
        prime_list.append(num)
    num += 1
b100 = np.array(prime_list)

intersection = np.intersect1d(a100, b100)
print("First 100 natural numbers:")
print(a100)
print("First 100 prime numbers:")
print(b100)
print("Intersection of a100 and b100:")
print(intersection, "\n")

# (vii) Elements in a100 not in b100 (set difference)
setdiff = np.setdiff1d(a100, b100)
print("Elements in a100 not in b100 (set difference):")
print(setdiff, "\n")

# (viii) Indices of elements common to a100 and b100
common_indices = np.where(np.isin(a100, b100))[0]
print("Indices of common elements in a100 and b100:")
print(common_indices)
print("Common elements using indices:")
print(a100[common_indices], "\n")

# (ix) Elements in a100 greater than 5 and less than 20
filtered = a100[(a100 > 5) & (a100 < 20)]
print("Elements in a100 greater than 5 and less than 20:")
print(filtered, "\n")


difference = np.setdiff1d(a, b)
print(difference)
