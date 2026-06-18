## Introduction

Metric-semantic understanding is the capability to simultaneously estimate the 3D geometry of a scene and attach a semantic label to objects and structures (*e.g., *tables, walls). Geometric information is critical for robots to navigate safely and to manipulate objects, while semantic information provides the ideal level of abstraction for a robot to understand and execute human instructions (*e.g., *"bring me a cup of coffee", "exit from the red door") and to provide humans with models of the environment that are easy to understand.

Despite the unprecedented progress in geometric reconstruction (*e.g., *SLAM, Structure from Motion, and Multi-View Stereo ) and deep-learning-based semantic segmentation (*e.g., *), research in these two fields has traditionally proceeded in isolation. However, recently there has been a growing interest towards research and applications at the intersection of these areas.

This growing interest motivated us to create and release *Kimera*, a library for metric-semantic localization and mapping that combines the state of the art in geometric and semantic understanding into a modern perception library. Contrary to related efforts targeting visual-inertial odometry (VIO) and SLAM, we combine visual-inertial SLAM, mesh reconstruction, and semantic understanding. Our effort also complements approaches at the boundary between metric and semantic understanding in several aspects. First, while existing efforts focus on RGB-D sensing, Kimera uses *visual* (RGB) and *inertial* sensing, which works well in a broader variety of (indoor and outdoor) environments. Second, while related works require a GPU for 3D mapping, we provide a *fast, lightweight, and scalable* CPU-based solution. Finally, we focus on *robustness*: we include state-of-the-art outlier rejection methods to ensure that Kimera executes robustly and with minimal parameter tuning across a variety of scenarios, from real benchmarking datasets to photo-realistic simulations.

mono/Stereo/IMU

mono/stereo/IMU

TABLE I: Related open-source libraries for visual and visual-inertial SLAM (top) and metric-semantic reconstruction (bottom).

Related Work. We refer the reader to Table I for a visual comparison against existing VIO and visual-SLAM systems, and to for a broader review on SLAM. While early work on metric-semantic understanding were designed for offline processing, recent years have seen a surge of interest towards *real-time* metric-semantic mapping, triggered by pioneering works such as SLAM++. Most of these works (i) rely on RGB-D cameras, (ii) use GPU processing, (iii) alternate tracking and mapping ("alternation" in Table I), and (iv) use voxel-based (*e.g., *Truncated Signed Distance Function, TSDF), surfel, or object representations. Examples include SemanticFusion, the approach of Zheng *et al.*, Tateno *et al.*, and Li *et al.*, Fusion++, Mask-fusion, Co-fusion, and MID-Fusion. Recent work investigates CPU-based approaches, *e.g., *Wald *et al.*, PanopticFusion, and Voxblox++; these also rely on RGB-D sensing. A sparser set of contributions address other sensing modalities, including monocular cameras (*e.g., *CNN-SLAM, VSO, VITAMIN-E, XIVO ) and lidar (*e.g., *SemanticKitti, SegMap ). XIVO and Voxblox++ are the closest to our proposal. XIVO is an EKF-based visual-inertial approach and produces an object-based map. Voxblox++ relies on RGB-D sensing, wheel odometry, and pre-built maps using maplab to obtain visual-inertial pose estimates. Contrary to these works, Kimera (i) provides a highly-accurate real-time optimization-based VIO, (ii) uses a robust and versatile pose graph optimizer, and (iii) provides a lightweight mesh reconstruction.

Contribution. We release *Kimera*, an open-source C++ library that uses visual-inertial sensing to estimate the state of the robot and build a lightweight metric-semantic mesh model of the environment. The name Kimera stems from the hybrid nature of our library, that unifies state-of-the-art efforts across research areas, including VIO, pose graph optimization (PGO), mesh reconstruction, and 3D semantic segmentation. Kimera includes four key modules:

Kimera-VIO: a VIO module for fast and accurate IMU-rate state estimation. At its core, Kimera-VIO features a GTSAM-based VIO approach, using IMU-preintegration and structureless vision factors, and achieves top performance on the EuRoC dataset;

Kimera-RPGO: a robust pose graph optimization (RPGO) method that capitalizes on modern techniques for outlier rejection. Kimera-RPGO adds a robustness layer that avoids SLAM failures due to perceptual aliasing, and relieves the user from time-consuming parameter tuning;

Kimera-Mesher: a module that computes a fast per-frame and multi-frame regularized 3D mesh to support obstacle avoidance. The mesher builds on previous algorithms by the authors and other groups;

Kimera-Semantics: a module that builds a slower-but-more-accurate global 3D mesh using a volumetric approach, and semantically annotates the 3D mesh using 2D pixel-wise semantic segmentation.

Kimera can work both with offline datasets or online using the Robot Operating System (ROS). It runs in real-time on a CPU and provides useful debugging and visualization tools. Moreover, it is modular and allows replacing each module or executing them in isolation. For instance, it can fall back to a VIO solution or can simply estimate a geometric mesh if the semantic labels are not available.

Figure 2: Kimera’s architecture. Kimera uses images and IMU data as input (shown on the left) and outputs (a) pose estimates and (b-e) multiple metric-semantic reconstructions. Kimera has 4 key modules: Kimera-VIO, Kimera-RPGO, Kimera-Mesher, Kimera-Semantics.

## Kimera

Fig. 2 shows Kimera's architecture. Kimera takes stereo frames and high-rate inertial measurements as input and returns (i) a highly accurate state estimate at IMU rate, (ii) a globally-consistent trajectory estimate, and (iii) multiple meshes of the environment, including a fast local mesh and a global semantically annotated mesh. Kimera is heavily parallelized and uses four threads to accommodate inputs and outputs at different rates (*e.g., *IMU, frames, keyframes). Here we describe the architecture *by threads*, while the description of each module is given in the following sections.

The first thread includes the Kimera-VIO front-end (Section II-A) that takes stereo images and IMU data and outputs feature tracks and preintegrated IMU measurements. The front-end also publishes IMU-rate state estimates. The second thread includes (i) the Kimera-VIO back-end, that outputs optimized state estimates, and (ii) Kimera-Mesher (Section II-C), that computes low-latency ($< {20\text{ms}}$) per-frame and multi-frame 3D meshes. These two threads allow creating the per-frame mesh in Fig. 2(b) (which can also come with semantic labels as in Fig. 2(c)), as well as the multi-frame mesh in Fig. 2(d). The last two threads operate at slower rate and are designed to support low-frequency functionalities, such as path planning. The third thread includes Kimera-RPGO (Section II-B), a robust PGO implementation that detects loop closures, rejects outliers, and estimates a globally consistent trajectory (Fig. 2(a)). The last thread includes Kimera-Semantics (Section II-D), that uses dense stereo and 2D semantic labels to obtain a refined metric-semantic mesh, using Kimera-VIO's pose estimates.

### II-A Kimera-VIO: Visual-Inertial Odometry Module

Kimera-VIO implements the keyframe-based maximum-a-posteriori visual-inertial estimator presented in. In our implementation, the estimator can perform both *full* smoothing or *fixed-lag* smoothing, depending on the specified time horizon; we typically use the latter to bound the estimation time. We also extend to work with both monocular and stereo frames. Kimera-VIO includes a (visual and inertial) front-end which is in charge of processing the raw sensor data, and a back-end, that fuses the processed measurements to obtain an estimate of the state of the sensors (*i.e., *pose, velocity, and sensor biases).

### II-A1 VIO Front-end

Our IMU front-end performs on-manifold preintegration to obtain compact preintegrated measurements of the relative state between two consecutive keyframes from raw IMU data. The vision front-end detects Shi-Tomasi corners, tracks them across frames using the Lukas-Kanade tracker, finds left-right stereo matches, and performs geometric verification. We perform both mono(cular) verification using 5-point RANSAC and stereo verification using 3-point RANSAC; the code also offers the option to use the IMU rotation and perform mono and stereo verification using 2-point and 1-point RANSAC, respectively. Feature detection, stereo matching, and geometric verification are executed at each *keyframe*, while we only track features at intermediate *frames*.

### II-A2 VIO Back-end

At each keyframe, preintegrated IMU and visual measurements are added to a fixed-lag smoother (a factor graph) which constitutes our VIO back-end. We use the preintegrated IMU model and the structureless vision model of. The factor graph is solved using iSAM2 in GTSAM. At each iSAM2 iteration, the structureless vision model estimates the 3D position of the observed features using DLT and analytically eliminates the corresponding 3D points from the VIO state. Before elimination, degenerate points (*i.e., *points behind the camera or without enough parallax for triangulation) and outliers (*i.e., *points with large reprojection error) are removed, providing an extra robustness layer. Finally, states that fall out of the smoothing horizon are marginalized out using GTSAM.

### II-B Kimera-RPGO: Robust Pose Graph Optimization Module

Kimera-RPGO is in charge of (i) detecting loop closures between the current and past keyframes, and (ii) computing globally consistent keyframe poses using robust PGO.

### II-B1 Loop Closure Detection

The loop closure detection relies on the DBoW2 library and uses a bag-of-word representation to quickly detect putative loop closures. For each putative loop closure, we reject outlier loop closures using mono and stereo geometric verification (as described in Section II-A), and pass the remaining loop closures to the robust PGO solver. Note that the resulting loop closures can still contain outliers due to perceptual aliasing (*e.g., *two identical rooms on different floors of a building).

### II-B2 Robust PGO

This module is implemented in GTSAM, and includes a modern outlier rejection method, *Incremental Consistent Measurement Set Maximization* (PCM), that we tailor to a single-robot and online setup. We store separately the odometry edges (produced by Kimera-VIO) and the loop closures (produced by the loop closure detection); each time the PGO is executed, we first select the largest set of consistent loop closures using a modified version of PCM, and then execute GTSAM on the pose graph including the odometry and the consistent loop closures.

PCM is designed for the multi-robot case and only checks that inter-robot loop closures are consistent. We developed a C++ implementation of PCM that (i) adds an *odometry consistency check* on the loop closures and (ii) *incrementally* updates the set of consistent measurements to enable online operation. The odometry check verifies that each loop closure (*e.g., *$l_{1}$ in Fig. 2(a)) is consistent with the odometry (in red in the figure): in the absence of noise, the poses along the cycle formed by the odometry and the loop $l_{1}$ must compose to the identity. As in PCM, we flag as outliers loops for which the error accumulated along the cycle is not consistent with the measurement noise using a Chi-squared test. If a loop detected at the current time $t$ passes the odometry check, we test if it is pairwise consistent with previous loop closures as in (*e.g., *check if loops $l_{1}$ and $l_{2}$ in Fig. 2(a) are consistent with each other). While PCM builds an adjacency matrix ${\mathbf{A}} \in {\mathbb{R}}^{L \times L}$ from scratch to keep track of pairwise-consistent loops (where $L$ is the number of detected loop closures), we enable online operation by building the matrix $\mathbf{A}$ incrementally. Each time a new loop is detected, we add a row and column to the matrix $\mathbf{A}$ and only test the new loop against the previous ones. Finally, we use the fast maximum clique implementation of to compute the largest set of consistent loop closures. The set of consistent measurements are added to the pose graph (together with the odometry) and optimized using Gauss-Newton.

### II-C Kimera-Mesher: 3D Mesh Reconstruction

Kimera-Mesher can quickly generate two types of 3D meshes: (i) a per-frame 3D mesh, and (ii) a multi-frame 3D mesh spanning the keyframes in the VIO fixed-lag smoother.

### II-C1 Per-frame mesh

As in, we first perform a 2D Delaunay triangulation over the successfully tracked 2D features (generated by the VIO front-end) in the current keyframe. Then, we back-project the 2D Delaunay triangulation to generate a 3D mesh (Fig. 2(b)), using the 3D point estimates from the VIO back-end. While the per-frame mesh is designed to provide low-latency obstacle detection, we also provide the option to semantically label the resulting mesh, by texturing the mesh with 2D labels (Fig. 2(c)).

### II-C2 Multi-frame mesh

The multi-frame mesh fuses the per-frame meshes collected over the VIO receding horizon into a single mesh (Fig. 2(d)). Both per-frame and multi-frame 3D meshes are encoded as a list of vertex positions, together with a list of triplets of vertex IDs to describe the triangular faces. Assuming we already have a multi-frame mesh at time $t - 1$, for each new per-frame 3D mesh that we generate (at time $t$), we loop over its vertices and triplets and add vertices and triplets that are in the per-frame mesh but are missing in the multi-frame one. Then we loop over the multi-frame mesh vertices and update their 3D position according to the latest VIO back-end estimates. Finally, we remove vertices and triplets corresponding to old features observed outside the VIO time horizon. The result is an up-to-date 3D mesh spanning the keyframes in the current VIO time horizon. If planar surfaces are detected in the mesh, *regularity factors* are added to the VIO back-end, which results in a tight coupling between VIO and mesh regularization, see for further details.

### II-D Kimera-Semantics: Metric-Semantic Segmentation

We adapt the bundled raycasting technique introduced in to (i) build an accurate global 3D mesh (covering the entire trajectory), and (ii) semantically annotate the mesh.

### II-D1 Global mesh

Our implementation builds on Voxblox and uses a voxel-based (TSDF) model to filter out noise and extract the global mesh. At each keyframe, we use dense stereo (semi-global matching ) to obtain a 3D point cloud from the current stereo pair. Then we apply bundled raycasting using Voxblox, using the "fast" option discussed in. This process is repeated at each keyframe and produces a TSFD, from which a mesh is extracted using marching cubes.

### II-D2 Semantic annotation

Kimera-Semantics uses 2D semantically labeled images (produced at each keyframe) to semantically annotate the global mesh; the 2D semantic labels can be obtained using off-the-shelf tools for pixel-level 2D semantic segmentation, *e.g., *deep neural networks or classical MRF-based approaches. To this end, during the bundled raycasting, we also propagate the semantic labels. Using the 2D semantic segmentation, we attach a label to each 3D point produced by the dense stereo. Then, for each bundle of rays in the bundled raycasting, we build a vector of label probabilities from the frequency of the observed labels in the bundle. We then propagate this information along the ray only within the TSDF truncation distance (*i.e., *near the surface) to spare computation. In other words, we spare the computational effort of updating probabilities for the "empty" label. While traversing the voxels along the ray, we use a Bayesian update to update the label probabilities at each voxel, similar to. After bundled semantic raycasting, each voxel has a vector of label probabilities, from which we extract the most likely label. The metric-semantic mesh is finally extracted using marching cubes. The resulting mesh is significantly more accurate than the multi-frame mesh of Section II-C, but it is slower to compute ($\approx {0.1\text{s}}$, see Section III-D).

### II-E Debugging Tools

While we limit the discussion for space reasons, it is worth mentioning that Kimera also provides an open-source suite of evaluation tools for debugging, visualization, and benchmarking of VIO, SLAM, and metric-semantic reconstruction. Kimera includes a Continuous Integration server (Jenkins) that asserts the quality of the code (compilation, unit tests), but also automatically evaluates Kimera-VIO and Kimera-RPGO on the EuRoC's datasets using *evo*. Moreover, we provide Jupyter Notebooks to visualize intermediate VIO statistics (*e.g., *quality of the feature tracks, IMU preintegration errors), as well as to automatically assess the quality of the 3D reconstruction using Open3D.

## Experimental Evaluation

Section III-A shows that (i) Kimera attains state-of-the-art state estimation performance and (ii) our robust PGO relieves the user from time-consuming parameter tuning. Section III-B demonstrates Kimera's 3D mesh reconstruction on EuRoC, using the subset of scenes providing a ground-truth point cloud. Section III-C inspects Kimera's 3D metric-semantic reconstruction using a photo-realistic simulator (see video attachment), which provides ground-truth 3D semantics. Finally, Section III-D highlights Kimera's real-time performance and analyzes the runtime of each module.

### III-A Pose Estimation Performance

Table II compares the Root Mean Squared Error (RMSE) of the Absolute Translation Error (ATE) of Kimera-VIO against state-of-the-art open-source VIO pipelines: OKVIS, MSCKF, ROVIO, VINS-Mono, and SVO-GTSAM using the independently reported values in and the self-reported values in. Note that these algorithms use a monocular camera, while we use a stereo camera. We align the estimated and ground-truth trajectories using an ${SE}{}$ transformation before evaluating the errors. Using a ${Sim}{}$ alignment, as in, would result in an even smaller error for Kimera: we preferred the ${SE}{}$ alignment, since it is more appropriate for VIO, where the scale is observable thanks to the IMU. We group the techniques depending on whether they use fixed-lag smoothing, full smoothing, and loop closures. Kimera-VIO and Kimera-RPGO achieve top performance across the spectrum.

Furthermore, Kimera-RPGO ensures robust performance, and is less sensitive to loop closure parameter tuning. Table III shows the PGO accuracy with and without outlier rejection (PCM) for different values of the loop closure threshold $\alpha$ used in DBoW2. Small values of $\alpha$ lead to more loop closure detections, but these are less conservative (more outliers). Table III shows that, by using PCM, Kimera-RPGO is fairly insensitive to the choice of $\alpha$. The results in Table II use $\alpha = 0.001$.

TABLE II: RMSE of state-of-the-art VIO pipelines (reported from and ) compared to Kimera, on the EuRoC dataset. In bold the best result for each category: fixed-lag smoothing, full smoothing, and PGO with loop closure. × indicates failure.

TABLE III: RMSE ATE [m] vs. loop closure threshold α (V1_01).

### III-B Geometric Reconstruction

We use the ground truth point cloud available in the EuRoC V1 and V2 datasets to assess the quality of the 3D meshes produced by Kimera. We evaluate each mesh against the ground truth using the accuracy and completeness metrics as in \[78, Sec. 4.3\]: (i) we compute a point cloud by sampling our mesh with a uniform density of ${10^{3}\text{points}}/\text{m}^{2}$, (ii) we register the estimated and the ground truth clouds with ICP using *CloudCompare*, and (iii) we evaluate the average distance from ground truth point cloud to its nearest neighbor in the estimated point cloud (accuracy), and vice-versa (completeness). Fig. 3(a) shows the estimated cloud (corresponding to the global mesh of Kimera-Semantics on V1_01) color-coded by the distance to the closest point in the ground-truth cloud (accuracy); Fig. 3(b) shows the ground-truth cloud, color-coded with the distance to the closest-point in the estimated cloud (completeness).

Figure 3: (a) Kimera’s 3D mesh color-coded by the distance to the ground-truth point cloud. (b) Ground-truth point cloud color-coded by the distance to the estimated cloud. EuRoC V1_01 dataset.

Table IV provides a quantitative comparison between the fast multi-frame mesh produced by Kimera-Mesher and the slow mesh produced via TSDF by Kimera-Semantics. To obtain a complete mesh from Kimera-Mesher we set a large VIO horizon (*i.e., *we perform full smoothing). As expected from Fig. 3(a), the global mesh from Kimera-Semantics is very accurate, with an average error of $0.35 - 0.48$m across datasets. Kimera-Mesher produces a more noisy mesh (up to $24\%$ error increase), but requires two orders of magnitude less time to compute (see Section III-D).

TABLE IV: Evaluation of Kimera multi-frame and global meshes’ completeness [78, Sec. 4.3.3] with an ICP threshold of 1.0m.

### III-C Semantic Reconstruction

To evaluate the accuracy of the metric-semantic reconstruction from Kimera-Semantics, we use a photo-realistic Unity-based simulator provided by MIT Lincoln Lab, that provides sensor streams (in ROS) and ground truth for both the geometry and the semantics of the scene, and has an interface similar to. To avoid biasing the results towards a particular 2D semantic segmentation method, we use ground truth 2D semantic segmentations and we refer the reader to for potential alternatives.

Kimera-Semantics builds a 3D mesh from the VIO pose estimates, and uses a combination of dense stereo and bundled raycasting. We evaluate the impact of each of these components by running three different experiments. First, we use Kimera-Semantics with ground-truth (GT) poses and ground-truth depth maps (available in simulation) to assess the initial loss of performance due to bundled raycasting. Second, we use Kimera-VIO's pose estimates. Finally, we use the full Kimera-Semantics pipeline including dense stereo. To analyze the semantic performance, we calculate the mean Intersection over Union (mIoU), and the overall portion of correctly labeled points (Acc). We also report the ATE to correlate the results with the drift incurred by Kimera-VIO. Finally, we evaluate the metric reconstruction registering the estimated mesh with the ground truth and computing the RMSE for the points as in Section III-B.

Table V summarizes our findings and shows that bundled raycasting results in a small drop in performance both geometrically ($< 8$cm error on the 3D mesh) as well as semantically (accuracy $> {94\%}$). Using Kimera-VIO also results in negligible loss in performance since our VIO has a small drift ($< {0.2\%}$, $4$cm for a $32$m long trajectory). Certainly, the biggest drop in performance is due to the use of dense stereo. Dense stereo has difficulties resolving the depth of texture-less regions such as walls, which are frequent in simulated scenes. Fig. 4 shows the confusion matrix when running Kimera-Semantics with Kimera-VIO and ground-truth depth (Fig. 4(a)), compared with using dense stereo (Fig. 4(b)). Large values in the confusion matrix appear between Wall/Shelf and Floor/Wall. This is exactly where dense stereo suffers the most; texture-less walls are difficult to reconstruct and are close to shelves and floor, resulting in increased geometric and semantic errors.

Figure 4: Confusion matrices for Kimera-Semantics using bundled raycasting and (a) ground truth stereo depth or (b) dense stereo. Both experiments use ground-truth 2D semantics. Values are saturated to 104 for visualization purposes.

TABLE V: Evaluation of Kimera-Semantics.

### III-D Timing

Fig. 5 reports the timing performance of Kimera's modules. The IMU front-end requires around $40\mu$s for preintegration, hence can generate state estimates at IMU rate ($> 200$Hz ). The vision front-end module shows a bi-modal distribution since, for every frame, we just perform feature tracking (which takes an average of $4.5$ms), while, at keyframe rate, we perform feature detection, stereo matching, and geometric verification, which, combined, take an average of $45$ms. Kimera-Mesher is capable of generating per-frame 3D meshes in less than $5$ms, while building the multi-frame mesh takes $15$ms on average. The back-end solves the factor-graph optimization in less than $40$ms. Kimera-RPGO and Kimera-Semantics run on slower threads since their outputs are not required for time-critical actions (*e.g., *control, obstacle avoidance). Kimera-RPGO took an average of $55$ms in our experiments on EuRoC, but in general its runtime depends on the size of the pose graph. Finally, Kimera-Semantics (not reported in figure for clarity) takes an average of $0.1\text{s}$ to update the global metric-semantic mesh at each keyframe, fusing a $720 \times 480$ dense depth image, as the one produced by our simulator.

Figure 5: Runtime breakdown for Kimera-VIO, RPGO, and Mesher.

## Conclusion

Kimera is an open-source C++ library for metric-semantic SLAM. It includes state-of-the-art implementations of visual-inertial odometry, robust pose graph optimization, mesh reconstruction, and 3D semantic labeling. It runs in real-time on a CPU and provides a suite of continuous integration and benchmarking tools. We hope Kimera can provide a solid basis for future research on robot perception, and an easy-to-use infrastructure for researchers across communities.
