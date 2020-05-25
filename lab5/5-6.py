import numpy as np

def back_substitution(U,y):
    n = len(y)
    x = np.array([0.]*n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(x, U[i])) / U[i,i]
    return x

U = np.array([[2.,-3.1,1.],[0.,1.,3.],[0.,0.,4.]])
y = np.array([1.,-2.1,3.])
print(back_substitution(U,y))
