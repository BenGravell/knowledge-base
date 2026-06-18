<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PolarStream: Streaming Lidar Object Detection and Segmentation with Polar Pillars

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent works recognized lidars as an inherently streaming data source and showed that the end-to-end latency of lidar perception models can be reduced significantly by operating on wedge-shaped point cloud sectors rather then the full point cloud. However, due to use of cartesian coordinate systems these methods represent the sectors as rectangular regions, wasting memory and compute. In this work we propose using a polar coordinate system and make two key improvements on this design. First, we increase the spatial context by using multi-scale padding from neighboring sectors: preceding sector from the current scan and/or the following sector from the past scan. Second, we improve the core polar convolutional architecture by introducing feature undistortion and range stratified convolutions. Experimental results on the nuScenes dataset show significant improvements over other streaming based methods. We also achieve comparable results to existing non-streaming methods but with lower latencies. The code and pretrained models are available .

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ability to accurately perceive objects in dense urban environments still remains a challenging problem for self-driving cars. While such self-driving cars typically deploy a wide variety of sensors lidars play a key role due to the accurate range information provided. Driven in part by the availability of benchmark datasets, the last decade has seen tremendous progress in lidar based 3D object detection. However, these methods all ignore the fact that most lidar sensors scan the scene sequentially as the lidar rotates around the z-axis. They instead wait for the rotational scan to complete (colloquially known as full sweep) before processing data, thereby introducing a large data capture latency (usually 50 to 100 ms).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, Han et al. and then STROBE recognized this problem and proposed solutions which processed lidar sectors (shown in Fig. 1) as soon as they arrived. They showed that a streaming based architecture can achieve significantly reduced latency over the traditional non-streaming baselines. Both of these methods encode the point clouds as an image in bird's-eye view (BEV) using cuboid-shaped voxels. In doing so, they ignore the natural polar representation formed by the lidar sectors. Using cuboid-shaped voxels restricts them to performing convolutions on the minimal rectangular

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

region enclosing the point cloud sector which wastes both computation and memory. As shown in Fig. 1, a large portion of the enclosed rectangular region remains empty.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another challenge associated with streaming perception models is the limited view of the scene observed by each sector. Objects close to the ego-vehicle can often be fragmented across multiple sectors as shown by the car highlighted in green in Fig.1. Han et al. proposes to increase the context available to the model by maintaining a recurrent memory across consecutive sectors. STROBE also aggregates representations from the previous sectors by maintaining full-sweep feature maps across multiple scales. However, both these solutions add extra computation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose to encode individual point cloud sectors using polar pillars. Polar pillars naturally address the inefficiency of existing streaming approaches by representing the point cloud sectors as more compact wedge-shaped regions as shown in Fig. 1. Further, we propose a simple minimal-latency approach to enhance the context available to the model by simply padding the representation of the neighboring sectors across multiple strides of the backbone. Using polar pillars allows us to pad features from the preceding sector of the current scan and/or the following sector from the previous scan, no matter how many sectors the full sweep is divided into.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The polar BEV representation has recently started gaining attention in the lidar perception literature primarily because it balances the points across grid cells. In fact, polar grid outperforms the cartesian grid on the lidar segmentation task. However, the detection peformance on a polar grid still lags the cartesian grid. This is because of the distortion the objects undergo when this representation is ultimately unfolded to a rectangular representation to enable the use of convolutional layers. The object represented by the green box in Fig. 2 shows an example of this distortion. Further, the distortion increases with range as the pillars progressively become larger. This makes a polar representation not compatible with the translation-invariance property of convolution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose several techniques to address the distortion problem described above. We first propose a Feature Undistortion module which transforms the polar representation into a canonical Cartesian representation (as shown in Fig. 2) for classification branch. Next, we propose using the Range Stratified Convolution&Normalization layers on the regression branches of the detection head. These layers apply different convolution kernels and normalization based on range (Fig.2) to cater to the changing pillar sizes in a polar grid. Our proposed model closes the gap on 3D object detection models using cartesian representations without adding any significant latency.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we train multitasking streaming models that do simultaneous 3D object detection, lidar segmentation and panoptic segmentation, for the first time in literature. Results on the nuScenes dataset show that our proposed model PolarStream outperforms all streaming methods in both panoptic quality and speed. PolarStream also stays competitive with the top-performing lidar perception methods on the nuScenes leaderboard while being at least twice as fast as the rest. We do several ablation studies and extensive analysis to show the effectiveness of PolarStream.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

An efficient streaming based lidar perception models using a polar grid.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-scale context padding: an efficient approach to enhance the context of streaming lidar perception models

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several improvements to the core problem of applying convolutions on a polar grid: Feature Undistortion, Range Stratified Convolution&Normalization all add minimal latency to our model.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Non-streaming lidar perception", "weight": 1.0} -->

Most lidar perception architectures take inspiration from the image perception literature. Some single-stage methods typically convert the point cloud into a bird's-eye view image or a range view image and perform detection in those views. The most common paradigm is to convert the lidar point cloud into a BEV image as it offers several advantages like a lack of scale ambiguity, a near lack of occlusion, the ease of fusing HD maps and performing simultaneous detection and trajectory predictions. To convert the point clouds into a BEV representation, most existing models choose to group the points into voxels. The most commonly used voxels are cuboid-shaped based on Cartesian coordinates. VoxNet, MV3D, Pixor, Complex-YOLO represent the cuboid-shaped voxels as occupancy grids. To avoid quantization effects of occupancy grids and extract richer voxel features, VoxelNet samples a fixed number of points within each voxel and applies a simple PointNet to them. For efficiency, PointPillars discretizes the 3D space into pillars so there is only one voxel along the height dimension.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Non-streaming lidar perception", "weight": 1.0} -->

Some recent methods that operate on BEV start to explore polar voxels for point clouds. For 3D object detection, Alsfasser et al voxelizes points under the Cylindrical Coordinate System, MVF adopts both cuboid-shaped voxels and spherical voxels, and CVCNet combines cylindrical and spherical coordinate system into one Hybrid-Cylindrical-Spherical (HCS) coordinate system to detect object from both bird's eye view and range view. On the other hand, the success of PolarNet and Cylinder3D shows the advantage of Cylindrical grids over Cartesian voxels in LiDAR semantic segmentation. Panoptic-PolarNet further extends PolarNet to the task of panoptic segmentation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Streaming lidar perception", "weight": 1.0} -->

Streaming lidar perception is relatively new in literature and offers a compelling argument in reducing the end-to-end latency. Han et al proposed a couple of enhancements to convert a 3D object detector to operate on streaming data: a) using an LSTM to accumulate features from preceding sectors and b) applying stateful NMS to suppress objects across multiple sectors. STROBE accumulates features not only from the preceding sectors of the same scan but also from the previous scan by maintaining multi-scale memory feature maps. Features extracted from the current sector is concatenated and fused with the corresponding cropped region in the memory feature maps.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PolarStream", "weight": 1.0} -->

In this section, we introduce PolarStream, a streaming model based on polar pillars. We introduce how we prepare lidar streaming data in Sec.3.1, polar pillars as a representation for point clouds sectors in Sec.3.2, the simultaneous detection and segmentation model including techniques to improve detection on a polar grid in Sec.3.3, and multi-scale context padding to enlarge context in Sec.3.4.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Streaming LiDAR Inputs", "weight": 1.0} -->

Since there is no streaming lidar dataset available, we simulate a streaming system from the NuScenes dataset by slicing the point clouds into n sectors according to their azimuth. As shown in Fig.1, each sector is like a slice of a full pizza. We try $n = {1,2,4,8,16,32}$ sectors in our experiments, where $n = 1$ means full sweep. The dataset contains $1,000$ scenes, comprising $700$ scenes for training, $150$ scenes for validation and $150$ scenes for test. Each scene is of $20s$ duration, captured by 32-beam lidar. $40,000$ frames are annotated in total, including 10 object categories such as cars, motorcycles and pedestrians and six stuff classes such as vegetation and drivable region. We consider 10 object classes for detection, 16 classes in total for semantic and panoptic segmentation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Polar Pillars", "weight": 1.0} -->

The point clouds sector consists of $N$ points, each represented by a vector of point feature $f_{p} = {(r_{p},\theta_{p},z_{p},x_{p},y_{p},i_{p},t_{p})}$, where $(x_{p},y_{p},z_{p})$ is its Cartesian coordinates. $(r_{p},\theta_{p})$ is the polar coordinates. $i_{p}$ is the reflection intensity and $t_{p}$ is the timestamp when the lidar point is captured. Points are accumulated from 10 successive frames in total to obtain denser point clouds. The points from previous frames are motion-compensated and transformed to current frame. We group the points according to the cylindrical pillar resolution $({\deltar},{\delta\theta},{\deltaz})$ where ${\deltaz} = {z_{max} - z_{min}}$ so there is only one pillar along the height dimension.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Polar Pillars", "weight": 1.0} -->

Following MVF, we adopt dynamic voxelization to sample all points within each pillar, instead of randomly sampling a fixed number of points per pillar.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Simultaneous Detection and Segmentation", "weight": 1.0} -->

We design PolarStream: a simultaneous object detection and segmentation network by extending PointPillars, one of the most widely used 3D object detectors balancing accuracy and speed. As shown in Fig.2, PolarStream consists of a Pillar Feature Encoder, followed by a 2D CNN backbone and a U-Net like structure. On top are the detection and segmentation heads.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Detection Heads", "weight": 1.0} -->

We adopt CenterPoint heads with modifications to make it compatible with polar pillars. To assign targets to the 10-class heatmap to indicate the objects, the gaussian radius of the object center is computed using the span of range and azimuth of the object bounding box, instead of using length and width of the box. Following CenterPoint, we also regress the center offset as $d_{x},d_{y}$, the bounding box size $l,w,h$ as ${\log l},{\log w},{\log h}$, and predict the bounding box height $z$. We regress the relative bounding box orientation $\phi$ as ${\cos\phi},{\sin\phi}$ and relative velocity as $v_{x},v_{y}$ similar to. Unlike most methods, which use multi-group detection heads that partition object classes to several groups according to their size, we use single-group detection heads to balance accuracy and speed. A comparison against multi-group detection heads is shown in Supplementary.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Detection Heads", "weight": 1.0} -->

For streaming data with $n > 1$, we apply stateful-NMS proposed in Han et al..

<!-- chunk {"id": "body-0024", "role": "body", "section": "Segmentation Head", "weight": 1.0} -->

To extend PointPillars for segmentation, we add a semantic segmentation head in parallel with the detection heads. The segmentation head is made of a single 1x1 convolution layer. The input for the segmentation head is concatenation of the outputs from pillar feature encoder and bilinearly upsampled features from the 2D backbone.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Panoptic Fusion", "weight": 1.0} -->

Similar to Panoptic-PolarNet, for each point belonging to things, we predict the instance id as the box id whose category is the same and center is the nearest. For streaming data with $n > 1$, the panoptic segmentation task is not well defined. For example, the points in the $i_{th}$ sector may belong to the box in the ${({i + 1})}_{th}$ sector if the majority of the box is in the ${({i + 1})}_{th}$ sector. However, when we are doing panoptic fusion for $i_{th}$ sector, we do not have information from the ${({i + 1})}_{th}$ sector. Therefore we choose global panoptic fusion for streaming point clouds, i.e., we assign instance ids according to the boxes from all sectors of the same sweep.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multi-Task Learning", "weight": 1.0} -->

We adopt Focal Loss for classification and L1 loss for bounding box regression, orientation and velocity estimation. For segmentation, we use the weighted cross-entropy loss and lovasz-softmax loss. The total loss is the weighted sum of losses for each component.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Feature Undistortion", "weight": 1.0} -->

As mentioned in Sec.1, objects have distorted appearances with polar pillars, we propose Feature Undistortion to undistort the features. As shown on the top right of Fig.2, the idea of undistortion is to interpolate features at cartesian pillar locations from the original polar pillar locations so that the translation-invariant property of convolution applies. We find the connection of bilinear sampling to convolution and mimic bilinear sampling using convolution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Feature Undistortion", "weight": 1.0} -->

We find Equation 1 has the similar form to convolution, except that for convolution $w_{k}$ is fixed because same kernel is slided through every location of the feature map.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Feature Undistortion", "weight": 1.0} -->

$g$ and $q$ is trained together with our main network, and during inference $w_{k}^{\prime}$ and $b_{k}^{\prime}$ are fixed for each location $p_{k}$ so it does not need extra runtime for $g$ and $q$. We apply feature undistortion in center heatmap prediction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Range Stratified Convolution&Normalization", "weight": 1.0} -->

Another challenge with polar pillars is that the center offset is dependent on range and azimuth so it has different statistics at different regions: suppose the heatmap center is at $(r_{c},\theta_{c})$, and the target is at $(r_{t},\theta_{t})$. The center offset is

<!-- chunk {"id": "body-0031", "role": "body", "section": "Range Stratified Convolution&Normalization", "weight": 1.0} -->

where $\theta_{s}$ is a small angle and $\delta\theta$ is the polar pillar angle size. Then

<!-- chunk {"id": "body-0032", "role": "body", "section": "Range Stratified Convolution&Normalization", "weight": 1.0} -->

Similarly, we can derive that $d_{y}$ is also dependent on range and azimuth and observe that for Cartesian pillars center offset ranges from -1 to 1 and mean is 0.49 and std is 0.28, while polar pillars center offset ranges from -2 to 2, mean is 0 and std is 0.64. The polar std is much larger than that for Cartesian pillars. Hence it's more difficult to regress center offset based on polar pillars. Based on these observations, we propose Range Stratified Convolution& Normalization instead of regular convolution and batch normalization. As shown on bottom right of Fig.2, Range Stratified Convolution applies individual kernels at different ranges and Range Stratified Normalization only normalizes over individual regions within certain range instead of entire spatial dimension. We apply Range Stratified Convolution&Normalization to center offset regression. We also apply Range Stratified Normalization to the shared convolution for detection heads.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Trailing-Edge Context Padding", "weight": 1.0} -->

As shown in Fig.3, the sector is unfolded to a rectangle feature map on $r$-$\theta$ plane as input for convolution. The lidar sectors arrive one after another by increasing the angle the sensor scans so the unfolded feature map of a sector is spatially connected to its preceding sector along $\theta$ dimension. This unique property of using polar pillars inspires us to, instead of zero-padding along $\theta$ dimension, pad the features from preceding sector where it is spatially connected to current sector. The receptive field of a neuron increases as the neural network goes from bottom layer to top and the network encodes multi-scale representation of the input at different stages. This motivates us to pad context from preceding sector before every convolution of the 2D CNN backbone, as illustrated in trailing-edge padding of Fig.3. Although we only pad a few columns to the feature map, the neural network is replenished with sufficient context from multiple ranges and multiple scales at different stages of the network.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Trailing-Edge Context Padding", "weight": 1.0} -->

We keep zero-padding for $r$ dimension and the other end of the $\theta$ dimension, as the other end of $\theta$ dimension points to the future sector.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Bidirectional Context Padding", "weight": 1.0} -->

With trailing-edge padding the current sector is padded with context from preceding sector. To provide further context we pad the leading-edge with warped features from the following sector of the *previous* sweep. To do this we aggregate the full-sweep multi-scale feature maps from the previous sweep and warp the feature maps to the coordinate system of current sweep using ego-motion compensation. We then pad the leading edge of the current sector with the corresponding warped features spatially connected to the current sector.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Network Details", "weight": 1.0} -->

For polar pillars with $n$ sectors per sweep, $r,\theta,z$ range is $\lbrack 0.3,50.3\rbrack$m, $\lbrack{- 3.1488},{{- 3.1488} + {6.2976/n}}\rbrack$ rad and $\lbrack{- 5},3\rbrack$m, the pillar size is $(0.098,0.0123,8)$. For Cartesian pillars, the pillar size is $(0.2,0.2,8)$. When $n = 1$, $x,y,z$ range is $\lbrack{- 51.2},51.2\rbrack$m, $\lbrack{- 51.2},51.2\rbrack$ m and $\lbrack{- 5},3\rbrack$m, leaving same input size of $512 \times 512 \times 1$ for both Cartesian pillars and polar pillars when $n = 1$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Network Details", "weight": 1.0} -->

We find the minimal rectangular region to enclose the sectors when $n > 1$ for Cartesian Pillars. We set segmentation loss weight to 2 and classification loss to 1 for both polar pillars and Cartesian pillars. For Cartesian pillars the bounding box regression weight is 0.25. For polar pillars, since regression is harder, we set the loss weight to 0.5. We make sure they are the best configuration for each setting. For $g$ and $q$ in Feature Undistortion, they share the same architecture: a 3x3 conv followed by 1x1 conv with tanh as activation. We show the network architecture in Supplementary. All runtimes are measured on a single V100 GPU using Pytorch.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Augmentation", "weight": 1.0} -->

We adopt class-balanced sampling as proposed in CBGS. Before slicing the point clouds into sectors, we conduct random flipping along $x,y$ axes, scaling with a scale factor sampled from \[0.95, 1.05\], rotation around $z$ axis between \[-0.3925, 0.3925\] rad and translation in range $\lbrack 0.2,0.2,0.2\rbrack$ m in $x,y,z$ axis. Unlike most methods, we do not use database sampling for fast training.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We gather the predictions from individual sectors and evaluate PolarStream similar to full-sweep methods. We evaluate 3D detection and lidar semantic segmentation on the NuScenes benchmark. The detection mean average precision (mAP) is based on the distance threshold (i.e. ${0.5m},{1.0m},{2.0m}$ and $4.0m$). Additionally, we use nuScenes detection score (NDS), a weighted sum of mAP and precision on box location, scale, orientation, velocity and attributes. For semantic segmentation, we follow the standard mean intersection-over-union (mIoU) metric. Since nuScenes does not provide instance labels for panoptic segmentation, we follow Panoptic-PolarNet to generate labels and evaluate panoptic segmentation on validation split using the Panoptic Quality (PQ) metric.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Baselines", "weight": 1.0} -->

Han et al. and STROBE did not release their code and in addition performed evaluation on two different datasets. To enable benchmarking we re-implemented their methods using the same backbone and input resolution as we use and evaluated on the nuScenes dataset. Specifically we re-implemented stateful-NMS and stateful-RNN of Han el al. and multi-scale memory module in STROBE. We did not implement the HD map branch in STROBE in order to ensure a fair comparison. We also apply stateful-NMS and global panoptic fusion to all the methods in comparison as they are just post-processing techniques. We extend both methods to the task of simultaneous object detection, semantic segmentation and panoptic segmentation. We also provide baselines that simply apply Cartesian pillars or polar pillars to individual point clouds sectors. We compare panoptic quality, segmentation mIoU, detection mAP, NDS with the baselines using $n = {1,2,4,8,16,32}$ sectors (Tab.1). We also show the comparison of our method to Han et al. and STROBE wrt. PQ vs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results", "weight": 1.0} -->

Tab. 1 shows that PolarStream outperforms all previous streaming methods, including the Cartesian pillars baseline, in both PQ and Segmentation mIoU. When there are more than four sectors in a scene, previous methods as well as the Cartsian/polar pillar baselines show a trend of decreasing PQ and mIoU as the number of sectors increases. However, our PolarStream with bidirectional context padding does not show such a trend: the performance remains almost the same or even better than the full-sweep method. When $n = 1$, PolarStream got $+ 0.9$ and $+ 1.3$ improvement in PQ and segmentation mIoU compared to the Cartesian pillars baseline. When sectors become smaller and spatial context becomes limited, the improvement is more significant. When $n = 32$, our PolarStream with Bidirectional Context Padding outperforms all previous streaming methods by a large margin, with $+ 6.7$ and $+ 6.6$ improvements in PQ and segmentation mIoU. This shows that our bidiretional context padding makes better use of spatial context compared to previous methods.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results", "weight": 1.0} -->

Our detection NDS is always the highest or at least on par with the highest among all streaming models. Interestingly, Cartesian pillars/Han et al.'s method show higher mAP than ours for 1, 4 and 8 sectors, when the sectors have plenty of spatial view and our context padding does not have many benefits. Our PolarStream outperform all previous streaming methods in detection mAP for 16 and 32 sectors, when spatial view is limited and Bidirectional Context Padding shows more advantages. In addition, the orientation and velocity error of Han et al.'s is on average 14.6% and 12.9% higher than ours, which will cause problems for the downstream tracking and prediction tasks. As shown in Fig.1, our methods offers better operating points considering both accuracy and end-to-end latency. Detailed metrics including velocity error and per-class metrics are shown in Supplementary.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Full Sweep vs. Streaming", "weight": 1.0} -->

Contrary to the findings of Han et al, we saw improved detection performance using 2, 4, 8 and 16 sectors as compared to models trained on full-sweeps. We hypothesize this improvement to less variation in point coordinates within a sector since all sectors are first transformed to a canonical coordinate frame before processing. This suggests that simulating streaming lidars can also serve as an augmentation technique for full-sweep detection.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Diagnosis of Previous Streaming Methods", "weight": 1.0} -->

We first analyze STROBE's low performance in Tab. 1. While all other methods aggregate points from past 10 sweeps after ego-motion compensation (Point Warp), STROBE processes the points one sweep at a time, and aggregates information from the past sweeps by first transforming the features based on ego-motion (Feature Warp) and then fusing them with the current frame. As shown in the full-sweep case in Tab.1, all the metrics for STROBE are significantly lower than other methods. We thus find Feature Warp inferior to Point Warp for detection and especially for velocity estimation. The average velocity error (AVE) of STROBE is 0.607 m/s, significantly higher compared to Cartesian Pillars with Point Warp (0.358 m/s). We speculate that this high velocity error is because the feature maps in STROBE don't encode time information on account of processing one sweep at a time as compared to the other methods which encode the time lag for each accumulated point from the past 10 sweeps. For 1, 2, 4 sectors, STROBE enjoys the lowest latency because it processes fewer points compared to other methods, also shown in Fig. 1.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Diagnosis of Previous Streaming Methods", "weight": 1.0} -->

The pillar feature encoder runs faster. But this advantage disappears for more than 8 sectors because there are also only a smaller number of points processed by all other methods.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Diagnosis of Previous Streaming Methods", "weight": 1.0} -->

Compared to baseline Cartesian Pillars, the method of Han et al. only start to work when more than 8 sectors per sweep. For 2 and 4 sectors, it even hurts the accuracy especially in object detection. This can be explained in Fig. 4. For 2 and 4 sectors, the feature map is fully occupied. Adding the pooled features from preceding sectors is like adding noise to current sector, resulting in worse accuracy. Starting from 8 sectors, there is an empty region in current sector so adding the pooled features from preceding sectors is like padding the empty region, and therefore enlarging the context.

<!-- chunk {"id": "body-0047", "role": "body", "section": "How Streaming Models Enlarge Context", "weight": 1.0} -->

We further hypothesize not only our method and Han et al work by padding context from preceding sectors, but also STROBE works by padding. As shown in Fig. 4, for 2 and 4 sectors when the feature map is fully occupied, fusing features from previous sweep is like densifying the features. Starting from 8 sectors, when there is an empty region, fusing features is like padding the empty region. We argue that all existing streaming methods work by padding, but in different format. STROBE and Han et al. are restricted by the shape of the sectors and require empty region as placeholder, and the padded features are added or fused to the placeholder. Our method pads along the edges of feature maps and is not constrained by the shape of the sector.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Further Thoughts about Context", "weight": 1.0} -->

We argue that context has two aspects. First is its feature values, for the texture information it carries. Second is its spatial relation to the object of interest. Since convolution is translation-invariant, convolutional neural networks alone do not encode spatial relation. The spatial relation is maintained in the spatial arrangement of neurons on the feature map. The stateful-RNN in Han et al. must work together with the empty region as placeholder to maintain the spatial arrangement, while stateful-RNN alone does not encode spatial relation. On the other hand, although our padding along the feature map edges seems simple, it is an effective solution to both add feature values and maintain spatial relation of context.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison with other Full-Sweep Models", "weight": 1.0} -->

As the full-sweep 3D object detection and LiDAR semantic segmentation have longer histories compared to streaming models, there are more full-sweep methods in the literature. We also compare with these methods. We present the results of our full-sweep PolarStream model with $n = 1$ (PLS1) and best performing PolarStream model with $n = 4$ (PLS4), with the same backbone as in PointPillars. As shown in Fig. 5, our method maintains a good balance of runtime and accuracy compared to other methods on both the nuScenes detection and semantic segmentation benchmark. We achieve even faster runtime with PLS4 while preserving almost same accuracy as PLS1. The panoptic segmentation results on the nuScenes val split show that our methods outperform all existing methods in PQ with at least $55\%$ less runtime.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparison with other Full-Sweep Models", "weight": 1.0} -->

We also adopt a heavier 3D ResNet backbone as in CBGS and compare with the state of the art methods for 3D object detection and semantic segmentation in Tab. 2. Our PLS1-heavy is able to match/beat the state-of-the-art models for detection (CenterPoint) and segmentation (Cylinder3D) on the nuScenes validation set. In this work, we focus on onboard applications so we only choose the same backbone as in PointPillars for streaming.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Comparison with other Full-Sweep Models", "weight": 1.0} -->

#parameters(MB)
#parameters(MB)

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Effect of Multi-Scale Context Padding", "weight": 1.0} -->

As shown in Tab.3, the advantage of Multi-Scale Context Padding starts to show up for 8, 16 and 32 sectors, especially in segmentation. For 32 sectors, when the spatial view is the most restricted, we observe the largest gain in detection mAP and segmentation mIoU. Multi-Scale Context Padding does not improve or hurt the baseline polar pillars model for 2 and 4 sectors, because the network already sees enough spatial view. As we increase the amount of context, from trailing-edge padding to bidirectional padding, we observe more improvements. Surprisingly, we observe that with 2, 4, 8 and 16 sectors, our PolarStream with bidirectional padding even outperforms our full-sweep baseline of polar pillars in all metrics including PQ, detection mAP, NDS and segmentation IoU. It suggests that streaming models can be both faster and more accurate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "The effect of Feature Undistortion and Range Stratified Convolution& Normalization", "weight": 1.0} -->

We do the ablation studies with $n = 1$, i.e., the full-sweep case. To show how we close the gap of detection accuracy between polar pillars and Cartesian Pillars, we also list the results of Cartesian pillars with the same architecture and input size. We find that polar pillars outperforms Cartesian pillars in semantic segmentation mIoU (73.2 vs 72.1), which is also found in prior arts, because points in the same polar pillar have less disagreement in the semantic label compared to those in a Cartesian pillar. However, polar pillars is less accurate in object detection due to the challenges we discussed. In Tab. 4 we show either Range Stratified Convolution& Normalization or Feature Undistortion helps to improve detection accuracy based on polar pillars (by 0.9 and 0.4 mAP respectively). With both techniques combined, we improve detection mAP from $48.2$ to $50.3$, narrowing the gap compared to Cartesian pillars ($50.6$).

<!-- chunk {"id": "body-0054", "role": "body", "section": "The effect of Feature Undistortion and Range Stratified Convolution& Normalization", "weight": 1.0} -->

We also apply both techniques to Cartesian pillars and they do not improve Cartesian pillars, showing they only address the specific challenges of polar pillars, instead of improving the performance by adding more parameters to the network. Our techniques do not add noticeable runtime (0.5ms). In addition, we find detection mAP can be improved when simultaneouly trained with semantic segmentation. The improvement is more significant for Cartesian pillars, but Cartesian pillars suffer from slight drop in segmentation mIoU.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work we propose a streaming model for simultaneous 3D object Detection, Lidar Segmentation and Panoptic Segmentation. Polar pillars is introduced as a more compact representation for lidar sectors compared to previous methods. Multi-scale context padding including trailing-edge padding and bidirectional padding is proposed to enhance spatial context of the streaming model with minimal latency. Additionally we make several improvements, Feature Undistortion and Range Stratified Convolution& Normalization, to address the problem of applying convolutions on a polar grid. Our model showed significant improvements over previous streaming methods with lower latency.
