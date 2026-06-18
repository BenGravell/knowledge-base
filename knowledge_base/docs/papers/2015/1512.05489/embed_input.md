Data-driven Inverse Optimization with Imperfect Information

In data-driven inverse optimization an observer aims to learn the preferences of an agent who solves a parametric optimization problem depending on an exogenous signal. Thus, the observer seeks the agent's objective function that best explains a historical sequence of signals and corresponding optimal actions. We focus here on situations where the observer has imperfect information, that is, where the agent's true objective function is not contained in the search space of candidate objectives, where the agent suffers from bounded rationality or implementation errors, or where the observed signal-response pairs are corrupted by measurement noise. We formalize this inverse optimization problem as a distributionally robust program minimizing the worst-case risk that the predicted decision (i.e., the decision implied by a particular candidate objective) differs from the agent's actual response to a random signal....

## Introduction

In inverse optimization an observer aims to learn the preferences of an agent who solves a parametric optimization problem depending on an exogenous signal. The observer knows the constraints imposed on the agent's actions but is unaware of her objective function. By monitoring a sequence of signals and corresponding actions, the observer seeks to identify an objective function that makes the observed actions optimal in the agent's optimization problem. This learning problem can be cast as an inverse optimization problem over candidate objective functions....

Inverse optimization has a wide spectrum of applications spanning several disciplines ranging from econometrics and operations research to engineering and biology. For example, a marketing executive aims to understand the purchasing behavior of consumers with unknown utility functions by monitoring sales figures, a transportation planner wishes to learn the route choice preferences of the passengers in a multimodal transport system by measuring traffic flows, or a healthcare manager seeks to design clinically acceptable treatments in view of historical treatment plans....

Table 5 reports the out-of-sample suboptimality and predictability risks, respectively, for the DRO, VI and ERM estimators. The non-parametric VI approach is exclusively used in the presence of model uncertainty, which is the only scenario in which it has a chance to outperform the more parsimonious parametric approaches. Our results show that the DRO estimator consistently attains the lowest suboptimality and predictability risk among all parametric approaches....

Table 5. Data-driven inverse optimization: Out-of-sample suboptimality and predictability risk of the VI, ERM and DRO approaches in different experimental settings

Under the assumptions of Theorem 5.2. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information"), the worst-case risk in (25. ‣ 5. Linear Hypotheses ‣ Data-driven Inverse Optimization with Imperfect Information")) corresponding to a fixed $\theta \in \Theta$ coincides with the optimal value of a finite convex program, i.e.,

Note that if $\varepsilon = 0$ and the empirical distribution is supported on $\Xi$, which is necessarily true in the absence of measurement noise, then the Wasserstein ball ${\mathbb{B}}_{\varepsilon}^{p}{({\hat{\mathbb{P}}}_{N})}$ shrinks...
