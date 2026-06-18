Learning Online Belief Prediction for Efficient POMDP Planning in Autonomous Driving

Topics include Autonomous driving, POMDPs, Belief-space planning, Belief-state planning, Trajectory prediction.

Learns an online belief-update model for other traffic agents and pairs it with an efficient POMDP planner. The main value is the closed-loop belief-state machinery, which lets predictions adapt as ego intentions and traffic interactions evolve.

Effective decision-making in autonomous driving relies on accurate inference of other traffic agents' future behaviors. To achieve this, we propose an online belief-update-based behavior prediction model and an efficient planner for Partially Observable Markov Decision Processes (POMDPs). We develop a Transformer-based prediction model, enhanced with a recurrent neural memory model, to dynamically update latent belief state and infer the intentions of other agents. The model can also integrate the ego vehicle's intentions to reflect closed-loop interactions among agents, and it learns from both offline data and online interactions. For planning, we employ a Monte-Carlo Tree Search (MCTS) planner with macro actions, which reduces computational complexity by searching over temporally extended action steps. Inside the MCTS planner, we use predicted long-term multi-modal trajectories to approximate future updates, which eliminates iterative belief updating and improves the running efficiency. Our approach also incorporates deep Q-learning (DQN) as a search prior, which significantly improves the performance of the MCTS planner.

## Introduction

Decision-making under uncertainties is crucial for the safety of autonomous driving systems. In particular, human traffic participants' behaviors are a primary source of uncertainties, which imposes significant challenges to the safe navigation of autonomous vehicles (AVs) in real-world scenarios. The Partially Observable Markov Decision Process (POMDP) offers a mathematically sound framework to address this problem.

One challenge is adapting the prediction model to an online and closed-loop setting. We propose a neural memory-based belief update model that optimizes closed-loop prediction performance and learns through online interactions. Specifically, our proposed model uses a Transformer-based encoder to map the observation to latent space. At each time step in online training or testing, we utilize a gated recurrent unit (GRU) model to update the latent belief state of the AV about each tracked agent by considering their last latent states, the current latent observations, and the intention of the ego agent.

Another challenge lies in developing a computationally efficient POMDP planner for AVs. We adopt the Monte-Carlo tree search (MCTS) algorithm and incorporate several enhancements. First, we leverage a macro-action-based method that searches over action sequences or motion primitives, allowing a more in-depth search within a limited computation budget. Additionally, we use predicted multi-modal long-term trajectories from the online prediction model to approximate future transitions for other agents within the planning horizon, which improves computational efficiency while ensuring planning performance.

In summary, we focus on the decision-making under uncertainty problem for AVs, and we have proposed several learning-based enhancements for effective POMDP planning. The core idea of our approach is illustrated in Fig.

We propose a neural memory-based belief update model that provides online and closed-loop agent behavior prediction for AV planning. Refer to Section III-B.

We introduce a macro-action-based MCTS planning method for AVs, which integrates the online prediction model for future approximation and a Q-value function network that acts as a heuristic guide. See Section III-C.
