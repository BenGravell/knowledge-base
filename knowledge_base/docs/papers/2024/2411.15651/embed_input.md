Model Predictive Trees: Sample-Efficient Receding Horizon Planning with Reusable Tree Search

Topics include Model predictive control, Tree search, Monte Carlo tree search, Receding horizon planning, Motion planning, Robotics, Sample efficiency.

Proposes reusing the entire optimal subtree (not just the best trajectory) across receding horizon planning steps, enabling simultaneous refinement toward better solutions and away from worse ones.

We present Model Predictive Trees (MPT), a receding horizon tree search algorithm that improves its performance by reusing information efficiently. Whereas existing solvers reuse only the highest-quality trajectory from the previous iteration as a "hotstart", our method reuses the entire optimal subtree, enabling the search to be simultaneously guided away from the low-quality areas and towards the high-quality areas. We characterize the restrictions on tree reuse by analyzing the induced tracking error under time-varying dynamics, revealing a tradeoff between the search depth and the timescale of the changing dynamics. In numerical studies, our algorithm outperforms state-of-the-art sampling-based cross-entropy methods with hotstarting. We demonstrate our planner on an autonomous vehicle testbed performing a nonprehensile manipulation task: pushing a target object through an obstacle field. Code associated with this work will be made available at

## Introduction

Gradient-free optimization techniques are an attractive framework for decision making and motion planning on robotic systems where high-fidelity models may not be differentiable and descent algorithms can get caught in local minima. As a motivating example, we consider nonprehensile manipulation, a setting where a robot uses pushing, pulling, or other means of manipulation without grasping the target object with appendages. This task is challenging for conventional gradient-based optimization because of its hybrid dynamics and sparse reward structure.

uct, a variant of \\acmcts, is a powerful gradient-free technique that strategically explores the space of possible future trajectories, with guaranteed convergence to the optimal trajectory as its runtime increases \[\]. Although \\acuct is widely applicable to a large class of decision-making problems, its performance is dependent on its computational resources and accumulating enough samples to make an accurate value estimate. With this context, there is clear benefit in reusing past simulations to improve the quality of search and reduce sample complexity....

## Conclusion

We present \\acmpt, a new receding horizon planning framework that reuses a rich set of information from prior solver iterations to solve challenging planning problems. Our theoretical analysis guarantees the stability of our method and robustness to model mismatch, characterizing the limitations of tree reuse. We use our planner to produce solutions in real-time for a challenging nonprehensile manipulation task to push a target barrel through an obstacle field....

With the tools of discrete-time contraction, we proceed to analyze the tracking performance of our proposed algorithm. So far in the analysis we have considered dynamical systems without control inputs; we now present a constructive proof for a feedback law that guarantees the contraction of a discrete-time control system:

Our analysis shows that for slowly-changing dynamics, the steady-state tracking error introduced by the use of past estimates is bounded. Furthermore, understanding the connection between dynamics error, steady-state tracking error, and the contraction metric used to stabilize the system allows us to perform informed hyperparameter tuning. We analyze this connection in Sec. III.
