## Introduction

One relaxing summer weekend, I drove my family on an excursion to the zoo. All of a sudden, I saw a tiny black creature in front of my car. It was too far away for me to tell what it was, but as an experienced driver, I rolled out a series of moves without hesitation: I performed a shoulder check, I signaled, and then I switched lanes. In the end, I still had not figured out what it was until my daughter told me it was a raccoon crossing the street. The ability to recognize an object without knowing its semantics seems innate to us humans. However, this is in fact one of the holy grails that we strive to develop in our robotic perception systems.

A common paradigm in robotics perception is to train and deploy a machine-learned model under the closed-set condition; *i.e*., the robot is only trained to identify instances from known classes. In this paper, we argue that this is not enough for a practical perception system, since in real-world applications, robots often have to operate in an open environment interacting with surrounding objects that were not seen during training. Thus, an ideal perception system should be capable of recognizing and localizing objects from both known and unknown classes. This is referred to as the open-set setting.

We are not the first to realize the importance of identifying and interacting with unknown instances. In the pioneering work by Saxena et al., the authors proposed to grasp a novel object by identifying good positions to grasp; this could be trained on known instances and then generalized to unknowns. Also, cognitive scientists have studied the underlying mechanism by which the human vision system detects novel objects. In the 1980s, experiments on novel objects were conducted on rats to reveal how long/short term memory influences recognition. In the computer vision community, researchers approached the open-set recognition problem by first defining the open space as the space sufficiently far from any known positive training samples, measured by a multi-class classification function, where unknowns would carry all zero values in the classifier outputs. However, these approaches are either restricted to a classification task or specific to downstream robotics tasks. We generalize this idea to open-set instance segmentation with the additional capability to group observations into the same instance.

Figure 1: Exemplar output of open-set instance segmentation. The left figure depicts a horse on the road while the right figure depicts several construction elements. These objects are uncommon sights in day-to-day driving. However, an ideal robotics perception system should still be able to recognize and localize such objects, and determine whether they belong to one of the known classes.

Recognizing and segmenting an object without seeing its category during training is fundamentally challenging for modern deep networks. It makes the networks unable to exploit shape, appearance, and other information about the category during training. However the aforementioned capability critically influences deep models' success. Back to the mid-20th century, vision scientists identified a mechanism in the human vision system which groups visual elements that belong together into an object. This mechanism is called perceptual grouping and it contributes to our ability to recognize novel objects. Motivated by the success of the human vision system, our goal is to empower robots with a similar capability; *i.e*., we would like them to learn to perceptually group visual elements into a "thing", and then classify whether it belongs to one of the known classes.

Towards this goal of jointly recognizing both known and unknown instances, we propose a novel perception algorithm for LiDAR point clouds: the Open-Set Instance Segmentation (OSIS) network. The high-level idea is to use a deep convolutional network to identify uncertain points and group them into novel unknown instances. Specifically, we propose a category-agnostic instance embedding network to project points from the same instance to be close together in the embedding space. As a result, the network learns to group observations into a thing without knowing the thing's category. Our open-set inference procedure is straightforward: We first compute prototypical features from each known-class instance and then associate points with them according to their embedding feature distance. Finally, we cluster the rest of the points to form new unknown-class instances.

We validate our model's performance on two large-scale self-driving datasets with unknown objects. Our experiments show that OSIS outperforms other competing methods in terms of identifying instances from both known and unknown classes.

## Related Work

The problem of segmentation originates from the concept of perceptual grouping, which argues that human perception organizes perceptual signals into objects and meaningful clusters instead of raw pixels. Early segmentation approaches mainly deal with low-level regions and often do not capture the notion of objects. Recently, with the growing availability of high-quality segmentation labels, several benchmarks have become very popular for both semantic and instance segmentation tasks. Panoptic segmentation was proposed to combine the two problems together by jointly reasoning about instances and background.

Standard instance and panoptic segmentation approaches, however, fail to capture unknown instances that have never appeared in the training set. Towards the goal of explaining all pixels in the scene, open-set or out-of-distribution detection has been studied in the classification settings. Typically a threshold is learned such that predictions below the threshold are classified as unknown. proposed to use generative models to help calibrate the confidence level. Open-set recognition is also closely related to zero-shot learning; however, the latter puts more emphasis on bootstrapping novel concepts from cross modality inputs (*e.g*. natural languages).

Recently, several approaches have been proposed to address the open-set instance segmentation scenario. proposes a Bayesian framework that combines an instance segmentation network for known classes with an off-the-shelf contour detection algorithm for unknown classes. This approach can potentially be limited by the capacity of the offline contour detection algorithm. extends the standard instance segmentation task with thousands of extra visual concepts in the form of weak labels, covering a wide range of rare objects. This is, however, still closed-set recognition with weak labels. In, a category-agnostic object proposal network is trained and applied on video sequences. Due to its "proposal + classification" nature, the model may learn to suppress unknown objects that are present but not labeled in the training examples. In the 3D point clouds domain, proposed to leverage connected components, which could be less robust to cluttered scenes.

Next we review existing literature on instance segmentation. One mainstream approach for instance segmentation is based on object detection boxes, where object segmentations are produced within detection boxes. These approaches are referred to as "two-stage" joint detection and segmentation models. output object instance proposals directly from each pixel. For 3D point cloud, also use similar two-stage architectures to perform point cloud detection and segmentation. As segmentation happens after detection, unknown objects are often left unrecognized. Unless the object detector is trained to recognize unknown classes, these approaches are likely unsuitable for our open-set instance segmentation problem.

Another line of work for instance segmentation is based on bottom-up grouping of pixels. predicts energy of each instances and obtains instance segmentations using flood fill. cluster pixels by their predicted centroid locations. predicts breaking points on vertical and horizontal directions, and segments objects using line scanning. In 3D point cloud instance segmentation, several bottom-up approaches have also been proposed. predicts point affinity to make segmentation proposals for each point. When the number of points is large, as in the case of LiDAR point clouds, this approach can end up with too many proposals to process.

Our method is most similar to a line of work in bottom-up segmentation that learns instance-aware embeddings. Our method and these approaches all use clustering (*e.g*. mean-shift, DBSCAN, *etc*.) to aggregate the points into instances based on their embedding similarities. Despite having a similar instance-aware embedding component, our proposed method is distinguished by two major differences. First, we leverage an object detection head to propose anchors against which points can be clustered, thus resulting in a more efficient and effective algorithm with top-down guidance. Second, we propose to directly predict prototypical features for each anchor to account for the spatial sparsity and non-uniform density LiDAR point clouds.

Figure 2: Our OSIS model contains two branches: a) a detection head to detect anchors representing instances of known thing classes; and b) an embedding head to extract instance-aware embeddings for each point as well as prototypes for each thing anchor and each stuff class. In the first stage of inference, the prototypes collectively filter out points from the known classes. In the second stage, we cluster the remaining unknown points into instances using their embeddings and 3D locations.

## Identifying the Unknowns

In this paper, we propose the Open-Set Instance Segmentation (OSIS) network for identifying known and unknown objects from point clouds. In the following, we first formally define the problem of open-set instance segmentation in Sec. 3.1. Then, we discuss our full inference framework in Sec. 3.2. Finally, we provide details on how to train our model in Sec. 3.3.

### Problem Formulation

Let $\mathcal{X} = {\{\mathbf{x}_{i}\}}_{i = 1}^{N}$ be an input set of $N$ points, where each $\mathbf{x}_{i} \in {\mathbb{R}}^{D}$ is the input feature for point $i$. Given a set of instance ids $\mathbb{I}$ and a set of open-set semantic labels $\mathbb{O}$, we want a function $f$ mapping each input feature $\mathbf{x}_{i} \in \mathcal{X}$ to a tuple ${(y_{i},z_{i})} \in {{\mathbb{I}} \times {\mathbb{O}}}$. Note that $\mathbb{O}$ may be partitioned into two disjoint subsets $\mathbb{C}$ and $\{\bot\}$, where $\mathbb{C}$ is the set of known classes and $\bot$ is the semantic label for the unknown class. The known classes $\mathbb{C}$ can be further divided into ${\mathbb{C}}_{thing}$ and ${\mathbb{C}}_{stuff}$, which correspond to the known thing classes (*e.g*., vehicle and pedestrian) and the known stuff classes (*e.g*., road) respectively. As in, we require that every point with the same instance id have the same semantic label. Furthermore, we ignore the instance ids of stuff points.

Our problem formulation differs from standard panoptic segmentation with regards to how the unknown (void) class is handled. In the standard setting, we do not require instance labels for points with a void semantic label. By contrast, in our setting, we want to identify individual instances for the unknown class as well. Fig. 1 shows an example output for this task.

### Open-Set Instance Segmentation

In this subsection, we describe our proposed approach for open-set instance segmentation. Our approach is based on learning a category-agnostic embedding space in which points can be clustered into instances irrespective of their semantics. To this end, we design a convolutional neural network that consists of three components: 1) a shared backbone feature extractor; 2) a detection head to detect anchors representing instances of known things; and 3) an embedding head to predict instance-aware features for each point as well as prototypes for each thing anchor and stuff class.

Our inference procedure consists of two stages. First, we perform closed-set perception by associating points to prototypes of known things and stuff using the learned embedding space. Next, we perform open-set perception by classifying points with uncertain associations as unknown, and then clustering them into instances using their instance-aware embeddings and 3D coordinates as features. We refer the reader to Fig. 2 for an illustration of our full inference pipeline.

### Input representation

Our model takes as input a bird's eye view (BEV) rasterized image of a LiDAR point cloud $\mathcal{X} = {\{{(x_{i},y_{i},z_{i})}\}}_{i = 1}^{N}$ centered on the ego-car. Specifically, we voxelize $\mathcal{X}$ into a 3D occupancy grid using reversed trilinear interpolation and treat its vertical axis as multi-dimensional features. This yields a compact yet effective representation of $\mathcal{X}$ on which we can use 2D convolutions. Our model can also exploit temporal information by taking multiple BEV LiDAR frames stacked along the feature channel as input. To alleviate misalignment across frames due to the ego-car's movements, we use localization to compensate the ego-motion.

### Backbone network

We use a custom 2D convolutional feature pyramid network to extract multi-scale features from the input BEV LiDAR frame. In this network, we stack several residual blocks to compute a feature hierarchy consisting of three scales of the input resolution: $1/4$, $1/8$, and $1/16$. These multi-scale features are then upsampled to the $1/4$ scale and fused via residual connections to output a $C \times H \times W$ feature map, where $C$ is the number of feature channels, and $H$ and $W$ is the height and width of the feature map respectively. This feature map is subsequently used as input to the detection and embedding heads.

### Detection head

Our detection head consists of four $3 \times 3$ convolution layers, followed by a $1 \times 1$ convolution layer. For each BEV pixel and for each class in ${\mathbb{C}}_{thing}$, it predicts $(\alpha,{dx},{dy},w,l,{\sin{({2\theta})}},{\cos{({2\theta})}})$, where $\alpha$ is the anchor confidence score, $({dx},{dy})$ is the position offsets to its object center, and the rest parameterize the geometry of its bounding box. During inference, we remove anchors with scores less than $\tau$ to obtain the set of anchors $\mathcal{A}_{\tau}$. Note that the bounding box parameters are predicted only to exploit additional supervision signals.

### Embedding head

The embedding head forms the core of our open-set instance segmentation model: it learns a category-agnostic embedding space in which points can be clustered into instances irrespective of their semantics. Specifically, the embedding head is a four-layer CNN with $3 \times 3$ filters followed by three distinct branches:

The point branch computes features $\Phi_{point} \in {\mathbb{R}}^{{({F \times Z})} \times H \times W}$ via a $1 \times 1$ convolution, where $F$ is the dimension of the embedding space, and $Z$ is the number of bins along the gravitational $z$-axis. For each point $i$ in $\mathcal{X}$, we extract an embedding $\mathbf{\phi}_{i}$ from $\Phi_{point}$ via trilinear interpolation.

The thing branch computes features $\Phi_{thing} \in {\mathbb{R}}^{{({F + 1})} \times H \times W}$ via a $1 \times 1$ convolution. For each anchor $k$ in $\mathcal{A}_{\tau}$, we extract its prototype ${({\mathbf{μ}}_{k},\sigma_{k}^{2})} \in {{\mathbb{R}}^{F} \times {\mathbb{R}}}$ by bilinearly interpolating $\Phi_{thing}$ around the anchor's object center. This yields a set of thing prototypes $\mathcal{P}_{thing}$.

The stuff branch performs global average pooling to obtain features $\Phi_{stuff} \in {\mathbb{R}}^{C \times 1 \times 1}$. For each stuff class $c \in {\mathbb{C}}_{stuff}$, we apply a linear layer on $\Phi_{stuff}$ to predict its prototype ${({\mathbf{μ}}_{c},\sigma_{c}^{2})} \in {{\mathbb{R}}^{F} \times {\mathbb{R}}}$. This yields a set of stuff prototypes $\mathcal{P}_{stuff}$.

### Closed-set perception

Our closed-set perception algorithm draws inspiration from prototypical networks for few-shot learning. First, we apply non-maximum suppression to $\mathcal{P}_{thing}$ to obtain a unique set of thing prototypes $\mathcal{P}_{thing}^{\prime}$. Let us denote $\mathcal{P}_{all} = {\mathcal{P}_{thing}^{\prime} \cup \mathcal{P}_{stuff}}$ as the final set of all thing and stuff prototypes. Then, given a point $i$ in $\mathcal{X}$, we compute its point-to-prototype association score with respect to every prototype $k$ in $\mathcal{P}_{all}$ as follows:

Additionally, we have a learnable global constant $U$ corresponding to its score ${\hat{\mathbf{y}}}_{i,{{|\mathcal{P}_{all}|} + 1}}$ of not associating with any prototype in $\mathcal{P}_{all}$. Thus, its instance label can be computed by taking the argmax over its association scores ${\hat{\mathbf{y}}}_{i}$. Furthermore, its semantic label is simply the class of its instance, or unknown if it is not associated with any prototypes in $\mathcal{P}_{all}$. Note that, in practice, we compute each point's scores only with the prototypes of its $k$-nearest thing anchors and all $|{\mathbb{C}}_{stuff}|$ stuff classes; this helps to accelerate inference speed.

### Identifying unknown instances

We assign instance labels to unknown points via DBSCAN clustering. Specifically, for two points ${{\mathbf{x}}_{\mathbf{i}},{\mathbf{x}}_{\mathbf{j}}} \in \mathcal{X}$, their pairwise distance used in DBSCAN is a convex combination of their point embedding squared distance and their 3D location squared distance; *i.e*.,

Combining the instance labels obtained from this stage with the results from closed-set perception, we obtain our final open-set instance segmentation predictions.

Figure 3: Qualitative results of open-set instance segmentation on TOR4D and Rare4D.

### Learning

Our model is optimized with respect to a combination of detection and embedding losses:

where $\ell_{\det}$ is the detection loss, $\ell_{emb}$ is the embedding loss, and $\lambda$'s are their associated loss weights. In our experiments, we set $\lambda$'s to 1. Since $\mathcal{L}$ is fully differentiable with respect to the network parameters, we train our model using the standard back-propagation algorithm.

### Detection loss

We use a standard multi-task loss function to train the detection head. In particular, for object classification, we use binary cross-entropy with online negative hard mining, where positive and negative BEV pixels are determined by their distances to an object center. For bounding box regression, we use a combination of IoU loss for box locations and sizes and SmoothL1 loss for box orientations on predictions at positive pixels. It is worth noting that box sizes and orientations are not used during inference, and we predict them only for a stronger supervision signal.

### Embedding loss

We use a standard cross-entropy loss function to encourage points to be assigned to the correct prototype. In particular, during training we first gather a set of prototypes $\mathcal{P}_{gt}$, which is the union of $\mathcal{P}_{stuff}$ and the set of thing prototypes obtained by bilinearly interpolating $\Phi_{thing}$ around ground truth object centers. Next, we compute point-to-prototype association scores ${\{{\hat{\mathbf{y}}}_{i}\}}_{i = 1}^{N}$ with respect to $\mathcal{P}_{gt}$, and normalize each ${\hat{\mathbf{y}}}_{i}$ using the softmax function. Finally, we calculate the cross-entropy loss as follows:

where each ${\mathbf{y}}_{i}$ is a one-hot vector indicating ground truth associations. We also apply a discriminative loss function on the point embeddings ${\{\mathbf{\phi}_{i}\}}_{i = 1}^{N}$, which we found improves performance. \\newfloatcommandcapbtabboxtable\[\]\[\\FBwidth\]

Table 1: Quantitative results of open-set instance segmentation on the TOR4D and Rare4D test sets.

## Experiments

In this section, we showcase the effectiveness of our proposed model OSIS on two large-scale self-driving datasets. We first describe our experimental setup and then discuss the results we obtained.

### Experimental Setup

### Datasets

TOR4D is a large-scale self-driving dataset collected from cities across North America. This dataset consists of 6500 distinct driving scenarios, each containing 250 sweeps of LiDAR point clouds. We partition TOR4D into a training set of 5000 scenarios, a validation set of 500, and a test set of 1000. Furthermore, we subsample every five frames across all three splits.

Each frame in TOR4D is annotated with per-point semantic and instance labels according to four classes: vehicle, pedestrian, motorbike, and road. Points not belonging to one of those classes are unlabled and regarded as unknown. To evaluate OSIS in the open-set setting, we annotate 5,702 and 10,127 unique unknown objects with instance labels in the validation and test sets respectively.

Rare4D is a dataset of curated self-driving scenarios containing 289 unique rare objects such as forklifts, tractors, and even horses (see Fig. 1). In our experiments, Rare4D is not used for training but for evaluation of unknown object identification only.

### Evaluation metrics

For known classes, we report the panoptic quality (PQ), recognition quality (RQ), and segmentation quality (SQ) metrics proposed in. Since the labels in our dataset consider only things that are removeable to be separate objects (*e.g*., flags attached to a building will not be labeled), we decide not to measure precision; instead, we modify PQ into the *unknown quality* (UQ), a recall-based metric that measures performance on annotated instances only:

where $TP$ is the set of true positives and $FN$ is the set of false negatives. As in, a predicted unknown instance $p$ matches with the ground truth unknown instance $g$ if and only if their intersection over union exceeds 0.5.

### Baselines

Due to a lack of prior work in open-set instance segmentation for point clouds, we adapt several deep learning based instance segmentation algorithms to the open-set setting to serve as baselines. Note that all baselines except for MT-PNet use the same backbone network and input representations.

MT-PNet is a state-of-the-art joint 3D semantic and instance segmentation algorithm^11^1The CRF post-processing stage is not included.. We adapt MT-PNet to the open-set setting as follows: 1) we augment its semantic header to predict an additional unknown class; and 2) we use DBSCAN to cluster unknown points into instances based on their embedding distances.

BottomUp first runs a state-of-the-art point cloud semantic segmentation algorithm with an additional unknown class, and then uses DBSCAN to cluster points of the same class into instances. We evaluate two versions of this baseline: 1) BottomUp clusters points using their 3D locations; and 2) BottomUp+E clusters points using embeddings learned via a discriminative loss function.

Panoptic3D is similar to the pioneering panoptic segmentation algorithm proposed for 2D images. We first perform 3D detection and segmentation, and then apply heuristics to merge the outputs into a panoptic segmentation of the scene. Unlike, we train a single network with both a 3D detection and a semantic segmentation header. Similar to BottomUp, Panoptic3D also predicts an additional unknown class. We compare two versions of this baseline: 1) Panoptic3D performs class-agnostic detections; and 2) Panoptic3D+C performs class-aware detections and uses DBSCAN to cluster unknown points into instances based on their 3D locations.

### Implementation details

In our BottomUp, Panoptic3D, and OSIS experiments, we use a $160 \times 160 \times 5$ meters region of interest centered on the ego-vehicle. Points within this area are rasterized into a BEV image using reversed trilinear interpolation at a discretization resolution of $0.15625$. We use five frames of LiDAR as input and align them using ego-motion. This yields an input tensor of size ${C \times H \times W} = {160 \times 1024 \times 1024}$. We use the Adam optimizer with a batch size of 32 and an initial learning rate of ${4e} - 3$, which we decay by 0.1 after every five epochs for a total of ten epochs. Note that experiments for MT-PNet follow a similar setup, with the exception that we feed raw LiDAR point clouds as input to the model.

### Results

As shown in Tab. 1, OSIS outperforms the baselines on known and unknown things on all metrics across both datasets. Our method is also comparable to state-of-the-art semantic segmentation models for known stuff classes. Interestingly, BottomUp+E is the best baseline for unknown things while Panoptic3D+C is the best baseline for known things. As our results suggest, OSIS achieves the best of both worlds by marrying a bottom-up approach with top-down guidance.

Qualitative results in Fig. 3 further higlight our method's ability to correctly segment instances from both known and unknown classes. In particular, OSIS is the sole method that correctly segmented the horse and identified it as an unknown object; by contrast, the baseline methods suffer from misclassification errors and noise in instance segmentation. We also illustrate a failure case in the second row of Fig. 3. In this figure, OSIS misclassified a construction vehicle as unknown. Despite this mistake, our method still successfully segmented the vehicle as an instance.

### Ablation Studies

Table 2: Ablation study of model components on TOR4D validation set.

### Model design choices

We first conduct an ablation study on three components of our model: 1) whether we optimize the discriminative loss (DL); 2) whether we perform bounding box regression (BR); and 3) whether we predict per-prototype scalar variances (${\mathbf{σ}}^{\mathbf{2}}$). Tab. 2 shows our results on the TOR4D validation set. From this table, we can see that all three components contribute towards the overall performance of our model.

Figure 4: Unknown instance segmentation performance using different features for clustering. ”w/ oracle” indicates that we use ground truth to remove known points prior to DBSCAN.
Figure 5: Ablation study on varying the relative weight β of using 3D location distance versus embedding distance for identifying unknown instances.

### Effectiveness of instance-aware embeddings

We also study the effectiveness of using instance-aware embeddings to group unknown points into instances. In particular, we compare our embeddings against other per-point features, namely 3D location (Points), predicted instance center (Center), and semantic features (Semantics). From Tab. 5, we see that our instance-aware embeddings acheive the best results among the alternatives. Fig. 5 also indicates that using a combination of instance-aware embeddings and geometry features yields further improvements.

## Conclusion

We have presented a novel and effective open-set instance segmentation method for point clouds. In particular, we proposed a deep convolutional neural network to encode points into a category-agnostic embedding space in which they can be clustered into instances. As a result, our method is able to perceptually group points into instances, irrespective of whether they belong to a known or unknown class. We validate our method on two large-scale self-driving datasets and achieve state-of-the-art performance in the open-set setting. In the future we plan to explicitly reason about motion as a cue for better instance segmentation of moving objects.
