Learning Lane Graph Representations for Motion Forecasting

We propose a motion forecasting model that exploits a novel structured map representation as well as actor-map interactions. Instead of encoding vectorized maps as raster images, we construct a lane graph from raw map data to explicitly preserve the map structure. To capture the complex topology and long range dependencies of the lane graph, we propose LaneGCN which extends graph convolutions with multiple adjacency matrices and along-lane dilation. To capture the complex interactions between actors and maps, we exploit a fusion network consisting of four types of interactions, actor-to-lane, lane-to-lane, lane-to-actor and actor-to-actor. Powered by LaneGCN and actor-map interactions, our model is able to predict accurate and realistic multi-modal trajectories. Our approach significantly outperforms the state-of-the-art on the large scale Argoverse motion forecasting benchmark.

## Introduction

Autonomous driving has the potential to revolutionize transportation. Self-driving vehicles (SDVs) have to accurately predict the future motions of other traffic participants in order to safely operate. High Definition maps (HD-maps) provide extremely useful geometric and semantic information for motion forecasting, as the behaviors of actors largely depend on the map topology. For example, a vehicle is unlikely to take a left turn when there is not a left turn lane nearby. Effectively exploiting HD maps is essential for motion forecasting models to produce plausible and accurate trajectories.

First attempts exploit HD maps as heuristics. Actors are first associated with lanes and all candidate motion paths are then generated based on map topology. In this way, the prediction results are constrained by the map. However, this approach can not capture rare and non-compliant behaviours, which while not very likely, might be safety critical.

In this paper we made three main contributions: Instead of using rasterization, we construct a lane graph from vectorized map data, thus avoiding information loss. We then propose the Lane Graph Convolutional Network (LaneGCN), which effectively captures the complex topology and long range dependencies of the lane graph. Based on LaneGCN, our motion forecasting model captures all possible actor-map interactions.

## Conclusion

In this paper, we propose a novel motion forecasting model to learn lane graph representations and perform a complete set of actor-map interactions. Instead of using a rasterized map as input, we construct a lane graph from vectorized map data and propose the LaneGCN to extract map topology features. We use spatial attention and the LaneGCN to fuse the information of both actors and lanes. We conduct experiments on the large scale Argoverse motion forecasting benchmark. Our model significantly outperforms the state-of-the-art. In the future we plan to explore the incorporation of other map data.
