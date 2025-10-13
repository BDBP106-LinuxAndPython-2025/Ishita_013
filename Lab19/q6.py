#!/usr/bin/python3
"""Write a function called cell_metabolism that takes the number of glucose and oxy-
gen molcules, that contains an inner function energy_output() to calculate ATP yield
(assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP
produced."""

def cell_metabolism(glucose, oxygen):
    def energy_output():
        return (glucose+oxygen//6)* 38
    return energy_output()
print(cell_metabolism(2, 18))



# the output must be 76
