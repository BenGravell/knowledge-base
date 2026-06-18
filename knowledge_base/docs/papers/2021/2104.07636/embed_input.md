Image Super-Resolution via Iterative Refinement

Topics include Image super-resolution, Diffusion models, Denoising diffusion, Iterative refinement, Conditional generation, Cascaded generation, Face super-resolution, SR3.

SR3 is an early and influential diffusion-based super-resolution method, replacing deterministic regression with repeated conditional denoising from noise. Its human-evaluation results made it a key reference for the shift from PSNR-driven super-resolution toward photorealistic generative restoration.

We present SR3, an approach to image Super-Resolution via Repeated Refinement. SR3 adapts denoising diffusion probabilistic models to conditional image generation and performs super-resolution through a stochastic denoising process. Inference starts with pure Gaussian noise and iteratively refines the noisy output using a U-Net model trained on denoising at various noise levels. SR3 exhibits strong performance on super-resolution tasks at different magnification factors, on faces and natural images. We conduct human evaluation on a standard 8X face super-resolution task on CelebA-HQ, comparing with SOTA GAN methods. SR3 achieves a fool rate close to 50%, suggesting photo-realistic outputs, while GANs do not exceed a fool rate of 34%. We further show the effectiveness of SR3 in cascaded image generation, where generative models are chained with super-resolution models, yielding a competitive FID score of 11.3 on ImageNet.

## Introduction

Single-image super-resolution is the process of generating a high-resolution image that is consistent with an input low-resolution image. It falls under the broad family of image-to-image translation tasks, including colorization, in-painting, and de-blurring. Like many such inverse problems, image super-resolution is challenging because multiple output images may be consistent with a single input image, and the conditional distribution of output images given the input typically does not conform well to simple parametric distributions, e.g., a multivariate Gaussian.

Deep generative models have seen success in learning complex empirical distributions of images (e.g., ). Autoregressive models, variational autoencoders (VAEs), Normalizing Flows (NFs), and GANs have shown convincing image generation results and have been applied to conditional tasks such as image super-resolution.

We propose SR3 (Super-Resolution via Repeated Refinement), a new approach to conditional image generation, inspired by recent work on Denoising Diffusion Probabilistic Models (DDPM), and denoising score matching. SR3 works by learning to transform a standard normal distribution into an empirical data distribution through a sequence of refinement steps, resembling Langevin dynamics. The key is a U-Net architecture that is trained with a denoising objective to iteratively remove various levels of noise from the output. We adapt DDPMs to conditional image generation by proposing a simple and effective modification to the U-Net architecture.

We adapt denoising diffusion models to conditional image generation. Our method, SR3, is an approach to image super-resolution via iterative refinement.

## Discussion and Conclusion

Bias is an important problem in all generative models. SR3 is no different, and suffers from bias issues. While in theory, our log-likelihood based objective is mode covering (e.g., unlike some GAN-based objectives), we believe it is likely our diffusion-based models drop modes. We observed some evidence of mode dropping, the model consistently generates nearly the same image output during sampling (when conditioned on the same input). We also observed the model to generate very continuous skin texture in face super-resolution, dropping moles, pimples and piercings found in the reference.
