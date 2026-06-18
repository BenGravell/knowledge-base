3D Gaussian Splatting for Real-Time Radiance Field Rendering

Topics include 3D Gaussian splatting, Gaussian splat, Gaussian splatting, 3D scene, Rendering, Real-time, Graphics processing unit, Ellipsoid.

Seminal paper that introduced 3D Gaussian Splatting, a rendering technique that optimizes the pose, shape, transparency, and view-dependent optic properties (modeled with spherical harmonics) of a large collection of 3D Gaussians (ellipsoidal distributions) to reconstruct a ground truth represented by multiple 2D image views (typically collected by taking photos or video from multiple views around an object or scene). The trained Gaussians are rendered via differentiable tile-based rasterization, enabling high-quality novel view synthesis at real-time frame rates.

Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= 30 fps) novel-view synthesis at 1080p resolution.

## Introduction

Meshes and points are the most common 3D scene representations because they are explicit and are a good fit for fast GPU/CUDA-based rasterization. In contrast, recent Neural Radiance Field (NeRF) methods build on continuous scene representations, typically optimizing a Multi-Layer Perceptron (MLP) using volumetric ray-marching for novel-view synthesis of captured scenes. Similarly, the most efficient radiance field solutions to date build on continuous representations by interpolating values stored , e.g., voxel or hash grids or points.

Our solution builds on three main components. We first introduce *3D Gaussians* as a flexible and expressive scene representation. We start with the same input as previous NeRF-like methods, i.e., cameras calibrated with Structure-from-Motion (SfM) and initialize the set of 3D Gaussians with the sparse point cloud produced for free as part of the SfM process. In contrast to most point-based solutions that require Multi-View Stereo (MVS) data, we achieve high-quality results with only SfM points as input. Note that for the NeRF-synthetic dataset, our method achieves high quality even with random initialization.

To

## Limitations

Our method is not without limitations. In regions where the scene is not well observed we have artifacts; in such regions, other methods also struggle (e.g., Mip-NeRF360 in Fig. 11). Even though the anisotropic Gaussians have many advantages as described above, our method can create elongated artifacts or "splotchy" Gaussians (see Fig. 12); again previous methods also struggle in these cases.

We also occasionally have popping artifacts when our optimization creates large Gaussians; this tends to happen in regions with view-dependent appearance. One reason for these popping artifacts is the trivial rejection of Gaussians via a guard band in the rasterizer. A more principled culling approach would alleviate these artifacts. Another factor is our simple visibility algorithm, which can lead to Gaussians suddenly switching depth/blending order. This could be addressed by antialiasing, which we leave as future work.

While we used the same hyperparameters for our full evaluation, early experiments show that reducing the position learning rate can be necessary to converge in very large scenes (e.g., urban datasets).
