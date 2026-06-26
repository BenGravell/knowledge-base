<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows

Topics include Attention mechanisms, Computer vision, Object detection, Semantic segmentation, Classification, Computational complexity, Accuracy, Transformers.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a new vision Transformer, called Swin Transformer, that capably serves as a general-purpose backbone for computer vision. Challenges in adapting Transformer from language to vision arise from differences between the two domains, such as large variations in the scale of visual entities and the high resolution of pixels in images compared to words in text. To address these differences, we propose a hierarchical Transformer whose representation is computed with \textbf{S}hifted \textbf{win}dows. The shifted windowing scheme brings greater efficiency by limiting self-attention computation to non-overlapping local windows while also allowing for cross-window connection. This hierarchical architecture has the flexibility to model at various scales and has linear computational complexity with respect to image size. These qualities of Swin Transformer make it compatible with a broad range of vision tasks, including image classification (87.3 top-1 accuracy on ImageNet-1K) and dense prediction tasks such as object detection (58.7 box AP and 51.1 mask AP on COCO test-dev) and semantic segmentation (53.5 mIoU on ADE20K val).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Its performance surpasses the previous state-of-the-art by a large margin of +2.7 box AP and +2.6 mask AP on COCO, and +3.2 mIoU on ADE20K, demonstrating the potential of Transformer-based models as vision backbones. The hierarchical design and the shifted window approach also prove beneficial for all-MLP architectures. The code and models are publicly available at~.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modeling in computer vision has long been dominated by convolutional neural networks (CNNs). Beginning with AlexNet and its revolutionary performance on the ImageNet image classification challenge, CNN architectures have evolved to become increasingly powerful through greater scale, more extensive connections, and more sophisticated forms of convolution. With CNNs serving as backbone networks for a variety of vision tasks, these architectural advances have led to performance improvements that have broadly lifted the entire field.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, the evolution of network architectures in natural language processing (NLP) has taken a different path, where the prevalent architecture today is instead the Transformer. Designed for sequence modeling and transduction tasks, the Transformer is notable for its use of attention to model long-range dependencies in the data. Its tremendous success in the language domain has led researchers to investigate its adaptation to computer vision, where it has recently demonstrated promising results on certain tasks, specifically image classification and joint vision-language modeling.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we seek to expand the applicability of Transformer such that it can serve as a general-purpose backbone for computer vision, as it does for NLP and as CNNs do in vision. We observe that significant challenges in transferring its high performance in the language domain to the visual domain can be explained by differences between the two modalities. One of these differences involves scale. Unlike the word tokens that serve as the basic elements of processing in language Transformers, visual elements can vary substantially in scale, a problem that receives attention in tasks such as object detection. In existing Transformer-based models, tokens are all of a fixed scale, a property unsuitable for these vision applications. Another difference is the much higher resolution of pixels in images compared to words in passages of text. There exist many vision tasks such as semantic segmentation that require dense prediction at the pixel level, and this would be intractable for Transformer on high-resolution images, as the computational complexity of its self-attention is quadratic to image size. To overcome these issues, we propose a general-purpose Transformer backbone, called Swin Transformer, which constructs hierarchical feature maps and has linear computational complexity to image size.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As illustrated in Figure 1(a), Swin Transformer constructs a hierarchical representation by starting from small-sized patches (outlined in gray) and gradually merging neighboring patches in deeper Transformer layers. With these hierarchical feature maps, the Swin Transformer model can conveniently leverage advanced techniques for dense prediction such as feature pyramid networks (FPN) or U-Net. The linear computational complexity is achieved by computing self-attention locally within non-overlapping windows that partition an image (outlined in red). The number of patches in each window is fixed, and thus the complexity becomes linear to image size. These merits make Swin Transformer suitable as a general-purpose backbone for various vision tasks, in contrast to previous Transformer based architectures which produce feature maps of a single resolution and have quadratic complexity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key design element of Swin Transformer is its *shift* of the window partition between consecutive self-attention layers, as illustrated in Figure 2. The shifted windows bridge the windows of the preceding layer, providing connections among them that significantly enhance modeling power (see Table 4). This strategy is also efficient in regards to real-world latency: all *query* patches within a window share the same *key* set^11^1The *query* and *key* are projection vectors in a self-attention layer., which facilitates memory access in hardware. In contrast, earlier *sliding window* based self-attention approaches suffer from low latency on general hardware due to different *key* sets for different *query* pixels^22^2While there are efficient methods to implement a sliding-window based convolution layer on general hardware, thanks to its shared kernel weights across a feature map, it is difficult for a sliding-window based self-attention layer to have efficient memory access in practice.. Our experiments show that the proposed *shifted window* approach has much lower latency than the *sliding window* method, yet is similar in modeling power (see Tables 5 and 6).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The shifted window approach also proves beneficial for all-MLP architectures.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed Swin Transformer achieves strong performance on the recognition tasks of image classification, object detection and semantic segmentation. It outperforms the ViT / DeiT and ResNe(X)t models significantly with similar latency on the three tasks. Its 58.7 box AP and 51.1 mask AP on the COCO test-dev set surpass the previous state-of-the-art results by +2.7 box AP (Copy-paste without external data) and +2.6 mask AP (DetectoRS ). On ADE20K semantic segmentation, it obtains 53.5 mIoU on the val set, an improvement of +3.2 mIoU over the previous state-of-the-art (SETR ). It also achieves a top-1 accuracy of 87.3% on ImageNet-1K image classification.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is our belief that a unified architecture across computer vision and natural language processing could benefit both fields, since it would facilitate joint modeling of visual and textual signals and the modeling knowledge from both domains can be more deeply shared. We hope that Swin Transformer's strong performance on various vision problems can drive this belief deeper in the community and encourage unified modeling of vision and language signals.

<!-- chunk {"id": "body-0012", "role": "body", "section": "CNN and variants", "weight": 1.0} -->

CNNs serve as the standard network model throughout computer vision. While the CNN has existed for several decades, it was not until the introduction of AlexNet that the CNN took off and became mainstream. Since then, deeper and more effective convolutional neural architectures have been proposed to further propel the deep learning wave in computer vision, e.g., VGG, GoogleNet, ResNet, DenseNet, HRNet, and EfficientNet. In addition to these architectural advances, there has also been much work on improving individual convolution layers, such as depth-wise convolution and deformable convolution. While the CNN and its variants are still the primary backbone architectures for computer vision applications, we highlight the strong potential of Transformer-like architectures for unified modeling between vision and language. Our work achieves strong performance on several basic visual recognition tasks, and we hope it will contribute to a modeling shift.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Self-attention based backbone architectures", "weight": 1.0} -->

Also inspired by the success of self-attention layers and Transformer architectures in the NLP field, some works employ self-attention layers to replace some or all of the spatial convolution layers in the popular ResNet. In these works, the self-attention is computed within a local window of each pixel to expedite optimization, and they achieve slightly better accuracy/FLOPs trade-offs than the counterpart ResNet architecture. However, their costly memory access causes their actual latency to be significantly larger than that of the convolutional networks. Instead of using sliding windows, we propose to *shift* windows between consecutive layers, which allows for a more efficient implementation in general hardware.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Self-attention/Transformers to complement CNNs", "weight": 1.0} -->

Another line of work is to augment a standard CNN architecture with self-attention layers or Transformers. The self-attention layers can complement backbones or head networks by providing the capability to encode distant dependencies or heterogeneous interactions. More recently, the encoder-decoder design in Transformer has been applied for the object detection and instance segmentation tasks. Our work explores the adaptation of Transformers for basic visual feature extraction and is complementary to these works.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Transformer based vision backbones", "weight": 1.0} -->

Most related to our work is the Vision Transformer (ViT) and its follow-ups. The pioneering work of ViT directly applies a Transformer architecture on non-overlapping medium-sized image patches for image classification. It achieves an impressive speed-accuracy trade-off on image classification compared to convolutional networks. While ViT requires large-scale training datasets (i.e., JFT-300M) to perform well, DeiT introduces several training strategies that allow ViT to also be effective using the smaller ImageNet-1K dataset. The results of ViT on image classification are encouraging, but its architecture is unsuitable for use as a general-purpose backbone network on dense vision tasks or when the input image resolution is high, due to its low-resolution feature maps and the quadratic increase in complexity with image size. There are a few works applying ViT models to the dense vision tasks of object detection and semantic segmentation by direct upsampling or deconvolution but with relatively lower performance. Concurrent to our work are some that modify the ViT architecture for better image classification.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Transformer based vision backbones", "weight": 1.0} -->

Empirically, we find our Swin Transformer architecture to achieve the best speed-accuracy trade-off among these methods on image classification, even though our work focuses on general-purpose performance rather than specifically on classification. Another concurrent work explores a similar line of thinking to build multi-resolution feature maps on Transformers. Its complexity is still quadratic to image size, while ours is linear and also operates locally which has proven beneficial in modeling the high correlation in visual signals. Our approach is both efficient and effective, achieving state-of-the-art accuracy on both COCO object detection and ADE20K semantic segmentation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Overall Architecture", "weight": 1.0} -->

An overview of the Swin Transformer architecture is presented in Figure 3, which illustrates the tiny version (Swin-T). It first splits an input RGB image into non-overlapping patches by a patch splitting module, like ViT. Each patch is treated as a "token" and its feature is set as a concatenation of the raw pixel RGB values. In our implementation, we use a patch size of $4 \times 4$ and thus the feature dimension of each patch is ${4 \times 4 \times 3} = 48$. A linear embedding layer is applied on this raw-valued feature to project it to an arbitrary dimension (denoted as $C$).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Overall Architecture", "weight": 1.0} -->

Several Transformer blocks with modified self-attention computation (Swin Transformer blocks) are applied on these patch tokens. The Transformer blocks maintain the number of tokens ($\frac{H}{4} \times \frac{W}{4}$), and together with the linear embedding are referred to as "Stage 1".

<!-- chunk {"id": "body-0019", "role": "body", "section": "Overall Architecture", "weight": 1.0} -->

To produce a hierarchical representation, the number of tokens is reduced by patch merging layers as the network gets deeper. The first patch merging layer concatenates the features of each group of $2 \times 2$ neighboring patches, and applies a linear layer on the $4C$-dimensional concatenated features. This reduces the number of tokens by a multiple of ${2 \times 2} = 4$ ($2 \times$ downsampling of resolution), and the output dimension is set to $2C$. Swin Transformer blocks are applied afterwards for feature transformation, with the resolution kept at $\frac{H}{8} \times \frac{W}{8}$. This first block of patch merging and feature transformation is denoted as "Stage 2". The procedure is repeated twice, as "Stage 3" and "Stage 4", with output resolutions of $\frac{H}{16} \times \frac{W}{16}$ and $\frac{H}{32} \times \frac{W}{32}$, respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Overall Architecture", "weight": 1.0} -->

These stages jointly produce a hierarchical representation, with the same feature map resolutions as those of typical convolutional networks, e.g., VGG and ResNet. As a result, the proposed architecture can conveniently replace the backbone networks in existing methods for various vision tasks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Swin Transformer block", "weight": 1.0} -->

Swin Transformer is built by replacing the standard multi-head self attention (MSA) module in a Transformer block by a module based on shifted windows (described in Section 3.2), with other layers kept the same. As illustrated in Figure 3(b), a Swin Transformer block consists of a shifted window based MSA module, followed by a 2-layer MLP with GELU non-linearity in between. A LayerNorm (LN) layer is applied before each MSA module and each MLP, and a residual connection is applied after each module.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Shifted Window based Self-Attention", "weight": 1.0} -->

The standard Transformer architecture and its adaptation for image classification both conduct global self-attention, where the relationships between a token and all other tokens are computed. The global computation leads to quadratic complexity with respect to the number of tokens, making it unsuitable for many vision problems requiring an immense set of tokens for dense prediction or to represent a high-resolution image.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Self-attention in non-overlapped windows", "weight": 1.0} -->

For efficient modeling, we propose to compute self-attention within local windows. The windows are arranged to evenly partition the image in a non-overlapping manner. Supposing each window contains $M \times M$ patches, the computational complexity of a global MSA module and a window based one on an image of $h \times w$ patches are^33^3We omit SoftMax computation in determining complexity.: where the former is quadratic to patch number $hw$, and the latter is linear when $M$ is fixed (set to $7$ by default). Global self-attention computation is generally unaffordable for a large $hw$, while the window based self-attention is scalable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Shifted window partitioning in successive blocks", "weight": 1.0} -->

The window-based self-attention module lacks connections across windows, which limits its modeling power. To introduce cross-window connections while maintaining the efficient computation of non-overlapping windows, we propose a shifted window partitioning approach which alternates between two partitioning configurations in consecutive Swin Transformer blocks.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Shifted window partitioning in successive blocks", "weight": 1.0} -->

As illustrated in Figure 2, the first module uses a regular window partitioning strategy which starts from the top-left pixel, and the $8 \times 8$ feature map is evenly partitioned into $2 \times 2$ windows of size $4 \times 4$ ($M = 4$). Then, the next module adopts a windowing configuration that is shifted from that of the preceding layer, by displacing the windows by $({\lfloor\frac{M}{2}\rfloor},{\lfloor\frac{M}{2}\rfloor})$ pixels from the regularly partitioned windows.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Shifted window partitioning in successive blocks", "weight": 1.0} -->

With the shifted window partitioning approach, consecutive Swin Transformer blocks are computed as where ${\hat{\mathbf{z}}}^{l}$ and $\mathbf{z}^{l}$ denote the output features of the (S)W-MSA module and the MLP module for block $l$, respectively; W-MSA and SW-MSA denote window based multi-head self-attention using regular and shifted window partitioning configurations, respectively.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Shifted window partitioning in successive blocks", "weight": 1.0} -->

The shifted window partitioning approach introduces connections between neighboring non-overlapping windows in the previous layer and is found to be effective in image classification, object detection, and semantic segmentation, as shown in Table 4.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Efficient batch computation for shifted configuration", "weight": 1.0} -->

An issue with shifted window partitioning is that it will result in more windows, from ${\lceil\frac{h}{M}\rceil} \times {\lceil\frac{w}{M}\rceil}$ to ${({{\lceil\frac{h}{M}\rceil} + 1})} \times {({{\lceil\frac{w}{M}\rceil} + 1})}$ in the shifted configuration, and some of the windows will be smaller than $M \times M$^44^4To make the window size $(M,M)$ divisible by the feature map size of $(h,w)$, bottom-right padding is employed on the feature map if needed.. A naive solution is to pad the smaller windows to a size of $M \times M$ and mask out the padded values when computing attention.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Efficient batch computation for shifted configuration", "weight": 1.0} -->

When the number of windows in regular partitioning is small, e.g. $2 \times 2$, the increased computation with this naive solution is considerable (${2 \times 2}\rightarrow{3 \times 3}$, which is 2.25 times greater). Here, we propose a *more efficient batch computation approach* by cyclic-shifting toward the top-left direction, as illustrated in Figure 4. After this shift, a batched window may be composed of several sub-windows that are not adjacent in the feature map, so a masking mechanism is employed to limit self-attention computation to within each sub-window. With the cyclic-shift, the number of batched windows remains the same as that of regular window partitioning, and thus is also efficient. The low latency of this approach is shown in Table 5.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Relative position bias", "weight": 1.0} -->

In computing self-attention, we follow by including a relative position bias $B \in {\mathbb{R}}^{M^{2} \times M^{2}}$ to each head in computing similarity: where ${Q,K,V} \in {\mathbb{R}}^{M^{2} \times d}$ are the *query*, *key* and *value* matrices; $d$ is the *query*/*key* dimension, and $M^{2}$ is the number of patches in a window. Since the relative position along each axis lies in the range $\lbrack{{- M} + 1},{M - 1}\rbrack$, we parameterize a smaller-sized bias matrix $\hat{B} \in {\mathbb{R}}^{{({{2M} - 1})} \times {({{2M} - 1})}}$, and values in $B$ are taken from $\hat{B}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Relative position bias", "weight": 1.0} -->

We observe significant improvements over counterparts without this bias term or that use absolute position embedding, as shown in Table 4. Further adding absolute position embedding to the input as in drops performance slightly, thus it is not adopted in our implementation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Relative position bias", "weight": 1.0} -->

The learnt relative position bias in pre-training can be also used to initialize a model for fine-tuning with a different window size through bi-cubic interpolation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Architecture Variants", "weight": 1.0} -->

We build our base model, called Swin-B, to have of model size and computation complexity similar to ViT-B/DeiT-B. We also introduce Swin-T, Swin-S and Swin-L, which are versions of about $0.25 \times$, $0.5 \times$ and $2 \times$ the model size and computational complexity, respectively. Note that the complexity of Swin-T and Swin-S are similar to those of ResNet-50 (DeiT-S) and ResNet-101, respectively. The window size is set to $M = 7$ by default. The query dimension of each head is $d = 32$, and the expansion layer of each MLP is $\alpha = 4$, for all experiments.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Architecture Variants", "weight": 1.0} -->

The architecture hyper-parameters of these model variants are: Swin-T: $C = 96$, layer numbers = $\{ 2,2,6,2\}$ Swin-S: $C = 96$, layer numbers =$\{ 2,2,18,2\}$ Swin-B: $C = 128$, layer numbers =$\{ 2,2,18,2\}$ Swin-L: $C = 192$, layer numbers =$\{ 2,2,18,2\}$ where $C$ is the channel number of the hidden layers in the first stage. The model size, theoretical computational complexity (FLOPs), and throughput of the model variants for ImageNet image classification are listed in Table 1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct experiments on ImageNet-1K image classification, COCO object detection, and ADE20K semantic segmentation. In the following, we first compare the proposed Swin Transformer architecture with the previous state-of-the-arts on the three tasks. Then, we ablate the important design elements of Swin Transformer.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Settings", "weight": 1.0} -->

For image classification, we benchmark the proposed Swin Transformer on ImageNet-1K, which contains 1.28M training images and 50K validation images from 1,000 classes. The top-1 accuracy on a single crop is reported. We consider two training settings: *Regular ImageNet-1K training*. This setting mostly follows. We employ an AdamW optimizer for 300 epochs using a cosine decay learning rate scheduler and 20 epochs of linear warm-up. A batch size of 1024, an initial learning rate of 0.001, and a weight decay of 0.05 are used. We include most of the augmentation and regularization strategies of in training, except for repeated augmentation and EMA, which do not enhance performance. Note that this is contrary to where repeated augmentation is crucial to stabilize the training of ViT.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Settings", "weight": 1.0} -->

*Pre-training on ImageNet-22K and fine-tuning on ImageNet-1K*. We also pre-train on the larger ImageNet-22K dataset, which contains 14.2 million images and 22K classes. We employ an AdamW optimizer for 90 epochs using a linear decay learning rate scheduler with a 5-epoch linear warm-up. A batch size of 4096, an initial learning rate of 0.001, and a weight decay of 0.01 are used. In ImageNet-1K fine-tuning, we train the models for 30 epochs with a batch size of 1024, a constant learning rate of $10^{- 5}$, and a weight decay of $10^{- 8}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Results with regular ImageNet-1K training", "weight": 1.0} -->

Table 1(a) presents comparisons to other backbones, including both Transformer-based and ConvNet-based, using regular ImageNet-1K training.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Results with regular ImageNet-1K training", "weight": 1.0} -->

Compared to the previous state-of-the-art Transformer-based architecture, i.e. DeiT, Swin Transformers noticeably surpass the counterpart DeiT architectures with similar complexities: +1.5% for Swin-T (81.3%) over DeiT-S (79.8%) using 224^2^ input, and +1.5%/1.4% for Swin-B (83.3%/84.5%) over DeiT-B (81.8%/83.1%) using 224^2^/384^2^ input, respectively.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Results with regular ImageNet-1K training", "weight": 1.0} -->

Compared with the state-of-the-art ConvNets, i.e. RegNet and EfficientNet, the Swin Transformer achieves a slightly better speed-accuracy trade-off. Noting that while RegNet and EfficientNet are obtained via a thorough architecture search, the proposed Swin Transformer is adapted from the standard Transformer and has strong potential for further improvement.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results with ImageNet-22K pre-training", "weight": 1.0} -->

We also pre-train the larger-capacity Swin-B and Swin-L on ImageNet-22K. Results fine-tuned on ImageNet-1K image classification are shown in Table 1(b). For Swin-B, the ImageNet-22K pre-training brings 1.8%$\sim$`<!-- -->`{=html}1.9% gains over training on ImageNet-1K from scratch. Compared with the previous best results for ImageNet-22K pre-training, our models achieve significantly better speed-accuracy trade-offs: Swin-B obtains 86.4% top-1 accuracy, which is 2.4% higher than that of ViT with similar inference throughput (84.7 vs. 85.9 images/sec) and slightly lower FLOPs (47.0G vs. 55.4G). The larger Swin-L model achieves 87.3% top-1 accuracy, +0.9% better than that of the Swin-B model.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results with ImageNet-22K pre-training", "weight": 1.0} -->

#param.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results with ImageNet-22K pre-training", "weight": 1.0} -->

#param.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Settings", "weight": 1.0} -->

Object detection and instance segmentation experiments are conducted on COCO 2017, which contains 118K training, 5K validation and 20K test-dev images. An ablation study is performed using the validation set, and a system-level comparison is reported on test-dev. For the ablation study, we consider four typical object detection frameworks: Cascade Mask R-CNN, ATSS, RepPoints v2, and Sparse RCNN in mmdetection. For these four frameworks, we utilize the same settings: multi-scale training (resizing the input such that the shorter side is between 480 and 800 while the longer side is at most 1333), AdamW optimizer (initial learning rate of 0.0001, weight decay of 0.05, and batch size of 16), and 3x schedule (36 epochs). For system-level comparison, we adopt an improved HTC (denoted as HTC++) with instaboost, stronger multi-scale training, 6x schedule (72 epochs), soft-NMS, and ImageNet-22K pre-trained model as initialization.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Settings", "weight": 1.0} -->

We compare our Swin Transformer to standard ConvNets, i.e. ResNe(X)t, and previous Transformer networks, e.g. DeiT. The comparisons are conducted by changing only the backbones with other settings unchanged. Note that while Swin Transformer and ResNe(X)t are directly applicable to all the above frameworks because of their hierarchical feature maps, DeiT only produces a single resolution of feature maps and cannot be directly applied. For fair comparison, we follow to construct hierarchical feature maps for DeiT using deconvolution layers.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Settings", "weight": 1.0} -->

#param.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Settings", "weight": 1.0} -->

Cascade Mask R-CNN (b) Various backbones w. Cascade Mask R-CNN

<!-- chunk {"id": "body-0048", "role": "body", "section": "Settings", "weight": 1.0} -->

#param.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison to ResNe(X)t", "weight": 1.0} -->

Table 2(a) lists the results of Swin-T and ResNet-50 on the four object detection frameworks. Our Swin-T architecture brings consistent +3.4$\sim$`<!-- -->`{=html}4.2 box AP gains over ResNet-50, with slightly larger model size, FLOPs and latency.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparison to ResNe(X)t", "weight": 1.0} -->

Table 2(b) compares Swin Transformer and ResNe(X)t under different model capacity using Cascade Mask R-CNN. Swin Transformer achieves a high detection accuracy of 51.9 box AP and 45.0 mask AP, which are significant gains of +3.6 box AP and +3.3 mask AP over ResNeXt101-64x4d, which has similar model size, FLOPs and latency. On a higher baseline of 52.3 box AP and 46.0 mask AP using an improved HTC framework, the gains by Swin Transformer are also high, at +4.1 box AP and +3.1 mask AP (see Table 2(c)). Regarding inference speed, while ResNe(X)t is built by highly optimized Cudnn functions, our architecture is implemented with built-in PyTorch functions that are not all well-optimized. A thorough kernel optimization is beyond the scope of this paper.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Comparison to DeiT", "weight": 1.0} -->

The performance of DeiT-S using the Cascade Mask R-CNN framework is shown in Table 2(b). The results of Swin-T are +2.5 box AP and +2.3 mask AP higher than DeiT-S with similar model size (86M vs. 80M) and significantly higher inference speed (15.3 FPS vs. 10.4 FPS). The lower inference speed of DeiT is mainly due to its quadratic complexity to input image size.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Comparison to previous state-of-the-art", "weight": 1.0} -->

Table 2(c) compares our best results with those of previous state-of-the-art models. Our best model achieves 58.7 box AP and 51.1 mask AP on COCO test-dev, surpassing the previous best results by +2.7 box AP (Copy-paste without external data) and +2.6 mask AP (DetectoRS ).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Comparison to previous state-of-the-art", "weight": 1.0} -->

#param.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Settings", "weight": 1.0} -->

ADE20K is a widely-used semantic segmentation dataset, covering a broad range of 150 semantic categories. It has 25K images in total, with 20K for training, 2K for validation, and another 3K for testing. We utilize UperNet in mmseg as our base framework for its high efficiency. More details are presented in the Appendix.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Results", "weight": 1.0} -->

Table 3 lists the mIoU, model size (#param), FLOPs and FPS for different method/backbone pairs. From these results, it can be seen that Swin-S is +5.3 mIoU higher (49.3 vs. 44.0) than DeiT-S with similar computation cost. It is also +4.4 mIoU higher than ResNet-101, and +2.4 mIoU higher than ResNeSt-101. Our Swin-L model with ImageNet-22K pre-training achieves 53.5 mIoU on the val set, surpassing the previous best model by +3.2 mIoU (50.3 mIoU by SETR which has a larger model size). abs.+rel. pos. rel. pos. w/o app.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

In this section, we ablate important design elements in the proposed Swin Transformer, using ImageNet-1K image classification, Cascade Mask R-CNN on COCO object detection, and UperNet on ADE20K semantic segmentation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Shifted windows", "weight": 1.0} -->

Ablations of the *shifted window* approach on the three tasks are reported in Table 4. Swin-T with the shifted window partitioning outperforms the counterpart built on a single window partitioning at each stage by +1.1% top-1 accuracy on ImageNet-1K, +2.8 box AP/+2.2 mask AP on COCO, and +2.8 mIoU on ADE20K. The results indicate the effectiveness of using shifted windows to build connections among windows in the preceding layers. The latency overhead by *shifted window* is also small, as shown in Table 5.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Relative position bias", "weight": 1.0} -->

Table 4 shows comparisons of different position embedding approaches. Swin-T with relative position bias yields +1.2%/+0.8% top-1 accuracy on ImageNet-1K, +1.3/+1.5 box AP and +1.1/+1.3 mask AP on COCO, and +2.3/+2.9 mIoU on ADE20K in relation to those without position encoding and with absolute position embedding, respectively, indicating the effectiveness of the relative position bias. Also note that while the inclusion of absolute position embedding improves image classification accuracy (+0.4%), it harms object detection and semantic segmentation (-0.2 box/mask AP on COCO and -0.6 mIoU on ADE20K).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Relative position bias", "weight": 1.0} -->

While the recent ViT/DeiT models abandon translation invariance in image classification even though it has long been shown to be crucial for visual modeling, we find that inductive bias that encourages certain translation invariance is still preferable for general-purpose visual modeling, particularly for the dense prediction tasks of object detection and semantic segmentation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Different self-attention methods", "weight": 1.0} -->

The real speed of different self-attention computation methods and implementations are compared in Table 5. Our cyclic implementation is more hardware efficient than naive padding, particularly for deeper stages. Overall, it brings a 13%, 18% and 18% speed-up on Swin-T, Swin-S and Swin-B, respectively.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Different self-attention methods", "weight": 1.0} -->

The self-attention modules built on the proposed *shifted window* approach are 40.8$\times$/2.5$\times$, 20.2$\times$/2.5$\times$, 9.3$\times$/2.1$\times$, and 7.6$\times$/1.8$\times$ more efficient than those of *sliding windows* in naive/kernel implementations on four network stages, respectively. Overall, the Swin Transformer architectures built on *shifted windows* are 4.1/1.5, 4.0/1.5, 3.6/1.5 times faster than variants built on *sliding windows* for Swin-T, Swin-S, and Swin-B, respectively. Table 6 compares their accuracy on the three tasks, showing that they are similarly accurate in visual modeling.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Different self-attention methods", "weight": 1.0} -->

Compared to Performer, which is one of the fastest Transformer architectures (see), the proposed *shifted window* based self-attention computation and the overall Swin Transformer architectures are slightly faster (see Table 5), while achieving +2.3% top-1 accuracy compared to Performer on ImageNet-1K using Swin-T (see Table 6). sliding window (naive) sliding window (kernel) shifted window (padding) shifted window (cyclic) Table 5: Real speed of different self-attention computation methods and implementations on a V100 GPU.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents Swin Transformer, a new vision Transformer which produces a hierarchical feature representation and has linear computational complexity with respect to input image size. Swin Transformer achieves the state-of-the-art performance on COCO object detection and ADE20K semantic segmentation, significantly surpassing previous best methods. We hope that Swin Transformer's strong performance on various vision problems will encourage unified modeling of vision and language signals.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusion", "weight": 1.5} -->

As a key element of Swin Transformer, the *shifted window* based self-attention is shown to be effective and efficient on vision problems, and we look forward to investigating its use in natural language processing as well.
