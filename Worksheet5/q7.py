#!/usr/bin/python3
# (7) Implement the Fibonacci function with parameter n. Use a decorator to log the time to run this function.
import time

def timer(func):
    """Decorator to log time taken by a function"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def fibonacci(n):
    """Returns the n-th Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(100))  # Output: (very large number) and time taken
