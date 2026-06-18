<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Diffusion models have gained attention for their success in modeling complex distributions, achieving impressive perceptual quality in SR tasks. However, existing diffusion-based SR methods often suffer from high computational costs, requiring numerous iterative steps for training and inference. Existing acceleration techniques, such as distillation and solver optimization, are generally task-agnostic and do not fully leverage the specific characteristics of low-level tasks like super-resolution (SR). In this study, we analyze the frequency- and spatial-domain properties of diffusion-based SR methods, revealing key insights into the temporal and spatial dependencies of high-frequency signal recovery. Specifically, high-frequency details benefit from concentrated optimization during early and late diffusion iterations, while spatially textured regions demand adaptive denoising strategies. Building on these observations, we propose the Time-Spatial-aware Sampling strategy (TSS) for the acceleration of Diffusion SR without any extra training cost. TSS combines Time Dynamic Sampling (TDS), which allocates more iterations to refining textures, and Spatial Dynamic Sampling (SDS), which dynamically adjusts strategies based on image content.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensive evaluations across multiple benchmarks demonstrate that TSS achieves state-of-the-art (SOTA) performance with significantly fewer iterations, improving MUSIQ scores by 0.2 - 3.0 and outperforming the current acceleration methods with only half the number of steps.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Image super-resolution (SR) Wang et al.; Zhang et al.; Liang et al.; Qin et al.; Liu et al.; Zhao et al.; Qin et al.; Bao et al. aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs. Recently, diffusion models Ho et al.; Song et al. have gained attention for their ability to model complex distributions, achieving notable success in SR Chen et al.; Wang et al.; Yang et al.; Yu et al.; Wu et al.; Qu et al., particularly in perceptual quality Wang et al.; Wu et al.. Diffusion-based image super-resolution methods take two primary approaches: integrating the low-resolution image into a task-specific denoiser Saharia et al.; Wang et al. or adapting the reverse diffusion process of pre-trained models Wu et al.; Yang et al.; Yu et al..

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These methods are computationally intensive, requiring 1000 steps for training and several, such as 20 (PASD Yang et al. ), 50 (SUPIR Yu et al. ), or more steps (StableSR Wang et al. ) during testing.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efforts to accelerate denoising generation focus on sampler acceleration and distillation, achieving results in 10 or fewer steps Yue et al.; Wang et al.. Most Diffusion SR methods Wang et al.; Yu et al.; Yang et al. adopt these general strategies without considering the unique frequency characteristics of low-level vision tasks. However, in fact, recent studies like STAR Xie et al. have highlighted the diverse recovery of diffusion-based SR across frequency domains, suggesting the potential to learn low- and high-frequency information at different training stages. Despite these insights, these works primarily focus on modifying the training process and optimization losses. Given the availability of many large-scale open source and pre-trained diffusion SR models Yang et al.; Yu et al.; Wang et al., we aim to develop a tailored training-free acceleration strategy by leveraging the characteristics of Diffusion SR methods with the spatial and frequency information, seeking to enhance the performance of these existing models at minimal cost.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To analyze frequency-based disparities in the denoising process, we conduct a tiny experiment, using SUPIR, one of the latest typical state-of-the-art Diffusion SR methods, on the dataset Yu et al.. comprises 60 real-world images from common benchmarks. To explore the frequency characteristics, we applied Fourier transformation Cochran et al. to categorize spectra into low, medium, and high-frequency signals. To observe the time domain dynamics, we recorded the signal-to-noise ratio (SNR) of intermediate and final outputs over the 100-step inference. As shown in Fig..a, SNR improvements were most pronounced in the later stages across all frequency bands. Notably, unlike low and medium frequency components, high-frequency components uniquely exhibited visible SNR gains in the early stages, indicating the critical role of early denoising in restoring high-frequency details.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we analyzed spatial variations in high-frequency recovery by cropping samples into 128-sized patches and categorizing them as smooth, medium-textured, or highly textured based on variance. We recorded the SNR of high-frequency signals for each category throughout the iterations, and analyzed the noise magnitude changes. For an intuitive comparison, Fig..d illustrates the denoising process for a typical sample with both low- and high-frequency regions, showing that smooth areas recover early, while high-frequency regions, such as fur, recover significantly in the final $0 \sim 100$ steps. Spatially, regions with more high-frequency information concentrate recovery in the initial and final stages, whereas content variation influences denoising dynamics.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on the above observations, efficiently generating high-frequency details requires leveraging their unique temporal optimization, which is concentrated in the early and late iterations. Therefore, we propose a Time Dynamic Sampling (TDS) strategy that prioritizes high-frequency signal recovery and enhances texture perception by allocating more denoising steps to diffusion stages critical for refining high-frequency details. Furthermore, from a spatial perspective, the sampling strategy must adapt to variations in image content. To achieve this, we introduce Spatial Dynamic Sampling (SDS), which dynamically adjusts the sampling frequency based on spatial content, ensuring alignment with the characteristics of different image regions. By integrating these two strategies, we propose Time-Spatial-Aware Sampling (TSS), a novel framework to accelerate existing diffusion-based SR without additional training costs. As both strategies require no additional training and only minimal code modifications, TSS offers an efficient and broadly applicable solution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evaluations on six BSR benchmarks across various metrics illustrate that TSS significantly improves the performance of various diffusion SR methods within a few iterations, without incurring additional training costs. TSS consistently achieves an increase of 0.2 $\sim$ 3.0 of MUSIQ in diverse SR diffusion frameworks and datasets. Remarkably, TSS outperforms the current state-of-the-art method while using only half the number of steps.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We identified the temporal and spatial dynamics of diffusion-based methods in high-frequency detail recovery of image super-resolution tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on the observations, we propose the Time-Spatial-aware Sampling strategy (TSS) to achieve training-free acceleration for diffusion-based image super-resolution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comprehensive evaluations across multiple real-world SR benchmarks show that TSS achieves state-of-the-art performance with fewer denoising iterations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Diffusion Model in Super-Resolution", "weight": 1.0} -->

Due to their exceptional ability to generate high-quality images, diffusion-based super-resolution methods have garnered widespread attention. Early approaches leveraged low-resolution images as guidance by training a conditional DDPM Ho et al.; Kawar et al.; Saharia et al., or conditionally steering a pre-trained DDPM Choi et al. to perform super-resolution tasks. Recently, several studies have utilized pre-trained text-to-image (T2I) models, such as Stable Diffusion (SD) Rombach et al.; Podell et al., harnessing learned priors to address super-resolution challenges and achieve high-quality image enhancements. These methods either train a ControlNet Zhang et al.; Yang et al.; Yu et al.; Chen et al. or an additional encoder that encodes guidance features Wu et al.; Wang et al., both of which have demonstrated outstanding performance. Yet, as mentioned earlier, these methods require a large number of diffusion steps, resulting in high computational costs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Diffusion Model Acceleration", "weight": 1.0} -->

Recent state-of-the-art super-resolution methods still require dozens or even hundreds of diffusion steps, even with acceleration techniques like DDIM Song et al., leading to significant time overhead. Reducing diffusion steps often degrades output quality. Various pruning Zhu et al., caching Ma et al., and distillation Yin et al. techniques have accelerated general T2I diffusion models while preserving generation quality. In super-resolution, ResShift Yue et al. reduces diffusion steps by modeling a Residual Shifting Markov chain between high-resolution and low-resolution images but requires a considerable cost of 500K iterations training from scratch. Distillation approaches Wu et al.; He et al. have achieved one-step diffusion in super-resolution tasks, but their training costs remain high, and their performance is constrained by the teacher models. Therefore, given the training costs and limitations of existing methods, exploring a training-free acceleration framework for diffusion-based super-resolution is valuable and necessary.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Revisiting Diffusion in Super-Resolution", "weight": 1.0} -->

To investigate the relationship between frequency signals, spatial characteristics, and temporal steps in denoising, we conducted two demo experiments using the representative SOTA method SUPIR, a classic framework based on pre-trained SD with fine-tuned ControlNet. The experiments are conducted on the dataset containing 60 real-world images from benchmarks like RealSR, DRealSR, and web sources.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Frequency Signal Analysis", "weight": 1.0} -->

We analyze the relationship between denoising stages and frequency-specific signal recovery by computing the signal-to-noise ratio (SNR) over 100-step inference using the Fourier Transform, with the final denoised result as a noise-free reference and intermediate results decoded from feature representations. As shown in Fig..a, SNR increases significantly in the late stages (400 $\sim$ 0 steps). Notably, high-frequency (HF) components, unlike low and medium frequencies, also exhibit visible SNR improvement in the early stages (1000 $\sim$ 700 steps). To further investigate HF signals crucial for SR, Fig..c presents the noise delta throughout denoising, where noise represents the residual with the final result, and delta denotes stepwise changes. Noise decreases in the early (1000 $\sim$ 700) and late (400 $\sim$ 0) stages but rises in the middle, mirroring the SNR trend in Fig..a. This suggests that, unlike low and medium frequencies, early denoising stages are also crucial for HF recovery, while intermediate stages may hinder optimization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Spatial Dynamics Analysis", "weight": 1.0} -->

To examine the spatial dynamics of denoising across regions with varying content, we analyzed signals in image patches of different textures. images were divided into non-overlapping 128×128 patches and classified as smooth, medium textured, or highly textured based on variance, applying Frequency Signal Analysis above to each category. As shown in Fig..c, higher variance patches have a narrower range of time steps for effective optimization in the early and late stages. Fig..d further illustrates that smooth regions undergo visible denoising earlier than fur-textured areas during late iterations. This suggests that denoising effectiveness varies across textures, with high-texture patches containing more high-frequency signals exhibiting shorter, more concentrated optimization stages in both early and late iterations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Spatial Dynamics Analysis", "weight": 1.0} -->

In summary, the restoration of high-frequency (HF) signals is unevenly distributed across both the denoising process and spatial regions within an image. However, the widely used traditional uniform, data-independent sampling methods haven't taken the spatiotemporal dynamics of HF signal denoising into account, which are critical for super-resolution tasks. Additionally, acceleration strategies relying on distillation or pruning often incur additional training time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Spatial Dynamics Analysis", "weight": 1.0} -->

Cost-Effectiveness. The strategy should achieve superior performance with fewer iterations while keeping additional training costs minimal.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Spatial Dynamics Analysis", "weight": 1.0} -->

Generality. The strategy should exhibit robust generalizability, enabling flexible integration across a wide range of established super-resolution frameworks.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Time-Spatial-aware Sampling", "weight": 1.0} -->

To address these issues and meet the requirements, we propose Time-Spatial-aware Sampling (TSS), a training-free content-adaptive accelerated sampling strategy. TSS integrates two core strategies: Time Dynamic Sampling and Spatial Dynamic Sampling, which are elaborated below.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Time Dynamics Sampling (TDS)", "weight": 1.0} -->

As discussed in Sec. 3.1, high-frequency signal optimization is concentrated in the early and late stages. Based on this observation, we propose the Time Dynamic Sampling (TDS) strategy with a non-uniform, adaptive timestep allocation. The non-uniform sampling design should meet two key criteria: 1) Higher sampling density in the early and late stages. 2) Adjustable non-uniformity, including uniform sampling as a special case. To achieve this, we propose a non-uniform denoising approach focused on high-frequency information by implementing a non-uniform resampling strategy in the time-step schedule. Specifically, for a given number of training steps $T$ and training scheduler $S = {\{ 1,2,3,\ldots,T\}}$, the scheduler $S^{\prime}$ for common uniform sampling of $T^{\prime}$ steps is

<!-- chunk {"id": "body-0024", "role": "body", "section": "Time Dynamics Sampling (TDS)", "weight": 1.0} -->

where $a$ denotes the transition point between early and late stages, and $n$ is the power factor. Fig. ‣ 3.2 Time-Spatial-aware Sampling ‣ 3 Method ‣ Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling") illustrates an example of the resampling function. When $n > 1$, sampling density is concentrated at $t = 0$ and $t = T$, while $n$ approaches 1, the function gradually converges to uniform sampling. Compared to uniform sampling, TDS enhances high-frequency signal recovery by prioritizing early and late-stage sampling, which is crucial for high-frequency restoration.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

TDS improves high-frequency signal restoration at the overall image level. However, as discussed in the previous section, different image regions exhibit distinct denoising dynamics, requiring region-specific sampling within a single image. To address this, we introduce Spatial Dynamic Sampling (SDS), which extends TDS with Variance-Adaptive Smooth Sampling and Spatial Dynamic Time Embedding.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

Variance-Adaptive Smooth Sampling To achieve dynamic scheduling across different image regions, as illustrated in Fig. ‣ 3.2 Time-Spatial-aware Sampling ‣ 3 Method ‣ Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling").a,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

Subsequently, we derive the non-uniform sampling strategy for each position based on the local smoothed variance $V_{g}$. Specifically, we assign an independent time scheduler to each position and adaptively adjust it based on local variations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

where $v_{g_{i,j}}$ denotes the local variance at position $(i,j)$ which controls $a$ and $n$. The spatial timestep $t_{spatial_{k}}$ for the $k^{th}$ denoising iteration represents a set of timesteps for each pixel,

<!-- chunk {"id": "body-0029", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

where ${\mathbb{S}}_{i,j}$ denotes the single scheduler in $\mathbb{S}$ for position $(i,j)$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

where $N_{\text{max}}$, $N_{\text{min}}$, $A_{\text{max}}$, and $A_{\text{min}}$ denote the range of $n$ and $a$. As shown in Fig. ‣ 3.2 Time-Spatial-aware Sampling ‣ 3 Method ‣ Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling").a, we assign different $a$ and $n$ values based on the local variance. In this way, we ensure that high-frequency texture regions with high variance.a) undergo greater sampling inhomogeneity, concentrating steps in the early and late phases to enhance high-frequency recovery. Conversely, smooth regions with lower variance.a) are sampled more uniformly, facilitating the restoration of smooth areas.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

While Variance-Adaptive Smooth Sampling allows for location-specific timestep allocation, segmenting images into separate patches to accommodate spatially varying timesteps will increase processing time and cause boundary artifacts. To adapt pre-trained denoising networks for spatial timestep embeddings in one step, we introduce a simple yet effective spatiotemporal embedding injection strategy. Specifically, existing methods generate individual timestep embedding $t_{emb} \in R^{C}$ and add them to main branch features $z \in R^{B \times C \times H \times W}$ at all spatial locations via automatic expansion.b), which can be formulated as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

where the expanded version ${expand}{(t_{emb})}$ matches the spatial dimensions of the main branch features $z$. In contrast, our spatial timestep embedding is the set of embeddings for each spatial location in $t_{spatial}$, which has the same spatial dimensions as the main branch features $z$, as depicted in Fig. ‣ 3.2 Time-Spatial-aware Sampling ‣ 3 Method ‣ Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling").c

<!-- chunk {"id": "body-0033", "role": "body", "section": "Spatial Dynamic Sampling (SDS)", "weight": 1.0} -->

This allows the network to adapt to spatially varying timestep embeddings while integrating flexibly into existing architectures without extra cropping or multiple forward passes.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Our approach modifies only the sampling strategy during inference, requiring no extra training. Experiments were conducted on an NVIDIA A800 GPU (80GB) using the official codebases and pre-trained weights. The PyTorch framework was used for implementation, and the detailed hyperparameters are provided in the full version.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Testing Datasets", "weight": 1.0} -->

Performance was evaluated on both synthetic and real-world data. Synthetic data used DIV2K with LR images degraded by BSRGAN. Real-world evaluations used DRealSR and RealSR, along with face SR benchmarks WebPhoto-Test \[2021a\] and LFW-test., WebPhoto, and LFW were tested at ×2 scale, and others at ×4.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

For the quantitative evaluation of super-resolution, we employed widely used perceptual quality metrics, including NIQE, CLIPIQA, MUSIQ, and QAlign, to compare the performance of the competing methods. Additionally, we provide the full-reference metrics including PSNR, SSIM, and LPIPS in the full version.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Comparison with State-of-the-Art Methods", "weight": 1.0} -->

For a comprehensive comparison, we integrate the TSS framework with three recent SOTA diffusion-based super-resolution (SR) methods: StableSR \[2024a\], SUPIR, and PASD. Their performance is evaluated against state-of-the-art (SOTA) SR approaches, including Real-ESRGAN \[2021b\], BSRGAN, SwinIR, SinSR \[2024b\], and ResShift, using both synthetic and real-world datasets. Real-ESRGAN, BSRGAN, and SwinIR are traditional deep learning-based SR frameworks using CNNs or transformers, while SinSR and ResShift are diffusion-accelerated SR methods leveraging distillation and fine-tuning, respectively. For fairness, the results are obtained from official codebases and pre-trained models. Quantitative evaluation and qualitative comparisons are presented in Tab. and Fig., respectively. As presented in Tab., our SUPIR^TSS^ outperforms the state-of-the-art acceleration stra-

<!-- chunk {"id": "body-0038", "role": "body", "section": "Comparison with State-of-the-Art Methods", "weight": 1.0} -->

tegies ReShift and SinSR on most benchmarks, achieving a 1.14 - 5.05 improvement in NIQE and a 0.09 - 1.52 improvement in QAlign across both synthetic and real datasets. Notably, while baseline SUPIR's 7-step QAlign results are initially inferior to ReShift and SinSR on real datasets, the incorporation of the TSS framework enables a QAlign improvement of 0.09 - 1.24 over SinSR and 0.12 - 1.58 over ReShift across all datasets. Although SinSR requires only a single iteration, its distillation strategy involves additional training costs, whereas TSS achieves comparable results without any extra training. Furthermore, compared to ReShift, which requires training and 15 inference steps, SUPIR^TSS^ delivers superior performance across all metrics except CLIPIQA, achieving these results in just 7 iterations, less than half the steps. Fig. provides examples of synthetic and real degradation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Comparison with State-of-the-Art Methods", "weight": 1.0} -->

Taking the first example in Fig. as an example, most existing methods, including CNN- and Transformer-based approaches and diffusion acceleration strategies, fail to generate the region with high-frequency textures (wrinkles, beard, and eyebrow). In contrast, SUPIR^TSS^ produces more realistic and richer high-frequency textures, as evidenced by both qualitative visual quality and quantitative results In summary, both quantitative and qualitative analyses show that TSS significantly enhances the high-frequency restoration capabilities of recent diffusion-based SR methods, achieving state-of-the-art texture generation performance on both synthetic and real-world datasets without any additional training costs.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Effectiveness of Time Dynamic Sampling", "weight": 1.0} -->

To validate the effectiveness of Time Dynamic Sampling (TDS), we compare SUPIR with its TDS-enhanced version on the dataset. As shown in Tab., TDS improves quantitative metrics, achieving a 20% increase in QAlign and a 35% increase in CLIPIQA at 7 steps. Fig. (Col. 3 vs. 1) visually compares SUPIR results with and without TDS on real samples. TDS enhances the butterfly texture reconstruction while uniform sampling introduces artifacts like color blocking. For further analysis, Fig. illustrates the relationship between high-frequency SNR and the number of denoising steps. Compared to the original SUPIR (blue), SUPIR+TDS (green) consistently achieves higher SNR at the same step count, even with fewer total steps, indicating its effectiveness in high-frequency signal restoration.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Necessity of Early Stage Sampling", "weight": 1.0} -->

To verify the need for early-stage sampling, we compare SUPIR with late-stage-only sampling ) and Time Dynamic Sampling (TDS) on the. As shown in Tab., late-stage-only sampling fails to improve NIQE and results in a 0.3 drop in QAlign, while TDS nearly doubles the MUSIQ gain by balancing early and late sampling. Fig. compares the high-frequency SNR of both methods. Due to insufficient early-stage denoising, late-stage-only sampling retains excessive HF noise at lower steps, sometimes underperforming the baseline. In contrast, TDS, with concentrated sampling in both early and late stages, effectively boosts HF SNR with fewer steps. Fig. (Col. 2 vs. 3) further illustrates this effect. While late-stage-only sampling enhances local texture, fewer steps in the early stage leave residual noise, causing visible artifacts. TDS, by ensuring adequate sampling across both stages, enables realistic texture generation without artifacts.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Non-Uniform Function Selection", "weight": 1.0} -->

We evaluated the impact of different non-uniform functions on sampling performance, including trigonometric, exponential, and polynomial functions. As shown in Tab., all three functions outperform the baseline with a 0.6 - 0.75 QAlign improvement, showing that non-uniform sampling aligns with high-frequency signal recovery regardless of the function type. For better controllability, we select the polynomial function as the final setting.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Effectiveness of Spatial Dynamic Sampling", "weight": 1.0} -->

To assess the necessity of Spatial Dynamic Sampling (SDS), we compare SUPIR with TDS alone and the full TSS (TDS+SDS). As shown in Tab. (Col. 2 and 3), the inclusion of SDS brings quantitative metric improvements over TDS alone. Moreover, Fig. further illustrates this effect. TDS alone (Col. 3) applies a spatial-unified scheduler, resulting in less sharp butterfly wings and an insufficiently smooth background. In contrast, SDS enables spatial-wise adaptive sampling, enhancing both texture-rich and smooth regions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "SDS in the Denoising Process", "weight": 1.0} -->

For a more intuitive explanation, we recorded the denoising process of PASD with different sampling strategies in Fig.. Excessive inhomogeneity (Col. 3) adds noise to smooth regions, while insufficient inhomogeneity (Cols. 1, 2) fails to generate textures. In contrast, SDS (Col. 4) adaptively balances inhomogeneity, ensuring optimal reconstruction of both smooth and textured areas.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we explore key insights in the denoising process: high-frequency components require focused optimization in early and late iterations, while spatially varying content necessitates adaptive strategies for effective restoration. Based on these findings, we propose Time-Spatial-aware Sampling (TSS), a training-free, content-adaptive sampling strategy to accelerate diffusion-based image super-resolution. By leveraging temporal and spatial dependencies in high-frequency recovery, TSS enhances texture restoration while significantly reducing computational costs. Compatible with various diffusion SR frameworks, it achieves state-of-the-art results with half the steps of recent accelerated methods.
