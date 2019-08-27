# Daniel Halvorsen
# 11/8/19
# Exercise 1 in TEP4165 using Python 3.6.8
# Important note: if you change spatial scale with 100 you need to change temporal scale
# with 100^2 due to the dimensionality of the PDE. Example: time: 0-25, x: 0-1.
# time:0-25/10000, x:0-0.01.
#Important: aeb = a*10^b, which means 1e-3 = 10⁻3
# todo: implement automatic time scaling based on spatial scale.

import numpy as np
import matplotlib.pyplot as plt
import pickle


def compute_T(T_l, T_r, t, i, alpha, L, x):
    # Expression to calculate one element of the sum in the analytical solution
    T = (2 * (T_l - T_r) / (np.pi * i)) * np.sin(np.pi * i / 2) * np.cos(
        np.pi * i * x / L) * \
        np.exp(-alpha * t * ((np.pi * i / L) ** 2))
    return T


if __name__ == '__main__':
    # Declaration of variables and vector spaces
    start = 0
    end = 1
    points = 100
    x_vector = np.linspace(start, end, points)
    L = x_vector[-1]
 #   time = np.linspace(0, 25, 5 + 1)
    time = np.array([0, 0.08, 5, 10,15,20, 25])
    alpha = 1E-3
    T_l = 200
    T_r = 600
    iterations = 50
    T = np.zeros([len(time), len(x_vector)])
    T[:, :] = ((T_l + T_r) / 2)

    # Computation of analytical Temperature solution
    plt.figure(1)
    for t_idx, t in enumerate(time):
        for i in range(1, iterations + 1):
            T[t_idx, :] = T[t_idx, :] + compute_T(T_l, T_r, t, i, alpha, L, x_vector)
        plt.plot(x_vector / x_vector[-1], T[t_idx, :])
    #Save T variable to use in next assignment
    with open('T_analytical.pkl','wb') as f:
        pickle.dump([T],f)
    # Plot commands
    plt.ylabel('Temperature, T')
    plt.xlabel('Spatial dimension, x/L')
    plt.axis([0, 1, 180, 620])
    plt.show()
