Interpretable Goal-Based Prediction and Planning for Autonomous Driving

Topics include Autonomous driving, Motion prediction, Motion planning, Monte Carlo tree search, Interaction-aware planning.

Builds an interpretable autonomous-driving stack that uses rational inverse planning to infer other vehicles goals and feeds those beliefs into Monte Carlo tree search for ego planning. The paper emphasizes explainable macro-action reasoning rather than opaque end-to-end trajectory prediction.

We propose an integrated prediction and planning system for autonomous driving which uses rational inverse planning to recognise the goals of other vehicles. Goal recognition informs a Monte Carlo Tree Search (MCTS) algorithm to plan optimal maneuvers for the ego vehicle. Inverse planning and MCTS utilise a shared set of defined maneuvers and macro actions to construct plans which are explainable by means of rationality principles. Evaluation in simulations of urban driving scenarios demonstrate the system's ability to robustly recognise the goals of other vehicles, enabling our vehicle to exploit non-trivial opportunities to significantly reduce driving times. In each scenario, we extract intuitive explanations for the predictions which justify the system's decisions.

## Introduction

The ability to predict the intentions and driving trajectories of other vehicles is a key problem for autonomous driving. This problem is significantly complicated by the need to make fast and accurate predictions based on limited observation data which originate from coupled multi-agent interactions.

To make prediction tractable in such conditions, a standard approach in autonomous driving research is to assume that vehicles use one of a finite number of distinct high-level maneuvers, such as lane-follow, lane-change, turn, stop, etc.. A classifier of some type is used to detect a vehicle's current executed maneuver based on its observed driving trajectory. The limitation in such methods is that they only detect the *current* maneuver of other vehicles, hence planners using such predictions are effectively limited to the timescales of the detected maneuvers....

## Conclusion

We proposed an autonomous driving system, IGP2, which integrates planning and prediction over extended horizons by reasoning about the goals of other vehicles via rational inverse planning. Evaluation in diverse urban driving scenarios showed that IGP2 robustly recognises the goals of non-ego vehicles, resulting in improved driving efficiency while allowing for intuitive interpretations of the predictions to explain the system's decisions. IGP2 is general in that it uses relatively standard planning techniques that could be replaced with other techniques (e.g....

A heuristic function is used to generate a set of possible goals $\mathcal{G}^{i}$ for vehicle $i$ based on its location and context information such as road layout. In our system, we include goals for the visible end of the current road and connecting roads (bounded by the ego vehicle's view region). In addition to such static goals, it is also possible to add dynamic goals which depend on current traffic. For example, in the dense merging scenario shown in Figure 2(d), stopping goals are dynamically added to model a vehicle's intention to allow the ego vehicle to merge in front.

### III-B Macro Actions

The algorithm performs a number of closed-loop simulations ${\hat{s}}_{t:n}$, starting in the current state ${\hat{s}}_{t} = s_{t}$ down to some fixed search depth or until a goal state is reached....
