Exploiting Diffusion Prior for Real-World Image Super-Resolution

Topics include Image super-resolution, Real-world super-resolution, Blind restoration, Diffusion models, Stable diffusion, Generative prior, Time-aware encoder, Feature wrapping, StableSR.

StableSR adapts a pretrained text-to-image diffusion model for blind real-world super-resolution while keeping the synthesis model fixed. Its time-aware encoder, controllable feature wrapping, and progressive aggregation sampling make the diffusion prior more practical for fidelity-controlled restoration at arbitrary image sizes.

We present a novel approach to leverage prior knowledge encapsulated in pre-trained text-to-image diffusion models for blind super-resolution (SR). Specifically, by employing our time-aware encoder, we can achieve promising restoration results without altering the pre-trained synthesis model, thereby preserving the generative prior and minimizing training cost. To remedy the loss of fidelity caused by the inherent stochasticity of diffusion models, we employ a controllable feature wrapping module that allows users to balance quality and fidelity by simply adjusting a scalar value during the inference process. Moreover, we develop a progressive aggregation sampling strategy to overcome the fixed-size constraints of pre-trained diffusion models, enabling adaptation to resolutions of any size. A comprehensive evaluation of our method using both synthetic and real-world benchmarks demonstrates its superiority over current state-of-the-art approaches. Code and models are available at

## Introduction

We have seen significant advancements in diffusion models for the task of image synthesis. Existing studies demonstrate that the diffusion prior, embedded in synthesis models like Stable Diffusion, can be applied to various downstream content creation tasks, including image (Choi et al. Avrahami et al. Hertz et al. Gu et al. Mou et al. Zhang et al. Gal et al., ) and video (Wu et al. Molad et al. Qi et al., ) editing. In this study, we extend the exploration beyond the realm of content creation and examine the potential benefits of using diffusion prior for super-resolution (SR).

In this study, we present StableSR, an approach that preserves pre-trained diffusion priors without making explicit assumptions about the degradations. Specifically, unlike previous works that concatenate the LR image to intermediate outputs, which requires one to train a diffusion model from scratch, our method only needs to fine-tune a lightweight time-aware encoder and a few feature modulation layers for the SR task.

Applying diffusion models to arbitrary resolutions has remained a persistent challenge, especially for the SR task. A simple solution would be to split the image into patches and process each independently. However, this method often leads to boundary discontinuity in the output. To address this issue, we introduce a progressive aggregation sampling strategy. Inspired by Jiménez, our approach involves dividing the image into overlapping patches and fusing these patches using a Gaussian kernel at each diffusion iteration. This process smooths out the boundaries, resulting in a more coherent output.

## Limitations

Though benefiting from the diffusion prior, StableSR also shares similar limitations with it. Specifically, StableSR may struggle in handling small texts, faces and patterns as shown in Fig.. While these cases are challenging for existing generic super-resolution approaches including StableSR, we believe adopting a more powerful diffusion prior and training on more high-quality data can help. We leave these as future work.
