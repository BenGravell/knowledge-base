Path Planning Using Wassertein Distributionally Robust Deep Q-learning

We investigate the problem of risk averse robot path planning using the deep reinforcement learning and distributionally robust optimization perspectives. Our problem formulation involves modelling the robot as a stochastic linear dynamical system, assuming that a collection of process noise samples is available. We cast the risk averse motion planning problem as a Markov decision process and propose a continuous reward function design that explicitly takes into account the risk of collision with obstacles while encouraging the robot's motion towards the goal. We learn the risk-averse robot control actions through Lipschitz approximated Wasserstein distributionally robust deep Q-learning to hedge against the noise uncertainty. The learned control actions result in a safe and risk averse trajectory from the source to the goal, avoiding all the obstacles. Various supporting numerical simulations are presented to demonstrate our proposed approach.

## Introduction

Given the tremendous increase in the computing power, many computationally expensive control theory problems can now be addressed using the deep reinforcement learning approaches. So far, the motion planning problem with uncertainty has been investigated from two different perspectives namely the control theory and the reinforcement learning (RL). When stochastic uncertainties are considered in the problems such as path planning, both the above said approaches resort to the powerful stochastic optimization techniques as in to ensure satisfaction of specifications with high probability.

Risk averse path planning problems emphasize the need for exact propagation of uncertainties. For instance, either the distributions of all the uncertainties or the moments defining the distributions are required to be known in advance or calculated exactly for all time steps to evaluate the risk of obstacle collision as . It is an usual practice to associate a particular distribution to the uncertainty (often Gaussian) just for the sake of tractability. But often in reality, all we have is just a collection of samples of the uncertainty and trying to fit a distribution to it may cause undue risk.

*Contributions:* This article leverages powerful results in deep reinforcement learning theory and distributionally robust optimization to learn control policies for robots to operate in a risk-averse manner in an environment.

we learn safe robot control actions at all the state space positions to infer a trajectory to move from source to goal by avoiding all obstacles. We account for the uncertainty due the robot initial states and the process noise through reward function design and learn the risk averse control actions using approximated Wasserstein distributionally robust $Q$-learning.

we demonstrate our proposed approach using a series of numerical simulations and show the effectiveness of our proposed approach.

## Conclusion

We proposed a path planning using approximated Wasserstein distributionally robust deep Q-learning approach. Through carefully designed reward function, we showed how to learn safe control policy for uncertain robots operating in an environment. Our numerical simulation results demonstrated our proposed approach.\
