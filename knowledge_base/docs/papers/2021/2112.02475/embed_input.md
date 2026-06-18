<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Deblurring via Stochastic Refinement

Topics include Diffusion models, Benchmarks, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Image deblurring is an ill-posed problem with multiple plausible solutions for a given input image. However, most existing methods produce a deterministic estimate of the clean image and are trained to minimize pixel-level distortion. These metrics are known to be poorly correlated with human perception, and often lead to unrealistic reconstructions. We present an alternative framework for blind deblurring based on conditional diffusion models. Unlike existing techniques, we train a stochastic sampler that refines the output of a deterministic predictor and is capable of producing a diverse set of plausible reconstructions for a given input. This leads to a significant improvement in perceptual quality over existing state-of-the-art methods across multiple standard benchmarks. Our predict-and-refine approach also enables much more efficient sampling compared to typical diffusion models. Combined with a carefully tuned network architecture and inference procedure, our method is competitive in terms of distortion metrics such as PSNR. These results show clear benefits of our diffusion-based method for deblurring and challenge the widely used strategy of producing a single, deterministic reconstruction.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Image deblurring is a long-standing problem in computer vision. Various conditions such as moving objects, camera shakes, or an out-of-focus lens may contribute to blurring artifacts. Single image deblurring is a highly ill-posed inverse problem where multiple plausible sharp images could lead to the very same blurry observation. Nonetheless, most existing methods produce a single deterministic estimate of the clean image.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional methods formulate deblurring as a variational optimization problem and find a solution that satisfies closeness to certain image and/or blur kernel prior. With the emergence of deep learning, convolutional neural networks (CNNs) have become the de-facto standard for deblurring models. Typically, these CNNs are trained with simulated sharp-blurry image pairs through supervised learning. Minimizing $L_{1}$ or $L_{2}$ pixel loss is perhaps the most widely adopted approach for training such models. These losses provide a straightforward learning objective and optimize for the popular PSNR (peak signal-to-noise-ratio) metric. Unfortunately, PSNR and other distortion metrics are well-known to only partially correspond to human perception and can actually lead to algorithms with visibly lower quality in the reconstructed images. To alleviate this problem, recent works introduced additional loss terms that seek to improve the quality of generated images under metrics that represent human perception more reliably. Training networks to go from corrupted images to a known ground truth in a supervised way belongs in the family of end-to-end methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These methods perform very well in-distribution, but can be quite fragile to distributional shifts or changes in the corruption process.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A second body of work has focused on using deep generative models to solve inverse problems. For deblurring, Generative Adversarial Networks (GANs) have been successfully applied with competitive performance. GAN-based restoration methods train the deblurring network with an adversarial loss to make the restored images more perceptually plausible. However the proposed methods so far have been deterministic, and adversarial losses often introduce artifacts not present in the original clean image, leading to large distortion (*e.g*. for super-resolution).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we adopt a different perspective and view deblurring as a conditional generative modeling task, where we seek to generate diverse samples from the posterior distribution. Specifically, we introduce a "predict-and-refine" conditional diffusion model, where a deterministic data-adaptive predictor is jointly trained with a stochastic sampler that refines the output of the said predictor (see Fig. 2).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our predict-and-refine approach enables more efficient sampling compared to the standard diffusion model. This formulation also naturally leads to a stochastic model capable of producing realistic images without sacrificing pixel-level distortion. To the best of our knowledge, this is the first blind deblurring technique that leverages a deep generative model and is capable of producing diverse samples.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, our method produces a variety of plausible and photo-realistic results, while achieving state-of-the-art performance under many quantitative metrics in terms of both distortion and perceptual quality across multiple standard datasets. In addition, by aggregating a different number of generated deblurred samples, our framework allows us to conveniently traverse the Perception-Distortion curve as shown in Fig. 1, without any expensive retraining or finetuning. These results show clear benefits of stochastic diffusion-based methods for deblurring and challenge the currently dominant strategy of producing deterministic reconstructions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

Diffusion probabilistic model is a latent variable model specified by a $T$-step Markov chain $({\mathbf{x}}_{0},{\mathbf{x}}_{1},\ldots,{\mathbf{x}}_{T})$ called the diffusion process. It starts from a clean data sample ${\mathbf{x}}_{0} \in {\mathbb{R}}^{d}$ and repeatedly injects Gaussian noise according to the transition kernel $q{(\left. {\mathbf{x}}_{t} \middle| {\mathbf{x}}_{t - 1} \right.)}$

<!-- chunk {"id": "body-0011", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

where $\alpha_{t} \in {}$ for all $t = {1,\ldots,T}$. The noise schedule ${\mathbf{α}}_{1:T} \triangleq {(\alpha_{1},\ldots,\alpha_{T})}$ is a hyperparameter that controls the variance of noise added at each step. The latent variables ${\mathbf{x}}_{1:T}$ have the same dimensionality as the original data sample ${\mathbf{x}}_{0}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

While this particular choice of diffusion process may seem arbitrary, it results in closed-form expressions for the following distributions: the marginal^11^1For notational brevity, we use the term "marginal" to include distributions conditioned on ${\mathbf{x}}_{0}$. distribution $q{(\left. {\mathbf{x}}_{t} \middle| {\mathbf{x}}_{0} \right.)}$ and the reverse diffusion step $q{(\left. {\mathbf{x}}_{t - 1} \middle| {{\mathbf{x}}_{t},{\mathbf{x}}_{0}} \right.)}$. Writing ${\overline{\alpha}}_{t} \triangleq {\prod_{j = 1}^{t}\alpha_{j}}$, we get

<!-- chunk {"id": "body-0013", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

The marginal distribution in Eq. 2 allows us to sample a partially noisy image ${\mathbf{x}}_{t}$ at an arbitrary time step, and the reverse diffusion step in Eq. 3 is a stochastic denoising procedure that tells us how to reverse a single diffusion step by sampling a slightly less noisy image ${\mathbf{x}}_{t - 1}$ from ${\mathbf{x}}_{t}$. The ability to sample from arbitrary marginals is important to make training of a DPM practical, as the training objective relies on it (see Eq. 5).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

We note that the diffusion process defined here has no learnable parameter. It is a fixed process that gradually destroys the original signal ${\mathbf{x}}_{0}$ and produces ${\mathbf{x}}_{T}$ that looks indistinguishable from pure Gaussian noise given a sufficiently large $T$. Thus, if we could apply the reverse diffusion step $T$ times starting from pure Gaussian noise, we would obtain a clean sample ${\mathbf{x}}_{0}$. However this is not possible because the reverse diffusion step itself requires access to ${\mathbf{x}}_{0}$, which is exactly what we are trying to generate.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

Reverse process and denoiser network. A key component of DPM is the denoiser network $f_{\theta}$ that tries to estimate ${\mathbf{x}}_{0}$ from the partially noisy image ${\mathbf{x}}_{t}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

This defines a Markov chain that runs backwards in time from ${\mathbf{x}}_{T}$ to ${\mathbf{x}}_{0}$, which we call the reverse process. The goal of DPM is to train $f_{\theta}$ to make $p_{\theta}{(\left. {\mathbf{x}}_{t - 1} \middle| {\mathbf{x}}_{t} \right.)}$ as close to the true reverse diffusion step $q{(\left. {\mathbf{x}}_{t - 1} \middle| {{\mathbf{x}}_{t},{\mathbf{x}}_{0}} \right.)}$ as possible. This is done by optimizing $f_{\theta}$ to maximize the variational lower bound of the marginal likelihood ${\log p_{\theta}}{({\mathbf{x}})}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

Continuous noise level. Chen *et al*. proposes a modified formulation based on a continuous noise level $\overline{\alpha}$, which we also adopt. An important property of this formulation is that it allows us to sample from the model using a noise schedule ${\mathbf{α}}_{1:T}$ different from the one used during training. This flexibility enables us to control the trade-off between the distortion and the perceptual quality of generated samples without having to retrain the model, as we show later.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

Conditional DPM. So far we have defined a DPM that is trained to model the unconditional data distribution. For conditional models that must estimate $p{(\left. {\mathbf{x}} \middle| {\mathbf{y}} \right.)}$, we make $f_{\theta}$ accept $\mathbf{y}$ as the conditioning input, as was done. This way, the iterative denoising procedure becomes dependent on $\mathbf{y}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Diffusion Probabilistic Models", "weight": 1.0} -->

Sampling from a DPM. As mentioned earlier, sampling an image from a DPM is done by running the reverse process. Given some inference-time noise schedule ${\overline{\alpha}}_{1:T}$, we start from a pure Gaussian noise ${\mathbf{x}}_{T} \sim {\mathcal{N}{(\mathbf{0},{\mathbf{I}}_{d})}}$ and repeatedly apply the reverse process transition $p_{\theta}{(\left. {\mathbf{x}}_{t - 1} \middle| {\mathbf{x}}_{t} \right.)}$ defined in Eq. 4. Notice that this procedure requires a total of $T$ calls to the denoiser network. At the end of this sampling procedure, we are left with a single sample ${\mathbf{x}}_{0}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Predict-and-Refine Diffusion Model", "weight": 1.0} -->

One of the main drawbacks of DPM is the computational cost of generating samples, which may require up to thousands of forward passes of the denoiser network due to the iterative denoising procedure. As such, many recent works have explored alternative sampling strategies that reduce the number of sampling steps.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Predict-and-Refine Diffusion Model", "weight": 1.0} -->

We introduce a simple technique that reduces this cost by exploiting the fact that it is often possible to get a cheap initial guess for conditional generative models. Specifically, we augment our conditional diffusion model with a deterministic initial predictor (Fig. 2), which provides a data-adaptive candidate for the clean image. Then the denoiser network only needs to model the residual.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Predict-and-Refine Diffusion Model", "weight": 1.0} -->

Letting $g_{\theta}$ denote the initial predictor, the new objective becomes: ${L_{\text{Ours}}{(\theta)}} =$

<!-- chunk {"id": "body-0023", "role": "body", "section": "Predict-and-Refine Diffusion Model", "weight": 1.0} -->

We include a pseudocode for the modified sampling procedure in Algorithm 1. Notice that the initial predictor $g_{\theta}$ does not require an extra loss or pretraining because the gradient from the loss flows through $f_{\theta}$ into $g_{\theta}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Predict-and-Refine Diffusion Model", "weight": 1.0} -->

Since the initial predictor runs only once, it is beneficial to keep the denoiser network small by offloading most of the computation to the initial predictor. This leads to much more efficient sampling because any reduction in the computational cost of the denoiser network gets amplified by the number of sampling steps used. We further explore this effect in Sec. 6.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Predict-and-Refine Diffusion Model", "weight": 1.0} -->

0: fθ: Denoiser network, gθ: Initial predictor, y: Blurry input image, α1: T: Noise schedule. 1: xinit ← gθ (y) ⊳ Initial prediction
2: zT ∼ 𝒩 (0,Id) ⊳ Run diffusion sampling
5: ${\mathbf{z}}_{t - 1}\leftarrow{{{\mathbf{μ}}_{t}{({\mathbf{z}}_{t},{f_{\theta}{({\mathbf{z}}_{t},{\overline{\alpha}}_{t},{\mathbf{y}})}})}} + {\beta_{t}\mathbf{\epsilon}_{t}}}$ ⊳ Reverse diffusion step; see Eq. 3
7: return xinit + z0 ⊳ Return the final restoration
Algorithm 1 Predict-and-refine diffusion sampling.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Perception-Distortion Trade-off", "weight": 1.0} -->

As explained in Sec. 3, conditioning the diffusion model on continuous noise level makes it possible to use a different noise schedule during inference. We observe that using many steps with small noise level generally leads to better perceptual quality, and using fewer steps with large noise level leads to lower distortion.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Perception-Distortion Trade-off", "weight": 1.0} -->

For our experiments, we run a small grid search over the noise schedule hyperparameters and use the model with the best LPIPS score (labeled "Ours"). We emphasize that this inference-time hyperparameter tuning is cheap as it does not involve retraining or finetuning the model itself.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Perception-Distortion Trade-off", "weight": 1.0} -->

Sample averaging. Our framework also provides a principled alternative to geometric self-ensemble. Since our stochastic sampler is trained to learn the target posterior $p{(\left. {\mathbf{x}} \middle| {\mathbf{y}} \right.)}$, we can average multiple samples from our model to approximate the conditional mean ${\mathbb{E}}\left\lbrack {\mathbf{x}} \middle| {\mathbf{y}} \right\rbrack$, *i.e*. the minimum mean squared error estimator. We thus report results for a second model (labeled "Ours-SA") that returns the average of multiple samples.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Perception-Distortion Trade-off", "weight": 1.0} -->

Traversing the Perception-Distortion curve. By appropriately setting the inference-time hyperparameters mentioned above (sampling steps $T$, noise schedule ${\overline{\alpha}}_{1:T}$, and sample averaging), we can smoothly traverse the P-D curve as shown in Fig. 1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Perception-Distortion Trade-off", "weight": 1.0} -->

For example, the LPIPS-optimized model ("Ours") uses a relatively large step count of $T = 500$ without sample averaging to achieve high perceptual quality at a slight cost of PSNR. The distortion-optimized model ("Ours-SA") does the opposite by using $T = 10$ with sample averaging to sacrifice perceptual quality for higher PSNR. Each point on the P-D curve in Fig. 1 thus corresponds to a specific choice of these hyperparameters.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Resolution-agnostic Architecture", "weight": 1.0} -->

Unlike the image benchmarks commonly used to evaluate DPMs, blind deblurring benchmarks contain images with various sizes. To support arbitrary input shapes, we use a fully-convolutional architecture for both initial predictor and denoiser network.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Resolution-agnostic Architecture", "weight": 1.0} -->

Our architecture is based on SR3, which uses a variant of U-Net architecture from with residual blocks replaced with that of BigGAN. To make our model agnostic to image resolution, we removed self-attention, positional encoding, and group normalization. The exact specification of our architecture can be found in Appendix E.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Resolution-agnostic Architecture", "weight": 1.0} -->

We note that, to the best of our knowledge, this is the first time a conditional diffusion model is made to support arbitrary image size. Our preliminary experiments show that the fully-convolutioanl architecture had little to no degradation in sample quality for deblurring at non-native resolutions. Because the denoiser network is a relatively simple U-Net, DPMs provide a particularly convenient choice for conditional image generation that must work on any input size.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Datasets", "weight": 1.0} -->

We train and evaluate our models on two widely-used image deblurring datasets. For a fair comparison, we follow the same setup used by and train our model only using the provided training data.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Datasets", "weight": 1.0} -->

GoPro. GoPro dataset contains 3214 pairs of clean and blurry $1280 \times 720$ images, of which 1111 are reserved for evaluation. These images are generated by recording video clips with high shutter speed, then averaging consecutive frames to simulate blurs caused by slow shutter speed.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Datasets", "weight": 1.0} -->

HIDE. We additionally evaluate our GoPro-trained model on the HIDE dataset, which contains 2025 images also of size $1280 \times 720$. By training and evaluating our model on different datasets, we can test its ability to generalize under a distributional shift.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model Training", "weight": 1.0} -->

We jointly train the initial predictor and denoiser network by minimizing the loss in Eq. 6. Since our model is fully convolutional, we use random $128 \times 128$ crops during training, but apply the model on full-size images for evaluation. We also perform training-time data augmentation with random horizontal/vertical flips and $90{^\circ}$/$180{^\circ}$/$270{^\circ}$ rotations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Model Training", "weight": 1.0} -->

A note on training data. Most currently leading methods only report distortion-based metrics (PSNR and SSIM) and provide pre-trained models for GoPro. Since our work focuses on perceptual quality, we need to compute perceptual metrics ourselves using outputs from other methods. Thus to ensure a fair comparison, we are limited to using models trained on the GoPro dataset, as it is the only dataset with widely available pre-trained models. Nonetheless, we provide additional results and the details of how we obtained the outputs of other methods in Appendices H and F.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Evaluation Metrics. We evaluate our method on four different perceptual metrics: LPIPS, NIQE, FID (Fréchet Inception Distance), and KID (Kernel Inception Distance). Because our datasets do not have enough examples to reliably compute FID and KID, we extract 15 non-overlapping patches of size $256 \times 240$ from each $1280 \times 720$ image and compute the Inception-based metrics at the patch level, similar to. For completeness, we also include two distortion-based metrics: PSNR and SSIM.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We note the importance of including full-reference metrics for conditional image generation. A method can achieve near-perfect score on a no-reference metric such as NIQE by producing highly realistic images that are completely unrelated to the input. This is particularly relevant for GAN-based methods, since the discriminator may not penalize the generator for producing natural-looking images that do not match the input. This is why we included LPIPS (and to some extent, PSNR and SSIM), even though it is technically not a perceptual metric. For a qualitative comparison, we also conduct a human study and provide sample restorations.

<!-- chunk {"id": "body-0041", "role": "body", "section": "GoPro Results", "weight": 1.0} -->

Table 1 shows quantitative results on the GoPro dataset. We compared our model with the current state-of-the-art (SOTA) methods HINet, MPRNet, and DeblurGAN-v2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "GoPro Results", "weight": 1.0} -->

Our model achieves SOTA performance across all perceptual metrics while maintaining competitive PSNR and SSIM to existing methods. Notably, we obtain the FID of 4.04, nearly a 70% reduction compared to DeblurGAN-v2, the current SOTA method in terms of perceptual quality. Moreover, the sample-averaging variant of our method achieves a new SOTA PSNR of 33.23 while still outperforming all other methods with respect to LPIPS. All in all, these results highlight our framework's flexibility to control the trade-off between perception and distortion using a single model. As shown in Figure 1, our result sets a new Pareto frontier on the Perception-Distortion plot.

<!-- chunk {"id": "body-0043", "role": "body", "section": "HIDE Results", "weight": 1.0} -->

We also evaluate our GoPro-trained model on the HIDE dataset to test its ability to generalize to out-of-distribution input. As the results in Table 2 clearly show, the gains in perceptual quality do translate over to the HIDE dataset. In particular, both of our models significantly outperform the baseline methods across all perceptual metrics while maintaining competitive distortion values.

<!-- chunk {"id": "body-0044", "role": "body", "section": "HIDE Results", "weight": 1.0} -->

Fig. 4 includes several sample reconstructions from both GoPro and HIDE datasets. Despite sometimes containing a little more noise (some of which was presumably learned from the training data itself), we see that our model shows a clear improvement in perceptual quality. Additional full-size comparisons are provided in Appendix G.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Human Study for Qualitative Evaluation", "weight": 1.0} -->

We ran a perceptual study with human subjects to further quantify the performance of the proposed deblurring framework. Our results are presented in Table 3. We used Amazon Mechanical Turk to obtain pairwise ratings comparing different deblurring methods applied on the GoPro dataset. In this study, the human subjects had a minimum of 70% approval rating, and were asked to select the image with the better quality from side-by-side crops of size $512 \times 512$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Human Study for Qualitative Evaluation", "weight": 1.0} -->

Results in Table 3 show the average rater's preference computed from 480 comparisons. As the highlighted cells show, these results indicate that both variations of our deblurring model outperform the competing methods.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Human Study for Qualitative Evaluation", "weight": 1.0} -->

We also observed that raters showed a modest preference for the sample-averaged variant in crops with relatively flat content. On the other hand, raters preferred individual samples for highly-textured crops. Fig. 5 shows that the level of detail produced by our model is adaptive to the blur present in the input. As expected, blurrier images generally lead to higher variance in the resulting samples.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion and Analysis", "weight": 1.5} -->

For the analysis of various aspects of our model, we used a custom dataset created by applying synthetic camera shake blur and noise (described in Appendix C) on the images of the DIV2K dataset. This was done to make qualitative evaluation in a more controlled environment, since the low-quality ground truth images in existing paired datasets make qualitative assessment difficult.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Benefits of Residual Modeling", "weight": 1.0} -->

More efficient sampling. The main benefit of residual modeling is the reduction in the computational cost of sampling. Due to the iterative nature of diffusion sampling, the denoiser network must run many times for each generated sample -- sometimes up to hundreds to thousands of steps. Thus, any reduction in the cost of running the denoiser is particularly valuable, and our initial predictor provides a simple way to offload some of this computation.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Benefits of Residual Modeling", "weight": 1.0} -->

A key question is then whether the initial predictor can compensate for the decrease in the sample quality from using a smaller denoiser network. We empirically explore this by comparing sampling latency against sample quality with and without the initial predictor. In Fig. 6, the non-residual model refers to a regular conditional diffusion model with a large denoiser network. The residual model follows our architecture and has a large initial predictor and a small denoiser. Overall, the residual model has more parameters (33M vs. 28M).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Benefits of Residual Modeling", "weight": 1.0} -->

We see that the residual model requires much less time to sample an image despite it being larger than the non-residual model. Importantly, this reduction in sampling cost does not negatively affect the sample quality -- in fact, the residual model is up to $7 \times$ faster for a comparable sample quality.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Benefits of Residual Modeling", "weight": 1.0} -->

Output of the initial predictor. One unexpected discovery from our experiments is that the output of the initial predictor is often a fairly reasonable reconstruction of the reference image. We can see this in Fig. 3. While lacking in detail, the initial prediction is certainly less blurry than the input.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Benefits of Residual Modeling", "weight": 1.0} -->

It is perhaps surprising that this happens even though there is no explicit loss on the initial predictor's output $g_{\theta}{({\mathbf{y}})}$ to match the reference. We also note that our method is not the only possible parameterization of a diffusion model with an explicit decoupling of the iterative portion (denoiser network) from the single-pass portion (initial predictor). For instance, we could have simply fed $g_{\theta}{({\mathbf{y}})}$ as an auxiliary input to the denoiser $f_{\theta}$ without computing the residual. We leave these investigations around the initial predictor as future work.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Benefits of Residual Modeling", "weight": 1.0} -->

Residual images are simpler to model. One may wonder why adding a deterministic initial predictor would help with the model's performance. We posit that the benefits of residual modeling may be due to the distribution of residual images being "simpler" than that of reference images.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Benefits of Residual Modeling", "weight": 1.0} -->

While it is impractical to approximate the true entropy of the two distributions, we can look at related quantities that may serve as a proxy. Specifically, we compute the entropy of pixel values aggregated across all pixel locations for residual and reference images. As expected from natural images, the reference pixel distribution is reasonably spread out and has the entropy of $7.42$ bits-per-dimension (bpd). On the other hand, the residual pixel values follow a much more sharply concentrated distribution, leading to a substantially lower entropy of $3.91$ bpd. This suggests that the residual images may indeed be simpler to model.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Network Architecture Ablation", "weight": 1.0} -->

To better understand where the performance gains of our method are originating, we trained a regression-based baseline that only uses the initial predictor. Surprisingly, we observed that the initial predictor alone was able to achieve state-of-the-art PSNR of 33.07 when trained with a simple $L_{2}$ loss. Through a detailed ablation study, we identified three key hyperparameters: exponential moving average (EMA) of weights, large batch size, and network size.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Network Architecture Ablation", "weight": 1.0} -->

In Table 4, we start from a simple U-Net architecture and gradually enable each of the aforementioned hyperparameters. All models were trained for 1M steps to ensure the differences are not due to insufficient training. As the results show, all three hyperparameters were critical to the model's performance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

We presented a new framework for stochastic blind image deblurring with a focus on perceptual quality using a conditional diffusion model. We introduced a novel technique for reducing the computational burden of diffusion sampling. We empirically showed that our method achieves significantly improved perceptual quality and competitive distortion metrics as compared to the current state-of-the-art methods. We believe that our work opens a new direction for blind deblurring with a focus on perceptual quality and establishes a strong benchmark for future works to improve upon.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

There are a number of avenues to explore to further address the limitations of our work. Due to slow sampling and large network size, diffusion models are computationally too expensive to be incorporated into consumer-level devices. One way to combat this is to use more efficient sampling schemes such as DDIM or distillation. Another promising direction is to replace our initial predictor and denoiser network with U-Net architectures that are optimized for both distortion and run time.
