<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation

Topics include Diffusion models, Control, ChopGrad.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent video diffusion models achieve high-quality generation through recurrent frame processing where each frame generation depends on previous frames. However, this recurrent mechanism means that training such models in the pixel domain incurs prohibitive memory costs, as activations accumulate across the entire video sequence. This fundamental limitation also makes fine-tuning these models with pixel-wise losses computationally intractable for long or high-resolution videos. This paper introduces ChopGrad, a truncated backpropagation scheme for video decoding, limiting gradient computation to local frame windows while maintaining global consistency. We provide a theoretical analysis of this approximation and show that it enables efficient fine-tuning with frame-wise losses. ChopGrad reduces training memory from scaling linearly with the number of video frames (full backpropagation) to constant memory, and compares favorably to existing state-of-the-art video diffusion models across a suite of conditional video generation tasks with pixel-wise losses, including video super-resolution, video inpainting, video enhancement of neural-rendered scenes, and controlled driving video generation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent methods in latent video diffusion are capable of generating high-resolution videos over long time horizons. Similar to latent image diffusion models, latent video diffusion models rely on pre-trained autoencoders to compress videos into latent embeddings and then learn over these embeddings. An enabling factor for recent video diffusion results is the use of temporal compression, where the autoencoder not only compresses video frames along spatial dimensions, but also along the temporal dimension.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Temporal compression groups multiple image frames into a single latent frame group. To incentivize temporal consistency between these frame groups causal caching has been introduced. This technique appends embeddings from previous frame group encodings onto the beginning of subsequent frame groups at each layer of the video encoder and decoder. Notably, this approach introduces a recurrent structure into the autoencoder, where the dependency graph of video latents requires gradients to be propagated through all previous frame embeddings.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, most successful latent video diffusion models are trained within the latent space, meaning gradients are not propagated through the encoder or decoder during latent video diffusion training. As such, existing methods make *pixel-wise losses intractable* for long-duration videos as the gradients of these losses require the recurrent accumulation of activations through the decoder. These pixel-level perceptual losses are used extensively in finetuning image diffusion models and video models with *short-duration*, low-resolution videos in applications such as single-step model distillation, enhancement of neural rendered scenes, image translation, video super-resolution, and controlled driving video generation. In work such as, the decoder itself is finetuned, making support for pixel-wise losses a strict requirement for training these types of models.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To enable pixel-wise losses for high-resolution, long duration video diffusion, this work introduces ChopGrad, a truncated backpropagation scheme for video decoding (Fig. 1). Truncated backpropagation prevents activation accumulation over the full unrolled network by limiting the number of previous frames the gradients can propagate through. To validate this, we define latent temporal locality to demonstrate that the effect of prior video frames in the gradient error drops off at an exponential rate. We show that the proposed method enables efficient training using pixel-wise losses, such as the LPIPS loss, across a variety of tasks and multiple video diffusion models. We evaluate our method on several applications, including video super-resolution, video inpainting, video enhancement of neural rendered scenes, and controlled driving video generation, outperforming existing latent video diffusion adaptation methods in terms of quantitative frame-wise and video performance metrics. These results are achieved with modest computational resources (training times of approximately 3 to 4 hours on 4 to 8 A100 GPUs).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are: A mathematical derivation and error analysis of truncated backpropagation for causal video autoencoders, A memory-efficient, practical approach for implementing pixel-wise losses for fine-tuning latent video diffusion models that generalizes across multiple diffusion models, Validation of the method across several tasks requiring pixel-wise losses, including video super-resolution, video inpainting, video enhancement of neural-rendered scenes, and controlled driving video generation, comparing favorably to existing baselines in all experiments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "ChopGrad", "weight": 1.0} -->

In order to enable training of video diffusion models on long, high-resolution videos with pixel-wise losses while maintaining modest memory requirements we present ChopGrad, a novel method for backpropagating through the video decoder. Sections 3.1 and 3.2 report that popular pre-trained video autoencoders with causal caching demonstrate temporal locality, where frame groups only affect other frame groups in close temporal proximity. Motivated by this insight, ChopGrad applies truncated backpropagation through time to the decoder cache to increase computational efficiency with minimal degradation in performance. With truncated backpropagation, gradients of each frame group are only able to accumulate to a portion of prior frame groups set by the truncation distance. This breaks the recursive loop present in popular video autoencoders and enables pixel-wise losses for long, high-resolution videos. In Section 3.3 we quantify temporal locality and truncation gradient error in the Wan2.1 decoder and transformer. Implementation details are provided in the Appendix.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Causal Caching in Temporal VAEs", "weight": 1.0} -->

The temporal VAE architecture with causal masking is first formalized. Let $\mathbf{X}=\{\mathbf{x}_{1},\mathbf{x}_{2},\ldots,\mathbf{x}_{T}\}$ denote a video sequence of $T$ frames, where each frame $\mathbf{x}_{t}\in\mathbb{R}^{H\times W\times C}$ has height $H$, width $W$, and $C$ channels.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Causal Caching in Temporal VAEs", "weight": 1.0} -->

The 3D VAE encoder groups consecutive frames into non-overlapping segments. For a frame group of size $G$, the $i$-th frame group contains frames $\mathbf{X}_{i}=\{\mathbf{x}_{iG},\mathbf{x}_{iG+1},\ldots,\mathbf{x}_{iG+G-1}\}$ for $i=0,1,2,\ldots,\lceil T/G\rceil$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Causal Caching in Temporal VAEs", "weight": 1.0} -->

Let $\mathbf{z}_{i,m}\in\mathbb{R}^{d_{m}\times T^{\prime}\times W^{\prime}\times H^{\prime}}$ be the video latent embedding of frame group $i$ at encoder layer $m$, where $H^{\prime},W^{\prime}$ are the down-sampled spatial dimensions, $T^{\prime}$ is the down-sampled temporal dimension, and $d_{m}$ is the latent dimension for layer $m$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Causal Caching in Temporal VAEs", "weight": 1.0} -->

The causal caching mechanism ensures that the decoder ($\mathcal{D}$) for frame group $i$ receives context from the previous group. Specifically, let $\mathbf{z}_{i-1,m}^{c}$ denote the causal cache of size $N$ of decoded features from group $i-1$ for the decoder layer $m$. The decoder then reconstructs the frames and constructs the cache The causal structure creates a recurrent dependency where the pixel-wise loss $\mathcal{L}^{\text{pix}}_{i}$ for group $i$ depends on all previous groups through the concatenated context $\mathbf{z}_{i-1}^{c}$ at each decoder layer.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Truncated Backpropagation and Locality", "weight": 1.0} -->

Truncated backpropagation leverages temporal locality to enable efficient training while preserving the essential temporal dependencies. The following analysis focuses on causal caching within the decoder network.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Truncated Backpropagation and Locality", "weight": 1.0} -->

Let $\mathbf{z}_{i}\in\mathbb{R}^{d}$ denote the unrolled latent, where the layer indices $m$ are omitted for notational convenience. Let $D(i,j)$ be a distance metric such that $D(i,j)=0$ if and only if $i$ and $j$ refer to latents belonging to the same frame group. This index-based distance formalism allows us to reason about temporal proximity and the influence of one latent on another.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Truncated Backpropagation and Locality", "weight": 1.0} -->

Let $J_{i,j}=\partial\mathbf{z}_{i}/\partial\mathbf{z}_{j}\in\mathbb{R}^{d\times d}$ denote the Jacobian of latent $i$ with respect to latent $j$. The scalar influence measure is then defined as for a chosen matrix norm. This quantity captures the effect of latent $j$ on latent $i$ and is a vector-norm on a vector space.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Truncated Backpropagation and Locality", "weight": 1.0} -->

Temporal locality is defined as the existence of constants $C,\alpha>0$ such that the influence measure decays exponentially with distance Intuitively, this means that a latent only meaningfully affects nearby latents in time. Using the chain rule, the gradient of the overall loss $\mathcal{L}$ with respect to a latent $\mathbf{z}_{i}$ decomposes as Taking the norm of both sides and applying the triangle inequality, which shows that the loss gradient at $\mathbf{z}_{i}$ is dominated by contributions from latents in close temporal proximity assuming temporal locality holds. Our key insight is that the temporal locality enables effective truncated backpropagation in the 3D VAE decoder. When we truncate gradients to only flow through a limited number of previous frame groups, the exponential decay in the influence measure ensures that the approximation error is bounded.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Truncated Backpropagation and Locality", "weight": 1.0} -->

Specifically, for truncated backpropagation at temporal distance $D_{\text{trunc}}$, the error in gradient computation is bounded by where $\mathcal{L}_{\text{trunc}}$ denotes the loss computed with truncated backpropagation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Truncated Backpropagation and Locality", "weight": 1.0} -->

A truncation distance $D_{\text{trunc}}\geq\frac{1}{\alpha}\log(\frac{C}{\epsilon})$ can therefore be chosen to satisfy a desired error tolerance $\epsilon$. In practice, the network still learns effectively with a small truncation distance as shown in Sections 3.3 and 4.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Truncated Backpropagation and Locality", "weight": 1.0} -->

The integration of causal caching with truncated backpropagation creates a hybrid approach: the network backbone can still attend to all video latent embeddings for global temporal understanding, while the 3D VAE decoder operates with limited temporal context, reducing computational complexity. This design preserves essential temporal dependencies while making large-scale video diffusion model training using pixel-wise losses computationally tractable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Temporal Locality", "weight": 1.0} -->

We analyze the proposed method by first confirming that temporal locality holds in the popular WAN 2.1 video decoder. The locality measure is averaged across several videos, each with $97$ frames and down-sampled to a resolution of $64\times 128$ to prevent prohibitive memory requirements. Fig. 3 reports the mean of the influence measure as a function of temporal distance, where a distance of $0$ indicates pixel $i$ is in the frame group of latent $j$. Notably, the locality measure decays at an exponential rate, meaning the influence of pixels on frame groups significantly decreases as the temporal distance increases. This property is demonstrated implicitly for other 3D VAEs by the results presented in Section 4.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Decoder Input Gradient Error", "weight": 1.0} -->

We likewise present the gradient error between the full and truncated backpropagation algorithms as a function of truncation distance. Gradients are computed by backpropagating pixel-wise losses to each decoder input latent considering varying truncation distances. Reported results are the absolute and relative difference between the gradients for the truncated distance and the full backpropagation scheme. Differences are measured using the Frobenius matrix norm and these, along with relative differences, are presented in Fig. 5. From this plot we see that, even for low truncation distances, gradients approach those of full backpropagation, confirming that truncated backpropagation can be applied with minimal degradation in temporal consistency as the decoder network only considers small temporal neighborhoods.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Effect on Backbone Model Parameters", "weight": 1.0} -->

Next, we evaluate the effect of gradient truncation on the backbone model parameters during training by computing the average gradient of the parameters of the public Wan 2.1 1.3B transformer checkpoint over the entire training set of the DL3DV-benchmark dataset (see Section 4.2), around 100 videos. We perform this computation over a range of truncation distances and compare to the gradients of the full backwards pass, with results presented in Fig. 4. Reported is the normalized mean absolute error (MAE) and cosine similarity, computed by flattening all model parameters into a single vector. The error is large for small truncation distances, indicating that the errors introduced by truncation are not averaged out over the dataset, and are propagated to model parameters. However, the high cosine similarity indicates that the error is primarily one of magnitude, not direction, and since gradient magnitudes are scaled by optimizers, the impact on training is negligible. This is confirmed by the results in Table 2, where increasing truncation distance only modestly improves performance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Runtime and Memory", "weight": 1.0} -->

Fig. 6 confirms that the proposed approach scales linearly with respect to truncation distance in terms of both computational time and memory. We reiterate that memory use is constant with respect to video length. To further save on memory, gradients are truncated spatially as well as temporally, such that gradients are computed over spatial chunks of the video separately. This spatial locality is illustrated in Fig. 7 and has been explored and leveraged by existing state-of-the-art video diffusion models.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Applications", "weight": 1.0} -->

We validate the efficacy of ChopGrad in four applications across multiple diffusion models: video super-resolution (Sec. 4.1), novel view synthesis (Sec. 4.2), video inpainting (Sec. 4.3), and controlled driving video generation (Sec. 4.4).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Video Super-Resolution", "weight": 1.0} -->

We first show that adding ChopGrad to a state-of-the-art video super-resolution method yields significant improvements in perceptual losses by finetuning DOVE using ChopGrad. DOVE finetunes CogVideoX, a DiT (Diffusion Transformer) model, for super-resolution. DOVE uses pixel-wise losses, including MSE and DISTS, but is forced to encode and decode each video frame separately during loss computation due to memory constraints, reducing inter-frame consistency and requiring the addition of a frame consistency loss to attempt to compensate for this. In contrast, for ChopGrad, we start with the publicly available DOVE checkpoint and perform full finetuning on the HQ-VSR dataset for 500 steps using video lengths of 24 frames, omitting interframe consistency losses. We use frame-wise DISTS loss with a weight of 0.1 and pixel-wise MSE with a weight of 1. All other settings are consistent with the original DOVE Stage-2 implementation, except that in DOVE 80% of the batches are images, not videos, while we train on videos only. For the DOVE baseline, the publicly available DOVE checkpoint is used.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Video Super-Resolution", "weight": 1.0} -->

As we found additional fine-tuning using the original DOVE method to result in equivalent performance, the results for the original model are presented.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Video Super-Resolution", "weight": 1.0} -->

Quantitative results for video super-resolution are presented in Table 1. The addition of the proposed truncated backpropagation scheme improves performance across the majority of datasets and metrics, and the improvements are more pronounced for perceptual metrics (LPIPS and DISTS). Selected frames from processed videos are shown in Fig. 8, where ChopGrad synthesizes fine-grained details such as fur, hair, and clouds better than the baseline approach.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Artifact Removal in Novel View Synthesis", "weight": 1.0} -->

Next, we use ChopGrad for refining renders from imperfect neural rendering models, which has recently become an established task. Renders of 3D Gaussian Splatting novel view synthesis methods often contain artifacts such as "floaters" that a set of recent diffusion models mitigate. Specifically, MVSplat-360 and Difix3D+ are designed for this task. MVSplat-360 is trained to refine video sequences of 14 frames rendered from 3DGS models while Difix is trained to refine individual frames. As a result, MVSplat-360 operates at a lower resolution ($448\times 256$) with a small window of temporal consistency while Difix operates at a higher resolution ($960\times 544$) but has no capacity to enforce temporal consistency. While MVSplat-360 and Difix both leverage pixel-wise losses, they are unable to scale to long and high-resolution videos.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Artifact Removal in Novel View Synthesis", "weight": 1.0} -->

We generate a dataset using the DL3DV-Benchmark, a collection of 140 videos and camera trajectories. Gaussian splat models are generated using every $50$th frame of each video and rendered videos are constructed along entire camera trajectories. For ChopGrad, we initialize the video diffusion model from a pre-trained Wan 2.1 14B model and fine-tune the transformer backbone for 10 epochs. Difix is fine-tuned for 10000 steps on the same data. As MVSplat-360 is trained on the DL3DV dataset, no fine-tuning is applied. We found that using the MVSplat-360 refinement model on our rendered videos led to poor performance. Performance was significantly improved using the same number of sparse views for constructing the 3DGS model when using the views specified in the MVSplat-360 repository. As such, we opt to use these improved selections for computing MVSplat-360 metrics.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Artifact Removal in Novel View Synthesis", "weight": 1.0} -->

Fig. 9 depicts ChopGrad alongside the baseline methods for several scenes from the DL3DV-Benchmark test set and Table 2 presents quantitative results. ChopGrad out-performs the baselines across all metrics except temporal flickering where results are competitive with MVSplat-360. A user study, available in the Appendix, also found that *$95.6\%$ of users preferred the videos generated by ChopGrad* over those generated by MVSplat-360 or Difix. Notably, while MVSplat-360 requires 60K training iterations, ChopGrad requires a small number of fine-tuning iterations when starting with the WAN2.1 14B pre-trained model. This demonstrates that ChopGrad enables diffusion models to quickly generalize to unseen tasks by fine-tuning using pixel-space losses.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Artifact Removal in Novel View Synthesis", "weight": 1.0} -->

To demonstrate that the performance gains are a result of pixel-wise losses enabled by ChopGrad and not simply a more powerful backbone, we report ablation experiments in Table 2 (bottom section) and a qualitative comparison in Fig. 10, where ChopGrad is trained using only MSE loss in the latent space and using various truncation distances. While training only on the video latents is faster, the perceptual quality is worse and blurring is prevalent, especially in regions with fine details. As discussed in Section 3.3, truncation distance has a minor impact on result quality. Videos of the DL3DV-Benchmark for ChopGrad and baselines can be found in the Appendix.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Video Inpainting", "weight": 1.0} -->

We demonstrate that in video inpainting applications, ChopGrad allows for reducing inference time by $50\times$ while remaining on-par in terms of quality. We evaluate ChopGrad for video inpainting on three datasets: DL3DV-Benchmark, Waymo Open Dataset, and ROVI. For DL3DV-Benchmark and Waymo, we mask a fixed central region covering half the height and width of each frame and use an uninformative prompt. With ROVI, we use the included object masks and text descriptions. For ChopGrad we finetune a Wan 2.1 14B model using latent MSE and pixel LPIPS losses for single-step inference using a truncation distance of 1. The baseline is VACE 14B, a control adapter for Wan 2.1 14B which is trained for a variety of tasks, including inpainting. VACE inference is performed using the default 50 steps from the VACE repository. For all datasets, we train both ChopGrad and VACE the same number of steps. More training details are available in the Appendix.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Video Inpainting", "weight": 1.0} -->

Quantitative results are reported in Table 3, qualitative results in Fig. 11. ChopGrad outperforms VACE on reconstruction-based metrics and maintains similar video quality metrics (VBench overall quality score within $1\%$ across all datasets) while reducing inference time compute budget by $50\times$. FVD (Fréchet Video Distance) is higher for ChopGrad on ROVI but lower for the other two datasets, likely stemming from the overall more extreme masking in D3LDV and ROVI. Qualitatively, we observe that the ChopGrad model adheres better to the scene and introduces fewer novel structures compared to VACE, occasionally at the cost of visual quality. In the more extreme masking regime of DL3DV and Waymo, VACE is penalized less for novel structures (relative to ChopGrad), as the unmasked region is less informative about the region inside the mask, resulting in smaller relative improvements in reconstruction-based losses.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Controlled Driving Video Generation", "weight": 1.0} -->

Visually realistic controlled driving video generation is essential for autonomous vehicle safety as it enables validation of vehicle behavior in rarely encountered scenarios. 3DGS offers powerful scene reconstruction approaches, and recent neural driving simulators allow for manipulation of vehicles and reconstructed assets using scene graphs of reconstructed splats to enable this kind of simulation. However, large manipulation of vehicles and assets in these simulators leads to myriad visual artifacts (see Naive Insertion columns of Fig. 12 for examples). Post-processing videos rendered from such neural scenes with single-step diffusion is a promising approach for overcoming these issues, but existing methods such as suffer from resolution / duration limitations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Controlled Driving Video Generation", "weight": 1.0} -->

Following we create a dataset based on Waymo Open Dataset where 3DGS models are constructed, then assets are extracted and reinserted, producing the desired artifacts and input/output pairs to train and test. Dataset construction details are presented in the Appendix.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Controlled Driving Video Generation", "weight": 1.0} -->

We demonstrate ChopGrad for controlled driving video generation on Mirage with our own Wan2.1-based implementation (details in the Appendix), as we were unable to acquire the original implementation even after contacting the authors. We train our implementation on 9-frame clips at a resolution of 480x832. After training Mirage we performed inference and evaluation at high resolution / duration (720x1280, 97 frames) as up-scaling training resolution outputs yielded poorer results. Subsequently, we finetuned Mirage's harmonization stage model using ChopGrad for 1000 steps at 720x1280 resolution, 49 frame duration, and performed inference on 49 frame segments. Results are reported in Table 4 and Fig. 12. Quantitative metrics are improved across all tests, while inspection of the qualitative results shows that finetuning Mirage with ChopGrad improves lighting fixing, artifact removal, and shadow insertion. Notably, the parameters of the decoder itself are finetuned in Mirage, confirming that ChopGrad can be used for decoder, as well as transformer, training.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce ChopGrad, a truncated backpropagation approach that enables pixel-wise supervision at high resolutions and long durations in latent video diffusion models with causal caching. In architectures where the decoder is finetuned (e.g. ) this capability is required, while in others it leads to significantly improved results (bottom of Table 2). Applications of such models trained with pixel-wise losses are numerous, including single-step model distillation, enhancement of neural rendered scenes, image translation, video super-resolution, and controlled driving video generation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

By analyzing latent temporal locality, we demonstrate that long-range gradient dependencies in causal video autoencoders decay exponentially, allowing gradients to be truncated without compromising performance. This insight enables efficient fine-tuning of high-resolution, long-duration video diffusion models using perceptual losses that were previously intractable due to recursive activation accumulation.
