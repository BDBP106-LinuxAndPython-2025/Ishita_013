#!/usr/bin/python3
"""Write a Python script to check if a given string
 contains an email address or not."""

import re
a=r"^[a-z0-9\.\_\%\-]+@[a-z0-9\.\_]+\.[a-z]{2,}$"
b=["1","ishitabadola@gmail.com","eivne@","ishi@new.com"]
for i in b:
    print(f"The mail id is {i} : {bool(re.match(a,i))}")