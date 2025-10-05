#!/usr/bin/python
""" One can use sets or lists or tuples as values in a dictionary. For example, let’s define the
following dictionary studentmarks={"Rahul":{49,58, 35,64}, "Sandeep":{80,92,94,83},"Sita":{44,65,76,54}}
Write a script to check and print the name of the student if the student has scored above60 in all subjects."""

studentmarks={
"Rahul":{49,58, 35,64}, "Sandeep":{80,92,94,83},"Sita":{44,65,76,54}}

for key , value in studentmarks.items():
    temp = True
    for i in value:
        if i <= 60:
            temp = False

    if temp == True:
        print(key, value)

