<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convergence of Flow-Policy Gradient Learning for Linear Quadratic Regulator Problems

Topics include Policy gradients, Offline algorithms, Learning, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Flow Q-learning has recently been introduced to integrate learning from expert demonstrations into an actor-critic structure. Central to this innovation is the ``the one-step policy'' network, which is optimized through a Q-function that is regularized with the behavioral cloning from expert trajectories, allowing learning more expressive policies using flow-based generative models. In this paper, we studied the convergence property and stabilizablity of the one-step policy during learning for linear quadratic problems under the offline settings. Our theoretical results are based on a new formulation of the one-step policy loss based on the average expected cost, and regularized with the behavioral cloning loss. Such a formulation allows us to tap into existing strong theoretical results from the policy gradient theorem to study the convergence properties of the one-step policy. We verify our theoretical finding with simulation results on a linearized inverted pendulum.
