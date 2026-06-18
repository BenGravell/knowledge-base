Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning

Topics include Reinforcement learning, Uncertainty, Sample complexity, Control, Learning.

Recent model-free reinforcement learning algorithms have proposed incorporating learned dynamics models as a source of additional data with the intention of reducing sample complexity. Such methods hold the promise of incorporating imagined data coupled with a notion of model uncertainty to accelerate the learning of continuous control tasks. Unfortunately, they rely on heuristics that limit usage of the dynamics model. We present model-based value expansion, which controls for uncertainty in the model by only allowing imagination to fixed depth. By enabling wider use of learned dynamics models within a model-free reinforcement learning algorithm, we improve value estimation, which, in turn, reduces the sample complexity of learning.

## Introduction

Recent progress in model-free (MF) reinforcement learning has demonstrated the capacity of rich value function approximators to master complex tasks. However, these model-free approaches require access to an impractically large number of training interactions for most real-world problems. In contrast, model-based (MB) methods can quickly arrive at near-optimal control with learned models under fairly restricted dynamics classes....

The MF and MB approaches have distinct strengths and weaknesses: expressive value estimation MF methods can achieve good asymptotic performance but have poor sample complexity, while MB methods exhibit efficient learning but struggle on complex tasks. In this paper, we seek to *reduce sample complexity while supporting complex non-linear dynamics by combining MB and MF learning techniques through disciplined model use for value estimation*.

Existing approaches following a general Dyna-like approach to using imagination rollouts for improvement of model-free value estimates either use stale data in an imagination buffer or use the model to imagine past horizons where the prediction is accurate. Multiple heuristics have been proposed to reduce model usage to combat such problems, but these techniques generally involve a complex combination of uncertainty estimation and additional hyperparameters and may not always appropriately restrict model usage to reasonable horizon lengths....

Our work justifies further exploration in model use for model-free sample complexity reduction. In particular, estimating uncertainty in the dynamics model explicitly would enable automatic selection of $H$. To deal with sparse reward signals, we also believe it is important to consider exploration with the model, not just refinement of value estimates. Finally, MVE admits extensions into domains with probabilistic dynamics models and stochastic policies via Monte Carlo integration over imagined rollouts.

Since we do not have access to the true MSE of $\hat{V}$, we minimize its Bellman error with respect to $\nu$, using this error as a proxy. In this context, using a target ${\hat{V}}_{k}{({\hat{s}}_{T})}$ is equivalent to training $\hat{V}$ with imagined TD-$k$ error. This TD-$k$ trick enables us to skirt the distribution mismatch problem to the extent that $\nu$ is an approximate fixed point....
