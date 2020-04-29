import numpy as np

def augment(A, b):
    return np.column_stack((A,b))

A=np.array([[3,2,1,1],[1,-2,1,1],[5,0,1,5]])
b=np.array([-1,3,2])
print(augment(A, b))
