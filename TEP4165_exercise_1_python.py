# Daniel Halvorsen
# 11/8/19
# Exercise 1 in TEP4165 using Python 3.6.8

import numpy as np

L = 1
time = np.linspace(0, 25, 5)
start = 0
end = 0.01
points = 100
x = np.linspace(start, end, points)
alpha = 1
T_l = 200
T_r = 600
iterations = 50
T = np.zeros([len(t),len(x)])
T[:,:] = ((T_l + T_r) / 2)
for t_idx, t in enumerate(time):
    for i in range(iterations):
        T[:] = T + ((2 * (T_l + T_r)) / (np.pi * i)) * np.sin(i * np.pi / 2) * np.cos(
            np.pi * i * x / L) * np.exp((-alpha * (np.pi * i / L) ** 2) * t)

