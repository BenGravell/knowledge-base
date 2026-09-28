<!-- arxiv-full-text:v1 {"arxiv_id": "2601.18336", "source": "arxiv-html"} -->

## Introduction

State-of-the-art multi-view 3D reconstruction methods have significantly advanced the fidelity of novel view synthesis (NVS), transforming it into a technology with real-world applications in physical AI simulation, virtual production, and content creation. Despite these advances, the quality of reconstruction and view synthesis remains highly sensitive to the quality of the input data---both to the distribution of camera poses and to multi-view appearance inconsistencies. The latter often arise from variations in camera optical characteristics and image signal processing (ISP) settings over time. These variations result in differences in color tone, intensity, and contrast that violate the photometric consistency assumptions underlying 3D reconstruction.

A common strategy to mitigate these appearance variations is to introduce additional, optimizable per-frame or per-camera parameters designed to capture photometric residuals while preserving a consistent multi-view scene representation. Recent state-of-the-art approaches include low-dimensional generative latent optimization (GLO) vectors, learnable affine transformations, and bilateral grids (BilaRF). However, these mitigation strategies face several trade-offs and challenges: Representation capacity: higher-capacity and less-constrained modules tend to improve PSNR on the training views but risk modeling more than just photometric variations, often degrading novel view synthesis quality.

Interpretability and controllability: the learned parameters are typically non-interpretable (*e.g*., in GLO or BilaRF), making it difficult to intuitively adjust properties such as brightness or white balance.

Parameters for novel views: since the parameters are optimized independently per frame, it is unclear how to assign appropriate values when synthesizing novel views.

The latter is especially challenging due to the tendency of these modules to conflate camera sensor intrinsic properties (*e.g*., vignetting and camera response function) with capture-dependent settings that vary per frame or are adjusted by the ISP (*e.g*., exposure time and white balance). As a consequence, evaluation protocols commonly assume access to the ground-truth novel view image and estimate a corrective mapping, such as an affine transform, quadratic polynomial, or direct parameter optimization, to minimize the difference between the synthesized and the ground-truth (GT) image before computing the evaluation metrics. But such protocols are inherently flawed as they: (i) deviate from real-world scenarios where GT novel views are unavailable, and (ii) conceal differences between methods by compensating for them through the corrective mapping.

To address these challenges, we propose a Physically-Plausible ISP (PPISP) correction module, grounded in the physical principles of camera image formation. Specifically, we disentangle sensor-intrinsic properties and capture-dependent settings through dedicated per-sensor and per-frame modules, respectively, and constrain their effects according to the image formation process (*e.g*., the exposure module can only modify the overall image brightness). Our model acts as a post-processing step applied to the raw images rendered from the 3D representation, and enables direct controllability through manual change of the parameters. Moreover, we introduce a PPISP controller that predicts the parameters of the per-frame modules for novel views, analogous to the auto exposure and auto white balance mechanisms in conventional cameras.

Figure 2: Our proposed pipeline applies a sequence of physically-grounded modules to the input reconstructed radiance (exposure offset, chromatic vignetting, linear color correction, and non-linear camera response function). Top: all modules except the controller are jointly optimized during the first training phase. Bottom: the controller is then trained to predict per-frame exposure and color correction for novel views while other modules are frozen. The image sequence illustrates the progressive effect of each module.

## Related Work

Appearance inconsistencies across multi-view input images significantly degrade the quality of radiance field reconstructions and subsequent novel-view synthesis. Such variations are common in unconstrained image collections, for instance when using internet photo collections or captures under uncontrolled lighting conditions.

### Compensation during reconstruction

To mitigate these inconsistencies, NeRF-W and GS-W introduce GLO that are optimized jointly with the scene representation. These per-image latent embeddings enable smooth interpolation across observed appearances, but risk entangling scene geometry with reflectance when optimized end-to-end. Block-NeRF extends this idea to city-scale scenes and additionally conditions on camera exposure metadata. To impose stronger constraints and better align with the image formation process, subsequent works model photometric transformations explicitly. URF represents per-image variations using affine color transformations, while BilaRF extends this idea to per-pixel affine mappings parameterized via bilateral grids. Several works instead model specific physical components of the image formation pipeline: Xian *et al*. learn lens distortion and vignetting jointly with the radiance field, and HDR-NeRF and HDR-GS recover HDR radiance by learning a camera response function (CRF) from multi-exposure captures. Closest to our approach, ADOP's post-processing models exposure, white balance, CRF, and vignetting effects as explicit calibration parameters. However, our formulation better disentangles exposure offset and white balance, while using a more compact CRF model. Recently, Huang *et al*. and Niemeyer *et al*. deviate from a frame-based correction and instead learn a 3D exposure neural field, predicting the optimal exposure values for each 3D point.

### Harmonizing appearance during preprocessing

An alternative strategy is to decouple the compensation from reconstruction and harmonize the input images as a preprocessing step. Shin *et al*. employ a transformer network to predict bilateral grids that harmonize each image to a chosen reference view. Alzayer *et al*. instead use a diffusion model to relight images directly, but due to the lack of paired real data, they train their generative model only on synthetic data. To overcome this limitation, Trevithick *et al*. use a generative video model to simulate capture-time inconsistencies on consistent multi-view images, creating pseudo-paired data to train a harmonization network.

### Novel view synthesis with target appearance

The above methods reconstruct the scene in a canonical or reference appearance, but it remains unclear how to set the parameters of their appearance modules to render an image in a desired target appearance. This target appearance could be user-defined or selected to match the appearance that a camera with auto exposure and white balance would produce. This ambiguity poses practical challenges for novel view synthesis and complicates fair evaluation under photometric variation. Prior work typically applies post-render normalization that assumes access to the target image during evaluation: NeRF-W fine-tunes latent embeddings on one half of each image and evaluates on the other, RawNeRF performs channel-wise affine alignment, Mip-NeRF 360 uses a quadratic color basis alignment, and ADOP re-optimizes per-frame parameters.

Such evaluation protocols, however, (i) mask differences between methods and (ii) are infeasible in real-world applications where access to the target image cannot be assumed. In line with the principle that novel views should be rendered solely from reconstructed data without access to target pixels, we introduce a PPISP controller that takes the *raw* radiance image rendered from the 3D representation as input and outputs the PPISP parameters. We optimize this network on the training views and then directly apply it to the novel views during inference. Somewhat related to our PPISP controller, train a network to predict exposure control for improved feature matching and object detection, respectively.

## Preliminaries

### Radiance Field Reconstruction

aims to optimize a parametric representation of a scene's volumetric density $\sigma\in\mathbb{R}$ and emitted radiance $\mathbf{c}\in\mathbb{R}^{3}$. The radiance $\mathbf{L}(\mathbf{r})$ of a camera ray $\mathbf{r}(x)=\mathbf{o}+x\,\mathbf{d}$ with origin $\mathbf{o}\in\mathbb{R}^{3}$ and direction $\mathbf{d}\in\mathbb{R}^{3}$ is rendered from this representation as where $T(x)=\exp(-\int_{near}^{x}\sigma(\mathbf{r}(y))\,dy)$ denotes the transmittance along the ray. The optimization is supervised using ground truth images $\mathbf{I}$ captured by one or more cameras with known intrinsics and extrinsics. This standard formulation alone does not account for camera-specific imaging effects.

### Camera Image Formation

is the process through which the radiance $\mathbf{L}$ is converted to the final image: Here, the function $\mathcal{F}(\cdot)$ models the complete image acquisition process, including lens distortions (e.g., vignetting, chromatic aberrations), exposure settings (aperture, shutter time), sensor characteristics (spectral response, noise, gain), and ISP operations according to some parameters $\mathbf{\Theta}$. While some components of this process remain constant across acquisition time, others may vary due to manual adjustments or automatic adaptation by the sensor controller.

### Notation

Let $\mathbf{I}\in\mathbb{R}^{H\times W\times 3}$ be an RGB image. The color at spatial location $\mathbf{u}=(i,j)$ is $\mathbf{x}=\mathbf{I}_{i,j}\in\mathbb{R}^{3}$ and its $k$-th channel value is $x=\mathbf{x}_{k}=\mathbf{I}_{i,j,k}\in\mathbb{R}$, $k\in\{R,G,B\}$. Operations defined on channel values or colors are understood element-wise when applied to an image.

## Method

We compensate for photometric inconsistencies across input images by jointly optimizing the scene representation together with a differentiable ISP pipeline that approximates the camera image formation function $\mathcal{F}(\cdot)$ defined in Eq. 2. During optimization, this pipeline models both camera-specific and time-varying effects. During inference (*i.e*., when rendering novel views), the learned controller (Sec. 4.5) predicts the time-varying parameters directly from the radiance $\mathbf{L}$ rendered from the scene representation.

Our ISP pipeline consists of four sequential modules (see Fig. 2): Exposure offset accounts for aperture, shutter time and gain variations, Vignetting models optical attenuation across the sensor, Color correction models sensor spectral response and white balance adjustments, Camera response function (CRF) applies a non-linear transformation from sensor irradiance to image colors.

Following Debevec and Malik, the first three modules operate linearly on the scene radiance, while the CRF provides the final non-linear mapping. Fig. 2 puts the pipeline in the context of the radiance reconstruction and illustrates the individual parts and their effects.

### Exposure Offset

We model exposure as a global, per-frame scale on the radiance using a base-2 exponent, mimicking photographic exposure values: where $\Delta t\in\mathbb{R}$ is an optimizable exposure offset. This offset represents the variation of the radiance intensity reaching the sensor and is specific to the capture. Thus, we estimate one such offset for each frame.

### Vignetting

Following Goldman, we model per-channel radial intensity falloff using a polynomial in the squared radius around an optimizable optical center: where $\boldsymbol{\mu}\in\mathbb{R}^{2}$ is the optical center, $\boldsymbol{\alpha}\in\mathbb{R}^{3}$ are polynomial coefficients, and $r=\lVert\mathbf{u}-\boldsymbol{\mu}\rVert_{2}$ is the distance of the pixel location $\mathbf{u}$ to the optical center. The attenuation factor $v(r)$ is defined as: At the start of optimization, we initialize $\boldsymbol{\alpha}=0$ and let $\boldsymbol{\mu}$ be the image center.

Since our vignetting model is chromatic, a falloff polynomial is defined for each color channel by distinct parameter values.

Figure 3: Dynamics of the controller module. The predicted exposure offset (inset) depends on the image content of the rendered radiance. Right side: Plot of exposure offsets as predicted for each frame of the caterpillar sequence, with the three displayed frames highlighted.

### Color Correction

To model effects such as white balance, which may vary per-frame, and gamut differences between multiple cameras, we apply color correction. To disentangle it from exposure correction, we apply a $3\times 3$ homography $\mathbf{H}$ on RG chromaticities and intensity --- following Finlayson *et al*. --- and ensure normalization of the intensity after the transform. Inspired by DeTone *et al*., we parameterize the color correction as four chromaticity offsets $\Delta\mathbf{c}_{k}$, construct $\mathbf{H}$ from them, and apply the color correction: Let $\mathbf{C}\in\mathbb{R}^{3\times 3}$ denote the RGB$\rightarrow$RGI conversion matrix and $\mathbf{C}^{-1}$ its inverse. The intensity normalization can then be defined as: Here, $\varepsilon$ is a small constant for numerical stability. This normalization decouples exposure from chromatic correction. The color transform follows compactly as To construct $\mathbf{H}$, we define four 2D source--target chromaticity pairs. Specifically, we fix the source RG chromaticities $\mathbf{c}_{s,\cdot}$ to the three primaries and a neutral white: | | $\displaystyle\mathbf{c}_{s,R}$ | $\displaystyle=^{T}\ \quad\mathbf{c}_{s,G}=^{T}\ $ | | \(9\) | | | $\displaystyle\mathbf{c}_{s,B}$ | $\displaystyle=^{T}\ \quad\mathbf{c}_{s,W}=\left(\tfrac{1}{3},\tfrac{1}{3}\right)^{T}\ $ | | | and define the targets $\mathbf{c}_{t,\cdot}$ as offsets from these sources $\mathbf{c}_{t,k}\;=\;\mathbf{c}_{s,k}+\Delta\mathbf{c}_{k}$ for $k\in\{R,G,B,W\}$. By lifting the 2D chromaticities to homogeneous coordinates and stacking them as $\mathbf{S}\;\doteq\;[\,\tilde{\mathbf{c}}_{s,R}\;\tilde{\mathbf{c}}_{s,G}\;\tilde{\mathbf{c}}_{s,B}\,]$ and $\mathbf{T}\;\doteq\;[\,\tilde{\mathbf{c}}_{t,R}\;\tilde{\mathbf{c}}_{t,G}\;\tilde{\mathbf{c}}_{t,B}\,]$, we can define where $[\cdot]_{\times}$ is the skew-symmetric cross-product matrix. Then, $\mathbf{k}\in\mathbb{R}^{3}$ can be obtained via a cross-product of any pair of linearly independent rows $i$ and $j$, where $\mathbf{m}_{1},\mathbf{m}_{2},\mathbf{m}_{3}$ are the rows of $\mathbf{M}$. Finally, we form and normalize A precise derivation and further details are provided in the Supplementary.

### Camera Response Function

Inspired by Grossberg and Nayar, we use a piecewise power curve to model non-linear chromatic transformations. The CRF operator $\mathcal{G}$ has four learned parameters: For each channel, the basic S-shaped curve is given: setting $a$ and $b$ to match the slope at the inflection point to ensure $C^{1}$ continuity: Finally, the CRF image operator $\mathcal{G}$ is a composition of this S-curve with a gamma correction: Figure 4: Qualitative comparison of novel view synthesis. Row labels indicate datasets and sequences (in italics). Column labels indicate methods. Heat maps show perceptual CIEDE2000 error (colormap range: 0–20 ΔE00). Our method achieves more consistent photometry and better color reproduction across various datasets and sequences. HDR-NeRF: When image metadata is available, our method can incorporate it to produce a more accurate novel view.

### Per-Frame ISP Parameter Controller

The exposure offsets and color correction transforms introduced above are valid only for a specific capture, *i.e*., a single camera pose, and therefore cannot be directly reused for novel view rendering. To address this limitation, we introduce a controller that predicts these parameters from the rendered scene radiance, analogous to how auto exposure and auto white balance work in conventional cameras: Here, $\mathcal{T}(\cdot)$ is the camera-specific controller parametric function, which we design as a coarse feature extractor ($1\times 1$ convolutions with pooling to a 5×5 grid), followed by a parameter regressor (an MLP with separate output heads). The detailed architecture of the controller is provided in the Supplementary.

We optimize the controller in a separate stage once the optimization of the scene representation is complete. At that stage, the underlying reconstruction and all per-camera ISP parameters are frozen, the controller-predicted parameters are applied through the ISP, and the controller itself is trained using the same photometric loss as in the initial phase. A qualitative example of the controller's effects is given in Fig. 3. Optional scalar controls (*e.g*., exposure compensation or EXIF-derived biases) can be concatenated to the regressor input.

### Regularization

Joint optimization of the modules can introduce brightness and color ambiguities between scene radiance and the ISP parameters. To mitigate this, we apply regularization on the previously defined parameters, using the Huber loss $\mathcal{L}_{\delta}$, where $\delta$ denotes the threshold. We use superscripts to indicate parameters belonging to specific camera sensors^(s)^ and frames^(f)^.

### Brightness

We penalize the mean exposure offset over frames:

### Color

We penalize the frame-mean of the target chromaticity offsets (element-wise in $\mathbb{R}^{2}$): Because chromatic corrections, as done in vignetting and CRF modules, may also introduce localized color shifts, we shrink parameter variance across channels. Let $\boldsymbol{\theta}_{m,k}$ be the parameters of channel $k$ for module $m\in\{\text{vig},\text{crf}\}$. We penalize their across-channel variance, averaged over parameters:

### Physically-plausible vignetting

For each polynomial, we penalize the center and softly enforce $\alpha_{j}\leq 0$: Here $[x]_{+}=\max(x,0)$ is the elementwise rectifier.

The overall regularizer is

## Experiments

We begin by evaluating the proposed PPISP correction module and controller on standard novel-view synthesis benchmarks, assessing both reconstruction fidelity and novel-view quality (Sec. 5.1). We then demonstrate how our formulation allows us to incorporate image metadata, such as relative exposure, when available (Sec. 5.2). We measure the runtime performance impact (Sec. 5.3). Finally, we analyze the relationship between model capacity, overfitting behavior, and novel-view synthesis performance (Sec. 5.4).

### Setting

As a reconstruction-agnostic post-processing step, the PPISP module readily applies to different radiance field methods. We integrate it in 3DGUT, GSplat (an accelerated implementation of 3DGS ), and Zip-NeRF.

Comparison baselines are the appearance correction approaches described in GLO, BilaRF, and ADOP. For experiments, we rely on their reference hyperparameters and reference implementations available in the respective framework. To increase the stability of ADOP's method, we increase the strength of their CRF regularization about $100\times$ compared to the reference value.

We jointly train the reconstruction method and the post-processing operator for 30k iterations. For the PPISP controller, we freeze both and train the controller for an additional 5k iterations. For 3DGS and 3DGUT, we enable MCMC sampling.

### Metrics

We evaluate the perceptual quality of the rendered views using peak signal-to-noise ratio (PSNR), structural similarity (SSIM), and learned perceptual image patch similarity (LPIPS) metrics.

As the PSNR metric is highly sensitive to global brightness shifts, and our baselines do not support appearance compensation for novel views, we additionally report the PSNR computed after affine color alignment, following RawNeRF. We denote this as "PSNR-CC", but emphasize that such comparison masks the differences between the methods and assumes access to the GT target views, which are not available in practice.

### Datasets

To show the robustness and generality of our method, we conducted experiments on a variety of publicly available datasets: Mip-NeRF 360, Tanks and Temples, BilaRF, HDR-NeRF, and nine static sequences of the Waymo Open Dataset.

To further highlight the differences of the methods in challenging real-world scenarios, we captured a new *PPISP dataset* consisting of four scenes. Each of them was captured with three different cameras (Apple iPhone 13 Pro, Nikon Z7, and OM System OM-1 Mark II) to ensure variations. More details about the scenes, resolution, and training-test splits are available in the Supplementary.

Table 1: Novel view synthesis results across methods and datasets. We compare appearance compensation methods applied on radiance field reconstruction methods. When the PPISP controller is omitted (w/o ctrl.), novel views use zero per-frame corrections. PSNR-CC factors out global exposure and color differences.

PPISP - no color correction Table 2: Component ablation of PPISP on the Tanks and Temples dataset for novel views (NV). Each row shows performance when removing the specified component.

### Novel View Synthesis Benchmark

Quantitative results on the standard benchmark scenes are presented in Tab. 1, and qualitative comparisons are shown in Fig. 4. Our method achieves the best PSNR, SSIM, and LPIPS in the large majority of settings across datasets and base methods, and on most datasets even surpasses the BilaRF baseline when that baseline is given privileged access to the target image, i.e., when comparing our PSNR against the baseline's PSNR-CC. These gains, established primarily on 3DGUT, extend to the 3DGS and Zip-NeRF integrations.

The comparison between PSNR and PSNR-CC further highlights the effectiveness of our controller in reproducing the camera's auto-exposure and white-balance behavior. On most datasets, the controller achieves metrics close to those obtained after affine color alignment, indicating that it faithfully predicts the necessary per-frame appearance corrections. The only notable discrepancy appears on the BilaRF dataset, likely due to the fact that this dataset contains some manual settings overrides (indicated by the metadata), which are not captured by our controller.

Both PPISP and ADOP employ camera-specific components (vignetting and CRF), which generalize to novel views, leading to improved metrics over BilaRF. Our base image formation model (*w/o ctrl.*) outperforms both of these baselines thanks to better separation of concerns of the individual modules and stronger constraints (see also Sec. 5.4; a detailed comparison to ADOP is provided in the Supplementary). Our full pipeline consistently improves upon the base model by providing plausible per-frame parameter estimates via the controller.

### Ablation

We ablate the relative contribution of each module in our pipeline through an ablation study on the Tanks and Temples dataset. Tab. 2 presents the novel view PSNR when individual components are removed from the full pipeline. The results demonstrate that all modules contribute to the full pipeline's performance, with exposure and vignetting corrections being most critical.

Table 3: Novel View PSNR across datasets with metadata. Our pipeline is able to leverage metadata (e.g. EXIF) from the sensor as a side data provided to the controller regressor.

### Using Image Metadata

Because our formulation closely mirrors the camera image formation process, it can naturally incorporate image metadata, such as the relative exposure of each frame, whenever available. We demonstrate this capability on the HDR-NeRF and PPISP datasets, both of which use exposure bracketing (*i.e*., captures with positive and negative exposure compensation) and provide the corresponding metadata. We concatenate this metadata to the input of the controller MLP regressor, allowing it to map rendered radiance plus metadata to effective ISP parameters.

Since the ADOP-style post-processing also models per-frame exposure offsets explicitly, we initialize them from known exposure values as proposed in ADOP.

Quantitative results in Tab. 3 show that supplying calibrated exposure offsets substantially improves novel-view accuracy. Moreover, providing this metadata to the controller yields further gains compared to ADOP, demonstrating our method's ability to leverage metadata for more accurate novel view appearance prediction.

Table 4: Rendering times (ms) on NVIDIA RTX 5090 for the MipNeRF 360 dataset.

Table 5: Average PSNR on the Tanks and Temples dataset comparing training views (TV) and novel views (NV) for ISP modules with varying capacity. The limited capacity of our proposed pipeline reduces overfitting and leads to better generalization.

### Runtime Performance

Tab. 4 presents the computational performance of the post-processing methods we evaluated compared to the scene rendering. PPISP (*w/o ctrl.*) and ADOP have a similar and very small computational footprint ($3\%$ of the rendering). The controller is adding a substantial overhead due to the required processing of the input image, but our pipeline remains significantly faster ($26\%$ vs $36\%$) compared to BilaRF on an NVIDIA RTX 5090 GPU.

### ISP Capacity vs. Training and Novel Views

Next, we investigate how the capacity of the correction module affects the overfitting (difference between the PSNR on training and novel views) and generalization to novel views. The bilateral grids used in BilaRF provide a highly expressive mechanism for modeling image operations extending beyond simple compensation of photometric inconsistencies. In BilaRF, this operation is learned independently for each frame, providing a high modeling capacity. In contrast, our PPISP module intentionally has limited capacity to prevent overfitting, but in turn cannot model complex image operations that mix spatial and intensity effects such as localized tone-mapping.

In Tab. 5, we therefore study hybrids of the two approaches. Adding more capacity to per-frame BilaRF with additional per-camera bilateral grids (+PC) does not meaningfully change PSNR on the training views as the model already has sufficient capacity. However, it does slightly improve the generalization as per-camera corrections carry over to novel viewpoints. Increasing our method's capacity by adding per-frame bilateral grids boosts PSNR on the training views, but noticeably degrades performance on novel views due to overfitting. Overall, our formulation achieves a favorable balance between capacity and generalization to unseen views.

## Conclusion and Limitations

Accurately reconstructing the radiance field of a scene requires accounting for variations in the camera imaging pipeline across the input frames. Ignoring these variations introduces strong biases, leading to spurious color shifts and geometric artifacts. In this work, we introduced a differentiable post-processing pipeline whose design permits simulating the imaging process while remaining highly constrained to prevent reconstruction bias. We further proposed a controller that improves generalization to novel views by predicting per-frame imaging parameters directly from the rendered radiance.

### Limitations

Our method shows superior generalization to novel views (Tab. 1), but it sometimes struggles to match the baselines on the training views (Tab. 5). This can be partially attributed to overfitting, but our formulation also ignores some important optical effects such as localized tone-mapping commonly found in modern phone cameras; lens flares, which are prominent in night scenes; and similar spatially-varying effects. While the proposed controller enables generalization to novel views, its ability to infer exposure and color-correction parameters from rendered radiance depends on the existence of meaningful correlations in the data. When such correlations are absent, for example when the physical camera controls (*e.g*., shutter, aperture, ISO) are manually overridden, the controller must rely on extra metadata to predict correct values.
