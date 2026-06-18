Approximately Optimal Approximate Reinforcement Learning

Topics include Reinforcement learning, Conservative policy iteration, Approximate dynamic programming, Policy improvement, Approximate greedy policies, Sample complexity.

Introduces conservative policy iteration as an approximate RL algorithm that mixes new approximate-greedy policies cautiously with the current policy. The paper gives iteration bounds for achieving near-optimality without explicit dependence on state-space size, helping formalize stable approximate policy improvement.

In order to solve realistic reinforcement learning problems, it is critical that approximate algorithms be used. In this paper, we present the conservative policy iteration algorithm which finds an approximately optimal policy, given access to a next distribution, which draws the next state from a particular distribution, and an approximate greedy policy chooser. Crudely, the greedy policy chooser outputs a policy that usually chooses actions with the largest state-action values of the current policy, i.e. it outputs an approximate greedy policy. Our contribution is in proving that such an algorithm converges in a small number of steps and returns an approximately optimal policy, where the quantified claims do not explicitly depend on the size of the state space.
