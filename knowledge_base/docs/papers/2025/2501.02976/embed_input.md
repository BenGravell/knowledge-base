<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

STAR: Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution

Topics include Video super-resolution, Real-world super-resolution, Image restoration, Text-to-video models, Diffusion models, Temporal consistency, Local information enhancement, Dynamic frequency loss, STAR.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

STAR adapts text-to-video diffusion models to real-world video super-resolution, using local information enhancement and a dynamic frequency loss to improve detail recovery while preserving temporal coherence. It is useful as a recent example of moving super-resolution from per-frame image priors toward video-native generative priors.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Image diffusion models have been adapted for real-world video super-resolution to tackle over-smoothing issues in GAN-based methods. However, these models struggle to maintain temporal consistency, as they are trained on static images, limiting their ability to capture temporal dynamics effectively. Integrating text-to-video (T2V) models into video super-resolution for improved temporal modeling is straightforward. However, two key challenges remain: artifacts introduced by complex degradations in real-world scenarios, and compromised fidelity due to the strong generative capacity of powerful T2V models (\textit{e.g.}, CogVideoX-5B). To enhance the spatio-temporal quality of restored videos, we introduce\textbf{~\name} (\textbf{S}patial-\textbf{T}emporal \textbf{A}ugmentation with T2V models for \textbf{R}eal-world video super-resolution), a novel approach that leverages T2V models for real-world video super-resolution, achieving realistic spatial details and robust temporal consistency.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Specifically, we introduce a Local Information Enhancement Module (LIEM) before the global attention block to enrich local details and mitigate degradation artifacts. Moreover, we propose a Dynamic Frequency (DF) Loss to reinforce fidelity, guiding the model to focus on different frequency components across diffusion steps. Extensive experiments demonstrate\textbf{~\name}~outperforms state-of-the-art methods on both synthetic and real-world datasets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Real-world video super-resolution (VSR) aims to generate high-resolution (HR) videos with clear details and strong temporal consistency from low-resolution (LR) inputs with unknown degradations. Most VSR methods only focus on simple, known degradations like downsampling or camera-related issues. However, real-world scenarios often involve unexpected degradations such as noise, blur, and compression, making it difficult for models to capture both spatial and temporal information needed for high-quality, consistent restoration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

GAN-based methods are widely used in real-world VSR for improving details through adversarial learning. By incorporating optical flow maps, they also improve temporal consistency, yielding smooth motion across frames. However, their limited generative capacity often results in oversmoothing, as illustrated in Figure. Recently, image diffusion models have been applied to real-world VSR for realistic video generation. Methods like incorporate temporal blocks or optical flow maps to improve temporal information capture. However, since these models are primarily trained on image data rather than video data, simply adding temporal layers often fails to ensure high temporal consistency. VEnhancer and LaVie-SR incorporate T2V models for super-resolving AI-generated videos. However, two key challenges still remain: artifacts introduced by complex degradations in real-world settings, and compromised fidelity due to the strong generative capacity of powerful T2V models (e.g., CogVideoX).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To fully leverage the T2V prior to enhance practical VSR, we introduce STAR, a novel Spatial-Temporal Augmentation approach for Real-world VSR that achieves realistic spatial details and robust temporal consistency. Specifically, $1$) To address artifacts, we introduce a Local Information Enhancement Module (LIEM) before global self-attention to evaluate its impact on T2V models for real-world VSR. This approach stems from our observation that most T2V models rely solely on a global information extraction module (i.e., global self-attention), whereas capturing local details is crucial for video restoration. $2$) To improve fidelity, we propose a Dynamic Frequency (DF) Loss, guiding the model to prioritize low- or high-frequency information at different diffusion steps. This is based on our observation that during the reverse diffusion process, our model tends to first recover structure and then refine details. This approach decouples fidelity requirements, reduces learning difficulty, and enhances restoration fidelity.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\bullet$ We propose STAR, a Spatio-Temporal quality Augmentation framework for Real-world VSR. To our best knowledge, we are the first to integrate diverse, powerful text-to-video diffusion priors into real-world VSR, improving both spatial details and temporal consistency.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\bullet$ We introduce LIEM to enhance local details and ease degradation removal, effectively mitigating artifacts. Moreover, we propose DF loss to guide the model in learning frequency-specific information across diffusion steps, decoupling fidelity requirements and ultimately improving overall fidelity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

$\bullet$ Our STAR achieves the highest clarity (DOVER scores) across all datasets compared to state-of-the-art methods, while maintaining robust temporal consistency.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Video Super-Resolution", "weight": 1.0} -->

Traditional VSR methods can be roughly divided into two categories: recurrent-based and sliding-window-based methods. Recurrent-based methods process LR video frame by frame using recurrent neural networks. In contrast, sliding-window-based methods divide a video sequence into segments, using each as input to super-resolve the video. However, both approaches suffer from degradation mismatch, leading to significant performance drops in real-world applications. Recently, there has been a growing focus on real-world VSR, targeting complex, unknown degradations. RealBasicVSR, an extension of BasicVSR, introduces a pre-cleaning module to mitigate artifacts. RealViformer discovers that channel attention is less sensitive to artifacts and uses squeeze-excite mechanisms and covariance-based rescaling to address these challenges further. While GAN-based and image diffusion models have made substantial progress, they still face issues such as over-smoothing details and temporal inconsistency.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Text-to-Video Diffusion Model", "weight": 1.0} -->

Large-scale pre-trained text-to-video (T2V) diffusion models have garnered significant attention, particularly with the impressive results from Sora. Numerous T2V models have since emerged, generally divided into: U-Net-based methods and DiT-based methods. I2VGen-XL, a U-Net-based method, employs a two-stage approach: first generating semantically and content-consistent LR videos, then using these as conditions to produce HR outputs. CogvideoX, built on DiT, introduces an adaptive LayerNorm to enhance text-video alignment and employs 3D attention to better integrate spatio-temporal information. Both models have large model capacities and are trained on large-scale datasets, enabling them to capture robust spatio-temporal priors. In this work, we propose STAR to fully leverage T2V model prior for real-world VSR.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Diffusion Prior for Super-Resolution", "weight": 1.0} -->

Several works have leveraged generative diffusion priors for image and video super-resolution. StableSR adds a time-aware encoder and feature warping module to the SD model. DiffBIR integrates restoration and generative modules via ControlNet, while PASD and SeeSR embed semantic information in U-Net to guide diffusion. These methods balance fidelity and perceptual quality, achieving high-resolution image details. Methods like Upscale-A-Video, MGLD-VSR, Inflating with Diffusion, and SATeCo have adapted text-to-image diffusion priors for VSR by adding temporal layers. However, rooted in text-to-image models, they often struggle with temporal consistency. More recently, VEnhancer and LaVie-SR have incorporated T2V models to super-resolve AI-generated videos but struggle with complex degradations in practical environments. In contrast, we are the first to integrate powerful T2V diffusion priors for real-world VSR, introducing the LIEM module to address spatial artifacts and DF loss to enhance fidelity.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Modules", "weight": 1.0} -->

The STAR primarily includes four modules: VAE, text encoder, ControlNet and T2V model with Local Information Enhancement Module (LIEM) to alleviate the artifacts (further analysis is provided in Sec. 3.2). As depicted in Figure, the VAE encoder takes HR videos $X_{H}$ and LR videos $X_{L}$ as input to generate latent tensors $Z_{H}$ and $Z_{L}$, respectively. The text encoder is responsible for generating text embeddings $c_{text}$ to provide high-level information. ControlNet takes $Z_{L}$ and $c_{text}$ as input to guide the T2V model output.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Losses", "weight": 1.0} -->

Given the strong generalization ability of T2V models, relying solely on the v-prediction objective for optimization may lead to restored outputs with low fidelity, an essential factor in video super-resolution tasks. To address this, we introduce Dynamic Frequency (DF) Loss, which adaptively adjusts the constraint on high- and low-frequency components of the predicted ${\hat{X}}_{H}$ across different diffusion steps.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Losses", "weight": 1.0} -->

where ${b{(t)}} = {1 - \frac{t}{t_{max}}}$ is a weighting function ($t_{max}$ is set to 999) to balance $\mathcal{L}_{v}$ and $\mathcal{L}_{DF}$. With the proposed LIEM and DF loss, STAR achieves high spatio-temporal quality, reduced artifacts and enhanced fidelity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivation", "weight": 1.0} -->

Most T2V models primarily use a global attention mechanism, which is well-suited to text-to-video tasks by capturing global information to generate complete videos from scratch. However, this approach may be suboptimal for real-world video super-resolution, where complex degradations occur and local details are crucial. Relying solely on global attention mechanisms presents two drawbacks for real-world video super-resolution: $1$) It complicates degradation removal, as it processes the entire degraded video at once (the first and second columns in Figure (right)). $2$) It lacks local details, resulting in blurry outputs (the third column in Figure (right)).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Details of LIEM", "weight": 1.0} -->

To address the above issues, we propose a simple but effective approach: adding a Local Information Enhancement Module (LIEM) before the global attention block to make T2V model pay more attention to local information.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Details of LIEM", "weight": 1.0} -->

where $AP{( \cdot )}$ and $MP{( \cdot )}$ denote average pooling and max pooling, respectively. $F_{I}$ and $F_{O}$ represent the input and output features, while $G{( \cdot )}$ and $L{( \cdot )}$ refer to the global attention block and LIEM. We adopt the local attention block in CBAM as LIEM for simplicity. Additional analysis on the impact of adding LIEM is provided in Sec.. Intuitively, as shown in the second row of Figure (left), incorporating LIEM enables the T2V model to address local region degradation first and then aggregate global features. This approach reduces the complexity of degradation removal and mitigates artifacts. Furthermore, the T2V model with LIEM produces clearer, more detailed results due to the enriched local information.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Motivation", "weight": 1.0} -->

The powerful generative capacity of diffusion models may compromise the fidelity in restored result. In Figure (Right), an interesting pattern emerges when examining restored results at each diffusion step during inference. In the early stages, the model primarily reconstructs structure with low frequency, whereas in later stages, after the structure is largely complete, focus shifts to refining details with high frequency. To further illustrate this phenomenon, Figure (Left) presents PSNR curves of low- and high-frequency components against the ground truth across diffusion steps. The low-frequency PSNR rises in the early stages, while the high-frequency PSNR increases later, aligning with the visual results.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Motivation", "weight": 1.0} -->

Fidelity can be divided into two types: $1$) Low-frequency fidelity, encompassing large structures and instances. 2) High-frequency fidelity, including edges and textures, aligning with the characteristics of the denoising process. This raises a question: Can we design a loss function that exploits this characteristic to decouple fidelity and simplify optimization? Specifically, we aim to guide the model to prioritize low-frequency components in the early stages, shifting focus to high-frequency components later.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Details of DF Loss", "weight": 1.0} -->

Here, we propose Dynamic Frequency Loss.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Details of DF Loss", "weight": 1.0} -->

Then, we use the decoder to convert the latent ${\hat{Z}}_{H}$ back to the pixel space, resulting in ${\hat{X}}_{H}$. After that, we apply Discrete Fourier Transform (DFT) to transform ${\hat{X}}_{H}$ into the frequency domain as shown in Figure.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Datasets and Implementation", "weight": 1.0} -->

Training Datasets. We train STAR using the subset of OpenVid-1M, containing $\sim$`<!-- -->`{=html}200K text-video pairs. The OpenVid-1M dataset is a high-quality video dataset consisting of over 1 million in-the-wild video clips with detailed captions, where the minimum resolution is $512$$\times$$512$ and the average length is 7.2 seconds. Utilizing this large-scale high-quality data for training further improves our model's restoration capacity for real-world VSR. More training dataset comparisons can be found in Table. We generate the LR-HR video pairs following the degradation strategy in Real-ESRGAN, combined with video compression operations, resulting in severe degradation similar to the approach used in RealBasicVSR.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Datasets and Implementation", "weight": 1.0} -->

#Frames

<!-- chunk {"id": "body-0026", "role": "body", "section": "Datasets and Implementation", "weight": 1.0} -->

Testing Datasets. We evaluate our method on both synthetic and real-world datasets. As for synthetic testing datasets, we follow the same degradation pipeline in training to generate LR videos from HR ones to construct three synthetic datasets (i.e. and ). The is split from OpenVid-1M ensuring no overlap with the training dataset and comprises the first approximately 100 frames of 30 videos. For the real-world dataset, we choose VideoLQ which contains 50 videos, each with 100 frames.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Datasets and Implementation", "weight": 1.0} -->

Training Details. By default, we adopt I2VGen-XL as our T2V backbone. For fast convergence, we initialize the model using the weights from VEnhancer. We then train the ControlNet and inserted LIEM to adapt the T2V model for the real-world VSR task. Specifically, we train STAR on $8$ NVIDIA A100-80G GPUs with $15$K iterations and a batch size of $8$. The training data is $720$$\times$$1280$ with $32$ frames. We use AdamW as the optimizer with a learning rate of 5e-5.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Datasets and Implementation", "weight": 1.0} -->

Evaluation Metrics. We adopt six metrics to evaluate the VSR outputs from several different perspectives: image fidelity (PSNR), perceptual similarity (SSIM, LPIPS ), quality, video clarity and temporal consistency ($E_{warp}^{\ast}$ ). For synthetic datasets, we calculate PSNR, SSIM and LPIPS between the output and ground-truth frames, along with DOVER and flow warping error (i.e., $E_{warp}^{\ast}$) of output videos. For real-world dataset, because of no ground-truth videos, we use three non-reference metrics: ILNIQE, DOVER, and $E_{warp}^{\ast}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Comparisons", "weight": 1.0} -->

To verify the effectiveness of our approach, we compare STAR with several state-of-the-art methods, including Real-ESRGAN, DBVSR, RealBasicVSR, RealViformer, ResShift, StableSR, and Upscale-A-Video.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Comparisons", "weight": 1.0} -->

Quantitative Evaluation. As shown in Table, we calculate five metrics on each synthetic benchmark. Our STAR achieves the best scores in four out of these five metrics (SSIM, LPIPS, DOVER, and $E_{warp}^{\ast}$) on both and datasets, along with the second-best PSNR scores. This indicates that STAR can generate realistic details with good fidelity and robust temporal consistency. Moreover, we evaluate three non-reference metrics on a real-world dataset. On this dataset, STAR achieves the best score in DOVER and the second-best scores in ILNIQE and $E_{warp}^{\ast}$. These results demonstrate that STAR can effectively restore real-world videos with high spatial and temporal quality. Additionally, our visual results on both real-world and synthetic datasets are preferred by human evaluators, as detailed in the User Study section (see Appendix).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Comparisons", "weight": 1.0} -->

Qualitative Evaluation. To intuitively demonstrate the effectiveness of the proposed STAR, we present visual results on both synthetic and real-world datasets in Figure and, respectively. As shown, our STAR generates the most realistic spatial details and exhibits the best degradation removal capability. Specifically, the first example in Figure illustrates that STAR reconstructs the text structure most effectively, thanks to the T2V prior efficiently capturing temporal information, and the DF loss that improves the fidelity. Furthermore, the T2V model has a strong spatial prior, which helps generate more realistic details and structures, such as the human hand in Figure and the horse shape and fur in Figure.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Comparisons", "weight": 1.0} -->

We also compare the temporal consistency in Figure. As observed in the left of Figure, StableSR demonstrates the most temporal inconsistency, primarily because it is originally designed for image super-resolution. Although RealBasicVSR, Upscale-A-Video, and RealViformer incorporate optical flow maps to enhance temporal consistency, they still face challenges in generating consistent results under complex degraded video conditions, as the optical flow maps may not always be accurate. In contrast, our proposed STAR achieves the best temporal consistency, thanks to the powerful temporal prior inherent in the T2V model, which effectively helps reconstruct temporal information even without the use of optical flow maps.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Local Information Enhancement Module. We primarily investigate the impact of introducing LIEM in different ways. First, we find that adding LIEM on both spatial and temporal blocks achieves the best results as shown in Table. Second, we consider three connection types as shown in Figure (Left). From visual results in Figure (Right) and quantitative results in Table, we find that position (i) achieves the best results. This phenomenon can be attributed to the fact that, with most weights frozen to preserve the prior, the newly added blocks can influence the model's mapping process. However, the impact at positions (ii) and (iii) is too large, making it difficult for the model to fine-tune and adapt to this change, resulting in poor performance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Dynamic Frequency Loss. First, we investigate the impact of different variants of frequency loss. As shown in Table, "Separate" indicates whether the frequency components are separated into high and low frequency, constraining them individually. "Type" refers to the specific definition of the DF loss: if set to "inverse," a higher weight is given to high frequencies in the early stages and a lower weight to low frequencies; if set to "direct", a higher weight is given to low frequencies initially and a lower weight to high frequencies, which is matching the analysis in Sec. 3.3. As observed, separating the frequency components and prioritizing low-frequency reconstruction early on yield the best perceptual quality while maintaining high fidelity. Second, we explore the optimal settings for $b{(t)}$ and $\alpha$ in $c{(t)}$. As shown in Table, using a linear form for $b{(t)}$ with $\alpha = 2$ for $c{(t)}$ yields the best results. Therefore, we adopt this DF loss configuration for training our model and comparing it with other state-of-the-art methods.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Scaling up with Larger T2V Models. To further validate the effectiveness of T2V diffusion priors for real-world VSR, we replace I2VGen-XL with larger DiT-based T2V models (i.e., CogVideoX ), and evaluate results both quantitatively and qualitatively. Since CogVideoX only supports inputs at 480$\times$`<!-- -->`{=html}720 resolution, we created a new test set by cropping 10 videos from OpenVid-1M to this size. As shown in Table, the powerful CogVideoX models yield consistent improvements across all metrics. Notably, SSIM improves from 0.6944 to 0.7400, and DOVER increases from 0.6609 to 0.7350, marking a substantial enhancement in visual quality. The robust spatio-temporal priors in CogVideoX enable realistic details and clear building structures, while maintaining high temporal consistency. Inspired by scaling law and our findings, we believe larger, more powerful T2V models will further advance VSR tasks.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we present STAR, a real-world VSR framework that leverages T2V diffusion prior to restore videos with fewer artifacts, higher spatial fidelity, and stronger temporal consistency. Specifically, we introduce a Local Information Enhancement Module into the original T2V backbone to improve its ability to handle degradations and reconstruct fine details. Additionally, we propose a Dynamic Frequency Loss that guides the model to focus on restoring different frequency components at each diffusion step, thereby enhancing fidelity. Furthermore, we demonstrate that a powerful T2V model can effectively generate high-quality results in both spatial and temporal dimensions. Extensive experiments show that STAR achieves superior performance in both spatial and temporal quality. We hope our work lays a solid foundation for applying T2V models in real-world VSR and inspires future advancements in the field.
