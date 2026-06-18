<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HDMapNet: An Online HD Map Construction and Evaluation Framework

Topics include High-definition map construction, Semantic map learning, Autonomous driving, Bird's-eye view perception, Sensor fusion, Lane detection, Chamfer distance, Vectorized maps, NuScenes, HDMapNet.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces online HD semantic map learning from onboard cameras and LiDAR, with HDMapNet producing bird's-eye-view semantic, instance, and direction predictions that can be converted into vectorized lane dividers, boundaries, and crossings. The paper is especially useful as an early benchmark and metric proposal for learned HD map construction, including semantic- and instance-level evaluations based on raster overlap, Chamfer-style geometry distance, and average precision.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Constructing HD semantic maps is a central component of autonomous driving. However, traditional pipelines require a vast amount of human efforts and resources in annotating and maintaining the semantics in the map, which limits its scalability. In this paper, we introduce the problem of HD semantic map learning, which dynamically constructs the local semantics based on onboard sensor observations. Meanwhile, we introduce a semantic map learning method, dubbed HDMapNet. HDMapNet encodes image features from surrounding cameras and/or point clouds from LiDAR, and predicts vectorized map elements in the bird's-eye view. We benchmark HDMapNet on nuScenes dataset and show that in all settings, it performs better than baseline methods. Of note, our camera-LiDAR fusion-based HDMapNet outperforms existing methods by more than 50% in all metrics. In addition, we develop semantic-level and instance-level metrics to evaluate the map learning performance. Finally, we showcase our method is capable of predicting a locally consistent map. By introducing the method and metrics, we invite the community to study this novel map learning problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-definition (HD) semantic maps are an essential module for autonomous driving. Traditional pipelines to construct such HD semantic maps involve capturing point clouds beforehand, building globally-consistent maps using SLAM, and annotating semantics in the maps. This paradigm, though producing accurate HD maps and adopted by many autonomous driving companies, requires a vast amount of human efforts.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an alternative, we investigate scalable and affordable autonomous driving solutions, e.g. minimizing human efforts in annotating and maintaining HD maps. To that end, we introduce a novel semantic map learning framework that makes use of on-board sensors and computation to estimate vectorized local semantic maps. Of note, our framework does not aim to replace global HD map reconstruction, instead to provide a simple way to predict local semantic maps for real-time motion prediction and planning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a semantic map learning method named HDMapNet, which produces vectorized map elements from images of the surrounding cameras and/or from point clouds like LiDARs. We study how to effectively transform perspective image features to bird's-eye view features when depth is missing. We put forward a novel view transformer that consists of both neural feature transformation and geometric projection. Moreover, we investigate whether point clouds and camera images complement each other in this task. We find different map elements are not equally recognizable in a single modality. To take the best from both worlds, our best model combines point cloud representations with image representations. This model outperforms its single-modal counterparts by a significant margin in all categories. To demonstrate the practical value of our method, we generate a locally-consistent map using our model in Figure 6; the map is immediately applicable to real-time motion planning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we propose comprehensive ways to evaluate the performance of map learning. These metrics include both semantic level and instance level evaluations as map elements are typically represented as object instances in HD maps. On the public NuScenes dataset, HDMapNet improves over existing methods by 12.1 IoU on semantic segmentation and 13.1 mAP on instance detection.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a novel online framework to construct HD semantic maps from the sensory observations, and together with a method named HDMapNet.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We come up with a novel feature projection module from perspective view to bird's-eye view. This module models 3D environments implicitly and considers the camera extrinsic explicitly.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop comprehensive evaluation protocols and metrics to facilitate future research.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Semantic Map Learning", "weight": 1.0} -->

We propose semantic map learning, a novel framework that produces local high-definition semantic maps. It takes sensor inputs like camera images and LiDAR point clouds, and outputs vectorized map elements, such as lane dividers, lane boundaries and pedestrian crossings. We use $\mathcal{I}$ and $P$ to denote the images and point clouds, respectively. Optionally, the framework can be extended to include other sensor signals like radars. We define $\mathcal{M}$ as the map elements to predict.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A HDMapNet", "weight": 1.0} -->

Our semantic map learning model, named HDMapNet, predicts map elements $\mathcal{M}$ from single frame $\mathcal{I}$ and $P$ with neural networks directly. An overview is shown in Figure 2, four neural networks parameterize our model: a perspective view image encoder $\phi_{\mathcal{I}}$ and a neural view transformer $\phi_{\mathcal{V}}$ in the image branch, a pillar-based point cloud encoder $\phi_{P}$, and a map element decoder $\phi_{\mathcal{M}}$. We denote our HDMapNet family as HDMapNet(Surr), HDMapNet(LiDAR), HDMapNet(Fusion) if the model takes only surrounding images, only LiDAR, or both of them as input.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A1 Image encoder", "weight": 1.0} -->

Our image encoder has two components, namely perspective view image encoder and neural view transformer.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A1 Image encoder", "weight": 1.0} -->

Perspective view image encoder. Our image branch takes perspective view inputs from $N_{m}$ surrounding cameras, covering the panorama of the scene. Each image $\mathcal{I}_{i}$ is embedded by a shared neural network $\phi_{\mathcal{I}}$ to get perspective view feature map $\mathcal{F}_{\mathcal{I}_{i}}^{pv} \subseteq {\mathbb{R}}^{H_{pv} \times W_{pv} \times K}$ where $H_{pv}$, $W_{pv}$, and $K$ are the height, width, and feature dimension respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A1 Image encoder", "weight": 1.0} -->

Neural view transformer. As shown in Figure 3, we first transform image features from perspective view to camera coordinate system and then to bird's-eye view.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A1 Image encoder", "weight": 1.0} -->

where $\phi_{\mathcal{V}_{i}}^{hw}$ models the relation between feature vector at position $(h,w)$ in the camera coodinate system and every pixel on the perspective view feature map. We denote $H_{c}$ and $W_{c}$ as the top-down spatial dimensions of $F_{\mathcal{I}}^{c}$. The bird's-eye view (ego coordinate system) features $\mathcal{F}_{\mathcal{I}_{i}}^{bev} \subseteq {\mathbb{R}}^{H_{bev} \times W_{bev} \times K}$ is obtained by transforming the features $\mathcal{F}_{\mathcal{I}_{i}}^{c}$ using geometric projection with camera extrinsics, where $H_{bev}$ and $W_{bev}$ are the height and width in the bird's-eye view.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A1 Image encoder", "weight": 1.0} -->

The final image feature $\mathcal{F}_{\mathcal{I}}^{bev}$ is an average of $N_{m}$ camera features.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A2 Point cloud encoder", "weight": 1.0} -->

Our point cloud encoder $\phi_{P}$ is a variant of PointPillar with dynamic voxelization, which divide the 3d space into multiple pillars and learn feature maps from pillar-wise features of pillar-wise point clouds. The input is $N$ lidar points in the point cloud. For each point $p$, it has three-dimensional coordinates and additional $K$-dimensional features represented as $f_{p} \subseteq {\mathbb{R}}^{K + 3}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A2 Point cloud encoder", "weight": 1.0} -->

When projecting features from points to bird's-eye view, multiple points can potentially fall into the same pillar. We define $P_{j}$ as the set of points corresponding to pillar $j$. To aggregate features from points in a pillar, a PointNet (denoted as $PN$) is warranted, where

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A2 Point cloud encoder", "weight": 1.0} -->

Then, pillar-wise features are further encoded through a convolutional neural network $\phi_{pillar}$. We denote the feature map in the bird's-eye view as $\mathcal{F}_{P}^{bev}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A3 Bird's-eye view decoder", "weight": 1.0} -->

The map is a complex graph network that includes instance-level and directional information of lane dividers and lane boundaries. Instead of pixel-level representation, lane lines need to be vectorized so that they can be followed by self-driving vehicles. Therefore, our BEV decoder $\phi_{\mathcal{M}}$ not only outputs semantic segmentation but also predicts instance embedding and lane direction. A post-processing process is applied to cluster instances from embeddings and vectorize them.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A3 Bird's-eye view decoder", "weight": 1.0} -->

Overall architecture. The BEV decoder is a fully convolutional network (FCN) with 3 branches, namely semantic segmentation branch, instance embedding branch, and direction prediction branch. The input of BEV decoder is image feature map $F_{\mathcal{I}}^{bev}$ and/or point cloud feature map $F_{P}^{bev}$, and we concatenate them if both exist.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A3 Bird's-eye view decoder", "weight": 1.0} -->

Semantic prediction. The semantic prediction module is a fully convolutional network (FCN) We use cross-entropy loss for the semantic prediction.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A3 Bird's-eye view decoder", "weight": 1.0} -->

Instance embedding. Our instance embedding module seeks to cluster each bird's-eye view embedding. For ease of notation, we follow the exact definition: $C$ is the number of clusters in the ground truth, $N_{c}$ is the number of elements in cluster $c$, $\mu_{c}$ is the mean embedding of cluster c, $\parallel \cdot \parallel$ is the L2 norm, and ${\lbrack x\rbrack}_{+}$ = max(0, x) denotes the element maximum. $\delta_{v}$ and $\delta_{d}$ are respectively the margins for the variance and distance loss.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A3 Bird's-eye view decoder", "weight": 1.0} -->

Direction prediction. Our direction module aims to predict directions of lanes from each pixel $C$. The directions are discretized into $N_{d}$ classes uniformed distributed on a unit circle. By classifying direction $D$ of current pixel $C_{now}$, the next pixel of lane $C_{next}$ can be obtained as $C_{next} = {C_{now} + {\Delta_{step} \cdot D}}$, where $\Delta_{step}$ is a predefined step size. Since we don't know the direction of the lane, we cannot identify the forward and backward direction of each node. Instead, we treat both of them as positive labels. Concretely, the direction label of each lane node is a $N_{d}$ vector with 2 indices labeled as 1 and others labeled as 0. Note that most of the pixels on the topdown map don't lie on the lanes, which means they don't have directions. The direction vector of those pixels is a zero vector and we never do backpropagation for those pixels during training. We use softmax as the activation function for classification.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A3 Bird's-eye view decoder", "weight": 1.0} -->

Vectorization. During inference, we first cluster instance embeddings using the Density-Based Spatial Clustering of Applications with Noise (DBSCAN). Then non-maximum suppression (NMS) is used to reduce redundancy. Finally, the vector representations are obtained by greedily connecting the pixels with the help of the predicted direction.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Evaluation", "weight": 1.0} -->

In this section, we propose evaluation protocols for semantic map learning, including semantic metrics and instance metrics.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B1 Semantic metrics", "weight": 1.0} -->

The semantics of model predictions can be evaluated in the Eulerian fashion and the Lagrangian fashion. Eulerian metrics are computed on a dense grid and measure the pixel value differences. In contrast, Lagrangian metrics move with the shape and measure the spatial distances of shapes.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B1 Semantic metrics", "weight": 1.0} -->

Eulerian metrics. We use intersection-over-union (IoU) as Eulerian metrics, which is given,

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B1 Semantic metrics", "weight": 1.0} -->

where ${\mathcal{D}_{1},\mathcal{D}_{2}} \subseteq {\mathbb{R}}^{H \times W \times D}$ are dense representations of shapes (curves rasterized on a grid); $H$ and $W$ are the height and width of the grid, $D$ is number of categories; $| \cdot |$ denotes the size of the set.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B1 Semantic metrics", "weight": 1.0} -->

Lagrangian metrics. We are interested in structured outputs, namely curves consists of connected points.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B1 Semantic metrics", "weight": 1.0} -->

where ${CD}_{dir}$ is the directional Chamfer distance and $CD$ is the bi-directional Chamfer distance; $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$ are the two sets of points on the curves.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B2 Instance metrics", "weight": 1.0} -->

We further evaluate the instance detection capability of our models. We use average precision (AP) similar to the one in object detection, given by

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B2 Instance metrics", "weight": 1.0} -->

where ${AP}_{r}$ is the precision at recall=$r$. We collect all predictions and rank them in descending order according to the semantic confidences. Then, we classify each prediction based on the CD threshold. For example, if the CD is lower than a predefined threshold, it is considered true positive, otherwise false positive. Finally, we obtain all precision-recall pairs and compute APs accordingly.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Implementation details", "weight": 1.0} -->

Tasks & Metrics. We evaluate our approach on the NuScenes dataset. We focus on two sub-tasks: semantic map segmentation and instance detection. Due to the limited types of map elements in the nuScenes dataset, we consider three static map elements: lane boundary, lane divider, and pedestrian crossing.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Implementation details", "weight": 1.0} -->

Architecture. For the perspective view image encoder, we adopt EfficientNet-B0 pre-trained on ImageNet, as. Then, we use a multi-layer perceptron (MLP) to convert the perspective view features to bird's-eye view features in the camera coordinate system. The MLP is shared channel-wisely and does not change the feature dimension. For point clouds, we use a variant of PointPillars with dynamic voxelization. We use a PointNet with a 64-dimensional layer to aggregate points in a pillar. ResNet with three blocks is used as the BEV decoder.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Implementation details", "weight": 1.0} -->

Training details. We use the cross-entropy loss for the semantic segmentation, and use the discriminative loss (Equation 5) for the instance embedding where we set $\alpha = \beta = 1$, $\delta_{v} = 0.5$, and $\delta_{d} = 3.0$. We use Adam for model training, witfh a learning rate of ${1e} - 3$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Baseline methods", "weight": 1.0} -->

For all baseline methods, we use the same image encoder and decoder as HDMapNet and only change the view transformation module.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Baseline methods", "weight": 1.0} -->

Inverse Perspective Mapping (IPM). The most straightforward baseline is to map segmentation predictions to the bird's-eye view via IPM.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Baseline methods", "weight": 1.0} -->

IPM with bird's-eye view decoder (IPM(B)). Our second baseline is an extension of IPM. Rather than making predictions in perspective view, we perform semantic segmentation directly in bird-eye view.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Baseline methods", "weight": 1.0} -->

IPM with perspective view feature encoder and bird's-eye view decoder (IPM(CB)). The next extension is to perform feature learning in the perspective view while making predictions in the bird's-eye view.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Baseline methods", "weight": 1.0} -->

Lift-Splat-Shoot. Lift-Splat-Shoot estimates a distribution over depth in the perspective view images. Then, it converts 2D images into 3D point clouds with features and projects them into the ego vehicle frame.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Baseline methods", "weight": 1.0} -->

View Parsing Network (VPN). VPN proposes a simple view transformation module: a view relation module to model the relations between any two pixels and a view fusion module to fuses the features of pixels.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Results", "weight": 1.0} -->

We compare our HDMapNet against baselines in Section IV-B. Table I shows the comparisons. First, Our HDMapNet(Surr), which is the surrounding camera-only method, outperforms all baselines. This suggests that our novel learning-based view transformation is indeed effective, without making impractical assumptions about a complex ground plane (IPM) or estimating the depth (Lift-Splat-Shoot). Second, our HDMapNet(LiDAR) is better than HDMapNet(Surr) in boundary but worse in divider and pedestrian crossing. This indicates different categories are not equally recognizable in one modality. Third, our fusion model with both camera images and LiDAR point clouds achieves the best performance. It improves over baselines and our camera-only method by 50% relatively.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Results", "weight": 1.0} -->

Another interesting phenomenon is that various models behave differently in terms of the CD. For example, VPN has the lowest CD~P~ in all categories, while it underperforms its counterparts on CD~L~ and has the worst overall CD. Instead, our HDMapNet(Surr) balances both CD~P~ and CD~L~, achieving the best CD among all camera-only-based methods. This finding indicates that CD is complementary to IoU, which shows the precision and recall aspects of models. This helps us understand the behaviors of different models from another perspective.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Results", "weight": 1.0} -->

Instance map detection. In Figure 2 (Instance detection branch), we show the visualization of embeddings using principal component analysis (PCA). Different lanes are assigned different colors even when they are close to each other or have intersections. This confirms our model learns instance-level information and can predict instance labels accurately. In Figure 2 (Direction classification branch), we show the direction mask predicted by our direction branch. The direction is consistent and smooth. We show the vectorized curve produced after post processing in Figure 4. In Table II, we present the quantitative results of instance map detection. HDMapNet(Surr) already outperforms baselines while HDMapNet(Fusion) is significantly better than all counterparts, e.g., it improves over IPM by 55.4%.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C Results", "weight": 1.0} -->

Sensor fusion. In this section, we further analyze the effect of sensor fusion for constructing HD semantic maps. As shown in Table I, for divider and pedestrian crossing, HDMapNet(Surr) outperforms HDMapNet(LiDAR), while for lane boundary, HDMapNet(LiDAR) works better. We hypothesize this is because there are elevation changes near the lane boundary, making it easy to detect in LiDAR point clouds. On the other hand, the color contrast of road divider and pedestrian crossing is helpful information, making two categories more recognizable in images; visualizations also confirm this in Figure 4. The strongest performance is achieved when combining LiDAR and cameras; the combined model outperforms both models with a single sensor by a large margin. This suggests these two sensors include complementary information for each other.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-C Results", "weight": 1.0} -->

Bad weather conditions. Here we assess the robustness of our model under extreme weather conditions. As shown in Figure 5, our model can generate complete lanes even when lighting condition is bad, or when the rain obscures sight. We speculate that the model can predict the shape of the lane based on partial observations when the roads are not completely visible. Although there are performance drop in extreme weather condition, the overall performance is still reasonable. (Table III)

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-C Results", "weight": 1.0} -->

Temporal Fusion. Here we experiment on temporal fusion strategies. We first conduct short-term temporal fusion by pasting feature maps of previous frames into current's according to ego poses. The feature maps are fused by max pooling and then fed into decoder. As shown in Table IV, fusing multiple frames can improve the IoU of the semantics. We further experiment on long-term temporal accumulation by fusing segmentation probabilities. As shown in Figure 6, our method produces consistent semantic maps with larger field of view while fusing multiple frames.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

HDMapNet predicts HD semantic maps directly from camera images and/or LiDAR point clouds. The local semantic map learning framework could be a more scalable approach than the global map construction and annotation pipeline that requires a significant amount of human efforts. Even though our baseline method of semantic map learning does not produce map elements as accurate, it gives system developers another possible choice of the trade-off between scalability and accuracy.
