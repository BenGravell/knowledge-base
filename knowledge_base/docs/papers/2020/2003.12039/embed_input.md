<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RAFT: Recurrent All-Pairs Field Transforms for Optical Flow

Topics include Optical flow, RAFT, Recurrent refinement, All-pairs correlation, 4D correlation volume, Dense matching, Cross-dataset generalization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

RAFT reframes optical flow around a dense all-pairs correlation volume and a recurrent update operator that repeatedly refines a single high-quality field. Its accuracy, generalization, and compact recurrent design made it a dominant baseline for modern learned optical flow.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Recurrent All-Pairs Field Transforms (RAFT), a new deep network architecture for optical flow. RAFT extracts per-pixel features, builds multi-scale 4D correlation volumes for all pairs of pixels, and iteratively updates a flow field through a recurrent unit that performs lookups on the correlation volumes. RAFT achieves state-of-the-art performance. On KITTI, RAFT achieves an F1-all error of 5.10%, a 16% error reduction from the best published result (6.10%). On Sintel (final pass), RAFT obtains an end-point-error of 2.855 pixels, a 30% error reduction from the best published result (4.098 pixels). In addition, RAFT has strong cross-dataset generalization as well as high efficiency in inference time, training speed, and parameter count. Code is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optical flow is the task of estimating per-pixel motion between video frames. It is a long-standing vision problem that remains unsolved. The best systems are limited by difficulties including fast-moving objects, occlusions, motion blur, and textureless surfaces.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optical flow has traditionally been approached as a hand-crafted optimization problem over the space of dense displacement fields between a pair of images. Generally, the optimization objective defines a trade-off between a *data* term which encourages the alignment of visually similar image regions and a *regularization* term which imposes priors on the plausibility of motion. Such an approach has achieved considerable success, but further progress has appeared challenging, due to the difficulties in hand-designing an optimization objective that is robust to a variety of corner cases.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, deep learning has been shown as a promising alternative to traditional methods. Deep learning can side-step formulating an optimization problem and train a network to directly predict flow. Current deep learning methods have achieved performance comparable to the best traditional methods while being significantly faster at inference time. A key question for further research is designing effective architectures that perform better, train more easily and generalize well to novel scenes.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce Recurrent All-Pairs Field Transforms (RAFT), a new deep network architecture for optical flow. RAFT enjoys the following strengths: *State-of-the-art accuracy*: On KITTI, RAFT achieves an F1-all error of 5.10%, a 16% error reduction from the best published result (6.10%). On Sintel (final pass), RAFT obtains an end-point-error of 2.855 pixels, a 30% error reduction from the best published result (4.098 pixels).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Strong generalization*: When trained only on synthetic data, RAFT achieves an end-point-error of 5.04 pixels on KITTI, a 40% error reduction from the best prior deep network trained on the same data (8.36 pixels).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*High efficiency*: RAFT processes $1088 \times 436$ videos at 10 frames per second on a 1080Ti GPU. It trains with 10X fewer iterations than other architectures. A smaller version of RAFT with 1/5 of the parameters runs at 20 frames per second while still outperforming all prior methods on Sintel.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

RAFT consists of three main components: a feature encoder that extracts a feature vector for each pixel; a correlation layer that produces a 4D correlation volume for all pairs of pixels, with subsequent pooling to produce lower resolution volumes; a recurrent GRU-based *update operator* that retrieves values from the correlation volumes and iteratively updates a flow field initialized at zero. Fig. 1 illustrates the design of RAFT.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The RAFT architecture is motivated by traditional optimization-based approaches. The feature encoder extracts per-pixel features. The correlation layer computes visual similarity between pixels. The update operator mimics the steps of an iterative optimization algorithm. But unlike traditional approaches, features and motion priors are not handcrafted but learned---learned by the feature encoder and the update operator respectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The design of RAFT draws inspiration from many existing works but is substantially novel. First, RAFT maintains and updates a single fixed flow field at high resolution. This is different from the prevailing coarse-to-fine design in prior work, where flow is first estimated at low resolution and upsampled and refined at high resolution. By operating on a single high-resolution flow field, RAFT overcomes several limitations of a coarse-to-fine cascade: the difficulty of recovering from errors at coarse resolutions, the tendency to miss small fast-moving objects, and the many training iterations (often over 1M) typically required for training a multi-stage cascade.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, the update operator of RAFT is recurrent and lightweight. Many recent works have included some form of iterative refinement, but do not tie the weights across iterations and are therefore limited to a fixed number of iterations. To our knowledge, IRR is the only deep learning approach that is recurrent. It uses FlowNetS or PWC-Net as its recurrent unit. When using FlowNetS, it is limited by the size of the network (38M parameters) and is only applied up to 5 iterations. When using PWC-Net, iterations are limited by the number of pyramid levels. In contrast, our update operator has only 2.7M parameters and can be applied 100+ times during inference without divergence.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, the update operator has a novel design, which consists of a convolutional GRU that performs lookups on 4D multi-scale correlation volumes; in contrast, refinement modules in prior work typically use only plain convolution or correlation layers.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We conduct experiments on Sintel and KITTI. Results show that RAFT achieves state-of-the-art performance on both datasets. In addition, we validate various design choices of RAFT through extensive ablation studies.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Approach", "weight": 1.0} -->

Given a pair of consecutive RGB images, $I_{1}$, $I_{2}$, we estimate a dense displacement field $(\mathbf{f}^{1},\mathbf{f}^{2})$ which maps each pixel $(u,v)$ in $I_{2}$ to its corresponding coordinates ${(u',v')} = {({u + {f^{1}{(u)}}},{v + {f^{2}{(v)}}})}$ in $I_{2}$. An overview of our approach is given in Figure 1. Our method can be distilled down to three stages: feature extraction, computing visual similarity, and iterative updates, where all stages are differentiable and composed into an end-to-end trainable architecture.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Feature Extraction", "weight": 1.0} -->

Features are extracted from the input images using a convolutional network. The feature encoder network is applied to both $I_{1}$ and $I_{2}$ and maps the input images to dense feature maps at a lower resolution. Our encoder, $g_{\theta}$ outputs features at 1/8 resolution $g_{\theta}:{{\mathbb{R}}^{H \times W \times 3}\mapsto{\mathbb{R}}^{{{{H/8} \times W}/8} \times D}}$ where we set $D = 256$. The feature encoder consists of 6 residual blocks, 2 at 1/2 resolution, 2 at 1/4 resolution, and 2 at 1/8 resolution (more details in the supplemental material).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Feature Extraction", "weight": 1.0} -->

We additionally use a context network. The context network extracts features only from the first input image $I_{1}$. The architecture of the context network, $h_{\theta}$ is identical to the feature extraction network. Together, the feature network $g_{\theta}$ and the context network $h_{\theta}$ form the first stage of our approach, which only need to be performed once.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

We compute visual similarity by constructing a full correlation volume between all pairs. Given image features ${g_{\theta}{(I_{1})}} \in {\mathbb{R}}^{H \times W \times D}$ and ${g_{\theta}{(I_{2})}} \in {\mathbb{R}}^{H \times W \times D}$, the correlation volume is formed by taking the dot product between all pairs of feature vectors. The correlation volume, $\mathbf{C}$, can be efficiently computed as a single matrix multiplication.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

Correlation Pyramid: We construct a 4-layer pyramid $\{\mathbf{C}^{1},\mathbf{C}^{2},\mathbf{C}^{3},\mathbf{C}^{4}\}$ by pooling the last two dimensions of the correlation volume with kernel sizes 1, 2, 4, and 8 and equivalent stride (Figure 2). Thus, volume $\mathbf{C}^{k}$ has dimensions ${{{H \times W \times H}/2^{k}} \times W}/2^{k}$. The set of volumes gives information about both large and small displacements; however, by maintaining the first 2 dimensions (the $I_{1}$ dimensions) we maintain high resolution information, allowing our method to recover the motions of small fast-moving objects.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

Correlation Lookup: We define a lookup operator $L_{\mathbf{C}}$ which generates a feature map by indexing from the correlation pyramid. Given a current estimate of optical flow $(\mathbf{f}^{1},\mathbf{f}^{2})$, we map each pixel $\mathbf{x} = {(u,v)}$ in $I_{1}$ to its estimated correspondence in $I_{2}$: $\mathbf{x}' = {({u + {f^{1}{(u)}}},{v + {f^{2}{(v)}}})}$. We then define a local grid around $\mathbf{x}'$ as the set of integer offsets which are within a radius of $r$ units of $\mathbf{x}'$ using the L1 distance. We use the local neighborhood $\mathcal{N}{(\mathbf{x}')}_{r}$ to index from the correlation volume.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

Since $\mathcal{N}{(\mathbf{x}')}_{r}$ is a grid of real numbers, we use bilinear sampling.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

We perform lookups on all levels of the pyramid, such that the correlation volume at level $k$, $\mathbf{C}^{k}$, is indexed using the grid $\mathcal{N}{({\mathbf{x}'/2^{k}})}_{r}$. A constant radius across levels means larger context at lower levels: for the lowest level, $k = 4$ using a radius of 4 corresponds to a range of 256 pixels at the original resolution. The values from each level are then concatenated into a single feature map.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

Efficient Computation for High Resolution Images: The all pairs correlation scales $O{(N^{2})}$ where $N$ is the number of pixels, but only needs to be computed once and is constant in the number of iterations $M$. However, there exists an equivalent implementation of our approach which scales $O{({NM})}$ exploiting the linearity of the inner product and average pooling. Consider the cost volume at level $m$, $\mathbf{C}_{ijkl}^{m}$, and feature maps $g^{} = {g_{\theta}{(I_{1})}}$, $g^{} = {g_{\theta}{(I_{2})}}$: which is the average over the correlation response in the $2^{m} \times 2^{m}$ grid.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

In this alternative implementation, we do not precompute the correlations, but instead precompute the pooled image feature maps. In each iteration, we compute each correlation value on demand---only when it is looked up. This gives a complexity of $O{({NM})}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Computing Visual Similarity", "weight": 1.0} -->

We found empirically that precomputing all pairs is easy to implement and not a bottleneck, due to highly optimized matrix routines on GPUs---even for 1088x1920 videos it takes only 17% of total inference time. Note that we can always switch to the alternative implementation should it become a bottleneck.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Iterative Updates", "weight": 1.0} -->

Our update operator estimates a sequence of flow estimates $\{\mathbf{f}_{1},\ldots,\mathbf{f}_{N}\}$ from an initial starting point $\mathbf{f}_{0} = \mathbf{0}$. With each iteration, it produces an update direction $\Delta\mathbf{f}$ which is applied to the current estimate: $\mathbf{f}_{k + 1} = {{\Delta\mathbf{f}} + \mathbf{f}_{k + 1}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Iterative Updates", "weight": 1.0} -->

The update operator takes flow, correlation, and a latent hidden state as input, and outputs the update $\Delta\mathbf{f}$ and an updated hidden state. The architecture of our update operator is designed to mimic the steps of an optimization algorithm. As such, we used tied weights across depth and use bounded activations to encourage convergence to a fixed point. The update operator is trained to perform updates such that the sequence converges to a fixed point $\mathbf{f}_{k}\rightarrow\mathbf{f}^{\ast}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Iterative Updates", "weight": 1.0} -->

Initialization: By default, we initialize the flow field to 0 everywhere, but our iterative approach gives us the flexibility to experiment with alternatives. When applied to video, we test *warm-start* initialization, where optical flow from the previous pair of frames is forward projected to the next pair of frames with occlusion gaps filled in using nearest neighbor interpolation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Iterative Updates", "weight": 1.0} -->

Inputs: Given the current flow estimate $\mathbf{f}^{k}$, we use it to retrieve correlation features from the correlation pyramid as described in Sec. 3.2. The correlation features are then processed by 2 convolutional layers. Additionally, we apply 2 convolutional layers to the flow estimate itself to generate flow features. Finally, we directly inject the input from the context network. The input feature map is then taken as the concatenation of the correlation, flow, and context features.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Iterative Updates", "weight": 1.0} -->

Update: A core component of the update operator is a gated activation unit based on the GRU cell, with fully connected layers replaced with convolutions: where $x_{t}$ is the concatenation of flow, correlation, and context features previously defined. We also experiment with a separable ConvGRU unit, where we replace the $3 \times 3$ convolution with two GRUs: one with a $1 \times 5$ convolution and one with a $5 \times 1$ convolution to increase the receptive field without significantly increasing the size of the model.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Iterative Updates", "weight": 1.0} -->

Flow Prediction: The hidden state outputted by the GRU is passed through two convolutional layers to predict the flow update $\Delta\mathbf{f}$. The output flow is at 1/8 resolution of the input image. During training and evaluation, we upsample the predicted flow fields to match the resolution of the ground truth.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Iterative Updates", "weight": 1.0} -->

Upsampling: The network outputs optical flow at 1/8 resolution. We upsample the optical flow to full resolution by taking the full resolution flow at each pixel to be the convex combination of a 3x3 grid of its coarse resolution neighbors. We use two convolutional layers to predict a ${{{H/8} \times W}/8} \times {({8 \times 8 \times 9})}$ mask and perform softmax over the weights of the 9 neighbors. The final high resolution flow field is found by using the mask to take a weighted combination over the neighborhood, then permuting and reshaping to a $H \times W \times 2$ dimensional flow field. This layer can be directly implemented in PyTorch using the unfold function.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Supervision", "weight": 1.0} -->

We supervised our network on the $l_{1}$ distance between the predicted and ground truth flow over the full sequence of predictions, $\{\mathbf{f}_{1},\ldots,\mathbf{f}_{N}\}$, with exponentially increasing weights. Given ground truth flow $\mathbf{f}_{gt}$, the loss is defined as where we set $\gamma = 0.8$ in our experiments.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate RAFT on Sintel and KITTI. Following previous works, we pretrain our network on FlyingChairs and FlyingThings, followed by dataset specific finetuning. Our method achieves state-of-the-art performance on both Sintel (both clean and final passes) and KITTI. Additionally, we test our method on 1080p video from the DAVIS dataset to demonstrate that our method scales to videos of very high resolutions.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Implementation Details: RAFT is implemented in PyTorch. All modules are initialized from scratch with random weights. During training, we use the AdamW optimizer and clip gradients to the range $\lbrack{- 1},1\rbrack$. Unless otherwise noted, we evaluate after 32 flow updates on Sintel and 24 on KITTI. For every update, ${\Delta\mathbf{f}} + \mathbf{f}_{k}$, we only backpropgate the gradient through the $\Delta\mathbf{f}$ branch, and zero the gradient through the $\mathbf{f}_{k}$ branch as suggested.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Training Schedule: We train RAFT using two 2080Ti GPUs. We pretrain on FlyingThings for 100k iterations with a batch size of 12, then train for 100k iterations on FlyingThings3D with a batch size of 6. We finetune on Sintel for another 100k by combining data from Sintel, KITTI-2015, and HD1K similar to MaskFlowNet and PWC-Net+. Finally, we finetune on KITTI-2015 for an additionally 50k iterations using the weights from the model finetuned on Sintel. Details on training and data augmentation are provided in the supplemental material. For comparison with prior work, we also include results from our model when finetuning only on Sintel and only on KITTI.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sintel", "weight": 1.0} -->

We train our model using the FlyingChairs$\rightarrow$FlyingThings schedule and then evaluate on the Sintel dataset using the *train* split for validation. Results are shown in Table 1 and Figure 3, and we split results based on the data used for training. C + T means that the models are trained on FlyingChairs(C) and FlyingThings(T), while +ft indicates the model is finetuned on Sintel data. Like PWC-Net+ and MaskFlowNet we include data from KITTI and HD1K when finetuning. We train 3 times with different seeds, and report results using the model with the median accuracy on the clean pass of Sintel (train).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sintel", "weight": 1.0} -->

When evaluating on the Sintel(test) set, we finetune on the combined clean and final passes of the training set along with KITTI and HD1K data. Our method ranks 1st on both the Sintel clean and final passes, and outperforms all prior work by 0.9 pixels (36%) on the clean pass and 1.2 pixels (30%) on the final pass. We evaluate two versions of our model, Ours (two-frame) uses zero initialization, while Ours (warp-start) initializes flow by forward projecting the flow estimate from the previous frame. Since our method operates at a single resolution, we can initialize the flow estimate to utilize motion smoothness from past frames, which cannot be easily done using the coarse-to-fine model.

<!-- chunk {"id": "body-0040", "role": "body", "section": "KITTI", "weight": 1.0} -->

We also evaluate RAFT on KITTI and provide results in Table 1 and Figure 4. We first evaluate cross-dataset generalization by evaluating on the KITTI-15 (train) split after training on Chairs(C) and FlyingThings(T). Our method outperforms prior works by a large margin, improving EPE (end-point-error) from 8.36 to 5.04, which shows that the underlying structure of our network facilitates generalization. Our method ranks 1st on the KITTI leaderboard among all optical flow methods.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablations", "weight": 1.0} -->

We perform a set of ablation experiments to show the relative importance of each component. All ablated versions are trained on FlyingChairs(C) + FlyingThings(T). Results of the ablations are shown in Table 2. In each section of the table, we test a specific component of our approach in isolation, the settings which are used in our final model is underlined. Below we describe each of the experiments in more detail.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablations", "weight": 1.0} -->

Reference Model (bilinear upsampling), Training: 100k(C) → 60k(T) Features for Refinement Reference Model (convex upsampling), Training: 100k(C) → 100k(T) Table 2: Ablation experiments. Settings used in our final model are underlined. See Sec. 4.3 for details.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablations", "weight": 1.0} -->

Architecture of Update Operator: We use a gated activation unit based on the GRU cell. We experiment with replacing the convolutional GRU with a set of 3 convolutional layers with ReLU activation. We achieve better performance by using the GRU block, likely because the gated activation makes it easier for the sequence of flow estimates to converge.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablations", "weight": 1.0} -->

Weight Tying: By default, we tied the weights across all instances of the update operator. Here, we test a version of our approach where each update operator learns a separate set of weights. Accuracy is better when weights are tied and the parameter count is significantly lower.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablations", "weight": 1.0} -->

Context: We test the importance of context by training a model with the context network removed. Without context, we still achieve good results, outperforming all existing works on both Sintel and KITTI. But context is helpful. Directly injecting image features into the update operator likely allows spatial information to be better aggregated within motion boundaries.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablations", "weight": 1.0} -->

Feature Scale: By default, we extract features at a single resolution. We also try extracting features at multiple resolutions by building a correlation volume at each scale separately. Single resolution features simplifies the network architecture and allows fine-grained matching even at large displacements.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablations", "weight": 1.0} -->

Lookup Radius: The lookup radius specifies the dimensions of the grid used in the lookup operation. When a radius of 0 is used, the correlation volume is retrieved at a single point. Surprisingly, we can still get a rough estimate of flow when the radius is 0, which means the network is learning to use 0'th order information. However, we see better results as the radius is increased.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablations", "weight": 1.0} -->

Correlation Pooling: We output features at a single resolution and then perform pooling to generate multiscale volumes. Here we test the impact when this pooling is removed. Results are better with pooling, because large and small displacements are both captured.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Ablations", "weight": 1.0} -->

Correlation Range: Instead of all-pairs correlation, we also try constructing the correlation volume only for a local neighborhood around each pixel. We try a range of 32 pixels, 64 pixels, and 128 pixels. Overall we get the best results when the all-pairs are used, although a 128px range is sufficient to perform well on Sintel because most displacements fall within this range. That said, all-pairs is still preferable because it eliminates the need to specify a range. It is also more convenient to implement: it can be computed using matrix multiplication allowing our approach to be implemented entirely in PyTorch.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Ablations", "weight": 1.0} -->

Features for Refinement: We compute visual similarity by building a correlation volume between all pairs of pixels. In this experiment, we try replacing the correlation volume with a warping layer, which uses the current estimate of optical flow to warp features from $I_{2}$ onto $I_{1}$ and then estimates the residual displacement. While warping is still competitive with prior work on Sintel, correlation performs significantly better, especially on KITTI.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Ablations", "weight": 1.0} -->

Upsampling: RAFT outputs flow fields at 1/8 resolution. We compare bilinear upsampling to our learned upsampling module. The upsampling module produces better results, particularly near motion boundaries.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablations", "weight": 1.0} -->

Inference Updates: Although we unroll 12 updates during training, we can apply an arbitrary number of updates during inference. In Table 2 we provide numerical results for selected number of updates, and test an extreme case of 200 to show that our method doesn't diverge. Our method quickly converges, surpassing PWC-Net after 3 updates and FlowNet2 after 6 updates, but continues to improve with more updates.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Timing and Parameter Counts", "weight": 1.0} -->

Inference time and parameter counts are shown in Figure 5. Accuracy is determined by performance on the Sintel(train) final pass after training on FlyingChairs and FlyingThings (C+T). In these plots, we report accuracy and timing after 10 iterations, and we time our method using a GTX 1080Ti GPU. Parameters counts for other methods are taken as reported in their papers, and we report times when run on our hardware. RAFT is more efficient in terms of parameter count, inference time, and training iterations. Ours-S uses only 1M parameters, but outperforms PWC-Net and VCN which are more than 6x larger. We provide an additional table with numerical values for parameters, timing, and training iterations in the supplemental material.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Video of Very High Resolution", "weight": 1.0} -->

To demonstrate that our method scales well to videos of very high resolution we apply our network to HD video from the DAVIS dataset. We use 1080p (1088x1920) resolution video and apply 12 iterations of our approach. Inference takes 550ms for 12 iterations on 1080p video, with all-pairs correlation taking 95ms. Fig. 6 visualizes example results on DAVIS.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have proposed RAFT---Recurrent All-Pairs Field Transforms---a new end-to-end trainable model for optical flow. RAFT is unique in that it operates at a single resolution using a large number of lightweight, recurrent update operators. Our method achieves state-of-the-art accuracy across a diverse range of datasets, strong cross dataset generalization, and is efficient in terms of inference time, parameter count, and training iterations.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Acknowledgments: This work was partially funded by the National Science Foundation under Grant No. 1617767.
