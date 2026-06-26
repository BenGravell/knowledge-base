<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Exploiting Diffusion Prior for Real-World Image Super-Resolution

Topics include Image super-resolution, Real-world super-resolution, Blind restoration, Diffusion models, Stable diffusion, Generative prior, Time-aware encoder, Feature wrapping, StableSR.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

StableSR adapts a pretrained text-to-image diffusion model for blind real-world super-resolution while keeping the synthesis model fixed. Its time-aware encoder, controllable feature wrapping, and progressive aggregation sampling make the diffusion prior more practical for fidelity-controlled restoration at arbitrary image sizes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel approach to leverage prior knowledge encapsulated in pre-trained text-to-image diffusion models for blind super-resolution (SR). Specifically, by employing our time-aware encoder, we can achieve promising restoration results without altering the pre-trained synthesis model, thereby preserving the generative prior and minimizing training cost. To remedy the loss of fidelity caused by the inherent stochasticity of diffusion models, we employ a controllable feature wrapping module that allows users to balance quality and fidelity by simply adjusting a scalar value during the inference process. Moreover, we develop a progressive aggregation sampling strategy to overcome the fixed-size constraints of pre-trained diffusion models, enabling adaptation to resolutions of any size. A comprehensive evaluation of our method using both synthetic and real-world benchmarks demonstrates its superiority over current state-of-the-art approaches. Code and models are available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We have seen significant advancements in diffusion models for the task of image synthesis. Existing studies demonstrate that the diffusion prior, embedded in synthesis models like Stable Diffusion, can be applied to various downstream content creation tasks, including image and video editing. In this study, we extend the exploration beyond the realm of content creation and examine the potential benefits of using diffusion prior for super-resolution (SR). This low-level vision task presents an additional non-trivial challenge, as it requires high image fidelity in its generated content, which stands in contrast to the stochastic nature of diffusion models.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common solution to the challenge above involves training a SR model from scratch. To preserve fidelity, these methods use the low-resolution (LR) image as an additional input to constrain the output space. While these methods have achieved notable success, they often demand significant computational resources to train the diffusion model. Moreover, training a network from scratch can potentially jeopardize the generative priors captured in synthesis models, leading to suboptimal performance in the final network. These limitations have inspired an alternative approach, which involves incorporating constraints into the reverse diffusion process of a pre-trained synthesis model. This paradigm avoids the need for model training while leveraging the diffusion prior. However, designing these constraints assumes knowing the image degradations as a priori, which are typically unknown and complex. Consequently, such methods exhibit limited generalizability.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this study, we present StableSR, an approach that preserves pre-trained diffusion priors without making explicit assumptions about the degradations. Specifically, unlike previous works that concatenate the LR image to intermediate outputs, which requires one to train a diffusion model from scratch, our method only needs to fine-tune a lightweight time-aware encoder and a few feature modulation layers for the SR task. When applying diffusion models for SR, the LR condition should provide adaptive guidance for each diffusion step during the restoration process, i.e., stronger guidance at earlier iterations to maintain fidelity and weaker guidance later to avoid introducing degradations. To this end, our encoder incorporates a time embedding layer to generate time-aware features, allowing the features in the diffusion model to be adaptively modulated at different iterations. Besides gaining improved training efficiency, keeping the original diffusion model frozen helps preserve the generative prior, which grants StableSR the capability of generating visually pleasant SR details and avoids overfitting to high-frequency degradations. Our experiments show that both the time-aware property of our encoder and the diffusion prior are crucial for achieving SR performance improvements.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To suppress randomness inherited from the diffusion model as well as the information loss due to the encoding process of the autoencoder, inspired by Codeformer, we apply a controllable feature wrapping module (CFW) with an adjustable coefficient to refine the outputs of the diffusion model during the decoding process of the autoencoder. Unlike CodeFormer, the multiple-step sampling nature of diffusion models makes it hard to finetune the CFW module directly. We overcome this issue by first generating synthetic LR-HR pairs with the diffusion training stage. Then, we obtain the corresponding latent codes using our finetuned diffusion model given the LR images as conditions. In this way, CFW can be trained using the generated data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Applying diffusion models to arbitrary resolutions has remained a persistent challenge, especially for the SR task. A simple solution would be to split the image into patches and process each independently. However, this method often leads to boundary discontinuity in the output. To address this issue, we introduce a progressive aggregation sampling strategy. Inspired by Jiménez, our approach involves dividing the image into overlapping patches and fusing these patches using a Gaussian kernel at each diffusion iteration. This process smooths out the boundaries, resulting in a more coherent output. To avoid altering the output resolution of SR images, the overlapping sizes at the right and bottom boundaries are dynamically adjusted to fit the target resolution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Adapting generative priors for real-world image super-resolution presents an intriguing yet challenging problem, and in this work, we offer a novel approach as a solution. We introduce a fine-tuning method that leverages pre-trained diffusion models without making explicit assumptions about degradations. We address key challenges, such as fidelity and arbitrary resolution, by proposing simple yet effective modules. With our time-aware encoder, controllable feature wrapping module, and progressive aggregation sampling strategy, our StableSR serves as a strong baseline that inspires future research in adopting diffusion priors for restoration tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Methodology", "weight": 1.0} -->

Our method employs diffusion prior for SR. Inspired by the generative capabilities of Stable Diffusion, we use it as the diffusion prior in our work, hence the name StableSR for our method. The main component of StableSR is a time-aware encoder, which is trained along with a frozen Stable Diffusion model to allow for conditioning based on the input image. To further facilitate a trade-off between realism and fidelity, depending on user preference, we follow CodeFormer to introduce an optional controllable feature wrapping module. The overall framework of StableSR is depicted in Fig. 2.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

To exploit the prior knowledge of Stable Diffusion for SR, we establish the following constraints when designing our model: 1) The resulting model must have the ability to generate a plausible HR image, conditioned on the observed LR input. This is vital because the LR image is the only source of structural information, which is crucial for maintaining high fidelity. 2) The model should introduce only minimal alterations to the original Stable Diffusion model to prevent disrupting the prior encapsulated within it.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

Feature Modulation. While several existing approaches have successfully controlled the generated semantic structure of a diffusion model via cross-attention, such a strategy can hardly provide detailed and high-frequency guidance due to insufficient inductive bias. To more accurately guide the generation process, we adopt an additional encoder to extract multi-scale features ${\{{\mathbf{F}}^{n}\}}_{n = 1}^{N}$ from the degraded LR image features, and use them to modulate the intermediate feature maps ${\{{\mathbf{F}}_{dif}^{n}\}}_{n = 1}^{N}$ of the residual blocks in Stable Diffusion via spatial feature transformations (SFT): where ${\mathbf{α}}^{n}$ and ${\mathbf{β}}^{n}$ denote the affine parameters in SFT and $\mathcal{M}_{\theta}^{n}$ denotes a small network consisting of several convolutional layers. Here $n$ indices the spatial scale of the UNet architecture in Stable Diffusion.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

During finetuning, we freeze the weights of Stable Diffusion and train only the encoder and SFT layers. This strategy allows us to insert structural information extracted from the LR image without destroying the generative prior captured by Stable Diffusion.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

Time-aware Guidance. We find that incorporating temporal information through a time-embedding layer in our encoder considerably enhances both the quality of generation and the fidelity to the ground truth, since it can adaptively adjust the condition strength derived from the LR features. Here, we analyze this phenomenon from a signal-to-noise ratio (SNR) standpoint and later quantitatively and qualitatively validate it in the ablation study.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

During the generation process, the SNR of the produced image progressively increases as noise is incrementally removed. A recent study indicates that image content is rapidly populated when the SNR approaches $5\text{e}^{- 2}$. In line with this observation, we notice that the time embedding enables the conditional encoder to provide stronger guidance within the range where the signal-to-noise ratio (SNR) hits $5\text{e}^{- 2}$. This is essential because the content generated at this stage significantly influences the super-resolution performance of our method. To further substantiate this, since the conditional features are inserted into the diffusion prior via SFT layers, we employ the cosine similarity between the features of Stable Diffusion before and after the SFT to measure the condition strength provided by the encoder. The cosine similarity values at different timesteps are plotted in Fig. 3-(a). As can be observed, the cosine similarity reaches its minimum value around an SNR of $5\text{e}^{- 2}$, indicative of the strongest conditions imposed by the encoder.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

In addition, we also depict the feature maps extracted from our specially designed encoder in Fig. 3-(b). It is noticeable that the features around the SNR point of $5\text{e}^{- 2}$ are sharper and contain more detailed image structures. We hypothesize that these adaptive feature conditions can furnish more comprehensive guidance for SR.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

Color Correction. Diffusion models can occasionally exhibit color shifts, as noted. To address this issue, we perform color normalization on the generated image to align its mean and variance with those of the LR input.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

In particular, if we let $\mathbf{x}$ denote the LR input and $\hat{\mathbf{y}}$ represent the generated HR image, the color-corrected output, $\mathbf{y}$, is calculated as follows: where $c \in {\{ r,g,b\}}$ denotes the color channel, ${\mathbf{μ}}_{\hat{\mathbf{y}}}^{c}$ and ${\mathbf{σ}}_{\hat{\mathbf{y}}}^{c}$ (or ${\mathbf{μ}}_{x}^{c}$ and ${\mathbf{σ}}_{x}^{c}$) are the mean and standard variance estimated from the $c$-th channel of $\hat{\mathbf{y}}$ (or $\mathbf{x}$), respectively. We find that this simple correction suffices to remedy the color difference.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

Though pixel color correction via channel matching can improve color fidelity, we notice that it may suffer from limited color correction ability due to the lack of pixel-wise controllability. The main reason is that it only introduces global statistics, i.e., channel-wise mean and variance of the input for color correction, ignoring pixel-wise semantics. Besides adopting color correction in the pixel domain, we further propose wavelet-based color correction for better visual performance in some cases. Wavelet color correction directly introduces the low-frequency part from the input since the color information belongs to the low-frequency components, while the degradations are mostly high-frequency components. In this way, we can improve the color fidelity of the results without perceptibly affecting the generated quality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

Given any image $\mathbf{I}$, we extract its high-frequency component ${\mathbf{H}}^{i}$ and low-frequency component ${\mathbf{L}}^{i}$ at the $i$-th ($1 \leq i \leq l$) scale via the wavelet decomposition, i.e., where ${\mathbf{L}}^{0} = {\mathbf{I}}$, $\mathcal{C}_{i}$ denotes the convolutional operator with a dilation of $2^{i}$, and $k$ is the convolutional kernel defined as: By denoting the $l$-th low-frequency and high-frequency components of $\mathbf{x}$ (or $\hat{\mathbf{y}}$) as ${\mathbf{L}}_{x}^{l}$ and ${\mathbf{H}}_{x}^{l}$ (or

<!-- chunk {"id": "body-0021", "role": "body", "section": "Guided Finetuning with Time Awareness", "weight": 1.0} -->

${\mathbf{L}}_{y}^{l}$ and ${\mathbf{H}}_{y}^{l}$), the desired HR output $\mathbf{y}$ is formulated as follows: Intuitively, we replace the low-frequency component ${\mathbf{L}}_{y}^{l}$ of $\hat{\mathbf{y}}$ with ${\mathbf{L}}_{x}^{l}$ to correct the color bias. By default, we adopt color correction in the pixel domain for simplicity.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Fidelity-Realism Trade-off", "weight": 1.0} -->

Although the output of the proposed approach is visually compelling, it often deviates from the ground truth due to the inherent stochasticity of the diffusion model. Drawing inspiration from CodeFormer, we introduce a Controllable Feature Wrapping (CFW) module to flexibly manage the balance between realism and fidelity. Unlike CodeFormer, there are multiple sampling steps for generating a sample during inference and we cannot finetune the CFW module directly. To overcome this problem, we first generate synthetic LR-HR pairs following the same degradation pipeline with the diffusion training stage. Then, the latent codes ${\mathbf{Z}}_{0}$ can be obtained using our finetuned diffusion model given the LR images as conditions. Finally, CFW can be trained using the generated data.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Fidelity-Realism Trade-off", "weight": 1.0} -->

Since Stable Diffusion is implemented in the latent space of an autoencoder, it is natural to leverage the encoder features of the autoencoder to modulate the corresponding decoder features for further fidelity improvement. Let ${\mathbf{F}}_{e}$ and ${\mathbf{F}}_{d}$ be the encoder and decoder features, respectively. We introduce an adjustable coefficient $w \in {\lbrack 0,1\rbrack}$ to control the extent of modulation: where $\mathcal{C}{(\cdot;{\mathbf{θ}})}$ represents convolution layers with trainable parameter $\mathbf{θ}$. The overall framework is shown in Fig. 2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Fidelity-Realism Trade-off", "weight": 1.0} -->

In this design, a small $w$ exploits the generation capability of Stable Diffusion, leading to outputs with high realism under severe degradations. In contrast, a large $w$ allows stronger structural guidance from the LR image, enhancing fidelity. We observe that $w = \, 0.5$ achieves a good balance between quality and fidelity. Note that we only train CFW in this particular stage. In practice, we notice that CFW involves additional GPU memory and the improvement can be subtle in some cases. Thus, we make it optional for different real-world applications.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Aggregation Sampling", "weight": 1.0} -->

Due to the heightened sensitivity of the attention layers in Stable Diffusion with respect to the image resolution, it tends to produce inferior outputs for resolutions differing from its training settings, specifically $512 \times 512$. This, in effect, constrains the practicality of StableSR.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Aggregation Sampling", "weight": 1.0} -->

A common workaround involves splitting the larger image into several overlapping smaller patches and processing each individually. While this strategy often yields good results for conventional CNN-based SR methods, it is not directly applicable to the diffusion paradigm. This is because discrepancies between patches are compounded and magnified over the course of diffusion iterations. A typical failure case is illustrated in Fig. 4.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Aggregation Sampling", "weight": 1.0} -->

Inspired by Jiménez, we apply a progressive patch aggregation sampling algorithm to handle images of arbitrary resolutions. Specifically, we begin by encoding the LR image into a latent feature map ${\mathbf{F}} \in \mathcal{R}^{h \times w}$, which is then subdivided into $M$ overlapping small patches ${\{{\mathbf{F}}_{\Omega_{n}}\}}_{n = 1}^{M}$, each with a resolution of $64 \times 64$ - matching the training resolution^11^1The downsampling scale factor of the autoencoder in Stable Diffusion is $8 \times$.. Here, $\Omega_{n}$ is the coordinate set of the $n$th patch in $\mathbf{F}$. During each timestep in the reverse sampling, each patch is individually processed through StableSR, with the processed patches subsequently aggregated.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Aggregation Sampling", "weight": 1.0} -->

To integrate overlapping patches, a weight map ${\mathbf{w}}_{\Omega_{n}} \in \mathcal{R}^{h \times w}$ whose entries follow up a Gaussian filter in $\Omega_{n}$ and 0 elsewhere is generated for each patch ${\mathbf{F}}_{\Omega_{n}}$. Overlapping pixels are then weighted in accordance with their respective Gaussian weight maps. In particular, we follow Jiménez to define a padding function $f{( \cdot )}$ that expands any patch of size $64 \times 64$ to the resolution of $h \times w$ by filling zeros outside the region $\Omega_{n}$. This procedure is reiterated until reaching the final iteration.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Aggregation Sampling", "weight": 1.0} -->

Based on $\epsilon_{\mathbf{θ}}{({\mathbf{Z}}^{(t)},{\mathbf{F}},t)}$, we can obtain ${\mathbf{Z}}^{({t - 1})}$ according to the sampling procedure, denoted as ${Sampler}{({\mathbf{Z}}^{(t)},{\epsilon_{\mathbf{θ}}{({\mathbf{Z}}^{(t)},{\mathbf{F}},t)}})}$, in the diffusion model. Subsequently, we re-split ${\mathbf{Z}}^{({t - 1})}$ into over-lapped patches and repeat the above steps until $t = 1$. The whole process is summed up in Algorithm 1. Our experiments suggest that this progressive aggregation method substantially mitigates discrepancies in the overlapped regions, as depicted in Fig. 4. More details can be found in the supplementary material.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Aggregation Sampling", "weight": 1.0} -->

1:Cropped Regions {Ωn}n = 1M, diffusion steps T, LR latent features F. 2:Initialize wΩn and $\hat{\mathbf{w}}$ Algorithm 1 Progressive Patch Aggregation

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

StableSR is built based on Stable Diffusion 2.1-base^22^2 Our time-aware encoder is similar to the contracting path of the denoising U-Net in Stable Diffusion but is much more lightweight ($\sim$`<!-- -->`{=html}105M, including SFT layers). SFT layers are inserted in each residual block of Stable Diffusion for effective control. We finetune the diffusion model of StableSR for $117$ epochs with a batch size of $192$, and the prompt is fixed as null. We follow Stable Diffusion to use Adam optimizer and the learning rate is set to $5 \times 10^{- 5}$. The training process is conducted on $512 \times 512$ resolution with 8 NVIDIA Tesla 32G-V100 GPUs. For inference, we adopt DDPM sampling with 200 timesteps. To handle images with arbitrary sizes, we adopt the proposed aggregation sampling strategy for images beyond $512 \times 512$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

As for images under $512 \times 512$, we first enlarge the LR images such that the shorter side has a length of $512$ and rescale the results back to target resolutions after generation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

To train CFW, we first generate 100k synthetic LR-HR pairs with $512 \times 512$ resolution following the degradation pipeline in Real-ESRGAN. Then, we adopt the finetuned diffusion model to generate the corresponding latent codes ${\mathbf{Z}}_{0}$ given the above LR images as conditions. The training losses are almost the same as the autoencoder used in LDM, except that we use a fixed adversarial loss weight of $0.025$ rather than a self-adjustable one.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Settings", "weight": 1.0} -->

Training Datasets. We adopt the degradation pipeline of Real-ESRGAN to synthesize LR/HR pairs on DIV2K, DIV8K, Flickr2K and OutdoorSceneTraining datasets. We additionally add 5000 face images from the FFHQ dataset for general cases.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Settings", "weight": 1.0} -->

Testing Datasets. We evaluate our approach on both synthetic and real-world datasets. For synthetic data, we follow the degradation pipeline of Real-ESRGAN and generate 3k LR-HR pairs from DIV2K validation set. The resolution of LR is $128 \times 128$ and that of the corresponding HR is $512 \times 512$. Note that for StableSR, the inputs are first upsampled to the same size as the outputs before inference. For real-world datasets, we follow common settings to conduct comparisons on RealSR, DRealSR and DPED-iPhone. We further collect 40 images from the Internet for comparison.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Settings", "weight": 1.0} -->

Evaluation Metrics. For benchmarks with paired data, i.e., DIV2K Valid, RealSR and DRealSR, we employ various perceptual metrics including LPIPS^66^6We use LPIPS-ALEX by default., FID, CLIP-IQA and MUSIQ to evaluate the perceptual quality of generated images. PSNR and SSIM scores (evaluated on the luminance channel in YCbCr color space) are also reported for reference. Since ground-truth images are unavailable in DPED-iPhone, we follow existing methods to report results on no-reference metrics i.e., CLIP-IQA and MUSIQ for perceptual quality evaluation. Besides, we further conduct a user study on $16$ real-world images to verify the effectiveness of our approach against existing methods.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Comparison with Existing Methods", "weight": 1.0} -->

Quantitative Comparisons. We first show the quantitative comparison on the synthetic DIV2K validation set and three real-world benchmarks. As shown in Table 1, our approach outperforms state-of-the-art SR methods in terms of multiple perceptual metrics, including FID, CLIP-IQA and MUSIQ. Specifically, on synthetic benchmark DIV2K Valid, our StableSR ($w = 0.5$) achieves a $24.44$ FID score, which is $7.7\%$ lower than LDM and at least $32.9\%$ lower than other GAN-based methods. Besides, our StableSR ($w = 0.5$) achieves the highest CLIP-IQA scores on the two commonly used real-world benchmarks, suggesting the superiority of StableSR. While we notice that StableSR achieves inferior performance on metrics including PSNR, SSIM and LPIPS compared with non-diffusion methods, these metrics only reflect certain aspects of performance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Comparison with Existing Methods", "weight": 1.0} -->

Besides, the previous non-diffusion methods tend to directly use $\ell_{2}$ losses and perceptual loss between the predictions and the corresponding ground truths for training, which are closely related to the calculation of PSNR and LPIPS, respectively. Different from previous methods, diffusion models only apply $\ell_{2}$ loss between the predicted and the ground-truth noise. We conjecture this is an important factor that makes diffusion models less competitive on these metrics, as observed by the recent work. Moreover, previous methods usually fail to restore faithful textures and generate blurry results, as shown in Fig. 5. In contrast, our StableSR is capable of generating sharp images with realistic details.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Comparison with Existing Methods", "weight": 1.0} -->

Qualitative Comparisons. To demonstrate the effectiveness of our method, we present visual results on real-world images from both real-world benchmarks and the internet in Fig. 5 and Fig. 6. It is observed that StableSR outperforms previous methods in both artifact removal and detail generation. Specifically, StableSR is able to generate faithful details, as shown in the first row of Fig. 5, while other methods either show blurry results (DASR, BSRGAN, Real-ESRGAN+, LDM) or unnatural details (RealSR, FeMaSR). Moreover, as shown in the fourth row of Fig. 5, StableSR generates sharp edges without obvious degradations, whereas other state-of-the-art methods generate blurry results. Figure 6 further demonstrates the superiority of StableSR on images beyond $512 \times 512$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Comparison with Existing Methods", "weight": 1.0} -->

Comparison with Concurrent Diffusion Applications. We notice that recent concurrent works can also be adopted for image SR. While IF_III upscaler is a super-resolution model training from scratch, ControlNet-tile also adopts a diffusion prior. The key technical differences regarding to the use of diffusion prior between our StableSR and ControlNet-tile lie in the different adaptor designs, i.e., ControlNet-tile adopts a trainable copy of the encoding layers in Stable Diffusion, whilst StableSR does not rely on any layer copies of the fixed diffusion prior, thus can be more flexible. Specifically, we introduce a time-aware encoder to modulate the feature maps of the fixed diffusion prior. This time-aware encoder is more lightweight than the copied layers in ControlNet-tile, i.e., 105M vs. 364M. As a result, StableSR is also faster than ControlNet-tile in terms of inference speed, i.e., 10.37s vs. 14.47s for 50 sampling steps. Here, we further conduct comparisons with these methods on real-world images.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison with Existing Methods", "weight": 1.0} -->

For fair comparisons, we use DDIM sampling with $\eta = 1.0$ and timestep $200$ for all the methods, and the seed is fixed to $42$. We further set $w = 0.0$ in StableSR to avoid additional improvement due to CFW. For ControlNet-tile, we generate additional prompts using stable-diffusion-webui^88^8 for better performance. For IF_III upscaler, we follow official examples to set noise level to $100$ w/o prompts. As shown in Fig. 8, ControlNet-tile shows poor fidelity due to the lack of specific designs for SR. Compared with IF_III upscaler, the proposed StableSR is capable of generating more faithful details with sharper edges, e.g., the text in the first row, the tiger's nose in the third row and the wing of the butterfly in the last row of Fig. 9. Note that IF_III upscaler is trained from scratch, which requires significant computational resources. The visual comparisons suggest the superiority of StableSR.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Effectiveness of Network Design. In StableSR, a time-aware encoder and SFT layers are adopted to harness the diffusion prior. While concurrent works ControlNet and T2I-Adaptor propose to exploit diffusion prior to image generation, their effectiveness for image super-resolution is underexplored. Here, we further compare our design with theirs. Specifically, we first retrain a ControlNet for image super-resolution using the same diffusion prior and training pipelines as ours. Recall that we have shown the superiority of StableSR compared with ControlNet-tile in Fig. 8. With retraining, the performance of ControlNet for super-resolution can be improved, but still inferior to ours as shown in Fig. 11. To compare with T2I-Adapter, while we have already verified the effectiveness of time-aware guidance, we further add a baseline w/o SFT layers by first mapping the features to the same shape as the prior features and then adding them together.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Note that such strategy can be regarded as a special case of SFT layers with ${{\mathbf{α}}^{n} = 0},{{\mathbf{β}}^{n} = 0}$ in Eq.. As shown in Fig. 12, SFT layers slightly improve the training performance on the validation sets in terms of LPIPS scores during training.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Importance of Time-aware Guidance and Color Correction. We then investigate the significance of time-aware guidance and color correction. Recall that in Fig. 3, we already show that the time-aware guidance allows the encoder to adaptively adjust the condition strength. Here, we further verify its effectiveness on real-world benchmarks. As shown in Table 3, removing time-aware guidance (i.e., removing the time-embedding layer) or color correction both lead to worse SSIM and LPIPS. Moreover, the comparisons in Fig. 13 also indicate inferior performance without the above two components, suggesting the effectiveness of time-aware guidance and color correction. In addition to directly adopting color correction in the pixel domain, our proposed wavelet color correction can further boost the visual quality, as shown in Fig. 14, which may further facilitate the practical use. Note that technically, the wavelet transform may introduce halo effects, though we do not observe this phenomenon during our experiments.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Pixel Color cor. Wavelet Color cor.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Flexibility of Fidelity-realism Trade-off. Our CFW module inspired by CodeFormer allows a flexible realism-fidelity trade-off. In particular, given a controllable coefficient $w$ with a range of $\lbrack 0,1\rbrack$, CFW with a small $w$ tends to generate a realistic result, especially for large degradations, while CFW with a larger $w$ improves the fidelity. As shown in Table 4, compared with StableSR ($w = 0.0$), StableSR with larger values of $w$ (e.g., 0.75) achieves higher PSNR and SSIM on all three paired benchmarks, indicating better fidelity. In contrast, StableSR ($w = 0.0$) achieves better perceptual quality with higher CLIP-IQA scores and MUSIQ scores. Similar phenomena can also be observed in Fig. 15. We further observe that a proper $w$ can lead to improvement in both fidelity and perceptual quality.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Specifically, StableSR ($w = 0.5$) shows comparable PSNR and SSIM with StableSR ($w = 1.0$) but achieves better perceptual metric scores in Table 4. Hence, we set the coefficient $w$ to 0.5 by default for trading between quality and fidelity. We observe that CFW necessitates extra GPU memory. Consequently, we designate it as an optional feature for varying applications.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Number of Inference step Table 5: Complexity comparison of model complexity. All methods are evaluated on 128 × 128 input images for 4x SR using an NVIDIA Tesla 32G-V100 GPU. The runtime is averaged by ten runs with a batch size of 1.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Complexity Comparison", "weight": 1.0} -->

StableSR is a diffusion-based approach and requires multi-step sampling for image generation. As shown in Table 5, when the number of sampling steps is set to 200, StableSR needs 15.16 seconds to generate a $512 \times 512$ image on one NVIDIA Tesla 32G-V100 GPU. This is comparable to IF_III upscaler but slower than GAN-based SR methods such as Real-ESRGAN+ and SwinIR-GAN, which require only a single forward pass. Fast sampling strategy and model distillation are two promising solutions to improve efficiency. Another viable remedy is to shorten the chain of diffusion process. As for trainable parameters, StableSR has $149.91$M trainable parameters, which is only 11.50% of the full model and less than IF_III, i.e., 473.40M. The trainable parameters can be further decreased with more careful design, e.g., adopting lightweight architectures or network pruning. Such exploration is beyond the scope of this paper.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Inference Strategies", "weight": 1.0} -->

The proposed StableSR already demonstrates superior performance quantitatively and qualitatively on both synthetic and real-world benchmarks, as shown in Sec. 4. Here, we discuss several effective strategies during the sampling process that can further boost the inference performance without additional finetuning.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Classifier-free Guidance with Negative Prompts", "weight": 1.0} -->

The default StableSR is trained with null prompts. Interestingly, we observe that StableSR can react to prompts, especially negative prompts. We examine the use of classifier-free guidance with negative prompts to further improve the visual quality during sampling. Given two StableSR models conditioned on null prompts $\epsilon_{\mathbf{θ}}{({\mathbf{Z}}^{(t)},{\mathbf{F}},{\lbrack\rbrack},t)}$ and negative prompts $\epsilon_{\mathbf{θ}}{({\mathbf{Z}}^{(t)},{\mathbf{F}},{\mathbf{c}},t)}$, respectively, the new sampling process can be performed using a linear combination of the estimations with a guidance scale $s$: where $\mathbf{c}$ is the negative prompt for guidance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Classifier-free Guidance with Negative Prompts", "weight": 1.0} -->

According to Eq., it is worth noting that $s = 0$ is equivalent to directly using negative prompts without guidance, and $s = 1$ is equivalent to our default settings with the null prompt.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Classifier-free Guidance with Negative Prompts", "weight": 1.0} -->

We compare the performance of StableSR with various positive prompts, i.e., "(masterpiece:2), (best quality:2), (realistic:2), (very clear:2)", and "Good photo.", and negative prompts, i.e., (a) "3d, cartoon, anime, sketches, (worst quality:2), (low quality:2)", and (b) "Bad photo.". As shown in Table 6, different prompts lead to diverse metric scores. Specifically, the classifier-free guidance with negative prompts shows a significant influence on the metrics, i.e., higher guidance scales lead to higher CLIP-IQA and MUSIQ scores, indicating sharper results. Similar phenomena can also be observed in Fig. 16. However, an overly strong guidance, e.g., $s = 7.5$ can result in oversharpening.

<!-- chunk {"id": "body-0054", "role": "body", "section": "StableSR with SD-Turbo", "weight": 1.0} -->

The default sampler of StableSR is DDPM with 200 sampling steps. Though effective, the sampling process can be time-consuming compared with non-diffusion approaches as shown in Table 5. In practice, we observe that StableSR is capable of generating high-quality results much faster using advanced samplers in fewer sampling steps. Specifically, DDIM enables StableSR to generate results with faithful details in 20 steps. Moreover, StableSR can be further applied to SD-turbo w/o further finetuning. As shown in Fig. 17, StableSR equipped with SD-turbo can generate high-quality results with only 4 steps, significantly reducing the inference time, i.e., 0.83s as shown in Table 5, which is 6.3 times faster than LDM with 200 sampling steps, while still remarkably outperforming popular GAN-based methods and LDM. Notably, directly speeding up LDM using existing fast sampling approaches, i.e., DDIM will lead to a severe performance drop as shown in Fig. 17.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Limitations", "weight": 1.5} -->

Though benefiting from the diffusion prior, StableSR also shares similar limitations with it. Specifically, StableSR may struggle in handling small texts, faces and patterns as shown in Fig. 18. While these cases are challenging for existing generic super-resolution approaches including StableSR, we believe adopting a more powerful diffusion prior and training on more high-quality data can help. We leave these as future work.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Motivated by the rapid development of diffusion models and their wide applications to downstream tasks, this work discusses an important yet underexplored problem of how diffusion prior can be adopted for super-resolution. In this paper, we present StableSR, a new way to exploit diffusion prior for real-world SR while avoiding source-intensive training from scratch. We devote our efforts to tackling the well-known problems, such as high computational cost and fixed resolution, and propose respective solutions, including the time-aware encoder, controllable feature wrapping module, and progressive aggregation sampling scheme. Extensive experiments are conducted for evaluation and effective inference strategies are further provided to facilitate practical applications. We believe that our exploration would lay a good foundation in this direction, and our proposed StableSR could provide useful insights for future works.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgement: This study is supported by the National Research Foundation, Singapore under its AI Singapore Programme, RIE2020 Industry Alignment Fund Industry Collaboration Projects (IAF-ICP) Funding Initiative, as well as cash and in-kind contribution from the industry partner(s). We sincerely thank Yi Li for providing valuable advice and building the WebUI implementation^1010^10 of our work. We also thank the continuous interest and contributions from the community.
