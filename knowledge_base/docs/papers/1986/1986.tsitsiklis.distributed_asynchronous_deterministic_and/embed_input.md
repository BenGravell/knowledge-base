<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributed Asynchronous Deterministic and Stochastic Gradient Optimization Algorithms

Topics include Distributed optimization, Asynchronous algorithms, Gradient method, Stochastic optimization, Parallel computation, Convergence analysis, Convex optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Tsitsiklis, Bertsekas, and Athans analyze deterministic and stochastic gradient-style optimization algorithms executed asynchronously across distributed processors. The paper is an early foundation for distributed optimization, showing how convergence can survive communication delays, stale information, and parallel updates under suitable assumptions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a model for asynchronous distributed computation and then proceed to analyze the convergence of natural asynchronous distributed versions of a large class of deterministic and stochastic gradient-like algorithms. We show that such algorithms retain the desirable convergence properties of their centralized counterparts, provided that the time between consecutive interprocessor communications and the communication delays are not too large.
