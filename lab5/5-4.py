import numpy as np

def identity(size):
    arr = []
    for i in range(size):
        arr.append([0.0]*size)
    for i in range(size):
        arr[i][i]=1.0
    return np.array(arr)

def lu_decomposition(A):
    m,n = np.shape(A)
    U = A
    L = identity(m)
    for col in range(n):
        for row in range(col+1, m):
            L[row,col] = U[row,col] / U[col,col]
            U[row] = U[row] - L[row,col] * U[col]
    return L, U

A = np.array([[3,1,-2],[1.5,2,-5],[2,-4,1]])
print(lu_decomposition(A))
