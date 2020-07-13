import numpy as np
from matplotlib import pyplot as plt

x = [18328,18333,18334,18335,18336,18338,18339,18341,18342,18343,18344,18345,18346,18347,18348,18349,18350,18351,18352,18353,18354,18355,18356,18357,18358,18359,18360,18361,18362,18363,18364,18365,18366,18367,18368,18369,18370,18371,18372,18373,18374,18375,18376,18377,18378,18379,18380,18381,18382,18383,18384,18385,18386,18387,18388,18389,18390,18391,18392,18393,18394,18395,18396,18397,18398,18399,18400,18401,18402,18403,18404,18405,18406,18407,18408,18409,18410,18411,18412,18413,18414,18415,18416,18417,18418,18419,18420,18421,18422,18423,18424,18425,18426,18427,18428,18429,18430,18431,18432,18433,18434,18435,18436,18437,18438,18439,18440,18441,18442,18443,18444,18445,18446,18447,18448,18449,18450,18451,18452]
y = [1,3,1,1,2,3,2,10,3,3,8,3,10,13,5,5,11,13,8,9,4,5,4,9,10,6,11,6,8,10,11,10,7,11,4,13,5,7,8,15,12,18,15,7,14,10,8,6,17,12,11,11,9,7,10,10,11,16,9,9,13,10,8,10,11,9,20,18,12,13,14,12,9,6,20,20,7,14,13,14,22,14,13,18,20,20,14,15,15,25,13,18,14,14,26,18,21,25,26,12,17,20,28,29,32,30,25,30,22,24,32,25,25,22,27,24,22,33,35]
x = list(map(lambda i: i-18328, x))
print(x, y)
pred_limit = 200

def plot_points(x, y):
    plt.plot(x, y, 'o', markersize=1, color='red')
    plt.show()

def plot_line(x, y):
    xArr = []
    for i in x:
        xArr.append([1, i])
    x1 = np.array(xArr)
    xT = np.transpose(x1)
    coef = np.matmul(xT, x1)
    vect = np.matmul(xT, y)
    beta = np.linalg.solve(coef, vect)
    pred = range(1,pred_limit)
    y_line = list(map(lambda i: beta[1] * i + beta[0], pred))
    plt.plot(x, y, 'o', markersize=1, color='red')
    plt.plot(pred, y_line)
    plt.xlim(0, pred[-1])
    plt.ylim(0, y_line[-1])
    plt.show()

def plot_quad(x, y):
    xArr = []
    for i in x:
        xArr.append([i, i*i])
    x2 = np.array(xArr)
    xT = np.transpose(x2)
    coef = np.matmul(xT, x2)
    vect = np.matmul(xT, y)
    beta = np.linalg.solve(coef, vect)
    pred = range(1,pred_limit)
    y_quad = list(map(lambda i: beta[0] * i + beta[1] * i * i, pred))
    plt.plot(x, y, 'o', markersize=1, color='red')
    plt.plot(pred, y_quad)
    plt.xlim(0, pred[-1])
    plt.ylim(0, y_quad[-1])
    plt.show()

def row_func(t, n):
    L = [f(k) for k in [N*t for N in range(1,n+1)] for f in [np.cos, np.sin]]
    L.insert(0, 1)
    return L

def design_matrix(x, n):
    L = []
    for j in range(len(x)):
        L.append(row_func(x[j], n))
    matrix = np.array(L)
    return matrix

def plot_curve(x, y, n):
    x1 = design_matrix(x, n)
    xT = np.transpose(x1)
    coef = np.matmul(xT, x1)
    vect = np.matmul(xT, y)
    beta = np.linalg.solve(coef, vect)
    pred = range(1,pred_limit)
    curve = np.array(list(map(lambda i: np.dot(beta, row_func(i, n)), pred)))
    plt.plot(x,y,'r.')
    plt.plot(pred,curve,'b-')
    plt.show()
    mse = (1.0/629.0) * np.linalg.norm(np.subtract(np.matmul(x1, beta), y))**2
    return mse

plot_points(x,y)
plot_line(x,y)
plot_quad(x,y)
print(plot_curve(x, y, 50))
