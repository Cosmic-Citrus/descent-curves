# Repo:    descent-curves

The purpose of this code is to explore descent curves. with special attention focused on the properties of the [brachistochrone](https://en.wikipedia.org/wiki/Brachistochrone_curve).

## Description

Suppose a particle of mass $m$ starts at rest and is subject to downward-directed gravitational acceleration $g$ due to the force of gravity; this particle traverses some curve from $A(x_0, y_0)$ to $B(x_1, y_1)$ in time $t$. One can construct infinitely many curves from $A$ to $B$, but only one curve is the optimal curve that corresponds to the least travel time - this special curve is called the brachistochrone.

![example-trajectory_comparison](output/example_01-trajectories/line-parabola-ellipse-exponential-cosine-brachistochrone-path.png)

A particle at rest necessarily has velocity $v=0 \frac{m}{s}$. At point $A$, the potential energy $U$ of a particle at a given height $h$ along the curve above the ground is given by $U=mgh$ and the kinetic energy $T$ is $0$ $J$; at ground-level ($h=0$ $m$), the potential and kinetic energies are given. by $U=0$ $J$ and $T = \frac{1}{2}mv^2$. The total energy at time $t$ is given by $\mathcal{H_{t}} = T_t + U_t$. Letting $h=y - y_0$ and exploiting conservation of energy, one can solve for the velocity of the particle.

$\mathcal{H_{t=0}} = \mathcal{H_{t}}$

$\implies$ $U_{t=0} + T_{t=0}$ = $U_t + T_t$

$\implies$ $mg(y-y_0) = \frac{1}{2}mv^2$

$\implies$ $v=\sqrt{2g(y-y_0)}$

To avoid ambiguity of variables, let $y^\prime = \frac{dy}{dx}$. The Pythagorean theorem $c^2 = a^2 + b^2$ can be reformulated in terms of differential lengths that apply to any geodesic curve of differential arc-length $ds$. Using $v=\frac{ds}{dt}$, we can re-arrange terms to solve for $t$:

$ds = \sqrt{dx^2 + dy^2} = \sqrt{dx^2 (1 + (\frac{dy}{dx})^2)} = \sqrt{1 + (\frac{dy}{dx})^2} dx$

$\implies \frac{ds}{dx} = \sqrt{1 + (\frac{dy}{dx})^2}$

$\implies dt = \frac{ds}{v} = \frac{\sqrt{1 + (\frac{dy}{dx})^2}}{\sqrt{2g(y-y_0)}} dx$

$\implies t = \int_{t_0}^{t_1} dt = \int_{x_0}^{x_1} \frac{\sqrt{1 + (\frac{dy}{dx})^2}}{\sqrt{2g(y-y_0)}} dx = \frac{1}{\sqrt{2g}} \int_{x_0}^{x_1} \frac{\sqrt{1 + (\frac{dy}{dx}^2)}}{\sqrt{y-y_0}} dx$

$\implies f(y, y^\prime) = \frac{\sqrt{1 + (y^\prime)^2}}{\sqrt{y-y_0}}$

The integrand $f(y, y^\prime)$ is independent of $x$, which satisfies the requirements of the [Beltrami Identity](https://en.wikipedia.org/wiki/Beltrami_identity):

$f - y^\prime\frac{df}{dy^\prime} = k \equiv constant$

The Beltrami Identity simplifies the procedure of solving the integral equation $t = \int_{t_0}^{t_1}dt$. Rather than assuming the identity a priori, the Beltrami Identity can be derived more explicitly.

The Lagrangian $\mathcal{L(q, \dot{q}, t)} \equiv \mathcal{L} = T - U$ can be used to quantify the action $S = \int_{0}^{t} \mathcal{L} dt$. The stationarity of the action $\delta S=0$ means that the [Euler-Lagrange equations](https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation) can be used to find the critical point of action $S$. In generalized coordinates $q$ and $\dot{q}=\frac{dq}{dt}$, the Euler-Lagrange equations are given by:

$\frac{d\mathcal{L}}{dq} = \frac{d}{dt} \frac{d\mathcal{L}}{d\dot{q}} \iff \frac{df}{dy} = \frac{d}{dx} \frac{df}{d{y^\prime}}$

In this [variational calculus](https://en.wikipedia.org/wiki/Calculus_of_variations) problem, the Lagrangian is given by $\mathcal{L} = T - U = \frac{1}{2}mv^2 - mg(y-y_0)$.

$\implies$ $\frac{df}{dy} = -\frac{\sqrt{1 + (y^\prime)^2}}{2(y-y_0)^\frac{3}{2}}$

$\implies$ $\frac{df}{d{y^\prime}} = \frac{y^\prime}{\sqrt{(y-y_0)(1+(y^\prime)^2)}}$

$\implies 2(y-y_0)\frac{d^2y}{dx^2} + 1 + (\frac{dy}{dx})^2 = 0$

This second-order differential equation can be simplified into a first-order differential equation that satisfies the Beltrami Identity.

$p = \frac{dy}{dx}$

$\implies p^\prime = \frac{d^2y}{dx^2}$

$\implies 2(y-y_0)pp^\prime = -(1+p^2)$

$\implies \frac{2p}{1+p^2}dp = -\frac{dy}{y-y_0}$

$\implies \int \frac{2p}{1+p^2}dp = \int -\frac{dy}{y-y_0}$

$\implies ln(1+p^2) = -ln(y-y_0) + ln(k)$

$\implies (1+p^2) = \frac{k}{y-y_0}$

$\implies y^\prime = \sqrt{\frac{k-(y-y_0)}{y-y_0}}$

$\implies k = f(y, y^\prime)$

This first-order differential equation can be solved using the [separation of variables method](https://en.wikipedia.org/wiki/Separation_of_variables):

$\frac{dy}{dx} = \sqrt{\frac{k-(y-y_0)}{y-y_0}}$

$\implies dx = \frac{dy}{\sqrt{\frac{k - (y-y_0)}{y-y_0}}} = \sqrt{\frac{y-y_0}{k - (y - y_0)}} dy$

By trigonometric substitution, let $y-y_0 = k sin^2\phi = \frac{k}{2} (1-cos(2\phi))$

$\implies dy = 2k sin\phi cos\phi d\phi = k sin(2\phi) d\phi$

$\implies dx = \sqrt{\frac{k sin^2\phi}{k - k sin^2\phi}} 2k sin\phi cos\phi d\phi = 2k sin^2\phi d\phi = k(1 - cos(2\phi)) d\phi$

$\implies x = \int dx = k \int (1 - cos(2\phi)) d\phi = \frac{k}{2} (2\phi - sin(2\phi)) + c_x$

The parametric form of the brachistochrone equations can be obtained by substituting $c_x = x_0$, $r=\frac{k}{2}$ and $\theta = 2\phi$:

$\implies x - x_0 = r(\theta - sin\theta)$

$\implies y-y_0 = 2r sin^2(\frac{\theta}{2}) = r(1 - cos\theta)$

This parametric form satisifies the conditions of the [cycloid](https://en.wikipedia.org/wiki/Cycloid).

## Getting Started

### Dependencies

- Python 3.9.6
- numpy == 1.26.4
- matplotlib == 3.9.4
- scipy == 1.13.1

### Executing program

- Download this repository to your local computer
  
- Modify `path_to_save_directory` in the following example codes
  
  - `src/example_01-trajectories.py`
    
  - Adjust the values from `x_i`, `y_i`, `x_f`, `y_f`, and `g_acceleration`
    
- Run the example codes
  

## Version History

- 0.1
  - Initial Release

## To-Do

- Use `sympy` to solve the differential equations
- Explore tautochrone properties
- Animate the rolling circle that generates the cycloid curve
- Re-create brachistochrone curves using hypercomplex numbers (Hurwitz quaternions)
- Explore Louville theorem and symplectic phase-space in higher dimensions

## License

This project is licensed under the Apache License - see the LICENSE file for details.
