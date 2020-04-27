import numpy as np
from matplotlib import pyplot as plt

def d(x):
    return x**2+x-5

def solve():
    return np.roots([1,1,-5])

def create():
    x = np.linspace(-1,3,20)
    plt.plot(x,d(x))
    plt.show()

def approximate(low, high, iterations):
    for i in range(iterations):
        x = (low+high)/2
        y = d(x)
        print(x,y)
        if y < 0:
            low = x
        else:
            high = x
    return x

create()
print(solve())
print(approximate(0,2,39))
