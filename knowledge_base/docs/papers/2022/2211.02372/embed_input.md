Path Planning Using Wassertein Distributionally Robust Deep Q-learning

We investigate the problem of risk averse robot path planning using the deep reinforcement learning and distributionally robust optimization perspectives. Our problem formulation involves modelling the robot as a stochastic linear dynamical system, assuming that a collection of process noise samples is available. We cast the risk averse motion planning problem as a Markov decision process and propose a continuous reward function design that explicitly takes into account the risk of collision with obstacles while encouraging the robot's motion towards the goal. We learn the risk-averse robot control actions through Lipschitz approximated Wasserstein distributionally robust deep Q-learning to hedge against the noise uncertainty. The learned control actions result in a safe and risk averse trajectory from the source to the goal, avoiding all the obstacles. Various supporting numerical simulations are presented to demonstrate our proposed approach.

## Introduction

Given the tremendous increase in the computing power, many computationally expensive control theory problems can now be addressed using the deep reinforcement learning approaches. So far, the motion planning problem with uncertainty has been investigated from two different perspectives namely the control theory and the reinforcement learning (RL). When stochastic uncertainties are considered in the problems such as path planning, both the above said approaches resort to the powerful stochastic optimization techniques as in to ensure satisfaction of specifications with high probability....

Risk averse path planning problems emphasize the need for exact propagation of uncertainties. For instance, either the distributions of all the uncertainties or the moments defining the distributions are required to be known in advance or calculated exactly for all time steps to evaluate the risk of obstacle collision as in. It is an usual practice to associate a particular distribution to the uncertainty (often Gaussian) just for the sake of tractability. But often in reality, all we have is just a collection of samples of the uncertainty and trying to fit a distribution to it may cause undue risk....

## Conclusion

We proposed a path planning using approximated Wasserstein distributionally robust deep Q-learning approach. Through carefully designed reward function, we showed how to learn safe control policy for uncertain robots operating in an environment. Our numerical simulation results demonstrated our proposed approach.\

By knowing the state of the robot $x_{k}$, the full state $s_{k}$ can be obtained by using the positions of the goal and obstacles of the current environment (which do not depend on the position of the robot), since these stay constant during an episode. For ease of notation, we refer to the next state $s_{k + 1}$ as $s^{\prime}$, and the samples of $s^{\prime}$ obtained from, are denoted as ${\hat{s}}^{\prime{(i)}}$ for $i = {1,{\ldotsN}}$. Then, the empirical distribution is given by ${\hat{\mathbb{P}}}_{s^{\prime}} = {\frac{1}{N}{\sum\limits_{i = 1}^{N}\delta_{{\hat{s}}^{\prime{(i)}}}}}$....

where $\mathbf{r}_{\mathbf{t}\mathbf{r}\mathbf{a}\mathbf{v}\mathbf{e}\mathbf{l}}$ is the travel penalty, $\mathbf{r}_{\mathbf{g}\mathbf{o}\mathbf{a}\mathbf{l}}$ is the reward for reaching the goal, and...
