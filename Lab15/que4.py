#!/usr/bin/python3
#a python script to take an input angle in degrees and print the values of all the 6 trigonometric functions for this angle.

import math

deg = float(input("Enter angle in degrees: "))

rad = math.radians(deg)
print("sin:", math.sin(rad))
print("cos:", math.cos(rad))
print("tan:", math.tan(rad))
print("cosec:", 1/math.sin(rad))
print("sec:", 1/math.cos(rad))
print("cot:", 1/math.tan(rad))

