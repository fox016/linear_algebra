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

def forward_substitution(L,b):
    n = len(b)
    y = np.array([0.]*n)
    for i in range(n):
        y[i] = (b[i] - np.dot(y, L[i])) / L[i,i]
    return y

def back_substitution(U,y):
    n = len(y)
    x = np.array([0.]*n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(x, U[i])) / U[i,i]
    return x

def LU_solver(A,b):
    L,U = lu_decomposition(A)
    y = forward_substitution(L,b)
    x = back_substitution(U,y)
    return x

A = np.array([[3.,1.,-2.],[1.5,2.,-5.],[2.,-4.,1.]])
b = np.array([1.1,3.,-2.])
print(LU_solver(A,b))
