<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Computational Optimal Transport: Complexity by Accelerated Gradient Descent Is Better than by Sinkhorn's Algorithm

Topics include Gradient descent, Accuracy, Optimal transport, Transport, APDAGD.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We analyze two algorithms for approximating the general optimal transport (OT) distance between two discrete distributions of size n, up to accuracy epsilon. For the first algorithm, which is based on the celebrated Sinkhorn's algorithm, we prove the complexity bound O~(n^/epsilon^) arithmetic operations. For the second one, which is based on our novel Adaptive Primal-Dual Accelerated Gradient Descent (APDAGD) algorithm, we prove the complexity bound O~(min{n^(9/4)/epsilon, n^/epsilon^ }) arithmetic operations. Both bounds have better dependence on epsilon than the state-of-the-art result given by O~(n^/epsilon^). Our second algorithm not only has better dependence on epsilon in the complexity bound, but also is not specific to entropic regularization and can solve the OT problem with different regularizers.
