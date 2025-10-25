#!/usr/bin/python3
"""Test if a DNA sequence contains an EcoRI restriction site using regular expressions. dna
= ”ATCGCGAATTCAC” pattern = GAATTC"""

import re

dna = "ATCGCGAATTCAC"
pattern = r'GAATTC'
print(re.search(pattern, dna))
