<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PointPainting: Sequential Fusion for 3D Object Detection

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Camera and lidar are important sensor modalities for robotics in general and self-driving cars in particular. The sensors provide complementary information offering an opportunity for tight sensor-fusion. Surprisingly, lidar-only methods outperform fusion methods on the main benchmark datasets, suggesting a gap in the literature. In this work, we propose PointPainting: a sequential fusion method to fill this gap. PointPainting works by projecting lidar points into the output of an image-only semantic segmentation network and appending the class scores to each point. The appended (painted) point cloud can then be fed to any lidar-only method. Experiments show large improvements on three different state-of-the art methods, Point-RCNN, VoxelNet and PointPillars on the KITTI and nuScenes datasets. The painted version of PointRCNN represents a new state of the art on the KITTI leaderboard for the bird's-eye view detection task. In ablation, we study how the effects of Painting depends on the quality and format of the semantic segmentation output, and demonstrate how latency can be minimized through pipelining.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Driven partially by the interest in self-driving vehicles, significant research effort has been devoted to 3D object detection. In this work we consider the problem of fusing a lidar point cloud with an RGB image. The point cloud provides a very accurate range view, but with low resolution and texture information. The image, on the other hand, has an inherent depth ambiguity but offers fine-grained texture and color information. This offers the compelling research opportunity of how to design a detector which utilizes the best of two worlds.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Early work on KITTI such as MV3D and AVOD proposed multi-view fusion pipelines to exploit these synergies. However recent detectors such as PointPillars, VoxelNet and STD use only lidar and still significantly outperform these methods. Indeed, despite recent fusion research, the top methods on the popular KITTI leaderboard are lidar only. Does this mean lidar makes vision redundant for 3D object detection?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The answer, surely, must be no. Consider the example in Fig. 3, where the pedestrian and signpost are clearly visible in the image, yet look more or less identical in the lidar modality. Surely vision based semantic information should be useful to improve detection of such objects. Also, by first principle, adding more information should at the minimum yield the *same* result, not *worse*. So why has it been so difficult? One reason is due to viewpoint misalignment.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While both sensors are natively captured in the range-view, most state of the art methods such as PointPillars or STD use convolutions in the bird's-eye view. This view has several advantages including lack of scale ambiguity and minimal occlusions. It also does not suffer from the depth-blurring effect which occurs with applying 2D convolutions to the range view. As a result, bird's-eye view methods outperform top range-view methods, such as LaserNet, on the KITTI leaderboard. However, while a lidar point cloud can trivially be converted to bird's-eye view, it is much more difficult to do so with an image.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, a core challenge of sensor fusion network design lies in consolidating the lidar bird's-eye view with the camera view. Previous methods can be grouped into four categories: object-centric fusion, continuous feature fusion, explicit transform and detection seeding.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Object-centric fusion, pioneered by MV3D and AVOD, is the most obvious choice for a two-stage architecture. Here, the modalities have different backbones, one in each view, and fusion happens at the object proposal level by applying roi-pooling in each modality from a shared set of 3D proposals. This allows for end-to-end optimization but tends to be slow and cumbersome.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A second family of methods applies "continuous feature fusion" to allow feature information to be shared across all strides of the image and lidar backbones. These methods can be used with single-state detection designs but require a mapping to be calculated, *a priori*, for each sample, from the point-cloud to the image. One subtle but important draw-back of this family of methods is "feature-blurring". This occurs since each feature vector from the bird's-eye view corresponds to multiple pixels in the image-view, and vice versa. ContFuse proposes a sophisticated method based on kNN, bilinear interpolation and a learned MLP to remedy this, but the core problem persists.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A third family of methods attempts to explicitly transform the image to a bird's-eye view representation and do the fusion there. Some of the most promising *image-only* methods use this idea of first creating an artificial point cloud from the image and then proceeding in the bird's-eye view. Subsequent work attempts fusion based on this idea, but the performance falls short of state of the art, and requires several expensive steps of processing to build the pseudo-point cloud.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A fourth family of methods uses detection seeding. There, semantics are extracted from an image *a priori* and used to seed detection in the point cloud. Frustrum PointNet and ConvNet use the 2D detections to limit the search space inside the frustum while IPOD uses semantic segmentation outputs to seed the 3D proposal. This improves precision, but imposes an upper bound on recall.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent work of Liang et. al tried combining several of these concepts. Results are not disclosed for all classes, but the method is outperformed on the car class by the top lidar-only method STD (Table 2).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we propose PointPainting: a simple yet effective sequential fusion method. Each lidar point is projected into the output of an image semantic segmentation network and the channel-wise activations are concatenated to the intensity measurement of each lidar point. The concatenated (painted) lidar points can then be used in any lidar detection method, whether bird's-eye view or front-view. PointPainting addresses the shortcomings of the previous fusion concepts: it does not add any restrictions on the 3D detection architecture; it does not suffer from feature or depth blurring; it does not require a pseudo-point cloud to be computed, and it does not limit the maximum recall.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that for lidar detection methods that operate directly on the raw point cloud, PointPainting requires minimal network adaptations such as changing the number of channels dedicated to reading the point cloud. For methods using hand-coded features, some extra work is required to modify the feature encoder.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

PointPainting is sequential by design which means that it is not always possible to optimize, end-to-end, for the final task of 3D detection. In theory, this implies sub-optimality in terms of performance. Empirically, however, PointPainting is more effective than all other proposed fusion methods. Further, a sequential approach has other advantages: semantic segmentation of an image is often a useful stand-alone intermediate product, and in a real-time 3D detection system, latency can be reduced by pipelining the image and lidar networks such that the lidar points are decorated with the semantics from the previous image. We show in ablation that such pipelining does not affect performance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We implement PointPainting with three state of the art lidar-only methods that have public code: PointPillars, VoxelNet (SECOND), and PointRCNN. PointPainting consistently improved results (Figure 1) and indeed, the painted version of PointRCNN achieves state of the art on the KITTI leaderboard (Table 2). We also show a significant improvement of 6.3 mAP (Table 4) for Painted PointPillars+ on nuScenes.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our main contribution is a novel fusion method, PointPainting, that augments the point cloud with image semantics.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contributions", "weight": 1.0} -->

general -- achieving significant improvements when used with 3 top lidar-only methods on the KITTI and nuScenes benchmarks;

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contributions", "weight": 1.0} -->

accurate -- the painted version of PointRCNN achieves state of the art on the KITTI benchmark;

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contributions", "weight": 1.0} -->

robust -- the painted versions of PointRCNN and PointPillars improved performance on *all classes* on the KITTI and nuScenes *test* sets, respectively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contributions", "weight": 1.0} -->

fast -- low latency fusion can be achieved by pipelining the image and lidar processing steps.

<!-- chunk {"id": "body-0022", "role": "body", "section": "PointPainting Architecture", "weight": 1.0} -->

The PointPainting architecture accepts point clouds and images as input and estimates oriented 3D boxes. It consists of three main stages (Fig. 2). Semantic Segmentation: an image based sem. seg. network which computes the pixel wise segmentation scores. Fusion: lidar points are painted with sem. seg. scores. 3D Object Detection: a lidar based 3D detection network.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Image Based Semantics Network", "weight": 1.0} -->

The image sem. seg. network takes in an input image and outputs per pixel class scores. These scores serve as compact summarized features of the image. There are several key advantages of using sem. seg. in a fusion pipeline. First, sem. seg. is an easier task than 3D object detection since segmentation only requires local, per pixel classification, while object detection requires 3D localization and classification. Networks that perform sem. seg. are easier to train and are also amenable to perform fast inference. Second, rapid advances are being made in sem. seg., which allows PointPainting to benefit from advances in both segmentation and 3D object detection. Finally, in a robotics or autonomous vehicle system, sem. seg. outputs are useful independent outputs for tasks like free-space estimation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Image Based Semantics Network", "weight": 1.0} -->

In this paper, the segmentation scores for our KITTI experiments are generated from DeepLabv3+, while for nuScenes experiments we trained a custom, lighter, network. However, we note that PointPainting is agnostic to the image segmentation network design.

<!-- chunk {"id": "body-0025", "role": "body", "section": "PointPainting", "weight": 1.0} -->

Here we provide details on the painting algorithm. Each point in the lidar point cloud is ($x$, $y$, $z$, $r$) or ($x$, $y$, $z$, $r$, $t$) for KITTI and nuScenes respectively, where $x$, $y$, $z$ are the spatial location of each lidar point, $r$ is the reflectance, and $t$ is the relative timestamp of the lidar point (applicable when using multiple lidar sweeps ). The lidar points are transformed by a homogenous transformation followed by a projection into the image. For KITTI this transformation is given by $T_{{camera}\leftarrow{lidar}}$. The nuScenes transformation requires extra care since the lidar and cameras operate at different frequencies.

<!-- chunk {"id": "body-0026", "role": "body", "section": "PointPainting", "weight": 1.0} -->

with transforms: lidar frame to the ego-vehicle frame; ego frame at time of lidar capture, $t_{l}$, to ego frame at the image capture time, $t_{c}$; and ego frame to camera frame. Finally, the camera matrix, $M$, projects the points into the image.

<!-- chunk {"id": "body-0027", "role": "body", "section": "PointPainting", "weight": 1.0} -->

The output of the segmentation network is $C$ class scores, where for KITTI $C = 4$ (car, pedestrian, cyclist, background) and for nuScenes $C = 11$ (10 detection classes plus background). Once the lidar points are projected into the image, the segmentation scores for the relevant pixel, ($h$, $w$), are appended to the lidar point to create the painted lidar point. Note, if the field of view of two cameras overlap, there will be some points that will project on two images simultaneously and we randomly choose the segmentation score vector from one of the two images. Another strategy can be to choose the more discriminative score vector by comparing their entropies or the margin between the top two scores. However, we leave that for future studies.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Lidar Detection", "weight": 1.0} -->

The decorated point clouds can be consumed by any lidar network that learns an encoder, since PointPainting just changes the input dimension of the lidar points. PointPainting can also be utilized by lidar networks with hand-engineered encoder, but requires specialized feature engineering for each method. In this paper, we demonstrate that PointPainting works with three different lidar detectors: PointPillars, VoxelNet, and PointRCNN. These are all state of the art lidar detectors with distinct network architectures: single stage (PointPillars, VoxelNet) vs two stage (PointRCNN), and pillars (PointPillars) vs voxels (VoxelNet) vs point-wise features (PointRCNN). Despite these different design choices, all lidar networks benefit from PointPainting (Table 1). Note that we were as inclusive as possible in this selection, and to the best of our knowledge, these represent all of the top KITTI detection leaderboard methods that have public code.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

In this section we present details of each dataset and the experimental settings of PointPainting.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Datasets", "weight": 1.0} -->

We evaluate our method on the KITTI and nuScenes datasets.

<!-- chunk {"id": "body-0031", "role": "body", "section": "KITTI", "weight": 1.0} -->

The KITTI dataset provides synced lidar point clouds and front-view camera images. It is relatively small with 7481 samples for training and 7518 samples for testing. For our test submission, we created a minival set of 784 samples from the training set and trained on the remaining 6733 samples. The KITTI object detection benchmark requires detection of cars, pedestrians, and cyclists. Ground truth objects were only annotated if they are visible in the image, so we follow the standard practice of only using lidar points that project into the image.

<!-- chunk {"id": "body-0032", "role": "body", "section": "nuScenes", "weight": 1.0} -->

The nuScenes dataset is larger than the KITTI dataset (7x annotations, 100x images). It it annotated with 3D bounding boxes for 1000 20-second scenes at 2Hz resulting in 28130 samples for training, 6019 samples for validation and 6008 samples for testing. nuScenes comprises the full autonomous vehicle data suite: synced lidar, cameras and radars with complete 360 coverage; in this work, we use the lidar point clouds and RGB images from all 6 cameras. The 3D object detection challenge evaluates the performance on 10 classes: cars, trucks, buses, trailers, construction vehicles, pedestrians, motorcycles, bicycles, traffic cones and barriers. Further, the dataset has an imbalance challenge with cars and pedestrians most frequent, and construction vehicles and bicycles least frequent.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Semantics Network Details", "weight": 1.0} -->

Here we provide more details on the semantics networks.

<!-- chunk {"id": "body-0034", "role": "body", "section": "KITTI", "weight": 1.0} -->

For experiments on KITTI, we used the DeepLabv3+ network^11^1 The network was first pretrained on Mapillary, then finetuned on Cityscapes, and finally finetuned again on KITTI pixelwise sem. seg.. Note that the class definition of cyclist differs between KITTI sem. seg. and object detection: in detection a cyclist is defined as rider $+$ bike, while in sem. seg. a cyclist is defined as only the rider with bike a separate class. There was therefore a need to map bikes which had a rider to the cyclist class, while supressing parked bikes to background. We did this after painting by mapping all points painted with the bike class within a $1m$ radius of a rider to the cyclist class; the rest to background.

<!-- chunk {"id": "body-0035", "role": "body", "section": "nuScenes", "weight": 1.0} -->

There was no public semantic segmentation method available on nuScenes so we trained a custom network using the nuImages dataset.^22^2We used an early access version; nuImages consists of $100$k images annotated with 2D bounding boxes and segmentation labels for all nuScenes classes. The segmentation network uses a ResNet backbone to generate features at strides $8$ to $64$ for a FCN segmentation head that predicts the nuScenes segmentation scores.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Lidar Network Details", "weight": 1.0} -->

We perform experiments using three different lidar networks: PointPillars, VoxelNet, and PointRCNN. The fusion versions of each network that use PointPainting will be referred to as being painted (e.g. Painted PointPillars).

<!-- chunk {"id": "body-0037", "role": "body", "section": "KITTI", "weight": 1.0} -->

We used the publicly released code for PointPillars^33^3 VoxelNet^44^4 and PointRCNN^55^5 and decorate the point cloud with the sem. seg. scores for $4$ classes. This changes the original decorated point cloud dimensions from $9\rightarrow 13$, $7\rightarrow 11$, and $4\rightarrow 8$ for PointPillars, VoxelNet, and PointRCNN respectively. For PointPillars, the new encoder has $$ channels, while for VoxelNet it has ${},{}$ channels. The $8$ dimensional painted point cloud for PointRCNN is given as input to both the encoder and the region pooling layer. No other changes were made to the public experimental configurations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "nuScenes", "weight": 1.0} -->

We use PointPillars for all nuScenes experiments. This requires changing the decorated point cloud from $7\rightarrow 18$, and the encoder has $$ channels now.

<!-- chunk {"id": "body-0039", "role": "body", "section": "nuScenes", "weight": 1.0} -->

In order to make sure the effect of painting is measured on a state of the art method, we made several improvemnts to the previously published PointPillars setup boosting the mAP by 10% on the nuScenes bechmark (Table 4). We refer to this improved baseline as PointPillars+. The changes are inspired by and comprise modifying pillar resolution, network architecture, attribute estimation, sample weighting, and data augmentation. First, the pillar resolution was reduced from 0.25 m to 0.2 m to allow for better localization of small objects. Second, the network architecture was changed to include more layers earlier in the network. Third, neither PointPillars nor PointPillars+ predict attributes, instead the attribute estimation heuristic was improved. Rather than using the most common attribute for each class, the predicted velocities and heights of each box are used to better estimate each attribute. Fourth, to reduce the class imbalance during training, a sample based weighting method was used where each sample was weighted according to the number of annotations in the sample. Fifth, the global yaw augmentation was changed from $\pi$ to $\pi/6$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we present PointPainting results on the KITTI and nuScenes datasets and compare to the literature.

<!-- chunk {"id": "body-0041", "role": "body", "section": "KITTI", "weight": 1.0} -->

All detection results are measured using the official KITTI evaluation detection for bird's-eye view (BEV) and 3D. The BEV results are presented here while the 3D results are included in the Supplementary Material. The KITTI dataset is stratified into easy, moderate, and hard difficulties, and the official KITTI leaderboard is ranked by performance on moderate average precision (AP).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Validation Set", "weight": 1.0} -->

First, we investigate the effect of PointPainting on three leading lidar detectors. Fig. 1 and Table 1 demonstrate that PointPainting improves the detection performance for PointPillars, VoxelNet, and PointRCNN. The PointPainting semantic information led to a widespread improvement in detection: 24 of 27 comparisons (${{{{3{experiments}} \times 3}{classes}} \times 3}{strata}$) were improved by PointPainting. While the greatest changes were for the more challenging scenarios of pedestrian and cyclist detection, most networks even saw an improvement on cars. This demonstrates that the utility of PointPainting is independent of the underlying lidar network.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Test Set", "weight": 1.0} -->

Here we compare PointPainting with state of the art KITTI test results. The KITTI leaderboard only allows one submission per paper, so we could not submit all Painted methods from Table 1. While Painted PointPillars performed better than Painted PointRCNN on the val set, of the two only PointPillars has public code for nuScenes. Therefore, to establish the generality of PointPainting, we chose to submit Painted PointPillars results to nuScenes test, and use our KITTI submission on Painted PointRCNN.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Test Set", "weight": 1.0} -->

As shown in Table 2, PointPainting leads to a robust improvement on the test set for PointRCNN: the average precision increases for every single class across all strata. Painted PointRCNN establishes new state of the art performance on mAP and cyclist AP.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Test Set", "weight": 1.0} -->

Based on the consistency of Painted PointRCNN improvements between val and test ($+ 2.73$ and $+ 2.94$ respectively), and the generality of PointPainting (Table 1), it is reasonable to believe that other methods in Table 2 would decidedly improve with PointPainting. The strength, generality, robustness, and flexibility of PointPainting suggests that it is the leading method for image-lidar fusion.

<!-- chunk {"id": "body-0046", "role": "body", "section": "nuScenes", "weight": 1.0} -->

To establish the versatility of PointPainting, we examine Painted PointPillars results on nuScenes. As a first step, we strengthened the lidar network baseline to PointPillars+. Even with this stronger baseline, PointPainting increases mean average precision (mAP) by $+ 6.3$ on the test set (Table 4). Painted PointPillars+ is only beat by MEGVII's lidar only method on nuScenes. However, MEGVII's network is impractical for a realtime system since it is an extremely large two stage network that requires high resolution inputs and uses multi-scale inputs and ensembles for test evaluation. Therefore, Painted PointPillars+ is the leading realtime method on nuScenes.

<!-- chunk {"id": "body-0047", "role": "body", "section": "nuScenes", "weight": 1.0} -->

The detection performance generalized well across classes with every class receiving a boost in AP from PointPainting (Table 3). In general, the worst performing detection classes in PointPillars+ benefited the most from painting, but there were exceptions. First, traffic cones received the largest increase in AP ($+ 16.8$) despite already having robust PointPillars+ detections. This is likely because traffic cones often have very few lidar points on them, so the additional information provided by semantic segmentation is extremely valuable. Second, trailer and construction vehicles had lower detection gains, despite starting from a smaller baseline. This was a consequence of the segmentation network having its worst recall on these classes (overall recall of $72\%$, but only $39\%$ on trailers and $40\%$ on construction vehicles; see Supplementary Material for details). Finally, despite a baseline of $76$ AP, cars still received a $+ 1.9$ AP boost, signaling the value of semantic information even for classes well detected by lidar only.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Here we give context to the evaluation metrics with some qualitative comparisons in Fig. 4 using Painted PointPillars, the best performing network on KITTI val set. In Fig. 4 A, original PointPillars correctly detects the cars, but misses a cyclist. The painted point cloud resolves this and the cyclist is detected. It also yields better orientation estimates for the vehicles. A common failure mode of lidar based methods is confusion between pedestrians and poles (Fig. 3). As expected, PointPainting can help resolve this (Fig. 4 B). Fig. 4 C suggests that the lidar detection step can correct incorrect painting. The loose segmentation masks in the image correctly paint nearby pedestrians, but extra paint also gets splattered onto the wall behind them. Despite this incorrect semantic information, the network does not predict false positive pedestrians. This leaves unanswered the precise characteristics of sem. seg. (e.g. precision vs recall) to optimize for PointPainting. In Fig. 4 D, Painted PointPillars predicts two false positive cyclists on the left because of two compounding mistakes. First, the sem. seg.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

network incorrectly predicts pedestrians as riders as they are so close to the parked bikes. Next, the heuristic that we used to resolve the discrepancy in the cyclist definition between detection and segmentation annotations (See Section 3.2) exacerbated the problem by painting all bikes with the cyclist class. However, throughout the rest of the crowded scene, the painted points lead to better oriented pedestrians, fewer false positives, and better detections of far away cars.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Here we perform ablation studies on the nuScenes dataset. All studies used the Painted PointPillars architecture and were trained for a quarter of the training time as compared to the test submissions. Using the one-cycle optimizer, we achieved 33.9 mAP and 46.3 NDS on the nuScenes val set as opposed to 44.85 mAP and 57.34 NDS for full training of Painted PointPillars+.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Quality", "weight": 1.0} -->

In PointPainting, the lidar points are fused with the semantic segmentation of the image. We investigate the impact of the semantic segmentation quality on the final detection performance. Using nuScenes, we generate a series of sem. seg. networks with varying segmentation quality by using multiple intermediate checkpoints from training. As shown in Fig. 5, improved sem. seg. (as measured by mean IOU), leads to improved 3D object detection.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Quality", "weight": 1.0} -->

For an upper bound, we include an "oracle" which uses the ground truth 3D boxes to paint the lidar points. This significantly improves the detection performance ($+ 27$ mAP), which demonstrates that advances in semantic segmentation would radically boost 3D object detection.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Quality", "weight": 1.0} -->

Using the oracle doesn't guarantee a perfect mAP because of several limitations. First, the ground truth bounding box can contain irrelevant points (e.g. from the ground). Second, nuScenes annotates all objects that contain a single lidar point. Turning one lidar point into an accurate, oriented 3D bounding box is difficult. Third, we trained it for the same total time as the other ablation studies, but it would probably benefit from longer training. Finally, PointPillars' stochastic sampling of the point cloud could significantly filter, or eliminate, the points that contain semantic information if the ground truth object contains only a few points.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Scores vs Labels", "weight": 1.0} -->

We investigate the effect of the segmentation prediction format on detection performance. To do so we convert the segmentation scores to a one hot encoding, effectively labelling each pixel as the class with the highest score. When using the labels instead of scores, the NDS was unchanged and the mAP was, surprisingly, $+ 0.4$ higher. However, the gains are marginal and within the noise of training. We also hypothesize that for future studies, a combination of calibrated segmentation scores and a larger PointPillars encoder would perform better.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Scores vs Labels", "weight": 1.0} -->

Comparing these results with the segmentation quality ablation suggests that future research focus more on improving segmentation quality and less on representation.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Sensitivity to Timing", "weight": 1.0} -->

We investigate the sensitivity of the lidar network to delays in semantic information. In the simplest scenario, which we used in all previous results, each point cloud is matched to the most recent image (Concurrent Matching - Fig. 6). However, this will introduce a latency in a real time system as the fusion step will have to wait for the image based sem. seg. scores. To eliminate the latency, the sem. seg. scores of the previous image can be pipelined into the lidar network (Consecutive Matching - Fig. 6). This involves an ego-motion compensation step where the lidar pointcloud is first transformed to the coordinate system of the ego-vehicle in the last frame followed by a projection into the image to get the segmentation scores. Our experiments suggest that using the previous images does not degrade detection performance (Table 5). Further, we measure that PointPainting only introduces an additional latency of 0.75 ms for the Painted PointPillars architecture (see Supplementary Material for details). This demonstrates that PointPainting can achieve high detection performance in a realtime system with minimal added latency.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we present PointPainting, a novel sequential fusion method that paints lidar point clouds with image based semantics. PointPainting produces state of the art results on the KITTI and nuScenes challenges with multiple different lidar networks. The PointPainting framework is flexible and can combine the outputs of any segmentation network with any lidar network. The strength of these results and the general applicability demonstrate that PointPainting is the leading architecture when fusing image and lidar information for 3D object detection.
