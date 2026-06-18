Splatting Physical Scenes: End-to-End Real-to-Sim from Imperfect Robot Data

Creating accurate, physical simulations directly from real-world robot motion holds great value for safe, scalable, and affordable robot learning, yet remains exceptionally challenging. Real robot data suffers from occlusions, noisy camera poses, dynamic scene elements, which hinder the creation of geometrically accurate and photorealistic digital twins of unseen objects. We introduce a novel real-to-sim framework tackling all these challenges at once. Our key insight is a hybrid scene representation merging the photorealistic rendering of 3D Gaussian Splatting with explicit object meshes suitable for physics simulation within a single representation. We propose an end-to-end optimization pipeline that leverages differentiable rendering and differentiable physics within MuJoCo to jointly refine all scene components - from object geometry and appearance to robot poses and physical parameters - directly from raw and imprecise robot trajectories. This unified optimization allows us to simultaneously achieve high-fidelity object mesh reconstruction, generate photorealistic novel views, and perform annotation-free robot pose calibration.

## Introduction

Creating physically accurate and visually realistic simulations directly from real-world robot interactions is crucial for scalable robotics, yet bridging the visual and physical sim-to-real gap remains a major hurdle, especially with imperfect data. While recent advances like Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) generate high-quality photorealistic novel views, they face significant challenges in dynamic robotic settings: they are sensitive to noisy camera poses common in real trajectories, and produce representations ill-suited for direct use in physics simulators like MuJoCo.

We argue that overcoming this requires tackling scene appearance reconstruction, object geometry extraction, and robot/camera calibration jointly within a single, end-to-end differentiable framework. This paper introduces such a framework, enabling the learning of explicit simulation scenes directly from imperfect, dynamic robot trajectory data. Our key innovation is the development of a single representation that combines SplatMesh, a hybrid scene representation that tightly couples 3DGS for appearance with explicit mesh geometry, with differentiable physics states.

## Conclusion

In this paper we explored the the feasibility of tackling a broad range of model identification and scene estimation problems by directly applying end-to-end optimization, fitting standard MuJoCo models to noisy real-world robot data drawn from existing platforms. We developed a novel explicit 3D scene representation, SplatMesh, which enables gradient signals from RGB pixels to propagate through to arbitrary model parameters including geometry, appearance and camera pose. We used this framework to refine the calibration of noisy robot and camera poses, and to show the reconstruction of 3D objects from this real data.

This conceptually streamlined but powerful framework is able to leverage existing models to efficiently extract precise information about key simulation quantities from scarce and noisy real world robot data. It opens a broad spectrum of possibilities for future work enriching and refining physical models with real world data.

## Limitations

While our framework demonstrates promising results in reconstructing dynamic robot scenes and novel object geometries, we identify limitations of the present version that motivate future extensions.
