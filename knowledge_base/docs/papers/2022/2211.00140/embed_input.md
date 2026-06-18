A Damped Newton Method Achieves Global O(1/k^2) and Local Quadratic Convergence Rate

In this paper, we present the first stepsize schedule for Newton method resulting in fast global and local convergence guarantees. In particular, a) we prove an O( frac 1 k^ ) global rate, which matches the state-of-the-art global rate of cubically regularized Newton method of Polyak and Nesterov and of regularized Newton method of Mishchenko and Doikov and Nesterov, b) we prove a local quadratic rate, which matches the best-known local rate of second-order methods, and c) our stepsize formula is simple, explicit, and does not require solving any subproblem. Our convergence proofs hold under affine-invariance assumptions closely related to the notion of self-concordance. Finally, our method has competitive performance when compared to existing baselines, which share the same fast global convergence guarantees.

### Introduction

Second-order optimization methods are the backbone of much of industrial and scientific computing. With origins that can be tracked back several centuries to the pioneering works of Newton (Newton, 1687), Raphson (Raphson, 1697) and Simpson (Simpson, 1740), they were extensively studied, generalized, modified, and improved in the last century. For a review of the historical development of the classical Newton-Raphson method, we refer the reader to the work of Ypma. The number of extensions and applications of second-order optimization methods is enormous; for example, the survey of Conn et al....

### Second-order methods and modern machine learning

For second part we solve the following minimization problem:

This function is a lower bound for a class of functions with Lipschitz continuous Hessian (4 and Local Quadratic Convergence Rate")) with additional regularization. In Figure 2 and Local Quadratic Convergence Rate"), we take $d = 20$, $x_{0} = 0$ (equal to all zeroes). Parameters $L_{\text{est}},L_{2},\alpha$ are fine-tuned to largest values having monotone decrease in reported metrics: $L_{\text{est}} = 662$ $L_{2} = 0.662$, $\alpha = 0.0172$....

### Significance for algorithms

Improvement: Avoiding latter subroutine yields theoretical improvements. If we compute matrix inverses naively, iteration cost of AICN is $\mathcal{O}{(d^{3})}$ (where $d$ is a dimension of the problem), which is improvement over $\mathcal{O}{({d^{3}{\log\varepsilon^{- 1}}})}$ iteration cost of Cubic Newton.

### Lemma 2

Despite the rich history of the field, research on second-order methods has been flourishing up to this day. Some of the most recent development in the area was motivated by the needs of modern machine learning. Data-oriented machine learning depends on large datasets (both in number of features and number of datapoints), which are often stored in distributed/decentalized fashion. Consequently, there is a need for scalable algorithms.

To tackle large number of features, Qu et al.; Gower et al.; Doikov and Richtárik and Hanzely et al. proposed variants of Newton method operating in random low-dimensional subspaces. On the other hand, Pilanci and Wainwright; Xu et al. and Kovalev et al. developed subsampled Newton methods for solving empirical risk minimization (ERM) problems with large training datasets....
