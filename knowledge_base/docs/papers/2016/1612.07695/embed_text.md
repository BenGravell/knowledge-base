## Introduction

Current advances in the field of computer vision have made clear that visual perception is going to play a key role in the development of self-driving cars. This is mostly due to the deep learning revolution which begun with the introduction of AlexNet in 2012. Since then, the accuracy of new approaches has been increasing at a vertiginous rate. Causes of this are the existence of more data, increased computation power and algorithmic developments. The current trend is to create deeper networks with as many layers as possible.

While performance is already extremely high, when dealing with real-world applications, running times becomes important. New hardware accelerators as well as compression, reduced precision and distillation methods have been exploited to speed up current networks.

Figure 1: Our goal: Solving street classification, vehicle detection and road segmentation in one forward pass.

In this paper we take an alternative approach and design a network architecture that can very efficiently perform classification, detection and semantic segmentation simultaneously. This is done by incorporating all three task into a unified encoder-decoder architecture. We name our approach MultiNet.

The encoder is a deep CNN, producing rich features that are shared among all task. Those features are then utilized by task-specific decoders, which produce their outputs in real-time. In particular, the detection decoder combines the fast regression design introduced in Yolo with the size-adjusting ROI-align of Faster-RCNN and Mask-RCNN, achieving a better speed-accuracy ratio.

We demonstrate the effectiveness of our approach in the challenging KITTI benchmark and show state-of-the-art performance in road segmentation. Importantly, our ROI-align implementation can significantly improve detection performance without requiring an explicit proposal generation network. This gives our decoder a significant speed advantage compared to Faster-RCNN. Our approach is able to benefit from sharing computations, allowing us to perform inference in less than 45 ms for all tasks.

All our code, training scripts and weights, required to reproduce our results, are released on Github.

Figure 2: MultiNet architecture.

## Related Work

In this section we review current approaches to the tasks that MultiNet tackles, i.e., detection, classification and semantic segmentation. We focus our attention on deep learning based approaches.

### Classification

After the development of AlexNet, most modern approaches to image classification utilize deep learning. Residual networks constitute the state-of-the-art, as they allow to train very deep networks without problems of vanishing or exploding gradients. In the context of road classification, deep neural networks are also widely employed. Sensor fusion has also been exploited in this context. In this paper we use classification to guide other semantic tasks, i.e., segmentation and detection.

### Detection

Traditional deep learning approaches to object detection follow a two step process, where region proposals are first generated and then scored using a convolutional network. Additional performance improvements can be gained by using convolutional neural networks (CNNs) for the proposal generation step or by reasoning in 3D. Recently, several methods have proposed to use a single deep network that is trainable end-to-end to directly perform detection. Their main advantage over proposal-based methods is that they are much faster at both training and inference time, and thus more suitable for real-time detection applications. However, so far they lag far behind in performance. In this paper we propose an end-to-end trainable detector which reduces significantly the performance gap. We argue that the main advantage of proposal-based methods is their ability to have size-adjustable features. This inspired our ROI pooling implementation.

### Segmentation

Inspired by the successes of deep learning, CNN-based classifiers were adapted to the task of semantic segmentation. Early approaches used the inherent efficiency of CNNs to implement implicit sliding-window. FCN were proposed to model semantic segmentation using a deep learning pipeline that is trainable end-to-end. Transposed convolutions are utilized to upsample low resolution features. A variety of deeper flavors of FCNs have been proposed since. Very good results are archived by combining FCN with conditional random fields (CRFs). showed that mean-field inference in the CRF can be cast as a recurrent net allowing end-to-end training. Dilated convolutions were introduced in to augment the receptive field size without losing resolution. The aforementioned techniques in conjunction with residual networks are currently the state-of-the-art.

### Multi-Task Learning

Multi-task learning techniques aim at learning better representations by exploiting many tasks. Several approaches have been proposed in the context of CNNs. An important application for multi-task learning is face recognition.

Learning semantic segmentation in order to perform detection or instance segmentation has been studied. In those systems, the main goal is to perform an instance level task. Semantic annotation is only viewed as an intermediate result. Systems like and many more design one system which can be fine-tuned to perform tasks like classification, detection or semantic segmentation. In this kind of approaches, a different set of parameters is learned for each task. Thus, joint inference is not possible in this models. The system described in is closest to our model. However this system relies on existing object detectors and does not fully leverage the rich features learned during segmentation for both tasks. To the best of our knowledge our system is the first one proposed which is able to do this.

## MultiNet for Joint Semantic Reasoning

In this paper we propose an efficient and effective feed-forward architecture, which we call MultiNet, to jointly reason about semantic segmentation, image classification and object detection. Our approach shares a common encoder over the three tasks and has three branches, each implementing a decoder for a given task. We refer the reader to Fig. 2 for an illustration of our architecture. MultiNet can be trained end-to-end and joint inference over all tasks can be done in less than 45ms. We start our discussion by introducing our joint encoder, followed by the task-specific decoders.

### Encoder

The task of the encoder is to process the image and extract rich abstract features that contain all necessary information to perform accurate segmentation, detection and image classification. The encoder consists of the convolutional and pooling layers of a classification network. The weights of the encoder are initialized using the weights pre-trained on ImageNet Classification Data. As encoder any modern classification network can be utilized.

We perform experiments using versions of and ResNet architectures. Our first VGG encoder uses all convolutional and pooling layers of. but discards the fully-connected softmax layers. We call this version *VGG-pool5*, as pool5 is the last layer used from. The second implementation only discards the final fully-connected softmax layer. We call this architecture *VGG-fc7*, as fc7 is the last layer used from. VGG-fc7 utilizes two fully-connected layers from VGG, namely *fc6* and *fc7*. We replace those layers with equal $1 \times 1$ convolutions as discussed in. This trick allows the encoder to process images with arbitrary input size. In particular we are not bound to the original VGG input of $224 \times 224$, which would be to small to perform perception in street scenes.

For ResNet we implement the $50$ and $101$ layer Version of the Network. As encoder we utilize all layers apart from the layers fully-connected softmax.

Figure 3: Visualization of our detection encoding. Blue grid: cells, Red cells: cells with positive confidence label. Transparent Cells: cells with negative confidence label. Grey cells: cells in don’t care area. Green boxes: ground truth boxes.

### Classification Decoder

We implement two classification decoders. One version is a vanilla fully-connected layer with softmax activation. This encoder is used in conjunction with an input size of $224 \times 224$. Thus, the overall network is equal to the original VGG or ResNet respectively, when used with the corresponding encoder. The purpose of this encoder is to serve as high quality baseline to show the effectiveness of our scene classification approach. This first classification encoder cannot be used for joint inference with segmentation and detection. Both approaches require a larger input size. Increasing the input size on this classification encoder however, yields into an unreasonable high amount of parameters for the final layer.

The second classification decoder is designed to take advantage of the high resolution features our encoder generates. In typical image classification tasks (e.g. ) the input features one object, usually centred prominently in the image. For this kind of task it is reasonable to use a very small input size. Street scenes on the other hand contain a large amount of smaller scale objects. We argue that it is vital to use high-resolution input in order to utilize features those objects provide. By increasing the input size of our image to $1248 \times 348$, we effectively apply our feature generator to each spatial location of the image. The result is a grid of $39 \times 12$ features, each corresponding to a spatial region of size $32 \times 32$ pixels. In order to utilize this features, we first apply a $1 \times 1$ convolution with $30$ channels. This layer serves as *BottleNeck*. The main purpose is to greatly reduce dimensionality.

### Detection Decoder

The detection decoder is designed to be a proposal free approach similar to ReInspect, Yolo and Overfeat. By omitting and artificial proposal generator step much faster inference can be obtained. This is crucial towards our goal of building a real-time capable detection system.

Proposal based detection systems have a crucial advantage over non-proposal based. They internally rescale the rich features utilized for detection. This makes the CNN internally invariant to scale. This is a crucial feature, as CNN are naturally not able to generalize over different scales. We argue, that the scale invariance is the main advantage of proposal based systems.

Our detection decoder tries to close the marry the good detection performance of proposal based detection systems with the fast speed of non-proposal based systems. To archive this, we include a rescaling layer inside the decoder. The rescaling layer consists of RoI align and provides the main advantage of proposal based systems. Unlike proposal based systems, no non-differential operations are done and the rescaling can be computed very efficiently.

The first step of our decoder is to produce a rough estimate of the bounding boxes. Towards this goal, we first pass the encoded features through a $1 \times 1$ convolutional layer with 500 filters, producing a tensor of shape $39 \times 12 \times 500$. Those features serve as *bottleneck*. This tensor is processed with another $1 \times 1$ convolutional layer which outputs 6 channels at resolution $39 \times 12$. We call this tensor *prediction*, the values of the tensor have a semantic meaning. The first two channels of this tensor form a coarse segmentation of the image. Their values represent the confidence that an object of interest is present at that particular location in the $39 \times 12$ grid. The last four channels represent the coordinates of a bounding box in the area around that cell. Fig. 3 shows an image with its cells.

Those prediction are then utilized to introduce scale invariance. A rescaling approach, similar to the ones found in proposal based systems is applied on the initial coarse prediction. The rescaling layer follows the RoI align strategy of. It uses however the prediction of each cell to produce a RoI align. This makes the operation differentiable. Thus it can be implemented insight the CNN pooling. The result is an end-to-end trainable system which is faster. The features pooled by the RoI align are concatenated with the initial prediction and used to produce a more accurate prediction. The second prediction is modeled as offset, its output is added to the initial prediction.

### Segmentation Decoder

The segmentation decoder follows the main ideas of the FCN architecture. Given the features produced by the encoder, we produce a low resolution segmentation of size $39 \times 12$ using a $1 \times 1$ convolutional layer. This output is then upsampled using three transposed convolution layers. Skip connections are utilized to extract high resolution features from the lower layers. Those features are first processed by a $1 \times 1$ convolution layer and then added to the partially upsampled results.

## Training Details

In this section we describe the loss functions we employ as well as other details of our training procedure including initialization.

### MultiNet Training Strategy

MultiNet training follows a fine-tuning approach. First the encoder network is trained to perform classification on the ILSVRC2012 data. In practice, this step is omitted. Instead we initialize the weights of all layers of the encoder with weights published by the authors whose network architecture we are using.

In a second step, the final fully connected layers are removed and replaced by our decoders. Then the network is trained end-to-end using KITTI data. Thus MultiNet training follows a classic fine-tuning pipeline.

Our joint training implementation computes the forward passes for examples corresponding to each of the three tasks independently. The gradients are only added during the back-propagation steps. This has the practical advantage that we are able to use different training parameters for each decoder. Having this degree of freedom is an important feature of our joint training implementation. The classification task for example requires a relative large batch size and more aggressive data-augmentation than the segmentation task to perform well.

### Loss function

Classification and segmentation are trained using a softmax cross-entropy loss function.

For the detection, the final prediction is a grid of $12 \times 39$ cells. Each cell gets assigned a confidence label as well as a box label. The box label encodes the coordinates of the box and is parametrized relative to the position of a cell. A cell $c$ gets assigned a positive confidence label if and only if it intersects with at least one bounding box. If this is the case the cell also gets assigned to predict the coordinates of the box it intersects with. If multiple boxes intersect with a cell, the box whose centre is closest to the centre of $c$ is chosen. Note that one box can be predicted by multiple cells.

If a box $b$ is assigned to a cell $c$ the following values are stored in c:

where $x_{b}$, $y_{b}$ and $x_{c}$ $y_{c}$ correspond to the center coordinates of $b$ and $c$ and $w$ and $h$ denote width and hight. Note, that $w_{c}$ and $h_{c}$ are always $32$, as the cells of our model have a fixed width and height. We use L1 as our loss

where $\hat{c}$ is the prediction of a cell and $c$ its ground-truth, and $c_{p}$ denotes whether a positive label has been assigned to a cell. The $\deltac_{p}$ term ensures that the regression loss is zero if no object is present. We train the confidence labels using cross-entropy loss. The loss per cell is given as the weighted sum over the confidence and the regression loss. The loss per image is the mean over the losses of all cells. The KITTI Dataset also contains 'don't Care areas'. Those areas are handled by multiplying the loss of the corresponding cells with zero. We note, that our label representation is much simpler than Faster-RCNN or ReInspect. This is an additional feature of our detection system. The loss for MultiNet is given as the sum of the losses for segmentation, detection and classification.

Figure 4: Visualization of the segmentation output. Top row: Soft segmentation output as red blue plot. The intensity of the plot reflects the confidence. Bottom row hard class labels.

The loss for the joint training is given as the sum of the losses for segmentation, detection and classification.

### Initialization

The weights of the encoder are initialized using weights trained on ImageNet data. The weights of the detection and classification decoder are initialized using the initialization scheme of. The transposed convolution layers of the segmentation decoder are initialized to perform bilinear upsampling. The skip connections of the segmentation decoder are initialized to very small weights. Both these modifications greatly improve segmentation performance.

### Optimizer and regularization

We use the Adam optimizer with a learning rate of $10^{- 5}$ to train our MultiNet. A weight decay of $5 \cdot 10^{- 4}$ is applied to all layers and dropout with probability $0.5$ is applied to the $3 \times 3$ convolution of the classification and all $1 \times 1$ convolutions of the detection decoder.

Standard data augmentation are applied to increase the amount of effective available training data. We augment colour features by applying random brightness and random contrast. Spatial feature are distorted by applying random flip, random resize and random crop.

## Experimental Results

In this section we perform our experimental evaluation on the challenging KITTI dataset.

Table 1: Summary of the URBAN ROAD scores on the public KITTIRoad Detection Leaderboard.

### Dataset

We evaluate MultiNet on the KITTI Vision Benchmark Suite. The Benchmark contains images showing a variety of street situations captured from a moving platform driving around the city of Karlsruhe. In addition to the raw data, KITTI comes with a number of labels for different tasks relevant to autonomous driving. We use the road benchmark of to evaluate the performance of our semantic segmentation decoder and the object detection benchmark for the detection decoder. We exploit the automatically generated labels of, which provide us with road labels generated by combining GPS information with open-street map data.

Detection performance is measured using the average precision score. For evaluation, objects are divided into three categories: easy, moderate and hard to detect. The segmentation performance is measured using the MaxF1 score. In addition, the average precision score is given for reference. Classification performance is evaluated by computing the mean accuracy, precision and recall.

### Experimental evaluation

The section is structured as fellows. We first evaluate the performance of the three decoders individually. To do this we fine-tune the encoder using just one of the three losses segmentation, detection and classification and compare their performance with a variety of baseline. In the second part we compare joint training of all three decoders with individual inference and show, that the performance of joint training can keep up with the performance of individual inferences. Overall we show, that our approach is competitive with individual inference. This makes our approach very relevant. Joint training has many advantages in robotics application, such as a fast inference time.

Table 2: Performance of the segmentation decoder.

VGG no RIO pool

Table 3: Performance of our detection decoder.

### Segmentation

The segmentation decoder encoder is trained using the four different encoders discussed in Section 3.1. The scores, computed on a halt-out validation set is reported in Table 1.

To compare my approach against the state-of-the-art we trained a segmentation network with VGG-fc7 encoder on the whole training set and submitted the results to the KITTI road leaderboard. At submission time my approach archived first place in the benchmark. Recently my approach was overtaken by newer submissions. All non-anonymous submissions to the benchmark are shown in Table 2.

Qualitative results are shown in Fig. 4 both as red blue plot showing the confidence level at each pixel as well as a hard prediction using a threshold of $0.5$.

Figure 5: Visualization of the detection output. With and without non-maximal suppression applied.

Table 4: Inference speed of our segmentation.

Table 5: Inference speed of our detection decoder.

### Detection

The detection decoder is trained and evaluated on the data provided by the KITTI object benchmark. We train the detection decoder on a VGG and ResNet decoder and evaluate on a validation set. Table 3 shows the results of our decoder compared to a Faster-RCNN baseline, evaluated on the same validation set. The results show that our rescaling approach is very efficient. Training the detection decoder with rescaling is only marginality slower then training it without. However it offers a significant improvement in detection performance. Overall our approach archives is speed-up over faster-rcnn of almost a factor 2 and outperforms its detection accuracy. Qualitative results of the detection decoder can be seen in 5.

All in all my results indicate that utilizing a rescaling layer in order to archive scale invariance is a good idea. A rescaling layer might be the key to closing the gap between proposal and non-proposal based approaches.

Our detection decoder is trained and evaluated on the data provided by the KITTI object benchmark. We train our detection decoder on a VGG and ResNet decoder and evaluate on a validation set. Table 3 shows the results of our decoder compared to a Faster-RCNN baseline, evaluated on the same validation set. We report the inference speed in Table 5. We observe that our approach archives is speed-up over faster-rcnn of almost a factor 2 and outperforms its detection accuracy. This makes our decoder particularly suitable for real-time applications. Qualitative results of our detection decoder can be seen in 5.

VGG pool5 [our]

Table 6: Classification performance of our decoder compared to baseline classification.

Figure 6: Visualization of the MultiNet output.

### Classification

The classification data is not part of the official KITTI Benchmark. To evaluate the classification decoder we first need to create our own dataset. This is done using the method descriped in. To obtain a meaningful task all images of one scene ether fully in the train or fully in the validation set. This is important as the images of one scene are usually visually very similar.

We use a vanilla ResNet and VGG classification approach as baseline and compare this to a VGG and ResNet approach with my classification decoder. The differences between those two approaches are discussed in more detail in Section 3.2. The results are reported in Table 6 and Table 7. Our customised classification decoder clearly outperforms vanilla decoders, showing the effectiveness of my approach.

VGG pool5 [our]

Table 7: Inference speed of our classification.

Table 8: Results of joint training

Table 9: Speed of joint inference.

### MultiNet

We ran a series of experiments comparing VGG and ResNet as encoder. Table 8 and Table 9 compare performance of VGG and ResNet. We observe, that both ResNet-based encoders are able to outperform VGG slightly. There is however a trade-off, as the VGG encoder is faster.

The speed gap between VGG pool5 and is much larger when performing joint inference compared to the individual task. This can be explained by the fact that ResNet computes features with $2048$ channels, while VGG features have only $512$ channels. Thus, computing the fist layer of each decoder is significantly more expensive.

Overall we conclude, that MultiNet using a VGG decoder offers a very good trade-off between performance and speed.

## Conclusion

In this paper we have developed a unified deep architecture which is able to jointly reason about classification, detection and semantic segmentation. Our approach is very simple, can be trained end-to-end and performs extremely well in the challenging KITTI dataset, outperforming the state-of-the-art in the road segmentation task. Our approach is also very efficient, taking $42.48\ \frac{ms}{}$ to perform all tasks. In the future we plan to exploit compression methods in order to further reduce the computational bottleneck and energy consumption of MutiNet.
