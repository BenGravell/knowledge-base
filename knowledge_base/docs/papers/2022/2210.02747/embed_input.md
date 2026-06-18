Flow Matching for Generative Modeling

Topics include Robustness, Diffusion models, Generalization, Sampling, Normalizing flows, Optimal transport, FM, Flow matching, Generative model.

We introduce a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing us to train CNFs at unprecedented scale. Specifically, we present the notion of Flow Matching (FM), a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths. Flow Matching is compatible with a general family of Gaussian probability paths for transforming between noise and data samples - which subsumes existing diffusion paths as specific instances. Interestingly, we find that employing FM with diffusion paths results in a more robust and stable alternative for training diffusion models. Furthermore, Flow Matching opens the door to training CNFs with other, non-diffusion probability paths. An instance of particular interest is using Optimal Transport (OT) displacement interpolation to define the conditional probability paths. These paths are more efficient than diffusion paths, provide faster training and sampling, and result in better generalization....

## Introduction

Deep generative models are a class of deep learning algorithms aimed at estimating and sampling from an unknown data distribution. The recent influx of amazing advances in generative modeling, e.g., for image generation Ramesh et al.; Rombach et al., is mostly facilitated by the scalable and relatively stable training of diffusion-based models Ho et al.; Song et al.. However, the restriction to simple diffusion processes leads to a rather confined space of sampling probability paths, resulting in very long training times and the need to adopt specialized methods (e.g., Song et al.; Zhang & Chen ) for efficient sampling.

In this work we consider the general and deterministic framework of Continuous Normalizing Flows (CNFs; Chen et al. ). CNFs are capable of modeling arbitrary probability path

## Social responsibility

Along side its many positive applications, image generation can also be used for harmful proposes. Using content-controlled training sets and image validation/classification can help reduce these uses. Furthermore, the energy demand for training large deep learning models is increasing at a rapid pace, focusing on methods that are able to train using less gradient updates / image throughput can lead to significant time and energy savings.

### Special instances of Gaussian conditional probability paths

### Conditional Flow Matching

where $\psi:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is the OT map pushing $p_{0}$ to $p_{1}$, $id$ denotes the identity map, i.e., ${{id}{(x)}} = x$, and ${{({1 - t})}{id}} + {t\psi}$ is called the OT displacement map. Example 1.7 in McCann shows, that in our case of two Gaussians where the first is a standard one, the OT displacement map takes the form of equation 22.

Figure 1: Unconditional ImageNet-128 samples of a CNF trained using Flow Matching with Optimal Transport probability paths.

and are in particular known to encompass the probability paths modeled by diffusion processes. However, aside from diffusion that can be trained efficiently via, e.g., denoising score matching, no scalable CNF training algorithms are known. Indeed, maximum likelihood training (e.g., Grathwohl et al. ) require expensive numerical ODE simulations, while existing simulation-free methods either involve intractable integrals or biased gradients.
