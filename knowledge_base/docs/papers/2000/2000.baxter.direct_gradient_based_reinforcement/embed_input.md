Direct Gradient-Based Reinforcement Learning

Topics include Reinforcement learning, Policy gradients, Direct policy search, Average reward, POMDPs, Gradient estimation, Stochastic policies.

Presents an early direct policy-gradient approach for estimating the gradient of average reward from a single trajectory in controlled POMDPs. The key contribution is to bypass value-function approximation and optimize policy parameters directly, with convergence guarantees tied to the estimator time constant and Markov-chain mixing behavior.

Many control, scheduling, planning and game-playing tasks can be formulated as reinforcement learning problems, in which an agent chooses actions to take in some environment, aiming to maximize a reward function. We present an algorithm for computing approximations to the gradient of the average reward from a single sample path of a controlled partially observable Markov decision process. We show that the accuracy of these approximations depends on the relationship between a time constant used by the algorithm and the mixing time of the Markov chain, and that the error can be made arbitrarily small by setting the time constant suitably large. We prove that the algorithm converges with probability 1.
