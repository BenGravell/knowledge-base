<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Online Planning Algorithms for POMDPs

Topics include POMDPs, Online planning, Heuristic search, Belief-state planning, Sequential decision making, Planning under uncertainty, Survey.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Surveys online planning methods for POMDPs, emphasizing lookahead search from the current belief state as a practical alternative to computing a full offline policy. It compares online algorithms and heuristic search variants empirically, highlighting how local planning and value-function bounds can make larger partially observable problems more tractable.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Partially Observable Markov Decision Processes (POMDPs) provide a rich framework for sequential decision-making under uncertainty in stochastic domains. However, solving a POMDP is often intractable except for small problems due to their complexity. Here, we focus on online approaches that alleviate the computational complexity by computing good local policies at each decision step during the execution. Online algorithms generally consist of a lookahead search to find the best action to execute at each time step in an environment. Our objectives here are to survey the various existing online POMDP methods, analyze their properties and discuss their advantages and disadvantages; and to thoroughly evaluate these online approaches in different environments under various metrics (return, error bound reduction, lower bound improvement). Our experimental results indicate that state-of-the-art online heuristic search methods can handle large POMDP domains efficiently.
