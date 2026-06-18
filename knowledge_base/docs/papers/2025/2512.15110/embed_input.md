<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Is Nano Banana Pro a Low-Level Vision All-Rounder? A Comprehensive Evaluation on 14 Tasks and 40 Datasets

Topics include Attention mechanisms, Image generation, Datasets, Benchmarks.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The rapid evolution of text-to-image generation models has revolutionized visual content creation. While commercial products like Nano Banana Pro have garnered significant attention, their potential as generalist solvers for traditional low-level vision challenges remains largely underexplored. In this study, we investigate the critical question: Is Nano Banana Pro a Low-Level Vision All-Rounder? We conducted a comprehensive zero-shot evaluation across 14 distinct low-level tasks spanning 40 diverse datasets. By utilizing simple textual prompts without fine-tuning, we benchmarked Nano Banana Pro against state-of-the-art specialist models. Our extensive analysis reveals a distinct performance dichotomy: while \textbf{Nano Banana Pro demonstrates superior subjective visual quality}, often hallucinating plausible high-frequency details that surpass specialist models, it lags behind in traditional reference-based quantitative metrics. We attribute this discrepancy to the inherent stochasticity of generative models, which struggle to maintain the strict pixel-level consistency required by conventional metrics. This report identifies Nano Banana Pro as a capable zero-shot contender for low-level vision tasks, while highlighting that achieving the high fidelity of domain specialists remains a significant hurdle.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent proliferation of Generative AI has fundamentally transformed the landscape of computer vision, with Text-to-Image (T2I) models demonstrating unprecedented capabilities in high-fidelity content creation. Among these, commercial products like Nano Banana Pro \[team2023gemini\] have emerged as standouts, garnering significant attention for their versatility. While its prowess in creative synthesis is well-documented, the extent to which such a large-scale foundation model can generalize to traditional low-level vision problems remains largely unexplored. This gap presents not only a challenge of capability but also one of evaluation, raising the pivotal research question: Is Nano Banana Pro a Low-Level Vision All-Rounder?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The motivation for this study is rooted in a fundamental tension between human perception and traditional metrics. On one hand, the rich visual priors encapsulated within robust generative models should theoretically enable them to hallucinate plausible solutions for restoration, enhancement, and fusion tasks without task-specific training. On the other hand, this generative nature may conflict with the goal of achieving the strict, pixel-perfect fidelity that is valued by conventional evaluation metrics. To investigate this, we systematically evaluate the zero-shot capabilities of Nano Banana Pro using simple textual prompts, a stark contrast to the complex pipeline fine-tuning typically required for specialist models.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our comprehensive empirical study spans 14 distinct low-level vision tasks across 40 datasets, covering image restoration, enhancement, and fusion. As visually exemplified in Fig. 1, Nano Banana Pro frequently produces outputs with remarkable perceptual quality. For instance, in tasks like dehazing or deraining, it can generate sharp edges and realistic textures that are often more aesthetically pleasing to a human observer than the results from specialist models. This initial observation immediately highlights a critical challenge: a model can be subjectively superior yet quantitatively inferior. Our work, therefore, aims not only to benchmark performance but also to delineate the boundaries of its current capabilities through rigorous quantitative and qualitative analysis. It is important to note that the present evaluation reflects a conservative estimate of the model's capability, as we did not engage in meticulous prompt tuning or employ multi-round inference to cherry-pick optimal outputs. Our fixed, simple prompts represent a pragmatic but unoptimized use case.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our findings uncover this anticipated dichotomy in stark detail: Nano Banana Pro excels in perceptual quality but lags in metric-driven fidelity. While it demonstrates remarkable zero-shot potential across a wide array of degradations, its outputs consistently score lower on reference-based metrics (e.g., PSNR, SSIM) when compared to domain-specific experts. We attribute this performance gap to the inherent stochasticity of generative models, which prioritize semantic plausibility over the strict pixel-wise alignment demanded by these metrics. In essence, while Nano Banana Pro has not yet achieved the status of a perfect all-rounder, it forces us to reconsider the traditional definition of success in low-level vision. It establishes a strong baseline for zero-shot restoration, highlighting both its emerging strengths and the critical need for new evaluation paradigms that can reconcile perceptual quality with pixel-level accuracy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this report is organized to systematically present these findings. We will detail our experimental results across Image Restoration, Image Enhancement, and Image Fusion, providing in-depth comparative analysis for each task. Finally, we conclude by summarizing the model's limitations and discussing potential future directions, including the development of more perception-aligned evaluation methods for generative low-level vision solvers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contents", "weight": 1.0} -->

2. 2.2 Quantitative and Qualitative Results
3. 4.3 Quantitative and Qualitative Results
2. 5.2 Qualitative and Quantitative Results
1. 6.2.1 Performance on Synthetic Datasets
2. 6.2.2 Performance on Real-World Datasets
3. 8.3 Quantitative and Qualitative Results
2. 10.2 Qualitative and Quantitative Results
11. 11 Low Light Image Enhancement
3. 11.3 Qualitative and Quantitative Results
12. 12 Underwater Image Enhancement
14. 14 Multi-Focus Image Fusion
15. 15 Infrared-Visible Image Fusion
1. 16.1 Generative vs. Regression Paradigms
2. 16.2 The Potential Misguidance of Traditional Metrics
3. 16.3 Operational Scope and Limitations of Nano Banana Pro
4. 16.4 Future Research Directions
1. 17.1 Prompts for Each Task

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Real-world Image Dehazing (RID) aims to recover clear and high-fidelity images from hazy observations captured in real-world environments. Unlike synthetic dehazing, where haze is generated under simplified physical assumptions, real-world haze is highly complex and exhibits strong spatial non-uniformity, large depth variations, severe color shifts, sensor noise, and compression artifacts. These factors make RID a long-standing and extremely challenging low-level vision problem. The goal of RID is not only to generate visually appealing results, but also to preserve accurate photometric and structural information to support reliable downstream vision tasks such as detection, tracking, and segmentation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Early dehazing methods \[song2023vision, qiu2023mb\] relied on handcrafted statistical priors, such as the Dark Channel Prior (DCP)\[he2010single\] and Non-Local Prior (NLP)\[berman2016non\], to constrain the solution space. While these physics-inspired approaches achieved initial success, they often fail to generalize across diverse real-world scenes and frequently introduce visible artifacts. With the rapid development of deep learning, numerous CNN-based and Transformer-based methods\[shao2020domain, chen2021psd, wu2023ridcp\], have significantly improved dehazing performance on synthetic benchmarks. However, collecting large-scale, perfectly aligned real-world hazy and clean image pairs remains nearly impossible. Although several real-world datasets have been constructed, their scale and diversity are still far from sufficient for training robust deep models. Consequently, most existing methods heavily rely on synthetic data and suffer from severe performance degradation when deployed in real-world scenarios.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To bridge this gap, recent studies have increasingly shifted their focus toward real-world dehazing. Some methods reintroduce physical priors to adapt pre-trained networks, while others modify inference strategies to improve generalization. Nevertheless, these approaches remain highly dependent on the quality of pre-training data. Moreover, heavily hazed images often contain severe information loss, fundamentally limiting the capability of traditional enhancement-based methods that lack generative flexibility to recover missing content.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nano Banana is an image generation model developed by Google DeepMind. Its professional version, Nano Banana Pro, further enhances precision and world knowledge understanding. We applied it to real-world image dehazing tasks, with a focus on its effectiveness in removing haze, restoring blurred textures, and maintaining scene semantic integrity and tested it on mainstream dehazing benchmarks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

To intuitively present the dehazing outcomes of the Nano Banana (NB) Pro model, we provide quantitative and qualitative evaluations of its processing results across the RTTS \[li2018benchmarking\] and Fattal's \[fattal2014dehazing\] datasets, with comparisons to state-of-the-art baseline methods in real-world dehazing tasks. Tab. 1 show the performance comparison between NB Pro and current mainstream dehazing networks on the RTTS and Fattal's datasets, where we evaluated three real-world-oriented dehazing metrics: FADE, BRISQUE and NIMA. Integrating the evaluation results on both the RTTS and Fattal's datasets, NB Pro demonstrates outstanding performance in terms of subjective visual quality, achieving top-tier NIMA scores on both benchmarks, which indicates that the generated images possess strong aesthetic appeal and favorable human perceptual quality. However, it performs poorly in terms of image naturalness. Specifically, NB Pro exhibits a significantly higher BRISQUE score on the Fattal's dataset, suggesting that the outputs may suffer from over-enhancement artifacts.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

Qualitative experimental results demonstrate that for extreme degradation scenarios such as dense fog with severe visibility loss, heavy atmospheric scattering, and complex urban or natural environments, NB Pro can generate perceptually enhanced results. Fig. 2 displays the visualization of exemplary dehazing cases for NB Pro on the RTTS dataset, highlighting both successful and challenging scenarios. For certain severely hazy images, benefiting from its powerful generative capabilities, NB Pro effectively restores intricate details---such as fine textures in buildings, vehicles, or vegetation---that are heavily obscured in the input, producing clear, high contrast outputs with impressive visual recovery of distant structures and overall scene coherence. Similarly, for some lightly foggy images, NB Pro performs well in optimization, selectively removing haze from distant backgrounds while preserving foreground sharpness and natural tones, resulting in balanced enhancements that improve visibility without introducing artifacts. Fig. 3 shows the visual comparison of NB and other methods on the RTTS dataset.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

However, NB Pro also exhibits numerous failure cases, as illustrated in Fig. 4. In these examples, spanning both moderate and heavy haze conditions, NB Pro often restores the images into distorted outputs characterized by unnatural color shifts, such as over-saturated or overly vibrant hues and hallucinatory weather elements, most notably forcing intensely blue skies into scenes that were originally overcast or neutral. These distortions undermine the authenticity of the atmospheric conditions, leading to results that deviate significantly from realistic dehazing expectations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

Overall, while NB Pro offers inspirational generative capabilities for ill-posed real-world dehazing, demonstrating the potential of semantic-driven priors in tackling highly ambiguous degradations---its limitations in color fidelity, physical realism, and consistent handling across varying haze densities suggest it is better suited for creative enhancements rather than precise low-level restoration. This prompts future research into hybrid approaches, such as combining NB Pro's zero-shot generative strengths with task-specific physical constraints or refined prompt engineering, to better constrain its tendencies toward perceptual appeal over faithful recovery.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Analyses", "weight": 1.0} -->

Stemming from a misalignment between training distributions and restoration objectives, NB Pro struggles to maintain spectral fidelity and atmospheric consistency. The model frequently over-corrects naturally muted, hazy tones into saturated, vibrant colors, introducing artificial chromatic biases that alter the scene's intrinsic mood. In severely hazy scenarios where high-frequency details are obliterated, NB Pro's generative priors dominate the restoration process. Rather than solving the inverse physical scattering model, it hallucinates details based on learned statistical patterns. A defining characteristic of this behavior is the systematic rendering of vivid blue skies in originally overcast scenes. While visually striking and aligned with subjective preferences for "clear weather", this deviation undermines the scene's authenticity and temporal consistency.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Analyses", "weight": 1.0} -->

Consequently, NB Pro is currently best positioned for creative content generation---prioritizing perceptual appeal and \"wow-factor\"---rather than forensic restoration tasks demanding strict adherence to physical constraints. However, its value remains significant. In the ill-posed domain of real-world dehazing, where traditional physics-based methods often falter due to unknown degradation parameters, NB Pro demonstrates the power of semantic priors to reconstruct plausible details in information-deficient scenarios. This suggests a pivotal direction for future research: developing hybrid frameworks. By integrating NB Pro-like generative backbones with task-specific physical constraints (e.g., atmospheric scattering laws) and fidelity anchors, we can bridge the gap between creative hallucination and realistic restoration, aiming for a paradigm that balances visual delight with physical truth.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Real-World Image Super-Resolution (Real-ISR) aims to restore high-fidelity, high-resolution content from low-resolution inputs degraded by complex, unknown physical processes. Unlike synthetic super-resolution, where degradations are modeled by simple bicubic downsampling, real-world scenarios involve intricate combinations of blur, sensor noise, compression artifacts, and varying camera response functions \[cai2019toward, wei2020component\]. This complexity renders traditional regression-based methods---which rely on pixel-wise optimization (e.g., MSE loss)---ineffective, often resulting in over-smoothed textures and a lack of high-frequency details \[dong2014learning, zhang2018image\].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

The landscape of generative Real-ISR has evolved rapidly. Generative Adversarial Networks (GANs) \[goodfellow2014generative, ledig2017photo\], represented by methods such as BSRGAN \[zhang2021designing\] and Real-ESRGAN \[wang2021real\], introduced high-order degradation modeling to synthesize realistic training pairs, significantly improving visual perceptual quality over PSNR-oriented baselines. More recently, Denoising Diffusion Probabilistic Models (DDPMs) \[ho2020denoising\] have emerged as the new state-of-the-art. Methods like StableSR \[wang2023exploiting\] and DiffBIR \[lin2023diffbir\] leverage strong priors from large-scale pre-trained text-to-image models (e.g., Stable Diffusion \[rombach2022high\]) to generate intricate textures. However, these multi-step diffusion models often suffer from high computational costs and slow inference speeds.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

To mitigate this, acceleration techniques have been proposed, exemplified by SinSR \[wang2024sinsr\], which distills complex diffusion priors into single-step inference models. Despite these advancements, a critical challenge remains: the inherent trade-off between perceptual quality and signal fidelity \[blau2018perception\], often leading to artifacts or structural hallucinations in the pursuit of sharpness.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we conduct a comprehensive quantitative and qualitative evaluation of Nano Banana Pro, a novel generative ISR framework, benchmarking it against a spectrum of industry-standard algorithms, including GAN-based approaches (BSRGAN \[zhang2021designing\], Real-ESRGAN \[wang2021real\]), multi-step diffusion models (StableSR \[wang2023exploiting\], DiffBIR \[lin2023diffbir\]), and accelerated diffusion methods (SinSR \[wang2024sinsr\]). Our goal is to rigorously assess where Nano Banana Pro stands within the current Perception-Distortion landscape.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

To ensure a robust evaluation across varying degradation complexities, our experiments are conducted on the large-scale DIV2K-Val dataset (2,994 images) \[agustsson2017ntire\] as well as the authentic RealSR \[cai2019toward\] and DRealSR \[wei2020component\] benchmarks. Recognizing that pixel fidelity alone is insufficient for characterizing generative performance, we employ a comprehensive set of evaluation metrics, incorporating not only standard Full-Reference indicators (PSNR, SSIM \[wang2004image\], LPIPS \[zhang2018unreasonable\]) but also widely-adopted No-Reference perceptual metrics (NIQE \[mittal2012making\], MUSIQ \[ke2021musiq\], CLIPIQA \[wang2023exploring\]). Under this rigorous testing framework, we systematically assess the reconstruction capabilities of Nano Banana Pro in comparison to established GAN-based and diffusion-based baselines.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting analysis provides a detailed characterization of the model's behavior regarding the perception-distortion trade-off, offering valuable insights into its suitability for real-world applications.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

To comprehensively evaluate Nano Banana Pro's performance in Real-ISR tasks, we quantitatively compared it against a range of advanced GAN-based and diffusion-based image super-resolution methods. We employed standard full-reference metrics: PSNR and SSIM to evaluate signal fidelity, and LPIPS to assess perceptual similarity. Additionally, No-Reference (NR) metrics NIQE, MUSIQ, and CLIPIQA were utilized to quantify the statistical naturalness and aesthetic quality of the generated images. Results are shown in Tab. 2. Nano Banana Pro significantly underperformed against the comparison methods in terms of traditional fidelity metrics. On the DIV2K-Val dataset, Nano Banana Pro achieved significantly lower PSNR and SSIM than the optimal method, lagging by over 4 dB. A similar trend, though less severe, was observed on the RealSR and DRealSR datasets, where its fidelity scores remained consistently behind both GAN-based and diffusion-based baselines. This result clearly indicates that under the standard full-reference evaluation framework, which prioritizes pixel-level accurate reconstruction, Nano Banana Pro's generated results exhibit systematic deviations from the ground-truth reference images.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Nano Banana Pro fundamentally differs from traditional super-resolution models optimized for specific degradation kernels. The latter typically undergo end-to-end training targeting minimization of pixel-level loss---thus inherently excelling in metrics like PSNR and SSIM. In contrast, Nano Banana Pro's generation process prioritizes semantic coherence and visual cleanliness. Its outputs can be viewed as plausible reconstructions of the input image rather than strict pixel-to-pixel mappings. Consequently, generated images may exhibit deviations in local texture alignment and structural positioning compared to reference images, leading to comprehensive score reductions across full-reference metrics. However, notably, on the NIQE metric, Nano Banana Pro consistently achieved the best scores across all three datasets (e.g., 3.52 on DIV2K-Val vs. 4.75 for BSRGAN). This suggests its outputs possess superior statistical naturalness, effectively suppressing artifacts, even though the low-level pixel arrangements have been altered from the original reference.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

In this section, we examine the generative characteristics of Nano Banana Pro across the DIV2K, RealSR, and DRealSR datasets. The qualitative evaluation is organized into four key scenarios to highlight both the strengths and failure modes of the model: geometric clarity, field-of-view artifacts, texture fidelity, and character reconstruction (Figs. 5--8).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 5 displays the super-resolution results on scenes with distinct geometric structures. In the examples of the architectural facade and hanging lanterns, Nano Banana Pro effectively sharpens the blurred edges and recovers the linear patterns lost in the low-resolution inputs. The resulting images maintain structural coherence and exhibit reduced noise, offering a noticeable improvement in clarity compared to the inputs.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 6 illustrates a distinct structural anomaly observed in Nano Banana Pro: unintended Field-of-View (FOV) expansion. Comparing the low-resolution input, the Ground Truth (GT), and the Nano Banana Pro generated result reveals that the model fails to strictly adhere to the original spatial boundaries of the input image. Instead of merely super-resolving the existing pixels, Nano Banana Pro erroneously hallucinates additional content along the image periphery.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 7 illustrates the tendency of Nano Banana Pro to synthesize plausible but non-existent details in areas with complex stochastic textures. In the foliage and stone carving examples, while the model produces sharp, high-frequency patterns, these generated textures often deviate from the Ground Truth. Specifically, the arrangement of leaf veins and the granular surface of the stone are reconstructed with altered local structures rather than being faithfully restored, leading to pixel-level discrepancies that lower fidelity scores.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 8 highlights the dependency of Nano Banana Pro on semantic recognizability for text reconstruction. In the examples on the left, where the low-resolution input retains discernible structural features (such as the logo and digits), the model accurately reconstructs sharp and legible characters. Conversely, the examples on the right demonstrate failure cases where severe degradation obscures the original glyphs, particularly with complex Chinese characters. In these instances, the model fails to recover the correct semantic content and instead hallucinates incorrect strokes or non-existent characters, resulting in high-contrast but semantically erroneous text.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Analyses", "weight": 1.0} -->

Our comprehensive evaluation elucidates the operational characteristics of Nano Banana Pro within the Real-ISR domain. Quantitatively, the model trails significantly behind mainstream GAN and diffusion-based methods in fidelity metrics (PSNR/SSIM) across the DIV2K-Val and RealSR datasets; however, it achieves remarkable performance in the no-reference NIQE metric. This discrepancy suggests that, as evidenced in Fig. 7, the model prioritizes learned generative priors to synthesize texture details rather than strictly adhering to the low-resolution input.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Analyses", "weight": 1.0} -->

Qualitatively, unlike traditional restoration models that maintain strict spatial consistency, Nano Banana Pro lacks precise pixel-level alignment with the reference image. Consequently, unintended Field-of-View (FOV) expansion is observed, as shown in Fig. 6. Furthermore, the text reconstruction failures in Fig. 8 reveal the model's heavy reliance on feature recognizability. When encountering degraded features such as blurred text, the model exhibits a tendency to aggressively generate sharp outputs. This behavior causes feature recognition errors to have a catastrophic impact on the result, leading to the hallucination of sharp but semantically incorrect text.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Analyses", "weight": 1.0} -->

Synthesizing these findings, Nano Banana Pro is highly suitable for perception-centric applications---such as artistic upscaling, old photo restoration, or casual photography---where visual purity and noise elimination are paramount. However, due to its propensities for texture hallucination, spatial misalignment, and semantic alteration, it is unsuitable for fidelity-critical scenarios.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

To thoroughly evaluate the performance and generalization ability of Nano Banana Pro on the single image deraining task, we conduct experiments on three widely used benchmark datasets: two synthetic datasets, Rain200L and Rain200H\[yang2017deep\], and one real-world dataset, SPA\[Wang_2019_CVPR\]. These datasets cover a broad range of rain patterns and scene complexities, enabling a comprehensive assessment of the model's restoration capability.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Rain200L\[yang2017deep\]: Contains 1,800 pairs of synthetic training images and 200 test pairs. The rain streaks in this dataset exhibit a single predominant direction and relatively low density, making it suitable for assessing the model's basic restoration ability under simple rain conditions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Rain200H\[yang2017deep\]: Provides 1,800 training pairs and 200 test pairs, but features rain streaks with higher density and more diverse orientations. This dataset is designed to evaluate the robustness of deraining models when faced with heavy and structurally complex rain degradations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

SPA\[Wang_2019_CVPR\]: A large-scale real-world rainy image dataset comprising 638,492 training pairs and 1,000 test images. The rain patterns in SPA are highly diverse, and the background scenes vary significantly, making it an appropriate benchmark for measuring cross-domain generalization from synthetic to real rainy conditions.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

All images from all datasets are given the prompt: "This is a rainy image. Please remove the rain streaks and raindrops while keeping all other elements, the original color tone, lighting, and atmosphere unchanged."

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

It is worth emphasizing that Nano Banana Pro is evaluated in a strictly zero-shot manner: no training images are used for optimization, fine-tuning, or adaptation, and the model is directly applied to the test images via a fixed textual prompt.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

For fair comparison, all metrics are computed under exactly the same evaluation protocol as NeRD-Rain, including image resolution, color space, and PSNR/SSIM computation. Based on the quantitative results reported in Tab. 3, we systematically evaluate the image deraining performance of Nano Banana Pro on two synthetic datasets, Rain200L\[yang2017deep\] and Rain200H\[yang2017deep\], as well as the real-world SPA-Data dataset\[Wang_2019_CVPR\], and compare it with a wide range of representative methods.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

The compared approaches cover prior-based methods (DSC\[luo2015removing\], GMM\[li2016rain\]), CNN-based methods (DDN\[fu2017removing\], RESCAN\[li2018recurrent\], PReNet\[ren2019progressive\], MSPFN\[jiang2020multi\], RCDNet\[wang2020model\], MPRNet\[zamir2021multi\], DualGCN\[fu2021rain\], SPDNet\[yi2021structure\]), and Transformer-based methods (Uformer\[wang2022uformer\], Restormer\[zamir2022restormer\], IDT\[xiao2022image\], DRSformer\[chen2023learning\], NeRD-Rain\[NeRD-Rain\]).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

The quantitative performance of Nano Banana Pro is significantly inferior to that of state-of-the-art deraining models across all three datasets. On Rain200L\[yang2017deep\], Nano Banana Pro achieves 26.05 dB PSNR and 0.7954 SSIM, which are substantially lower than those of supervised learning-based methods. On the more challenging Rain200H dataset with complex rain patterns, Nano Banana Pro obtains 21.10 dB PSNR and 0.6659 SSIM. Although it outperforms traditional prior-based methods, a considerable performance gap remains compared to CNN-based and Transformer-based approaches. On the real-world SPA-Data dataset\[Wang_2019_CVPR\], Nano Banana Pro reaches 32.25 dB PSNR and 0.9142 SSIM, still noticeably below the current best-performing methods.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

This quantitative degradation is consistent with the visual results in Fig. 9, where large and dense synthetic rain streaks severely obscure background content, leading to color deviations and missing or oversmoothed fine details. Since Nano Banana Pro is not trained specifically for image deraining, local structures are often reconstructed via implicit generative hallucination rather than pixel-wise restoration, which negatively affects PSNR and SSIM. Nevertheless, the model demonstrates notable strength in recovering certain global structures; for example, the cable geometry of the suspension bridge is reconstructed with higher structural coherence and semantic plausibility than several supervised baselines.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

Furthermore, Fig. 10 shows that the deraining performance of Nano Banana Pro is highly sensitive to rainfall intensity: under low-rain conditions, where more reliable visual information is preserved, both color fidelity and fine details are significantly improved, whereas heavy rainfall introduces severe occlusion and ambiguity, resulting in pronounced color shifts and detail degradation. Overall, these results indicate that while generative multimodal models are disadvantaged in pixel-level fidelity under zero-shot deraining, they retain strong semantic and structural priors, suggesting complementary potential in scenarios with limited supervision or severe information loss.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

Our qualitative analysis reveals a fundamental limitation in the instruction-following behavior of prompt-conditioned multimodal generative models. As shown in Fig. 11, despite utilizing explicit prompts that constrain the model to preserve non-rain regions, we consistently observe unintended alterations in background elements.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

This phenomenon stems from an inherent bias in fine-grained semantic understanding. As clearly illustrated in Fig. 12, the model conflates rain streaks with atmospheric haze (i.e., the rain-mist ambiguity). Consequently, it aggressively removes the mist alongside the rain, yielding an output image that appears clearer and visually superior in low-level details. However, this visual enhancement paradoxically leads to lower quantitative scores (e.g., PSNR), as the complete removal of haze introduces a significant pixel-wise deviation from the ground truth. This observation underscores the prevalent perception-distortion trade-off in image restoration tasks.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Analyses", "weight": 1.0} -->

In this study, we investigated the feasibility of Nano Banana Pro for single-image deraining under a zero-shot setting. Experimental results indicate that the application of generative models to image restoration presents a "double-edged sword" effect. On one hand, compared to specialized deraining models trained on extensive supervised data, such as NeRD-Rain and Restormer, Nano Banana Pro exhibits a significant gap in pixel-level objective metrics like PSNR and SSIM (e.g., achieving a PSNR of only 21.10 dB on the Rain200H dataset). This quantitative deficiency is primarily attributed to the inherent tendency of generative models to prioritize semantic reconstruction over strict pixel-wise restoration, resulting in deviations in high-frequency detail preservation and color fidelity. On the other hand, leveraging its robust world model and semantic reasoning capabilities, Nano Banana Pro demonstrates superior structural coherence and visual plausibility compared to traditional methods when handling regions with severe rain occlusion (such as bridge cables). This confirms the unique complementary advantages of generative models in addressing extreme degradation and information loss.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Analyses", "weight": 1.0} -->

Future work will focus on employing prompt tuning to further enhance pixel-level restoration accuracy for low-level vision tasks, while preserving the model's strong semantic generation capabilities.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

Fig. 13 presents the well-performing shadow removal results of NB Pro on the SRD dataset \[qu2017deshadownet\]. It can be observed that NB Pro effectively removes shadows from the image while highly preserving the original elements without alteration. Tab. 4 presents the quantitative comparison on SRD dataset of NB Pro against state-of-the-art shadow removal methods, using PSNR and SSIM as the primary evaluation metrics.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

As shown in Tab. 4, a significant discrepancy exists between the visual quality discussed earlier and the numerical fidelity scores. While leading methods such as ShadowDiffusion \[guo2023shadowdiffusion\] and HomoFormer \[xiao2024homoformer\] achieve PSNR scores exceeding 34 dB and SSIM values above 0.97, NB Pro records comparatively lower scores, with a PSNR of 20.67 dB and SSIM of 0.682. This quantitative gap can be attributed to the inherent characteristics of generative models: NB Pro prioritizes perceptual plausibility and visual naturalness over strict pixel-wise alignment with ground truth references. Unlike traditional methods that focus on precise reconstruction, generative approaches like NB Pro tend to produce images with enhanced visual appeal, which may deviate from the exact pixel values of ground truth images, resulting in lower scores on fidelity-based metrics.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

In addition to its successful cases, we systematically document representative failure modes of NB Pro in shadow removal, as compiled in Fig. 14. These examples reveal two core, recurring limitations that stem from the model's generative nature: a propensity for over-generation and a blindness to subtle shadows.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

A consistent pattern of failure emerges across the SDR dataset, revealing critical limitations in NB Pro's approach. The first failure mode stems from the model's inherent generative bias. Driven by a compulsion to produce visually 'complete' scenes, NB Pro often prioritizes hallucinated content over fidelity. As illustrated in Fig. 14, while the cast shadow is successfully removed, the model erroneously synthesizes a new hand to fill the void, fundamentally compromising the scene's semantic integrity. This highlights a tension between the model's creative instinct and the strict fidelity required for low-level vision, where structural preservation is paramount. The second failure mode exposes a lack of sensitivity in shadow detection. NB Pro frequently overlooks soft, low-contrast, or faint shadows (as seen in the second example), leaving them entirely untreated. This suggests a potential bias in the training data or optimization objectives that under-weights subtle illumination changes. Furthermore, the model struggles with color fidelity, frequently exhibiting shifts in tone and saturation that deviate from the ground truth. Collectively, these structural hallucinations, detection failures, and color shifts lead to unsatisfactory quantitative performance.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Analysis", "weight": 1.0} -->

Nano Banana Pro demonstrates a remarkable ability to decouple shadow components from the underlying reflectance. However, its effectiveness is fundamentally constrained by its generative nature, which presents a significant paradigm mismatch with the strict fidelity requirements of shadow removal.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Analysis", "weight": 1.0} -->

First, the model's inherent generative bias prioritizes perceptual plausibility over structural fidelity. As a generative model, NB Pro tends to hallucinate details, alter textures, or even synthesize new objects to create visually complete scenes. While this enhances aesthetic appeal, it compromises pixel-level accuracy, causing the output to deviate from a truthful reconstruction of the original reflectance. Consequently, NB Pro is better suited for creative applications requiring visual realism rather than low-level vision tasks demanding precise photometric or geometric correspondence.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Analysis", "weight": 1.0} -->

Second, the model exhibits limited sensitivity in shadow detection. This limitation is likely attributable to biases in its training data or optimization objectives. If the training distribution under-represents subtle, soft, or low-contrast shadows, the model fails to learn the necessary features to identify them. As a result, NB Pro often leaves faint shadows untreated or, conversely, erroneously alters well-lit areas in an attempt to enforce uniform illumination, introducing artifacts in non-shadow regions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Analysis", "weight": 1.0} -->

Finally, these limitations are exacerbated by the incompatibility between generative outputs and traditional evaluation metrics. NB Pro typically generates images at fixed, high resolutions (e.g., 1K or 4K). Downsampling these outputs to match benchmark ground-truth resolutions smooths out high-frequency details, artificially depressing scores on pixel-wise metrics like PSNR and SSIM. More critically, a paradox arises where the model's generative enhancements, such as implicit super-resolution or denoising, are heavily penalized as deviations from the ground truth. This stark divergence between perceptual quality and quantitative scores underscores the inadequacy of current fidelity-based frameworks for evaluating generative restoration models.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

We conduct a visual analysis of NB Pro on standard benchmark datasets(GoPro \[nah2017deep\], HIDE \[shen2019human\] and RealBlur \[rim2020real\]) to evaluate its performance in restoring structural details and handling complex degradations.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Performance on Synthetic Datasets", "weight": 1.0} -->

NB Pro demonstrates impressive deblurring capabilities on synthetic datasets, particularly in recovering static environmental details. As observed in Fig. 15, in the second column of GoPro and the first column of HIDE, the model effectively suppresses severe motion blur and restores high-frequency structures with great precision. Architectural elements, such as the building facades and pavement textures, are reconstructed with high fidelity. Notably, the model excels at text preservation in these scenarios; for instance, the \"SEPHORA\" signboard in the HIDE dataset is rendered clearly. This indicates strong spatial adaptability in handling rigid motion and structural edges.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Performance on Synthetic Datasets", "weight": 1.0} -->

However, significant limitations become apparent when processing highly dynamic scenes involving humans. The model struggles to fully eliminate complex synthetic motion trajectories, leading to noticeable residual artifacts. In the first column of GoPro, for example, the clothes hanging on the wall appear duplicated, and the woman's headscarf exhibits a double-layer ghosting effect, suggesting an incomplete resolution of the motion path. Furthermore, the model tends to hallucinate facial details. While the restored faces in both GoPro (1st column) and HIDE (2nd column) appear visually sharp, they suffer from semantic inconsistencies. The facial features are altered to the extent that the identity of the pedestrians no longer matches the Ground Truth (GT), highlighting a critical lack of fidelity in semantic reconstruction.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Performance on Real-World Datasets", "weight": 1.0} -->

On real-world datasets, NB Pro exhibits strong robustness against complex degradations such as low light and overexposure. As seen in Fig. 16, in the RealBlur-J dataset, the model successfully recovers the legibility of text on posters and signboards. Its ability to handle high dynamic range scenes is particularly noteworthy, in the storefront examples (2nd columns of both RealBlur-J and RealBlur-R), the model manages high-contrast lighting effectively. However, the result generated by NB Pro in the second column of RealBlur-R deviates significantly from the GT properties. While the output appears cleaner, it aggressively removes noise and alters lighting textures, resulting in a synthesized appearance that loses the atmosphere of the original scene.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Performance on Real-World Datasets", "weight": 1.0} -->

Moreover, the model's reliance on generative priors introduces substantial perceptual deviations from the ground truth. In the poster examples of RealBlur-J (1st column), the restored facial features differ from the original image, creating a \"hallucinated\" face that does not preserve the subject's identity. Similar discrepancies are observed in the text content of the RealBlur-J (2nd column) result, where the generated characters deviate from the GT, such as pink characters on the window. This can be also observed in the second column of RealBlur-R, where the characters on the illuminated sign are significantly altered compared to GT. Additionally, color fidelity is occasionally compromised. For instance, in the first column of RealBlur-R, the skin tone of the person in the result exhibits a noticeable color shift compared to the target image. These issues indicate that while NB Pro excels at producing visually pleasing results, it sacrifices faithfulness to the original semantic content.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Tab. 5 presents the quantitative comparison of NB Pro against state-of-the-art deblurring methods, including transformer-based models like Uformer and Restormer, as well as recent diffusion-based approaches like HI-Diff and ID-CDM. The evaluation is performed on four standard benchmarks: GoPro \[nah2017deep\], HIDEHIDE \[shen2019human\] and RealBlur \[rim2020real\], using PSNR and SSIM as the primary metrics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

As observed in Tab. 5, a significant divergence exists between the previously discussed visual sharpness and the numerical fidelity scores. While top-performing methods such as ID-CDM and HI-Diff achieve PSNR scores exceeding 33 dB on the GoPro dataset and 36 dB on RealBlur-R, NB Pro records comparatively lower values, such as 21.41 dB on GoPro and 21.35 dB on HIDE. Similarly, the SSIM scores for NB Pro range between 0.645 and 0.778, whereas competing methods consistently score above 0.90. This quantitative gap can be primarily attributed to the model's heavy reliance on strong generative priors, which prioritizes perceptual plausibility over strict pixel-wise alignment with the ground truth.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

The lower PSNR and SSIM scores directly corroborate the limitations identified in the qualitative analysis. Standard metrics like PSNR are highly sensitive to pixel-level deviations. As noted in the visual evaluation, NB Pro tends to hallucinate high-frequency details, such as altering facial identities or modifying text characters, to maximize sharpness. These generated features, while appearing visually coherent, act as \"errors\" regarding the reference image, leading to heavy penalties in signal-to-noise calculations. Furthermore, the reported semantic inconsistencies, such as color shifts and the \"double-layer ghosting\" effects caused by misinterpreted motion trajectories, significantly disrupt structural similarity, resulting in the observed drop in SSIM. This confirms that the model's generated content often diverges from the underlying ground truth signal.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Analysis", "weight": 1.0} -->

The discrepancy between NB Pro's superior visual sharpness and its lower quantitative scores stems primarily from the perception-distortion trade-off. While regression-based methods minimize pixel-wise error to maximize PSNR, often resulting in over-smoothed textures, NB Pro leverages generative priors to create high-frequency details. This strategy produces visually realistic textures but introduces stochastic pixel deviations from the ground truth. Since standard metrics like PSNR penalize any deviation equally, NB Pro receives lower scores despite operating at a higher level of perceptual quality.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Analysis", "weight": 1.0} -->

Furthermore, the evaluation on real-world datasets reveals the specific limitations of the model's reconstruction capability. While the ground truth in RealBlur sometimes contains noise or light scattering, NB Pro's tendency to completely \"clean\" these elements represents a deviation from the scene's authentic characteristics. Rather than simply restoring the signal, the model synthesizes a new, idealized version of the image. This leads to low quantitative scores not just because of metric limitations, but because the model fails to preserve the original distribution of the input data, effectively altering the scene's atmosphere.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Analysis", "weight": 1.0} -->

Consequently, this reliance on generative priors introduces significant risks regarding semantic fidelity. When motion blur obliterates structural information, the model synthesizes plausible but factually incorrect content, leading to the observed \"identity swaps\" in human faces and ghosting artifacts in complex motion paths. While NB Pro excels in perceptual synthesis, making it suitable for visually-oriented restoration, these semantic inconsistencies highlight its unsuitability for applications requiring strict adherence to the original input signal, such as forensic analysis or high-fidelity surveillance.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Introduction", "weight": 1.5} -->

Defocus blur, an inherent optical phenomenon resulting from limited depth of field and aperture configurations, presents one of the most complex challenges in computational photography and low-level vision. Unlike uniform degradations such as global motion blur, defocus acts as a spatially varying aberration where the point spread function (PSF) changes according to the scene depth. This results in a non-uniform loss of high-frequency details and edge information, making the restoration process an ill-posed inverse problem that requires estimating spatially adaptive kernels.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Introduction", "weight": 1.5} -->

The field of single-image defocus deblurring has advanced significantly with the advent of deep learning. Early data-driven approaches, such as DPDNet \[abuolaim2020defocus\], established strong baselines by leveraging dual-pixel data to supervise defocus removal. Subsequent architectures, including IFANet \[lee2021iterative\] and KPAC \[son2021single\], introduced iterative filtering and kernel prediction mechanisms to better handle spatially varying blur. More recently, the introduction of Transformer-based architectures, such as Restormer \[zamir2022restormer\], and multi-stage networks like MPRNet \[mehri2021mprnet\], has pushed the boundaries of restoration fidelity by capturing long-range dependencies and global context. Current state-of-the-art methods, such as GGKMNet \[quan2024deep\], further refine this process by integrating grouped kernel modeling to precisely invert the blurring process across complex depth maps.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this section, we extend our evaluation of the Nano Banana Pro (NB Pro) to the domain of defocus deblurring. Unlike the aforementioned supervised methods, which are trained specifically on paired defocus datasets, our investigation focuses on assessing the NB Pro model in a zero-shot inference setting. By benchmarking the model against standard datasets such as DPDD \[abuolaim2020defocus\] and RealDOF \[ruan2021aifnet\], we aim to analyze its efficacy in handling the inverse problem of deblurring without domain-specific fine-tuning. Specifically, we examine whether the model's processing pipeline can genuinely recover lost structural information comparable to established specialized networks, or if it merely relies on superficial enhancement techniques.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Tab. 6 presents the quantitative evaluation on the DPDD \[abuolaim2020defocus\] and RealDOF \[ruan2021aifnet\] datasets. The results indicate a substantial performance gap between the Nano Banana Pro and established defocus deblurring methods. On the DPDD dataset, the Nano Banana Pro yields a PSNR of 20.180 dB and an SSIM of 0.635, significantly trailing the state-of-the-art GGKMNet by over 6 dB. A similar deficiency is evident on the RealDOF dataset, where NB Pro lags behind even early baselines like DPDNet. These low metrics align consistently with our qualitative findings: the depressed PSNR reflects the model's general failure to restore pixel-level sharpness, while the low SSIM corroborates the structural hallucinations and inability to remove blur observed in the visual comparison.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

However, it is worth noting that the competing methods, such as Restormer and DPDNet, are supervised models trained directly on the DPDD dataset, whereas NB Pro is evaluated here in a zero-shot setting without domain-specific training.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

We evaluated the perceptual performance of the Nano Banana Pro by conducting a comprehensive visual analysis on the DPDD and RealDOF datasets. The results indicate a consistent limitation in the model's ability to recover high-frequency details from severe defocus, with the model frequently prioritizing global contrast enhancement over effective blur removal.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

On the DPDD dataset, NB Pro behaves more akin to an image enhancement filter than a specialized deblurring network. As seen in Fig. 17, in scenarios such as Case 1 and Case 2, the primary modification to the input is a global increase in luminance and contrast. While this improves the visual punch of the image, it fails to address the underlying degradation. Specifically, the severely defocused foreground in Case 2 remains blurry, and the background bokeh in Case 1 is only marginally reduced in spread. Furthermore, the model exhibits instability in structural reconstruction. This is evident in Case 3, where the restoration process hallucinates semantic details, incorrectly recovering the text \"GE CANADA\" as \"OE CANADA\" despite only a slight improvement in sharpness. Similarly, in Case 4, while the foreground fence is adequately sharpened, it compromises geometric fidelity, resulting in an unexplained scale alteration of the red vehicle in the background.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

The limitations of NB Pro are even more pronounced in the RealDOF dataset evaluations, where the model demonstrates a negligible deblurring effect across multiple test cases. As seen in Fig. 18, in scenes with spatially varying blur, such as the mid-range focus in Case 1 and the foreground focus in Case 2, the model fails to reverse the defocus entirely. The output images are characterized solely by a slight boost in contrast, leaving the blurred regions perceptually identical to the input. While the model achieves a degree of sharpness recovery in the fully blurred scenario of Case 3, this comes at the cost of introducing high-frequency artifacts, specifically salt-and-pepper noise visible on the building structures. Moreover, the restoration in Case 4 is depth-limited. The model successfully restores the ground texture closest to the lens but fails to extend the depth of field to the background, which remains in a state of defocus with only a minor reduction in the circle of confusion. Collectively, these qualitative results suggest that the Nano Banana Pro lacks the robustness required for consistent defocus deblurring, often failing to produce a discernible improvement in image sharpness.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Analysis", "weight": 1.0} -->

The disparity between the quantitative metrics and the qualitative visual outputs reveals the inherent instability of applying a general-purpose generative model to the specific physical constraints of defocus deblurring. Our analysis suggests that the Nano Banana Pro does not perform a mathematical inversion of the optical point spread function. Instead, it relies on semantic-aware generative priors to synthesize sharp details. This results in a bimodal behavior where the model oscillates between superficial contrast adjustment and aggressive, perceptually driven reconstruction depending on the scene's semantic recognisability.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Analysis", "weight": 1.0} -->

In complex scenes with varying depth and high-frequency clutter, such as those in the DPDD dataset, the model's generative mechanism often struggles to identify coherent structural cues. Consequently, the model defaults to a global contrast maximization approach. This explains the consistently low PSNR values observed in Tab. 6. While increasing local contrast can improve perceptual punch in slightly out-of-focus regions, it fails to mathematically invert the point spread function. Consequently, the model exhibits inconsistent restoration behaviors, resorting to superficial contrast adjustment when semantic cues are ambiguous, while attempting aggressive reconstruction in scenes with recognizable structures.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Analysis", "weight": 1.0} -->

However, in scenarios with regular, recognizable structures such as the building facade in Fig. 18 Case 3, the model successfully engages its learned priors to \"re-paint\" the geometry, effectively removing the blur. Yet, this reconstruction is perceptually driven rather than physically constrained, leading to high-frequency artifacts. The salt-and-pepper noise observed along the window frames is likely a byproduct of the generative process (e.g., instability in the diffusion sampling) attempting to force high-frequency gradients into latent features that do not perfectly align with the degraded input.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Analysis", "weight": 1.0} -->

Conversely, when the defocus aligns with typical photographic aesthetics, the model exhibits passivity. This is clearly observed in Fig. 18 Case 4, where the background exhibits only mild defocus and remains semantically distinguishable, yet the model sharpens only the foreground ground texture while leaving the background blur intact. This divergence strongly suggests that the model's priors interpret the slight background defocus as an intended aesthetic attribute, specifically, as a natural depth-of-field, rather than a degradation requiring correction. Unlike dedicated deblurring networks that aim to minimize the circle of confusion globally, NB Pro appears to prioritize perceptual naturalness, effectively treating the background blur as context to be preserved rather than an error to be inverted.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Analysis", "weight": 1.0} -->

Finally, the lack of fidelity constraints in this zero-shot setting leads to significant structural deviations. Since the model prioritizes perceptual plausibility over pixel-wise accuracy, it introduces semantic errors when input ambiguity is high (such as hallucinating \"OE CANADA\" instead of \"GE CANADA\" in Fig. 18 and altering the geometric scale of the vehicle in Fig. 17). These behaviors confirm that the Nano Banana Pro operates as an image re-synthesis engine rather than a dedicated restoration tool, resulting in low quantitative scores (PSNR/SSIM) despite occasional visual successes.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

NanoBanana is a closed-source unified multimodal model accessed through its official API. As a model capable of image understanding, generation, and text-driven editing, we evaluate its denoising capability by providing noisy images alongside a natural language instruction. The prompt used throughout our experiments is: "This is a noisy image, please remove the noise in this image while keep other elements in this image unchanged."

<!-- chunk {"id": "body-0083", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Datasets. We evaluate Nano Banana Pro on five widely-used image denoising benchmarks spanning both synthetic and real-world noise scenarios. For synthetic noise datasets like McMaster \[mcmaster\], \[Kodak\], and Urban100 \[urban\], we corrupt clean images with additive white Gaussian noise at a fixed noise level of $\sigma$ = 50, representing a challenging high-noise regime. McMaster contains 18 high-resolution images with rich color and texture, comprises 24 classic photographic images, and Urban100 includes 100 images with complex urban structures and repetitive patterns that stress high-frequency reconstruction. For real-world noise datasets like PolyU \[polyu\] and SIDD-small \[sidd\], we use the standard noisy/clean image pairs provided by each benchmark without additional synthetic corruption. These datasets capture realistic sensor noise from various camera devices under diverse lighting conditions, presenting a more practical evaluation scenario.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Resolution and Failure Case Handling. Nano Banana Pro outputs images at approximately 1K resolution, though the exact dimensions vary across samples (e.g., 1024×1024, 1200×896, 720×1456). We resize the output images to match the resolution of corresponding ground truth images using bilinear interpolation. All metrics are then computed between the resized outputs and the ground truths. In addition, during evaluation, we observed that Nano Banana Pro occasionally produces outputs that are either semantically irrelevant to the input image or fail to remove noise effectively. In such cases, we regenerate the output by resubmitting the same input and prompt to the API until a valid denoised result is obtained. This protocol ensures that our quantitative metrics reflect the model's denoising capability under successful generation, while the occurrence of such failures is noted as a limitation of applying unified generative models to restoration tasks.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Evaluation Metrics. We adopt two complementary metrics to assess denoising quality: PSNR (Peak Signal-to-Noise Ratio), which measures pixel-level fidelity. SSIM (Structural Similarity Index): Evaluates perceptual structural similarity. Both are computed on RGB channels

<!-- chunk {"id": "body-0086", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

To systematically evaluate the image denoising capabilities of Nano Banana Pro, we invoked the model via its official API and compared its performance against five representative task-specific baselines (DnCNN \[dncnn\], Restormer \[zamir2022restormer\], MaskDenoising \[maskdenoising\], HAT \[HAT\], and DIL \[DIL\]). The evaluation spans two distinct regimes. First, we employed three synthetic benchmarks---McMaster \[mcmaster\], \[Kodak\], and Urban100 \[urban\]---corrupted with additive Gaussian noise ($\sigma = 50$) to test reconstruction across varying complexities. Specifically, McMaster assesses basic noise removal in smooth textures; covers diverse natural scenes to balance texture and color fidelity; and Urban100 challenges the model's ability to preserve high-frequency details within complex architectural structures. Complementing these synthetic tests, we assessed real-world blind denoising performance using SIDD Val \[sidd\] and PolyU \[polyu\], where no prior noise information is provided.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

SIDD Val serves as a core benchmark for handling authentic sensor noise captured under varying lighting and device conditions. Furthermore, PolyU is utilized to stress-test the model's generalization capabilities on irregular noise distributions characteristic of low-light and complex environments.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

As shown in Tab. 7, Nano Banana Pro exhibits a substantial performance deficit compared to all task-specific baselines. On synthetic datasets, it lags significantly behind the state-of-the-art DIL, with PSNR gaps ranging from 5.04 dB to 7.42 dB and SSIM reductions between 0.075 and 0.219. Notably, this disparity persists regardless of texture complexity (from McMaster to Urban100), indicating a fundamental lack of competitiveness in Gaussian noise removal. This limitation is further exacerbated in real-world blind denoising tasks. On SIDD Val \[sidd\], Nano Banana Pro trails DIL by 8.00 dB in PSNR. The gap widens drastically on PolyU \[polyu\], where it underperforms DIL by 14.83 dB and even falls behind the basic MaskDenoising model. These results underscore an inherent inability of Nano Banana Pro to effectively model and remove complex, realistic noise compared to specialized restoration models.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Quantitative and Qualitative Results", "weight": 1.0} -->

Fig. 19 visually compares Nano Banana Pro against state-of-the-art baselines. The results reveal a distinct characteristic of the generative approach: a trade-off between perceptual clarity and pixel-level fidelity. As shown in the first row, Nano Banana Pro exhibits exceptional perceptual quality on text-rich images. Leveraging its generative priors, it reconstructs the characters with remarkable sharpness. Notably, the output appears even clearer and more legible than the Ground Truth, effectively performing text enhancement alongside denoising. Conversely, the model struggles with consistency in texture and color, as seen in the subsequent rows: In the second row, the model fails to recover the subtle grain of the surface. Instead of preserving the original high-frequency details, it produces an over-smoothed or hallucinated texture that deviates significantly from the Ground Truth. In the third row, the model introduces chromatic deviations. While the noise is removed, the color of the grapes shifts noticeably (appearing brighter and yellower). These cases underscore that while Nano Banana Pro can generate visually pleasing results, it lacks the strict fidelity required for high-precision restoration tasks.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion", "weight": 1.5} -->

Misalignment of Task Objectives: Nano Banana Pro is a general-purpose model optimized for high-level multimodal understanding and generation, rather than low-level pixel-wise restoration. It lacks the specialized architectural biases and targeted loss functions that enable baseline models to effectively balance noise removal with detail preservation.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion", "weight": 1.5} -->

Trade-off Between Generative Prior and Pixel Fidelity: As a unified model, Nano Banana Pro prioritizes semantic plausibility and visual coherence over strict pixel-level accuracy. This generative nature often leads to the over-smoothing of high-frequency details in pursuit of "reasonable" content, resulting in inferior quantitative metrics compared to task-specific models trained via strict supervision.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Discussion", "weight": 1.5} -->

In summary, this study evaluated the unified generative model Nano Banana Pro against state-of-the-art specialized models on both synthetic Gaussian noise and real-world blind denoising datasets. Nano Banana Pro significantly underperforms task-specific baselines across all benchmarks, indicating limited competitiveness in direct denoising applications. Direct application of Nano Banana Pro for denoising is not recommended without modification. Enhancing its utility requires targeted adaptations such as prompt engineering, parameter fine-tuning, or integration with post-processing modules. Future research should explore methodologies to align general-purpose generative priors with low-level processing demands.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

To evaluate the performance of Google's Nano Banana Pro model on the SIRR task, we conducted experiments using the model as an off-the-shelf solution via API calls. Given the closed-source nature of the model which precludes task-specific fine-tuning, we adopted a direct inference strategy. Only the raw reflection-contaminated images and task-specific prompts were provided as input, without introducing any additional priors or auxiliary guidance. It is worth noting that the resolution of images generated by Nano Banana Pro is fixed at a scale of approximately 1024 pixels, which differs from the original input dimensions. To ensure the fairness and accuracy of the quantitative evaluation, all output images were resized to match the original resolution of the corresponding ground-truth images before metric calculation.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

For a comprehensive assessment, we adopted three mainstream datasets in the SIRR domain as our evaluation benchmark. Specifically, we utilized \[zhangSingleImageReflection2018\], which contains 20 images from real-world glass reflection scenes; Nature \[liSingleImageReflection2020\], consisting of 20 samples focusing on outdoor natural landscapes; and SIR^2^ \[wanBenchmarkingSingleImageReflection2017\], where we evaluated on its Objects, Postcard, and Wild subsets.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

We compared Nano Banana Pro against 15 state-of-the-art baseline models, including ERRNet \[weiSingleImageReflection2019\], IBCLN \[liSingleImageReflection2020\], YTMT \[huTrashTreasureInteractive2021\], Dong et al. \[dongLocationawareSingleImage2021\], DSRNet \[huSingleImageReflection2023\], RAGNet \[liTwostageSingleImage2023\], RRW \[zhuRevisitingSingleImage2024\], DSIT \[guoSingleImageReflection2024\], RDNet \[zhaoReversibleDecouplingNetwork2025\], F2T2-HiT \[caiF2T2HiTUShapedFFT2025\], Huang et al. \[huangSingleImageReflection2025\], L-DiffER \[hongLDiffERSingleImage2025\], DAI \[huDereflectionAnyImage2025\], Lu et al.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

The evaluation metrics assess both basic image quality and perceptual quality. For pixel-level fidelity, we employed Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM), with comprehensive comparison results summarized in Tab. 8. To better assess visual perception, we further incorporated Multi-Scale Structural Similarity (MS-SSIM) and Learned Perceptual Image Patch Similarity (LPIPS). Note that lower LPIPS values indicate better perceptual quality. For these perceptual metrics, we selected recent SOTA methods for comparison (with baseline data sourced from WindowSeat \[zakarinReflectionRemovalEfficient2025\]), as presented in Tab. 9. All metrics were calculated on the RGB channels between the resized output and the ground truth.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

As shown in Tab. 8, Nano Banana Pro exhibits a notable performance gap compared to state-of-the-art specialist methods. Quantitatively, it lags behind across all datasets in pixel-wise metrics (PSNR/SSIM). This disparity largely stems from the fundamental difference in optimization objectives: regression-based SOTA methods are supervised to minimize pixel-level reconstruction error, ensuring precise alignment. In contrast, the generative approach of Nano Banana Pro prioritizes semantic coherence over structural fidelity, often resulting in global intensity scaling and spatial shifts that heavily penalize PSNR, even if the image content is semantically correct.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Tab. 9 further illustrates the performance in terms of perceptual quality metrics. Despite the generative nature of Nano Banana Pro, which typically favors perceptual scores, it still exhibits high LPIPS values (e.g., 0.2513 on Postcard vs. 0.0549 for SOTA). Unlike PSNR, which penalizes misalignment, the poor LPIPS performance points to a deeper issue: semantic and stylistic deviation. The model tends to perform aggressive \"image-to-image translation\" rather than faithful restoration, altering fundamental scene characteristics---such as modifying illumination, hallucinating textures, or shifting the color domain---thereby drifting away from the ground truth's perceptual manifold.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

From an interpretive perspective, the elevated LPIPS and sub-optimal MS-SSIM scores highlight the limitations of general-purpose generative models in high-fidelity restoration tasks. Although the model possesses strong generative capabilities, it lacks a precise mechanism for decoupling reflection layers from the background. The high LPIPS values suggest a substantial deviation in color distribution, texture details, and high-level semantic features relative to the ground truth. This deviation likely stems from the model partially merging residual reflections into the background or altering the original color and complex textures during the regeneration process. Consequently, while the generated images may appear visually natural, they fail to meet the strict fidelity requirements essential for reflection removal tasks.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

In this section, we conduct a comprehensive qualitative evaluation of the proposed Nano Banana Pro. To establish a comparative baseline, we first benchmark our visual results against existing state-of-the-art methods in Fig. 20. Subsequently, we examine the specific restoration capabilities of our model through selected samples in Fig. 21. Finally, to ensure a balanced assessment and facilitate future improvements, we provide an analysis of the model's limitations by categorizing typical failure cases and degradation patterns in Fig. 22.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

As illustrated in Fig. 20, the proposed Nano Banana Pro exhibits a high variance in performance compared to state-of-the-art methods. In specific instances, our method outperforms existing approaches, yielding results that are visually comparable from the ground truth. However, generally, it lacks the stability of specialized regression-based models. Notably, the model struggles with preserving high-frequency details, leading to the loss of complex textures (e.g., row 1), or suffers from semantic ambiguity where reflection artifacts are erroneously interpreted as background elements and subsequently enhanced (e.g., row 4). These limitations contribute to a lower average performance despite the high perceptual quality in successful cases.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 21 showcases selected samples where Nano Banana Pro demonstrates superior restoration capabilities. It is observed that when there is a significant semantic or visual distinction between the reflection and transmission layers, the model effectively suppresses the reflection while preserving background integrity. The results indicate that the model possesses a high performance upper bound, occasionally achieving reconstruction quality nearly identical to the ground truth. We attribute this potential to the robust generative priors acquired from large-scale pre-training. However, the absence of domain-specific supervision for reflection separation implies a trade-off: without explicit guidance, the model may misapply these priors, failing to disentangle the layers or introducing generative hallucinations and noise into the transmission layer. Experimental results suggest that such misuse of priors accounts for a considerable portion of the suboptimal outputs.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Given the quantitative gap observed in the previous section, explicitly analyzing the failure modes provides critical insights into the misbehavior of generative priors. Based on the distinct characteristics of the introduced artifacts and degradation mechanisms, the suboptimal performance of Nano Banana Pro can be systematically categorized into six types, as visualized in Fig. 22.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

\(a\) Incomplete Reflection Removal. In these instances, the model fails to effectively decouple the reflection layer from the transmission layer, resulting in significant residual artifacts. This behavior likely stems from a conservative inference strategy induced by prompts emphasizing background preservation. When the reflection intensity is high or statistically similar to the background, the model tends to classify the reflection as intrinsic scene content to avoid over-erasing potential background details.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

\(b\) Erroneous Enhancement due to Semantic Ambiguity. Despite explicit instructions to suppress reflections, the model occasionally misinterprets reflection artifacts as valid background elements and erroneously enhances them. This phenomenon highlights a limitation in current generative priors: the model is driven by semantic plausibility rather than physical layer separation. When a reflection (e.g., a light source or architectural reflection) aligns semantically with the background scene, the model prioritizes generating a \"coherent\" image without contradictions, thereby integrating the artifact as a strengthened feature.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

\(c\) Unintended Chromatic and Domain Shift. This error is predominantly observed in the Postcard dataset, which features images of paintings or prints (e.g., urban or humanist subjects). The model struggles with domain ambiguity, failing to distinguish between a \"picture of a scene\" and a \"real-world scene.\" Consequently, it attempts to \"restore\" the printed content as a realistic photograph, aggressively altering saturation, removing characteristic grain, or modifying illumination. This results in severe color deviations and stylistic inconsistencies compared to the ground truth.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

\(d\) Texture Fidelity Loss. In scenarios containing high-frequency details, such as natural foliage or fabric textures (e.g., towels), the generative process often fails to maintain the original texture distribution. The output tends to exhibit either unnatural over-smoothing (loss of fine grain) or artificial sharpening (introduction of high-frequency noise), indicating a lack of fine-grained control in the texture reconstruction module.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

\(e\) Structural Hallucination and Deformation. In rare but severe cases, the model breaks structural consistency, generating outputs that deviate geometrically from the input. This includes the hallucination of non-existent background structures or the removal of actual objects mistaken for reflections. Such failures represent a collapse of the conditioning mechanism, where the strong generative prior overrides the spatial constraints provided by the input image.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

\(f\) Compound Degradation. A significant portion of low-scoring results exhibits a hybrid of the aforementioned failure modes. For example, an image may suffer from incomplete reflection removal while simultaneously undergoing a global color shift, or experience structural deformation alongside texture smoothing. These complex scenarios represent the most challenging cases for the current architecture.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

To comprehensively assess the capabilities of Nano Banana Pro, we organized our experiments into quantitative evaluation and qualitative analysis.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

Quantitative Evaluation. We first evaluated the model on the Flare7K++ dataset configured to an output resolution of 1K. Performance was measured using Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM) \[wang2004image\]. As shown in Tab. 10, we compared Nano Banana Pro against state-of-the-art methods trained on the same dataset, including Restormer \[zamir2022restormer\], Uformer \[wang2022uformer\], and DeflareMamba \[Huang2025DeflareMamba\]. Subsequently, we extended our evaluation to the FlareReal600 dataset, processing images at their native resolutions to output 2K and 4K results. In addition to PSNR and SSIM, Learned Perceptual Image Patch Similarity (LPIPS) \[zhang2018unreasonable\] was included to assess perceptual quality. Tab. 11 benchmarks our results against the MIPI 2024 Challenge champion, MiAlgo AI. Note that while the challenge metrics were derived from an unpublished test set, our evaluation utilized the publicly available validation set.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

We observed two notable quantitative trends: 1) Resolution Impact: Performance metrics generally decline as output resolution increases. 2) Brightness Sensitivity: On the high-resolution FlareReal600 dataset, higher image brightness results in degraded metrics. However, this trend is not evident in the lower-resolution Flare7K++ dataset.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

Qualitative Analysis. Visual comparisons in Fig.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

1\. Visual Superiority vs. Stochastic Instability: On optimal inputs, Nano Banana Pro demonstrates exceptional deflaring capabilities, often surpassing SOTA methods in detail restoration. However, this advantage is compromised by the inherent stochasticity of diffusion models. The model exhibits significant variance and is prone to semantic hallucinations---such as generating unrelated content, suppressing valid light sources, or erroneously illuminating inactive bulbs. While prompt engineering offers partial mitigation, it fails to guarantee the deterministic reliability required for industrial deployment.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

2\. Perceptual-Metric Misalignment: As illustrated in Fig. 24, we observe a notable divergence between quantitative metrics and perceptual quality. Instances with low scores sometimes retain high visual fidelity, suggesting that pixel-level metrics may not fully capture the perceptual advantages of generative reconstruction.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

In conclusion, Nano Banana Pro exhibits a "high ceiling, low floor" characteristic. While it possesses the generative potential to outperform traditional regression-based methods in perceptual quality, it currently sacrifices the stability and consistency essential for robust image restoration.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Datasets. We conduct experiments on three established low-light enhancement benchmarks. LOLv1 \[lolv1\] contains 485 training pairs and 15 testing pairs of real-world low-light and normal-light images captured by adjusting camera exposure time and ISO. LOLv2-real \[lolv2\] extends this with 689 training pairs and 100 testing pairs, featuring more diverse indoor and outdoor scenes. SICE \[sice\] is a larger-scale dataset containing multi-exposure sequences, from which low-light and reference pairs are constructed; its test set comprises a more diverse range of scenes and illumination conditions.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Evaluation Metrics. we adopt two standard full-reference image quality metrics: Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM). Higher values indicate better reconstruction quality relative to the ground-truth normal-light images.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Comparison Methods. We compare Nano Banana Pro against several representative low-light enhancement methods spanning different paradigms: ZeroDCE \[zerodce\] (zero-reference learning), RUAS \[ruas\] (architecture search-based), LLFlow \[llflow\](normalizing flow-based), LLFormer \[llformer\] (transformer-based), GSAD \[GSAD\] (diffusion-based), and Quadprior \[quadprior\] (diffusion prior-based). These methods represent the current state of the art in supervised and unsupervised low-light enhancement.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

Nano Banana Pro Configuration. Nano Banana Pro is evaluated in a zero-shot setting without any fine-tuning on low-light enhancement data \[lolv1, lolv2, sice\]. We provide the model with the following natural language instruction: "This is a low-light image, please turn this image into a normal image while keeping other elements unchanged." No additional inference-time configurations or post-processing steps are applied.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

Tab. 12 presents the quantitative comparison across all three benchmarks. On LOLv1 \[lolv1\] and LOLv2-real \[lolv2\], Nano Banana Pro's zero-shot performance falls considerably short of the state-of-the-art supervised methods. The gap is particularly pronounced on LOLv2-real \[lolv2\], where the PSNR of 15.661 dB and SSIM of 0.537 lag behind leading methods by a substantial margin. This suggests that without task-specific training, the model struggles to consistently produce enhancements that align with the ground-truth references in these benchmarks. Interestingly, on the SICE \[sice\] dataset, Nano Banana Pro achieves slightly higher metrics than several comparison methods, demonstrating competitive zero-shot performance on this more challenging and diverse benchmark.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Qualitative and Quantitative Results", "weight": 1.0} -->

Fig. 25 presents representative visual comparisons across these three datasets \[lolv1, lolv2, sice\]. Nano Banana Pro produces visually reasonable enhancements in many cases, successfully brightening dark regions and revealing scene content. However, the model exhibits inconsistent brightness control: in the first row, it tends to overexpose bright regions, while in others, it insufficiently enhances dark areas, leaving the output still underexposed. This inconsistency likely stems from the model's reliance on general visual priors rather than explicit illumination modeling. Notably, Nano Banana Pro does not introduce visible artifacts such as color distortion, halo effects, or structural corruption, which is a common failure mode of some enhancement methods. Texture preservation remains comparable to other approaches, with fine details in enhanced regions generally retained. The absence of artifacts suggests that the model's generative capabilities are well-regularized, even when applied to out-of-distribution tasks like low-light enhancement.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Analysis", "weight": 1.0} -->

The evaluation results reveal a nuanced picture of Nano Banana Pro's zero-shot capabilities for low-light image enhancement. In this section, we provide an in-depth analysis of the observed performance patterns, examine potential underlying causes, and discuss broader implications for applying unified multimodal models to image restoration tasks. A notable positive finding is that Nano Banana Pro does not introduce visible artifacts such as color distortion, halo effects around high-contrast edges, amplified noise, or structural corruption. This is significant because artifact introduction is a common failure mode of enhancement methods, particularly those based on generative models. The absence of artifacts may partially explain the moderate PSNR/SSIM scores. More aggressive enhancement methods might achieve higher metrics on average by pushing brightness and contrast more strongly, but at the cost of occasional artifacts. Nano Banana Pro's conservative approach avoids such failures but may sacrifice peak performance. For practical applications where artifact-free outputs are critical, this trade-off may be acceptable. However, the performance gap on standard benchmarks indicates that zero-shot application is not yet competitive with task-specific methods. The lack of explicit illumination modeling, sensitivity to prompt formulation, and inability to match benchmark-specific ground-truth definitions all limit current performance.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Analysis", "weight": 1.0} -->

Several avenues could potentially improve performance: 1) prompt engineering to provide more specific enhancement guidance; 2) few-shot learning with example image pairs to calibrate the model's enhancement behavior; 3) lightweight fine-tuning or adapter-based adaptation to inject task-specific knowledge while preserving general capabilities; and 4) hybrid approaches that combine unified models' semantic understanding with task-specific enhancement modules.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

We conducted experiments using the Nano Banana Pro model configured to output 1K resolution across three datasets, quantitatively evaluating underwater image enhancement performance through reference-free metrics. The Underwater Image Quality Measure (UIQM) \[panetta2015hvsunderwater\] comprehensively quantifies underwater image quality by integrating color richness, sharpness, and contrast. Underwater Color Image Quality Evaluation (UCIQE) \[yang2015underwatercolor\] addresses non-uniform color shifts and low contrast in underwater scenes by evaluating quality across standard deviation, luminance contrast, and saturation mean dimensions. Both metrics adapt to real-world unreferenced scenarios without requiring reference images. Results were compared against UWCNN \[li2019underwater\], UIEC²-Net \[wang2021uiec2net\], U-Shape \[peng2023ushapetransformer\], PUGAN \[cong2023pugan\], DM-water \[tang2023transformerdiffusion\], and WF-Diff \[zhao2024wfdiff\]. Relevant details are summarized in Tab. 13.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

NB Pro demonstrates competitiveness on underwater image reference-free evaluation metrics UIQM and UCIQE that rivals existing mainstream UIE methods. On the UIEB dataset, NB Pro's gap with optimal results in reference-free metrics is relatively small. On the larger-scale LSUI dataset with more complex degradation scenarios, NB Pro achieves top performance in both UIQM and UCIQE metrics, fully validating its robustness in challenging environments. On the reference-free dataset U45, NB Pro achieves the best UIQM score and ranks third in UCIQE, demonstrating its practical value in real-world reference-free scenarios.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

To intuitively present the underwater image enhancement outcomes of the Nano Banana (NB) Pro model, we provide visualizations of its processing results across the UIEB, LSUI, and U45 datasets, with comparisons to state-of-the-art baseline methods. Fig. 26 displays the visualization of exemplary cases for NB Pro in underwater image enhancement tasks on the UIEB and LSUI datasets. Fig. 27 presents the visualization of failed cases for NB Pro in underwater image enhancement tasks on the UIEB and LSUI datasets. Fig. 28 shows the visual comparison of processing results between NB Pro and other mainstream underwater image enhancement methods on the reference-free U45 dataset.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Qualitative experimental results demonstrate that for extreme degradation scenarios such as severe green color bias, severe blue color bias, insufficient illumination, and high turbidity, NB Pro can generate high-quality enhanced results without relying on GT images from paired training data. Even in scenarios with multiple severe degradations overlapping, its output images exhibit superior visual quality compared to GT images (as shown in Fig. 26). However, in mildly degraded scenarios with weaker color shifts, NB Pro struggles to effectively identify degradation features. The generated enhanced images exhibit minimal differences from the input images, resulting in visual quality inferior to GT images and failing to fully meet the core objective of underwater image enhancement (as shown in Fig. 27).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

This conclusion is further validated by visualization results from the reference-free dataset U45 (Fig. 28): In the first row depicting a diver scene with high turbidity and severe green color cast degradation, NB Pro's enhancement significantly outperforms other comparison methods, completely eliminating the color cast while removing foggy blur; In the second row of underwater scenes with blue color cast, NB Pro also performed comparably to existing mainstream methods; however, in the third row of slightly degraded underwater plant scenes, NB Pro's restoration results were relatively poor among all comparison methods, failing to effectively optimize image details and contrast.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Analyses", "weight": 1.0} -->

This study conducted a comprehensive evaluation across multiple benchmark datasets representing both synthetic and real underwater environments. Results demonstrate that NB Pro offers a unique paradigm for underwater image enhancement. Its core characteristic is a distinct trade-off between robust perceptual recovery in complex environments and precise pixel-level fidelity in benign conditions.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Analyses", "weight": 1.0} -->

Quantitative analysis demonstrates that NB Pro excels in the absence of reference images, achieving state-of-the-art results on large-scale complex datasets like LSUI and real-world datasets such as U45. This indicates that when confronted with severely degraded images, the model efficiently generates images with perceptual clarity, rich color saturation, and optimal contrast. Existing underwater ground truth images often exhibit residual degradation or artifacts. NB Pro's generative freedom enables it to surpass the visual quality of these reference images, consistent with its performance in the no-reference evaluation.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Analyses", "weight": 1.0} -->

From a qualitative perspective, NB Pro demonstrates unique strengths in handling extremely degraded scenarios. Visual examples prove that NB Pro can successfully reconstruct scenes severely affected by green/blue color casts, low light, and high turbidity. It can simultaneously synthesize clear details and correct severe color shifts, sometimes producing results that visually outperform the ground truth images. This indicates NB Pro possesses a strong understanding of underwater degradation and the potential to reverse such degradation.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Analyses", "weight": 1.0} -->

Despite these strengths in high-intensity restoration tasks, the model exhibits instability in mildly degraded scenarios. For scenes with only slight color shifts or minor turbidity, its enhancement effects are suboptimal, reflecting NB Pro's sensitivity limitations. When degradation signals are weak, the model struggles to identify or localize degraded features, failing to trigger necessary optimizations for fine details and contrast. Future research should focus on enhancing NB Pro's adaptability across the full spectrum of degradation levels. This will ensure it achieves both refined enhancement in mildly blurred environments and thorough reconstruction in severely degraded scenarios, delivering outstanding results in both cases.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

To comprehensively evaluate Nano Banana Pro's performance in HDR tasks, we quantitatively compared it against a range of advanced traditional and deep learning-based image enhancement methods. To ensure fair comparison, all images were downsampled to 480p resolution for evaluation. We employed four standard metrics: PSNR and SSIM to evaluate perceptual similarity, LPIPS to assess visual similarity, and $\bigtriangleupE$ to quantify color differences. Results are shown in Tab. 14. NB Pro significantly underperformed against the comparison methods. On the HDR+ dataset, NB Pro achieved lower PSNR and SSIM than the optimal method, while also exhibiting poorer LPIPS and $\bigtriangleupE$ values. On the MIT-FiveK dataset, although its PSNR and SSIM improved, they still lagged significantly behind the optimal method. This result clearly indicates that under the standard full-reference evaluation framework, which prioritizes pixel-level accurate reconstruction and color fidelity, NB Pro's generated results exhibit systematic deviations from professionally enhanced or color-graded reference images.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

NB Pro fundamentally differs from traditional HDR/enhancement models optimized for specific imaging scenarios. The latter typically undergo end-to-end training directly on paired LDR-reference images, targeting minimization of pixel-level loss, thus inherently excelling in metrics like PSNR and SSIM. In contrast, NB Pro's generation process prioritizes semantic coherence and overall visual appeal. Its outputs can be viewed as reconstructions of the input image rather than strict pixel-to-pixel mappings. Consequently, generated images may exhibit deviations in luminance distribution, local contrast, and even color style compared to reference images, leading to comprehensive score reductions across full-reference metrics. Notably, on the LPIPS metric, NB Pro's performance on the MIT-FiveK dataset remains behind but shows a narrowed gap compared to pixel-level metrics. This suggests its outputs may retain some similarity to reference images at higher-level semantic features, while low-level pixel arrangements have been significantly altered.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

To visually evaluate the performance and potential limitations of NB Pro in HDR imaging tasks, this study conducted qualitative visualization experiments using representative scenes from the HDR+ and MIT-FiveK datasets. The experiments cover three core scenarios: conventional lighting, low-light with minimal detail, and complex dense textures. The corresponding results are presented in Fig. 29, Fig. 30, and Fig. 31, respectively.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 29 presents an illustrative case of NB Pro in HDR imaging tasks. Comparing the low-dynamic-range input image, the true high-dynamic-range reference image, and the NB Pro generated result reveals that in conventionally lit scenes, such as moderately bright indoor settings or outdoor natural light environments, NB Pro effectively restores the scene's dynamic range and color gradation. The overall visual quality of the generated result approaches or even rivals the reference image, fully validating the model's effectiveness in fundamental HDR imaging tasks.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 30 further highlights texture anomalies in low-light, low-detail scenarios. When input low-dynamic-range images contain severe shadow areas with inherently weak texture or detail information, NB Pro tends to exhibit two typical defects. One type involves detail loss, such as in the third case where the model's output lacks the wall tile texture and sofa outline in the shadow regions of the input image. The second involves artificially redundant additions, such as the extra cookie surface texture generated in the first case that did not exist in the original scene. The second case failed to restore the vegetables' original colors and applied redundant diffuse rendering to the green spots. The fourth case generated mountain elements out of thin air in the house background. These issues stem from insufficient detail features in low-light scenes, causing the model's texture perception and generation logic to deviate, ultimately reducing detail restoration accuracy.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 31 shows evaluation results for complex, densely textured scenes. When input images contain fine, dense textures---such as fabric patterns, intricate vegetation textures, or architectural wall textures---NB Pro struggles to precisely balance texture preservation and enhancement scales. Generated results commonly exhibit visual artifacts from excessive sharpening, overly pronounced texture edges, localized artifacts, and even masking of the original texture's natural gradations. This phenomenon reflects the model's ongoing limitations in perceiving fine textures and controlling enhancement. In summary, qualitative experiments indicate that NB Pro delivers satisfactory visual effects in standard HDR imaging scenarios. However, in low-light, low-detail environments, the model tends to suffer from texture loss or redundant additions. In complex, densely textured scenes, the model exhibits a tendency toward excessive sharpening.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Analyses", "weight": 1.0} -->

The quantitative and qualitative evaluation results systematically reveal the comprehensive performance characteristics of NB Pro in HDR imaging tasks. Quantitatively, the model significantly lags behind mainstream HDR reconstruction methods in all reference evaluation metrics during 480p resolution tests on the HDR+ and MIT-FiveK datasets. However, the gap narrows for the LPIPS metric on the MIT-FiveK dataset, indicating that while its generated results exhibit significant pixel-level deviations, they maintain a degree of semantic consistency with reference images. Qualitatively, NB Pro achieves acceptable visual results in standard-illumination HDR scenes. However, it exhibits pronounced limitations in two typical scenarios: low-light environments with sparse details and complex, densely textured scenes. Specific issues include texture information loss, artificial redundant detail generation, color distortion, and over-sharpening artifacts.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Analyses", "weight": 1.0} -->

The evaluation results clearly reveal three core deficiencies of NB Pro when applied to HDR imaging tasks: First, in low-light, low-detail scenes, the model exhibits weaknesses in perceiving and accurately restoring subtle texture features in shadow areas. The weak feature signals in these input shadows struggle to support precise reconstruction, leading to either the omission of shadow texture information or the generation of artificial redundant detail fill. Second, for fine-grained texture scenarios like fabric weaves and dense vegetation patterns, the model lacks adaptive control over texture preservation and enhancement scales. Over-sharpening not only disrupts natural texture gradation but also readily induces edge artifacts. Third, the model's color rendering mechanism lacks strong constraints on reference color distributions. In complex color scenes, it prioritizes visual harmony over precise target color reproduction, ultimately causing color distortion. Comprehensive experimental results indicate that NB Pro is only suitable for non-critical HDR imaging scenarios where pixel-level precision is less demanding and visual experience is paramount. It is unsuitable for safety-critical or professional-grade applications requiring stringent detail and color restoration accuracy.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Analyses", "weight": 1.0} -->

Issues such as texture loss, artificial redundant details, and color distortion may cause scene analysis bias or decision misjudgment, failing to meet the core requirements of such scenarios.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the computer vision and digital photography, acquiring fully clear images is crucial for subsequent analysis and processing. However, due to the limited depth of field (DoF) of camera lenses, a single shot cannot concurrently focus on all the objects at varying depths. Multi-focus image fusion (MFIF) provides an effective solution to this challenge, aiming to generate an AIF output from multiple images of the same scene with different focal points. This technique has found significant applications in various fields such as medical diagnosis and consumer electronics.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, deep learning has been widely applied to MFIF, typically falling into two categories: decision-based and reconstruction-based approaches. Decision-based methods learn a decision map by classifying pixels in the source images as either in-focus or out-of-focus, and then select the appropriate pixel to assemble the final composite \[liu2017multi, li2020drpl, xiao2021dtmnet\]. Reconstruction-based methods employ end-to-end networks to directly extract features from source images and reconstruct the all-in-focus output \[zhang2020ifcnn, ma2022swinfusion, li2024fusiondiff\]. However, the former methods normally struggle with focused-defocused boundaries whose focus attributes are ambiguous to distinguish, while the letter ones often suffer from detail loss in other regions away from the boundaries.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, the rapid advancement of Generative Artificial Intelligence has opened new avenues for MFIF. Generative models learn the distribution from massive datasets, enabling them to understand and generate complex visual content and structures. Despite the potential for creative fusion, their application in pixel-precise tasks like MFIF remains under-explored. There is a critical need to verify whether a model designed for creativity can adhere to the strict fidelity requirements of fusion tasks without introducing hallucinations or losing spectral information. This report evaluates the performance of the newest generative model Nano Banana Pro in the task of MFIF, comparing its fusion quality with existing baseline methods using various metrics. The results aim to provide insights into its strengths and limitations in real-world applications.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

We evaluate the performance of MFIF on four benchmark: Lytro \[nejati2015multi\], MFFW \[xu2020mffw\], MFI-WHU \[zhang2021mff\] and SIMIF \[chun2025multi\]. The Lytro dataset contains 20 pairs of multi-focus images captured by a light field camera. The MFFW dataset includes 13 real image pairs with strong Defocus Spread Effect (DSE). The MFI-WHU dataset is constructed using Gaussian blur and decision maps, consists of a larger scale with 120 pairs. The SIMIF dataset is composed of 12 pairs of high-resolution images.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Six popular objective metrics are employed for evaluation, including non-reference metrics, $EN$ \[jahne2005digital\], $AG$ \[cui2015detail\], $SF$ \[zheng2007new\], and Source-reference metrics $NMI$ \[hossny2008comments\], $Q_{Y}$ \[yang2008novel\], $Q_{CB}$ \[chen2009new\]. These datasets and metrics provide a comprehensive assessment from multiple perspectives.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

We compare the Nano Banana Pro (NB Pro) with 10 other state-of-the-art and representative MFIF methods, where ZMFF is a Zero-shot method, IFCNN and MUFusion are unsupervised methods, and the rest are supervised methods. According to the comparison results shown in the Tab. 32 and Tab. 33, NB Pro performs exceptionally well on non-reference metrics, achieving results that are close to or even surpassing the current state-of-the-art, indicating the high quality of the generated images themselves. Conversely, on source-reference metrics, NB Pro shows poorer performance, meeting the similar dilemma faced by previous Zero-shot and unsupervised methods. This indicates that during the fusion process, the model failed to adequately preserve consistency between the generated image and the source images in terms of aspects like gradients and structure; it exhibits excessive creativity at the expense of fidelity.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 32 illustrates a visualization of the fusion results generated by the Nano Banana Pro. The fusion performance varies across different samples, with some being successful and others subpar. For instance, the first example in the first row showcases a favorable fusion result, where the fused image not only preserves the focused foreground person and the background golf course from the source images but also achieves a seamless transition between different regions, effectively avoiding artifacts. Notably, it even recovers richer details in the lawn area---which originally had limited clarity---thereby enhancing the overall visual quality. Conversely, limitations are observed in some other cases. Specifically, in the second sample of the second row, the white petals at the base of the foreground plant remain blurred. Similarly, in the second sample of the third row, the grass in the bottom-right corner is still defocused. Given that sharp counterparts for these regions exist in the source images, this indicates that the model failed to correctly identify or localize the optimal in-focus regions during the fusion process.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

To more intuitively verify the capability of NB Pro, Fig. 33 and Fig. 34 compares the fusion results against state-of-the-art MFIF approaches. In the 'lock' example, NB Pro achieves remarkably smooth transitions across regions without introducing artifacts near the lock head, while producing even sharper details on the house wall that was already in focus in the source images. In the 'coffee cup' example, due to the spread effect caused by defocus, some methods generate artifacts at the boundary between the two cup rims, and others produce dark ghosting along the cup wall. In contrast, NB Pro effectively overcomes these issues and delivers a visually pleasing fusion result.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Analyses", "weight": 1.0} -->

This comprehensive evaluation, conducted across four diverse benchmarks and benchmarked against ten state-of-the-art methods, establishes NB Pro as a paradigm shift in Multi-Focus Image Fusion. The results characterize a distinct trade-off between perceptual quality and signal fidelity.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Analyses", "weight": 1.0} -->

Quantitative analysis reveals a significant performance divergence. NB Pro excels in non-reference metrics, generating images with exceptional clarity, textural richness, and visual appeal. Conversely, its performance on source-reference metrics uncovers a critical limitation inherent to zero-shot generative approaches: the prioritization of generative freedom over strict pixel-level adherence to source inputs. While the model can hallucinate plausible high-frequency details (e.g., enhancing lawn textures), it occasionally alters gradients or structures that require preservation.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Analyses", "weight": 1.0} -->

This quantitative discrepancy stems from the fundamental conflict between the strict consistency required by traditional fusion tasks and the stochastic nature of generative models. First, despite prompt-based constraints, the model's high degree of freedom can lead to semantic alterations in regions that should be preserved. Second, source images are rarely perfect; NB Pro often performs generative enhancement (e.g., super-resolution or denoising) to supplement details. However, traditional reference-based metrics penalize these visual improvements as errors because they deviate from the imperfect source.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Analyses", "weight": 1.0} -->

Qualitatively, NB Pro demonstrates superior capability in handling complex scenarios, particularly those affected by the Defocus Spread Effect. By effectively mitigating boundary artifacts, dark ghosting, and unnatural transitions common in traditional algorithms, the model showcases a superior semantic understanding of scene structure.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Analyses", "weight": 1.0} -->

Despite these strengths, instability in focus detection remains a challenge; the model occasionally blurs clear regions, suggesting failures in the attention mechanism's pixel localization. Ultimately, the misalignment between visual superiority and metric penalties suggests that current evaluation frameworks are insufficient for Generative AI. Future work must focus on better constraining the generative process and developing novel metrics capable of distinguishing between hallucinatory errors and generative enhancements.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the field of modern computer vision, multi-modal image fusion technology plays an increasingly critical role. Infrared-Visible Image Fusion (IVIF) aims to synergize the thermal radiation information from infrared images with the texture details and color information from visible images. Infrared sensors capture thermal signatures of objects and are robust against varying lighting conditions and adverse weather (such as smoke or darkness), effectively highlighting targets. Conversely, visible light sensors provide rich high-frequency details and scene descriptions that align with human visual perception. By fusing these two complementary modalities, the resulting images not only possess all-weather scene perception capabilities but also significantly enhance the accuracy and robustness of target detection, autonomous driving navigation, and security surveillance systems.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional IVIF methods (such as multi-scale transform \[liu2015general\] and sparse representation \[li2019discriminative\]) often struggle to balance the saliency of thermal targets with the fidelity of background textures, frequently resulting in artificial artifacts. In recent years, deep learning-based methods (such as CNNs \[tang2022learning, ma2020infrared, zhao2021efficient\], GANs \[ma2019fusiongan, ma2020ddcgan, li2020attentionfgan\]) and transformers \[wang2022swinfuse, vs2022image, li2022cgtf\] have achieved performance breakthroughs but still face challenges in cross-modal feature alignment and detail preservation. With the explosion of generative AI technologies, particularly Diffusion Models, image generation quality has reached unprecedented heights. However, existing high-compute models are often bulky and difficult to run in real-time on edge devices. Furthermore, balancing generative quality with physical fidelity in fusion tasks under specific physical constraints remains a pressing problem.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Introduction", "weight": 1.5} -->

Against this backdrop, Google's newly released Nano Banana Pro has garnered widespread attention in the industry. Nano Banana Pro employs optimized Latent Diffusion technology and efficient attention mechanisms, specifically designed to handle high dynamic range and multi-modal inputs. Its uniqueness lies in its ability to understand semantic context more precisely, suggesting that in image fusion tasks, it may preserve the edge information of infrared thermal sources more effectively than its predecessors while naturally integrating visible textures.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although Nano Banana Pro has demonstrated impressive performance in general image generation, its effectiveness in the specific scientific task of Infrared-Visible Image Fusion has not yet been systematically verified. This report aims to bridge this gap by comprehensively evaluating the actual performance of Nano Banana Pro in IVIF tasks through qualitative analysis (visual effects) and quantitative assessment. We will focus on examining its fusion quality, noise control capabilities, and inference efficiency across various lighting scenarios to assess its potential as a foundation model for next-generation image fusion.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

Following \[zhao2024equivariant\], we conduct experiments on three mainstream benchmarks: MSRS \[tang2022piafusion\], RoadScene \[xu2020fusiondn\] and M^3^FD \[liu2022target\] datasets, and leverage six popular metrics for assignment, including non-reference metrics $EN$, $SD$, $SF$, $AG$ and source-reference metrics $SCD$, $VIF$. We compare the fusion results of Nano Banana Pro (NB Pro) with 10 other state-of-the-art and representative IVIF methods, where SDNet and DeFusion are CNN-based methods, TarDAL is a GAN-based method, CDDFuse is a CNN-transfomer hybrid method, DDFM is a diffusion-based and training-free method, and the remaining ones are model or task driven approaches.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

As shown in Tab. 17, the results demonstrate that NB Pro exhibits overwhelming superiority in non-reference metrics representing image information content and texture details, particularly on the MSRS and RoadScene datasets. On the MSRS dataset, NB Pro secures the top rank in all four of these metrics. Notably, its $EN$ reaches 6.85 and $AG$ hits 4.56, significantly surpassing the runner-up. On the RoadScene dataset, this advantage is even more pronounced. NB Pro achieves an $SF$ score of 21.81, outperforming the nearest competitor (EMMA, 15.21) by nearly 43%. This indicates that the fused images generated by NB Pro possess extremely high clarity and contrast. It is capable of mining and reconstructing rich high-frequency edge information from source images, attributing to the acute capability of its powerful generative architecture in capturing latent features.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

However, we also observe an intriguing phenomenon: while NB Pro leads by a wide margin in detail metrics, it scores relatively lower in source-reference metrics, specifically $SCD$ and $VIF$. For instance, on the MSRS dataset, its $VIF$ is only 0.58, and and it drops to 0.38 on M^3^FD. This reflects the inherent characteristic of generative models: while the model dramatically enhances texture and human-perceived sharpness, this reconstruction process may introduce stylized features or pixel-level deviations not present in the source images, leading to reduced correlation with the original infrared/visible inputs. In contrast, traditional methods, while not as sharp as NB Pro, demonstrate more robustness in maintaining original pixel fidelity.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Quantitative Results", "weight": 1.0} -->

NB Pro's performance varies across different scenarios. It performs best on MSRS (often containing night-time and complex lighting scenes) and RoadScene, suggesting its proficiency in handling high dynamic range scenes requiring edge enhancement. On the M^3^FD dataset, although it maintains the second-best score in $SD$(43.44), its overall dominance is less distinct compared to the other two datasets. This implies there may still be room for parameter fine-tuning in specific types of multi-modal target detection scenarios.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

While NB Pro yields impressive fusion results in most scenarios, certain limitations persist. To intuitively demonstrate the perceptual quality of the fused images, Fig. 35 presents qualitative results on the MSRS dataset. As illustrated in the first row, the method effectively handles extreme lighting conditions. It accurately captures pedestrian targets hidden in low-light regions of the visible spectrum, establishing sharp contours for thermal targets while enhancing overall background illumination. Simultaneously, it restores clear details and textures in over-exposed areas, such as those adjacent to vehicle headlights. However, suboptimal cases are observed in the second row. Although the thermal targets remain highlighted, the first sample exhibits excessive sharpening of the building structure, leading to slight over-exposure. In the second example, a distinct halo effect emerges around the pedestrian, manifesting as unnatural bright fringes surrounding the thermal target.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 36 further visualize the fusion performance on the other two datasets. In general, NB Pro demonstrates superior performance in terms of overall visual quality and realism, excelling in infrared target recovery and background texture reconstruction. Nevertheless, deficiencies persist in certain fine-grained details. The model may occasionally fail to faithfully utilize and preserve the source information, leading to the introduction of unnatural hallucinations or artifacts.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Analyses", "weight": 1.0} -->

This report presents a comprehensive evaluation of Google's Nano Banana Pro in Infrared-Visible Image Fusion.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Analyses", "weight": 1.0} -->

On one hand, leveraging powerful generative priors, NB Pro demonstrates overwhelming superiority in non-reference metrics. It successfully circumvents the bottlenecks of traditional methods regarding night-time enhancement and texture reconstruction, yielding fused images of exceptional contrast and clarity. On the other hand, this aggressive generation strategy incurs a fidelity cost. Lower scores in source consistency metrics, combined with qualitative artifacts such as excessive sharpening and halo effects, indicate that the model sacrifices pixel-level fidelity to the original physical signals in exchange for perceptual appeal.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Analyses", "weight": 1.0} -->

Traditional methods fundamentally operate as signal processing routines aiming to preserve pixel intensity. However, NB Pro introduces a paradigm of semantic generation. Rather than merely superimposing pixels, it interprets the scene context to re-synthesize the image. This explains its capability to recover astonishing details alongside its propensity for hallucinations. Future research must focus on integrating physical constraints, enforcing strict adherence to thermal distribution laws while exploiting generative capabilities.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Analyses", "weight": 1.0} -->

While visually striking, NB Pro's outputs raise concerns for safety-critical applications like autonomous driving. Perceptual pleasantness does not equate to operational reliability. Artifacts or over-sharpening can trigger false positives in detection algorithms or obscure small targets. Consequently, evaluation standards must evolve beyond visual quality to include Machine Perception Metrics, directly validating the utility of fused images on downstream tasks.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Analyses", "weight": 1.0} -->

Our findings highlight the insufficiency of the current evaluation framework. Metrics like SCD and VIF, which penalize pixel-level misalignment, are overly rigid for generative models. As Generative AI becomes prevalent, there is an imperative need for novel No-Reference Image Quality Assessment metrics that prioritize semantic consistency and naturalness over strict pixel-wise alignment.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Discussion", "weight": 1.5} -->

This comprehensive empirical study, through systematic zero-shot evaluation across 14 diverse low-level vision tasks, elucidates the dual nature of Nano Banana Pro as a generalist generative model: it excels in perceptual quality but lags significantly in traditional pixel-fidelity metrics. This core finding not only quantifies the current capabilities of large-scale generative models within the low-level vision domain but also prompts profound reflections on task definitions, evaluation paradigms, and future model evolution.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Generative vs. Regression Paradigms", "weight": 1.0} -->

Our work highlights intrinsic difference between generative and traditional low-level vision models. Traditional methods predominantly follow a regression paradigm. They learn a deterministic mapping from degraded inputs to clean references via pixel-level supervision, aligning their optimization objective directly with metrics like PSNR and SSIM. In contrast, Nano Banana Pro embodies a generative paradigm. Its training core involves learning the joint distribution of large-scale image data and performing conditional synthesis based on semantic priors. Its goal is to produce plausible and visually pleasing images, not to achieve pixel-wise alignment with a specific reference. Consequently, in regions with severe information loss, traditional methods, constrained by input information, often yield blurry or insipid results. The generative model, however, can leverage its robust world knowledge to hallucinate plausible details, leading to subjectively superior outputs that constitute a deviation from the canonical ground truth.

<!-- chunk {"id": "body-0173", "role": "body", "section": "The Potential Misguidance of Traditional Metrics", "weight": 1.0} -->

Our results strongly challenge the universal applicability of full-reference metrics (e.g., PSNR, SSIM), which are predominant in current low-level vision research. These pixel-difference-based metrics carry a strong implicit assumption: the existence of a single, pixel-perfect ground truth.

<!-- chunk {"id": "body-0174", "role": "body", "section": "The Potential Misguidance of Traditional Metrics", "weight": 1.0} -->

Ground truth is not the unique optimum for generative repair. For regions with catastrophic information loss, multiple visually plausible and contextually correct reconstructions may exist. A generative model provides one such possibility, yet it is penalized by the metric as incorrect.

<!-- chunk {"id": "body-0175", "role": "body", "section": "The Potential Misguidance of Traditional Metrics", "weight": 1.0} -->

The metrics are misaligned with human perception. As shown in previous sections, Nano Banana Pro achieves excellent scores on No-Reference perceptual metrics (e.g., NIQE, NIMA), often surpassing specialized models. This indicates its outputs possess superior statistical naturalness and aesthetic appeal. The drop in PSNR can sometimes be attributed solely to the model's reasonable global color adjustment, mild denoising, or detail enhancement, which are improvements that are paradoxically penalized.

<!-- chunk {"id": "body-0176", "role": "body", "section": "The Potential Misguidance of Traditional Metrics", "weight": 1.0} -->

The quality of dataset ground truth itself. Ground truth images in many real-world datasets contain residual noise, slight blur, or imperfect color balance. A generative model producing a cleaner version constitutes a perceptual enhancement but is scored as a fidelity loss.

<!-- chunk {"id": "body-0177", "role": "body", "section": "The Potential Misguidance of Traditional Metrics", "weight": 1.0} -->

Therefore, judging generative low-level vision models solely by traditional metrics may be both unfair and misleading. This calls for the community to establish a new generation of evaluation frameworks.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Operational Scope and Limitations of Nano Banana Pro", "weight": 1.0} -->

Our evaluation clearly defines the scope of Nano Banana Pro, shaped by a fundamental compromise: it favors semantic plausibility and visual appeal over precise pixel-level fidelity. This positions the model as highly effective for creative and perceptual tasks, such as artistic image enhancement, restoration of severely degraded photos, and scenarios where a visually compelling result is more critical than strict accuracy. Its ability to perform these tasks without specialized training also makes it a practical tool for rapid prototyping.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Operational Scope and Limitations of Nano Banana Pro", "weight": 1.0} -->

However, these capabilities come with inherent constraints. The model is not suitable for applications demanding rigorous factual accuracy, including forensic examination, scientific imaging, or any context where the output must correspond exactly to the original scene data. Its generative approach can introduce alterations, such as softened boundaries in super-resolution, altered text in deblurring, or non-physical color shifts, that prioritize visual completeness over authentic reproduction. In essence, Nano Banana Pro serves as a powerful semantic reconstructor and enhancer for common visual applications, but it is not designed for high-precision tasks where strict fidelity is paramount.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Future Research Directions", "weight": 1.0} -->

Exploration of Hybrid Architectures. The future all-rounder may not be a purely generative model but a generative-regression hybrid. For instance, a lightweight regression network could first recover basic structure and color in the front-end, followed by a conditional generative model for detail enhancement and beautification in the back-end. This process should be constrained by physics-informed loss functions to curb arbitrariness.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Future Research Directions", "weight": 1.0} -->

Prompt Engineering and Controllable Generation. It is important to note that the present evaluation reflects a conservative estimate of the model's capability, as we did not engage in meticulous prompt tuning or employ multi-round inference to cherry-pick optimal outputs. Our fixed, simple prompts represent a pragmatic but unoptimized use case. Future work should therefore systematically explore how carefully designed textual instructions, visual cues, or interactive refinement can more effectively steer the generative process. Enhancing such controllability will be key to reducing unwanted variability in color, structure, and texture---ultimately improving the reliability and practical utility of generative models in restoration-sensitive applications.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Future Research Directions", "weight": 1.0} -->

Innovation in Evaluation Frameworks for Generative Models. The rise of generative models calls for a fundamental shift in how we evaluate their output. Traditional metrics, which rely on a single ground truth, fall short when assessing models that can produce multiple plausible reconstructions from a degraded image. We urgently need new benchmarks that reflect this reality, for instance, datasets that include several expert-approved restoration options for a given input. At the same time, evaluation should move beyond pixel-level fidelity alone. Developing unified metrics that capture both perceptual quality and distortion would provide a more nuanced view of a model's performance across the quality--fidelity spectrum.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The evaluation of Nano Banana Pro signals a paradigm shift: foundational generative models are redefining the boundaries of low-level vision. Functioning less as a traditional restoration tool and more as a semantic reconstruction engine, the model leverages deep generative priors to synthesize visual content rather than merely recovering pixels. This emergence challenges the community to reconsider the fundamental metric of success: is it absolute pixel fidelity, or the maximization of perceptual plausibility?.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our empirical results confirm that while Nano Banana Pro trails domain-specific experts in zero-shot pixel fidelity, it demonstrates exceptional potential in perceptual quality, particularly when handling extreme degradations and cross-task generalization. Consequently, the trajectory of the field lies not in a binary choice between paradigms, but in strategic integration. The next generation of robust vision systems must bridge the semantic imagination of generative models with the physical constraints and precision of specialized networks.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Ultimately, Nano Banana Pro is a double-edged sword. It has successfully raised the ceiling of perceptual quality for complex visual tasks, yet it has not secured the floor of stability required for forensic precision.
