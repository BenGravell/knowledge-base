Error Propagation for Approximate Policy and Value Iteration

Topics include Approximate dynamic programming, Policy iteration, Value iteration, Error propagation, Reinforcement learning, Bellman residuals.

Quantifies how per-iteration approximation errors and Bellman residuals propagate through approximate policy and value iteration. The paper refines earlier worst-case analyses by using concentrability-style distribution terms rather than only supremum error bounds.

We address the question of how the approximation error/Bellman residual at each iteration of the Approximate Policy/Value Iteration algorithms influences the quality of the resulted policy. We quantify the performance loss as the Lp norm of the approximation error/Bellman residual at each iteration. Moreover, we show that the performance loss depends on the expectation of the squared Radon-Nikodym derivative of a certain distribution rather than its supremum, as opposed to what has been suggested by the previous results. Also our results indicate that the contribution of the approximation/Bellman error to the performance loss is more prominent in the later iterations of API/AVI, and the effect of an error term in the earlier iterations decays exponentially fast.
