<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

VectorMapNet: End-to-End Vectorized HD Map Learning

Topics include High-definition map construction, Vectorized maps, Autonomous driving, Bird's-eye view perception, Polyline generation, Sensor fusion, Set prediction, Motion forecasting, NuScenes, Argoverse 2, VectorMapNet.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Recasts learned HD map construction as direct prediction of sparse vector polylines rather than raster segmentation followed by hand-built post-processing. VectorMapNet combines BEV feature extraction, set-style map element detection, and object-level polyline generation, making its output closer to what downstream forecasting and planning systems consume.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous driving systems require High-Definition (HD) semantic maps to navigate around urban roads. Existing solutions approach the semantic mapping problem by offline manual annotation, which suffers from serious scalability issues. Recent learning-based methods produce dense rasterized segmentation predictions to construct maps. However, these predictions do not include instance information of individual map elements and require heuristic post-processing to obtain vectorized maps. To tackle these challenges, we introduce an end-to-end vectorized HD map learning pipeline, termed VectorMapNet. VectorMapNet takes onboard sensor observations and predicts a sparse set of polylines in the bird's-eye view. This pipeline can explicitly model the spatial relation between map elements and generate vectorized maps that are friendly to downstream autonomous driving tasks. Extensive experiments show that VectorMapNet achieve strong map learning performance on both nuScenes and Argoverse2 dataset, surpassing previous state-of-the-art methods by 14.2 mAP and 14.6mAP. Qualitatively, VectorMapNet is capable of generating comprehensive maps and capturing fine-grained details of road geometry.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To the best of our knowledge, VectorMapNet is the first work designed towards end-to-end vectorized map learning from onboard observations. Our project website is available .

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving systems require an understanding of map elements on the road, including lanes, pedestrian crossing, and traffic signs, to navigate around the world. Such map elements are typically provided by pre-annotated High-Definition (HD) semantic maps in existing pipelines. However, these methods face scalability issues due to their heavy reliance on human labor for annotating HD maps. Additionally, they necessitate precise localization of the ego-vehicle to derive local maps from the global one, a process that could introduce meter-level errors.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, our focus lies in developing a learning-based approach for online HD semantic map learning. The aim is to use onboard sensors, including LiDARs and cameras, to estimate map elements on-the-fly. This methodology avoids the need for localization, allowing for prompt updates. Furthermore, learning-based methods can generate uncertainty or confidence indicators that downstream modules, such as motion forecasting and planning, can utilize to offset imperfect perception. These methods can leverage increasing data and model size, promptly reflect current conditions, and generalize from annotated maps to under-annotated or even non-annotated areas (please refer to Figure 6).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most of HD semantic map learning methods consider the task as a semantic segmentation problem in bird's-eye view (BEV), which rasterizes map elements into pixels and assigns each pixel with a class label. This formulation makes it straightforward to leverage fully convolutional networks. However, rasterized maps are not an ideal map representation for autonomous driving, for three reasons. First, rasterized maps lack instance information necessary to distinguish map elements with the same class label but different semantics, e.g. left boundary and right boundary. Second, it is hard to enforce spatial consistency within the predicted rasterized maps, e.g. nearby pixels might have contradicted semantics or geometries. Third, 2D rasterized maps are incompatible with most autonomous driving systems which consume instance-level 2D/3D vectorized maps for motion forecasting and planning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To alleviate these issues and produce vectorized outputs, HDMapNet generates semantic, instance, and directional maps and vectorizes these three maps with a hand-designed post-processing algorithm. However, HDMapNet still relies on the rasterized map predictions, and its heuristic post-processing step restricts the model's scalability and performance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose an end-to-end vectorized HD map learning model named VectorMapNet, an end-to-end framework that does not involve dense semantic pixels or sophisticated post-processing steps. Instead, it represents map elements as a set of polylines closely related to downstream tasks, e.g. motion forecasting. Therefore, the mapping problem boils down to predicting a sparse set of polylines from sensor observations. Specifically, we pose it as a detection problem and leverage recent set detection and sequence generation methods. First, VectorMapNet aggregates features generated from different modalities (e.g. camera images and LiDAR) into a common BEV feature space. Then, it detects map element locations based on learnable element queries and BEV features. Finally, we decode each element query into a polyline. An overview of VectorMapNet is shown in Figure 1.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments show that VectorMapNet achieves state-of-the-art performance on the public nuScenes dataset and Argoverse2, outperforming HDMapNet and another baseline by at least 14.2 mAP. Qualitatively, VectorMapNet builds a more comprehensive map than previous works and can capture fine details, e.g. jagged boundaries. Furthermore, we feed our predicted vectorized HD map into a downstream motion forecasting module, demonstrating the predicted map's compatibility and effectiveness. To summarize, the contributions of the paper are as follows: We present VectorMapNet, an end-to-end mapping approach that eliminates the need for map rasterization and post-processing by predicting vectorized outputs directly from sensor observations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We utilize polyline, a flexible primitive with variable lengths and encoded order, to accommodate the heterogeneous nature of map elements. This approach effectively formulates the construction of a polyline map as a detection issue, thereby introducing a new strategy to the mapping paradigm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We adapt detection transformer (DETR) models to locate deformable elements within a 3D space. Recognizing that prevalent centerpoint-based feature extraction methods fall short when dealing with map elements of varying sizes and shapes, we propose an innovative solution. Our novel method overcomes these limitations, delivering state-of-the-art performance in online semantic HD map learning tasks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Semantic map learning. Annotating semantic maps attracts plenty of interests thanks to autonomous driving. Recently, semantic map learning is formulated as a semantic segmentation problem and is solved by using aerial images, LiDAR points, and HD panorama. The crowdsourcing tags are used to improve the performance of fine-grained segmentation. Instead of using offline data, recent works focus on understanding BEV semantics from onboard camera images, and videos. Only using onboard sensors as model input is particularly challenging as the inputs and target map lie in different coordinate systems. Recently, several cross-view learning approaches leverage the geometric structure of scenes to mitigate the mismatch between sensor inputs and BEV representations. Some methods use pixel-level semantic maps to solve downstream tasks, but the entire downstream pipeline needs to be redesigned to accommodate these rasterized map inputs. Beyond pixel-level semantic maps, our work extracts a consistent vectorized map around ego-vehicle from surrounding cameras or LiDARs, which suits for existing downstream tasks like motion forecasting without further post-processing.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

Lane detection. Lane detection aims to separate lane segments from road scenes precisely. Most lane detection algorithms use a pixel-level segmentation technique combined with sophisticated post-processing. Another line of work leverages the predefined proposal to achieve high accuracy and fast inference speed. These methods typically involve handcrafted elements such as vanishing points, polynomial curves, line segments, and Bézier curves to model proposals. In addition to using perspective view cameras as inputs, and extract lane segments from overhead highway cameras and LiDAR imagery with a recurrent neural network. Instead of discovering the road's topology via boundaries detection, STSU and LaneGraphNet construct lane graphs from centerline segments that are encoded by Bézier curves and line segments, respectively. To model complex geometries in the urban environment, we leverage polylines to represent all the map elements in perceptual scopes.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

Geometric data modeling. Another line of work closely related to VectorMapNet is geometric data generation. These methods typically treat geometric elements as a sequence, such as primitive parts of furniture, states of sketch strokes, vertices of $n$-gon mesh, and parameters of SVG primitives. These methods generate these sequences by leveraging autoregressive models (e.g. Transformer). Since the directly modeling sequence is challenging for long-range centerline maps, HDMapGen views the map as a two-level hierarchy. It produces a global and local graph separately with a hierarchical graph RNN. Instead of treating geometric elements as a sequence generation problem, LETR models line segment as a detection problem and tackle it with a query-based detector. Unlike the above approaches that focus on single-level geometric modelings, such as scene level (e.g. line segments in an image) or object-level (e.g. furniture), VectorMapNet is designed to address both the scene level and object level geometric modeling. Specifically, VectorMapNet constructs a map by modeling the global relationship between map elements in the scene and the local geometric details inside each element.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

Learning vector representations from images. VectorMapNet bears some similarities with predicting vector graphics from raster images. Several recent works use different vector representations to generate vector images. converts images to CAD, CanvasVAE learns vectorized canvas layouts from images, and generates vectorized stroke primitives from a raster line drawing. The instance segmentation community has also been concerned with a similar task of detecting object contours in a vector form from an image. These methods initialize a contour for every object instance and then refine the vertex positions of the contour. However, The above methods are highly domain-dependent, and it is non-trivial to adapt them for our task that requires detecting and generating map elements with different semantics and geometry in the 3D world.

<!-- chunk {"id": "body-0017", "role": "body", "section": "VectorMapNet", "weight": 1.0} -->

Problem Formulation and Challenges. Similar to HDMapNet, our task is to vectorize map elements using data from onboard sensors of autonomous vehicle, such as RGB cameras and/or LiDARs. These map elements include but are not limited to: Road boundaries (boundaries of roads separating roads and sidewalks, typically irregularly-shaped curves of arbitrary lengths), Lane dividers (boundaries dividing lanes on the road, usually straight lines), and Pedestrian crossings (regions with white markings indicating legal pedestrian crossing points, typically represented as polygons). While the task is clearly defined, it is fraught with complexities and unique challenges when tackling it. The diverse geometric structures of map elements make it difficult to establish a unified geometric representation. The inputs and outputs of the mapping problem are not perfectly aligned. They exist in different view spaces (e.g. camera data is in perspective view and map elements are in BEV), and not all map elements are fully visible from input sensors. In some extreme cases, map elements may be completely occluded by vehicles. The task requires more than simple vectorization; it also necessitates scene understanding because of the complex geometrical and topological relationships between map elements.

<!-- chunk {"id": "body-0018", "role": "body", "section": "VectorMapNet", "weight": 1.0} -->

For instance, map elements may overlap, or two traffic cones connected with a wire might indicate a road boundary.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Method Overview", "weight": 1.0} -->

The challenges above underline the need for a primitive that effectively represents a variety of geometric structures and a model that is capable of capturing the geometrical and topological relationships from various sensor inputs.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Method Overview", "weight": 1.0} -->

In practice, we pre-process public autonomous driving semantic maps to obtain a unified polyline representation of map elements: polygons are represented as closed polylines; curves are converted into polylines by applying the Ramer--Douglas--Peucker algorithm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Method Overview", "weight": 1.0} -->

Using polylines to represent map elements has three main advantages: HD maps are typically composed of a mixture of different geometries, such as points, lines, curves, and polygons. Polylines are a flexible primitive that can represent these geometric elements effectively. The order of polyline vertices is a natural way to encode the direction of map elements, which is vital to driving. The polyline representation has been widely used by downstream autonomous driving modules, such as motion forecasting.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Method Overview", "weight": 1.0} -->

VectorMapNet. We introduce VectorMapNet, an end-to-end model designed to represent a map $\mathcal{M}$ with a sparse set of polylines ${\mathcal{V}}^{poly}$, thus formulating the task as a sparse set detection problem. In our approach, we convert sensor data into a canonical Bird's Eye View (BEV) representation, ${\mathcal{F}}_{BEV}$, and model polylines based on this BEV. Given the complexity and diversity of map elements' structural and location patterns and relationships, we divide the task into three distinct components: A BEV feature extractor (§ 3.2) that lifts various sensor modality inputs into a canonical feature space. A map element detector (§ 3.3) that locates and classifies all map elements by predicting element keypoints ${\mathcal{A}} = \left.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method Overview", "weight": 1.0} -->

\{{{\mathbf{A}}_{i} \in {\mathbb{R}}^{k \times 2}} \middle| {i = {1,\ldots,N}}\} \right.$ and their class labels ${\mathcal{L}} = \left. \{{l_{i} \in {\mathbb{Z}}} \middle| {i = {1,\ldots,N}}\} \right.$. The definition of element keypoint representation $\mathcal{A}$ is described in § 3.3. A polyline generator (§ 3.4) that produces a sequence of ordered polyline vertices which describes the local geometry of each detected map element $({\mathbf{A}}_{i},l_{i})$. An overview of three components is demonstrated in Figure 2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "BEV Feature Extractor", "weight": 1.0} -->

The objective of BEV feature extractor is to lift various modality inputs into a canonical feature space and aggregates and align features these features into a canonical representation termed BEV features ${\mathcal{F}}_{BEV} \in {\mathbb{R}}^{W \times H \times {({C_{1} + C_{2}})}}$ based on their coordinates, where $W$ and $H$ represent the width and height of the BEV feature, respectively; $C_{1}$ and $C_{2}$ represent the output channels of the BEV feature extracted from the two common modalities: surrounding camera images $\mathcal{I}$ and LiDAR points $\mathcal{P}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "BEV Feature Extractor", "weight": 1.0} -->

Camera branch. We use ResNet to extract features from images, followed by a feature transformation module from image space to BEV space. VectorMapNet does not rely on certain feature transformation approaches and we opt to use a simple but popular variant of IPM, which produces BEV features of ${\mathcal{F}}_{BEV}^{\mathcal{I}} \in {\mathbb{R}}^{W \times H \times C_{1}}$. The detailed structure of the image extractor can be found in Appendix C.3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "BEV Feature Extractor", "weight": 1.0} -->

LiDAR branch. For LiDAR data $\mathcal{P}$, we use a variant of PointPillars with dynamic voxelization, which divides the 3D space into multiple pillars and uses pillar-wise point clouds to learn pillar-wise feature maps. We denote this feature map in BEV as ${\mathcal{F}}_{BEV}^{\mathcal{P}} \in {\mathbb{R}}^{W \times H \times C_{2}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "BEV Feature Extractor", "weight": 1.0} -->

For sensor fusion, we obtain the BEV features ${\mathcal{F}}_{BEV} \in {\mathbb{R}}^{W \times H \times {({C_{1} + C_{2}})}}$ by concatenating ${\mathcal{F}}_{BEV}^{\mathcal{I}}$ and ${\mathcal{F}}_{BEV}^{\mathcal{P}}$, and then process the concatenated result with a two-layer convolutional network. An overview of the BEV feature extractor is shown at the bottom-left of Figure 2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Map Element Detector", "weight": 1.0} -->

After extracting the bird's-eye view (BEV) features, VectorMapNet have to identify and abstractly represent map elements using these features. We employ a hierarchical representation for this purpose, specifically through element queries and keypoint queries, enabling us to model the non-local shape of map elements effectively. We leverage a variant of transformer set prediction detector to achieve this goal, as it is a robust detector that eliminates the need for extra post-processing. Specifically, the detector represents map elements' locations and categories by predicting their element keypoints $\mathcal{A}$ and class labels $\mathcal{L}$ from the BEV features ${\mathcal{F}}_{BEV}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Map Element Detector", "weight": 1.0} -->

Element queries. The detector uses learnable element queries ${{\mathbf{q}}_{i}^{elem} \in \left. {\mathbb{R}}^{k \times d} \middle| i \right. = 1},{\ldots,N_{\max}}$ as its inputs, where $d$ represents the hidden embedding size and $N_{\max}$ is a preset constant, which is much greater than the number of map elements $N$ in the scene. The $i$-th element query ${\mathbf{q}}_{i}^{elem}$ is composed of $k$ element keypoint embeddings ${\mathbf{q}}_{i,j}^{kp}$: ${\mathbf{q}}_{i}^{elem} = \left.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Map Element Detector", "weight": 1.0} -->

\{{{\mathbf{q}}_{i,j}^{kp} \in {\mathbb{R}}^{d}} \middle| {j = {1,\ldots,k}}\} \right.$. Element queries are similar to object queries used in Detection Transformer (DETR), where a query represents an object. In our case, an element query represents a map element.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Map Element Detector", "weight": 1.0} -->

Keypoint representations. In object detection problems, people use bounding box to abstract object shape. Here we use $k$ element keypoints locations ${\mathbf{A}}_{i} = \left. \{{{\mathbf{a}}_{i,j} \in {\mathbb{R}}^{2}} \middle| {j = {1,\ldots,k}}\} \right.$ (please refer to Figure 3), to represent the outline of a map element. However, defining keypoints for map elements is not straightforward due to their diversity. We conduct an ablation study to investigate the performance of different choices in § 4.3. Note that element keypoints are different from polyline vertices and the element keypoints are intermediate representations of VectorMapNet that are passed to the polyline generator (§ 3.4) for conditional prediction, and the number of keypoints for each type of polyline is fixed and determined by its definition. Polylines are our output representations.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Map Element Detector", "weight": 1.0} -->

Architecture. The overall architecture of the map element detector consists of a transformer decoder and a prediction head, as shown at the bottom-middle of Figure 2. The decoder transforms the element queries using multi-head self-/cross-attention mechanisms. In particular, we use the deformable attention module as the decoder's cross attention module, where each element query has a 2D location grounding. It improves interpretability and accelerates training convergence.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Polyline Generator", "weight": 1.0} -->

Upon the approximate position, shape, and category of map elements identified by map element detector, the polyline generator focuses on the detailed geometry of HD map, which entails calculating variable-length polyline vertices and their order. Accurate modeling of vertex relationships is crucial - for instance, a white line between two vertices often signifies a line connection in the vectorized map. The polyline generator operates as a discrete distribution $p{(\left. {\mathbf{V}}_{i}^{poly} \middle| {{\mathbf{A}}_{i},l_{i},{\mathcal{F}}_{BEV}^{f}} \right.)}$ over the vertices of each polyline, conditioned on the initial layout (i.e., element keypoints ${\mathbf{A}}_{i}$ and class label $l_{i}$) and BEV features. To estimate this distribution, we decompose the joint distribution over each polyline ${\mathbf{V}}_{i}^{poly}$ as a product of a series of conditional vertex coordinate distributions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Polyline Generator", "weight": 1.0} -->

In particular, we transform each polyline ${\mathbf{V}}_{i}^{poly} = \left. \{{{\mathbf{v}}_{i,n} \in {\mathbb{R}}^{2}} \middle| {n = {1,\ldots,N_{v}}}\} \right.$ into a flattened sequence $\left. \{{v_{i,n}^{f} \in {\mathbb{R}}} \middle| {n = {1,\ldots,{2N_{v}}}}\} \right.$ by concatenating coordinates values of polyline vertices and add an additional End of Sequence token ($EOS$) at the end of each sequence, and the target distribution turns into: Following PolyGen, we use a categorical distribution to model the probability of each vertex position given the preceding vertex position. This allows us to model the complex and irregular shapes of map elements while maintaining the efficiency of discrete distributions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Polyline Generator", "weight": 1.0} -->

And we model this distribution using an autoregressive network that outputs the parameters of a predictive distribution at each step for the next vertex coordinate. This predictive distribution is defined over all possible discrete vertex coordinate values and $EOS$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Polyline Generator", "weight": 1.0} -->

Vertices as discrete variables. Using discrete distributions to model polyline vertices has the advantage of representing arbitrary shapes, i.e., categorical distributions can easily represent various polylines, such as multi-modal, skewed, peaked, or long-tailed, that are commonly seen in our task. Thus, we quantize the coordinate values into discrete tokens and model each token with a categorical distribution. We also conduct an ablation study in Appendix § D.2 to investigate other choices.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Polyline Generator", "weight": 1.0} -->

Architecture. To model these local geometric structures of polylines, the autoregressive network we choose is Transformer (see the bottom-right of Figure 2). Transformer architecture has consistently demonstrated superior performance in conditional sequence generation tasks and are highly effective at capturing the vertex dependencies present in map data. Each polyline's keypoint coordinates and class label are tokenized and fed in as the query inputs of the transformer decoder. Then a sequence of vertex tokens are fed into the transformer iteratively, integrating BEV features with cross-attention, and decoded as polyline vertices. Note that the generator can generate all polylines in parallel.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Polyline Generator", "weight": 1.0} -->

Vertex embeddings. Following PolyGen, we use an addition of three learned embeddings as the embedding of each vertex token: Coordinate Embedding, indicating whether the token represents $x$ or $y$ coordinate; Position Embedding, representing which vertex the token belongs to; Value Embedding, expressing the token's quantized coordinate value.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Learning", "weight": 1.0} -->

We train our model by minimizing the sum of map element detector loss and polyline generator loss: Map element detector loss. Following, the detector is trained with bipartite matching loss, thus avoiding post-processing steps like non-maximum suppression (NMS). We describe the detail of the map element detector loss $\mathcal{L}_{det}$ function in Appendix § C.4.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Learning", "weight": 1.0} -->

Polyline generator loss. Polyline generator is trained to maximize the log-probability of the polyline vertices. We use negative log-likelihood as its loss function: where $\hat{p}{(\left. v_{i,n}^{f} \middle| \ldots \right.)}$ is the conditional probability of discrete coordinate value $v_{i,n}^{f}$, and $v_{i,{< n}}^{f}$ are ground truth discrete coordinate values with index less than $n$. The default training strategy is teacher forcing, meaning that we use ground truth keypoints as generator input. To avoid the exposure bias, we further experiment with first training with teacher forcing, and then fine-tuning with predicted keypoints.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

Experiments protocol. We conduct experiments on the nuScenes and Argoverse2 dataset. Following HDMapNet, we assess the quality of a predicted HD map by comparing its components (i.e., polylines) with ground truth. Both HDMapNet and our paper use Chamfer distance for polyline matching (Chamfer AP). Additionally, we also introduced another distance metric termed Fréchet distance (Fréchet AP), which better measures the distance between polylines by considering the order of vertices. The definitions and calculation processes of Chamfer AP and Fréchet AP are in § A.2. Additionally, the details of dataset settings (§ A.1), implementations (§ C), and additional qualitative results (§ B) are presented in the Appendix as well.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

VectorMapNet (Camera) + fine-tune VectorMapNet (Fusion) + fine-tune Table 1: Results on nuScenes dataset. Fusion denotes the model using both images and LiDAR points as inputs. Methods with fine-tune means the model is applied two stage training strategy introduced in § 3.5

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

#dim

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

The HD semantic map construction is a new problem, and there are no established methods to compare. Therefore, we carefully chose two baselines HDMapNet and STSU that are representative and can effectively compare with VectorMapNet. Specifically: HDMapNet can provide valuable insights into the effectiveness of commonly used map segmentation methods for HD semantic map construction. STSU, a direct map structure learning method, can provide valuable insights into its effectiveness for HD semantic map construction. Moreover, our baseline comparison also includes the results of HDMapNet and VectorMapNet using different modalities as inputs, which demonstrate the impact of different feature extraction methods on HD semantic map construction. The details of baselines model are described in Appendix § C.5. We report the average precision that uses Chamfer distance as the threshold to determine the positive matches with ground truth. $\{ 0.5,1.0,1.5\}$ are the predefined thresholds of Chamfer distance AP.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

Results on nuScenes. As shown in Table 1, VectorMapNet outperforms HDMapNet by a large margin under all settings (+17.9 mAP in Camera, +9.9 mAP in LiDAR, and +14.2 mAP in Fusion). Compared to camera-only and LiDAR-only, sensor fusion introduces +4.3 mAP improvement and +11.2 mAP improvement, respectively. As described in § 3.5, our two stage training strategy further boosts the performance of both camera-only and sensor fusion methods by +6.9 mAP and +8.5 mAP, respectively. STSU is -29.2 mAP lower than VectorMapNet. Since STSU treats all map elements as a set of fixed-size segments, we hypothesize that ignoring the fine geometry of map elements hurts the performance.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison with Baselines", "weight": 1.0} -->

Results on Argoverse2. We further compare HDMapNet and VectorMapNet on Argoverse2 dataset, shown in Table 2. Since Argoverse2 provides z-axis annotations, we give VectorMapNet results both in 2D and 3D. In many cases of Argoverse2, the annotated boundaries and divider lines overlap with each other, making it difficult for models to separate them. It results in a drop in performance of both methods, especially in AP$_{divider}$ of HDMapNet (21.7 AP$_{divider}$ to 5.7 AP$_{divider}$) because its rasterized representation fails to handle these cases. In contrast, VectorMapNet remains competent, showing the advantage of using vectorized representation to represent overlapping elements.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Benefits of using polylines as primitives. From visualizations, we find that using polylines as primitives has brought us two benefits compared with baselines: First, polylines effectively encode the detailed geometries of map elements, e.g. the corners of boundaries (see the red ellipses in Figure 4). Second, polyline representations prevent VectorMapNet from generating ambiguous results, as it consistently encodes direction information. In contrast, Rasterized methods are prone to falsely generating loopy curves (see the blue ellipses in Figure 4). These ambiguities hinder safe autonomous driving. Therefore, the polyline is a desired primitive for map learning, as it can reflect real-world road layouts and explicitly encode directions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Benefits of posing map learning as a detection problem. VectorMapNet operates in a top-down detection manner: it first models the map's topology and the locations of map elements, then generates the details of these elements. Visualizations demonstrate that VectorMapNet captures all map elements comprehensively, even the smaller ones near edges. The high mAP of VectorMapNet, when compared to other baselines, validates this observation. We attribute these impressive results to the model's ability to model topological relationships between map elements, thus implicitly capturing complex scene interrelationships. This is evidenced by Figure 6, where the model identifies pedestrian crossings at intersections that are missed in the annotations of the HD map provided by the dataset. Although these relationships are not explicitly taught, the model learns them via controlled information propagation between query embeddings, using self-attention modules --- a technique from the original Transformer paper. This showcases the model's proficient scene understanding.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Centerline prediction by VectorMapNet. As discussed in § 3.1 and above, the polyline is a versatile primitive, capable of representing map element classes that extend beyond the elements in the HD semantic map setting. To further demonstrate this flexibility, we expand VectorMapNet to predict the centerline, an imaginary line commonly used as a reference for driving direction, vehicle positioning, and navigation. The adaptation is quite straightforward: VectorMapNet treats centerlines as a set of polylines and implicitly encodes their topological relations. This process involves no modifications to the model structure. Figure 5 displays the results of VectorMapNet's centerline prediction.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Traj. + Pred. Map Table 4: The benefits of predicted maps in improving the motion forecasting baseline. There are three input settings: past trajectories (denoted as Traj.), past trajectories with the human-annotated HD map from the nuScenes (denoted as Traj. + G.T. Map), and past trajectories with the predicted map from VectorMapNet (denoted as Traj. + Pred. Map). The predicted map greatly improves the prediction performance compared with the model that only use past trajectories.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We provide ablation studies for keypoint representation in this section. For other ablation studies (i.e., curve sampling strategies, vertex modeling methods, and extrinsic robustness), please refer to Appendix § D.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Keypoint representations. Since there is no straightforward keypoint design to represent map elements with few fixed number of points, we propose three simple representations as shown in Figure 3: Bounding Box (Bbox), which is the smallest box enclosing a polyline, and its keypoints are defined as the top-right and bottom-left points of the box; Start-Middle-End (SME), which samples the start, middle, and end point from a polyline; Extreme Points, which are the left-most, right-most, top-most, and bottom-most points of a polyline. We experiment with these representations and list the results in Table 3. Our results show that the bounding box representation leads to the best mean average performance in both metrics, outperforming others by 2.0 Fréchet mAP and 7.3 Chamfer mAP.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Motion Forecasting with Vectorized HD Maps from VectorMapNet", "weight": 1.0} -->

To evaluate the capacity of our method to understand scene relationships and to investigate its usefulness in subsequent tasks, we put our predicted HD map to the test within a motion forecasting task. This task heavily relies on precise map information for accurate prediction of future motion.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Motion Forecasting with Vectorized HD Maps from VectorMapNet", "weight": 1.0} -->

Task Settings. The motion forecasting requires that the model have to predict 6 possible future trajectories (3 seconds) from past agents' trajectories (1 second) and an HD semantic map spanning ${{60m} \times 30}m$. Data is generated from the nuScenes tracking dataset, selecting agents with complete 3-second future observations. This results in 25,645 training and 5,460 test samples. We examine three input scenarios: past trajectories alone, past trajectories with the true HD map, and past trajectories with the VectorMapNet predicted map. We utilize mmTransformer for motion forecasting due to its versatility in using map data or relying solely on past trajectories. This assists in assessing the quality of our learned maps.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Motion Forecasting with Vectorized HD Maps from VectorMapNet", "weight": 1.0} -->

Results. To evaluate the performance of motion forecasting under different input settings, we report results on three commonly used metrics: minimum average displacement error (minADE), minimum final displacement error (minFDE) and miss rate (MR). To get the results, these metrics only account for the best trajectory out of 6 predicted trajectories. Results in Table 4 show that the map predicted by VectorMapNet has encoded environment information that greatly helps the motion forecaster, compared with the model that only takes past trajectories as inputs. The gap between the ground-truth map and the predicted map is not big either, especially in terms of MR (-0.2%). We think future research could further close the performance gap.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussions", "weight": 1.0} -->

Limitations. It is worth noting that the model has some limitations, and we leave it for future works. Lacking Temporal Information: The model generates coherent geometries in a single frame but doesn't guarantee temporally consistent predictions. Mismatch Problem of a Two-stage Model: A feature space mismatch exists between the map element detector and the polyline generator due to the teacher-forcing training strategy. Although fine-tuning is necessary for optimal performance, it results in tricky training schedules. Hallucination Ability: The model can make predictions at locations that are occluded and not visible to cameras, showcasing its scene understanding capabilities. However, this reduces the model's interpretability.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussions", "weight": 1.0} -->

For further discussions, such as the potential societal impact of our method, please refer to Appendix § E.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We present VectorMapNet, an end-to-end model to tackle the HD semantic map learning problem. Unlike existing works, VectorMapNet uses polylines as the primitives to represent vectorized HD map elements. To predict polylines from sensor data, we decompose the problem into a detection step and a generation step. Our experiments show that VectorMapNet can generate coherent and complex geometries for urban map elements, benefiting from the polyline primitives. We believe that this novel way to learn HD maps provides a new perspective on the HD semantic map learning problem.
