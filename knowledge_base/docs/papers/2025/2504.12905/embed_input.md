Matrix-free Second-order Optimization of Gaussian Splats with Residual Sampling

Topics include Computational complexity, Optimization, Learning, Sampling, LM, Conjugate gradient, CG, Line search.

3D Gaussian Splatting (3DGS) is widely used for novel view synthesis due to its high rendering quality and fast inference time. However, 3DGS predominantly relies on first-order optimizers such as Adam, which leads to long training times. To address this limitation, we propose a novel second-order optimization strategy based on Levenberg-Marquardt (LM) and Conjugate Gradient (CG), specifically tailored towards Gaussian Splatting. Our key insight is that the Jacobian in 3DGS exhibits significant sparsity since each Gaussian affects only a limited number of pixels. We exploit this sparsity by proposing a matrix-free and GPU-parallelized LM optimization. To further improve its efficiency, we propose sampling strategies for both camera views and loss function and, consequently, the normal equation, significantly reducing the computational complexity. In addition, we increase the convergence rate of the second-order approximation by introducing an effective heuristic to determine the learning rate that avoids the expensive computation cost of line search methods....

## Introduction

Figure 1: We introduce a matrix-free second-order optimizer for Gaussian Splatting. Notably, our dedicated optimizer converges significantly faster than Adam and already achieves reasonable renderings after very few seconds of training.

Photoreal novel view synthesis from multi-view images or video has attracted significant attention in recent years due to widely applicable downstream tasks in content creation, VR/XR, gaming, and the movie industry, to name a few. Here, Neural Radiance Fields (NeRF) \[\] and 3D Gaussian Splatting (3DGS) \[\] mark a major milestone, due to their unprecedented quality leading to follow ups beyond view synthesis like VR rendering \[\], avatar creation \[\], simultaneous localization and mapping (SLAM), and scene editing.

## Conclusion

By leveraging the inherent sparsity of the Jacobian matrix and integrating a GPU-parallelized conjugate gradient solver, our method significantly reduces the computational overhead. Our novel view and pixel-wise sampling further enhance efficiency, enabling rapid convergence by decreasing the per-step overhead. Additionally, our dynamic learning rate scheduler eliminates the need for costly line search procedures, further accelerating training. Our approach achieves up to $5 \times$ speedup over Adam, particularly excelling in scenarios with low number of Gaussians....

### View Sampling

### Levenberg-Marquardt Optimizer for 3DGS

Note that this approximation preserves the symmetry and positive semi-definiteness of $\mathbf{J}^{\top}\mathbf{J}$, a property required for the convergence of the conjugate gradient algorithm.

However, NeRF-based models often require substantial training time, and researchers have developed various techniques to mitigate this problem. Some of them include neural hashing \[\], employing explicit scene modeling \[\], improved sampling strategies \[\], and tensor factorization methods \[\]. 3DGS \[\] instead does not rely on coordinate-based representations, but leverages a set of 3D Gaussians, which can be effectively rendered into image space using tile-based rasterization. Nonetheless, optimizing the parameters of each Gaussian can still take hours....

Second-order optimization is known for having better convergence guarantees compared to first-order methods....
