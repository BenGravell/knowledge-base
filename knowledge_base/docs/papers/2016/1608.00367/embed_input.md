<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accelerating the Super-Resolution Convolutional Neural Network

Topics include Image super-resolution, Convolutional networks, Efficient inference, Deconvolution, Low-resolution feature extraction, Shrinking and expanding layers, Transfer strategy, FSRCNN.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

FSRCNN reworks SRCNN for speed by operating before bicubic upsampling, adding a final deconvolution layer, and using a compact hourglass mapping. The design makes the classic CNN super-resolution pipeline much more practical for real-time CPU inference.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As a successful deep model applied in image super-resolution (SR), the Super-Resolution Convolutional Neural Network (SRCNN) has demonstrated superior performance to the previous hand-crafted models either in speed and restoration quality. However, the high computational cost still hinders it from practical usage that demands real-time performance (24 fps). In this paper, we aim at accelerating the current SRCNN, and propose a compact hourglass-shape CNN structure for faster and better SR. We re-design the SRCNN structure mainly in three aspects. First, we introduce a deconvolution layer at the end of the network, then the mapping is learned directly from the original low-resolution image (without interpolation) to the high-resolution one. Second, we reformulate the mapping layer by shrinking the input feature dimension before mapping and expanding back afterwards. Third, we adopt smaller filter sizes but more mapping layers. The proposed model achieves a speed up of more than 40 times with even superior restoration quality. Further, we present the parameter settings that can achieve real-time performance on a generic CPU while still maintaining good performance.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A corresponding transfer strategy is also proposed for fast training and testing across different upscaling factors.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Single image super-resolution (SR) aims at recovering a high-resolution (HR) image from a given low-resolution (LR) one. Recent SR algorithms are mostly learning-based (or patch-based) methods that learn a mapping between the LR and HR image spaces. Among them, the Super-Resolution Convolutional Neural Network (SRCNN) has drawn considerable attention due to its simple network structure and excellent restoration quality. Though SRCNN is already faster than most previous learning-based methods, the processing speed on large images is still unsatisfactory. For example, to upsample an $240 \times 240$ image by a factor of 3, the speed of the original SRCNN is about 1.32 fps, which is far from real-time (24 fps). To approach real-time, we should accelerate SRCNN for at least 17 times while keeping the previous performance. This sounds implausible at the first glance, as accelerating by simply reducing the parameters will severely impact the performance. However, when we delve into the network structure, we find two inherent limitations that restrict its running speed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, as a pre-processing step, the original LR image needs to be upsampled to the desired size using bicubic interpolation to form the input. Thus the computation complexity of SRCNN grows quadratically with the spatial size of the HR image (not the original LR image). For the upscaling factor $n$, the computational cost of convolution with the interpolated LR image will be $n^{2}$ times of that for the original LR one. This is also the restriction for most learning-based SR methods. If the network was learned directly from the original LR image, the acceleration would be significant, *i.e.,* about $n^{2}$ times faster.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second restriction lies on the costly non-linear mapping step. In SRCNN, input image patches are projected on a high-dimensional LR feature space, then followed by a complex mapping to another high-dimensional HR feature space. Dong *et al.* show that the mapping accuracy can be substantially improved by adopting a wider mapping layer, but at the cost of the running time. For example, the large SRCNN (SRCNN-Ex) has 57,184 parameters, which are six times larger than that for SRCNN (8,032 parameters). Then the question is how to shrink the network scale while still keeping the previous accuracy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

According to the above observations, we investigate a more concise and efficient network structure for fast and accurate image SR. To solve the first problem, we adopt a deconvolution layer to replace the bicubic interpolation. To further ease the computational burden, we place the deconvolution layer^11^1We follow to adopt the terminology 'deconvolution'. We note that it carries very different meaning in classic image processing, see. at the end of the network, then the computational complexity is only proportional to the spatial size of the original LR image. It is worth noting that the deconvolution layer is not equal to a simple substitute of the conventional interpolation kernel like in FCN, or 'unpooling+convolution' like. Instead, it consists of diverse automatically learned upsampling kernels (see Figure 3) that work jointly to generate the final HR output, and replacing these deconvolution filters with uniform interpolation kernels will result in a drastic PSNR drop (*e.g.,* at least 0.9 dB on the Set5 dataset for $\times 3$).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

For the second problem, we add a shrinking and an expanding layer at the beginning and the end of the mapping layer separately to restrict mapping in a low-dimensional feature space. Furthermore, we decompose a single wide mapping layer into several layers with a fixed filter size $3 \times 3$. The overall shape of the new structure looks like an hourglass, which is symmetrical on the whole, thick at the ends and thin in the middle. Experiments show that the proposed model, named as Fast Super-Resolution Convolutional Neural Networks (FSRCNN) ^22^2The implementation is available on the project page achieves a speed-up of more than $40 \times$ with even superior performance than the SRCNN-Ex. In this work, we also present a small FSRCNN network (FSRCNN-s) that achieves similar restoration quality as SRCNN, but is $17.36$ times faster and can run in real time (24 fps) with a generic CPU. As shown in Figure 1, the FSRCNN networks are much faster than contemporary SR models yet achieving superior performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Apart from the notable improvement in speed, the FSRCNN also has another appealing property that could facilitate fast training and testing across different upscaling factors. Specifically, in FSRCNN, all convolution layers (except the deconvolution layer) can be shared by networks of different upscaling factors. During training, with a well-trained network, we only need to fine-tune the deconvolution layer for another upscaling factor with almost no loss of mapping accuracy. During testing, we only need to do convolution operations once, and upsample an image to different scales using the corresponding deconvolution layer.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are three-fold: 1) We formulate a compact hourglass-shape CNN structure for fast image super-resolution. With the collaboration of a set of deconvolution filters, the network can learn an end-to-end mapping between the original LR and HR images with no pre-processing. 2) The proposed model achieves a speed up of at least $40 \times$ than the SRCNN-Ex while still keeping its exceptional performance. One of its small-size version can run in real-time ($>$`<!-- -->`{=html}24 fps) on a generic CPU with better restoration quality than SRCNN. 3) We transfer the convolution layers of the proposed networks for fast training and testing across different upscaling factors, with no loss of restoration quality.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Fast Super-Resolution by CNN", "weight": 1.0} -->

We first briefly describe the network structure of SRCNN, and then we detail how we reformulate the network layer by layer. The differences between FSRCNN and SRCNN are presented at the end of this section.

<!-- chunk {"id": "body-0013", "role": "body", "section": "SRCNN", "weight": 1.0} -->

SRCNN aims at learning an end-to-end mapping function $F$ between the bicubic-interpolated LR image $Y$ and the HR image $X$. The network contains all convolution layers, thus the size of the output is the same as that of the input image. As depicted in Figure 2, the overall structure consists of three parts that are analogous to the main steps of the sparse-coding-based methods. The patch extraction and representation part refers to the first layer, which extracts patches from the input and represents each patch as a high-dimensional feature vector. The non-linear mapping part refers to the middle layer, which maps the feature vectors non-linearly to another set of feature vectors, or namely HR features. Then the last reconstruction part aggregates these features to form the final output image.

<!-- chunk {"id": "body-0014", "role": "body", "section": "SRCNN", "weight": 1.0} -->

The computation complexity of the network can be calculated as follows,

<!-- chunk {"id": "body-0015", "role": "body", "section": "SRCNN", "weight": 1.0} -->

where ${\{ f_{i}\}}_{i = 1}^{3}$ and ${\{ n_{i}\}}_{i = 1}^{3}$ are the filter size and filter number of the three layers, respectively. $S_{HR}$ is the size of the HR image. We observe that the complexity is proportional to the size of the HR image, and the middle layer contributes most to the network parameters. In the next section, we present the FSRCNN by giving special attention to these two facets.

<!-- chunk {"id": "body-0016", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

As shown in Figure 2, FSRCNN can be decomposed into five parts -- feature extraction, shrinking, mapping, expanding and deconvolution. The first four parts are convolution layers, while the last one is a deconvolution layer. For better understanding, we denote a convolution layer as $Conv{(f_{i},n_{i},c_{i})}$, and a deconvolution layer as $DeConv{(f_{i},n_{i},c_{i})}$, where the variables $f_{i},n_{i},c_{i}$ represent the filter size, the number of filters and the number of channels, respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

As the whole network contains tens of variables (*i.e.,* ${\{ f_{i},n_{i},c_{i}\}}_{i = 1}^{6}$), it is impossible for us to investigate each of them. Thus we assign a reasonable value to the insensitive variables in advance, and leave the sensitive variables unset. We call a variable sensitive when a slight change of the variable could significantly influence the performance. These sensitive variables always represent some important influential factors in SR, which will be shown in the following descriptions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Feature extraction: This part is similar to the first part of SRCNN, but different on the input image. FSRCNN performs feature extraction on the original LR image without interpolation. To distinguish from SRCNN, we denote the small LR input as $Y_{s}$. By doing convolution with the first set of filters, each patch of the input (1-pixel overlapping) is represented as a high-dimensional feature vector.

<!-- chunk {"id": "body-0019", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

We refer to SRCNN on the choice of parameters -- $f_{1},n_{1},c_{1}$. In SRCNN, the filter size of the first layer is set to be 9. Note that these filters are performed on the upscaled image $Y$. As most pixels in $Y$ are interpolated from $Y_{s}$, a $5 \times 5$ patch in $Y_{s}$ could cover almost all information of a $9 \times 9$ patch in $Y$. Therefore, we can adopt a smaller filter size $f_{1} = 5$ with little information loss. For the number of channels, we follow SRCNN to set $c_{1} = 1$. Then we only need to determine the filter number $n_{1}$. From another perspective, $n_{1}$ can be regarded as the number of LR feature dimension, denoted as $d$ -- the first sensitive variable. Finally, the first layer can be represented as $Conv{(5,d,1)}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Shrinking: In SRCNN, the mapping step generally follows the feature extraction step, then the high-dimensional LR features are mapped directly to the HR feature space. However, as the LR feature dimension $d$ is usually very large, the computation complexity of the mapping step is pretty high. This phenomenon is also observed in some deep models for high-level vision tasks. Authors in apply $1 \times 1$ layers to save the computational cost.

<!-- chunk {"id": "body-0021", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

With the same consideration, we add a shrinking layer after the feature extraction layer to reduce the LR feature dimension $d$. We fix the filter size to be $f_{2} = 1$, then the filters perform like a linear combination within the LR features. By adopting a smaller filter number $n_{2} = s\operatorname{<<}d$, the LR feature dimension is reduced from $d$ to $s$. Here $s$ is the second sensitive variable that determines the level of shrinking, and the second layer can be represented as $Conv{(1,s,d)}$. This strategy greatly reduces the number of parameters (detailed computation in Section 3.3).

<!-- chunk {"id": "body-0022", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Non-linear mapping: The non-linear mapping step is the most important part that affects the SR performance, and the most influencing factors are the width (*i.e.,* the number of filters in a layer) and depth (*i.e.,* the number of layers) of the mapping layer. As indicated in SRCNN, a $5 \times 5$ layer achieves much better results than a $1 \times 1$ layer. But they are lack of experiments on very deep networks. The above experiences help us to formulate a more efficient mapping layer for FSRCNN. First, as a trade-off between the performance and network scale, we adopt a medium filter size $f_{3} = 3$. Then, to maintain the same good performance as SRCNN, we use multiple $3 \times 3$ layers to replace a single wide one. The number of mapping layers is another sensitive variable (denoted as $m$), which determines both the mapping accuracy and complexity. To be consistent, all mapping layers contain the same number of filters $n_{3} = s$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Then the non-linear mapping part can be represented as ${m \times C}onv{(3,s,s)}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Expanding: The expanding layer acts like an inverse process of the shrinking layer. The shrinking operation reduces the number of LR feature dimension for the sake of the computational efficiency. However, if we generate the HR image directly from these low-dimensional features, the final restoration quality will be poor. Therefore, we add an expanding layer after the mapping part to expand the HR feature dimension. To maintain consistency with the shrinking layer, we also adopt $1 \times 1$ filters, the number of which is the same as that for the LR feature extraction layer. As opposed to the shrinking layer $Conv{(1,s,d)}$, the expanding layer is $Conv{(1,d,s)}$. Experiments show that without the expanding layer, the performance decreases up to 0.3 dB on the Set5 test set.

<!-- chunk {"id": "body-0025", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Deconvolution: The last part is a deconvolution layer, which upsamples and aggregates the previous features with a set of deconvolution filters. The deconvolution can be regarded as an inverse operation of the convolution. For convolution, the filter is convolved with the image with a stride $k$, and the output is $1/k$ times of the input. Contrarily, if we exchange the position of the input and output, the output will be $k$ times of the input, as depicted in Figure 4. We take advantage of this property to set the stride $k = n$, which is the desired upscaling factor. Then the output is directly the reconstructed HR image.

<!-- chunk {"id": "body-0026", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

When we determine the filter size of the deconvolution filters, we can look at the network from another perspective. Interestingly, the reversed network is like a downscaling operator that accepts an HR image and outputs the LR one. Then the deconvolution layer becomes a convolution layer with a stride $n$. As it extracts features from the HR image, we should adopt $9 \times 9$ filters that are consistent with the first layer of SRCNN. Similarly, if we reverse back, the deconvolution filters should also have a spatial size $f_{5} = 9$. Experiments also demonstrate this assumption. Figure 3 shows the learned deconvolution filters, the patterns of which are very similar to that of the first-layer filters in SRCNN. Lastly, we can represent the deconvolution layer as $DeConv{(9,1,d)}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Different from inserting traditional interpolation kernels (*e.g.,* bicubic or bilinear) in-network or having 'unpooling+convolution', the deconvolution layer learns a set of upsampling kernel for the input feature maps. As shown in Figure 3, these kernels are diverse and meaningful. If we force these kernels to be identical, the parameters will be used inefficiently (equal to sum up the input feature maps as one), and the performance will drop at least 0.9 dB on the Set5.

<!-- chunk {"id": "body-0028", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

PReLU: For the activation function after each convolution layer, we suggest the use of the Parametric Rectified Linear Unit (PReLU) instead of the commonly-used Rectified Linear Unit (ReLU). They are different on the coefficient of the negative part. For ReLU and PReLU, we can define a general activation function as ${f{(x_{i})}} = {{max{(x_{i},0)}} + {a_{i}min{(0,x_{i})}}}$, where $x_{i}$ is the input signal of the activation $f$ on the $i$-th channel, and $a_{i}$ is the coefficient of the negative part. The parameter $a_{i}$ is fixed to be zero for ReLU, but is learnable for PReLU. We choose PReLU mainly to avoid the "dead features" caused by zero gradients in ReLU. Then we can make full use of all parameters to test the maximum capacity of different network designs.

<!-- chunk {"id": "body-0029", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Experiments show that the performance of the PReLU-activated networks is more stable, and can be seen as the up-bound of that for the ReLU-activated networks.

<!-- chunk {"id": "body-0030", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Overall structure: We can connect the above five parts to form a complete FSRCNN network as ${Conv{(5,d,1)}} - {PReLU} - {Conv{(1,s,d)}} - {PReLU} - {{m \times C}onv{(3,s,s)}} - {PReLU} - {Conv{(1,d,s)}} - {PReLU} - {DeConv{(9,1,d)}}$. On the whole, there are three sensitive variables (*i.e.,* the LR feature dimension $d$, the number of shrinking filters $s$, and the mapping depth $m$) governing the performance and speed. For simplicity, we represent a FSRCNN network as $FSRCNN{(d,s,m)}$. The computational complexity can be calculated as

<!-- chunk {"id": "body-0031", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

We exclude the parameters of PReLU, which introduce negligible computational cost. Interestingly, the new structure looks like an hourglass, which is symmetrical on the whole, thick at the ends, and thin in the middle. The three sensitive variables are just the controlling parameters for the appearance of the hourglass. Experiments show that this hourglass design is very effective for image super-resolution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

Cost function: Following SRCNN, we adopt the mean square error (MSE) as the cost function. The optimization objective is represented as

<!-- chunk {"id": "body-0033", "role": "body", "section": "FSRCNN", "weight": 1.0} -->

where $Y_{s}^{i}$ and $X^{i}$ are the $i$-th LR and HR sub-image pair in the training data, and $F{(Y_{s}^{i};\theta)}$ is the network output for $Y_{s}^{i}$ with parameters $\theta$. All parameters are optimized using stochastic gradient descent with the standard backpropagation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Differences against SRCNN: From SRCNN to FSRCNN", "weight": 1.0} -->

To better understand how we accelerate SRCNN, we transform the SRCNN-Ex to another FSRCNN within three steps, and show how much acceleration and PSNR gain are obtained by each step. We use a representative upscaling factor $n = 3$. The network configurations of SRCNN, FSRCNN and the two transition states are shown in Table 1. We also show their performance (average PSNR on Set5) trained on the 91-image dataset.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Differences against SRCNN: From SRCNN to FSRCNN", "weight": 1.0} -->

First, we replace the last convolution layer of SRCNN-Ex with a deconvolution layer, then the whole network will perform on the original LR image and the computation complexity is proportional to $S_{LR}$ instead of $S_{HR}$. This step will enlarge the network scale but achieve a speedup of $8.7 \times$ (*i.e.,* ${57184/58976} \times 3^{2}$). As the learned deconvolution kernels are better than a single bicubic kernel, the performance increases roughly by 0.12 dB. Second, the single mapping layer is replaced with the combination of a shrinking layer, 4 mapping layers and an expanding layer. Overall, there are 5 more layers, but the parameters are decreased from 58,976 to 17,088. Also, the acceleration after this step is the most prominent -- $30.1 \times$. It is widely observed that depth is the key factor that affects the performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Differences against SRCNN: From SRCNN to FSRCNN", "weight": 1.0} -->

Here, we use four "narrow" layers to replace a single "wide" layer, thus achieving better results (33.01 dB) with much less parameters. Lastly, we adopt smaller filter sizes and less filters (*e.g.,* from $Conv{}$ to $Conv{}$), and obtain a final speedup of $41.3 \times$. As we remove some redundant parameters, the network is trained more efficiently and achieves another 0.05 dB improvement.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Differences against SRCNN: From SRCNN to FSRCNN", "weight": 1.0} -->

It is worth noting that this acceleration is NOT at the cost of performance degradation. Contrarily, the FSRCNN outperforms SRCNN-Ex by a large margin (*e.g.,* 0.23dB on the Set5 dataset). The main reasons of high performance have been presented in the above analysis. This is the main difference between our method and other CNN acceleration works. Nevertheless, with the guarantee of good performance, it is easier to cooperate with other acceleration methods to get a faster model.

<!-- chunk {"id": "body-0038", "role": "body", "section": "SR for Different Upscaling Factors", "weight": 1.0} -->

Another advantage of FSRCNN over the previous learning-based methods is that FSRCNN could achieve fast training and testing across different upscaling factors. Specifically, we find that all convolution layers on the whole act like a complex feature extractor of the LR image, and only the last deconvolution layer contains the information of the upscaling factor. This is also proved by experiments, of which the convolution filters are almost the same for different upscaling factors^33^3Note that in SRCNN and SCN, the convolution filters differ a lot for different upscaling factors.. With this property, we can transfer the convolution filters for fast training and testing.

<!-- chunk {"id": "body-0039", "role": "body", "section": "SR for Different Upscaling Factors", "weight": 1.0} -->

In practice, we train a model for an upscaling factor in advance. Then during training, we only fine-tune the deconvolution layer for another upscaling factor and leave the convolution layers unchanged. The fine-tuning is fast, and the performance is as good as training from scratch (see Section 4.4). During testing, we perform the convolution operations once, and upsample an image to different sizes with the corresponding deconvolution layer. If we need to apply several upscaling factors simultaneously, this property can lead to much faster testing (as illustrated in Figure 4).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Training dataset. The 91-image dataset is widely used as the training set in learning-based SR methods. As deep models generally benefit from big data, studies have found that 91 images are not enough to push a deep model to the best performance. Yang *et al.* and Schulter *et al.* use the BSD500 dataset. However, images in the BSD500 are in JPEG format, which are not optimal for the SR task. Therefore, we contribute a new General-100 dataset that contains 100 bmp-format images (with no compression)^44^4We follow to introduce only 100 images in a new super-resolution dataset. A larger dataset with more training images will be released on the project page.. The size of the newly introduced 100 images ranges from $710 \times 704$ (large) to $131 \times 112$ (small). They are all of good quality with clear edges but fewer smooth regions (*e.g.,* sky and ocean), thus are very suitable for the SR training.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In the following experiments, apart from using the 91-image dataset for training, we will also evaluate the applicability of the joint set of the General-100 dataset and the 91-image dataset to train our networks. To make full use of the dataset, we also adopt data augmentation as. We augment the data in two ways. 1) Scaling: each image is downscaled with the factor 0.9, 0,8, 0.7 and 0.6. 2) Rotation: each image is rotated with the degree of 90, 180 and 270. Then we will have ${{5 \times 4} - 1} = 19$ times more images for training.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Test and validation dataset. Following SRCNN and SCN, we use the Set5, and BSD200 dataset for testing. Another 20 images from the validation set of the BSD500 dataset are selected for validation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Training samples. To prepare the training data, we first downsample the original training images by the desired scaling factor $n$ to form the LR images. Then we crop the LR training images into a set of $f_{sub} \times f_{sub}$-pixel sub-images with a stride $k$. The corresponding HR sub-images (with size ${({nf_{sub}})}^{2}$) are also cropped from the ground truth images. These LR/HR sub-image pairs are the primary training data.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

For the issue of padding, we empirically find that padding the input or output maps does little effect on the final performance. Thus we adopt zero padding in all layers according to the filter size. In this way, there is no need to change the sub-image size for different network designs. Another issue affecting the sub-image size is the deconvolution layer. As we train our models with the Caffe package, its deconvolution filters will generate the output with size ${({{{nf_{sub}} - n} + 1})}^{2}$ instead of ${({nf_{sub}})}^{2}$. So we also crop $({n - 1})$-pixel borders on the HR sub-images.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Training strategy. For fair comparison with the state-of-the-arts (Sec. 4.5), we adopt the 91-image dataset for training. In addition, we also explore a two-step training strategy. First, we train a network from scratch with the 91-image dataset. Then, when the training is saturated, we add the General-100 dataset for fine-tuning. With this strategy, the training converges much earlier than training with the two datasets from the beginning.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

When training with the 91-image dataset, the learning rate of the convolution layers is set to be $10^{- 3}$ and that of the deconvolution layer is $10^{- 4}$. Then during fine-tuning, the learning rate of all layers is reduced by half. For initialization, the weights of the convolution filters are initialized with the method designed for PReLU. As we do not have activation functions at the end, the deconvolution filters are initialized by the same way as in SRCNN (*i.e.,* drawing randomly from a Gaussian distribution with zero mean and standard deviation 0.001).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Investigation of Different Settings", "weight": 1.0} -->

To test the property of the FSRCNN structure, we design a set of controlling experiments with different values of the three sensitive variables -- the LR feature dimension $d$, the number of shrinking filters $s$, and the mapping depth $m$. Specifically, we choose $d = {48,56}$, $s = {12,16}$ and $m = {2,3,4}$, thus we conduct a total of ${2 \times 2 \times 3} = 12$ experiments with different combinations.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Investigation of Different Settings", "weight": 1.0} -->

The average PSNR values on the Set5 dataset of these experiments are shown in Table 2. We analyze the results in two directions, *i.e.,* horizontally and vertically in the table. First, we fix $d,s$ and examine the influence of $m$. Obviously, $m = 4$ leads to better results than $m = 2$ and $m = 3$. This trend can also be observed from the convergence curves shown in Figure 5(a). Second, we fix $m$ and examine the influence of $d$ and $s$. In general, a better result usually requires more parameters (*e.g.,* a larger $d$ or $s$), but more parameters do not always guarantee a better result. This trend is also reflected in Figure 5(b), where we see the three largest networks converge together. From all the results, we find the best trade-off between performance and parameters -- FSRCNN, which achieves one of the highest results with a moderate number of parameters.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Investigation of Different Settings", "weight": 1.0} -->

It is worth noticing that the smallest network FSRCNN achieves an average PSNR of 32.87 dB, which is already higher than that of SRCNN-Ex (32.75 dB) reported. The FSRCNN contains only 8,832 parameters, then the acceleration compared with SRCNN-Ex is ${{57184/8832} \times 9} = 58.3$ times.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Towards Real-Time SR with FSRCNN", "weight": 1.0} -->

Now we want to find a more concise FSRCNN network that could realize real-time SR while still keep good performance. First, we calculate how many parameters can meet the minimum requirement of real-time implementation (24 fps). As mentioned in the introduction, the speed of SRCNN to upsample an image to the size $760 \times 760$ is 1.32 fps. The upscaling factor is 3, and SRCNN has 8032 parameters. Then according to Equation 1 and 2, the desired FSRCNN network should have at most ${{{8032 \times 1.32}/24} \times 3^{2}} \approx 3976$ parameters. To achieve this goal, we find an appropriate configuration -- FSRCNN that contains 3937 parameters. With our C++ test code, the speed of FSRCNN reaches 24.7 fps, satisfying the real-time requirement. Furthermore, the FSRCNN even outperforms SRCNN (9-1-5) (see Table 3 and 4).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experiments for Different Upscaling Factors", "weight": 1.0} -->

Unlike existing methods that need to train a network from scratch for a different scaling factor, the proposed FSRCNN enjoys the flexibility of learning and testing across upscaling factors through transferring the convolution filters (Sec. 3.4). We demonstrate this flexibility in this section. We choose the FSRCNN as the default network.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experiments for Different Upscaling Factors", "weight": 1.0} -->

As we have obtained a well-trained model under the upscaling factor 3 (in Section 4.2), we then train the network for $\times$`<!-- -->`{=html}2 on the basis of that for $\times$`<!-- -->`{=html}3. To be specific, the parameters of all convolution filters in the well-trained model are transferred to the network of $\times$`<!-- -->`{=html}2. During training, we only fine-tune the deconvolution layer on the 91-image and General-100 datasets of $\times$`<!-- -->`{=html}2. For comparison, we train another network also for $\times$`<!-- -->`{=html}2 but from scratch. The convergence curves of these two networks are shown in Figure 6. Obviously, with the transferred parameters, the network converges very fast (only a few hours) with the same good performance as that training form scratch.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiments for Different Upscaling Factors", "weight": 1.0} -->

In the following experiments, we only train the networks from scratch for $\times$`<!-- -->`{=html}3, and fine-tune the corresponding deconvolution layers for $\times$`<!-- -->`{=html}2 and $\times$`<!-- -->`{=html}4.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Comparison with State-of-the-Arts", "weight": 1.0} -->

Compare using the same training set. First, we compare our method with four state-of-the-art learning-based SR algorithms that rely on external databases, namely the super-resolution forest (SRF), SRCNN, SRCNN-Ex and the sparse coding based network (SCN). The implementations of these methods are all based on their released source code. As they are written in different programming languages, the comparison of their test time may not be fair, but still reflects the main trend. To have a fair comparison on restoration quality, all models are trained on the augmented 91-image dataset, so the results are slightly different from that in the corresponding paper. We select two representative FSRCNN networks -- FSRCNN (short for FSRCNN ), and FSRCNN-s (short for FSRCNN ). The inference time is tested with the C++ implementation on an Intel i7 CPU 4.0 GHz. The quantitative results (PSNR and test time) for different upscaling factors are listed in Table 3. We first look at the test time, which is the main focus of our work.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Comparison with State-of-the-Arts", "weight": 1.0} -->

The proposed FSRCNN is undoubtedly the fastest method that is at least $40$ times faster than SRCNN-Ex, SRF and SCN (with the upscaling factor 3), while the fastest FSRCNN-s can achieve real-time performance ($> 24$ fps) on almost all the test images. Moreover, the FSRCNN still outperforms the previous methods on the PSNR values especially for $\times$`<!-- -->`{=html}2 and $\times$`<!-- -->`{=html}3. We also notice that the FSRCNN achieves slightly lower PSNR than SCN on factor 4. This is mainly because that the SCN adopts two models of $\times$`<!-- -->`{=html}2 to upsample an image by $\times$`<!-- -->`{=html}4. We have also tried this strategy and achieved comparable results. However, as we pay more attention to speed, we still present the results of a single network.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison with State-of-the-Arts", "weight": 1.0} -->

Compare using different training sets (following the literature). To follow the literature, we also compare the best PSNR results that are reported in the corresponding paper, as shown in Table 4. We also add another two competitive methods -- KK and A+ for comparison. Note that these results are obtained using different datasets, and our models are trained on the 91-image and General-100 datasets. From Table 4, we can see that the proposed FSRCNN still outperforms other methods on most upscaling factors and datasets. We have also done comprehensive comparisons in terms of SSIM and IFC in Table 5 and 6, where we observe the same trend. The reconstructed images of FSRCNN (shown in Figure 7 and 8), more examples can be found on the project page) are sharper and clearer than other results. In another aspect, the restoration quality of small models (FSRCNN-s and SRCNN) is slightly worse than large models (SRCNN-Ex, SCN and FSRCNN). In Figure 7, we could observe some "jaggies" or ringing effects in the results of FSRCNN-s and SRCNN.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

While observing the limitations of current deep learning based SR models, we explore a more efficient network structure to achieve high running speed without the loss of restoration quality. We approach this goal by re-designing the SRCNN structure, and achieves a final acceleration of more than 40 times. Extensive experiments suggest that the proposed method yields satisfactory SR performance, while superior in terms of run time. The proposed model can be adapted for real-time video SR, and motivate fast deep models for other low-level vision tasks.
