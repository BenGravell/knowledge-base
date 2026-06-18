Deblurring via Stochastic Refinement

Topics include Diffusion models, Benchmarks, Sampling.

Image deblurring is an ill-posed problem with multiple plausible solutions for a given input image. However, most existing methods produce a deterministic estimate of the clean image and are trained to minimize pixel-level distortion. These metrics are known to be poorly correlated with human perception, and often lead to unrealistic reconstructions. We present an alternative framework for blind deblurring based on conditional diffusion models. Unlike existing techniques, we train a stochastic sampler that refines the output of a deterministic predictor and is capable of producing a diverse set of plausible reconstructions for a given input. This leads to a significant improvement in perceptual quality over existing state-of-the-art methods across multiple standard benchmarks. Our predict-and-refine approach also enables much more efficient sampling compared to typical diffusion models. Combined with a carefully tuned network architecture and inference procedure, our method is competitive in terms of distortion metrics such as PSNR.

## Introduction

Image deblurring is a long-standing problem in computer vision. Various conditions such as moving objects, camera shakes, or an out-of-focus lens may contribute to blurring artifacts. Single image deblurring is a highly ill-posed inverse problem where multiple plausible sharp images could lead to the very same blurry observation. Nonetheless, most existing methods produce a single deterministic estimate of the clean image.

In this work, we adopt a different perspective and view deblurring as a conditional generative modeling task, where we seek to generate diverse samples from the posterior distribution. Specifically, we introduce a "predict-and-refine" conditional diffusion model, where a deterministic data-adaptive predictor is jointly trained with a stochastic sampler that refines the output of the said predictor (see Fig. 2).

Overall, our method produces a variety of plausible and photo-realistic results, while achieving state-of-the-art performance under many quantitative metrics in terms of both distortion and perceptual quality across multiple standard datasets. In addition, by aggregating a different number of generated deblurred samples, our framework allows us to conveniently traverse the Perception-Distortion curve as shown in Fig. 1, without any expensive retraining or finetuning. These results show clear benefits of stochastic diffusion-based methods for deblurring and challenge the currently dominant strategy of producing deterministic reconstructions.

## Discussion and Analysis

For the analysis of various aspects of our model, we used a custom dataset created by applying synthetic camera shake blur and noise (described in Appendix C) on the images of the DIV2K dataset. This was done to make qualitative evaluation in a more controlled environment, since the low-quality ground truth images in existing paired datasets make qualitative assessment difficult.
