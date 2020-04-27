import numpy as np
from matplotlib import pyplot as plt

def g(x):
    return x**4 - 2*x**3 - 17*x**2 + 4*x + 30

def g_prime(x):
    return 4*x**3 - 6*x**2 - 34*x + 4

def newtons_method(starting_guess, n):
    x = starting_guess
    for i in range(n):
        #print(x)
        den = g_prime(x)
        if den == 0:
            return x
        x = x - (g(x) / den)
    return x

#print(g(7))
#print(g_prime(-2))

print(newtons_method(10, 10))
print(newtons_method(-10, 10))
print(newtons_method(2, 10))
print(newtons_method(-1, 10))
