<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Denoising Diffusion Probabilistic Models

Topics include Diffusion models, Probabilistic models, Datasets, Generalization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep generative models of all kinds have recently exhibited high quality samples in a wide variety of data modalities. Generative adversarial networks (GANs), autoregressive models, flows, and variational autoencoders (VAEs) have synthesized striking image and audio samples, and there have been remarkable advances in energy-based modeling and score matching that have produced images comparable to those of GANs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents progress in diffusion probabilistic models. A diffusion probabilistic model (which we will call a "diffusion model" for brevity) is a parameterized Markov chain trained using variational inference to produce samples matching the data after finite time. Transitions of this chain are learned to reverse a diffusion process, which is a Markov chain that gradually adds noise to the data in the opposite direction of sampling until signal is destroyed. When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for a particularly simple neural network parameterization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Diffusion models are straightforward to define and efficient to train, but to the best of our knowledge, there has been no demonstration that they are capable of generating high quality samples. We show that diffusion models actually are capable of generating high quality samples, sometimes better than the published results on other types of generative models (Section 4). In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and with annealed Langevin dynamics during sampling (Section 3.2). We obtained our best sample quality results using this parameterization (Section 4.2), so we consider this equivalence to be one of our primary contributions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their sample quality, our models do not have competitive log likelihoods compared to other likelihood-based models (our models do, however, have log likelihoods better than the large estimates annealed importance sampling has been reported to produce for energy based models and score matching ). We find that the majority of our models' lossless codelengths are consumed to describe imperceptible image details (Section 4.3). We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models is a type of progressive decoding that resembles autoregressive decoding along a bit ordering that vastly generalizes what is normally possible with autoregressive models.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Diffusion models and denoising autoencoders", "weight": 1.0} -->

Diffusion models might appear to be a restricted class of latent variable models, but they allow a large number of degrees of freedom in implementation. One must choose the variances $\beta_{t}$ of the forward process and the model architecture and Gaussian distribution parameterization of the reverse process. To guide our choices, we establish a new explicit connection between diffusion models and denoising score matching (Section 3.2) that leads to a simplified, weighted variational bound objective for diffusion models (Section 3.4). Ultimately, our model design is justified by simplicity and empirical results (Section 4). Our discussion is categorized by the terms of Eq. 5.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Forward process and $L_{T}$", "weight": 1.0} -->

We ignore the fact that the forward process variances $\beta_{t}$ are learnable by reparameterization and instead fix them to constants (see Section 4 for details). Thus, in our implementation, the approximate posterior $q$ has no learnable parameters, so $L_{T}$ is a constant during training and can be ignored.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Reverse process and $L_{1:{T - 1}}$", "weight": 1.0} -->

So, we see that the most straightforward parameterization of ${\mathbf{μ}}_{\theta}$ is a model that predicts ${\overset{\sim}{\mathbf{μ}}}_{t}$, the forward process posterior mean.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Reverse process and $L_{1:{T - 1}}$", "weight": 1.0} -->

Since $\mathbf{x}_{t}$ is available as input to the model, we may choose the parameterization where $\mathbf{\epsilon}_{\theta}$ is a function approximator intended to predict $\mathbf{\epsilon}$ from $\mathbf{x}_{t}$. To sample $\mathbf{x}_{t - 1} \sim {p_{\theta}{(\left.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reverse process and $L_{1:{T - 1}}$", "weight": 1.0} -->

Furthermore, with the parameterization 11, Eq. 10 simplifies to: which resembles denoising score matching over multiple noise scales indexed by $t$. As Eq. 12 is equal to (one term of) the variational bound for the Langevin-like reverse process 11, we see that optimizing an objective resembling denoising score matching is equivalent to using variational inference to fit the finite-time marginal of a sampling chain resembling Langevin dynamics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Reverse process and $L_{1:{T - 1}}$", "weight": 1.0} -->

To summarize, we can train the reverse process mean function approximator ${\mathbf{μ}}_{\theta}$ to predict ${\overset{\sim}{\mathbf{μ}}}_{t}$, or by modifying its parameterization, we can train it to predict $\mathbf{\epsilon}$. (There is also the possibility of predicting $\mathbf{x}_{0}$, but we found this to lead to worse sample quality early in our experiments.) We have shown that the $\mathbf{\epsilon}$-prediction parameterization both resembles Langevin dynamics and simplifies the diffusion model's variational bound to an objective that resembles denoising score matching. Nonetheless, it is just another parameterization of $p_{\theta}{(\left.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Reverse process and $L_{1:{T - 1}}$", "weight": 1.0} -->

\mathbf{x}_{t - 1} \middle| \mathbf{x}_{t} \right.)}$, so we verify its effectiveness in Section 4 in an ablation where we compare predicting $\mathbf{\epsilon}$ against predicting ${\overset{\sim}{\mathbf{μ}}}_{t}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Data scaling, reverse process decoder, and $L_{0}$", "weight": 1.0} -->

We assume that image data consists of integers in $\{ 0,1,\ldots,255\}$ scaled linearly to $\lbrack{- 1},1\rbrack$. This ensures that the neural network reverse process operates on consistently scaled inputs starting from the standard normal prior $p{(\mathbf{x}_{T})}$. To obtain discrete log likelihoods, we set the last term of the reverse process to an independent discrete decoder derived from the Gaussian $\mathcal{N}{(\mathbf{x}_{0};{{\mathbf{μ}}_{\theta}{(\mathbf{x}_{1},1)}},{\sigma_{1}^{2}\mathbf{I}})}$: | | {p_{\theta}{(\left.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Data scaling, reverse process decoder, and $L_{0}$", "weight": 1.0} -->

(It would be straightforward to instead incorporate a more powerful decoder like a conditional autoregressive model, but we leave that to future work.) Similar to the discretized continuous distributions used in VAE decoders and autoregressive models, our choice here ensures that the variational bound is a lossless codelength of discrete data, without need of adding noise to the data or incorporating the Jacobian of the scaling operation into the log likelihood. At the end of sampling, we display ${\mathbf{μ}}_{\theta}{(\mathbf{x}_{1},1)}$ noiselessly.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Simplified training objective", "weight": 1.0} -->

With the reverse process and decoder defined above, the variational bound, consisting of terms derived from Eqs. 12 and 13, is clearly differentiable with respect to $\theta$ and is ready to be employed for training. However, we found it beneficial to sample quality (and simpler to implement) to train on the following variant of the variational bound: where $t$ is uniform between $1$ and $T$. The $t = 1$ case corresponds to $L_{0}$ with the integral in the discrete decoder definition 13 approximated by the Gaussian probability density function times the bin width, ignoring $\sigma_{1}^{2}$ and edge effects. The $t > 1$ cases correspond to an unweighted version of Eq. 12, analogous to the loss weighting used by the NCSN denoising score matching model. ($L_{T}$ does not appear because the forward process variances $\beta_{t}$ are fixed.) Algorithm 1 displays the complete training procedure with this simplified objective.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Simplified training objective", "weight": 1.0} -->

Since our simplified objective 14 discards the weighting in Eq. 12, it is a weighted variational bound that emphasizes different aspects of reconstruction compared to the standard variational bound. In particular, our diffusion process setup in Section 4 causes the simplified objective to down-weight loss terms corresponding to small $t$. These terms train the network to denoise data with very small amounts of noise, so it is beneficial to down-weight them so that the network can focus on more difficult denoising tasks at larger $t$ terms. We will see in our experiments that this reweighting leads to better sample quality.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments", "weight": 1.0} -->

We set $T = 1000$ for all experiments so that the number of neural network evaluations needed during sampling matches previous work. We set the forward process variances to constants increasing linearly from $\beta_{1} = 10^{- 4}$ to $\beta_{T} = 0.02$. These constants were chosen to be small relative to data scaled to $\lbrack{- 1},1\rbrack$, ensuring that reverse and forward processes have approximately the same functional form while keeping the signal-to-noise ratio at $\mathbf{x}_{T}$ as small as possible ($L_{T} = {D_{KL}\left( {{q{(\left. \mathbf{x}_{T} \middle| \mathbf{x}_{0} \right.)}} \parallel {\mathcal{N}{(\mathbf{0},\mathbf{I})}}} \right)} \approx 10^{- 5}$ bits per dimension in our experiments).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

To represent the reverse process, we use a U-Net backbone similar to an unmasked PixelCNN++ with group normalization throughout. Parameters are shared across time, which is specified to the network using the Transformer sinusoidal position embedding. We use self-attention at the $16 \times 16$ feature map resolution. Details are in Appendix B.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sample quality", "weight": 1.0} -->

NLL Test (Train) Ours (L, fixed isotropic Σ) Table 2: Unconditional reverse process parameterization and training objective ablation. Blank entries were unstable to train and generated poor samples with out-of-range scores. $\overset{\sim}{\mathbf{μ}}$ prediction (baseline) $\left\| {\overset{\sim}{\mathbf{μ}} - {\overset{\sim}{\mathbf{μ}}}_{\theta}} \right\|^{2}$ $\left\| {\overset{\sim}{\mathbf{\epsilon}} - \mathbf{\epsilon}_{\theta}} \right\|^{2}$ (Lsimple) Table 1 shows Inception scores, FID scores, and negative log likelihoods (lossless codelengths). With our FID score of 3.17, our unconditional model achieves better sample quality than most models in the literature, including class conditional models.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sample quality", "weight": 1.0} -->

Our FID score is computed with respect to the training set, as is standard practice; when we compute it with respect to the test set, the score is 5.24, which is still better than many of the training set FID scores in the literature.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sample quality", "weight": 1.0} -->

We find that training our models on the true variational bound yields better codelengths than training on the simplified objective, as expected, but the latter yields the best sample quality. See Fig. 1 for and CelebA-HQ $256 \times 256$ samples, Fig. 4 and Fig. 4 for LSUN $256 \times 256$ samples, and Appendix D for more.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Reverse process parameterization and training objective ablation", "weight": 1.0} -->

In Table 2, we show the sample quality effects of reverse process parameterizations and training objectives (Section 3.2). We find that the baseline option of predicting $\overset{\sim}{\mathbf{μ}}$ works well only when trained on the true variational bound instead of unweighted mean squared error, a simplified objective akin to Eq. 14. We also see that learning reverse process variances (by incorporating a parameterized diagonal $\mathbf{\Sigma}_{\theta}{(\mathbf{x}_{t})}$ into the variational bound) leads to unstable training and poorer sample quality compared to fixed variances. Predicting $\mathbf{\epsilon}$, as we proposed, performs approximately as well as predicting $\overset{\sim}{\mathbf{μ}}$ when trained on the variational bound with fixed variances, but much better when trained with our simplified objective.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Progressive coding", "weight": 1.0} -->

Table 1 also shows the codelengths of our models. The gap between train and test is at most 0.03 bits per dimension, which is comparable to the gaps reported with other likelihood-based models and indicates that our diffusion model is not overfitting (see Appendix D for nearest neighbor visualizations). Still, while our lossless codelengths are better than the large estimates reported for energy based models and score matching using annealed importance sampling, they are not competitive with other types of likelihood-based generative models.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Progressive coding", "weight": 1.0} -->

Since our samples are nonetheless of high quality, we conclude that diffusion models have an inductive bias that makes them excellent lossy compressors. Treating the variational bound terms $L_{1} + \cdots + L_{T}$ as rate and $L_{0}$ as distortion, our model with the highest quality samples has a rate of 1.78 bits/dim and a distortion of 1.97 bits/dim, which amounts to a root mean squared error of 0.95 on a scale from 0 to 255. More than half of the lossless codelength describes imperceptible distortions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Progressive lossy compression", "weight": 1.0} -->

We can probe further into the rate-distortion behavior of our model by introducing a progressive lossy code that mirrors the form of Eq. 5: see Algorithms 3 and 4, which assume access to a procedure, such as minimal random coding, that can transmit a sample $\mathbf{x} \sim {q{(\mathbf{x})}}$ using approximately $D_{KL}\left( {{q{(\mathbf{x})}} \parallel {p{(\mathbf{x})}}} \right)$ bits on average for any distributions $p$ and $q$, for which only $p$ is available to the receiver beforehand.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Progressive lossy compression", "weight": 1.0} -->

When applied to $\mathbf{x}_{0} \sim {q{(\mathbf{x}_{0})}}$, Algorithms 3 and 4 transmit $\mathbf{x}_{T},\ldots,\mathbf{x}_{0}$ in sequence using a total expected codelength equal to Eq. 5. The receiver, at any time $t$, has the partial information $\mathbf{x}_{t}$ fully available and can progressively estimate: due to Eq. 4. (A stochastic reconstruction $\mathbf{x}_{0} \sim {p_{\theta}{(\left. \mathbf{x}_{0} \middle| \mathbf{x}_{t} \right.)}}$ is also valid, but we do not consider it here because it makes distortion more difficult to evaluate.) Figure 5 shows the resulting rate-distortion plot on the test set.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Progressive lossy compression", "weight": 1.0} -->

At each time $t$, the distortion is calculated as the root mean squared error $\sqrt{{\|{\mathbf{x}_{0} - {\hat{\mathbf{x}}}_{0}}\|}^{2}/D}$, and the rate is calculated as the cumulative number of bits received so far at time $t$. The distortion decreases steeply in the low-rate region of the rate-distortion plot, indicating that the majority of the bits are indeed allocated to imperceptible distortions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Progressive generation", "weight": 1.0} -->

We also run a progressive unconditional generation process given by progressive decompression from random bits. In other words, we predict the result of the reverse process, ${\hat{\mathbf{x}}}_{0}$, while sampling from the reverse process using Algorithm 2. Figures 6 and 10 show the resulting sample quality of ${\hat{\mathbf{x}}}_{0}$ over the course of the reverse process. Large scale image features appear first and details appear last. Figure 7 shows stochastic predictions $\mathbf{x}_{0} \sim {p_{\theta}{(\left. \mathbf{x}_{0} \middle| \mathbf{x}_{t} \right.)}}$ with $\mathbf{x}_{t}$ frozen for various $t$. When $t$ is small, all but fine details are preserved, and when $t$ is large, only large scale features are preserved. Perhaps these are hints of conceptual compression.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Connection to autoregressive decoding", "weight": 1.0} -->

Note that the variational bound 5 can be rewritten as: (See Appendix A for a derivation.) Now consider setting the diffusion process length $T$ to the dimensionality of the data, defining the forward process so that $q{(\left. \mathbf{x}_{t} \middle| \mathbf{x}_{0} \right.)}$ places all probability mass on $\mathbf{x}_{0}$ with the first $t$ coordinates masked out (i.e. $q{(\left. \mathbf{x}_{t} \middle| \mathbf{x}_{t - 1} \right.)}$ masks out the $t^{\text{th}}$ coordinate), setting $p{(\mathbf{x}_{T})}$ to place all mass on a blank image, and, for the sake of argument, taking $p_{\theta}{(\left.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Connection to autoregressive decoding", "weight": 1.0} -->

Thus, training $p_{\theta}$ with this particular diffusion is training an autoregressive model.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Connection to autoregressive decoding", "weight": 1.0} -->

We can therefore interpret the Gaussian diffusion model 2 as a kind of autoregressive model with a generalized bit ordering that cannot be expressed by reordering data coordinates. Prior work has shown that such reorderings introduce inductive biases that have an impact on sample quality, so we speculate that the Gaussian diffusion serves a similar purpose, perhaps to greater effect since Gaussian noise might be more natural to add to images compared to masking noise. Moreover, the Gaussian diffusion length is not restricted to equal the data dimension; for instance, we use $T = 1000$, which is less than the dimension of the $32 \times 32 \times 3$ or $256 \times 256 \times 3$ images in our experiments. Gaussian diffusions can be made shorter for fast sampling or longer for model expressiveness.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Interpolation", "weight": 1.0} -->

\mathbf{x}_{0} \middle| {\overline{\mathbf{x}}}_{t} \right.)}}$. In effect, we use the reverse process to remove artifacts from linearly interpolating corrupted versions of the source images, as depicted in Fig. 8 (left). We fixed the noise for different values of $\lambda$ so $\mathbf{x}_{t}$ and $\mathbf{x}_{t}'$ remain the same. Fig. 8 (right) shows interpolations and reconstructions of original CelebA-HQ $256 \times 256$ images ($t = 500$). The reverse process produces high-quality reconstructions, and plausible interpolations that smoothly vary attributes such as pose, skin tone, hairstyle, expression and background, but not eyewear. Larger $t$ results in coarser and more varied interpolations, with novel samples at $t = 1000$ (Appendix Fig. 9).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented high quality image samples using diffusion models, and we have found connections among diffusion models and variational inference for training Markov chains, denoising score matching and annealed Langevin dynamics (and energy-based models by extension), autoregressive models, and progressive lossy compression. Since diffusion models seem to have excellent inductive biases for image data, we look forward to investigating their utility in other data modalities and as components in other types of generative models and machine learning systems.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Our work on diffusion models takes on a similar scope as existing work on other types of deep generative models, such as efforts to improve the sample quality of GANs, flows, autoregressive models, and so forth. Our paper represents progress in making diffusion models a generally useful tool in this family of techniques, so it may serve to amplify any impacts that generative models have had (and will have) on the broader world.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

Unfortunately, there are numerous well-known malicious uses of generative models. Sample generation techniques can be employed to produce fake images and videos of high profile figures for political purposes. While fake images were manually created long before software tools were available, generative models such as ours make the process easier. Fortunately, CNN-generated images currently have subtle flaws that allow detection, but improvements in generative models may make this more difficult. Generative models also reflect the biases in the datasets on which they are trained. As many large datasets are collected from the internet by automated systems, it can be difficult to remove these biases, especially when the images are unlabeled. If samples from generative models trained on these datasets proliferate throughout the internet, then these biases will only be reinforced further.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Broader Impact", "weight": 1.0} -->

On the other hand, diffusion models may be useful for data compression, which, as data becomes higher resolution and as global internet traffic increases, might be crucial to ensure accessibility of the internet to wide audiences. Our work might contribute to representation learning on unlabeled raw data for a large range of downstream tasks, from image classification to reinforcement learning, and diffusion models might also become viable for creative uses in art, photography, and music.
