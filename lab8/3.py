import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def showplot(H):
    # This function displays the image produce by the collection of coordinates given in H
    cougarplot=plt.plot(H[0,:],H[1,:],'k.',markersize=3.5)
    plt.axis([-1.5,1.5,-1.5,1.5])
    plt.gca().set_aspect("equal")
    plt.show()
    return None

def stretch(image, a, b):
    A = np.array([[a,0],[0,b]])
    return np.matmul(A, image)

def shear(image, a, b):
    A = np.array([[1,a],[b,1]])
    return np.matmul(A, image)

def reflect(image, a, b):
    A = np.multiply(1./(a**2+b**2), [[a**2-b**2, 2*a*b], [2*a*b, b**2-a**2]])
    return np.matmul(A, image)

def rotate(image, theta):
    A = np.array([[np.cos(theta),-1*np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    return np.matmul(A, image)

df = pd.read_csv('./cougar.csv')
cougar = df.values
cougar

#showplot(cougar)
#showplot(stretch(cougar, 0.5, 1.2))
#showplot(shear(cougar, 0.5, -0.5))
#showplot(reflect(cougar, 0.5, 1))
#showplot(rotate(cougar, 3*np.pi/2.))

iden=np.array([[1,0],[0,1]]) # The identity matrix may be helpful here.
comp_matrix = stretch(reflect(rotate(stretch(iden, 1, 2), -np.pi/4.), 2, -3), 0.5, 1)
showplot(np.matmul(comp_matrix, cougar))
