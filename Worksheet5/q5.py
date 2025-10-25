#!/usr/bin/python3
# (5) Define a module called prime that contains a function isPrime() that returns whether the passed argument is prime or not.
def isPrime(num):

    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def printPrimes(n):
    count, num = 0, 2
    primes = []
    while count < n:
        if isPrime(num):
            primes.append(num)
            count += 1
        num += 1
    print(primes)

# Example usage:
printPrimes(5)  # Output: [2, 3, 5, 7, 11]
