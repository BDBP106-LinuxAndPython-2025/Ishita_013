# (4) Define a module called factorial that contains a function to find the factorial of a given integer. Using this function, find the permutation and combination of the given inputs.

# factorial_module.py
def factorial(n):
    #Returns factorial of n
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def permutation(n, r):

    return factorial(n) // factorial(n - r)

def combination(n, r):

    return factorial(n) // (factorial(r) * factorial(n - r))

# Example usage:
if __name__ == "__main__":
    n, r = 5, 2
    print("Permutation:", permutation(n, r))  # Output: 20
    print("Combination:", combination(n, r))  # Output: 10
