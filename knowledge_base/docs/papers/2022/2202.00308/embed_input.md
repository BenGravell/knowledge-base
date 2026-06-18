PAGE-PG: A Simple and Loopless Variance-Reduced Policy Gradient Method with Probabilistic Gradient Estimation

Topics include Policy gradients, Supervised learning, Probabilistic models, Sample complexity, Control, Learning, Sampling, PAGE-PG.

Despite their success, policy gradient methods suffer from high variance of the gradient estimate, which can result in unsatisfactory sample complexity. Recently, numerous variance-reduced extensions of policy gradient methods with provably better sample complexity and competitive numerical performance have been proposed. After a compact survey on some of the main variance-reduced REINFORCE-type methods, we propose ProbAbilistic Gradient Estimation for Policy Gradient (PAGE-PG), a novel loopless variance-reduced policy gradient method based on a probabilistic switch between two types of updates. Our method is inspired by the PAGE estimator for supervised learning and leverages importance sampling to obtain an unbiased gradient estimator. We show that PAGE-PG enjoys a O( epsilon^(-3) ) average sample complexity to reach an epsilon-stationary solution, which matches the sample complexity of its most competitive counterparts under the same setting. A numerical evaluation confirms the competitive performance of our method on classical control tasks.

## Introduction

Policy gradient methods have proved to be really effective in many challenging deep reinforcement learning (RL) applications. Their success is also due to their versatility as they are applicable to any differentiable policy parametrization, including complex neural networks, and they admit easy extensions to model-free settings and continuous state and action spaces. This class of methods has a long history in the RL literature that dates back to, but only very recent work has characterized their theoretical properties, such as convergence to a globally optimal solution and sample and iteration complexity.

In this work, we focus on variance-reduced extensions of REINFORCE-type methods, such as REINFORCE, GPOMDP and their variants with baseline. After reviewing the principal variance-reduced extensions of REINFORCE-type methods, we introduce a novel variance-reduced policy gradient method, PAGE-PG, based on the recently proposed PAGE estimator for supervised learning. We prove that PAGE-PG only takes $\mathcal{O}\left( \epsilon^{- 3} \right)$ trajectories on average to achieve an $\epsilon$-stationary policy, which translates into a near-optimal solution for gradient dominated objectives.

Main contributions. Our main contributions are summarized below.

We propose PAGE-PG, a novel loopless variance-reduced extension of REINFORCE-type methods based on a probabilistic update.

We show that PAGE-PG enjoys a fast rate of convergence and achieves an $\epsilon$-stationary policy within $\mathcal{O}\left( \epsilon^{- 3} \right)$ trajectories on average. We further show that, with gradient dominated objectives, similar results are valid for near-optimal solutions.
