A Differential Equation for Modeling Nesterov's Accelerated Gradient Method: Theory and Insights

Topics include Nesterov acceleration, Ordinary differential equation, Differential equation.

We derive a second-order ordinary differential equation (ODE) which is the limit of Nesterov's accelerated gradient method. This ODE exhibits approximate equivalence to Nesterov's scheme and thus can serve as a tool for analysis. We show that the continuous time ODE allows for a better understanding of Nesterov's scheme. As a byproduct, we obtain a family of schemes with similar convergence rates. The ODE interpretation also suggests restarting Nesterov's scheme leading to an algorithm, which can be rigorously proven to converge at a linear rate whenever the objective is strongly convex.

## Introduction

In many fields of machine learning, minimizing a convex function is at the core of efficient model estimation. In the simplest and most standard form, we are interested in solving

where $f$ is a convex function, smooth or non-smooth, and $x \in {\mathbb{R}}^{n}$ is the variable. Since Newton, numerous algorithms and methods have been proposed to solve the minimization problem, notably gradient and subgradient descent, Newton's methods, trust region methods, conjugate gradient methods, and interior point methods.

In a different direction, there is a long history relating ordinary differential equation (ODEs) to optimization, see Helmke and Moore, Schropp and Singer, and Fiori for example. The connection between ODEs and numerical optimization is often established via taking step sizes to be very small so that the trajectory or solution path converges to a curve modeled by an ODE. The conciseness and well-established theory of ODEs provide deeper insights into optimization, which has led to many interesting findings.

Approximate equivalence between Nesterov's scheme and the ODE is established later in various perspectives, rigorous and intuitive. In the main body of this paper, examples and case studies are provided to demonstrate that the homogeneous and conceptually simpler ODE can serve as a tool for understanding, analyzing and generalizing Nesterov's scheme.

## Discussion

This paper introduces a second-order ODE and accompanying tools for characterizing Nesterov's accelerated gradient method. This ODE is applied to study variants of Nesterov's scheme and is capable of interpreting some empirically observed phenomena, such as oscillations along the trajectories. Our approach suggests a large family of generalized Nesterov's schemes that are all guaranteed to converge at the rate $O{({1/k^{2}})}$, and a restarting scheme provably achieving a linear convergence rate whenever $f$ is strongly convex.

In this paper, we often utilize ideas from continuous-time ODEs, and then apply these ideas to discrete schemes. The translation, however, involves parameter tuning and tedious calculations. This is the reason why a general theory mapping properties of ODEs into corresponding properties for discrete updates would be a welcome advance. Indeed, this would allow researchers to only study the simpler and more user-friendly ODEs.
