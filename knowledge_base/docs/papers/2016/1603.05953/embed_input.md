<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Katyusha: The First Direct Acceleration of Stochastic Gradient Methods

Topics include Stochastic optimization, Gradient descent, Stochastic gradients, Optimization, Katyusha, Variance reduction.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Nesterov's momentum trick is famously known for accelerating gradient descent, and has been proven useful in building fast iterative algorithms. However, in the stochastic setting, counterexamples exist and prevent Nesterov's momentum from providing similar acceleration, even if the underlying problem is convex and finite-sum. We introduce mathttKatyusha, a direct, primal-only stochastic gradient method to fix this issue. In convex finite-sum stochastic optimization, mathttKatyusha has an optimal accelerated convergence rate, and enjoys an optimal parallel linear speedup in the mini-batch setting. The main ingredient is Katyusha momentum, a novel "negative momentum" on top of Nesterov's momentum. It can be incorporated into a variance-reduction based algorithm and speed it up, both in terms of sequential and parallel performance. Since variance reduction has been successfully applied to a growing list of practical problems, our paper suggests that in each of such cases, one could potentially try to give Katyusha a hug.
