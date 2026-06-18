<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optical Flow Estimation Using a Spatial Pyramid Network

Topics include Optical flow, SPyNet, Spatial pyramid, Convolutional networks, Coarse-to-fine estimation, Image warping, Embedded vision.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

SPyNet is a compact hybrid of classical coarse-to-fine warping and learned flow-update networks. Its importance is that it demonstrates a smaller, more interpretable neural optical-flow model by pushing large displacement handling back into a spatial pyramid rather than asking a single large CNN to solve everything at once.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We learn to compute optical flow by combining a classical spatial-pyramid formulation with deep learning. This estimates large motions in a coarse-to-fine approach by warping one image of a pair at each pyramid level by the current flow estimate and computing an update to the flow. Instead of the standard minimization of an objective function at each pyramid level, we train one deep network per level to compute the flow update. Unlike the recent FlowNet approach, the networks do not need to deal with large motions; these are dealt with by the pyramid. This has several advantages. First, our Spatial Pyramid Network (SPyNet) is much simpler and 96% smaller than FlowNet in terms of model parameters. This makes it more efficient and appropriate for embedded applications. Second, since the flow at each pyramid level is small (< 1 pixel), a convolutional approach applied to pairs of warped images is appropriate. Third, unlike FlowNet, the learned convolution filters appear similar to classical spatio-temporal filters, giving insight into the method and how to improve it. Our results are more accurate than FlowNet on most standard benchmarks, suggesting a new direction of combining classical flow methods with deep learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have seen significant progress on the problem of accurately estimating optical flow, as evidenced by improving performance on increasingly challenging benchmarks. Despite this, most flow methods are derived from a "classical formulation" that makes a variety of assumptions about the image, from brightness constancy to spatial smoothness. These assumptions are only coarse approximations to reality and this likely limits performance. The recent history of the field has focused on improving these assumptions or making them more robust to violations. This has led to steady but incremental progress.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative approach abandons the classical formulation altogether and starts over using recent neural network architectures. Such an approach takes a pair (or sequence) of images and learns to directly compute flow from them. Ideally such a network would learn to solve the correspondence problem (short and long range), learn filters relevant to the problem, learn what is constant in the sequence, and learn about the spatial structure of the flow and how it relates to the image structure. The first attempts are promising but are not yet as accurate as the classical methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Goal. We argue that there is an alternative approach that combines the best of both approaches. Decades of research on flow has produced well engineered systems and principles that are effective. But there are places where these methods make assumptions that limit their performance. Consequently, here we apply machine learning to address the weak points, while keeping the engineered architecture, with the goal of 1) improving performance over existing neural networks and the classical methods upon which our work is based; 2) achieving real-time flow estimates with accuracy better than the much slower classical methods; and 3) reducing memory requirements to make flow more practical for embedded, robotic, and mobile applications.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problem. The key problem with recent methods for learning flow is that they typically take two frames, stack them together, and apply a convolutional network architecture. When the motions between frames are larger than one (or a few) pixels, spatio-temporal convolutional filters will not obtain meaningful responses. Said another way, if a convolutional window in one image does not overlap with related image pixels at the next time instant, no meaningful temporal filter can be learned.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are two problems that need to be solved. One is to solve for long-range correlations while the other is to solve for detailed, sub-pixel, optical flow and precise motion boundaries. FlowNet attempts to learn both of these at once. In contrast, we tackle the latter using deep learning and rely on existing methods to solve the former.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Approach. To deal with large motions we adopt a traditional coarse-to-fine approach using a spatial pyramid^11^1This, of course, has well-known limitations, which we discuss later.. At that top level of the pyramid, the hope is that the motions between frames are smaller than a few pixels and that, consequently, the convolutional filters can learn meaningful temporal structure. At each level of the pyramid we solve for the flow using a convolutional network and up-sample the flow to the next pyramid level. As is standard, with classical formulations, we warp one image towards the other using the current flow, and repeat this process at each pyramid level. Instead of minimizing a classical objective function at each level, we learn a convolutional network to predict the flow increment at that level. We train the network from coarse to fine to learn the flow correction at each level and add this to the flow output of the network above. The idea is that the displacements are then always less than a few pixels at each pyramid level.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We call the method SPyNet, for Spatial Pyramid Network, and train it using the same Flying Chairs data as FlowNet. We report similar performance as FlowNet on Flying Chairs and Sintel but are significantly more accurate than FlowNet on Middlebury and KITTI after fine tuning. The total size of SPyNet is 96% smaller than FlowNet, meaning that it runs faster, and uses much less memory. The expensive iterative propagation of classical methods is replaced by the non-iterative computation of the neural network.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We do not claim to solve the full optical flow problem with SPyNet -- we address the same problem as traditional approaches and inherit some of their limitations. For example, it is well known that large motions of small or thin objects are difficult to capture with a pyramid representation. We see the large motion problem as separate, requiring different solutions. Rather, what we show is that the traditional problem can be reformulated, portions of it can be learned, and performance improves in many scenarios.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Additionally, because our approach connects past methods with new tools, it provides insights into how to move forward. In particular, we find that SPyNet learns spatio-temporal convolutional filters that resemble traditional spatio-temporal derivative or Gabor filters. The learned filters resemble biological models of motion processing filters in MT and V1. This is in contrast to the highly random-looking filters learned by FlowNet. This suggests that it is timely to reexamine older spatio-temporal filtering approaches with new tools.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary our contributions are: 1) the combination of traditional coarse-to-fine pyramid methods with deep learning for optical flow estimation; 2) a new SPyNet model that is 96% smaller and faster than FlowNet; 3) SPyNet achieves comparable or lower error than FlowNet on standard benchmarks -- Sintel, KITTI and Middlebury; 4) the learned spatio-temporal filters provide insight about what filters are needed for flow estimation; 5) the trained network and related code are publicly available for research ^22^2

<!-- chunk {"id": "body-0014", "role": "body", "section": "Spatial Pyramid Network", "weight": 1.0} -->

Our approach uses the coarse-to-fine spatial pyramid structure of to learn residual flow at each pyramid level. Here we describe the network and training procedure.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Spatial Sampling", "weight": 1.0} -->

Let $d{( \cdot )}$ be the downsampling function that decimates an $m \times n$ image $I$ to the corresponding image $d{(I)}$ of size ${{m/2} \times n}/2$. Let $u{( \cdot )}$ be the reverse operation that upsamples images. These operators are also used for downsampling and upsampling the horizontal and vertical components of the optical flow field, $V$. We also define a warping operator $w{(I,V)}$ that warps the image, $I$ according to the flow field, $V$, using bi-linear interpolation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Inference", "weight": 1.0} -->

Let $\{ G_{0},\ldots,G_{K}\}$ denote a set of trained convolutional neural network (convnet) models, each of which computes residual flow, $v_{k}$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Inference", "weight": 1.0} -->

at the $k$-th pyramid level. The convnet $G_{k}$ computes the residual flow $v_{k}$ using the upsampled flow from the previous pyramid level, $V_{k - 1}$, and the frames $\{ I_{k}^{1},I_{k}^{2}\}$ at level $k$. The second frame $I_{k}^{2}$ is warped using the flow as $w{(I_{k}^{2},{u{(V_{k - 1})}})}$ before feeding it to the convnet $G_{k}$. The flow, $V_{k}$ at the $k$-th pyramid level is then

<!-- chunk {"id": "body-0018", "role": "body", "section": "Inference", "weight": 1.0} -->

As shown in Fig. 1, we start with downsampled images $\{ I_{0}^{1},I_{0}^{2}\}$ and an initial flow estimate that is zero everywhere to compute the residual flow $v_{0} = V_{0}$ at the top of the pyramid. We upsample the resulting flow, $u{(V_{0})}$, and pass it to the network $G_{1}$ along with $\{ I_{1}^{1},{w{(I_{1}^{2},{u{(V_{0})}})}}\}$ to compute the residual flow $v_{1}$. At each pyramid level, we compute the flow $V_{k}$ using Equation. The flow $V_{k}$ is similarly propagated to higher resolution layers of the pyramid until we obtain the flow $V_{K}$ at full resolution. Figure 1 shows the working of our approach using a 3-level pyramid.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Training and Network Architecture", "weight": 1.0} -->

We train each of the convnets $\{ G_{0},\ldots,G_{K}\}$ independently and sequentially to compute the residual flow $v_{k}$ given the inputs $\{ I_{k}^{1},{w{(I_{k}^{2},{u{(V_{k - 1})}})}},{u{(V_{k - 1})}}\}$. We compute target residual flows ${\hat{v}}_{k}$ as a difference of target flow $V_{k}$ at the $k$-th pyramid level and the upsampled flow, $u{(V_{k - 1})}$ obtained from the trained convnet of the previous level

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training and Network Architecture", "weight": 1.0} -->

As shown in Fig. 2, we train each of the networks, $G_{k}$, to minimize the average End Point Error (EPE) loss on the residual flow $v_{k}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training and Network Architecture", "weight": 1.0} -->

Each level in the pyramid has a simplified task relative to the full optical flow estimation problem; it only has to estimate a small-motion update to an existing flow field. Consequently each network can be simple. Here, each $G_{k}$ has 5 convolutional layers, which we found gave the best combination of accuracy, size, and speed. We train five convnets $\{ G_{0},\ldots,G_{4}\}$ at different resolutions of the Flying Chairs dataset. The network $G_{0}$ is trained with 24x32 images. We double the resolution at each lower level and finally train the convnet, $G_{4}$ with a resolution of 384x512.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training and Network Architecture", "weight": 1.0} -->

Each convolutional layer is followed by a Rectified Linear Unit (ReLU), except the last one. We use a 7x7 convolutional kernel for each of the layers and found these work better than smaller filters. The number of feature maps in each convnet, $G_{k}$ are {32, 64, 32, 16, 2}. The image $I_{k}^{1}$ and the warped image $w{(I_{k}^{2},{u{(V_{k - 1})}})}$ have 3 channels each (RGB). The upsampled flow $u{(V_{k - 1})}$ is 2 channel (horizontal and vertical). We stack image frames together with upsampled flow to form an 8 channel input to each $G_{k}$. The output is 2 channel flow corresponding to velocity in $x$ and $y$ directions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training and Network Architecture", "weight": 1.0} -->

We train five networks $\{ G_{0},\ldots,G_{4}\}$ such that each network $G_{k}$ uses the previous network $G_{k - 1}$ as initialization. The networks are trained using Adam optimization with $\beta_{1} = 0.9$ and $\beta_{2} = 0.999$. We use a batch size of 32 across all networks with 4000 iterations per epoch. We use a learning rate of 1e-4 for the first 60 epochs and decrease it to 1e-5 until the networks converge. We use Torch7^33^3 as our deep learning framework. We use the Flying Chairs dataset and the MPI Sintel for training our network. All our networks are trained on a single Nvidia K80 GPU.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training and Network Architecture", "weight": 1.0} -->

We include various types of data augmentation during training. We randomly scale images by a factor of $\lbrack 1,2\rbrack$ and apply rotations at random within $\lbrack{- 17^{\circ}},17^{\circ}\rbrack$. We then apply a random crop to match the resolution of the convnet, $G_{k}$ being trained. We include additive white Gaussian noise sampled uniformly from $\mathcal{N}{(0,0.1)}$. We apply color jitter with additive brightness, contrast and saturation sampled from a Gaussian, $\mathcal{N}{(0,0.4)}$. We finally normalize the images using a mean and standard deviation computed from a large corpus of ImageNet data.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our performance on standard optical flow benchmarks and compare with FlowNet and Classic+NLP, a traditional pyramid-based method. We compare performance using average end point errors in Table 1. We evaluate on all the standard benchmarks and find that SPyNet is the most accurate overall, with and without fine tuning (details below). Additionally SPyNet is faster than all other methods.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Note that the FlowNet results reported on the MPI-Sintel website are for a version that applies variational refinement ("+v") to the convnet results. Here we are not interested in the variational component and only compare the results of the convnet output.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Flying Chairs", "weight": 1.0} -->

Once the convnets $G_{k}$ are trained on Flying Chairs, we fine tune the network on the same dataset but without any data augmentation at a learning rate of 1e-6. We see an improvement of EPE by 0.14 on the test set. Our model achieves better performance than FlowNetS on the Flying Chairs dataset, however FlowNetC performs better than ours. We show the qualitative results on Flying Chairs dataset in Fig. 3 and compare the performance in Table 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "MPI-Sintel", "weight": 1.0} -->

The resolution of Sintel images is 436x1024. To use SPyNet, we scale the images to 448x1024, and use 6 pyramid levels to compute the optical flow. The networks used on each pyramid level are $\{ G_{0},G_{1},G_{2},G_{3},G_{4},G_{4}\}$. We repeat the network $G_{4}$ at the sixth level of pyramid for experiments on Sintel. Because Sintel has extremely large motions, we found that this gives better performance than using just five levels.

<!-- chunk {"id": "body-0029", "role": "body", "section": "MPI-Sintel", "weight": 1.0} -->

We evaluate the performance of our model on MPI-Sintel in two ways. First, we directly use the model trained on Flying Chairs dataset and evaluate our performance on both the training and the test sets. Second, we extract a validation set from the Sintel training set, using the same partition as. We fine tune our model independently on the Sintel Clean and Sintel Final split, and evaluate the EPE. The fine-tuned models are listed as "+ft" in Table 1. We show the qualitative results on MPI-Sintel in Fig. 4.

<!-- chunk {"id": "body-0030", "role": "body", "section": "MPI-Sintel", "weight": 1.0} -->

Table 2 compares our fine-tuned model with FlowNet for different velocities and distances from motion boundaries. We observe that SPyNet is more accurate than FlowNet for all velocity ranges except the largest displacements (over 40 pixels/frame). SPyNet is also more accurate than FlowNet close to motion boundaries, which is important for many problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "KITTI and Middlebury", "weight": 1.0} -->

We evaluate KITTI scenes using the base model SPyNet trained on Flying Chairs. We then fine-tune the model on Driving and Monkaa scenes from and evaluate the fine-tuned model SPyNet+ft. Fine tuning results in a significant improvement in accuracy by about 5 pixels. The large improvement in accuracy suggests that better training datasets are needed and that these could improve the accuracy of SPyNet further on general scenes. While SPyNet+ft is much more accurate than FlowNet+ft, the latter is fine-tuned on different data.

<!-- chunk {"id": "body-0032", "role": "body", "section": "KITTI and Middlebury", "weight": 1.0} -->

For the Middlebury dataset, we evaluate the sequences using the base model SPyNet as well as SPyNet+ft, which is fine-tuned on the Sintel-Final dataset; the Middlebury dataset itself is too small for fine-tuning. SPyNet is significantly more accurate on Middlebury, where FlowNet has trouble with the small motions. Both learned methods are less accurate than Classic+NL on Middlebury but both are also significantly faster.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Model Size", "weight": 1.0} -->

Combining spatial pyramids with convnets results in a huge reduction in model complexity. At each pyramid level, a network, $G_{k}$, has 240,050 learned parameters. The total number of parameters learned by the entire network is 1,200,250, with 5 spatial pyramid levels. In comparison, FlowNetS and FlowNetC have 32,070,472 and 32,561,032 parameters respectively. SPyNet is about 96 % smaller than FlowNet (Fig. 5).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Model Size", "weight": 1.0} -->

The spatial pyramid approach enables a significant reduction in model parameters without sacrificing accuracy. There are two reasons -- the warping function and learning of residual flow. By using the warping function directly, the convnet does not need to learn it. More importantly, the residual learning restricts the range of flow fields in the output space. Each network only has to model a smaller range of velocities at each level of the spatial pyramid.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Model Size", "weight": 1.0} -->

SPyNet also has a small memory footprint. The disk space required to store all the model parameters is 9.7 MB. This could simplify deployment on mobile or embedded devices with GPU support.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Visualization of Learned Filters", "weight": 1.0} -->

We observe that many of the spatial filters appear to be similar to traditional Gaussian derivative filters used by classical methods. These classical filters are hand crafted and typically are applied in the horizontal and vertical direction. Here, we observe a greater variety of derivative-like filters of varied scales and orientations. We also observe filters that spatially resemble second derivative or Gabor filters. The temporal filters show a clear derivative-like structure in time. Note that these filters are very different from those reported in (Sup. Mat.), which have a high-frequency structure, unlike classical filters.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Speed", "weight": 1.0} -->

Optical flow estimation is traditionally viewed as an optimization problem involving some form of variational inference. Such algorithms are computationally expensive, often taking several seconds or minutes per frame. This has limited the application of optical flow in robotics, embedded systems, and video analysis.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Speed", "weight": 1.0} -->

Using a GPU can speed up traditional methods but with reduced accuracy. Feed forward deep networks leverage fast GPU convolutions and avoid iterative optimization. Of course for embedded applications, network size is critical (see Fig. 5). Figure 7 shows the speed-accuracy comparisons of several well known methods. All times shown are measured with the images already loaded in the memory. The errors are computed as the average EPE of both the clean and final MPI-Sintel sequences. SPyNet offers a good balance between speed and accuracy; no faster method is as accurate.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Traditional flow methods linearize the brightness constancy equation resulting in an optical flow constraint equation implemented with spatial and temporal derivative filters. Sometimes methods adopt a more generic filter constancy assumption. Our filters are somewhat different. The filters learned by SPyNet are used in the direct computation of the flow by the feed-forward network.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

SPyNet is small compared with other recent optical flow networks. Examination of the filters, however, suggests that it might be possible to make it significantly smaller still. Many of the filters resemble derivative of Gaussian filters or Gabor filters at various scales, orientations, spatial frequencies, and spatial shifts. Given this, it may be possible to significantly compress the filter bank by using dimensionality reduction or by using a set of analytic spatio-temporal features. Some of the filters may also be separable.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Early methods for optical flow used analytic spatio-temporal features but, at the time, did not produce good results and the general line of spatio-temporal filtering decayed. The difference from early work is that our approach suggests the need for a large filter bank of varied filters. Note also that these approaches considered only the first convolutional layer of filters and did not seek a "deep" solution. This all suggests the possibility that a deep network of analytic filters could perform well. This could vastly reduce the size of the network and the number of parameters that need to be learned.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Note that pyramids have well-known limitations for dealing with large motions. In particular, small or thin objects that move quickly effectively disappear at coarse pyramid levels, making it impossible to capture their motion. Recent approaches for dealing with such large motions use sparse matching to augment standard pyramids. Future work should explore adding long-range matches to SPyNet. Alternatively Sevilla et al. define a channel constancy representation that preserves fine structures in a pyramid. The channels effectively correspond to filters that could be learned.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

A spatial pyramid can be thought of as the simple application of a set of linear filters. Here we take a standard spatial pyramid but one could learn the filters for the pyramid itself. SPyNet also uses a standard warping function to align images using the flow computed from the previous pyramid level. This too could be learned.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

An appealing feature of SPyNet is that it is small enough to fit on a mobile device. Future work will explore a mobile implementation and its applications. Additionally, we will explore extending the method to use more frames (e.g. 3 or 4). Multiple frames could enable the network to reason more effectively about occlusion.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

Finally, Flying Chairs is not representative of natural scene motions, containing many huge displacements. We are exploring new training datasets to improve performance on common sequences where the motion is less dramatic.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In summary, we have described a new optical flow method that combines features of classical optical flow algorithms with deep learning. In a sense, there are two notions of "deepness" here. First we use a "deep" spatial pyramid to deal with large motions. Second we use deep neural networks at each level of the spatial pyramid and train them to estimate a flow update at each level. This approach means that each network has less work to do than a fully generic flow method that has to estimate arbitrarily large motions. At each pyramid level we assume that the motion is small (on the order of a pixel). This is borne out by the fact that the network learns spatial and temporal filters that resemble classical derivatives of Gaussians and Gabors. Because each sub-task is so much simpler, our network needs many fewer parameters than previous methods like FlowNet. This results in a method with a small memory footprint that is faster than existing methods. At the same time, SPyNet achieves an accuracy comparable to FlowNet, surpassing it in several benchmarks. This opens up the promise of optical flow that is both accurate, practical, and widely deployable.
