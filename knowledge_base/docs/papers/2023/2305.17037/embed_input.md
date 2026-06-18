Distributionally Robust Linear Quadratic Control

Linear-Quadratic-Gaussian (LQG) control is a fundamental control paradigm that is studied in various fields such as engineering, computer science, economics, and neuroscience. It involves controlling a system with linear dynamics and imperfect observations, subject to additive noise, with the goal of minimizing a quadratic cost function for the state and control variables. In this work, we consider a generalization of the discrete-time, finite-horizon LQG problem, where the noise distributions are unknown and belong to Wasserstein ambiguity sets centered at nominal (Gaussian) distributions. The objective is to minimize a worst-case cost across all distributions in the ambiguity set, including non-Gaussian distributions. Despite the added complexity, we prove that a control policy that is linear in the observations is optimal for this problem, as in the classic LQG problem. We propose a numerical solution method that efficiently characterizes this optimal control policy....

## Introduction

The Linear Quadratic Regulator (LQR) is a classic control problem that has served as a building block for numerous applications in engineering and computer science, economics, or neuroscience. It involves controlling a system with linear dynamics and imperfect observations affected by additive noise, with the goal of minimizing a quadratic state and control cost....

Motivated by practical settings where noise distributions may not be readily available or may not be Gaussian, this paper considers a discrete-time, finite-horizon generalization of the LQG setting where noise distributions are unknown and are chosen adversarially from ambiguity sets characterized by a Wasserstein distance and centered around nominal (Gaussian) distributions.

In view of the popularity of LQG models, the results in this work carry important theoretical and practical implications. Despite considering a generalization of the classic LQG setting where the noise affecting the system dynamics and the observations follows unknown (and potentially non-Gaussian) distributions, our findings suggest that certain classic structural results continue to hold and that highly efficient methods can be adapted to tackle this more realistic (and more challenging) problem....

The results also raise several important questions that warrant future exploration. First, it would be highly relevant to consider extensions where the system matrices are also affected by uncertainty, as this captures many applications of practical interest in, e.g., reinforcement learning or revenue management. Second, it would be worth exploring an infinite horizon setting or relaxing the assumption that the nominal distribution is Gaussian, as both assumptions may be limiting the practical appeal of the framework....

As we obtained by restricting the feasible set of the outer maximization problem in, it is clear that ${\underset{¯}{d}}^{\star} \leq d^{\star}$. Next, we show that can be recast as a finite-dimensional zero-sum game. This result critically relies on the following known fact regarding the 2-Wasserstein distance between two normal distributions, which coincides with the Gelbrich distance between their covariance matrices.

### Definition 2 (Gelbrich distance)

The identity $p^{\star} = {\overline{p}}^{\star}$ readily implies that is solved by a causal controller that is linear in the...
