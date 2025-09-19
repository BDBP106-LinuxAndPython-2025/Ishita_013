#a program to find the roots of a quadratic equation. Figure out what the inputs should be and also have provision to deal with cases where you end up getting complex roots.
#!/usr/bin/python


import cmath
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = b**2 - 4*a*c
root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)
print("Roots:", root1, root2)
