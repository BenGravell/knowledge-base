## Introduction

Recent years have seen significant progress on the problem of accurately estimating optical flow, as evidenced by improving performance on increasingly challenging benchmarks. Despite this, most flow methods are derived from a "classical formulation" that makes a variety of assumptions about the image, from brightness constancy to spatial smoothness. These assumptions are only coarse approximations to reality and this likely limits performance. The recent history of the field has focused on improving these assumptions or making them more robust to violations. This has led to steady but incremental progress.

An alternative approach abandons the classical formulation altogether and starts over using recent neural network architectures. Such an approach takes a pair (or sequence) of images and learns to directly compute flow from them. Ideally such a network would learn to solve the correspondence problem (short and long range), learn filters relevant to the problem, learn what is constant in the sequence, and learn about the spatial structure of the flow and how it relates to the image structure. The first attempts are promising but are not yet as accurate as the classical methods.

Goal. We argue that there is an alternative approach that combines the best of both approaches. Decades of research on flow has produced well engineered systems and principles that are effective. But there are places where these methods make assumptions that limit their performance. Consequently, here we apply machine learning to address the weak points, while keeping the engineered architecture, with the goal of 1) improving performance over existing neural networks and the classical methods upon which our work is based; 2) achieving real-time flow estimates with accuracy better than the much slower classical methods; and 3) reducing memory requirements to make flow more practical for embedded, robotic, and mobile applications.

Problem. The key problem with recent methods for learning flow is that they typically take two frames, stack them together, and apply a convolutional network architecture. When the motions between frames are larger than one (or a few) pixels, spatio-temporal convolutional filters will not obtain meaningful responses. Said another way, if a convolutional window in one image does not overlap with related image pixels at the next time instant, no meaningful temporal filter can be learned.

There are two problems that need to be solved. One is to solve for long-range correlations while the other is to solve for detailed, sub-pixel, optical flow and precise motion boundaries. FlowNet attempts to learn both of these at once. In contrast, we tackle the latter using deep learning and rely on existing methods to solve the former.

Approach. To deal with large motions we adopt a traditional coarse-to-fine approach using a spatial pyramid^11^1This, of course, has well-known limitations, which we discuss later.. At that top level of the pyramid, the hope is that the motions between frames are smaller than a few pixels and that, consequently, the convolutional filters can learn meaningful temporal structure. At each level of the pyramid we solve for the flow using a convolutional network and up-sample the flow to the next pyramid level. As is standard, with classical formulations, we warp one image towards the other using the current flow, and repeat this process at each pyramid level. Instead of minimizing a classical objective function at each level, we learn a convolutional network to predict the flow increment at that level. We train the network from coarse to fine to learn the flow correction at each level and add this to the flow output of the network above. The idea is that the displacements are then always less than a few pixels at each pyramid level.

We call the method SPyNet, for Spatial Pyramid Network, and train it using the same Flying Chairs data as FlowNet. We report similar performance as FlowNet on Flying Chairs and Sintel but are significantly more accurate than FlowNet on Middlebury and KITTI after fine tuning. The total size of SPyNet is 96% smaller than FlowNet, meaning that it runs faster, and uses much less memory. The expensive iterative propagation of classical methods is replaced by the non-iterative computation of the neural network.

We do not claim to solve the full optical flow problem with SPyNet -- we address the same problem as traditional approaches and inherit some of their limitations. For example, it is well known that large motions of small or thin objects are difficult to capture with a pyramid representation. We see the large motion problem as separate, requiring different solutions. Rather, what we show is that the traditional problem can be reformulated, portions of it can be learned, and performance improves in many scenarios.

Additionally, because our approach connects past methods with new tools, it provides insights into how to move forward. In particular, we find that SPyNet learns spatio-temporal convolutional filters that resemble traditional spatio-temporal derivative or Gabor filters. The learned filters resemble biological models of motion processing filters in MT and V1. This is in contrast to the highly random-looking filters learned by FlowNet. This suggests that it is timely to reexamine older spatio-temporal filtering approaches with new tools.

In summary our contributions are: 1) the combination of traditional coarse-to-fine pyramid methods with deep learning for optical flow estimation; 2) a new SPyNet model that is 96% smaller and faster than FlowNet; 3) SPyNet achieves comparable or lower error than FlowNet on standard benchmarks -- Sintel, KITTI and Middlebury; 4) the learned spatio-temporal filters provide insight about what filters are needed for flow estimation; 5) the trained network and related code are publicly available for research ^22^2

## Related Work

Our formulation effectively combines ideas from "classical" optical flow and recent deep learning methods. Our review focuses on the work most relevant to this.

Spatial pyramids and optical flow. The classical formulation of the optical flow problem dates to Horn and Schunck and involves optimizing the sum of a data term based on brightness constancy and a spatial smoothness term. The classical methods typically suffer from the fact that they make very approximate assumptions about the image brightness change and the spatial structure of the flow. Many methods focus on improving robustness by changing the assumptions. A full review would effectively cover the history of the field; for this we refer the reader to. The key advantage of learning to compute flow, as we do here, is that we do not hand craft changes in these assumptions. Rather, the variation in image brightness and spatial smoothness are embodied in the learned network.

The idea of using a spatial pyramid has a similarly long history dating to with its first use in the classical flow formulation appearing . Typically Gaussian or Laplacian pyramids are used for flow estimation with the primary motivation to deal with large motions. These methods are well known to have problems when small objects move quickly. Brox et al. incorporate long range matching into the traditional optical flow objective function. This approach of combining image matching to capture large motions, with a variational or discrete optimization for fine motions, can produce accurate results.

Of course spatial pyramids are widely used in other areas of computer vision and have recently been used in deep neural networks to learn generative image models.

Spatio-temporal filters. Burt and Adelson lay out the theory of spatio-temporal models for motion estimation and Heeger provides a computational embodiment. While inspired by human perception, such methods did not perform well at the time.

Various methods have shown that spatio-temporal filters emerge from learning, for example using independent component analysis, sparseness, and multi-layer models. Memisevic and Hinton learn simple spatial transformations with a restricted Boltzmann machine, finding a variety of filters. Taylor et al. use synthetic data to learn "flow like" features using a restricted Boltzmann machine but do not evaluate flow accuracy.

Dosovitskiy et al. learn spatio-temporal filters for flow estimation using a deep network, yet these filters do not resemble classical filters inspired by neuroscience. By using a pyramid approach, here we learn filters that are visually similar to classical spatio-temporal filters, yet because they are learned from data, produce good flow estimates.

Learning to model and compute flow. Possibly the first attempt to learn a model to estimate optical flow is the work of Freeman et al. using an MRF. They consider a simple synthetic world of uniform moving blobs with ground truth flow. The training data was not realistic and they did not apply the method to real image sequences.

Roth and Black learn a field-of-experts (FoE) model to capture the spatial statistics of optical flow. The FoE can be viewed as a (shallow) convolutional neural network. The model is trained using flow fields generated from laser scans of real scenes and natural camera motions. They have no images of the scenes (only their flow) and consequently the method only learns the spatial component.

Sun et al. describe the first fully learned model that can be considered a (shallow) convolutional neural network. They formulate a classical flow problem with a data term and a spatial term. The spatial term uses the FoE model , while the data term replaces traditional derivative filters with a set of learned convolutional image filters. With limited training data and a small set of filters, it did not fully show the full promise of learning flow.

Wulff and Black learn the spatial statistics of optical flow by a applying robust PCA to real (noisy) optical flow computed from natural movies. While this produces a global flow basis and overly smooth flow, they use the model to compute reasonable flow relatively quickly.

Deep Learning. The above learning methods suffer from limited training data and the use of shallow models. In contrast, deep convolutional neural networks have emerged as a powerful class of models for solving recognition and dense estimation problems.

FlowNet represents the first deep convolutional architecture for flow estimation that is trained end-to-end. The network shows promising results, despite being trained on an artificial dataset of chairs flying over randomly selected images. Despite promising results, the method lags behind the state of the art in terms of accuracy. Deep matching methods \[20, 31, 42, thewlis2016fully\] do not fully solve the problem, since they resort to classical methods to compute the final flow field. It remains an open question as to which architectures are most appropriate for the problem and how best to train these.

Tran et al., use a traditional flow method to create "semi-truth" training data for a 3D convolutional network. The performance is below the state of the art and the method is not tested on the standard benchmarks. There have also been several attempts at estimating optical flow using unsupervised learning. However these methods have lower accuracy on standard benchmarks.

Fast flow. Several recent methods attempt to balance speed and accuracy, with the goal of real-time processing and reasonable (though not top) accuracy. GPU-flow began this trend but several methods now outperform it. PCA-Flow runs on a CPU, is slower than frame rate, and produces overly smooth flow fields. EPPM achieves similar, middle-of-the-pack, performance on Sintel (test), with similar speed on a GPU. Most recently DIS-Fast is a GPU method that is significantly faster than previous methods but is also significantly less accurate.

Our method is also significantly faster than the best previous CNN flow method (FlowNet), which reports a runtime of 80ms/frame for FlowNetS. The key to our speed is to create a small neural network that fits entirely on the GPU. Additionally all our pyramid operations are implemented on the GPU.

Size is an important issue that has not attracted as much attention as speed. For optical flow to exist on embedded processors, aerial vehicles, phones, etc., the algorithm needs a small memory footprint. Our network is 96% smaller than FlowNetS and uses only 9.7 MB for the model parameters, making it easily small enough to fit on a mobile phone GPU.

## Spatial Pyramid Network

Our approach uses the coarse-to-fine spatial pyramid structure of to learn residual flow at each pyramid level. Here we describe the network and training procedure.

Figure 1: Inference in a 3-Level Pyramid Network: The network G0 computes the residual flow v0 at the highest level of the pyramid (smallest image) using the low resolution images {I01, I02}. At each pyramid level, the network Gk computes a residual flow vk which propagates to each of the next lower levels of the pyramid in turn, to finally obtain the flow V2 at the highest resolution.

### Spatial Sampling

Let $d{( \cdot )}$ be the downsampling function that decimates an $m \times n$ image $I$ to the corresponding image $d{(I)}$ of size ${{m/2} \times n}/2$. Let $u{( \cdot )}$ be the reverse operation that upsamples images. These operators are also used for downsampling and upsampling the horizontal and vertical components of the optical flow field, $V$. We also define a warping operator $w{(I,V)}$ that warps the image, $I$ according to the flow field, $V$, using bi-linear interpolation.

### Inference

Let $\{ G_{0},\ldots,G_{K}\}$ denote a set of trained convolutional neural network (convnet) models, each of which computes residual flow, $v_{k}$ at the $k$-th pyramid level. The convnet $G_{k}$ computes the residual flow $v_{k}$ using the upsampled flow from the previous pyramid level, $V_{k - 1}$, and the frames $\{ I_{k}^{1},I_{k}^{2}\}$ at level $k$. The second frame $I_{k}^{2}$ is warped using the flow as $w{(I_{k}^{2},{u{(V_{k - 1})}})}$ before feeding it to the convnet $G_{k}$. The flow, $V_{k}$ at the $k$-th pyramid level is then As shown in Fig. 1, we start with downsampled images $\{ I_{0}^{1},I_{0}^{2}\}$ and an initial flow estimate that is zero everywhere to compute the residual flow $v_{0} = V_{0}$ at the top of the pyramid. We upsample the resulting flow, $u{(V_{0})}$, and pass it to the network $G_{1}$ along with $\{ I_{1}^{1},{w{(I_{1}^{2},{u{(V_{0})}})}}\}$ to compute the residual flow $v_{1}$. At each pyramid level, we compute the flow $V_{k}$ using Equation. The flow $V_{k}$ is similarly propagated to higher resolution layers of the pyramid until we obtain the flow $V_{K}$ at full resolution. Figure 1 shows the working of our approach using a 3-level pyramid. In experiments, we use a 5-level pyramid ($K = 4$).

Figure 2: Training network Gk requires trained models {G0 … Gk − 1} to obtain the initial flow u (Vk − 1). We obtain ground truth residual flows v̂k by subtracting downsampled ground truth flow V̂k and u (Vk − 1) to train the network Gk using the EPE loss.

### Training and Network Architecture

We train each of the convnets $\{ G_{0},\ldots,G_{K}\}$ independently and sequentially to compute the residual flow $v_{k}$ given the inputs $\{ I_{k}^{1},{w{(I_{k}^{2},{u{(V_{k - 1})}})}},{u{(V_{k - 1})}}\}$. We compute target residual flows ${\hat{v}}_{k}$ as a difference of target flow $V_{k}$ at the $k$-th pyramid level and the upsampled flow, $u{(V_{k - 1})}$ obtained from the trained convnet of the previous level As shown in Fig. 2, we train each of the networks, $G_{k}$, to minimize the average End Point Error (EPE) loss on the residual flow $v_{k}$.

Each level in the pyramid has a simplified task relative to the full optical flow estimation problem; it only has to estimate a small-motion update to an existing flow field. Consequently each network can be simple. Here, each $G_{k}$ has 5 convolutional layers, which we found gave the best combination of accuracy, size, and speed. We train five convnets $\{ G_{0},\ldots,G_{4}\}$ at different resolutions of the Flying Chairs dataset. The network $G_{0}$ is trained with 24x32 images. We double the resolution at each lower level and finally train the convnet, $G_{4}$ with a resolution of 384x512.

Each convolutional layer is followed by a Rectified Linear Unit (ReLU), except the last one. We use a 7x7 convolutional kernel for each of the layers and found these work better than smaller filters. The number of feature maps in each convnet, $G_{k}$ are {32, 64, 32, 16, 2}. The image $I_{k}^{1}$ and the warped image $w{(I_{k}^{2},{u{(V_{k - 1})}})}$ have 3 channels each (RGB). The upsampled flow $u{(V_{k - 1})}$ is 2 channel (horizontal and vertical). We stack image frames together with upsampled flow to form an 8 channel input to each $G_{k}$. The output is 2 channel flow corresponding to velocity in $x$ and $y$ directions.

We train five networks $\{ G_{0},\ldots,G_{4}\}$ such that each network $G_{k}$ uses the previous network $G_{k - 1}$ as initialization. The networks are trained using Adam optimization with $\beta_{1} = 0.9$ and $\beta_{2} = 0.999$. We use a batch size of 32 across all networks with 4000 iterations per epoch. We use a learning rate of 1e-4 for the first 60 epochs and decrease it to 1e-5 until the networks converge. We use Torch7^33^3 as our deep learning framework. We use the Flying Chairs dataset and the MPI Sintel for training our network. All our networks are trained on a single Nvidia K80 GPU.

We include various types of data augmentation during training. We randomly scale images by a factor of $\lbrack 1,2\rbrack$ and apply rotations at random within $\lbrack{- 17^{\circ}},17^{\circ}\rbrack$. We then apply a random crop to match the resolution of the convnet, $G_{k}$ being trained. We include additive white Gaussian noise sampled uniformly from $\mathcal{N}{(0,0.1)}$. We apply color jitter with additive brightness, contrast and saturation sampled from a Gaussian, $\mathcal{N}{(0,0.4)}$. We finally normalize the images using a mean and standard deviation computed from a large corpus of ImageNet data .

## Experiments

Figure 3: Visualization of optical flow estimates using our model (SPyNet) and the corresponding ground truth flow fields on the Flying Chairs dataset.

Figure 4: Visual comparison of optical flow estimates using our SPyNet model with FlowNet on the MPI Sintel dataset. The top five rows are from the Sintel Final set and the bottom five row are from the Sintel Clean set. SPyNet performs particularly well when the motions are relatively small.

Table 1: Average end point errors (EPE). Results are divided into methods trained with (+ft) and without fine tuning. Bold font indicates the most accurate results among the convnet methods. All run times are measured on Flying Chairs and exclude image loading time.

Table 2: Comparison of FlowNet and SpyNet on the Sintel benchmark for different velocities, s, and distances, d, from motion boundaries.

We evaluate our performance on standard optical flow benchmarks and compare with FlowNet and Classic+NLP, a traditional pyramid-based method. We compare performance using average end point errors in Table 1. We evaluate on all the standard benchmarks and find that SPyNet is the most accurate overall, with and without fine tuning (details below). Additionally SPyNet is faster than all other methods.

Note that the FlowNet results reported on the MPI-Sintel website are for a version that applies variational refinement ("+v") to the convnet results. Here we are not interested in the variational component and only compare the results of the convnet output.

### Flying Chairs

Once the convnets $G_{k}$ are trained on Flying Chairs, we fine tune the network on the same dataset but without any data augmentation at a learning rate of 1e-6. We see an improvement of EPE by 0.14 on the test set. Our model achieves better performance than FlowNetS on the Flying Chairs dataset, however FlowNetC performs better than ours. We show the qualitative results on Flying Chairs dataset in Fig. 3 and compare the performance in Table 1.

### MPI-Sintel

The resolution of Sintel images is 436x1024. To use SPyNet, we scale the images to 448x1024, and use 6 pyramid levels to compute the optical flow. The networks used on each pyramid level are $\{ G_{0},G_{1},G_{2},G_{3},G_{4},G_{4}\}$. We repeat the network $G_{4}$ at the sixth level of pyramid for experiments on Sintel. Because Sintel has extremely large motions, we found that this gives better performance than using just five levels.

We evaluate the performance of our model on MPI-Sintel in two ways. First, we directly use the model trained on Flying Chairs dataset and evaluate our performance on both the training and the test sets. Second, we extract a validation set from the Sintel training set, using the same partition as. We fine tune our model independently on the Sintel Clean and Sintel Final split, and evaluate the EPE. The fine-tuned models are listed as "+ft" in Table 1. We show the qualitative results on MPI-Sintel in Fig. 4.

Table 2 compares our fine-tuned model with FlowNet for different velocities and distances from motion boundaries. We observe that SPyNet is more accurate than FlowNet for all velocity ranges except the largest displacements (over 40 pixels/frame). SPyNet is also more accurate than FlowNet close to motion boundaries, which is important for many problems.

### KITTI and Middlebury

We evaluate KITTI scenes using the base model SPyNet trained on Flying Chairs. We then fine-tune the model on Driving and Monkaa scenes from and evaluate the fine-tuned model SPyNet+ft. Fine tuning results in a significant improvement in accuracy by about 5 pixels. The large improvement in accuracy suggests that better training datasets are needed and that these could improve the accuracy of SPyNet further on general scenes. While SPyNet+ft is much more accurate than FlowNet+ft, the latter is fine-tuned on different data.

For the Middlebury dataset, we evaluate the sequences using the base model SPyNet as well as SPyNet+ft, which is fine-tuned on the Sintel-Final dataset; the Middlebury dataset itself is too small for fine-tuning. SPyNet is significantly more accurate on Middlebury, where FlowNet has trouble with the small motions. Both learned methods are less accurate than Classic+NL on Middlebury but both are also significantly faster.

## Analysis

### Model Size

Combining spatial pyramids with convnets results in a huge reduction in model complexity. At each pyramid level, a network, $G_{k}$, has 240,050 learned parameters. The total number of parameters learned by the entire network is 1,200,250, with 5 spatial pyramid levels. In comparison, FlowNetS and FlowNetC have 32,070,472 and 32,561,032 parameters respectively. SPyNet is about 96 % smaller than FlowNet (Fig. 5).

Figure 5: Model size of various methods. Our model is 96% smaller than the previous state-of-the-art flow method trained using end-to-end deep learning.

The spatial pyramid approach enables a significant reduction in model parameters without sacrificing accuracy. There are two reasons -- the warping function and learning of residual flow. By using the warping function directly, the convnet does not need to learn it. More importantly, the residual learning restricts the range of flow fields in the output space. Each network only has to model a smaller range of velocities at each level of the spatial pyramid.

SPyNet also has a small memory footprint. The disk space required to store all the model parameters is 9.7 MB. This could simplify deployment on mobile or embedded devices with GPU support.

Figure 6: (a) Visualization of filter weights in the first layer of G2 showing their spatiotemporal nature on RGB image pairs. (b) Evolution of filters across the pyramid levels (from low resolution to high resolution )

### Visualization of Learned Filters

Figure 6 shows examples of filters learned by the first layer of the network, $G_{2}$. In each row, the first two columns show the spatial filters that operate on the RGB channels of the two input images respectively. The third column is the difference between the two spatial filters hence representing the temporal features learned by our model. We observe that most of the spatio-temporal filters in Fig. 6 are equally sensitive to all color channels, and hence appear mostly grayscale. Note that the actual filters are $7 \times 7$ pixels and are upsampled for visualization.

We observe that many of the spatial filters appear to be similar to traditional Gaussian derivative filters used by classical methods. These classical filters are hand crafted and typically are applied in the horizontal and vertical direction. Here, we observe a greater variety of derivative-like filters of varied scales and orientations. We also observe filters that spatially resemble second derivative or Gabor filters. The temporal filters show a clear derivative-like structure in time. Note that these filters are very different from those reported in (Sup. Mat.), which have a high-frequency structure, unlike classical filters.

Figure 6 illustrates how filters learned by the network at each level of the pyramid differ from each other. Recall that, during training, each network is initialized with the network before it in the pyramid. The filters, however, do not stay exactly the same with training. Most of the filters in our network look like rows 1 and 2, where the filters become sharper as we progress towards the finer-resolution levels of the pyramid. However, there are some filters that are similar to rows 3 and 4, where these filters become more defined at higher resolution levels of the pyramid.

Figure 7: Average EPE vs. runtime on MPI-Sintel. Zoomed in version on the bottom shows the fastest methods. Times were measured by us. Adapted .

### Speed

Optical flow estimation is traditionally viewed as an optimization problem involving some form of variational inference. Such algorithms are computationally expensive, often taking several seconds or minutes per frame. This has limited the application of optical flow in robotics, embedded systems, and video analysis.

Using a GPU can speed up traditional methods but with reduced accuracy. Feed forward deep networks leverage fast GPU convolutions and avoid iterative optimization. Of course for embedded applications, network size is critical (see Fig. 5). Figure 7 shows the speed-accuracy comparisons of several well known methods. All times shown are measured with the images already loaded in the memory. The errors are computed as the average EPE of both the clean and final MPI-Sintel sequences. SPyNet offers a good balance between speed and accuracy; no faster method is as accurate.

## Discussion and Future Work

Traditional flow methods linearize the brightness constancy equation resulting in an optical flow constraint equation implemented with spatial and temporal derivative filters. Sometimes methods adopt a more generic filter constancy assumption. Our filters are somewhat different. The filters learned by SPyNet are used in the direct computation of the flow by the feed-forward network.

SPyNet is small compared with other recent optical flow networks. Examination of the filters, however, suggests that it might be possible to make it significantly smaller still. Many of the filters resemble derivative of Gaussian filters or Gabor filters at various scales, orientations, spatial frequencies, and spatial shifts. Given this, it may be possible to significantly compress the filter bank by using dimensionality reduction or by using a set of analytic spatio-temporal features. Some of the filters may also be separable.

Early methods for optical flow used analytic spatio-temporal features but, at the time, did not produce good results and the general line of spatio-temporal filtering decayed. The difference from early work is that our approach suggests the need for a large filter bank of varied filters. Note also that these approaches considered only the first convolutional layer of filters and did not seek a "deep" solution. This all suggests the possibility that a deep network of analytic filters could perform well. This could vastly reduce the size of the network and the number of parameters that need to be learned.

Note that pyramids have well-known limitations for dealing with large motions. In particular, small or thin objects that move quickly effectively disappear at coarse pyramid levels, making it impossible to capture their motion. Recent approaches for dealing with such large motions use sparse matching to augment standard pyramids. Future work should explore adding long-range matches to SPyNet. Alternatively Sevilla et al. define a channel constancy representation that preserves fine structures in a pyramid. The channels effectively correspond to filters that could be learned.

A spatial pyramid can be thought of as the simple application of a set of linear filters. Here we take a standard spatial pyramid but one could learn the filters for the pyramid itself. SPyNet also uses a standard warping function to align images using the flow computed from the previous pyramid level. This too could be learned.

An appealing feature of SPyNet is that it is small enough to fit on a mobile device. Future work will explore a mobile implementation and its applications. Additionally, we will explore extending the method to use more frames (e.g. 3 or 4). Multiple frames could enable the network to reason more effectively about occlusion.

Finally, Flying Chairs is not representative of natural scene motions, containing many huge displacements. We are exploring new training datasets to improve performance on common sequences where the motion is less dramatic.

## Conclusions

In summary, we have described a new optical flow method that combines features of classical optical flow algorithms with deep learning. In a sense, there are two notions of "deepness" here. First we use a "deep" spatial pyramid to deal with large motions. Second we use deep neural networks at each level of the spatial pyramid and train them to estimate a flow update at each level. This approach means that each network has less work to do than a fully generic flow method that has to estimate arbitrarily large motions. At each pyramid level we assume that the motion is small (on the order of a pixel). This is borne out by the fact that the network learns spatial and temporal filters that resemble classical derivatives of Gaussians and Gabors. Because each sub-task is so much simpler, our network needs many fewer parameters than previous methods like FlowNet. This results in a method with a small memory footprint that is faster than existing methods. At the same time, SPyNet achieves an accuracy comparable to FlowNet, surpassing it in several benchmarks. This opens up the promise of optical flow that is both accurate, practical, and widely deployable.
