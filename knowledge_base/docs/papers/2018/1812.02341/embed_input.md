Quantifying Generalization in Reinforcement Learning

In this paper, we investigate the problem of overfitting in deep reinforcement learning. Among the most common benchmarks in RL, it is customary to use the same environments for both training and testing. This practice offers relatively little insight into an agent's ability to generalize. We address this issue by using procedurally generated environments to construct distinct training and test sets. Most notably, we introduce a new environment called CoinRun, designed as a benchmark for generalization in RL. Using CoinRun, we find that agents overfit to surprisingly large training sets. We then show that deeper convolutional architectures improve generalization, as do methods traditionally found in supervised learning, including L2 regularization, dropout, data augmentation and batch normalization.

## Introduction

Generalizing between tasks remains difficult for state of the art deep reinforcement learning (RL) algorithms. Although trained agents can solve complex tasks, they struggle to transfer their experience to new environments. Agents that have mastered ten levels in a video game often fail catastrophically when first encountering the eleventh. Humans can seamlessly generalize across such similar tasks, but this ability is largely absent in RL agents. In short, agents become overly specialized to the environments encountered during training.

That RL agents are prone to overfitting is widely appreciated, yet the most common RL benchmarks still encourage training and evaluating on the same set of environments. We believe there is a need for more metrics that evaluate generalization by explicitly separating training and test environments. In the same spirit as the Sonic Benchmark, we seek to better quantify an agent's ability to generalize.

## Conclusion

Our results provide insight into the challenges underlying generalization in RL. We have observed the surprising extent to which agents can overfit to a fixed training set. Using the procedurally generated CoinRun environment, we can precisely quantify such overfitting. With this metric, we can better evaluate key architectural and algorithmic decisions. We believe that the lessons learned from this environment will apply in more complex settings, and we hope to use this benchmark, and others like it, to iterate towards more generalizable agents.

It is likely that further architectural tuning could yield even greater generalization performance. As is common in supervised learning, we expect much larger networks to have a higher capacity for generalization. In our experiments, however, we noticed diminishing returns increasing the network size beyond IMPALA-Large, particularly as wall clock training time can dramatically increase. In any case, we leave further architectural investigation to future work.

Using the CoinRun environment, we can measure how successfully agents generalize from a given set of training levels to an unseen set of test levels. Train and test levels are drawn from the same distribution, so the gap between train and test performance determines the extent of overfitting....
