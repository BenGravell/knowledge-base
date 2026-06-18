Active Learning for Control-Oriented Identification of Nonlinear Systems

Model-based reinforcement learning is an effective approach for controlling an unknown system. It is based on a longstanding pipeline familiar to the control community in which one performs experiments on the environment to collect a dataset, uses the resulting dataset to identify a model of the system, and finally performs control synthesis using the identified model. As interacting with the system may be costly and time consuming, targeted exploration is crucial for developing an effective control-oriented model with minimal experimentation. Motivated by this challenge, recent work has begun to study finite sample data requirements and sample efficient algorithms for the problem of optimal exploration in model-based reinforcement learning. However, existing theory and algorithms are limited to model classes which are linear in the parameters. Our work instead focuses on models with nonlinear parameter dependencies, and presents the first finite sample analysis of an active learning algorithm suitable for a general class of nonlinear dynamics. In certain settings, the excess control cost of our algorithm achieves the optimal rate, up to logarithmic factors....

## Introduction

In recent years, model-based reinforcement learning has been successfully applied to various application domains including robotics, healthcare, and autonomous driving (Levine et al. Moerland et al., ). These approaches often proceed by performing experiments on a system to collect data, and then using the data to fit models for the dynamics. In the specified application domains, performing experiments requires interaction with the physical world, which can be both costly and time-consuming....

Driven by the empirical success of machine and deep learning in solving classes of complex control problems, the learning and control communities have recently begun revisiting the classical pipeline of identification to control, proposing new algorithms, and analyzing them from a non-asymptotic viewpoint. Early efforts focused on end-to-end control guarantees for unknown linear system under naive exploration (injecting white noise inputs) (Dean et al. Mania et al., ). These methods have also been refined by using active learning to collect better data for control synthesis....

## Conclusions

We have introduced and analyzed the Active Learning for Control-Oriented Identification (ALCOI) algorithm, marking a significant step towards understanding active exploration in model-based reinforcement learning for a general class of nonlinear dynamical systems. We provide finite sample bounds on the excess control cost achieved by the algorithm which offer insight into the interaction between the hardness of control and identification. Our bounds are known to be sharp up to logarithmic factors in the setting of nonlinear dynamical systems with linear dependence on the parameters, and we conjecture that they are sharp in general....

### Definition 2.3 (Lojasiewicz condition, Roulet and d'Aspremont )

to describe the control cost of applying a certainty equivalence policy synthesized using parameter $\phi$ on a system with dynamics described by $\overset{\sim}{\phi}$. It has been shown by Wagenmaker et al. that for models which are linear in the parameters, the gap ${\mathcal{J}_{\phi^{\star}}{(\phi)}} - {\mathcal{J}_{\phi^{\star}}{(\phi^{\star})}}$ is characterized by the squared parameter error weighted by the *model-task Hessian*, defined below.

In light of this, we would like to choose the exploration policy $\pi$ which minimizes this upper bound:
