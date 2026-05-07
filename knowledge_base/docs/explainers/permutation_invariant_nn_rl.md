# Permutation-Invariant Neural Networks for Reinforcement Learning

*Work by Yujin Tang and David Ha at Google Brain*

## Summary

In this [2021 NeurIPS conference paper](https://arxiv.org/abs/2109.02869) conference, researchers at Google Brain created a reinforcement learning (RL) agent that uses a collection of sensory neural networks trained on segments of the observation space and uses an attention mechanism to communicate information between the sensory networks. The [interactive demo](https://attentionneuron.github.io/) shows that an agent trained to balance a cartpole (the [CartPoleSwingUpHarder environment](https://github.com/worldanon/learntopredict/blob/master/cartpole/cartpole_swingup_harder.py)) can continue to succeed at its task *even when the order of the observations is permuted during operation in real time* – very impressive! The other videos show similar performance on the PyBullet Ant robot environment and simple videogame environments.

## Robustness without domain randomization

Allow me to address an important concept in RL that will make the performance of these agents even more remarkable and perhaps surprising.

Perhaps the most persistent and onerous concern in data-driven control is **robustness to uncertainty**. Uncertainties can arise due to inherent time-varying randomness in the environment, as well as (nearly-)static changes in the environment which manifest as distribution shift in data observed by a controller.

A [standard trick in RL](https://arxiv.org/abs/1703.06907) to promote robustness is [**domain randomization**](https://lilianweng.github.io/lil-log/2019/05/05/domain-randomization.html). In this procedure, [certain aspects of the environment](https://arxiv.org/abs/1910.10537) are changed during training of a control policy. In so doing, the learner is exposed to a wider variety of situations, which are presumed to somehow make the learner “aware” of the potential uncertainties that exist and hence learns a policy that accounts for these uncertainties.

The simplest optimal control task is linear quadratic regulation (LQR), [which has been argued](http://www.argmin.net/2018/02/08/lqr/) as the natural starting point for analysis of learning-based control:

> [“If a machine learning algorithm does crazy things when restricted to linear models, it’s going to do crazy things on complex nonlinear models too.” - Ben Recht](https://www.argmin.net/2018/02/05/linearization/)

Analogously, I argue that multiplicative noise (aka stochastic system parameters) is the simplest type of domain randomization for learning-based control. [CONLab](https://labs.utdallas.edu/conlab) has extensively studied the properties of [linear systems with multiplicative noise in learning-based control](https://labs.utdallas.edu/conlab/learning-robust-control-for-lqr-systems-with-multiplicative-noise-via-policy-gradient/), and established both [theoretically](https://arxiv.org/abs/2004.08019) and [empirically](https://labs.utdallas.edu/conlab/robust-learning-based-control-via-bootstrapped-multiplicative-noise/) that designing (training) controllers in the presence of multiplicative noise does indeed produce robustness of stability to parameter uncertainty.

What is amazing about Google Brain’s permutation-invariant agents is that they achieve permutation-invariance *without the need for domain randomization*; during training, the order of the observations was kept constant, and only at test time was the observation ordering permuted. In fact, the permutation-invariance is explicitly considered through the design of the attention mechanism, which merges the outputs of the sensory neurons in a permutation-invariant way. This suggests that the need for domain randomization during training can be obviated if the form of the domain uncertainty is known ahead of time and can be designed into the control policy architecture.

## A parting question

I leave the reader with a natural follow-on question:

> Is there an analogous way to design a control policy architecture that is robust to system parameter uncertainties without the need for domain randomization during training?

## Links

- [2021 NeurIPS conference paper](https://arxiv.org/abs/2109.02869)
- [Interactive demo](https://attentionneuron.github.io/)
- [TwoMinutePapers video](https://youtu.be/BS2la3C-TYc)
