VectorNet: Encoding HD Maps and Agent Dynamics from Vectorized Representation

Topics include Multi-agent systems, Vehicles, Neural networks, Convolutional networks, Graph neural networks, Graphs, Datasets, Benchmarks, Learning, VectorNet, HD, ENCODE, FLOPS, Convolutional neural network.

Behavior prediction in dynamic, multi-agent systems is an important problem in the context of self-driving cars, due to the complex representations and interactions of road components, including moving agents (e.g. pedestrians and vehicles) and road context information (e.g. lanes, traffic lights). This paper introduces VectorNet, a hierarchical graph neural network that first exploits the spatial locality of individual road components represented by vectors and then models the high-order interactions among all components. In contrast to most recent approaches, which render trajectories of moving agents and road context information as bird-eye images and encode them with convolutional neural networks (ConvNets), our approach operates on a vector representation. By operating on the vectorized high definition (HD) maps and agent trajectories, we avoid lossy rendering and computationally intensive ConvNet encoding steps. To further boost VectorNet's capability in learning context features, we propose a novel auxiliary task to recover the randomly masked out map entities and agent trajectories based on their context....

## Introduction

This paper focuses on behavior prediction in complex multi-agent systems, such as self-driving vehicles. The core interest is to find a unified representation which integrates the agent dynamics, acquired by perception systems such as object detection and tracking, with the scene context, provided as prior knowledge often in the form of High Definition (HD) maps. Our goal is to build a system which learns to predict the intent of vehicles, which are parameterized as trajectories.

Figure 1: Illustration of the rasterized rendering (left) and vectorized approach (right) to represent high-definition map and agent trajectories.

## Conclusion and future work

We proposed to represent the HD map and agent dynamics with a vectorized representation. We designed a novel hierarchical graph network, where the first level aggregates information among vectors inside a polyline, and the second level models the higher-order relationships among polylines. Experiments on the large scale in-house dataset and the public available Argoverse dataset show that the proposed VectorNet outperforms the ConvNet counterpart while at the same time reducing the computational cost by a large margin. VectorNet also achieves state-of-the-art performance (DE@3s, K=1) on the Argoverse test set....

Once the hierarchical graph network is constructed, we optimize for the multi-task training objective

In practice, $g_{\text{enc}}{( \cdot )}$ is a multi-layer perceptron (MLP) whose weights are shared over all nodes; specifically, the MLP contains a single fully connected layer followed by layer normalization and then ReLU non-linearity. $\varphi_{\text{agg}}{( \cdot )}$ is the maxpooling operation, and $\varphi_{\text{rel}}{( \cdot )}$ is a simple concatenation. An illustration is shown in Figure 3. We stack multiple layers of the subgraph networks, where the weights for $g_{\text{enc}}{( \cdot )}$ are different. Finally, to obtain polyline level features, we compute

Our baseline uses a ConvNet to encode the rasterized images, whose architecture is comparable to IntentNet: we use a ResNet-18 as the ConvNet backbone. Unlike IntentNet, we do not use the LiDAR inputs. To obtain vehicle-centric features, we crop the feature patch around the target vehicle from the convolutional feature map, and average pool over all the spatial locations of the cropped feature map to get a...
