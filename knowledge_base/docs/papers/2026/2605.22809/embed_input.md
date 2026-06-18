<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robust training and validation of Autonomous Driving Systems (ADS) require massive, diverse datasets. Proprietary data collected by Autonomous Vehicle (AV) fleets, while high-fidelity, are limited in scale, diversity of sensor configurations, as well as geographic and long-tail-behavioral coverage. In contrast, in-the-wild data from sources like dashcams offers immense scale and diversity, capturing critical long-tail scenarios and novel environments. However, this unstructured, in-the-wild video data is incompatible with ADS expecting structured, multi-modal sensor inputs for validation and training. To bridge this data gap, we propose Sensor2Sensor, a novel generative modeling paradigm that translates in-the-wild monocular dashcam videos into a high-fidelity, multi-modal sensor suite (AV logs) comprising multi-view camera images and LiDAR point clouds. A core challenge is the lack of paired training data. We address this by converting real AV logs into dashcam-style videos via 4D Gaussian Splatting (4DGS) reconstruction and novel-view rendering. Sensor2Sensor then utilizes a diffusion architecture to perform the generative conversion.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We perform comprehensive quantitative evaluations on the fidelity and realism of the generated sensor data. We demonstrate Sensor2Sensor's practical utility by converting challenging in-the-wild internet and dashcam footage into realistic, multi-modal data formats, further unlocking vast external data sources for AV development.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The validation of Autonomous Driving Systems (ADS) against the full spectrum of real-world driving scenarios remains a paramount challenge in the field. While generalist policies trained on aggregated data from diverse embodiments have shown promise, they do not obviate the need for rigorous, per-embodiment evaluation. This evaluation is non-negotiable for safety-critical systems, and its efficacy is fundamentally constrained by the profound scarcity of *long-tail data*. These long-tail scenarios encompass statistically rare yet safety-critical events, including erratic driving, sudden pedestrian maneuvers, and extreme weather or environmental conditions. Collecting such data organically is prohibitively expensive, requiring fleet-scale operations of immense cost and duration.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two main avenues have been explored to address this data deficiency. The first is de novo scenario synthesis using generative models. While this can create novel events, the generated data often suffers from a critical plausibility gap (non-physical dynamics) and a realism problem (low sensor fidelity) unsuitable for ADS validation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second avenue seeks to leverage the immense scale and diversity of "in-the-wild" third-party data, sourced from internet videos or partner dashcam fleets (Original Equipment Manufacturers, OEMs). These data are, by construction, grounded in physical reality, thus eliminating concerns of event plausibility. It is also naturally skewed towards the long-tail, as mundane events are less likely to be recorded or shared. This approach, however, suffers from a severe *embodiment gap*. This in-the-wild data is sensorially and geometrically misaligned with the target ADS platforms: it typically consists of a single monocular video, lacks the 360-degree multi-camera perspectives, and is devoid of critical modalities like LiDAR. This frames the problem as a highly complex, unpaired domain translation task. Unfortunately, classical unpaired translation methods are ill-equipped to bridge such a vast domain gap, as they lack the strong geometric priors and modal capacity to generate a coherent, temporally-consistent, multi-modal sensor suite from a single, uncalibrated video stream.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose *Sensor2Sensor*, a novel generative paradigm for cross-embodiment sensor conversion that synthesizes the advantages of both paths. As shown in Figure LABEL:fig:teaser, Sensor2Sensor inherits the real-world plausibility of in-the-wild data while generatively re-rendering it into the precise, multi-modal format of a target AV embodiment.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The central challenge in training Sensor2Sensor is the absence of large-scale, paired (dashcam, AV log) training data. We circumvent this limitation by proposing a novel synthetic data-pairing pipeline. We leverage existing AV logs, which, by design, contain rich 3D information and 360-degree coverage. This high-fidelity data enables us to first reconstruct a 4D scene representation via dynamic 3D Gaussian Splatting (3DGS). From this reconstructed scene, we can render novel, synthetic-yet-realistic dashcam views, complete with augmentations of intrinsic and extrinsic parameters sampled from real-world dashcam distributions. This process yields the required paired training corpus: (synthetic dashcam, real AV log).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

With this paired dataset, we design Sensor2Sensor as a conditional diffusion model for multi-sensor (eight cameras) and multi-modal (camera and LiDAR) output, conditioned on the input dashcam video. This use of diffusion for geometrically-aware domain adaptation aligns with recent successes in cross-domain transfer.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate Sensor2Sensor through a comprehensive evaluation strategy. Quantitative fidelity is assessed using a bespoke, manually-collected ground-truth dataset. Concurrently, a broad qualitative analysis demonstrates the model's efficacy in converting challenging, real-world in-the-wild videos into realistic and usable sensor logs. Our results affirm that Sensor2Sensor achieves state-of-the-art (SOTA) fidelity, further unlocking vast, previously-incompatible data sources for AV development.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce Sensor2Sensor, a novel generative paradigm for translating in-the-wild monocular videos into high-fidelity, multi-modal, and multi-sensor AV logs specific to a target vehicle embodiment.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a pipeline using dynamic 3D Gaussian Splatting to reconstruct scenes from raw AV logs, rendering paired realistic dashcam views as high-quality training data for diffusion models.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a conditional diffusion architecture, designed to be multi-sensor multi-modal, capable of geometrically-aware cross-embodiment sensor conversion.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate, through comprehensive evaluation, that our method further unlocks the vast scale and diversity of in-the-wild video, converting challenging internet footage into realistic, usable data for AV development.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

Generative World Models and High-Fidelity Sensor Synthesis. Generative World Models, often built upon diffusion architectures, are now foundational for physical AI, enabling the synthesis of photorealistic, physics-based data. Prominent examples, such as Wayve's GAIA-1 and the NVIDIA Cosmos platform, primarily target scenario generation, future prediction, and planning for closed-loop simulation. While powerful, their objective is orthogonal to our goal of data *conversion*. However, the success of conditional diffusion in *intra*-embodiment sensor translation validates its use for our complex, multi-modal task. Specifically, Camera-to-LiDAR generation using models like LiDMs successfully navigates the spatial and modal mismatch between camera views and 3D point clouds. More recent cross-modality frameworks like X-Drive further demonstrate the ability to generate consistent multi-sensor data. Sensor2Sensor extends this conditional diffusion capability to the more challenging *cross-embodiment* setting, translating a single monocular stream into a geometrically-accurate, multi-sensor AV log. This complex translation necessitates a geometrically-anchored training corpus, which motivates our integration of reconstructive techniques.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

Reconstructive World Models and 4D Scene Representation. Reconstructive World Models are essential for high-fidelity 4D (spatio-temporal) scene representation, enabling closed-loop evaluation and novel view synthesis. Advances in explicit representations, particularly 3D Gaussian Splatting (3DGS), have allowed for real-time, photorealistic rendering and dynamic scene modeling in autonomous driving. Methods like PAGS and Driv3R focus on decomposing the scene or achieving fast, dense 4D reconstruction from multi-view inputs, ensuring geometric accuracy and temporal consistency. These models serve as powerful "data machines" to augment viewpoints, as seen in works like DriveDreamer4D. Sensor2Sensor critically repurposes this reconstructive capability to resolve the training data bottleneck. We reconstruct scenes from existing AV logs via 4DGS, treating the reconstruction as a geometric oracle. This allows us to render a synthetic dashcam view from a novel, external viewpoint. This process yields a perfectly paired training corpus, transforming the cross-embodiment challenge into a fully supervised, geometrically-anchored generation task.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Our approach consists of two key stages: a scalable data curation pipeline using 4DGS to synthesize paired training data (Section 3.1), and a diffusion model that generates synchronized multi-view imagery and LiDAR point clouds conditioned on a single camera input (Section 3.2). We further extend this to temporally consistent video generation via auto-regressive modeling (Section 3.3).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Synthetic Sensor Simulation via 4DGS", "weight": 1.0} -->

4DGS for Autonomous Driving. We use a variant of 3D Gaussian Splatting (3DGS) with support for dynamic rigid (e.g. vehicles) and deformable (e.g. pedestrian) objects to construct 4D representations of diverse AV scenarios. In total, approximately 100,000 scenes of 10s duration were chosen for reconstruction. Each scene contains multi-view camera data spanning 360 degrees as well as LiDAR data, which is used to initialize and regularize the geometry of the 3D Gaussian Splats, though optional. Splats belonging to moving objects are accumulated using a canonical object model to achieve more complete object coverage. Once a scene is optimized, it can be rendered using virtual cameras with augmented intrinsic and extrinsic parameters to mimic the optics and placement of dashcams found in-the-wild. Note that due to the purely reconstructive nature of 3DGS, the best rendering quality is achieved within a bounded region around the original camera poses. Unlike the original 3DGS formulation, we use a ray-tracing-based rendering approach to better support fish-eye optics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Synthetic Sensor Simulation via 4DGS", "weight": 1.0} -->

Third-party Camera Synthesis. We leverage high-fidelity 4DGS representations to synthesize a large, paired training corpus by rendering virtual cameras (Figure 2). This process explicitly bridges the domain gap between the source sensor data and the target third-party sensors (e.g., dashcams). The synthesis pipeline models two primary sources of sensor variation found in off-the-shelf dashcam systems: *Intrinsic Parameters* ($\mathbf{p}_{i}$): Generated by sampling realistic focal lengths, principal points, and distortion coefficients ($\kappa$). This step emulates the diverse optical profiles of low-cost, wide-angle lenses prone to significant distortion. *Extrinsic Parameters* ($\mathbf{p}_{e}$): Sampled as 6-DoF poses, $\mathbf{p}_{e} = {\lbrack\left. \mathbf{R} \middle| \mathbf{t} \right.\rbrack}$, relative to the vehicle frame.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Synthetic Sensor Simulation via 4DGS", "weight": 1.0} -->

This accounts for variations in vehicle type, diverse mounting locations (e.g., driver-side), and minor rotational perturbations ($\theta_{p},\theta_{y},\theta_{r}$) simulating imperfect camera installation. This rendering approach creates a vast dataset where each dashcam-style frame is perfectly time-synchronized and spatially aligned with the ground truth sensors.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Multi-modal Diffusion Model for Sensors", "weight": 1.0} -->

To enable sensor conversion from third-party data, we first develop a multi-sensor, multi-view generation model. This model simultaneously generates multi-view images $C = {\{\mathbf{c}_{i}\}}_{i = 1}^{N}$ and the LiDAR point cloud $L$. Each sensor modality has its own VAE and U-Net branch for diffusion. The key attributes of this model are multi-view (Section 3.2.1) and multi-sensor (Section 3.2.3) consistency.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Multi-view Image Generation", "weight": 1.0} -->

The image branch builds on a multi-view diffusion model that enables view consistency and camera pose control over the image generation. Given the camera parameters for each camera, this model learns a joint distribution of all images. To achieve multi-view consistency, the model replaces the $2$D attention modules in the original LDM to $3$D ($1$D cross views and $2$D in spatial) and computes attentions on all images.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Multi-view Image Generation", "weight": 1.0} -->

Furthermore, to precisely control the poses of generated images, this model accepts camera parameters as conditions. The camera parameters are represented via raymaps, which encode the ray origin and direction at each spatial location. All raymaps are normalized with regard to the first camera and concatenated channel-wise onto the image features.

<!-- chunk {"id": "body-0024", "role": "body", "section": "LiDAR Generation", "weight": 1.0} -->

LiDAR Representation. To effectively leverage the capabilities of 2D generative models, we utilize the LiDAR point cloud's native representation as range-view spin images---a tensor with shape $\lbrack H_{L},W_{L},D_{L}\rbrack$, where the $D_{L} = 4$ channels correspond to range (depth in meters), intensity (amount of light reflected), elongation (to what extent the waveform has been "flattened"), and validity (1 for a return, 0 otherwise). The image rows and columns map to the sensor's elevation and azimuth angles, respectively. Each (row, col, range) value can be projected to and from 3D Euclidean space $(x,y,z)$ given the vehicle trajectory and sensor calibration. For normalization, range values are clamped at 150 meters and linearly scaled to the $\lbrack 0,1\rbrack$ interval. Intensity and elongation are similarly normalized to fit within $\lbrack 0,1\rbrack$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "LiDAR Generation", "weight": 1.0} -->

LiDAR VAE. We introduce a VAE architecture for generating LiDAR spin images, jointly encoding depth, intensity, and elongation. The encoder and decoder are both convolutional, and we optimize the VAE via

<!-- chunk {"id": "body-0026", "role": "body", "section": "LiDAR Generation", "weight": 1.0} -->

Additional training details are provided in the supplemental.

<!-- chunk {"id": "body-0027", "role": "body", "section": "LiDAR Generation", "weight": 1.0} -->

LiDAR Diffusion. We first project the raw LiDAR range images into a latent space using the LiDAR VAE. A LiDAR U-Net branch then performs diffusion on this latent, operating similarly to a standard single-view image diffusion model. Each layer in the LiDAR U-Net is designed to output a feature with the same channel dimension as its corresponding layer in the multi-view image branch, enabling our cross-sensor feature fusion.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Cross-Sensor Attention Module", "weight": 1.0} -->

As shown in Figure 3, to simultaneously generate consistent images and LiDAR, we introduce a cross-sensor attention module within each U-Net block. We inject this module after convolutional layers to promote continuous information interchange. In detail, at a given block $i$, we flatten the image features $\mathbf{f}_{C}^{i}$ and LiDAR features $\mathbf{f}_{L}^{i}$ into token sequences $\mathbf{T}_{C}^{i} \in {\mathbb{R}}^{K_{C} \times d^{i}}$ and $\mathbf{T}_{L}^{i} \in {\mathbb{R}}^{K_{L} \times d^{i}}$, where $K_{C} = {N \times h_{C}^{i} \times w_{C}^{i}}$ and $K_{L} = {h_{L}^{i} \times w_{L}^{i}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Cross-Sensor Attention Module", "weight": 1.0} -->

The shared U-Net architecture for both modalities ensures their feature dimension $d^{i}$ is identical. These tokens are then concatenated into a unified sequence $\mathbf{T}_{U}^{i} \in {\mathbb{R}}^{{({K_{C} + K_{L}})} \times d^{i}}$, and the module computes self-attention over this sequence, allowing features from both sensors to interact directly.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Third-party Camera Condition", "weight": 1.0} -->

To directly leverage the visual context of the third-party data (e.g., dashcams), we introduce it as an additional, conditional ninth view, distinct from the $N = 8$ views targeted for generation. This conditional input is processed by the encoder to generate a latent representation, which is then concatenated with a corresponding raymap and a binary conditioning mask. This mask explicitly signals to the model that this view is a known, noise-free condition, distinguishing it from the $N$ noisy latents to be denoised. This augmented latent is then concatenated along the view dimension with the latents from the original eight views, and the resulting ${({N + 1})} \times H \times W \times C$ tensor is processed by the diffusion layers. This allows the features from the $8$ target views to interact with the conditional view through attention, effectively conditioning the synthesis of the surrounding scene on the dashcam's context. This $9^{th}$ view is excluded from the loss computation, ensuring its role as a conditioning input and that the network's capacity is focused on accurately generating the eight target views.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Auto-regressive Video Generation", "weight": 1.0} -->

To convert third-party videos to driving logs, we extend our model for auto-regressive generation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Auto-regressive Video Generation", "weight": 1.0} -->

When $t = 0$, sensor data is generated conditioning only on $\mathbf{x}_{0}$. Vanilla auto-regressive generation suffers from drifting, as models trained on ground-truth (GT) context must generate sequences conditioned on their own imperfect generations during inference. This causes errors to accumulate over long rollouts. To mitigate this, we introduce the DAgger algorithm, which augments the training context with the model's own generations. We gradually shrink this train-test mismatch by iteratively generating rollout videos and training a new model on the resulting context. To maintain robustness, we set a 0.2 probability of training on the original GT context.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments are designed to: quantify the fidelity of our generated images, video, and LiDAR point clouds against strong baselines; test model's generalizability on challenging, in-the-wild driving footage; and validate key architectural and training choices via ablation studies.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Evaluation metrics. We evaluate our results using Fréchet Inception Distance (FID) ($\downarrow$) for image realism and Fréchet Video Distance (FVD) ($\downarrow$) for video realism. For paired ground-truth comparisons, we use Peak Signal-to-Noise Ratio (PSNR) ($\uparrow$), Structural Similarity Index Measure (SSIM) ($\uparrow$), and the Learned Perceptual Image Patch Similarity (LPIPS) ($\downarrow$). These are supplemented by Human Evaluation ($\uparrow$), where raters choose the more realistic result in side-by-side comparisons.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Dataset. Since paired, third-party-to-AV sensor generation is a novel task, no public datasets with such synchronized data exist for evaluation. We therefore curated an evaluation dataset comprising two key components: (a) A dataset of 1,000 paired "Fixed-Camera-to-AV" log sequences (each 3 seconds long). The fixed-camera is a bumper camera positioned at the front-left bumper of the AV, and the 8-view surrounding cameras and the LiDAR are on top of the AV. (b) An "in-the-wild" dataset, including manually-collected real dashcam recordings, driving videos available on the internet, phone recordings and footage from other ADAS, for showing the in-the-wild generalizability.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Baselines. End-to-end conversion of a monocular third-party video to a full AV sensor suite (multi-view cameras and LiDAR) has not been fully explored in previous work. Thus, no direct baselines exist for our specific task. To benchmark Sensor2Sensor, we adapted several state-of-the-art methods for comparison. Reconstruction-based: We compare against state-of-the-art feedforward 3D scene reconstruction models VGGT and $\pi^{3}$ for the multi-camera generation task. Generative models: We adapt two SOTA generative models. X-Drive, an image-LiDAR co-generation model, was modified to condition on the dashcam input via attention. We also adapted CAT3D by enabling LiDAR generation using the same VAE as our method and conditioning it on the dashcam via channel-concatenation (CC) instead of view-concatenation (VC). We refer to this baseline as "Ours without (wo) VC", which also serves as a key ablation against our approach.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Multi-view Image Generation", "weight": 1.0} -->

We first evaluate the task of multi-view image generation. To quantitatively measure performance, we curate a "Fixed-Camera-to-AV" dataset. The input for this task comes from a real, front-left facing camera fixed on the AV near the bumper. This input camera is synchronized and calibrated with the target 8 surrounding views, to provide an accurate quantitative benchmark, as shown in Table 1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Multi-view Image Generation", "weight": 1.0} -->

On this "Fixed-Camera-to-AV" generation task, our method outperforms all baselines with an FID of 6.47 and LPIPS of 0.316, demonstrating the superior generative quality. Figure 4 shows that images generated by Sensor2Sensor are clear, geometrically plausible, and maintain consistent appearance of objects as they appear between camera views. In contrast, baseline methods often produce blurry results, distorted geometry, or noticeable artifacts.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Video Generation", "weight": 1.0} -->

Beyond static images, we evaluate the temporal consistency of our generated multi-view videos. We report quantitative results on our paired "Fixed-Camera-to-AV" dataset in Table 2. We use Fréchet Video Distance (FVD) ($\downarrow$) as the primary metric for overall video quality, supplemented by frame-wise PSNR ($\uparrow$), SSIM ($\uparrow$), and LPIPS ($\downarrow$). X-Drive is excluded from this comparison, as it is an image-only model and does not generate video. Furthermore, the reconstruction-based methods (VGGT and $\pi^{3}$) only generate complete results for the front view, as their other views suffer from large empty regions. For a better comparison, all metrics in this table are computed exclusively on the generated front-view videos.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Video Generation", "weight": 1.0} -->

Our model shows superior temporal stability, achieving the best FVD of 278.12. This significantly outperforms all baselines, such as Ours wo VC (293.73) and the feedforward reconstruction models $\pi^{3}$ and VGGT (2373.15). The feedforward models' high FVD scores are expected, as their reconstructive-only design cannot produce coherent novel views. This indicates that we not only generate realistic individual frames but also ensure they are coherent over time. The strong per-frame metrics (PSNR 22.42, SSIM 0.623, LPIPS 0.186) further support this, reinforcing the high fidelity seen in our static image evaluation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Video Generation", "weight": 1.0} -->

Moreover, as shown in Figure 5, while baselines exhibit noticeable flickering or inconsistent object appearance across frames, our model produces smooth and coherent video sequences for all views, which is critical for downstream consumption by perception or simulation systems.

<!-- chunk {"id": "body-0042", "role": "body", "section": "LiDAR Generation", "weight": 1.0} -->

A key contribution of Sensor2Sensor is its multi-modal capability to co-generate LiDAR point clouds along with multi-view videos. Qualitatively, Figure 6 provides a direct comparison against baseline methods. Our model shows a superior ability to reconstruct plausible 3D geometry for both nearby actors (like the truck) and the static environment. Our results are cleaner, with fewer noise artifacts and more accurate intensity rendering compared to X-Drive and Ours wo VC. Furthermore, Figure 7 highlights our model's strength in producing *jointly consistent* image and LiDAR outputs. The generated LiDAR points correctly align with their corresponding objects in the generated camera views, demonstrating that the model has learned a coherent underlying 3D representation of the scene.

<!-- chunk {"id": "body-0043", "role": "body", "section": "LiDAR Generation", "weight": 1.0} -->

Quantitatively, we report the Chamfer Distance for generated LiDAR in Table 3. Moreover, human evaluation of LiDAR generation in Table 4 also demonstrates a clear preference for our generated LiDAR over the baselines.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Generalization on in-the-wild driving data", "weight": 1.0} -->

The primary motivation for Sensor2Sensor is to further unlock "in-the-wild" data. We test this by applying our model, trained only on our paired dataset, to a diverse set of uncurated videos from internet, dashcams, and other third-party sources. These videos feature camera intrinsics, extrinsics, weather conditions and content unseen during training.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Generalization on in-the-wild driving data", "weight": 1.0} -->

As shown in Fig. 8, Sensor2Sensor demonstrates strong qualitative generalization. Despite facing unknown sensor characteristics and challenging, unseen environments (such as night-time near collisions, accidents, and active incidents), our model converts monocular inputs into coherent multi-sensor AV logs while preserving critical scene elements. This highlights its robustness for mining long-tail scenarios from vast, previously incompatible data sources.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Generalization on in-the-wild driving data", "weight": 1.0} -->

Quantitatively, a comprehensive human evaluation is shown in Table 4. 26 participants evaluated $40 \times 3$ generated image and LiDAR samples based on realism and alignment with the input image. After training and qualification on the protocol, they ranked each triplet as best, middle, or worst, from which we computed top-rank and pairwise preference rates. On dashcam data, Sensor2Sensor is top-preferred in 83.46% of image cases and 68.08% for LiDAR; on internet data, 84.62% and 58.46%, respectively. Pairwise comparisons show Sensor2Sensor is preferred over X-Drive in over 94% of image cases and 85% for LiDAR.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Model Architecture. Table 5 analyzes key architectural choices. First, we compare input conditioning via channel concatenation (CC) and view concatenation (VC). In the image-only setting, VC achieves better FID (6.20 vs. 6.63). Second, we study joint image-LiDAR training. Our full model achieves LPIPS 0.316, outperforming the CC variant (0.346) while remaining competitive with image-only VC (0.307). This confirms that our design enables joint LiDAR generation without obvious image quality degradation.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

DAgger Finetuning. Table 6 shows that DAgger finetuning improves video quality. With DAgger, FVD and FID improve to 278.12 and 21.54. This demonstrates improved temporal consistency and fidelity.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Downstream Tasks", "weight": 1.0} -->

We aim to build a high-fidelity simulation environment. To assess realism, we apply perception models trained on real data directly to our generated data without finetuning. Comparable performance on real and generated data in LiDAR detection (Fig. 9) and image segmentation (Fig. 10) indicates strong alignment with real-world distributions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

*Sensor2Sensor* is a novel generative paradigm that bridges the embodiment gap between consumer driving videos and the complex, multi-modal sensor suites required for AV validation. Leveraging a 4DGS-based data pairing pipeline and a conditional diffusion architecture, Sensor2Sensor converts monocular third-party videos into synchronized multi-view camera streams and LiDAR point clouds, achieving state-of-the-art performance in cross-embodiment sensor generation. Crucially, the model co-generates consistent LiDAR and demonstrates strong generalization to real-world footage. By unlocking large-scale driving videos for AV development, our approach provides a scalable solution to data scarcity for safety-critical validation and deployment of safety-critical autonomous systems. Future work will explore improved scalability, generalization to more sensors, and a more scalable evaluation protocol.
