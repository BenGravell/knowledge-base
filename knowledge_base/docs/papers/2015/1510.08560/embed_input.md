Why Random Reshuffling Beats Stochastic Gradient Descent

Topics include Gradient descent, Stochastic gradients, RR, Stochastic gradient descent.

We analyze the convergence rate of the random reshuffling (RR) method, which is a randomized first-order incremental algorithm for minimizing a finite sum of convex component functions. RR proceeds in cycles, picking a uniformly random order (permutation) and processing the component functions one at a time according to this order, i.e., at each cycle, each component function is sampled without replacement from the collection. Though RR has been numerically observed to outperform its with-replacement counterpart stochastic gradient descent (SGD), characterization of its convergence rate has been a long standing open question. In this paper, we answer this question by showing that when the component functions are quadratics or smooth and the sum function is strongly convex, RR with iterate averaging and a diminishing stepsize alpha_k = Theta(1/k^(s)) for s in (1/2, 1) converges at rate Theta(1/k^s) with probability one in the suboptimality of the objective value, thus improving upon the Omega(1/k) rate of SGD....

## Introduction: First-order incremental methods

We consider the following unconstrained optimization problem where the objective function is the sum of a large number of component functions:

with $f_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$. This problem arises in many contexts and applications including regression or more generally parameter estimation problems (where $f_{i}{(x)}$ is the loss function representing the error between the output and the prediction of a parametric model), minimization of an expected value of a function (where the expectation is taken over a finite probability distribution or approximated by an $m$-sample average), machine learning, or distributed optimization over networks.

After characterizing the convergence rate of RR, we look into second-order terms in the asymptotic expansion of the averaged RR iterates and obtain high probability bounds. We use these bounds to develop a new method that can accelerate the convergence rate of RR to $\mathcal{O}{(\frac{1}{k^{2}})}$ with high probability. Finally, we show that the $\mathcal{O}{(\frac{1}{k^{2}})}$ rate can also be achieved in expectation (which is a weaker notion of convergence with respect to convergence with high probability) for the $s = 1$ case by adjusting the stepsize to the strong convexity constant of the objective properly.

Figure 2: Comparison of RR, Debiased-RR (DRR) and SGD when component functions are random quadratics with m = 50, n = 20 and with simulation time 0.5 seconds over 500 sample paths. Top, left: Histograms of distk for RR, DRR and SGD. Bottom, left: Histograms of distk for RR and DRR only (without SGD). Top, right: Histograms of the suboptimality in objective value for RR, DRR and SGD. Bottom, right: Histograms of the suboptimality in objective value for RR and DRR only (without SGD).
Figure 3: Comparison of RR, De-biased-RR (DRR) and SGD. The simulation framework and parameters are the same as those in Fig....

A consequence of Lemma B.3 proved in the Appendix is that

We also observe that the cycle gradient error $E_{k}$ given by consists of the sum of two terms: The first term is $\mathcal{O}{(\alpha_{k})}$ and is independent over the cycles as the permutations $\sigma_{k}$ are independent and identically distributed whereas the second term is of smaller (second) order as $x_{0}^{j}\rightarrow 0$....
