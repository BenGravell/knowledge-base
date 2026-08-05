<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

OpenSGA: Efficient 3D Scene Graph Alignment in the Open World

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Scene graph alignment establishes object correspondences between two 3D scene graphs constructed from partially overlapping observations. This enables efficient scene understanding and object-level relocalization when a robot revisits a place, as well as global map fusion across multiple agents. Such capabilities are essential for robots that require long-term memory for long-horizon tasks involving interactions with the environment. Existing approaches mainly focus on subscan-to-subscan (S2S) alignment and depend heavily on geometric point-cloud features, leaving frame-to-scan (F2S) alignment and open-set vision-language features underexplored. In addition, existing datasets for scene graph alignment remain small-scale with limited object diversity, constraining systematic training and evaluation. We present a unified and efficient scene graph alignment framework that predicts object correspondences by fusing vision-language, textual, and geometric features with spatial context. The framework comprises modules such as a distance-gated spatial attention encoder, a minimum-cost-flow-based allocator, and a global scene embedding generator to achieve accurate alignment even under large coordinate discrepancies.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We further introduce ScanNet-SG, a large-scale dataset generated via an automated annotation pipeline with over 700k samples, covering 509 object categories from ScanNet labels and over 3k categories from GPT-4o-based tagging. Experiments show that our method achieves the best overall performance on both F2S and S2S tasks, substantially outperforming existing scene graph alignment methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

3D scene graphs (Armeni et al. ) are emerging as a powerful representation for embodied agents operating in open-world environments, as they provide a compact and scalable abstraction that integrates semantic, geometric, and spatial information about objects. A typical 3D scene graph models the environment as nodes corresponding to objects and edges encoding relationships between them. This structured representation has demonstrated increasing value across a wide range of robotics tasks, including open-world navigation (Liu et al.; Dai et al.; Devarakonda et al.; Tang et al. ), mobile manipulation (Gu et al.; Honerkamp et al.; Rana et al. ), simultaneous localization and mapping (SLAM) (Bavle et al.; Peterson et al.; Liu et al. ), and high-level scene understanding and reasoning (Ge et al.; Gorlo et al. ).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many of these applications, robots must continuously integrate observations across time and across agents by revisiting previously observed places and maintaining a consistent object-level representation. This requires identifying shared objects across scene graphs of the same environment despite viewpoint changes and partial overlap, which is formalized as the scene graph alignment problem (Sarkar et al. ) and remains challenging due to viewpoint-dependent appearance variation, partial observations, and the diverse set of objects encountered in real-world environments.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, scene graph alignment arises in two complementary settings: frame-to-scan (F2S) alignment, which aligns a partial observation (e.g., a single RGB-D frame) to a global scan-level scene graph under limited visible context, and subscan-to-subscan (S2S) alignment, which aligns two partial reconstructions (e.g., subscans / submaps) captured from different viewpoints, time periods, or agents. F2S is particularly useful for scene understanding and object relocalization when a robot revisits a place or resumes operation after charging or recovery, and must quickly align a partial observation to its global map. S2S is particularly useful for global map fusion, allowing a single robot or multiple agents to align and merge independently built submaps.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some recent works (Sarkar et al.; Xie et al.; Liu et al.; Singh et al. ) have started to formalize this problem, demonstrating scene graph alignment as a key primitive for single or multiple robot mapping and navigation. However, these works remain limited in task coverage, matching strategies, and dataset scale, which constrains systematic evaluation in robotics settings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(1\) Tasks: Although existing methods have been proposed for the S2S alignment, the F2S alignment setting is still underexplored. SceneGraphLoc (Miao et al. ) introduces a cross-modal localization method for the F2S task, but focuses on room-level coarse localization rather than object-level node alignment.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(2\) Matching methods: Most approaches rely heavily on geometric registration cues from point clouds, which are unreliable under partial observations due to sparse overlap and viewpoint-dependent occlusions. Although some methods incorporate semantic embeddings (Liu et al.; Singh et al. ), the potential of modern vision--language models (VLMs) derived open-set object features remains underexplored for robust scene graph alignment.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(3\) Datasets: Current datasets do not provide large-scale, diverse open-set object alignment data. For instance, SGAligner (Sarkar et al. ) constructs a benchmark with 17k samples on 3D SSG (Wald et al. ), but the label space remains limited to 160 classes. In contrast, SG-Reg (Liu et al. ) includes a broader open-set vocabulary but releases only 100 alignment samples. These limitations motivate a new large-scale dataset and learning-based alignment framework that support open-world objects under partial and cross-view overlap in both S2S and F2S settings.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose an efficient scene graph alignment framework that fuses VLM features from GroundingDINO (Liu et al. ), BERT features (Reimers and Gurevych ), and 3D bounding box features with spatial context to predict correspondences between two scene graphs. The framework incorporates a distance-gated spatial attention (DGSA) encoder for contextual feature fusion, a matching score predictor with lightweight and high-performance variants, and a minimum-cost-flow (MCF)--based allocator for many-to-one matching. A learnable class embedding is further introduced to facilitate scalable alignment in big multi-scene environments. To enable large-scale training and evaluation, we also develop an automated annotation pipeline that generates open-set 3D scene graphs from RGB-D images and poses by integrating foundation models with point cloud processing tools. Applying this pipeline to ScanNet (Dai et al. ), we construct a dataset supporting both F2S and S2S alignment tasks, in which each object node is enriched with multimodal attributes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Figure 1 presents the dataset and representative F2S and S2S alignment results generated by the high-performance variant of our model.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contributions include: We introduce an end-to-end 3D scene graph alignment framework for object-level correspondence prediction, enabling robust alignment under partial observations and viewpoint changes. Compared with baseline methods, our approach improves accuracy by 6.4%--13.7% and F1 score by 4.1%--11.2% in different test groups. Relative to the state-of-the-art method that also requires training, our framework reduces both training and inference time by at least 60% while maintaining superior performance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a distance-gated spatial attention encoder to capture node context under large coordinate discrepancies, an MCF-based allocator for many-to-one association, and a global embedding module for efficient matching across multi-scene environments. Together, these components improve alignment accuracy on both F2S and S2S tasks.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop an automated annotation pipeline for constructing 3D scene graphs enriched with textual and VLM features. Building on this pipeline, we introduce ScanNet-SG, a large-scale dataset and benchmark that supports both F2S and S2S alignment tasks in indoor environments. ScanNet-SG contains over 700k annotated alignment samples, making it approximately 45× larger than existing datasets, and covers more than 500 object classes in the SG-509 subset and 3k classes in the SG-GPT subset, representing 3× and 18× increases in category diversity, respectively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also tested using the predicted correspondences to support downstream point cloud registration, demonstrating their practical utility for registering point clouds with low overlap ratios. We release both lightweight and high-performance models of our method to support different efficiency--accuracy trade-offs.

<!-- chunk {"id": "body-0017", "role": "body", "section": "3D Scene Graph", "weight": 1.0} -->

In recent years, 3D scene graphs have emerged as a tool for environment representation, encoding perceptually relevant elements in a graph, where nodes correspond to objects or regions, and edges encode relationships such as spatial or semantic interactions (Armeni et al. ). Each node is often associated with rich semantic and geometric attributes, such as semantic labels, text embeddings, point clouds, 3D bounding boxes, and other node-level properties. As a compact and scalable environment representation (Gu et al.; Hughes et al. ), 3D scene graphs have recently gained significant attention in robotics.

<!-- chunk {"id": "body-0018", "role": "body", "section": "3D Scene Graph", "weight": 1.0} -->

They have been used for open-world navigation and mobile manipulation (Gu et al.; Honerkamp et al.; Rana et al.; Liu et al.; Dai et al.; Devarakonda et al.; Tang et al.; Chen et al. ), as well as to improve the accuracy of SLAM (Bavle et al.; Peterson et al. ), infer the location of unseen objects (Ge et al. ), perform visual relocalization (Oliveira et al. ), predict long-term human trajectories (Gorlo et al. ), and support scene generation (Liu et al. ). These applications highlight the versatility of 3D scene graphs as a unified high-level representation for perception, decision-making, and planning.

<!-- chunk {"id": "body-0019", "role": "body", "section": "3D Scene Graph", "weight": 1.0} -->

Hydra (Hughes et al. ) enables real-time hierarchical scene graph construction from RGB-D data by integrating SLAM, object detection, and geometric verification, while Hydra-Multi (Chang et al. ) extends this capability to collaborative multi-robot mapping through hierarchical graph fusion. With the emergence of foundation models, such as VLMs (Liu et al.; Radford et al.; OpenAI ) and segmentation models such as Segment Anything (Kirillov et al.; Zhao et al. ), recent works have explored building open-world 3D scene graphs that support open-set object categories (Koch et al.; Chen et al.; Maggio et al.; Zhang et al.; Wu et al.; Strader et al.; Olivastri et al.; Liu et al. ). These methods typically use SLAM for localization and dense geometric reconstruction, while VLMs and segmentation models are used to detect object instances, associate geometric points with each node, and infer spatial or semantic relationships between nearby nodes to construct graph edges. We do not focus on real-time scene graph construction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "3D Scene Graph", "weight": 1.0} -->

Instead, we propose an offline pipeline to build scene graphs for generating training and evaluation data for scene graph alignment. Our primary focus is on the scene graph alignment described in the following sections.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Scene Graph Alignment", "weight": 1.0} -->

Scene graph alignment aims to establish correspondences between nodes in two scene graphs that represent partially overlapping observations of the same environment (Sarkar et al. ). Unlike geometric registration, which focuses on estimating spatial transformations, scene graph alignment operates at the object level by matching nodes based on semantic, geometric, and relational attributes. Accurate alignment is critical for robotics applications, such as localization (Bavle et al.; Peterson et al. ) or relocalization (Oliveira et al. ), long-term or multi-gent mapping (Liu et al. ), and downstream point cloud registration (Sarkar et al.; Xie et al. ), where reliable object correspondence matters.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Scene Graph Alignment", "weight": 1.0} -->

SGAligner (Sarkar et al. ) first formalized scene graph alignment by encoding object point clouds as node features and uses graph attention networks to aggregate spatial and structural context from neighboring nodes, followed by contrastive learning to predict correspondences. SG-PGM (Xie et al. ) further improves alignment by fusing the semantic point clouds through joint node-level and fragment-level encoders, enabling more robust matching under partial overlap. More recent works incorporate additional modalities to improve robustness and generalization. SG-Reg (Liu et al. ) integrates point cloud feature, Bert embedding of the object label, and bounding box features for efficient and generalizable alignment, while SGAligner++ (Singh et al. ) further incorporates CAD features, constructing unified scene graphs that preserve structural relationships across observations. In addition to learned matching methods, ROMAN (Peterson et al. ) performs zero-shot scene graph alignment by leveraging CLIP (Radford et al. ) embeddings, PCA-based geometric features extracted from object point clouds, and a unified graph-theoretic global data association framework.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Scene Graph Alignment", "weight": 1.0} -->

Despite these advances, most existing scene graph alignment methods rely predominantly on geometric features derived from object point clouds, which are sensitive to incomplete observations and sparse overlap. While VLM features have been exploited in zero-shot approaches such as ROMAN (Peterson et al. ), their incorporation into trainable matching architectures remains largely underexplored. Furthermore, prior works have primarily focused on the S2S alignment task, where both scene graphs typically have comparable spatial coverage. The F2S alignment task, in which one graph represents only a small partial observation of another much larger scene graph, remains insufficiently studied. In this work, we address both the F2S and S2S alignment tasks within a unified framework, evaluated on different subsets of the proposed dataset.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dataset", "weight": 1.0} -->

Several datasets with 3D scene graph annotations have been proposed in recent years, such as 3D SSG (Wald et al. ), SG-FRONT (Ge et al. ), VLA-3D (Zhang et al. ), and SG3D (Zhang et al. ). These datasets construct scene graphs on top of semantically annotated point cloud scans for navigation and mobile manipulation tasks. However, they do not contain scene graph pairs constructed from partially overlapping observations of the same environment, and thus do not support the scene graph alignment task.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Dataset", "weight": 1.0} -->

Few datasets explicitly supporting 3D scene graph alignment have been proposed. Building upon the scene graph annotations of 3DSSG, SGAligner (Sarkar et al. ) introduces a dataset for aligning partially overlapping 3D scene graphs. In this dataset, subscans are generated from globally aligned scans in 3RScan (Wald et al. ) with controlled overlap ratios. Each subscan is converted into a sub-scene graph, and nodes within overlapping regions are treated as ground-truth correspondences. The dataset contains approximately 15.1k training pairs and 1.9k validation pairs, covering around 160 object classes. Later, SG-Reg (Liu et al. ) proposed a smaller dataset of approximately 4k samples tailored specifically for S2S alignment.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dataset", "weight": 1.0} -->

Although both SGAligner and SG-Reg provide object-level point clouds and semantic labels, they do not include vision--language features, which we identify as a critical cue for robust open-world scene graph matching. Moreover, these datasets focus exclusively on S2S alignment. The F2S setting, where a partial observation must be matched to a larger global map, remains unexplored. In contrast, our dataset is substantially larger, covering over 500 and 3k object classes across different groups and containing more than 700k samples. It additionally incorporates GroundingDino (Liu et al. ) vision--language features for each node and supports both S2S alignment and F2S matching, enabling evaluation in more diverse open-world scenarios.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

OpenSGA is mainly targeted to solve the open-world 3D semantic scene graph alignment problem. A 3D scene graph is denoted as $\mathcal{G}=\{\mathcal{V},\mathcal{E}\}$, where $\mathcal{V}$ is a set of nodes that represent real objects in the environment and $\mathcal{E}$ is a set of edges that connect the nodes.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

\(a\) Nodes: Each node $\boldsymbol{v}_{i}\in\mathcal{V}$ corresponds to a real-world object and contains multimodal attributes, such as visual--language features $\boldsymbol{f}_{\mathrm{vl}}$, text embedding $\boldsymbol{f}_{\mathrm{t}}$, and a geometric feature $\boldsymbol{f}_{\mathrm{g}}$. Let $\boldsymbol{x}_{i}\in\mathbb{R}^{3}$ denote the object's 3D position. The node representation is then where $\boldsymbol{f}_{\mathrm{g},i}$ in our method is the size of the object's 3D oriented bounding box, while point-based geometric descriptors used in prior works (Liu et al.; Xie et al.) are included only for comparison.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

The text embeddings $\boldsymbol{f}_{\mathrm{t}}$ and the vision--language features $\boldsymbol{f}_{\mathrm{vl}}$ are obtained by encoding the label text with SBERT (Reimers and Gurevych) and by extracting the hidden-layer representation of GroundingDINO (Liu et al.) during object detection, respectively. Details of these features are provided in Section 5.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

\(b\) Edges: An undirected edge $\boldsymbol{e}_{ij}\in\mathcal{E}$ connects nodes $\boldsymbol{v}_{i}$ and $\boldsymbol{v}_{j}$ and stores their Euclidean distance, To avoid fully connected graphs, we connect only the $N$ nearest neighbors for each node.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

\(c\) Alignment Problem: Given two partially overlapped 3D scene graphs $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ captured from the same environment, the goal is to find the correct node correspondences Only nodes that physically correspond to the same real object should be matched. Note some nodes have no matches because the graphs are often built from different views and may cover different areas of the scene.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

In practical robotic navigation scenarios, we assume that $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ originate from different sources in the two tasks described in Section 1. In the F2S task, $\mathcal{G}^{A}$ is constructed from the current observation, while $\mathcal{G}^{B}$ is derived from a more complete map accumulated from previous observations. The node positions in $\mathcal{G}^{B}$ are represented in the global reference frame of the previously built map. In contrast, the node positions in $\mathcal{G}^{A}$ are defined in the current camera frame, whose pose may be arbitrary and unrelated to the global reference frame of $\mathcal{G}^{B}$. This design decouples object alignment from ego-pose estimation, ensuring that correspondences are established based on object features and spatial relationships rather than similarities in global poses.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

In the S2S task, both $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ are constructed from sequences of images that capture the same scene with partial overlap. These graphs represent submaps generated either by multiple robots or by a single robot at different times. We assume a static environment for both tasks. Since both tasks are inherently node-level alignment problems, we address them using a unified network architecture. The similarities and differences of the two tasks will be further discussed in Section 5.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Scene Graph Alignment", "weight": 1.0} -->

In this section, we first present our network designed for F2S and S2S alignment in 4.1. We assume that the graphs to align have been built and represented as $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ (specifications of how the scene graphs are built can be found later in Section 5.1). As a large-scale environment can contain multiple scenes to align, we introduce a global graph retrieval module that computes discriminative graph-level embeddings in 4.2. The loss functions used in training are presented in 4.3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Alignment Network", "weight": 1.0} -->

Our alignment network is designed to find the match $\mathcal{M}^{AB}$ given input 3D scene graphs $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$. The architecture of the network is shown in Fig. 2. We divide our network into three parts: encoder, matcher and allocator. Each part is introduced in detail in the following: Figure 2: The system architecture of our 3D scene graph alignment network. From left to right: input scene graphs, alignment network composed of encoder, matcher and allocator, output matching result. Each node is composed of 3D position x, visual language feature fvl, text feature ft and geometry feature fg. The green lines in the output block illustrate the matched nodes. “Nbr” is the abbreviation of “neighbor”. The global embedding module is connected with white arrows, as it is used only in large environments containing multiple scenes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Encoder", "weight": 1.0} -->

The encoder aims to generate a feature vector that encodes the essential characteristics of each node as well as its surrounding neighborhood under open-world variations. The encoders for $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ share the same structure and weights. For clarity, we omit the superscripts $A$ and $B$ in the following description.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Encoder", "weight": 1.0} -->

The text embeddings $\boldsymbol{f}_{\mathrm{t}}$ and the vision--language features $\boldsymbol{f}_{\mathrm{vl}}$ are already high-dimensional embeddings produced by pre-trained models (Reimers and Gurevych; Liu et al. ). In contrast, the geometric descriptor $\boldsymbol{f}_{\mathrm{g}}$ is a normalized 3D vector representing the size of the object's oriented bounding box. We first encode $\boldsymbol{f}_{\mathrm{g}}$ using a feed-forward network (FFN) with one hidden layer to obtain a higher-dimensional embedding.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Encoder", "weight": 1.0} -->

By concatenating this embedding with $\boldsymbol{f}_{\mathrm{vl}}$ and $\boldsymbol{f}_{\mathrm{t}}$, we obtain the initial node feature vector, illustrated as a three-block stacked column in the encoder portion of Fig. 2 and denoted as $\boldsymbol{c}_{i}$ hereafter.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Encoder", "weight": 1.0} -->

While this initial embedding captures only the intrinsic properties of a node (center node), it does not incorporate any context or neighborhood information. Prior works have demonstrated that local context is critical for accurate scene graph alignment (Sarkar et al.; Liu et al.; Xie et al. ). However, it is still nontrivial to get a good embedding since it needs to be inherently translation and rotation invariant to ensure consistent representations even when the two input graphs $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ are defined in very different coordinate frames.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Encoder", "weight": 1.0} -->

The current state-of-the-art, Triplet-boosted Graph Neural Network (T-GNN) (Xie et al. ), addresses this issue by constructing triplet features that incorporate the edge length and angle of two randomly selected neighbor nodes and the center node. However, T-GNN introduces two key limitations: (i) it enforces only yaw-rotation invariance, while pitch and roll invariance are not supported since the method relies on defining an anti-clockwise ordering of neighbors for constructing triplet features; (ii) at least two neighbor nodes are required to make a Triplet thus for a frame with only one neighbor node, the neighbor information, which is still useful, is skipped.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Encoder", "weight": 1.0} -->

Our method begins by leveraging the inherent global rigidity of local 3D scene graphs. Under the assumption that each node has at least three neighbors in non-coplanar positions, the center node and its neighbors form a globally rigid subgraph, whose structure is uniquely determined by the set of pairwise distances between nodes. Therefore, the geometric layout of the objects can be fully described using only the distances, which naturally yields translation- and rotation-invariant representations. Building upon this insight, our method encodes neighborhood geometry exclusively through center-to-neighbor distances and neighbor-to-neighbor distances. Specifically, we make two distance-gated attention blocks: \(a\) Center to neighbor attention: For each center node $\boldsymbol{v}_{i}$, we first calculate the distance $d_{ij}$ to each neighbor node $\boldsymbol{v}_{j}$. The distance is encoded by a sinusoidal positional encoder described in (Vaswani et al.). Let $\text{PE}(d_{ij}),\ i\neq j$ denote the encoded distance embedding.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Encoder", "weight": 1.0} -->

The neighbor feature of $\boldsymbol{v}_{j}$ is defined as We then compute the attention from the center node to its neighbors: where $\boldsymbol{q}_{i}$, $\boldsymbol{k}_{ij}$ and $\boldsymbol{v}_{ij}$ are the query, key and value while $\boldsymbol{W}_{\mathrm{q}}$, $\boldsymbol{W}_{\mathrm{k}}$ and $\boldsymbol{W}_{\mathrm{v}}$ are the corresponding learnable weight matrices. $d_{h}$ is the dimensionality of each attention head. $\alpha^{raw}_{ij}$ is the calculated raw attention score and is further gated: where $\mathrm{g}(d_{ij})$ denotes the distance gate function implemented by a lightweight gating network. The network consists of a two-layer MLP followed by a sigmoid activation, producing a scalar value in $$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Encoder", "weight": 1.0} -->

This distance gate explicitly adds geometric prior into the attention to enforce biased attention based on distance, e.g., close neighbors should get more attention.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Encoder", "weight": 1.0} -->

Then the attention weight is normalized with softmax and the output $\boldsymbol{o}_{i}^{(\mathrm{c}\rightarrow\mathrm{n})}$ is calculated with where the superscript $(c\rightarrow n)$ stands for center to neighbors and $\mathcal{N}(i)$ is the neighbor ID set of the $i$th node.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Encoder", "weight": 1.0} -->

\(b\) Neighbor to neighbor attention: The neighbor to neighbor attention of the $i$th node works similarly as the center to neighbor attention and can be formulated as the following: where $i\neq j\neq k$ and $\boldsymbol{W}^{\prime}_{\mathrm{q}}$, $\boldsymbol{W}^{\prime}_{\mathrm{k}}$ and $\boldsymbol{W}^{\prime}_{\mathrm{v}}$ are learnable weight matrices. The output $\boldsymbol{o}_{i}^{(\mathrm{n}\rightarrow\mathrm{n})}$ in is the average pooling over all neighbors.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Encoder", "weight": 1.0} -->

Note the computational complexity of center to neighbor attention is $O(N)$ while that of neighbor to neighbor attention is $O(N^{2})$. In practice, we set the maximum neighbor number $N=4$ to ensure efficiency.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Encoder", "weight": 1.0} -->

After $\boldsymbol{o}_{i}^{(\mathrm{c}\rightarrow\mathrm{n})}$ and $\boldsymbol{o}_{i}^{(\mathrm{n}\rightarrow\mathrm{n})}$ are computed, we get the combined neighbor feature embedding using residual (He et al.) and LayerNorm (Ba et al.) as follows: where $\boldsymbol{W}_{\mathrm{o}}$ stands for the weight of a single MLP layer.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Encoder", "weight": 1.0} -->

The final node representation for alignment is obtained by concatenating $\tilde{\boldsymbol{c}_{i}}$ and $\boldsymbol{c}_{i}$. The concatenated feature is then passed through a projection feed-forward network (FFN) to match the input dimensionality required by the matcher. When the number of neighbors is fewer than three, the local 3D scene graph composed of the ego node and its neighbors is no longer globally rigid. Nevertheless, the distance-gated attention still serves as an effective cue for modeling neighborhood relationships, and our method performs well in practice.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Matcher", "weight": 1.0} -->

Given the encoded node sets from $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$, this module predicts matching scores, i.e., the pairwise similarities between nodes in $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$. For simplicity, we refer to this matching score prediction module as the matcher in the following sections.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Matcher", "weight": 1.0} -->

Our framework provides two variants of the matcher. The first is a lightweight cosine-similarity-based matcher. It computes pairwise similarities using normalized dot products. To handle unmatched nodes, we incorporate a learnable "dustbin" row and column that provide the model with an explicit option for non-matches.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Matcher", "weight": 1.0} -->

The second variant adapts LightGlue (Lindenberger et al. ), a popular and efficient 2D visual keypoint matching network, to the 3D setting in order to estimate similarity scores. Specifically, we extend keypoints to 3D, apply 3D coordinate normalization, and lift the positional encoding to 3D accordingly. The input feature dimension is also adjusted to be compatible with our model. The adapted version is referred to as LightGlue3D in Fig. 2. Compared to the first matcher, LightGlue3D achieves a higher performance but requires more GPU memory as well as longer training and inference time.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Allocator", "weight": 1.0} -->

Our matcher outputs a similarity score matrix. Let $I$ and $J$ denote the number of nodes in $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$, respectively. Suppose $\boldsymbol{P}\in\left[0,1\right]^{I\times J}$ is the similarity score matrix. Once $\boldsymbol{P}\in\left[0,1\right]^{I\times J}$ is predicted, the final matching result $\mathcal{M}^{AB}$ needs to be allocated. Note this step is not included in training but uses the algorithm described in the following.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Allocator", "weight": 1.0} -->

One commonly used allocation strategy is mutual nearest neighbor (MNN), which we adopt as one of the allocation algorithms in our framework. However, MNN only supports one-to-one matching. In practice, under-segmentation occasionally occurs (3--5% of nodes in our dataset). For example, two spatially adjacent sofas or connected cabinets may be segmented as a single instance in some frames and ultimately merged into one object in the map, while in the current frame, they can be segmented as two separate instances. As a result, multiple instances in the frame may correspond to the same object in the map. We further illustrate this issue in Fig. 5. Therefore, the matching can be many-to-one rather than strictly one-to-one. To address this, we formulate the matching problem as an iterative minimum-cost flow (MCF) problem and introduce a geometric penalty to encourage shape consistency between $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Allocator", "weight": 1.0} -->

We define a virtual source node $\boldsymbol{s}$ and a sink node $\boldsymbol{t}$ and construct the flow in the following. Each node $\boldsymbol{v}^{A}_{i}$ receives one unit of flow from the source: where $\mathrm{cap}$ is the capacity. For each pair with similarity above a threshold $\tau$ and among the top K candidates in $P$, we add a candidate matching edge, which is where $\mathrm{Top}\text{-}K(i)$ denotes the indices of the $K$ largest entries in row $i$ of $P$. The cost is defined as follows: where $(t)$ represents the current iteration. For a candidate correspondence $(i,j)$ and a set of previously selected matches $\mathcal{M}^{(t-1)}=\{(k,l)\}$, we define the geometry penalty as which is, pairwise structural consistency term, penalizing matchings that distort relative distances using the matching result from last iteration.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Allocator", "weight": 1.0} -->

Each node in $\mathcal{G}^{A}$ may also be left unmatched with a constant cost $\text{C}_{\text{unmatched}}$: Nodes in $\mathcal{G}^{B}$ have matching capacity more than one: allowing at most $\text{Cap}_{max}$ matches to be assigned to $\boldsymbol{v}^{B}_{j}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Allocator", "weight": 1.0} -->

The problem is solved by iteratively solving a linear min-cost flow problem with NetworkX (Hagberg et al. ) in CPU and recalculating $\mathrm{pen}^{(t-1)}(i,j)$ until the result has converged or a maximum iteration is reached. Detailed parameter values are provided in Appendix A.3.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Allocator", "weight": 1.0} -->

Note that in our setting, $\mathcal{G}^{B}$ is typically constructed from a more complete scan, where spatially adjacent objects with the same semantic label are fused into a single instance, as discussed at the beginning of this subsection. As a result, many-to-one matching can occur in our setting, whereas one-to-many matching does not. Nevertheless, if one-to-many matching were to be considered, the capacity of the edge $(\boldsymbol{s}\rightarrow\boldsymbol{v}_{i})$ could be increased to a value greater than one.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Global scene embeddings", "weight": 1.0} -->

Our alignment network performs node-level matching between two scene graphs. However, in large-scale environments containing multiple scenes, a robot must first identify the most relevant scene corresponding to the current observation before performing detailed node-level matching. Exhaustively matching the current observation against all candidate scenes is computationally inefficient. To address this, we introduce a global graph retrieval module that computes discriminative graph-level embeddings and retrieves the Top-K candidate scenes for subsequent node-level matching.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Global scene embeddings", "weight": 1.0} -->

Specifically, we incorporate a learnable class embedding $\mathbf{c}_{\mathrm{CLS}}$ into the encoder. The class token aggregates the graph information via an independent two-layered multi-head self-attention module. This descriptor is then used to query the most relevant scene graphs from a database containing all candidate scenes, thereby enabling a more efficient matching process.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Global scene embeddings", "weight": 1.0} -->

To select the Top-K graphs for node-level matching, we first perform database filtering based on the cosine similarity between global descriptors. We then apply a weighted reranking step to the retrieved Top-K candidates, combining global similarity with node-level matching confidence. The reranking score is defined as: In this setting, $s_{tq}$ is the similarity between a graph query $q$ and a target $t$. The elements $i,j\in\mathcal{M}$ are the set of matched nodes between graphs and $\mathbf{P}$ is the matrix that contains all the scores of the matching elements between the two graphs $q$ and $t$. When doing a matching against a database of graphs, the selected graph to match against is the graph $t$ that yields the highest $s_{tq}$ with the query graph $q$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Loss function", "weight": 1.0} -->

For node-level correspondence prediction in 4.1, methods using the cosine-similarity-based efficient matcher (marked with "L" in the results) are trained with the bidirectional InfoNCE loss proposed in CLIP (Radford et al. ). This objective maximizes similarity between matched pairs while minimizing similarity between unmatched pairs, encouraging discriminative embeddings for different objects. Methods using lifted LightGlue (Lindenberger et al. ) as the matcher (marked with "H" in the results) are trained using the negative log-likelihood (NLL) loss implemented in the LightGlue codebase.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Loss function", "weight": 1.0} -->

To train the global scene embedding in 4.2, we rely on a triplet margin contrastive loss with negative hard-mining. Given a processed batch, we select the positive pair and the hardest negative scan, the one that is closest in embedding space to $\mathbf{c}^{a}_{\mathrm{CLS}}$. To train our samples, we use the following loss function where $\mathbf{c}^{a}_{\mathrm{CLS}}$ is the global embedding associated to the graph from the image, $\mathbf{c}^{p}_{\mathrm{CLS}}$ is the embedding of the associated scan graph and $\mathbf{c}^{n}_{\mathrm{CLS}}$ is the embedding of the mined graph.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Scene Graph Building and Dataset Construction", "weight": 1.0} -->

This section first introduces our pipeline used to construct 3D scene graphs with the object features described in Section 3. We apply this pipeline to the ScanNet (Dai et al. ) dataset to build ScanNet-SG, our dataset designed for scene graph alignment in both the F2S and S2S tasks. We then present the dataset construction and grouping strategies for the F2S and S2S tasks, respectively.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Scene Graph Building", "weight": 1.0} -->

Our 3D semantic scene graph is constructed from RGB-D images with given camera poses.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Image tagging", "weight": 1.0} -->

Given an RGB image, we first use either the human annotations provided in ScanNet or an object-tagging model, such as ChatGPT-4o (OpenAI ), to generate labels or textual descriptions of the objects present in the image.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Segmentation and VLM feature extraction", "weight": 1.0} -->

The generated text descriptions are provided as prompts to Grounded-SAM (Ren et al. ) to obtain instance-level object masks. At the same time, we acquire Visual--language embeddings $\boldsymbol{f}_{\mathrm{vl}}$ by extracting a 256-dimensional embedding vector from the hidden layers of GroundingDINO (Liu et al. ) used within Grounded-SAM.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Text embedding", "weight": 1.0} -->

Text embeddings $\boldsymbol{f}_{\mathrm{t}}$ are extracted from the object descriptions using SBERT (Reimers and Gurevych ), resulting in 384-dimensional embedding vectors.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Bounding box computation", "weight": 1.0} -->

Using the depth image and instance masks, we compute instance-aware point clouds. Oriented 3D bounding boxes are then estimated using PCA-based OBB fitting (Gottschalk et al.; Ericson ). The geometric feature $\boldsymbol{f}_{\mathrm{g}}$ corresponds to the normalized size of the bounding box, where normalization is performed with respect to the maximum extent of the entire point cloud. The center of each bounding box is used as the spatial position of the corresponding object.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Bounding box computation", "weight": 1.0} -->

For a 3D scene graph constructed from a single frame, Steps 1)--4) yield the object nodes. Edges are established by computing pairwise distances between nodes and connecting each node to its $N$ nearest neighbors within a distance threshold $d_{th}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Multiview fusion", "weight": 1.0} -->

We use instance masks and depth images from multiple views to generate per-instance point clouds. Instances corresponding to the same object are merged based on 3D mIoU and $\boldsymbol{f}_{\mathrm{t}}$ similarity. During merging, the visual--language embeddings $\boldsymbol{f}_{\mathrm{vl}}$ and text embeddings $\boldsymbol{f}_{\mathrm{t}}$ are averaged, while the point clouds from different views are aggregated and downsampled using a voxel grid filter. The bounding box is then recomputed from the merged point cloud to obtain $\boldsymbol{f}_{\mathrm{g}}$. We further present the details of the multiview fusion step in Appendix A.1.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Multiview fusion", "weight": 1.0} -->

The key procedures and data flow is shown in figure 3 Multiview fusion ‣ 5.1 Scene Graph Building ‣ 5 Scene Graph Building and Dataset Construction ‣ OpenSGA: Efficient 3D Scene Graph Alignment in the Open World"). In the following, we assume that scene graphs $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ are constructed using the above procedure. In the frame-to-scan node matching task, $\mathcal{G}^{A}$ represents a smaller graph built from a single frame, while $\mathcal{G}^{B}$ corresponds to a complete scan of the scene. In the subscan-to-subscan node matching task, both $\mathcal{G}^{A}$ and $\mathcal{G}^{B}$ are constructed from incomplete scans of the same scene and share partial overlap.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Multiview fusion", "weight": 1.0} -->

Our dataset is built upon ScanNet (Dai et al. ), which contains over 1,500 RGB-D scans spanning 807 indoor scenes. Most scenes contain more than one scan captured from different camera trajectories. In the following, we present the subsets for frame-to-scan task and subscan to subscan task, respectively.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Frame-to-Scan (F2S) Matching", "weight": 1.0} -->

To support frame-to-scan matching, we generate two groups of frame--scan pairs. The Self Scan group refers to the setting where the frame-level and the scan-level scene graphs originate from the same scan. This setting evaluates whether a robot revisiting a previously observed pose, with access to only a single-frame partial observation, can correctly associate objects with their more complete counterparts in the fused map. Cross Scan Group considers frames sampled from a different scan of the same scene. This setting introduces novel viewpoints and newly appearing and missing regions, thereby reflecting more realistic scenarios.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Frame-to-Scan (F2S) Matching", "weight": 1.0} -->

In the original ScanNet dataset, different scans of the same scene are represented in separate global coordinate frames, and object instances are not associated across scans. To enable cross-scan matching, we register the scan-level point clouds from different scans of ScanNet using RANSAC-based global registration followed by ICP refinement (Fischler and Bolles; Besl and McKay ) to estimate the transformation between scans. To ensure estimation quality, we manually inspect all registration results and discard scan pairs with noticeable misalignment. We report the estimation performance in Appendix A.2. Each instance within a scan is assigned a unique identifier in accordance with the labels provided in ScanNet. Cross-scan instance association within the same scene is then performed using 3D mIoU together with semantic label consistency, as detailed in Step 5) and Appendix A.1.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Frame-to-Scan (F2S) Matching", "weight": 1.0} -->

We use Scenes 0--599 (1,276 scans) to construct the training set and Scenes 600--705 (237 scans) for testing. Frames are sampled every three frames from the original sequences. In total, the dataset contains approximately 557.0k training pairs and 87.9k test pairs, where 48.3% are generated from Self Scan and 52.7% from Cross Scan. The objects in this dataset span 509 unique semantic labels, and therefore we refer to this benchmark as ScanNet-SG-509.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Frame-to-Scan (F2S) Matching", "weight": 1.0} -->

To further increase object diversity and improve open-world generalization, we additionally use GPT-4o-mini (OpenAI ) for image-based object tagging. Recent study Xie et al. has shown that tags generated with large VLMs achieve strong agreement with human labels and can support downstream learning tasks effectively. Compared to the original ScanNet annotations, the labels generated by GPT-4o-mini capture a substantially richer set of fine-grained and previously unannotated objects, including frequently occurring everyday items such as cable, mouse, water bottle, and light switch, as well as many other categories. Although only Scenes 0--99 are used for training and Scenes 601--610 and 696--705 for testing---amounting to 17.0% of the total data in ScanNet-SG-509---this process yields 3,195 unique object labels, which is 6.3× more than in ScanNet-SG-509. We refer to this benchmark as ScanNet-SG-GPT.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Subscan-to-subscan (S2S) Matching", "weight": 1.0} -->

Each subscan is constructed from 50 to 300 randomly selected yet temporally contiguous frames processed in Section 5.2 Matching ‣ 5 Scene Graph Building and Dataset Construction ‣ OpenSGA: Efficient 3D Scene Graph Alignment in the Open World") (150 to 900 frames in the original ScanNet dataset). We use the method described in Section 5.1 to build the point-cloud map and the scene graph for each subscan. If two subscans from different scans of the same scene overlap, we include the pair as one dataset sample. In total, the dataset contains 13.4k training samples from Scenes 0--599 and 3.4k test samples from Scenes 600--705. In Figure 1B, Subscan 264_1029 is constructed from frames 264 to 1029 in Scene0000_00 of ScanNet, while Subscan 459_1027 is constructed from frames 459 to 1027 in Scene0000_01.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Subscan-to-subscan (S2S) Matching", "weight": 1.0} -->

The samples in the S2S task have the following difference compared to the F2S task: (i) In F2S, the node-overlap ratio is typically close to one ($>90\%$ on average) from $\mathcal{G}_{A}$ to $\mathcal{G}_{B}$ while very low ($<20\%$ on average) from $\mathcal{G}_{B}$ to $\mathcal{G}_{A}$, since the frame-level nodes are usually a subset of those in the complete scan, except when new regions are observed in the cross-scan setting. In S2S, the overlap ratio between two subscans spans $(0,1]$. We report the detailed distribution in Fig. 13 in Appendix A.2. (ii) In F2S, the two scene graphs are expressed in the camera frame and the world frame, respectively, and therefore differ substantially in their coordinate systems. In contrast, in S2S, both scene graphs are expressed in world frames.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Subscan-to-subscan (S2S) Matching", "weight": 1.0} -->

While these world frames are not identical because the graphs are built from different scans, they share a similar gravity alignment (i.e., the $z$-axis points upward). (iii) In ScanNet-SG-509, F2S matches a small graph with 4.5 nodes on average to a larger graph with 22.2 nodes on average, whereas S2S matches two graphs with 17.3 nodes on average. (iv) There are no many-to-one matching in S2S, as both subscans are fused maps.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Subscan-to-subscan (S2S) Matching", "weight": 1.0} -->

The general data statistics are presented in Table 1 Matching ‣ 5 Scene Graph Building and Dataset Construction ‣ OpenSGA: Efficient 3D Scene Graph Alignment in the Open World"), where the many-to-one ratio indicates the percentage of nodes that have many-to-one matching from a frame to a scan. More statistics and visualizations of the dataset are provided in Appendix A.2.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Results", "weight": 1.0} -->

This section reports experimental results. Section 6.1 describes the experimental setup and baseline methods. In Section 6.2, we present results on the F2S alignment task. Section 6.3 further extends F2S by registering a frame-level SG against multiple scan-level SGs from different scenes, thereby simulating matching in large-scale environments containing multiple scenes. In Section 6.4, the results on the S2S task are reported.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Results", "weight": 1.0} -->

Additional results, including additional ablation studies with different input feature types, performance of fine tuned models for the S2S task, performance of models trained jointly on F2S and S2S data, and downstream point cloud registration results, are provided in Appendix A.4 and Appendix A.5 to maintain clarity and conciseness in the main text.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Five baseline methods and seven ablation variants of our method are evaluated for F2S and S2S tasks. As a learning-based baseline, we include SG-Reg (Liu et al. ), a state-of-the-art scene graph alignment method that leverages instance point clouds, 3D bounding boxes, and text features through a dedicated matching network. We further consider four zero-shot baselines.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The first is ROMAN (Peterson et al. ), which performs geometrically consistent matching using point cloud features and VLM embeddings. For a fair comparison, we adapt ROMAN by replacing its original FastSAM (Zhao et al. ) segments with our object-level segments and by using the VLM embeddings generated by GroundingDINO (Liu et al. ) rather than CLIP (Radford et al. ).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The remaining three zero-shot baselines rely on cosine similarity between object embeddings: VLM embeddings from GroundingDINO (Liu et al. ), language embeddings from SBERT (Reimers and Gurevych ), and their concatenation. For each query object, the instance with the highest similarity exceeding a predefined threshold is selected as the match. These VLM and language embeddings are trained to produce high cosine similarity for semantically consistent objects while separating distinct ones, making cosine similarity a strong yet simple baseline for zero-shot matching.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Finally, we evaluate seven ablation variants of our approach that isolate the impact of different encoders, matchers, and allocators. The full configurations are summarized in Table 2. Our approach builds on the same pretrained features as the zero-shot baselines but further trains a matching network. In general, the model size and computational cost of the variants are primarily determined by the choice of matcher. Variants based on the cosine-similarity efficient matcher are lightweight but typically achieve lower accuracy, whereas variants based on LightGlue3D are more computationally demanding yet consistently deliver stronger performance. To reflect this trade-off, we report both a Lightweight and a High-performance version of our method, and denote them with markers L and H, respectively. In addition to the T-GNN encoder (Liu et al. ) and our DGSA encoder, we also tested FFN as a baseline variant.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Ours L T-GNN + MNN Ours L DGSA + MNN Ours L DGSA + MCF Final Ours H FFN + MNN Ours H T-GNN + MNN Ours H DGSA + MNN Ours H DGSA + MCF Final Table 2: Ablation Variants All models are trained on NVIDIA A40 GPUs and tested on a desktop equipped with an NVIDIA RTX 3080 Ti. Each model is trained for 10 epochs using the AdamW optimizer (Loshchilov and Hutter) with a learning rate of $2\times 10^{-4}$ and a batch size of 64. Detailed model parameters are provided in Appendix A.3. Performance is evaluated using four metrics: Accuracy, Precision, Recall, and F1 score. Each metric is computed per test sample over the nodes and then averaged across the test set. The minimum matching score thresholds and other key parameters of the compared methods are optimized using Optuna (Akiba et al.) to maximize the F1 score.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

For this task, all models are trained on the ScanNet-SG-509 training split, which includes a mixture of self-scan and cross-scan samples. We evaluate performance on three test sets: (i) the self-scan group, (ii) the cross-scan group, and (iii) the ScanNet-SG-GPT subset. These test sets represent progressively more challenging settings. In (i), query frames are drawn from the same scan used to construct the map, resulting in minimal viewpoint and coverage variation. In (ii), query frames originate from different scanning trajectories, leading to larger viewpoint changes. In (iii), we further evaluate on ScanNet-SG-GPT, whose expanded object vocabulary generated by GPT-4o presents the most challenging generalization setting. Importantly, we do not use the ScanNet-SG-GPT training split; instead, all models are trained exclusively on ScanNet-SG-509. This design enables a direct assessment of cross-vocabulary generalization from ScanNet-SG-509 to ScanNet-SG-GPT Tables 3--5 summarize the F2S matching results in the three test sets.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

For each metric, the best result is highlighted in bold with an orange background, and the second-best result is highlighted with a cyan background. In general, our method consistently outperforms both SG-Reg (Liu et al.) and the zero-shot cosine-similarity baselines. In particular, Ours H DGSA + MCF Final achieves the highest accuracy and F1 score in all three settings.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

VLM+Bert CosSim Ours L T-GNN + MNN Ours L DGSA + MNN Ours L DGSA + MCF Final Ours H FFN + MNN Ours H T-GNN + MNN Ours H DGSA + MNN Ours H DGSA + MCF Final Table 3: Matching Results in ScanNet-SG-509 Self Scan Group (Simple) VLM+Bert CosSim Ours L T-GNN + MNN Ours L DGSA + MNN Ours L DGSA + MCF Final Ours H FFN + MNN Ours H T-GNN + MNN Ours H DGSA + MNN Ours H DGSA + MCF Final Table 4: Matching Results in ScanNet-SG-509 Cross Scan Group (Medium) VLM+Bert CosSim Ours L T-GNN + MNN Ours L DGSA + MNN Ours L DGSA + MCF Final Ours H FFN + MNN Ours H T-GNN + MNN Ours H DGSA + MNN Ours H DGSA + MCF Final Table 5: Matching Results in ScanNet-SG-GPT Test Set (Difficult)

<!-- chunk {"id": "body-0091", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

The first key observation is the importance of pretrained semantic features for open-vocabulary instance matching.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

The cosine-similarity baselines demonstrate that VLM and SBERT embeddings already provide strong correspondence signals, and their combination further improves performance, indicating that the two modalities capture complementary information. SG-Reg does not leverage VLM features and instead relies heavily on instance point clouds and coordinate-dependent geometric encoding. In F2S, the large coordinate-system mismatch between the frame and the scan, together with partial observations caused by limited view coverage, makes such point-cloud-based features substantially less reliable, leading to a significant performance degradation. Building on these pretrained representations, our learned models improve robustness across all settings. Even the lightweight variants outperform most baselines, indicating that training enables the matcher to exploit additional contextual and geometric cues beyond raw semantic similarity. We visualize the results of five different methods on seven F2S samples with varying numbers of nodes in the frame in Fig. 4.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

A second consistent trend is the impact of the encoder design. T-GNN, originally proposed in SG-Reg (Liu et al. ), performs noticeably worse than our DGSA encoder across all evaluation settings. This is mainly because T-GNN relies on encoding coordinate-sensitive position relations, while F2S involves a significant coordinate-system discrepancy between frame-level and scan-level observations. As a result, the geometric patterns learned by T-GNN become difficult to transfer reliably, even compared to the FFN baseline. In contrast, the spatial-attention encoder provides a more stable representation under these conditions, enabling stronger matching performance for both lightweight (L) and high-performance (H) matchers.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

Comparing our variants with MNN and MCF allocators, we observe that MCF---by explicitly supporting many-to-one correspondences---primarily improves performance by increasing recall and yielding more stable F1 scores across all test sets. With the lightweight matcher, recall and F1 improve by 0.093 and 0.025 on average over the three test sets (from Ours L DGSA + MNN to Ours L DGSA + MCF Final). With the high-performance matcher, the gains are smaller, with average improvements of 0.010 in recall and 0.003 in F1 (from Ours H DGSA + MNN to Ours H DGSA + MCF Final). The larger improvement in the lightweight setting stems from the fact that the lightweight matcher relies mainly on feature similarity and does not enforce geometric consistency between matched object pairs, whereas MCF incorporates such global allocation constraints. In contrast, the high-performance matcher already models relative-distance consistency internally, and therefore, MCF mainly contributes by enabling many-to-one matching.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

As shown in Table 1 Matching ‣ 5 Scene Graph Building and Dataset Construction ‣ OpenSGA: Efficient 3D Scene Graph Alignment in the Open World"), many-to-one cases occur in only a small fraction of nodes in the dataset, which limits the overall performance gain. In Figure 5, we compare the matching results using the MNN and MCF allocators for samples with many-to-one correspondences. MNN fails to resolve the many-to-one case, causing one of the two instances to be either mismatched or assigned to the no-match class. In contrast, MCF correctly handles the many-to-one correspondence and produces consistent matches.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Frame-to-scan Node Matching", "weight": 1.0} -->

To jointly compare efficiency and matching performance, we visualize the results in a radar plot in Fig. 6. Efficiency is quantified by the number of model parameters, the average training time per epoch, and the average inference time per sample, while performance is measured by accuracy and F1 score. All results are reported on the cross-scan (*Medium*) test set. The plot includes SG-Reg and three representative variants of our method. We omit the cosine-similarity baselines, as they require no additional training and their inference cost is dominated by a simple similarity computation. As shown in Fig. 6, our variants are three times faster than SG-Reg. Ours L DGSA + MCF Final achieves a favorable trade-off between efficiency and performance, whereas Ours H DGSA + MCF Final is larger and slower but has the best overall accuracy and F1 score.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Frame-to-scan with Multiple Scenes", "weight": 1.0} -->

When operating in a large-scale environment containing multiple scenes, the system must identify the correct scene against which to perform object node matching. To showcase the necessity of a global embedding, we evaluate the retrieval accuracy of the correct scene graph from a graph database given a query graph obtained from an image. The metric Recall@K is employed to evaluate whether the target scene is ranked among the top K scenes in terms of similarity. Additionally, we report the inference time to assess the efficiency of each method. For this evaluation, we use the data from the testing scenes (scenes 600-705) and treat each scene's graph as one entry of our database, ensuring that there is only one correct graph in our target set. In these experiments, we only evaluate the final versions of our networks: the high-performance variant (Ours H) and the lightweight variant (Ours L), both employing DGSA and MCF.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Frame-to-scan with Multiple Scenes", "weight": 1.0} -->

The first experiment evaluates the ability of the proposed global embedding to retrieve the correct graph from a database of graphs. We test different values of K to evaluate the capacity of using the global embedding as a filtering step in the retrieval step. The results of this experiment are presented in Table 6. As it can be seen, both variants yield similar retrieval accuracy across different K value, mainly because they employ the same number of multi-head attention layers to produce the global embedding.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Frame-to-scan with Multiple Scenes", "weight": 1.0} -->

For our final experiment, we ablate different methods to obtain the correct scene graph (Recall@1) from one forward pass with our network: match against all candidates followed by reranking (baseline), or first using the global embedding for filtering, denoted as top K, and then performing reranking. In our experiments, we also compare two reranking strategies: the weighted reranking proposed in equation (weight rerank) and direct reranking based on the matching score, which would be the same as in but with the dot product being equal to one. The filtering step, based on the global embedding, consists of selecting the Top-K candidates from the database according to the cosine similarity of the global embeddings, after which only the selected scenes are reranked. The results are presented in Table 7.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Frame-to-scan with Multiple Scenes", "weight": 1.0} -->

From the results, we observe that the high-performance version of our network achieves higher accuracy at the expense of increased computation time. Compared to the baseline, incorporating filtering improves overall accuracy by removing incorrect graphs that would otherwise obtain high matching scores. Regarding the reranking strategies, the proposed weighted reranking consistently outperforms score-based reranking, indicating that the global embeddings of correct matches are closer in the embedding space than those of incorrect pairs. In terms of processing time, all methods that use the global embedding for filtering are more efficient than performing individual graph matching for all candidates, followed by a selection. As the filter size (K) increases, computation time increases, while accuracy also improves. As expected, the lightweight version is more computationally efficient than the high-performance version of the network.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Frame-to-scan with Multiple Scenes", "weight": 1.0} -->

Ours L + Top 5 + direct rerank Ours L + Top 10 + direct rerank Ours L + Top 20 + direct rerank Ours L + Top 5 + weighted rerank Ours L + Top 10 + weighted rerank Ours L + Top 20 + weighted rerank Ours H + Top 5 + direct rerank Ours H + Top 10 + direct rerank Ours H + Top 20 + direct rerank Ours H + Top 5 + weighted rerank Ours H + Top 10 + weighted rerank Ours H + Top 20 + weighted rerank Table 7: Correct scene graph retrieval and computation time in ScanNet-SG Test Set (Medium) with different reranking strategies.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Table 8 presents the results of the S2S node matching task. The results of two high-performing baseline methods and three of our variants are further illustrated in Fig. 9. Since both subscans are fused from multiple frames, the S2S setting contains almost no many-to-one correspondences (Table 1 Matching ‣ 5 Scene Graph Building and Dataset Construction ‣ OpenSGA: Efficient 3D Scene Graph Alignment in the Open World")). Therefore, we use MNN as the only allocator and focus on comparing different feature choices and matching network designs.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

In the S2S node matching task, the zero-shot cosine-similarity baselines achieve relatively high recall, especially for VLM CosSim (0.906 Re) and VLM+Bert CosSim (0.898 Re). However, their precision remains low (0.370--0.400), leading to moderate F1 scores (0.477--0.530). In contrast, our learned matching models substantially improve accuracy and precision, demonstrating that training a matcher on top of pretrained semantics is critical for disambiguating semantically similar objects. Compared to the best cosine-similarity baseline (VLM+Bert CosSim, 0.530 F1), all variants of our method achieve stronger overall performance. In particular, the best-performing model Ours H DGSA + MNN achieves 0.681 Acc and 0.589 F1, reflecting a more balanced precision--recall trade-off.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Unlike in F2S, T-GNN (Liu et al. ) becomes a more competitive encoder in S2S. In this task, both graphs are constructed from fused multi-frame subscans, which reduces the coordinate-system mismatch and alleviates the extreme partial-observation issue present in F2S. As a result, T-GNN-based variants benefit more from their geometric encoding and achieve strong performance: Ours H T-GNN + MNN reaches the best F1 (0.592) and the highest recall among our variants (0.732). Meanwhile, the FFN encoder yields the highest precision (0.565) but lower recall (0.592), leading to a lower F1 (0.556). This suggests that in S2S, geometric consistency encoded by T-GNN helps recover additional true correspondences, whereas simpler encoders tend to be more conservative. SG-Reg (Liu et al. ) remains significantly behind all other methods. We observe that in the training set, SG-Reg achieves a precision of 0.501 and a recall of 0.512, indicating a tendency to overfit to training data.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Although SG-Reg proposed T-GNN, its matching network and feature design rely primarily on point cloud information and do not incorporate VLM features. This design is not suited for the subscan matching setting, where instance point clouds are often incomplete and the overlap between subscans is limited. ROMAN (Peterson et al. ), which additionally incorporates PCA-based point cloud features alongside VLM embeddings, achieves relatively high precision but substantially lower recall compared to the other zero-shot baselines. As a result, its overall F1 score is the lowest among the four zero-shot methods, primarily due to its limited recall.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

VLM+Bert CosSim Ours L T-GNN + MNN Ours L DGSA + MNN Ours H FFN + MNN Ours H T-GNN + MNN Ours H DGSA + MNN Table 8: Subscan-to-subscan Matching Result Figure 7: Radar plot comparing four learning-based methods across five metrics on S2S task. Accuracy and F1 score are shown on a scale. Parameters, training time (per epoch on an NVIDIA A40 GPU), and inference time (per sample on an NVIDIA 3080Ti GPU) are normalized to the ranges M, [0.01, 3.5] h, and ms, respectively.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Moreover, we find that the performance of all methods strongly depends on the overlap ratio between two subscans. In Figure 8, we further group the test set into 10 bins according to overlap ratio from 0 to 1 with a step size of 0.1. In the F1 score--overlap ratio plot, the F1 score of all methods increases noticeably with overlap, indicating that the amount of shared observed area is a primary factor affecting subscan matching difficulty.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Interestingly, the accuracy curves of our variants remain relatively flat compared to their F1 curves, whereas the zero-shot VLM+Bert CosSim (Liu et al.; Reimers and Gurevych ) baseline shows a much steeper increase in accuracy as overlap grows. This behavior is mainly driven by the handling of no-match cases at low overlap. When the overlap is small, most query objects have no correspondence in the other subscan, making true negatives dominate the evaluation. While true negatives are reflected in accuracy, they do not contribute to the F1 score. ROMAN (Peterson et al. ) and our models, which consider geometric consistency, are more reliable at predicting the "no-match" label in these low-overlap regimes, maintaining stable accuracy even when the overlap is limited. In contrast, VLM+Bert CosSim tends to produce spurious matches when no correspondence exists due to its lack of geometric consistency, leading to many false positives and thus lower accuracy at low overlap.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Notably, compared to the zero-shot setting of ROMAN, the additional task-specific training of our models enables the matcher to better adapt the feature representations and more accurately predict the "no-match" class, thereby improving accuracy under low-overlap conditions.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Overall, the S2S results confirm that subscan-level matching benefits from additional training. Compared to F2S, the T-GNN encoder is more effective in S2S, which can be attributed to the reduced coordinate discrepancy between subscans. We further summarize the performance and efficiency metrics of the trained methods in the radar plot shown in Fig. 7. Considering the trade-off between accuracy and computational cost, Ours L T-GNN (Liu et al. ) + MNN provides the best overall balance, whereas Ours H DGSA + MNN achieves the highest accuracy.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

Although the S2S task differs from the F2S task as discussed in Section 5.3 Matching ‣ 5 Scene Graph Building and Dataset Construction ‣ OpenSGA: Efficient 3D Scene Graph Alignment in the Open World"), both tasks involve object node matching using the same types of features. Therefore, pretraining the model on the F2S dataset, which is substantially larger than the S2S dataset, and subsequently fine-tuning it on the S2S dataset is expected to improve performance. We report the results in Appendix A.4, which show that fine-tuning improves accuracy by 2--3% and F1 score by more than 4% compared to training solely on the S2S dataset. In addition, Appendix A.4 presents results for models trained using all available training data, including F2S data annotated with ScanNet labels and GPT-4o labels, as well as S2S data. The results show improved performance on the S2S task and on the difficult F2S test group (GPT-4o annotated ).

<!-- chunk {"id": "body-0112", "role": "body", "section": "Subscan-to-subscan Node Matching", "weight": 1.0} -->

In contrast, a performance decrease is observed on the easy and medium F2S groups annotated with ScanNet labels since more labels are involved. Detailed results are provided in the appendix.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented a learning-based framework and a benchmark for scene graph alignment under partial observations, covering both F2S and S2S node matching. Across both tasks and all three F2S evaluation settings, our methods consistently achieve the best overall performance. The results highlight two main insights. First, features derived from raw instance point clouds are unreliable under partial observations and coordinate discrepancies, especially in F2S, where point-cloud-centric designs degrade substantially. In contrast, pretrained semantic representations are crucial: VLM and SBERT embeddings already provide strong zero-shot matching signals, and combining them yields complementary gains of 2.5%--8.1% in F1 score across evaluation settings. Second, learning on top of these pretrained features further improves robustness. Our trained matching network consistently outperforms zero-shot cosine-similarity baselines by reducing semantic ambiguity and incorporating contextual and geometric cues, improving accuracy by 6.4%--13.7% and F1 score by 4.1%--11.2%. Compared to the training-based baseline, our method further reduces both training and inference time by over 60%.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Despite these strengths, our current dataset still has limitations. In particular, edge relationships are mainly represented by geometric distance, and their language descriptions are simplified to a single "next to" relation, limiting the evaluation of richer relation-aware grounding. Enriching edge descriptions and expanding relation diversity are promising directions for future work, alongside further exploiting multi-modal cues to improve alignment in larger-scale and outdoor environments.
