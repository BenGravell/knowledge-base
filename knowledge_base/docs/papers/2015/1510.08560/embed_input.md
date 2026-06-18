Why Random Reshuffling Beats Stochastic Gradient Descent

Topics include Gradient descent, Stochastic gradients, RR, Stochastic gradient descent.

We analyze the convergence rate of the random reshuffling (RR) method, which is a randomized first-order incremental algorithm for minimizing a finite sum of convex component functions. RR proceeds in cycles, picking a uniformly random order (permutation) and processing the component functions one at a time according to this order, i.e., at each cycle, each component function is sampled without replacement from the collection. Though RR has been numerically observed to outperform its with-replacement counterpart stochastic gradient descent (SGD), characterization of its convergence rate has been a long standing open question. In this paper, we answer this question by showing that when the component functions are quadratics or smooth and the sum function is strongly convex, RR with iterate averaging and a diminishing stepsize alpha_k = Theta(1/k^(s)) for s in (1/2, 1) converges at rate Theta(1/k^s) with probability one in the suboptimality of the objective value, thus improving upon the Omega(1/k) rate of SGD.

## Introduction: First-order incremental methods

We

with $f_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$. This problem arises in many contexts and applications including regression or more generally parameter estimation problems (where $f_{i}{(x)}$ is the loss function representing the error between the output and the prediction of a parametric model), minimization of an expected value of a function (where the expectation is taken over a finite probability distribution or approximated by an $m$-sample average), machine learning, or distributed optimization over networks.

Intuitively, it is clear that slow progress can be obtained if the functions that are processed consecutively have gradients close to zero. Indeed, the performance of IG is known to be pretty sensitive to the order functions are processed \[6, Example 2.1.3\].

where $\alpha_{k} > 0$ is a stepsize. We set $x_{0}^{k + 1} = x_{m}^{k}$ as before and refer to $\{ x_{0}^{k}\}$ as the outer iterates. This method is called the Random Reshuffling (RR) method \[6, Section 2.1\] and will be the focus of this paper.

## Conclusion

We analyzed the random reshuffling (RR) method for minimizing a finite sum of convex component functions. When the objective function is strongly convex and the component functions are smooth, averaged RR iterates converge at rate $\sim {1/k^{s}}$ to the optimal solution almost surely (which translates into a rate of $1/k^{2s}$ in the suboptimality of the objective value) for a diminishing stepsize $\alpha_{k} = {\Theta{({1/k^{s}})}}$ with $s \in {({1/2},1)}$. This is faster than SGD's $\Omega{(\frac{1}{k})}$ rate.

After characterizing the convergence rate of RR, we look into second-order terms in the asymptotic expansion of the averaged RR iterates and obtain high probability bounds. We use these bounds to develop a new method that can accelerate the convergence rate of RR to $\mathcal{O}{(\frac{1}{k^{2}})}$ with high probability. Finally, we show that the $\mathcal{O}{(\frac{1}{k^{2}})}$ rate can also be achieved in expectation (which is a weaker notion of convergence with respect to convergence with high probability) for the $s = 1$ case by adjusting the stepsize to the strong convexity constant of the objective properly.
