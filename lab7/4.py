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

plot1(T, Y)
