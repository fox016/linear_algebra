import numpy as np

def forward_substitution(L,b):
    n = len(b)
    y = np.array([0.]*n)
    for i in range(n):
        y[i] = (b[i] - np.dot(y, L[i])) / L[i,i]
    return y

L = np.array([[1.,0.,0.],[3.,1.,0.],[-1.1,2.,1.]])
b = np.array([-2.1,1.,-1.])
print(forward_substitution(L,b))
