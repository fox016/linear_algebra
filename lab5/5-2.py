import numpy as np

def first_column_zeros(A):
    if A[0,0] == 0:
        raise Exception("First value in matrix cannot be 0")
    rows = len(A)
    for row in range(1, rows):
        A[row] = A[row] - (A[row,0]/A[0,0]) * A[0]
    return A

A=np.array([[2,1,3,1],[1,2,-1,2.5],[4,2,-1,1]])
print(first_column_zeros(A))
