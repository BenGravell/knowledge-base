<!-- arxiv-full-text:v1 {"arxiv_id": "2501.02976", "source": "arxiv-html"} -->

## Introduction

Real-world video super-resolution (VSR) aims to generate high-resolution (HR) videos with clear details and strong temporal consistency from low-resolution (LR) inputs with unknown degradations. Most VSR methods only focus on simple, known degradations like downsampling or camera-related issues. However, real-world scenarios often involve unexpected degradations such as noise, blur, and compression, making it difficult for models to capture both spatial and temporal information needed for high-quality, consistent restoration.

GAN-based methods are widely used in real-world VSR for improving details through adversarial learning. By incorporating optical flow maps, they also improve temporal consistency, yielding smooth motion across frames. However, their limited generative capacity often results in oversmoothing, as illustrated in Figure 1. Recently, image diffusion models have been applied to real-world VSR for realistic video generation. Methods like incorporate temporal blocks or optical flow maps to improve temporal information capture. However, since these models are primarily trained on image data rather than video data, simply adding temporal layers often fails to ensure high temporal consistency (see Figure 8). VEnhancer and LaVie-SR incorporate T2V models for super-resolving AI-generated videos. However, two key challenges still remain: artifacts introduced by complex degradations in real-world settings, and compromised fidelity due to the strong generative capacity of powerful T2V models (e.g., CogVideoX).

To fully leverage the T2V prior to enhance practical VSR, we introduce STAR, a novel Spatial-Temporal Augmentation approach for Real-world VSR that achieves realistic spatial details and robust temporal consistency. Specifically, $1$) To address artifacts, we introduce a Local Information Enhancement Module (LIEM) before global self-attention to evaluate its impact on T2V models for real-world VSR. This approach stems from our observation that most T2V models rely solely on a global information extraction module (i.e., global self-attention), whereas capturing local details is crucial for video restoration. $2$) To improve fidelity, we propose a Dynamic Frequency (DF) Loss, guiding the model to prioritize low- or high-frequency information at different diffusion steps. This is based on our observation that during the reverse diffusion process, our model tends to first recover structure and then refine details. This approach decouples fidelity requirements, reduces learning difficulty, and enhances restoration fidelity.

In summary, our main contributions are as follows: $\bullet$ We propose STAR, a Spatio-Temporal quality Augmentation framework for Real-world VSR. To our best knowledge, we are the first to integrate diverse, powerful text-to-video diffusion priors into real-world VSR, improving both spatial details and temporal consistency. $\bullet$ We introduce LIEM to enhance local details and ease degradation removal, effectively mitigating artifacts. Moreover, we propose DF loss to guide the model in learning frequency-specific information across diffusion steps, decoupling fidelity requirements and ultimately improving overall fidelity. $\bullet$ Our STAR achieves the highest clarity (DOVER scores) across all datasets compared to state-of-the-art methods, while maintaining robust temporal consistency.

## Related Work

Figure 2: Overview of the proposed STAR.

### Video Super-Resolution

Traditional VSR methods can be roughly divided into two categories: recurrent-based and sliding-window-based methods. Recurrent-based methods process LR video frame by frame using recurrent neural networks. In contrast, sliding-window-based methods divide a video sequence into segments, using each as input to super-resolve the video. However, both approaches suffer from degradation mismatch, leading to significant performance drops in real-world applications. Recently, there has been a growing focus on real-world VSR, targeting complex, unknown degradations. RealBasicVSR, an extension of BasicVSR, introduces a pre-cleaning module to mitigate artifacts. RealViformer discovers that channel attention is less sensitive to artifacts and uses squeeze-excite mechanisms and covariance-based rescaling to address these challenges further. While GAN-based and image diffusion models have made substantial progress, they still face issues such as over-smoothing details and temporal inconsistency.

### Text-to-Video Diffusion Model

Large-scale pre-trained text-to-video (T2V) diffusion models have garnered significant attention, particularly with the impressive results from Sora. Numerous T2V models have since emerged, generally divided into: U-Net-based methods and DiT-based methods. I2VGen-XL, a U-Net-based method, employs a two-stage approach: first generating semantically and content-consistent LR videos, then using these as conditions to produce HR outputs. CogvideoX, built on DiT, introduces an adaptive LayerNorm to enhance text-video alignment and employs 3D attention to better integrate spatio-temporal information. Both models have large model capacities and are trained on large-scale datasets, enabling them to capture robust spatio-temporal priors. In this work, we propose STAR to fully leverage T2V model prior for real-world VSR.

### Diffusion Prior for Super-Resolution

Several works have leveraged generative diffusion priors for image and video super-resolution. StableSR adds a time-aware encoder and feature warping module to the SD model. DiffBIR integrates restoration and generative modules via ControlNet, while PASD and SeeSR embed semantic information in U-Net to guide diffusion. These methods balance fidelity and perceptual quality, achieving high-resolution image details. Methods like Upscale-A-Video, MGLD-VSR, Inflating with Diffusion, and SATeCo have adapted text-to-image diffusion priors for VSR by adding temporal layers. However, rooted in text-to-image models, they often struggle with temporal consistency. More recently, VEnhancer and LaVie-SR have incorporated T2V models to super-resolve AI-generated videos but struggle with complex degradations in practical environments. In contrast, we are the first to integrate powerful T2V diffusion priors for real-world VSR, introducing the LIEM module to address spatial artifacts and DF loss to enhance fidelity.

## Methodology

Figure 3: Motivation of LIEM. Left: schematic diagram illustrating the impact of using only global structure versus a combination of local and global structures. Right: visual comparison on real-world and synthetic videos. (Zoom-in for best view) Figure 4: Motivation of DF Loss. Left: PSNR curves of low- and high-frequency components relative to ground truth across diffusion steps. The low-frequency PSNR increases during the early diffusion steps, while the high-frequency PSNR rises in the later diffusion steps. Right: visual results of low- and high-frequency components at different diffusion stage. (Zoom-in for best view)

### Overview

### Modules

The STAR primarily includes four modules: VAE, text encoder, ControlNet and T2V model with Local Information Enhancement Module (LIEM) to alleviate the artifacts (further analysis is provided in Sec. 3.2). As depicted in Figure 2, the VAE encoder takes HR videos $X_{H}$ and LR videos $X_{L}$ as input to generate latent tensors $Z_{H}$ and $Z_{L}$, respectively. The text encoder is responsible for generating text embeddings $c_{text}$ to provide high-level information. ControlNet takes $Z_{L}$ and $c_{text}$ as input to guide the T2V model output. Finally, the T2V model $\phi_{\theta}$ with LIEM receives noisy input $Z_{t} = {{\alpha_{t}Z_{H}} + {\sigma_{t}\epsilon}}$ ($t$ denotes diffusion step, $\alpha_{t}$ and $\sigma_{t}$ are noise scheduler parameters), $c_{text}$ and the control signal from ControlNet $c_{l}$ to predict the velocity $v_{t} \equiv {{\alpha_{t}\epsilon} - {\sigma_{t}Z_{H}}}$.

### Losses

We utilize v-prediction objective in optimization: Given the strong generalization ability of T2V models, relying solely on the v-prediction objective for optimization may lead to restored outputs with low fidelity, an essential factor in video super-resolution tasks. To address this, we introduce Dynamic Frequency (DF) Loss, which adaptively adjusts the constraint on high- and low-frequency components of the predicted ${\hat{X}}_{H}$ across different diffusion steps. The overall optimization objective for STAR is as follows: where ${b{(t)}} = {1 - \frac{t}{t_{max}}}$ is a weighting function ($t_{max}$ is set to 999) to balance $\mathcal{L}_{v}$ and $\mathcal{L}_{DF}$. With the proposed LIEM and DF loss, STAR achieves high spatio-temporal quality, reduced artifacts and enhanced fidelity.

### Local Information Enhancement Module

### Motivation

Most T2V models primarily use a global attention mechanism, which is well-suited to text-to-video tasks by capturing global information to generate complete videos from scratch. However, this approach may be suboptimal for real-world video super-resolution, where complex degradations occur and local details are crucial. Relying solely on global attention mechanisms presents two drawbacks for real-world video super-resolution: $1$) It complicates degradation removal, as it processes the entire degraded video at once (the first and second columns in Figure 3 (right)). $2$) It lacks local details, resulting in blurry outputs (the third column in Figure 3 (right)).

### Details of LIEM

To address the above issues, we propose a simple but effective approach: adding a Local Information Enhancement Module (LIEM) before the global attention block to make T2V model pay more attention to local information. It can be expressed: where $AP{(\cdot)}$ and $MP{(\cdot)}$ denote average pooling and max pooling, respectively. $F_{I}$ and $F_{O}$ represent the input and output features, while $G{(\cdot)}$ and $L{(\cdot)}$ refer to the global attention block and LIEM. We adopt the local attention block in CBAM as LIEM for simplicity. Additional analysis on the impact of adding LIEM is provided in Sec. 3. Intuitively, as shown in the second row of Figure 3 (left), incorporating LIEM enables the T2V model to address local region degradation first and then aggregate global features. This approach reduces the complexity of degradation removal and mitigates artifacts. Furthermore, the T2V model with LIEM produces clearer, more detailed results due to the enriched local information.

### Dynamic Frequency Loss

Table 1: Quantitative evaluations on diverse VSR benchmarks from synthetic ( ) and real-world (VideoLQ) sources. The best performance is highlighted in bold, and the second-best in underlined. Ewarp* refers to Ewarp (×10−3).

### Motivation

The powerful generative capacity of diffusion models may compromise the fidelity in restored result. In Figure 4 (Right), an interesting pattern emerges when examining restored results at each diffusion step during inference. In the early stages, the model primarily reconstructs structure with low frequency, whereas in later stages, after the structure is largely complete, focus shifts to refining details with high frequency. To further illustrate this phenomenon, Figure 4 (Left) presents PSNR curves of low- and high-frequency components against the ground truth across diffusion steps. The low-frequency PSNR rises in the early stages, while the high-frequency PSNR increases later, aligning with the visual results.

Fidelity can be divided into two types: $1$) Low-frequency fidelity, encompassing large structures and instances. 2) High-frequency fidelity, including edges and textures, aligning with the characteristics of the denoising process. This raises a question: Can we design a loss function that exploits this characteristic to decouple fidelity and simplify optimization? Specifically, we aim to guide the model to prioritize low-frequency components in the early stages, shifting focus to high-frequency components later.

Figure 5: Dynamic Frequency Loss. Left: curves of weighting function c(t) for different α. Right: details of DF loss.

### Details of DF Loss

Here, we propose Dynamic Frequency Loss. Specifically, in each diffusion step $t$, we use the following equation to obtain the estimated ${\hat{Z}}_{H}$: Then, we use the decoder to convert the latent ${\hat{Z}}_{H}$ back to the pixel space, resulting in ${\hat{X}}_{H}$. After that, we apply Discrete Fourier Transform (DFT) to transform ${\hat{X}}_{H}$ into the frequency domain as shown in Figure 5. We predefine a low-frequency pass filter $\psi$ to obtain the low- and high-frequency: where $\mathcal{F}{(\cdot)}$ is DFT, $\odot$ is element-wise multiplication. ${\hat{f}}_{l}$ and ${\hat{f}}_{h}$ denote the low and high frequency of ${\hat{X}}_{H}$. The proposed DF loss can be written as: where $f_{l}$ / $f_{h}$ stand for low- / high-frequency of $X_{H}$, respectively. ${c{(t)}} = {({t/t_{max}})}^{\alpha}$ is the weighting function.

## Experiments

Figure 6: Qualitative comparisons on synthetic LR videos from and. (Zoom-in for best view) Figure 7: Qualitative comparisons on real-world test videos in VideoLQ dataset. (Zoom-in for best view) Figure 8: Qualitative comparisons on temporal consistency in and OpenVid dataset. (Zoom-in for best view)

### Datasets and Implementation

Training Datasets. We train STAR using the subset of OpenVid-1M, containing $\sim$`<!-- -->`{=html}200K text-video pairs. The OpenVid-1M dataset is a high-quality video dataset consisting of over 1 million in-the-wild video clips with detailed captions, where the minimum resolution is $512$$\times$$512$ and the average length is 7.2 seconds. Utilizing this large-scale high-quality data for training further improves our model's restoration capacity for real-world VSR. More training dataset comparisons can be found in Table 2. We generate the LR-HR video pairs following the degradation strategy in Real-ESRGAN, combined with video compression operations, resulting in severe degradation similar to the approach used in RealBasicVSR.

#Frames

Table 2: Training dataset comparison.

Testing Datasets. We evaluate our method on both synthetic and real-world datasets. As for synthetic testing datasets, we follow the same degradation pipeline in training to generate LR videos from HR ones to construct three synthetic datasets (i.e. and ). The is split from OpenVid-1M ensuring no overlap with the training dataset and comprises the first approximately 100 frames of 30 videos. For the real-world dataset, we choose VideoLQ which contains 50 videos, each with 100 frames.

Training Details. By default, we adopt I2VGen-XL as our T2V backbone. For fast convergence, we initialize the model using the weights from VEnhancer. We then train the ControlNet and inserted LIEM to adapt the T2V model for the real-world VSR task. Specifically, we train STAR on $8$ NVIDIA A100-80G GPUs with $15$K iterations and a batch size of $8$. The training data is $720$$\times$$1280$ with $32$ frames. We use AdamW as the optimizer with a learning rate of 5e-5.

Evaluation Metrics. We adopt six metrics to evaluate the VSR outputs from several different perspectives: image fidelity (PSNR), perceptual similarity (SSIM, LPIPS ), quality (ILNIQE ), video clarity (DOVER ) and temporal consistency ($E_{warp}^{\ast}$ ). For synthetic datasets, we calculate PSNR, SSIM and LPIPS between the output and ground-truth frames, along with DOVER and flow warping error (i.e., $E_{warp}^{\ast}$) of output videos. For real-world dataset, because of no ground-truth videos, we use three non-reference metrics: ILNIQE, DOVER, and $E_{warp}^{\ast}$.

### Comparisons

To verify the effectiveness of our approach, we compare STAR with several state-of-the-art methods, including Real-ESRGAN, DBVSR, RealBasicVSR, RealViformer, ResShift, StableSR, and Upscale-A-Video.

Quantitative Evaluation. As shown in Table 1, we calculate five metrics on each synthetic benchmark. Our STAR achieves the best scores in four out of these five metrics (SSIM, LPIPS, DOVER, and $E_{warp}^{\ast}$) on both and datasets, along with the second-best PSNR scores. This indicates that STAR can generate realistic details with good fidelity and robust temporal consistency. Moreover, we evaluate three non-reference metrics on a real-world dataset. On this dataset, STAR achieves the best score in DOVER and the second-best scores in ILNIQE and $E_{warp}^{\ast}$. These results demonstrate that STAR can effectively restore real-world videos with high spatial and temporal quality. Additionally, our visual results on both real-world and synthetic datasets are preferred by human evaluators, as detailed in the User Study section (see Appendix).

Qualitative Evaluation. To intuitively demonstrate the effectiveness of the proposed STAR, we present visual results on both synthetic and real-world datasets in Figure 6 and 7, respectively. As shown, our STAR generates the most realistic spatial details and exhibits the best degradation removal capability. Specifically, the first example in Figure 7 illustrates that STAR reconstructs the text structure most effectively, thanks to the T2V prior efficiently capturing temporal information, and the DF loss that improves the fidelity. Furthermore, the T2V model has a strong spatial prior, which helps generate more realistic details and structures, such as the human hand in Figure 6 and the horse shape and fur in Figure 7.

We also compare the temporal consistency in Figure 8. As observed in the left of Figure 8, StableSR demonstrates the most temporal inconsistency, primarily because it is originally designed for image super-resolution. Although RealBasicVSR, Upscale-A-Video, and RealViformer incorporate optical flow maps to enhance temporal consistency, they still face challenges in generating consistent results under complex degraded video conditions, as the optical flow maps may not always be accurate. In contrast, our proposed STAR achieves the best temporal consistency, thanks to the powerful temporal prior inherent in the T2V model, which effectively helps reconstruct temporal information even without the use of optical flow maps.

### Ablation Study

Figure 9: Ablation study about LIEM. Left: illustration of different insertion positions of LIEM and the structure of LIEM. Right: visual comparison on real-world and synthetic videos with different LIEM positions.

Table 3: Ablation of LIEM position.

Local Information Enhancement Module. We primarily investigate the impact of introducing LIEM in different ways. First, we find that adding LIEM on both spatial and temporal blocks achieves the best results as shown in Table 3. Second, we consider three connection types as shown in Figure 9 (Left). From visual results in Figure 9 (Right) and quantitative results in Table 3, we find that position (i) achieves the best results. This phenomenon can be attributed to the fact that, with most weights frozen to preserve the prior, the newly added blocks can influence the model's mapping process. However, the impact at positions (ii) and (iii) is too large, making it difficult for the model to fine-tune and adapt to this change, resulting in poor performance.

Table 4: Ablation of different variants of DF loss.

Table 5: Ablation of b(t) and α in c(t).

Figure 10: Illustration on scaling up with larger t2v models on a real-world low-quality video. (Zoom-in for best view) Dynamic Frequency Loss. First, we investigate the impact of different variants of frequency loss. As shown in Table 4, "Separate" indicates whether the frequency components are separated into high and low frequency, constraining them individually. "Type" refers to the specific definition of the DF loss: if set to "inverse," a higher weight is given to high frequencies in the early stages and a lower weight to low frequencies; if set to "direct", a higher weight is given to low frequencies initially and a lower weight to high frequencies, which is matching the analysis in Sec. 3.3. As observed, separating the frequency components and prioritizing low-frequency reconstruction early on yield the best perceptual quality while maintaining high fidelity. Second, we explore the optimal settings for $b{(t)}$ and $\alpha$ in $c{(t)}$. As shown in Table 5, using a linear form for $b{(t)}$ with $\alpha = 2$ for $c{(t)}$ yields the best results. Therefore, we adopt this DF loss configuration for training our model and comparing it with other state-of-the-art methods.

Table 6: Effectiveness of T2V diffusion prior for real-world VSR.

Scaling up with Larger T2V Models. To further validate the effectiveness of T2V diffusion priors for real-world VSR, we replace I2VGen-XL with larger DiT-based T2V models (i.e., CogVideoX ), and evaluate results both quantitatively and qualitatively. Since CogVideoX only supports inputs at 480$\times$`<!-- -->`{=html}720 resolution, we created a new test set by cropping 10 videos from OpenVid-1M to this size. As shown in Table 6, the powerful CogVideoX models yield consistent improvements across all metrics. Notably, SSIM improves from 0.6944 to 0.7400, and DOVER increases from 0.6609 to 0.7350, marking a substantial enhancement in visual quality. The robust spatio-temporal priors in CogVideoX enable realistic details and clear building structures (Figure 10), while maintaining high temporal consistency (Figure 8 Right). Inspired by scaling law and our findings, we believe larger, more powerful T2V models will further advance VSR tasks.

## Conclusion

In this paper, we present STAR, a real-world VSR framework that leverages T2V diffusion prior to restore videos with fewer artifacts, higher spatial fidelity, and stronger temporal consistency. Specifically, we introduce a Local Information Enhancement Module into the original T2V backbone to improve its ability to handle degradations and reconstruct fine details. Additionally, we propose a Dynamic Frequency Loss that guides the model to focus on restoring different frequency components at each diffusion step, thereby enhancing fidelity. Furthermore, we demonstrate that a powerful T2V model can effectively generate high-quality results in both spatial and temporal dimensions. Extensive experiments show that STAR achieves superior performance in both spatial and temporal quality. We hope our work lays a solid foundation for applying T2V models in real-world VSR and inspires future advancements in the field.
