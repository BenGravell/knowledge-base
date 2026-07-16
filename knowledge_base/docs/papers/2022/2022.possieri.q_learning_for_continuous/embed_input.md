<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Q-Learning for Continuous-Time Linear Systems: A Data-Driven Implementation of the Kleinman Algorithm

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A data-driven strategy to estimate the optimal feedback and the value function in an infinite-horizon, continuous-time, linear-quadratic optimal control problem for an unknown system is proposed. The method permits the construction of the optimal policy without any knowledge of the model, without requiring that the time derivatives of the state are available for the design, and without even assuming that an initial stabilizing feedback policy is available. Two alternative architectures are discussed: the first scheme revolves around the periodic computation of some matrix inversions involving the Q-function, whereas the second approach relies on a purely continuous-time implementation of some dynamic systems whose trajectories are uniformly attracted by the solutions to the above algebraic equations. Interestingly, the proposed strategy essentially constitutes a (direct) data-driven implementation of the celebrated Kleinman algorithm, hence subsuming the particularly appealing features of the latter, such as quadratic monotone convergence to the optimal solution. The theory is then validated by the means of practically motivated applications.
