import numpy as np
from matplotlib import pyplot as plt

"""
x = np.linspace(-5,5,50)
y = x**2
z = np.log(x**2)
plt.plot(x,y)
plt.plot(x,z)
plt.show()
"""

def create():
    x = np.linspace(-2*np.pi, 2*np.pi, 200)
    y = np.sin(x)
    z = np.cos(4*x)
    plt.plot(x,y)
    plt.plot(x,z)
    plt.show()

create()
