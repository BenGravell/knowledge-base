Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling

Topics include Computational complexity, Optimization, Learning, Sampling, LM, Conjugate gradient, CG, Line search.

3D Gaussian Splatting (3DGS) is widely used for novel view synthesis due to its high rendering quality and fast inference time. However, 3DGS predominantly relies on first-order optimizers such as Adam, which leads to long training times. To address this limitation, we propose a novel second-order optimization strategy based on Levenberg-Marquardt (LM) and Conjugate Gradient (CG), specifically tailored towards Gaussian Splatting. Our key insight is that the Jacobian in 3DGS exhibits significant sparsity since each Gaussian affects only a limited number of pixels. We exploit this sparsity by proposing a matrix-free and GPU-parallelized LM optimization. To further improve its efficiency, we propose sampling strategies for both camera views and loss function and, consequently, the normal equation, significantly reducing the computational complexity. In addition, we increase the convergence rate of the second-order approximation by introducing an effective heuristic to determine the learning rate that avoids the expensive computation cost of line search methods.

## Introduction

Photoreal novel view synthesis from multi-view images or video has attracted significant attention in recent years due to widely applicable downstream tasks in content creation, VR/XR, gaming, and the movie industry, to name a few. Here, Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) mark a major milestone, due to their unprecedented quality leading to follow ups beyond view synthesis like VR rendering, avatar creation, simultaneous localization and mapping (SLAM), and scene editing.

To overcome these challenges, we propose a GPU-parallelized matrix-free conjugate gradient solver coupled with pixel sampling, which circumvents explicit storage of the Jacobian matrix and solves the matrix inverse iteratively. Firstly, we show that implementing a matrix-free solver naively does not result in a fast optimizer because of the high computational cost of Jacobian-vector products. Therefore, we propose to approximate the full normal equation by an effective view sampling strategy and by sampling individual pixels, which results in significantly faster convergence.

## Limitations

We use only a diagonally approximated SSIM loss for performance reasons, which may affect the convergence behavior. Future work could explore more efficient implementations enabling the use of full SSIM loss. In addition, our matrix-free implementation requires more intermediate vectors than Adam, leading $3 \times$ higher memory usage.

## Conclusion

By leveraging the inherent sparsity of the Jacobian matrix and integrating a GPU-parallelized conjugate gradient solver, our method significantly reduces the computational overhead. Our novel view and pixel-wise sampling further enhance efficiency, enabling rapid convergence by decreasing the per-step overhead. Additionally, our dynamic learning rate scheduler eliminates the need for costly line search procedures, further accelerating training. Our approach achieves up to $5 \times$ speedup over Adam, particularly excelling in scenarios with low number of Gaussians.
