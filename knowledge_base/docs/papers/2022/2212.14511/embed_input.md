Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I

Topics include Reinforcement learning, Partial observability, Optimal control, Representation learning, Control, Learning, Linear quadratic Gaussian, Linear quadratic Gaussian control, State space.

We study the task of learning state representations from potentially high-dimensional observations, with the goal of controlling an unknown partially observable system. We pursue a cost-driven approach, where a dynamic model in some latent state space is learned by predicting the costs without predicting the observations or actions. In particular, we focus on an intuitive cost-driven state representation learning method for solving Linear Quadratic Gaussian (LQG) control, one of the most fundamental partially observable control problems. As our main results, we establish finite-sample guarantees of finding a near-optimal state representation function and a near-optimal controller using the directly learned latent model, for finite-horizon time-varying LQG control problems. To the best of our knowledge, despite various empirical successes, finite-sample guarantees of such a cost-driven approach remain elusive. Our result underscores the value of predicting multi-step costs, an idea that is key to our theory, and notably also an idea that is known to be empirically valuable for learning state representations....

## Introduction

We consider state representation learning for control in partially observable systems, inspired by the recent successes of *control from pixels*. Control from pixels is an everyday task for human beings, but it remains challenging for learning agents. Methods to achieve it generally fall into two main categories: *model-free* and *model-based* ones. Model-free methods directly learn a visuomotor policy, also known as direct reinforcement learning (RL)....

In latent-model-based control, the state of the latent model is also referred to as a *state representation* in the deep RL literature, and the mapping from an observed history to a latent state is referred to as the (state) representation function. *Reconstructing the observation* often serves as a supervision for representation learning for control in the empirical RL literature. This is in sharp contrast to model-free methods, where the policy improvement step is completely *cost-driven*....

We examined the cost-driven state representation learning methods in time-varying LQG control. With a finite-sample analysis, we showed that a direct, cost-driven state representation learning algorithm effectively solves LQG. In the analysis, we revealed the importance of using multi-step cumulative costs as the supervision signal, and the dependence on $\ell$, the controllability index, due to early-stage insufficient excitement of the system....

In Part II of this work, we will explore how the cost-driven state representation learning approach performs in the infinite-horizon LTI setting, as well as discuss more opportunities that this work has opened up for future research.

Since $\xi$ is a vector of zero-mean subexponential variables with subexponential norms bounded by $E$, ${\|\xi\|} = {\mathcal{O}{({En^{1/2}{\log{({n/p})}}})}}$. Hence, we have

### Assumption 5

As shown in Lemma 5. ‣ 4.4 Perturbed linear regression bound ‣ 4 Theoretical guarantees and proofs ‣ Cost-Driven Representation Learning for Linear Quadratic Gaussian Control: Part I"), if the input of linear regression does not have full-rank covariance, then the parameters can only be identified in certain directions. The following lemma studies the performance of the certainty equivalent optimal controller in this case.
