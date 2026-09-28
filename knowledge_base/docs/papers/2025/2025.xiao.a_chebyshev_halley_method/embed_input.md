<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Chebyshev–Halley Method with Gradient Regularization and an Improved Convergence Rate

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

High-order methods are particularly crucial for achieving highly accurate solutions or satisfying high-order optimality conditions. However, most existing high-order methods require solving complex high-order Taylor polynomial models, which pose significant computational challenges. In this paper, we propose a Chebyshev–Halley method with gradient regularization, which retains the convergence advantages of high-order methods while effectively addressing computational challenges in polynomial model solving. The proposed method incorporates a quadratic regularization term with an adaptive parameter proportional to a certain power of the gradient norm, thereby ensuring a closed-form solution at each iteration. In theory, the method achieves a global convergence rate of O(k−3) or even O(k−5), attaining the optimal rate of third-order methods without requiring additional acceleration techniques. Moreover, it maintains local superlinear convergence for strongly convex functions. Numerical experiments demonstrate that the proposed method compares favorably with similar methods in terms of efficiency and applicability.
