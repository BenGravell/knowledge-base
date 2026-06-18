<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe Multi-agent Motion Planning via Filtered Reinforcement Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of safe multi-agent motion planning in cluttered environments. Existing multi-agent reinforcement learning-based motion planners only provide approximate safety enforcement. We propose a safe reinforcement learning algorithm that leverages single-agent reinforcement learning for target regulation and a subsequent convex optimization-based filtering that ensures the collective safety of the system. Our approach yields a safe, real-time implementable multi-agent motion planner that is simpler to train and enforces safety as hard constraints. Our approach can handle state and control constraints on the agents, and enforce collision avoidance among themselves and with static obstacles in the environment. Numerical simulations and hardware experiments show the efficacy of the approach.
