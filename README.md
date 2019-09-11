# TEP4165_python #
### TEP4165 assignments from 2018/2019 written in Python 3.6.8. ###

* Assignment 1
   * Features an analytical solution for the 1D heat conduction equation.
   * Both boundaries are kept insulated.
   
<p align="center"><img src="/tex/a3f4ce18d220d3d653d024810301792e.svg?invert_in_darkmode&sanitize=true" align=middle width=84.37884345pt height=33.81208709999999pt/></p>
<p align="center"><img src="/tex/389df9f52d48c9152c208e369bcc7ead.svg?invert_in_darkmode&sanitize=true" align=middle width=253.90813965pt height=33.81208709999999pt/></p>

                  
* Assignment 2
   * Features an approximate solution to the 1D heat conduction equation using a standard FVM discretization in space and the explicit Euler method in time.
   * The boundary is insulated for both x=0 and x=L

<p align="center"><img src="/tex/a3f4ce18d220d3d653d024810301792e.svg?invert_in_darkmode&sanitize=true" align=middle width=84.37884345pt height=33.81208709999999pt/></p>
<p align="center"><img src="/tex/3125cc3ae12e9b013c4792763c41caf2.svg?invert_in_darkmode&sanitize=true" align=middle width=235.1180502pt height=34.7253258pt/></p>
<p align="center"><img src="/tex/8f30b89e9ae3bfbe35ad5797de695672.svg?invert_in_darkmode&sanitize=true" align=middle width=286.95335295pt height=33.62942055pt/></p>


<p align="center">
  <img width="460" height="300" src="https://github.com/danielhalvorsen/TEP4165_python/blob/master/Figures/FVM_EXACT_HEATCONDUCTION.png">
</p>

* Assignment 3
    * Features an explicit upwind finite volume method for the 1D linear advection equation. 
    * For this specific case the advection velocity is u=-0.25 and the Courant number is C=-0.5.
    * We let the right boundary condition coincide with the initial condition.
<p align="center"><img src="/tex/a82824f040a8cdddbc8a5eb01a0f5ef3.svg?invert_in_darkmode&sanitize=true" align=middle width=108.61548059999998pt height=33.81208709999999pt/></p>
<p align="center"><img src="/tex/7fe17e02e9fd0a01e704486c0882084d.svg?invert_in_darkmode&sanitize=true" align=middle width=225.23061824999996pt height=56.06774085pt/></p>
<p align="center"><img src="/tex/ce12996e3583a73354c592172e71ea69.svg?invert_in_darkmode&sanitize=true" align=middle width=131.77839674999998pt height=15.068469899999998pt/></p>

<p align="center">
  <img width="460" height="300" src="https://github.com/danielhalvorsen/TEP4165_python/blob/master/Figures/expl_upwind_C-05.png">
</p>