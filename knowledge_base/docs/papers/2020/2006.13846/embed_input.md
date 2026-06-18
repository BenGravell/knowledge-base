Understanding SSIM

Topics include Neural networks, Deep learning, Learning, Structural similarity index measure.

The use of the structural similarity index (SSIM) is widespread. For almost two decades, it has played a major role in image quality assessment in many different research disciplines. Clearly, its merits are indisputable in the research community. However, little deep scrutiny of this index has been performed. Contrary to popular belief, there are some interesting properties of SSIM that merit such scrutiny. In this paper, we analyze the mathematical factors of SSIM and show that it can generate results, in both synthetic and realistic use cases, that are unexpected, sometimes undefined, and nonintuitive. As a consequence, assessing image quality based on SSIM can lead to incorrect conclusions and using SSIM as a loss function for deep learning can guide neural network training in the wrong direction.

## Introduction

The original SSIM paper has over $20,000$ citations on Google Scholar. Thousands of research papers have used it as a quality index when comparing images, and we are indeed authors of a few of those. In this paper, we provide a review and a deep inspection of SSIM, and we show that SSIM can deliver unexpected or invalid results in both simple use cases and for real image pairs. See Figure LABEL:fig_teaser. We start with an overview of SSIM.

The input color space of SSIM is never defined. As the reference Matlab script performs no color space transformations on inputs, our assumption throughout this paper is that all images are encoded in sRGB color space, i.e., approximately gamma encoded with an exponent $\approx 2.4$. Note that this means that an image that is loaded by the SSIM script is assumed to be viewed directly on screen as is. For two images A and B, the original formula for per-pixel SSIM is given by

where A and B are inputs to all functions, but omitted for clarity. To compute mean, variance, and covariance in a patch around a pixel, they use Gaussian-weighted versions of these formulae with a filter kernel of $11 \times 11$ pixels and $\sigma = 1.5$. The luminance component, $l$, is then

where $w$ and $h$ are the width and height of the image. As can be seen, the term $\sigma_{\text{A}}\sigma_{\text{B}}$ is in the numerator in Equation 3 and in the denominator in Equation 4. To create a simplified expression, Wang et al. therefore proposed to use $\alpha = \beta = \gamma = 1$ and $C_{3} = {C_{2}/2}$, which results in
