<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Lossy Image Compression with Compressive Autoencoders

Topics include Autoencoders, Image compression, Joint photographic experts group, Joint photographic experts group 2000.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new approach to the problem of optimizing autoencoders for lossy image compression. New media formats, changing hardware technology, as well as diverse requirements and content types create a need for compression algorithms which are more flexible than existing codecs. Autoencoders have the potential to address this need, but are difficult to optimize directly due to the inherent non-differentiabilty of the compression loss. We here show that minimal changes to the loss are sufficient to train deep autoencoders competitive with JPEG 2000 and outperforming recently proposed approaches based on RNNs. Our network is furthermore computationally efficient thanks to a sub-pixel architecture, which makes it suitable for high-resolution images. This is in contrast to previous work on autoencoders for compression using coarser approximations, shallower architectures, computationally expensive methods, or focusing on small images.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in training of neural networks have helped to improve performance in a number of domains, but neural networks have yet to surpass existing codecs in lossy image compression. Promising first results have recently been achieved using autoencoders -- in particular on small images -- and neural networks are already achieving state-of-the-art results in lossless image compression.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autoencoders have the potential to address an increasing need for flexible lossy compression algorithms. Depending on the situation, encoders and decoders of different computational complexity are required. When sending data from a server to a mobile device, it may be desirable to pair a powerful encoder with a less complex decoder, but the requirements are reversed when sending data in the other direction. The amount of computational power and bandwidth available also changes over time as new technologies become available. For the purpose of archiving, encoding and decoding times matter less than for streaming applications. Finally, existing compression algorithms may be far from optimal for new media formats such as lightfield images, 360 video or VR content. While the development of a new codec can take years, a more general compression framework based on neural networks may be able to adapt much quicker to these changing tasks and environments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, lossy compression is an inherently non-differentiable problem. In particular, quantization is an integral part of the compression pipeline but is not differentiable. This makes it difficult to train neural networks for this task. Existing transformations have typically been manually chosen (e.g., the DCT transformation used in JPEG) or have been optimized for a task different from lossy compression. In contrast to most previous work, but in line with Ballé et al., we here aim at directly optimizing the rate-distortion tradeoff produced by an autoencoder. We propose a simple but effective approach for dealing with the non-differentiability of rounding-based quantization, and for approximating the non-differentiable cost of coding the generated coefficients.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using this approach, we achieve performance similar to or better than JPEG 2000 when evaluated for perceptual quality. Unlike JPEG 2000, however, our framework can be optimized for specific content (e.g., thumbnails or non-natural images), arbitrary metrics, and is readily generalizable to other forms of media. Notably, we achieve this performance using efficient neural network architectures which would allow near real-time decoding of large images even on low-powered consumer devices.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Compressive autoencoders", "weight": 1.0} -->

We define a compressive autoencoder (CAE) to have three components: an encoder $f$, a decoder $g$, and a probabilistic model $Q$, The discrete probability distribution defined by $Q$ is used to assign a number of bits to representations based on their frequencies, that is, for entropy coding. All three components may have parameters and our goal is to optimize the tradeoff between using a small number of bits and having small distortion, Here, $\beta$ controls the tradeoff, square brackets indicate quantization through rounding to the nearest integer, and $d$ measures the distortion introduced by coding and decoding. The quantized output of the encoder is the code used to represent an image and is stored losslessly. The main source of information loss is the quantization (Appendix A.3). Additional information may be discarded by the encoder, and the decoder may not perfectly decode the available information, increasing distortion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Compressive autoencoders", "weight": 1.0} -->

Unfortunately we cannot optimize Equation 2 directly using gradient-based techniques, as $Q$ and $\lbrack \cdot \rbrack$ are non-differentiable. The following two sections propose a solution to deal with this problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Quantization and differentiable alternatives", "weight": 1.0} -->

The derivative of the rounding function is zero everywhere except at integers, where it is undefined. We propose to replace its derivative in the backward pass of backpropagation with the derivative of a smooth approximation, $r$, that is, effectively defining the derivative to be Importantly, we do not fully replace the rounding function with a smooth approximation but only its derivative, which means that quantization is still performed as usual in the forward pass. If we replaced rounding with a smooth approximation completely, the decoder might learn to invert the smooth approximation, thereby removing the information bottle neck that forces the network to compress information.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Quantization and differentiable alternatives", "weight": 1.0} -->

Empirically, we found the identity, ${r{(y)}} = y$, to work as well as more sophisticated choices. This makes this operation easy to implement, as we simply have to pass gradients without modification from the decoder to the encoder.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Quantization and differentiable alternatives", "weight": 1.0} -->

Note that the gradient with respect to the decoder's parameters can be computed without resorting to approximations, assuming $d$ is differentiable. In contrast to related approaches, our approach has the advantage that it does not change the gradients of the decoder, since the forward pass is kept the same.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Quantization and differentiable alternatives", "weight": 1.0} -->

In the following, we discuss alternative approaches proposed by other authors. Motivated by theoretical links to dithering, Ballé et al. proposed to replace quantization by additive uniform noise, Toderici et al., on the other hand, used a stochastic form of binarization. Generalizing this idea to integers, we define the following stochastic rounding operation: where $\lfloor \cdot \rfloor$ is the floor operator. In the backward pass, the derivative is replaced with the derivative of the expectation, Figure 1 shows the effect of using these two alternatives as part of JPEG, whose encoder and decoder are based on a block-wise DCT transformation. Note that the output is visibly different from the output produced with regular quantization by rounding and that the error signal sent to the autoencoder depends on these images. Whereas in Fig. 1B the error signal received by the decoder would be to remove blocking artefacts, the signal in Fig. 1D will be to remove high-frequency noise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Quantization and differentiable alternatives", "weight": 1.0} -->

We expect this difference to be less of a problem with simple metrics such as mean-squared error and to have a bigger impact when using more perceptually meaningful measures of distortion.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Quantization and differentiable alternatives", "weight": 1.0} -->

An alternative would be to use the latter approximations only for the gradient of the encoder but not for the gradients of the decoder. While this is possible, it comes at the cost of increased computational and implementational complexity, since we would have to perform the forward and backward pass through the decoder twice: once using rounding, once using the approximation. With our approach the gradient of the decoder is correct even for a single forward and backward pass.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Entropy rate estimation", "weight": 1.0} -->

Since $Q$ is a discrete function, we cannot differentiate it with respect to its argument, which prevents us from computing a gradient for the encoder. To solve this problem, we use a continuous, differentiable approximation. We upper-bound the non-differentiable number of bits by first expressing the model's distribution $Q$ in terms of a probability density $q$, An upper bound is given: where the second step follows from Jensen's inequality. An unbiased estimate of the upper bound is obtained by sampling $\mathbf{u}$ from the unit cube $\lbrack -.5,.5\lbrack^{M}$. If we use a differentiable density, this estimate will be differentiable in $\mathbf{z}$ and therefore can be used to train the encoder.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Variable bit rates", "weight": 1.0} -->

In practice we often want fine-gained control over the number of bits used. One way to achieve this is to train an autoencoder for different rate-distortion tradeoffs. But this would require us to train and store a potentially large number of models. To reduce these costs, we finetune a pre-trained autoencoder for different rates by introducing scale parameters^11^1To ensure positivity, we use a different parametrization and optimize log-scales rather than scales. ${\mathbf{λ}} \in {\mathbb{R}}^{M}$, Here, $\circ$ indicates point-wise multiplication and division is also performed point-wise. To reduce the number of trainable scales, they may furthermore be shared across dimensions. Where $f$ and $g$ are convolutional, for example, we share scale parameters across spatial dimensions but not across channels.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Variable bit rates", "weight": 1.0} -->

An example of learned scale parameters is shown in Figure 3A. For more fine-grained control over bit rates, the optimized scales can be interpolated.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Encoder, decoder, and entropy model", "weight": 1.0} -->

We use common convolutional neural networks for the encoder and the decoder of the compressive autoencoder. Our architecture was inspired by the work of Shi et al., who demonstrated that super-resolution can be achieved much more efficiently by operating in the low-resolution space, that is, by convolving images and then upsampling instead of upsampling first and then convolving an image.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Encoder, decoder, and entropy model", "weight": 1.0} -->

The first two layers of the encoder perform preprocessing, namely mirror padding and a fixed pixel-wise normalization. The mirror-padding was chosen such that the output of the encoder has the same spatial extent as an 8 times downsampled image. The normalization centers the distribution of each channel's values and ensures it has approximately unit variance. Afterwards, the image is convolved and spatially downsampled while at the same time increasing the number of channels to 128. This is followed by three residual blocks, where each block consists of an additional two convolutional layers with 128 filters each. A final convolutional layer is applied and the coefficients downsampled again before quantization through rounding to the nearest integer.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Encoder, decoder, and entropy model", "weight": 1.0} -->

The decoder mirrors the architecture of the encoder (Figure 9). Instead of mirror-padding and valid convolutions, we use zero-padded convolutions. Upsampling is achieved through convolution followed by a reorganization of the coefficients. This reorganization turns a tensor with many channels into a tensor of the same dimensionality but with fewer channels and larger spatial extent. A convolution and reorganization of coefficients together form a sub-pixel convolution layer. Following three residual blocks, two sub-pixel convolution layers upsample the image to the resolution of the input. Finally, after denormalization, the pixel values are clipped to the range of 0 to 255. Similar to how we deal with gradients of the rounding function, we redefine the gradient of the clipping function to be 1 outside the clipped range. This ensures that the training signal is non-zero even when the decoded pixels are outside this range (Appendix A.1).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Encoder, decoder, and entropy model", "weight": 1.0} -->

To model the distribution of coefficients and estimate the bit rate, we use independent Gaussian scale mixtures (GSMs), where $i$ and $j$ iterate over spatial positions, and $k$ iterates over channels of the coefficients for a single image $\mathbf{z}$. GSMs are well established as useful building blocks for modelling filter responses of natural images. We used 6 scales in each GSM. Rather than using the more common parametrization above, we parametrized the GSM so that it can be easily used with gradient based methods, optimizing log-weights and log-precisions rather than weights and variances. We note that the leptokurtic nature of GSMs means that the rate term encourages sparsity of coefficients.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Encoder, decoder, and entropy model", "weight": 1.0} -->

All networks were implemented in Python using Theano and Lasagne. For entropy encoding of the quantized coefficients, we first created Laplace-smoothed histogram estimates of the coefficient distributions across a training set. The estimated probabilities were then used with a publicly available BSD licensed implementation of a range coder^22^2

<!-- chunk {"id": "body-0023", "role": "body", "section": "Incremental training", "weight": 1.0} -->

All models were trained using Adam applied to batches of 32 images $128 \times 128$ pixels in size. We found it beneficial to optimize coefficients in an incremental manner (Figure 3B). This is done by introducing an additional binary mask $\mathbf{m}$, Initially, all but 2 entries of the mask are set to zero. Networks are trained until performance improvements reach below a threshold, and then another coefficient is enabled by setting an entry of the binary mask to 1. After all coefficients have been enabled, the learning rate is reduced from an initial value of $10^{- 4}$ to $10^{- 5}$. Training was performed for up to $10^{6}$ updates but usually reached good performance much earlier.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Incremental training", "weight": 1.0} -->

After a model has been trained for a fixed rate-distortion trade-off ($\beta$), we introduce and fine-tune scale parameters (Equation 9) for other values of $\beta$ while keeping all other parameters fixed. Here we used an initial learning rate of $10^{- 3}$ and continuously decreased it by a factor of $\tau^{\kappa}/{({\tau + t})}^{\kappa}$, where $t$ is the current number of updates performed, $\kappa =.8$, and $\tau = 1000$. Scales were optimized for 10,000 iterations. For even more fine-grained control over the bit rates, we interpolated between scales optimized for nearby rate-distortion tradeoffs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Natural images", "weight": 1.0} -->

We trained compressive autoencoders on 434 high quality images licensed under creative commons and obtained from flickr.com. The images were downsampled to below $1536 \times 1536$ pixels and stored as lossless PNGs to avoid compression artefacts. From these images, we extracted $128 \times 128$ crops to train the network. Mean squared error was used as a measure of distortion during training. Hyperparameters affecting network architecture and training were evaluated on a small set of held-out Flickr images. For testing, we use the commonly used Kodak PhotoCD dataset of 24 uncompressed $768 \times 512$ pixel images^33^3 We compared our method to JPEG, JPEG 2000, and the RNN-based method of ^44^4We used the code which was made available on We note that at the time of this writing, this implementation does not include entropy coding as in the paper of Toderici et al.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Natural images", "weight": 1.0} -->

Bits for header information were not counted towards the bit rate of JPEG and JPEG 2000. Among the different variants of JPEG, we found that optimized JPEG with 4:2:0 chroma sub-sampling generally worked best (Appendix A.2).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Natural images", "weight": 1.0} -->

While fine-tuning a single compressive autoencoder for a wide range of bit rates worked well, optimizing all parameters of a network for a particular rate distortion trade-off still worked better. We here chose the compromise of combining autoencoders trained for low, medium or high bit rates (see Appendix A.4 for details).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Natural images", "weight": 1.0} -->

For each image and bit rate, we choose the autoencoder producing the smallest distortion. This increases the time needed to compress an image, since an image has to be encoded and decoded multiple times. However, decoding an image is still as fast, since it only requires choosing and running one decoder network. A more efficient but potentially less performant solution would be to always choose the same autoencoder for a given rate-distortion tradeoff. We added 1 byte to the coding cost to encode which autoencoder of an ensemble is used.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Natural images", "weight": 1.0} -->

Rate-distortion curves averaged over all test images are shown in Figure 4. We evaluated the different methods in terms of PSNR, SSIM, and multiscale SSIM. We used the implementation of van der Walt et al. for SSIM and the implementation of Toderici et al. for MS-SSIM. We find that in terms of PSNR, our method performs similar to JPEG 2000 although slightly worse at low and medium bit rates and slightly better at high bit rates. In terms of SSIM, our method outperforms all other tested methods. MS-SSIM produces very similar scores for all methods, except at very low bit rates. However, we also find these results to be highly image dependent. Results for individual images are provided as supplementary material^55^5 In Figure 5 we show crops of images compressed to low bit rates. In line with quantitative results, we find that JPEG 2000 reconstructions appear visually more similar to CAE reconstructions than those of other methods. However, artefacts produced by JPEG 2000 seem more noisy than CAE's, which are smoother and sometimes appear Gábor-filter-like.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Natural images", "weight": 1.0} -->

To quantify the subjective quality of compressed images, we ran a mean opinion score (MOS) test. While MOS tests have their limitations, they are a widely used standard for evaluating perceptual quality. Our MOS test set included the 24 full-resolution uncompressed originals from the Kodak dataset, as well as the same images compressed using each of four algorithms at or near three different bit rates: $0.25$, $0.372$ and $0.5$ bits per pixel. Only the low-bit-rate CAE was included in this test.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Natural images", "weight": 1.0} -->

For each image, we chose the CAE setting which produced the highest bit rate but did not exceed the target bit rate. The average bit rates of CAE compressed images were $0.24479$, $0.36446$, and $0.48596$, respectively. We then chose the smallest quality factor for JPEG and JPEG 2000 for which the bit rate exceeded that of the CAE. The average bit rates for JPEG were $0.25221$, $0.37339$ and $0.49534$, for JPEG 2000 $0.24631$, $0.36748$ and $0.49373$. For some images the bit rate of the CAE at the lowest setting was still higher than the target bit rate. These images were excluded from the final results, leaving 15, 21, and 23 images, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Natural images", "weight": 1.0} -->

The perceptual quality of the resulting $273$ images was rated by $n = 24$ non-expert evaluators. One evaluator did not finish the experiment, so her data was discarded. The images were presented to each individual in a random order. The evaluators gave a discrete opinion score for each image from a scale between $1$ (bad) to $5$ (excellent). Before the rating began, subjects were presented an uncompressed calibration image of the same dimensions as the test images (but not from the Kodak dataset). They were then shown four versions of the calibration image using the worst quality setting of all four compression methods, and given the instruction "These are examples of compressed images. These are some of the worst quality examples."

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have introduced a simple but effective way of dealing with non-differentiability in training autoencoders for lossy compression. Together with an incremental training strategy, this enabled us to achieve better performance than JPEG 2000 in terms of SSIM and MOS scores. Notably, this performance was achieved using an efficient convolutional architecture, combined with simple rounding-based quantization and a simple entropy coding scheme. Existing codecs often benefit from hardware support, allowing them to run at low energy costs. However, hardware chips optimized for convolutional neural networks are likely to be widely available soon, given that these networks are now key to good performance in so many applications.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

While other trained algorithms have been shown to provide similar results as JPEG 2000, to our knowledge this is the first time that an end-to-end trained architecture has been demonstrated to achieve this level of performance on high-resolution images. An end-to-end trained autoencoder has the advantage that it can be optimized for arbitrary metrics. Unfortunately, research on perceptually relevant metrics suitable for optimization is still in its infancy. While perceptual metrics exist which correlate well with human perception for certain types of distortions, developing a perceptual metric which can be optimized is a more challenging task, since this requires the metric to behave well for a much larger variety of distortions and image pairs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

In future work, we would like to explore the optimization of compressive autoencoders for different metrics. A promising direction was presented by Bruna et al., who achieved interesting super-resolution results using metrics based on neural networks trained for image classification. Gatys et al. used similar representations to achieve a breakthrough in perceptually meaningful style transfer. An alternative to perceptual metrics may be to use generative adversarial networks. Building on the work of Bruna et al. and Dosovitskiy & Brox, Ledig et al. recently demonstrated impressive super-resolution results by combining GANs with feature-based metrics.
