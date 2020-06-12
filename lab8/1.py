import numpy as np

def transform(x):
    A = np.array([[2,1],[1,-3],[0,1]])
    return np.matmul(A, x)

print(transform(np.array([1,2])))
