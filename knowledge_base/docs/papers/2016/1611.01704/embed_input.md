<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

End-to-end Optimized Image Compression

Topics include Gradient descent, Stochastic gradients, Neural networks, Convolutional networks, Variational autoencoders, Autoencoders, Online algorithms, Control, Joint photographic experts group, Image compression, Convolutional neural network.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe an image compression method, consisting of a nonlinear analysis transformation, a uniform quantizer, and a nonlinear synthesis transformation. The transforms are constructed in three successive stages of convolutional linear filters and nonlinear activation functions. Unlike most convolutional neural networks, the joint nonlinearity is chosen to implement a form of local gain control, inspired by those used to model biological neurons. Using a variant of stochastic gradient descent, we jointly optimize the entire model for rate-distortion performance over a database of training images, introducing a continuous proxy for the discontinuous loss function arising from the quantizer. Under certain conditions, the relaxed loss function may be interpreted as the log likelihood of a generative model, as implemented by a variational autoencoder. Unlike these models, however, the compression model must operate at any given point along the rate-distortion curve, as specified by a trade-off parameter. Across an independent set of test images, we find that the optimized method generally exhibits better rate-distortion performance than the standard JPEG and JPEG 2000 compression methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

More importantly, we observe a dramatic improvement in visual quality for all images at all bit rates, which is supported by objective quality estimates using MS-SSIM.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data compression is a fundamental and well-studied problem in engineering, and is commonly formulated with the goal of designing codes for a given discrete data ensemble with minimal entropy. The solution relies heavily on knowledge of the probabilistic structure of the data, and thus the problem is closely related to probabilistic source modeling. However, since all practical codes must have finite entropy, continuous-valued data (such as vectors of image pixel intensities) must be quantized to a finite set of discrete values, which introduces error. In this context, known as the *lossy compression problem*, one must trade off two competing costs: the entropy of the discretized representation (*rate*) and the error arising from the quantization (*distortion*). Different compression applications, such as data storage or transmission over limited-capacity channels, demand different rate--distortion trade-offs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Joint optimization of rate and distortion is difficult. Without further constraints, the general problem of optimal quantization in high-dimensional spaces is intractable. For this reason, most existing image compression methods operate by linearly transforming the data vector into a suitable continuous-valued representation, quantizing its elements independently, and then encoding the resulting discrete representation using a lossless *entropy code*. This scheme is called *transform coding* due to the central role of the transformation. For example, JPEG uses a discrete cosine transform on blocks of pixels, and JPEG 2000 uses a multi-scale orthogonal wavelet decomposition. Typically, the three components of transform coding methods -- transform, quantizer, and entropy code -- are separately optimized (often through manual parameter adjustment).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We have developed a framework for end-to-end optimization of an image compression model based on *nonlinear* transforms (figure 1). Previously, we demonstrated that a model consisting of linear--nonlinear block transformations, optimized for a measure of perceptual distortion, exhibited visually superior performance compared to a model optimized for mean squared error (MSE). Here, we optimize for MSE, but use a more flexible transforms built from cascades of linear convolutions and nonlinearities. Specifically, we use a generalized divisive normalization (GDN) joint nonlinearity that is inspired by models of neurons in biological visual systems, and has proven effective in Gaussianizing image densities. This cascaded transformation is followed by uniform scalar quantization (i.e., each element is rounded to the nearest integer), which effectively implements a parametric form of vector quantization on the original image space. The compressed image is reconstructed from these quantized values using an approximate parametric nonlinear inverse transform.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For any desired point along the rate--distortion curve, the parameters of both analysis and synthesis transforms are jointly optimized using stochastic gradient descent. To achieve this in the presence of quantization (which produces zero gradients almost everywhere), we use a proxy loss function based on a continuous relaxation of the probability model, replacing the quantization step with additive uniform noise. The relaxed rate--distortion optimization problem bears some resemblance to those used to fit generative image models, and in particular variational autoencoders, but differs in the constraints we impose to ensure that it approximates the discrete problem all along the rate--distortion curve. Finally, rather than reporting differential or discrete entropy estimates, we implement an entropy code and report performance using actual bit rates, thus demonstrating the feasibility of our solution as a complete lossy compression method.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Choice of forward, inverse, and perceptual transforms", "weight": 1.0} -->

Most compression methods are based on orthogonal linear transforms, chosen to reduce correlations in the data, and thus to simplify entropy coding. But the joint statistics of linear filter responses exhibit strong higher order dependencies. These may be significantly reduced through the use of joint local nonlinear gain control operations, inspired by models of visual neurons. Cascaded versions of such models have been used to capture multiple stages of visual transformation. Some earlier results suggest that incorporating local normalization in linear block transform coding methods can improve coding performance, and can improve object recognition performance of cascaded convolutional neural networks. However, the normalization parameters in these cases were not optimized for the task. Here, we make use of a generalized divisive normalization (GDN) transform with optimized parameters, that we have previously shown to be highly efficient in Gaussianizing the local joint statistics of natural images, much more so than cascades of linear transforms followed by pointwise nonlinearities.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Choice of forward, inverse, and perceptual transforms", "weight": 1.0} -->

Note that some training algorithms for deep convolutional networks incorporate "batch normalization", rescaling the responses of linear filters in the network so as to keep it in a reasonable operating range. This type of normalization is different from local gain control in that the rescaling factor is identical across all spatial locations. Moreover, once the training is completed, the scaling parameters are typically fixed, which turns the normalization into an affine transformation with respect to the data -- unlike GDN, which is spatially adaptive and can be highly nonlinear.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Choice of forward, inverse, and perceptual transforms", "weight": 1.0} -->

Specifically, our analysis transform $g_{a}$ consists of three stages of convolution, subsampling, and divisive normalization. We represent the $i$th input channel of the $k$th stage at spatial location $(m,n)$ as $u_{i}^{(k)}{(m,n)}$. The input image vector $\mathbf{x}$ corresponds to $u_{i}^{}{(m,n)}$, and the output vector $\mathbf{y}$ is $u_{i}^{}{(m,n)}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Choice of forward, inverse, and perceptual transforms", "weight": 1.0} -->

The full set of $h$, $c$, $\beta$, and $\gamma$ parameters (across all three stages) constitute the parameter vector $\mathbf{\phi}$ to be optimized.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Choice of forward, inverse, and perceptual transforms", "weight": 1.0} -->

Analogously, the synthesis transform $g_{s}$ consists of three stages, with the order of operations reversed within each stage, downsampling replaced by upsampling, and GDN replaced by an approximate inverse we call IGDN (more details in the appendix). We define ${\hat{u}}_{i}^{(k)}{(m,n)}$ as the input to the $k$th synthesis stage, such that $\hat{\mathbf{y}}$ corresponds to ${\hat{u}}_{i}^{}{(m,n)}$, and $\hat{\mathbf{x}}$ to ${\hat{u}}_{i}^{}{(m,n)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Choice of forward, inverse, and perceptual transforms", "weight": 1.0} -->

Analogously, the set of $\hat{h}$, $\hat{c}$, $\hat{\beta}$, and $\hat{\gamma}$ make up the parameter vector $\mathbf{θ}$. Note that the down/upsampling operations can be implemented jointly with their adjacent convolution, improving computational efficiency.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Choice of forward, inverse, and perceptual transforms", "weight": 1.0} -->

In previous work, we used a perceptual transform $g_{p}$, separately optimized to mimic human judgements of grayscale image distortions, and showed that a set of one-stage transforms optimized for this distortion measure led to visually improved results. Here, we set the perceptual transform $g_{p}$ to the identity, and use mean squared error (MSE) as the metric (i.e., ${d{({\mathbf{z}},\hat{\mathbf{z}})}} = {\|{{\mathbf{z}} - \hat{\mathbf{z}}}\|}_{2}^{2}$). This allows a more interpretable comparison to existing methods, which are generally optimized for MSE, and also allows optimization for color images, for which we do not currently have a reliable perceptual metric.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimization of nonlinear transform coding model", "weight": 1.0} -->

Our objective is to minimize a weighted sum of the rate and distortion, $R + {\lambdaD}$, over the parameters of the analysis and synthesis transforms and the entropy code, where $\lambda$ governs the trade-off between the two terms (figure 2, left panel). Rather than attempting optimal quantization directly in the image space, which is intractable due to the high dimensionality, we instead assume a fixed uniform scalar quantizer in the code space, and aim to have the nonlinear transformations warp the space in an appropriate way, effectively implementing a parametric form of vector quantization (figure 1).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimization of nonlinear transform coding model", "weight": 1.0} -->

where both expectations will be approximated by averages over a training set of images. Given a powerful enough set of transformations, we can assume without loss of generality that the quantization bin size is always one and the representing values are at the centers of the bins. That is,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimization of nonlinear transform coding model", "weight": 1.0} -->

where index $i$ runs over all elements of the vectors, including channels and spatial locations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimization of nonlinear transform coding model", "weight": 1.0} -->

Note that both terms in depend on the quantized values, and the derivatives of the quantization function are zero almost everywhere, rendering gradient descent ineffective. To allow optimization via stochastic gradient descent, we replace the quantizer with an additive i.i.d. uniform noise source $\Delta{\mathbf{y}}$, which has the same width as the quantization bins (one). This relaxed formulation has two desirable properties.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimization of nonlinear transform coding model", "weight": 1.0} -->

which implies that the differential entropy of $\overset{\sim}{\mathbf{y}}$ can be used as an approximation of the entropy of $\mathbf{q}$. Second, independent uniform noise approximates quantization error in terms of its marginal moments, and is frequently used as a model of quantization error. We can thus use the same approximation for our measure of distortion. We examine the empirical quality of these rate and distortion approximations in section 4.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimization of nonlinear transform coding model", "weight": 1.0} -->

We assume independent marginals in the code space for both the relaxed probability model of $\overset{\sim}{\mathbf{y}}$ and the entropy code, and model the marginals $p_{{\overset{\sim}{y}}_{i}}$ non-parametrically to reduce model error. Specifically, we use finely sampled piecewise linear functions which we update similarly to one-dimensional histograms (see appendix). Since $p_{{\overset{\sim}{y}}_{i}} = {{p_{y_{i}} \ast \mathcal{U}}{}}$ is effectively smoothed by a box-car filter -- the uniform density on the unit interval, $\mathcal{U}{}$ -- the model error can be made arbitrarily small by decreasing the sampling interval.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimization of nonlinear transform coding model", "weight": 1.0} -->

where vector ${\mathbf{ψ}}^{(i)}$ parameterizes the piecewise linear approximation of $p_{{\overset{\sim}{y}}_{i}}$ (trained jointly with $\mathbf{θ}$ and $\mathbf{φ}$). This is continuous and differentiable, and thus well-suited for stochastic optimization.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Relationship to variational generative image models", "weight": 1.0} -->

We derived our formulation directly from the classical rate--distortion optimization problem. However, once the transition to a continuous loss function is made, the optimization problem resembles those encountered in fitting generative models of images, and can more specifically be cast in the context of variational autoencoders. In Bayesian variational inference, we are given an ensemble of observations of a random variable $x$ along with a generative model $p_{x|y}{(\left. x \middle| y \right.)}$. We seek to find a posterior $p_{y|x}{(\left. y \middle| x \right.)}$, which generally cannot be expressed in closed form. The approach followed by consists of approximating this posterior with a density $q{(\left. y \middle| x \right.)}$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Relationship to variational generative image models", "weight": 1.0} -->

where $\mathcal{U}{({\overset{\sim}{y}}_{i};y_{i},1)}$ is the uniform density on the unit interval centered on $y_{i}$. With this, the first term in the Kullback--Leibler divergence is constant; the second term corresponds to the distortion, and the third term corresponds to the rate (both up to additive constants). Note that if a perceptual transform $g_{p}$ is used, or the metric $d$ is not Euclidean, $p_{{\mathbf{x}}|\overset{\sim}{\mathbf{y}}}$ is no longer Gaussian, and equivalence to variational autoencoders cannot be guaranteed, since the distortion term may not correspond to a normalizable density. For any affine and invertible perceptual transform and any translation-invariant metric, it can be shown to correspond to the density

<!-- chunk {"id": "body-0024", "role": "body", "section": "Relationship to variational generative image models", "weight": 1.0} -->

where $Z{(\lambda)}$ normalizes the density (but need not be computed to fit the model).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Relationship to variational generative image models", "weight": 1.0} -->

Despite the similarity between our nonlinear transform coding framework and that of variational autoencoders, it is worth noting several fundamental differences. First, variational autoencoders are continuous-valued, and digital compression operates in the discrete domain. Comparing differential entropy with (discrete) entropy, or entropy with an actual bit rate, can potentially lead to misleading results. In this paper, we use the continous domain strictly for optimization, and perform the evaluation on actual bit rates, which allows comparison to existing image coding methods. We assess the quality of the rate and distortion approximations empirically.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Relationship to variational generative image models", "weight": 1.0} -->

Second, generative models aim to minimize differential entropy of the data ensemble under the model, i.e., explaining fluctuations in the data. This often means minimizing the variance of a "slack" term like, which in turn *maximizes* $\lambda$. Transform coding methods, on the other hand, are optimized to achieve the best trade-off between having the model explain the data (which increases rate and decreases distortion), and having the slack term explain the data (which decreases rate and increases distortion). The overall performance of a compression model is determined by the shape of the convex hull of attainable model distortions and rates, over all possible values of the model parameters. Finding this convex hull is equivalent to optimizing the model for *particular* values of $\lambda$ (see figure 2). In contrast, generative models operate in a regime where $\lambda$ is inferred and ideally approaches infinity for noiseless data, which corresponds to the regime of lossless compression. Even so, lossless compression methods still need to operate in a discretized space, typically directly on quantized luminance values.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Relationship to variational generative image models", "weight": 1.0} -->

For generative models, the discretization of luminance values is usually considered a nuisance, although there are examples of generative models that operate on quantized pixel values.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Relationship to variational generative image models", "weight": 1.0} -->

Finally, although correspondence between the typical slack term of a generative model (figure 3, left panel) and the distortion metric in rate--distortion optimization holds for simple metrics (e.g., Euclidean distance), a more general perceptual measure would be considered a peculiar choice from a generative modeling perspective, if it corresponds to a density at all.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental results", "weight": 1.0} -->

We jointly optimized the full set of parameters $\mathbf{\phi}$, $\mathbf{θ}$, and all $\mathbf{ψ}$ over a subset of the ImageNet database consisting of 6507 images using stochastic descent. This optimization was performed separately for each $\lambda$, yielding separate transforms and marginal probability models for each value.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental results", "weight": 1.0} -->

For the grayscale analysis transform, we used 128 filters (size $9 \times 9$) in the first stage, each subsampled by a factor of 4 vertically and horizontally. The remaining two stages retain the number of channels, but use filters operating across all input channels ($5 \times 5 \times 128$), with outputs subsampled by a factor of 2 in each dimension. The net output thus has half the dimensionality of the input. The synthesis transform is structured analogously. For RGB images, we trained a separate set of models, with the first stage augmented to operate across three (color) input channels. For the two largest values of $\lambda$, and for RGB models, we increased the network capacity by increasing the number of channels in each stage to 256 and 192, respectively. Further details about the parameterization of the transforms and their training can be found in the appendix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental results", "weight": 1.0} -->

We first verified that the continuously-relaxed loss function given in section 3 provides a good approximation to the actual rate--distortion values obtained with quantization (figure 4). The relaxed distortion term appears to be mostly unbiased, and exhibits a relatively small variance. The relaxed (differential) entropy provides a somewhat positively biased estimate of the discrete entropy for the coarser quantization regime, but the bias disappears for finer quantization, as expected. Note that since the values of $\lambda$ do not have any intrinsic meaning, but serve only to map out the convex hull of optimal points in the rate--distortion plane (figure 2, left panel), a constant bias in either of the terms would simply alter the effective value of $\lambda$, with no effect on the compression performance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental results", "weight": 1.0} -->

Proposed method, 3986 bytes (0.113 bit/px), PSNR: luma 27.01 dB/chroma 34.16 dB, MS-SSIM: 0.9039

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental results", "weight": 1.0} -->

JPEG 2000, 4004 bytes (0.113 bit/px), PSNR: luma 26.61 dB/chroma 33.88 dB, MS-SSIM: 0.8860
Figure 5: A heavily compressed example image, 752 × 376 pixels. Note the appearance of artifacts, especially near edges, in both the JPEG and JPEG2000 images.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental results", "weight": 1.0} -->

We compare the rate--distortion performance of our method to two standard methods: JPEG and JPEG 2000. For our method, all images were compressed using uniform quantization (the continuous relaxation using additive noise was used only for training purposes). To make the comparisons more fair, we implemented a simple entropy code based on the context-based adaptive binary arithmetic coding framework (CABAC; ). All sideband information needed by the decoder (size of images, value of $\lambda$, etc.) was included in the bit stream (see appendix). Note that although the computational costs for training our models are quite high, encoding or decoding an image with the trained models is efficient, requiring only execution of the optimized analysis transformation and quantizer, or the synthesis transformation, respectively. Evaluations were performed on the Kodak image dataset^11^1Downloaded from an uncompressed set of images commonly used to evaluate image compression methods. We also examined a set of relatively standard (if outdated) images used by the compression community (known by the names "Lena", "Barbara", "Peppers", and "Mandrill") as well as a set of our own digital photographs.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental results", "weight": 1.0} -->

None of these test images was included in the training set. All test images, compressed at a variety of bit rates using all three methods, along with their associated rate--distortion curves, are available online at

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental results", "weight": 1.0} -->

Although we used MSE as a distortion metric for training, the appearance of compressed images is both qualitatively different and substantially improved, compared to JPEG and JPEG 2000. As an example, figure 5 shows an image compressed using our method optimized for a low value of $\lambda$ (and thus, a low bit rate), compared to JPEG/JPEG 2000 images compressed at equal or greater bit rates. The image compressed with our method has less detail than the original (not shown, but available online), with fine texture and other patterns often eliminated altogether, but this is accomplished in a way that preserves the smoothness of contours and sharpness of many of the edges, giving them a natural appearance. By comparison, the JPEG and JPEG 2000 images exhibit artifacts that are common to all linear transform coding methods: since local features (edges, contours, texture elements, etc.) are represented using particular combinations of localized linear basis functions, independent scalar quantization of the transform coefficients causes imbalances in these combinations, and leads to visually disturbing blocking, aliasing, and ringing artifacts that reflect the underlying basis functions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental results", "weight": 1.0} -->

Remarkably, we find that the perceptual advantages of our method hold for *all* images tested, and at all bit rates. The progression from high to low bit rates is shown for an example image in figure 6 (additional examples provided in appendix and online). As bit rate is reduced, JPEG and JPEG 2000 degrade their approximation of the original image by coarsening the precision of the coefficients of linear basis functions, thus exposing the visual appearance of those basis functions. On the other hand, our method appears to progressively simplify contours and other image features, effectively concealing the underlying quantization of the representation. Consistent with the appearance of these example images, we find that distortion measured with a perceptual metric (MS-SSIM; ), indicates substantial improvements across all tested images and bit rates (figure 7; additional examples provided in the appendix and online). Finally, when quantified with PSNR, we find that our method exhibits better rate--distortion performance than both JPEG and JPEG 2000 for most (but not all) test images, especially at the lower bit rates.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have presented a complete image compression method based on *nonlinear transform coding*, and a framework to optimize it end-to-end for rate--distortion performance. Our compression method offers improvements in rate--distortion performance over JPEG and JPEG 2000 for most images and bit rates. More remarkably, although the method was optimized using mean squared error as a distortion metric, the compressed images are much more natural in appearance than those compressed with JPEG or JPEG 2000, both of which suffer from the severe artifacts commonly seen in linear transform coding methods. Consistent with this, perceptual quality (as estimated with the MS-SSIM index) exhibits substantial improvement across all test images and bit rates. We believe this visual improvement arises because the cascade of biologically-inspired nonlinear transformations in the model have been optimized to capture the features and attributes of images that are represented in the statistics of the data, parallel to the processes of evolution and development that are believed to have shaped visual representations within the human brain. Nevertheless, additional visual improvements might be possible if the method were optimized using a perceptual metric in place of MSE.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

For comparison to linear transform coding methods, we can interpret our analysis transform as a single-stage linear transform followed by a complex vector quantizer. As in many other optimized representations -- e.g., sparse coding -- as well as many engineered representations -- e.g., the steerable pyramid, curvelets, and dual-tree complex wavelets -- the filters in this first stage are localized and oriented and the representation is *overcomplete*. Whereas most transform coding methods use complete (often orthogonal) linear transforms with spatially separable filters, the overcompleteness and orientation tuning of our initial transform may explain the ability of the model to better represent features and contours with continuously varying orientation, position and scale.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our work is related to two previous publications that optimize image representations with the goal of image compression. introduce an interesting hierarchical representation of images, in which degradations are more natural looking than those of linear representations. However, rather than optimizing directly for rate--distortion performance, their modeling is generative. Due to the differences between these approaches (as outlined in section 3.1), their procedure of obtaining coding representations from the generative model (scalar quantization, and elimination of hierarchical levels of the representation) is less systematic than our approach and unlikely to be optimal. Further, no entropy code is provided, and the authors therefore resort to comparing entropy estimates to bit rates of established compression methods, which can be unreliable. The model developed by is optimized to provide various rate--distortion trade-offs and directly output a binary representation, making it more easily comparable to other image compression methods. Moreover, their formulation has the advantage over ours that a single representation is sought for all rate points. However, it is not clear whether their formulation necessarily leads to rate--distortion optimality (and their empirical results suggest that this is not the case).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

We are currently testing models that use simpler rectified-linear or sigmoidal nonlinearities, to determine how much of the performance and visual quality of our results is due to use of biologically-inspired joint nonlinearities. Preliminary results indicate that qualitatively similar results are achievable with other activation functions we tested, but that rectified linear units generally require a substantially larger number of model parameters/stages to achieve the same rate--distortion performance as the GDN/IGDN nonlinearities. This suggests that GDN/IGDN transforms are more efficient for compression, producing better models with fewer stages of processing (as we previously found for density estimation; ), which might be an advantage for deployment of our method, say, in embedded systems. However, such conclusions are based on a somewhat limited set of experiments and should at this point be considered provisional. More generally, GDN represents a multivariate generalization of a particular type of sigmoidal function. As such, the observed efficiency advantage relative to pointwise nonlinearities is expected, and a variant of a universal function approximation theorem (e.g., ) should hold.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

The rate--distortion objective can be seen as a particular instantiation of the general unsupervised learning or density estimation problems. Since the transformation to a discrete representation may be viewed as a form of classification, it is worth considering whether our framework offers any insights that might be transferred to more specific supervised learning problems, such as object recognition. For example, the additive noise used in the objective function as a relaxation of quantization might also serve the purpose of making supervised classification networks more robust to small perturbations, and thus allow them to avoid catastrophic "adversarial" failures that have been demonstrated in previous work. In any case, our results provide a strong example of the power of end-to-end optimization in achieving a new solution to a classical problem.
