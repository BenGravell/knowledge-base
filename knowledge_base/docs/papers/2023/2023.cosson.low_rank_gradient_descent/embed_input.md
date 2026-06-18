<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Low-Rank Gradient Descent

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Several recent empirical studies demonstrate that important machine learning tasks such as training deep neural networks, exhibit a low-rank structure, where most of the variation in the loss function occurs only in a few directions of the input space. In this paper, we leverage such low-rank structure to reduce the high computational cost of canonical gradient-based methods such as gradient descent (GD). Our proposed Low-Rank Gradient Descent (LRGD) algorithm finds an epsilon -approximate stationary point of a p-dimensional function by first identifying r ≤ p significant directions, and then estimating the true p-dimensional gradient at every iteration by computing directional derivatives only along those r directions. We establish that the “directional oracle complexities” of LRGD for strongly convex and non-convex objective functions are O(r {rmlog}(1/epsilon) + rp) and O(r/epsilon^ + rp), respectively. Therefore, when rll p, LRGD provides significant improvement over the known complexities of O(p rmlog(1/epsilon) ) and O(p/epsilon^) of GD in the strongly convex and non-convex settings, respectively.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, we formally characterize the classes of exactly and approximately low-rank functions. Empirically, using real and synthetic data, LRGD provides significant gains over GD when the data has low-rank structure, and in the absence of such structure, LRGD does not degrade performance compared to GD. This suggests that LRGD could be used in practice in any setting in place of GD.
