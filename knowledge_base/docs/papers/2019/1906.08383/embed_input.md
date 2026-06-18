Global Convergence of Policy Gradient Methods to (Almost) Locally Optimal Policies

Topics include Convex optimization, Nonconvex optimization, Reinforcement learning, Robotics, Autonomous driving, Optimization, Learning, Policy gradients, Saddle point, Stationary point.

Policy gradient (PG) methods are a widely used reinforcement learning methodology in many applications such as video games, autonomous driving, and robotics. In spite of its empirical success, a rigorous understanding of the global convergence of PG methods is lacking in the literature. In this work, we close the gap by viewing PG methods from a nonconvex optimization perspective. In particular, we propose a new variant of PG methods for infinite-horizon problems that uses a random rollout horizon for the Monte-Carlo estimation of the policy gradient. This method then yields an unbiased estimate of the policy gradient with bounded variance, which enables the tools from nonconvex optimization to be applied to establish global convergence. Employing this perspective, we first recover the convergence results with rates to the stationary-point policies in the literature. More interestingly, motivated by advances in nonconvex optimization, we modify the proposed PG method by introducing periodically enlarged stepsizes. The modified algorithm is shown to escape saddle points under mild assumptions on the reward and the policy parameterization....

## Introduction

In reinforcement learning (RL), an autonomous agent moves through a state space and seeks to learn a policy which maps states to a probability distribution over actions to maximize a long-term accumulation of rewards. When the agent selects a given action at a particular state, a reward is revealed and a random transition to a new state occurs according to a probability density that only depends on the current state and action, i.e., state transitions are Markovian. This evolution process is usually modeled as a Markov decision process (MDP)....

Despite the increasing prevalence of policy gradient methods, their global convergence in the infinite-horizon discounted setting, which is conventional in dynamic programming, is not yet well understood. This gap stems firstly from the fact that obtaining unbiased estimates of the policy gradient through sampling is often elusive....

## Conclusions

Despite its tremendous popularity, policy gradient methods in RL have rarely been investigated in terms of their global convergence, i.e., there seems to be a gap in the literature regarding the limiting properties of policy search and how this is a function of the initialization. Motivated by this gap, we have adopted the perspective and tools from nonconvex optimization to clarify and partially overcome some of the challenges of policy search for MDPs over continuous spaces....

### Theorem 4.3 (Convergence Rate of Algorithm 3 Locally Optimal Policies") with Diminishing Stepsize)

We then establish in the following theorem, which states that all the stochastic policy gradients ${\hat{\nabla}J{(\theta)}},{\check{\nabla}J{(\theta)}}$, and $\overset{\sim}{\nabla}J{(\theta)}$ are unbiased estimates of ${\nabla J}{(\theta)}$ \cf. ([3.4 Locally Optimal Policies"))\]. Additionally, we can also establish the boundedness of ${\|{\hat{\nabla}J{(\theta)}}\|},{\|{\check{\nabla}J{(\theta)}}\|}$, and $\|{\overset{\sim}{\nabla}J{(\theta)}}\|$, as well as $\|{{\nabla J}{(\theta)}}\|$ for any $\theta \in$. The proof is deferred to Appendix A.2 Locally Optimal Policies").

else if gradient type $\diamondsuit = \overset{\sim}{}$ then
Simulate the next state: s′ ∼ P(⋅|s,a).
Obtain estimates V̂πθ (s) ← EstV (s,θ) and V̂πθ (s′) ← EstV (s′,θ).
Calculate $\overset{\sim}{\nabla}J{(\theta)}$, i.e., let
