# TEP4165_python #
### TEP4165 assignments from 2018/2019 written in Python 3.6.8. ###

* Assignment 1
   * Features an analytical solution for the 1D heat conduction equation.
   * Both boundaries are kept insulated.
   
$$\frac{\partial T}{\partial t}=\alpha \frac{\partial T}{\partial x^{2}}$$
$$\frac{\partial}{\partial x}T(x=0,t)=\frac{\partial}{\partial x}T(x=L,t)=0$$

                  
* Assignment 2
   * Features an approximate solution to the 1D heat conduction equation using a standard FVM discretization in space and the explicit Euler method in time.
   * The boundary is insulated for both x=0 and x=L

$$\frac{\partial T}{\partial t}=\alpha \frac{\partial T}{\partial x^{2}}$$
$$\frac{\partial T(x=0,t)}{\partial x}=\frac{\partial T(x=L,t)}{\partial x}=0$$
$$T_{j}^{n+1}=T_{j}^{n}+\frac{\alpha \Delta t}{\Delta x^{2}}\left[T_{j+1}^{n}-2T_{j}^{n}+T_{j-1}^{n}\right]$$


<p align="center">
  <img width="460" height="300" src="https://github.com/danielhalvorsen/TEP4165_python/blob/master/Figures/FVM_EXACT_HEATCONDUCTION.png">
</p>

* Assignment 3
    * Features an explicit upwind finite volume method for the 1D linear advection equation. 
    * For this specific case the advection velocity is u=-0.25 and the Courant number is C=-0.5.
    * We let the right boundary condition coincide with the initial condition.
$$\frac{\partial T}{\partial t}+u\frac{\partial T}{\partial x}=0$$
$$T_{j}^{n+1}=T_{j}^{n}-\underbrace{\frac{u \Delta t}{\Delta x}}_{\text{C}}\left(T_{j+1}^{n}-T_{j}^{n}  \right)$$
$$T_{NJ+1}=T_{b}=200$$

<p align="center">
  <img width="460" height="300" src="https://github.com/danielhalvorsen/TEP4165_python/blob/master/Figures/expl_upwind_C-05.png">
</p>