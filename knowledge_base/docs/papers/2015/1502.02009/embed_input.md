A General Analysis of the Convergence of ADMM

Topics include Stability analysis, Optimization, Alternating-direction method of multipliers, Rate of convergence.

We provide a new proof of the linear convergence of the alternating direction method of multipliers (ADMM) when one of the objective terms is strongly convex. Our proof is based on a framework for analyzing optimization algorithms introduced in Lessard et al., reducing algorithm convergence to verifying the stability of a dynamical system. This approach generalizes a number of existing results and obviates any assumptions about specific choices of algorithm parameters. On a numerical example, we demonstrate that minimizing the derived bound on the convergence rate provides a practical approach to selecting algorithm parameters for particular ADMM instances. We complement our upper bound by constructing a nearly-matching lower bound on the worst-case rate of convergence.

## Introduction

The alternating direction method of multipliers (ADMM) seeks to solve the problem

with variables $x \in {\mathbb{R}}^{p}$ and $z \in {\mathbb{R}}^{q}$ and constants $A \in {\mathbb{R}}^{r \times p}$, $B \in {\mathbb{R}}^{r \times q}$, and $c \in {\mathbb{R}}^{r}$. ADMM was introduced in Glowinski & Marroco and Gabay & Mercier. More recently, it has found applications in a variety of distributed settings such as model fitting, resource allocation, and classification....

In the case that Assumption 3 does not hold, the most likely cause is that we lack the strong convexity of $f$. One approach to handling this is to run Algorithm 2 on the modified function ${f{(x)}} + {\frac{\delta}{2}{\| x\|}^{2}}$. By completing the square in the $x$ update, we see that this amounts to an extremely minor algorithmic modification (it only affects the $x$ update).

It should be clear that other operator splitting methods such as Douglas--Rachford splitting and forward-backward splitting can be cast in this framework and analyzed using the tools presented here.

and so the linear matrix inequality in depends only on $\kappa$ and not on $\hat{m}$ and $\hat{L}$. Therefore, we will consider step sizes of this form (recall from that $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\rho_{0}}$). The choice $\varepsilon = 0$ is common in the literature, but requires the user to know the strong-convexity parameter $\hat{m}$. We also consider the choice $\varepsilon = 0.5$, which produces worse guarantees, but does not require knowledge of $\hat{m}$.

### Proof

Let $Q$ be a $d$-dimensional symmetric positive-definite matrix whose largest and smallest eigenvalues are $L$ and $m$ respectively. Let ${f{(x)}} = {\frac{1}{2}x^{\top}Qx}$ be a quadratic and let ${g{(z)}} = {\frac{\delta}{2}{\| z\|}^{2}}$ for some $\delta \geq 0$. Let $A = I_{d}$, $B = {- I_{d}}$, and $c = 0$. With these definitions, the optimization problem in is solved by $x = z = 0$. The updates for Algorithm 2 are given by

Part of the appeal of ADMM is the fact that, in many contexts, the algorithm updates lend themselves to parallel implementations. The algorithm is given in Algorithm 1. We refer to $\rho > 0$ as the step-size parameter.

1: Input: functions f and g, matrices A and B, vector c, parameter ρ
7: until meet stopping criterion
Algorithm 1 Alternating Direction Method of Multipliers
