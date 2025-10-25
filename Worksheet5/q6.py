#!/usr/bin/python3
# (6) Write an interactive calculator as described. Custom error FormulaError.

class FormulaError(Exception):
    pass

def calculate():
    while True:
        user_input = input("Enter formula (or 'quit' to exit): ")
        if user_input.strip().lower() == 'quit':
            break
        parts = user_input.split()
        if len(parts) != 3:
            raise FormulaError("Input must contain exactly 3 elements")
        str1, operator, str2 = parts
        try:
            num1 = float(str1)
            num2 = float(str2)
        except ValueError:
            raise FormulaError("First and third input must be numbers")
        if operator not in ('+', '-'):
            raise FormulaError("Operator must be + or -")
        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        print("Result:", result)


calculate()
