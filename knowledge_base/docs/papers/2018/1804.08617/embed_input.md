Distributed Distributional Deterministic Policy Gradients

This work adopts the very successful distributional perspective on reinforcement learning and adapts it to the continuous control setting. We combine this within a distributed framework for off-policy learning in order to develop what we call the Distributed Distributional Deep Deterministic Policy Gradient algorithm, D4PG. We also combine this technique with a number of additional, simple improvements such as the use of N-step returns and prioritized experience replay. Experimentally we examine the contribution of each of these individual components, and show how they interact, as well as their combined contributions. Our results show that across a wide variety of simple control tasks, difficult manipulation tasks, and a set of hard obstacle-based locomotion tasks the D4PG algorithm achieves state of the art performance.

## Introduction

The ability to solve complex control tasks with high-dimensional input and action spaces is a key milestone in developing real-world artificial intelligence. The use of reinforcement learning to solve these types of tasks has exploded following the work of the Deep Q Network (DQN) algorithm, capable of human-level performance on many Atari games. Similarly, ground breaking achievements have been made in classical games such as Go. However, these algorithms are restricted to problems with a finite number of discrete actions.

In control tasks, commonly seen in the robotics domain, continuous action spaces are the norm. For algorithms such as DQN the policy is only implicitly defined in terms of its value function, with actions selected by maximizing this function. In the continuous control domain this would require either a costly optimization step or discretization of the action space. While discretization is perhaps the most straightforward solution, this can prove a particularly poor approximation in high-dimensional settings or those that require finer grained control....

In this work we introduced the D4PG, or Distributed Distributional DDPG, algorithm. Our main contributions include the inclusion of a distributional updates to the DDPG algorithm, combined with the use of multiple distributed workers all writing into the same replay table. We also consider a number of other, smaller changes to the algorithm. All of these simple modifications contribute to the overall performance of the D4PG algorithm; the biggest performance gain of these simple changes is arguably the use of $N$-step returns....

Finally, as our results can attest, the D4PG algorithm is capable of state-of-the-art performance on a number of very difficult continuous control problems.

8: Update network parameters θ ← θ + αt δθ, w ← w + βt δw
9: If t = 0mod ttarget, update the target networks (θ′,w′) ← (θ,w)
10: If t = 0mod tactors, replicate network weights to the actors
12: return policy parameters θ
3: Execute action a, observe reward r and state x′
5: until learner finishes

where equality is with respect to the probability law of the random variables; note that this expectation is taken with respect to distribution of $Z$ as well as the transition dynamics.
