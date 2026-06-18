<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampled Differential Dynamic Programming

Topics include Trajectory optimization, Differential dynamic programming, Sampled differential dynamic programming, Sampling-based control, Sampling-based planning, Hessian-free optimization, Path integral control, Evolution strategies, Covariance matrix adaptation evolution strategy, Taylor expansion, Gradient-based.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines DDP and path integral control by estimating the DDP Hessian via zero-order sampling rather than analytical differentiation, yielding a trajectory optimizer that blends the structure and efficiency of DDP with the robustness and simplicity of sampling-based methods. Think of it as Hessian-Free optimization specialized to trajectory optimization problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present SaDDP, a sampled version of the widely used differential dynamic programming (DDP) control algorithm. We contribute through establishing a novel connection between two major branches of robotics control research, that is, gradient-based methods such as DDP, and Monte Carlo methods such as path integral control (PI) that utilize random simulated trajectory rollouts. One of our key observations is that the Taylor-expansion, central to DDP, can be reformulated in terms of second-order statistics computed of the sampled trajectories. SaDDP makes few assumptions about the controlled system and works with black-box dynamics simulations with non-smooth contacts. Our simulation results show that the method outperforms PI and CMA-ES in both a simple linear-quadratic problem, and a multilink arm reaching task with obstacles.
