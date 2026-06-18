<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Fastest Known Globally Convergent First-Order Method for Minimizing Strongly Convex Functions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We design and analyze a novel gradient-based algorithm for unconstrained convex optimization. When the objective function is m-strongly convex and its gradient is L-Lipschitz continuous, the iterates and function values converge linearly to the optimum at rates p and p 2, respectively, where p = 1 - √m/L. These are the fastest known guaranteed linear convergence rates for globally convergent first-order methods, and for high desired accuracies the corresponding iteration complexity is within a factor of two of the theoretical lower bound. We use a simple graphical design procedure based on integral quadratic constraints to derive closed-form expressions for the algorithm parameters. The new algorithm, which we call the triple momentum method, can be seen as an extension of methods such as gradient descent, Nesterov's accelerated gradient descent, and the heavy-ball method.
