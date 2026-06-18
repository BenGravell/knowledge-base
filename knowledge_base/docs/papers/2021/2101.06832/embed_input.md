Deep Structured Reactive Planning

An intelligent agent operating in the real-world must balance achieving its goal with maintaining the safety and comfort of not only itself, but also other participants within the surrounding scene. This requires jointly reasoning about the behavior of other actors while deciding its own actions as these two processes are inherently intertwined - a vehicle will yield to us if we decide to proceed first at the intersection but will proceed first if we decide to yield. However, this is not captured in most self-driving pipelines, where planning follows prediction. In this paper we propose a novel data-driven, reactive planning objective which allows a self-driving vehicle to jointly reason about its own plans as well as how other actors will react to them. We formulate the problem as an energy-based deep structured model that is learned from observational data and encodes both the planning and prediction problems....

## Introduction

Self-driving vehicles (SDVs) face many challenging situations when dealing with complex dynamic environments. Consider a scenario where an SDV is trying to merge left into a lane that is currently blocked by traffic. The SDV cannot reasonably merge by simply waiting - it could be waiting for quite a while and inconvenience the cars behind it. On the other hand, it cannot aggressively merge into the lane disregarding the lane congestion, as this will likely lead to a collision....

This complex reasoning is, however, seldom used in self-driving approaches. Instead, the autonomy stack of an SDV is composed of a set of modules executed one after another. The AV first detects other actors in the scene (perception) and predicts their future trajectories (prediction). Given the output of perception and prediction, it plans a trajectory towards its intended goal that will be executed by the control module. This implies that behavior forecasts of other actors are not affected by the AV's own plan; the SDV is a passive actor assuming a stochastic world that it cannot change....

## Conclusion

We have presented a novel reactive planning objective allowing the ego-agent to jointly reason about its own plans as well as how other actors will react to them. We formulated the problem with a deep energy-based model which enables us to explicitly model trajectory goodness as well as interaction cost between actors. Our experiments showed that our reactive model outperforms the non-reactive model in various highly interactive simulation scenarios without trading off collision rate. Moreover, we outperform or are competitive with state-of-the-art in prediction metrics.

where $p_{\mathbf{y}_{i}|\mathbf{y}_{0}}$ represents the marginal probability of the actor trajectory conditioned on the candidate ego-agent trajectory. These marginal probabilities which are tensors of size $N \times K \times K$, can all be efficiently approximated by exploiting Loopy Belief Propagation (LBP). This in turn allows efficient batch evaluation of the planning objective: for every sample of every actor ($N \times K$ samples), evaluate the conditional marginal probability times the corresponding energy term....

We decompose the joint energy $C{(\mathcal{Y},\mathcal{X};\mathbf{w})}$ in terms of an actor-specific energy that encodes the cost of a given trajectory for each...
