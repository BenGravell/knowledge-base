<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Escaping Local Minima with Stochastic Noise

Topics include Stochastic gradient descent, Nonconvex optimization, Smoothing, Global convergence, Optimization theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes noise-smoothed optimization for structured nonconvex functions and establishes convergence toward approximate global minima under suitable smoothing conditions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With the recent advancements in Deep Learning, non-convex problems have received wide spread attention. However, while stochastic gradient descent (SGD) can often successfully optimize these non-convex models in practice, the theoretical analysis - mapping SGD to Gradient Descent (GD) in expectation - cannot explain global convergence, as GD gets trapped in local minima and stationary points. We introduce a novel proof framework to analyze stochastic methods on a class of structured non-convex functions. We prove that SGD converges linearly to approximate global minima on non-convex functions that are `close' to a convex-like (strongly convex or P\L) function when its iterates are perturbed with stochastic noise of appropriate strength (smoothing). Our analysis applies to a strictly larger class of functions than studied in prior work. We demonstrate that special cases of smoothing are equivalent to vanilla SGD in expectation, which explains why SGD can escape local minima in practice.
