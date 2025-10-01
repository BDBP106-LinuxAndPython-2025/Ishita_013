#!/usr/bin/python3
#Write a script to convert the decimal number D into binary.
D=int(input("Enter a number: "))
b=bin(D)                                                   # [2: ] Removes '0b' prefix
print(b)

#can also be done like this
#D = int(input("Enter decimal number: "))
#binary_str = ""
#n = D
#while n > 0:
#    binary_str = str(n % 2) + binary_str
#    n //= 2
#print(binary_str)
