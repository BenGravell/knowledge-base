Q-learning with Logarithmic Regret

This paper presents the first non-asymptotic result showing that a model-free algorithm can achieve a logarithmic cumulative regret for episodic tabular reinforcement learning if there exists a strictly positive sub-optimality gap in the optimal Q-function. We prove that the optimistic Q-learning studied in [Jin et al. 2018] enjoys a O(fracSA* poly(H){Delta_min}log(SAT)) cumulative regret bound, where S is the number of states, A is the number of actions, H is the planning horizon, T is the total number of steps, and Delta_min is the minimum sub-optimality gap. This bound matches the information theoretical lower bound in terms of S,A,T up to a log(SA) factor. We further extend our analysis to the discounted setting and obtain a similar logarithmic cumulative regret bound.

## Introduction

$Q$-learning is one of the most popular classes of methods for solving reinforcement learning (RL) problems. $Q$-learning tries to estimate the optimal state-action value function ($Q$-function). With a $Q$-function, at every state, one can just greedily choose the action with the largest $Q$ value to interact with the RL environment. Compared to another popular class of methods, model-based learning, $Q$-learning algorithms (or more generally, model-free algorithms) often enjoy better memory and time efficiency^11^1See Section 2 for the precise definitions of model-free and model-based algorithms in the tabular setting..

While model-free methods are widely applied in practice, most theoretical works study model-based RL. In one of the most fundamental RL frameworks, tabular RL, which is the focus of this paper, the majority of works study model-based algorithms with a few exceptions. From a regret minimization point of view, the state-of-the-art analysis demonstrates that one can achieve a $\sqrt{T}$-type regret bound where $T$ is the number of episodes. Although these bounds are sharp in the worst-case scenario, they do not reveal the favorable structures of the environment, which can significantly decrease the regret.

One such structure is the existence of a strictly positive sub-optimality gap, i.e., for every state, there is a strictly positive value gap between the optimal action(s) and the rest (cf. Definition 2.1. ‣ Sub-optimality Gap ‣ 2 Preliminaries")). In practice, arguably, nearly all environments with finite action sets satisfy some sub-optimality gap conditions. In Atari-games, e.g., Freeway, the optimal action has a value that is usually very distinctive from the rest of actions. In many other environments with finite number of actions, e.g. those control environments in OpenAI gym, the gap condition usually holds.

## Conclusion and Future Directions

This paper gives the first logarithmic regret bounds for $Q$-learning in both finite-horizon and discounted tabular MDPs. Below we list some future directions that we believe are worth exploring.
