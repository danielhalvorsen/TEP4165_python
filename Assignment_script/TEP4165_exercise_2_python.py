# Daniel Halvorsen
# 24/8/19
# Exercise 2 in TEP4165 using Python 3.6.8
# Remember: when indexing arrays in python, array[-1] access last element while array[
# #:-1] access the list from index # to the second to last element. To access index #
# to last we need array[#:].
# Remember: difference between shallow and deep copy of variables. T_old = T.copy() etc.
# Spatial loop redundant due to vector operations. Be careful of the distinct
        # indexation between Matlab and Python. python[0]=Matlab[1]
#todo map #points in assignment 2 with #points in assignment 1 such that one can plot a
# [30] vector with i.e. a [100] vector.

import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import rc
import itertools

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
## for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

if __name__ == '__main__':
    # Declaration of variables and vectors
    # Import analytical temperature from last assignment
    with open('T_analytical.pkl', 'rb') as f:
        # T = [T(t,x)] indexation with T[0][#,#] for first row.
        T_analytical = pickle.load(f)
    # Spatial
    NJ = 100
    dx = 1 / NJ
    x_vec = np.linspace(0, 1, NJ)

    # Constants
    alpha = 1E-3
    r = 0.4
    T_l = 200
    T_r = 600

    # Temporal
    time_vec = np.array([0, 0.08, 5, 10, 15, 20, 25])
    dt = r * (dx ** 2) / alpha
    time_step = np.ceil(time_vec / dt)

    fig1 = plt.figure()
    ax   = fig1.add_subplot(111)
    ax2  = ax.twinx()
    # marker = itertools.cycle(('.', 'v', 's', '*', 'p', 'D', 'o'))
    # can use marker=next(marker) in plt.plot() command
    for t_idx, t in enumerate(time_vec):
        T = np.zeros(len(x_vec))
        T[0:int(NJ / 2)] += np.ones(int(NJ / 2)) * T_l
        T[int(NJ / 2):] += np.ones(int(NJ / 2)) * T_r
        for n in range(int(time_step[t_idx])):
            # Temporal loop
            T_old = T.copy()
            T[0] = T_old[0] + r * (T_old[1] - T_old[0])
            T[-1] = T_old[-1] + r * (T_old[-2] - T_old[-1])
            T[1:-1] = T_old[1:-1] + r * (T_old[2:] - 2 * T_old[1:-1] + T_old[0:-2])
        ax.plot(x_vec / x_vec[-1], T, marker='x', markersize=3, linestyle='',
                 label='FVM t=  ' + np.str(t))
        ax.legend(loc=0)
        ax2.plot(x_vec / x_vec[-1], T_analytical[0][t_idx, :], linestyle='-',
                 linewidth=1, label='Exact t= ' + np.str(t))
        ax2.legend(loc=4)
    ax.axis([0, 1, 180, 620])
    ax2.axis([0, 1, 180, 620])
    ax.set_xlabel('Spatial dimension, $x/L [-]$')
    ax.set_ylabel('Temperature, $T [K]$')
    plt.show()
