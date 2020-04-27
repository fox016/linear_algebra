import numpy as np

def matrix_sum(M):
    total = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            total += M[i,j]
    return total

print(matrix_sum(np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])))
