Learning Online Belief Prediction for Efficient POMDP Planning in Autonomous Driving

Topics include Autonomous driving, POMDPs, Belief-space planning, Belief-state planning, Trajectory prediction.

Learns an online belief-update model for other traffic agents and pairs it with an efficient POMDP planner. The main value is the closed-loop belief-state machinery, which lets predictions adapt as ego intentions and traffic interactions evolve.

Effective decision-making in autonomous driving relies on accurate inference of other traffic agents' future behaviors. To achieve this, we propose an online belief-update-based behavior prediction model and an efficient planner for Partially Observable Markov Decision Processes (POMDPs). We develop a Transformer-based prediction model, enhanced with a recurrent neural memory model, to dynamically update latent belief state and infer the intentions of other agents. The model can also integrate the ego vehicle's intentions to reflect closed-loop interactions among agents, and it learns from both offline data and online interactions. For planning, we employ a Monte-Carlo Tree Search (MCTS) planner with macro actions, which reduces computational complexity by searching over temporally extended action steps. Inside the MCTS planner, we use predicted long-term multi-modal trajectories to approximate future updates, which eliminates iterative belief updating and improves the running efficiency. Our approach also incorporates deep Q-learning (DQN) as a search prior, which significantly improves the performance of the MCTS planner....

## Introduction

Decision-making under uncertainties is crucial for the safety of autonomous driving systems. In particular, human traffic participants' behaviors are a primary source of uncertainties, which imposes significant challenges to the safe navigation of autonomous vehicles (AVs) in real-world scenarios. The Partially Observable Markov Decision Process (POMDP) \[\] offers a mathematically sound framework to address this problem....

Figure 1: Illustration of our proposed planning approach. We utilize a neural memory-based belief update model to continually update other human agents’ intentions over time based on new observations and the AV’s actions. A macro-action-based MCTS planner, guided by a learned Q-value function, searches for the approximately optimal action based on the current belief state.

## Conclusions

We develop an online behavior prediction model for POMDP planning in autonomous driving. Specifically, we propose a recurrent neural belief update model and a macro-action-based MCTS planner guided by deep Q-learning. We introduce an online learning framework, which combines belief update learning and deep Q-learning to guide tree search. We validate our framework in simulated environments based on real-world driving scenarios. The experimental results indicate that our proposed online belief update model can significantly improve temporal consistency and accuracy....

MCTS Algorithm. MCTS consists of several key steps: selection, expansion, evaluation, and backup, and this process is repeated multiple times until a termination condition is reached. We focus on the selection step in the following, and more details about MCTS can be found in \[\]. In the selection step, the nodes are selected according to:

We denote the encoding process as a function with parameters $f_{\theta}$ and the final encoding as $\mathbf{z} \in {\mathbb{R}}^{{({N_{a} + N_{m}})} \times D}$, and we can retrieve $N$ agents of interest from the scene encoding.

We employ the Waymo Open Motion Dataset (WOMD) \[\] to train the models and replay the traffic data for surrounding agents in the MetaDrive \[\] simulator to conduct online training and testing. Additionally, we set the agent behavior to be reactive in the simulator, allowing other agents to perform basic reactive actions, such as avoiding collisions from the rear end of the ego vehicle. Fig....
