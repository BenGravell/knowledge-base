The Speed-Robustness Trade-Off for First-Order Methods with Additive Gradient Noise

Topics include Gradient descent, Robustness, Optimization, GD, S heavy Ball, HB, S Fast gradient, FG, Convex function.

We study the trade-off between convergence rate and sensitivity to stochastic additive gradient noise for first-order optimization methods. Ordinary Gradient Descent (GD) can be made fast-and-sensitive or slow-and-robust by increasing or decreasing the stepsize, respectively. However, it is not clear how such a trade-off can be navigated when working with accelerated methods such as Polyak's Heavy Ball (HB) or Nesterov's Fast Gradient (FG) methods. We consider two classes of functions: strongly convex quadratics and smooth strongly convex functions. For each function class, we present a tractable way to compute the convergence rate and sensitivity to additive gradient noise for a broad family of first-order methods, and we present algorithm designs that trade off these competing performance metrics. Each design consists of a simple analytic update rule with two states of memory, similar to HB and FG. Moreover, each design has a scalar tuning parameter that explicitly trades off convergence rate and sensitivity to additive gradient noise....

## Introduction

We consider the problem of designing robust first-order methods for unconstrained minimization. Given a continuously differentiable function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, consider solving the optimization problem

where the algorithm only has access to gradient measurements corrupted by additive stochastic noise.^11^1Preliminary versions of portions of this work appeared in the conference proceedings. Specifically, the algorithm can sample the oracle ${g{(x)}}{: =}{{{\nabla f}{(x)}} + w}$, where $w$ is zero-mean and independent across queries. This form of additive noise arises in various applications....

An interesting future direction is exploring adaptive versions of these algorithms, where the parameter $r$ is varied over time. We showed in Fig. 5 that a hand-tuned piecewise constant version of RHB can match both Nesterov's lower bound and the gradient lower bound, so more sophisticated adaptive schemes such as those described in Section 1.2 might also work. One could also adjust parameters continually, but proving the convergence of adaptive algorithms is generally more challenging....

Another interesting open question is whether our analysis is tight. For $F_{m,L}$ (Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise")), our bounds depend on $\ell$. It is unknown (i) how large $\ell$ needs to be in order to obtain the tightest possible bounds on convergence rate and sensitivity, and (ii) whether Theorem 4.5....

Although we set out to design an algorithm in the three-parameter class $(\alpha,\beta,\eta)$, our designed algorithm RHB uses $\eta = 0$, so it is a particular tuning of HB. Our numerical experiments in Section 5.1 suggest that this parameter choice yields the most effective trade-off between rate and sensitivity. In other words, it is unnecessary to use a nonzero $\eta$ when optimizing over the class $Q_{m,L}$.

Table 1: Comparison of different algorithms with their recommended/standard tunings. For RM, the parameter satisfies ${1 - \sqrt{\frac{m}{L}}} \leq r \leq {1 - \frac{m}{L}}$, and interpolates between TM and GD with $\alpha = \frac{1}{L}$.

We now use the interpolation conditions to search for a Lyapunov function that depends on the state ${\mathbf{x}}^{t}$ of the lifted...
