Trajectron++: Dynamically-Feasible Trajectory Forecasting with Heterogeneous Data

Topics include Trajectory prediction, Motion forecasting, Multi-agent prediction, Graph neural networks, Heterogeneous data, Probabilistic prediction, Conditional variational autoencoder.

Extends Trajectron with dynamic feasibility constraints and heterogeneous input data (HD maps, agent types), using a CVAE-based graph recurrent network to produce multi-modal trajectory distributions for multiple interacting agents simultaneously.

Reasoning about human motion is an important prerequisite to safe and socially-aware robotic navigation. As a result, multi-agent behavior prediction has become a core component of modern human-robot interactive systems, such as self-driving cars. While there exist many methods for trajectory forecasting, most do not enforce dynamic constraints and do not account for environmental information (e.g., maps). Towards this end, we present Trajectron++, a modular, graph-structured recurrent model that forecasts the trajectories of a general number of diverse agents while incorporating agent dynamics and heterogeneous data (e.g., semantic maps). Trajectron++ is designed to be tightly integrated with robotic planning and control frameworks; for example, it can produce predictions that are optionally conditioned on ego-agent motion plans. We demonstrate its performance on several challenging real-world trajectory forecasting datasets, outperforming a wide array of state-of-the-art deterministic and generative methods.

## Introduction

Predicting the future behavior of humans is a necessary part of developing safe human-interactive autonomous systems. Humans can naturally navigate through many social interaction scenarios because they have an intrinsic "theory of mind," which is the capacity to reason about other people's actions in terms of their mental states. As a result, imbuing autonomous systems with this capability could enable more informed decision making and proactive actions to be taken in the presence of other intelligent agents, e.g., in human-robot interaction scenarios....

Figure 1: Exemplary road scene depicting pedestrians crossing a road in front of a vehicle which may continue straight or turn right. The graph representation of the scene is shown on the ground, where each agent and their interactions are represented as nodes and edges, visualized as white circles and dashed black lines, respectively. Arrows depict potential future agent velocities, with colors representing different high-level future behavior modes.

## Conclusion

In this work, we present *Trajectron++*, a generative multi-agent trajectory forecasting approach which uniquely addresses our desiderata for an open, generally-applicable, and extensible framework. It can incorporate heterogeneous data beyond prior trajectory information and is able to produce future-conditional predictions that respect dynamics constraints, all while producing full probability distributions, which are especially useful in downstream robotic tasks such as motion planning, decision making, and control....

4\. *Distribution*: Due to the use of a discrete latent variable and Gaussian output structure, the model can provide an analytic output distribution by directly computing ${p{({\mathbf{y} \mid \mathbf{x}})}} = {\sum_{z \in Z}{p_{\psi}{({\mathbf{y} \mid {\mathbf{x},z}})}p_{\theta}{({z \mid \mathbf{x}})}}}$.

Encoding Agent Interactions. To model neighboring agents' influence on the modeled agent, *Trajectron++* encodes graph edges in two steps. First, edge information is aggregated from neighboring agents of the same semantic class. In this work, an element-wise sum is used as the aggregation operation. We choose to combine features in this way rather than with concatenation or an average to handle a variable number of neighboring nodes with a fixed architecture while preserving count information....
