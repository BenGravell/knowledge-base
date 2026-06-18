Understanding SSIM

Topics include Neural networks, Deep learning, Learning, Structural similarity index measure.

The use of the structural similarity index (SSIM) is widespread. For almost two decades, it has played a major role in image quality assessment in many different research disciplines. Clearly, its merits are indisputable in the research community. However, little deep scrutiny of this index has been performed. Contrary to popular belief, there are some interesting properties of SSIM that merit such scrutiny. In this paper, we analyze the mathematical factors of SSIM and show that it can generate results, in both synthetic and realistic use cases, that are unexpected, sometimes undefined, and nonintuitive. As a consequence, assessing image quality based on SSIM can lead to incorrect conclusions and using SSIM as a loss function for deep learning can guide neural network training in the wrong direction.

## Introduction

The original SSIM paper has over $20,000$ citations on Google Scholar. Thousands of research papers have used it as a quality index when comparing images, and we are indeed authors of a few of those. In this paper, we provide a review and a deep inspection of SSIM, and we show that SSIM can deliver unexpected or invalid results in both simple use cases and for real image pairs. See Figure LABEL:fig_teaser. We start with an overview of SSIM.

The input color space of SSIM is never defined. As the reference Matlab script performs no color space transformations on inputs, our assumption throughout this paper is that all images are encoded in sRGB color space, i.e., approximately gamma encoded with an exponent $\approx 2.4$. Note that this means that an image that is loaded by the SSIM script is assumed to be viewed directly on screen as is. For two images A and B, the original formula for per-pixel SSIM is given by

SSIM is at its core a statistical measure, a product of three local dissimilarity factors, namely, luminance, variance, and correlation. We have derived these factors' minima and shown how their ranges and normalization are creating nonintuitive results. This occurs, for example, for low luminance values or when the local distribution of pixel values visually differ very little, though regularly. We have also shown that the original SSIM formulation with certain parameters can output undefined results....

Current graphics and rendering research has a major focus on Monte Carlo ray tracing and denoising and reconstruction algorithms using neural networks. Such networks often introduce small variations during training and could potentially suffer disproportionately from the shortcomings of SSIM. We thus encourage further graphics research to employ the index with care and caution, or preferably replace it, since its use may distort or bias image quality assessment. The difference evaluator for alternating images ( F LIP), is a step toward such a replacement.

The claim that the $l$ factor is perceptually motivated is problematic. Evidence for this can easily be found and first, we point to Figure 4 to get a feel for this. To explain these results, we refer to Figure 3, which shows a plot of SSIM as a function of a constant colored image from black to white, against both a black and a white image....
