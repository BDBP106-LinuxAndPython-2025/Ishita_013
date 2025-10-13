#!/usr/bin/python3
"""Write a function population_growth(initial,rate, time) that definss an inner func-tion exponential_growth()
using the formula N(t) = N0 + exp(rate ∗ time) where N0represents the initial population and N(t) is population after time t
The inner function returns the population after time, and the outer function rounds and prints it."""

import math
def population_growth(initial, rate, time):
    def exponential_growth():
        return initial * math.exp(-rate * time)
    print(exponential_growth())
population_growth(300, 0.05, 10)

