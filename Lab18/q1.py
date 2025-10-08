#!/usr/bin/python3

a = []
for i in range(1,51):
    a.append(i)
print("The list a is: ", a)
#slicing with positve step
print(a[1:5])                       #start,stop,step:1,5,1
print(a[3:20:2])                    #3,20,2
print(a[::2])                       #1,51,2
print(a[::])                        #1,51,1
print(a[10::2])                     #10,51,2
print(a[1:1:1])                     #1,1,1
print(a[:0:])
print(a[-7::1])                     #43,51,1
#
print(a[-6:])
print(a[-10:-4])                    #40,51,1
#slicing with negative step
print(a[::-1])                      #51,1,1
print(a[::-3])                      #51,1,-3
print(a[:1:-2])                     #51,1,-2
print(a[-1:-1:-1])                  #-1,-1,-1
print(a[:-5:-1])                    #51,1,-1
print(a[:0:-1])                     #51,0,-1
print(a[:-1:-1])
print(a[0:-5:-1])
print(a[-1:5:-1])
print(a[2:2:-1])
print(a[2:1:-1])
print(a[0:-5])
#Create a list of even numbers from a using list slicing technique.
print("A list of even numbers:")
print(a[1::2])
#Create a new list from a by choosing the first 10 numbers, then the even numbers from 35-50.
print("The first 10 numbers of list a" , a[0:10])
b = []
for i in range(0,10):
    b.append(a[i])
print(b)

for i in range(25,40):
    if a[i] % 2 == 0:
        b.append(a[i])
print("The new list b:" , b)