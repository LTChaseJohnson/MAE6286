import numpy as np
import matplotlib.pyplot as plt
import sympy

u_max,u_star,rho_max,rho_star,A,B,u_wave,rho_min = sympy.symbols('u_max u_* rho_max rho_* A B u_wave rho_min')

eq1 = sympy.Eq(0,u_max*rho_max*(1-A*rho_max-B*rho_max**2))
eq2 = sympy.Eq(0,u_max*(1-2*A*rho_star-3*B*rho_star**2))
eq3 = sympy.Eq(u_star,u_max*(1-A*rho_star-B*rho_star**2))

eq4 = sympy.Eq(eq2.lhs-3*eq3.lhs,eq2.rhs-3*eq3.rhs)

rho_starsolve = sympy.solve(eq4,rho_star)[0]
B_sol = sympy.solve(eq1,B)[0]

quad_A = eq2.subs([(rho_star,rho_starsolve),(B,B_sol)])
A_sol = sympy.solve(quad_A,A)

A1 = A_sol[0].evalf(subs={u_star:1.5,u_max:2.0,rho_max:15.})
A2 = A_sol[1].evalf(subs={u_star:1.5,u_max:2.0,rho_max:15.})
B = B_sol.evalf(subs={A: A2,rho_max:15.})

eq5 = sympy.Eq(0,u_max*(1-2*A*rho_min-3*B*rho_min**2))
rho_min_sol = sympy.solve(eq5,rho_min)

print 'A1 = ',A1
print 'A2 = ',A2
print 'B = ',B
print 'rho_min = ',rho_min_sol