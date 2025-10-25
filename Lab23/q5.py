#!/usr/bin/python3
"""Write a Python script that scans through a given piece of text and extracts all unique
email addresses from it."""

import re

text = """Contact: newmail@gmail.im and bob@test.org"""
emails = set(re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text))
print(emails)
