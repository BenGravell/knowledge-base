<!-- arxiv-full-text:v1 {"arxiv_id": "2207.05844", "source": "ar5iv"} -->

## Introduction

In this work, we focus on the general task of future behavior prediction of agents (pedestrians, vehicles, cyclists) in real-world driving environments.

Figure 1: The Wayformer architecture as a pair of encoder/decoder Transformer networks. This model takes multimodal scene data as input and produces multimodal distribution of trajectories.

This is an essential task for safe and comfortable human-robot interactions, enabling high-impact robotics applications like autonomous driving.

The modeling needed for such scene understanding is challenging for many reasons. For one, the *output* is highly unstructured and multimodal---*e.g.*, a person driving a vehicle could carry out one of many underlying intents unknown to an observer, and representing a distribution over diverse and disjoint possible futures is required. A second challenge is that the *input* consists of a heterogeneous mix of modalities, including agents' past physical state, static road information (*e.g.* location of lanes and their connectivity), and time-varying traffic light information.

Many previous efforts address how to model the multimodal output, and develop hand-engineered architectures to fuse different input types, each requiring their own preprocessing (*e.g.*, image rasterization ). Here, we focus on the multimodality of the *input space*, and develop a simple yet effective modality-agnostic framework that avoids complex and heterogeneous architectures, and leads to a simpler architecture parameterization. This compact description of a family of architectures results in a simpler design space and allows us to more directly and effectively control for trade-offs in model quality and latency by tuning model computation and capacity.

To keep complexity under control without sacrificing quality or efficiency, we need to find general modeling primitives, which can handle multimodal features that exist in temporal and spatial dimensions concurrently. Recently, several approaches proposed Transformer networks as the networks of choice for motion forecasting problems. While these approaches offer simplified model architectures, they still require domain expertise and excessive modality specific tuning. proposed a stack of cross attention layers sequentially processing one modality at a time. The order in which to process each modality is left to the designer and enumerating all possibilities is combinatorially prohibitive. proposed using separate encoders for each modality, where the type of network and its capacity is open for tuning on a per-modality basis. Then modalities' embeddings are flattened and one single vector is fed to the predictor. While these approaches allow for many degrees of freedom, they increase the search space significantly. Without efficient network architecture search or significant human input and hand engineering, the chosen models will likely be sub-optimal given that a limited amount of the modeling options have been explored.

Our experiments suggest the domain of motion forecasting conforms to Occam's Razor. We show state of the art results with the simplest design choices and making minimal domain specific assumptions, which is in stark contrast to previous work. When tested in simulation and on real AVs, these Wayformer models showed good understanding of the scene.

Our contributions can be summarized as follows: We design a family of models with two basic primitives: a *self-attention encoder*, where we fuse one or more modalities across temporal and spatial dimensions, and a *cross-attention decoder*, where we attend to driving scene elements to produce a diverse set of trajectories.

We study three variations of the scene encoder that differ in how and when different input modalities are fused.

To keep our proposed models within practical real time constraints of motion forecasting, we study two common techniques to speed up self-attention: *factorized attention* and *latent query attention*.

We achieve state-of-the-art results on both WOMD and Argoverse challenges.

## Multimodal Scene Understanding

Driving scenarios consist of multimodal data, such as road information, traffic light state, agent history, and agent interactions. In this section we detail the representation of these modalities in our setup. For readability, we define the following symbols: $A$ denotes the number of modeled ego-agents, $T$ denotes the number of past and current timesteps being considered in the history, with a feature size $D_{m}$. For a modality $m$, we might have a $4^{th}$ dimension ($S_{m}$) representing a "set of contextual objects" (i.e. representations of other road users) for each modeled agent.

### Agent History

contains a sequence of past agent states along with the current state $\lbrack A,T,1,D_{h}\rbrack$. For each timestep $t \in T$, we consider features that define the state of the agent e.g. x, y, velocity, acceleration, bounding box and so . We include a context dimension $S_{h} = 1$ for homogeneity.

### Agent Interactions

The interaction tensor $\lbrack A,T,S_{i},D_{i}\rbrack$ represents the relationship between agents. For each modeled agent $a \in A$, a fixed number of the closest context agents $c_{i} \in S_{i}$ around the modeled agent are considered. These context agents represent the agents which influence the behavior of our modeled agent. The features in $D_{i}$ represent the physical state of each context agents (as in $D_{h}$ above), but transformed into the frame of reference of our ego-agent.

### Roadgraph

The roadgraph $\lbrack A,1,S_{r},D_{r}\rbrack$ contains road features around the agent. Following, we represent roadgraph segments as polylines, approximating the road shape with collections of line segments specified by their endpoints and annotated with type information. We use $S_{r}$ roadgraph segments closest to the modeled agent. Note that there is no time dimension for the road features, but we include a time dimension of 1 for homogeneity with the other modalities.

### Traffic Light State

For each agent $a \in A$, traffic light information $\lbrack A,T,S_{tls},D_{tls}\rbrack$ contains the states of the traffic signals that are closest to that agent. Each traffic signal point ${tls} \in S_{tls}$ has features $D_{tls}$ describing the position and confidence of the signal.

## Wayformer

We design the family of Wayformer models to consist of two main components: a Scene Encoder and a Decoder. The scene encoder is mainly composed of one or more attention encoders that summarize the driving scene. The decoder is a stack of one or more standard transformer cross-attention blocks, in which learned initial queries are fed , and then cross-attended with the scene encoding to produce trajectories. Figure 1 shows the Wayformer model processing multimodal inputs to produce scene encoding. This scene encoding serves as the context for the decoder to generate $k$ possible trajectories covering the multimodality of the output space.

### Frame of Reference

As our model is trained to produce futures for a single agent, we transform the scene into an ego-centric frame of reference by centering and rotating the scene's spatial features around the ego-agent's position and heading at the current time step.

### Projection Layers

Different input modalities may not share the same number of features, so we project them to a common dimension $D$ before concatenating all modalities along the temporal and spatial dimensions \[$S$, $T$\]. We found the simple transformation ${\text{~Projection}{(x_{i})}} = {{relu}{({{\mathbf{W}x_{i}} + b})}}$, where $x_{i} \in {\mathbb{R}}^{D_{m}}$, $b \in {\mathbb{R}}^{D}$, and $\mathbf{W} \in {\mathbb{R}}^{D \times D_{m}}$, to be sufficient. Concretely, given an input of shape $\lbrack A,T,S_{m},D_{m}\rbrack$ we project its last dimension producing a tensor of size $\lbrack A,T,S_{m},D\rbrack$.

Figure 2: Wayformer scene encoder fusing multimodal inputs at different stages. Late fusion dedicates an attention encoder per modality while early fusion process all inputs within one cross modal encoder. Finally, hierarchical fusion combines both the approaches.

### Positional Embeddings

Self-attention is naturally permutation equivariant, therefore, we may think of them as set-encoders rather than sequence encoders. However, for modalities where the data does follow a specific ordering, for example agent state across different time steps, it is beneficial to break permutation equivariance and utilize the sequence information. This is commonly done through positional embeddings. For simplicity, we add learned positional embeddings for all modalities. As not all modalities are ordered, the learned positional embeddings are initially set to zero, letting the model learn if it is necessary to utilize the ordering within a modality.

### Fusion

Once projections and positional embeddings are applied to different modalities, the scene encoder combines the information from all modalities to generate a representation of the environment. Concretely, we aim to learn a scene representation ${{\mathbf{Z}} = {Encoder{({\{ m_{0},m_{1},\ldots,m_{k}\}})}}},$ where $m_{i} \in {\mathbb{R}}^{A \times {({T \times S_{m}})} \times D}$, ${\mathbf{Z}} \in {\mathbb{R}}^{A \times L \times D}$, and $L$ is a hyperparameter.

However, the diversity of input sources makes this integration a non-trivial task. Modalities might not be represented at the same abstraction level or scale: {pixels vs objects}. Therefore, some modalities might require more computation than the others. Splitting compute and parameter count among modalities is application specific and non-trivial to hand-engineer. We attempt to simplify the process by proposing three levels of fusion: {Late, Early, Hierarchical}.

### Late Fusion

This is the most common approach used by motion forecasting models, where each modality has its own dedicated encoder (See Figure 2). We set the width of these encoders to be equal to avoid introducing extra projection layers to their outputs. Moreover, we share the same depth across all encoders to narrow down the exploration space to a manageable scope. Transfer of information across modalities is allowed only in the cross-attention layers of the trajectory decoder.

### Early Fusion

Instead of dedicating a self-attention encoder to each modality, early fusion reduces modality specific parameters to only the projection layers (See Figure 2). In this paradigm, the scene encoder consists of a single self-attention encoder ("Cross-Modal Encoder"), giving the network maximum flexibility in assigning importance across modalities with minimal inductive bias.

### Hierarchical Fusion

As a compromise between the two previous extremes, capacity is split between modality-specific self-attention encoders and the cross-modal encoder in a hierarchical fashion. As done in late fusion, width and depth is common across attention encoders and the cross modal encoder. This effectively splits the depth of the scene encoder between modality specific encoders and the cross modal encoder (Figure 2).

Figure 3: A summary of encoder architectures considered for Wayformer. (a) provides an overview of different encoder blocks and (b) explains how these blocks are arranged to construct the encoder.

### Attention

Transformer networks do not scale well for large multidimensional sequences due to two factors: (a) Self-attention is quadratic in the input sequence length. (b) Position-wise Feed-forward networks are expensive sub-networks. In the following sections, we discuss different speedups to the transformer networks that will help us scale more effectively.

### Multi-Axis Attention

This refers to the default transformer setting which applies self-attention across both spatial and temporal dimensions simultaneously (See Figure 3(b)), which we expect to be the most expensive computationally. Computational complexity of early, late and hierarchical fusions with multi-axis attention is $\mathcal{O}{({S_{m}^{2} \times T^{2}})}$.

### Factorized Attention

Computational complexity of the self-attention is a quadratic in input sequence length. This becomes more pronounced in multi-dimensional sequences, since each extra dimension increases the size of the input by a multiplicative factor. For example, some input modalities have both temporal and spatial dimensions, so the compute cost scales as $\mathcal{O}{({S_{m}^{2} \times T^{2}})}$. To alleviate this, we consider factorized attention along the two dimensions. This exploits the multidimensional structure of input sequences by applying self-attention over each dimension individually, which reduces the cost of self-attention sub-network from $\mathcal{O}{({S_{m}^{2} \times T^{2}})}$ to ${\mathcal{O}{(S_{m}^{2})}} + {\mathcal{O}{(T^{2})}}$. Note that the linear term still tends to dominate if ${\sum_{m}{\mathcal{S}_{m} \times T}}\operatorname{<<}{12 \times D}$.

While factorized attention has the potential to reduce computation compared to multi-axis attention, it introduces complexity in deciding the order in which self-attention is applied to each dimension. In our work, we compare two paradigms of factorized attention (see Figure 3(b)): Sequential Attention: an $N$ layer encoder consists of $N/2$ temporal encoder blocks followed by another $N/2$ spatial encoder blocks.

Interleaved Attention: an $N$ layer encoder consists of temporal and spatial encoder blocks alternating $N/2$ times.

### Latent Query Attention

Another approach to address the computational costs of large input sequences is to use latent queries in the first encoder block, where input $x \in {\mathbb{R}}^{A \times L_{\text{in}} \times D}$ is mapped to latent space $z \in {\mathbb{R}}^{A \times L_{\text{out}} \times D}$. These latents $z \in {\mathbb{R}}^{A \times L_{\text{out}} \times D}$ are processed further by a series of encoder blocks that take in and return arrays in this latent space (see Figure 3(a)). This gives us full freedom to set the latent space resolution, reducing the computational costs of the both self-attention component and the position-wise feedforward network of each block. We set the reduction value $\left( {R = {L_{\text{out}}/L_{\text{in}}}} \right)$ to be a percentage of the input sequence length. Reduction factor $R$ is kept constant across all the attention encoders in late and hierarchical fusions.

### Trajectory Decoding

As our focus is on how to integrate information from different modalities in the encoder, we simply follow the training and output format of, where the Wayformer predictor outputs a mixture of Gaussians to represent the possible trajectories an agent may take. To generate predictions, we use a Transformer decoder which is fed a set of $k$ learned initial queries (${\mathbf{S}}_{i} \in {\mathbb{R}}^{h})_{i = 1}^{k}$ and cross attends them with the scene embeddings from the encoder in order to generate embeddings for each component in the output mixture of Gaussians.

Given the embedding $Y_{i}$ for a particular component of the mixture, we estimate the mixture likelihood with a linear projection layer that produces the unnormalized log-likelihood for the component. To generate the trajectory, we project $Y_{i}$ using another linear layer to output 4 time series: $T_{i} = {\{\mu_{x}^{t},\mu_{y}^{t},{\log\sigma_{x}^{t}},{\log\sigma_{y}^{t}}\}}_{t = 1}^{T}$ corresponding to the means and log-standard deviations of the predicted Gaussian at each timestep.

During training, we follow in decomposing the loss into separate classification and regression losses. Given $k$ predicted Gaussians ${(T_{i})}_{i = 1}^{k}$, let $\hat{i}$ denote the index of the Gaussian with mean closest to the ground truth trajectory $G$. We train the mixture likelihoods on the log likelihood of selecting the index $\hat{i}$, and the Gaussian $T_{\hat{i}}$ to maximize the log-probability of the ground truth trajectory.

### Trajectory Aggregation

If the predictor outputs a GMM with many modes, it can be difficult to reason about a mixture with so many components, and the benchmark metrics often restrict the number of trajectories being considered. During evaluation, we thus apply trajectory aggregation following in order to reduce the number of modes being considered while still preserving the diversity in the original output mixture. We refer the reader to Appendix C and for details of the aggregation scheme.

## Experimental Setup

### Datasets

### Waymo Open Motion Dataset (WOMD)

consists of 1.1M examples time-windowed from 103K 20s scenarios derived from real-world driving in urban and suburban environments. Each example consists of 1 second of history state and 8 seconds of future, which we resample at 5Hz. The object-agent state contains attributes such as position, agent dimensions, velocity and acceleration vectors, orientation, angular velocity, and turn signal state. The long (8s) time horizon in this dataset tests the model's ability to capture a large field of view and scale to a large output space of trajectories.

### Argoverse Dataset

consists of 333K scenarios containing trajectory histories, context agents, and lane centerline inputs for motion prediction. The trajectories are sampled at 10Hz, with 2 seconds of history and a 3-second future prediction horizon.

### Training Details and Hyperparameters

We compare models using competition specific metrics associated with these datasets (see Appendix E). For all metrics, we consider only the top $k = 6$ most likely modes output by our model (after trajectory aggregation) and use only the mean of each mode.

For all experiments, we train models using the AdamW optimizer with an initial learning rate of 2e-4 and linearly decaying to 0 over 1M steps. We train models using 16 TPU v3 cores each, with a batch size of 16 per core, resulting in a total batch size of 256 examples per step.

To vary the capacity of the models, we consider hidden sizes among $\{ 64,128,256\}$ and depths among $\{ 1,2,4\}$ layers. We fix the intermediate size in the feedforward network of the Transformer block to be either 2 or 4 times the hidden size.

Figure 4: MinADE of different fusion models with multi-axis attention.

For our architecture study in Sections (5.1-5.3), each predictor outputs a mixture of Gaussians with $m = 6$ components, with no trajectory aggregation. For our benchmark results in Section 5.4, each predictor outputs a mixture of Gaussians with $m = 64$ components, and we prune the mixture components using the trajectory aggregation scheme described in Section 3.4. For experiments with latent queries, we experiment with reducing the original input resolution to $0.25,0.5$, $0.75$ and $0.9$ times the original sequence length. We include a full description of hyperparameters in Appendix B.

## Results

In this Section, we present experiments that demonstrate the trade-offs of combining different fusion strategies with vanilla self-attention (multi-axis) and more optimized methods such as factorized attention and learned queries. In our ablation studies (Section 5.1-5.3), we trained models with varying capacities (0.3M-20M parameters) for 1M steps on WOMD. We report their inference latency on a current generation GPU, capacity, and minADE as a proxy of quality.

### Multi-Axis Attention

In these experiments, we train Wayformer models on early, hierarchical and late fusion (Section 3.1) in combination with multi-axis attention. In Figure, we show that for models with low latency ($x \leq 16$ ms), late fusion represents an optimal choice. These models are computationally cheap since there is no interaction between modalities during the scene encoding step. Adding the cross modal encoder for hierarchical models unlocks further quality gains for models in the range ($16$ms $< x < 32$ms). Finally, we can see that early fusion can match hierarchical fusion at higher computational cost ($x > 32$ms). We then study the model quality as a function of capacity, as measured by the number of trainable parameters (Figure 4). Small models perform best with early fusion, but as model capacity increases, sensitivity to the choice of fusion decreases dramatically.

### Factorized Attention

To reduce the computational budget of our models, we train models with factorized attention instead of jointly attending to spatial and temporal dimensions together. When combining different modalities together for the cross modal encoder, we first tile the roadgraph modality to a common temporal dimension as the other modalities, then concatenate modalities along the spatial dimension. After the scene encoder, we pool the encodings over the time dimension before feeding to the predictor.

Figure 5: Factorized attention improves quality, but only speeds up late fusion models.

We study two types of factorized attention: sequential, interleaved (Figure 5). First, we observe that both sequential and interleaved factorized attention perform similarly across all types of fusion. Second, we are surprised to see quality gains from applying factorized attention to the early and late fusion cases (Figures 5(a), 5(b)). Finally, we only observe latency improvements for late fusion models (Figure 5(b)), since tiling the road graph to the common temporal dimension in cross-modal encoder used in early and hierarchical fusion significantly increases the count of tokens.

### Latent Queries

In this study, we train models with multi-axis latent query encoders with varying levels of input sequence length reduction in the first layer as shown in Figure 5. The number of the latent queries is calculated to be a percentage of the input size of the Transformer network with $0.0\%$ indicating the baseline models (multi-axis attention with no latent queries as presented in Figure 4).

Figure 6: Latent queries reduce models’ latency without significant degradation to the quality.

Figure 6 shows the results of applying latent queries, which speeds up all fusion models by 2x-16x times with minimal to no quality regression. Early and hierarchical fusion still produce the best quality results, showing the importance of the cross modal interaction stage.

### Benchmark Results

We validate our learnings by comparing Wayformer models to competitive models on popular benchmarks of motion forecasting. We choose early fusion models since they match the quality of the hierarchical models without increased complexity of implementation. Moreover, as models' capacity increases they are less sensitive to the choice of fusion (See Figure 4). We use latent queries since they speed up models without noticeable quality regression and, in some models, we combine them with factorized attention (see Appendix A) since that improves the quality further. We further apply ensembling, a standard practice for producing SOTA results for leaderboard submissions. Full hyperparameters for Wayformer models reported on benchmarks are reported in Appendix D.

When ensembling for WOMD, the model has a single shared encoder but uses $N = 3$ separate Transformer decoders. To merge predictions over the ensemble, we simply combine all mixture components from each predictor to get a total of $N \times 64$ modes, and renormalize the mixture probabilities. We then apply our trajectory aggregation scheme (section 3.4) to the combined mixture distribution to reduce the number of output modes to the desired count $k = 6$.

In Table 1, we present results on the Waymo Open Motion Dataset and Argoverse Dataset. We use the standard metrics used for the each dataset for their respective evaluation (see Appendix E). For the Waymo Open Motion Dataset, both Wayformer early fusion models outperform other models across all metrics; early fusion of input modalities results in better overall metrics independent of the attention structure (multi-axis or factorized attention).

For Argoverse leaderboard, we train 15 replicas each with its own encoder and $N = 10$ transformer decoders. To merge predictions over $N$ decoders we follow the aggregation scheme in section 3.4 to result in $k = 6$ modes for each model. We then ensemble 15 such replicas following the same aggregation scheme (section 3.4) to reduce $N \times 6$ modes to $k = 6$.

Waymo Open Motion Dataset Wayformer Early Fusion Table 1: Wayformer models and select SOTA baselines on Waymo Open Motion Dataset 2021 and Argoverse 2021. * denotes the metric used for leaderboard ranking. LQ denotes latent query.

## Related Work

### Motion prediction architectures

Increasing interest in self-driving applications and the availability of benchmarks has allowed motion prediction models to flourish. Successful modeling techniques fuse multi-modal inputs that represent different static, dynamic, social and temporal aspects of the scene. One class of models draws heavily from the computer vision literature, rendering inputs as a multichannel rasterized top-down image. In this approach, relationships between scene elements are rendered in the top down orthographic plane and modeled via spatio-temporal convolutional networks. However, the localized structure of convolutions is well suited to processing image inputs, but is not effective at capturing the long range spatio-temporal relationships. A popular alternative is to use an entity-centric approach, where agent state history is typically encoded via sequence modeling techniques like RNNs or temporal convolutions. Road elements are approximated with basic primitives (e.g. piece-wise linear segments) which encode pose and semantic information. Modeling relationships between entities is often presented as an information aggregation process, and models employ pooling, soft-attention or graph neural networks. Like our proposed method, several recent models use Transformers, which are a popular state-of-the-art choice for sequence modeling in NLP, and have shown promise in core computer vision tasks such as detection, tracking and classification.

### Iterative cross-attention

A recent approach to encode multi-modal data is to sequentially process one modality at a time. ingests the scene in the order {agent history, nearby agents, map}; they argue that it is computationally expensive to perform self-attention over multiple modalities at once. pre-encodes the agent history and contextual agents through self-attention and cross-attends to the map with agent encodings as queries. The order of self-attention and cross-attention relies heavily on the designer's intuition and has, to our knowledge, not been ablated before.

### Factorized Attention

Flattening high dimensional data leads to long sequences which make self-attention computationally prohibitive. proposed limiting each attention operation to a single axes to alleviate the computational costs and applied this technique to autoregressive generative modeling for images. Similarly, factorize the spatial and temporal dimensions of the video input when constructing their self-attention based classifier. This axis based attention, which gets applied in interleaved fashion across layers, has been adopted in Transformer-based motion forecasting models and graph neural network approaches. The order of applying attention over {temporal, social/spatial} dimensions has been studied with two different common patterns: (a) Temporal first (b) Social/Spatial first. In Section 3.2, we study a 'sequential' mode and contrast it with interleaved mode where interleave dimensions of attention similar to.

### Multimodal Encoding

argued that attending to temporal and spatial dimensions independently leads to loss of information. Moreover, allowing all inputs to self-attend to each other early on the encoding process reduces complexity and the need to handcraft architectures to address the scaling of computation for transformers with the increase in the input sequence length. However, self-attention is known to be computationally expensive for large inputs, and recently there has been huge interest in approaches improving its scalability. For a complete discussion of previous works, we refer the reader to the comprehensive survey. One compelling approach is to use learned latent queries to decouples the number of query vectors of a Transformer encoder from the original input sequence length. This allows us to set the resolution of the Transformer output to arbitrary scales independent of the input, and flexibly tune model computational costs. This approach is appealing since it does not assume any structure in the input and has proven effective in fusing multimodal inputs. We take inspiration from such frameworks and present a study of their benefits when applied to the task of motion forecasting in the self-driving domain.

## Limitations

Scope of the current study is subject to the following limitations: Ego-centric modeling is subject to repeated computations on dense scenes. This can be alleviated by encoding the scene only once in a global frame of reference. Our system input is a sparse abstract state description of the world, which fails to capture some important nuances in highly interactive scenes, e.g., visual cues from pedestrians or fine-granularity contour or wheel angle information for vehicles. Learning perception and prediction end-to-end could unlock improvements. We model the distribution over possible futures independently per agent, and temporally conditionally independent for each agent given intent. These simplifying assumptions allow for efficient computation but fail to fully describe combinatorially many futures. Multi-agent, temporally causal models could show further benefits in interactive situations.
