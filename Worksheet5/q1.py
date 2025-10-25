#!/usr/bin/python3
# (1) Explain the various ways of importing module contents with examples.

# 1. Import the whole module
import math
print(math.sqrt(16))  # Output: 4.0

# 2. Import a specific function or variable
from math import sqrt
print(sqrt(25))  # Output: 5.0

# 3. Import with an alias
import math as m
print(m.factorial(5))  # Output: 120

# 4. Import all contents (not recommended for large modules)
from math import *
print(sin(0))  # Output: 0.0
