import numpy as np
from matplotlib import pyplot as plt

y2 = np.array([20.57, 87.48, 197.45, 347.67, 546.12, 784.35, 1066.02, 1390.97, 1761.85, 2177.34])
x2Arr = []
for x in range(5, 51, 5):
    x2Arr.append([x, x*x])
x2 = np.array(x2Arr)
print(x2)
print(y2)

xT = np.transpose(x2)
normal_coef2 = np.matmul(xT, x2)
normal_vect2 = np.matmul(xT, y2)

beta2 = np.linalg.solve(normal_coef2, normal_vect2)
print(beta2)

def ls2_par(x):
    global beta2
    return beta2[0] * x + beta2[1] * x * x

def draw_ls2():
    x = range(5, 51, 5)
    y1 = [20.57, 87.48, 197.45, 347.67, 546.12, 784.35, 1066.02, 1390.97, 1761.85, 2177.34]
    y2 = list(map(ls2_par, x))
    plt.plot(x, y1, 'o', markersize=2, alpha=1)
    plt.plot(x, y2)
    plt.show()

draw_ls2()

pred2 = ls2_par(60)
print(pred2)
