#!/usr/bin/python3
"""Write a regular expression that matches integers from 0 to 255. (Note that this is different
from the question above. Implement this in a script and test for various possibilities.
"""

import re
a="^(25[0-5]|1?\d?\d|2[0-4]\d|\d\d)$"
b=["0","93","2758","96","267","256","1","190"]
for i in b:
    print(f"The number given is {i}: {bool(re.match(a,i))}")