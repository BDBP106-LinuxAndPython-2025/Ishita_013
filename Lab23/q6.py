#!/usr/bin/pyhton3
"""Write a Python script that reads in a piece of text and prints it out masking out
email addresses. Thus and email address ”helloworld@python.com” should become
”h********d@python.com”."""

import re


text = "helloworld@python.com"
print(re.sub(r'([A-Za-z0-9._%+-])([A-Za-z0-9._%+-]*)(@)', lambda m: m.group(1) + '*' * len(m.group(2)) + m.group(3), text))