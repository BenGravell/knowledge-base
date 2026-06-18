RES: Regularized Stochastic BFGS Algorithm

Topics include Convex optimization, Gradient descent, Stochastic gradients, Optimization, RES, Stochastic BFGS, BFGS, Stochastic gradient descent.

RES, a regularized stochastic version of the Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton method is proposed to solve convex optimization problems with stochastic objectives. The use of stochastic gradient descent algorithms is widespread, but the number of iterations required to approximate optimal arguments can be prohibitive in high dimensional problems. Application of second order methods, on the other hand, is impracticable because computation of objective function Hessian inverses incurs excessive computational cost. BFGS modifies gradient descent by introducing a Hessian approximation matrix computed from finite gradient differences. RES utilizes stochastic gradients in lieu of deterministic gradients for both, the determination of descent directions and the approximation of the objective function's curvature. Since stochastic gradients can be computed at manageable computational cost RES is realizable and retains the convergence rate advantages of its deterministic counterparts. Convergence results show that lower and upper bounds on the Hessian egeinvalues of the sample functions are sufficient to guarantee convergence to optimal arguments....

## Introduction

Stochastic optimization algorithms are used to solve the problem of optimizing an objective function over a set of feasible values in situations where the objective function is defined as an expectation over a set of random functions. In particular, consider an optimization variable $\mathbf{w} \in {\mathbb{R}}^{n}$ and a random variable ${\mathbf{θ}} \in \Theta \subseteq {\mathbb{R}}^{p}$ that determines the choice of a function ${f{(\mathbf{w},{\mathbf{θ}})}}:{{\mathbb{R}}^{n \times p}\rightarrow{\mathbb{R}}}$....

We refer to $f{(\mathbf{w},{\mathbf{θ}})}$ as the random or instantaneous functions and to ${F{(\mathbf{w})}}:={{\mathbb{E}}_{\mathbf{θ}}{\lbrack{f{(\mathbf{w},{\mathbf{θ}})}}\rbrack}}$ as the average function. Problems having the form in are common in machine learning as well as in optimal resource allocation in wireless systems.

## Conclusions

Convex optimization problems with stochastic objectives were considered. RES, a stochastic implementation of a regularized version of the Broyden-Fletcher-Goldfarb-Shanno quasi-Newton method was introduced to find corresponding optimal arguments. Almost sure convergence was established under the assumption that sample functions have well behaved Hessians. A linear convergence rate in expectation was further proven. Numerical results showed that RES affords important reductions in terms of convergence time relative to stochastic gradient descent....

Substituting the lower bound in for the corresponding summand in (III) and further noting the definition of $K:={{MS^{2}{({{1/\delta} + \Gamma})}^{2}}/2}$ in the statement of the lemma, the result in follows.

Our goal here is to show that as time progresses the sequence of variable iterates $\mathbf{w}_{t}$ approaches the optimal argument $\mathbf{w}^{\ast}$. In proving this result we make the following assumptions.

In (IV), the random vector $\mathbf{θ}$ is chosen uniformly at random from the $n$ dimensional box $\Theta = {\lbrack{- \theta_{0}},\theta_{0}\rbrack}^{n}$ for some given constant $\theta_{0} < 1$. The linear term $\mathbf{b}^{T}\mathbf{w}$ is added so that the instantaneous functions $f{(\mathbf{w},\theta)}$ have different minima which are (almost surely) different from the minimum of the average function $F{(\mathbf{w})}$....
