<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Theoretical Framework for Back-Propagation

Topics include Backpropagation, Lagrange multipliers, Optimal control, Recurrent neural networks, Weight sharing, Constrained optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Derives backpropagation from a Lagrangian formulation of neural network training with constraints on network dynamics. The framework also derives continuous recurrent network learning and shows how weight-sharing constraints incorporate prior knowledge while reducing the number of trainable parameters.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Among all the supervised learning algorithms, back propagation (BP) is probably the most wi(l)dely used. Although numerous experimental works have demonstrated its capabilities, a deeper theoretical understanding of the algorithm is definitely needed. We present a mathematical framework for studying back-propagation based on the Lagrangian formalism. In this framework, inspired by optimal control theory, back-propagation is formulated as an optimization problem with nonlinear constraints. The Lagrange function is the sum of an output objective function and a constraint term which describes the network dynamics. This approach suggests many natural extensions to the basic algorithm. It also provides an extremely simple formulation (and derivation) of continuous recurrent network equations as described by Pineda [Pineda, 1987]. Other easily described variations involve either additional terms in the error function, additional constraints on the set of solutions, or transformations of the parameter space. An interesting kind of constraint is an equality constraint among the weights, which can be implemented with little overhead. It is shown that this sort of constraint provides a way of putting a priori knowledge into the network while reducing the number of free parameters.
