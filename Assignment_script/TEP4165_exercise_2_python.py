# Daniel Halvorsen
# 24/8/19
# Exercise 2 in TEP4165 using Python 3.6.8
# Remember: when indexing arrays in python, array[-1] access last element while array[
# #:-1] access the list from index # to the second to last element. To access index #
# to last we need array[#:].
# Remember: difference between shallow and deep copy of variables. T_old = T.copy() etc.


import numpy as np
import matplotlib.pyplot as plt
import pickle


if __name__ == '__main__':
    # Declaration of variables and vectors
    NJ = 100
    dx = 1 / NJ
    x_vec = np.linspace(0, 1, NJ)
    alpha = 10E-3
    r = 0.4
    t_end = 0.08
    T_l = 200
    T_r = 600
    dt = r * (dx ** 2) / alpha
    time_step = np.ceil(t_end / dt)
    time_vec = np.linspace(0, t_end, time_step + 1)
    T = np.zeros(len(x_vec))
    T[0:int(NJ / 2)] += np.ones(int(NJ / 2)) * T_l
    T[int(NJ / 2):] += np.ones(int(NJ / 2)) * T_r

    for t in range(int(time_step)):
        # Temporal loop
        T_old = T.copy()
        T[0] = T_old[0] + r * (T_old[1] - T_old[0])
        T[-1] = T_old[-1] + r * (T_old[-2] - T_old[-1])
        T[1:-1] = T_old[1:-1] + r * (T_old[2:] - 2 * T_old[1:-1] + T_old[0:-2])
    # Spatial loop redundant due to vector operations. Be careful of the distinct
    # indexation between Matlab and Python. python[0]=Matlab[1]

    with open('T_analytical.pkl','rb') as f:
        T_analytical = pickle.load(f)

    plt.figure(1)
    plt.plot(x_vec / x_vec[-1], T,'.m',markersize=1)
    plt.axis([0, 1, 180, 620])
    plt.xlabel('Spatial dimension x/L [-]')
    plt.ylabel('Temperature, T [K]')
    plt.show()
