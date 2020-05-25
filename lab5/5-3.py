import numpy as np

def row_echelon(A, b):
    rows = len(A)
    if rows == 0:
        raise Exception("A cannot be an empty matrix")
    for row in range(rows):
        if A[row,row] == 0:
            raise Exception("0 cannot be on main diagonal of A")
    cols = len(A[0])
    if rows != cols:
        raise Exception("A must me a square matrix")
    if len(b) != rows:
        raise Exception("b must have same cardinality as A")
    A = np.column_stack((A,b))
    for col in range(0, cols):
        for row in range(col+1, rows):
            A[row] = A[row] - (A[row,col]/A[col,col]) * A[col]
    return A

A=np.array([[3.,1.,-2.],[1.,2.,-5.],[2.,-4.,1.]])
b=np.array([1.1,2,-3])
#A=np.array([[1,-1,-1],[1,1,-2],[4,-2,4]])
#b=np.array([3,1,1])
ech = row_echelon(A, b)
print(ech)
print(np.shape(ech))
