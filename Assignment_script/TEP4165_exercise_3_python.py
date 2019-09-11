# Daniel Halvorsen
# 26/8/19
# Exercise 3 in TEP4165 using Python 3.6.8


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc



def upwind(u, Tb, NJ, T_0, C, t_end):
    # Explicit upwind FVM algorithm
    # Initializing constants and variables
    dx = 1 / NJ
    dt = C * dx / u
    timesteps = int(np.ceil(t_end / dt))
    T = T_0.copy()
    T_new = T.copy()

    for n in range(timesteps):
    # Temporal loop
        #Spatial loop using array operations
        T_new[1:NJ-1] = (1 + C) * T[1:NJ-1] - C * T[2:NJ]
        T_new[-1] = Tb

        # Update old variable with new data
        T = T_new.copy()
    return T


rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
## for Palatino and other serif fonts use:
# rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

if __name__ == '__main__':
    # Declaration of variables and constants
    Tb = 200
    NJ = 100
    C = -0.5
    u = -0.25
    t_end_list = [0.04,0.5,1.2]
    L = 1
    x = np.linspace(0, L, NJ)/L

    # Initial vector
    T_left = 800
    T_right = 200
    T_0_left = np.ones(int(NJ / 2)) * T_left
    T_0_right = np.ones(int(NJ / 2)) * T_right
    T_0 = np.concatenate((T_0_left,T_0_right),axis=None)

    fig1 = plt.figure()
    ax = fig1.add_subplot(111)

    for t_end in t_end_list:
    # Loop over different time levels
        T = upwind(u, Tb, NJ, T_0, C, t_end)
        ax.plot(x,T,marker='d',markersize=3,linestyle='-',linewidth=0.3,label='Upwind, t= '+np.str(t_end))
        ax.legend(loc=0)
    plt.xlabel('$x/L (-)$')
    plt.ylabel('Temperature, $T (K)$')
    plt.savefig('expl_upwind_C-05.png')
    plt.show()