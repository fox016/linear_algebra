import numpy as np

def first_rpt(M):
    for i in range(len(M)):
        M[i] = M[0];
    return M

print(first_rpt(np.array([[1,2,3],[4,5,6],[7,8,9]])))
