Quantifying Generalization in Reinforcement Learning

In this paper, we investigate the problem of overfitting in deep reinforcement learning. Among the most common benchmarks in RL, it is customary to use the same environments for both training and testing. This practice offers relatively little insight into an agent's ability to generalize. We address this issue by using procedurally generated environments to construct distinct training and test sets. Most notably, we introduce a new environment called CoinRun, designed as a benchmark for generalization in RL. Using CoinRun, we find that agents overfit to surprisingly large training sets. We then show that deeper convolutional architectures improve generalization, as do methods traditionally found in supervised learning, including L2 regularization, dropout, data augmentation and batch normalization.

## Introduction

Generalizing between tasks remains difficult for state of the art deep reinforcement learning (RL) algorithms. Although trained agents can solve complex tasks, they struggle to transfer their experience to new environments. Agents that have mastered ten levels in a video game often fail catastrophically when first encountering the eleventh. Humans can seamlessly generalize across such similar tasks, but this ability is largely absent in RL agents. In short, agents become overly specialized to the environments encountered during training.

To begin, we train agents on CoinRun, a procedurally generated environment of our own design, and we report the surprising extent to which overfitting occurs. Using this environment, we investigate how several key algorithmic and architectural decisions impact the generalization performance of trained agents.

The

We show that the number of training environments required for good generalization is much larger than the number used by prior work on transfer in RL.

We propose a generalization metric using the CoinRun environment, and we show how this metric provides a useful signal upon which to iterate.

## Discussion

In both CoinRun-Platforms and RandomMazes, agents must learn to leverage recurrence and memory to optimally navigate the environment. The need to memorize and recall past experience presents challenges to generalization unlike those seen in CoinRun. It is unclear how well suited LSTMs are to this task. We empirically observe that given sufficient data and training time, agents using LSTMs eventually converge to a near optimal policy. However, the relatively poor generalization performance raises the question of whether different recurrent architectures might be better suited for generalization in these environments.

## Conclusion

Our results provide insight into the challenges underlying generalization in RL. We have observed the surprising extent to which agents can overfit to a fixed training set. Using the procedurally generated CoinRun environment, we can precisely quantify such overfitting. With this metric, we can better evaluate key architectural and algorithmic decisions. We believe that the lessons learned from this environment will apply in more complex settings, and we hope to use this benchmark, and others like it, to iterate towards more generalizable agents.
