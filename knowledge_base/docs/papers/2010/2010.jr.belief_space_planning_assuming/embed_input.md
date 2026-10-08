<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Belief Space Planning Assuming Maximum Likelihood Observations

Topics include Belief-space planning, Partial observability, Maximum likelihood observations, Linear quadratic regulation, Replanning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Approximates belief dynamics using maximum-likelihood future observations and Gaussian stochastic effects. Applies belief-space LQR and local planning, and establishes finite-step convergence of a replanning strategy in the studied setting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We cast the partially observable control problem as a fully observable underactuated stochastic control problem in belief space and apply standard planning and control techniques. One of the difficulties of belief space planning is modeling the stochastic dynamics resulting from unknown future observations. The core of our proposal is to define deterministic beliefsystem dynamics based on an assumption that the maximum likelihood observation (calculated just prior to the observation) is always obtained. The stochastic effects of future observations are modelled as Gaussian noise. Given this model of the dynamics, two planning and control methods are applied. In the first, linear quadratic regulation (LQR) is applied to generate policies in the belief space. This approach is shown to be optimal for linear-Gaussian systems. In the second, a planner is used to find locally optimal plans in the belief space. We propose a replanning approach that is shown to converge to the belief space goal in a finite number of replanning steps. These approaches are characterized in the context of a simple nonlinear manipulation problem where a planar robot simultaneously locates and grasps an object.
