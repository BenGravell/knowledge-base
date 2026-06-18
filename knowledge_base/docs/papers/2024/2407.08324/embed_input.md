A Cantor-Kantorovich Metric between Markov Decision Processes with Application to Transfer Learning

We extend the notion of Cantor-Kantorovich distance between Markov chains introduced by in the context of Markov Decision Processes (MDPs). The proposed metric is well-defined and can be efficiently approximated given a finite horizon. Then, we provide numerical evidences that the latter metric can lead to interesting applications in the field of reinforcement learning. In particular, we show that it could be used for forecasting the performance of transfer learning algorithms.

## Introduction

Research on quantitative notion of behavioural distance between Markov processes by the reinforcement learning community (see and the references therein) mimics the study of distance between dynamical systems conducted by the control community (see, and the references therein). Both communities are interested in computing *how much processes/dynamical systems differ in terms of their behaviour*. Several metrics have been proposed for Markov Chains (MC) (see ), including the recent Cantor-Kantorovich metric by Banse et al. where they applied it for abstraction-based methods.

It is typical to train a reinforcement learning algorithm in a simpler world modeled as a Markov Decision Process (MDP) and deploy it in a real world setting corresponding to a different MDP. Several Transfer Learning (TL) algorithms have been developed in this paradigm where one transfers a learned policy from one MDP to another in the hope of improving the performance of the latter (see Lazaric et al., Wang et al., Tao et al., Bou Ammar et al. ).

This manuscript extends the range of application of the Cantor-Kantorovich metric proposed by Banse et al. in the context of TL.

The Cantor-Kantorovich metric is formulated in the context of MDPs.

The promising potential of the proposed metric is demonstrated on a transfer learning problem where sources having smaller Cantor-Kantorovich distance with the target are shown to guarantee performance using TL techniques.

Outline: Following a short summary of notations and preliminaries, we present the proposed metric between MDPs in Section. Subsequently, the application to problems in Transfer Learning domain is demonstrated in Section. Finally, the paper is summarised in Section along with the discussion of potential future research directions.

## Conclusion & Future Outlook

In this work, a novel Cantor-Kantorovich metric with reasonable computational complexity was introduced in the context of MDPs. Its applicability to problems in the TL domain was also demonstrated using a simple numerical simulation.

There are several promising and potential research directions for the future. For instance, one could aim for improving the upper bound for accuracy of the proposed Cantor-Kantorovich metric with a finite horizon $N$. Similarly, one could investigate a distance of the form
