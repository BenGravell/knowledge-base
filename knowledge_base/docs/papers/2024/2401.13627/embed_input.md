Scaling up to Excellence: Practicing Model Scaling for Photo-Realistic Image Restoration in the Wild

Topics include Image restoration, Image super-resolution, Real-world restoration, Generative prior, Model scaling, Text-guided restoration, Negative-quality prompts, Restoration-guided sampling, SUPIR.

SUPIR scales generative image restoration with a large annotated high-quality image corpus, prompt-aware restoration, negative-quality prompts, and restoration-guided sampling. It is notable less as a narrow architecture tweak and more as evidence that low-level restoration benefits strongly from data and model scale.

We introduce SUPIR (Scaling-UP Image Restoration), a groundbreaking image restoration method that harnesses generative prior and the power of model scaling up. Leveraging multi-modal techniques and advanced generative prior, SUPIR marks a significant advance in intelligent and realistic image restoration. As a pivotal catalyst within SUPIR, model scaling dramatically enhances its capabilities and demonstrates new potential for image restoration. We collect a dataset comprising 20 million high-resolution, high-quality images for model training, each enriched with descriptive text annotations. SUPIR provides the capability to restore images guided by textual prompts, broadening its application scope and potential. Moreover, we introduce negative-quality prompts to further improve perceptual quality. We also develop a restoration-guided sampling method to suppress the fidelity issue encountered in generative-based restoration. Experiments demonstrate SUPIR's exceptional restoration effects and its novel capacity to manipulate restoration through textual prompts.

## Introduction

The development of image restoration (IR) has greatly elevated expectations for both the perceptual effects and the intelligence of IR results. IR methods based on generative priors leverage powerful pre-trained generative models to introduce high-quality generation and prior knowledge into IR, bringing significant progress in these aspects. Continuously improving the capabilities of the generative prior is key to achieving better IR results, with model scaling being a crucial and effective approach. There are many tasks that have obtained astonishing improvements from scaling, such as SAM and large language models (LLMs).

In this work, we introduce SUPIR (Scaling-UP IR), the largest-ever IR method, aimed at exploring greater potential in restoration visual effects and intelligence. Specifically, SUPIR employs StableDiffusion-XL (SDXL) as a powerful generative prior, which contains 2.6 billion parameters. To effectively deploy this model in IR, we design and train a large-scale adaptor that incorporates a novel component named the ZeroSFT connector. To maximize the benefits of model scaling, we collect a dataset of over 20 million high-quality, high-resolution images, each accompanied by detailed descriptive text.

Our work goes far beyond simply scaling. While pursuing an increase in model scale, we face a series of complex challenges. First, existing adaptor designs either too simple to meet the complex requirements of IR or are too large to train together with SDXL. To solve this problem, we trim the ControlNet and designed a new connector called ZeroSFT to work with the pre-trained SDXL, aiming to efficiently implement the IR task while reducing computing costs.

## Conclusion

We propose SUPIR as a pioneering IR method, empowered by model scaling, dataset enrichment, and advanced design features, expanding the horizons of IR with enhanced perceptual quality and controlled textual prompts.
