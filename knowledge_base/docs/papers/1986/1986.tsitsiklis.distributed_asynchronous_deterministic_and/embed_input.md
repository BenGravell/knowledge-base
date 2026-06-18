Distributed Asynchronous Deterministic and Stochastic Gradient Optimization Algorithms

Topics include Distributed optimization, Asynchronous algorithms, Gradient method, Stochastic optimization, Parallel computation, Convergence analysis, Convex optimization.

Tsitsiklis, Bertsekas, and Athans analyze deterministic and stochastic gradient-style optimization algorithms executed asynchronously across distributed processors. The paper is an early foundation for distributed optimization, showing how convergence can survive communication delays, stale information, and parallel updates under suitable assumptions.

We present a model for asynchronous distributed computation and then proceed to analyze the convergence of natural asynchronous distributed versions of a large class of deterministic and stochastic gradient-like algorithms. We show that such algorithms retain the desirable convergence properties of their centralized counterparts, provided that the time between consecutive interprocessor communications and the communication delays are not too large.
