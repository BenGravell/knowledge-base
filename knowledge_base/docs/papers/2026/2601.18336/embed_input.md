<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PPISP: Physically-Plausible Compensation and Control of Photometric Variations in Radiance Field Reconstruction

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Multi-view 3D reconstruction methods remain highly sensitive to photometric inconsistencies arising from camera optical characteristics and variations in image signal processing (ISP). Existing mitigation strategies such as per-frame latent variables or affine color corrections lack physical grounding and generalize poorly to novel views. We propose the Physically-Plausible ISP (PPISP) correction module, which disentangles camera-intrinsic and capture-dependent effects through physically based and interpretable transformations. A dedicated PPISP controller, trained on the input views, predicts ISP parameters for novel viewpoints, analogous to auto exposure and auto white balance in real cameras. This design enables realistic and fair evaluation on novel views without access to ground-truth images. PPISP achieves state-of-the-art performance on standard benchmarks, while providing intuitive control and supporting the integration of metadata when available.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

State-of-the-art multi-view 3D reconstruction methods have significantly advanced the fidelity of novel view synthesis (NVS), transforming it into a technology with real-world applications in physical AI simulation, virtual production, and content creation. Despite these advances, the quality of reconstruction and view synthesis remains highly sensitive to the quality of the input data---both to the distribution of camera poses and to multi-view appearance inconsistencies. The latter often arise from variations in camera optical characteristics and image signal processing (ISP) settings over time. These variations result in differences in color tone, intensity, and contrast that violate the photometric consistency assumptions underlying 3D reconstruction.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common strategy to mitigate these appearance variations is to introduce additional, optimizable per-frame or per-camera parameters designed to capture photometric residuals while preserving a consistent multi-view scene representation. Recent state-of-the-art approaches include low-dimensional generative latent optimization (GLO) vectors, learnable affine transformations, and bilateral grids (BilaRF). However, these mitigation strategies face several trade-offs and challenges: Representation capacity: higher-capacity and less-constrained modules tend to improve PSNR on the training views but risk modeling more than just photometric variations, often degrading novel view synthesis quality.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Interpretability and controllability: the learned parameters are typically non-interpretable (*e.g*., in GLO or BilaRF), making it difficult to intuitively adjust properties such as brightness or white balance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Parameters for novel views: since the parameters are optimized independently per frame, it is unclear how to assign appropriate values when synthesizing novel views.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The latter is especially challenging due to the tendency of these modules to conflate camera sensor intrinsic properties (*e.g*., vignetting and camera response function) with capture-dependent settings that vary per frame or are adjusted by the ISP (*e.g*., exposure time and white balance). As a consequence, evaluation protocols commonly assume access to the ground-truth novel view image and estimate a corrective mapping, such as an affine transform, quadratic polynomial, or direct parameter optimization, to minimize the difference between the synthesized and the ground-truth (GT) image before computing the evaluation metrics. But such protocols are inherently flawed as they: (i) deviate from real-world scenarios where GT novel views are unavailable, and (ii) conceal differences between methods by compensating for them through the corrective mapping.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, we propose a Physically-Plausible ISP (PPISP) correction module, grounded in the physical principles of camera image formation. Specifically, we disentangle sensor-intrinsic properties and capture-dependent settings through dedicated per-sensor and per-frame modules, respectively, and constrain their effects according to the image formation process (*e.g*., the exposure module can only modify the overall image brightness). Our model acts as a post-processing step applied to the raw images rendered from the 3D representation, and enables direct controllability through manual change of the parameters. Moreover, we introduce a PPISP controller that predicts the parameters of the per-frame modules for novel views, analogous to the auto exposure and auto white balance mechanisms in conventional cameras.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Compensation during reconstruction", "weight": 1.0} -->

To mitigate these inconsistencies, NeRF-W and GS-W introduce GLO that are optimized jointly with the scene representation. These per-image latent embeddings enable smooth interpolation across observed appearances, but risk entangling scene geometry with reflectance when optimized end-to-end. Block-NeRF extends this idea to city-scale scenes and additionally conditions on camera exposure metadata. To impose stronger constraints and better align with the image formation process, subsequent works model photometric transformations explicitly. URF represents per-image variations using affine color transformations, while BilaRF extends this idea to per-pixel affine mappings parameterized via bilateral grids. Several works instead model specific physical components of the image formation pipeline: Xian *et al*. learn lens distortion and vignetting jointly with the radiance field, and HDR-NeRF and HDR-GS recover HDR radiance by learning a camera response function (CRF) from multi-exposure captures. Closest to our approach, ADOP's post-processing models exposure, white balance, CRF, and vignetting effects as explicit calibration parameters.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Compensation during reconstruction", "weight": 1.0} -->

However, our formulation better disentangles exposure offset and white balance, while using a more compact CRF model. Recently, Huang *et al*. and Niemeyer *et al*. deviate from a frame-based correction and instead learn a 3D exposure neural field, predicting the optimal exposure values for each 3D point.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Harmonizing appearance during preprocessing", "weight": 1.0} -->

An alternative strategy is to decouple the compensation from reconstruction and harmonize the input images as a preprocessing step. Shin *et al*. employ a transformer network to predict bilateral grids that harmonize each image to a chosen reference view. Alzayer *et al*. instead use a diffusion model to relight images directly, but due to the lack of paired real data, they train their generative model only on synthetic data. To overcome this limitation, Trevithick *et al*. use a generative video model to simulate capture-time inconsistencies on consistent multi-view images, creating pseudo-paired data to train a harmonization network.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Novel view synthesis with target appearance", "weight": 1.0} -->

The above methods reconstruct the scene in a canonical or reference appearance, but it remains unclear how to set the parameters of their appearance modules to render an image in a desired target appearance. This target appearance could be user-defined or selected to match the appearance that a camera with auto exposure and white balance would produce. This ambiguity poses practical challenges for novel view synthesis and complicates fair evaluation under photometric variation. Prior work typically applies post-render normalization that assumes access to the target image during evaluation: NeRF-W fine-tunes latent embeddings on one half of each image and evaluates on the other, RawNeRF performs channel-wise affine alignment, Mip-NeRF 360 uses a quadratic color basis alignment, and ADOP re-optimizes per-frame parameters.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Novel view synthesis with target appearance", "weight": 1.0} -->

Such evaluation protocols, however, (i) mask differences between methods and (ii) are infeasible in real-world applications where access to the target image cannot be assumed. In line with the principle that novel views should be rendered solely from reconstructed data without access to target pixels, we introduce a PPISP controller that takes the *raw* radiance image rendered from the 3D representation as input and outputs the PPISP parameters. We optimize this network on the training views and then directly apply it to the novel views during inference. Somewhat related to our PPISP controller, train a network to predict exposure control for improved feature matching and object detection, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Radiance Field Reconstruction", "weight": 1.0} -->

aims to optimize a parametric representation of a scene's volumetric density $\sigma\in\mathbb{R}$ and emitted radiance $\mathbf{c}\in\mathbb{R}^{3}$. The radiance $\mathbf{L}(\mathbf{r})$ of a camera ray $\mathbf{r}(x)=\mathbf{o}+x\,\mathbf{d}$ with origin $\mathbf{o}\in\mathbb{R}^{3}$ and direction $\mathbf{d}\in\mathbb{R}^{3}$ is rendered from this representation as where $T(x)=\exp(-\int_{near}^{x}\sigma(\mathbf{r}(y))\,dy)$ denotes the transmittance along the ray. The optimization is supervised using ground truth images $\mathbf{I}$ captured by one or more cameras with known intrinsics and extrinsics. This standard formulation alone does not account for camera-specific imaging effects.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Camera Image Formation", "weight": 1.0} -->

is the process through which the radiance $\mathbf{L}$ is converted to the final image: Here, the function $\mathcal{F}(\cdot)$ models the complete image acquisition process, including lens distortions (e.g., vignetting, chromatic aberrations), exposure settings (aperture, shutter time), sensor characteristics (spectral response, noise, gain), and ISP operations according to some parameters $\mathbf{\Theta}$. While some components of this process remain constant across acquisition time, others may vary due to manual adjustments or automatic adaptation by the sensor controller.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

We compensate for photometric inconsistencies across input images by jointly optimizing the scene representation together with a differentiable ISP pipeline that approximates the camera image formation function $\mathcal{F}(\cdot)$ defined in Eq. 2. During optimization, this pipeline models both camera-specific and time-varying effects. During inference (*i.e*., when rendering novel views), the learned controller (Sec. 4.5) predicts the time-varying parameters directly from the radiance $\mathbf{L}$ rendered from the scene representation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Our ISP pipeline consists of four sequential modules (see Fig. 2): Exposure offset accounts for aperture, shutter time and gain variations, Vignetting models optical attenuation across the sensor, Color correction models sensor spectral response and white balance adjustments, Camera response function (CRF) applies a non-linear transformation from sensor irradiance to image colors.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

Following Debevec and Malik, the first three modules operate linearly on the scene radiance, while the CRF provides the final non-linear mapping. Fig. 2 puts the pipeline in the context of the radiance reconstruction and illustrates the individual parts and their effects.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Exposure Offset", "weight": 1.0} -->

We model exposure as a global, per-frame scale on the radiance using a base-2 exponent, mimicking photographic exposure values: where $\Delta t\in\mathbb{R}$ is an optimizable exposure offset. This offset represents the variation of the radiance intensity reaching the sensor and is specific to the capture. Thus, we estimate one such offset for each frame.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Vignetting", "weight": 1.0} -->

Following Goldman, we model per-channel radial intensity falloff using a polynomial in the squared radius around an optimizable optical center: where $\boldsymbol{\mu}\in\mathbb{R}^{2}$ is the optical center, $\boldsymbol{\alpha}\in\mathbb{R}^{3}$ are polynomial coefficients, and $r=\lVert\mathbf{u}-\boldsymbol{\mu}\rVert_{2}$ is the distance of the pixel location $\mathbf{u}$ to the optical center. The attenuation factor $v(r)$ is defined as: At the start of optimization, we initialize $\boldsymbol{\alpha}=0$ and let $\boldsymbol{\mu}$ be the image center.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Vignetting", "weight": 1.0} -->

Since our vignetting model is chromatic, a falloff polynomial is defined for each color channel by distinct parameter values.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Color Correction", "weight": 1.0} -->

To model effects such as white balance, which may vary per-frame, and gamut differences between multiple cameras, we apply color correction. To disentangle it from exposure correction, we apply a $3\times 3$ homography $\mathbf{H}$ on RG chromaticities and intensity --- following Finlayson *et al*. --- and ensure normalization of the intensity after the transform. Inspired by DeTone *et al*., we parameterize the color correction as four chromaticity offsets $\Delta\mathbf{c}_{k}$, construct $\mathbf{H}$ from them, and apply the color correction: Let $\mathbf{C}\in\mathbb{R}^{3\times 3}$ denote the RGB$\rightarrow$RGI conversion matrix and $\mathbf{C}^{-1}$ its inverse. The intensity normalization can then be defined as: Here, $\varepsilon$ is a small constant for numerical stability. This normalization decouples exposure from chromatic correction.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Color Correction", "weight": 1.0} -->

The color transform follows compactly as To construct $\mathbf{H}$, we define four 2D source--target chromaticity pairs.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Color Correction", "weight": 1.0} -->

Then, $\mathbf{k}\in\mathbb{R}^{3}$ can be obtained via a cross-product of any pair of linearly independent rows $i$ and $j$, where $\mathbf{m}_{1},\mathbf{m}_{2},\mathbf{m}_{3}$ are the rows of $\mathbf{M}$. Finally, we form and normalize A precise derivation and further details are provided in the Supplementary.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Camera Response Function", "weight": 1.0} -->

Inspired by Grossberg and Nayar, we use a piecewise power curve to model non-linear chromatic transformations. The CRF operator $\mathcal{G}$ has four learned parameters: For each channel, the basic S-shaped curve is given: setting $a$ and $b$ to match the slope at the inflection point to ensure $C^{1}$ continuity: Finally, the CRF image operator $\mathcal{G}$ is a composition of this S-curve with a gamma correction: Figure 4: Qualitative comparison of novel view synthesis. Row labels indicate datasets and sequences (in italics). Column labels indicate methods. Heat maps show perceptual CIEDE2000 error (colormap range: 0–20 ΔE00). Our method achieves more consistent photometry and better color reproduction across various datasets and sequences. HDR-NeRF: When image metadata is available, our method can incorporate it to produce a more accurate novel view.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Per-Frame ISP Parameter Controller", "weight": 1.0} -->

The exposure offsets and color correction transforms introduced above are valid only for a specific capture, *i.e*., a single camera pose, and therefore cannot be directly reused for novel view rendering. To address this limitation, we introduce a controller that predicts these parameters from the rendered scene radiance, analogous to how auto exposure and auto white balance work in conventional cameras: Here, $\mathcal{T}(\cdot)$ is the camera-specific controller parametric function, which we design as a coarse feature extractor ($1\times 1$ convolutions with pooling to a 5×5 grid), followed by a parameter regressor (an MLP with separate output heads). The detailed architecture of the controller is provided in the Supplementary.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Per-Frame ISP Parameter Controller", "weight": 1.0} -->

We optimize the controller in a separate stage once the optimization of the scene representation is complete. At that stage, the underlying reconstruction and all per-camera ISP parameters are frozen, the controller-predicted parameters are applied through the ISP, and the controller itself is trained using the same photometric loss as in the initial phase. A qualitative example of the controller's effects is given in Fig. 3. Optional scalar controls (*e.g*., exposure compensation or EXIF-derived biases) can be concatenated to the regressor input.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Regularization", "weight": 1.0} -->

Joint optimization of the modules can introduce brightness and color ambiguities between scene radiance and the ISP parameters. To mitigate this, we apply regularization on the previously defined parameters, using the Huber loss $\mathcal{L}_{\delta}$, where $\delta$ denotes the threshold. We use superscripts to indicate parameters belonging to specific camera sensors^(s)^ and frames^(f)^.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Color", "weight": 1.0} -->

We penalize the frame-mean of the target chromaticity offsets (element-wise in $\mathbb{R}^{2}$): Because chromatic corrections, as done in vignetting and CRF modules, may also introduce localized color shifts, we shrink parameter variance across channels. Let $\boldsymbol{\theta}_{m,k}$ be the parameters of channel $k$ for module $m\in\{\text{vig},\text{crf}\}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Physically-plausible vignetting", "weight": 1.0} -->

For each polynomial, we penalize the center and softly enforce $\alpha_{j}\leq 0$: Here $[x]_{+}=\max(x,0)$ is the elementwise rectifier.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

We begin by evaluating the proposed PPISP correction module and controller on standard novel-view synthesis benchmarks, assessing both reconstruction fidelity and novel-view quality (Sec. 5.1). We then demonstrate how our formulation allows us to incorporate image metadata, such as relative exposure, when available (Sec. 5.2). We measure the runtime performance impact (Sec. 5.3). Finally, we analyze the relationship between model capacity, overfitting behavior, and novel-view synthesis performance (Sec. 5.4).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Setting", "weight": 1.0} -->

As a reconstruction-agnostic post-processing step, the PPISP module readily applies to different radiance field methods. We integrate it in 3DGUT, GSplat (an accelerated implementation of 3DGS ), and Zip-NeRF.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Setting", "weight": 1.0} -->

Comparison baselines are the appearance correction approaches described in GLO, BilaRF, and ADOP. For experiments, we rely on their reference hyperparameters and reference implementations available in the respective framework. To increase the stability of ADOP's method, we increase the strength of their CRF regularization about $100\times$ compared to the reference value.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Setting", "weight": 1.0} -->

We jointly train the reconstruction method and the post-processing operator for 30k iterations. For the PPISP controller, we freeze both and train the controller for an additional 5k iterations. For 3DGS and 3DGUT, we enable MCMC sampling.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Metrics", "weight": 1.0} -->

We evaluate the perceptual quality of the rendered views using peak signal-to-noise ratio (PSNR), structural similarity (SSIM), and learned perceptual image patch similarity (LPIPS) metrics.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Metrics", "weight": 1.0} -->

As the PSNR metric is highly sensitive to global brightness shifts, and our baselines do not support appearance compensation for novel views, we additionally report the PSNR computed after affine color alignment, following RawNeRF. We denote this as "PSNR-CC", but emphasize that such comparison masks the differences between the methods and assumes access to the GT target views, which are not available in practice.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Datasets", "weight": 1.0} -->

To show the robustness and generality of our method, we conducted experiments on a variety of publicly available datasets: Mip-NeRF 360, Tanks and Temples, BilaRF, HDR-NeRF, and nine static sequences of the Waymo Open Dataset.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Datasets", "weight": 1.0} -->

To further highlight the differences of the methods in challenging real-world scenarios, we captured a new *PPISP dataset* consisting of four scenes. Each of them was captured with three different cameras (Apple iPhone 13 Pro, Nikon Z7, and OM System OM-1 Mark II) to ensure variations. More details about the scenes, resolution, and training-test splits are available in the Supplementary.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Datasets", "weight": 1.0} -->

PPISP - no color correction Table 2: Component ablation of PPISP on the Tanks and Temples dataset for novel views (NV). Each row shows performance when removing the specified component.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Novel View Synthesis Benchmark", "weight": 1.0} -->

Quantitative results on the standard benchmark scenes are presented in Tab. 1, and qualitative comparisons are shown in Fig. 4. Our method achieves the best PSNR, SSIM, and LPIPS in the large majority of settings across datasets and base methods, and on most datasets even surpasses the BilaRF baseline when that baseline is given privileged access to the target image, i.e., when comparing our PSNR against the baseline's PSNR-CC. These gains, established primarily on 3DGUT, extend to the 3DGS and Zip-NeRF integrations.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Novel View Synthesis Benchmark", "weight": 1.0} -->

The comparison between PSNR and PSNR-CC further highlights the effectiveness of our controller in reproducing the camera's auto-exposure and white-balance behavior. On most datasets, the controller achieves metrics close to those obtained after affine color alignment, indicating that it faithfully predicts the necessary per-frame appearance corrections. The only notable discrepancy appears on the BilaRF dataset, likely due to the fact that this dataset contains some manual settings overrides (indicated by the metadata), which are not captured by our controller.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Novel View Synthesis Benchmark", "weight": 1.0} -->

Both PPISP and ADOP employ camera-specific components (vignetting and CRF), which generalize to novel views, leading to improved metrics over BilaRF. Our base image formation model (*w/o ctrl.*) outperforms both of these baselines thanks to better separation of concerns of the individual modules and stronger constraints (see also Sec. 5.4; a detailed comparison to ADOP is provided in the Supplementary). Our full pipeline consistently improves upon the base model by providing plausible per-frame parameter estimates via the controller.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablation", "weight": 1.0} -->

We ablate the relative contribution of each module in our pipeline through an ablation study on the Tanks and Temples dataset. Tab. 2 presents the novel view PSNR when individual components are removed from the full pipeline. The results demonstrate that all modules contribute to the full pipeline's performance, with exposure and vignetting corrections being most critical.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Using Image Metadata", "weight": 1.0} -->

Because our formulation closely mirrors the camera image formation process, it can naturally incorporate image metadata, such as the relative exposure of each frame, whenever available. We demonstrate this capability on the HDR-NeRF and PPISP datasets, both of which use exposure bracketing (*i.e*., captures with positive and negative exposure compensation) and provide the corresponding metadata. We concatenate this metadata to the input of the controller MLP regressor, allowing it to map rendered radiance plus metadata to effective ISP parameters.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Using Image Metadata", "weight": 1.0} -->

Since the ADOP-style post-processing also models per-frame exposure offsets explicitly, we initialize them from known exposure values as proposed in ADOP.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Using Image Metadata", "weight": 1.0} -->

Quantitative results in Tab. 3 show that supplying calibrated exposure offsets substantially improves novel-view accuracy. Moreover, providing this metadata to the controller yields further gains compared to ADOP, demonstrating our method's ability to leverage metadata for more accurate novel view appearance prediction.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Runtime Performance", "weight": 1.0} -->

Tab. 4 presents the computational performance of the post-processing methods we evaluated compared to the scene rendering. PPISP (*w/o ctrl.*) and ADOP have a similar and very small computational footprint ($3\%$ of the rendering). The controller is adding a substantial overhead due to the required processing of the input image, but our pipeline remains significantly faster ($26\%$ vs $36\%$) compared to BilaRF on an NVIDIA RTX 5090 GPU.

<!-- chunk {"id": "body-0048", "role": "body", "section": "ISP Capacity vs. Training and Novel Views", "weight": 1.0} -->

Next, we investigate how the capacity of the correction module affects the overfitting (difference between the PSNR on training and novel views) and generalization to novel views. The bilateral grids used in BilaRF provide a highly expressive mechanism for modeling image operations extending beyond simple compensation of photometric inconsistencies. In BilaRF, this operation is learned independently for each frame, providing a high modeling capacity. In contrast, our PPISP module intentionally has limited capacity to prevent overfitting, but in turn cannot model complex image operations that mix spatial and intensity effects such as localized tone-mapping.

<!-- chunk {"id": "body-0049", "role": "body", "section": "ISP Capacity vs. Training and Novel Views", "weight": 1.0} -->

In Tab. 5, we therefore study hybrids of the two approaches. Adding more capacity to per-frame BilaRF with additional per-camera bilateral grids (+PC) does not meaningfully change PSNR on the training views as the model already has sufficient capacity. However, it does slightly improve the generalization as per-camera corrections carry over to novel viewpoints. Increasing our method's capacity by adding per-frame bilateral grids boosts PSNR on the training views, but noticeably degrades performance on novel views due to overfitting. Overall, our formulation achieves a favorable balance between capacity and generalization to unseen views.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion and Limitations", "weight": 1.5} -->

Accurately reconstructing the radiance field of a scene requires accounting for variations in the camera imaging pipeline across the input frames. Ignoring these variations introduces strong biases, leading to spurious color shifts and geometric artifacts. In this work, we introduced a differentiable post-processing pipeline whose design permits simulating the imaging process while remaining highly constrained to prevent reconstruction bias. We further proposed a controller that improves generalization to novel views by predicting per-frame imaging parameters directly from the rendered radiance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Limitations", "weight": 1.5} -->

Our method shows superior generalization to novel views (Tab. 1), but it sometimes struggles to match the baselines on the training views (Tab. 5). This can be partially attributed to overfitting, but our formulation also ignores some important optical effects such as localized tone-mapping commonly found in modern phone cameras; lens flares, which are prominent in night scenes; and similar spatially-varying effects. While the proposed controller enables generalization to novel views, its ability to infer exposure and color-correction parameters from rendered radiance depends on the existence of meaningful correlations in the data. When such correlations are absent, for example when the physical camera controls (*e.g*., shutter, aperture, ISO) are manually overridden, the controller must rely on extra metadata to predict correct values.
