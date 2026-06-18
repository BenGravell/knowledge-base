<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Image Super-Resolution via Iterative Refinement

Topics include Image super-resolution, Diffusion models, Denoising diffusion, Iterative refinement, Conditional generation, Cascaded generation, Face super-resolution, SR3.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

SR3 is an early and influential diffusion-based super-resolution method, replacing deterministic regression with repeated conditional denoising from noise. Its human-evaluation results made it a key reference for the shift from PSNR-driven super-resolution toward photorealistic generative restoration.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present SR3, an approach to image Super-Resolution via Repeated Refinement. SR3 adapts denoising diffusion probabilistic models to conditional image generation and performs super-resolution through a stochastic denoising process. Inference starts with pure Gaussian noise and iteratively refines the noisy output using a U-Net model trained on denoising at various noise levels. SR3 exhibits strong performance on super-resolution tasks at different magnification factors, on faces and natural images. We conduct human evaluation on a standard 8X face super-resolution task on CelebA-HQ, comparing with SOTA GAN methods. SR3 achieves a fool rate close to 50%, suggesting photo-realistic outputs, while GANs do not exceed a fool rate of 34%. We further show the effectiveness of SR3 in cascaded image generation, where generative models are chained with super-resolution models, yielding a competitive FID score of 11.3 on ImageNet.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Single-image super-resolution is the process of generating a high-resolution image that is consistent with an input low-resolution image. It falls under the broad family of image-to-image translation tasks, including colorization, in-painting, and de-blurring. Like many such inverse problems, image super-resolution is challenging because multiple output images may be consistent with a single input image, and the conditional distribution of output images given the input typically does not conform well to simple parametric distributions, e.g., a multivariate Gaussian. Accordingly, while simple regression-based methods with feedforward convolutional nets may work for super-resolution at low magnification ratios, they often lack the high-fidelity details needed for high magnification ratios.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep generative models have seen success in learning complex empirical distributions of images (e.g., ). Autoregressive models, variational autoencoders (VAEs), Normalizing Flows (NFs), and GANs have shown convincing image generation results and have been applied to conditional tasks such as image super-resolution. However, these approaches often suffer from various limitations; e.g., autoregressive models are prohibitively expensive for high-resolution image generation, NFs and VAEs often yield sub-optimal sample quality, and GANs require carefully designed regularization and optimization tricks to tame optimization instability and mode collapse.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose SR3 (Super-Resolution via Repeated Refinement), a new approach to conditional image generation, inspired by recent work on Denoising Diffusion Probabilistic Models (DDPM), and denoising score matching. SR3 works by learning to transform a standard normal distribution into an empirical data distribution through a sequence of refinement steps, resembling Langevin dynamics. The key is a U-Net architecture that is trained with a denoising objective to iteratively remove various levels of noise from the output. We adapt DDPMs to conditional image generation by proposing a simple and effective modification to the U-Net architecture. In contrast to GANs that require inner-loop maximization, we minimize a well-defined loss function. Unlike autoregressive models, SR3 uses a constant number of inference steps regardless of output resolution.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

SR3 works well across a range of magnification factors and input resolutions. SR3 models can also be cascaded, e.g., going from $64 \times 64$ to $256 \times 256$, and then to $1024 \times 1024$. Cascading models allows one to independently train a few small models rather than a single large model with a high magnification factor. We find that chained models enable more efficient inference, since directly generating a high-resolution image requires more iterative refinement steps for the same quality. We also find that one can chain an unconditional generative model with SR3 models to unconditionally generate high-fidelity images. Unlike existing work that focuses on specific domains (e.g., faces), we show that SR3 is effective on both faces and natural images.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Automated image quality scores like PSNR and SSIM do not reflect human preference well when the input resolution is low and the magnification ratio is large (e.g., ). These quality scores often penalize synthetic high-frequency details, such as hair texture, because synthetic details do not perfectly align with the reference details. We resort to human evaluation to compare the quality of super-resolution methods. We adopt a 2-alternative forced-choice (2AFC) paradigm in which human subjects are shown a low-resolution input and are required to select between a model output and a ground truth image (cf. ). Based on this study, we calculate fool rate scores that capture both image quality and the consistency of model outputs with low-resolution inputs. Experiments demonstrate that SR3 achieves a significantly higher fool rate than SOTA GAN methods and a strong regression baseline.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We adapt denoising diffusion models to conditional image generation. Our method, SR3, is an approach to image super-resolution via iterative refinement.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

SR3 proves effective on face and natural image super-resolution at different magnification factors. On a standard 8$\times$ face super-resolution task, SR3 achieves a human fool rate close to $50\%$, outperforming FSRGAN and PULSE that achieve fool rates of at most 34%.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate unconditional and class-conditional generation by cascading a $64 \times 64$ image synthesis model with SR3 models to progressively generate $1024 \times 1024$ unconditional faces in 3 stages, and $256 \times 256$ class-conditional ImageNet samples in 2 stages. Our class conditional ImageNet samples attain competitive FID scores.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Conditional Denoising Diffusion Model", "weight": 1.0} -->

We are given a dataset of input-output image pairs, denoted $\mathcal{D} = {\{{\mathbf{x}}_{i},{\mathbf{y}}_{i}\}}_{i = 1}^{N}$, which represent samples drawn from an unknown conditional distribution $p{(\left. {\mathbf{y}} \middle| {\mathbf{x}} \right.)}$. This is a one-to-many mapping in which many target images may be consistent with a single source image. We are interested in learning a parametric approximation to $p{(\left. {\mathbf{y}} \middle| {\mathbf{x}} \right.)}$ through a stochastic iterative refinement process that maps a source image $\mathbf{x}$ to a target image ${\mathbf{y}} \in {\mathbb{R}}^{d}$. We approach this problem by adapting the denoising diffusion probabilistic (DDPM) model of to conditional image generation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Conditional Denoising Diffusion Model", "weight": 1.0} -->

The distributions of intermediate images in the inference chain are defined in terms of a forward diffusion process that gradually adds Gaussian noise to the signal via a fixed Markov chain, denoted $q{(\left. {\mathbf{y}}_{t} \middle| {\mathbf{y}}_{t - 1} \right.)}$. The goal of our model is to reverse the Gaussian diffusion process by iteratively recovering signal from noise through a reverse Markov chain conditioned on $\mathbf{x}$. In principle, each forward process step can be conditioned on $\mathbf{x}$ too, but we leave that to future work. We learn the reverse chain using a neural denoising model $f_{\theta}$ that takes as input a source image and a noisy target image and estimates the noise. We first give an overview of the forward diffusion process, and then discuss how our denoising model $f_{\theta}$ is trained and used for inference.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Gaussian Diffusion Process", "weight": 1.0} -->

where the scalar parameters $\alpha_{1:T}$ are hyper-parameters, subject to $0 < \alpha_{t} < 1$, which determine the variance of the noise added at each iteration. Note that ${\mathbf{y}}_{t - 1}$ is attenuated by $\sqrt{\alpha_{t}}$ to ensure that the variance of the random variables remains bounded as $t\rightarrow\infty$. For instance, if the variance of ${\mathbf{y}}_{t - 1}$ is $1$, then the variance of ${\mathbf{y}}_{t}$ is also $1$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gaussian Diffusion Process", "weight": 1.0} -->

Importantly, one can characterize the distribution of ${\mathbf{y}}_{t}$ given ${\mathbf{y}}_{0}$ by marginalizing out the intermediate steps as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gaussian Diffusion Process", "weight": 1.0} -->

This posterior distribution is helpful when parameterizing the reverse chain and formulating a variational lower bound on the log-likelihood of the reverse chain. We next discuss how one can learn a neural network to reverse this Gaussian diffusion process.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimizing the Denoising Model", "weight": 1.0} -->

5: Take a gradient descent step on
6:$\nabla_{\theta}\left. \parallel f_{\theta}\left( {\mathbf{x}},\sqrt{\gamma}{\mathbf{y}}_{0} + \sqrt{1 - \gamma}\mathbf{\epsilon},\gamma \right) - \mathbf{\epsilon}\parallel \right._{p}^{p}$
Algorithm 1 Training a denoising model fθ

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimizing the Denoising Model", "weight": 1.0} -->

To help reverse the diffusion process, we take advantage of additional side information in the form of a source image $\mathbf{x}$ and optimize a neural denoising model $f_{\theta}$ that takes as input this source image $\mathbf{x}$ and a noisy target image $\overset{\sim}{\mathbf{y}}$,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimizing the Denoising Model", "weight": 1.0} -->

and aims to recover the noiseless target image ${\mathbf{y}}_{0}$. This definition of a noisy target image $\overset{\sim}{\mathbf{y}}$ is compatible with the marginal distribution of noisy images at different steps of the forward diffusion process.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimizing the Denoising Model", "weight": 1.0} -->

In addition to a source image $\mathbf{x}$ and a noisy target image $\overset{\sim}{\mathbf{y}}$, the denoising model $f_{\theta}{({\mathbf{x}},\overset{\sim}{\mathbf{y}},\gamma)}$ takes as input the sufficient statistics for the variance of the noise $\gamma$, and is trained to predict the noise vector $\mathbf{\epsilon}$. We make the denoising model aware of the level of noise through conditioning on a scalar $\gamma$, similar to. The proposed objective function for training $f_{\theta}$ is

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimizing the Denoising Model", "weight": 1.0} -->

where $\mathbf{\epsilon} \sim {\mathcal{N}{(\mathbf{0},{\mathbf{I}})}}$, $({\mathbf{x}},{\mathbf{y}})$ is sampled from the training dataset, $p \in {\{ 1,2\}}$, and $\gamma \sim {p{(\gamma)}}$. The distribution of $\gamma$ has a big impact on the quality of the model and the generated outputs. We discuss our choice of $p{(\gamma)}$ in Section 2.4.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimizing the Denoising Model", "weight": 1.0} -->

Instead of regressing the output of $f_{\theta}$ to $\mathbf{\epsilon}$, as, one can also regress the output of $f_{\theta}$ to ${\mathbf{y}}_{0}$. Given $\gamma$ and $\overset{\sim}{\mathbf{y}}$, the values of $\mathbf{\epsilon}$ and ${\mathbf{y}}_{0}$ can be derived from each other deterministically, but changing the regression target has an impact on the scale of the loss function. We expect both of these variants to work reasonably well if $p{(\gamma)}$ is modified to account for the scale of the loss function. Further investigation of the loss function used for training the denoising model is an interesting avenue for future research in this area.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Inference via Iterative Refinement", "weight": 1.0} -->

We define the inference process in terms of isotropic Gaussian conditional distributions, $p_{\theta}{(\left. {\mathbf{y}}_{t - 1} \middle| {{\mathbf{y}}_{t},{\mathbf{x}}} \right.)}$, which are learned. If the noise variance of the forward process steps are set as small as possible, i.e., $\alpha_{1:T} \approx 1$, the optimal reverse process $p{(\left. {\mathbf{y}}_{t - 1} \middle| {{\mathbf{y}}_{t},{\mathbf{x}}} \right.)}$ will be approximately Gaussian. Accordingly, our choice of Gaussian conditionals in the inference process can provide a reasonable fit to the true reverse process.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Inference via Iterative Refinement", "weight": 1.0} -->

Meanwhile, $1 - \gamma_{T}$ should be large enough so that ${\mathbf{y}}_{T}$ is approximately distributed according to the prior ${p{({\mathbf{y}}_{T})}} = {\mathcal{N}{(\left. {\mathbf{y}}_{T} \middle| {\mathbf{0},{\mathbf{I}}} \right.)}}$, allowing the sampling process to start at pure Gaussian noise.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Inference via Iterative Refinement", "weight": 1.0} -->

Recall that the denoising model $f_{\theta}$ is trained to estimate $\mathbf{\epsilon}$, given any noisy image $\overset{\sim}{\mathbf{y}}$ including ${\mathbf{y}}_{t}$. Thus, given ${\mathbf{y}}_{t}$, we approximate ${\mathbf{y}}_{0}$ by rearranging the terms in as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Inference via Iterative Refinement", "weight": 1.0} -->

Following this parameterization, each iteration of iterative refinement under our model takes the form,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Inference via Iterative Refinement", "weight": 1.0} -->

where $\mathbf{\epsilon}_{t} \sim {\mathcal{N}{(\mathbf{0},{\mathbf{I}})}}$. This resembles one step of Langevin dynamics with $f_{\theta}$ providing an estimate of the gradient of the data log-density. We justify the choice of the training objective in for the probabilistic model outlined in from a variational lower bound perspective and a denoising score-matching perspective in Appendix B.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SR3 Model Architecture and Noise Schedule", "weight": 1.0} -->

The SR3 architecture is similar to the U-Net found in DDPM, with modifications adapted; we replace the original DDPM residual blocks with residual blocks from BigGAN, and we re-scale skip connections by $\frac{1}{\sqrt{2}}$. We also increase the number of residual blocks, and the channel multipliers at different resolutions (see Appendix A for details). To condition the model on the input $\mathbf{x}$, we up-sample the low-resolution image to the target resolution using bicubic interpolation. The result is concatenated with ${\mathbf{y}}_{t}$ along the channel dimension. We experimented with more sophisticated methods of conditioning, such as using FiLM, but we found that the simple concatenation yielded similar generation quality.

<!-- chunk {"id": "body-0029", "role": "body", "section": "SR3 Model Architecture and Noise Schedule", "weight": 1.0} -->

For our training noise schedule, we follow, and use a piece wise distribution for $\gamma$, ${p{(\gamma)}} = {\sum_{t = 1}^{T}{\frac{1}{T}U{(\gamma_{t - 1},\gamma_{t})}}}$. Specifically, during training, we first uniformly sample a time step $t \sim {\{ 0,\ldots,T\}}$ followed by sampling $\gamma \sim {U{(\gamma_{t - 1},\gamma_{t})}}$. We set $T = 2000$ in all our experiments.

<!-- chunk {"id": "body-0030", "role": "body", "section": "SR3 Model Architecture and Noise Schedule", "weight": 1.0} -->

Prior work of diffusion models require 1-2k diffusion steps during inference, making generation slow for large target resolution tasks. We adapt techniques from to enable more efficient inference. Our model conditions on $\gamma$ directly (vs $t$ as in ), which allows us flexibility in choosing number of diffusion steps, and the noise schedule during inference. This has been demonstrated to work well for speech synthesis, but has not been explored for images. For efficient inference we set the maximum inference budget to 100 diffusion steps, and hyper-parameter search over the inference noise schedule. This search is inexpensive as we only need to train the model once. We use FID on held out data to choose the best noise schedule, as we found PSNR did not correlate well with image quality.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

We assess the effectiveness of SR3 models in super-resolution on faces, natural images, and synthetic images obtained from a low-resolution generative model. The latter enables high-resolution image synthesis using model cascades. We compare SR3 with recent methods such as FSRGAN and PULSE using human evaluation^22^2Samples generously provided by the authors of, and report FID for various tasks. We also compare to a regression baseline model that shares the same architecture as SR3, but is trained with a MSE loss.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Face super-resolution at ${16 \times 16}\rightarrow{128 \times 128}$ and ${64 \times 64}\rightarrow{512 \times 1512}$ trained on FFHQ and evaluated on CelebA-HQ.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Natural image super-resolution at ${64 \times 64}\rightarrow{256 \times 256}$ pixels on ImageNet.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Unconditional $1024 \times 1024$ face generation by a cascade of 3 models, and class-conditional $256 \times 256$ ImageNet image generation by a cascade of 2 models.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Datasets: We follow previous work, training face super-resolution models on Flickr-Faces-HQ (FFHQ) and evaluating on CelebA-HQ. For natural image super-resolution, we train on ImageNet 1K and use the dev split for evaluation. We train unconditional face and class-conditional ImageNet generative models using DDPM on the same datasets discussed above. For training and testing, we use low-resolution images that are down-sampled using bicubic interpolation with anti-aliasing enabled. For ImageNet, we discard images where the shorter side is less than the target resolution. We use the largest central crop like, which is then resized to the target resolution using area resampling as our high resolution image.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Training Details: We train all of our SR3 and regression models for 1M training steps with a batch size of 256. We choose a checkpoint for the regression baseline based on peak-PSNR on the held out set. We do not perform any checkpoint selection on SR3 models and simply select the latest checkpoint. Consistent, we use the Adam optimizer with a linear warmup schedule over 10k training steps, followed by a fixed learning rate of 1e-4 for SR3 models and 1e-5 for regression models. We use 625M parameters for our ${64 \times 64}\rightarrow{\{{256 \times 256},{512 \times 512}\}}$ models, 550M parameters for the 16$\times$`<!-- -->`{=html}16 $\rightarrow$ 128$\times$`<!-- -->`{=html}128 models, and 150M parameters for 256$\times$`<!-- -->`{=html}256 $\rightarrow$ 1024$\times$`<!-- -->`{=html}1024 model.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

We use a dropout rate of 0.2 for 16$\times$`<!-- -->`{=html}16 $\rightarrow$ 128$\times$`<!-- -->`{=html}128 models super-resolution, but otherwise, we do not use dropout. (See Appendix A for task specific architectural details.)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Natural Images: Figure 3 gives examples of super-resolution natural images for 64$\times$`<!-- -->`{=html}64 $\rightarrow$ 256$\times$`<!-- -->`{=html}256 on the ImageNet dev set, along with enlarged patches for finer inspection. The baseline Regression model generates images that are faithful to the inputs, but are blurry and lack detail. By comparison, SR3 produces sharp images with more detail; this is most evident in the enlarged patches. For more samples see Appendix C.3 and C.4.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Face Images: Figure 4 shows outputs of a face super-resolution model (${64 \times 64}\rightarrow{512 \times 512}$) on two test images, again with selected patches enlarged. With the 8$\times$ magnification factor one can clearly see the detailed structure inferred. Note that, because of the large magnification factor, there are many plausible outputs, so we do not expect the output to exactly match the reference image. This is evident in the regions highlighted in the faces. For more samples see Appendix C.1 and C.2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Automated metrics", "weight": 1.0} -->

Table 1 shows the PSNR, SSIM and Consistency scores for 16$\times$`<!-- -->`{=html}16 $\rightarrow$ 128$\times$`<!-- -->`{=html}128 face super-resolution. SR3 outperforms PULSE and FSRGAN on PSNR and SSIM while underperforming the regression baseline. Previous work observed that these conventional automated evaluation measures do not correlate well with human perception when the input resolution is low and the magnification factor is large. This is not surprising because these metrics tend to penalize any synthetic high-frequency detail that is not perfectly aligned with the target image. Since generating perfectly aligned high-frequency details, e.g., the exact same hair strands in Figure 4 and identical leopard spots in Figure 3, is almost impossible, PSNR and SSIM tend to prefer MSE regression-based techniques that are extremely conservative with high-frequency details.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Automated metrics", "weight": 1.0} -->

This is further confirmed in Table 2 for ImageNet super-resolution (${64 \times 64}\rightarrow{256 \times 256}$) where the outputs of SR3 achieve higher sample quality scores (FID and IS), but worse PSNR and SSIM than regression.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Automated metrics", "weight": 1.0} -->

Consistency: As a measure of the consistentcy of the super-resolution outputs, we compute MSE between the downsampled outputs and the low resolution inputs. Table 1 shows that SR3 achieves the best consistency error beating PULSE and FSRGAN by a significant margin slightly outperforming even the regression baseline. This result demonstrates the key advantage of SR3 over state of the art GAN based methods as they do not require any auxiliary objective function in order to ensure consistency with the low resolution inputs.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Automated metrics", "weight": 1.0} -->

Classification Accuracy: Table 3 compares our 4$\times$ natural image super-resolution models with previous work in terms of object classification on low-resolution images. We mirror the evaluation setup of and apply 4$\times$ super-resolution models to 56$\times$`<!-- -->`{=html}56 center crops from the validation set of ImageNet.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Automated metrics", "weight": 1.0} -->

Then, we report classification error based on a pre-trained ResNet-50. Since, our super-resolution models are trained on the task of 64$\times$`<!-- -->`{=html}64 $\rightarrow$ 256$\times$`<!-- -->`{=html}256, we use bicubic interpolation to resize the input 56$\times$`<!-- -->`{=html}56 to 64$\times$`<!-- -->`{=html}64, then we apply 4$\times$ super-resolution, followed by resizing back to 224$\times$`<!-- -->`{=html}224. SR3 outperforms existing methods by a large margin on top-1 and top-5 classification errors, demonstrating high perceptual quality of SR3 outputs. The Regression model achieves strong performance compared to existing methods demonstrating the strength of our baseline model. However, SR3 significantly outperforms Regression re-affirming the limitation of conventional metrics such as PSNR and SSIM.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Automated metrics", "weight": 1.0} -->

Fool rates (3 sec display w/ inputs, 16 × 16 → 128 × 128)
Fool rates (3 sec display w/o inputs, 16 × 16 → 128 × 128)
Figure 6: Face super-resolution human fool rates (higher is better, photo-realistic samples yield a fool rate of 50%). Outputs of 4 models are compared against ground truth. (top) Subjects are shown low-resolution inputs. (bottom) Inputs are not shown.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

In this work, we are primarily interested in photo-realistic super-resolution with large magnification factors. Accordingly, we resort to direct human evaluation. While mean opinion score (MOS) is commonly used to measure image quality in this context, forced choice pairwise comparison has been found to be a more reliable method for such subjective quality assessments. Furthermore, standard MOS studies do not capture consistency between low-resolution inputs and high-resolution outputs. We use a 2-alternative forced-choice (2AFC) paradigm to measure how well humans can discriminate true images from those generated from a model. In Task-1 subjects were shown a low resolution input in between two high-resolution images, one being the real image (ground truth), and the other generated from the model. Subjects were asked "Which of the two images is a better high quality version of the low resolution image in the middle?" This task takes into account both image quality and consistency with the low resolution input. Task-2 is similar to Task-1, except that the low-resolution image was not shown, so subjects only had to select the image that was more photo-realistic.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

They were asked "Which image would you guess is from a camera?" Subjects viewed images for 3 seconds before responding, in both tasks. The source code for human evaluation can be found here ^33^3

<!-- chunk {"id": "body-0048", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

The subject fool rate is the fraction of trials on which a subject selects the model output over ground truth. Our fool rates for each model are based on 50 subjects, each of whom were shown 50 of the 100 images in the test set. Figure 6 shows the fool rates for Task-1 (top), and for Task-2 (bottom). In both experiments, the fool rate of SR3 is close to 50%, indicating that SR3 produces images that are both photo-realistic and faithful to the low-resolution inputs. We find similar fool rates over a wide range of viewing durations up to 12 seconds.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

The fool rates for FSRGAN and PULSE in Task-1 are lower than the Regression baseline and SR3. We speculate that the PULSE optimization has failed to converge to high resolution images sufficiently close to the inputs. Indeed, when asked solely about image quality in Task-2 (Fig. 6 (bottom)), the PULSE fool rate increases significantly.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

The fool rate for the Regression baseline is lower in Task-2 (Fig. 6 (bottom)) than Task-1. The regression model tends to generate images that are blurry, but nevertheless faithful to the low resolution input. We speculate that in Task-1, given the inputs, subjects are influenced by consistency, while in Task-2, ignoring consistency, they instead focus on image sharpness. SR3 and Regression samples used for human evaluation are provided here ^44^4

<!-- chunk {"id": "body-0051", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

Fool rates (3 sec display w/ inputs, 64 × 64 → 256 × 256)
Fool rates (3 sec display w/o inputs, 64 × 64 → 256 × 256)
Figure 7: ImageNet super-resolution fool rates (higher is better, photo-realistic samples yield a fool rate of 50%). SR3 and Regression outputs are compared against ground truth. (top) Subjects are shown low-resolution inputs. (bottom) Inputs are not shown.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

We conduct similar human evaluation studies on natural images comparing SR3 and the regression baseline on ImageNet. Figure 7 ‣ 4.2 Benchmark Comparison ‣ 4 Experiments ‣ Image Super-Resolution via Iterative Refinement") shows the results for Task-1 (top) and task-2 (bottom). In both tasks with natural images, SR3 achieves a human subject fool rate is close to 40%. Like the face image experiments in Fig. 6, here again we find that the Regression baseline yields a lower fool rate in Task-2, where the low resolution image is not shown. Again we speculate that this is a result of a somewhat simpler task (looking at 2 rather than 3 images), and the fact that subjects can focus solely on image artifacts, such as blurriness, without having to worry about consistency between model output and the low resolution input.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Human Evaluation (2AFC)", "weight": 1.0} -->

To further appreciate the experimental results it is useful to visually compare outputs of different models on the same inputs, as in Figure 5. FSRGAN exhibits distortion in face region and struggles with generating glasses properly (e.g., top row). It also fails to recover texture details in the hair region (see bottom row). PULSE often produces images that differ significantly from the input image, both in the shape of the face and the background, and sometimes in gender too (see bottom row) presumably due to failure of the optimization to find a sufficiently good minima. As noted above, our Regression baseline produces results consistent to the input, however they are typically quite blurry. By comparison, the SR3 results are consistent with the input and contain more detailed image structure.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Cascaded High-Resolution Image Synthesis", "weight": 1.0} -->

We study cascaded image generation, where SR3 models at different scales are chained together with unconditional generative models, enabling high-resolution image synthesis. Cascaded generation allows one to train different models in parallel, and each model in the cascade solves a simpler task, requiring fewer parameters and less computation for training. Inference with cascaded models is also more efficient, especially for iterative refinement models. With cascaded generation we found it effective to use more refinement steps at low-resolutions, and fewer steps at higher resolutions. This was much more efficient than generating directly at high resolution without sacrificing image quality.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Cascaded High-Resolution Image Synthesis", "weight": 1.0} -->

We train a DDPM model for unconditional $64 \times 64$ face generation. Samples from this model are then fed to two 4$\times$ SR3 models, up-sampling to $256^{2}$ and then to $1024^{2}$ pixels. Synthetic high-resolution face samples are shown in Figure 8. In addition, we train an Improved DDPM model on class-conditional $64 \times 64$ ImageNet, and we pass its generated samples to a 4$\times$ SR3 model yielding $256^{2}$ pixels. The 4$\times$ SR3 model is not conditioned on the class label. See Figure 9 for representative samples.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Cascaded High-Resolution Image Synthesis", "weight": 1.0} -->

Table 4 reports FID scores for the resulting class-conditional ImageNet samples. Our 2-stage model improves on VQ-VAE-2, is comparable to deep BigGANs at truncation factor of 1.5 but underperforms them a truncation factor of $1.0$. Unlike BigGAN, our diffusion models do not provide a knob to control sample quality vs. sample diversity, and finding ways to do so is interesting avenue for future research. Nichol and Dhariwal concurrently trained cascaded generation models using super-resolution conditioned on class labels (our super-resolution is not conditioned on class labels), and observed a similar trend in FID scores. The effectiveness of cascaded image generation indicates that SR3 models are robust to the precise distribution of inputs (i.e., the specific form of anti-aliasing and downsampling).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Cascaded High-Resolution Image Synthesis", "weight": 1.0} -->

Ablation Studies: Table 5 shows ablation studies on our ${64 \times 64}\rightarrow{256 \times 256}$ Imagenet SR3 model. In order to improve the robustness of the SR3 model, we experiment with use of data augmentation while training. Specifically, we trained the model with varying amounts of Gaussian Blurring noise added to the low resolution input image. No blurring is applied during inference. We find that this has a siginificant impact, improving the FID score roughly by 2 points. We also explore the choice of $L_{p}$ norm for the denoising objective (Equation 6). We find that $L_{1}$ norm gives slightly better FID scores than $L_{2}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Bias is an important problem in all generative models. SR3 is no different, and suffers from bias issues. While in theory, our log-likelihood based objective is mode covering (e.g., unlike some GAN-based objectives), we believe it is likely our diffusion-based models drop modes. We observed some evidence of mode dropping, the model consistently generates nearly the same image output during sampling (when conditioned on the same input). We also observed the model to generate very continuous skin texture in face super-resolution, dropping moles, pimples and piercings found in the reference. SR3 should not be used for any real world super-resolution tasks, until these biases are thoroughly understood and mitigated.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In conclusion, SR3 is an approach to image super-resolution via iterative refinement. SR3 can be used in a cascaded fashion to generate high resolution super-resolution images, as well as unconditional samples when cascaded with a unconditional model. We demonstrate SR3 on face and natural image super-resolution at high resolution and high magnification ratios (e.g., 64$\times$`<!-- -->`{=html}64$\rightarrow$`<!-- -->`{=html}256$\times$`<!-- -->`{=html}256 and 256$\times$`<!-- -->`{=html}256$\rightarrow$`<!-- -->`{=html}1024$\times$`<!-- -->`{=html}1024). SR3 achieves a human fool rate close to 50%, suggesting photo-realistic outputs.
