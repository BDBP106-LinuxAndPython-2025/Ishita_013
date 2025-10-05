#!/usr/bin/python
""" One can create a set from several different objects – lists, tuples and dictionaries. Come
up with an example for each object type, and create a set out of that object using the
set() function. In the case of a dictionary, what does the set contain?."""
l = [1,2,2,3,4,2,34,5,4]
print("Orignal list: " , l)
li_set = set(l)
print(li_set)
t = ('apple', 'apple','banana','banana', 'orange')
print("Original tupple: ", t)
tuple_set = set(t)
print(tuple_set)
d = {"name":"John", "age":25, "city":"New York", "name":"Doe"}
#even a dictionary does not print two same keys. only the last one is printed
print("Original dictionary: ", d)
dict_set = set(d)
print(dict_set)
#when coverting a dictionary to a  set it is important to note that only the keys are taken into
#consideration and not the values!