A Gentle Lecture Note on Filtrations in Reinforcement Learning

Topics include Reinforcement learning, Learning.

This note aims to provide a basic intuition on the concept of filtrations as used in the context of reinforcement learning (RL). Filtrations are often used to formally define RL problems, yet their implications might not be eminent for those without a background in measure theory. Essentially, a filtration is a construct that captures partial knowledge up to time t, without revealing any future information that has already been simulated, yet not revealed to the decision-maker. We illustrate this with simple examples from the finance domain on both discrete and continuous outcome spaces. Furthermore, we show that the notion of filtration is not needed, as basing decisions solely on the current problem state (which is possible due to the Markovian property) suffices to eliminate future knowledge from the decision-making process.

## Abstract

This note aims to provide a basic intuition on the concept of filtrations as used in the context of reinforcement learning (RL). Filtrations are often used to formally define RL problems, yet their implications might not be eminent for those without a background in measure theory. Essentially, a filtration is a construct that captures partial knowledge up to time $t$, without revealing any future information that has already been simulated, yet not revealed to the decision-maker. We illustrate this with simple examples from the finance domain on both discrete and continuous outcome spaces.

When reinforcement learning (RL) problems are introduced, papers typically start with some generic Markov Decision Process (MDP) model that looks something like $(\mathcal{S},{\mathcal{X}{(S_{t + 1})}},{{\mathbb{P}}^{\Omega}{({S_{t + 1} \mid {S_{t},x_{t}}})}},{R{(S_{t},x_{t})}},\rho)$.

We proceed to introduce an example. To illustrate the concept of filtration as simply as possible, we introduce a problem setting in which the state $S_{t} \in {\mathbb{R}}^{+}$ represents the price of a given financial stock at time $t$. No other model information is needed for this exercise, although for practical purposes you might imagine that you aim to buy at a low price and sell at a high price to lock in profits. Suppose the initial stock price is defined by $S_{0}$ and we have a time horizon composed of three discrete time steps ($T = 3$).

Recall that in RL, we aim to find a decision-making policy $\pi:{S_{t}\mapsto x_{t}}$. The state $S_{t}$ can be computed based on the initial state $S_{0}$, the decisions made, and the information sequence ${W_{1} = {\omega_{1},\ldots}},{W_{t} = \omega_{t}}$. However, as the Markovian property holds (remind that decisions only depend on the current state of the system, not on information from the past), we need solely our current state $S_{t}$ to make a decision, not the entire information sequence leading to that state.
