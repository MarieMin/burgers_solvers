import method1 as m1
import method2 as m2
from math import pi as PI

# Method 1

# u, x = m1.convection_diffusion(151, 151, 0.5, 2.0 * PI, 0.1)
# u_analytical, x = m1.analytical_solution(151, 151, 0.5, 2.0 * PI, 0.1)
# m1.plot_diffusion(u_analytical, u, x, 151, 'Figure 1: nu=0.1, nt=151, nx=151, tmax=0.5s')
#
# u, x = m1.convection_diffusion(151, 151, 0.5, 2.0 * PI, 0.01)
# u_analytical, x = m1.analytical_solution(151, 151, 0.5, 2.0 * PI, 0.01)
# m1.plot_diffusion(u_analytical, u, x, 151, 'Figure 2: nu=0.01, nt=151, nx=151, tmax=0.5s')



# Method 2

m2.burgers2()
