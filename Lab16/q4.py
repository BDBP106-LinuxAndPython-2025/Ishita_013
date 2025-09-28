#a script to print individual digits of a number, N.
N = input("Enter a number: ")
for i in N:
    print(i)



#or can be done this way
N = int(input("Enter a number: "))
digits = []

while N > 0:
    digits.append(N % 10)  # get last digit
    N = N // 10            # remove last digit
print(digits)             # prints in reverse order


# The digits will be in reverse order, so print in correct order
for digit in reversed(digits):
    print(digit)
