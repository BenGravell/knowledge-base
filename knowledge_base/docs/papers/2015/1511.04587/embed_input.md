<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accurate Image Super-Resolution Using Very Deep Convolutional Networks

Topics include Image super-resolution, Convolutional networks, Very deep networks, Residual learning, Gradient clipping, High learning rate, VGG-style networks, VDSR.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

VDSR shows that much deeper CNNs can improve single-image super-resolution when trained as residual predictors with aggressive learning rates and gradient clipping. It marks an important transition from shallow SRCNN-style mappings to deeper residual restoration networks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a highly accurate single-image super-resolution (SR) method. Our method uses a very deep convolutional network inspired by VGG-net used for ImageNet classification \cite{simonyan2015very}. We find increasing our network depth shows a significant improvement in accuracy. Our final model uses 20 weight layers. By cascading small filters many times in a deep network structure, contextual information over large image regions is exploited in an efficient way. With very deep networks, however, convergence speed becomes a critical issue during training. We propose a simple yet effective training procedure. We learn residuals only and use extremely high learning rates (10^ times higher than SRCNN \cite{dong2015image}) enabled by adjustable gradient clipping. Our proposed method performs better than existing methods in accuracy and visual improvements in our results are easily noticeable.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address the problem of generating a high-resolution (HR) image given a low-resolution (LR) image, commonly referred as single image super-resolution (SISR). SISR is widely used in computer vision applications ranging from security and surveillance imaging to medical imaging where more image details are required on demand.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many SISR methods have been studied in the computer vision community. Early methods include interpolation such as bicubic interpolation and Lanczos resampling more powerful methods utilizing statistical image priors or internal patch recurrence.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Currently, learning methods are widely used to model a mapping from LR to HR patches. Neighbor embedding methods interpolate the patch subspace. Sparse coding methods use a learned compact dictionary based on sparse signal representation. Lately, random forest and convolutional neural network (CNN) have also been used with large improvements in accuracy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among them, Dong et al. has demonstrated that a CNN can be used to learn a mapping from LR to HR in an end-to-end manner. Their method, termed SRCNN, does not require any engineered features that are typically necessary in other methods and shows the state-of-the-art performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While SRCNN successfully introduced a deep learning technique into the super-resolution (SR) problem, we find its limitations in three aspects: first, it relies on the context of small image regions; second, training converges too slowly; third, the network only works for a single scale.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a new method to practically resolve the issues.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Context We utilize contextual information spread over very large image regions. For a large scale factor, it is often the case that information contained in a small patch is not sufficient for detail recovery (ill-posed). Our very deep network using large receptive field takes a large image context into account.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convergence We suggest a way to speed-up the training: residual-learning CNN and extremely high learning rates. As LR image and HR image share the same information to a large extent, explicitly modelling the residual image, which is the difference between HR and LR images, is advantageous. We propose a network structure for efficient learning when input and output are highly correlated. Moreover, our initial learning rate is $10^{4}$ times higher than that of SRCNN. This is enabled by residual-learning and gradient clipping.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scale Factor We propose a single-model SR approach. Scales are typically user-specified and can be arbitrary including fractions. For example, one might need smooth zoom-in in an image viewer or resizing to a specific dimension. Training and storing many scale-dependent models in preparation for all possible scenarios is impractical. We find a single convolutional network is sufficient for multi-scale-factor super-resolution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contribution In summary, in this work, we propose a highly accurate SR method based on a very deep convolutional network. Very deep networks converge too slowly if small learning rates are used. Boosting convergence rate with high learning rates lead to exploding gradients and we resolve the issue with residual-learning and gradient clipping. In addition, we extend our work to cope with multi-scale SR problem in a single network. Our method is relatively accurate and fast in comparison to state-of-the-art methods as illustrated in Figure 1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Convolutional Network for Image Super-Resolution", "weight": 1.0} -->

Model SRCNN consists of three layers: patch extraction/representation, non-linear mapping and reconstruction. Filters of spatial sizes $9 \times 9$, $1 \times 1$, and $5 \times 5$ were used respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Convolutional Network for Image Super-Resolution", "weight": 1.0} -->

In, Dong et al. attempted to prepare deeper models, but failed to observe superior performance after a week of training. In some cases, deeper models gave inferior performance. They conclude that deeper networks do not result in better performance (Figure 9).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Convolutional Network for Image Super-Resolution", "weight": 1.0} -->

However, we argue that increasing depth significantly boosts performance. We successfully use 20 weight layers ($3 \times 3$ for each layer). Our network is very deep (20 vs. 3 ) and information used for reconstruction (receptive field) is much larger ($41 \times 41$ vs. $13 \times 13$).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convolutional Network for Image Super-Resolution", "weight": 1.0} -->

Training For training, SRCNN directly models high-resolution images. A high-resolution image can be decomposed into a low frequency information (corresponding to low-resolution image) and high frequency information (residual image or image details). Input and output images share the same low-frequency information. This indicates that SRCNN serves two purposes: carrying the input to the end layer and reconstructing residuals. Carrying the input to the end is conceptually similar to what an auto-encoder does. Training time might be spent on learning this auto-encoder so that the convergence rate of learning the other part (image details) is significantly decreased. In contrast, since our network models the residual images directly, we can have much faster convergence with even better accuracy.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convolutional Network for Image Super-Resolution", "weight": 1.0} -->

Scale As in most existing SR methods, SRCNN is trained for a single scale factor and is supposed to work only with the specified scale. Thus, if a new scale is on demand, a new model has to be trained. To cope with multiple scale SR (possibly including fractional factors), we need to construct individual single scale SR system for each scale of interest.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convolutional Network for Image Super-Resolution", "weight": 1.0} -->

However, preparing many individual machines for all possible scenarios to cope with multiple scales is inefficient and impractical. In this work, we design and train a single network to handle multiple scale SR problem efficiently. This turns out to work very well. Our single machine is compared favorably to a single-scale expert for the given sub-task. For three scales factors ($\times 2,3,4$), we can reduce the number of parameters by three-fold.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Convolutional Network for Image Super-Resolution", "weight": 1.0} -->

In addition to the aforementioned issues, there are some minor differences. Our output image has the same size as the input image by padding zeros every layer during training whereas output from SRCNN is smaller than the input. Finally, we simply use the same learning rates for all layers while SRCNN uses different learning rates for different layers in order to achieve stable convergence.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

For SR image reconstruction, we use a very deep convolutional network inspired by Simonyan and Zisserman. The configuration is outlined in Figure 2. We use $d$ layers where layers except the first and the last are of the same type: 64 filter of the size $3 \times 3 \times 64$, where a filter operates on $3 \times 3$ spatial region across 64 channels (feature maps). The first layer operates on the input image. The last layer, used for image reconstruction, consists of a single filter of size $3 \times 3 \times 64$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

The network takes an interpolated low-resolution image (to the desired size) as input and predicts image details. Modelling image details is often used in super-resolution methods and we find that CNN-based methods can benefit from this domain-specific knowledge.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

In this work, we demonstrate that explicitly modelling image details (residuals) has several advantages. These are further discussed later in Section 4.2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

One problem with using a very deep network to predict dense outputs is that the size of the feature map gets reduced every time convolution operations are applied. For example, when an input of size ${({n + 1})} \times {({n + 1})}$ is applied to a network with receptive field size $n \times n$, the output image is $1 \times 1$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

This is in accordance with other super-resolution methods since many require surrounding pixels to infer center pixels correctly. This center-surround relation is useful since the surrounding region provides more constraints to this ill-posed problem (SR). For pixels near the image boundary, this relation cannot be exploited to the full extent and many SR methods crop the result image.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

This methodology, however, is not valid if the required surround region is very big. After cropping, the final image is too small to be visually pleasing.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

To resolve this issue, we pad zeros before convolutions to keep the sizes of all feature maps (including the output image) the same. It turns out that zero-padding works surprisingly well. For this reason, our method differs from most other methods in the sense that pixels near the image boundary are also correctly predicted.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Proposed Network", "weight": 1.0} -->

Once image details are predicted, they are added back to the input ILR image to give the final image (HR). We use this structure for all experiments in our work.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training", "weight": 1.0} -->

We now describe the objective to minimize in order to find optimal parameters of our model. Let $\mathbf{x}$ denote an interpolated low-resolution image and $\mathbf{y}$ a high-resolution image. Given a training dataset ${\{\mathbf{x}^{(i)},\mathbf{y}^{(i)}\}}_{i = 1}^{N}$, our goal is to learn a model $f$ that predicts values $\hat{\mathbf{y}} = {f{(\mathbf{x})}}$, where $\hat{\mathbf{y}}$ is an estimate of the target HR image. We minimize the mean squared error $\frac{1}{2}{\|{\mathbf{y} - {f{(\mathbf{x})}}}\|}^{2}$ averaged over the training set is minimized.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Training", "weight": 1.0} -->

Residual-Learning In SRCNN, the exact copy of the input has to go through all layers until it reaches the output layer. With many weight layers, this becomes an end-to-end relation requiring very long-term memory. For this reason, the vanishing/exploding gradients problem can be critical. We can solve this problem simply with residual-learning.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Training", "weight": 1.0} -->

As the input and output images are largely similar, we define a residual image $\mathbf{r} = {\mathbf{y} - \mathbf{x}}$, where most values are likely to be zero or small. We want to predict this residual image. The loss function now becomes $\frac{1}{2}{\|{\mathbf{r} - {f{(\mathbf{x})}}}\|}^{2}$, where $f{(\mathbf{x})}$ is the network prediction.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Training", "weight": 1.0} -->

In networks, this is reflected in the loss layer as follows. Our loss layer takes three inputs: residual estimate, network input (ILR image) and ground truth HR image. The loss is computed as the Euclidean distance between the reconstructed image (the sum of network input and output) and ground truth.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Training", "weight": 1.0} -->

Training is carried out by optimizing the regression objective using mini-batch gradient descent based on back-propagation (LeCun et al. ). We set the momentum parameter to 0.9. The training is regularized by weight decay ($L_{2}$ penalty multiplied by 0.0001).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Training", "weight": 1.0} -->

High Learning Rates for Very Deep Networks Training deep models can fail to converge in realistic limit of time. SRCNN fails to show superior performance with more than three weight layers. While there can be various reasons, one possibility is that they stopped their training procedure before networks converged. Their learning rate $10^{- 5}$ is too small for a network to converge within a week on a common GPU. Looking at Fig. 9 of, it is not easy to say their deeper networks have converged and their performances were saturated. While more training will eventually resolve the issue, but increasing depth to 20 does not seems practical with SRCNN.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Training", "weight": 1.0} -->

It is a basic rule of thumb to make learning rate high to boost training. But simply setting learning rate high can also lead to vanishing/exploding gradients. For the reason, we suggest an adjustable gradient clipping for maximal boost in speed while suppressing exploding gradients.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training", "weight": 1.0} -->

Adjustable Gradient Clipping Gradient clipping is a technique that is often used in training recurrent neural networks. But, to our knowledge, its usage is limited in training CNNs. While there exist many ways to limit gradients, one of the common strategies is to clip individual gradients to the predefined range $\lbrack{- \theta},\theta\rbrack$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Training", "weight": 1.0} -->

With clipping, gradients are in a certain range. With stochastic gradient descent commonly used for training, learning rate is multiplied to adjust the step size. If high learning rate is used, it is likely that $\theta$ is tuned to be small to avoid exploding gradients in a high learning rate regime. But as learning rate is annealed to get smaller, the effective gradient (gradient multiplied by learning rate) approaches zero and training can take exponentially many iterations to converge if learning rate is decreased geometrically.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Training", "weight": 1.0} -->

For maximal speed of convergence, we clip the gradients to $\lbrack{- \frac{\theta}{\gamma}},\frac{\theta}{\gamma}\rbrack$, where $\gamma$ denotes the current learning rate. We find the adjustable gradient clipping makes our convergence procedure extremely fast. Our 20-layer network training is done within 4 hours whereas 3-layer SRCNN takes several days to train.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Training", "weight": 1.0} -->

Multi-Scale While very deep models can boost performance, more parameters are now needed to define a network. Typically, one network is created for each scale factor. Considering that fractional scale factors are often used, we need an economical way to store and retrieve networks.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Training", "weight": 1.0} -->

For this reason, we also train a multi-scale model. With this approach, parameters are shared across all predefined scale factors. Training a multi-scale model is straightforward. Training datasets for several specified scales are combined into one big dataset.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Training", "weight": 1.0} -->

Data preparation is similar to SRCNN with some differences. Input patch size is now equal to the size of the receptive field and images are divided into sub-images with no overlap. A mini-batch consists of 64 sub-images, where sub-images from different scales can be in the same batch.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Training", "weight": 1.0} -->

We implement our model using the MatConvNet^11^1 package.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Understanding Properties", "weight": 1.0} -->

In this section, we study three properties of our proposed method. First, we show that large depth is necessary for the task of SR. A very deep network utilizes more contextual information in an image and models complex functions with many nonlinear layers. We experimentally verify that deeper networks give better performances than shallow ones.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Understanding Properties", "weight": 1.0} -->

Second, we show that our residual-learning network converges much faster than the standard CNN. Moreover, our network gives a significant boost in performance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Understanding Properties", "weight": 1.0} -->

Third, we show that our method with a single network performs as well as a method using multiple networks trained for each scale. We can effectively reduce model capacity (the number of parameters) of multi-network approaches.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

Convolutional neural networks exploit spatially-local correlation by enforcing a local connectivity pattern between neurons of adjacent layers. In other words, hidden units in layer $m$ take as input a subset of units in layer $m - 1$. They form spatially contiguous receptive fields.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

Each hidden unit is unresponsive to variations outside of the receptive field with respect to the input. The architecture thus ensures that the learned filters produce the strongest response to a spatially local input pattern.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

However, stacking many such layers leads to filters that become increasingly "global" (i.e. responsive to a larger region of pixel space). In other words, a filter of very large support can be effectively decomposed into a series of small filters.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

In this work, we use filters of the same size, 3$\times$`<!-- -->`{=html}3, for all layers. For the first layer, the receptive field is of size 3$\times$`<!-- -->`{=html}3. For the next layers, the size of the receptive field increases by 2 in both height and width. For depth $D$ network, the receptive field has size ${({{2D} + 1})} \times {({{2D} + 1})}$. Its size is proportional to the depth.

<!-- chunk {"id": "body-0050", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

In the task of SR, this corresponds to the amount of contextual information that can be exploited to infer high-frequency components. A large receptive field means the network can use more context to predict image details. As SR is an ill-posed inverse problem, collecting and analyzing more neighbor pixels give more clues. For example, if there are some image patterns entirely contained in a receptive field, it is plausible that this pattern is recognized and used to super-resolve the image.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

In addition, very deep networks can exploit high nonlinearities. We use 19 rectified linear units and our networks can model very complex functions with moderate number of channels (neurons). The advantages of making a thin deep network is well explained in Simonyan and Zisserman.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

We now experimentally show that very deep networks significantly improve SR performance. We train and test networks of depth ranging from 5 to 20 (only counting weight layers excluding nonlinearity layers). In Figure 3, we show the results. In most cases, performance increases as depth increases. As depth increases, performance improves rapidly.

<!-- chunk {"id": "body-0053", "role": "body", "section": "The Deeper, the Better", "weight": 1.0} -->

PSNR/SSIM/time
PSNR/SSIM/time
PSNR/SSIM/time
PSNR/SSIM/time
PSNR/SSIM/time
PSNR/SSIM/time

<!-- chunk {"id": "body-0054", "role": "body", "section": "Residual-Learning", "weight": 1.0} -->

As we already have a low-resolution image as the input, predicting high-frequency components is enough for the purpose of SR. Although the concept of predicting residuals has been used in previous methods, it has not been studied in the context of deep-learning-based SR framework.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Residual-Learning", "weight": 1.0} -->

In this work, we have proposed a network structure that learns residual images. We now study the effect of this modification to a standard CNN structure in detail.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Residual-Learning", "weight": 1.0} -->

First, we find that this residual network converges much faster. Two networks are compared experimentally: the residual network and the standard non-residual network. We use depth 10 (weight layers) and scale factor 2. Performance curves for various learning rates are shown in Figure 4. All use the same learning rate scheduling mechanism that has been mentioned above.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Residual-Learning", "weight": 1.0} -->

Second, at convergence, the residual network shows superior performance. In Figure 4, residual networks give higher PSNR when training is done.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Residual-Learning", "weight": 1.0} -->

Another remark is that if small learning rates are used, networks do not converge in the given number of epochs. If initial learning rate 0.1 is used, PSNR of a residual-learning network reaches 36.90 within 10 epochs. But if 0.001 is used instead, the network never reaches the same level of performance (its performance is 36.52 after 80 epochs). In a similar manner, residual and non-residual networks show dramatic performance gaps after 10 epochs (36.90 vs. 27.42 for rate 0.1).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Residual-Learning", "weight": 1.0} -->

In short, this simple modification to a standard non-residual network structure is very powerful and one can explore the validity of the idea in other image restoration problems where input and output images are highly correlated.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Single Model for Multiple Scales", "weight": 1.0} -->

Scale augmentation during training is a key technique to equip a network with super-resolution machines of multiple scales. Many SR processes for different scales can be executed with our multi-scale machine with much smaller capacity than that of single-scale machines combined.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Single Model for Multiple Scales", "weight": 1.0} -->

We start with an interesting experiment as follows: we train our network with a single scale factor $s_{\text{train}}$ and it is tested under another scale factor $s_{\text{test}}$. Here, factors 2,3 and 4 that are widely used in SR comparisons are considered. Possible pairs ($s_{\text{train}}$,$s_{\text{test}}$) are tried for the dataset 'Set5'. Experimental results are summarized in Table 2.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Single Model for Multiple Scales", "weight": 1.0} -->

Performance is degraded if $s_{\text{train}} \neq s_{\text{test}}$. For scale factor 2, the model trained with factor 2 gives PSNR of 37.10 (in dB), whereas models trained with factor 3 and 4 give 30.05 and 28.13, respectively. A network trained over single-scale data is not capable of handling other scales. In many tests, it is even worse than bicubic interpolation, the method used for generating the input image.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Single Model for Multiple Scales", "weight": 1.0} -->

We now test if a model trained with scale augmentation is capable of performing SR at multiple scale factors. The same network used above is trained with multiple scale factors $s_{\text{train}} = {\{ 2,3,4\}}$. In addition, we experiment with the cases $s_{\text{train}} = {{\{ 2,3\}},{\{ 2,4\}},{\{ 3,4\}}}$ for more comparisons.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Single Model for Multiple Scales", "weight": 1.0} -->

We observe that the network copes with any scale used during training. When $s_{\text{train}} = {\{ 2,3,4\}}$ ($\times 2,3,4$ in Table 2), its PSNR for each scale is comparable to those achieved from the corresponding result of single-scale network: 37.06 vs. 37.10 ($\times 2$), 33.27 vs. 32.89 ($\times 3$), 30.95 vs. 30.86 ($\times 4$).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Single Model for Multiple Scales", "weight": 1.0} -->

Another pattern is that for large scales ($\times 3,4$), our multi-scale network outperforms single-scale network: our model ($\times 2,3$), ($\times 3,4$) and ($\times 2,3,4$) give PSNRs 33.22, 33.24 and 33.27 for test scale 3, respectively, whereas ($\times 3$) gives 32.89. Similarly, ($\times 2,4$), ($\times 3,4$) and ($\times 2,3,4$) give 30.86, 30.94 and 30.95 (vs. 30.84 by $\times 4$ model), respectively. From this, we observe that training multiple scales boosts the performance for large scales.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we evaluate the performance of our method on several datasets. We first describe datasets used for training and testing our method. Next, parameters necessary for training are given.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

After outlining our experimental setup, we compare our method with several state-of-the-art SISR methods.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Datasets for Training and Testing", "weight": 1.0} -->

Training dataset Different learning-based methods use different training images. For example, RFL has two methods, where the first one uses 91 images from Yang et al. and the second one uses 291 images with the addition of 200 images from Berkeley Segmentation Dataset. SRCNN uses a very large ImageNet dataset.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Datasets for Training and Testing", "weight": 1.0} -->

We use 291 images as in for benchmark with other methods in this section. In addition, data augmentation (rotation or flip) is used. For results in previous sections, we used 91 images to train network fast, so performances can be slightly different.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Datasets for Training and Testing", "weight": 1.0} -->

Test dataset For benchmark, we use four datasets. Datasets 'Set5' and '' are often used for benchmark in other works. Dataset 'Urban100', a dataset of urban images recently provided by Huang et al., is very interesting as it contains many challenging images failed by many of the existing methods. Finally, dataset 'B100', natural images in the Berkeley Segmentation Dataset used in Timofte et al. and Yang and Yang for benchmark, is also employed.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Training Parameters", "weight": 1.0} -->

We provide parameters used to train our final model. We use a network of depth 20. Training uses batches of size 64. Momentum and weight decay parameters are set to 0.9 and $0.0001$, respectively.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Training Parameters", "weight": 1.0} -->

For weight initialization, we use the method described in He et al.. This is a theoretically sound procedure for networks utilizing rectified linear units (ReLu).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Training Parameters", "weight": 1.0} -->

We train all experiments over 80 epochs (9960 iterations with batch size 64). Learning rate was initially set to 0.1 and then decreased by a factor of 10 every 20 epochs. In total, the learning rate was decreased 3 times, and the learning is stopped after 80 epochs. Training takes roughly 4 hours on GPU Titan Z.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Benchmark", "weight": 1.0} -->

For benchmark, we follow the publicly available framework of Huang et al.. It enables the comparison of many state-of-the-art results with the same evaluation procedure.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Benchmark", "weight": 1.0} -->

The framework applies bicubic interpolation to color components of an image and sophisticated models to luminance components as in other methods. This is because human vision is more sensitive to details in intensity than in color.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Benchmark", "weight": 1.0} -->

This framework crops pixels near image boundary. For our method, this procedure is unnecessary as our network outputs the full-sized image. For fair comparison, however, we also crop pixels to the same amount.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Comparisons with State-of-the-Art Methods", "weight": 1.0} -->

We provide quantitative and qualitative comparisons. Compared methods are A+, RFL, SelfEx and SRCNN. In Table 3, we provide a summary of quantitative evaluation on several datasets. Our methods outperform all previous methods in these datasets. Moreover, our methods are relatively fast. The public code of SRCNN based on a CPU implementation is slower than the code used by Dong et. al in their paper based on a GPU implementation.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Comparisons with State-of-the-Art Methods", "weight": 1.0} -->

In Figures 6 and 7, we compare our method with top-performing methods. In Figure 6, only our method perfectly reconstructs the line in the middle. Similarly, in Figure 7, contours are clean and vivid in our method whereas they are severely blurred or distorted in other methods.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have presented a super-resolution method using very deep networks. Training a very deep network is hard due to a slow convergence rate. We use residual-learning and extremely high learning rates to optimize a very deep network fast. Convergence speed is maximized and we use gradient clipping to ensure the training stability. We have demonstrated that our method outperforms the existing method by a large margin on benchmarked images. We believe our approach is readily applicable to other image restoration problems such as denoising and compression artifact removal.
