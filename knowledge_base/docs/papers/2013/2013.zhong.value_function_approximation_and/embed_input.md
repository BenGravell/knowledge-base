<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Value Function Approximation and Model Predictive Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Both global methods and on-line trajectory optimization methods are powerful techniques for solving optimal control problems; however, each has limitations. In order to mitigate the undesirable properties of each, we explore the possibility of combining the two. We explore two methods of deriving a descriptive final cost function to assist model predictive control (MPC) in selecting a good policy without having to plan as far into the future or having to fine-tune delicate cost functions. First, we exploit the large amount of data which is generated in MPC simulations (based on the receding horizon iterative LQG method) to learn, off-line, the global optimal value function for use as a final cost. We demonstrate that, while the global function approximation matches the value function well on some problems, there is relatively little improvement to the original MPC. Alternatively, we solve the Bellman equation directly using aggregation methods for linearly-solvable Markov Decision Processes to obtain an approximation to the value function and the optimal policy. Using both pieces of information in the MPC framework, we find controller performance of similar quality to MPC alone with long horizon, but now we may drastically shorten the horizon.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Implementation of these methods shows that Bellman equation-based methods and on-line trajectory methods can be combined in real applications to the benefit of both.
