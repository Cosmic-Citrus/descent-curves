import sympy
sympy.init_printing(use_unicode=True)

## Define symbols
x = sympy.symbols("x")
y = sympy.Function("y")(x)
y_prime = y.diff(x)
y_double_prime = y.diff(x, 2)
g, y0 = sympy.symbols("g y0")

## Define f(y, y')
f = 1/sympy.sqrt(2*g) * sympy.sqrt(1 + y_prime**2) / sympy.sqrt(y - y0)

## Euler-Lagrange equations
df_dy = sympy.diff(f, y)
df_dy_prime = sympy.diff(f, y_prime)
d_dx_df_dy_prime = sympy.diff(df_dy_prime, x)
el_eq = df_dy - d_dx_df_dy_prime
el_eq_simp = el_eq.factor().simplify()

#####
# sympy.pprint(
# 	el_eq_simp)
#####

# sol = sympy.dsolve(
# 	el_eq_simp,
# 	y)

# sympy.pprint(
# 	sol)

p = sympy.Function('p')(y) # p is dy/dx, treated as a function of y
# # Replace y'' with p * dp/dy
# reduced_ode = el_eq_simp.numerator.subs({
#     y_double_prime: p * p.diff(y),
#     y_prime: p
# })

# # Simplify to see the first-order ODE
# re_reduced_ode = sympy.simplify(reduced_ode)
# # Result: 2*p(y)*(y - y0)*p'(y) + p(y)**2 + 1 = 0
num, den = el_eq_simp.as_numer_denom()

# 3. Perform the substitution
# We replace the derivatives of y(x) with p and its derivative with respect to y
reduced_ode = num.subs({
    y.diff(x, 2): p * p.diff(y),
    y.diff(x): p,
    y: y # This ensures y(x) symbols are treated as the variable y
})

reduced_ode_simp = reduced_ode.simplify().factor()
# sympy.pprint(
# 	reduced_ode_simp)


k, phi = sympy.symbols("k phi")


y = y0 - k * sympy.sin(phi)**2

# 1. Calculate dy/d_phi
dy_dphi = y.diff(phi) # Result: -2*k*sin(phi)*cos(phi)

# 2. Use our discovered p = cot(phi)
p = sympy.cot(phi)

# 3. Find dx/d_phi
dx_dphi = dy_dphi / p 
# Result simplifies to: -2*k*sin^2(phi)

sympy.pprint(
	dy_dphi.simplify())
sympy.pprint(
	dx_dphi.simplify())



# sympy.pprint(sympy.simplify(reduced_ode))

# p_sol = sympy.dsolve(reduced_ode_simp, p)
# sympy.pprint(p_sol)






##