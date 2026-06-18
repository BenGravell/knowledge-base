Learning Autonomous Vehicle Safety Concepts from Demonstrations

Topics include Vehicles, Control barrier functions, Safety, Control, Learning, AV.

Evaluating the safety of an autonomous vehicle (AV) depends on the behavior of surrounding agents which can be heavily influenced by factors such as environmental context and informally-defined driving etiquette. A key challenge is in determining a minimum set of assumptions on what constitutes reasonable foreseeable behaviors of other road users for the development of AV safety models and techniques. In this paper, we propose a data-driven AV safety design methodology that first learns ``reasonable'' behavioral assumptions from data, and then synthesizes an AV safety concept using these learned behavioral assumptions. We borrow techniques from control theory, namely high order control barrier functions and Hamilton-Jacobi reachability, to provide inductive bias to aid interpretability, verifiability, and tractability of our approach. In our experiments, we learn an AV safety concept using demonstrations collected from a highway traffic-weaving scenario, compare our learned concept to existing baselines, and showcase its efficacy in evaluating real-world driving logs.

## Introduction

As autonomous vehicle (AV) operations grow, developing appropriate methods for evaluating AV safety becomes ever more imperative. The question of "is a vehicle in an unsafe state?" is relevant for AV system developers, policymakers, and the general public alike (see Figure 1). While *guaranteeing* safety may not be practical in the face of the myriad uncertainties and complexities that come with real-world driving, there is still a broad desire to codify, to some extent, collectively agreed-upon notions of safety....

Towards this goal of building safe and trustworthy AVs, various stakeholders have advanced safety concepts consisting, in general, of two functions mapping world state (e.g., joint state of all agents and environmental context) to (i) a scalar measure of safety, and (ii) a set of allowable (safe) agent actions. Numerous uses of such safety concepts have been proposed throughout AV pipelines, e.g., a criterion to prune away unsafe plans, a safety monitor to determine when evasive action must be taken, a component in the planning objective, or for perception safety evaluation metrics....

### VIII-C Conclusions

We have proposed a data-driven safety concept that is robust yet reflective of real-world driving interaction behaviors. We first learn control sets describing collision avoidance behaviors by leveraging high order control barrier functions, and then use them to constrain the HJ reachability computation used for safety concept synthesis....

### V-B3 HOCBF learning algorithm

### Definition 4 (Relative degree)

## Experiments and Discussion

To address this challenge, we propose designing novel safety concepts by learning from data what are controls, specifically, control sets, that humans operate with when their safety is threatened, and then using these learned control sets to inform AVs of what are reasonable foreseeable behaviors of other agents in safety-critical scenarios. Equipped with such a learned "human behavior collision avoidance model," we perform safety concept synthesis by using robust control theory, specifically Hamilton-Jacobi reachability, as a powerful inductive bias for interpretability, verifiability, and tractability....

Figure 1: Evaluating the safety of an autonomous vehicle (AV) depends on what constitutes as reasonable foreseeable behaviors of other road users....
