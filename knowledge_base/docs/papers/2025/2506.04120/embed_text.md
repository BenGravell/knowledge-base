<!-- arxiv-full-text:v1 {"arxiv_id": "2506.04120", "source": "arxiv-html"} -->

## Introduction

Creating physically accurate and visually realistic simulations directly from real-world robot interactions is crucial for scalable robotics, yet bridging the visual and physical sim-to-real gap remains a major hurdle, especially with imperfect data. While recent advances like Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) generate high-quality photorealistic novel views, they face significant challenges in dynamic robotic settings: they are sensitive to noisy camera poses common in real trajectories, and produce representations ill-suited for direct use in physics simulators like MuJoCo. Extracting usable simulation assets often requires laborious post-processing or separate geometry estimation pipelines, breaking the link between visual input and physical behaviour. This disconnect critically limits the automated creation of high-fidelity digital twins for robot learning and planning.

We argue that overcoming this requires tackling scene appearance reconstruction, object geometry extraction, and robot/camera calibration jointly within a single, end-to-end differentiable framework. This paper introduces such a framework, enabling the learning of explicit simulation scenes directly from imperfect, dynamic robot trajectory data. Our key innovation is the development of a single representation that combines SplatMesh, a hybrid scene representation that tightly couples 3DGS for appearance with explicit mesh geometry, with differentiable physics states.

Our end-to-end optimization pipeline leverages differentiable rendering and differentiable physics using MuJoCo MJX. This allows visual discrepancies to directly propagate gradients back through the entire system, simultaneously refining not only the 3DGS appearance but also the underlying mesh geometry, estimated robot poses, and camera parameters. This unified approach eliminates the need for separate processing steps and leverages visual feedback to ground the physical reconstruction, proving effective even with imperfect real robot platforms. We demonstrate the effectiveness of our framework on object reconstruction with the low-cost ALOHA bi-manual manipulator using only onboard RGB sensors and a pre-existing, imperfect robot model.

Our contributions are as follows: *End-to-End Real-to-Sim Pipeline:* A fully differentiable framework jointly optimizing scene appearance, object geometry, robot poses, and camera parameters directly from raw RGB sequences.

*Scene Reconstruction from Imperfect Data:* Demonstrated reconstruction of dynamic robot scenes, including novel objects, from noisy monocular trajectories captured by real robots.

*Simulation-Ready Asset Generation:* Controllable reconstruction of object meshes suitable for direct integration into physics engines, driven by visual consistency.

## Related work

### 3D scene reconstruction

Radiance fields represent a 3D scene in terms of a rendering function which determines the view-dependent color and opacity of each point $(x,y,z)$ in the 3D space of the scene. Evaluating this along the 3D rays for each pixel enables the scene to be consistently rendered from arbitrary camera viewpoints. This function can be parameterized in different ways - implicitly via Neural Networks as in such as Neural Radiance Fields, or explicitly as in 3D Gaussian Splatting (3DGS).

The key assumption of these methods is knowledge of the 3D structure of the generation process of the multi-view image data, usually by requiring scene to be static across the image views. The camera parameters must also be known precisely, typically by preprocessing with COLMAP which also performs best on static scenes.

Render robot kinematics Learn novel object mesh Learning from dynamic scenes Table 1: Feature Comparison of 3DGS robotics simulators

### Real2Sim robotics with radiance fields

Beyond the computer graphics community, there has been considerable research into radiance fields applied to robotics. Several recent works obtain 3DGS representations able to render a robot arm and its articulated poses, such as. A 3DGS representation of the robot is learned either from its CAD model or from manually collected posed photographs, and the Gaussians then segmented according to the robot model. A learned mapping between the kinematic configurations and part poses is used to render the robot in arbitrary joint configurations. Articulated 3DGS models must also be learned for each simulated interaction object. Such models can be applied to trajectory tracking via inverse video, sim-to-real policy learning in visually realistic simulations (e.g. ), or physical property estimation. We compare the features of these works with ours in table 1. We additionally focus on the ability to fit models to imprecise low-cost robots without separate data collection steps.

### Object-based scene decomposition

Many applications require compositionally structured scenes with objects. Pre-trained instance segmentation models enable masking the objects of interest, before fitting the masked images separately with local radiance fields. For example, uses the Detic model combined with NeRF, while combines SAM with 3DGS, and considers various methods together with CropFormer.

## Problem setting

Given a reasonable but inaccurate simulation of our robot, and samples of real observation data, we wish to recover an accurate simulation of our scene, including new scene geometry.

### Fitting models with prediction errors

For any simulation of a system we can always consider "prediction error": how well do the simulator predicted observations agree with data from the real world?

Formally, given a multi-modal robot observation $Y$ composed of $I$ modality specific components, $Y = {(y_{1},\ldots,y_{I})}$, we choose divergence functions $d_{i}{(\cdots,\cdots)}$ and weights $\beta_{i} \in {\mathbb{R}}$. Our idealized simulator is a model that generates observations from physics states $s \in \mathcal{S}$: $Y' = {m{(s)}}$. As the physics state may be large and is not necessarily differentiable, we will further consider perturbations from a base state $s' = {f{(s_{0},\theta)}}$ with respect to a selected parameter set $\theta \in \Theta$. We can then finally define our loss as the weighted sum of the divergence terms over each observation component:

### Real-world constraints in robotics

This high-level scheme is very general, so to ground our investigation, we consider a realistic real-to-simulation problem: access to a simulator with reasonably accurate geometry and kinematics, but not perfect system identification or camera calibration. The scene also contains an unmodelled novel object, and must be learned from on-board robot sensors without additional data collection. We consider the ALOHA2 low-cost bi-manual tabletop manipulation platform, together with its associated open-source MuJoCo model. This limits us to four RGB cameras, two fixed and two mounted on the moving wrists. The robot has 6 degrees of freedom in each arm and 1 in each gripper, with Dynamixel actuators.

This setting poses obstacles for standard 3DGS data collection and scene modelling: a small number of cameras enables only a constrained range of viewpoints; the motion of the robot arms makes the scenes dynamic; camera position estimates are noisy due to timing, backlash, imperfect encoder calibration etc. These challenging conditions mean several popular pipeline components are not applicable here. We tested COLMAP on both masked object images, and on the full image trajectories, but could not obtain coherent estimates across the cameras. Moreover, as shown in the Appendix, object segmentation models like SAM2 can provide good segmentations for semantic scene objects, but are not effective for segmenting elements like the robot body that have little texture, lack clear semantic descriptions, and are easily confounded with similar distractor elements in the scene background. To evaluate the recovered simulation, we perform calibration of camera extrinsics and robot pose, novel view synthesis, and novel object geometry reconstruction.

## Method

### System overview

Figure 2: Fitting with differentiable rendering. We optimize the scene parameters θ, consisting of object vertices, 3D Gaussian parameters, camera poses and robot joint angles, uniquely using real-world data acquired by robot sensors.

We propose a general framework that solves a diverse range of tasks in a real, low-cost, bi-manual robot setting via end-to-end optimization of all the components in our scene. To achieve our goal, we implement a prediction error optimization scheme using automatic differentiation and GPU acceleration. Specifically, we first collect real RGB images and robot states from recorded robot trajectories to build a model of our scene. For this purpose, we propose a novel scene representation that enables end-to-end optimization of all the represented elements. Then, we optimize the required components via this robot trajectory data alone, using differentiable physics simulation and differentiable rendering. Please refer to the Appendix for full details.

### Scene representation

### SplatMesh

We represent scene objects using SplatMesh, a hybrid representation combining a triangle mesh for geometry with 3D Gaussians for appearance (Fig. 1). 3D Gaussians are constrained to lie on the surface of the mesh faces, and their orientations transform as the underlying mesh moves. Decoupling visual and geometry information allows flexibility to learn the appearance, pose, and/or shapes of each element, or to treat these as fixed by the original model.

To optimize the geometry, we deform the vertices while preserving the underlying connectivity. This approach maintains a consistent mesh topology, ensuring a fixed and controllable number of vertices and faces. The optimization of the explicit underlying geometry offers two key advantages. First, it enables the direct incorporation of mesh regularization terms into the optimization objective, promoting desirable properties such as smoothness and mesh uniformity. Second, it provides precise control over mesh complexity, resulting in computationally efficient simulations of the reconstructions.

The mean $\mu$ of each Gaussian is initialized using a weighted barycentric coordinate approach. Given a face defined by the vertices ${\mathbf{v}_{\mathbf{1}},\mathbf{v}_{\mathbf{2}},\mathbf{v}_{\mathbf{3}}} \in {\mathbb{R}}^{3}$, we randomly sample barycentric weights (implicitly summing to 1) to determine the Gaussians positions: Each 3D Gaussian is further parameterized by a covariance $\Sigma \in {\mathbb{R}}^{3 \times 3}$, view-dependent spherical harmonics coefficients representing color, and an opacity term $o \in {\lbrack 0,1\rbrack}$. Object appearance is rendered through the differentiable rasterization of the 3D Gaussians. All SplatMesh parameters, encompassing both appearance and geometry, can be optimized via supervision from RGB images thanks to the differentiable pipeline connecting geometry, Gaussians, and the final rendering.

### End-to-end optimization

Given a set of input images and an initial scene composed of a coarse mesh, e.g. a sphere, and a set of 3D Gaussians, our framework iteratively refines this representation by minimizing the photometric error between the rendered and the ground-truth images. This enables the optimization of both the scene geometry, represented by the underlying mesh, and the appearance defined by the 3D Gaussian representation. We adopt the differentiable rasterization pipeline , including a custom CUDA kernel for efficient forward and backward passes.

Additionally, we leverage recent advancements in 3DGS-based surface reconstruction, specifically the use of surface elements or surfels. Surfels, similar to 3DGS, are geometric primitives associated with a 2D covariance matrix. In contrast to we simultaneously optimize Gaussians constrained to the mesh while clamping the covariance in the normal direction to a tiny constant, rather than learning unconstrained surfels and subsequently inferring a mesh.

The precise objective function we optimize can be varied to suit the specific task, and we typically include a weighted sum of terms from three broad families:\Photometric losses: We use $L_{1}$ or $L_{2}$ losses between predicted and ground truth RGB pixel values to supervise the optimization of the 3D Gaussians.\Geometric regularization: Explicitly optimizing geometry jointly with appearance, we can incorporate Laplacian regularization $L_{LL}$ which penalizes deviations of a vertex from the centroid of its nearest neighbors, thus promoting a smooth surface. We can also use estimates of geometry from other models, e.g. surface normals.\Object segmentation: An $L_{2}$ silhouette masking loss. This loss compares the predicted silhouette, obtained by adapting the 3D Gaussian rasterizer to object-identity values, against a ground truth object mask obtained using SAM2. However, the binary nature of the ground-truth mask presents a challenge as non-overlapping regions provide no gradient information. To address this, we smooth the binary mask with the Euclidean Distance Transform. This smoothing ensures that gradients can propagate throughout the image, even in areas where the predicted and ground-truth silhouettes do not initially overlap.

## Results

To highlight the contribution of our proposed general framework, we demonstrate its capabilities in novel-view synthesis, geometry reconstruction, and 3D asset generation on two datasets: Simulation: A synthetic dataset, generated using the YCB objects, consists of 50 posed images for each of 64 objects. This dataset was divided 80%/20% into train and test sets.\Real-to-sim: A novel dataset captured on the ALOHA2 platform consisting of 6 observation trajectories (approx. 800 frames in total) including multiview RGB from 4 cameras together with recorded joint angles. 16 frames from the moving cameras were held out for evaluation.

All our experiments are run on a single GPU NVIDIA H100 (80GB VRAM). Please refer to the Appendix for more details.

### Simulation

### Geometry reconstruction

We assess the quality of SplatMesh-based object reconstruction on the Simulated YCB dataset. Reconstruction quality was evaluated using the Chamfer Distance (CD) computed on 10 000 points sampled uniformly on both the ground truth and reconstructed meshes. Our full framework obtains ${CD} = {0.073{mm}^{2}}$. Without Laplacian mesh regularization we see increased geometric error (${CD} = {0.237{mm}^{2}}$) due to high frequency artifacts. An alternative ablation without the surface-aligned Gaussians (surfels) constraint obtains ${CD} = {0.122{mm}^{2}}$.

While our method directly optimize a mesh, NeRFacto produces a radiance field without explicit geometry. The meshes we recovered with NeRFacto's Poisson Surface reconstruction pipeline displayed significant artifacts, e.g. floaters and reconstruction of the background, and we were not able to compare them.

### Novel-view synthesis

Figure 3: Recovering real world assets from robot data only.

We benchmark our method in simulation against two radiance-field techniques: NeRFacto, a state-of-the-art implementation of NeRF in the nerfstudio framework, and 3DGS, also implemented in nerfstudio. The strong performance in novel-view synthesis and fast reconstruction make these approaches well-suited for robotics applications. All methods are optimized for 15000 iterations. Additionally, we conduct an ablation study to investigate the influence of mesh reconstruction regularization terms on novel-view synthesis. Specifically, the performance of the proposed reconstruction method is assessed both with and without the inclusion of Laplacian and average edge length loss functions, and without constraining the covariance. Tab. 2 shows our results when compared to benchmarks and ablations. We report the standard photometric quality metrics commonly utilized in radiance-field techniques: Peak Signal-to-Noise-Ratio (PSNR), Structural Similarity Index (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) between the predicted and ground truth images across all YCB objects.

Ours w/o mesh reg.

Table 2: Novel-view synthesis metrics on the simulated YCB object dataset after 15K iterations.

Unlike NeRF, which often exhibits artifacts like "floaters" due to unconstrained volumetric density, our method bounds Gaussians to desired surfaces, leading to higher photometric quality. 3DGS relies on iterative heuristic procedures, such as pruning, cloning, and splitting Gaussians, which necessitate careful tuning and often require several iterations. In contrast, our method benefits from a streamlined optimization process, achieving high-quality reconstructions within a fixed budget of 15000 iterations ( 3-4 minutes). The inclusion of mesh regularization terms results in an increased visual quality, with a PSNR of 30.91, compared to a PSNR of 30.70 when regularization was not applied. Without regularization, a uniform weight ($\lambda_{L1} = 0.1$) was assigned to the reconstruction loss. When regularization terms were incorporated, object-specific weighting ($\lambda_{LL} \in {\lbrack 0.1,1.0\rbrack}$ and $\lambda_{E} \in {\lbrack 0.01,0.1\rbrack}$) are employed to accommodate varying levels of guidance required by different objects. Additionally, an ablation study on surfel constraints shows the importance of restricting the 3D Gaussian covariance matrices. Unconstrained Gaussians can expand arbitrarily in 3D space, artificially achieving desired colors or opacities by adopting background colors or near-full transparency. This behavior, while potentially leading to overfitting on training views, results in poor generalization to unseen views.

### Real

Geometry ${(\sqrt{CD},{mm})} \downarrow$ Novel view synthesis (PSNR, dB) ↑ Blue tuna can Table 3: Real object recovery metrics for individual YCB prop objects.

We test the reconstruction of six YCB objects from real robot trajectory data (segmented with text prompts as described in the Appendix). We additionally estimate surface normals for each RGB camera frame independently using the pre-trained model .

The objective is a weighted sum of L1 RGB loss, L2 masks smoothed with 2d distance transforms, and L2 between the predicted and estimated surface normals, with mesh Laplacian regularization. We optimize the mesh vertices, Gaussian parameters, and camera extrinsic rotation parameters. We run the optimization for 40000 steps, and report in Table 3 the Chamfer Distance values for geometry reconstruction and PSNR for novel view synthesis on held-out views of the asset.

We compare with the *Proprio-only* ablation, the same model with the camera extrinsics frozen at the nominal values. The geometry fails to converge effectively, demonstrating that without further optimization this low-cost robot platform lacks the high precision required for the reconstruction task. We also compare shape reconstruction against output from TRELLIS,. This pre-trained 3D foundation model produces 3D appearance and geometry from one or few image views. We provide it with the best hand-chosen masked image from each dataset, and did not find that additional views improved performance. The model does not predict metric scales or object poses, so to enable comparison we optimize the SE3 pose and scale of the TRELLIS mesh using privileged information (Chamfer Distance to the ground truth asset mesh), shown as *Aligned TRELLIS* in the Tab. 3. We observe that while it can sometimes produce high quality shape predictions, on this real robot dataset it can sometimes introduce anisotropic scale distortions, add spurious geometry like additional ground planes, or fail to capture the 3D structure of simple shapes - see the Appendix.

### 3D asset generation

Figure 4: 3D asset generation with SplatMesh. Assets, which are generated from text or a single view image, can be imported in any simulator.

Our framework extends beyond calibration and object reconstruction to enable the generation of 3D objects from single images or text prompts. The incorporation of single-image or text-based object reconstruction provides a streamlined approach for the rapid creation of diverse object instances with varying geometries and appearances. This capability is particularly valuable for training robust robotic policies by augmenting datasets and enriching synthetic environments.

Given a text prompt or a single image, we leverage CAT3D to predict geometrically consistent multi-views from single-view input. Then, we follow the procedures outlined in Sec. 4.2.1 for novel-view synthesis and geometry reconstruction using SplatMesh. This approach yields accurate geometry as a mesh and visual appearance as a 3DGS representation. However, as traditional simulators and rendering engines cannot directly render a 3DGS representation, we further optimize a texture map using inverse rendering, supervised on the images produced by our 3DGS differentiable renderer. Fig. 4 presents a qualitative result of our generated assets within the MuJoCo simulation. Additional results are reported in the Appendix.

## Conclusion

In this paper we explored the the feasibility of tackling a broad range of model identification and scene estimation problems by directly applying end-to-end optimization, fitting standard MuJoCo models to noisy real-world robot data drawn from existing platforms. We developed a novel explicit 3D scene representation, SplatMesh, which enables gradient signals from RGB pixels to propagate through to arbitrary model parameters including geometry, appearance and camera pose. We used this framework to refine the calibration of noisy robot and camera poses, and to show the reconstruction of 3D objects from this real data.

This conceptually streamlined but powerful framework is able to leverage existing models to efficiently extract precise information about key simulation quantities from scarce and noisy real world robot data. It opens a broad spectrum of possibilities for future work enriching and refining physical models with real world data.

## Limitations

While our framework demonstrates promising results in reconstructing dynamic robot scenes and novel object geometries, we identify limitations of the present version that motivate future extensions.

Making use of gradient descent to fit parameters is a straightforward way to leverage the differentiability of the model, but is applicable only to smooth parameters and can only provide local information. In particular this limits meshes learned in this way to those homeomorphic to the topology fixed at initialization (e.g. if the initial geometry is topologically equivalent to a sphere, the refined mesh will also be topologically equivalent to a sphere). This limitation can be mitigated through the choice of initialization mesh structure, but future work will explore more robust and flexible solutions. More generally, gradient descent finds only local minima and so is sensitive to the choice of initialization for non-convex problems. We can consider several possible ways to handle this: In our real robot setting, with existing but noisy data, in practice it is often possible to constrain many parameters to a small region of interest for initialization.

Using more general uncertainty-aware inference methods rather than simply optimization is an interesting direction for future work Complementing gradient optimization, which excels at high precision and local refinement, with initialization proposed by data-driven learning based approaches Visually, the rendering model used in 3DGS does not enable relighting, so cannot represent effects like reflections and shadows if the dynamic scene elements are moved. This restriction has been overcome in some later works but the data gathering requirements may prove a challenge given the real robot constraints.

Finally, since we base our differentiable physics simulation on MuJoCo, we are limited to simulation features supported in its JAX based MJX implementation. For now this restricts us to rigid objects, although the framework is open source and still under development, so could in principle be extended to support deformable objects as is the case in the C++ Mujoco implementation.
