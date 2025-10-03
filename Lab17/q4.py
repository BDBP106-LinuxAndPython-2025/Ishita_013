#!/usr/bin/pyhton
#Given a dictionary with a values list, extract the key whose value has the most unique values.

test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
un = -1
newkey = None
for key, value in test_dict.items():
    count = len(set(value))
    if count > un:
        un = count
        newkey = key

print("The most unique elements are in:", newkey)
