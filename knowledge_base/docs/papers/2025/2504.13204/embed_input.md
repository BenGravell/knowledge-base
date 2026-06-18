EDGS: Eliminating Densification for Efficient Convergence of 3DGS

Topics include 3D Gaussian splatting, Scene reconstruction, Dense initialization, Densification, Computer vision, Neural rendering.

Replaces iterative Gaussian-splat densification with a dense one-step initialization derived from image correspondences. The paper targets the slow convergence and high-frequency artifacts of standard 3DGS training by starting optimization from a more complete geometric scaffold.

3D Gaussian Splatting reconstructs scenes by starting from a sparse Structure-from-Motion initialization and refining under-reconstructed regions. This process is slow, as it requires multiple densification steps where Gaussians are repeatedly split and adjusted, following a lengthy optimization path. Moreover, this incremental approach often yields suboptimal renderings in high-frequency regions. We propose a fundamentally different approach: eliminate densification with a one-step approximation of scene geometry using triangulated pixels from dense image correspondences. This dense initialization allows us to estimate the rough geometry of the scene while preserving rich details from input RGB images, providing each Gaussian with well-informed color, scale, and position. As a result, we dramatically shorten the optimization path and remove the need for densification. Unlike methods that rely on sparse keypoints, our dense initialization ensures uniform detail across the scene, even in high-frequency regions where other methods struggle.

## Introduction

Reconstructing 3D scenes from collections of 2D images is a fundamental challenge in computer vision, with applications in virtual and augmented reality, robotics, and content creation. The goal is to obtain high-quality 3D representations efficiently, enabling real-time rendering while maintaining reconstruction fidelity. However, achieving balance between efficiency, speed, and quality requires a representation that is both expressive and computationally efficient.

In this paper, we propose a direct initialization strategy that eliminates the need for incremental densification used in the original 3DGS method. Rather than waiting for the model to gradually fill in missing details, we precompute a dense set of 3D Gaussians by triangulating dense 2D correspondences across multiple input views. Knowing the viewing rays for each correspondence pixel and the camera poses, we recover 3D positions of Gaussians by triangulating matched pixels between image pairs. This allows us to assign each Gaussian well-informed initial parameters, such as position, color, and scale, from the start.

Although this initialization is noisy (see Fig. 1), we show that it remains robust and leads to faster convergence. Our experiments, quantitatively and qualitatively, confirm that EDGS yields higher reconstruction quality, shorter training time, fewer Gaussians, and eliminates the need for densification.

We introduce a novel dense initialization for 3D Gaussian Splatting, based on the sampling distribution of triangulated multi-view correspondences, which effectively replaces the traditional incremental refinement process.

## Conclusion

We introduce a new initialization strategy for 3D Gaussian Splatting that removes the need for iterative densification. The approach relies on carefully sampling 2D correspondences that are both geometrically consistent and provide uniform, dense coverage of the scene.

Our method reaches state-of-the-art performance without any densification and matches efficiency-oriented methods with substantially fewer optimization steps. Moreover, EDGS functions as a plug-and-play initialization for adaptive density control techniques, improving reconstruction quality without increasing training time or Gaussian count, making it a practical and broadly applicable enhancement for 3D reconstruction pipelines.
