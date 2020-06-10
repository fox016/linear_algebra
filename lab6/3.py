import numpy as np
from matplotlib import pyplot as plt

y1 = np.array([3.33, 4.43, 4.39, 5.23, 5.67, 6.06, 7.01, 7.16, 8.03, 8.78])
xArr = []
for x in range(5, 51, 5):
  xArr.append([1, x])
x1 = np.array(xArr)
print(x1)
print(y1)

xT = np.transpose(x1)
normal_coef1 = np.matmul(xT, x1)
normal_vect1 = np.matmul(xT, y1)

beta1 = np.linalg.solve(normal_coef1, normal_vect1)
print(beta1)
#beta2 = np.linalg.lstsq(x1, y1, rcond=None)

def ls1_line(x):
    global beta1
    return beta1[1] * x + beta1[0]

def draw_ls1():
    x = range(5, 51, 5)
    y1 = [3.33, 4.43, 4.39, 5.23, 5.67, 6.06, 7.01, 7.16, 8.03, 8.78]
    y2 = list(map(ls1_line, x))
    plt.plot(x, y1, 'o', markersize=2, alpha=1)
    plt.plot(x, y2)
    plt.xlim(0, 55)
    plt.ylim(0, 10)
    plt.show()

draw_ls1()

pred1 = ls1_line(60)
print(pred1)
