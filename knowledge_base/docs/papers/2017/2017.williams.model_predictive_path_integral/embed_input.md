<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model Predictive Path Integral Control: From Theory to Parallel Computation

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Stochastic optimal control, Graphics processing unit parallelization, Autonomous driving.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Tutorial paper introducing MPPI as a sampling-based model predictive control method, deriving it from path integral control theory and demonstrating a GPU-parallelized implementation for real-time autonomous driving.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, a model predictive path integral control algorithm based on a generalized importance sampling scheme is developed and parallel optimization via sampling is performed using a graphics processing unit. The proposed generalized importance sampling scheme allows for changes in the drift and diffusion terms of stochastic diffusion processes and plays a significant role in the performance of the model predictive control algorithm. The proposed algorithm is compared in simulation with a model predictive control version of differential dynamic programming on nonlinear systems. Finally, the proposed algorithm is applied on multiple vehicles for the task of navigating through a cluttered environment. The current simulations illustrate the efficiency and robustness of the proposed approach and demonstrate the advantages of computational frameworks that incorporate concepts from statistical physics, control theory, and parallelization against more traditional approaches of optimal control theory.
