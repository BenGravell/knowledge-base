<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network

Topics include Image super-resolution, Video super-resolution, Convolutional networks, Sub-pixel convolution, Pixel shuffle, Real-time inference, Low-resolution feature extraction, ESPCN.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

ESPCN moves most computation into low-resolution feature space and performs learned upsampling with a sub-pixel convolution layer, making real-time 1080p super-resolution feasible. The sub-pixel or pixel-shuffle idea became a widely reused upsampling primitive in image and video restoration networks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recently, several models based on deep neural networks have achieved great success in terms of both reconstruction accuracy and computational performance for single image super-resolution. In these methods, the low resolution (LR) input image is upscaled to the high resolution (HR) space using a single filter, commonly bicubic interpolation, before reconstruction. This means that the super-resolution (SR) operation is performed in HR space. We demonstrate that this is sub-optimal and adds computational complexity. In this paper, we present the first convolutional neural network (CNN) capable of real-time SR of 1080p videos on a single K2 GPU. To achieve this, we propose a novel CNN architecture where the feature maps are extracted in the LR space. In addition, we introduce an efficient sub-pixel convolution layer which learns an array of upscaling filters to upscale the final LR feature maps into the HR output. By doing so, we effectively replace the handcrafted bicubic filter in the SR pipeline with more complex upscaling filters specifically trained for each feature map, whilst also reducing the computational complexity of the overall SR operation.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We evaluate the proposed approach using images and videos from publicly available datasets and show that it performs significantly better (+0.15dB on Images and +0.39dB on Videos) and is an order of magnitude faster than previous CNN-based methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recovery of a high resolution (HR) image or video from its low resolution (LR) counter part is topic of great interest in digital image processing. This task, referred to as super-resolution (SR), finds direct applications in many areas such as HDTV, medical imaging, satellite imaging, face recognition and surveillance. The global SR problem assumes LR data to be a low-pass filtered (blurred), downsampled and noisy version of HR data. It is a highly ill-posed problem, due to the loss of high-frequency information that occurs during the non-invertible low-pass filtering and subsampling operations. Furthermore, the SR operation is effectively a one-to-many mapping from LR to HR space which can have multiple solutions, of which determining the correct solution is non-trivial. A key assumption that underlies many SR techniques is that much of the high-frequency data is redundant and thus can be accurately reconstructed from low frequency components. SR is therefore an inference problem, and thus relies on our model of the statistics of images in question.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many methods assume multiple images are available as LR instances of the same scene with different perspectives, i.e. with unique prior affine transformations. These can be categorised as multi-image SR methods and exploit *explicit redundancy* by constraining the ill-posed problem with additional information and attempting to invert the downsampling process. However, these methods usually require computationally complex image registration and fusion stages, the accuracy of which directly impacts the quality of the result. An alternative family of methods are single image super-resolution (SISR) techniques. These techniques seek to learn *implicit redundancy* that is present in natural data to recover missing HR information from a single LR instance. This usually arises in the form of local spatial correlations for images and additional temporal correlations in videos. In this case, prior information in the form of reconstruction constraints is needed to restrict the solution space of the reconstruction.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivations and contributions", "weight": 1.0} -->

With the development of CNN, the efficiency of the algorithms, especially their computational and memory cost, gains importance. The flexibility of deep network models to learn nonlinear relationships has been shown to attain superior reconstruction accuracy compared to previously hand-crafted models. To super-resolve a LR image into HR space, it is necessary to increase the resolution of the LR image to match that of the HR image at some point.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivations and contributions", "weight": 1.0} -->

In Osendorfer et al., the image resolution is increased in the middle of the network gradually. Another popular approach is to increase the resolution before or at the first layer of the network. However, this approach has a number of drawbacks. Firstly, increasing the resolution of the LR images before the image enhancement step increases the computational complexity. This is especially problematic for convolutional networks, where the processing speed directly depends on the input image resolution. Secondly, interpolation methods typically used to accomplish the task, such as bicubic interpolation, do not bring additional information to solve the ill-posed reconstruction problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivations and contributions", "weight": 1.0} -->

Learning upscaling filters was briefly suggested in the footnote of Dong et.al.. However, the importance of integrating it into the CNN as part of the SR operation was not fully recognised and the option not explored. Additionally, as noted by Dong et al., there are no efficient implementations of a convolution layer whose output size is larger than the input size and well-optimized implementations such as convnet do not trivially allow such behaviour.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivations and contributions", "weight": 1.0} -->

In this paper, contrary to previous works, we propose to increase the resolution from LR to HR only at the very end of the network and super-resolve HR data from LR feature maps. This eliminates the need to perform most of the SR operation in the far larger HR resolution. For this purpose, we propose an efficient sub-pixel convolution layer to learn the upscaling operation for image and video super-resolution.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivations and contributions", "weight": 1.0} -->

The advantages of these contributions are two fold: In our network, upscaling is handled by the last layer of the network. This means each LR image is directly fed to the network and feature extraction occurs through nonlinear convolutions in LR space. Due to the reduced input resolution, we can effectively use a smaller filter size to integrate the same information while maintaining a given contextual area. The resolution and filter size reduction lower the computational and memory complexity substantially enough to allow super-resolution of high definition (HD) videos in real-time as shown in Sec. 3.5.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motivations and contributions", "weight": 1.0} -->

For a network with $L$ layers, we learn $n_{L - 1}$ upscaling filters for the $n_{L - 1}$ feature maps as opposed to one upscaling filter for the input image. In addition, not using an explicit interpolation filter means that the network implicitly learns the processing necessary for SR. Thus, the network is capable of learning a better and more complex LR to HR mapping compared to a single fixed filter upscaling at the first layer. This results in additional gains in the reconstruction accuracy of the model as shown in Sec. 3.3.2 and Sec. 3.4.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motivations and contributions", "weight": 1.0} -->

We validate the proposed approach using images and videos from publicly available benchmarks datasets and compared our performance against previous works including. We show that the proposed model achieves state-of-art performance and is nearly an order of magnitude faster than previously published methods on images and videos.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

The task of SISR is to estimate a HR image $\mathbf{I}^{SR}$ given a LR image $\mathbf{I}^{LR}$ downscaled from the corresponding original HR image $\mathbf{I}^{HR}$. The downsampling operation is deterministic and known: to produce $\mathbf{I}^{LR}$ from $\mathbf{I}^{HR}$, we first convolve $\mathbf{I}^{HR}$ using a Gaussian filter - thus simulating the camera's point spread function - then downsample the image by a factor of $r$. We will refer to $r$ as the upscaling ratio. In general, both $\mathbf{I}^{LR}$ and $\mathbf{I}^{HR}$ can have $C$ colour channels, thus they are represented as real-valued tensors of size $H \times W \times C$ and ${{{rH} \times r}W} \times C$, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

To solve the SISR problem, the SRCNN proposed in recovers from an upscaled and interpolated version of $\mathbf{I}^{LR}$ instead of $\mathbf{I}^{LR}$. To recover $\mathbf{I}^{SR}$, a 3 layer convolutional network is used. In this section we propose a novel network architecture, as illustrated in Fig. 1, to avoid upscaling $\mathbf{I}^{LR}$ before feeding it into the network. In our architecture, we first apply a $l$ layer convolutional neural network directly to the LR image, and then apply a sub-pixel convolution layer that upscales the LR feature maps to produce $\mathbf{I}^{SR}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

For a network composed of $L$ layers, the first $L - 1$ layers can be described as follows: Where ${W_{l},b_{l},l} \in {(1,{L - 1})}$ are learnable network weights and biases respectively. $W_{l}$ is a 2D convolution tensor of size $n_{l - 1} \times n_{l} \times k_{l} \times k_{l}$, where $n_{l}$ is the number of features at layer $l$, $n_{0} = C$, and $k_{l}$ is the filter size at layer $l$. The biases $b_{l}$ are vectors of length $n_{l}$. The nonlinearity function (or activation function) $\phi$ is applied element-wise and is fixed. The last layer $f^{L}$ has to convert the LR feature maps to a HR image $\mathbf{I}^{SR}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Deconvolution layer", "weight": 1.0} -->

The addition of a deconvolution layer is a popular choice for recovering resolution from max-pooling and other image down-sampling layers. This approach has been successfully used in visualizing layer activations and for generating semantic segmentations using high level features from the network. It is trivial to show that the bicubic interpolation used in SRCNN is a special case of the deconvolution layer, as suggested already. The deconvolution layer proposed in can be seen as multiplication of each input pixel by a filter element-wise with stride $r$, and sums over the resulting output windows also known as backwards convolution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Efficient sub-pixel convolution layer", "weight": 1.0} -->

The other way to upscale a LR image is convolution with fractional stride of $\frac{1}{r}$ in the LR space as mentioned, which can be naively implemented by interpolation, perforate or un-pooling from LR space to HR space followed by a convolution with a stride of $1$ in HR space. These implementations increase the computational cost by a factor of $r^{2}$, since convolution happens in HR space.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Efficient sub-pixel convolution layer", "weight": 1.0} -->

Alternatively, a convolution with stride of $\frac{1}{r}$ in the LR space with a filter $W_{s}$ of size $k_{s}$ with weight spacing $\frac{1}{r}$ would activate different parts of $W_{s}$ for the convolution. The weights that fall between the pixels are simply not activated and do not need to be calculated. The number of activation patterns is exactly $r^{2}$. Each activation pattern, according to its location, has at most ${\lceil\frac{k_{s}}{r}\rceil}^{2}$ weights activated. These patterns are periodically activated during the convolution of the filter across the image depending on different sub-pixel location: ${\text{mod}(x,r)},{\text{mod}(y,r)}$ where $x,y$ are the output pixel coordinates in HR space.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Efficient sub-pixel convolution layer", "weight": 1.0} -->

In this paper, we propose an effective way to implement the above operation when ${\text{mod}\left(k_{s},r \right)} = 0$: where $\mathcal{P}\mathcal{S}$ is an periodic shuffling operator that rearranges the elements of a ${H \times W \times C} \cdot r^{2}$ tensor to a tensor of shape ${{{rH} \times r}W} \times C$. The effects of this operation are illustrated in Fig. 1. Mathematically, this operation can be described in the following way The convolution operator $W_{L}$ thus has shape ${{n_{L - 1} \times r^{2}}C} \times k_{L} \times k_{L}$. Note that we do not apply nonlinearity to the outputs of the convolution at the last layer.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Efficient sub-pixel convolution layer", "weight": 1.0} -->

It is easy to see that when $k_{L} = \frac{k_{s}}{r}$ and ${\text{mod}\left(k_{s},r \right)} = 0$ it is equivalent to sub-pixel convolution in the LR space with the filter $W_{s}$. We will refer to our new layer as the sub-pixel convolution layer and our network as efficient sub-pixel convolutional neural network (ESPCN). This last layer produces a HR image from LR feature maps directly with one upscaling filter for each feature map as shown in Fig. 4.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Efficient sub-pixel convolution layer", "weight": 1.0} -->

Given a training set consisting of HR image examples ${\mathbf{I}_{n}^{HR},n} = {1\ldotsN}$, we generate the corresponding LR images ${\mathbf{I}_{n}^{LR},n} = {1\ldotsN}$, and calculate the pixel-wise mean squared error (MSE) of the reconstruction as an objective function to train the network: It is noticeable that the implementation of the above periodic shuffling can be avoided in training time. Instead of shuffling the output as part of the layer, we can pre-shuffle the training data to match the output of the layer before $\mathcal{P}\mathcal{S}$. Thus our proposed layer is $log_{2}r^{2}$ times faster compared to deconvolution layer in training and $r^{2}$ times faster compared to implementations using various forms of upscaling before convolution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

The detailed report of quantitative evaluation including the original data including images and videos, down-sampled data, super-resolved data, overall and individual scores and run-times on a K2 GPU are provided in the supplemental material^11^1Supplemental material

<!-- chunk {"id": "body-0024", "role": "body", "section": "Datasets", "weight": 1.0} -->

During the evaluation, we used publicly available benchmark datasets including the Timofte dataset widely used by SISR papers which provides source code for multiple methods, 91 training images and two test datasets Set5 and which provides 5 and 14 images; The Berkeley segmentation dataset BSD300 and BSD500 which provides 100 and 200 images for testing and the super texture dataset which provides 136 texture images. For our final models, we use 50,000 randomly selected images from ImageNet for the training. Following previous works, we only consider the luminance channel in YCbCr colour space in this section because humans are more sensitive to luminance changes. For each upscaling factor, we train a specific network.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Datasets", "weight": 1.0} -->

For video experiments we use 1080p HD videos from the publicly available Xiph database^22^2Xiph.org Video Test Media \[derf's collection\] which has been used to report video SR results in previous methods. The database contains a collection of $8$ HD videos approximately $10$ seconds in length and with width and height $1920 \times 1080$. In addition, we also use the Ultra Video Group database^33^3Ultra Video Group Test Sequences containing $7$ videos of $1920 \times 1080$ in size and $5$ seconds in length.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Implementation details", "weight": 1.0} -->

For the ESPCN, we set $l = 3$, ${(f_{1},n_{1})} = {}$, ${(f_{2},n_{2})} = {}$ and $f_{3} = 3$ in our evaluations. The choice of the parameter is inspired by SRCNN's 3 layer 9-5-5 model and the equations in Sec. 2.2. In the training phase, ${{17r} \times 17}r$ pixel sub-images are extracted from the training ground truth images $\mathbf{I}^{HR}$, where $r$ is the upscaling factor. To synthesize the low-resolution samples $\mathbf{I}^{LR}$, we blur $\mathbf{I}^{HR}$ using a Gaussian filter and sub-sample it by the upscaling factor.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Implementation details", "weight": 1.0} -->

The sub-images are extracted from original images with a stride of ${({17 - {\sum{\text{mod}(f,2)}}})} \times r$ from $\mathbf{I}^{HR}$ and a stride of $17 - {\sum{\text{mod}(f,2)}}$ from $\mathbf{I}^{LR}$. This ensures that all pixels in the original image appear once and only once as the ground truth of the training data. We choose $tanh$ instead of $relu$ as the activation function for the final model motivated by our experimental results.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Implementation details", "weight": 1.0} -->

The training stops after no improvement of the cost function is observed after 100 epochs. Initial learning rate is set to 0.01 and final learning rate is set to 0.0001 and updated gradually when the improvement of the cost function is smaller than a threshold $\mu$. The final layer learns 10 times slower as. The training takes roughly three hours on a K2 GPU on 91 images, and seven days on images from ImageNet for upscaling factor of 3. We use the PSNR as the performance metric to evaluate our models. PSNR of SRCNN and Chen's models on our extended benchmark set are calculated based on the Matlab code and models provided.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Benefits of the sub-pixel convolution layer", "weight": 1.0} -->

In this section, we demonstrate the positive effect of the sub-pixel convolution layer as well as $tanh$ activation function. We first evaluate the power of the sub-pixel convolution layer by comparing against SRCNN's standard 9-1-5 model. Here, we follow the approach, using $relu$ as the activation function for our models in this experiment, and training a set of models with 91 images and another set with images from ImageNet. The results are shown in Tab. 1. ESPCN with $relu$ trained on ImageNet images achieved statistically significantly better performance compared to SRCNN models. It is noticeable that ESPCN performs very similar to SRCNN. Training with more images using ESPCN has a far more significant impact on PSNR compared to SRCNN with similar number of parameters (+0.33 vs +0.07).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Benefits of the sub-pixel convolution layer", "weight": 1.0} -->

To make a visual comparison between our model with the sub-pixel convolution layer and SRCNN, we visualized weights of our ESPCN (ImageNet) model against SRCNN 9-5-5 ImageNet model from in Fig. 3 and Fig. 4. The weights of our first and last layer filters have a strong similarity to designed features including the log-Gabor filters, wavelets and Haar features. It is noticeable that despite each filter is independent in LR space, our independent filters is actually smooth in the HR space after $\mathcal{P}\mathcal{S}$. Compared to SRCNN's last layer filters, our final layer filters has complex patterns for different feature maps, it also has much richer and more meaningful representations.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Benefits of the sub-pixel convolution layer", "weight": 1.0} -->

We also evaluated the effect of $tanh$ activation function based on the above model trained on 91 images and ImageNet images. Results in Tab. 1 suggests that $tanh$ function performs better for SISR compared to $relu$. The results for ImageNet images with $tanh$ activation is shown in Tab. 2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Comparison to the state-of-the-art", "weight": 1.0} -->

In this section, we show ESPCN trained on ImageNet compared to results from SRCNN and the TNRD which is currently the best performing approach published. For simplicity, we do not show results which are known to be worse than. For the interested reader, the results of other previous methods can be found. We choose to compare against the best SRCNN 9-5-5 ImageNet model in this section. And, results are calculated based on the $7 \times 7$ $5$ stages model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Comparison to the state-of-the-art", "weight": 1.0} -->

Our results shown in Tab. 2 are significantly better than the SRCNN 9-5-5 ImageNet model, whilst being close to, and in some cases out-performing, the TNRD. Although TNRD uses a single bicubic interpolation to upscale the input image to HR space, it possibly benefits from a trainable nonlinearity function. This trainable nonlinearity function is not exclusive from our network and will be interesting to explore in the future. Visual comparison of the super-resolved images is given in Fig. 5 and Fig. 6, the CNN methods create a much sharper and higher contrast images, ESPCN provides noticeably improvement over SRCNN.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Run time evaluations", "weight": 1.0} -->

In this section, we evaluated our best model's run time on ^44^4It should be noted our results outperform all other algorithms in accuracy on the larger BSD datasets. However, the use of on a single CPU core is selected here in order to allow a straight-forward comparison with results from previous published results. with an upscale factor of 3. We evaluate the run time of other methods from the Matlab codes provided by and. For methods which use convolutions including our own, a python/theano implementation is used to improve the efficiency based on the Matlab codes provided. The results are presented in Fig. 2. Our model runs a magnitude faster than the fastest methods published so far. Compared to SRCNN 9-5-5 ImageNet model, the number of convolution required to super-resolve one image is $r \times r$ times smaller and the number of total parameters of the model is $2.5$ times smaller. The total complexity of the super-resolution operation is thus $2.5 \times r \times r$ times lower.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Run time evaluations", "weight": 1.0} -->

We have achieved a stunning average speed of $4.7ms$ for super-resolving one single image from on a K2 GPU. Utilising the amazing speed of the network, it will be interesting to explore ensemble prediction using independently trained models as discussed in to achieve better SR performance in the future.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Run time evaluations", "weight": 1.0} -->

We also evaluated run time of 1080 HD video super-resolution using videos from the Xiph and the Ultra Video Group database. With upscale factor of 3, SRCNN 9-5-5 ImageNet model takes 0.435s per frame whilst our ESPCN model takes only 0.038s per frame. With upscale factor of 4, SRCNN 9-5-5 ImageNet model takes 0.434s per frame whilst our ESPCN model takes only 0.029s per frame.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we demonstrate that a non-adaptive upscaling at the first layer provides worse results than an adaptive upscaling for SISR and requires more computational complexity. To address the problem, we propose to perform the feature extraction stages in the LR space instead of HR space. To do that we propose a novel sub-pixel convolution layer which is capable of super-resolving LR data into HR space with very little additional computational cost compared to a deconvolution layer at training time. Evaluation performed on an extended bench mark data set with upscaling factor of 4 shows that we have a significant speed ($> 10 \times$) and performance (+0.15dB on Images and +0.39dB on videos) boost compared to the previous CNN approach with more parameters (5-3-3 vs 9-5-5). This makes our model the first CNN model that is capable of SR HD videos in real time on a single GPU.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Future work", "weight": 1.5} -->

A reasonable assumption when processing video information is that most of a scene's content is shared by neighbouring video frames. Exceptions to this assumption are scene changes and objects sporadically appearing or disappearing from the scene. This creates additional data-implicit redundancy that can be exploited for video super-resolution as has been shown. Spatio-temporal networks are popular as they fully utilise the temporal information from videos for human action recognition. In the future, we will investigate extending our ESPCN network into a spatio-temporal network to super-resolve one frame from multiple neighbouring frames using 3D convolutions.
