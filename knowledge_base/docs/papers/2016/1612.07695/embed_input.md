<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MultiNet: Real-time Joint Semantic Reasoning for Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While most approaches to semantic reasoning have focused on improving performance, in this paper we argue that computational times are very important in order to enable real time applications such as autonomous driving. Towards this goal, we present an approach to joint classification, detection and semantic segmentation via a unified architecture where the encoder is shared amongst the three tasks. Our approach is very simple, can be trained end-to-end and performs extremely well in the challenging KITTI dataset, outperforming the state-of-the-art in the road segmentation task. Our approach is also very efficient, taking less than 100 ms to perform all tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current advances in the field of computer vision have made clear that visual perception is going to play a key role in the development of self-driving cars. This is mostly due to the deep learning revolution which begun with the introduction of AlexNet in 2012. Since then, the accuracy of new approaches has been increasing at a vertiginous rate. Causes of this are the existence of more data, increased computation power and algorithmic developments. The current trend is to create deeper networks with as many layers as possible.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While performance is already extremely high, when dealing with real-world applications, running times becomes important. New hardware accelerators as well as compression, reduced precision and distillation methods have been exploited to speed up current networks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we take an alternative approach and design a network architecture that can very efficiently perform classification, detection and semantic segmentation simultaneously. This is done by incorporating all three task into a unified encoder-decoder architecture. We name our approach MultiNet.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The encoder is a deep CNN, producing rich features that are shared among all task. Those features are then utilized by task-specific decoders, which produce their outputs in real-time. In particular, the detection decoder combines the fast regression design introduced in Yolo with the size-adjusting ROI-align of Faster-RCNN and Mask-RCNN, achieving a better speed-accuracy ratio.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the effectiveness of our approach in the challenging KITTI benchmark and show state-of-the-art performance in road segmentation. Importantly, our ROI-align implementation can significantly improve detection performance without requiring an explicit proposal generation network. This gives our decoder a significant speed advantage compared to Faster-RCNN. Our approach is able to benefit from sharing computations, allowing us to perform inference in less than 45 ms for all tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

All our code, training scripts and weights, required to reproduce our results, are released on Github.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Classification", "weight": 1.0} -->

After the development of AlexNet, most modern approaches to image classification utilize deep learning. Residual networks constitute the state-of-the-art, as they allow to train very deep networks without problems of vanishing or exploding gradients. In the context of road classification, deep neural networks are also widely employed. Sensor fusion has also been exploited in this context. In this paper we use classification to guide other semantic tasks, i.e., segmentation and detection.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Detection", "weight": 1.0} -->

Traditional deep learning approaches to object detection follow a two step process, where region proposals are first generated and then scored using a convolutional network. Additional performance improvements can be gained by using convolutional neural networks (CNNs) for the proposal generation step or by reasoning in 3D. Recently, several methods have proposed to use a single deep network that is trainable end-to-end to directly perform detection. Their main advantage over proposal-based methods is that they are much faster at both training and inference time, and thus more suitable for real-time detection applications. However, so far they lag far behind in performance. In this paper we propose an end-to-end trainable detector which reduces significantly the performance gap. We argue that the main advantage of proposal-based methods is their ability to have size-adjustable features. This inspired our ROI pooling implementation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Segmentation", "weight": 1.0} -->

Inspired by the successes of deep learning, CNN-based classifiers were adapted to the task of semantic segmentation. Early approaches used the inherent efficiency of CNNs to implement implicit sliding-window. FCN were proposed to model semantic segmentation using a deep learning pipeline that is trainable end-to-end. Transposed convolutions are utilized to upsample low resolution features. A variety of deeper flavors of FCNs have been proposed since. Very good results are archived by combining FCN with conditional random fields (CRFs). showed that mean-field inference in the CRF can be cast as a recurrent net allowing end-to-end training. Dilated convolutions were introduced in to augment the receptive field size without losing resolution. The aforementioned techniques in conjunction with residual networks are currently the state-of-the-art.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Multi-Task Learning", "weight": 1.0} -->

Multi-task learning techniques aim at learning better representations by exploiting many tasks. Several approaches have been proposed in the context of CNNs. An important application for multi-task learning is face recognition.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Multi-Task Learning", "weight": 1.0} -->

Learning semantic segmentation in order to perform detection or instance segmentation has been studied. In those systems, the main goal is to perform an instance level task. Semantic annotation is only viewed as an intermediate result. Systems like and many more design one system which can be fine-tuned to perform tasks like classification, detection or semantic segmentation. In this kind of approaches, a different set of parameters is learned for each task. Thus, joint inference is not possible in this models. The system described in is closest to our model. However this system relies on existing object detectors and does not fully leverage the rich features learned during segmentation for both tasks. To the best of our knowledge our system is the first one proposed which is able to do this.

<!-- chunk {"id": "body-0014", "role": "body", "section": "MultiNet for Joint Semantic Reasoning", "weight": 1.0} -->

In this paper we propose an efficient and effective feed-forward architecture, which we call MultiNet, to jointly reason about semantic segmentation, image classification and object detection. Our approach shares a common encoder over the three tasks and has three branches, each implementing a decoder for a given task. We refer the reader to Fig. 2 for an illustration of our architecture. MultiNet can be trained end-to-end and joint inference over all tasks can be done in less than 45ms. We start our discussion by introducing our joint encoder, followed by the task-specific decoders.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Encoder", "weight": 1.0} -->

The task of the encoder is to process the image and extract rich abstract features that contain all necessary information to perform accurate segmentation, detection and image classification. The encoder consists of the convolutional and pooling layers of a classification network. The weights of the encoder are initialized using the weights pre-trained on ImageNet Classification Data. As encoder any modern classification network can be utilized.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Encoder", "weight": 1.0} -->

We perform experiments using versions of and ResNet architectures. Our first VGG encoder uses all convolutional and pooling layers of. but discards the fully-connected softmax layers. We call this version *VGG-pool5*, as pool5 is the last layer used. The second implementation only discards the final fully-connected softmax layer. We call this architecture *VGG-fc7*, as fc7 is the last layer used. VGG-fc7 utilizes two fully-connected layers from VGG, namely *fc6* and *fc7*. We replace those layers with equal $1 \times 1$ convolutions as discussed. This trick allows the encoder to process images with arbitrary input size. In particular we are not bound to the original VGG input of $224 \times 224$, which would be to small to perform perception in street scenes.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Encoder", "weight": 1.0} -->

For ResNet we implement the $50$ and $101$ layer Version of the Network. As encoder we utilize all layers apart from the layers fully-connected softmax.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Classification Decoder", "weight": 1.0} -->

We implement two classification decoders. One version is a vanilla fully-connected layer with softmax activation. This encoder is used in conjunction with an input size of $224 \times 224$. Thus, the overall network is equal to the original VGG or ResNet respectively, when used with the corresponding encoder. The purpose of this encoder is to serve as high quality baseline to show the effectiveness of our scene classification approach. This first classification encoder cannot be used for joint inference with segmentation and detection. Both approaches require a larger input size. Increasing the input size on this classification encoder however, yields into an unreasonable high amount of parameters for the final layer.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Classification Decoder", "weight": 1.0} -->

The second classification decoder is designed to take advantage of the high resolution features our encoder generates. In typical image classification tasks (e.g. ) the input features one object, usually centred prominently in the image. For this kind of task it is reasonable to use a very small input size. Street scenes on the other hand contain a large amount of smaller scale objects. We argue that it is vital to use high-resolution input in order to utilize features those objects provide. By increasing the input size of our image to $1248 \times 348$, we effectively apply our feature generator to each spatial location of the image. The result is a grid of $39 \times 12$ features, each corresponding to a spatial region of size $32 \times 32$ pixels. In order to utilize this features, we first apply a $1 \times 1$ convolution with $30$ channels. This layer serves as *BottleNeck*. The main purpose is to greatly reduce dimensionality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Detection Decoder", "weight": 1.0} -->

The detection decoder is designed to be a proposal free approach similar to ReInspect, Yolo and Overfeat. By omitting and artificial proposal generator step much faster inference can be obtained. This is crucial towards our goal of building a real-time capable detection system.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Detection Decoder", "weight": 1.0} -->

Proposal based detection systems have a crucial advantage over non-proposal based. They internally rescale the rich features utilized for detection. This makes the CNN internally invariant to scale. This is a crucial feature, as CNN are naturally not able to generalize over different scales. We argue, that the scale invariance is the main advantage of proposal based systems.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Detection Decoder", "weight": 1.0} -->

Our detection decoder tries to close the marry the good detection performance of proposal based detection systems with the fast speed of non-proposal based systems. To archive this, we include a rescaling layer inside the decoder. The rescaling layer consists of RoI align and provides the main advantage of proposal based systems. Unlike proposal based systems, no non-differential operations are done and the rescaling can be computed very efficiently.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Detection Decoder", "weight": 1.0} -->

The first step of our decoder is to produce a rough estimate of the bounding boxes. Towards this goal, we first pass the encoded features through a $1 \times 1$ convolutional layer with 500 filters, producing a tensor of shape $39 \times 12 \times 500$. Those features serve as *bottleneck*. This tensor is processed with another $1 \times 1$ convolutional layer which outputs 6 channels at resolution $39 \times 12$. We call this tensor *prediction*, the values of the tensor have a semantic meaning. The first two channels of this tensor form a coarse segmentation of the image. Their values represent the confidence that an object of interest is present at that particular location in the $39 \times 12$ grid. The last four channels represent the coordinates of a bounding box in the area around that cell. Fig. 3 shows an image with its cells.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Detection Decoder", "weight": 1.0} -->

Those prediction are then utilized to introduce scale invariance. A rescaling approach, similar to the ones found in proposal based systems is applied on the initial coarse prediction. The rescaling layer follows the RoI align strategy of. It uses however the prediction of each cell to produce a RoI align. This makes the operation differentiable. Thus it can be implemented insight the CNN pooling. The result is an end-to-end trainable system which is faster. The features pooled by the RoI align are concatenated with the initial prediction and used to produce a more accurate prediction. The second prediction is modeled as offset, its output is added to the initial prediction.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Segmentation Decoder", "weight": 1.0} -->

The segmentation decoder follows the main ideas of the FCN architecture. Given the features produced by the encoder, we produce a low resolution segmentation of size $39 \times 12$ using a $1 \times 1$ convolutional layer. This output is then upsampled using three transposed convolution layers. Skip connections are utilized to extract high resolution features from the lower layers. Those features are first processed by a $1 \times 1$ convolution layer and then added to the partially upsampled results.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training Details", "weight": 1.0} -->

In this section we describe the loss functions we employ as well as other details of our training procedure including initialization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "MultiNet Training Strategy", "weight": 1.0} -->

MultiNet training follows a fine-tuning approach. First the encoder network is trained to perform classification on the ILSVRC2012 data. In practice, this step is omitted. Instead we initialize the weights of all layers of the encoder with weights published by the authors whose network architecture we are using.

<!-- chunk {"id": "body-0028", "role": "body", "section": "MultiNet Training Strategy", "weight": 1.0} -->

In a second step, the final fully connected layers are removed and replaced by our decoders. Then the network is trained end-to-end using KITTI data. Thus MultiNet training follows a classic fine-tuning pipeline.

<!-- chunk {"id": "body-0029", "role": "body", "section": "MultiNet Training Strategy", "weight": 1.0} -->

Our joint training implementation computes the forward passes for examples corresponding to each of the three tasks independently. The gradients are only added during the back-propagation steps. This has the practical advantage that we are able to use different training parameters for each decoder. Having this degree of freedom is an important feature of our joint training implementation. The classification task for example requires a relative large batch size and more aggressive data-augmentation than the segmentation task to perform well.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Loss function", "weight": 1.0} -->

Classification and segmentation are trained using a softmax cross-entropy loss function.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Loss function", "weight": 1.0} -->

For the detection, the final prediction is a grid of $12 \times 39$ cells. Each cell gets assigned a confidence label as well as a box label. The box label encodes the coordinates of the box and is parametrized relative to the position of a cell. A cell $c$ gets assigned a positive confidence label if and only if it intersects with at least one bounding box. If this is the case the cell also gets assigned to predict the coordinates of the box it intersects. If multiple boxes intersect with a cell, the box whose centre is closest to the centre of $c$ is chosen. Note that one box can be predicted by multiple cells.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Loss function", "weight": 1.0} -->

where $x_{b}$, $y_{b}$ and $x_{c}$ $y_{c}$ correspond to the center coordinates of $b$ and $c$ and $w$ and $h$ denote width and hight. Note, that $w_{c}$ and $h_{c}$ are always $32$, as the cells of our model have a fixed width and height. We use L1 as our loss

<!-- chunk {"id": "body-0033", "role": "body", "section": "Loss function", "weight": 1.0} -->

where $\hat{c}$ is the prediction of a cell and $c$ its ground-truth, and $c_{p}$ denotes whether a positive label has been assigned to a cell. The $\deltac_{p}$ term ensures that the regression loss is zero if no object is present. We train the confidence labels using cross-entropy loss. The loss per cell is given as the weighted sum over the confidence and the regression loss. The loss per image is the mean over the losses of all cells. The KITTI Dataset also contains 'don't Care areas'. Those areas are handled by multiplying the loss of the corresponding cells with zero. We note, that our label representation is much simpler than Faster-RCNN or ReInspect. This is an additional feature of our detection system. The loss for MultiNet is given as the sum of the losses for segmentation, detection and classification.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Loss function", "weight": 1.0} -->

The loss for the joint training is given as the sum of the losses for segmentation, detection and classification.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Initialization", "weight": 1.0} -->

The weights of the encoder are initialized using weights trained on ImageNet data. The weights of the detection and classification decoder are initialized using the initialization scheme of. The transposed convolution layers of the segmentation decoder are initialized to perform bilinear upsampling. The skip connections of the segmentation decoder are initialized to very small weights. Both these modifications greatly improve segmentation performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Optimizer and regularization", "weight": 1.0} -->

We use the Adam optimizer with a learning rate of $10^{- 5}$ to train our MultiNet. A weight decay of $5 \cdot 10^{- 4}$ is applied to all layers and dropout with probability $0.5$ is applied to the $3 \times 3$ convolution of the classification and all $1 \times 1$ convolutions of the detection decoder.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Optimizer and regularization", "weight": 1.0} -->

Standard data augmentation are applied to increase the amount of effective available training data. We augment colour features by applying random brightness and random contrast. Spatial feature are distorted by applying random flip, random resize and random crop.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section we perform our experimental evaluation on the challenging KITTI dataset.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dataset", "weight": 1.0} -->

We evaluate MultiNet on the KITTI Vision Benchmark Suite. The Benchmark contains images showing a variety of street situations captured from a moving platform driving around the city of Karlsruhe. In addition to the raw data, KITTI comes with a number of labels for different tasks relevant to autonomous driving. We use the road benchmark of to evaluate the performance of our semantic segmentation decoder and the object detection benchmark for the detection decoder. We exploit the automatically generated labels of, which provide us with road labels generated by combining GPS information with open-street map data.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Dataset", "weight": 1.0} -->

Detection performance is measured using the average precision score. For evaluation, objects are divided into three categories: easy, moderate and hard to detect. The segmentation performance is measured using the MaxF1 score. In addition, the average precision score is given for reference. Classification performance is evaluated by computing the mean accuracy, precision and recall.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental evaluation", "weight": 1.0} -->

The section is structured as fellows. We first evaluate the performance of the three decoders individually. To do this we fine-tune the encoder using just one of the three losses segmentation, detection and classification and compare their performance with a variety of baseline. In the second part we compare joint training of all three decoders with individual inference and show, that the performance of joint training can keep up with the performance of individual inferences. Overall we show, that our approach is competitive with individual inference. This makes our approach very relevant. Joint training has many advantages in robotics application, such as a fast inference time.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Segmentation", "weight": 1.0} -->

The segmentation decoder encoder is trained using the four different encoders discussed in Section 3.1. The scores, computed on a halt-out validation set is reported in Table 1.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Segmentation", "weight": 1.0} -->

To compare my approach against the state-of-the-art we trained a segmentation network with VGG-fc7 encoder on the whole training set and submitted the results to the KITTI road leaderboard. At submission time my approach archived first place in the benchmark. Recently my approach was overtaken by newer submissions. All non-anonymous submissions to the benchmark are shown in Table 2.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Segmentation", "weight": 1.0} -->

Qualitative results are shown in Fig. 4 both as red blue plot showing the confidence level at each pixel as well as a hard prediction using a threshold of $0.5$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Detection", "weight": 1.0} -->

The detection decoder is trained and evaluated on the data provided by the KITTI object benchmark. We train the detection decoder on a VGG and ResNet decoder and evaluate on a validation set. Table 3 shows the results of our decoder compared to a Faster-RCNN baseline, evaluated on the same validation set. The results show that our rescaling approach is very efficient. Training the detection decoder with rescaling is only marginality slower then training it without. However it offers a significant improvement in detection performance. Overall our approach archives is speed-up over faster-rcnn of almost a factor 2 and outperforms its detection accuracy. Qualitative results of the detection decoder can be seen in 5.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Detection", "weight": 1.0} -->

All in all my results indicate that utilizing a rescaling layer in order to archive scale invariance is a good idea. A rescaling layer might be the key to closing the gap between proposal and non-proposal based approaches.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Detection", "weight": 1.0} -->

Our detection decoder is trained and evaluated on the data provided by the KITTI object benchmark. We train our detection decoder on a VGG and ResNet decoder and evaluate on a validation set. Table 3 shows the results of our decoder compared to a Faster-RCNN baseline, evaluated on the same validation set. We report the inference speed in Table 5. We observe that our approach archives is speed-up over faster-rcnn of almost a factor 2 and outperforms its detection accuracy. This makes our decoder particularly suitable for real-time applications. Qualitative results of our detection decoder can be seen in 5.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Classification", "weight": 1.0} -->

The classification data is not part of the official KITTI Benchmark. To evaluate the classification decoder we first need to create our own dataset. This is done using the method descriped. To obtain a meaningful task all images of one scene ether fully in the train or fully in the validation set. This is important as the images of one scene are usually visually very similar.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Classification", "weight": 1.0} -->

We use a vanilla ResNet and VGG classification approach as baseline and compare this to a VGG and ResNet approach with my classification decoder. The differences between those two approaches are discussed in more detail in Section 3.2. The results are reported in Table 6 and Table 7. Our customised classification decoder clearly outperforms vanilla decoders, showing the effectiveness of my approach.

<!-- chunk {"id": "body-0050", "role": "body", "section": "MultiNet", "weight": 1.0} -->

We ran a series of experiments comparing VGG and ResNet as encoder. Table 8 and Table 9 compare performance of VGG and ResNet. We observe, that both ResNet-based encoders are able to outperform VGG slightly. There is however a trade-off, as the VGG encoder is faster.

<!-- chunk {"id": "body-0051", "role": "body", "section": "MultiNet", "weight": 1.0} -->

The speed gap between VGG pool5 and is much larger when performing joint inference compared to the individual task. This can be explained by the fact that ResNet computes features with $2048$ channels, while VGG features have only $512$ channels. Thus, computing the fist layer of each decoder is significantly more expensive.

<!-- chunk {"id": "body-0052", "role": "body", "section": "MultiNet", "weight": 1.0} -->

Overall we conclude, that MultiNet using a VGG decoder offers a very good trade-off between performance and speed.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we have developed a unified deep architecture which is able to jointly reason about classification, detection and semantic segmentation. Our approach is very simple, can be trained end-to-end and performs extremely well in the challenging KITTI dataset, outperforming the state-of-the-art in the road segmentation task. Our approach is also very efficient, taking $42.48\ \frac{ms}{}$ to perform all tasks. In the future we plan to exploit compression methods in order to further reduce the computational bottleneck and energy consumption of MutiNet.
