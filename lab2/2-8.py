import numpy as np

long_list = [0.5**i for i in range(1, 101)]
print(len(long_list))
print(long_list)

very_long_list = [a**b for b in range(1,100) for a in range(1,4)]
print(very_long_list)
