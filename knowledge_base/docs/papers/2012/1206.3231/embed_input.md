<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CORL: A Continuous-state Offset-dynamics Reinforcement Learner

Topics include Reinforcement learning, Continuous state spaces, Offset dynamics, Sample complexity, Fitted value iteration, Robotic driving, Probably approximately correct learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces CORL for learning continuous-state MDPs whose dynamics switch among offset models, giving PAC-style sample-complexity bounds that include the cost of approximate planning. The paper is a bridge between theoretical RL and robotics because it learns a structured transition model, solves it with fitted value iteration, and demonstrates the representation on a robotic car over varying terrain.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Continuous state spaces and stochastic, switching dynamics characterize a number of rich, realworld domains, such as robot navigation across varying terrain. We describe a reinforcementlearning algorithm for learning in these domains and prove for certain environments the algorithm is probably approximately correct with a sample complexity that scales polynomially with the state-space dimension. Unfortunately, no optimal planning techniques exist in general for such problems; instead we use fitted value iteration to solve the learned MDP, and include the error due to approximate planning in our bounds. Finally, we report an experiment using a robotic car driving over varying terrain to demonstrate that these dynamics representations adequately capture real-world dynamics and that our algorithm can be used to efficiently solve such problems.
