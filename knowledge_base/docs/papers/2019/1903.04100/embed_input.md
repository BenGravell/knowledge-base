Conformal Symplectic and Relativistic Optimization

Topics include Optimization, Symplectic geometry, Momentum methods, Nesterov acceleration, Hamiltonian systems, Relativistic mechanics.

Analyzes momentum-based optimization algorithms (Nesterov, heavy ball) through the lens of structure-preserving discretizations of dissipative Hamiltonian systems. Proposes a novel relativistic optimizer that normalizes momentum, unifying both Nesterov and heavy ball as special limiting cases, with improved stability and no additional computational overhead. Published at NeurIPS 2020.

Arguably, the two most popular accelerated or momentum-based optimization methods in machine learning are Nesterov's accelerated gradient and Polyaks's heavy ball, both corresponding to different discretizations of a particular second order differential equation with friction. Such connections with continuous-time dynamical systems have been instrumental in demystifying acceleration phenomena in optimization. Here we study structure-preserving discretizations for a certain class of dissipative (conformal) Hamiltonian systems, allowing us to analyze the symplectic structure of both Nesterov and heavy ball, besides providing several new insights into these methods. Moreover, we propose a new algorithm based on a dissipative relativistic system that normalizes the momentum and may result in more stable/faster optimization. Importantly, such a method generalizes both Nesterov and heavy ball, each being recovered as distinct limiting cases, and has potential advantages at no additional cost.

## Introduction

Gradient based optimization methods are ubiquitous in machine learning since they only require first order information on the objective function. This makes them computationally efficient. However, vanilla gradient descent can be slow. Alternatively, *accelerated gradient methods*, whose construction can be traced back to Polyak and Nesterov, became popular due to their ability to achieve best worst-case complexity bounds. The heavy ball method, also known as *classical momentum* (CM) method, is given by

where $k = {0,1,\ldots}$ is the iteration number, $\mu \in {}$ is the momentum factor, $\epsilon > 0$ is the learning rate, and $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is the function being minimized. Similarly, *Nesterov's accelerated gradient* (NAG) can be found in the form

On a higher level, this paper shows how structure-preserving discretizations of classical dissipative systems can be useful for studying existing optimization algorithms, as well as introduce new methods inspired by real physical systems. A thorough justification for the use of structure-preserving---or "dissipative symplectic"---discretizations in this context was recently provided in under great generality.

Finally, a more refined analysis of RGD is certainly an interesting future problem, though considerably challenging due to the nonlinearity introduced by the $\sqrt{1 + {\delta{\| v\|}^{2}}}$ term in the updates of Algorithm 1. To give an example, even if one assumes a simple quadratic function ${f{(x)}} = {{({\lambda/2})}x^{2}}$, the differential equation (5.2) is nonlinear and does not admit a closed form solution, contrary to the differential equation associated to CM and NAG which is linear and can be readily integrated. Thus, even in continuous-time, the analysis for RGD is likely to be involved....

### Preserving stability and continuous-time rates

The classical momentum or heavy ball method (1.1) is a conformal symplectic integrator for the Hamiltonian system (2.2). Moreover, it is an integrator of order $r = 1$.

Again, this is strikingly similar to (4.20). Note that this equation does not have the spurious damping term ${({h/m})}{\nabla^{2}f}{(x)}$ as in (4.20), making even more explicit that it preserves exactly the dissipation of the original continuous-time system....
