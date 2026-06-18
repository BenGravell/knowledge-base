Minimizing Finite Sums with the Stochastic Average Gradient

Topics include Stochastic average gradient, Finite-sum optimization, Variance reduction, Linear convergence, Convex optimization, Non-uniform sampling, Empirical risk minimization.

Gives the extended analysis of SAG for smooth finite-sum convex objectives, proving faster rates than black-box stochastic gradient methods and linear convergence under strong convexity. Compared with the shorter NeurIPS paper, this version clarifies the Lyapunov-style proof, step-size behavior, storage tradeoffs, and non-uniform sampling ideas that made SAG a canonical variance-reduction method.

We propose the stochastic average gradient (SAG) method for optimizing the sum of a finite number of smooth convex functions. Like stochastic gradient (SG) methods, the SAG method's iteration cost is independent of the number of terms in the sum. However, by incorporating a memory of previous gradient values the SAG method achieves a faster convergence rate than black-box SG methods. The convergence rate is improved from O(1/k^{1/2}) to O(1/k) in general, and when the sum is strongly-convex the convergence rate is improved from the sub-linear O(1/k) to a linear convergence rate of the form O(p^k) for p \textless{} 1. Further, in many cases the convergence rate of the new method is also faster than black-box deterministic gradient methods, in terms of the number of gradient evaluations. Numerical experiments indicate that the new algorithm often dramatically outperforms existing SG and deterministic gradient methods, and that the performance may be further improved through the use of non-uniform sampling strategies.

## Introduction

A plethora of the optimization problems arising in practice involve computing a minimizer of a finite sum of functions measuring misfit over a large number of data points. A classical example is least-squares regression,

where the $a_{i} \in {\mathbb{R}}^{p}$ and $b_{i} \in {\mathbb{R}}$ are the data samples associated with a regression problem. Another important example is logistic regression,

Non-Uniform Sampling: We have given an argument that non-uniform sampling should benefit the SAG algorithm, and shown empirically that it can lead to a substantial improvement. However, we have not yet given a full analysis of this scheme. Subsequent works have shown that the type of dependency we conjecture here (e.g., dependence on the average Lispschitz constant) can be achieved with non-uniform sampling in the context of SDCA \Qu et al., [2014, Zhao and Zhang, 2014\], SVRG \Xiao and Zhang and SAGA \Schmidt et al.,

Step-size selection and termination criteria: The three major disadvantages of SG methods are: (i) the slow convergence rate, (ii) deciding when to terminate the algorithms, and (iii) choosing the step size while running the algorithm. This work shows that the SAG iterations achieve a much faster convergence rate, but the SAG iterations may also be advantageous in terms of termination criteria and choosing step sizes....

### Comparison to FG and SG Methods

This update allows SAG to be efficiently applied to sparse data sets where $n$ and $p$ are both in the millions or higher but the number of non-zeros is much less than $np$.

Figure 2: Comparison of optimization different FG and SG methods to coordinate optimization methods.The top row gives results on the quantum (left), protein (center) and covertype (right) datasets. The middle row gives results on the rcv1 (left), news (center) and spam (right) datasets. The bottom row gives results on the rcv1Full (left), sido (center), and alpha (right) datasets. This figure is best viewed in colour.

where the $a_{i} \in {\mathbb{R}}^{p}$ and $b_{i} \in {\{{- 1},1\}}$ are the data samples associated with a binary classification problem. A key challenge arising in modern applications is that the number of data points $n$ (also known as *training examples*) can be extremely large, while there is often a large amount of redundancy between examples....
