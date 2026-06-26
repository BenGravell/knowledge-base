## Introduction

Visual navigation is an important area of research in robotics. Visual odometry (VO) estimates the motion of a camera (i.e., its egomotion) relative to observed static objects within a scene. These static objects must be accurately segmented from any dynamic noise, and this segmentation itself is an area of research focus. Less research in visual navigation has focused on also analyzing the dynamic regions of the scene that these approaches reject.

This motion estimation problem requires both *estimation*, i.e., calculating the motion of a set of points, and *segmentation*, i.e., clustering points according to their movement between observations. The interdependence of these tasks creates a *chicken-and-egg* problem that is addressed in VO systems by using heuristics (e.g., number of features) to select the egomotion and ignore the other motions in the scene. These heuristics are not readily extensible to *multimotion* estimation problems and analyzing multiple independently moving bodies remains a challenging problem for state-of-the-art vision systems. This paper extends traditional VO to multimotion visual odometry (MVO) and applies state-of-the-art techniques to estimate trajectories for *every* motion in a scene.

Figure 1: Motion segmentation produced by our multimotion visual odometry (MVO) system. The egomotion of the camera is estimated from the static points in the scene shown in black. The other colors represent the segmentation of the other motions in the scene.

Figure 2: Illustrations of the multimotion estimation problem showing the motion of frames through time, (a), and the relative point observations, (b). A series of two independent third-party motions, ${\underset{\rightarrow}{\mathcal{F}}}_{A}$ and ${\underset{\rightarrow}{\mathcal{F}}}_{B}$, are observed by a moving camera, ${\underset{\rightarrow}{\mathcal{F}}}_{C}$, through feature measurements on the objects, pCkak Ck and pCkbk Ck. Solving the problem requires simultaneously segmenting and estimating the set of measurements.

MVO applies multimodel fitting techniques (e.g., CORAL ) to the traditional VO pipeline to simultaneously estimate the trajectories of all motions within a scene. Sparse, 3D visual features are decomposed into independent rigid motions and the trajectories of all of these motions, including the egomotion of the camera, are estimated simultaneously (Fig. 1: Simultaneous Estimation of Camera and Third-Party Motions")). This paper demonstrates MVO on a stereo camera, but the technique is applicable to a variety of other 3D sensors, including RGB-D cameras and lidar. To the best of our knowledge, this is the first approach capable of estimating the full $SE$ trajectory of every rigid motion in a complex, dynamic scene from a stereo/RGB-D camera without relying on simplifying constraints or fragile initialization.

## Background

The constituent aspects of the multimotion estimation problem are often referred to as multiple object tracking (MOT) and multibody structure from motion (MBSfM). As such, the majority of approaches focus primarily on one part of the problem and either do not fully estimate $SE$ motions (Sections II-B: Simultaneous Estimation of Camera and Third-Party Motions") and II-C: Simultaneous Estimation of Camera and Third-Party Motions")), depend on simplifying constraints and assumptions (Sections II-D: Simultaneous Estimation of Camera and Third-Party Motions") and II-E: Simultaneous Estimation of Camera and Third-Party Motions")), or require fragile initialization steps (Section II-F: Simultaneous Estimation of Camera and Third-Party Motions")).

### II-A Problem Definition

Discrete multimotion estimation is the problem of estimating all the motions, including the camera, in a scene from a set of point observations at each time step. It both estimates the motions as a series of discrete $SE$ transforms and associates the observed tracklets with the estimated motions.

Dynamic environments consist of the static background, a moving observer, i.e., the camera, and one or more independent, third-party motions. The pose of a motion, $\ell$, at each discrete time, $k$, is represented as a coordinate frame, ${\underset{\rightarrow}{\mathcal{F}}}_{\ell_{k}}$, and related to a privileged initial pose through an $SE$ transform, $\mathbf{T}_{\ell{{}_{k}^{}\ell}_{1}}$ (Fig. 2a: Simultaneous Estimation of Camera and Third-Party Motions")). A sequence of these transforms over a set of $K$ frames constitutes the trajectory of the motion, $T_{\ell} ≔ \left( \mathbf{T}_{\ell{{}_{k}^{},}\ell_{1}} \right)_{k = {1\ldotsK}}$. Likewise, a sequence of observations of a point, $j$, by a moving camera, $C$, over multiple frames forms a tracklet, $p^{j} ≔ \left( \mathbf{p}_{C_{k}}^{j_{k}C_{k}} \right)_{k = {1\ldotsK}}$, where $C_{k}$ refers to the observing camera frame at time $k$ (Fig. 2b: Simultaneous Estimation of Camera and Third-Party Motions")). Tracklets moving with a common trajectory can be grouped into bulk motions as $\mathcal{P}_{\ell} ≔ \left\{ p^{j} \right\}_{1\ldotsN}$.

Motions estimated from these measurements are *egocentric*. They can be represented as *geocentric* motions after identifying one motion as the camera, $T_{C}$.

### II-B Flow Techniques

Optical flow, scene flow, and sparse scene flow are approaches for finding the 2D or 3D velocity vector of pixels or feature points in a scene. These individual velocities are inherently translational and motions involving rotations (i.e., $SE$ transforms) can only be estimated from segmentations of three or more velocities. In the presence of small rotations, these segmentations can be achieved using flow discontinuities or the vector distance between velocities.

Larger rotations result in smoothly varying tangential velocities that provide no clear segmentations (Fig. 3: Simultaneous Estimation of Camera and Third-Party Motions")a). To correctly estimate these motions, flow techniques must solve an equivalent segmentation and estimation problem posed in the space of velocities. In contrast to these flow techniques, MVO simultaneously segments and estimates full $SE$ transforms of motions in the scene (Fig. 3: Simultaneous Estimation of Camera and Third-Party Motions")b).

Figure 3: Scene flow, (a), and MVO, (b), on a checkerboard rotating about the optical axis. Flow techniques inherently calculate individual translational velocities. Since each point on a rotating body has a different tangential velocity, flow techniques fail to segment the velocities into bulk motions. MVO estimates motions as SE transforms even in the presence of rotation. To estimate these motions, flow techniques must solve an equivalent segmentation and estimation problem in the space of velocities.

### II-C Tracking-by-Detection Methods

Appearance-based tracking techniques detect objects in images and then solve the association and motion estimation problems. Kalman or particle filters are widely used to estimate the motion of the detected objects given a motion model but struggle to handle detection errors or occlusions.

Byeon et al. propose an optimization framework for tracking multiple objects and estimating their trajectories from multiple static cameras by incorporating reconstruction and motion dynamics in their cost function. Zhang et al. model tracking as a mininimum-flow problem on a graph where nodes represent detections and edges represent transitions between frames.

Object detectors are designed either for some specified class of objects or dynamically for some object of interest. These detectors are therefore specialized for a specific set of applications or are fragile to appearance changes and need to be refined over time.

Many of these approaches require either static or known camera motion and therefore need to incorporate separate egomotion estimators. The object positions only exist in ${\mathbb{R}}^{3}$ and do not fully encapsulate the $SE$ motions of the objects. Kundu et al. extend egomotion estimation with MBSfM techniques similar to to estimate the $SE$ trajectories of the third-party motions in a scene, but they constrain all the motions to the horizontal plane.

Unlike these appearance-based techniques, MVO relies on low-level feature tracking. This means it can handle large changes in object appearance over time so long as a suitable number of features remain stable between each pair of frames. MVO also estimates the full, unconstrained $SE$ motion within a scene, including the egomotion of the camera.

### II-D Subspace Methods

Subspace techniques cluster sparse feature points and their $SE$ motions into lower-dimensional subspaces using the affine camera model. The affine model approximates the nonlinear perspective projection with a linear parallel projection. This simplifies the camera model but introduces severe projection errors in scenes with a wide field of view or a large depth of field.

Tomasi and Kanade use the affine model and matrix factorization to decompose tracked image points into a motion and a shape matrix. Costeira and Kanade extend this technique to mutiple bodies where points may belong to different objects. This approach is inherently fragile as noise propagates through the factorization in complex ways. It also requires points to be tracked for the entirety of the estimation window, which is difficult in complex scenes.

This formulation was extended by using an optimization framework to allow feature point dropouts and by merging motions to mitigate the effect of noise. While these techniques are able to estimate full $SE$ motions, they still depend upon an affine camera model, meaning they fail under any significant perspective effects.

These factorization techniques have also been extended to the perspective camera model by estimating depth in a preprocessing stage or by applying geometric constraints but still remain very sensitive to noise. In comparison, MVO can robustly estimate full $SE$ trajectories using a perspective model while also handling the significant feature tracking failures characteristic of dynamic scenes.

### II-E Sampling Methods

Sampling methods estimate and fit models (e.g., motion trajectories) to a subset of the data before evaluating them across its entirety. RANSAC is a popular framework to fit a model to data in the presence of noise. Points are sampled from the data to estimate a hypothesis model, which is then used to segment the data into inliers and outliers according to their fit. Hypotheses are repeatedly generated for some number of iterations and the model with the most inliers is selected as the segmentation and estimation.

Figure 4: A comparison of the number of models found by a sequential RANSAC (red) and MVO (blue) over 500 frames of a five-motion experiment (Section IV). The first 100-frame section of the sequence is shown in (a) with the cumulative totals for the full sequence in (b). Without prior knowledge of the number of motions, sequential RANSAC greedily overfits to noise and finds an inconsistent number of models. MVO consistently segments the correct number of motions, except for frames 68–87 when some of the motions partially move outside the camera frustum. While RANSAC only found the correct number of models 31.2% of the time, MVO found the correct number 96.8% of the time.

Torr extends the RANSAC framework to multiple models by finding the dominant model, removing those points that fit the model, and then recursively applying RANSAC to the remaining points. This recursive, sequential RANSAC framework is efficient at finding the dominant models in a scene, but the ability to sample consistent models decreases as models are removed and the signal-to-noise ratio of the remaining points decreases. Sabzevari and Scaramuzza apply geometric and kinematic constraints to reduce the required number of points to estimate a motion model and then realign point assignments to the best set of motion hypotheses in a separate step. They use the same matrix formulation as, meaning points must be successfully tracked through the entirety of the window, and their applications are limited by the constraints.

Other techniques use sampling methods to generate a large number of initial model hypotheses, realizing many of them would be redundant or poorly fit the data. Models are merged if their inlier sets are largely overlapping, and the models with the largest nonoverlapping inlier sets after merging are taken as the constituent scene motions.

These sampling methods are efficient but the probability of sampling inliers all from a single model decreases rapidly with the signal-to-noise ratio. Finding a motion in complex dynamic scenes is challenging because all other motions are outliers that decrease the signal-to-noise ratio and make it harder to find correct models. As a result, many of these sampling-based initializations struggle to find correct models.

Without prior knowledge of the number of models in the data, RANSAC tends to greedily overfit to noise and finds erroneous or incomplete models (Fig. 4: Simultaneous Estimation of Camera and Third-Party Motions")). In contrast, MVO estimates all models simultaneously and requires no *a priori* knowledge of the number of models.

Figure 5: An illustration of the stereo multimotion visual odometry (MVO) pipeline, (a), including details of the multimotion fitting component, (b). The pipeline operates on RGB stereo image pairs and estimates the segmentation and trajectories of all motions in the scene. It extends the standard stereo visual odometry pipeline by replacing the egomotion estimator with a multimotion estimator that operates on the tracklets produced by the previous stages. The multimotion-fitting pipeline builds a neighborhood graph based on the distances between pairs of points throughout the estimation batch. The pipeline iteratively splits and estimates new labels using the neighborhood graph, performs label-assignment using CORAL, and merges labels that can be considered redundant until convergence. Finally, the label set is sanitized and a full-batch estimation step produces the final segmentation and trajectories.

### II-F Energy Minimization Methods

Energy minimization approaches segment data into multiple labels simultaneously by reducing a cost function. In multimotion estimation, this cost is designed to encompass how well the estimated trajectories describe the data, e.g., reprojection or photoconsistency error, as well as encourage piecewise smoothness throughout the scene. Smoothness is enforced over a graph structure, usually either a dense Markov random field or a sparse, feature-based graph.

Rother et al. use a minimization framework to find a binary segmentation of the static background from a manually selected dynamic foreground object, but the approach can only segment a single object within a bounding box. PEARL uses $\alpha$-expansion and model refitting to iteratively estimate both models and point assignments in an expectation-maximization framework. The framework can be applied to motion segmentation by first sampling the data to estimate a large number of motion models (similarly to ) and then refining the models and segmentation with PEARL. Roussos et al. use PEARL as part of a dense expectation-maximization pipeline that estimates depth, motion, and segmentation from monocular images in an offline manner. Optical flow is used to initialize the depth maps and the approach is crucially dependent on this initialization.

Rünz and Agapito use a similar optimization framework to segment dense RGB-D camera observations. Using this segmentation they create multiple 3D object models whose $SE$ motions are then tracked, establishing new motions online. This approach requires an initialization phase that seeds the structure and segmentation of the background of the scene.

These approaches are capable of estimating full $SE$ motions but are dependent upon comprehensive initialization, often using RANSAC, as they are designed around refining existing labels. In comparison, MVO iteratively proposes and refines labels, allowing it to find motions that may be difficult to initially segment with sampling methods alone.

### II-G Multimotion Visual Odometry (MVO)

To the best of our knowledge, this paper introduces the first online approach capable of directly estimating full $SE$ trajectories for every motion in a complex, dynamic scene from a stereo/RGB-D camera using only a rigid-body assumption. The approach uses multilabeling and estimation techniques to model the motions of tracklet features over multiple frames. The hypothesis trajectories are then applied to individual tracklets by CORAL, a convex optimization approach to the multilabeling problem. These hypotheses are iteratively improved through splitting and merging of the models, unlike other labeling approaches that initially sample them from the scene. The full $SE$ trajectory of *each* motion is finally estimated using traditional VO batch estimation techniques. This approach is evaluated on a dataset containing ground-truth trajectories for all motions in the scene.

## Methodology

The stereo MVO pipeline (Fig. 5: Simultaneous Estimation of Camera and Third-Party Motions")a) extends the traditional stereo VO pipeline to *multimodel* segmentation and estimation. The incoming RGB stereo images are first rectified and undistorted according to known camera extrinsics and intrinsics. Salient image points are detected and matched across left and right images in each stereo pair and across temporally consecutive pairs of stereo frames. These stereo- and temporally-matched feature points are back-projected into the 3D space using the camera intrinsics, forming world- and image-space tracklet histories for each feature point. This set of tracklets, $\mathcal{P} ≔ \left\{ p \right\}$, becomes the input to the multimotion segmentation and estimation engine (Fig. 5: Simultaneous Estimation of Camera and Third-Party Motions")b). These tracklets could alternatively be found by associating observations from other 3D sensors (e.g., RGB-D cameras) over time.

The multimotion engine segments tracklets by their observed motion, which is a combination of camera and object motions. In the absence of *a priori* information about the scene, each group of tracklets is used to estimate a camera egomotion by assuming those tracklets belong to a static object. These camera egomotion *hypotheses* can later be converted into estimates of the camera and object motions by identifying the static part of the scene (e.g., as in VO).

The segmentation and estimation are posed as a multilabeling problem where a a label, $\ell$, represents the egomotion hypothesis, ${}_{}^{\ell}T_{C}^{}$, calculated from a group of tracklets, $\mathcal{P}_{\ell} \subseteq \mathcal{P}$. These labels are assigned by minimizing a cost function over a graph of all observed tracklets (Section III-A: Simultaneous Estimation of Camera and Third-Party Motions")). New labels are proposed for each disconnected component of a label's subgraph through a multiframe RANSAC procedure (Section III-B: Simultaneous Estimation of Camera and Third-Party Motions")). Motion labels are assigned to minimize the reprojection residual of the associated trajectory and maximize the label smoothness in the graph (Section III-C: Simultaneous Estimation of Camera and Third-Party Motions")). An outlier label, $\mathcal{O}$, is assigned to points whose motions are not well explained by any other label. Redundant and oversegmented labels are then merged (Section III-D: Simultaneous Estimation of Camera and Third-Party Motions")).

The algorithm iterates this process until label convergence. The final labels are then sanitized and any remaining outliers are rejected (Section III-E: Simultaneous Estimation of Camera and Third-Party Motions")) before a final, full-batch estimation of each label (Section III-F: Simultaneous Estimation of Camera and Third-Party Motions")). Egocentric or geocentric trajectories are found by selecting a label to represent the motion of the camera (Section III-G: Simultaneous Estimation of Camera and Third-Party Motions")).

### III-A Graph Construction

The rigid-body assumption is approximated through a geometric neighborhood graph, $\mathcal{N}$. Each vertex of the graph represents an observed tracklet and is connected to its $k$-nearest-neighbors. The distance between two vertices is defined as the maximum distance in image space between those image tracklets over the entire batch, where $\mathbf{s}(\cdot)$ applies the nonlinear perspective camera projection. This allows for edges between features that are consistently close while not connecting features that are ever far apart or that never coexist in a frame. This connectivity forms the basis for label generation and assignment.

### III-B Label Proposal

The label set, $\mathcal{L}$, must dynamically grow and adapt to correctly converge in a given scene. To accomplish this, new labels are generated by splitting label support groups whenever their tracklets' motions could more accurately be explained by multiple trajectories. A potential new label, $\ell'$, is generated for each fully-disjoint component of the subgraph defined by the label's support, $\mathcal{N}_{\ell'} \subseteq \mathcal{N}_{\ell} \subseteq \mathcal{N}$. This ensures a level of spatial smoothness while allowing new labels to be proposed from large label supports comprised of tracklets from spatially or temporally distinct motions in the scene.

The new label proposals are generated by computing both the dominant motion of the given points and the segmentation between inliers and outliers of that motion. This single-motion segmentation and estimation problem is solved by applying RANSAC in a frame-to-frame fashion, similar to standard VO systems.

Three tracklets are sampled from those visible in the current, $k$, and previous, $k - 1$, frames to estimate the $SE{}$ transform between the two frames ${}_{}^{\ell'}\mathbf{T}_{C_{k},C_{k - 1}}^{}$. The proposed transform is evaluated according to how many tracklet reprojection residuals, are within a given threshold error, $e_{th}$. This process is repeated many times and the transform with the largest inlier set is appended to the proposed trajectory hypothesis, ${}_{}^{\ell'}T_{C}^{}$.

Any tracklets found to be outliers of the newly estimated models are appended to the outlier label, $\mathcal{O}$. New labels are generated from the outlier label last.

### III-C Label Assignment

Each tracklet, $p \in \mathcal{P}$, is assigned a label, $\ell \in \mathcal{L}$, to minimize the energy functional, where $\ell(p)$ gives the label currently assigned to $p$. The energy functional combines the residual error, the label smoothness, and the label complexity term, using a user-selected proportionality parameter, $\lambda$.

### Residual

The residual term penalizes labels that poorly describe the observed data. It is defined as the sum of the residual errors of applying the label trajectories to tracklets. The residual for each point-label pair is defined as where $e_{k}$ as defined in Eq. 1: Simultaneous Estimation of Camera and Third-Party Motions").

### Smoothness

The smoothness term penalizes neighboring tracklets that do not share the same label by an edge cost, $\omega_{pq}$. This encourages a piecewise-smooth solution. It is a weighted sum of all edges penalized according to

### Complexity

The complexity term encourages a compact solution by penalizing the use of many labels. It is the sum of the per-label cost, $\gamma_{\ell}$, of each label with non-empty support set according to the function,

### Outliers

The outlier label, $\mathcal{O}$, is designed to be attractive to all points whose motions are not well explained by existing labels. The residual energy of the outlier label decays exponentially with that of the best-fitting label, where $\alpha$ and $\beta$ are tuning parameters. Points that are well-explained by an extant label will have high outlier data cost. The label cost, $\gamma_{\mathcal{O}}$, for the outlier label is zero as outliers are assumed to always exist.

Given the current label set, $\alpha$-expansion (e.g., PEARL ) or convex optimization (e.g., CORAL ) assigns a label to each tracklet to minimize the residual and smoothness energies of Eq. 2: Simultaneous Estimation of Camera and Third-Party Motions"). The minimization can result in an oversegmentation due to outliers and poorly estimated intermediate trajectories. Model merging is therefore used to improve the motion estimation.

### III-D Label Merging

Two labels, $\ell$ and $\ell'$, may be merged if relabeling all $\mathcal{P}_{\ell'}$ as $\ell$ would decrease the total energy of Eq. 2: Simultaneous Estimation of Camera and Third-Party Motions"). This occurs when the increase in residual error due to reduced overfitting is less than the cost of using the label, $\gamma_{\ell'}$, and any change in smoothness.

Only the periods during which the two labels' supports overlap are considered because there is no cost for applying a new label to portions of the batch in which the tracklets do not exist. When more than one merge would reduce the total energy, the one that results in the greatest decrease in cost is chosen. Merging continues until no more merges would reduce (2: Simultaneous Estimation of Camera and Third-Party Motions")). The outlier label, $\mathcal{O}$, is excluded from merging.

The merging stage only considers label pairs with tracklets adjacent in $\mathcal{N}$, i.e., those where $\mathcal{N}_{\ell}$ is connected to $\mathcal{N}_{\ell'}$. If they are disconnected, merging the two supports would be undone by the splitting routine (Section III-B: Simultaneous Estimation of Camera and Third-Party Motions")). If the two support sets are connected then the new label will persist until the next labeling stage.

The algorithm iterates the label splitting, assignment, and merging (Sections III-B: Simultaneous Estimation of Camera and Third-Party Motions") to III-D: Simultaneous Estimation of Camera and Third-Party Motions")) until the labels converge or a maximum number of iterations have been reached. The final label set is then sanitized (Section III-E: Simultaneous Estimation of Camera and Third-Party Motions")) before being used to estimate the final trajectory hypotheses (Section III-F: Simultaneous Estimation of Camera and Third-Party Motions")).

### III-E Label Sanitization

The final labels are sanitized to refine the segmentation output and remove noisy tracklets before the final model estimation. A merging step first combines any redundant labels regardless of graph connectivity as there is no subsequent splitting stage. After merging, any label with fewer than a minimum number of support tracklets or that exists for fewer than a minimum number of frames is merged with $\mathcal{O}$. Likewise, tracklets whose residual error is greater than a threshold, $e_{th}$, are relabeled as outliers. This provides a consistent set of tracklets for the batch estimation of each motion.

### III-F Final Model Estimation

For each label, an egomotion hypothesis, ${}_{}^{\ell}T_{C}^{}$, is estimated to explain the motion of the tracklets, $\mathcal{P}_{\ell}$, using bundle adjustment. This paper follows the single-motion approach described by Barfoot to estimate the trajectory of each label in an egocentric frame.

The system state, $\mathbf{x}$, of each label is defined to include both the estimated pose transforms, ${{}_{}^{\ell}T} ≔ \left( {{}_{}^{\ell}\mathbf{T}_{C_{k}C_{1}}^{}} \right)_{k = {2\ldotsK}}$, and the landmark points, $\left\{ \mathbf{p}_{C_{1}}^{j_{1}C_{1}} \right\}_{j = {1\ldots{|\mathcal{P}_{\ell}|}}}$. The state $\mathbf{x}_{jk} ≔ \left\{ {{}_{}^{\ell}\mathbf{T}_{C_{k}C_{1}}^{}},\mathbf{p}_{C_{1}}^{j_{1}C_{1}} \right\}$ is defined for each pair of transforms and points belonging to label $\ell$.

Each observation, $\mathbf{y}_{jk}$, of point $\mathbf{p}^{j}$ at pose ${}_{}^{\ell}\mathbf{T}_{C_{k}C_{1}}^{}$ is modeled as The measurement model, $\mathbf{g}(\cdot)$, encompasses both the motion model, $\mathbf{z}(\cdot)$, which applies $SE{}$ transforms to observed points, and the sensor model, $\mathbf{s}(\cdot)$, derived from the perspective camera model. The model assumes additive Gaussian noise, $\mathbf{n}_{jk}$, with zero mean and covariance $\mathbf{R}_{jk}$. The least-squares cost function is defined as the difference between the measurement model and the observations, This cost is linearized about an operating point, $\mathbf{x}_{op}$, and then minimized using Gauss-Newton. The operating point is perturbed according to the transform perturbations, $\{{\mathbf{\epsilon}_{k} \in {\mathbb{R}}^{6}}\}$, and landmark perturbations, $\{{{\mathbf{ζ}}_{j} \in {\mathbb{R}}^{3}}\}$, which together form the full state perturbation, $\delta\mathbf{x}$. An indicator matrix $\mathbf{P}_{jk}$ is defined such that ${\delta\mathbf{x}_{jk}} = {\mathbf{P}_{jk}\delta\mathbf{x}}$. See for more detail.

(a) Top-left swinging box (b) Top-right swinging and rotating box (c) Bottom-left swinging box (d) Bottom-right rotating box Figure 6: The translational and rotational errors for the estimated motion of each object over the length of the estimation window as compared to ground-truth trajectory data. Errors are reported in an arbitrary geocentric frame with the z-axis up, and the arbitrary x- and y-axes. Both the top-left block (a) and the bottom-left block (c) partially left the camera frustum near the beginning of the segment which resulted in gaps in the trajectory estimates for those blocks.

The error function is linearized using $\mathbf{G}_{jk}$, the Jacobian of the measurement function, $\mathbf{g}(\cdot)$, where the matrix operator $(\cdot)^{\odot}$ is defined. The cost function can then be linearized using The optimal perturbation, $\delta\mathbf{x}^{\ast}$, for minimizing the cost function, $J$, is the solution to ${\mathbf{A}\delta\mathbf{x}^{\ast}} = \mathbf{b}$. Each element of the state is then updated according to where the vector operator $(\cdot)^{\land}$ is defined. The cost function is then relinearized about the updated operating point and the process iterates until convergence.

### III-G Egocentric and Geocentric Trajectories

### Egocentric

Egocentric motions are expressed in the moving camera frame, ${\underset{\rightarrow}{\mathcal{F}}}_{C_{k}}$. The egocentric motion of the camera is identity by definition and the egocentric motions of the scene are given by One of these motions is the egocentric motion of the static world *caused* by the camera motion.

### Geocentric

Geocentric motions are expressed in some earth-attached frame. The geocentric motion of the camera is given by the hypothesis motion estimated from the static background, where the static label may be selected by heuristics as in VO (e.g., label support size).

Figure 7: The translational and rotational errors for the egomotion of the camera over its path compared to ground-truth trajectory data. Errors are reported in the egocentric camera frame with the z-axis along the optical axis, and the y-axis down.

The geocentric motions of the rest of the scene are given by where $\mathbf{F}_{\ell_{k}\ell_{1}}$ is the object deformation matrix and is assumed to be identity, (i.e., rigid body). The initial transform, relates the camera to the center of motion of each object, $\mathbf{r}_{\ell_{1}}^{C_{1}\ell_{1}}$. The object center is calculated from the centroid of all points, $\mathcal{P}_{\ell}$, projected into the first observed frame, where $t_{j}$ is the first frame where $p^{j}$ is observed, and $\mathbf{C}_{\ell_{1}C_{1}}$ is arbitrary and assumed to be identity. This averaging allows the centroid estimate to adjust as new points are observed due to rotation or occlusion.

## Experiments and Results

The accuracy of the MVO algorithm is evaluated on real-world data collected using a Bumblebee XB3 stereo camera and a Vicon motion capture system. Unlike existing multimotion datasets designed for egomotion or segmentation (e.g., ), this new dataset contains ground truth for the *entire* scene which consisted of a moving camera observing four moving blocks (Fig. 1: Simultaneous Estimation of Camera and Third-Party Motions")).

The results (Figs. 7: Simultaneous Estimation of Camera and Third-Party Motions") and 6: Simultaneous Estimation of Camera and Third-Party Motions")) were produced from a $500$-frame image sequence. Estimation was performed as a 48-frame sliding window, with $5$ neighbors for each point in the graph, $1000$ RANSAC iterations per new label, $e_{th} = 4$, $\alpha = 100$, $\beta = 2$, $\psi_{\ell} = 1000$, $\lambda = 1$, and a minimum model size and length of $10$ points and $3$ frames, respectively. Feature detection and matching were performed using LIBVISO2 and the Gauss-Newton minimization was performed with Ceres using analytical derivatives (Section III-F: Simultaneous Estimation of Camera and Third-Party Motions")).

The transforms between the Vicon frames and our estimated frames are arbitrary, so the first $25$ frames of the estimates are used to calibrate this transform. All errors are reported for geocentric trajectory estimates. The camera egomotion (Fig. 7: Simultaneous Estimation of Camera and Third-Party Motions")) exhibits a maximum total drift of $0.21$ m, $3.24\%$ of total path length, and a maximum rotational error of $1.96^{\circ}$, $- 1.00^{\circ}$, and $- 0.42^{\circ}$ in roll-pitch-yaw, respectively. This error is reasonable compared to the level of drift in other model-free, camera-only VO systems.

The motion estimates of the bodies varied with their motion and their visibility. The two swinging blocks partially left the camera frustum near the beginning of the segment which caused estimation dropouts and higher translational errors. A portion of the geocentric error of each motion is due to the error in the camera motion estimate. The maximum translational and rotational errors for each block are $0.44$ m, $- 9.09^{\circ}$, $- 5.28^{\circ}$, and $2.67^{\circ}$ for the top-left block; $0.27$ m, $- 6.19^{\circ}$, $- 6.05^{\circ}$, and $- 5.00^{\circ}$ for the top-right block; $0.99$ m, $2.33^{\circ}$, $6.58^{\circ}$, and $3.15^{\circ}$ for the bottom-left block; and $0.39$ m, $- 2.74^{\circ}$, $1.71^{\circ}$, and $- 8.10^{\circ}$ for the bottom-right block (Fig. 6: Simultaneous Estimation of Camera and Third-Party Motions")).

The gaps in the trajectories occur when the motion was not successfully segmented or the final estimation stage (Section III-F: Simultaneous Estimation of Camera and Third-Party Motions")) fails to converge. This is often due to poor feature distribution, especially when objects reach the edge of the camera frustum. These discontinuities, coupled with the dynamic camera motion, caused errors in the trajectory estimate.

## Discussion

MVO consistently segments and estimates the motions of the camera and the four independent objects when they are fully visible. As is to be expected, the two blocks that partially exited the camera frustum had segmentation failures and higher errors, largely due to incomplete feature tracklets.

Feature distribution is an important factor in the performance of any sparse approach. This problem is exacerbated for dynamic objects that take up a small portion of the scene. Additionally, the appearance of these objects is often more volatile making feature association even more difficult. The algorithm is dependent on the accuracy of the input tracklet set and cannot estimate motions for which there are insufficient features. Feature dropouts and lack of tracklets are therefore significant challenges for this type of pipeline, and the development of more robust feature detection and matching pipelines is an ongoing area of research.

The distribution of features also influences the estimate of the center of the motion. It is difficult to infer the structure of an object beyond the surfaces that are observed in the batch without a priori knowledge of the object's shape. This means the centroid of the observed feature points for a label can often be a bad estimate of the the label's true center of motion.

## Conclusion

This paper extends the classic VO pipeline to address the multimotion estimation problem. The multimotion visual odometry (MVO) pipeline segments and estimates *all* rigid motions in a scene. It does so by using feature-tracking, sparse graph segmentation, and multiframe batch motion estimation such that it avoids many of the limitations of other multimotion estimation approaches.

We evaluated MVO on a multimotion dataset with ground-truth trajectories for all motions in the scene. Its estimation accuracy is comparable to similarly defined egomotion-only VO systems while also exhibiting similar limitations. We are actively exploring the application benefits of continuous-time state estimation and continuous labels, as well as implementing the pipeline such that it can be used in real-time.
