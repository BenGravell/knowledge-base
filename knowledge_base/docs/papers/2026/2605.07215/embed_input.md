<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PISTO: Proximal Inference for Stochastic Trajectory Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic trajectory optimization methods like STOMP enable planning with non-differentiable costs, offering substantial flexibility over gradient-based approaches. We show that STOMP implicitly minimizes the KL divergence from a Boltzmann trajectory distribution, revealing an elegant Variational Inference (VI) structure underlying its updates. Building on this insight, we propose the \textit{Proximal Inference for Stochastic Trajectory Optimization} (PISTO) algorithm that stabilizes the updates by augmenting the objective with a KL regularization between successive Gaussian proposals. This proximal formulation admits a trust-region interpretation and yields closed-form mean updates computable as expectations under a surrogate distribution. We estimate these expectations via importance-weighted Monte Carlo sampling, producing a simple, derivative-free algorithm that inherits STOMP's ability to handle non-differentiable and discontinuous costs without modification. On robot arm motion planning benchmarks, PISTO achieves an 89\% success rate - outperforming CHOMP (63\%) and STOMP (68\%) - while producing shorter, smoother paths at twice the speed of competing stochastic methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We further validate PISTO on contact-rich MuJoCo locomotion and manipulation tasks, where it consistently outperforms both CEM and MPPI baselines in reward.
