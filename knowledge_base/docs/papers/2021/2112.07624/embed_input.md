Interaction-Aware Trajectory Prediction and Planning for Autonomous Vehicles in Forced Merge Scenarios

Merging is, in general, a challenging task for both human drivers and autonomous vehicles, especially in dense traffic, because the merging vehicle typically needs to interact with other vehicles to identify or create a gap and safely merge into. In this paper, we consider the problem of autonomous vehicle control for forced merge scenarios. We propose a novel game-theoretic controller, called the Leader-Follower Game Controller (LFGC), in which the interactions between the autonomous ego vehicle and other vehicles with a priori uncertain driving intentions is modeled as a partially observable leader-follower game. The LFGC estimates the other vehicles' intentions online based on observed trajectories, and then predicts their future trajectories and plans the ego vehicle's own trajectory using Model Predictive Control (MPC) to simultaneously achieve probabilistically guaranteed safety and merging objectives. To verify the performance of LFGC, we test it in simulations and with the NGSIM data, where the LFGC demonstrates a high success rate of 97.5% in merging.

## Introduction

Advances in autonomous vehicle technologies are projected to reduce vehicle crashes and fatalities, improve mobility especially for elderly and disabled people, improve fuel economy and emission control, and to promote more efficient land uses. Despite these benefits, there are still many challenges that need to be addressed to deliver a highly (level 4 or level 5) autonomous vehicle....

Figure 1: The autonomous vehicle (blue) needs to merge onto the highway before the on-ramp section ends. In dense traffic, there may not be a sufficient gap for the autonomous vehicle to merge into. In this case, the autonomous vehicle needs to force the other vehicles to cooperate and let it cut in. However, interacting vehicles that are aware of the autonomous vehicle’s merging attempt (red) may choose to proceed or yield depending on their intentions.

## Summary

In this paper, we proposed a Leader-Follower Game Controller (LFGC) for autonomous vehicle planning and control in merge scenarios. The LFGC treats interaction uncertainties due to different driver intentions as latent variables, estimates on-board other driver intentions, and chooses actions to facilitate ego vehicle's merge. In particular, the LFGC is able to perform a receding horizon optimization subject to an explicit probabilistic safety characterization i.e., subject to constraints representing vehicle safety requirements....

The ego vehicle is assumed to have a prior belief on $\sigma$, denoted as ${\mathbb{P}}{({\sigma = l})}$, with $l \in L = {\{\text{leader},\text{follower}\}}$. Then based on all previous traffic states and on all actions taken by the ego vehicle,

During a highway forced merge process, the merging vehicle (ego vehicle) interacts with other vehicles driving in the target lane, who may choose to proceed or yield to the merging vehicle depending on the traffic situation and individual driver's preference. In this paper, we consider a game-theoretic model based on pairwise leader-follower interactions, called a leader-follower game, to represent drivers' cooperation intentions and their resulting vehicle behaviors....

The major differences between and are the following: 1) $\{ u_{t}^{1},u_{t + 1}^{1},\ldots,u_{{t + N} - 1}^{1}\}$ presented in are unknown, while in, they are obtained based on trained policy from the imitation learning; 2) The maximization of the...
