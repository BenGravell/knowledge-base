<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Non-Convex Optimization for Machine Learning: Design, Analysis, and Understanding

Topics include Non-convex optimization, Optimization landscapes, Machine learning theory, Alternating minimization, Sparse coding, Matrix completion, Linear dynamical systems, Word embeddings.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops tools for proving convergence of non-convex learning algorithms, including alternating minimization for sparse coding and geometric analyses of matrix completion and linear dynamical systems. A generative account of word embeddings explains their linear structure, word analogies, and polysemy.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Non-convex optimization is ubiquitous in modern machine learning: recent breakthroughs in deep learning require optimizing non-convex training objective functions; problems that admit accurate convex relaxation can often be solved more efficiently with non-convex formulations. However, the theoretical understanding of non-convex optimization remained rather limited. Can we extend the algorithmic frontier by efficiently optimizing a family of interesting non-convex functions? Can we successfully apply non-convex optimization to machine learning problems with provable guarantees? How do we interpret the complicated models in machine learning that demand non-convex optimizers? Towards addressing these questions, in this thesis, we theoretically studied various machine learning models including sparse coding, topic models, and matrix completion, linear dynamical systems, and word embeddings. We first consider how to find a coarse solution to serve as a good starting point for local improvement algorithms such as stochastic gradient descent. We propose efficient methods for sparse coding and topic inference with better provable guarantees. Second, we propose a framework for analyzing local improvement algorithms that start from a course solution. We apply it successfully to the sparse coding problem.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Then, we consider a family of non-convex functions satisfying that all local minima are also global (and some additional regularity property). Such functions can be optimized by local improvement algorithms efficiently from a random or arbitrary starting point. The challenge that we address here, in turn, becomes proving that an objective function belongs to this class. We establish such results for the natural learning objectives of matrix completion and linear dynamical systems. Finally, we make steps towards interpreting the non-linear models that require non-convex training algorithms. We reflect on the principles of word embeddings in natural language processing. We give a generative model for the texts, using which we explain why different non-convex formulations such as word2vec and GloVe can learn similar word embeddings with the surprising performance — analogous words have embeddings with similar differences.
