import numpy as np

y1 = np.array([3.33, 4.43, 4.39, 5.23, 5.67, 6.06, 7.01, 7.16, 8.03, 8.78])
xArr = []
for x in range(5, 51, 5):
  xArr.push([1, x])
x1 = np.array(xArr)
print(x1, y1)

xT = np.transpose(x1)
normal_coef1 = np.matmul(xT, x1)
normal_vect1 = np.matmul(xT, y1)
print(normal_coef1, normal_vect1)

beta1 = np.linalg.solve(normal_coef1, normal_vect1)
print(beta1)

beta2 = np.linalg.lstsq(x1, y1)
print(beta2)
