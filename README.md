# TEP4165_python #
### TEP4165 assignments written in Python 3.6.8. ###

* Assignment 1
   * Features an analytical solution for the 1D heatconduction equation.
   
<p align="center"><img src="/tex/a3f4ce18d220d3d653d024810301792e.svg?invert_in_darkmode&sanitize=true" align=middle width=84.37884345pt height=33.81208709999999pt/></p>

                  
* Assignment 2
   * Features an approximate solution to the 1d heat conduction equation using a standard FVM discretization in space and the explicit Euler method in time.

<p align="center"><img src="/tex/a3f4ce18d220d3d653d024810301792e.svg?invert_in_darkmode&sanitize=true" align=middle width=84.37884345pt height=33.81208709999999pt/></p>
$$T_{j}^{n+1}=T_{j}^{n}+\frac{\alpha \Delta t}{\Delta x^{2}}\[T_{j+1}^{n}-2T_{j}^{n}+T_{j-1}^{n}\]
