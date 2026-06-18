A Cantor-Kantorovich Metric between Markov Decision Processes with Application to Transfer Learning

We extend the notion of Cantor-Kantorovich distance between Markov chains introduced by in the context of Markov Decision Processes (MDPs). The proposed metric is well-defined and can be efficiently approximated given a finite horizon. Then, we provide numerical evidences that the latter metric can lead to interesting applications in the field of reinforcement learning. In particular, we show that it could be used for forecasting the performance of transfer learning algorithms.

## Introduction

Research on quantitative notion of behavioural distance between Markov processes by the reinforcement learning community (see and the references therein) mimics the study of distance between dynamical systems conducted by the control community (see, and the references therein). Both communities are interested in computing *how much processes/dynamical systems differ in terms of their behaviour*. Several metrics have been proposed for Markov Chains (MC) (see ), including the recent Cantor-Kantorovich metric by Banse et al. where they applied it for abstraction-based methods....

It is typical to train a reinforcement learning algorithm in a simpler world modeled as a Markov Decision Process (MDP) and deploy it in a real world setting corresponding to a different MDP. Several Transfer Learning (TL) algorithms have been developed in this paradigm where one transfers a learned policy from one MDP to another in the hope of improving the performance of the latter (see Lazaric et al., Wang et al., Tao et al., Bou Ammar et al. ). Many works have shown numerical evidences that TL algorithms have better performances when the source and target MDPs are similar to each other (see Song et al., Carroll and Seppi, Zhu et al....

There are several promising and potential research directions for the future. For instance, one could aim for improving the upper bound for accuracy of the proposed Cantor-Kantorovich metric with a finite horizon $N$. Similarly, one could investigate a distance of the form

where $\mathbf{d}_{r}$ is a distance between the rewards of $M_{1}$ and $M_{2}$. The choice of $\mathbf{d}_{r},\alpha$ and $\beta$ would therefore depend on the application context. For example, one could investigate the distances described in. In the same fashion as Carroll and Seppi, one could apply such distances to the same grid-world example as above, but where the goal is moving. Finally, it would be interesting to investigate other performance measures than the jumpstart reward to evaluate the performance of the proposed metric in the transfer learning setting.

### Theorem 1

A Markov Decision Process is described using a tuple $M = {(\mathcal{S},\mathcal{U},\mathcal{T},R,\mu)}$, where $\mathcal{S}$ is the set of *states*, $\mathcal{U}$ is the set of *control actions*, $\mathcal{T}$ is the conditional stochastic kernel that assigns to each state $s...
