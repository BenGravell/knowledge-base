Near-optimal Local Convergence of Alternating Gradient Descent-Ascent for Minimax Optimization

Topics include Gradient descent, Optimization, SCSC, IQC.

Smooth minimax games often proceed by simultaneous or alternating gradient updates. Although algorithms with alternating updates are commonly used in practice, the majority of existing theoretical analyses focus on simultaneous algorithms for convenience of analysis. In this paper, we study alternating gradient descent-ascent (Alt-GDA) in minimax games and show that Alt-GDA is superior to its simultaneous counterpart~(Sim-GDA) in many settings. We prove that Alt-GDA achieves a near-optimal local convergence rate for strongly convex-strongly concave (SCSC) problems while Sim-GDA converges at a much slower rate. To our knowledge, this is the first result of any setting showing that Alt-GDA converges faster than Sim-GDA by more than a constant. We further adapt the theory of integral quadratic constraints (IQC) and show that Alt-GDA attains the same rate globally for a subclass of SCSC minimax problems. Empirically, we demonstrate that alternating updates speed up GAN training significantly and the use of optimism only helps for simultaneous algorithms.

## INTRODUCTION

Since the seminal work of von Neumann, minimax optimization in the form of ${\min_{\mathbf{x}}{\max_{\mathbf{y}}f}}{(\mathbf{x},\mathbf{y})}$ has been a major focus of research in mathematics, economics and computer science. Recently, minimax optimization has gained tremendous attention in machine learning as it offers a flexible paradigm that goes beyond ordinary loss function minimization. In particular, there is an increasing set of models that can be formulated as minimax problems, including (but not limited to) generative adversarial networks, adversarial training, robust optimization and primal-dual reinforcement learning.

The most natural and frequently used method for solving minimax problems is a generalization of gradient descent known as gradient descent-ascent (GDA), with either simultaneous or alternating updates of the two players, referred to as Sim-GDA and Alt-GDA, respectively, throughout the sequel. Unlike gradient descent, which converges to a local minimum for minimization problems under a broad range of conditions, it is known that GDA with constant step-sizes can fail to converge for general smooth functions, even for unconstrained bilinear games.

Our contributions. In this paper, we take a step towards understanding Alt-GDA and closing the gap between theory and practice. We first revisit the convergence properties of Alt-GDA in bilinear games for completeness. We then discuss our main contributions on proving near-optimal convergence rates of Alt-GDA.

We show that Alt-GDA can converge with the same rate $\mathcal{O}{(\kappa)}$ globally for a class of SCSC minimax games with a bilinear coupling term. This is done by using theory of IQC to automatically search for a Lyapunov function.

## CONCLUSION

In this paper, we take an important step towards understanding alternating algorithms in minimax optimization by analyzing Alt-GDA in three distinct settings. In particular, we show theoretically that Alt-GDA outperforms its simultaneous counterpart by a big margin in all three settings. Unexpectedly, Alt-GDA achieves a near-optimal convergence rate locally for strongly convex-strongly concave smooth minimax games, matching the known coarse lower bound. Moreover, the acceleration effect of Alt-GDA remains when the minimax problem has only strong concavity in the dual variables.
