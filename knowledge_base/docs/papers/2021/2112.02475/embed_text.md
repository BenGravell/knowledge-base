## Introduction

Figure 1: Top: Perception-Distortion (P-D) trade-off of current state-of-the-art deblurring methods (top). Our method sets a new Pareto frontier in the P-D plot and allows us to traverse through the P-D curve using a single model without retraining or finetuning. Bottom: Samples from our method compared to other competitive methods. We include two extremes from our model – one optimized for perceptual quality (“Ours”) and one for distortion using Sample Averaging (“Ours-SA”). These correspond to the two end points of the P-D curve. For the ease of interpretation, we used negative Kernel Inception Distance (C − KID for a constant C) as the measure of perceptual quality.

Image deblurring is a long-standing problem in computer vision. Various conditions such as moving objects, camera shakes, or an out-of-focus lens may contribute to blurring artifacts. Single image deblurring is a highly ill-posed inverse problem where multiple plausible sharp images could lead to the very same blurry observation. Nonetheless, most existing methods produce a single deterministic estimate of the clean image.

Traditional methods formulate deblurring as a variational optimization problem and find a solution that satisfies closeness to certain image and/or blur kernel prior. With the emergence of deep learning, convolutional neural networks (CNNs) have become the de-facto standard for deblurring models. Typically, these CNNs are trained with simulated sharp-blurry image pairs through supervised learning. Minimizing $L_{1}$ or $L_{2}$ pixel loss is perhaps the most widely adopted approach for training such models. These losses provide a straightforward learning objective and optimize for the popular PSNR (peak signal-to-noise-ratio) metric. Unfortunately, PSNR and other distortion metrics are well-known to only partially correspond to human perception and can actually lead to algorithms with visibly lower quality in the reconstructed images. To alleviate this problem, recent works introduced additional loss terms that seek to improve the quality of generated images under metrics that represent human perception more reliably. Training networks to go from corrupted images to a known ground truth in a supervised way belongs in the family of end-to-end methods. These methods perform very well in-distribution, but can be quite fragile to distributional shifts or changes in the corruption process.

A second body of work has focused on using deep generative models to solve inverse problems. For deblurring, Generative Adversarial Networks (GANs) have been successfully applied with competitive performance. GAN-based restoration methods train the deblurring network with an adversarial loss to make the restored images more perceptually plausible. However the proposed methods so far have been deterministic, and adversarial losses often introduce artifacts not present in the original clean image, leading to large distortion (*e.g*. for super-resolution).

In this work, we adopt a different perspective and view deblurring as a conditional generative modeling task, where we seek to generate diverse samples from the posterior distribution. Specifically, we introduce a "predict-and-refine" conditional diffusion model, where a deterministic data-adaptive predictor is jointly trained with a stochastic sampler that refines the output of the said predictor (see Fig. 2).

Our predict-and-refine approach enables more efficient sampling compared to the standard diffusion model. This formulation also naturally leads to a stochastic model capable of producing realistic images without sacrificing pixel-level distortion. To the best of our knowledge, this is the first blind deblurring technique that leverages a deep generative model and is capable of producing diverse samples.

Overall, our method produces a variety of plausible and photo-realistic results, while achieving state-of-the-art performance under many quantitative metrics in terms of both distortion and perceptual quality across multiple standard datasets. In addition, by aggregating a different number of generated deblurred samples, our framework allows us to conveniently traverse the Perception-Distortion curve as shown in Fig. 1, without any expensive retraining or finetuning. These results show clear benefits of stochastic diffusion-based methods for deblurring and challenge the currently dominant strategy of producing deterministic reconstructions.

## Related Work

Figure 2: Diagram describing our dual-network architecture. The initial predictor produces the deterministic candidate for the denoiser network, which then models the residual.

The goal of image deblurring is to generate a plausible reconstruction of the unobserved sharp, clean image $\mathbf{x}$ from a blurry input $\mathbf{y}$. Deblurring techniques differ in what they aim to obtain. For example, one could try to directly sample from the posterior $p{(\left. {\mathbf{x}} \middle| {\mathbf{y}} \right.)}$. Another viable option is to compute a point-estimate such as the conditional mean ${\mathbb{E}}\left\lbrack {\mathbf{x}} \middle| {\mathbf{y}} \right\rbrack$ or the maximum a posteriori estimate ${{\arg\max}_{\mathbf{x}}p}{(\left. {\mathbf{x}} \middle| {\mathbf{y}} \right.)}$.

Deblurring through point estimates. Traditional deblurring methods formulate the problem as one of blind deconvolution. In this setup, the blur is generally modeled as a noisy linear operator acting on the clean image. While the exact values of the blur operator are not assumed to be known, one can enforce some prior distribution on the blur and the sharp image and try to find the most likely solution.

Alternatively, many recent methods adopt an end-to-end approach where a deep neural network is trained to directly produce a point estimate. These methods generally rely on pairs of blurry-sharp images as training data and cast the deblurring problem as a supervised regression task. Much of the efforts have gone into developing specialized network architectures and loss functions to achieve better pixel-level reconstruction metrics such as PSNR or SSIM. For example, MIMO-UNet proposed an architecture that facilitates information flow across different image resolutions in a multi-scale U-Net. Another work HINet introduced Half Instance Normalization, which can be used as a building block for image restoration networks. MPRNet presented an improved multi-stage architecture designed to incorporate both high-level global features as well as local details.

Issue of *regression to the mean*. While the aforementioned approaches lead to state-of-the-art PSNR, they share the limitation that they can only produce a deterministic output. This is at odds with the nature of blind image deblurring, which is an inherently ill-posed inverse problem with multiple valid solutions for a single input. In fact, the current trend of developing point-estimators that directly minimize a distortion loss suffers from the problem of "regression to the mean". If there are multiple possible clean images that correspond to the blurry input, the optimal reconstruction according to the given loss function will be an average of them. Consequently, the resultant deterministic reconstruction often lacks details as it learns to produce the average of all possible solutions at best.

Diverse image restoration. One way to circumvent the *regression to the mean* phenomenon is to avoid point estimations and directly learn to generate samples from the posterior distribution. While techniques based on adversarial training have been explored for blind deblurring, in general they are not trained to produce multiple samples. Additionally, non-reference based adversarial losses can introduce significant hallucinations and distortions.

Likelihood-based deep generative models such as Variational Autoencoders, Normalizing Flows, and Diffusion Probabilistic Models (DPMs) have also been successfully applied to other image enhancement tasks such as super-resolution, where a diverse set of candidates can be generated from the learned posterior. Compared to point estimates, solving imaging inverse problems by sampling from the posterior has additional benefits such as uncertainty quantification, near-optimal sample complexity and better fairness guarantees.

## Diffusion Probabilistic Models

Diffusion probabilistic model is a latent variable model specified by a $T$-step Markov chain $({\mathbf{x}}_{0},{\mathbf{x}}_{1},\ldots,{\mathbf{x}}_{T})$ called the diffusion process. It starts from a clean data sample ${\mathbf{x}}_{0} \in {\mathbb{R}}^{d}$ and repeatedly injects Gaussian noise according to the transition kernel $q{(\left. {\mathbf{x}}_{t} \middle| {\mathbf{x}}_{t - 1} \right.)}$ as follows:

where $\alpha_{t} \in {}$ for all $t = {1,\ldots,T}$. The noise schedule ${\mathbf{α}}_{1:T} \triangleq {(\alpha_{1},\ldots,\alpha_{T})}$ is a hyperparameter that controls the variance of noise added at each step. The latent variables ${\mathbf{x}}_{1:T}$ have the same dimensionality as the original data sample ${\mathbf{x}}_{0}$.

While this particular choice of diffusion process may seem arbitrary, it results in closed-form expressions for the following distributions: the marginal^11^1For notational brevity, we use the term "marginal" to include distributions conditioned on ${\mathbf{x}}_{0}$. distribution $q{(\left. {\mathbf{x}}_{t} \middle| {\mathbf{x}}_{0} \right.)}$ and the reverse diffusion step $q{(\left. {\mathbf{x}}_{t - 1} \middle| {{\mathbf{x}}_{t},{\mathbf{x}}_{0}} \right.)}$. Writing ${\overline{\alpha}}_{t} \triangleq {\prod_{j = 1}^{t}\alpha_{j}}$, we get

where ${\mathbf{μ}}_{t}{({\mathbf{x}}_{t},{\mathbf{x}}_{0})}$ and $\beta_{t}$ are quantities that depend on ${\mathbf{x}}_{t},{\mathbf{x}}_{0}$ and ${\mathbf{α}}_{1:T}$. Their full expressions and derivations are included in Appendix D.

The marginal distribution in Eq. 2 allows us to sample a partially noisy image ${\mathbf{x}}_{t}$ at an arbitrary time step, and the reverse diffusion step in Eq. 3 is a stochastic denoising procedure that tells us how to reverse a single diffusion step by sampling a slightly less noisy image ${\mathbf{x}}_{t - 1}$ from ${\mathbf{x}}_{t}$. The ability to sample from arbitrary marginals is important to make training of a DPM practical, as the training objective relies on it (see Eq. 5).

We note that the diffusion process defined here has no learnable parameter. It is a fixed process that gradually destroys the original signal ${\mathbf{x}}_{0}$ and produces ${\mathbf{x}}_{T}$ that looks indistinguishable from pure Gaussian noise given a sufficiently large $T$. Thus, if we could apply the reverse diffusion step $T$ times starting from pure Gaussian noise, we would obtain a clean sample ${\mathbf{x}}_{0}$. However this is not possible because the reverse diffusion step itself requires access to ${\mathbf{x}}_{0}$, which is exactly what we are trying to generate.

Reverse process and denoiser network. A key component of DPM is the denoiser network $f_{\theta}$ that tries to estimate ${\mathbf{x}}_{0}$ from the partially noisy image ${\mathbf{x}}_{t}$. With it, we can apply the reverse diffusion step without knowing ${\mathbf{x}}_{0}$ by using the estimate $f_{\theta}{({\mathbf{x}}_{t},t)}$ in place of ${\mathbf{x}}_{0}$:

This defines a Markov chain that runs backwards in time from ${\mathbf{x}}_{T}$ to ${\mathbf{x}}_{0}$, which we call the reverse process. The goal of DPM is to train $f_{\theta}$ to make $p_{\theta}{(\left. {\mathbf{x}}_{t - 1} \middle| {\mathbf{x}}_{t} \right.)}$ as close to the true reverse diffusion step $q{(\left. {\mathbf{x}}_{t - 1} \middle| {{\mathbf{x}}_{t},{\mathbf{x}}_{0}} \right.)}$ as possible. This is done by optimizing $f_{\theta}$ to maximize the variational lower bound of the marginal likelihood ${\log p_{\theta}}{({\mathbf{x}})}$.

In practice, we use an alternative parametrization of $f_{\theta}$ proposed by that instead predicts the Gaussian noise $\mathbf{\epsilon}$ that deterministically relates ${\mathbf{x}}_{t}$ and ${\mathbf{x}}_{0}$ via Equation 2. Specifically, we write ${\mathbf{x}}_{t} = {{\sqrt{{\overline{\alpha}}_{t}}{\mathbf{x}}_{0}} + {{({1 - {\overline{\alpha}}_{t}})}\mathbf{\epsilon}}}$ for $\mathbf{\epsilon} \sim {\mathcal{N}{(\mathbf{0},{\mathbf{I}}_{d})}}$ and train $f_{\theta}$ to predict $\mathbf{\epsilon}$.

Continuous noise level. Chen *et al*. proposes a modified formulation based on a continuous noise level $\overline{\alpha}$, which we also adopt. An important property of this formulation is that it allows us to sample from the model using a noise schedule ${\mathbf{α}}_{1:T}$ different from the one used during training. This flexibility enables us to control the trade-off between the distortion and the perceptual quality of generated samples without having to retrain the model, as we show later.

Conditional DPM. So far we have defined a DPM that is trained to model the unconditional data distribution. For conditional models that must estimate $p{(\left. {\mathbf{x}} \middle| {\mathbf{y}} \right.)}$, we make $f_{\theta}$ accept $\mathbf{y}$ as the conditioning input, as was done in. This way, the iterative denoising procedure becomes dependent on $\mathbf{y}$. The final training objective is:

where the expectation is over ${\mathbf{y}},{\mathbf{x}}_{0},\overline{\alpha}$, and $\mathbf{\epsilon}$.

Sampling from a DPM. As mentioned earlier, sampling an image from a DPM is done by running the reverse process. Given some inference-time noise schedule ${\overline{\alpha}}_{1:T}$, we start from a pure Gaussian noise ${\mathbf{x}}_{T} \sim {\mathcal{N}{(\mathbf{0},{\mathbf{I}}_{d})}}$ and repeatedly apply the reverse process transition $p_{\theta}{(\left. {\mathbf{x}}_{t - 1} \middle| {\mathbf{x}}_{t} \right.)}$ defined in Eq. 4. Notice that this procedure requires a total of $T$ calls to the denoiser network. At the end of this sampling procedure, we are left with a single sample ${\mathbf{x}}_{0}$.

## Predict-and-Refine Diffusion Model

Figure 3: Output of the initial predictor and multiple samples generated from it. We see that the over-smoothed initial prediction lacking texture is “corrected” by the stochastic sampler, producing crisp and diverse final reconstructions. The residual (top right) shows the the difference between reference and initial prediction.

One of the main drawbacks of DPM is the computational cost of generating samples, which may require up to thousands of forward passes of the denoiser network due to the iterative denoising procedure. As such, many recent works have explored alternative sampling strategies that reduce the number of sampling steps.

We introduce a simple technique that reduces this cost by exploiting the fact that it is often possible to get a cheap initial guess for conditional generative models. Specifically, we augment our conditional diffusion model with a deterministic initial predictor (Fig. 2), which provides a data-adaptive candidate for the clean image. Then the denoiser network only needs to model the residual.

Letting $g_{\theta}$ denote the initial predictor, the new objective becomes: ${L_{\text{Ours}}{(\theta)}} =$

We include a pseudocode for the modified sampling procedure in Algorithm 1. Notice that the initial predictor $g_{\theta}$ does not require an extra loss or pretraining because the gradient from the loss flows through $f_{\theta}$ into $g_{\theta}$.

Since the initial predictor runs only once, it is beneficial to keep the denoiser network small by offloading most of the computation to the initial predictor. This leads to much more efficient sampling because any reduction in the computational cost of the denoiser network gets amplified by the number of sampling steps used. We further explore this effect in Sec. 6.

0: fθ: Denoiser network, gθ: Initial predictor, y: Blurry input image, α1: T: Noise schedule.
1: xinit ← gθ (y) ⊳ Initial prediction
2: zT ∼ 𝒩 (0,Id) ⊳ Run diffusion sampling
5: ${\mathbf{z}}_{t - 1}\leftarrow{{{\mathbf{μ}}_{t}{({\mathbf{z}}_{t},{f_{\theta}{({\mathbf{z}}_{t},{\overline{\alpha}}_{t},{\mathbf{y}})}})}} + {\beta_{t}\mathbf{\epsilon}_{t}}}$ ⊳ Reverse diffusion step; see Eq. 3
7: return xinit + z0 ⊳ Return the final restoration
Algorithm 1 Predict-and-refine diffusion sampling.
The expressions for ${\mathbf{μ}}_{t},{\overline{\alpha}}_{t},\beta_{t}$ can be found in Sec. 3.

### Perception-Distortion Trade-off

As explained in Sec. 3, conditioning the diffusion model on continuous noise level makes it possible to use a different noise schedule during inference. We observe that using many steps with small noise level generally leads to better perceptual quality, and using fewer steps with large noise level leads to lower distortion.

For our experiments, we run a small grid search over the noise schedule hyperparameters and use the model with the best LPIPS score (labeled "Ours"). We emphasize that this inference-time hyperparameter tuning is cheap as it does not involve retraining or finetuning the model itself.

Sample averaging. Our framework also provides a principled alternative to geometric self-ensemble. Since our stochastic sampler is trained to learn the target posterior $p{(\left. {\mathbf{x}} \middle| {\mathbf{y}} \right.)}$, we can average multiple samples from our model to approximate the conditional mean ${\mathbb{E}}\left\lbrack {\mathbf{x}} \middle| {\mathbf{y}} \right\rbrack$, *i.e*. the minimum mean squared error estimator. We thus report results for a second model (labeled "Ours-SA") that returns the average of multiple samples.

Traversing the Perception-Distortion curve. By appropriately setting the inference-time hyperparameters mentioned above (sampling steps $T$, noise schedule ${\overline{\alpha}}_{1:T}$, and sample averaging), we can smoothly traverse the P-D curve as shown in Fig. 1.

For example, the LPIPS-optimized model ("Ours") uses a relatively large step count of $T = 500$ without sample averaging to achieve high perceptual quality at a slight cost of PSNR. The distortion-optimized model ("Ours-SA") does the opposite by using $T = 10$ with sample averaging to sacrifice perceptual quality for higher PSNR. Each point on the P-D curve in Fig. 1 thus corresponds to a specific choice of these hyperparameters.

### Resolution-agnostic Architecture

Unlike the image benchmarks commonly used to evaluate DPMs, blind deblurring benchmarks contain images with various sizes. To support arbitrary input shapes, we use a fully-convolutional architecture for both initial predictor and denoiser network.

Our architecture is based on SR3, which uses a variant of U-Net architecture from with residual blocks replaced with that of BigGAN. To make our model agnostic to image resolution, we removed self-attention, positional encoding, and group normalization. The exact specification of our architecture can be found in Appendix E.

We note that, to the best of our knowledge, this is the first time a conditional diffusion model is made to support arbitrary image size. Our preliminary experiments show that the fully-convolutioanl architecture had little to no degradation in sample quality for deblurring at non-native resolutions. Because the denoiser network is a relatively simple U-Net, DPMs provide a particularly convenient choice for conditional image generation that must work on any input size.

## Experiments

### Datasets

We train and evaluate our models on two widely-used image deblurring datasets. For a fair comparison, we follow the same setup used by and train our model only using the provided training data.

GoPro. GoPro dataset contains 3214 pairs of clean and blurry $1280 \times 720$ images, of which 1111 are reserved for evaluation. These images are generated by recording video clips with high shutter speed, then averaging consecutive frames to simulate blurs caused by slow shutter speed.

HIDE. We additionally evaluate our GoPro-trained model on the HIDE dataset, which contains 2025 images also of size $1280 \times 720$. By training and evaluating our model on different datasets, we can test its ability to generalize under a distributional shift.

### Model Training

We jointly train the initial predictor and denoiser network by minimizing the loss in Eq. 6. Since our model is fully convolutional, we use random $128 \times 128$ crops during training, but apply the model on full-size images for evaluation. We also perform training-time data augmentation with random horizontal/vertical flips and $90{^\circ}$/$180{^\circ}$/$270{^\circ}$ rotations.

A note on training data. Most currently leading methods only report distortion-based metrics (PSNR and SSIM) and provide pre-trained models for GoPro. Since our work focuses on perceptual quality, we need to compute perceptual metrics ourselves using outputs from other methods. Thus to ensure a fair comparison, we are limited to using models trained on the GoPro dataset, as it is the only dataset with widely available pre-trained models. Nonetheless, we provide additional results and the details of how we obtained the outputs of other methods in Appendices H and F.

Table 1: Image deblurring results on the GoPro dataset. Our proposed method sets the new Pareto frontier in terms of Perception-Distortion trade-off. Best values and second-best values for each metric are color-coded. KID values are scaled by a factor of 1000 for readability.

### Evaluation

Evaluation Metrics. We evaluate our method on four different perceptual metrics: LPIPS, NIQE, FID (Fréchet Inception Distance), and KID (Kernel Inception Distance). Because our datasets do not have enough examples to reliably compute FID and KID, we extract 15 non-overlapping patches of size $256 \times 240$ from each $1280 \times 720$ image and compute the Inception-based metrics at the patch level, similar to. For completeness, we also include two distortion-based metrics: PSNR and SSIM.

We note the importance of including full-reference metrics for conditional image generation. A method can achieve near-perfect score on a no-reference metric such as NIQE by producing highly realistic images that are completely unrelated to the input. This is particularly relevant for GAN-based methods, since the discriminator may not penalize the generator for producing natural-looking images that do not match the input. This is why we included LPIPS (and to some extent, PSNR and SSIM), even though it is technically not a perceptual metric. For a qualitative comparison, we also conduct a human study and provide sample restorations.

Figure 4: Sample deblurred images from GoPro and HIDE datasets. Because our method is not trained to minimize distortion-based loss (e.g. L2), it avoids producing blurry output and achieves better reconstruction of detailed textures. Full-size images are provided in Appendix G. Best viewed electronically.

### Quantitative Results

### GoPro Results

Table 1 shows quantitative results on the GoPro dataset. We compared our model with the current state-of-the-art (SOTA) methods HINet, MPRNet, and DeblurGAN-v2.

Our model achieves SOTA performance across all perceptual metrics while maintaining competitive PSNR and SSIM to existing methods. Notably, we obtain the FID of 4.04, nearly a 70% reduction compared to DeblurGAN-v2, the current SOTA method in terms of perceptual quality. Moreover, the sample-averaging variant of our method achieves a new SOTA PSNR of 33.23 while still outperforming all other methods with respect to LPIPS. All in all, these results highlight our framework's flexibility to control the trade-off between perception and distortion using a single model. As shown in Figure 1, our result sets a new Pareto frontier on the Perception-Distortion plot.

Table 2: Image deblurring results on the HIDE dataset, using models trained on GoPro. Our method significantly outperforms the baseline methods under all perceptual metrics while maintaining competitive PSNR and SSIM. Best values and second-best values for each each metric are color-coded.

### HIDE Results

We also evaluate our GoPro-trained model on the HIDE dataset to test its ability to generalize to out-of-distribution input. As the results in Table 2 clearly show, the gains in perceptual quality do translate over to the HIDE dataset. In particular, both of our models significantly outperform the baseline methods across all perceptual metrics while maintaining competitive distortion values.

Fig. 4 includes several sample reconstructions from both GoPro and HIDE datasets. Despite sometimes containing a little more noise (some of which was presumably learned from the training data itself), we see that our model shows a clear improvement in perceptual quality. Additional full-size comparisons are provided in Appendix G.

### Human Study for Qualitative Evaluation

We ran a perceptual study with human subjects to further quantify the performance of the proposed deblurring framework. Our results are presented in Table 3. We used Amazon Mechanical Turk to obtain pairwise ratings comparing different deblurring methods applied on the GoPro dataset. In this study, the human subjects had a minimum of 70% approval rating, and were asked to select the image with the better quality from side-by-side crops of size $512 \times 512$.

Results in Table 3 show the average rater's preference computed from 480 comparisons. As the highlighted cells show, these results indicate that both variations of our deblurring model outperform the competing methods.

We also observed that raters showed a modest preference for the sample-averaged variant in crops with relatively flat content. On the other hand, raters preferred individual samples for highly-textured crops. Fig. 5 shows that the level of detail produced by our model is adaptive to the blur present in the input. As expected, blurrier images generally lead to higher variance in the resulting samples.

Table 3: Average pairwise human preference for deblurring results on the GoPro dataset. Each value represents the percentage of times Amazon Mechanical Turk raters chose the row over the column. Each preference percentage is an average over 480 ratings (20 raters, and 24 unique image pairs).

## Discussion and Analysis

For the analysis of various aspects of our model, we used a custom dataset created by applying synthetic camera shake blur and noise (described in Appendix C) on the images of the DIV2K dataset. This was done to make qualitative evaluation in a more controlled environment, since the low-quality ground truth images in existing paired datasets make qualitative assessment difficult.

Figure 5: Deblurred samples for crops of two different images. The ill-posedness of the restoration task (i.e. strength of the blur) has a direct impact on the diversity of the generated samples. This is illustrated by the per-pixel standard deviation computed using multiple restorations for each input image. As clearly visible in the right-most column, the blurrier input (first row) corresponds to overall higher per-pixel standard deviations.

### Benefits of Residual Modeling

More efficient sampling. The main benefit of residual modeling is the reduction in the computational cost of sampling. Due to the iterative nature of diffusion sampling, the denoiser network must run many times for each generated sample -- sometimes up to hundreds to thousands of steps. Thus, any reduction in the cost of running the denoiser is particularly valuable, and our initial predictor provides a simple way to offload some of this computation.

A key question is then whether the initial predictor can compensate for the decrease in the sample quality from using a smaller denoiser network. We empirically explore this by comparing sampling latency against sample quality with and without the initial predictor. In Fig. 6, the non-residual model refers to a regular conditional diffusion model with a large denoiser network. The residual model follows our architecture and has a large initial predictor and a small denoiser. Overall, the residual model has more parameters (33M vs. 28M).

We see that the residual model requires much less time to sample an image despite it being larger than the non-residual model. Importantly, this reduction in sampling cost does not negatively affect the sample quality -- in fact, the residual model is up to $7 \times$ faster for a comparable sample quality.

Figure 6: Plot of sampling cost vs. sample quality. Even with the added parameters from the initial predictor, the residual model achieves lower latency while maintaining higher sample quality.

Output of the initial predictor. One unexpected discovery from our experiments is that the output of the initial predictor is often a fairly reasonable reconstruction of the reference image. We can see this in Fig. 3. While lacking in detail, the initial prediction is certainly less blurry than the input.

It is perhaps surprising that this happens even though there is no explicit loss on the initial predictor's output $g_{\theta}{({\mathbf{y}})}$ to match the reference. We also note that our method is not the only possible parameterization of a diffusion model with an explicit decoupling of the iterative portion (denoiser network) from the single-pass portion (initial predictor). For instance, we could have simply fed $g_{\theta}{({\mathbf{y}})}$ as an auxiliary input to the denoiser $f_{\theta}$ without computing the residual. We leave these investigations around the initial predictor as future work.

Residual images are simpler to model. One may wonder why adding a deterministic initial predictor would help with the model's performance. We posit that the benefits of residual modeling may be due to the distribution of residual images being "simpler" than that of reference images.

While it is impractical to approximate the true entropy of the two distributions, we can look at related quantities that may serve as a proxy. Specifically, we compute the entropy of pixel values aggregated across all pixel locations for residual and reference images. As expected from natural images, the reference pixel distribution is reasonably spread out and has the entropy of $7.42$ bits-per-dimension (bpd). On the other hand, the residual pixel values follow a much more sharply concentrated distribution, leading to a substantially lower entropy of $3.91$ bpd. This suggests that the residual images may indeed be simpler to model.

### Network Architecture Ablation

To better understand where the performance gains of our method are originating from, we trained a regression-based baseline that only uses the initial predictor. Surprisingly, we observed that the initial predictor alone was able to achieve state-of-the-art PSNR of 33.07 when trained with a simple $L_{2}$ loss. Through a detailed ablation study, we identified three key hyperparameters: exponential moving average (EMA) of weights, large batch size, and network size.

In Table 4, we start from a simple U-Net architecture and gradually enable each of the aforementioned hyperparameters. All models were trained for 1M steps to ensure the differences are not due to insufficient training. As the results show, all three hyperparameters were critical to the model's performance.

Table 4: Ablation study on the effects of various hyperparameters for our U-Net architecture, evaluated on the GoPro dataset.

## Conclusion and Future Directions

We presented a new framework for stochastic blind image deblurring with a focus on perceptual quality using a conditional diffusion model. We introduced a novel technique for reducing the computational burden of diffusion sampling. We empirically showed that our method achieves significantly improved perceptual quality and competitive distortion metrics as compared to the current state-of-the-art methods. We believe that our work opens a new direction for blind deblurring with a focus on perceptual quality and establishes a strong benchmark for future works to improve upon.

There are a number of avenues to explore to further address the limitations of our work. Due to slow sampling and large network size, diffusion models are computationally too expensive to be incorporated into consumer-level devices. One way to combat this is to use more efficient sampling schemes such as DDIM or distillation. Another promising direction is to replace our initial predictor and denoiser network with U-Net architectures that are optimized for both distortion and run time.
