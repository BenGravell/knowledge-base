BITKOMO: Combining Sampling and Optimization for Fast Convergence in Optimal Motion Planning

Optimal sampling based motion planning and trajectory optimization are two competing frameworks to generate optimal motion plans. Both frameworks have complementary properties: Sampling based planners are typically slow to converge, but provide optimality guarantees. Trajectory optimizers, however, are typically fast to converge, but do not provide global optimality guarantees in nonconvex problems, e.g. scenarios with obstacles. To achieve the best of both worlds, we introduce a new planner, BITKOMO, which integrates the asymptotically optimal Batch Informed Trees (BIT*) planner with the K-Order Markov Optimization (KOMO) trajectory optimization framework. Our planner is anytime and maintains the same asymptotic optimality guarantees provided by BIT*, while also exploiting the fast convergence of the KOMO trajectory optimizer. We experimentally evaluate our planner on manipulation scenarios that involve high dimensional configuration spaces, with up to two 7-DoF manipulators, obstacles and narrow passages. BITKOMO performs better than KOMO by succeeding even when KOMO fails, and it outperforms BIT* in terms of convergence to the optimal solution.

## Introduction

Generating optimal motions plans is crucial for almost any robotic tasks ranging from typical manipulation tasks such as bin-picking to autonomous navigation of mobile robots. To solve such tasks, the robotics community relies on two powerful motion planning frameworks: Sampling-based planners and trajectory optimization.

Sampling-based planners like RRT\*, BIT\* or FMT\* converge asymptotically to optimal solutions and almost surely provide a solution if one exists. However, these planners are slow at converging to the optimal trajectory, because improvements to the current best solution only arise when we sample a state nearby, and often provide non-smooth trajectories that may require post-processing.

Even though we observe faster convergence than BIT\* to optimal paths, our planner does not have a better success rate. A dedicated planner could be developed to generate improved initial guesses to the optimizer, resulting in an increased success rate. The optimization and sampling modules could also easily be parallelized, providing a higher speed-up. Calling the KOMO optimizer ahead of the BIT\* planner could increase the speed further.

Our experiments clearly demonstrate that BITKOMO can robustly achieve fast convergence to optimal motion plans. This is an important step towards making optimal motion planners converge as quickly as trajectory optimizers --- all while keeping asymptotic optimality guarantees.

High dimensional spaces containing narrow passages are challenging for sampling based planners. This is because it is difficult to sample collision free edges through narrow passages. Since KOMO can push paths out of obstacles, we could allow paths partially in collision into the BIT\* tree. However, these edges need to be added with sufficient collision penalty to ensure that BIT\* does not mistake a path in collision to be of a lower cost than the true minima. We also want our collision checker to quickly guess the extent of collision so as to be quick in finding a solution for BIT\*....

### IV-A1 Initialize (A)

We evaluate our algorithm on 6 different robotic scenarios^11^1 In all scenarios, the robot moves from the initial configuration (solid color) to the goal configuration (translucent color) (Fig. 4)....
