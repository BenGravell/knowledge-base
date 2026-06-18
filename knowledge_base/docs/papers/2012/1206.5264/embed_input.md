<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Apprenticeship Learning Using Inverse Reinforcement Learning and Gradient Methods

Topics include Inverse reinforcement learning, Apprenticeship learning, Natural gradients, Subgradient methods, Markov decision process, Reward learning, Policy matching.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Frames apprenticeship learning as a nonsmooth optimization problem over reward parameters and uses subgradients plus natural gradients to deal with policy non-smoothness and reward redundancy. The contribution is a more direct gradient-based IRL procedure that can match expert behavior reliably without repeatedly solving the max-margin style formulations common in earlier approaches.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we propose a novel gradient algorithm to learn a policy from an expert's observed behavior assuming that the expert behaves optimally with respect to some unknown reward function of a Markovian Decision Problem. The algorithm's aim is to find a reward function such that the resulting optimal policy matches well the expert's observed behavior. The main difficulty is that the mapping from the parameters to policies is both nonsmooth and highly redundant. Resorting to subdifferentials solves the first difficulty, while the second one is overcome by computing natural gradients. We tested the proposed method in two artificial domains and found it to be more reliable and efficient than some previous methods.
