<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regret Bounds for the Adaptive Control of Linear Quadratic Systems

Topics include Adaptive control, Linear quadratic control, Regret bounds, Optimism, Online least squares, Model uncertainty, Reinforcement learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Applies confidence-set optimism to adaptive average-cost LQ control with unknown dynamics. The paper is significant because it gives a sublinear regret guarantee for LQ control without forced exploration, tying adaptive control to the online least-squares and bandit confidence machinery developed in the same line of work.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the average cost Linear Quadratic (LQ) control problem with unknown model parameters, also known as the adaptive control problem in the control community. We design an algorithm and prove that apart from logarithmic factors its regret up to time T is O(sqrt(T)). Unlike previous approaches that use a forced-exploration scheme, we construct a high-probability confidence set around the model parameters and design an algorithm that plays optimistically with respect to this confidence set. The construction of the confidence set is based on the recent results from online least-squares estimation and leads to improved worst-case regret bound for the proposed algorithm. To the best of our knowledge this is the the first time that a regret bound is derived for the LQ control problem.
