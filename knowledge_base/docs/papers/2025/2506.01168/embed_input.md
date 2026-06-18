The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions

Topics include Optimization, C2M, TM, Convex function.

We consider iterative gradient-based optimization algorithms applied to functions that are smooth and strongly convex. The fastest globally convergent algorithm for this class of functions is the Triple Momentum (TM) method. We show that if the objective function is also twice continuously differentiable, a new, faster algorithm emerges, which we call C2-Momentum (C2M). We prove that C2M is globally convergent and that its worst-case convergence rate is strictly faster than that of TM, with no additional computational cost. We validate our theoretical findings with numerical examples, demonstrating that C2M outperforms TM when the objective function is twice continuously differentiable.

## INTRODUCTION

We consider the well-studied optimization problem

where $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is continuously differentiable. A popular approach to solving, particularly when the dimension $d$ is large, is to use iterative gradient-based methods, such as Gradient Descent (GD) and its accelerated variants.

A central question in the study of iterative methods is that of *worst-case convergence rate* over a class of functions $\mathcal{F}$. In this letter, we consider the *root-convergence factor* (also known as geometric convergence rate), denoted $\rho \in {}$, a notion we make precise in Section 2.

## Lower bounds

$\rho$ is a *lower bound* for $\mathcal{F}$ if for any algorithm, there exists $f \in \mathcal{F}$ and an algorithm initialization such that the algorithm converges no faster than $\rho$.

## DISCUSSION

The proposed C2M algorithm is the first method, to the best of the authors' knowledge, that is designed specifically for the function class $\mathcal{S}_{m,L}^{2}$. The minimax rate for this function class, however, is not known, in contrast to the function classes $\mathcal{S}_{m,L}^{1}$ and $\mathcal{Q}_{m,L}$. Finding this minimax rate or even lower bounds are interesting open problems.

The parameters of C2M are related to two other algorithms from the literature. As we have already seen, C2M reduces to HB when $\rho = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$. Moreover, the general C2M parameters are identical (after appropriate transformations) to those of GAG \[, Cor. 1.1\]. This makes sense, since the work also considers the family of algorithms and is optimizing for local convergence. The two cases differ, however, in the choice of $\rho$, since GAG is optimized over the function class $\mathcal{F}_{m,L}$ defined in Section 1 rather than $\mathcal{S}_{m,L}^{2}$.
