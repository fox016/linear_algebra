import numpy as np

def integration(m):
    e = 1 - (1/np.exp(1))
    for j in range(1, m+1):
        e = 1 - j*e
    return e

print(integration(0))
print(integration(1))
print(integration(15))
print(integration(16))
print(integration(17))
print(integration(18))
