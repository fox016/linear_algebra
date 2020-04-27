import numpy as np

list1 = [1,2,3]
list2 = [2,-1,0]
print(list1+list2)

matrix1 = np.array([[1,2,3,4],[-5,-6,-7,-8],[1,5,2,3]])
print(matrix1)
print(matrix1+matrix1)
print(matrix1*3)

a = np.array([1,2,3,1])
b = np.array([1,1,1,1])
print(np.dot(a,b))

v = np.array([1,3,-2,4,5])
u = np.array([1,1,-2,1,1])
w = np.array([1,0,1,0,1])
first = (((np.dot(v,u)) / (np.dot(u,u))) * u)
second = (((np.dot(v,w)) / (np.dot(w,w))) * w)
print(first + second)

my_matrix=np.array([[1, 2, 3, 4],[-5, -6, -7, -8],[1, 5, 2, 3]])
print(my_matrix[1,2])
print(my_matrix[2,1:3])
print(my_matrix[:,3])
print(my_matrix[2,:])
