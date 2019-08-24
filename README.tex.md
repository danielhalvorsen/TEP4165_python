# TEP4165_python #
### TEP4165 assignments written in Python 3.6.8. ###

* Assignment 1
   * Features an analytical solution for the 1D heatconduction equation.
   
$$\frac{\partial T}{\partial t}=\alpha \frac{\partial T}{\partial x^{2}}$$

                  
* Assignment 2
   * Features an approximate solution to the 1D heat conduction equation using a standard FVM discretization in space and the explicit Euler method in time.

$$\frac{\partial T}{\partial t}=\alpha \frac{\partial T}{\partial x^{2}}$$
$$T_{j}^{n+1}=T_{j}^{n}+\frac{\alpha \Delta t}{\Delta x^{2}}\left[T_{j+1}^{n}-2T_{j}^{n}+T_{j-1}^{n}\right]$$