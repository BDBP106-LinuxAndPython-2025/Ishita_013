#!/usr/bin/python3
"""Write a Python script that accepts a line of CSV and checks if the 3rd field contains
exactly an email address or not, given that there are more than 3 fields."""

import re
a=r"^[a-z0-9\.\-\%\_]+@[a-z0-9\.\_]+\.[a-z]{2,}$"
L="2,ishitab,ishitabad123@gmail.ac.in,pune,21yrs"
gmail=False
words=L.split(',')
print(words)
for i in range(len(words)):
    if i==2:
        gmail=bool(re.match(a,words[i]))
        print(gmail)
        if gmail==True:
            print("Third field has gmail id")
        else:
            print("Third field doesnt have mail id")