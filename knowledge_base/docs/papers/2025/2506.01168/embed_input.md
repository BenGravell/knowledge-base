The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions

Topics include Optimization, C2M, TM, Convex function.

We consider iterative gradient-based optimization algorithms applied to functions that are smooth and strongly convex. The fastest globally convergent algorithm for this class of functions is the Triple Momentum (TM) method. We show that if the objective function is also twice continuously differentiable, a new, faster algorithm emerges, which we call C2-Momentum (C2M). We prove that C2M is globally convergent and that its worst-case convergence rate is strictly faster than that of TM, with no additional computational cost. We validate our theoretical findings with numerical examples, demonstrating that C2M outperforms TM when the objective function is twice continuously differentiable.

## INTRODUCTION

We consider the well-studied optimization problem

where $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is continuously differentiable. A popular approach to solving, particularly when the dimension $d$ is large, is to use iterative gradient-based methods, such as Gradient Descent (GD) and its accelerated variants.

We apply Sturm's theorem \[, Thm. 2.62\] to $p{(\kappa,\rho)}$ as a polynomial in $\rho$. Define the Sturm sequence

where $\text{rem}{}$ denotes the remainder after polynomial division (considered as polynomials in $\rho$), and the sequence terminates when $p_{i}$ is constant, which occurs for $i \leq 7$ since $p$ is degree $7$ in $\rho$. Evaluating the Sturm sequence at $\rho = 0$ and $\rho = 1$ yields 5 sign changes and 3 sign changes, respectively. Therefore, there are two real roots in the interval $$. Moreover, $p$ is positive when $\rho = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$, negative when $\rho = {1 - \sqrt{\frac{2}{\kappa}}}$, and positive when $\rho = 1$....

### Global Stability via Frequency-Domain Analysis

To describe our main result, we first define the root-convergence factor of an algorithm, which is a way to characterize its rate of convergence; see \[, §9.2\].

The stability condition is equivalent to stability of $\overset{\sim}{G}$. It is straightforward to verify that the interconnection of $\overset{\sim}{G}$ and $\overset{\sim}{\Delta}$ is well-posed and that $\tau\overset{\sim}{\Delta}$ satisfies the IQC $\Pi = {\Pi_{{- 1},1} \otimes I_{d}}$ for all $\tau \in {\lbrack 0,1\rbrack}$. Therefore, the first two conditions in ‣ 3.1 Global Stability via Frequency-Domain Analysis ‣ 3 CONVERGENCE ANALYSIS ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions") hold for the transformed system $\overset{\sim}{G}$ and the IQC $\Pi$....

A central question in the study of iterative methods is that of *worst-case convergence rate* over a class of functions $\mathcal{F}$. In this letter, we consider the *root-convergence factor* (also known as geometric convergence rate), denoted $\rho \in {}$, a notion we make precise in Section 2. Associated with the root-convergence factor are two important concepts:

### Lower bounds

$\rho$ is a *lower bound* for $\mathcal{F}$ if for any algorithm, there exists $f \in \mathcal{F}$ and an algorithm...
