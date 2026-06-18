Tree-structured Policy Planning with Learned Behavior Models

Topics include Vehicles, Deep learning, Datasets, Optimization, Planning, Learning, TPP, Propose tree policy planning, Markov decision process.

Autonomous vehicles (AVs) need to reason about the multimodal behavior of neighboring agents while planning their own motion. Many existing trajectory planners seek a single trajectory that performs well under all plausible futures simultaneously, ignoring bi-directional interactions and thus leading to overly conservative plans. Policy planning, whereby the ego agent plans a policy that reacts to the environment's multimodal behavior, is a promising direction as it can account for the action-reaction interactions between the AV and the environment. However, most existing policy planners do not scale to the complexity of real autonomous vehicle applications: they are either not compatible with modern deep learning prediction models, not interpretable, or not able to generate high quality trajectories. To fill this gap, we propose Tree Policy Planning (TPP), a policy planner that is compatible with state-of-the-art deep learning prediction models, generates multistage motion plans, and accounts for the influence of ego agent on the environment behavior.

## Introduction

A key challenge of motion planning for autonomous vehicles (AV)s is reasoning about the interaction between the ego vehicle and neighboring agents. The task is commonly divided into two subproblems: trajectory prediction for other agents, and ego motion planning with prediction. Trajectory prediction has seen substantial progress in recent years, coming from simple kineamtic models to powerful deep learning models capable of generating high-quality, multi-modal predictions. However, motion planning with such high-capacity prediction models remains a challenge.

Typical AV planners simplify the ego behavior planning problem into *trajectory planning*, where a single trajectory is sought that minimizes an expected cost over *all* predicted futures within the planning horizon. Such trajectory planning leads to overly conservative plans because it ignores the new information to be acquired about other agents in subsequent time steps, and the effects of ego actions on the behavior of other agents.

In fact, in decision-making literature, people have long been pursuing a closed-loop policy instead of an open-loop plan as the former is shown to be optimal for problems such as Markov decision processes (MDP).

We evaluate TPP in closed-loop simulation based on a recently proposed realistic data-driven traffic model. Our results show that TPP achieves good closed-loop driving performance in real-world scenarios from the nuScenes dataset, and significantly outperforms non-policy planning baselines. The algorithm is highly parallelizable, and can run in real time.

## Conclusion

We present TPP, a policy planner capable of generating multistage motion policies that react to the environment. It is centered around an ego trajectory tree and a scenario tree that predicts the environment behavior, both containing multiple stages. Ego-conditioning is applied to leverage the reactive behavior of the environment under the ego vehicle's presence. The closed-loop simulation result shows that TPP significantly outperform two non-policy benchmarks and the runtime test suggest that such sophisticated policy planner can be run in real time.
