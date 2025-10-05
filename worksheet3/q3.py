#!/usr/bin/python
""" Define a dictionary containing 10 fruits and their colours. Make sure that the colours
are repeated as values. Write a loop to iterate over the key-value pairs, and check which
all fruits are green in colour (this means that your dictionary should contain at least two
fruits with green as its value (for this example to work well)."""
fruits = {"apple":"red", "banana":"yellow", "kiwi":"green", "grapes":"green", "pear":"green" , "pineapple":"yellow"}
for key,values in fruits.items():
    if values == "green":
        print(key, values)