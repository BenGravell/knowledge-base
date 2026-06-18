How Are Policy Gradient Methods Affected by the Limits of Control?

Topics include Policy gradients, Control, Curse of dimensionality, Gradient method.

We study stochastic policy gradient methods from the perspective of control-theoretic limitations. Our main result is that ill-conditioned linear systems in the sense of Doyle inevitably lead to noisy gradient estimates. We also give an example of a class of stable systems in which policy gradient methods suffer from the curse of dimensionality. Our results apply to both state feedback and partially observed systems.

## Introduction

Reinforcement learning (RL) methods have shown great empirical success in controlling complex dynamical systems Silver et al.. While these methods are promising, we have only begun to understand performance guarantees and fundamental limitations in continuous state and action problems. Providing such guarantees and understanding such limitations is crucial to deploying these methods in safety-critical systems. In this paper, we focus on a particular class of such methods; namely, we seek to understand fundamental limitations for policy gradient methods.

Policy gradient methods are a relatively simple class of algorithms that have been recently analyzed in the context of the linear quadratic regulator (LQR), Fazel et al.; Tu and Recht. The motivation for studying policy gradients in the context of LQR stems from that it serves as an analytically tractable benchmark for RL in continuous state and action spaces. For instance, by direct arguments on can show that control-theoretic parameters affect the hardness of both offline and online learning in LQR Tsiamis and Pappas; Ziemann and Sandberg; Tsiamis et al.....

## Discussion

In this work we showed that estimating policy gradients can become arbitrarily hard due to known control-theoretic fundamental limitations Doyle by leveraging the classic two point method due to Le Cam LeCam. For instance, we showed with system that a partially observed system with small Markov parameters necessarily has noisy policy gradients and that this holds independently of the parametrization. Our bounds also show that learning controllers that are close to marginal stability can be hard. This is similar to what has already been observed for adaptive LQR/LQG in Ziemann and Sandberg. Leveraging results from Tsiamis et al....

### Consequences of Theorem 1

Proposition 1 shows that the global minimax complexity of estimating gradients is infinite. While this shows that estimating gradients can be hard, it does not reveal how this hardness depends on control theoretic parameters.

In other words, there are classes of stable systems for which the policy gradient suffers from exponential complexity in the state dimension.

### Problem Formulation

We are interested in studying how policy gradient methods applied to the linear system
