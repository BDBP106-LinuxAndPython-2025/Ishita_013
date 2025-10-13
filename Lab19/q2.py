#!/usr/bin/python
#Write the above program using lambda expression.
celsius = [65, 76, 35, 43]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
