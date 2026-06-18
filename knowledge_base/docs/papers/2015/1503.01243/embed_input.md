A Differential Equation for Modeling Nesterov's Accelerated Gradient Method: Theory and Insights

Topics include Nesterov acceleration, Ordinary differential equation, Differential equation.

We derive a second-order ordinary differential equation (ODE) which is the limit of Nesterov's accelerated gradient method. This ODE exhibits approximate equivalence to Nesterov's scheme and thus can serve as a tool for analysis. We show that the continuous time ODE allows for a better understanding of Nesterov's scheme. As a byproduct, we obtain a family of schemes with similar convergence rates. The ODE interpretation also suggests restarting Nesterov's scheme leading to an algorithm, which can be rigorously proven to converge at a linear rate whenever the objective is strongly convex.

## Introduction

In many fields of machine learning, minimizing a convex function is at the core of efficient model estimation. In the simplest and most standard form, we are interested in solving

where $f$ is a convex function, smooth or non-smooth, and $x \in {\mathbb{R}}^{n}$ is the variable. Since Newton, numerous algorithms and methods have been proposed to solve the minimization problem, notably gradient and subgradient descent, Newton's methods, trust region methods, conjugate gradient methods, and interior point methods.

In this paper, we often utilize ideas from continuous-time ODEs, and then apply these ideas to discrete schemes. The translation, however, involves parameter tuning and tedious calculations. This is the reason why a general theory mapping properties of ODEs into corresponding properties for discrete updates would be a welcome advance. Indeed, this would allow researchers to only study the simpler and more user-friendly ODEs.

As evidenced by many examples, the viewpoint of regarding the ODE as a surrogate for Nesterov's scheme would allow a new perspective for studying accelerated methods in optimization. The discrete scheme and the ODE are closely connected by the exact mapping between the coefficients of momentum (e.g. ${({k - 1})}/{({k + 2})}$) and velocity (e.g. $3/t$). The derivations of generalized Nesterov's schemes and the speed restarting scheme are both motivated by trying a different velocity coefficient, in which the surprising phase transition at 3 is observed....

Now, it is tempting to obtain such analogs for the discrete Nesterov's scheme as well. Following the formulation of Beck and Teboulle, we wish to minimize $f$ in the composite form ${f{(x)}} = {{g{(x)}} + {h{(x)}}}$, where $g \in \mathcal{F}_{L}$ for some $L > 0$ and $h$ is convex on ${\mathbb{R}}^{n}$ possibly assuming extended value $\infty$. Define the proximal subgradient

Recall that the function considered in Figure 1 is ${f{(x)}} = {{0.02x_{1}^{2}} + {0.005x_{2}^{2}}}$, starting from $x_{0} = {}$. As the step size $s$ becomes smaller, the trajectory of Nesterov's scheme converges to the solid curve represented via the Bessel function. While approaching the minimizer $x^{\star}$, each trajectory displays the oscillation pattern, as well-captured by the zoomed Figure 1(b). This prevents Nesterov's scheme from achieving better convergence rate....
