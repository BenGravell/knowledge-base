<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

Topics include Object detection, Region proposal networks, Convolutional neural network, Two-stage detectors, Fast R-CNN, PASCAL VOC, COCO, Computer vision.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Region Proposal Networks as a learned, convolutional replacement for external proposal methods, letting proposals and Fast R-CNN detection share the same feature backbone. This made two-stage object detection substantially faster while improving accuracy, and became the reference architecture behind many later detection and instance-segmentation systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

State-of-the-art object detection networks depend on region proposal algorithms to hypothesize object locations. Advances like SPPnet and Fast R-CNN have reduced the running time of these detection networks, exposing region proposal computation as a bottleneck. In this work, we introduce a Region Proposal Network (RPN) that shares full-image convolutional features with the detection network, thus enabling nearly cost-free region proposals. An RPN is a fully convolutional network that simultaneously predicts object bounds and objectness scores at each position. The RPN is trained end-to-end to generate high-quality region proposals, which are used by Fast R-CNN for detection. We further merge RPN and Fast R-CNN into a single network by sharing their convolutional features - using the recently popular terminology of neural networks with 'attention' mechanisms, the RPN component tells the unified network where to look.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For the very deep VGG-16 model, our detection system has a frame rate of 5fps (including all steps) on a GPU, while achieving state-of-the-art object detection accuracy on PASCAL VOC 2007, 2012, and MS COCO datasets with only 300 proposals per image. In ILSVRC and COCO 2015 competitions, Faster R-CNN and RPN are the foundations of the 1st-place winning entries in several tracks. Code has been made publicly available.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in object detection are driven by the success of region proposal methods (*e.g*., ) and region-based convolutional neural networks (R-CNNs). Although region-based CNNs were computationally expensive as originally developed, their cost has been drastically reduced thanks to sharing convolutions across proposals. The latest incarnation, Fast R-CNN, achieves near real-time rates using very deep networks, *when ignoring the time spent on region proposals*. Now, proposals are the test-time computational bottleneck in state-of-the-art detection systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Region proposal methods typically rely on inexpensive features and economical inference schemes. Selective Search, one of the most popular methods, greedily merges superpixels based on engineered low-level features. Yet when compared to efficient detection networks, Selective Search is an order of magnitude slower, at 2 seconds per image in a CPU implementation. EdgeBoxes currently provides the best tradeoff between proposal quality and speed, at 0.2 seconds per image. Nevertheless, the region proposal step still consumes as much running time as the detection network.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

One may note that fast region-based CNNs take advantage of GPUs, while the region proposal methods used in research are implemented on the CPU, making such runtime comparisons inequitable. An obvious way to accelerate proposal computation is to re-implement it for the GPU. This may be an effective engineering solution, but re-implementation ignores the down-stream detection network and therefore misses important opportunities for sharing computation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we show that an algorithmic change---computing proposals with a deep convolutional neural network---leads to an elegant and effective solution where proposal computation is nearly cost-free given the detection network's computation. To this end, we introduce novel *Region Proposal Networks* (RPNs) that share convolutional layers with state-of-the-art object detection networks. By sharing convolutions at test-time, the marginal cost for computing proposals is small (*e.g*., 10ms per image).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our observation is that the convolutional feature maps used by region-based detectors, like Fast R-CNN, can also be used for generating region proposals. On top of these convolutional features, we construct an RPN by adding a few additional convolutional layers that simultaneously regress region bounds and objectness scores at each location on a regular grid. The RPN is thus a kind of fully convolutional network (FCN) and can be trained end-to-end specifically for the task for generating detection proposals.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

RPNs are designed to efficiently predict region proposals with a wide range of scales and aspect ratios. In contrast to prevalent methods that use pyramids of images (Figure 1, a) or pyramids of filters (Figure 1, b), we introduce novel "anchor" boxes that serve as references at multiple scales and aspect ratios. Our scheme can be thought of as a pyramid of regression references (Figure 1, c), which avoids enumerating images or filters of multiple scales or aspect ratios. This model performs well when trained and tested using single-scale images and thus benefits running speed.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To unify RPNs with Fast R-CNN object detection networks, we propose a training scheme that alternates between fine-tuning for the region proposal task and then fine-tuning for object detection, while keeping the proposals fixed. This scheme converges quickly and produces a unified network with convolutional features that are shared between both tasks.^11^1Since the publication of the conference version of this paper, we have also found that RPNs can be trained jointly with Fast R-CNN networks leading to less training time.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We comprehensively evaluate our method on the PASCAL VOC detection benchmarks where RPNs with Fast R-CNNs produce detection accuracy better than the strong baseline of Selective Search with Fast R-CNNs. Meanwhile, our method waives nearly all computational burdens of Selective Search at test-time---the effective running time for proposals is just 10 milliseconds. Using the expensive very deep models of, our detection method still has a frame rate of 5fps (*including all steps*) on a GPU, and thus is a practical object detection system in terms of both speed and accuracy. We also report results on the MS COCO dataset and investigate the improvements on PASCAL VOC using the COCO data. Code has been made publicly available at (in MATLAB) and (in Python).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

A preliminary version of this manuscript was published previously. Since then, the frameworks of RPN and Faster R-CNN have been adopted and generalized to other methods, such as 3D object detection, part-based detection, instance segmentation, and image captioning. Our fast and effective object detection system has also been built in commercial systems such as at Pinterests, with user engagement improvements reported.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In ILSVRC and COCO 2015 competitions, Faster R-CNN and RPN are the basis of several 1st-place entries in the tracks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation. RPNs completely learn to propose regions from data, and thus can easily benefit from deeper and more expressive features (such as the 101-layer residual nets adopted in ). Faster R-CNN and RPN are also used by several other leading entries in these competitions^22^2[ These results suggest that our method is not only a cost-efficient solution for practical usage, but also an effective way of improving object detection accuracy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Faster R-CNN", "weight": 1.0} -->

Our object detection system, called Faster R-CNN, is composed of two modules. The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector that uses the proposed regions. The entire system is a single, unified network for object detection (Figure 2). Using the recently popular terminology of neural networks with 'attention' mechanisms, the RPN module tells the Fast R-CNN module where to look. In Section 3.1 we introduce the designs and properties of the network for region proposal. In Section 3.2 we develop algorithms for training both modules with features shared.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Region Proposal Networks", "weight": 1.0} -->

A Region Proposal Network (RPN) takes an image (of any size) as input and outputs a set of rectangular object proposals, each with an objectness score.^33^3"Region" is a generic term and in this paper we only consider *rectangular* regions, as is common for many methods (*e.g*., ). "Objectness" measures membership to a set of object classes *vs*. background. We model this process with a fully convolutional network, which we describe in this section. Because our ultimate goal is to share computation with a Fast R-CNN object detection network, we assume that both nets share a common set of convolutional layers. In our experiments, we investigate the Zeiler and Fergus model (ZF), which has 5 shareable convolutional layers and the Simonyan and Zisserman model (VGG-16), which has 13 shareable convolutional layers.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Region Proposal Networks", "weight": 1.0} -->

To generate region proposals, we slide a small network over the convolutional feature map output by the last shared convolutional layer. This small network takes as input an $n \times n$ spatial window of the input convolutional feature map. Each sliding window is mapped to a lower-dimensional feature (256-d for ZF and 512-d for VGG, with ReLU following). This feature is fed into two sibling fully-connected layers---a box-regression layer (*reg*) and a box-classification layer (*cls*). We use $n = 3$ in this paper, noting that the effective receptive field on the input image is large (171 and 228 pixels for ZF and VGG, respectively). This mini-network is illustrated at a single position in Figure 3 (left). Note that because the mini-network operates in a sliding-window fashion, the fully-connected layers are shared across all spatial locations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Region Proposal Networks", "weight": 1.0} -->

This architecture is naturally implemented with an $n \times n$ convolutional layer followed by two sibling $1 \times 1$ convolutional layers (for *reg* and *cls*, respectively).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Anchors", "weight": 1.0} -->

At each sliding-window location, we simultaneously predict multiple region proposals, where the number of maximum possible proposals for each location is denoted as $k$. So the *reg* layer has $4k$ outputs encoding the coordinates of $k$ boxes, and the *cls* layer outputs $2k$ scores that estimate probability of object or not object for each proposal^44^4For simplicity we implement the *cls* layer as a two-class softmax layer. Alternatively, one may use logistic regression to produce $k$ scores.. The $k$ proposals are parameterized *relative* to $k$ reference boxes, which we call *anchors*. An anchor is centered at the sliding window in question, and is associated with a scale and aspect ratio (Figure 3, left). By default we use 3 scales and 3 aspect ratios, yielding $k = 9$ anchors at each sliding position. For a convolutional feature map of a size $W \times H$ (typically $\sim$`<!-- -->`{=html}2,400), there are $WHk$ anchors in total.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Anchors", "weight": 1.0} -->

An important property of our approach is that it is *translation invariant*, both in terms of the anchors and the functions that compute proposals relative to the anchors. If one translates an object in an image, the proposal should translate and the same function should be able to predict the proposal in either location. This translation-invariant property is guaranteed by our method^55^5As is the case of FCNs, our network is translation invariant up to the network's total stride.. As a comparison, the MultiBox method uses k-means to generate 800 anchors, which are *not* translation invariant. So MultiBox does not guarantee that the same proposal is generated if an object is translated.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Anchors", "weight": 1.0} -->

The translation-invariant property also reduces the model size. MultiBox has a ${({4 + 1})} \times 800$-dimensional fully-connected output layer, whereas our method has a ${({4 + 2})} \times 9$-dimensional convolutional output layer in the case of $k = 9$ anchors. As a result, our output layer has $2.8 \times 10^{4}$ parameters ($512 \times {({4 + 2})} \times 9$ for VGG-16), two orders of magnitude fewer than MultiBox's output layer that has $6.1 \times 10^{6}$ parameters ($1536 \times {({4 + 1})} \times 800$ for GoogleNet in MultiBox ).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Anchors", "weight": 1.0} -->

If considering the feature projection layers, our proposal layers still have an order of magnitude fewer parameters than MultiBox^66^6Considering the feature projection layers, our proposal layers' parameter count is ${{3 \times 3 \times 512 \times 512} + {512 \times 6 \times 9}} = {2.4 \times 10^{6}}$; MultiBox's proposal layers' parameter count is ${{7 \times 7 \times {({64 + 96 + 64 + 64})} \times 1536} + {1536 \times 5 \times 800}} = {27 \times 10^{6}}$.. We expect our method to have less risk of overfitting on small datasets, like PASCAL VOC.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Anchors", "weight": 1.0} -->

Our design of anchors presents a novel scheme for addressing multiple scales (and aspect ratios). As shown in Figure 1, there have been two popular ways for multi-scale predictions. The first way is based on image/feature pyramids, *e.g*., in DPM and CNN-based methods. The images are resized at multiple scales, and feature maps (HOG or deep convolutional features ) are computed for each scale (Figure 1(a)). This way is often useful but is time-consuming. The second way is to use sliding windows of multiple scales (and/or aspect ratios) on the feature maps. For example, in DPM, models of different aspect ratios are trained separately using different filter sizes (such as 5$\times$`<!-- -->`{=html}7 and 7$\times$`<!-- -->`{=html}5). If this way is used to address multiple scales, it can be thought of as a "pyramid of filters" (Figure 1(b)). The second way is usually adopted jointly with the first way.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Anchors", "weight": 1.0} -->

As a comparison, our anchor-based method is built on *a pyramid of anchors*, which is more cost-efficient. Our method classifies and regresses bounding boxes with reference to anchor boxes of multiple scales and aspect ratios. It only relies on images and feature maps of a single scale, and uses filters (sliding windows on the feature map) of a single size. We show by experiments the effects of this scheme for addressing multiple scales and sizes (Table VIII).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Anchors", "weight": 1.0} -->

Because of this multi-scale design based on anchors, we can simply use the convolutional features computed on a single-scale image, as is also done by the Fast R-CNN detector. The design of multi-scale anchors is a key component for sharing features without extra cost for addressing scales.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Loss Function", "weight": 1.0} -->

For training RPNs, we assign a binary class label (of being an object or not) to each anchor. We assign a positive label to two kinds of anchors: (i) the anchor/anchors with the highest Intersection-over-Union (IoU) overlap with a ground-truth box, *or* (ii) an anchor that has an IoU overlap higher than 0.7 with any ground-truth box. Note that a single ground-truth box may assign positive labels to multiple anchors. Usually the second condition is sufficient to determine the positive samples; but we still adopt the first condition for the reason that in some rare cases the second condition may find no positive sample. We assign a negative label to a non-positive anchor if its IoU ratio is lower than 0.3 for all ground-truth boxes. Anchors that are neither positive nor negative do not contribute to the training objective.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Loss Function", "weight": 1.0} -->

With these definitions, we minimize an objective function following the multi-task loss in Fast R-CNN.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Loss Function", "weight": 1.0} -->

Here, $i$ is the index of an anchor in a mini-batch and $p_{i}$ is the predicted probability of anchor $i$ being an object. The ground-truth label $p_{i}^{\ast}$ is 1 if the anchor is positive, and is 0 if the anchor is negative. $t_{i}$ is a vector representing the 4 parameterized coordinates of the predicted bounding box, and $t_{i}^{\ast}$ is that of the ground-truth box associated with a positive anchor. The classification loss $L_{cls}$ is log loss over two classes (object *vs*. not object). For the regression loss, we use ${L_{reg}{(t_{i},t_{i}^{\ast})}} = {R{({t_{i} - t_{i}^{\ast}})}}$ where $R$ is the robust loss function (smooth L~1~) defined.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Loss Function", "weight": 1.0} -->

The term $p_{i}^{\ast}L_{reg}$ means the regression loss is activated only for positive anchors ($p_{i}^{\ast} = 1$) and is disabled otherwise ($p_{i}^{\ast} = 0$). The outputs of the *cls* and *reg* layers consist of $\{ p_{i}\}$ and $\{ t_{i}\}$ respectively.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Loss Function", "weight": 1.0} -->

The two terms are normalized by $N_{cls}$ and $N_{reg}$ and weighted by a balancing parameter $\lambda$. In our current implementation (as in the released code), the $cls$ term in Eqn. is normalized by the mini-batch size (*i.e*., $N_{cls} = 256$) and the $reg$ term is normalized by the number of anchor locations (*i.e*., $N_{reg} \sim {2,400}$). By default we set $\lambda = 10$, and thus both *cls* and *reg* terms are roughly equally weighted. We show by experiments that the results are insensitive to the values of $\lambda$ in a wide range (Table IX). We also note that the normalization as above is not required and could be simplified.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Loss Function", "weight": 1.0} -->

where $x$, $y$, $w$, and $h$ denote the box's center coordinates and its width and height. Variables $x$, $x_{\text{a}}$, and $x^{\ast}$ are for the predicted box, anchor box, and ground-truth box respectively (likewise for $y,w,h$). This can be thought of as bounding-box regression from an anchor box to a nearby ground-truth box.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Loss Function", "weight": 1.0} -->

Nevertheless, our method achieves bounding-box regression by a different manner from previous RoI-based (Region of Interest) methods. In, bounding-box regression is performed on features pooled from *arbitrarily* sized RoIs, and the regression weights are *shared* by all region sizes. In our formulation, the features used for regression are of the *same* spatial size ($3 \times 3$) on the feature maps. To account for varying sizes, a set of $k$ bounding-box regressors are learned. Each regressor is responsible for one scale and one aspect ratio, and the $k$ regressors do *not* share weights. As such, it is still possible to predict boxes of various sizes even though the features are of a fixed size/scale, thanks to the design of anchors.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Training RPNs", "weight": 1.0} -->

The RPN can be trained end-to-end by back-propagation and stochastic gradient descent (SGD). We follow the "image-centric" sampling strategy from to train this network. Each mini-batch arises from a single image that contains many positive and negative example anchors. It is possible to optimize for the loss functions of all anchors, but this will bias towards negative samples as they are dominate. Instead, we randomly sample 256 anchors in an image to compute the loss function of a mini-batch, where the sampled positive and negative anchors have a ratio of *up to* 1:1. If there are fewer than 128 positive samples in an image, we pad the mini-batch with negative ones.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Training RPNs", "weight": 1.0} -->

We randomly initialize all new layers by drawing weights from a zero-mean Gaussian distribution with standard deviation 0.01. All other layers (*i.e*., the shared convolutional layers) are initialized by pre-training a model for ImageNet classification, as is standard practice. We tune all layers of the ZF net, and conv3$\_1$ and up for the VGG net to conserve memory. We use a learning rate of 0.001 for 60k mini-batches, and 0.0001 for the next 20k mini-batches on the PASCAL VOC dataset. We use a momentum of 0.9 and a weight decay of 0.0005. Our implementation uses Caffe.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

Thus far we have described how to train a network for region proposal generation, without considering the region-based object detection CNN that will utilize these proposals. For the detection network, we adopt Fast R-CNN. Next we describe algorithms that learn a unified network composed of RPN and Fast R-CNN with shared convolutional layers (Figure 2).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

Both RPN and Fast R-CNN, trained independently, will modify their convolutional layers in different ways. We therefore need to develop a technique that allows for sharing convolutional layers between the two networks, rather than learning two separate networks.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

\(i\) *Alternating training*. In this solution, we first train RPN, and use the proposals to train Fast R-CNN. The network tuned by Fast R-CNN is then used to initialize RPN, and this process is iterated. This is the solution that is used in all experiments in this paper.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

\(ii\) *Approximate joint training*. In this solution, the RPN and Fast R-CNN networks are merged into one network during training as in Figure 2. In each SGD iteration, the forward pass generates region proposals which are treated just like fixed, pre-computed proposals when training a Fast R-CNN detector. The backward propagation takes place as usual, where for the shared layers the backward propagated signals from both the RPN loss and the Fast R-CNN loss are combined. This solution is easy to implement. But this solution ignores the derivative w.r.t. the proposal boxes' coordinates that are also network responses, so is approximate. In our experiments, we have empirically found this solver produces close results, yet reduces the training time by about 25-50% comparing with alternating training. This solver is included in our released Python code.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

\(iii\) *Non-approximate joint training*. As discussed above, the bounding boxes predicted by RPN are also functions of the input. The RoI pooling layer in Fast R-CNN accepts the convolutional features and also the predicted bounding boxes as input, so a theoretically valid backpropagation solver should also involve gradients w.r.t. the box coordinates. These gradients are ignored in the above approximate joint training. In a non-approximate joint training solution, we need an RoI pooling layer that is differentiable w.r.t. the box coordinates. This is a nontrivial problem and a solution can be given by an "RoI warping" layer as developed, which is beyond the scope of this paper.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

4-Step Alternating Training. In this paper, we adopt a pragmatic 4-step training algorithm to learn shared features via alternating optimization. In the first step, we train the RPN as described in Section 3.1.3. This network is initialized with an ImageNet-pre-trained model and fine-tuned end-to-end for the region proposal task. In the second step, we train a separate detection network by Fast R-CNN using the proposals generated by the step-1 RPN. This detection network is also initialized by the ImageNet-pre-trained model. At this point the two networks do not share convolutional layers. In the third step, we use the detector network to initialize RPN training, but we fix the shared convolutional layers and only fine-tune the layers unique to RPN. Now the two networks share convolutional layers. Finally, keeping the shared convolutional layers fixed, we fine-tune the unique layers of Fast R-CNN. As such, both networks share the same convolutional layers and form a unified network.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

A similar alternating training can be run for more iterations, but we have observed negligible improvements.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

train-time region proposals
test-time region proposals

<!-- chunk {"id": "body-0043", "role": "body", "section": "Sharing Features for RPN and Fast R-CNN", "weight": 1.0} -->

## boxes
## proposals

<!-- chunk {"id": "body-0044", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

We train and test both region proposal and object detection networks on images of a single scale. We re-scale the images such that their shorter side is $s = 600$ pixels. Multi-scale feature extraction (using an image pyramid) may improve accuracy but does not exhibit a good speed-accuracy trade-off. On the re-scaled images, the total stride for both ZF and VGG nets on the last convolutional layer is 16 pixels, and thus is $\sim$`<!-- -->`{=html}10 pixels on a typical PASCAL image before resizing ($\sim$`<!-- -->`{=html}500$\times$`<!-- -->`{=html}375). Even such a large stride provides good results, though accuracy may be further improved with a smaller stride.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

For anchors, we use 3 scales with box areas of $128^{2}$, $256^{2}$, and $512^{2}$ pixels, and 3 aspect ratios of 1:1, 1:2, and 2:1. These hyper-parameters are *not* carefully chosen for a particular dataset, and we provide ablation experiments on their effects in the next section. As discussed, our solution does not need an image pyramid or filter pyramid to predict regions of multiple scales, saving considerable running time. Figure 3 (right) shows the capability of our method for a wide range of scales and aspect ratios. Table I shows the learned average proposal size for each anchor using the ZF net. We note that our algorithm allows predictions that are larger than the underlying receptive field. Such predictions are not impossible---one may still roughly infer the extent of an object if only the middle of the object is visible.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

The anchor boxes that cross image boundaries need to be handled with care. During training, we ignore all cross-boundary anchors so they do not contribute to the loss. For a typical $1000 \times 600$ image, there will be roughly 20000 ($\approx {60 \times 40 \times 9}$) anchors in total. With the cross-boundary anchors ignored, there are about 6000 anchors per image for training. If the boundary-crossing outliers are not ignored in training, they introduce large, difficult to correct error terms in the objective, and training does not converge. During testing, however, we still apply the fully convolutional RPN to the entire image. This may generate cross-boundary proposal boxes, which we clip to the image boundary.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Some RPN proposals highly overlap with each other. To reduce redundancy, we adopt non-maximum suppression (NMS) on the proposal regions based on their *cls* scores. We fix the IoU threshold for NMS at 0.7, which leaves us about 2000 proposal regions per image. As we will show, NMS does not harm the ultimate detection accuracy, but substantially reduces the number of proposals. After NMS, we use the top-$N$ ranked proposal regions for detection. In the following, we train Fast R-CNN using 2000 RPN proposals, but evaluate different numbers of proposals at test-time.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments on PASCAL VOC", "weight": 1.0} -->

We comprehensively evaluate our method on the PASCAL VOC 2007 detection benchmark. This dataset consists of about 5k trainval images and 5k test images over 20 object categories. We also provide results on the PASCAL VOC 2012 benchmark for a few models. For the ImageNet pre-trained network, we use the "fast" version of ZF net that has 5 convolutional layers and 3 fully-connected layers, and the public VGG-16 model^77^7[www.robots.ox.ac.uk/\~vgg/research/very_deep/](www.robots.ox.ac.uk/~vgg/research/very_deep/) that has 13 convolutional layers and 3 fully-connected layers. We primarily evaluate detection mean Average Precision (mAP), because this is the actual metric for object detection (rather than focusing on object proposal proxy metrics).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments on PASCAL VOC", "weight": 1.0} -->

Table II (top) shows Fast R-CNN results when trained and tested using various region proposal methods. These results use the ZF net. For Selective Search (SS), we generate about 2000 proposals by the "fast" mode. For EdgeBoxes (EB), we generate the proposals by the default EB setting tuned for 0.7 IoU. SS has an mAP of 58.7% and EB has an mAP of 58.6% under the Fast R-CNN framework. RPN with Fast R-CNN achieves competitive results, with an mAP of 59.9% while using *up to* 300 proposals^88^8For RPN, the number of proposals (*e.g*., 300) is the maximum number for an image. RPN may produce fewer proposals after NMS, and thus the average number of proposals is smaller.. Using RPN yields a much faster detection system than using either SS or EB because of shared convolutional computations; the fewer proposals also reduce the region-wise fully-connected layers' cost (Table V).

<!-- chunk {"id": "body-0050", "role": "body", "section": "proposals", "weight": 1.0} -->

Ablation Experiments on RPN. To investigate the behavior of RPNs as a proposal method, we conducted several ablation studies. First, we show the effect of sharing convolutional layers between the RPN and Fast R-CNN detection network. To do this, we stop after the second step in the 4-step training process. Using separate networks reduces the result slightly to 58.7% (RPN+ZF, unshared, Table II). We observe that this is because in the third step when the detector-tuned features are used to fine-tune the RPN, the proposal quality is improved.

<!-- chunk {"id": "body-0051", "role": "body", "section": "proposals", "weight": 1.0} -->

Next, we disentangle the RPN's influence on training the Fast R-CNN detection network. For this purpose, we train a Fast R-CNN model by using the 2000 SS proposals and ZF net. We fix this detector and evaluate the detection mAP by changing the proposal regions used at test-time. In these ablation experiments, the RPN does not share features with the detector.

<!-- chunk {"id": "body-0052", "role": "body", "section": "proposals", "weight": 1.0} -->

Replacing SS with 300 RPN proposals at test-time leads to an mAP of 56.8%. The loss in mAP is because of the inconsistency between the training/testing proposals. This result serves as the baseline for the following comparisons.

<!-- chunk {"id": "body-0053", "role": "body", "section": "proposals", "weight": 1.0} -->

Somewhat surprisingly, the RPN still leads to a competitive result (55.1%) when using the top-ranked 100 proposals at test-time, indicating that the top-ranked RPN proposals are accurate. On the other extreme, using the top-ranked 6000 RPN proposals (without NMS) has a comparable mAP (55.2%), suggesting NMS does not harm the detection mAP and may reduce false alarms.

<!-- chunk {"id": "body-0054", "role": "body", "section": "proposals", "weight": 1.0} -->

Next, we separately investigate the roles of RPN's *cls* and *reg* outputs by turning off either of them at test-time. When the *cls* layer is removed at test-time (thus no NMS/ranking is used), we randomly sample $N$ proposals from the unscored regions. The mAP is nearly unchanged with $N = 1000$ (55.8%), but degrades considerably to 44.6% when $N = 100$. This shows that the *cls* scores account for the accuracy of the highest ranked proposals.

<!-- chunk {"id": "body-0055", "role": "body", "section": "proposals", "weight": 1.0} -->

On the other hand, when the *reg* layer is removed at test-time (so the proposals become anchor boxes), the mAP drops to 52.1%. This suggests that the high-quality proposals are mainly due to the regressed box bounds. The anchor boxes, though having multiple scales and aspect ratios, are not sufficient for accurate detection.

<!-- chunk {"id": "body-0056", "role": "body", "section": "proposals", "weight": 1.0} -->

We also evaluate the effects of more powerful networks on the proposal quality of RPN alone. We use VGG-16 to train the RPN, and still use the above detector of SS+ZF. The mAP improves from 56.8% (using RPN+ZF) to 59.2% (using RPN+VGG). This is a promising result, because it suggests that the proposal quality of RPN+VGG is better than that of RPN+ZF. Because proposals of RPN+ZF are competitive with SS (both are 58.7% when consistently used for training and testing), we may expect RPN+VGG to be better than SS. The following experiments justify this hypothesis.

<!-- chunk {"id": "body-0057", "role": "body", "section": "box", "weight": 1.0} -->

Performance of VGG-16. Table III shows the results of VGG-16 for both proposal and detection. Using RPN+VGG, the result is 68.5% for *unshared* features, slightly higher than the SS baseline. As shown above, this is because the proposals generated by RPN+VGG are more accurate than SS. Unlike SS that is pre-defined, the RPN is actively trained and benefits from better networks. For the feature-*shared* variant, the result is 69.9%---better than the strong SS baseline, yet with nearly cost-free proposals. We further train the RPN and detection network on the union set of PASCAL VOC 2007 trainval and 2012 trainval. The mAP is 73.2%. Figure 5 shows some results on the PASCAL VOC 2007 test set. On the PASCAL VOC 2012 test set (Table IV), our method has an mAP of 70.4% trained on the union set of VOC 2007 trainval+test and VOC 2012 trainval. Table VI and Table VII show the detailed numbers.

<!-- chunk {"id": "body-0058", "role": "body", "section": "box", "weight": 1.0} -->

In Table V we summarize the running time of the entire object detection system. SS takes 1-2 seconds depending on content (on average about 1.5s), and Fast R-CNN with VGG-16 takes 320ms on 2000 SS proposals (or 223ms if using SVD on fully-connected layers ). Our system with VGG-16 takes in total 198ms for both proposal and detection. With the convolutional features shared, the RPN alone only takes 10ms computing the additional layers. Our region-wise computation is also lower, thanks to fewer proposals (300 per image). Our system has a frame-rate of 17 fps with the ZF net.

<!-- chunk {"id": "body-0059", "role": "body", "section": "box", "weight": 1.0} -->

dense, 3 scales, 3 aspect ratios
Fast R-CNN + ZF, 1 scale

<!-- chunk {"id": "body-0060", "role": "body", "section": "box", "weight": 1.0} -->

dense, 3 scales, 3 aspect ratios
Fast R-CNN + ZF, 5 scales

<!-- chunk {"id": "body-0061", "role": "body", "section": "box", "weight": 1.0} -->

Sensitivities to Hyper-parameters. In Table VIII we investigate the settings of anchors. By default we use 3 scales and 3 aspect ratios (69.9% mAP in Table VIII). If using just one anchor at each position, the mAP drops by a considerable margin of 3-4%. The mAP is higher if using 3 scales (with 1 aspect ratio) or 3 aspect ratios (with 1 scale), demonstrating that using anchors of multiple sizes as the regression references is an effective solution. Using just 3 scales with 1 aspect ratio (69.8%) is as good as using 3 scales with 3 aspect ratios on this dataset, suggesting that scales and aspect ratios are not disentangled dimensions for the detection accuracy. But we still adopt these two dimensions in our designs to keep our system flexible.

<!-- chunk {"id": "body-0062", "role": "body", "section": "box", "weight": 1.0} -->

In Table IX we compare different values of $\lambda$ in Equation. By default we use $\lambda = 10$ which makes the two terms in Equation roughly equally weighted after normalization. Table IX shows that our result is impacted just marginally (by $\sim {1\%}$) when $\lambda$ is within a scale of about two orders of magnitude (1 to 100). This demonstrates that the result is insensitive to $\lambda$ in a wide range.

<!-- chunk {"id": "body-0063", "role": "body", "section": "box", "weight": 1.0} -->

Analysis of Recall-to-IoU. Next we compute the recall of proposals at different IoU ratios with ground-truth boxes. It is noteworthy that the Recall-to-IoU metric is just *loosely* related to the ultimate detection accuracy. It is more appropriate to use this metric to *diagnose* the proposal method than to evaluate it.

<!-- chunk {"id": "body-0064", "role": "body", "section": "box", "weight": 1.0} -->

In Figure 4, we show the results of using 300, 1000, and 2000 proposals. We compare with SS and EB, and the $N$ proposals are the top-$N$ ranked ones based on the confidence generated by these methods. The plots show that the RPN method behaves gracefully when the number of proposals drops from 2000 to 300. This explains why the RPN has a good ultimate detection mAP when using as few as 300 proposals. As we analyzed before, this property is mainly attributed to the *cls* term of the RPN. The recall of SS and EB drops more quickly than RPN when the proposals are fewer.

<!-- chunk {"id": "body-0065", "role": "body", "section": "box", "weight": 1.0} -->

One-Stage Detection *vs*. Two-Stage Proposal + Detection. The OverFeat paper proposes a detection method that uses regressors and classifiers on sliding windows over convolutional feature maps. OverFeat is a *one-stage*, *class-specific* detection pipeline, and ours is a *two-stage cascade* consisting of class-agnostic proposals and class-specific detections. In OverFeat, the region-wise features come from a sliding window of one aspect ratio over a scale pyramid. These features are used to simultaneously determine the location and category of objects. In RPN, the features are from square (3$\times$`<!-- -->`{=html}3) sliding windows and predict proposals relative to anchors with different scales and aspect ratios. Though both methods use sliding windows, the region proposal task is only the first stage of Faster R-CNN---the downstream Fast R-CNN detector *attends* to the proposals to refine them. In the second stage of our cascade, the region-wise features are adaptively pooled from proposal boxes that more faithfully cover the features of the regions.

<!-- chunk {"id": "body-0066", "role": "body", "section": "box", "weight": 1.0} -->

We believe these features lead to more accurate detections.

<!-- chunk {"id": "body-0067", "role": "body", "section": "box", "weight": 1.0} -->

To compare the one-stage and two-stage systems, we *emulate* the OverFeat system (and thus also circumvent other differences of implementation details) by *one-stage* Fast R-CNN. In this system, the "proposals" are dense sliding windows of 3 scales and 3 aspect ratios (1:1, 1:2, 2:1). Fast R-CNN is trained to predict class-specific scores and regress box locations from these sliding windows. Because the OverFeat system adopts an image pyramid, we also evaluate using convolutional features extracted from 5 scales. We use those 5 scales as.

<!-- chunk {"id": "body-0068", "role": "body", "section": "box", "weight": 1.0} -->

Table X compares the two-stage system and two variants of the one-stage system. Using the ZF model, the one-stage system has an mAP of 53.9%. This is lower than the two-stage system (58.7%) by 4.8%. This experiment justifies the effectiveness of cascaded region proposals and object detection. Similar observations are reported, where replacing SS region proposals with sliding windows leads to $\sim$`<!-- -->`{=html}6% degradation in both papers. We also note that the one-stage system is slower as it has considerably more proposals to process.

<!-- chunk {"id": "body-0069", "role": "body", "section": "box", "weight": 1.0} -->

Fast R-CNN [impl. in this paper]

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

We present more results on the Microsoft COCO object detection dataset. This dataset involves 80 object categories. We experiment with the 80k images on the training set, 40k images on the validation set, and 20k images on the test-dev set. We evaluate the mAP averaged for IoU $\in {\lbrack 0.5:0.05:0.95\rbrack}$ (COCO's standard metric, simply denoted as mAP@\[.5,.95\]) and mAP@0.5 (PASCAL VOC's metric).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

There are a few minor changes of our system made for this dataset. We train our models on an 8-GPU implementation, and the effective mini-batch size becomes 8 for RPN (1 per GPU) and 16 for Fast R-CNN (2 per GPU). The RPN step and Fast R-CNN step are both trained for 240k iterations with a learning rate of 0.003 and then for 80k iterations with 0.0003. We modify the learning rates (starting with 0.003 instead of 0.001) because the mini-batch size is changed. For the anchors, we use 3 aspect ratios and 4 scales (adding $64^{2}$), mainly motivated by handling small objects on this dataset. In addition, in our Fast R-CNN step, the negative samples are defined as those with a maximum IoU with ground truth in the interval of $\lbrack 0,0.5)$, instead of $\lbrack 0.1,0.5)$ used.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

We note that in the SPPnet system, the negative samples in $\lbrack 0.1,0.5)$ are used for network fine-tuning, but the negative samples in $\lbrack 0,0.5)$ are still visited in the SVM step with hard-negative mining. But the Fast R-CNN system abandons the SVM step, so the negative samples in $\lbrack 0,0.1)$ are never visited. Including these $\lbrack 0,0.1)$ samples improves mAP@0.5 on the COCO dataset for both Fast R-CNN and Faster R-CNN systems (but the impact is negligible on PASCAL VOC).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

The rest of the implementation details are the same as on PASCAL VOC. In particular, we keep using 300 proposals and single-scale ($s = 600$) testing. The testing time is still about 200ms per image on the COCO dataset.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

In Table XI we first report the results of the Fast R-CNN system using the implementation in this paper. Our Fast R-CNN baseline has 39.3% mAP@0.5 on the test-dev set, higher than that reported. We conjecture that the reason for this gap is mainly due to the definition of the negative samples and also the changes of the mini-batch sizes. We also note that the mAP@\[.5,.95\] is just comparable.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

Next we evaluate our Faster R-CNN system. Using the COCO training set to train, Faster R-CNN has 42.1% mAP@0.5 and 21.5% mAP@\[.5,.95\] on the COCO test-dev set. This is 2.8% higher for mAP@0.5 and 2.2% higher for mAP@\[.5,.95\] than the Fast R-CNN counterpart under the same protocol (Table XI). This indicates that RPN performs excellent for improving the localization accuracy at higher IoU thresholds. Using the COCO trainval set to train, Faster R-CNN has 42.7% mAP@0.5 and 21.9% mAP@\[.5,.95\] on the COCO test-dev set. Figure 6 shows some results on the MS COCO test-dev set.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

Faster R-CNN in ILSVRC & COCO 2015 competitions We have demonstrated that Faster R-CNN benefits more from better features, thanks to the fact that the RPN completely learns to propose regions by neural networks. This observation is still valid even when one increases the depth substantially to over 100 layers. Only by replacing VGG-16 with a 101-layer residual net (ResNet-101), the Faster R-CNN system increases the mAP from 41.5%/21.2% (VGG-16) to 48.4%/27.2% (ResNet-101) on the COCO val set. With other improvements orthogonal to Faster R-CNN, He *et al*. obtained a single-model result of 55.7%/34.9% and an ensemble result of 59.0%/37.4% on the COCO test-dev set, which won the 1st place in the COCO 2015 object detection competition. The same system also won the 1st place in the ILSVRC 2015 object detection competition, surpassing the second place by absolute 8.5%.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Experiments on MS COCO", "weight": 1.0} -->

RPN is also a building block of the 1st-place winning entries in ILSVRC 2015 localization and COCO 2015 segmentation competitions, for which the details are available in and respectively.

<!-- chunk {"id": "body-0078", "role": "body", "section": "From MS COCO to PASCAL VOC", "weight": 1.0} -->

Large-scale data is of crucial importance for improving deep neural networks. Next, we investigate how the MS COCO dataset can help with the detection performance on PASCAL VOC.

<!-- chunk {"id": "body-0079", "role": "body", "section": "From MS COCO to PASCAL VOC", "weight": 1.0} -->

As a simple baseline, we directly evaluate the COCO detection model on the PASCAL VOC dataset, *without fine-tuning on any PASCAL VOC data*. This evaluation is possible because the categories on COCO are a superset of those on PASCAL VOC. The categories that are exclusive on COCO are ignored in this experiment, and the softmax layer is performed only on the 20 categories plus background. The mAP under this setting is 76.1% on the PASCAL VOC 2007 test set (Table XII). This result is better than that trained on +12 (73.2%) by a good margin, even though the PASCAL VOC data are not exploited.

<!-- chunk {"id": "body-0080", "role": "body", "section": "From MS COCO to PASCAL VOC", "weight": 1.0} -->

Then we fine-tune the COCO detection model on the VOC dataset. In this experiment, the COCO model is in place of the ImageNet-pre-trained model (that is used to initialize the network weights), and the Faster R-CNN system is fine-tuned as described in Section 3.2. Doing so leads to 78.8% mAP on the PASCAL VOC 2007 test set. The extra data from the COCO set increases the mAP by 5.6%. Table VI shows that the model trained on COCO+VOC has the best AP for every individual category on PASCAL VOC 2007. Similar improvements are observed on the PASCAL VOC 2012 test set (Table XII and Table VII). We note that the test-time speed of obtaining these strong results is still about 200ms per image.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented RPNs for efficient and accurate region proposal generation. By sharing convolutional features with the down-stream detection network, the region proposal step is nearly cost-free. Our method enables a unified, deep-learning-based object detection system to run at near real-time frame rates. The learned RPN also improves region proposal quality and thus the overall object detection accuracy.
