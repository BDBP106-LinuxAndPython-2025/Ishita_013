#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
# Define the function for general sigma
def gauss(x, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-x**2 / (2 * sigma**2))

sigmas = [1, 1.5, 2]
x = np.linspace(-10, 10, 1000)
plt.figure()

for sigma in sigmas:
    plt.plot(x, gauss(x, sigma), label=f'sigma = {sigma}')

plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Normalized Gaussian function for different sigma')
plt.legend()
plt.grid(True)
plt.show()
