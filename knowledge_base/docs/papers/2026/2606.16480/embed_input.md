<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HOLO-MPPI: Multi-Scenario Motion Planning via Hierarchical Policy Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robots deployed in the real world must plan motions across diverse scenarios without per-scenario retuning. End-to-end reinforcement learning (RL) can generalize across scenarios but often becomes brittle under distribution shift, reward misspecification, and stochastic interactions. Model predictive path integral (MPPI) control enables strong real-time refinement without gradients, but its performance depends on a well-shaped sampling prior, while manually designing the priors does not scale to multi-scenario deployment. We present HOLO-MPPI (High-level Offline, Low-level Online MPPI), a multi-scenario motion planning framework that combines high-level policy learning with low-level stochastic optimal control. Offline, we learn a high-level policy that proposes scenario-robust plans in an abstract action space, with a learned world model for online rollout. Online, the policy serves as a data-driven prior generator that parameterizes MPPI's sampling distribution conditioned on the current observation and goal. MPPI then optimizes low-level control sequences around this prior in real time to adapt to local disturbances.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We instantiate HOLO-MPPI in autonomous driving by designing an effective high-level action space and tailored model architectures. Our evaluation across diverse driving scenarios shows that HOLO-MPPI improves upon MPPI and end-to-end RL baselines while maintaining real-time control.
