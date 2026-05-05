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

## --- ADDED SYMBOLS FOR MWE COMPLETION ---
p, p_prime = sympy.symbols("p p_prime")
# First, replace the formal derivatives with our algebraic placeholders
el_eq_reduced = el_eq.subs({y.diff(x, 2): p_prime, y.diff(x): p})

## 1. Define dp/dy as a single symbol 
dp_dy = sympy.symbols("dp_dy")

# 2. Substitute p' with p * (dp/dy)
el_eq_first_order = el_eq_reduced.subs(p_prime, p * dp_dy)

# 3. Rearrange to separate variables strictly: f(p) dp = g(y) dy
# From dp/dy = (1 + p^2) / (2p * (y0 - y))
# We move terms: (2p / (1 + p^2)) dp = (1 / (y0 - y)) dy
lhs_integrand = 2*p / (1 + p**2)
rhs_integrand = 1 / (y0 - y)

# 4. Integrate both sides
lhs_int = sympy.Integral(lhs_integrand, p)
rhs_int = sympy.Integral(rhs_integrand, y)

# 5. Evaluate and equate
log_eq = sympy.Eq(lhs_int.doit(), rhs_int.doit())
print("Equation with logs:")
sympy.pprint(log_eq)

# 6. Exponentiate both sides to "cancel" logs (SymPy's solve does this automatically)
p_sol = sympy.solve(log_eq, p)
print("\nFinal y' (p) solution:")
sympy.pprint(p_sol)


# Use the substitution y = y0 + k * sin^2(phi)
phi = sympy.symbols("phi")
k = sympy.symbols("k")

# y - y0 = k * sin^2(phi)
# dy = 2k * sin(phi) * cos(phi) dphi
dy_dphi = 2 * k * sympy.sin(phi) * sympy.cos(phi)

# Substitute y into your integrand: sqrt((y - y0) / (k - (y - y0)))
# This simplifies to sqrt(sin^2(phi) / cos^2(phi)) = tan(phi)
dx_dphi = sympy.tan(phi) * dy_dphi

# Integrate with respect to phi
x_param = sympy.integrate(dx_dphi, phi)

print("Parametric x(phi):")
sympy.pprint(sympy.simplify(x_param))

theta = sympy.symbols("theta", real=True)

phi = theta / 2

# From previous derivation:
# y = y0 + k * sin(phi)**2
y_phi = y0 + k * sympy.sin(phi)**2
y_theta = sympy.simplify(y_phi.subs(phi, theta/2))
# y_rewritten = sympy.expand_trig(y_theta).rewrite(sympy.cos)
# FORCE the (1 - cos(theta)) form:
# 1. Rewrite in terms of cos
# 2. expand_trig to apply the half-angle reduction
y_traditional = y0 + sympy.expand_trig(y_theta.rewrite(sympy.cos))
y_rewritten = sympy.simplify(y_traditional)


# x = k * (phi - sin(2*phi)/2)
x_phi = k * (phi - sympy.sin(2*phi)/2)
x_theta = sympy.simplify(x_phi.subs(phi, theta/2))

sympy.pprint(y_theta)
sympy.pprint(y_rewritten)
# sympy.pprint(y_traditional)
sympy.pprint(x_theta)
##