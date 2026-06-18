GameFormer: Game-theoretic Modeling and Learning of Transformer-based Interactive Prediction and Planning for Autonomous Driving

Autonomous vehicles operating in complex real-world environments require accurate predictions of interactive behaviors between traffic participants. This paper tackles the interaction prediction problem by formulating it with hierarchical game theory and proposing the GameFormer model for its implementation. The model incorporates a Transformer encoder, which effectively models the relationships between scene elements, alongside a novel hierarchical Transformer decoder structure. At each decoding level, the decoder utilizes the prediction outcomes from the previous level, in addition to the shared environmental context, to iteratively refine the interaction process. Moreover, we propose a learning process that regulates an agent's behavior at the current level to respond to other agents' behaviors from the preceding level. Through comprehensive experiments on large-scale real-world driving datasets, we demonstrate the state-of-the-art accuracy of our model on the Waymo interaction prediction task....

## Introduction

Figure 1: Hierarchical game theoretic modeling of agent interactions. The historical states of agents and maps are encoded as background information; a level-0 agent’s future is predicted independently based on the initial modality query; a level-k agent responds to all other level-(k−1) agents.

Accurately predicting the future behaviors of surrounding traffic participants and making safe and socially-compatible decisions are crucial for modern autonomous driving systems. However, this task is highly challenging due to the complexities arising from road structures, traffic norms, and interactions among road users. In recent years, deep neural network-based approaches have shown remarkable advancements in prediction accuracy and scalability....

## Conclusions

This paper introduces GameFormer, a Transformer-based model that utilizes hierarchical game theory for interactive prediction and planning. Our proposed approach incorporates novel level-$k$ interaction decoders in the Transformer prediction model that iteratively refine the future trajectories of interacting agents. We also implement a learning process that regulates the predicted behaviors of agents based on the prediction results from the previous level....

where $d{( \cdot, \cdot )}$ is the $L_{2}$ distance between the future states ($(x,y)$ positions), $m$ is the mode of the agent $i$, $n$ is the mode of the level-$({k - 1})$ agent $j$. To ensure activation of the repulsive force solely within close proximity, a safety margin is introduced, meaning the loss is only applied to interaction pairs with distances smaller than a threshold.

Agent History Encoding. We use LSTM networks to encode the historical state sequence $S_{p}$ for each agent, resulting in a tensor $A_{p} \in {\mathbb{R}}^{N \times D}$, which contains the past features of all agents. Here, $D$ denotes the hidden feature dimension.

Qualitative results. Fig. 4 illustrates the interaction prediction performance of our approach in several typical scenarios. In the vehicle-vehicle interaction scenario, two distinct situations are captured by our model: vehicle 2 accelerates to take precedence at the intersection, and vehicle 2 yields to vehicle 1. In both cases, our model predicts that vehicle 1 creeps forward to observe the actions of vehicle 2 before executing a left turn....
