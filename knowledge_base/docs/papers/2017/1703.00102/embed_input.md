SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient

Topics include Stochastic gradients, Learning, SARAH, Stochastic recursive gradients.

In this paper, we propose a StochAstic Recursive grAdient algoritHm (SARAH), as well as its practical variant SARAH+, as a novel approach to the finite-sum minimization problems. Different from the vanilla SGD and other modern stochastic methods such as SVRG, S2GD, SAG and SAGA, SARAH admits a simple recursive framework for updating stochastic gradient estimates; when comparing to SAG/SAGA, SARAH does not require a storage of past gradients. The linear convergence rate of SARAH is proven under strong convexity assumption. We also prove a linear convergence rate (in the strongly convex case) for an inner loop of SARAH, the property that SVRG does not possess. Numerical experiments demonstrate the efficiency of our algorithm.

## Introduction

We are interested in solving a problem of the form

where each $f_{i}$, $i \in {\lbrack n\rbrack}\overset{\text{def}}{=}{\{ 1,\ldots,n\}}$, is convex with a Lipschitz continuous gradient. Throughout the paper, we assume that there exists an optimal solution $w^{\ast}$ of.

## Conclusion

We propose a new variance reducing stochastic recursive gradient algorithm SARAH, which combines some of the properties of well known existing algorithms, such as SAGA and SVRG. For smooth convex functions, we show a sublinear convergence rate, while for strongly convex cases, we prove the linear convergence rate and the computational complexity as those of SVRG and SAG. However, compared to SVRG, SARAH's convergence rate constant is smaller and the algorithms is more stable both theoretically and numerically. Additionally, we prove the linear convergence for inner loops of SARAH which support the claim of stability....

### Lemma 2

Again, we note that Assumption 2b implies Assumption 3, but Assumption 2a. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient") does not. Hence in our analysis, depending on the result we aim at, we will require Assumption 3 to hold by itself, or Assumption 2a. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient") and Assumption 3 to hold together, or Assumption 2b to hold by itself. We will always use Assumption 1....

We now turn to estimating convergence of SARAH with multiple outer steps. Simply using Theorem 2 for each of the outer steps we have the following result.

In recent years, many advanced optimization methods have been developed for problem. While the objective function is smooth and convex, the traditional optimization methods, such as gradient descent (GD) or Newton method are often impractical for this problem, when $n$ -- the number of training samples and hence the number of $f_{i}$'s -- is very large. In particular, GD updates iterates as follows

Under strong convexity assumption on $P$ and with appropriate choice of $\eta_{t}$, GD converges at a linear rate in terms of objective function values $P{(w_{t})}$. However, when $n$ is large, computing ${\nabla P}{(w_{t})}$ at each iteration can be prohibitive.
