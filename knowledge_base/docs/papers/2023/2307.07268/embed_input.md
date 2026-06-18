An Online Learning Analysis of Minimax Adaptive Control

We present an online learning analysis of minimax adaptive control for the case where the uncertainty includes a finite set of linear dynamical systems. Precisely, for each system inside the uncertainty set, we define the model-based regret by comparing the state and input trajectories from the minimax adaptive controller against that of an optimal controller in hindsight that knows the true dynamics. We then define the total regret as the worst case model-based regret with respect to all models in the considered uncertainty set. We study how the total regret accumulates over time and its effect on the adaptation mechanism employed by the controller. Moreover, we investigate the effect of the disturbance on the growth of the regret over time and draw connections between robustness of the controller and the associated regret rate.

## Introduction

The interplay between machine learning, system identification and adaptive control has unveiled a fertile area of research which has the potential to answer some of the standing research questions in the field of learning-based control. Recent advances in online learning techniques have provided new perspectives on the design of algorithms where unknown systems can be controlled by acquiring knowledge through repeated interactions with the unknown environment Hazan & Singh. This has close connections with adaptive control Astrom & Wittenmark and in general with learning-based control techniques Benosman.

We provide a detailed analysis for the minimax adaptive control algorithm proposed in Rantzer with the aim to improve our understanding on the role of the adaptation mechanism and the adversary disturbance on the regret. Since an explicit expression for the optimal minimax adaptive controller is not known, we apply our analysis to the candidate sub-optimal minimax adaptive control algorithm^11^1The distinction between the optimal and the sub-optimal minimax adaptive control policies will be made clear at appropriate places. developed in Rantzer; Cederberg et al..

Definition of the: model-based regret corresponding to a specific model in the uncertainty set characterizing the accumulated cost with respect to an optimal controller in hindsight which knows the true dynamics; total regret as the worst-case model-based regret corresponding to any model in the uncertainty set.

Despite the possible difficulty in the identification of the true dynamics, we show that the minimax adaptive controller enjoys a sub-linear regret rate with respect to the best $\mathcal{H}_{\infty}$ controller in hindsight (Theorem 2).

## Conclusion

An online learning-inspired analysis for a recently proposed solution for a class of minimax adaptive control problems has been presented. Model-based regret and total regret for the minimax adaptive control policy were defined by comparing the state and input trajectories against that of the optimal $\mathcal{H}_{\infty}$ controller in hindsight (i.e. having knowledge of the true system dynamics). One of the highlights of the analysis is that the total regret is sub-linear for exogenous disturbances in the $\ell_{2}$ space, confirming links between system theoretic properties and regret for control systems.
