import numpy as np
import matplotlib.pyplot as plt
import sympy
sympy.init_printing()

u_max,u_star,rho_max,rho_star,A,B = sympy.symbols('u_max u_* rho_max rho_* A B')

eq1 = sympy.Eq(0,u_max*rho_max*(1-A*rho_max-B*rho_max**2))
eq2 = sympy.Eq(0,u_max*(1-2*A*rho_star-3*B*rho_star**2))
eq3 = sympy.Eq(u_star,u_max*(1-A*rho_star-B*rho_star**2))

eq4 = sympy.Eq(eq2.lhs-3*eq3.lhs,eq2.rhs-3*eq3.rhs)

rho_starsolve = sympy.solve(eq4,rho_star)[0]
B_sol = sympy.solve(eq1,B)[0]

quad_A = eq2.subs([(rho_star,rho_starsolve),(B,B_sol)])
A_sol = sympy.solve(quad_A,A)
