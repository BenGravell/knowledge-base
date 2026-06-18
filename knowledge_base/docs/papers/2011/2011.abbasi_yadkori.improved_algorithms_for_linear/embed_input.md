<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Improved Algorithms for Linear Stochastic Bandits

Topics include Linear bandits, Stochastic bandits, Optimism, Confidence sets, UCB algorithms, Regret bounds, Online learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Improves UCB-style algorithms for stochastic and linear stochastic bandits by replacing looser confidence regions with tighter self-normalized confidence sets. The resulting optimistic linear-bandit method improves regret bounds by logarithmic factors and gives a practical empirical gain, making it a standard reference for OFUL-style algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We improve the theoretical analysis and empirical performance of algorithms for the stochastic multi-armed bandit problem and the linear stochastic multi-armed bandit problem. In particular, we show that a simple modification of Auer’s UCB algorithm achieves with high probability constant regret. More importantly, we modify and, consequently, improve the analysis of the algorithm for the for linear stochastic bandit problem studied by Auer, Dani et al., Rusmevichientong and Tsitsiklis, Li et al.. Our modification improves the regret bound by a logarithmic factor, though experiments show a vast improvement. In both cases, the improvement stems from the construction of smaller confidence sets. For their construction we use a novel tail inequality for vector-valued martingales.
