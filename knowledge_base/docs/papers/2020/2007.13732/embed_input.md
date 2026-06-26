<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Lane Graph Representations for Motion Forecasting

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a motion forecasting model that exploits a novel structured map representation as well as actor-map interactions. Instead of encoding vectorized maps as raster images, we construct a lane graph from raw map data to explicitly preserve the map structure. To capture the complex topology and long range dependencies of the lane graph, we propose LaneGCN which extends graph convolutions with multiple adjacency matrices and along-lane dilation. To capture the complex interactions between actors and maps, we exploit a fusion network consisting of four types of interactions, actor-to-lane, lane-to-lane, lane-to-actor and actor-to-actor. Powered by LaneGCN and actor-map interactions, our model is able to predict accurate and realistic multi-modal trajectories. Our approach significantly outperforms the state-of-the-art on the large scale Argoverse motion forecasting benchmark.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving has the potential to revolutionize transportation. Self-driving vehicles (SDVs) have to accurately predict the future motions of other traffic participants in order to safely operate. High Definition maps (HD-maps) provide extremely useful geometric and semantic information for motion forecasting, as the behaviors of actors largely depend on the map topology. For example, a vehicle is unlikely to take a left turn when there is not a left turn lane nearby. Effectively exploiting HD maps is essential for motion forecasting models to produce plausible and accurate trajectories.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

First attempts exploit HD maps as heuristics. Actors are first associated with lanes and all candidate motion paths are then generated based on map topology. In this way, the prediction results are constrained by the map. However, this approach can not capture rare and non-compliant behaviours, which while not very likely, might be safety critical.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent works use machine learning to learn semantic representations from maps. To enable HD maps to be processed by neural networks the map data is rasterized to create image-like raster inputs. Map topology is implicitly encoded as lines, masks or colours, which are then processed by a 2D Convolutional Neural Network (CNN). These learned map features were shown to provide useful context information for motion forecasting. However, these approach has two disadvantages. First, the rasterization process inevitably results in information loss. Second, maps have a graph structure with complex topology which 2D convolution may be very inefficient to capture. For example, a lane of interest may extend for a long range in the lane direction. To capture this information, the receptive field has to be very large, covering not only the intended area, but also large areas outside the lane. Furthermore, lane pairs in the same or opposite directions have completely different semantic meanings and dependencies, although the lanes in both pairs are spatially close to each other.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we made three main contributions: Instead of using rasterization, we construct a lane graph from vectorized map data, thus avoiding information loss. We then propose the Lane Graph Convolutional Network (LaneGCN), which effectively captures the complex topology and long range dependencies of the lane graph. Based on LaneGCN, our motion forecasting model captures all possible actor-map interactions. In particular, we represent both actors and lanes as nodes in the graph and use a 1D CNN and LaneGCN to extract the features for the actor and lane nodes respectively, and then exploit spatial attention and another LaneGCN to model four types of interactions: actor-to-lane, lane-to-lane, lane-to-actor and actor-to-actor. We refer the reader to Fig. 1 for an illustration of our approach. We conduct experiments on the large-scale Argoverse motion forecasting benchmark, and show significant improvements over the state-of-the-art.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Lane Graph Representations for Motion Forecasting", "weight": 1.0} -->

In this section, we propose a novel motion forecasting model that learns structured map representations and fuses the information of traffic actors and HD maps taking into account their interactions. In the following, we explain the four modules that compose our model, *i.e*., how to compute actor features with ActorNet, how to represent the map via MapNet, how to fuse the information from both actors and the map with FusionNet, and finally how to predict the final motion forecasting trajectories through the Prediction Header. We refer the reader to Fig. 2 for an illustration of the overall architecture.

<!-- chunk {"id": "body-0008", "role": "body", "section": "ActorNet: Extracting Traffic Participant Representations", "weight": 1.0} -->

We assume actor data is composed of the observed past trajectories of all actors in the scene. Each trajectory is represented as a sequence of displacements $\{{\Delta\mathbf{p}_{- {({T - 1})}}},\ldots,{\Delta\mathbf{p}_{- 1}},{\Delta\mathbf{p}_{0}}\}$, where $\Delta\mathbf{p}_{t}$ is the 2D displacement from time step $t - 1$ to $t$, and $T$ is the trajectory size. All coordinates are defined in the Bird's Eye View (BEV), as this is the space of interest for traffic agents. For trajectories with sizes smaller than $T$, we pad them with zeros. We add a binary $1 \times T$ mask to indicate if the element at each step is padded or not and concatenate it with the trajectory tensor, resulting in an input tensor of size $3 \times T$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "ActorNet: Extracting Traffic Participant Representations", "weight": 1.0} -->

While both CNNs and RNNs can be used for temporal data, here we use an 1D CNN to process the trajectory input for its effectiveness in extracting multi-scale features and efficiency in parallel computing. The output of ActorNet is a temporal feature map, whose element at $t = 0$ is used as the actor feature. The network has $3$ groups/scales of 1D convolutions. Each group consists of $2$ residual blocks, with the stride of the first block as $2$. We then use a Feature Pyramid Network (FPN) to fuse the multi-scale features, and apply another residual block to obtain the output tensor. For all layers, the convolution kernel size is $3$ and the number of output channels is $128$. Layer normalization and the Rectified Linear Unit (ReLU) are used after each convolution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "MapNet: Extracting Structured Map Representation", "weight": 1.0} -->

We use a novel deep model, called MapNet, to learn structured map representations from vectorized map data. This contrasts previous approaches, which encode the map as a raster image and apply 2D convolutions to extract features. MapNet consists of two steps: building a lane graph from vectorized map data; applying our novel LaneGCN to the lane graph to output the map features.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Map Data", "weight": 1.0} -->

In this paper, we adopt a simple form of vectorized map data as our representation of HD maps. Specifically, the map data is represented as a set of lanes and their connectivity. Each lane contains a centerline, *i.e*., a sequence of 2D BEV points, which are arranged following the lane direction (see Fig. 3, top). For any two lanes which are directly reachable, $4$ types of connections are given: predecessor, successor, left neighbour and right neighbour. Given a lane $A$, its predecessor and successor are the lanes which can directly travel to $A$ and from $A$ respectively. Left and right neighbours refer to the lanes which can be directly reached without violating traffic rules. This simple map format provides essential geometric and semantic information for motion forecasting, as vehicles generally plan their routes by reference to lane centerlines and their connectivity.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Lane Graph Construction", "weight": 1.0} -->

Instead of encoding maps as raster images, we derive a lane graph from the map data as the input. In designing the lane graph, we expect its nodes to have a fine resolution. Given any actor location, we query the lane graph and find its nearest nodes to retrieve accurate map information. From this point of view, it is not an optimal choice to directly use the lane centerlines as the nodes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Lane Graph Construction", "weight": 1.0} -->

We refer the reader to Fig. 3 for an example of the lane graph construction. We first define a lane node as the straight line segment formed by any two consecutive points (grey circles in Fig. 3) of the centerline. The location of a lane node is the averaged coordinates of its two end points. Following the connections between lane centerlines, we also derive $4$ connectivity types for the lane nodes, *i.e*., predecessor, successor, left neighbour and right neighbour. For any lane node $A$, its predecessor and successor are defined as the neighbouring lane nodes that can travel to $A$ or from $A$ respectively. Note that one can reach the first lane node of a lane $l_{A}$ from the last lane node of lane $l_{B}$ if $l_{B}$ is the predecessor of $l_{A}$. Left and right neighbours are defined as the spatially closest lane node measured by $\ell_{2}$ distance on the left and on the right neighbouring lane respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Lane Graph Construction", "weight": 1.0} -->

We denote the lane nodes with $V \in {\mathbb{R}}^{N \times 2}$, where $N$ is the number of lane nodes and the $i$-th row of $V$ is the BEV coordinates of the $i$-th node. We represent the connectivity with $4$ adjacency matrices ${\{ A_{i}\}}_{i \in {\{\text{pre},\text{suc},\text{left},\text{right}\}}}$, with $A_{i} \in {\mathbb{R}}^{N \times N}$. We denote $A_{i,{jk}}$, as the element in the $j$-th row and $k$-th column of $A_{i}$. Then $A_{i,{jk}} = 1$ if node $k$ is an $i$-type neighbor of node $j$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "LaneConv Operator", "weight": 1.0} -->

A natural operator to handle lane graphs is the graph convolution. The most widely used graph convolution operator is defined as $Y = {LXW}$, where $X \in {\mathbb{R}}^{N \times F}$ is the node feature, $W \in {\mathbb{R}}^{F \times O}$ is the weight matrix, and $Y \in {\mathbb{R}}^{N \times O}$ is the output. The graph Laplacian matrix $L \in {\mathbb{R}}^{N \times N}$ takes the form $L = {D^{- {1/2}}{({I + A})}D^{- {1/2}}}$, where $I$, $A$ and $D$ are the identity, adjacency and degree matrices respectively. $I$ and $A$ account for self connection and connections between different nodes. All connections share the same weight $W$, and the degree matrix $D$ is used to normalize the output.

<!-- chunk {"id": "body-0016", "role": "body", "section": "LaneConv Operator", "weight": 1.0} -->

However, this vanilla graph convolution is inefficient in our case due to the following reasons. First, it is not clear what kind of node feature will preserve the information in the lane graphs. Second, a single graph Laplacian can not capture the connection type, *i.e*., losing the directional information carried by the connection type. Third, it is not straightforward to handle long range dependencies, *e.g*., akin dilated convolution, within this form of graph convolution. Motivated by these challenges, we introduce our novel specially designed operator for lane graphs, called LaneConv.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Node Feature", "weight": 1.0} -->

We first define the input feature of the lane nodes. Each lane node corresponds to a straight line segment of a centerline. To encode all the lane node information, we need to take into account both the shape (size and orientation) and the location (the coordinates of the center) of the corresponding line segment. We parameterize the node feature as follows, where MLP indicates a multi-layer perceptron and the two subscripts refer to shape and location, respectively. $\text{v}_{i}$ is the location of the $i$-th lane node, *i.e*., the center between two end points, $\mathbf{v}_{i}^{\text{start}}$ and $\mathbf{v}_{i}^{\text{end}}$ are the BEV coordinates of the node $i$'s starting and ending points, and $\mathbf{x}_{i}$ is the $i$-th row of the node feature matrix $X$, denoting the input feature of the $i$-th lane node.

<!-- chunk {"id": "body-0018", "role": "body", "section": "LaneConv", "weight": 1.0} -->

The node feature above only captures the local information of a line segment. To aggregate the topology information of the lane graph at a larger scale, we design the following LaneConv operator where $A_{i}$ and $W_{i}$ are the adjacency and the weight matrices corresponding to the $i$-th connection type respectively. Since we order the lane nodes from the start to the end of the lane, $A_{\text{suc}}$ and $A_{\text{pre}}$ are matrices obtained by shifting the identity matrix one step towards upper right (non-zero superdiagonal) and lower left (non-zero subdiagonal). $A_{\text{suc}}$ and $A_{\text{pre}}$ can propagate information from the forward and backward neighbours whereas $A_{\text{left}}$ and $A_{\text{right}}$ allow information to flow from the cross-lane neighbours.

<!-- chunk {"id": "body-0019", "role": "body", "section": "LaneConv", "weight": 1.0} -->

It is not hard to see that our LaneConv builds on top of the general graph convolution and encodes more geometric (*e.g*., connection type/direction) information. As shown in our experiments this improves over the vanilla graph convolution.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Dilated LaneConv", "weight": 1.0} -->

Since motion forecasting models usually predict the future trajectories of actors with a time horizon of several seconds, actors with high speed could have moved a long distance. Therefore, the model needs to capture the long range dependency along the lane direction for accurate prediction. In regular grid graphs, a dilated convolution operator can effectively capture the long range dependency by enlarging the receptive field. Inspired by this operator, we propose the dilated LaneConv operator to achieve a similar goal for irregular graphs.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Dilated LaneConv", "weight": 1.0} -->

In particular, the $k$-dilation LaneConv operator is defined as follows, where $A_{\text{pre}}^{k}$ is the $k$-th matrix power of $A_{\text{pre}}$. This allows us to directly propagate information along the lane for $k$ steps, with $k$ a hyperparameter. Since $A_{\text{pre}}^{k}$ is highly sparse, one can efficiently compute it using sparse matrix multiplication. Note that the dilated LaneConv is only used for predecessor and successor, as the long range dependency is mostly along the lane direction.

<!-- chunk {"id": "body-0022", "role": "body", "section": "LaneGCN", "weight": 1.0} -->

Based on the dilated LaneConv, we further propose a multi-scale LaneConv operator and use it to build our LaneGCN. Combining Eq. and with multiple dilations, we get a multi-scale LaneConv operator with $C$ dilation sizes as follows where $k_{c}$ is the $c$-th dilation size. We denote $\text{LaneConv}{(k_{1},\cdots,k_{C})}$ this multi-scale layer. The architecture of LaneGCN is shown in Fig. 4. The network is composed of $4$ LaneConv residual blocks, which are the stack of a LaneConv and a linear layer, as well as a shortcut. All layers have 128 feature channels. Layer normalization and ReLU are used after each LaneConv and linear layer.

<!-- chunk {"id": "body-0023", "role": "body", "section": "FusionNet", "weight": 1.0} -->

In this section we propose a network to fuse the information of the actor and lane nodes given by ActorNet and MapNet, respectively. The behaviour of an actor strongly depends on its context, *i.e*., other actors and the map. Although the interactions between actors has been explored by previous work, the interactions between the actors and the map, and map conditioned interactions between actors have received much less attention. In our model, we use spatial attention and LaneGCN to capture a complete set of actor-map interactions (see Fig. 2).

<!-- chunk {"id": "body-0024", "role": "body", "section": "FusionNet", "weight": 1.0} -->

We build a stack of four fusion modules to capture all information flows between actors and lane nodes, *i.e*., actors to lanes (A2L), lanes to lanes (L2L), lanes to actors (L2A) and actors to actors (A2A). Intuitively, A2L introduces real-time traffic information to lane nodes, such as blockage or usage of the lanes. L2L updates lane node features by propagating the traffic information over the lane graph. L2A fuses updated map features with real-time traffic information back to the actors. A2A handles the interactions between actors and produces the output actor features, which are then used by the prediction header for motion forecasting.

<!-- chunk {"id": "body-0025", "role": "body", "section": "FusionNet", "weight": 1.0} -->

We implement L2L using another LaneGCN, which has the same architecture as the one used in our MapNet (see Section 3.2.4). In the following we describe the other three modules in detail. We exploit a spatial attention layer for A2L, L2A and A2A. The attention layer applies to each of the three modules in the same way. Taking A2L as an example, given an actor node $i$, we aggregate the features from its context lane nodes $j$ as follows with $\mathbf{x}_{i}$ the feature of the $i$-th node, $W$ a weight matrix, $\phi$ the composition of layer normalization and ReLU, and $\Delta_{ij} = {\text{MLP}{({\mathbf{v}_{j} - \mathbf{v}_{i}})}}$, where $\mathbf{v}$ denotes the node location. The context nodes are defined to be the lane nodes whose $\ell_{2}$ distance from the actor node $i$ is smaller than a threshold.

<!-- chunk {"id": "body-0026", "role": "body", "section": "FusionNet", "weight": 1.0} -->

The thresholds for A2L, L2A and A2A are set to 7, 6, and 100 meters respectively. Each of A2L, L2A and A2A has two residual blocks, which consist of a stack of the proposed attention layer and a linear layer, as well as a residual connection. All layers have 128 output feature channels.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Prediction Header", "weight": 1.0} -->

Taking the after-fusion actor features as input, a multi-modal prediction header outputs the final motion forecasting. For each actor, it predicts $K$ possible future trajectories and their confidence scores. The header has two branches, a regression branch to predict the trajectory of each mode and a classification branch to predict the confidence score of each mode. For the $m$-th actor, we apply a residual block and a linear layer in the regression branch to regress the $K$ sequences of BEV coordinates: where $\mathbf{p}_{m,i}^{k}$ is the predicted $m$-th actor's BEV coordinates of the $k$-th mode at the $i$-th time step. For the classification branch, we apply an MLP to $\mathbf{p}_{m,T}^{k} - \mathbf{p}_{m,0}$ to get $K$ distance embeddings.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Prediction Header", "weight": 1.0} -->

We then concatenate each distance embedding with the actor feature, apply a residual block and a linear layer to output $K$ confidence scores, $O_{m,\text{cls}} = {(c_{m,0},c_{m,1},\ldots,c_{m,{K - 1}})}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Learning", "weight": 1.0} -->

As all the modules are differentiable, we can train the model in an end-to-end way. We use the sum of classification and regression losses to train the model where $\alpha = 1.0$. Given $K$ predicted trajectories of an actor, we find a positive trajectory $\hat{k}$ that has the minimum final displacement error, *i.e*., the Euclidean distance between the predicted and ground truth locations at the final time step.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Learning", "weight": 1.0} -->

For classification, we use the max-margin loss: where $\epsilon$ is the margin and $M$ is the total number of actors. For regression, we apply the smooth $\ell1$ loss on all predicted time steps: where $\mathbf{p}_{t}^{\ast}$ is the ground truth BEV coordinates at time step $t$, ${\text{reg}{(\mathbf{x})}} = {\sum_{i}{d{(x_{i})}}}$, $x_{i}$ is the $i$-th element of $\mathbf{x}$, and $d{(x_{i})}$ is the smooth $\ell1$ loss defined as where $\parallel x_{i}\parallel$ denotes the $\ell_{1}$ norm of $x_{i}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

We evaluate our model on the large scale Argoverse motion forecasting benchmark, which is publicly available and provides vectorized map data. We first compare our model with the state-of-the-art and show significant improvements in all metrics. We then conduct ablation studies on the architecture and LaneConv operators, and show the advantage of our model design choices. Finally, we show qualitative results and discuss future directions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dataset", "weight": 1.0} -->

Argoverse is a motion forecasting benchmark with over 30K scenarios collected in Pittsburgh and Miami. Each scenario is a sequence of frames sampled at 10 HZ. Each sequence has an interesting object called "agent", and the task is to predict the future locations of agents in a 3 seconds future horizon. The sequences are split into training, validation and test sets, which have 205942, 39472 and 78143 sequences respectively. These splits have no geographical overlap. For the training and validation sets, each sequence lasts for 5 seconds. The first two seconds are used as input data and the other 3 seconds are used as ground truth for models to predict. For the test set, only the first 2 seconds are provided. Each frame is given as the centroid coordinates of all objects in the scene. The actor data is a trajectory of 20 time steps. The map data is a set of lane centerlines and their connectivity. We use both actor and map data in the way described in Sections 3.1 and 3.2.2, without any other preprocessing step. We did not use the other map data such as the rasterized drivable area map and ground height map provided with the benchmark.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Metrics", "weight": 1.0} -->

We employ two extensively used motion forecasting metrics, Average Displacement Error (ADE) is defined as the $\ell_{2}$ distance between the predicted and ground truth locations, averaged over all steps. Final Displacement Error (FDE) is defined as the $\ell_{2}$ distance between the predicted and ground truth locations at the last step in the predicted horizon. As motion forecasting is by nature multi-modal, Argoverse uses the minimum ADE (minADE) and minimum FDE (minFDE) of the top K predictions as the metrics. When K=1, minADE and minFDE are equal to the deterministic ADE and FDE. Argoverse benchmark allows up to 6 predictions, and the online server ranks the entries with minFDE with K=6. We use minADE and minFDE for K=1 and K=6 as the main metrics. When comparing our model with top entries on the leaderboard, we also show Miss Rate (MR), which is the ratio of predictions (the best mode) whose final location is more than 2.0 meters away from the ground truth.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

We use all actors and lanes whose distance from the agent is smaller than 100 meters as the input. The coordinate system in our model is the BEV centered at the agent location at $t = 0$. We use the orientation from the agent location at $t = {- 1}$ to the agent location at $t = 0$ as the positive x axis. We train the model on 4 TITAN-X GPUs using a batch size of 128 with the Adam optimizer with an initial learning rate of $1 \times 10^{- 3}$, which is decayed to $1 \times 10^{- 4}$ at 32 epochs. The training process finishes at 36 epochs and takes about 11.5 hours. All our results are based on the same model, whose architecture and hyper-parameters are described in Section 3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Lane Graph Operators", "weight": 1.0} -->

In Table 3, we show the results of the ablation study on lane graph operators. The baseline model uses the combination of A2L, L2L and L2A. We start from the vanilla graph convolution (GraphConv), and evaluate the effect of adding each component of the LaneConv block (see Figure 4), including the residual block, multi-type connections and dilation. The last row is the LaneConv used in our model (fourth row of Table 2). All these components significantly improve the performance. The residual block only adds about $7\%$ parameters, but effectively facilitates the training. Both multi-type connections and dilation significantly boost the performance, demonstrating the clear advantage of LaneConv over vanilla graph convolution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

In Fig. 5, we compare qualitatively our model to other methods on 4 hard cases. The results of other models are adapted from the slides of Argoverse motion forecasting competition. As the examples are from the test set and we have no access to the labels, in our results we did not show the ground truth trajectory. The first row shows a case where the baselines miss the mode. While the other methods fail to capture the right turn prediction, our model produces a mode which nicely follows the right turn centerline. The second row shows a case where the agent is waiting to perform an unprotected left turn for the first 2 seconds. Due to the lack of actor motion history, maps are important for the model to produce reasonable trajectories. The other models produce divergent trajectories, some of which are non-traffic-rule compliant. In contrast, our model produces reasonable trajectories following the lane topology. The third row shows a case of a car decelerating and coming to a stop at the intersection. Our model produces a mode with more deceleration then the baselines and all the modes reasonably follow the lane. The fourth row shows a case of extreme acceleration.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

None of the models captures this case well, possibly because there is not enough information to make this prediction.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Overall, these results suggest that LaneGCN effectively learns structured map representations, which are used by the model to predict realistic trajectories. One potential way to improve our model is to incorporate more map information into the lane graph. Currently our model uses the centerlines and their connectivity. Other map information, such as traffic lights and traffic signs, provides useful information for motion forecasting, which is well illustrated by the second and third cases in Fig. 5. To account for new map data, our model can be easily extended by introducing new nodes and connections. We will explore this direction in future work.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose a novel motion forecasting model to learn lane graph representations and perform a complete set of actor-map interactions. Instead of using a rasterized map as input, we construct a lane graph from vectorized map data and propose the LaneGCN to extract map topology features. We use spatial attention and the LaneGCN to fuse the information of both actors and lanes. We conduct experiments on the large scale Argoverse motion forecasting benchmark. Our model significantly outperforms the state-of-the-art. In the future we plan to explore the incorporation of other map data.
