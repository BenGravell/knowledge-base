3D Gaussian Splatting for Real-Time Radiance Field Rendering

Topics include 3D Gaussian splatting, Gaussian splat, Gaussian splatting, 3D scene, Rendering, Real-time, Graphics processing unit, Ellipsoid.

Seminal paper that introduced 3D Gaussian Splatting, a rendering technique that optimizes the pose, shape, transparency, and view-dependent optic properties (modeled with spherical harmonics) of a large collection of 3D Gaussians (ellipsoidal distributions) to reconstruct a ground truth represented by multiple 2D image views (typically collected by taking photos or video from multiple views around an object or scene). The trained Gaussians are rendered via differentiable tile-based rasterization, enabling high-quality novel view synthesis at real-time frame rates.

Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (>= 30 fps) novel-view synthesis at 1080p resolution....

## Introduction

Meshes and points are the most common 3D scene representations because they are explicit and are a good fit for fast GPU/CUDA-based rasterization. In contrast, recent Neural Radiance Field (NeRF) methods build on continuous scene representations, typically optimizing a Multi-Layer Perceptron (MLP) using volumetric ray-marching for novel-view synthesis of captured scenes. Similarly, the most efficient radiance field solutions to date build on continuous representations by interpolating values stored in, e.g., voxel or hash grids or points....

Our goal is to allow real-time rendering for scenes captured with multiple photos, and create the representations with optimization times as fast as the most efficient previous methods for typical real scenes. Recent methods achieve fast training, but struggle to achieve the visual quality obtained by the current SOTA NeRF methods, i.e., Mip-NeRF360, which requires up to 48 hours of training time. The fast -- but lower-quality -- radiance field methods can achieve interactive rendering times depending on the scene (10-15 frames per second), but fall short of real-time rendering at high resolution.

It would be interesting to see if our Gaussians can be used to perform mesh reconstructions of the captured scene. Aside from practical implications given the widespread use of meshes, this would allow us to better understand where our method stands exactly in the continuum between volumetric and surface representations.

In conclusion, we have presented the first real-time rendering solution for radiance fields, with rendering quality that matches the best expensive previous methods, with training times competitive with the fastest existing solutions.

## Fast Differentiable Rasterizer for Gaussians

To allow independent optimization of both factors, we store them separately: a 3D vector $s$ for scaling and a quaternion $q$ to represent rotation. These can be trivially converted to their respective matrices and combined, making sure to normalize $q$ to obtain a valid unit quaternion.

We tested our algorithm on a total of 13 real scenes taken from previously published datasets and the synthetic Blender dataset. In particular, we tested our approach on the full set of scenes presented in Mip-Nerf360, which is the current state of the art in NeRF rendering quality, two scenes from the Tanks&Temples...
