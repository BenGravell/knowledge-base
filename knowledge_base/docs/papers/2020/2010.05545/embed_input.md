Local Search for Policy Iteration in Continuous Control

We present an algorithm for local, regularized, policy improvement in reinforcement learning (RL) that allows us to formulate model-based and model-free variants in a single framework. Our algorithm can be interpreted as a natural extension of work on KL-regularized RL and introduces a form of tree search for continuous action spaces. We demonstrate that additional computation spent on model-based policy improvement during learning can improve data efficiency, and confirm that model-based policy improvement during action selection can also be beneficial. Quantitatively, our algorithm improves data efficiency on several continuous control benchmarks (when a model is learned in parallel), and it provides significant improvements in wall-clock time in high-dimensional domains (when a ground truth model is available). The unified framework also helps us to better understand the space of model-based and model-free algorithms. In particular, we demonstrate that some benefits attributed to model-based RL can be obtained without a model, simply by utilizing more computation.

## Introduction

Stable policy optimization in high-dimensions, and continuous action spaces, can be a challenge even in simulation. In recent years, a variety of deep RL algorithms have been developed, both for the model-free and model-based setting, that aim to tackle this challenge. In continuous control, recent progress on scalable (distributed) algorithms now allows us to solve problems with high-dimensional observation and action spaces end-to-end, provided adequate computation for simulation and learning is available.

In this paper we make an attempt to understand these questions better. In particular we aim to understand how data efficiency and scalability of algorithms for continuous control can be influenced through the use of additional compute during acting or learning. We build on a class of KL-regularized policy iteration schemes that separate acting, policy improvement, and learning and thus allow us to flexibly employ parametric policies, value functions, exact or approximate environment models, and search based methods in combination.

Using our approach we make a number of observations regarding the questions 1)-3) posed above:\
1. The literature on model-free algorithms in continuous control has underestimated their data efficiency. Through additional updates of the policy and value-function (additional compute), we can achieve significant improvements.\
2. At the expense of additional compute a learned predictive model (of rewards and values) can be used during learning for model-based policy optimization; providing a stronger policy improvement operator than a model-free algorithm.\
3.

## Discussion and Related work

Policy optimization schemes based on the KL regularized objective have a long history in the RL and optimal control literature -- see e.g. Kappen; Toussaint & Storkey; Todorov; Rawlik et al. for different perspectives on this objective. A number of different approaches have been considered for its optimization. These include both policy iteration schemes similar to the ones considered in this paper as well as algorithms that optimize the regularized objective that we consider in the E-step, often via some form of regularized policy gradient.
