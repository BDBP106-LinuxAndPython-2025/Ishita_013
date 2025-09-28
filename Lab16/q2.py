#a script that computes power - raise base to the n-th power. Eg. power(2, 5).Here base is 2 and n-th power is 5.
def power(base, n):
    result = 1
    for i in range(n):
        result *=base
    return result

print(power(2, 5))
