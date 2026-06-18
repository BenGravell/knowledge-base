<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PointPillars: Fast Encoders for Object Detection from Point Clouds

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Object detection in point clouds is an important aspect of many robotics applications such as autonomous driving. In this paper we consider the problem of encoding a point cloud into a format appropriate for a downstream detection pipeline. Recent literature suggests two types of encoders; fixed encoders tend to be fast but sacrifice accuracy, while encoders that are learned from data are more accurate, but slower. In this work we propose PointPillars, a novel encoder which utilizes PointNets to learn a representation of point clouds organized in vertical columns (pillars). While the encoded features can be used with any standard 2D convolutional detection architecture, we further propose a lean downstream network. Extensive experimentation shows that PointPillars outperforms previous encoders with respect to both speed and accuracy by a large margin. Despite only using lidar, our full detection pipeline significantly outperforms the state of the art, even among fusion methods, with respect to both the 3D and bird's eye view KITTI benchmarks. This detection performance is achieved while running at 62 Hz: a 2 - 4 fold runtime improvement. A faster version of our method matches the state of the art at 105 Hz.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These benchmarks suggest that PointPillars is an appropriate encoding for object detection in point clouds.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deploying autonomous vehicles (AVs) in urban environments poses a difficult technological challenge. Among other tasks, AVs need to detect and track moving objects such as vehicles, pedestrians, and cyclists in realtime. To achieve this, autonomous vehicles rely on several sensors out of which the lidar is arguably the most important. A lidar uses a laser scanner to measure the distance to the environment, thus generating a sparse point cloud representation. Traditionally, a lidar robotics pipeline interprets such point clouds as object detections through a bottom-up pipeline involving background subtraction, followed by spatiotemporal clustering and classification.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following the tremendous advances in deep learning methods for computer vision, a large body of literature has investigated to what extent this technology could be applied towards object detection from lidar point clouds. While there are many similarities between the modalities, there are two key differences: 1) the point cloud is a sparse representation, while an image is dense and 2) the point cloud is 3D, while the image is 2D. As a result object detection from point clouds does not trivially lend itself to standard image convolutional pipelines.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some early works focus on either using 3D convolutions or a projection of the point cloud into the image. Recent methods tend to view the lidar point cloud from a bird's eye view. This overhead perspective offers several advantages such as lack of scale ambiguity and the near lack of occlusion.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the bird's eye view tends to be extremely sparse which makes direct application of convolutional neural networks impractical and inefficient. A common workaround to this problem is to partition the ground plane into a regular grid, for example 10 x 10 cm, and then perform a hand crafted feature encoding method on the points in each grid cell. However, such methods may be sub-optimal since the hard-coded feature extraction method may not generalize to new configurations without significant engineering efforts. To address these issues, and building on the PointNet design developed by Qi et al., VoxelNet was one of the first methods to truly do end-to-end learning in this domain. VoxelNet divides the space into voxels, applies a PointNet to each voxel, followed by a 3D convolutional middle layer to consolidate the vertical axis, after which a 2D convolutional detection architecture is applied. While the VoxelNet performance is strong, the inference time, at $4.4Hz$, is too slow to deploy in real time. Recently SECOND improved the inference speed of VoxelNet but the 3D convolutions remain a bottleneck.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we propose PointPillars: a method for object detection in 3D that enables end-to-end learning with only 2D convolutional layers. PointPillars uses a novel encoder that learn features on pillars (vertical columns) of the point cloud to predict 3D oriented boxes for objects. There are several advantages of this approach. First, by learning features instead of relying on fixed encoders, PointPillars can leverage the full information represented by the point cloud. Further, by operating on pillars instead of voxels there is no need to tune the binning of the vertical direction by hand. Finally, pillars are highly efficient because all key operations can be formulated as 2D convolutions which are extremely efficient to compute on a GPU. An additional benefit of learning features is that PointPillars requires no hand-tuning to use different point cloud configurations. For example, it can easily incorporate multiple lidar scans, or even radar point clouds.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluated our PointPillars network on the public KITTI detection challenges which require detection of cars, pedestrians, and cyclists in either the bird's eye view (BEV) or 3D. While our PointPillars network is trained using only lidar point clouds, it dominates the current state of the art including methods that use lidar *and* images, thus establishing new standards for performance on both BEV and 3D detection (Table 1 and Table 2). At the same time PointPillars runs at $62Hz$, which is orders of magnitude faster than previous art. PointPillars further enables a trade off between speed and accuracy; in one setting we match state of the art performance at over $100Hz$ (Figure 5). We have also released code that can reproduce our results.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Object detection using CNNs", "weight": 1.0} -->

Starting with the seminal work of Girshick et al. it was established that convolutional neural network (CNN) architectures are state of the art for detection in images. The series of papers that followed advocate a two-stage approach to this problem, where in the first stage a region proposal network (RPN) suggests candidate proposals. Cropped and resized versions of these proposals are then classified by a second stage network. Two-stage methods dominated the important vision benchmark datasets such as COCO over single-stage architectures originally proposed by Liu et al.. In a single-stage architecture a dense set of anchor boxes is regressed and classified in a single stage into a set of predictions providing a fast and simple architecture. Recently Lin et al. convincingly argued that with their proposed focal loss function a single stage method is superior to two-stage methods, both in terms of accuracy *and* runtime. In this work, we use a single stage method.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Object detection in lidar point clouds", "weight": 1.0} -->

Object detection in point clouds is an intrinsically three dimensional problem. As such, it is natural to deploy a 3D convolutional network for detection, which is the paradigm of several early works. While providing a straight-forward architecture, these methods are slow; e.g. Engelcke et al. require $0.5s$ for inference on a single point cloud. Most recent methods improve the runtime by projecting the 3D point cloud either onto the ground plane or the image plane. In the most common paradigm the point cloud is organized in voxels and the set of voxels in each vertical column is encoded into a fixed-length, hand-crafted, feature encoding to form a pseudo-image which can be processed by a standard image detection architecture. Some notable works here include MV3D, AVOD, PIXOR and Complex YOLO which all use variations on the same fixed encoding paradigm as the first step of their architectures. The first two methods additionally fuse the lidar features with image features to create a multi-modal detector. The fusion step used in MV3D and AVOD forces them to use two-stage detection pipelines, while PIXOR and Complex YOLO use single stage pipelines.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Object detection in lidar point clouds", "weight": 1.0} -->

In their seminal work Qi et al. proposed a simple architecture, PointNet, for learning from unordered point sets, which offered a path to full end-to-end learning. VoxelNet is one of the first methods to deploy PointNets for object detection in lidar point clouds. In their method, PointNets are applied to voxels which are then processed by a set of 3D convolutional layers followed by a 2D backbone and a detection head. This enables end-to-end learning, but like the earlier work that relied on 3D convolutions, VoxelNet is slow, requiring 225ms inference time ($4.4Hz$) for a single point cloud. Another recent method, Frustum PointNet, uses PointNets to segment and classify the point cloud in a frustum generated from projecting a detection on an image into 3D. Frustum PointNet's achieved high benchmark performance compared to other fusion methods, but its multi-stage design makes end-to-end learning impractical. Very recently SECOND offered a series of improvements to VoxelNet resulting in stronger performance and a much improved speed of $20Hz$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Object detection in lidar point clouds", "weight": 1.0} -->

However, they were unable to remove the expensive 3D convolutional layers.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

We propose a novel point cloud encoder and network, PointPillars, that operates on the point cloud to enable end-to-end training of a 3D object detection network.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

We show how all computations on pillars can be posed as dense 2D convolutions which enables inference at $62Hz$; a factor of 2-4 times faster than other methods.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

We conduct experiments on the KITTI dataset and demonstrate state of the art results on cars, pedestrians, and cyclists on both BEV and 3D benchmarks.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions", "weight": 1.0} -->

We conduct several ablation studies to examine the key factors that enable a strong detection performance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "PointPillars Network", "weight": 1.0} -->

PointPillars accepts point clouds as input and estimates oriented 3D boxes for cars, pedestrians and cyclists. It consists of three main stages (Figure 2): A feature encoder network that converts a point cloud to a sparse pseudo-image; a 2D convolutional backbone to process the pseudo-image into high-level representation; and a detection head that detects and regresses 3D boxes.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Pointcloud to Pseudo-Image", "weight": 1.0} -->

To apply a 2D convolutional architecture, we first convert the point cloud to a pseudo-image.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Pointcloud to Pseudo-Image", "weight": 1.0} -->

We denote by $l$ a point in a point cloud with coordinates $x$, $y$, $z$ and reflectance $r$. As a first step the point cloud is discretized into an evenly spaced grid in the x-y plane, creating a set of pillars $\mathcal{P}$ with ${|\mathcal{P}|} = B$. Note that there is no need for a hyper parameter to control the binning in the z dimension. The points in each pillar are then augmented with $x_{c}$, $y_{c}$, $z_{c}$, $x_{p}$ and $y_{p}$ where the $c$ subscript denotes distance to the arithmetic mean of all points in the pillar and the $p$ subscript denotes the offset from the pillar $x,y$ center. The augmented lidar point $l$ is now $D = 9$ dimensional.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Pointcloud to Pseudo-Image", "weight": 1.0} -->

The set of pillars will be mostly empty due to sparsity of the point cloud, and the non-empty pillars will in general have few points in them. For example, at $0.16^{2}m^{2}$ bins the point cloud from an HDL-64E Velodyne lidar has 6k-9k non-empty pillars in the range typically used in KITTI for $\sim {97\%}$ sparsity. This sparsity is exploited by imposing a limit both on the number of non-empty pillars per sample ($P$) and on the number of points per pillar ($N$) to create a dense tensor of size $(D,P,N)$. If a sample or pillar holds too much data to fit in this tensor the data is randomly sampled. Conversely, if a sample or pillar has too little data to populate the tensor, zero padding is applied.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Pointcloud to Pseudo-Image", "weight": 1.0} -->

Next, we use a simplified version of PointNet where, for each point, a linear layer is applied followed by BatchNorm and ReLU to generate a $(C,P,N)$ sized tensor. This is followed by a max operation over the channels to create an output tensor of size $(C,P)$. Note that the linear layer can be formulated as a 1x1 convolution across the tensor resulting in very efficient computation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Pointcloud to Pseudo-Image", "weight": 1.0} -->

Once encoded, the features are scattered back to the original pillar locations to create a pseudo-image of size $(C,H,W)$ where $H$ and $W$ indicate the height and width of the canvas.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Backbone", "weight": 1.0} -->

We use a similar backbone as and the structure is shown in Figure 2. The backbone has two sub-networks: one top-down network that produces features at increasingly small spatial resolution and a second network that performs upsampling and concatenation of the top-down features. The top-down backbone can be characterized by a series of blocks Block($S$, $L$, $F$). Each block operates at stride $S$ (measured relative to the original input pseudo-image). A block has $L$ 3x3 2D conv-layers with $F$ output channels, each followed by BatchNorm and a ReLU. The first convolution inside the layer has stride $\frac{S}{S_{in}}$ to ensure the block operates on stride $S$ after receiving an input blob of stride $S_{in}$. All subsequent convolutions in a block have stride 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Backbone", "weight": 1.0} -->

The final features from each top-down block are combined through upsampling and concatenation as follows. First, the features are upsampled, Up($S_{in}$, $S_{out}$, $F$) from an initial stride $S_{in}$ to a final stride $S_{out}$ (both again measured wrt. original pseudo-image) using a transposed 2D convolution with $F$ final features. Next, BatchNorm and ReLU is applied to the upsampled features. The final output features are a concatenation of all features that originated from different strides.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Detection Head", "weight": 1.0} -->

In this paper, we use the Single Shot Detector (SSD) setup to perform 3D object detection. Similar to SSD, we match the priorboxes to the ground truth using 2D Intersection over Union (IoU). Bounding box height and elevation were not used for matching; instead given a 2D match, the height and elevation become additional regression targets.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In this section we describe our network parameters and the loss function that we optimize.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Network", "weight": 1.0} -->

Instead of pre-training our networks, all weights were initialized randomly using a uniform distribution as.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Network", "weight": 1.0} -->

The encoder network has $C = 64$ output features. The car and pedestrian/cyclist backbones are the same except for the stride of the first block ($S = 2$ for car, $S = 1$ for pedestrian/cyclist). Both network consists of three blocks, Block1($S$, 4, C), Block2($2S$, 6, 2C), and Block3($4S$, 6, 4C). Each block is upsampled by the following upsampling steps: Up1($S$, $S$, 2C), Up2($2S$, $S$, 2C) and Up3($4S$, $S$, 2C). Then the features of Up1, Up2 and Up3 are concatenated together to create 6C features for the detection head.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Loss", "weight": 1.0} -->

We use the same loss functions introduced in SECOND. Ground truth boxes and anchors are defined by $(x,y,z,w,l,h,\theta)$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Loss", "weight": 1.0} -->

Since the angle localization loss cannot distinguish flipped boxes, we use a softmax classification loss on the discretized directions, $\mathcal{L}_{dir}$, which enables the network to learn the heading.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Loss", "weight": 1.0} -->

where $p^{a}$ is the class probability of an anchor. We use the original paper settings of $\alpha = 0.25$ and $\gamma = 2$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Loss", "weight": 1.0} -->

To optimize the loss function we use the Adam optimizer with an initial learning rate of $2 \ast 10^{- 4}$ and decay the learning rate by a factor of $0.8$ every $15$ epochs and train for $160$ epochs. We use a batch size of 2 for validation set and 4 for our test submission.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

In this section we present our experimental setup, including dataset, experimental settings and data augmentation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Dataset", "weight": 1.0} -->

All experiments use the KITTI object detection benchmark dataset, which consists of samples that have both lidar point clouds and images. We only train on lidar point clouds, but compare with fusion methods that use both lidar and images. The samples are originally divided into 7481 training and 7518 testing samples. For experimental studies we split the official training into 3712 training samples and 3769 validation samples, while for our test submission we created a minival set of 784 samples from the validation set and trained on the remaining 6733 samples. The KITTI benchmark requires detections of cars, pedestrians, and cyclists. Since the ground truth objects were only annotated if they are visible in the image, we follow the standard convention of only using lidar points that project into the image. Following the standard literature practice on KITTI, we train one network for cars and one network for both pedestrians and cyclists.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Settings", "weight": 1.0} -->

Unless explicitly varied in an experimental study, we use an xy resolution: 0.16 m, max number of pillars ($P$): 12000, and max number of points per pillar ($N$): 100.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Settings", "weight": 1.0} -->

We use the same anchors and matching strategy as. Each class anchor is described by a width, length, height, and z center, and is applied at two orientations: 0 and 90 degrees. Anchors are matched to ground truth using the 2D IoU with the following rules. A positive match is either the highest with a ground truth box, or above the positive match threshold, while a negative match is below the negative threshold. All other anchors are ignored in the loss.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Settings", "weight": 1.0} -->

At inference time we apply axis aligned non maximum suppression (NMS) with an overlap threshold of $0.5$ IoU. This provides similar performance compared to rotational NMS, but is much faster.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Car", "weight": 1.0} -->

The x, y, z range is \[(0, 70.4), (-40, 40), (-3, 1)\] meters respectively. The car anchor has width, length, and height of (1.6, 3.9, 1.5) m with a z center of -1 m. Matching uses positive and negative thresholds of 0.6 and 0.45.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Pedestrian & Cyclist", "weight": 1.0} -->

The x, y, z range of \[, (-20, 20), (-2.5, 0.5)\] meters respectively. The pedestrian anchor has width, length, and height of (0.6, 0.8, 1.73) meters with a z center of -0.6 meters, while the cyclist anchor has width, length, and height of (0.6, 1.76, 1.73) meters with a z center of -0.6 meters. Matching uses positive and negative thresholds of 0.5 and 0.35.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data Augmentation", "weight": 1.0} -->

Data augmentation is critical for good performance on the KITTI benchmark.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Data Augmentation", "weight": 1.0} -->

First, following SECOND, we create a lookup table of the ground truth 3D boxes for all classes and the associated point clouds that falls inside these 3D boxes. Then for each sample, we randomly select $15,0,8$ ground truth samples for cars, pedestrians, and cyclists respectively and place them into the current point cloud. We found these settings to perform better than the proposed settings.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Data Augmentation", "weight": 1.0} -->

Next, all ground truth boxes are individually augmented. Each box is rotated (uniformly drawn from $\lbrack{- {\pi/20}},{\pi/20}\rbrack$) and translated (x, y, and z independently drawn from $\mathcal{N}{(0,0.25)}$) to further enrich the training set.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Data Augmentation", "weight": 1.0} -->

Finally, we perform two sets of global augmentations that are jointly applied to the point cloud and all boxes. First, we apply random mirroring flip along the x axis, then a global rotation and scaling. Finally, we apply a global translation with x, y, z drawn from $\mathcal{N}{(0,0.2)}$ to simulate localization noise.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results", "weight": 1.0} -->

In this section we present results of our PointPillars method and compare to the literature.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

All detection results are measured using the official KITTI evaluation detection metrics which are: bird's eye view (BEV), 3D, 2D, and average orientation similarity (AOS). The 2D detection is done in the image plane and average orientation similarity assesses the average orientation (measured in BEV) similarity for 2D detections. The KITTI dataset is stratified into easy, moderate, and hard difficulties, and the official KITTI leaderboard is ranked by performance on moderate.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

As shown in Table 1 and Table 2, PointPillars outperforms all published methods with respect to mean average precision (mAP). Compared to lidar-only methods, PointPillars achieves better results across all classes and difficulty strata except for the easy car stratum. It also outperforms fusion based methods on cars and cyclists.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

While PointPillars predicts 3D oriented boxes, the BEV and 3D metrics do not take orientation into account. Orientation is evaluated using AOS, which requires projecting the 3D box into the image, performing 2D detection matching, and then assessing the orientation of these matches. The performance of PointPillars on AOS significantly exceeds in all strata as compared to the only two 3D detection methods that predict oriented boxes (Table 3). In general, image only methods perform best on 2D detection since the 3D projection of boxes into the image can result in loose boxes depending on the 3D pose. Despite this, PointPillars moderate cyclist AOS of 68.16 outperforms the best image based method.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Quantitative Analysis", "weight": 1.0} -->

For comparison to other methods on val, we note that our network achieved BEV AP of ($87.98$, $63.55$, $69.71$) and 3D AP of ($77.98$, $57.86$, $66.02$) for the moderate strata of cars, pedestrians, and cyclists respectively.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

We provide qualitative results in Figure 3 and 4. While we only train on lidar point clouds, for ease of interpretation we visualize the 3D bounding box predictions from the BEV and image perspective. Figure 3 shows our detection results, with tight oriented 3D bounding boxes. The predictions for cars are particularly accurate and common failure modes include false negatives on difficult samples (partially occluded or faraway objects) or false positives on similar classes (vans or trams). Detecting pedestrians and cyclists is more challenging and leads to some interesting failure modes. Pedestrians and cyclists are commonly misclassified as each other (see Figure 4a for a standard example and Figure 4d for the combination of pedestrian and table classified as a cyclist). Additionally, pedestrians are easily confused with narrow vertical features of the environment such as poles or tree trunks (see Figure 4b). In some cases we correctly detect objects that are missing in the ground truth annotations (see Figure 4c).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Realtime Inference", "weight": 1.0} -->

As indicated by our results (Table 1 and Figure 5), PointPillars represent a significant improvement in terms of inference runtime. In this section we break down our runtime and consider the different design choices that enabled this speedup. We focus on the car network, but the pedestrian and bicycle network runs at a similar speed since the smaller range cancels the effect of the backbone operating at lower strides. All runtimes are measured on a desktop with an Intel i7 CPU and a 1080ti GPU.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Realtime Inference", "weight": 1.0} -->

The main inference steps are as follows. First, the point cloud is loaded and filtered based on range and visibility in the images ($1.4ms$). Then, the points are organized in pillars and decorated ($2.7ms$). Next, the PointPillar tensor is uploaded to the GPU ($2.9ms$), encoded ($1.3ms$), scattered to the pseudo-image ($0.1ms$), and processed by the backbone and detection heads ($7.7ms$). Finally NMS is applied on the CPU ($0.1ms$) for a total runtime of $16.2ms$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Encoding", "weight": 1.0} -->

The key design to enable this runtime is the PointPilar encoding. For example, at $1.3ms$ it is 2 orders of magnitude faster than the VoxelNet encoder ($190ms$). Recently, SECOND proposed a faster sparse version of the VoxelNet encoder for a total network runtime of $50ms$. They did not provide a runtime analysis, but since the rest of their architecture is similar to ours, it suggests that the encoder is still significantly slower; in their open source implementation^11^1 the encoder requires $48ms$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Slimmer Design", "weight": 1.0} -->

We opt for a single PointNet in our encoder, compared to 2 sequential PointNets suggested. This reduced our runtime by $2.5ms$ in our PyTorch runtime. The number of dimensions of the first block were also lowered $64$ to match the encoder output size, which reduced the runtime by $4.5ms$. Finally, we saved another $3.9ms$ by cutting the output dimensions of the upsampled feature layers by half to $128$. Neither of these changes affected detection performance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "TensorRT", "weight": 1.0} -->

While all our experiments were performed in PyTorch, the final GPU kernels for encoding, backbone and detection head were built using NVIDIA TensorRT, which is a library for optimized GPU inference. Switching to TensorRT gave a $45.5\%$ speedup from the PyTorch pipeline which runs at $42.4Hz$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "The Need for Speed", "weight": 1.0} -->

As seen in Figure 5, PointPillars can achieve $105Hz$ with limited loss of accuracy. While it could be argued that such runtime is excessive since a lidar typically operates at $20Hz$, there are two key things to keep in mind. First, due to an artifact of the KITTI ground truth annotations, only lidar points which projected into the front image are utilized, which is only $\sim {10\%}$ of the entire point cloud. However, an operational AV needs to view the full environment and process the complete point cloud, significantly increasing all aspects of the runtime. Second, timing measurements in the literature are typically done on a high-power desktop GPU. However, an operational AV may instead use embedded GPUs or embedded compute which may not have the same throughput.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

In this section we provide ablation studies and discuss our design choices compared to the recent literature.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Spatial Resolution", "weight": 1.0} -->

A trade-off between speed and accuracy can be achieved by varying the size of the spatial binning. Smaller pillars allow finer localization and lead to more features, while larger pillars are faster due to fewer non-empty pillars (speeding up the encoder) and a smaller pseudo-image (speeding up the CNN backbone). To quantify this effect we performed a sweep across grid sizes. From Figure 5 it is clear that the larger bin sizes lead to faster networks; at $0.28^{2}$ we achieve $105Hz$ at similar performance to previous methods. The decrease in performance was mainly due to the pedestrian and cyclist classes, while car performance was stable across the bin sizes.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Per Box Data Augmentation", "weight": 1.0} -->

Both VoxelNet and SECOND recommend extensive per box augmentation. However, in our experiments, minimal box augmentation worked better. In particular, the detection performance for pedestrians degraded significantly with more box augmentation. Our hypothesis is that the introduction of ground truth sampling mitigates the need for extensive per box augmentation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Point Decorations", "weight": 1.0} -->

During the lidar point decoration step, we perform the VoxelNet decorations plus two additional decorations: $x_{p}$ and $y_{p}$ which are the $x$ and $y$ offset from the pillar $x,y$ center. These extra decorations added 0.5 mAP to final detection performance and provided more reproducible experiments.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Encoding", "weight": 1.0} -->

To assess the impact of the proposed PointPillar encoding in isolation, we implemented several encoders in the official codebase of SECOND. For details on each encoding, we refer to the original papers.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Encoding", "weight": 1.0} -->

As shown in Table 4, learning the feature encoding is strictly superior to fixed encoders across all resolution. This is expected as most successful deep learning architectures are trained end-to-end. Further, the differences increase with larger bin sizes where the lack of expressive power of the fixed encoders are accentuated due to a larger point cloud in each pillar. Among the learned encoders VoxelNet is marginally stronger than PointPillars. However, this is not a fair comparison, since the VoxelNet encoder is orders of magnitude slower and has orders of magnitude more parameters. When the comparison is made for a similar *inference time*, it is clear that PointPillars offers a better operating point (Figure 5).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Encoding", "weight": 1.0} -->

There are a few curious aspects of Table 4. First, despite notes in the original papers that their encoder only works on cars, we found that the MV3D and PIXOR encoders can learn pedestrians and cyclists quite well. Second, our implementations beat the respective published results by a large margin ($1 - 10$ mAP). While this is not an apples to apples comparison since we only used the respective *encoders* and not the full network architectures, the performance difference is noteworthy. We see several potential reasons. For VoxelNet and SECOND we suspect the boost in performance comes from improved data augmentation hyperparameters as discussed in Section 7.2. Among the fixed encoders, roughly half the performance increase can be explained by the introduction of ground truth database sampling, which we found to boost the mAP by around $3\%$ mAP.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Encoding", "weight": 1.0} -->

The remaining differences are likely due to a combination of multiple hyperparameters including network design (number of layers, type of layers, whether to use a feature pyramid); anchor box design (or lack thereof ); localization loss with respect to 3D and angle; classification loss; optimizer choices (SGD vs Adam, batch size); and more. However, a more careful study is needed to isolate each cause and effect.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduce PointPillars, a novel deep network and encoder that can be trained end-to-end on lidar point clouds. We demonstrate that on the KITTI challenge, PointPillars dominates all existing methods by offering higher detection performance (mAP on both BEV and 3D) at a faster speed. Our results suggests that PointPillars offers the best architecture so far for 3D object detection from lidar.
