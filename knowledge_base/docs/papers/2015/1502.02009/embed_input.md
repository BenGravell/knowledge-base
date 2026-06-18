A General Analysis of the Convergence of ADMM

Topics include Stability analysis, Optimization, Alternating-direction method of multipliers, Rate of convergence.

We provide a new proof of the linear convergence of the alternating direction method of multipliers (ADMM) when one of the objective terms is strongly convex. Our proof is based on a framework for analyzing optimization algorithms introduced in Lessard et al., reducing algorithm convergence to verifying the stability of a dynamical system. This approach generalizes a number of existing results and obviates any assumptions about specific choices of algorithm parameters. On a numerical example, we demonstrate that minimizing the derived bound on the convergence rate provides a practical approach to selecting algorithm parameters for particular ADMM instances. We complement our upper bound by constructing a nearly-matching lower bound on the worst-case rate of convergence.

## Introduction

The alternating direction method of multipliers (ADMM) seeks to solve the problem

with variables $x \in {\mathbb{R}}^{p}$ and $z \in {\mathbb{R}}^{q}$ and constants $A \in {\mathbb{R}}^{r \times p}$, $B \in {\mathbb{R}}^{r \times q}$, and $c \in {\mathbb{R}}^{r}$. ADMM was introduced in Glowinski & Marroco and Gabay & Mercier. More recently, it has found applications in a variety of distributed settings such as model fitting, resource allocation, and classification.

Part of the appeal of ADMM is the fact that, in many contexts, the algorithm updates lend themselves to parallel implementations. The algorithm is given in Algorithm 1. We refer to $\rho > 0$ as the step-size parameter.

The parameter $\alpha$ is typically chosen to lie in the interval $(0,2\rbrack$, but we demonstrate in Section 8 that a larger set of choices can lead to convergence. Over-relaxed ADMM is described in Algorithm 2. When $\alpha = 1$, Algorithm 2 and Algorithm 1 coincide. We will analyze Algorithm 2.

The conventional wisdom that ADMM works well without any tuning, for instance by setting $\rho = 1$, is often not borne out in practice. Algorithm 1 can be challenging to tune, and Algorithm 2 is even harder. We use the machinery developed in this paper to make reasonable recommendations for setting $\rho$ and $\alpha$ when some information about $f$ is available (Section 8).

## Discussion

We showed that a framework based on semidefinite programming can be used to prove convergence rates for the alternating direction method of multipliers and allows a unified treatment of the algorithm's many variants, which arise through the introduction of additional parameters. We showed how to use this framework for establishing convergence rates, as in Theorem 6 and Theorem 7, and how to use this framework for parameter selection in practice, as in Section 8. The potential uses are numerous.

In the case that Assumption 3 does not hold, the most likely cause is that we lack the strong convexity of $f$. One approach to handling this is to run Algorithm 2 on the modified function ${f{(x)}} + {\frac{\delta}{2}{\| x\|}^{2}}$. By completing the square in the $x$ update, we see that this amounts to an extremely minor algorithmic modification (it only affects the $x$ update).
