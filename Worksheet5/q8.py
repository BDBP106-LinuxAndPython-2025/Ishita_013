#!/usr/bin/python3
# (8) Using lru_cache, docstrings, and custom decorators for Fibonacci calculation
from functools import lru_cache
import time
from datetime import datetime

# (i) Fibonacci with and without lru_cache for performance comparison

@lru_cache(maxsize=5)
def fibonacci_lru(n):
    """This function outputs the sum of n Fibonacci numbers"""
    if n <= 1:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

# Standard recursive Fibonacci for comparison
def fibonacci_plain(n):
    """This function outputs the sum of n Fibonacci numbers"""
    if n <= 1:
        return n
    return fibonacci_plain(n-1) + fibonacci_plain(n-2)

# Timing both versions
def time_function(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    print(f"{func.__name__}({n}) Result: {result}")
    print(f"Time taken: {end - start:.6f} seconds")

N = 30  # or higher for more pronounced time difference

print("Without lru_cache:")
time_function(fibonacci_plain, N)

print("\nWith lru_cache (maxsize=5):")
time_function(fibonacci_lru, N)

# (ii) Docstring demonstration
print("\nDocstring of fibonacci_lru:")
print(fibonacci_lru.__doc__)

# (iii) Custom log_time decorator to print datetime on entry and exit

def log_time(func):
    def wrapper(*args, **kwargs):
        entry_time = datetime.now()
        print(f"[ENTRY] {func.__name__} called at {entry_time} with n={args[0]}")
        result = func(*args, **kwargs)
        exit_time = datetime.now()
        print(f"[EXIT] {func.__name__} exited at {exit_time} with n={args[0]}")
        return result
    return wrapper

@log_time
def sample_fibo(n):
    if n <= 1:
        return n
    return sample_fibo(n-1) + sample_fibo(n-2)

print("\nUsing custom decorator log_time:")

sample_fibo(5)
