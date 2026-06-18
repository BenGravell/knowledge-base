## Introduction

Figure 1: VoxelNet directly operates on the raw point cloud (no need for feature engineering) and produces the 3D detection results using a single end-to-end trainable network.

Figure 2: VoxelNet architecture. The feature learning network takes a raw point cloud as input, partitions the space into voxels, and transforms points within each voxel to a vector representation characterizing the shape information. The space is represented as a sparse 4D tensor. The convolutional middle layers processes the 4D tensor to aggregate spatial context. Finally, a RPN generates the 3D detection.

Point cloud based 3D object detection is an important component of a variety of real-world applications, such as autonomous navigation, housekeeping robots, and augmented/virtual reality. Compared to image-based detection, LiDAR provides reliable depth information that can be used to accurately localize objects and characterize their shapes. However, unlike images, LiDAR point clouds are sparse and have highly variable point density, due to factors such as non-uniform sampling of the 3D space, effective range of the sensors, occlusion, and the relative pose. To handle these challenges, many approaches manually crafted feature representations for point clouds that are tuned for 3D object detection. Several methods project point clouds into a perspective view and apply image-based feature extraction techniques. Other approaches rasterize point clouds into a 3D voxel grid and encode each voxel with hand-crafted features. However, these manual design choices introduce an information bottleneck that prevents these approaches from effectively exploiting 3D shape information and the required invariances for the detection task. A major breakthrough in recognition and detection tasks on images was due to moving from hand-crafted features to machine-learned features.

Recently, Qi et al. proposed PointNet, an end-to-end deep neural network that learns point-wise features directly from point clouds. This approach demonstrated impressive results on 3D object recognition, 3D object part segmentation, and point-wise semantic segmentation tasks. In, an improved version of PointNet was introduced which enabled the network to learn local structures at different scales. To achieve satisfactory results, these two approaches trained feature transformer networks on all input points ($\sim$`<!-- -->`{=html}1k points). Since typical point clouds obtained using LiDARs contain $\sim$`<!-- -->`{=html}100k points, training the architectures as in results in high computational and memory requirements. Scaling up 3D feature learning networks to orders of magnitude more points and to 3D detection tasks are the main challenges that we address in this paper.

Region proposal network (RPN) is a highly optimized algorithm for efficient object detection. However, this approach requires data to be dense and organized in a tensor structure (e.g. image, video) which is not the case for typical LiDAR point clouds. In this paper, we close the gap between point set feature learning and RPN for 3D detection task.

We present VoxelNet, a generic 3D detection framework that simultaneously learns a discriminative feature representation from point clouds and predicts accurate 3D bounding boxes, in an end-to-end fashion, as shown in Figure 2. We design a novel voxel feature encoding (VFE) layer, which enables inter-point interaction within a voxel, by combining point-wise features with a locally aggregated feature. Stacking multiple VFE layers allows learning complex features for characterizing local 3D shape information. Specifically, VoxelNet divides the point cloud into equally spaced 3D voxels, encodes each voxel via stacked VFE layers, and then 3D convolution further aggregates local voxel features, transforming the point cloud into a high-dimensional volumetric representation. Finally, a RPN consumes the volumetric representation and yields the detection result. This efficient algorithm benefits both from the sparse point structure and efficient parallel processing on the voxel grid.

We evaluate VoxelNet on the bird's eye view detection and the full 3D detection tasks, provided by the KITTI benchmark. Experimental results show that VoxelNet outperforms the state-of-the-art LiDAR based 3D detection methods by a large margin. We also demonstrate that VoxelNet achieves highly encouraging results in detecting pedestrians and cyclists from LiDAR point cloud.

### Related Work

Rapid development of 3D sensor technology has motivated researchers to develop efficient representations to detect and localize objects in point clouds. Some of the earlier methods for feature representation are. These hand-crafted features yield satisfactory results when rich and detailed 3D shape information is available. However their inability to adapt to more complex shapes and scenes, and learn required invariances from data resulted in limited success for uncontrolled scenarios such as autonomous navigation.

Given that images provide detailed texture information, many algorithms infered the 3D bounding boxes from 2D images. However, the accuracy of image-based 3D detection approaches are bounded by the accuracy of the depth estimation.

Several LIDAR based 3D object detection techniques utilize a voxel grid representation. encode each nonempty voxel with 6 statistical quantities that are derived from all the points contained within the voxel. fuses multiple local statistics to represent each voxel. computes the truncated signed distance on the voxel grid. uses binary encoding for the 3D voxel grid. introduces a multi-view representation for a LiDAR point cloud by computing a multi-channel feature map in the bird's eye view and the cylindral coordinates in the frontal view. Several other studies project point clouds onto a perspective view and then use image-based feature encoding schemes.

There are also several multi-modal fusion methods that combine images and LiDAR to improve detection accuracy. These methods provide improved performance compared to LiDAR-only 3D detection, particularly for small objects (pedestrians, cyclists) or when the objects are far, since cameras provide an order of magnitude more measurements than LiDAR. However the need for an additional camera that is time synchronized and calibrated with the LiDAR restricts their use and makes the solution more sensitive to sensor failure modes. In this work we focus on LiDAR-only detection.

### Contributions

We propose a novel end-to-end trainable deep architecture for point-cloud-based 3D detection, VoxelNet, that directly operates on sparse 3D points and avoids information bottlenecks introduced by manual feature engineering.

We present an efficient method to implement VoxelNet which benefits both from the sparse point structure and efficient parallel processing on the voxel grid.

We conduct experiments on KITTI benchmark and show that VoxelNet produces state-of-the-art results in LiDAR-based car, pedestrian, and cyclist detection benchmarks.

## VoxelNet

In this section we explain the architecture of VoxelNet, the loss function used for training, and an efficient algorithm to implement the network.

### VoxelNet Architecture

The proposed VoxelNet consists of three functional blocks: Feature learning network, Convolutional middle layers, and Region proposal network, as illustrated in Figure 2. We provide a detailed introduction of VoxelNet in the following sections.

### Feature Learning Network

Voxel Partition Given a point cloud, we subdivide the 3D space into equally spaced voxels as shown in Figure 2. Suppose the point cloud encompasses 3D space with range $D$, $H$, $W$ along the Z, Y, X axes respectively. We define each voxel of size $v_{D}$, $v_{H}$, and $v_{W}$ accordingly. The resulting 3D voxel grid is of size ${D^{\prime} = {D/v_{D}}},{{H^{\prime} = {H/v_{H}}},{W^{\prime} = {W/v_{W}}}}$. Here, for simplicity, we assume $D$, $H$, $W$ are a multiple of $v_{D}$, $v_{H}$, $v_{W}$.

Grouping We group the points according to the voxel they reside in. Due to factors such as distance, occlusion, object's relative pose, and non-uniform sampling, the LiDAR point cloud is sparse and has highly variable point density throughout the space. Therefore, after grouping, a voxel will contain a variable number of points. An illustration is shown in Figure 2, where Voxel-1 has significantly more points than Voxel-2 and Voxel-4, while Voxel-3 contains no point.

Random Sampling Typically a high-definition LiDAR point cloud is composed of $\sim$`<!-- -->`{=html}100k points. Directly processing all the points not only imposes increased memory/efficiency burdens on the computing platform, but also highly variable point density throughout the space might bias the detection. To this end, we randomly sample a fixed number, $T$, of points from those voxels containing more than $T$ points. This sampling strategy has two purposes, computational savings (see Section 2.3 for details); and decreases the imbalance of points between the voxels which reduces the sampling bias, and adds more variation to training.

Stacked Voxel Feature Encoding The key innovation is the chain of VFE layers. For simplicity, Figure 2 illustrates the hierarchical feature encoding process for one voxel. Without loss of generality, we use VFE Layer-1 to describe the details in the following paragraph. Figure 3 shows the architecture for VFE Layer-1.

Figure 3: Voxel feature encoding layer.

Figure 4: Region proposal network architecture.

Denote $\mathbf{V} = {\{{\mathbf{p}_{i} = {\lbrack x_{i},y_{i},z_{i},r_{i}\rbrack}^{T} \in {\mathbb{R}}^{4}}\}}_{i = {1\ldotst}}$ as a non-empty voxel containing $t \leq T$ LiDAR points, where $\mathbf{p}_{i}$ contains XYZ coordinates for the $i$-th point and $r_{i}$ is the received reflectance. We first compute the local mean as the centroid of all the points in $\mathbf{V}$, denoted as $(v_{x},v_{y},v_{z})$. Then we augment each point $\mathbf{p}_{i}$ with the relative offset w.r.t. the centroid and obtain the input feature set $\mathbf{V}_{\text{in}} = {\{{{\hat{\mathbf{p}}}_{i} = {\lbrack x_{i},y_{i},z_{i},r_{i},{x_{i} - v_{x}},{y_{i} - v_{y}},{z_{i} - v_{z}}\rbrack}^{T} \in {\mathbb{R}}^{7}}\}}_{i = {1\ldotst}}$. Next, each ${\hat{\mathbf{p}}}_{i}$ is transformed through the fully connected network (FCN) into a feature space, where we can aggregate information from the point features $\mathbf{f}_{i} \in {\mathbb{R}}^{m}$ to encode the shape of the surface contained within the voxel. The FCN is composed of a linear layer, a batch normalization (BN) layer, and a rectified linear unit (ReLU) layer. After obtaining point-wise feature representations, we use element-wise MaxPooling across all $\mathbf{f}_{i}$ associated to $\mathbf{V}$ to get the locally aggregated feature $\overset{\sim}{\mathbf{f}} \in {\mathbb{R}}^{m}$ for $\mathbf{V}$. Finally, we augment each $\mathbf{f}_{i}$ with $\overset{\sim}{\mathbf{f}}$ to form the point-wise concatenated feature as $\mathbf{f}_{i}^{out} = {\lbrack\mathbf{f}_{i}^{T},{\overset{\sim}{\mathbf{f}}}^{T}\rbrack}^{T} \in {\mathbb{R}}^{2m}$. Thus we obtain the output feature set $\mathbf{V}_{\text{out}} = {\{\mathbf{f}_{i}^{out}\}}_{i\ldotst}$. All non-empty voxels are encoded in the same way and they share the same set of parameters in FCN.

We use $\text{VFE-i}{(c_{in},c_{out})}$ to represent the $i$-th VFE layer that transforms input features of dimension $c_{in}$ into output features of dimension $c_{out}$. The linear layer learns a matrix of size $c_{in} \times {({c_{out}/2})}$, and the point-wise concatenation yields the output of dimension $c_{out}$.

Because the output feature combines both point-wise features and locally aggregated feature, stacking VFE layers encodes point interactions within a voxel and enables the final feature representation to learn descriptive shape information. The voxel-wise feature is obtained by transforming the output of VFE-$n$ into ${\mathbb{R}}^{C}$ via FCN and applying element-wise Maxpool where $C$ is the dimension of the voxel-wise feature, as shown in Figure 2.

Sparse Tensor Representation By processing only the non-empty voxels, we obtain a list of voxel features, each uniquely associated to the spatial coordinates of a particular non-empty voxel. The obtained list of voxel-wise features can be represented as a sparse 4D tensor, of size $C \times D^{\prime} \times H^{\prime} \times W^{\prime}$ as shown in Figure 2. Although the point cloud contains $\sim$`<!-- -->`{=html}100k points, more than $90\%$ of voxels typically are empty. Representing non-empty voxel features as a sparse tensor greatly reduces the memory usage and computation cost during backpropagation, and it is a critical step in our efficient implementation.

### Convolutional Middle Layers

We use $\text{Conv}M\text{D}{(c_{in},c_{out},\mathbf{k},\mathbf{s},\mathbf{p})}$ to represent an $M$-dimensional convolution operator where $c_{in}$ and $c_{out}$ are the number of input and output channels, $\mathbf{k}$, $\mathbf{s}$, and $\mathbf{p}$ are the $M$-dimensional vectors corresponding to kernel size, stride size and padding size respectively. When the size across the $M$-dimensions are the same, we use a scalar to represent the size e.g. $k$ for $\mathbf{k} = {(k,k,k)}$.

Each convolutional middle layer applies 3D convolution, BN layer, and ReLU layer sequentially. The convolutional middle layers aggregate voxel-wise features within a progressively expanding receptive field, adding more context to the shape description. The detailed sizes of the filters in the convolutional middle layers are explained in Section 3.

### Region Proposal Network

Recently, region proposal networks have become an important building block of top-performing object detection frameworks. In this work, we make several key modifications to the RPN architecture proposed in, and combine it with the feature learning network and convolutional middle layers to form an end-to-end trainable pipeline.

The input to our RPN is the feature map provided by the convolutional middle layers. The architecture of this network is illustrated in Figure 4. The network has three blocks of fully convolutional layers. The first layer of each block downsamples the feature map by half via a convolution with a stride size of 2, followed by a sequence of convolutions of stride 1 ($\times q$ means $q$ applications of the filter). After each convolution layer, BN and ReLU operations are applied. We then upsample the output of every block to a fixed size and concatanate to construct the high resolution feature map. Finally, this feature map is mapped to the desired learning targets: a probability score map and a regression map.

### Loss Function

Let ${\{ a_{i}^{\text{pos}}\}}_{i = {1\ldotsN_{\text{pos}}}}$ be the set of $N_{\text{pos}}$ positive anchors and ${\{ a_{j}^{\text{neg}}\}}_{j = {1\ldotsN_{\text{neg}}}}$ be the set of $N_{\text{neg}}$ negative anchors. We parameterize a 3D ground truth box as $(x_{c}^{g},y_{c}^{g},z_{c}^{g},l^{g},w^{g},h^{g},\theta^{g})$, where $x_{c}^{g},y_{c}^{g},z_{c}^{g}$ represent the center location, $l^{g},w^{g},h^{g}$ are length, width, height of the box, and $\theta^{g}$ is the yaw rotation around Z-axis. To retrieve the ground truth box from a matching positive anchor parameterized as $(x_{c}^{a},y_{c}^{a},z_{c}^{a},l^{a},w^{a},h^{a},\theta^{a})$, we define the residual vector $\mathbf{u}^{\ast} \in {\mathbb{R}}^{7}$ containing the 7 regression targets corresponding to center location ${\Deltax},{\Deltay},{\Deltaz}$, three dimensions ${\Deltal},{\Deltaw},{\Deltah}$, and the rotation $\Delta\theta$, which are computed as:

where $d^{a} = \sqrt{{(l^{a})}^{2} + {(w^{a})}^{2}}$ is the diagonal of the base of the anchor box. Here, we aim to directly estimate the oriented 3D box and normalize $\Deltax$ and $\Deltay$ homogeneously with the diagonal $d^{a}$, which is different from. We define the loss function as follows:

where $p_{i}^{\text{pos}}$ and $p_{j}^{\text{neg}}$ represent the softmax output for positive anchor $a_{i}^{\text{pos}}$ and negative anchor $a_{j}^{\text{neg}}$ respectively, while $\mathbf{u}_{i} \in {\mathbb{R}}^{7}$ and $\mathbf{u}_{i}^{\ast} \in {\mathbb{R}}^{7}$ are the regression output and ground truth for positive anchor $a_{i}^{\text{pos}}$. The first two terms are the normalized classification loss for ${\{ a_{i}^{\text{pos}}\}}_{i = {1\ldotsN_{\text{pos}}}}$ and ${\{ a_{j}^{\text{neg}}\}}_{j = {1\ldotsN_{\text{neg}}}}$, where the $L_{\text{cls}}$ stands for binary cross entropy loss and $\alpha$, $\beta$ are postive constants balancing the relative importance. The last term $L_{reg}$ is the regression loss, where we use the SmoothL1 function.

Figure 5: Illustration of efficient implementation.

### Efficient Implementation

GPUs are optimized for processing dense tensor structures. The problem with working directly with the point cloud is that the points are sparsely distributed across space and each voxel has a variable number of points. We devised a method that converts the point cloud into a dense tensor structure where stacked VFE operations can be processed in parallel across points and voxels.

The method is summarized in Figure 5. We initialize a $K \times T \times 7$ dimensional tensor structure to store the voxel input feature buffer where $K$ is the maximum number of non-empty voxels, $T$ is the maximum number of points per voxel, and $7$ is the input encoding dimension for each point. The points are randomized before processing. For each point in the point cloud, we check if the corresponding voxel already exists. This lookup operation is done efficiently in $O{}$ using a hash table where the voxel coordinate is used as the hash key. If the voxel is already initialized we insert the point to the voxel location if there are less than $T$ points, otherwise the point is ignored. If the voxel is not initialized, we initialize a new voxel, store its coordinate in the voxel coordinate buffer, and insert the point to this voxel location. The voxel input feature and coordinate buffers can be constructed via a single pass over the point list, therefore its complexity is $O{(n)}$. To further improve the memory/compute efficiency it is possible to only store a limited number of voxels ($K$) and ignore points coming from voxels with few points.

After the voxel input buffer is constructed, the stacked VFE only involves point level and voxel level dense operations which can be computed on a GPU in parallel. Note that, after concatenation operations in VFE, we reset the features corresponding to empty points to zero such that they do not affect the computed voxel features. Finally, using the stored coordinate buffer we reorganize the computed sparse voxel-wise structures to the dense voxel grid. The following convolutional middle layers and RPN operations work on a dense voxel grid which can be efficiently implemented on a GPU.

## Training Details

In this section, we explain the implementation details of the VoxelNet and the training procedure.

### Network Details

Our experimental setup is based on the LiDAR specifications of the KITTI dataset.

Car Detection For this task, we consider point clouds within the range of ${\lbrack{- 3},1\rbrack} \times {\lbrack{- 40},40\rbrack} \times {\lbrack 0,70.4\rbrack}$ meters along Z, Y, X axis respectively. Points that are projected outside of image boundaries are removed. We choose a voxel size of ${v_{D} = 0.4},{{v_{H} = 0.2},{v_{W} = 0.2}}$ meters, which leads to $D^{\prime} = 10$, $H^{\prime} = 400$, $W^{\prime} = 352$. We set $T = 35$ as the maximum number of randomly sampled points in each non-empty voxel. We use two VFE layers $\text{VFE-1}{}$ and $\text{VFE-2}{}$. The final FCN maps VFE-2 output to ${\mathbb{R}}^{128}$. Thus our feature learning net generates a sparse tensor of shape $128 \times 10 \times 400 \times 352$. To aggregate voxel-wise features, we employ three convolution middle layers sequentially as Conv3D(128, 64, 3 ), Conv3D(64, 64, 3 ), and Conv3D(64, 64, 3 ), which yields a 4D tensor of size $64 \times 2 \times 400 \times 352$. After reshaping, the input to RPN is a feature map of size $128 \times 400 \times 352$, where the dimensions correspond to channel, height, and width of the 3D tensor. Figure 4 illustrates the detailed network architecture for this task. Unlike, we use only one anchor size, ${l^{a} = 3.9},{{w^{a} = 1.6},{h^{a} = 1.56}}$ meters, centered at $z_{c}^{a} = {- 1.0}$ meters with two rotations, 0 and 90 degrees. Our anchor matching criteria is as follows: An anchor is considered as positive if it has the highest Intersection over Union (IoU) with a ground truth or its IoU with ground truth is above 0.6 (in bird's eye view). An anchor is considered as negative if the IoU between it and all ground truth boxes is less than 0.45. We treat anchors as don't care if they have $0.45 \leq \text{IoU} \leq 0.6$ with any ground truth. We set $\alpha = 1.5$ and $\beta = 1$ in Eqn. 2.

Pedestrian and Cyclist Detection The input range^11^1Our empirical observation suggests that beyond this range, LiDAR returns from pedestrians and cyclists become very sparse and therefore detection results will be unreliable. is ${\lbrack{- 3},1\rbrack} \times {\lbrack{- 20},20\rbrack} \times {\lbrack 0,48\rbrack}$ meters along Z, Y, X axis respectively. We use the same voxel size as for car detection, which yields $D = 10$, $H = 200$, $W = 240$. We set $T = 45$ in order to obtain more LiDAR points for better capturing shape information. The feature learning network and convolutional middle layers are identical to the networks used in the car detection task. For the RPN, we make one modification to block 1 in Figure 4 by changing the stride size in the first 2D convolution from 2 to 1. This allows finer resolution in anchor matching, which is necessary for detecting pedestrians and cyclists. We use anchor size ${l^{a} = 0.8},{{w^{a} = 0.6},{h^{a} = 1.73}}$ meters centered at $z_{c}^{a} = {- 0.6}$ meters with 0 and 90 degrees rotation for pedestrian detection and use anchor size ${l^{a} = 1.76},{{w^{a} = 0.6},{h^{a} = 1.73}}$ meters centered at $z_{c}^{a} = {- 0.6}$ with 0 and 90 degrees rotation for cyclist detection. The specific anchor matching criteria is as follows: We assign an anchor as postive if it has the highest IoU with a ground truth, or its IoU with ground truth is above 0.5. An anchor is considered as negative if its IoU with every ground truth is less than 0.35. For anchors having $0.35 \leq \text{IoU} \leq 0.5$ with any ground truth, we treat them as don't care.

During training, we use stochastic gradient descent (SGD) with learning rate 0.01 for the first 150 epochs and decrease the learning rate to 0.001 for the last 10 epochs. We use a batchsize of 16 point clouds.

### Data Augmentation

With less than 4000 training point clouds, training our network from scratch will inevitably suffer from overfitting. To reduce this issue, we introduce three different forms of data augmentation. The augmented training data are generated on-the-fly without the need to be stored on disk.

Define set $\mathbf{M} = {\{{\mathbf{p}_{i} = {\lbrack x_{i},y_{i},z_{i},r_{i}\rbrack}^{T} \in {\mathbb{R}}^{4}}\}}_{i = {1,\ldots,N}}$ as the whole point cloud, consisting of $N$ points. We parameterize a 3D bouding box $\mathbf{b}_{i}$ as $(x_{c},y_{c},z_{c},l,w,h,\theta)$, where $x_{c},y_{c},z_{c}$ are center locations, $l,w,h$ are length, width, height, and $\theta$ is the yaw rotation around Z-axis. We define $\Omega_{i} = \left. \{\mathbf{p} \middle| {{x \in {\lbrack{x_{c} - {l/2}},{x_{c} + {l/2}}\rbrack}},{{y \in {\lbrack{y_{c} - {w/2}},{y_{c} + {w/2}}\rbrack}},{{z \in {\lbrack{z_{c} - {h/2}},{z_{c} + {h/2}}\rbrack}},{\mathbf{p} \in \mathbf{M}}}}}\} \right.$ as the set containing all LiDAR points within $\mathbf{b}_{i}$, where $\mathbf{p} = {\lbrack x,y,z,r\rbrack}$ denotes a particular LiDAR point in the whole set $\mathbf{M}$.

The first form of data augmentation applies perturbation independently to each ground truth 3D bounding box together with those LiDAR points within the box. Specifically, around Z-axis we rotate $\mathbf{b}_{i}$ and the associated $\Omega_{i}$ with respect to $(x_{c},y_{c},z_{c})$ by a uniformally distributed random variable ${\Delta\theta} \in {\lbrack{- {\pi/10}},{+ {\pi/10}}\rbrack}$. Then we add a translation $({\Deltax},{\Deltay},{\Deltaz})$ to the XYZ components of $\mathbf{b}_{i}$ and to each point in $\Omega_{i}$, where $\Deltax$, $\Deltay$, $\Deltaz$ are drawn independently from a Gaussian distribution with mean zero and standard deviation 1.0. To avoid physically impossible outcomes, we perform a collision test between any two boxes after the perturbation and revert to the original if a collision is detected. Since the perturbation is applied to each ground truth box and the associated LiDAR points independently, the network is able to learn from substantially more variations than from the original training data.

Secondly, we apply global scaling to all ground truth boxes $\mathbf{b}_{i}$ and to the whole point cloud $\mathbf{M}$. Specifically, we multiply the XYZ coordinates and the three dimensions of each $\mathbf{b}_{i}$, and the XYZ coordinates of all points in $\mathbf{M}$ with a random variable drawn from uniform distribution $\lbrack 0.95,1.05\rbrack$. Introducing global scale augmentation improves robustness of the network for detecting objects with various sizes and distances as shown in image-based classification and detection tasks.

Finally, we apply global rotation to all ground truth boxes $\mathbf{b}_{i}$ and to the whole point cloud $\mathbf{M}$. The rotation is applied along Z-axis and around $$. The global rotation offset is determined by sampling from uniform distribution $\lbrack{- {\pi/4}},{+ {\pi/4}}\rbrack$. By rotating the entire point cloud, we simulate the vehicle making a turn.

Table 1: Performance comparison in bird’s eye view detection: average precision (in %) on KITTI validation set.

Table 2: Performance comparison in 3D detection: average precision (in %) on KITTI validation set.

## Experiments

We evaluate VoxelNet on the KITTI 3D object detection benchmark which contains 7,481 training images/point clouds and 7,518 test images/point clouds, covering three categories: Car, Pedestrian, and Cyclist. For each class, detection outcomes are evaluated based on three difficulty levels: easy, moderate, and hard, which are determined according to the object size, occlusion state, and truncation level. Since the ground truth for the test set is not available and the access to the test server is limited, we conduct comprehensive evaluation using the protocol described in and subdivide the training data into a training set and a validation set, which results in 3,712 data samples for training and 3,769 data samples for validation. The split avoids samples from the same sequence being included in both the training and the validation set. Finally we also present the test results using the KITTI server.

For the Car category, we compare the proposed method with several top-performing algorithms, including image based approaches: Mono3D and 3DOP; LiDAR based approaches: VeloFCN and 3D-FCN; and a multi-modal approach MV. Mono3D, 3DOP and MV use a pre-trained model for initialization whereas we train VoxelNet from scratch using only the LiDAR data provided in KITTI.

To analyze the importance of end-to-end learning, we implement a strong baseline that is derived from the VoxelNet architecture but uses hand-crafted features instead of the proposed feature learning network. We call this model the hand-crafted baseline (HC-baseline). HC-baseline uses the bird's eye view features described in which are computed at $0.1$m resolution. Different from, we increase the number of height channels from 4 to 16 to capture more detailed shape information-- further increasing the number of height channels did not lead to performance improvement. We replace the convolutional middle layers of VoxelNet with similar size 2D convolutional layers, which are Conv2D, Conv2D, Conv2D. Finally RPN is identical in VoxelNet and HC-baseline. The total number of parameters in HC-baseline and VoxelNet are very similar. We train the HC-baseline using the same training procedure and data augmentation described in Section 3.

Figure 6: Qualitative results. For better visualization 3D boxes detected using LiDAR are projected on to the RGB images.

### Evaluation on KITTI Validation Set

### Metrics

We follow the official KITTI evaluation protocol, where the IoU threshold is 0.7 for class Car and is 0.5 for class Pedestrian and Cyclist. The IoU threshold is the same for both bird's eye view and full 3D evaluation. We compare the methods using the average precision (AP) metric.

### Evaluation in Bird's Eye View

The evaluation result is presented in Table 1. VoxelNet consistently outperforms all the competing approaches across all three difficulty levels. HC-baseline also achieves satisfactory performance compared to the state-of-the-art, which shows that our base region proposal network (RPN) is effective. For Pedestrian and Cyclist detection tasks in bird's eye view, we compare the proposed VoxelNet with HC-baseline. VoxelNet yields substantially higher AP than the HC-baseline for these more challenging categories, which shows that end-to-end learning is essential for point-cloud based detection.

We would like to note that reported 88.9%, 77.3%, and 72.7% for easy, moderate, and hard levels respectively, but these results are obtained based on a different split of 6,000 training frames and $\sim$`<!-- -->`{=html}1,500 validation frames, and they are not directly comparable with algorithms in Table 1. Therefore, we do not include these results in the table.

### Evaluation in 3D

Compared to the bird's eye view detection, which requires only accurate localization of objects in the 2D plane, 3D detection is a more challenging task as it requires finer localization of shapes in 3D space. Table 2 summarizes the comparison. For the class Car, VoxelNet significantly outperforms all other approaches in AP across all difficulty levels. Specifically, using only LiDAR, VoxelNet significantly outperforms the state-of-the-art method MV (BV+FV+RGB) based on LiDAR+RGB, by 10.68%, 2.78% and 6.29% in easy, moderate, and hard levels respectively. HC-baseline achieves similar accuracy to the MV method.

As in the bird's eye view evaluation, we also compare VoxelNet with HC-baseline on 3D Pedestrian and Cyclist detection. Due to the high variation in 3D poses and shapes, successful detection of these two categories requires better 3D shape representation. As shown in Table 2 the improved performance of VoxelNet is emphasized for more challenging 3D detection tasks (from $\sim$`<!-- -->`{=html}8% improvement in bird's eye view to $\sim$`<!-- -->`{=html}12% improvement on 3D detection) which suggests that VoxelNet is more effective in capturing 3D shape information than hand-crafted features.

### Evaluation on KITTI Test Set

We evaluated VoxelNet on the KITTI test set by submitting detection results to the official server. The results are summarized in Table 3. VoxelNet, significantly outperforms the previously published state-of-the-art in all the tasks (bird's eye view and 3D detection) and all difficulties. We would like to note that many of the other leading methods listed in KITTI benchmark use both RGB images and LiDAR point clouds whereas VoxelNet uses only LiDAR.

We present several 3D detection examples in Figure 6. For better visualization 3D boxes detected using LiDAR are projected on to the RGB images. As shown, VoxelNet provides highly accurate 3D bounding boxes in all categories.

The inference time for the VoxelNet is 225ms where the voxel input feature computation takes 5ms, feature learning net takes 20ms, convolutional middle layers take 170ms, and region proposal net takes 30ms on a TitanX GPU and 1.7Ghz CPU.

Car (Bird’s Eye View)

Pedestrian (Bird’s Eye View)

Cyclist (Bird’s Eye View)

Table 3: Performance evaluation on KITTI test set.

## Conclusion

Most existing methods in LiDAR-based 3D detection rely on hand-crafted feature representations, for example, a bird's eye view projection. In this paper, we remove the bottleneck of manual feature engineering and propose VoxelNet, a novel end-to-end trainable deep architecture for point cloud based 3D detection. Our approach can operate directly on sparse 3D points and capture 3D shape information effectively. We also present an efficient implementation of VoxelNet that benefits from point cloud sparsity and parallel processing on a voxel grid. Our experiments on the KITTI car detection task show that VoxelNet outperforms state-of-the-art LiDAR based 3D detection methods by a large margin. On more challenging tasks, such as 3D detection of pedestrians and cyclists, VoxelNet also demonstrates encouraging results showing that it provides a better 3D representation. Future work includes extending VoxelNet for joint LiDAR and image based end-to-end 3D detection to further improve detection and localization accuracy.
