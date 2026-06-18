Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning

Topics include Reinforcement learning, Uncertainty, Sample complexity, Control, Learning.

Recent model-free reinforcement learning algorithms have proposed incorporating learned dynamics models as a source of additional data with the intention of reducing sample complexity. Such methods hold the promise of incorporating imagined data coupled with a notion of model uncertainty to accelerate the learning of continuous control tasks. Unfortunately, they rely on heuristics that limit usage of the dynamics model. We present model-based value expansion, which controls for uncertainty in the model by only allowing imagination to fixed depth. By enabling wider use of learned dynamics models within a model-free reinforcement learning algorithm, we improve value estimation, which, in turn, reduces the sample complexity of learning.

## Introduction

Recent progress in model-free (MF) reinforcement learning has demonstrated the capacity of rich value function approximators to master complex tasks. However, these model-free approaches require access to an impractically large number of training interactions for most real-world problems. In contrast, model-based (MB) methods can quickly arrive at near-optimal control with learned models under fairly restricted dynamics classes.

The MF and MB approaches have distinct strengths and weaknesses: expressive value estimation MF methods can achieve good asymptotic performance but have poor sample complexity, while MB methods exhibit efficient learning but struggle on complex tasks. In this paper, we seek to *reduce sample complexity while supporting complex non-linear dynamics by combining MB and MF learning techniques through disciplined model use for value estimation*.

We present model-based value expansion (MVE), a hybrid algorithm that uses a dynamics model to simulate the short-term horizon and Q-learning to estimate the long-term value beyond the simulation horizon. This improves Q-learning by providing higher-quality target values for training. Splitting value estimates into a near-future MB component and a distant-future MF component offers a model-based value estimate that creates a decoupled interface between value estimation and model use and does not require differentiable dynamics.

## Conclusion

In this paper, we introduce the model-based value expansion (MVE) method, an algorithm for incorporating predictive models of system dynamics into model-free value function estimation. Our approach provides for improved sample complexity on a range of continuous action benchmark tasks, and our analysis illuminates some of the design decisions that are involved in choosing how to combine model-based predictions with model-free value function learning.
