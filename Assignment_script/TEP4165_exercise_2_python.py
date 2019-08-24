# Daniel Halvorsen
# 24/8/19
# Exercise 2 in TEP4165 using Python 3.6.8

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Declaration of variables and vectors
    NJ = 100
    dx = 1 / NJ
    x_vec = np.linspace(0, 1, NJ + 1)
    timesteps = 1000
    start = 0
    end = 1
    alpha = 10E-3
    r = 0.4
    time_vec = np.linspace(start, end, timesteps + 1)
    T = x_vec[:].copy()

    for t_idx, t in enumerate(time_vec):
    # Temporal loop
        for x_idx, x in enumerate(x_vec[1:-1]):
        # Spatial loop with inner points
