<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

VectorNet: Encoding HD Maps and Agent Dynamics from Vectorized Representation

Topics include Multi-agent systems, Vehicles, Neural networks, Convolutional networks, Graph neural networks, Graphs, Datasets, Benchmarks, Learning, VectorNet, HD, ENCODE, FLOPS, Convolutional neural network.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Behavior prediction in dynamic, multi-agent systems is an important problem in the context of self-driving cars, due to the complex representations and interactions of road components, including moving agents (e.g. pedestrians and vehicles) and road context information (e.g. lanes, traffic lights). This paper introduces VectorNet, a hierarchical graph neural network that first exploits the spatial locality of individual road components represented by vectors and then models the high-order interactions among all components. In contrast to most recent approaches, which render trajectories of moving agents and road context information as bird-eye images and encode them with convolutional neural networks (ConvNets), our approach operates on a vector representation. By operating on the vectorized high definition (HD) maps and agent trajectories, we avoid lossy rendering and computationally intensive ConvNet encoding steps. To further boost VectorNet's capability in learning context features, we propose a novel auxiliary task to recover the randomly masked out map entities and agent trajectories based on their context. We evaluate VectorNet on our in-house behavior prediction benchmark and the recently released Argoverse forecasting dataset.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our method achieves on par or better performance than the competitive rendering approach on both benchmarks while saving over 70% of the model parameters with an order of magnitude reduction in FLOPs. It also outperforms the state of the art on the Argoverse dataset.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper focuses on behavior prediction in complex multi-agent systems, such as self-driving vehicles. The core interest is to find a unified representation which integrates the agent dynamics, acquired by perception systems such as object detection and tracking, with the scene context, provided as prior knowledge often in the form of High Definition (HD) maps. Our goal is to build a system which learns to predict the intent of vehicles, which are parameterized as trajectories.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional methods for behavior prediction are rule-based, where multiple behavior hypotheses are generated based on constraints from the road maps. More recently, many learning-based approaches are proposed; they offer the benefit of having probabilistic interpretations of different behavior hypotheses, but require building a representation to encode the map and trajectory information. Interestingly, while the HD maps are highly structured, organized as entities with location (*e.g*. lanes) and attributes (*e.g*. a green traffic light), most of these approaches choose to render the HD maps as color-coded attributes (Figure 1, left), which requires manual specifications; and encode the scene context information with ConvNets, which have limited receptive fields. This raise the question: can we learn a meaningful context representation directly from the structured HD maps?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose to learn a unified representation for multi-agent dynamics and structured scene context directly from their vectorized form (Figure 1, right). The geographic extent of the road features can be a point, a polygon, or a curve in geographic coordinates. For example, a lane boundary contains multiple control points that build a spline; a crosswalk is a polygon defined by several points; a stop sign is represented by a single point. All these geographic entities can be closely approximated as polylines defined by multiple control points, along with their attributes. Similarly, the dynamics of moving agents can also be approximated by polylines based on their motion trajectories. All these polylines can then be represented as sets of vectors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use graph neural networks (GNNs) to incorporate these sets of vectors. We treat each vector as a node in the graph, and set the node features to be the start location and end location of each vector, along with other attributes such as polyline group id and semantic labels. The context information from HD maps, along with the trajectories of other moving agents are propagated to the target agent node through the GNN. We can then take the output node feature corresponding to the target agent to decode its future trajectories.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, to learn competitive representations with GNNs, we observe that it is important to constrain the connectivities of the graph based on the spatial and semantic proximity of the nodes. We therefore propose a hierarchical graph architecture, where the vectors belonging to the same polylines with the same semantic labels are connected and embedded into polyline features, and all polylines are then fully connected with each other to exchange information. We implement the local graphs with multi-layer perceptrons, and the global graphs with self-attention. An overview of our approach is shown in Figure 2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, motivated by the recent success of self-supervised learning from sequential linguistic and visual data, we propose an auxiliary graph completion objective in addition to the behavior prediction objective. More specifically, we randomly mask out the input node features belonging to either scene context or agent trajectories, and ask the model to reconstruct the masked features. The intuition is to encourage the graph networks to better capture the interactions between agent dynamics and scene context.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are the first to demonstrate how to directly incorporate vectorized scene context and agent dynamics information for behavior prediction.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose the hierarchical graph network VectorNet and the node completion auxiliary task.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate the proposed method on our in-house behavior prediction dataset and the Argoverse dataset, and show that our method achieves on par or better performance over a competitive rendering baseline with 70% model size saving and an order of magnitude reduction in FLOPs. Our method also achieves the state-of-the-art performance on Argoverse.

<!-- chunk {"id": "body-0013", "role": "body", "section": "VectorNet approach", "weight": 1.0} -->

This section introduces our VectorNet approach. We first describe how to vectorize agent trajectories and HD maps. Next we present the hierarchical graph network which aggregates local information from individual polylines and then globally over all trajectories and map features. This graph can then be used for behavior prediction.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Representing trajectories and maps", "weight": 1.0} -->

Most of the annotations from an HD map are in the form of splines (*e.g*. lanes), closed shape (*e.g*. regions of intersections) and points (*e.g*. traffic lights), with additional attribute information such as the semantic labels of the annotations and their current states (*e.g*. color of the traffic light, speed limit of the road). For agents, their trajectories are in the form of directed splines with respect to time. All of these elements can be approximated as sequences of vectors: for map features, we pick a starting point and direction, uniformly sample key points from the splines at the same spatial distance, and sequentially connect the neighboring key points into vectors; for trajectories, we can just sample key points with a fixed temporal interval (0.1 second), starting from $t = 0$, and connect them into vectors. Given small enough spatial or temporal intervals, the resulting polylines serve as close approximations of the original map and trajectories.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Representing trajectories and maps", "weight": 1.0} -->

Our vectorization process is a one-to-one mapping between continuous trajectories, map annotations and the vector set, although the latter is unordered. This allows us to form a graph representation on top of the vector sets, which can be encoded by graph neural networks. More specifically, we treat each vector $\mathbf{v}_{i}$ belonging to a polyline $\mathcal{P}_{j}$ as a node in the graph with node features given by

<!-- chunk {"id": "body-0016", "role": "body", "section": "Representing trajectories and maps", "weight": 1.0} -->

where $\mathbf{d}_{i}^{s}$ and $\mathbf{d}_{i}^{e}$ are coordinates of the start and end points of the vector, $\mathbf{d}$ itself can be represented as $(x,y)$ for 2D coordinates or $(x,y,z)$ for 3D coordinates; $\mathbf{a}_{i}$ corresponds to attribute features, such as object type, timestamps for trajectories, or road feature type or speed limit for lanes; $j$ is the integer id of $\mathcal{P}_{j}$, indicating $\mathbf{v}_{i} \in \mathcal{P}_{j}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Representing trajectories and maps", "weight": 1.0} -->

To make the input node features invariant to the locations of target agents, we normalize the coordinates of all vectors to be centered around the location of target agent at its last observed time step. A future work is to share the coordinate centers for all interacting agents, such that their trajectories can be predicted in parallel.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Constructing the polyline subgraphs", "weight": 1.0} -->

To exploit the spatial and semantic locality of the nodes, we take a hierarchical approach by first constructing subgraphs at the vector level, where all vector nodes belonging to the same polyline are connected with each other. Considering a polyline $\mathcal{P}$ with its nodes $\left\{ \mathbf{v}_{1},\mathbf{v}_{2},\ldots,\mathbf{v}_{P} \right\}$, we define a single layer of subgraph propagation operation as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Constructing the polyline subgraphs", "weight": 1.0} -->

where $\mathbf{v}_{i}^{(l)}$ is the node feature for $l$-th layer of the subgraph network, and $\mathbf{v}_{i}^{}$ is the input features $\mathbf{v}_{i}$. Function $g_{\text{enc}}{( \cdot )}$ transforms the individual node features, $\varphi_{\text{agg}}{( \cdot )}$ aggregates the information from all neighboring nodes, and $\varphi_{\text{rel}}{( \cdot )}$ is the relational operator between node $\mathbf{v}_{i}$ and its neighbors.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Constructing the polyline subgraphs", "weight": 1.0} -->

In practice, $g_{\text{enc}}{( \cdot )}$ is a multi-layer perceptron (MLP) whose weights are shared over all nodes; specifically, the MLP contains a single fully connected layer followed by layer normalization and then ReLU non-linearity. $\varphi_{\text{agg}}{( \cdot )}$ is the maxpooling operation, and $\varphi_{\text{rel}}{( \cdot )}$ is a simple concatenation. An illustration is shown in Figure 3. We stack multiple layers of the subgraph networks, where the weights for $g_{\text{enc}}{( \cdot )}$ are different. Finally, to obtain polyline level features, we compute

<!-- chunk {"id": "body-0021", "role": "body", "section": "Constructing the polyline subgraphs", "weight": 1.0} -->

where $\varphi_{\text{agg}}{( \cdot )}$ is again maxpooling.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Constructing the polyline subgraphs", "weight": 1.0} -->

Our polyline subgraph network can be seen as a generalization of PointNet: when we set $\mathbf{d}^{s} = \mathbf{d}^{e}$ and let $\mathbf{a}$ and $\mathbf{l}$ to be empty, our network has the same inputs and compute flow as PointNet. However, by embedding the ordering information into vectors, constraining the connectivity of subgraphs based on the polyline groupings, and encoding attributes as node features, our method is particularly suitable to encode structured map annotations and agent trajectories.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

where $\{\mathbf{p}_{i}^{(l)}\}$ is the set of polyline node features, $\text{GNN}{( \cdot )}$ corresponds to a single layer of a graph neural network, and $\mathcal{A}$ corresponds to the adjacency matrix for the set of polyline nodes.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

The adjacency matrix $\mathcal{A}$ can be provided a heuristic, such as using the spatial distances between the nodes. For simplicity, we assume $\mathcal{A}$ to be a fully-connected graph.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

where $L_{t}$ is the number of the total number of GNN layers, and $\varphi_{\text{traj}}{( \cdot )}$ is the trajectory decoder. For simplicity, we use an MLP as the decoder function. More advanced decoders, such as the anchor-based approach from MultiPath, or variational RNNs can be used to generate diverse trajectories; these decoders are complementary to our input encoder.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

We use a single GNN layer in our implementation, so that during inference time, only the node features corresponding to the target agents need to be computed. However, we can also stack multiple layers of $\text{GNN}{( \cdot )}$ to model higher-order interactions when needed.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

To encourage our global interaction graph to better capture interactions among different trajectories and map polylines, we introduce an auxiliary graph completion task. During training time, we randomly mask out the features for a subset of polyline nodes, *e.g*. $\mathbf{p}_{i}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

where $\varphi_{\text{node}}{( \cdot )}$ is the node feature decoder implemented as an MLP. These node feature decoders are not used during inference time.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

Recall that $\mathbf{p}_{i}$ is a node from a fully-connected, unordered graph. In order to identify an individual polyline node when its corresponding feature is masked out, we compute the minimum values of the start coordinates from all of its belonging vectors to obtain the identifier embedding $\mathbf{p}_{i}^{\text{id}}$. The inputs node features then become

<!-- chunk {"id": "body-0030", "role": "body", "section": "Global graph for high-order interactions", "weight": 1.0} -->

Our graph completion objective is closely related to the widely successful BERT method for natural language processing, which predicts missing tokens based on bidirectional context from discrete and sequential text data. We generalize this training objective to work with unordered graphs. Unlike several recent methods (*e.g*. ) that generalizes the BERT objective to unordered image patches with pre-computed visual features, our node features are jointly optimized in an end-to-end framework.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Overall framework", "weight": 1.0} -->

Once the hierarchical graph network is constructed, we optimize for the multi-task training objective

<!-- chunk {"id": "body-0032", "role": "body", "section": "Overall framework", "weight": 1.0} -->

where $\mathcal{L}_{\text{traj}}$ is the negative Gaussian log-likelihood for the groundtruth future trajectories, $\mathcal{L}_{\text{node}}$ is the Huber loss between predicted node features and groundtruth masked node features, and $\alpha = 1.0$ is a scalar that balances the two loss terms. To avoid trivial solutions for $\mathcal{L}_{\text{node}}$ by lowering the magnitude of node features, we L2 normalize the polyline node features before feeding them to the global graph network.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Overall framework", "weight": 1.0} -->

Our predicted trajectories are parameterized as per-step coordinate offsets, starting from the last observed location. We rotate the coordinate system based on the heading of the target vehicle at the last observed location.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we first describe the experimental settings, including the datasets, metrics and rasterized + ConvNets baseline. Secondly, comprehensive ablation studies are done for both the rasterized baseline and VectorNet. Thirdly, we compare and discuss the computation cost, including FLOPs and number of parameters. Finally, we compare the performance with state-of-the-art methods.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Datasets", "weight": 1.0} -->

We report results on two vehicle behavior prediction benchmarks, the recently released Argoverse dataset and our in-house behavior prediction dataset.\
Argoverse motion forecasting is a dataset designed for vehicle behavior prediction with trajectory histories. There are 333K 5-second long sequences split into 211K training, 41K validation and 80K testing sequences. The creators curated this dataset by mining interesting and diverse scenarios, such as yielding for a merging vehicle, crossing an intersection, etc. The trajectories are sampled at 10Hz, with (0, 2\] seconds are used as observation and (2, 5\] seconds for trajectory prediction. Each sequence has one "interesting" agent whose trajectory is the prediction target. In addition to vehicle trajectories, each sequence is also associated with map information. The future trajectories of the test set are held out. Unless otherwise mentioned, our ablation study reports performance on the validation set.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Datasets", "weight": 1.0} -->

In-house dataset is a large-scale dataset collected for behavior prediction. It contains HD map data, bounding boxes and tracks obtained with an automatic in-house perception system, and manually labeled vehicle trajectories. The total number of vehicle trajectories are 2.2M and 0.55M for train and test sets. Each trajectory has a length of 4 seconds, where the (0, 1\] second is the history trajectory used as observation, and (1, 4\] seconds are the target future trajectories to be evaluated. The trajectories are sampled from real world vehicles' behaviors, including stationary, going straight, turning, lane change and reversing, and roughly preserves the natural distribution of driving scenarios. For the HD map features, we include lane boundaries, stop/yield signs, crosswalks and speed bumps.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Datasets", "weight": 1.0} -->

For both datasets, the input history trajectories are derived from automatic perception systems and are thus noisy. Argoverse's future trajectories are also machine generated, while In-house has manually labeled future trajectories.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Metrics", "weight": 1.0} -->

For evaluation we adopt the widely used Average Displacement Error (ADE) computed over the entire trajectories and the Displacement Error at $t$ (DE@$t$s) metric, where $t \in {\{ 1.0,2.0,3.0\}}$ seconds. The displacements are measured in meters.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Baseline with rasterized images", "weight": 1.0} -->

We render $N$ consecutive past frames, where $N$ is 10 for the in-house dataset and 20 for the Argoverse dataset. Each frame is a 400$\times$`<!-- -->`{=html}400$\times$`<!-- -->`{=html}3 image, which has road map information and the detected object bounding boxes. 400 pixels correspond to 100 meters in the in-house dataset, and 130 meters in the Argoverse dataset. Rendering is based on the position of self-driving vehicle in the last observed frame; the self-driving vehicle is placed at the coordinate location in in-house dataset, and in Argoverse dataset. All $N$ frames are stacked together to form a 400$\times$`<!-- -->`{=html}400$\times$`<!-- -->`{=html}3N image as model input.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Baseline with rasterized images", "weight": 1.0} -->

Our baseline uses a ConvNet to encode the rasterized images, whose architecture is comparable to IntentNet: we use a ResNet-18 as the ConvNet backbone. Unlike IntentNet, we do not use the LiDAR inputs. To obtain vehicle-centric features, we crop the feature patch around the target vehicle from the convolutional feature map, and average pool over all the spatial locations of the cropped feature map to get a single vehicle feature vector. We empirically observe that using a deeper ResNet model or rotating the cropped features based on target vehicle headings do not lead to better performance. The vehicle features are then fed into a fully connected layer (as used by IntentNet) to predict the future coordinates in parallel. The model is optimized on 8 GPUs with synchronous training. We use the Adam optimizer and decay the learning rate every 5 epochs by a factor of 0.3. We train the model for a total of 25 epochs with an initial learning rate of 0.001.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baseline with rasterized images", "weight": 1.0} -->

To test how convolutional receptive fields and feature cropping strategies influence the performance, we conduct ablation study on the network receptive field, feature cropping strategy and input image resolutions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VectorNet with vectorized representations", "weight": 1.0} -->

To ensure a fair comparison, the vectorized representation takes as input the same information as the rasterized representation. Specifically, we extract exactly the same set of map features as when rendering. We also make sure that the visible road feature vectors for a target agent are the same as in the rasterized representation. However, the vectorized representation does enjoy the benefit of incorporating more complex road features which are non-trivial to render.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VectorNet with vectorized representations", "weight": 1.0} -->

Unless otherwise mentioned, we use three graph layers for the polyline subgraphs, and one graph layer for the global interaction graph. The number of hidden units in all MLPs are fixed to 64. The MLPs are followed by layer normalization and ReLU nonlinearity. We normalize the vector coordinates to be centered around the location of target vehicle at the last observed time step. Similar to the rasterized model, VectorNet is trained on 8 GPUs synchronously with Adam optimizer. The learning rate is decayed every 5 epochs by a factor of 0.3, we train the model for a total of 25 epochs with initial learning rate of 0.001.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VectorNet with vectorized representations", "weight": 1.0} -->

To understand the impact of the components on the performance of VectorNet, we conduct ablation studies on the type of context information, *i.e*. whether to use only map or also the trajectories of other agents as well as the impact of number of graph layers for the polyline subgraphs and global interaction graphs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablation study for the ConvNet baseline", "weight": 1.0} -->

We conduct ablation studies on the impact of ConvNet receptive fields, feature cropping strategies, and the resolution of the rasterized images.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation study for the ConvNet baseline", "weight": 1.0} -->

Impact of receptive fields. As behavior prediction often requires capturing long range road context, the convolutional receptive field could be critical to the prediction quality. We evaluate different variants to see how two key factors of receptive fields, convolutional kernel sizes and feature cropping strategies, affect the prediction performance. The results are shown in Table 1. By comparing kernel size 3, 5 and 7 at 400$\times$`<!-- -->`{=html}400 resolution, we can see that a larger kernel size leads to slight performance improvement. However, it also leads to quadratic increase of the computation cost. We also compare different cropping methods, by increasing the crop size or cropping along the vehicle trajectory at all observed time steps. From the 3rd to 6th rows of Table 1 we can see that a larger crop size (3 v.s. 1) can significantly improve the performance, and cropping along observed trajectory also leads to better performance. This observation confirms the importance of receptive fields when rasterized images are used as inputs. It also highlights its limitation, where a carefully designed cropping strategy is needed, often at the cost of increased computation cost.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation study for the ConvNet baseline", "weight": 1.0} -->

Impact of rendering resolution. We further vary the resolutions of rasterized images to see how it affects the prediction quality and computation cost, as shown in the first three rows of Table 1. We test three different resolutions, including $400 \times 400$ (0.25 meter per pixel), $200 \times 200$ (0.5 meter per pixel) and $100 \times 100$ (1 meter per pixel). It can be seen that the performance increases generally as the resolution goes up. However, for the Argoverse dataset we can see that increasing the resolution from 200$\times$`<!-- -->`{=html}200 to 400$\times$`<!-- -->`{=html}400 leads to slight drop in performance, which can be explained by the decrease of effective receptive field size with the fixed 3$\times$`<!-- -->`{=html}3 kernel. We discuss the impact on computation cost of these design choices in Section 4.4.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation study for VectorNet", "weight": 1.0} -->

Impact of input node types. We study whether it is helpful to incorporate both map features and agent trajectories for VectorNet. The first three rows in Table 2 correspond to using only the past trajectory of the target vehicle ("none" context), adding only map polylines ("map"), and finally adding trajectory polylines ("map + agents"). We can clearly observe that adding map information significantly improves the trajectory prediction performance. Incorporating trajectory information furthers improves the performance.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Ablation study for VectorNet", "weight": 1.0} -->

Impact of node completion loss. The last four rows of Table 2 compares the impact of adding the node completion auxiliary objective. We can see that adding this objective consistently helps with performance, especially at longer time horizons.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ablation study for VectorNet", "weight": 1.0} -->

Impact on the graph architectures. In Table 3 we study the impact of depths and widths of the graph layers on trajectory prediction performance. We observe that for the polyline subgraph three layers gives the best performance, and for the global graph just one layer is needed. Making the MLPs wider does not lead to better performance, and hurts for Argoverse, presumably because it has a smaller training dataset. Some example visualizations on predicted trajectory and lane attention are shown in Figure 4.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablation study for VectorNet", "weight": 1.0} -->

Comparison with ConvNets. Finally, we compare our VectorNet with the best ConvNet model in Table 4. For the in-house dataset, our model achieves on par performance with the best ResNet model, while being much more economically in terms of model size and FLOPs. For the Argoverse dataset, our approach significantly outperforms the best ConvNet model with 12% reduction in DE@3. We observe that the in-house dataset contains a lot of stationary vehicles due to its natural distribution of driving scenarios; those cases can be easily solved by ConvNets, which are good at capturing local pattern. However, for the Argoverse dataset where only "interesting" cases are preserved, VectorNet outperforms the best ConvNet baseline by a large margin; presumably due to its ability to capture long range context information via the hierarchical graph network.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation study for VectorNet", "weight": 1.0} -->

#Param

<!-- chunk {"id": "body-0053", "role": "body", "section": "Comparison of FLOPs and model size", "weight": 1.0} -->

We now compare the FLOPs and model size between ConvNets and VectorNet, and their implications on performance. The results are shown in Table 4. The prediction decoder is not counted for FLOPs and number of parameters. We can see that the FLOPs of ConvNets increase quadratically with the kernel size and input image size; the number of parameters increases quadratically with the kernel size. As we render the images centered at the self driving vehicle, the feature map can be reused among multiple targets, so the FLOPs of the backbone part is a constant number. However, if the rendered images are target-centered, the FLOPs increases linearly with the number of targets. For VectorNet, the FLOPs depends on the number of vector nodes and polylines in the scene. For the in-house dataset, the average number of road map polylines is 17 containing 205 vectors; the average number of road agent polylines is 59 containing 590 vectors. We calculate the FLOPs based on these average numbers.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Comparison of FLOPs and model size", "weight": 1.0} -->

Note that, as we need to re-normalize the vector coordinates and re-compute the VectorNet features for each target, the FLOPs increase linearly with the number of predicting targets ($n$ in Table 4).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Comparison of FLOPs and model size", "weight": 1.0} -->

Comparing R18-k3-t-r400 (the best model among ConvNets) with VectorNet, VectorNet significantly outperforms ConvNets. For computation, ConvNets consumes 200+ times more FLOPs than VectorNet (10.56G vs 0.041G) for a single agent; considering that the average number of vehicles in a scene is around 30 (counted from the in-house dataset), the actual computation consumption of VectorNet is still much smaller than that of ConvNets. At the same time, VectorNet needs 29% of the parameters of ConvNets (72K vs 246K). Based on the comparison, we can see that VectorNet can significantly boost the performance while at the same time dramatically reducing computation cost.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison with state-of-the-art methods", "weight": 1.0} -->

Finally, we compare VectorNet with several baseline approaches and some state-of-the-art methods on the Argoverse test set. We report K=1 results (the most likely predictions) in Table 5. The baseline approaches include the constant velocity baseline, nearest neighbor retrieval, and LSTM encoder-decoder. The state-of-the-art approaches are the winners of Argoverse Forecasting Challenge. It can be seen that VectorNet improves the state-of-the-art performance from 4.17 to 4.01 for the DE@3s metric when K=1.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

We proposed to represent the HD map and agent dynamics with a vectorized representation. We designed a novel hierarchical graph network, where the first level aggregates information among vectors inside a polyline, and the second level models the higher-order relationships among polylines. Experiments on the large scale in-house dataset and the public available Argoverse dataset show that the proposed VectorNet outperforms the ConvNet counterpart while at the same time reducing the computational cost by a large margin. VectorNet also achieves state-of-the-art performance (DE@3s, K=1) on the Argoverse test set. A natural next step is to incorporate the VectorNet encoder with a multi-modal trajectory decoder (e.g. ) to generate diverse future trajectories.
