<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Dynamic Programming Implementations of Newton's Method for Unconstrained Optimal Control Problems

Topics include Differential dynamic programming, Newton's method, Unconstrained optimal control, Dynamic programming, Trajectory optimization, Second-order methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Dunn develops efficient dynamic-programming implementations of Newton's method for unconstrained optimal-control problems. The paper clarifies how dynamic-programming structure can be exploited to solve the Newton system efficiently, connecting second-order optimization with trajectory-optimization algorithms such as DDP.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Naive implementations of Newton's method for unconstrainedN-stage discrete-time optimal control problems with Bolza objective functions tend to increase in cost likeN 3 asN increases. However, if the inherent recursive structure of the Bolza problem is properly exploited, the cost of computing a Newton step will increase only linearly withN. The efficient Newton implementation scheme proposed here is similar to Mayne's DDP (differential dynamic programming) method but produces the Newton step exactly, even when the dynamical equations are nonlinear. The proposed scheme is also related to a Riccati treatment of the linear, two-point boundary-value problems that characterize optimal solutions. For discrete-time problems, the dynamic programming approach and the Riccati substitution differ in an interesting way; however, these differences essentially vanish in the continuous-time limit.
