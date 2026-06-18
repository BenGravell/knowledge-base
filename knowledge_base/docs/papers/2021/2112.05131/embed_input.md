Plenoxels: Radiance Fields without Neural Networks

Topics include Radiance fields, Novel view synthesis, Computer graphics, Computer vision, Sparse voxel grid, Spherical harmonics, Differentiable rendering, Neural rendering, NeRF.

Introduces Plenoxels, an explicit sparse voxel radiance-field representation whose density and view-dependent color coefficients can be optimized directly from posed images without an MLP. The paper helped establish that high-quality NeRF-like novel view synthesis could be achieved with direct grid optimization, greatly reducing training time while preserving visual fidelity on standard benchmarks.

We introduce Plenoxels (plenoptic voxels), a system for photorealistic view synthesis. Plenoxels represent a scene as a sparse 3D grid with spherical harmonics. This representation can be optimized from calibrated images via gradient methods and regularization without any neural components. On standard, benchmark tasks, Plenoxels are optimized two orders of magnitude faster than Neural Radiance Fields with no loss in visual quality.

## Introduction

A recent body of research has capitalized on implicit, coordinate-based neural networks as the 3D representation to optimize 3D volumes from calibrated 2D image supervision. In particular, Neural Radiance Fields (NeRF) demonstrated photorealistic novel viewpoint rendering, capturing scene geometry as well as view-dependent effects. This impressive quality, however, requires extensive computation time for both training and rendering, with training lasting more than a day and rendering requiring 30 seconds per frame, on a single GPU.

In this paper, we show that we can train a radiance field from scratch, without neural networks, while maintaining NeRF quality and reducing optimization time by two orders of magnitude. We provide a custom CUDA implementation that capitalizes on the model simplicity to achieve substantial speedups. Our typical optimization time on a single Titan RTX GPU is 11 minutes on bounded scenes (compared to roughly 1 day for NeRF, more than a $100 \times$ speedup) and 27 minutes on unbounded scenes (compared to roughly 4 days for NeRF++, again more than a $100 \times$ speedup).

Specifically, we propose an explicit volumetric representation, based on a view-dependent sparse voxel grid without any neural networks. Our model can render photorealistic novel viewpoints and be optimized end-to-end from calibrated 2D photographs, using the differentiable rendering loss on training views as well as a total variation regularizer. We call our model Plenoxel for plenoptic volume elements, as it consists of a sparse voxel grid in which each voxel stores opacity and spherical harmonic coefficients. These coefficients are interpolated to model the full plenoptic function continuously in space.

## Discussion

We present a method for photorealistic scene modeling and novel viewpoint rendering that produces results with comparable fidelity to the state-of-the-art, while taking orders of magnitude less time to train. Our method is also strikingly straightforward, shedding light on the core elements that are necessary for solving 3D inverse problems: a differentiable forward model, a continuous representation (in our case, via trilinear interpolation), and appropriate regularization.
