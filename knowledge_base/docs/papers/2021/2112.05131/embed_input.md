Plenoxels: Radiance Fields without Neural Networks

Topics include Radiance fields, Novel view synthesis, Computer graphics, Computer vision, Sparse voxel grid, Spherical harmonics, Differentiable rendering, Neural rendering, NeRF.

Introduces Plenoxels, an explicit sparse voxel radiance-field representation whose density and view-dependent color coefficients can be optimized directly from posed images without an MLP. The paper helped establish that high-quality NeRF-like novel view synthesis could be achieved with direct grid optimization, greatly reducing training time while preserving visual fidelity on standard benchmarks.

We introduce Plenoxels (plenoptic voxels), a system for photorealistic view synthesis. Plenoxels represent a scene as a sparse 3D grid with spherical harmonics. This representation can be optimized from calibrated images via gradient methods and regularization without any neural components. On standard, benchmark tasks, Plenoxels are optimized two orders of magnitude faster than Neural Radiance Fields with no loss in visual quality.

## Introduction

A recent body of research has capitalized on implicit, coordinate-based neural networks as the 3D representation to optimize 3D volumes from calibrated 2D image supervision. In particular, Neural Radiance Fields (NeRF) demonstrated photorealistic novel viewpoint rendering, capturing scene geometry as well as view-dependent effects. This impressive quality, however, requires extensive computation time for both training and rendering, with training lasting more than a day and rendering requiring 30 seconds per frame, on a single GPU....

Figure 1: Plenoxel: Plenoptic Volume Elements for fast optimization of radiance fields. We show that direct optimization of a fully explicit 3D model can match the rendering quality of modern neural based approaches such as NeRF while optimizing over two orders of magnitude faster.

Our method should extend naturally to support multiscale rendering with proper anti-aliasing through voxel cone-tracing, similar to the modifications in Mip-NeRF. Another easy addition is tone-mapping to account for white balance and exposure changes, which we expect would help especially in the real $360^{\circ}$ scenes. A hierarchical data structure (such as an octree) may provide additional speedup compared to our sparse array implementation, provided that differentiable interpolation is preserved.

Since our method is two orders of magnitude faster than NeRF, we believe that it may enable downstream applications currently bottlenecked by the performance of NeRF--for example, multi-bounce lighting and 3D generative models across large databases of scenes. By combining our method with additional components such as camera optimization and large-scale voxel hashing, it may enable a practical pipeline for end-to-end photorealistic 3D reconstruction.

Figure 3: Ablation over TV regularization. Clear artifacts are visible in the forward-facing scenes without TV on both σ and SH coefficients, although PSNR does not always reflect this.

### Coarse to Fine

Our synthetic experiments use the 8 scenes from NeRF: chair, drums, ficus, hotdog, lego, materials, mic, and ship. Each scene includes 100 ground truth training views with 800 $\times$ 800 resolution, from known camera positions distributed randomly in the upper hemisphere facing the object, which is set against a plain white background....
