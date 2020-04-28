import numpy as np
from matplotlib import pyplot as plt

def jacobi1_iteration(x, y):
    new_x = (6+y)/7
    new_y = (x+4)/5
    return [new_x, new_y]

def jacobi1_method(n):
    x, y = 0, 0
    for i in range(n):
        x, y = jacobi1_iteration(x, y)
    return [x, y]

def gs1_iteration(x,y):
    new_x = (6+y)/7
    new_y = (new_x+4)/5
    return [new_x, new_y]

def gs1_method(n):
    x, y = 0, 0
    for i in range(n):
        x, y = gs1_iteration(x, y)
    return [x, y]

def gs1_error(n):
    solution = np.array([1, 1])
    approx = np.array(gs1_method(n))
    return np.linalg.norm(solution - approx)

def create_plot1(x_vals):
    y_vals = list(map(gs1_error, x_vals))
    print(y_vals)
    plt.plot(x_vals, y_vals)
    plt.show()

def gs2_iteration(x,y):
    new_x = y+1
    new_y = (-2*new_x)+5
    return [new_x, new_y]

def gs2_method(n):
    x, y = 0, 0
    for i in range(n):
        x, y = gs2_iteration(x, y)
    return [x, y]

def gs2_error(n):
    solution = np.array([2, 1])
    approx = np.array(gs2_method(n))
    return np.linalg.norm(solution - approx)

def create_plot2(x_vals):
    y_vals = list(map(gs2_error, x_vals))
    print(y_vals)
    plt.plot(x_vals, y_vals)
    plt.show()

def gs3_iteration(x,y,z):
    new_x = (-8 + 2*y - 3*z)/5
    new_y = (102 - new_x + 4*z)/4
    new_z = (-90 + 2*new_x + 2*new_y)/4
    return [new_x, new_y, new_z]

def gs3_method(n):
    x, y, z = 0, 0, 0
    for i in range(n):
        x, y, z = gs3_iteration(x, y, z)
    return [x, y, z]

print(jacobi1_iteration(3,5))
print(jacobi1_method(3))
for i in range(1, 10):
    print(i, jacobi1_method(i))
n_var1 = 2
n_var2 = 6
print(gs1_iteration(3,5))
print(gs1_method(2))
for i in range(1, 10):
    print(i, gs1_method(i))
n_var3 = 2
n_var4 = 4
print(gs1_error(3))
#create_plot1(list(range(50)))
print(gs2_method(5))
print(gs2_error(3))
#create_plot2(list(range(50)))
"""
[7 -1  [x = [6,
 1 -5]  y]   -4]

[1 -1  [x = [1,
 2 1]   y]   5]
 """
print(gs3_method(4))
for i in range(1, 20):
    print(i, gs3_method(i))
