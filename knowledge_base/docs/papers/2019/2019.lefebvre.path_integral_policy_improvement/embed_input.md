<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Integral Policy Improvement with Differential Dynamic Programming

Topics include Trajectory optimization, Differential dynamic programming, Path integral control, Model predictive path integral control, Policy improvement.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Integrates path integral policy improvement (PI²) with differential dynamic programming (DDP), using DDP's second-order local model to guide the sampling distribution in a PI-style update.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Path Integral Policy Improvement with Covariance Matrix Adaptation (PI2-CMA) is a step-based model-free reinforcement learning approach that combines statistical estimation techniques with fundamental results from Stochastic Optimal Control. Basically, a policy distribution is improved iteratively using reward weighted averaging of the corresponding rollouts. It was assumed that PI2-CMA somehow exploited gradient information that was contained by the reward weighted statistics. To our knowledge we are the first to expose the principle of this gradient extraction rigorously. Our findings reveal that PI2-CMA essentially obtains gradient information similar to the forward and backward passes in the Differential Dynamic Programming (DDP) method. It is then straightforward to extend the analogy with DDP by introducing a feedback term in the policy update. This suggests a novel algorithm which we coin Path Integral Policy Improvement with Differential Dynamic Programming (PI2-DDP). The resulting algorithm is similar to the previously proposed Sampled Differential Dynamic Programming (SaDDP) but we derive the method independently as a generalization of the framework of PI2-CMA. Our derivations suggest to implement some small variations to SaDDP so to increase performance. We validated our claims on a robot trajectory learning task.
