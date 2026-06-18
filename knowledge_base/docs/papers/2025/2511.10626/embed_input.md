<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Solutions to Non-Convex Functional Constrained Problems with Hidden Convexity

Topics include Convex optimization, Reinforcement learning, Safety, Online algorithms, Optimization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Constrained non-convex optimization is fundamentally challenging, as global solutions are generally intractable and constraint qualifications may not hold. However, in many applications, including safe policy optimization in control and reinforcement learning, such problems possess hidden convexity, meaning they can be reformulated as convex programs via a nonlinear invertible transformation. Typically such transformations are implicit or unknown, making the direct link with the convex program impossible. On the other hand, (sub-)gradients with respect to the original variables are often accessible or can be easily estimated, which motivates algorithms that operate directly in the original (non-convex) problem space using standard (sub-)gradient oracles. In this work, we develop the first algorithms to provably solve such non-convex problems to global minima. First, using a modified inexact proximal point method, we establish global last-iterate convergence guarantees with O~(epsilon^(-3)) oracle complexity in non-smooth setting. For smooth problems, we propose a new bundle-level type method based on linearly constrained quadratic subproblems, improving the oracle complexity to O~(epsilon^(-1)).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Surprisingly, despite non-convexity, our methodology does not require any constraint qualifications, can handle hidden convex equality constraints, and achieves complexities matching those for solving unconstrained hidden convex optimization.
