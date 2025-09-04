import cmath
import math 

a=5
b=6
c=6

d = (b ** 2) - (4 * a * c)
e = (2 * a)

#using cmath
root1 = (-b + cmath.sqrt(d)) / e
root2 = (-b - cmath.sqrt(d)) / e
print(root1)
print(root2)

#using just math
root1 = (-b + math.sqrt(d)) / e
root2 = (-b - math.sqrt(d)) / e
print(root1)
print(root2)

#result of cmath
#(-0.6+0.916515138991168j)
#(-0.6-0.916515138991168j)

#result of math
#Traceback (most recent call last):
# File "/home/ibab/git_tests/Ishita_013/python_exercises/que4.py", line 18, in <module>
#root1 = (-b + math.sqrt(d)) / e
                

