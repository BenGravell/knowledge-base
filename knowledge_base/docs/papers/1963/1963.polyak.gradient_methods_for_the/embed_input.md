<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradient Methods for the Minimisation of Functionals

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Historically important because it introduced what is now called the Polyak-Lojasiewicz (PL) or gradient-domination condition: the objective gap is controlled by the squared gradient norm, so a small gradient certifies near-optimality and gradient descent can converge linearly without strong convexity. This idea became a central bridge from classical optimization to modern machine learning: Karimi et al. showed that the PL inequality gives simple linear-convergence analyses for least squares, logistic regression, coordinate descent, stochastic and variance-reduced methods, proximal-gradient methods, SVMs, and L1-regularized problems, while Fazel et al. used the same gradient-domination viewpoint to explain why policy gradient methods can globally optimize the nonconvex LQR objective."

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Let f(t) be a functional defined in the (real) Hilbert space H. The problem consists in finding its minimum value f* = inf f(x) and some minimum point x* (if such exists).
