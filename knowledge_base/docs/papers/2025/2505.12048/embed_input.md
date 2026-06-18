Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling

Diffusion models have gained attention for their success in modeling complex distributions, achieving impressive perceptual quality in SR tasks. However, existing diffusion-based SR methods often suffer from high computational costs, requiring numerous iterative steps for training and inference. Existing acceleration techniques, such as distillation and solver optimization, are generally task-agnostic and do not fully leverage the specific characteristics of low-level tasks like super-resolution (SR). In this study, we analyze the frequency- and spatial-domain properties of diffusion-based SR methods, revealing key insights into the temporal and spatial dependencies of high-frequency signal recovery. Specifically, high-frequency details benefit from concentrated optimization during early and late diffusion iterations, while spatially textured regions demand adaptive denoising strategies. Building on these observations, we propose the Time-Spatial-aware Sampling strategy (TSS) for the acceleration of Diffusion SR without any extra training cost....

## Introduction

Figure 1: (a) SNR of different frequency components in SUPIR denoising, where high-frequency signals show a unique two-stage pattern. (b) SNR of high-frequency signals in different spatial regions during the denoising process of SUPIR. (c) Noise amplitude in high-frequency regions of SUPIR denoising: higher variance shortens the positive optimization phase. (d) Denoising visualization of a sample.

Image super-resolution (SR) Wang et al.; Zhang et al.; Liang et al.; Qin et al.; Liu et al.; Zhao et al.; Qin et al.; Bao et al. aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs. Recently, diffusion models Ho et al.; Song et al. have gained attention for their ability to model complex distributions, achieving notable success in SR Chen et al.; Wang et al.; Yang et al.; Yu et al.; Wu et al.; Qu et al., particularly in perceptual quality Wang et al.; Wu et al.....

## Conclusion

In this work, we explore key insights in the denoising process: high-frequency components require focused optimization in early and late iterations, while spatially varying content necessitates adaptive strategies for effective restoration. Based on these findings, we propose Time-Spatial-aware Sampling (TSS), a training-free, content-adaptive sampling strategy to accelerate diffusion-based image super-resolution. By leveraging temporal and spatial dependencies in high-frequency recovery, TSS enhances texture restoration while significantly reducing computational costs....

where $v_{g_{i,j}}$ denotes the local variance at position $(i,j)$ which controls $a$ and $n$. The spatial timestep $t_{spatial_{k}}$ for the $k^{th}$ denoising iteration represents a set of timesteps for each pixel,

Generality. The strategy should exhibit robust generalizability, enabling flexible integration across a wide range of established super-resolution frameworks.

### Evaluation Metrics

Efforts to accelerate denoising generation focus on sampler acceleration and distillation, achieving results in 10 or fewer steps Yue et al.; Wang et al.. Most Diffusion SR methods Wang et al.; Yu et al.; Yang et al. adopt these general strategies without considering the unique frequency characteristics of low-level vision tasks. However, in fact, recent studies like STAR Xie et al....
