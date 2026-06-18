<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Focal Loss for Dense Object Detection

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The highest accuracy object detectors to date are based on a two-stage approach popularized by R-CNN, where a classifier is applied to a sparse set of candidate object locations. In contrast, one-stage detectors that are applied over a regular, dense sampling of possible object locations have the potential to be faster and simpler, but have trailed the accuracy of two-stage detectors thus far. In this paper, we investigate why this is the case. We discover that the extreme foreground-background class imbalance encountered during training of dense detectors is the central cause. We propose to address this class imbalance by reshaping the standard cross entropy loss such that it down-weights the loss assigned to well-classified examples. Our novel Focal Loss focuses training on a sparse set of hard examples and prevents the vast number of easy negatives from overwhelming the detector during training. To evaluate the effectiveness of our loss, we design and train a simple dense detector we call RetinaNet. Our results show that when trained with the focal loss, RetinaNet is able to match the speed of previous one-stage detectors while surpassing the accuracy of all existing state-of-the-art two-stage detectors.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current state-of-the-art object detectors are based on a two-stage, proposal-driven mechanism. As popularized in the R-CNN framework, the first stage generates a *sparse* set of candidate object locations and the second stage classifies each candidate location as one of the foreground classes or as background using a convolutional neural network. Through a sequence of advances, this two-stage framework consistently achieves top accuracy on the challenging COCO benchmark.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the success of two-stage detectors, a natural question to ask is: could a simple one-stage detector achieve similar accuracy? One stage detectors are applied over a regular, *dense* sampling of object locations, scales, and aspect ratios. Recent work on one-stage detectors, such as YOLO and SSD, demonstrates promising results, yielding faster detectors with accuracy within 10-40% relative to state-of-the-art two-stage methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper pushes the envelop further: we present a one-stage object detector that, for the first time, matches the state-of-the-art COCO AP of more complex two-stage detectors, such as the Feature Pyramid Network (FPN) or Mask R-CNN variants of Faster R-CNN. To achieve this result, we identify class imbalance during training as the main obstacle impeding one-stage detector from achieving state-of-the-art accuracy and propose a new loss function that eliminates this barrier.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Class imbalance is addressed in R-CNN-like detectors by a two-stage cascade and sampling heuristics. The proposal stage (*e.g*., Selective Search, EdgeBoxes, DeepMask, RPN ) rapidly narrows down the number of candidate object locations to a small number (*e.g*., 1-2k), filtering out most background samples. In the second classification stage, sampling heuristics, such as a fixed foreground-to-background ratio (1:3), or online hard example mining (OHEM), are performed to maintain a manageable balance between foreground and background.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, a one-stage detector must process a much larger set of candidate object locations regularly sampled across an image. In practice this often amounts to enumerating $\sim$`<!-- -->`{=html}100k locations that densely cover spatial positions, scales, and aspect ratios. While similar sampling heuristics may also be applied, they are inefficient as the training procedure is still dominated by easily classified background examples. This inefficiency is a classic problem in object detection that is typically addressed via techniques such as bootstrapping or hard example mining.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a new loss function that acts as a more effective alternative to previous approaches for dealing with class imbalance. The loss function is a dynamically scaled cross entropy loss, where the scaling factor decays to zero as confidence in the correct class increases, see Figure 1. Intuitively, this scaling factor can automatically down-weight the contribution of easy examples during training and rapidly focus the model on hard examples. Experiments show that our proposed *Focal Loss* enables us to train a high-accuracy, one-stage detector that significantly outperforms the alternatives of training with the sampling heuristics or hard example mining, the previous state-of-the-art techniques for training one-stage detectors. Finally, we note that the exact form of the focal loss is not crucial, and we show other instantiations can achieve similar results.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To demonstrate the effectiveness of the proposed focal loss, we design a simple one-stage object detector called *RetinaNet*, named for its dense sampling of object locations in an input image. Its design features an efficient in-network feature pyramid and use of anchor boxes. It draws on a variety of recent ideas. RetinaNet is efficient and accurate; our best model, based on a ResNet-101-FPN backbone, achieves a COCO test-dev AP of 39.1 while running at 5 fps, surpassing the previously best published single-model results from both one and two-stage detectors, see Figure 2.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Classic Object Detectors", "weight": 1.0} -->

The sliding-window paradigm, in which a classifier is applied on a dense image grid, has a long and rich history. One of the earliest successes is the classic work of LeCun *et al*. who applied convolutional neural networks to handwritten digit recognition. Viola and Jones used boosted object detectors for face detection, leading to widespread adoption of such models. The introduction of HOG and integral channel features gave rise to effective methods for pedestrian detection. DPMs helped extend dense detectors to more general object categories and had top results on PASCAL for many years. While the sliding-window approach was the leading detection paradigm in classic computer vision, with the resurgence of deep learning, two-stage detectors, described next, quickly came to dominate object detection.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Two-stage Detectors", "weight": 1.0} -->

The dominant paradigm in modern object detection is based on a two-stage approach. As pioneered in the Selective Search work, the first stage generates a sparse set of candidate proposals that should contain all objects while filtering out the majority of negative locations, and the second stage classifies the proposals into foreground classes / background. R-CNN upgraded the second-stage classifier to a convolutional network yielding large gains in accuracy and ushering in the modern era of object detection. R-CNN was improved over the years, both in terms of speed and by using learned object proposals. Region Proposal Networks (RPN) integrated proposal generation with the second-stage classifier into a single convolution network, forming the Faster R-CNN framework. Numerous extensions to this framework have been proposed, *e.g*..

<!-- chunk {"id": "body-0012", "role": "body", "section": "One-stage Detectors", "weight": 1.0} -->

OverFeat was one of the first modern one-stage object detector based on deep networks. More recently SSD and YOLO have renewed interest in one-stage methods. These detectors have been tuned for speed but their accuracy trails that of two-stage methods. SSD has a 10-20% lower AP, while YOLO focuses on an even more extreme speed/accuracy trade-off. See Figure 2. Recent work showed that two-stage detectors can be made fast simply by reducing input image resolution and the number of proposals, but one-stage methods trailed in accuracy even with a larger compute budget. In contrast, the aim of this work is to understand if one-stage detectors can match or surpass the accuracy of two-stage detectors while running at similar or faster speeds.

<!-- chunk {"id": "body-0013", "role": "body", "section": "One-stage Detectors", "weight": 1.0} -->

The design of our RetinaNet detector shares many similarities with previous dense detectors, in particular the concept of 'anchors' introduced by RPN and use of features pyramids as in SSD and FPN. We emphasize that our simple detector achieves top results not based on innovations in network design but due to our novel loss.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Class Imbalance", "weight": 1.0} -->

Both classic one-stage object detection methods, like boosted detectors and DPMs, and more recent methods, like SSD, face a large class imbalance during training. These detectors evaluate $10^{4}$-$10^{5}$ candidate locations per image but only a few locations contain objects. This imbalance causes two problems: training is inefficient as most locations are easy negatives that contribute no useful learning signal; en masse, the easy negatives can overwhelm training and lead to degenerate models. A common solution is to perform some form of hard negative mining that samples hard examples during training or more complex sampling/reweighing schemes. In contrast, we show that our proposed focal loss naturally handles the class imbalance faced by a one-stage detector and allows us to efficiently train on all examples without sampling and without easy negatives overwhelming the loss and computed gradients.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Robust Estimation", "weight": 1.0} -->

There has been much interest in designing robust loss functions (*e.g*., Huber loss ) that reduce the contribution of *outliers* by down-weighting the loss of examples with large errors (hard examples). In contrast, rather than addressing outliers, our focal loss is designed to address class imbalance by down-weighting *inliers* (easy examples) such that their contribution to the total loss is small even if their number is large. In other words, the focal loss performs the *opposite* role of a robust loss: it focuses training on a sparse set of hard examples.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

The *Focal Loss* is designed to address the one-stage object detection scenario in which there is an extreme imbalance between foreground and background classes during training (*e.g*., 1:1000). We introduce the focal loss starting from the cross entropy (CE) loss for binary classification^11^1Extending the focal loss to the multi-class case is straightforward and works well; for simplicity we focus on the binary loss in this work.:

<!-- chunk {"id": "body-0017", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

In the above $y \in {\{{\pm 1}\}}$ specifies the ground-truth class and $p \in {\lbrack 0,1\rbrack}$ is the model's estimated probability for the class with label $y = 1$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

The CE loss can be seen as the blue (top) curve in Figure 1. One notable property of this loss, which can be easily seen in its plot, is that even examples that are easily classified ($p_{\text{t}} \gg.5$) incur a loss with non-trivial magnitude. When summed over a large number of easy examples, these small loss values can overwhelm the rare class.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Balanced Cross Entropy", "weight": 1.0} -->

A common method for addressing class imbalance is to introduce a weighting factor $\alpha \in {\lbrack 0,1\rbrack}$ for class $1$ and $1 - \alpha$ for class $- 1$. In practice $\alpha$ may be set by inverse class frequency or treated as a hyperparameter to set by cross validation. For notational convenience, we define $\alpha_{\text{t}}$ analogously to how we defined $p_{\text{t}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Balanced Cross Entropy", "weight": 1.0} -->

This loss is a simple extension to CE that we consider as an experimental baseline for our proposed focal loss.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Focal Loss Definition", "weight": 1.0} -->

As our experiments will show, the large class imbalance encountered during training of dense detectors overwhelms the cross entropy loss. Easily classified negatives comprise the majority of the loss and dominate the gradient. While $\alpha$ balances the importance of positive/negative examples, it does not differentiate between easy/hard examples. Instead, we propose to reshape the loss function to down-weight easy examples and thus focus training on hard negatives.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Focal Loss Definition", "weight": 1.0} -->

More formally, we propose to add a modulating factor $\left( {1 - p_{\text{t}}} \right)^{\gamma}$ to the cross entropy loss, with tunable *focusing* parameter $\gamma \geq 0$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Focal Loss Definition", "weight": 1.0} -->

The focal loss is visualized for several values of $\gamma \in {\lbrack 0,5\rbrack}$ in Figure 1. We note two properties of the focal loss. When an example is misclassified and $p_{\text{t}}$ is small, the modulating factor is near $1$ and the loss is unaffected. As $p_{\text{t}}\rightarrow 1$, the factor goes to 0 and the loss for well-classified examples is down-weighted. The focusing parameter $\gamma$ smoothly adjusts the rate at which easy examples are down-weighted. When $\gamma = 0$, FL is equivalent to CE, and as $\gamma$ is increased the effect of the modulating factor is likewise increased (we found $\gamma = 2$ to work best in our experiments).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Focal Loss Definition", "weight": 1.0} -->

Intuitively, the modulating factor reduces the loss contribution from easy examples and extends the range in which an example receives low loss. For instance, with $\gamma = 2$, an example classified with $p_{\text{t}} = 0.9$ would have $100 \times$ lower loss compared with CE and with $p_{\text{t}} \approx 0.968$ it would have $1000 \times$ lower loss. This in turn increases the importance of correcting misclassified examples (whose loss is scaled down by at most $4 \times$ for $p_{\text{t}} \leq.5$ and $\gamma = 2$).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Focal Loss Definition", "weight": 1.0} -->

We adopt this form in our experiments as it yields slightly improved accuracy over the non-$\alpha$-balanced form. Finally, we note that the implementation of the loss layer combines the sigmoid operation for computing $p$ with the loss computation, resulting in greater numerical stability.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Focal Loss Definition", "weight": 1.0} -->

While in our main experimental results we use the focal loss definition above, its precise form is not crucial. In the appendix we consider other instantiations of the focal loss and demonstrate that these can be equally effective.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Class Imbalance and Model Initialization", "weight": 1.0} -->

Binary classification models are by default initialized to have equal probability of outputting either $y = {- 1}$ or $1$. Under such an initialization, in the presence of class imbalance, the loss due to the frequent class can dominate total loss and cause instability in early training. To counter this, we introduce the concept of a 'prior' for the value of $p$ estimated by the model for the rare class (foreground) *at the start of training*. We denote the prior by $\pi$ and set it so that the model's estimated $p$ for examples of the rare class is low, *e.g*. $0.01$. We note that this is a change in model initialization (see §4.1) and *not* of the loss function. We found this to improve training stability for both the cross entropy and focal loss in the case of heavy class imbalance.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Class Imbalance and Two-stage Detectors", "weight": 1.0} -->

Two-stage detectors are often trained with the cross entropy loss without use of $\alpha$-balancing or our proposed loss. Instead, they address class imbalance through two mechanisms: a two-stage cascade and biased minibatch sampling. The first cascade stage is an object proposal mechanism that reduces the nearly infinite set of possible object locations down to one or two thousand. Importantly, the selected proposals are not random, but are likely to correspond to true object locations, which removes the vast majority of easy negatives. When training the second stage, biased sampling is typically used to construct minibatches that contain, for instance, a 1:3 ratio of positive to negative examples. This ratio is like an implicit $\alpha$-balancing factor that is implemented via sampling. Our proposed focal loss is designed to address these mechanisms in a one-stage detection system directly via the loss function.

<!-- chunk {"id": "body-0029", "role": "body", "section": "RetinaNet Detector", "weight": 1.0} -->

RetinaNet is a single, unified network composed of a *backbone* network and two task-specific *subnetworks*. The backbone is responsible for computing a convolutional feature map over an entire input image and is an off-the-self convolutional network. The first subnet performs convolutional object classification on the backbone's output; the second subnet performs convolutional bounding box regression. The two subnetworks feature a simple design that we propose specifically for one-stage, dense detection, see Figure 3. While there are many possible choices for the details of these components, most design parameters are not particularly sensitive to exact values as shown in the experiments. We describe each component of RetinaNet next.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Feature Pyramid Network Backbone", "weight": 1.0} -->

We adopt the Feature Pyramid Network (FPN) from as the backbone network for RetinaNet. In brief, FPN augments a standard convolutional network with a top-down pathway and lateral connections so the network efficiently constructs a rich, multi-scale feature pyramid from a single resolution input image, see Figure 3(a)-(b). Each level of the pyramid can be used for detecting objects at a different scale. FPN improves multi-scale predictions from fully convolutional networks (FCN), as shown by its gains for RPN and DeepMask-style proposals, as well at two-stage detectors such as Fast R-CNN or Mask R-CNN.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Feature Pyramid Network Backbone", "weight": 1.0} -->

Following, we build FPN on top of the ResNet architecture. We construct a pyramid with levels $P_{3}$ through $P_{7}$, where $l$ indicates pyramid level ($P_{l}$ has resolution $2^{l}$ lower than the input). As in all pyramid levels have $C = 256$ channels.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Feature Pyramid Network Backbone", "weight": 1.0} -->

Details of the pyramid generally follow with a few modest differences.^22^2RetinaNet uses feature pyramid levels $P_{3}$ to $P_{7}$, where $P_{3}$ to $P_{5}$ are computed from the output of the corresponding ResNet residual stage ($C_{3}$ through $C_{5}$) using top-down and lateral connections just as, $P_{6}$ is obtained via a 3$\times$`<!-- -->`{=html}3 stride-2 conv on $C_{5}$, and $P_{7}$ is computed by applying ReLU followed by a 3$\times$`<!-- -->`{=html}3 stride-2 conv on $P_{6}$. This differs slightly: we don't use the high-resolution pyramid level $P_{2}$ for computational reasons, $P_{6}$ is computed by strided convolution instead of downsampling, and we include $P_{7}$ to improve large object detection.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Feature Pyramid Network Backbone", "weight": 1.0} -->

These minor modifications improve speed while maintaining accuracy. While many design choices are not crucial, we emphasize the use of the FPN backbone is; preliminary experiments using features from only the final ResNet layer yielded low AP.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Anchors", "weight": 1.0} -->

We use translation-invariant anchor boxes similar to those in the RPN variant. The anchors have areas of $32^{2}$ to $512^{2}$ on pyramid levels $P_{3}$ to $P_{7}$, respectively. As, at each pyramid level we use anchors at three aspect ratios $\{ 1$:$2,$ $1$:$1$, $2$:$1\}$. For denser scale coverage than, at each level we add anchors of sizes {$2^{0}$, $2^{1/3}$, $2^{2/3}$} of the original set of 3 aspect ratio anchors. This improve AP in our setting. In total there are $A = 9$ anchors per level and across levels they cover the scale range 32 - 813 pixels with respect to the network's input image.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Anchors", "weight": 1.0} -->

Each anchor is assigned a length $K$ one-hot vector of classification targets, where $K$ is the number of object classes, and a 4-vector of box regression targets. We use the assignment rule from RPN but modified for multi-class detection and with adjusted thresholds. Specifically, anchors are assigned to ground-truth object boxes using an intersection-over-union (IoU) threshold of 0.5; and to background if their IoU is in \0, 0.4). As each anchor is assigned to at most one object box, we set the corresponding entry in its length $K$ label vector to $1$ and all other entries to $0$. If an anchor is unassigned, which may happen with overlap in \[0.4, 0.5), it is ignored during training. Box regression targets are computed as the offset between each anchor and its assigned object box, or omitted if there is no assignment.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Classification Subnet", "weight": 1.0} -->

The classification subnet predicts the probability of object presence at each spatial position for each of the $A$ anchors and $K$ object classes. This subnet is a small FCN attached to each FPN level; parameters of this subnet are shared across all pyramid levels. Its design is simple. Taking an input feature map with $C$ channels from a given pyramid level, the subnet applies four 3$\times$`<!-- -->`{=html}3 conv layers, each with $C$ filters and each followed by ReLU activations, followed by a 3$\times$`<!-- -->`{=html}3 conv layer with $KA$ filters. Finally sigmoid activations are attached to output the $KA$ binary predictions per spatial location, see Figure [3 (c). We use $C = 256$ and $A = 9$ in most experiments.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Classification Subnet", "weight": 1.0} -->

In contrast to RPN, our object classification subnet is deeper, uses only 3$\times$`<!-- -->`{=html}3 convs, and does not share parameters with the box regression subnet (described next). We found these higher-level design decisions to be more important than specific values of hyperparameters.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Box Regression Subnet", "weight": 1.0} -->

In parallel with the object classification subnet, we attach another small FCN to each pyramid level for the purpose of regressing the offset from each anchor box to a nearby ground-truth object, if one exists. The design of the box regression subnet is identical to the classification subnet except that it terminates in $4A$ linear outputs per spatial location, see Figure 3 (d). For each of the $A$ anchors per spatial location, these $4$ outputs predict the relative offset between the anchor and the ground-truth box (we use the standard box parameterization from R-CNN ). We note that unlike most recent work, we use a class-agnostic bounding box regressor which uses fewer parameters and we found to be equally effective. The object classification subnet and the box regression subnet, though sharing a common structure, use separate parameters.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Inference", "weight": 1.0} -->

RetinaNet forms a single FCN comprised of a ResNet-FPN backbone, a classification subnet, and a box regression subnet, see Figure 3. As such, inference involves simply forwarding an image through the network. To improve speed, we only decode box predictions from at most 1k top-scoring predictions per FPN level, after thresholding detector confidence at 0.05. The top predictions from all levels are merged and non-maximum suppression with a threshold of 0.5 is applied to yield the final detections.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

We use the focal loss introduced in this work as the loss on the output of the classification subnet. As we will show in §5, we find that $\gamma = 2$ works well in practice and the RetinaNet is relatively robust to $\gamma \in {\lbrack 0.5,5\rbrack}$. We emphasize that when training RetinaNet, the focal loss is applied to *all* $\sim$`<!-- -->`{=html}100k anchors in each sampled image. This stands in contrast to common practice of using heuristic sampling (RPN) or hard example mining (OHEM, SSD) to select a small set of anchors (*e.g*., 256) for each minibatch. The total focal loss of an image is computed as the sum of the focal loss over all $\sim$`<!-- -->`{=html}100k anchors, *normalized by the number of anchors assigned to a ground-truth box*.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

We perform the normalization by the number of assigned anchors, not total anchors, since the vast majority of anchors are easy negatives and receive negligible loss values under the focal loss. Finally we note that $\alpha$, the weight assigned to the rare class, also has a stable range, but it interacts with $\gamma$ making it necessary to select the two together (see Tables 1a and 1b). In general $\alpha$ should be decreased slightly as $\gamma$ is increased (for $\gamma = 2$, $\alpha = 0.25$ works best).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

#sc
#ar

<!-- chunk {"id": "body-0043", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

(c) Varying anchor scales and aspects

<!-- chunk {"id": "body-0044", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

(d) FL vs. OHEM baselines (with ResNet-101-FPN)

<!-- chunk {"id": "body-0045", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

(e) Accuracy/speed trade-off RetinaNet (on test-dev)

<!-- chunk {"id": "body-0046", "role": "body", "section": "Initialization", "weight": 1.0} -->

We experiment with ResNet-50-FPN and ResNet-101-FPN backbones. The base ResNet-50 and ResNet-101 models are pre-trained on ImageNet1k; we use the models released. New layers added for FPN are initialized as. All new conv layers except the final one in the RetinaNet subnets are initialized with bias $b = 0$ and a Gaussian weight fill with $\sigma = 0.01$. For the final conv layer of the classification subnet, we set the bias initialization to $b = {- {\log{({{({1 - \pi})}/\pi})}}}$, where $\pi$ specifies that at the start of training every anchor should be labeled as foreground with confidence of $\sim$$\pi$. We use $\pi =.01$ in all experiments, although results are robust to the exact value. As explained in §3.3, this initialization prevents the large number of background anchors from generating a large, destabilizing loss value in the first iteration of training.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Optimization", "weight": 1.0} -->

RetinaNet is trained with stochastic gradient descent (SGD). We use synchronized SGD over 8 GPUs with a total of 16 images per minibatch (2 images per GPU). Unless otherwise specified, all models are trained for 90k iterations with an initial learning rate of 0.01, which is then divided by 10 at 60k and again at 80k iterations. We use horizontal image flipping as the only form of data augmentation unless otherwise noted. Weight decay of 0.0001 and momentum of 0.9 are used. The training loss is the sum the focal loss and the standard smooth $L_{1}$ loss used for box regression. Training time ranges between 10 and 35 hours for the models in Table 1e.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

We present experimental results on the bounding box detection track of the challenging COCO benchmark. For training, we follow common practice and use the COCO trainval35k split (union of 80k images from train and a random 35k subset of images from the 40k image val split). We report lesion and sensitivity studies by evaluating on the minival split (the remaining 5k images from val). For our main results, we report COCO AP on the test-dev split, which has no public labels and requires use of the evaluation server.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Training Dense Detection", "weight": 1.0} -->

We run numerous experiments to analyze the behavior of the loss function for dense detection along with various optimization strategies. For all experiments we use depth 50 or 101 ResNets with a Feature Pyramid Network (FPN) constructed on top. For all ablation studies we use an image scale of 600 pixels for training and testing.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Network Initialization", "weight": 1.0} -->

Our first attempt to train RetinaNet uses standard cross entropy (CE) loss without any modifications to the initialization or learning strategy. This fails quickly, with the network diverging during training. However, simply initializing the last layer of our model such that the prior probability of detecting an object is $\pi =.01$ (see §4.1) enables effective learning. Training RetinaNet with ResNet-50 and this initialization already yields a respectable AP of 30.2 on COCO. Results are insensitive to the exact value of $\pi$ so we use $\pi =.01$ for all experiments.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Balanced Cross Entropy", "weight": 1.0} -->

Our next attempt to improve learning involved using the $\alpha$-balanced CE loss described in §3.1. Results for various $\alpha$ are shown in Table 1a. Setting $\alpha =.75$ gives a gain of 0.9 points AP.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

Results using our proposed focal loss are shown in Table 1b. The focal loss introduces one new hyperparameter, the focusing parameter $\gamma$, that controls the strength of the modulating term. When $\gamma = 0$, our loss is equivalent to the CE loss. As $\gamma$ increases, the shape of the loss changes so that "easy" examples with low loss get further discounted, see Figure 1. FL shows large gains over CE as $\gamma$ is increased. With $\gamma = 2$, FL *yields a 2.9 AP improvement over the $\alpha$-balanced CE loss*.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Focal Loss", "weight": 1.0} -->

For the experiments in Table 1b, for a fair comparison we find the best $\alpha$ for each $\gamma$. We observe that lower $\alpha$'s are selected for higher $\gamma$'s (as easy negatives are down-weighted, less emphasis needs to be placed on the positives). Overall, however, the benefit of changing $\gamma$ is much larger, and indeed the best $\alpha$'s ranged in just \[.25,.75\] (we tested $\alpha \in {\lbrack.01,.999\rbrack}$). We use $\gamma = 2.0$ with $\alpha =.25$ for all experiments but $\alpha =.5$ works nearly as well (.4 AP lower).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Analysis of the Focal Loss", "weight": 1.0} -->

To understand the focal loss better, we analyze the empirical distribution of the loss of a *converged* model. For this, we take take our default ResNet-101 600-pixel model trained with $\gamma = 2$ (which has 36.0 AP). We apply this model to a large number of random images and sample the predicted probability for $\sim$$10^{7}$ negative windows and $\sim$$10^{5}$ positive windows. Next, separately for positives and negatives, we compute FL for these samples, and normalize the loss such that it sums to one. Given the normalized loss, we can sort the loss from lowest to highest and plot its cumulative distribution function (CDF) for both positive and negative samples and for different settings for $\gamma$ (even though model was trained with $\gamma = 2$).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Analysis of the Focal Loss", "weight": 1.0} -->

Cumulative distribution functions for positive and negative samples are shown in Figure 4. If we observe the positive samples, we see that the CDF looks fairly similar for different values of $\gamma$. For example, approximately 20% of the hardest positive samples account for roughly half of the positive loss, as $\gamma$ increases more of the loss gets concentrated in the top 20% of examples, but the effect is minor.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Analysis of the Focal Loss", "weight": 1.0} -->

The effect of $\gamma$ on negative samples is dramatically different. For $\gamma = 0$, the positive and negative CDFs are quite similar. However, as $\gamma$ increases, substantially more weight becomes concentrated on the hard negative examples. In fact, with $\gamma = 2$ (our default setting), the vast majority of the loss comes from a small fraction of samples. As can be seen, FL can effectively discount the effect of easy negatives, focusing all attention on the hard negative examples.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Online Hard Example Mining (OHEM)", "weight": 1.0} -->

proposed to improve training of two-stage detectors by constructing minibatches using high-loss examples. Specifically, in OHEM each example is scored by its loss, non-maximum suppression (nms) is then applied, and a minibatch is constructed with the highest-loss examples. The nms threshold and batch size are tunable parameters. Like the focal loss, OHEM puts more emphasis on misclassified examples, but unlike FL, OHEM completely discards easy examples. We also implement a variant of OHEM used in SSD: after applying nms to all examples, the minibatch is constructed to enforce a 1:3 ratio between positives and negatives to help ensure each minibatch has enough positives.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Online Hard Example Mining (OHEM)", "weight": 1.0} -->

We test both OHEM variants in our setting of one-stage detection which has large class imbalance. Results for the original OHEM strategy and the 'OHEM 1:3' strategy for selected batch sizes and nms thresholds are shown in Table 1d. These results use ResNet-101, our baseline trained with FL achieves 36.0 AP for this setting. In contrast, the best setting for OHEM (no 1:3 ratio, batch size 128, nms of.5) achieves 32.8 AP. This is a gap of 3.2 AP, showing FL is more effective than OHEM for training dense detectors. We note that we tried other parameter setting and variants for OHEM but did not achieve better results.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Hinge Loss", "weight": 1.0} -->

Finally, in early experiments, we attempted to train with the hinge loss on $p_{\text{t}}$, which sets loss to 0 above a certain value of $p_{\text{t}}$. However, this was unstable and we did not manage to obtain meaningful results. Results exploring alternate loss functions are in the appendix.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Anchor Density", "weight": 1.0} -->

One of the most important design factors in a one-stage detection system is how densely it covers the space of possible image boxes. Two-stage detectors can classify boxes at any position, scale, and aspect ratio using a region pooling operation. In contrast, as one-stage detectors use a fixed sampling grid, a popular approach for achieving high coverage of boxes in these approaches is to use multiple 'anchors' at each spatial position to cover boxes of various scales and aspect ratios.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Anchor Density", "weight": 1.0} -->

We sweep over the number of scale and aspect ratio anchors used at each spatial position and each pyramid level in FPN. We consider cases from a single square anchor at each location to 12 anchors per location spanning 4 sub-octave scales ($2^{k/4}$, for $k \leq 3$) and 3 aspect ratios \[0.5, 1, 2\]. Results using ResNet-50 are shown in Table 1c. A surprisingly good AP (30.3) is achieved using just one square anchor. However, the AP can be improved by nearly 4 points (to 34.0) when using 3 scales and 3 aspect ratios per location. We used this setting for all other experiments in this work.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Anchor Density", "weight": 1.0} -->

Finally, we note that increasing beyond 6-9 anchors did not shown further gains. Thus while two-stage systems can classify arbitrary boxes in an image, the saturation of performance w.r.t. density implies the higher potential density of two-stage systems may not offer an advantage.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Speed versus Accuracy", "weight": 1.0} -->

Larger backbone networks yield higher accuracy, but also slower inference speeds. Likewise for input image scale (defined by the shorter image side). We show the impact of these two factors in Table 1e. In Figure 2 we plot the speed/accuracy trade-off curve for RetinaNet and compare it to recent methods using public numbers on COCO test-dev. The plot reveals that RetinaNet, enabled by our focal loss, forms an upper envelope over all existing methods, discounting the low-accuracy regime. RetinaNet with ResNet-101-FPN and a 600 pixel image scale (which we denote by RetinaNet-101-600 for simplicity) matches the accuracy of the recently published ResNet-101-FPN Faster R-CNN, while running in 122 ms per image compared to 172 ms (both measured on an Nvidia M40 GPU). Using larger scales allows RetinaNet to surpass the accuracy of all two-stage approaches, while still being faster. For faster runtimes, there is only one operating point (500 pixel input) at which using ResNet-50-FPN improves over ResNet-101-FPN.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Speed versus Accuracy", "weight": 1.0} -->

Addressing the high frame rate regime will likely require special network design, as, and is beyond the scope of this work. We note that after publication, faster and more accurate results can now be obtained by a variant of Faster R-CNN.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Comparison to State of the Art", "weight": 1.0} -->

We evaluate RetinaNet on the challenging COCO dataset and compare test-dev results to recent state-of-the-art methods including both one-stage and two-stage models. Results are presented in Table 2 for our RetinaNet-101-800 model trained using scale jitter and for 1.5$\times$ longer than the models in Table 1e (giving a 1.3 AP gain). Compared to existing one-stage methods, our approach achieves a healthy 5.9 point AP gap (39.1 *vs*. 33.2) with the closest competitor, DSSD, while also being faster, see Figure 2. Compared to recent two-stage methods, RetinaNet achieves a 2.3 point gap above the top-performing Faster R-CNN model based on Inception-ResNet-v2-TDM. Plugging in ResNeXt-32x8d-101-FPN as the RetinaNet backbone further improves results another 1.7 AP, surpassing 40 AP on COCO.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we identify class imbalance as the primary obstacle preventing one-stage object detectors from surpassing top-performing, two-stage methods. To address this, we propose the *focal loss* which applies a modulating term to the cross entropy loss in order to focus learning on hard negative examples. Our approach is simple and highly effective. We demonstrate its efficacy by designing a fully convolutional one-stage detector and report extensive experimental analysis showing that it achieves state-of-the-art accuracy and speed. Source code is available at
