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

def curve_approx(n):
    global T
    global Y
    x = design_matrix(n)
    xT = np.transpose(x)
    normal_coef = np.matmul(xT, x)
    normal_vector = np.matmul(xT, Y)
    beta = np.linalg.solve(normal_coef, normal_vector)
    curve = np.array(list(map(lambda x: np.dot(beta, row_func(x, n)), T)))
    plt.plot(T,Y,'r.')
    plt.plot(T,curve,'b-')
    plt.show()
    mse = (1.0/629.0) * np.linalg.norm(np.subtract(np.matmul(x, beta), Y))**2
    return mse

#plot1(T, Y)
#print(row_func(2,5))
#matrix = design_matrix(10)
#print(np.shape(matrix))
#matrix = design_matrix(4)
#print(matrix[100,:])
print(curve_approx(2))
print(curve_approx(10))
print(curve_approx(100))
print(curve_approx(1000))
