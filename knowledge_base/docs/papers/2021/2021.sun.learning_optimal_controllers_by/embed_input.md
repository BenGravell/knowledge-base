<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Optimal Controllers by Policy Gradient: Global Optimality via Convex Parameterization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Common reinforcement learning methods seek optimal controllers for unknown dynamical systems by searching in the "policy" space directly. A recent line of research, starting , aims to provide theoretical guarantees for such direct policy-update methods by exploring their performance in classical control settings, such as the infinite horizon linear quadratic regulator (LQR) problem. A key property these analyses rely on is that the LQR cost function satisfies the "gradient dominance" property with respect to the policy parameters. Gradient dominance helps guarantee that the optimal controller can be found by running gradient-based algorithms on the LQR cost. The gradient dominance property has so far been verified on a case-by-case basis for several control problems including continuous/discrete time LQR, LQR with decentralized controller, H_2/H_infinity robust control.In this paper, we make a connection between this line of work and classical convex parameterizations based on linear matrix inequalities (LMIs). Using this, we propose a unified framework for showing that gradient dominance indeed holds for a broad class of control problems, such as continuous- and discrete-time LQR, minimizing the L2 gain, and problems using system-level parameterization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our unified framework provides insights into the landscape of the cost function as a function of the policy, and enables extending convergence results for policy gradient descent to a much larger class of problems.
