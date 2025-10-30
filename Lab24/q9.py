#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)  #creates an array from 20 to 1000


f1 = np.log(1 / np.cos(x)**2)
f2 = np.log(1 / np.sin(x)**2)

fig, ax = plt.subplots()            #used to create an empty graph
ax.plot(x, f1)
ax.plot(x, f2)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('graph')
plt.show()
