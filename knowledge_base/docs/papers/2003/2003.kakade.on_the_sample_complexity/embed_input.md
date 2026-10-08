<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Sample Complexity of Reinforcement Learning

Topics include Reinforcement learning, Sample complexity, Policy search, Exploration, Learning theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies how much experience reinforcement learning requires under policy-search and online exploration models, developing algorithms and sample-complexity guarantees.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This thesis is a detailed investigation into the following question: how much data must an agent collect in order to perform “reinforcement learning” successfully? This question is analogous to the classical issue of the sample complexity in supervised learning, but is harder because of the increased realism of the reinforcement learning setting. This thesis summarizes recent sample complexity results in the reinforcement learning literature and builds on these results to provide novel algorithms with strong performance guarantees. We focus on a variety of reasonable performance criteria and sampling models by which agents may access the environment. For instance, in a policy search setting, we consider the problem of how much simulated experience is required to reliably choose a “good” policy among a restricted class of policies Π (as in Kearns, Mansour, and Ng ). In a more online setting, we consider the case in which an agent is placed in an environment and must follow one unbroken chain of experience with no access to “offline” simulation (as in Kearns and Singh ). We build on the sample based algorithms suggested by Kearns, Mansour, and Ng. Their sample complexity bounds have no dependence on the size of the state space, an exponential dependence on the planning horizon time, and linear dependence on the complexity of Π.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We suggest novel algorithms with more restricted guarantees whose sample complexities are again independent of the size of the state space and depend linearly on the complexity of the policy class Π, but have only a polynomial dependence on the horizon time. We pay particular attention to the tradeoffs made by such algorithms.
