import numpy as np
from matplotlib import pyplot as plt

r = [0.389, 0.724, 1.0, 1.524, 5.2, 9.510]
T = [87.77, 224.70, 365.25, 686.95, 4332.62, 10759.2]

y3 = np.array(list(map(np.log, r)))
x3Arr = []
for x in T:
    x3Arr.append([1, np.log(x)])
x3 = np.array(x3Arr)
print(x3)
print(y3)

xT = np.transpose(x3)
normal_coef3 = np.matmul(xT, x3)
normal_vect3 = np.matmul(xT, y3)

beta3 = np.linalg.solve(normal_coef3, normal_vect3)
print(beta3)

def per_to_rad(x):
    global beta3
    ln_r = beta3[1] * np.log(x) + beta3[0]
    return np.exp(ln_r)

for x in T:
    print(x, per_to_rad(x))

pred_Uran = per_to_rad(30687.15)
pred_Nept = per_to_rad(60190.03)
print(pred_Uran)
print(pred_Nept)
