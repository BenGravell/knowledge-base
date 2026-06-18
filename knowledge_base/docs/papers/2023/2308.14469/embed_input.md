Pixel-Aware Stable Diffusion for Realistic Image Super-Resolution and Personalized Stylization

Topics include Image super-resolution, Real-world super-resolution, Image restoration, Stable diffusion, Diffusion models, Pixel-aware attention, Image stylization, Degradation removal, PASD.

PASD adds pixel-aware conditioning to Stable Diffusion so that its generative prior can be used for realistic super-resolution without losing local structure. The same conditioning design also lets the method act as a bridge between restoration and stylization by swapping the underlying diffusion model.

Diffusion models have demonstrated impressive performance in various image generation, editing, enhancement and translation tasks. In particular, the pre-trained text-to-image stable diffusion models provide a potential solution to the challenging realistic image super-resolution (Real-ISR) and image stylization problems with their strong generative priors. However, the existing methods along this line often fail to keep faithful pixel-wise image structures. If extra skip connections between the encoder and the decoder of a VAE are used to reproduce details, additional training in image space will be required, limiting the application to tasks in latent space such as image stylization. In this work, we propose a pixel-aware stable diffusion (PASD) network to achieve robust Real-ISR and personalized image stylization. Specifically, a pixel-aware cross attention module is introduced to enable diffusion models perceiving image local structures in pixel-wise level, while a degradation removal module is used to extract degradation insensitive features to guide the diffusion process together with image high level information....

## Introduction

Real-world images often suffer from a mixture of complex degradations, such as low resolution, blur, noise, etc., in the acquisition process. While image restoration methods have achieved significant progress, especially in the era of deep learning, they still tend to generate over-smoothed details, partially due to the pursue of image fidelity in the methodology design. By relaxing the constraint on image fidelity, realistic image super-resolution (Real-ISR) aims to reproduce perceptually realistic image details from the degraded observation....

Recently, denoising diffusion probabilistic models (DDPMs) have shown outstanding performance in tasks of image generation \[\], and it has become a strong alternative to GAN due to its powerful capability in approximating diverse and complicated distributions. With DDPM, the pre-trained text-to-image (T2I) and text-to-video (T2V) latent diffusion models have been popularly used in numerous downstream tasks, including personalized image generation, image editing, image inpainting \[\] and conditional image synthesis \[\]. Diffusion models have also been adopted to solve image restoration tasks....

We proposed a pixel-aware diffusion network, namely PASD, for realistic image restoration and personalized stylization. By introducing a pixel-aware cross attention module, PASD succeeded in perceiving image local structures in pixel-level and achieved robust and perceptually realistic Real-ISR results. An adjustable noise schedule was also proposed, which helped PASD to achieve flexible perception-fidelity trade-off during the inference stage. By replacing the base model to a personalized one, PASD could produce diverse stylization results with highly consistent semantic contents with the input....

Though PASD can achieve pixel-level enhancement, it still suffers from the balance between fidelity and perception. In addition, it may fail to reproduce faithful details when the input image is heavily degraded or the semantic information is inaccurate. A more robust degradation estimation module can be designed, and more precise semantic information can be extracted to further improve the performance of PASD, which will be considered in our future work.

### Experiment Setup

In this way, by choosing a proper value of ${\overline{\alpha}}_{a}$, we can adjust the strength of the residual signal...
