import numpy as np
from matplotlib import pyplot as plt

def create():
    x = np.random.normal(scale=1.5, size=500)
    y = np.random.normal(scale=1, size=500)
    plt.plot(x, y, 'x', markersize=5, alpha=1)
    plt.show()

create()
