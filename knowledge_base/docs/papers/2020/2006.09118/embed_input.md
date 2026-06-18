Q-learning with Logarithmic Regret

This paper presents the first non-asymptotic result showing that a model-free algorithm can achieve a logarithmic cumulative regret for episodic tabular reinforcement learning if there exists a strictly positive sub-optimality gap in the optimal Q-function. We prove that the optimistic Q-learning studied in [Jin et al. 2018] enjoys a O(fracSA* poly(H){Delta_min}log(SAT)) cumulative regret bound, where S is the number of states, A is the number of actions, H is the planning horizon, T is the total number of steps, and Delta_min is the minimum sub-optimality gap. This bound matches the information theoretical lower bound in terms of S,A,T up to a log(SA) factor. We further extend our analysis to the discounted setting and obtain a similar logarithmic cumulative regret bound.

## Introduction

$Q$-learning is one of the most popular classes of methods for solving reinforcement learning (RL) problems. $Q$-learning tries to estimate the optimal state-action value function ($Q$-function). With a $Q$-function, at every state, one can just greedily choose the action with the largest $Q$ value to interact with the RL environment. Compared to another popular class of methods, model-based learning, $Q$-learning algorithms (or more generally, model-free algorithms) often enjoy better memory and time efficiency^11^1See Section 2 for the precise definitions of model-free and model-based algorithms in the tabular setting.....

While model-free methods are widely applied in practice, most theoretical works study model-based RL. In one of the most fundamental RL frameworks, tabular RL, which is the focus of this paper, the majority of works study model-based algorithms with a few exceptions. From a regret minimization point of view, the state-of-the-art analysis demonstrates that one can achieve a $\sqrt{T}$-type regret bound where $T$ is the number of episodes. Although these bounds are sharp in the worst-case scenario, they do not reveal the favorable structures of the environment, which can significantly decrease the regret.

### Function Approximation

Lastly, we note that recently researchers found the sub-optimality gap assumption is crucial for dealing with large state-space RL problems where function approximation is needed. Du et al. presented an algorithm that enjoys polynomial sample complexity if there is a sub-optimality gap and the environment satisfies a low-variance assumption. Du et al. further showed this assumption is necessary in certain settings. There is another line of works putting certain low-rank assumptions on MDPs. It would be interesting to extend our analysis to these settings and obtain logarithmic regret bounds.

One may wonder whether it is possible to obtain a regret bound that only depends the sum of positive gaps, e.g., $O\left( {\sum_{{{(x,a)},{\Delta_{1}{(x,a)}}} > 0}{\frac{H^{2}}{\Delta_{1}(x,a)}{\log T}}} \right)$, unlike ours, which is a multiple of $1/\Delta_{\min}$....
