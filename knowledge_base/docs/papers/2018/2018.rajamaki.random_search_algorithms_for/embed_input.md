<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Random Search Algorithms for Optimal Control

Topics include Optimal control, Monte Carlo tree search, Trajectory optimization, Differential dynamic programming, Sampling-based control, Supervised learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops sampled differential dynamic programming and real-time Monte Carlo tree search for control without differentiable dynamics. Integrates supervised learning and multiple expert information sources to improve search for physics-based character control.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Optimal control is an important tool in many application areas, it is for example a central tool in robotics. Many widely used methods such as differential dynamic programming (DDP) are based on differentiating the dynamics of the controlled systems and the objective function. The assumption that one would have access to a differentiable model of the entire system does not hold for many systems of interest. For example, collisions break this assumption. In this case one has to resort to random search (Monte Carlo) algorithms. This thesis presents random search algorithms that fall into two categories. The first category is locally optimal sampling based trajectory optimization methods. The second one is real-time capable Monte Carlo tree search (MCTS) methods augmented with supervised machine learning. This thesis presents sampled differential dynamic programming (SaDDP), which is a random search trajectory optimization method, derived from the differential dynamic programming algorithm. SaDDP is derived by relating the quantities of the Taylor-expansion in DDP to the statistics of a multivariate normal distribution. This allows the statistics to be recomputed from sampled data instead of utilizing differentiation to obtain them. The thesis also presents ways to regularize the SaDDP algorithm efficiently.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The real-time capable MCTS methods presented in this thesis enable the real-time control of complicated systems, such as physics-based 3D characters. The methods perform a receding horizon lookahead search and use the data produced by the lookahead search to teach machine learning models how to better search for the actions in the future. The demonstrated combination of receding horizon search and supervised learning is fast to converge and yields robust learning. The MCTS in this thesis combines information from multiple sources. This thesis presents how to combine the information from various sources in such a way that the search adapts to the information sources agreeing or disagreeing. In addition to new search algorithms, this thesis presents a combination of MCTS and a neural network generative model. This combination enables the neural network to learn that it can perform different actions in a single state.
