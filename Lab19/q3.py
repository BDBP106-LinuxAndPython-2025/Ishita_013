#!/usr/bin/python3
#Write a program to convert a tuple of angles into a list of tuples with each tuple containing
# the sine and cosine of an angle

import math
angles = (5,6,7,8,9)
result = list(map(lambda x: (math.sin(x), math.cos(x)), angles))
print(result)
