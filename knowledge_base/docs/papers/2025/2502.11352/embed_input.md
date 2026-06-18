A Framework for Learning Scoring Rules in Autonomous Driving Planning Systems

In autonomous driving systems, motion planning is commonly implemented as a two-stage process: first, a trajectory proposer generates multiple candidate trajectories, then a scoring mechanism selects the most suitable trajectory for execution. For this critical selection stage, rule-based scoring mechanisms are particularly appealing as they can explicitly encode driving preferences, safety constraints, and traffic regulations in a formalized, human-understandable format. However, manually crafting these scoring rules presents significant challenges: the rules often contain complex interdependencies, require careful parameter tuning, and may not fully capture the nuances present in real-world driving data. This work introduces FLoRA, a novel framework that bridges this gap by learning interpretable scoring rules represented in temporal logic. Our method features a learnable logic structure that captures nuanced relationships across diverse driving scenarios, optimizing both rules and parameters directly from real-world driving demonstrations collected in NuPlan....

## Introduction

Figure 1: This figure illustrates our framework for scoring and selecting trajectories in autonomous driving systems. Modern autonomous driving planners typically follow a propose-selection paradigm, where multiple candidate trajectories are first generated and then filtered through a scoring mechanism. As shown in the Motion Plan Proposing block, multiple trajectories (colored lines) are proposed as potential future paths for the autonomous vehicle. These candidates need to be evaluated and ranked to select the most suitable trajectory for execution....

Modern autonomous driving systems typically produce multiple potential plans, as this parallel approach offers several key advantages: it allows the system to consider different driving modalities (such as aggressive or conservative behaviors), accounts for future uncertainties, and provides redundancy in case certain paths become infeasible. These generated plans then need to be evaluated through a scoring mechanism to select the most suitable one for execution.

## Conclusion, Limitations, and Future Work

This paper introduces FLoRA, a framework for learning interpretable scoring rules expressed in temporal logic for autonomous driving planning systems. FLoRA addresses key challenges by developing a learnable logic structure to capture nuanced relationships among driving predicates; proposing a data-driven method to optimize rule structure and parameters from demonstrations; and presenting an optimization framework for learning from driving demonstration data....

Aggregating the output from a single Propositional layer can represent any formula in the form of.

### IV-A Condition-Action Pair

The learning system evaluates driving behaviors in a state space $S = {\{{(\mathcal{E}_{t},\tau_{t})}\}}_{t = 0}^{T}$, where behaviors with ${\overline{\mathcal{L}}{(S;{\mathbf{θ}})}} > 0$ are considered acceptable. Without constraints, the system might learn shortcuts that accept almost any behavior. Consider a simple example where we want to learn rules for safe lane changes. Without regularization, the system might learn the rule: $\text{InLane} \vee \text{SafeDistance}$ that accepts behaviors in which the car is either in a lane OR maintains safe distance, which is clearly too permissive....
