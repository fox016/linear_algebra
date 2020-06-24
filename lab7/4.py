import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./Lab7data.csv')
signal_data = df.values
T = signal_data[:,0]
Y = signal_data[:,1]

def plot1(x, y):
    plt.plot(x, y, 'o', markersize=1, color='red')
    plt.show()

def row_func(t, n):
    L = [f(k) for k in [N*t for N in range(1,n+1)] for f in [np.cos, np.sin]]
    L.insert(0, 1)
    return L

def design_matrix(n):
    global T
    L = []
    for j in range(len(T)):
        L.append(row_func(T[j], n))
    matrix = np.array(L)
    return matrix

#plot1(T, Y)
#print(row_func(2,5))
#matrix = design_matrix(10)
#print(np.shape(matrix))
#matrix = design_matrix(4)
#print(matrix[100,:])
