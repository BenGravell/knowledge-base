<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Unified Autonomy Stack: Toward a Blueprint for Generalizable Robot Autonomy

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce and open-source the Unified Autonomy Stack, a system-level solution that enables resilient autonomy across diverse aerial and ground robot morphologies. The architecture centers on three synergistic modules - multi-modal perception, multi-behavior planning, and multi-layered safe navigation - that together deliver comprehensive mission autonomy. The stack fuses data from LiDAR, radar, vision, and inertial sensing, enabling (a) robust localization and mapping through factor graph-based fusion, (b) semantic scene understanding, (c) motion and informative path planning through sampling-based techniques adaptive across spatial scales, as well as (d) multi-layered safe navigation both through planning on the online reconstructed map and deep learning-driven exteroceptive policies alongside last-resort safety filters using control barrier functions. The resulting behaviors include safe GNSS-denied navigation into unknown and perceptually-degraded regions, exploration of complex environments, object discovery, and efficient inspection planning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The stack has been field-tested and validated on both aerial (rotorcraft) and ground (legged) robots operating in a host of demanding environments, including self-similar and smoke-filled settings, with complex geometries and high obstacle clutter. These tests demonstrate resilient performance in challenging conditions. To facilitate ease of adoption, we open-source the implementation alongside supporting documentation, validation, and evaluation datasets A video giving the overview of the paper and the field experiments is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mobile robots are increasingly deployed to operate in environments where Global Navigation Satellite System ([GNSS]) is unavailable, perception is degraded, geometry is self-similar, and safe navigation is broadly challenged Tranzatto et al.; Harlow et al.; Ebadi et al.; Datar et al.; Chung et al.. Although the robotics community has developed mature components for many individual functionalities such as localization, planning and control, existing autonomy stacks (e.g., the works in Fernandez-Cortizas et al.; Sanchez-Lopez et al.; Baca et al.; Mohta et al.; Foehn et al.; Goodin et al.; AirLab; Real et al. ) remain largely specialized to a particular robot morphology, sensor suite, or mission class. This specialization limits reuse across platforms, makes systematic field evaluation difficult, slows the accumulation of shared deployment experience, and hinders both consolidation and broader uptake of autonomy across robot categories.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, limited attention has been given to feature-rich autonomy stacks readily delivering complex behaviors and functionalities such as resilient [GNSS]-denied navigation in perceptually-degraded environments, combined with sophisticated informative path planning and assured safety ensuring robust operation across operational environments and conditions. However, recent advances across the "sense-think-act" loop -from perception to planning and deep control policies- point toward the potential for a resilient and, to a significant extent, unified autonomy engine. Although research on universal autonomy is still in its early stages, the benefits of unification and the collective need to advance robot capabilities underscore the need for general autonomy solutions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by the above, we present the Unified Autonomy stack ([UAstack]), a comprehensive open-source autonomy stack that can support mission-level operation across diverse aerial and ground robot configurations. The [UAstack] represents a step towards a common autonomy blueprint across diverse robot types -from multirotors and other rotorcrafts to ground robots such as legged systems- delivering mission-complete capabilities for navigation and complex information sampling behaviors (e.g., exploration, inspection, object discovery) in diverse settings, including in strenuous, high-risk natural and industrial environments. Its design emphasizes resilience in that it presents robustness (e.g., against noisy sensor data and mapping imperfections), resourcefulness (e.g., multiple solutions for safety in navigation), and redundancy (e.g., complementary sensor data to handle single-modality failures), enabling it to retain high performance across environments and conditions, including [GNSS]-denied, perceptually-degraded, geometrically complex, and potentially adversarial settings that typically challenge safe navigation and mission autonomy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The [UAstack] builds upon three core modules and associated contributions. The perception module is centered around a novel approach to multi-modal Simultaneous Localization And Mapping ([SLAM]) based on factor graphs, enabling robust fusion of LiDAR, Frequency Modulated Continuous Wave ([FMCW]) radar, visual perception, and Inertial Measurement Unit ([IMU]) cues. This supports resilient performance in [GNSS]-denied environments with multiple perceptual degradations, including geometric self-similarity, low texture, icy scenes, and dense obscurants (e.g., fog, smoke). Furthermore, the perception module integrates scene reasoning through Vision-Language Models enabling object discovery and visual question & answering (Q&A). The planning module builds upon OmniPlanner Zacharia et al., facilitating target reaching, exploration, and inspection path planning through sampling-based methods over an online-derived volumetric map of the environment. It provides a versatile framework that abstracts vehicle configuration and supports diverse mission objectives, which the planner optimizes accordingly.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The navigation module builds upon the contributions in Jacquet et al.; Harms et al., alongside introducing a novel approach to exteroceptive reinforcement learning for navigation. Recognizing that localization errors and mapping imperfections may arise, we adopt a redundant, multi-layered safety approach in which depth-based exteroceptive navigation policies and last-resort control barrier function-based safety filters enhance safety by providing direct and reactive collision avoidance. As a result, the [UAstack] is tailored to environments that challenge localization and mapping, both by leveraging sensor multi-modality to maintain perception under degraded conditions, and by implementing reactive safety mechanisms to reduce reliance on perfect scene understanding.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To evaluate the performance and assess its resilience, the [UAstack] is evaluated onboard multiple robot configurations and within a diverse set of environments, an indicative subset of which is shown in Figure 1. First, a detailed quantitative evaluation of the perception module is presented, covering $2$ urban tunnels, a frozen lake and a university campus environment characterized by geometric self-similarity, low visibility, and heavy airborne obscurants. It displays the superior performance of the perception module compared to State-of-the-Art LiDAR-Inertial, LiDAR-Radar-Inertial, LiDAR-Visual-Inertial, or Visual-Inertial [SLAM] methods. Object-level reasoning is assessed by building 3D scene graphs with object-level annotations, alongside enabling visual Q&A on online camera data. Next, the navigation module is evaluated in two real-world deployments. First, in a forest environment for a waypoint-navigation task requiring maneuvering to avoid trees, while map-based path planning is disabled to isolate the reactive layer.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we evaluate safety under map discrepancies by introducing previously unmapped obstacles along the path planned by the planning module and demonstrate that the navigation module layer can handle such unseen obstacles. These experiments highlight the importance of the multi-layered safety approach and the complementary roles of each safety method. Finally, the full [UAstack] is evaluated on aerial and legged robots performing autonomous exploration and inspection missions guided by the planning module. The aerial robot is deployed in a) a low-visibility, multi-branched underground mine, and b) a forest with thin obstacles and local clutter, performing exploration missions, with navigation module modalities being tested. Additionally, the aerial robot is deployed in the cargo hold of a ship performing an exploration and inspection mission. On the other hand, the legged robot is deployed in a university campus, and inside the same underground mine as the aerial robot. This demonstrates large-scale missions across heterogeneous platforms and environments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Importantly, the Unified Autonomy Stack is open to extension, both from the perspective of the robots it readily supports and the missions it enables. Our team is targeting its full-fledged expansion to a diverse set of robot configurations and the extension of the enabled behaviors. To that end, the full implementation is open-sourced, alongside documentation and supporting datasets.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is structured as follows. Section 2 overviews related work in autonomy stacks. The [UAstack] and its modules are detailed in Section 3. Evaluation studies are presented in Section 4, followed by conclusions and plans for future work in Section 5.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Unified Autonomy", "weight": 1.0} -->

This section presents the architecture and key modules of the unified autonomy stack.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Autonomy Architecture", "weight": 1.0} -->

The Unified Autonomy Stack is organized around three core modules -- perception, planning, and navigation -- following the principles of the "sense-think-act" loop, while targeting generalizability across aerial and ground robot configurations, and resilience in demanding environments. Its overall architecture is presented in Figure 2. The [UAstack] consumes diverse sensor data and outputs low-level commands to standard controllers available in most modern robotic systems, for example, on PX4-based drones Meier et al. (or any other MAVLink-compatible autopilot Koubâa et al.)) and standard (linear and angular) velocity controllers on ground platforms. Its key features are as follows: Figure 2: The architecture of the UAstack. The stack involves three core modules, on perception, planning, and navigation that operate in a synergistic fashion. Aiming for operational resilience in diverse GNSS-denied, perceptually-degraded environments the UAstack emphasizes multi-modal sensor fusion merging data from LiDAR, radar, and camera sensing, alongside IMU cues. VLM-based reasoning builds upon the geometric reconstruction and supports object discovery and visual question/answering.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Autonomy Architecture", "weight": 1.0} -->

The stack’s planning layer offers diverse behaviors, with ready-made implementations for target-reach, unknown area exploration and inspection, across robot morphologies. Even though map-based collision avoidance and traversability analysis are provided within the planning module, the stack’s navigation module further offers a multi-layered approach to safety involving deep exteroceptive navigation strategies, either through neural model predictive control or reinforcement learning, alongside formal last-resort safety based on control barrier functions. In terms of morphologies, the UAstack currently supports aerial and ground robots, especially rotorcrafts (e.g., multirotors), legged robots and ground rovers. Experimental validation has taken place on different multirotor systems and quadruped legged robots, while simulation examples in the released code include additional morphologies such as ground rovers and helicopters.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Generalizability", "weight": 1.0} -->

The [UAstack] applies with few adjustments to a wide range of robot configurations, offering a consistent user experience for navigation and informative path planning tasks across platforms. Currently out-of-the-box supporting multirotors and other rotorcrafts, alongside several ground systems and especially legged robots, it provides a strong foundation for research in unified embodied AI. In this paper, we present experimental verification with multirotors and quadrupeds, while the associated open-source repository includes examples with additional morphologies such as ground rovers and helicopters.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Multi-modality", "weight": 1.0} -->

The [UAstack] fuses complementary sensor cues, currently including LiDAR, [FMCW] radar, vision, and [IMU], enabling resilience in perceptually-degraded and [GNSS]-denied conditions Chung et al., including settings characterized by self-similar geometries, dark or low-texture scenes, icy regions, and obscurants such as smoke and dust. We emphasize the tight fusion of LiDAR and radar data focusing on their complementary role in numerous perceptually-degraded environments as discussed in the evaluation section.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Multi-layer Safety", "weight": 1.0} -->

The [UAstack] departs from conventional architectures in which safety is ensured by solutions with a single point-of-failure. Most commonly, modern autonomy solutions rely on a cascade of calculations in which collision-free planning takes place only on an online reconstructed map. In practice, it entails that non-trivial localization or mapping errors (e.g., such as those often encountered in perceptually-degraded settings or when encountering thin obstacles) can lead to collisions. The [UAstack] combines map-based motion planning with deep learning-driven navigation strategies and safety filters that directly consume online exteroceptive depth measurements and, if necessary, adjust the robot's path to re-assert safety.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Methodological Plurality", "weight": 1.0} -->

The [UAstack] integrates both "conventional" model-based control, estimation, perception, optimization and planning techniques, as well as deep learning-based methods alongside hybrid techniques. Indicative examples include its factor graph-based multi-modal [SLAM] and its navigation policies offering options for Deep Reinforcement Learning ([DRL])-based and Neural Model Predictive Control ([NMPC]).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Methodological Plurality", "weight": 1.0} -->

Subsequently, we outline the key modules of the [UAstack] and point to prior works as applicable. Furthermore, we discuss the interfaces considered and how [UAstack] can be extended to new robot configurations. Importantly, all autonomy modules described hereafter operate subject to the information provided to the stack's Robot Abstraction Layer and the Mission Abstraction Layer.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Robot Abstraction Layer", "weight": 1.0} -->

This layer defines the robot type (e.g., multirotor, quadruped, etc.) and its key motion parameters, alongside its sensor suite $\pazocal{S}$ including the sensor types (e.g., LiDAR, Radar, cameras, [IMU]) and their configurations (e.g., fields of view, effective ranges, calibration constants). Based on this layer, the modules of the [UAstack] determine the robot motion constraints $\mu_{R}$ to be applied (e.g., robot size, potentially applicable traversability constraints, kinematic constraints), the sensor data to be fused, sensor intrinsic and extrinsic calibration parameters, time-synchronization information between the sensors, as well as the command interface to be used (e.g., acceleration commands for multirotors, velocity commands to a quadruped legged robot) as detailed in Section 3.5. It also sets if certain modules of the [UAstack] are enabled such as if multi-layered safety will be employed and if yes, which submodules of it will be engaged.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Mission Abstraction Layer", "weight": 1.0} -->

This layer sets the task for the robot, including if this relates to reaching a target, exploring an unknown area, inspecting a previously explored region, any combination among those, or any other behavior built beyond the existing capabilities of the [UAstack]. It accordingly defines the objective of the planning module. It also sets if certain modules are active such as the [VLM]-based scene reasoning.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Perception Module", "weight": 1.0} -->

The perception module includes our solution for multi-modal [SLAM], alongside integration with a [VLM]-based reasoning step.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Multi-Modal [SLAM]", "weight": 1.0} -->

The proposed novel multi-modal [SLAM] system (dubbed MIMOSA-X, where 'X' denotes the modalities used) uses a factor graph estimator to fuse LiDAR, radar, camera, and [IMU] measurements using a windowed smoother Dellaert and GTSAM Contributors for computational efficiency. This architecture, as shown in Figure˜2, builds upon ideas proposed in Khedekar et al.; Nissov et al., with improvements drawn from further developments in Khedekar and Alexis; Nissov et al. for enhanced LiDAR and radar integration, alongside vision integration. Unlike loosely coupled approaches Khedekar et al.; Khattak et al.; Shan et al., MIMOSA-X fuses LiDAR registration factors, radar Doppler factors, and preintegrated [IMU] factors in a tightly-coupled manner to avoid degenerate optimizations returning partially observable results. Vision is further optionally fused through between factors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Multi-Modal [SLAM]", "weight": 1.0} -->

Furthermore, calibration states such as the accelerometer $\bm{b}_{\mathtt{a}}^{\mathtt{}}$ and gyroscope $\bm{b}_{\mathtt{g}}^{\mathtt{}}$ biases and gravity direction $\bm{g}_{\mathtt{}}^{\mathtt{W}}$ in the map frame are also included. The online gravity estimation has been shown to improve performance Nemiroff et al., as initial uncertainty regarding the platform attitude can result in map-errors which compound over large distances.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multi-Modal [SLAM]", "weight": 1.0} -->

The state space $\mathbf{x}$ is thus decomposed into local $\mathbf{x}_{\text{L}}$ and global $\mathbf{x}_{\text{G}}$ states such that By concatenating the states from times $t_{k-l}$ to $t_{k}$, the windowed set of states $\mathcal{X}_{k-l:k}$ is defined as The states over this temporal window of size $l+1$ are thus estimated by the iSAM2 Kaess et al. nonlinear optimizer, where the optimal estimate $\mathcal{X}_{k-l:k}^{*}$ is found by minimizing the covariance-weighted ($\Sigma_{\star}$) sum of the residuals $\bm{e}_{\star}$ derived from the [IMU], LiDAR, radar, and vision sensor measurements included in the temporal window, denoted by $\mathcal{I}$, $\mathcal{L}$,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Multi-Modal [SLAM]", "weight": 1.0} -->

For each [IMU] measurement, a prediction is made from the current graph state, resulting in a high-rate odometry output. Upon receiving a new exteroceptive sensor measurement, the graph is updated with the relevant factors, and the optimal state estimate is calculated, alongside maps updated if the measurement was a LiDAR measurement.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Multi-Modal [SLAM]", "weight": 1.0} -->

It is not required that all sensors operate at the same frequency, nor that their measurements arrive chronologically by their timestamps. The method does, however, assume that the timestamps of the input measurements are accurate, i.e., some effort from the implementer has been taken to ensure the accuracy of the timestamping of the sensor data in the form of hardware or software-based time synchronization, such that all timestamps are on a common time axis. A representative factor graph constructed by the multi-modal estimator is shown in Figure˜3. We first give an overarching view of the operation of the system and later detail how each of the sensor measurements is used.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Initialization", "weight": 1.0} -->

The method assumes the system is stationary at startup. During this period, [IMU] measurements are accumulated over a $1\text{\,}\mathrm{s}\text{/}$ window and averaged, yielding the mean accelerometer reading $\bm{\mu}_{\mathtt{a}}^{\mathtt{}}$ and mean gyroscope reading $\bm{\mu}_{\mathtt{g}}^{\mathtt{}}$. Since the system is at rest, the gyroscope mean is a direct estimate of the gyroscope bias, so we set $\bm{b}_{\mathtt{g,0}}^{\mathtt{}}=\bm{\mu}_{\mathtt{g}}^{\mathtt{}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Initialization", "weight": 1.0} -->

Because the accelerometer bias is not yet known, we approximate $\mathbf{R}_{\mathtt{B,0}}^{\mathtt{W}}$ by aligning $\bm{\mu}_{\mathtt{a}}^{\mathtt{}}$ with the gravity direction $\begin{bmatrix}0&0&1\end{bmatrix}^{\top}$, which determines the roll and pitch components. The yaw component is unobservable from accelerometry alone and is set to zero. This approximation introduces an attitude error proportional to the magnitude of $\bm{b}_{\mathtt{a,0}}^{\mathtt{}}$; for instance, a bias of $1\text{\,}\mathrm{m}\text{/}{\mathrm{s}}^{2}$ yields an initial attitude error of approximately $5\text{\,}\mathrm{\SIUnitSymbolDegree}\text{/}$, following Farrell.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Initialization", "weight": 1.0} -->

Initialization is triggered upon arrival of the first exteroceptive sensor measurement, provided the [IMU] buffer spans at least $1\text{\,}\mathrm{s}\text{/}$. In the case of LiDAR, this step additionally initializes the global map, as described in the following section.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Propagation", "weight": 1.0} -->

Upon receiving a new measurement from the [IMU], the measurement is added to a buffer for future use in the main thread. In a separate thread, this measurement is used to propagate the latest state in the graph, which is then published to provide high-rate odometry for feedback control.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Propagation", "weight": 1.0} -->

Upon receiving a new measurement from an exteroceptive sensor, typically, the method (a) creates a new state at the timestamp derived from the measurement, (b) connects the new state with the remaining graph with a preintegrated [IMU] factor derived from the [IMU] buffer, (c) adds a factor derived from the measurement, (d) optimizes the graph, and (e) publishes the new state. However, depending upon the actual sensor stream and system, the method may deviate slightly from this. We now detail these deviations. If the timestamp of the incoming measurement is older than the lag window, it is discarded prioritizing low-latency data. If the timestamp of the new measurement is very close (i.e., there are no [IMU] measurements in between) to the timestamp of any of the states in the window, then we treat the measurement as having the same timestamp as that state, i.e., we do not create a new state and use the matched state for adding a measurement-derived factor.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Propagation", "weight": 1.0} -->

This has the added advantage that late measurements arriving to the graph out-of-order can seamlessly be integrated, assuming they are within the smoother window. If the timestamp is older than the newest state in the window (i.e., it arrived with high latency), then we identify the correct location that it should have been added as well as the preintegrated [IMU] factor that currently connects the states straddling this timestamp. The preintegrated [IMU] factor is then replaced by a new state at the new timestamp, along with the measurement-derived factor and two new preintegrated [IMU] factors.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Propagation", "weight": 1.0} -->

The next paragraphs detail the specifics on the handling of each sensor modality. Note, some factor residuals are constructed on a per-point basis, e.g., in the case of the LiDAR and radar factors. For computational savings, these are implemented as a single Hessian factor by summing individual contributions. For brevity, the factor residuals will be defined on a per-point basis, and the summation implied.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Inertial Measurement Unit", "weight": 1.0} -->

[IMU] measurements are stored in a buffer on arrival, for easy use upon receiving measurements from one of the aiding sensors. At that point, the corresponding exteroceptive factors are created and connected to the graph by an [IMU] preintegration factor, following Forster et al., with the following residuals that preintegrate the measurements between times $i$ and $j$ including attitude $\bm{e}_{\mathcal{I},\mathbf{R}}$, position $\bm{e}_{\mathcal{I},\bm{p}}$, and velocity $\bm{e}_{\mathcal{I},\bm{v}}$ error terms. The reader is referred to Forster et al.; Dellaert and GTSAM Contributors for a detailed description of each term.

<!-- chunk {"id": "body-0037", "role": "body", "section": "LiDAR", "weight": 1.0} -->

The point cloud measurement obtained from a LiDAR typically contains several thousand points that were sampled at various instants between $[t,t+t_{s}]$ where $t$ is the timestamp of the measurement and $t_{s}$ is the duration of the sweep. Since the LiDAR is likely to have moved during this time, it is necessary to deskew the point cloud to account for this motion. As the [IMU] measurements for this duration are available, we use them to propagate the latest state in the graph up to $t+t_{s}$, storing the intermediate pose $\mathbf{\tilde{T}}_{\mathtt{B,t+t_{k}}}^{\mathtt{W}}$ for every unique timestamp $t+t_{k}$ in the point cloud.

<!-- chunk {"id": "body-0038", "role": "body", "section": "LiDAR", "weight": 1.0} -->

Using these intermediate poses, we iterate over the points $\bm{r}_{\mathtt{}}^{\mathtt{L,t+t_{k}}}$ at each unique timestamp and transform them to the body frame at the timestamp of the last point $t+t_{s}$ as given by where $\circ$ denotes the homogeneous transformation action on a vector in $\mathbb{R}^{3}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "LiDAR", "weight": 1.0} -->

For further processing, assuming that the IMU propagation was correct, the point cloud is considered to have been sampled instantaneously at $t+t_{s}$. Afterwards, the point cloud is downsampled, for computational efficiency, first by removing three out of four points, and second by organizing the point cloud into a voxel grid and subsampling, ensuring a maximum of $n_{p}$ points per voxel and a minimum distance of $\eta_{p}$ between any two points in a voxel. Afterwards, the correspondences are found by relating points in the current cloud with planes fit in the map; these correspondences are added to the graph in the form of point-to-plane residuals.

<!-- chunk {"id": "body-0040", "role": "body", "section": "LiDAR", "weight": 1.0} -->

This per-point residual $\epsilon_{\mathcal{L}}$ is calculated as follows for a plane defined by the normal $\bm{n}_{\mathtt{}}^{\mathtt{W}}$ and point $\bm{r}_{\mathtt{0}}^{\mathtt{W}}$ and the corresponding transformed point $\bm{\tilde{r}}_{\mathtt{\mathcal{L}}}^{\mathtt{B}}$ from the downsampled LiDAR point cloud. The per-point residuals are whitened using the point noise covariance $\sigma_{\epsilon_{\mathcal{L}}}^{2}$ and assembled into a single dense hessian factor. For outlier rejection, these residuals are augmented with Huber M-estimators Huber. Post-optimization, the pose is compared with previous key frames, and if a significant difference in position or attitude is detected, a new key frame is created, and the current point cloud is added to maintain a monolithic map.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Radar", "weight": 1.0} -->

In the context of this method, [FMCW] radars are assumed to return point cloud measurements, where each point is defined by its 3D position $\bm{r}_{\mathtt{\mathcal{R}}}^{\mathtt{}}$ and radial speed $v_{r}$. Unlike the estimator proposed in Nissov et al., here the RANdom SAmple Consensus ([RANSAC]) least-squares calculation of linear velocity from the radar point cloud is omitted. Instead, the individual points from the radar point cloud are integrated into the graph. By directly integrating the radial speed measurements, we avoid the potential limitations associated with first estimating linear velocity independently. Namely, these are the minimum number and diversity of points required for fully resolving the 3 axes of linear velocity. Even with sufficient points, low point cloud sizes can still result in poor estimation of either the velocity or the covariance matrix, leading to degraded performance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Radar", "weight": 1.0} -->

Thus, the per-point residual $\epsilon_{\mathcal{R}}$ for the radar Doppler factor is where $\bm{\hat{v}}_{\mathtt{WR}}^{\mathtt{R}}$ is the radar-frame velocity estimate and $\tilde{\bm{r}}$, $\tilde{v}_{r}$ are the radar point position and radial speed measurements.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Radar", "weight": 1.0} -->

The radar-frame velocity is composed from the state estimates as assuming the extrinsic translation $\bm{p}_{\mathtt{BR}}^{\mathtt{B}}$ and rotation $\mathbf{R}_{\mathtt{B}}^{\mathtt{R}}$ between $\{\mathtt{B}\}$ and $\{\mathtt{R}\}$ is known a priori, and that the angular rate during a given radar chirp period $\bm{\bar{\omega}}_{\mathtt{WB}}^{\mathtt{B}}$ can be accurately estimated by averaging the [IMU] gyroscope measurements. As the radar sensor is known to generate spurious points Harlow et al., the residual is augmented with a Cauchy M-estimator for outlier rejection. This has the added benefit of improved resilience against dynamic objects by suppressing the influence of such outliers.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Radar", "weight": 1.0} -->

The choice of Cauchy is motivated by the desire for an M-estimator that more rapidly nullifies the impact of significantly large outliers.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Vision", "weight": 1.0} -->

Vision factors are added in a loosely-coupled manner, taking advantage of the wealth of capable estimators that exist in the vision community. Specifically, a visual-inertial estimator based on Bloesch et al. processes the camera and [IMU] measurements, creating odometry estimates as a result. The pose estimates $\mathbf{\tilde{T}}_{\mathtt{B}}^{\mathtt{W}}$ from this external method are stored in a buffer. This information is incorporated, if it passes a D-Optimality pose quality check Carrillo et al., into the factor graph with a relative transform factor, which compares the relative transform between pose estimates $\mathbf{\hat{T}}_{\mathtt{B}}^{\mathtt{W}}$ and the aforementioned measurements across the same time interval.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Vision", "weight": 1.0} -->

Assuming vision pose measurements are available for times $t_{i}$ and $t_{j}$, the factor residual can be calculated as where $\operatorname*{Log}$ denotes the logarithmic map from the $\textit{SE}$ manifold to its Lie algebra $\mathfrak{se}$. This approach draws inspiration from Khattak et al.; Khedekar et al..

<!-- chunk {"id": "body-0047", "role": "body", "section": "Vision-Language Reasoning", "weight": 1.0} -->

Our semantic reasoning system integrates two complementary vision-language model (VLM) capabilities: (i) open-vocabulary object perception with semantic 3D mapping, and (ii) binary visual question-answering (Yes/No) for high-level scene reasoning. Together, these capabilities collectively enable semantic scene understanding and contextual judgment and decision making from online visual data. The [VLM]-based functionality is illustrated in Figure 4. Even though our implementation employs YOLOe Wang2025YOLOE and GPT-5, the proposed semantic reasoning system is designed to be compatible with other open-source and proprietary [VLM]s that support open-vocabulary object detection and visual question-answering tasks.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Open-Vocabulary Object Detection and Semantic 3D Mapping", "weight": 1.0} -->

3D object detection is formulated as a semantic mapping problem. Objects are detected on the camera image using an open-vocabulary detector (YOLOe) or a [VLM]-based detector (GPT-5) initialized with a set of labels. These models produce labeled 2D bounding boxes and associated detection confidences. In parallel, a 3D voxel grid is maintained using LiDAR measurements and pose estimates from our [SLAM] solution.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Open-Vocabulary Object Detection and Semantic 3D Mapping", "weight": 1.0} -->

To integrate semantic detections into the 3D representation, voxel grid points are projected into the camera frame using the camera extrinsics and the current odometry estimate. For each 2D detection, the subset of projected points that fall within the corresponding bounding box is extracted and clustered to remove outliers. The resulting points are used to update the voxels' semantic values via Bayesian fusion, which uses the object detector's confidences.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Open-Vocabulary Object Detection and Semantic 3D Mapping", "weight": 1.0} -->

Finally, Euclidean clustering is performed for each semantic class present in the voxel grid to extract 3D object instances. These objects are represented as 3D bounding boxes, enabling semantic and spatial reasoning.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Binary Visual Question-Answering", "weight": 1.0} -->

For high-level semantic assessment, a [VLM] (GPT-5) processes the front-camera image together with a binary "Yes/No" question. These visual question-answering tasks typically focus on safety- or navigation-related properties of the scene (e.g., "is an object blocking a door?"), which can be challenging to infer from geometric information alone. The model produces a binary answer, alongside its response confidence (ranging from 0 to 1) and a brief explanation of its reasoning.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Planning Module", "weight": 1.0} -->

The planning module in the [UAstack] is facilitated through [OmniPlanner] Zacharia et al., a graph-based planner designed to work across diverse aerial, ground, and underwater robot morphologies. The planner is currently applicable to systems for which graph-based planning is a viable option (e.g., various thrust-controlled aerial and underwater systems such as multirotors and ROVs, legged robots, and differential drive ground rovers). At the core, the planner utilizes a unified planning kernel that is agnostic to robot morphology, environment type, and mission objective and provides both target navigation as well as informative planning behaviors, such as exploration and inspection, based on the task objective $\mathcal{J}$ ($\mathcal{J}_{TP}$: Planning to a target, $\mathcal{J}_{EP}$: Exploration Planning, $\mathcal{J}_{IP}$: Inspection Planning) set by the Mission Abstraction Layer. Algorithm 1 gives a high-level overview of the planning module, while Figure 5 illustrates the different parts of the module and their interactions.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Planning Module", "weight": 1.0} -->

The reader is referred to Zacharia et al. for the algorithmic details regarding this module.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Planning Module", "weight": 1.0} -->

$\textbf{ExplorationPlanning(}\mu_{R},\pazocal{D},\mathbb{G}_{L},\mathbb{G}_{G},\pazocal{M}\textbf{)}$ 12: $\textbf{InspectionPlanning(}\mu_{R},\pazocal{D},\pazocal{C},\mathbb{G}_{L},\pazocal{M}\textbf{)}$ 14:until Robot Endurance Critical 15:ReturnToHome(𝔾L, 𝔾G, μR) ⊳ Planning Kernel Algorithm 1 planning module

<!-- chunk {"id": "body-0055", "role": "body", "section": "Planning Kernel", "weight": 1.0} -->

The Planning Kernel of [OmniPlanner] serves as the backbone of the methodology, providing the data structures and functions for searching the robot's admissible configuration space to enable the desired behaviors. All operations take place on a dual environment representation consisting of a) a Volumetric Map $\pazocal{M}$ (in this work Voxblox Oleynikova et al. ), with voxel size $v_{m}$, and, when applicable, b) an elevation map $\pazocal{H}$ for ground robots (utilizing the work from Fankhauser et al. ), with grid size $v_{h}$. The kernel employs a bifurcated local/global planning architecture.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Planning Kernel", "weight": 1.0} -->

The Local Planning Submodule operates in a local volume $\bm{b}_{L}$ and constructs a bounded, sampling-based, dense graph $\mathbb{G}_{L}$, with its vertex and edge sets $\pazocal{V}_{L},\pazocal{E}_{L}$ inside $\bm{b}_{L}$ spanning the locally reachable configuration space. All vertices and edges are sampled such that they lie entirely in collision-free space and respect the robot motion constraints $\mu_{R}$ defined by the Robot Abstraction Layer (e.g., traversability, robot size $\bm{b}_{R}$, etc.). The graph $\mathbb{G}_{L}$ is used by the planning module for local information gathering and collision-free navigation as described in the subsequent subsections.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Planning Kernel", "weight": 1.0} -->

The Global Planning Submodule maintains a sparse global graph $\mathbb{G}_{G}=\{\pazocal{V}_{G},\pazocal{E}_{G}\}$ built by aggregating the sparsified local planning graphs across the mission. This graph is used to represent the entire known space, providing fast global planning functionality. As $\mathbb{G}_{G}$ is built from $\mathbb{G}_{L}$, all vertices and edges in $\pazocal{V}_{G},\pazocal{E}_{G}$ are in free space and satisfy the robot motion constraints. The Global Planning Submodule also keeps track of the robot's remaining endurance (or otherwise-defined remaining mission time). At each planning iteration, the Planning Kernel checks if the remaining time is sufficient to execute the path given by the specific behavior and return to the start location. If yes, that path is executed, else, the Kernel triggers a homing manuever to guide the robot back to the starting location.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Planning to a Target", "weight": 1.0} -->

[UAstack] facilitates planning to a desired waypoint $\bm{p}_{t}$ both within the already explored space, as well as in the unknown, as long as this is iteratively found to be possible. In each planning iteration, first, a guiding path $\sigma_{t}$ is calculated. If $\bm{p}_{t}$ lies in the known (explored) space, $\sigma_{t}$ is simply calculated as the shortest path along $\mathbb{G}_{G}$ to the vertex in $\pazocal{V}_{G}$ closest to $\bm{p}_{t}$. Otherwise, $\sigma_{t}$ is calculated as the path towards the vertex that is on the frontier of the explored space and is closest to $\bm{p}_{t}$. Next, $\mathbb{G}_{L}$ is used to calculate a local path $\sigma_{TP}$ guiding the robot along $\sigma_{t}$ which is then commanded to the subsequent modules to track.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Planning to a Target", "weight": 1.0} -->

When the robot reaches within a distance $d_{path}$ from the last point in $\sigma_{TP}$, the next iteration of the planner is triggered. This entire process is repeated until the robot reaches $\bm{p}_{t}$ or no progress can be made towards it, at which point the planner declares that the waypoint is unreachable. It is highlighted that the homing maneuver mentioned in Section˜3.3.1 uses the Planning to Target behavior with the starting location as $\bm{p}_{t}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Exploration Planning", "weight": 1.0} -->

The first informative planning behavior supported by OmniPlanner is the Volumetric Exploration ([VE]), where the robot is tasked to iteratively uncover the unknown volume using an Field of View ([FoV])- and range-constrained depth sensor $\pazocal{D}$ (whose parameters are given by the Robot Abstraction Layer). In each planning iteration, $\mathbb{G}_{L}$ is used to find the path that leads to uncovering the largest amount of unknown space. First, shortest paths from the current robot location to each vertex in $\pazocal{V}_{L}$ are calculated. An information gain, called Volume Gain, related to the amount of unknown volume mapped by $\pazocal{D}$ from a robot configuration, is calculated for each vertex in $\pazocal{V}_{L}$. The path $\sigma_{EP}$ with the highest aggregated Volume Gain is selected as the next exploration path.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Exploration Planning", "weight": 1.0} -->

When the robot reaches within a distance $d_{path}$ from the last point in $\sigma_{EP}$, the next iteration of the planner is triggered and the process is repeated. When no informative path is found in $\mathbb{G}_{L}$, the $\mathbb{G}_{G}$ is utilized to reposition the robot to a frontier of the explored space. The planner tracks vertices in $\mathbb{G}_{G}$ having high Volume Gain (called frontier vertices), and repositions the robot to the frontier vertex having the highest gain using the Planning to Target behavior described in Section˜3.3.2. Upon reaching the frontier, local exploration continues.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Inspection Planning", "weight": 1.0} -->

In the Visual Inspection ([VI]) behavior, the planner is tasked to inspect a subset of the occupied surface in the mapped volume using an [FoV]- and range-constrained camera sensor $\pazocal{C}$ (whose parameters are given by the Robot Abstraction Layer) at the desired viewing distance $d_{view}$ (given by the Mission Abstraction Layer). A set $\mathbb{V}$ of viewpoints, at a distance $d_{view}$ from the occupied surface, is built. A graph $\mathbb{G}_{VI}$ is built using the Local Planning Submodule to connect the viewpoints in $\mathbb{V}$. The minimal viewpoint set $\mathbb{V}_{best}$ viewing the entire surface is selected, and the order to visit them is calculated by solving the Traveling Salesman Problem ([TSP]) problem. The shortest paths along $\mathbb{G}_{VI}$ connecting the subsequent viewpoint in the tour are concatenated to form the inspection path.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Navigation Module", "weight": 1.0} -->

The [UAstack] takes a multi-layered approach to safety, illustrated in Figure 6. Conventional modern safe navigation and collision avoidance are based on the planning of paths subject to map constraints, which are then blindly followed by an onboard controller. Despite the major success of this paradigm in many environments and mission profiles, as discussed in Jacquet et al.; Kulkarni and Alexis and demonstrated in field experience Ebadi et al. it represents a single point of failure which can lead robots to collisions due to odometry errors or erroneous/incomplete mapping. Although such errors are not common, experience shows that they do manifest and are often catastrophic, at least regarding a robot's ability to continue its mission. Furthermore, odometry and mapping challenges manifest more frequently in perceptually-degraded and geometrically complex environments Ebadi et al.. While the [UAstack] does perform map-based avoidance through volumetric mapping for collisions and traversability analysis for ground systems, it further adds two redundant layers of safety: depth sensor-based trajectory tracking and a last-resort safety filtering based on Control Barrier Functions.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Navigation Module", "weight": 1.0} -->

With respect to depth sensor-driven navigation policies, two approaches are offered within the stack, owing to their distinct benefits in certain conditions: (i) a Signed Distance Function ([SDF])-based neural [NMPC] Jacquet et al. or (ii) a novel [DRL]-based policy trained for safe navigation and smooth collision avoidance. These methods enable local deviations from the reference trajectory if and when necessary, to ensure collision avoidance. Both methods provide swappable local navigation policies with distinct performance characteristics that will be discussed in Section 3.4.4. To further assert safety with formal guarantees, a composite [CBF]-based formulation building upon Harms et al. is introduced as a last-resort safety filter allowing to modify the control references in the unlikely situation that all other collision-avoidance methods in the stack fail. Importantly, this additional safety layer within the [UAstack] is currently implemented for obstacle avoidance and not for traversability analysis, predominantly targeting flying robots.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Navigation Module", "weight": 1.0} -->

This architecture extends upon recent ideas and developments in the research community, such as the perceptive locomotion in Miki et al., which indeed may also be used as an alternative to the exteroceptive depth navigation strategies discussed below when it comes to quadruped robots.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Neural SDF-NMPC", "weight": 1.0} -->

Detailed in Jacquet et al., the [SDF-NMPC] enables collision-free navigation in unknown environments relying only on depth sensing and (possibly drifting) odometry. In its current implementation, it emphasizes rotorcraft navigation.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Neural SDF-NMPC", "weight": 1.0} -->

The [SDF-NMPC] represents the visible environment as a Euclidean [SDF], defined to be positive in visible free space and negative in occluded regions (i.e., behind obstacles). For efficient computation and to provide a representation compatible with gradient-based [NMPC], this [SDF] is approximated by a neural network, online, from the latest depth measurement. As a result, the environment is described purely locally, improving robustness to potentially drifting odometry. To keep the representation compatible with a compact neural model, the [SDF] is saturated beyond a threshold $T_{\text{SDF}}$. This [SDF] is constructed online from the latest depth measurement. As a result, the environment is described purely locally, improving robustness to potentially drifting odometry.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Neural SDF-NMPC", "weight": 1.0} -->

A two-stage neural network is used. First, the input depth image is clamped at a distance $d_{\text{max}}$, since only short-range surroundings are relevant for short-horizon collision avoidance. Compression into a low-dimensional latent space $\mathbf{z}$ is achieved via a convolutional encoder, trained jointly with a decoder to reconstruct the input, ensuring that $\mathbf{z}$ captures a reliable latent representation of the depth data. Notably, the encoding is biased to place greater emphasis on obstacles close to the robot, encouraging accurate encoding of nearby geometry. The decoder is used only during training, while the encoder provides input to a downstream Multi-Layer Perceptron ([MLP]) network that reconstructs the [SDF].

<!-- chunk {"id": "body-0069", "role": "body", "section": "Neural SDF-NMPC", "weight": 1.0} -->

Specifically, this [MLP] takes as input the latent vector and a $3$D position, and approximates the corresponding [SDF] value evaluated in that point. The regression task is trained in a supervised manner, including losses that enforce consistency of the [SDF] gradient. In this way, the trained [MLP] represents the following parametric function: where $\bm{\theta}$ are the neural network weights, and $\mathbf{z}$ is the latent code corresponding to the depth measurement.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Neural SDF-NMPC", "weight": 1.0} -->

Finally, the neural [SDF] is embedded into the nonlinear [NMPC] controller as an explicit position constraint. The following constraint is enforced over the receding horizon: where $r$ is a user-defined threshold accounting for the robot radius and a possible safety margin, and $\bm{p}_{\mathtt{S}}^{\mathtt{B}}$ denotes the position of the robot expressed in the frame $\{\mathtt{S}\}$ in which the depth measurement was captured. Note that additional constraints further ensure that the robot remains within the sensor frustum, i.e., within the region that is currently observable and where the neural [SDF] is defined. This follows the intuitive principle of "look where you move", effectively restricting motion to visible free space.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Neural SDF-NMPC", "weight": 1.0} -->

Critically, the method enforces feasibility and stability-type criteria (under fixed sensor observations), with a terminal condition ensuring that the terminal state allows a collision-free braking maneuver to hover. This is assessed by computing the minimum braking distance given the input bounds, and evaluating the [SDF] at the predicted hovering position. Under this condition, recursive feasibility is ensured, and with a suitable quadratic terminal cost, the optimal value is shown to be non-increasing over time. The [NMPC] generates acceleration commands from a velocity reference trajectory, since velocity tracking prevents the accumulation of position errors when collision constraints prevent accurate tracking of a nominal trajectory. Accordingly, the interface with the planning module provides such velocity references derived from planned paths.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Exteroceptive Deep Reinforcement Learning", "weight": 1.0} -->

The [UAstack] further offers exteroceptive [DRL]-based navigation (dubbed [ExRL]). The proposed novel Exteroceptive DRL ([ExRL]) approach is formulated as a waypoint navigation problem and considers as input the vector to goal location, the robot orientation, velocity, and angular rates alongside the instantaneous depth image from an exteroceptive sensor (including stereo or RGB-D cameras, Time-of-Flight camera sensors, or LiDARs). We employ end-to-end learning to train a navigation policy to generate commands directly from the robot's current state and range measurement. The policy is trained using the Aerial Gym Simulator Kulkarni et al. to command acceleration and yaw-rate setpoint commands (as commonly provided by most autopilots such as PX4 Meier et al. and ArduPilot ArduPilot Dev Team ). Relevant open-source examples for training are provided in Aerial Gym, while the policy can be trained on any compatible simulation tool. Similar to the [SDF-NMPC], [ExRL] ensures safe collision-free navigation without a map and thus contributes to multi-layered safety.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Exteroceptive Deep Reinforcement Learning", "weight": 1.0} -->

This work is distinct from prior work of the authors in Kulkarni et al.; Kulkarni and Alexis, by a) departing from a modularized two-step approach and introducing an end-to-end methodology, b) introducing a novel reward function incorporating Time-to-Collision ([TTC]), and c) commanding acceleration and yaw-rate setpoints instead of velocity references.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Observations", "weight": 1.0} -->

The observation vector for training the policy consists of both proprioceptive and exteroceptive components. The proprioceptive components are expressed in a yaw-aligned, roll and pitch stabilized coordinate frame $\{\mathtt{V}\}$ sharing the same origin as the robot body IMU frame $\{\mathtt{B}\}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Observations", "weight": 1.0} -->

During training, the goal direction $\bm{\delta}_{\mathtt{}}^{\mathtt{V}}/{\delta}$, roll $\phi$ and pitch $\theta$ measurements are perturbed by adding noise sampled from a uniform distribution before populating the observation tensor. The linear $\bm{v}_{\mathtt{WB}}^{\mathtt{B}}$ and angular velocities $\bm{\omega}_{\mathtt{WB}}^{\mathtt{B}}$ are not perturbed. The range measurements from the exteroceptive sensor are min-pooled to $16\times 20$ pixels and inverted as a $2$D inverse range-image $\mathbf{I_{r}}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Observations", "weight": 1.0} -->

Yaw error (rad/) Angular velocity in {B} (rad/s) Previous setpoint (m/s2, rad/s) Table 2: Observation vector ot ∈ ℝ337.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Time-to-Collision ([TTC])", "weight": 1.0} -->

We propose the usage of an expected "time-to-collision" metric at each timestep that provides a dense reward signal to the robot. This metric is distinct compared to approaches that directly reward based on raw range data Kulkarni and Alexis, thus prioritizing the relationship between velocity and distance to measured obstacles, only penalizing rapid approaches to obstacles. This metric is calculated only in simulation and is treated as privileged information that is not available to the policy, yet influences the reward signal. For each point $i$ in the full-resolution point cloud expressed in a sensor frame $\{\mathtt{S}\}$, the vector from the sensor is calculated as ${\bm{r}_{\mathtt{}}^{\mathtt{S}}}_{i}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Time-to-Collision ([TTC])", "weight": 1.0} -->

The linear component of velocity of the robot along the direction to each point is computed as the projection of $\bm{v}_{\mathtt{WB}}^{\mathtt{S}}$ onto the unit direction vector of ${\bm{r}_{\mathtt{}}^{\mathtt{S}}}_{i}$. This is subsequently used to calculate the expected time to collision $\tau_{i}$ using the distance of the point from the robot: Positive time-to-collision values are clamped between $0\text{\,}\mathrm{s}\text{/}$ and $10\text{\,}\mathrm{s}\text{/}$. Negative values indicate that the robot is moving away from an obstacle, hence they are set to $10\text{\,}\mathrm{s}\text{/}$ to make their effect negligible.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Time-to-Collision ([TTC])", "weight": 1.0} -->

The minimum time-to-collision $\tau_{min}=\min_{i}\tau_{i}$ across all points is considered and used to penalize the robot, emphasizing imminent collisions while largely ignoring well-separated obstacles.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Policy Architecture", "weight": 1.0} -->

The observation vector $\bm{o}_{t}$ is partitioned into a proprioceptive and an exteroceptive component, as detailed in Table 2. The latter is treated as a single-channel $2$D image and processed by a Convolutional Neural Network ([CNN])-based encoder $f_{\text{CNN}}$ with three convolutional blocks. Each block consists of a $3\times 3$ convolution with padding of width $1$, an Exponential Linear Unit ([ELU]) activation, and a $3\times 3$ max-pooling layer. The resulting feature map is flattened into a 128-dimensional range embedding, which is concatenated with the proprioceptive state vector. This combined representation is then passed through an MLP with hidden layer sizes $$ and ELU activations, followed by a 128-dimensional Gated Recurrent Unit ([GRU]) layer. The policy is trained using Proximal Policy Optimization ([PPO]) Schulman et al. implementation provided by Sample Factory Petrenko et al..

<!-- chunk {"id": "body-0081", "role": "body", "section": "Policy Architecture", "weight": 1.0} -->

The training time is about $60\text{\,}\mathrm{min}\text{/}$ on a consumer grade laptop with an NVIDIA RTX 3080 Ti GPU.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Environment Setup and Curriculum", "weight": 1.0} -->

Each simulated environment is composed of a rectangular room with dimensions ranging from $10\times 10\times 6$ to $15\times 15\times 10$ m. A simulated robot is initialized on one side of the environment while the goal position is sampled on the opposite side with an arbitrary yaw setpoint. The acceleration and yaw-rate setpoint is tracked using a controller derived from the work in Lee et al.), whose parameters are randomized at each episode to increase robustness and improve sim2real performance. Within each environment, 25 to 70 cuboidal obstacles of various sizes are sampled. An episode is marked as a success if the robot reaches within $1\text{\,}\mathrm{m}\text{/}$ of the goal after a predefined number of time steps. If the robot remains collision-free but does not reach the goal, the episode is marked as a timeout. Collisions with obstacles are detected by the physics engine, terminate the episode, and are recorded as crashes. To encourage stable learning across various environment complexities, a curriculum adjusts the number of obstacles $n_{\textrm{obs}}$ in each environment.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Environment Setup and Curriculum", "weight": 1.0} -->

The number is increased or decreased when the average success rate $\zeta_{s}$ over $2048$ episodes crosses the upper or lower thresholds, $\zeta_{s}^{+}=0.70$ and $\zeta_{s}^{-}=0.60$, respectively: The normalized progress fraction $\wp=(n_{\textrm{obs}}-25)/(70-25)$ is calculated and used to scale all non-terminal reward terms by $K(\wp)=1+2\wp\in$, amplifying training signal as task difficulty increases.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Reward Function", "weight": 1.0} -->

The reward function is designed to encourage the robot to navigate efficiently to the goal while maintaining safe separation from obstacles and smooth control behavior. It contains three groups of terms: (i) goal-directed terms that reward proximity and velocity alignment toward the goal, (ii) stabilization terms that encourage low velocity, correct heading, and low angular rate when in the vicinity of the goal, and (iii) penalty terms that discourage excessive speed, large control increments, and proximity to obstacles as captured by the [TTC] metric.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Reward Function", "weight": 1.0} -->

Let the speed $v=\rVert\bm{v}_{\mathtt{WB}}^{\mathtt{B}}\lVert$, $\bm{u}_{t-1}^{acc}\in\mathbb{R}^{4}$ the previous command; $\tau_{min}\in\,\mathrm{s}$ the minimum time-to-collision across all rays; and $\wp\in$ the curriculum progress fraction. Two kernel functions compose all reward and penalty terms: The following intermediate quantities are defined for compactness and summarized in Table 3, while all reward terms are presented in Table 4.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Composite CBF-based Safety Filter", "weight": 1.0} -->

Beyond the aforementioned navigation approaches --which combine map-based safety of the planning module with reactive collision avoidance control-- the [UAstack] further provides a last-resort safety filter. The rationale for adding this final layer is twofold. On the one hand, both the Neural NMPC through Signed Distance Field Encoding for Collision Avoidance ([SDF-NMPC]) and the [DRL] navigation strategies involve deep neural network processing, which, despite training to consider noise and other imperfections, is treated as a source of possible (albeit unlikely) error. On the other hand, using fundamentally different collision-checking at different spatiotemporal scales --spanning map-based planning, the navigation strategies, and the safety filter-- offers resourcefulness. It thus reflects a conservative but meaningful choice to safeguard the robot from a collision which represents one of the most problematic events during a mission.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Composite CBF-based Safety Filter", "weight": 1.0} -->

Based on Composite Control Barrier Functions formalism for safe navigation Harms et al., we compose a [C-CBF] directly from recent range measurements as in Misyats et al. to modify the acceleration setpoint when an unexpected impending collision is detected. It is a key module to fully and formally safeguard autonomous robots. The [C-CBF] is described hereafter considering the case of a flying robot. First, the system model is approximated to be of degree $2$ and takes the form: For a rotorcraft such as a multirotor aerial robot, we here use the simplified linear system model where $\bm{a}_{\mathtt{WB}}^{\mathtt{W}}$ is the linear acceleration. Here $f(\bm{x}_{\mathtt{}}^{\mathtt{}})$ and $g(\bm{x}_{\mathtt{}}^{\mathtt{}})\bm{u}_{\mathtt{}}^{\mathtt{}}$ denote the state system dynamics vectors.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Composite CBF-based Safety Filter", "weight": 1.0} -->

This is then associated with equivalent scalar "distance-squared" functions $\mathbf{\nu}_{i,0}(\bm{x}_{\mathtt{}}^{\mathtt{}}):=\|\bm{p}_{\mathtt{WB}}^{\mathtt{W}}-\bm{p}_{\mathtt{WO}_{i}}^{\mathtt{W}}\|^{2}-\varepsilon^{2}$ with the safety for obstacle $i$ being $\mathbf{\nu}_{i,0}\geq 0$. Note that there is no dependence on any consistent world frame as only the relative distances are used in the construction.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Composite CBF-based Safety Filter", "weight": 1.0} -->

Subsequently, we define higher-order CBF (HO-CBF) functions as: where $\mathfrak{L}_{f}$ is the Lie derivative along the drift dynamics and $\varsigma$ is a tunable class $\mathcal{K}_{\infty}$ function of the form The used function $\varsigma$ with parameters $\lambda>0,\sigma>0,p>0$ is displayed in Fig. 7. For $p<1$ the tuneable parameters allow for a more rapid convergence behavior than a for $p=1$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Composite CBF-based Safety Filter", "weight": 1.0} -->

We formulate the [C-CBF] as Figure 7: Visualization of the used kappa function with nominal values λ = 1, p = 0.5, σ = 1. with saturation parameter $\gamma$ and temperature parameter $\kappa$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Composite CBF-based Safety Filter", "weight": 1.0} -->

0}}\frac{\rho(y)}{y}$ in the low-level controllers.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Composite CBF-based Safety Filter", "weight": 1.0} -->

This scheme can thus be used to certify collision-free navigation in spite of imperfect tracking. We enforce the condition for a nominal input $\bm{u}_{\mathtt{\textrm{sp}}}^{\mathtt{}}$ by means of a reactive safety filter Quadratic Programming ([QP]) of the form For the case of one single constraint, an analytical solution to can be computed Alan et al. as This computationally cheap and flexible scheme to reactively enforce collision avoidance of any higher level control policy. To further reduce chattering of the safety filter, we further apply Exponential Moving Average ([EMA]) filtering to the output.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

A set of evaluation studies are conducted using a simulated quadrotor with mass $2.10\text{\,}\mathrm{kg}\text{/}$ and dimensions $0.3\times 0.3\times 0.1$\mathrm{m}\text{/}$$ in Gazebo Koenig and Howard. The robot is equipped with an acceleration and yaw-rate tracking controller and a hemispherical dome LiDAR sensor modeled after the RoboSense Airy ([FoV] $180\text{\,}\mathrm{\SIUnitSymbolDegree}\text{/}$$\times$$90\text{\,}\mathrm{\SIUnitSymbolDegree}\text{/}$).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

The performance of the [ExRL] and the [SDF-NMPC] methods is compared both with and without the [C-CBF]-based safety filter, across environments of varying density, and under different levels of command mismatch induced by an independent first-order low-pass filter with time constant $\tau_{d}$ on each acceleration and yaw-rate command dimension. The slower dynamics introduced by the low-pass filter serve to practically emulate the effects of the closed-loop attitude response of the system, which presents non-instantaneous reference tracking and at times imperfect disturbance rejection. This is of particular interest especially as the actual time constant of the attitude subsystem differs between robots and delayed response poses a challenge to navigation in tight spaces. This allows us to characterize the failure modes of the navigation policies induced by increasingly disturbed system behavior.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Test environments, illustrated in Figure LABEL:fig:world-densities, are procedurally generated as rectangular corridors of width and height $8\text{\,}\mathrm{m}\text{/}$ each, populated with spherical obstacles of $1\text{\,}\mathrm{m}\text{/}$ diameter placed using Poisson-disc sampling, guaranteeing a parametric minimum separation $r_{\textrm{sep}}\in\{1.5,1.8,2.0,2.5,3.0\}$ m between obstacle centers, i.e., surface-to-surface gaps of $\{0.5,0.8,1.0,1.5,2.0\}$ m. The corridor is bounded above, below and on the sides by walls, leaving the longitudinal direction open for traversal. The robot is initialized at the start of the corridor and tasked with following a path through the corridor to the other side.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

For each environment, and for each value of the low-pass time constant $\tau_{d}$, $20$ independent runs are performed with each of the four configurations and the outcomes are visualized in Figure LABEL:fig:ablations-combined. Every run terminates in one of three mutually exclusive states: success, in which the robot reaches the goal; stagnation, in which the robot halts before the goal but remains collision-free; or crash, in which a collision with the environment is detected. The figure reports the rate of each outcome as a function of $r_{\textrm{sep}}$, with rows corresponding to the three outcome categories and columns to the four values of $\tau_{d}$. Smaller $r_{\textrm{sep}}$ values correspond to denser, more constrained environments, while larger $\tau_{d}$ values correspond to a more severe command mismatch. Solid lines indicate the [C-CBF]-filtered configurations and dashed lines the baselines without this last-resort filter, with colour distinguishing the upstream policy ([ExRL] in blue, [SDF-NMPC] in green).

<!-- chunk {"id": "body-0097", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Each marker aggregates the $20$ runs for the corresponding combination of parameters.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Two sets of comparisons are performed. Among the values of $\tau_{d}$ tested, $\tau_{d}\leq$0.10\text{\,}\mathrm{s}\text{/}$$ corresponds to the realistic operating regime that the studies are intended to characterize; $\tau_{d}=$0.25\text{\,}\mathrm{s}\text{/}$$ is included as a deliberate stress test, beyond realistic deployment conditions, in order to probe the limits of each configuration and expose the regime in which the safety ceases to hold. Because both success and stagnation outcomes correspond to collision-free behaviour, the crash rate is treated as the primary safety metric throughout, while the success rate is reported as a secondary but important measure of task completion.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

The first comparison contrasts the two unfiltered baselines, [ExRL] only and [SDF-NMPC] only, which differ markedly in how they degrade under increasing $\tau_{d}$. At $\tau_{d}=0$ both reach the goal on $80$--$100\text{\,}\mathrm{\char 37\relax}\text{/}$ of runs across all densities, with the [ExRL] policy crashing on $5\text{\,}\mathrm{\char 37\relax}\text{/}$ of the densest layouts and [SDF-NMPC] on $10\text{\,}\mathrm{\char 37\relax}\text{/}$. As $\tau_{d}$ grows, the two baselines diverge sharply. [SDF-NMPC] degrades gracefully and primarily along the density axis $r_{\textrm{sep}}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

[ExRL], in contrast, degrades globally: at the same $\tau_{d}$ it crashes on $85$--$100\text{\,}\mathrm{\char 37\relax}\text{/}$ of runs across the three densest settings and even at $r_{\textrm{sep}}=$3.0\text{\,}\mathrm{m}\text{/}$$ retains only $65\text{\,}\mathrm{\char 37\relax}\text{/}$ success. This asymmetry may reflect [SDF-NMPC]'s robustness against the induced mismatch, while the learned policy's reliance on a specific dynamics model employed during training and the subsequent degradation wherever it departs from that model.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

The second comparison contrasts each baseline against its [C-CBF]-augmented counterpart. At $\tau_{d}=0$, the safety filter eliminates collisions entirely and converts results into stagnations rather than goal completions, preserving safety at the cost of task completion. The filter's protective effect persists across the realistic regime. At $\tau_{d}=$0.10\text{\,}\mathrm{s}\text{/}$$, [SDF-NMPC]+[C-CBF] crashes on at most $20\text{\,}\mathrm{\char 37\relax}\text{/}$ of runs in any environment, always lower than [SDF-NMPC] alone, and [ExRL]+[C-CBF] crashes on $10$--$85\text{\,}\mathrm{\char 37\relax}\text{/}$ in the dense band, again lower than [ExRL] alone. This indicates a substantial reduction in crash rate with the inclusion of the [C-CBF].

<!-- chunk {"id": "body-0102", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Under the unrealistic $\tau_{d}=$0.25\text{\,}\mathrm{s}\text{/}$$ conditions, the filter loses authority in the densest environments and both augmented pipelines crash on $85$--$100\text{\,}\mathrm{\char 37\relax}\text{/}$ of runs at $r_{\textrm{sep}}=$1.5\text{\,}\mathrm{m}\text{/}$$, locating the failure boundary that the test is designed to expose. The augmented versions inherit the characteristics of their upstream policy: [ExRL]+[C-CBF] crashes earlier and across a wider density range than [SDF-NMPC]+[C-CBF] at every $\tau_{d}>0$, indicating that the [C-CBF] compensates for command distortion but not for the upstream policy's own degradation under that distortion. This analysis shows that imperfect control can occur in demanding environments and conditions, highlighting the need for navigation strategies with multiple layers of safety checking and avoidance.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

The [UAstack] offers a configurable methodological plurality to support demanding deployments.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Exteroceptive Overwrite", "weight": 1.0} -->

When the map-based safety of planning module or the specific exteroceptive navigation methods are not desirable, or compatible, a given robot, the [UAstack] allows the use of a conventional state-feedback controller. Examples include the Linear MPC methods in Greeff and Schoellig; Kamel et al., the underlying MPC in [SDF-NMPC] with disabled collision constraints, or a solution for any other particular robot or through existing autopilot (e.g., PX4).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Low-level Interfaces", "weight": 1.0} -->

The [UAstack] interfaces diverse aerial and ground robots as follows.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Aerial Robots - Full Stack", "weight": 1.0} -->

When the full stack with multi-layered safety is considered for flying systems, we command acceleration setpoints directly to compatible autopilots and low-level controllers such as PX4- and ArduPilot-based flight controllers.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Aerial Robots - Without Multi-layered Safety", "weight": 1.0} -->

If the multi-layered safe navigation is not necessary for flying systems, we provide options for commanding waypoints or 3D accelerations to existing controllers. Waypoints are straightforward for all systems that offer such control. However, this does not deliver the full stack functionality and collision avoidance is ensured only at the map/planning level.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Ground Robots", "weight": 1.0} -->

For legged systems and other ground robots, we interface the planning module with a custom PID tracking controller to output velocity commands to follow the path given by the planning module. Velocity-setpoint commands are provided to the platforms for them to track. Those velocity references may be passed through other safety-mechanisms in case those are provided onboard the platforms.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Ground Robots", "weight": 1.0} -->

Direct support for widely-adopted low-level control or autopilot interfaces is available out-of-the-box through MAVROS, or more broadly through the ROS framework. As the stack is structured in a Dockerized format, we support both ROS 1 and ROS 2-based robots out of the box.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Ground Robots", "weight": 1.0} -->

Thin obstacles and cluttered Thin obstacles and cluttered Narrow and multiple branches Narrow, varying size, and multiple branches Which modules of the UAstack were used, including SLAM (denoted by S, with a subscript denoting the configuration used in autonomous missions, where L: LiDAR, R: Radar, I: IMU), VLM (denoted by V), Planning (denoted by P, while PE refers to exploration and PI to inspection), ExRL (denoted by R), SDF-NMPC (denoted by NS), SDF-NMPC without SDF constraints (denoted by NU), and C-CBF (denoted by C).

<!-- chunk {"id": "body-0111", "role": "body", "section": "Evaluation Studies", "weight": 1.0} -->

To validate the [UAstack], a comprehensive set of evaluation studies was conducted including (a) evaluation of the performance, accuracy and overall resilience of the perception module in diverse environments and conditions, (b) evaluation of the performance and safety-inducing behaviors of the navigation module, as well as (c) full-stack results requiring the orchestrated operation of the perception, planning and navigation modules. Studies were conducted using both aerial and ground robots, alongside some handheld experiments (as part of the evaluation regime of the perception module). An overview of these experiments is shown in Table˜5 and key parameters are listed in Table˜6. All presented field experiments are included in the video files of the submission and can be found at $\mathrm{\SIUnitSymbolDegree}\text{/}$ Map update thresholds $\mathrm{\SIUnitSymbolDegree}\text{/}$ $\mathrm{\SIUnitSymbolDegree}\text{/}$ $\mathrm{\SIUnitSymbolDegree}\text{/}$ Unitless quantities denoted by –.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Verified Robot Morphologies", "weight": 1.0} -->

In this paper, we evaluate the [UAstack] on two multirotor robot configurations and a legged robot. In all robot missions, the [UAstack] runs fully onboard in real-time, with module configurations as detailed in Table 5. The released open-source code involves simulation examples with additional morphologies such as ground rovers and helicopters. Verifying on diverse robots -- while further expanding the morphologies we support -- is aligned with our strategic goal to provide a generalist autonomy stack across broad morphological categories.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Aerial Robot 1 ([AR-1])", "weight": 1.0} -->

The first aerial robot, referred to as [AR-1], is an improved version of the RMF-Owl Petris et al..

<!-- chunk {"id": "body-0114", "role": "body", "section": "Aerial Robot 1 ([AR-1])", "weight": 1.0} -->

[AR-1] integrates a Khadas Vim4 computer and a sensing suite comprising of an Ouster OS0-128 LiDAR ($10\text{\,}\mathrm{Hz}\text{/}$), a Flir Blackfly S 0.4 MP color camera ($20\text{\,}\mathrm{Hz}\text{/}$ normally, $25\text{\,}\mathrm{Hz}\text{/}$ in Fyllingsdal), a Texas Instruments $\mathrm{mm}\text{/}$Wave IWR6843AOP radar sensor ($10\text{\,}\mathrm{Hz}\text{/}$ normally, $25\text{\,}\mathrm{Hz}\text{/}$ in Fyllingsdal), and a VectorNav VN-100 [IMU] ($200\text{\,}\mathrm{Hz}\text{/}$). The sensors and the onboard computer are time synchronized using a separate microcontroller as described in Nissov et al..

<!-- chunk {"id": "body-0115", "role": "body", "section": "Aerial Robot 2 ([AR-2])", "weight": 1.0} -->

[AR-2] is a collision-tolerant quadrotor designed for autonomous operation in [GNSS]-denied confined environments. [AR-2] features a lightweight protective frame made from carbon-foam sandwich measuring approximately \\qtyproduct0.52x0.52x0.24 (L $\times$ W $\times$ H), weighing $2.3\text{\,}\mathrm{kg}\text{/}$. The robot carries the UniPilot Kulkarni et al. sensing and computing payload on which the entire [UAstack] runs onboard.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Aerial Robot 2 ([AR-2])", "weight": 1.0} -->

The module features an NVIDIA Jetson Orin NX as the compute module and a multi-modal sensing suite including a RoboSense Airy dome LiDAR ($10\text{\,}\mathrm{Hz}\text{/}$), $3\times$ MIPI Vision Components IMX296 color cameras ($20\text{\,}\mathrm{Hz}\text{/}$), a D3 Embedded RS-6843AOPU [FMCW] radar ($10\text{\,}\mathrm{Hz}\text{/}$), and a VectorNav VN-100 [IMU] ($200\text{\,}\mathrm{Hz}\text{/}$). The onboard sensors are time-synchronized following the work in Kulkarni et al. [AR-2] further integrates a Pixracer Pro PX4-based flight control to track the acceleration commands given by the [UAstack].

<!-- chunk {"id": "body-0117", "role": "body", "section": "Ground Robot 1 ([GR-1])", "weight": 1.0} -->

On the ground, the [UAstack] is evaluated using the ANYmal D legged robot -- hereafter referred to as [GR-1] -- with dimensions of \\qtyproduct0.93x0.53x0.80 (L $\times$ W $\times$ H), and a mass of $50\text{\,}\mathrm{kg}\text{/}$. The stock standard robot features a Velodyne VLP-16 LiDAR and $6\times$ depth cameras for sensing and two 8th-generation Intel Core i7 CPUs (6 cores each) for compute. However, [GR-1] is also equipped with the UniPilot module which runs the [UAstack] for all evaluations. This UniPilot carries the same sensing payload as in the [AR-2] platform and is interfaced with the onboard Intel computers which then run the locomotion and velocity tracking controllers. All the stack runs on the onboard UniPilot, considering the data of this module.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Perception Module Evaluation", "weight": 1.0} -->

We first evaluate the performance and resilience of the stack's perception module, focused around its multi-modal [SLAM] functionalities. We subsequently evaluate downstream functionalities for [VLM]-based scene reasoning.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Perception Module Evaluation", "weight": 1.0} -->

ATE [m/] / [$\mathrm{\char 37\relax}\text{/}$] $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$

<!-- chunk {"id": "body-0120", "role": "body", "section": "Perception Module Evaluation", "weight": 1.0} -->

$\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$

<!-- chunk {"id": "body-0121", "role": "body", "section": "Perception Module Evaluation", "weight": 1.0} -->

$\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$

<!-- chunk {"id": "body-0122", "role": "body", "section": "Perception Module Evaluation", "weight": 1.0} -->

$\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ $\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\times$ Method failure due to ATE > 5% is indicated by × and due to inability to generalize to sensor configuration (radar being at 25Hz) is indicated by −. For verifiability and reproducibility, the full implementation and the dataset involved in these studies are openly released.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Multi-Modal SLAM", "weight": 1.0} -->

To evaluate the multi-modal [SLAM] solution, we assess its accuracy and robustness in perceptually-degraded conditions. Considering a set of diverse environments, specifically a bicycle tunnel (Fyllingsdal), a road tunnel (Runehamar), a frozen lake, and the [NTNU] main campus, we present a modality-wise ablation as well as comparisons against state-of-the-art methods. The goal of this evaluation is to demonstrate the flexibility of the proposed [SLAM] system, as well as the comparative advantages of the multi-modal fusion. These experiments are collected with ground truth, such that the estimation performance can be evaluated quantitatively. The same [SLAM] system runs online to support the autonomous missions conducted in all the other experiments. For these autonomous missions, the [SLAM] module is operating in the Ours - LRI (fusing LiDAR, radar, [IMU]) configuration, except when noted otherwise (see Table˜5), as this has been found to be most robust across diverse environments and conditions.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Multi-Modal SLAM", "weight": 1.0} -->

The results of the evaluation are presented in Table 7. The table compares and ablates our multi-modal solution against state-of-the-art LiDAR-Inertial (FAST-LIO2 Xu et al. ), Visual-Inertial (ROVIO Bloesch et al. and OpenVINS Geneva et al. ), LiDAR-Visual-Inertial (FAST-LIVO2 Zheng et al. ), and LiDAR-Radar-Inertial (GaRLIO Noh et al. and AF-RLIO Qian et al. ) works. GaRLIO and AF-RLIO are selected as a representative set of state-of-the-art methods for LiDAR-radar-inertial fusion which are both: likely to work with the small form-factor sensors considered in this work and with open-source implementations. The different permutations of our MIMOSA-X multi-modal [SLAM] (LiDAR (L), Radar (R), Vision (V), and Inertial (I)) are noted in the table as Ours - XXXI.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Multi-Modal SLAM", "weight": 1.0} -->

As the [IMU] is an integral component of our method, permutations without [IMU] are omitted. The key parameters used in the evaluation of the [SLAM] module are reported in Table˜6. Note that all parameters are fixed across all tests, with the sole exception of the LiDAR point standard deviation (which is increased in the frozen lake environment), the [IMU] bias noise densities (decreased in the frozen lake environment), and the D-Optimality threshold for the vision fusion (which is different between environments with and without fog). In turn, the latter is one of the reasons that the robot experiments presented subsequently predominantly rely on the LRI solution. The table reports the Absolute Trajectory Error ([ATE]) (in $\text{\,}\mathrm{m}\text{/}$) and Relative Trajectory Error ([RTE~10~]) (in %), with $10\text{\,}\mathrm{m}\text{/}$ segment length, following Grupp, calculated against the ground truth estimates.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Multi-Modal SLAM", "weight": 1.0} -->

The ground truth for the tunnel trajectories (Fyllingsdal and Runehamar) is generated by fusing the tracking of a Leica GRZ101 mini-prism mounted on [AR-1] by a Leica MultiStation with the onboard [IMU] in an offline Levenberg--Marquardt ([LM]) optimization. In the campus and frozen lake datasets, where [GNSS] is available, ground truth is created using Pix4DMatic for a [GNSS]-augmented visual bundle adjustment optimization.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Multi-Modal SLAM", "weight": 1.0} -->

The [SLAM] datasets were collected with (a) [AR-1] aerial robot and (b) a helmet-mounted modified version of the UniPilot Kulkarni et al. module integrating a Hesai JT-128 LiDAR ($10\text{\,}\mathrm{Hz}\text{/}$), replacing the Robosense Airy, and a uRAD Industrial radar ($10\text{\,}\mathrm{Hz}\text{/}$), replacing the 3D Embedded RS-6843AOPU radar (both of which integrate the Texas Instruments IWR6843AOP chip). The full datasets including raw data and ground-truth are released to facilitate comparison and reproducibility.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Fyllingsdal Tunnel", "weight": 1.0} -->

The [AR-1] aerial robot was manually piloted at an average speed of $6.82\text{\,}\mathrm{m}\text{/}\mathrm{s}$ (max speed $9.2\text{\,}\mathrm{m}\text{/}\mathrm{s}$) in a $\sim 650\text{\,}\mathrm{m}\text{/}$ section of the Fyllingsdal bicycle tunnel. The tunnel is composed primarily of long geometrically self-similar sections with sparse geometrically dissimilar rest areas. Ground truth for this environment is generated using the Leica-IMU fusion described above. Notably, the chirp configuration for the radar in this experiment is changed for better performance at high speeds. This results in a greater maximum Doppler as well as an increased measurement rate of $25\text{\,}\mathrm{Hz}\text{/}$. GaRLIO could not be evaluated on this sequence as the implementation requires the radar and LiDAR to be at the same rate.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Fyllingsdal Tunnel", "weight": 1.0} -->

Due to the geometric self-similarity affecting the LiDAR optimization, FAST-LIO2 as well as Ours - LI failed. AF-RLIO fails similarly, due to the method relying on radar-based scan registration during periods of LiDAR degeneracy, which the small form-factor radar sensor used on the aerial platform is not well-suited. The radar-inertial ablation (Ours - RI), while able to function, has a significant vertical and yaw drift due to the nature of the sensor. Furthermore, the high speeds created difficulties for vision-based methods, resulting in significant performance deterioration for ROVIO. As a result, Ours - VI fails, and Ours - RVI does not see large performance improvements over Ours - RI. OpenVINS performed better than ROVIO, Ours - VI, Ours - RVI, and Ours - LVI, however still not as well as the nominal multi-modal configuration Ours - LRI and Ours - LRVI.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Fyllingsdal Tunnel", "weight": 1.0} -->

The proposed method, by fusing the multiple exteroceptive modalities, demonstrates performance robust both to the challenging conditions, but also to the asynchronous measurements, leading to the improved results of Ours - LRI, and Ours - LRVI. Similarly, FAST-LIVO2 is able to leverage the vision information to outperform most of the other methods, achieving performance similar to, but slightly worse than, Ours - LRI and Ours - LRVI. The estimated trajectories, ground truth and the accumulated LiDAR point cloud map from the Ours - LRI configuration is visualized in Figure˜9.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Runehamar Tunnel", "weight": 1.0} -->

The [AR-1] aerial robot was manually flown through a section of the Runehamar tunnel, for a total trajectory length of $\sim 1.4\text{\,}\mathrm{km}\text{/}$. Ground truth for this environment is generated using the Leica-[IMU] method described above. The tunnel has a rough interior, which allows for LiDAR-based methods (FAST-LIO2 and Ours - LI) to function well despite the otherwise minor geometric self-similarity. However, regions of the tunnel are not illuminated. Despite the aerial platform carrying onboard lighting, the scale of the environment is such that the images captured by the camera are dark and hence challenging for visual-based methods, leading to very poor performance from ROVIO (and hence Ours - VI). OpenVINS, by doing a histogram equalization of the image is able to better extract features from the darkest regions and as a result, demonstrates improved performance over ROVIO, however, still worse than the LiDAR-based fusions. Impacted by the poor visual measurement quality, FAST-LIVO2 performs slightly worse than FAST-LIO2.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Runehamar Tunnel", "weight": 1.0} -->

Radar measurement quality in this environment was also quite poor, in part due to the speed of the trajectory and in part due to low number of reflections. As a result Ours - RI, Ours - RVI, and the baseline radar-fusion methods (GaRLIO and AF-RLIO) do not perform well either. However, in combination with the LiDAR (in Ours - LVI, Ours - LRI, or Ours - LRVI) the proposed multi-modal fusion demonstrates robust performance. Some of the aforementioned results are visualized in Figure˜9, alongside the previous tunnel experiment. Note here the sparsity of the instantaneous radar point cloud in this particular environment.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Frozen Lake", "weight": 1.0} -->

The [AR-1] aerial robot was manually piloted on top of a frozen lake, starting from close to a bank, flying out into the middle, and returning close to the starting location. The ground truth was generated using the Pix4DMatic bundle adjustment result. Once the robot has traveled further than the range of the LiDAR away from any bank of the lake, the point cloud is geometrically self-similar and resembles a large plane. Notably, the LiDAR point cloud is also affected by the ice such that rays with a large incidence angle on the ice return invalid points and valid points have increased noise standard deviation. The radar after takeoff and before landing mostly returns less than three points per point cloud with frequently empty point clouds. The returns are primarily from the surface directly below the robot as it is flying.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Frozen Lake", "weight": 1.0} -->

GaRLIO fails in this dataset as it calculates a least-squares estimate of velocity from the radar point cloud for outlier rejection, which requires a minimum of three points. AF-RLIO while functioning initially, quickly breaks once far enough away from the bank due to the sparse radar point clouds. Both FAST-LIO2 and FAST-LIVO2 initially function well, however, their accuracy deteriorates rapidly when the system performs an aggressive yaw maneuver and accumulates significant error. Despite also based on LiDAR-inertial fusion, Ours - LI does not fail in this environment due to parametric differences in Ours - LI, that were not replicable in FAST-LIO2, which results in more robust performance. Due to the visually feature-full environment and good outdoor lighting conditions, OpenVINS provides the best baseline performance (followed by ROVIO). Our solution retains performance similar to these baselines across most vision-involving configurations (i.e., Ours - VI, Ours - LVI, Ours - RVI, and Ours - LRVI), while it is notable that Ours - LI, Ours - RI, and Ours - LRI remain functional.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Frozen Lake", "weight": 1.0} -->

The performance of the proposed method's ablation is shown in Figure˜10, where the geometric self-similarity of the frozen lake is clear.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Campus Fog", "weight": 1.0} -->

A handheld UniPilot module is carried through a typical university campus environment, for a total trajectory length of $670\text{\,}\mathrm{m}\text{/}$. The trajectory starts outdoors but proceeds indoors into a fog-filled room before returning outdoors. As a result, the experiment features large variation in the local environment scale as well as dense visual obscurants, which are known to cause problems for LiDAR- and vision-based estimation. The ground truth for this experiment is created using the Pix4DMatic bundle adjustment-based method.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Campus Fog", "weight": 1.0} -->

As expected, both the vision- and LiDAR-based methods (i.e., FAST-LIO2, FAST-LIVO2, ROVIO, OpenVINS, Ours - LI, Ours - VI, and Ours - LVI) perform well until the room with visual obscurants (fog), wherein the aforementioned methods accumulate significant error resulting from the extended duration of unusable measurements. The Ours - RI ablation functions regardless as the radar is unaffected by such phenomena, however still accumulates drift due to the long mission duration. GaRLIO and AF-RLIO, despite including the radar, are challenged here as well. For the former, the sparseness of the radar point clouds result in challenges with respect to [RANSAC]-based outlier rejection, and as a result the method fails. For the latter, when LiDAR point cloud degeneracy is detected, the method switches to radar-based registration. This is generally difficult with small form-factor radar sensors, again leading to failure. This also indicates the strengths and inherent robustness of our radar Doppler factor formulation.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Campus Fog", "weight": 1.0} -->

The proposed multi-modal ablations which include the radar (Ours - RI, Ours - RVI, Ours - LRI, and LRVI) perform robustly, as the radar's invariance to visual obscurants is able to be complementarily fused with the accuracy associated with vision- and LiDAR-based methods in suitable conditions. As expected, the ablations which include the LiDAR together with the radar perform best. The results for this experiment are visualized in Figure˜11, note in particular the challenge posed on LiDAR- and vision-based sensing by the visual obscurants in the fog-filled room. Here, the LiDAR returns nearly no points and the camera is completely blinded.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Scene Reasoning", "weight": 1.0} -->

Provided the multi-modal [SLAM] capabilities of the [UAstack], we further assess downstream functionality for scene reasoning. Figure˜12 presents two real-world examples of the proposed [VLM] reasoning system. As a straightforward extension to the core perception module capabilities, our open-vocabulary semantic mapping system and 3D object detection are shown on the left side of the figure, where the reconstructed point cloud, together with the bounding boxes of the detected objects, is illustrated. Our semantic mapping pipeline, based on the open-vocabulary object detector, operates at 1 Hz. This result demonstrates the ability of the perception module to consistently maintain semantic understanding over time.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Scene Reasoning", "weight": 1.0} -->

On the right side of Figure˜12, we show instances of the visual question/answering module, which provides contextual reasoning beyond geometric perception. As shown in the examples, the system correctly identifies potentially unsafe conditions in fog with high confidence, as well as determines whether there are exits or entrances in the current view. In our current implementation, GPT-5 is queried through the OpenAI API every 50 s. The end-to-end inference latency across our evaluations was $5.66\pm 1.55$ s, including both the API latency and the model inference time. Overall, these results demonstrate that the combination of semantic 3D mapping and binary visual Q&A can enable more robust scene understanding and reasoning.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Navigation Module Evaluation", "weight": 1.0} -->

We conduct experiments to thoroughly evaluate the navigation module. Specifically, two studies are conducted. The first, evaluates the ability of the navigation module to navigate to a waypoint without the presence of a guiding path from the planning module. In the second, the ability of the navigation module to handle the sudden appearance of unmapped obstacles in the planned path is studied. The aim of these experiments is to a) evaluate the performance of the navigation module in the [SDF-NMPC] + [C-CBF], [ExRL] + [C-CBF], and unsafe controller + [C-CBF] (where applicable) configurations, b) contrast the behaviors of these collision avoidance methods, and c) evaluate the benefits of the multi-layered safety approach. In all these missions, the [AR-2] platform was used, with the [SLAM] module running the graph optimization online after receiving each exteroceptive measurement, considering radar measurements at $10\text{\,}\mathrm{Hz}\text{/}$ and LiDAR measurements at $10\text{\,}\mathrm{Hz}\text{/}$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Navigation Module Evaluation", "weight": 1.0} -->

In each experiment (including the evaluations in Section˜4.4) the [SDF-NMPC] runs at $40\text{\,}\mathrm{Hz}\text{/}$, [ExRL] at $30\text{\,}\mathrm{Hz}\text{/}$, and [C-CBF] runs at $50\text{\,}\mathrm{Hz}\text{/}$. The last received exteroceptive sensor measurements and state estimates are used to populate the state and inputs for each method while it executes at the desired frequency.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Navigation to Waypoint", "weight": 1.0} -->

The first evaluation studies the ability of the navigation module to navigate to a waypoint without a guiding path from the map-based planning module. The study is conducted in a forest environment. Three experiments are conducted in which the collision avoidance methods used are [SDF-NMPC] + [C-CBF], [ExRL] + [C-CBF], and an unsafe policy ([SDF-NMPC] but with its collision-avoidance constraints disabled) + [C-CBF]. In each experiment, the robot starts from the same location, and the same waypoint is given to the navigation module. The results of the study are shown in Figure 13. Both configurations, [SDF-NMPC] + [C-CBF] and [ExRL] + [C-CBF], are able to reach the waypoint, avoiding the obstacles. The collision avoidance is predominantly carried out by the [SDF-NMPC] or [ExRL], with the [C-CBF] intervening only in a few instances (Figures 13.1.3, 13.2.1, and 13.2.2).

<!-- chunk {"id": "body-0144", "role": "body", "section": "Navigation to Waypoint", "weight": 1.0} -->

Engagement of the [C-CBF] is not a proof that [SDF-NMPC] or [ExRL] would necessarily lead to a collision but indicates that the tuning of this last-resort method was such that it triggers it to adjust the reference commands. In turn, close evaluation of the few instances when [C-CBF] was engaged in these experiments indicates that the robot centroid was on average $0.65\text{\,}\mathrm{m}\text{/}$ from the obstacles (which given the robot dimensions, entails less than $0.5\text{\,}\mathrm{m}\text{/}$ clearance). On the other hand, the combination of the unsafe version of [SDF-NMPC] with the [C-CBF] (which then becomes the only obstacle-avoidance mechanism) is not able to reach the goal and gets stuck, but remains safe at all times. As the [C-CBF] only aims to remain in the safe set, navigating to the goal is not per se an objective for this method.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Navigation to Waypoint", "weight": 1.0} -->

It is noted that the third configuration (unsafe controller + [C-CBF]) is not a recommended configuration of the [UAstack] and is only evaluated to present the different roles of the navigation layers.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Navigation to Waypoint", "weight": 1.0} -->

Qualitatively, this study further shows the clear difference in the robot's behavior when using [SDF-NMPC] vs [ExRL]. The [SDF-NMPC] follows the straight line from the start to the goal more closely, while the [ExRL] policy deviates significantly. On the other hand, the [ExRL] achieves higher speeds throughout the trajectory than [SDF-NMPC]. Due to this, the resulting mission time for both is comparable. Hence, the selection between [SDF-NMPC] and [ExRL] depends on the requirements of the task. The different behaviors manifested between [SDF-NMPC] and [ExRL] is among the reasons why the release of the [UAstack] contains both methods.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Moving Obstacles", "weight": 1.0} -->

The second study conducted to evaluate the navigation module aims to evaluate its performance in the presence of obstacles appearing in the planned path. Specifically, the following scenario was constructed. The robot was tasked to explore a section of a university building at NTNU. In two separate instances, after the planning module plans a path based on the online map, an obstacle is placed to block this path. The planner is not re-triggered and thus the reference path shall be in collision. The ability of the navigation module to handle this scenario is tested. Two experiments are conducted with the configurations [SDF-NMPC] + [C-CBF] and [ExRL] + [C-CBF]. Figures 14 and 15 show the result of the respective experiments. As can be seen, both policies are able to successfully avoid the unseen obstacle. The figures also show that the [SDF-NMPC] tends to avoid the obstacle with less, yet sufficiently safe, clearance as compared to [ExRL] as its formulation requires it to have minimal deviation from the reference path. [ExRL] does not have this constraint and only aims to reach the end of the planned path safely.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Evaluation of the Full Stack", "weight": 1.0} -->

The full [UAstack] is evaluated using both aerial and ground robots. When evaluating the full stack, we examine the result of the coordinated interaction between the perception, planning and navigation modules. The perception module is the foundation of the demonstrated autonomy, the planning module drives the behaviors manifested by the robots, while the navigation module provides control and reinforces safety for the autonomous systems. Specifically, the Exploration and Inspection objectives are tested with the Planning to Target being implicitly evaluated through these. Additional insights regarding the Planning to Target behavior can be found in Zacharia et al.. Similarly to Section˜4.3 the [SLAM] module graph optimization is calculated online, with update rate matching what was previously described.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Evaluations with an Aerial Robot", "weight": 1.0} -->

We evaluate the [UAstack] on the [AR-2] in three distinct environments namely a) an underground mine, b) a forest, and c) a ship cargo hold.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Underground Mine", "weight": 1.0} -->

The first experiment is conducted in a section of the Løkken mine in Norway. We demonstrate results both when otherwise using the [SDF-NMPC] and [ExRL]. The selected section of the mine is a $3$-way intersection with the robot starting at one end of the narrowest branch ($1.5\text{\,}\mathrm{m}\text{/}$ wide). The mine has low lighting conditions, and due to the dome [FoV], the LiDAR data can quickly become degenerate in narrow branches if the sensor is facing a wall. In both missions, the robot explored the first branch it started, continued to one of the other branches, repositioned to the next upon exploring it, before finally returning to the start location when the allotted area was fully explored. The robot successfully explored the environment while remaining safe at all times. Figures 16 and 17 show the maps and planning instances in the missions corresponding to [SDF-NMPC] and [ExRL] respectively. As the environment topology does not allow much deviation from the planned path, the total path length in both missions is comparable, however, the [ExRL] policy finishes faster reaching higher speeds.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Underground Mine", "weight": 1.0} -->

It was observed that at some instances in the narrowest part near the starting area (marked as Start/End in the figures), the [SDF-NMPC]/[ExRL] and the [C-CBF] objectives are competing resulting in transient oscillations. The [SDF-NMPC]/[ExRL] are tasked to both make progress along the planned path and maintain safety, while the [C-CBF] only aims for robot safety thus leading to competing actions in situations that have tight safety margins as here. Nevertheless, the system was always able to continue and this behavior was short-lived.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Forest", "weight": 1.0} -->

The [AR-2] was deployed in a forest in Trondheim, Norway to explore an area of \\qtyproduct120x80 with height limited to $2.5\text{\,}\mathrm{m}\text{/}$. The forest area contains trees at varying densities with thin branches and foliage in some places. The ground was covered in snow at the time of testing. In this test, two missions were conducted, one each with the [SDF-NMPC] and the [ExRL] as the core navigation policy feeding into the [C-CBF]. Figures 18 and 19 show the results for the respective missions. In both missions, the robot started at the same location with identical mission and robot parameters. The robot first performed exploration of the given space and returned back to the start location. As can be seen from Figures 18 and 19, the [SDF-NMPC] is designed to follow the path given by the planning module more accurately than [ExRL]. Hence, the robot can take longer trajectories to reach the end of the same path when [ExRL] is used as compared to [SDF-NMPC].

<!-- chunk {"id": "body-0153", "role": "body", "section": "Forest", "weight": 1.0} -->

However, as shown by the average and max speed, the [ExRL] policy generates smoother and faster trajectories than [SDF-NMPC] (partially as a result of the non-smooth paths given by the planning module), thus resulting in similar mission times. It is thus a decision point for the user of the [UAstack] to select among these two core navigation policies with the [SDF-NMPC] being a very reasonable choice when following the planner plans closely is desired, while [ExRL] is particularly relevant when a more loose tracking of these references combined with agile maneuvering is preferred. Figures 18 and 19 show the full map and planning instances from the respective missions, along with the robot in the environment. In both missions, the robot was successfully able to explore the allotted area, avoiding collisions even in the presence of thin obstacles due to the multi-layered safety. Figures 18.2.1-18.2.4 show one such instance where the [SDF-NMPC] deviates from the path planned by the planning module. Similarly, the [ExRL] policy successfully guides the robot to the end of the path.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Forest", "weight": 1.0} -->

At one instance in the mission, shown in Figure 19.1.2, the [C-CBF] can be seen intervening and correcting the command of the [ExRL] policy as the robot passes through a narrow opening, thus highlighting the importance of the multi-layered safety approach. As when the navigation module was evaluated separately, it is worth mentioning that when the [C-CBF] was engaged the distance of the robot centroid from the obstacles was $0.68\text{\,}\mathrm{m}\text{/}$ and the component of the velocity towards the obstacle was $1.10\text{\,}\mathrm{m}\text{/}\mathrm{s}$. Although the engagement of the [C-CBF] does not strictly imply that the core method would lead to a collision, it indicates the role of such a last-resort safety method to assure what proximity and maneuvering towards the obstacles is considered as acceptable.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Ship Cargo Hold", "weight": 1.0} -->

In the third experiment, the [AR-2] was deployed in a cargo hold of an oil tanker ship. In contrast to the previous missions, here the inspection behavior of the planning module is engaged. The dimensions of the cargo hold were \\qtyproduct16x13x15, however, the mission height was limited to $3\text{\,}\mathrm{m}\text{/}$ for safety considerations. The robot was tasked to explore the cargo hold and inspect the mapped surfaces. The robot started inside the cargo hold with no prior knowledge, performed exploration, and upon completion switched to the inspection behavior. The complete map and instances of the mission along with an image of the robot in the environment is shown in Figure 20. As an exception, it is noted that in this experiment the safety policies in the navigation module were disabled as (a) the environment is not demanding in terms of collision avoidance (one large room with no obstacles inside), and (b) this allows the robot to more flexibly travel outside the depth sensor's [FoV] in the inspection phase.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Ship Cargo Hold", "weight": 1.0} -->

Through these experiments, we demonstrate the importance and the role of the three layers of safety namely a) map-based collision-avoidance, b) depth-driven [SDF-NMPC] or [ExRL] policies, and c) the last resort [C-CBF]. The map-based safety allows longer horizon planning enabling more complex behavior, and is the safety layer doing the majority of the collision-avoidance throughout the missions. The depth-driven navigation policies add an additional safeguard against challenges to map-based safety as documented in this work. Finally, the [C-CBF] provides formal safety guarantees ensuring that the robot remains safe at all times.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Legged", "weight": 1.0} -->

To demonstrate the performance of the [UAstack] on ground robots, we deployed [GR-1] in two distinct settings a) in an underground mine, and b) inside a university building at NTNU.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Underground Mine", "weight": 1.0} -->

In the first mission, [GR-1] was deployed in another section of the Løkken mine. This section consisted of one mine shaft having narrow passages and areas with gaps on the side, requiring careful planning and locomotion. Figure 21 shows the map and planning instances of the mission. Using the dual map representation (volumetric and elevation map), the [UAstack] is able to successfully complete the mission. It is noted that here the additional safety layers of the navigation module are not utilized as the commercial ANYmal robot already provides the partially analogous feature of "perceptive locomotion" fusing short-range depth from its all-around depth cameras for traversability-aware near-term navigation.

<!-- chunk {"id": "body-0159", "role": "body", "section": "University Building", "weight": 1.0} -->

The second mission was conducted inside a building at NTNU. The building consists of two sections a) a large open hall with side offshoots, and b) a section with a network of narrow (width $<1.5\text{\,}\mathrm{m}\text{/}$) corridors, as can be seen in Figure 22. The robot started in the open hall, and explored it along with the offshoots. Upon completion, the robot repositioned towards the narrow corridor section, explored those, and returned to the start location. This environment presents several challenges to the entire stack, including a) large scale, b) branching corridors, and c) varying environment size. However, the multi-modal [SLAM] solution provided resilient odometry and consistent maps throughout the mission, as well as the bifurcated architecture of the planning module with traversability-aware planning (exploiting both the volumetric and the elevation maps) lead to successful mission completion.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Conclusion & Future Work", "weight": 1.5} -->

The [UAstack] is openly released with the aim of serving as a foundation for a common autonomy blueprint across diverse robot configurations operating in the air, on land, and at sea. Currently, the [UAstack] supports a wide variety of aerial and ground robot morphologies and enables resilient [GNSS]-denied, perceptually-degraded localization, mapping, and scene reasoning within target reach, exploration and inspection missions with a key focus on assured safety through multi-layered navigation. Extensive field evaluation results, alongside openly released datasets, allow for its comprehensive evaluation.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Conclusion & Future Work", "weight": 1.5} -->

We seek to collaborate with the research community towards enhancing the reliability and resilient performance of the stack, alongside its extension to different robot morphologies and the incorporation of new behaviors. Future development plans specifically include (a) the support of further morphologies, including highly non-holonomic platforms such as fixed-wing uncrewed aerial vehicles, (b) increased emphasis on navigation within dynamic environments, (c) development of further object-centric behaviors, especially guided by natural language, (d) the fusion of additional modalities and specifically infrared vision, (e) improving the vision fusion into MIMOSA-X to be more tightly coupled analogous to what is already done for LiDAR and radar, (f) enhancing the [ExRL] toward improved long-horizon capabilities, and (g) extend multi-layered safety with traversability-aware reactive modules for ground systems.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Conclusion & Future Work", "weight": 1.5} -->

Last but not least, we aim to document how lessons learned from the deployment of the stack can lead to certain improvements and adaptations. This currently includes investigations for (a) how to best handle the trade-off between [C-CBF] and the exteroceptive [SDF-NMPC] and [ExRL] methods, (b) computationally-efficient ways to directly fuse vision features in the [SLAM] solution of the [UAstack], alongside (c) refining the rewards of [ExRL] to better balance between the ability of the method to negotiate complex environments, and how energetically-efficient the trajectories are.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Conclusion & Future Work", "weight": 1.5} -->

We would like to acknowledge Statens Vegvesen for enabling us to perform tests in Runehamar, Vestland Fylkeskommune for allowing us to perform experiments in the Fyllingsdal sykkeltunnel, Leica Geosystems for providing the Robot Operating System ([ROS]) compatible and setup for collection of ground truth, as well as Orkla Industrimuseum for facilitating the tests in the Løkken Mine.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Mihir Dharmadhikari: Contributed in the formulation of the idea, the [UAstack] architecture, and all the evaluations. Furthermore, he is the core developer of the planning module.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Nikhil Khedekar: Contributed in the formulation of the idea, the [UAstack] architecture, and all the evaluations. Furthermore, he is a core developer of the multi-modal [SLAM], specifically the LiDAR and Vision modalities.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Mihir Kulkarni: Contributed in the formulation of the idea, the [UAstack] architecture, and all the evaluations. Furthermore, he is the core developer of Exteroceptive Deep RL navigation policy.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Morten Nissov: Contributed in the formulation of the idea, the [UAstack] architecture, and all the evaluations. Furthermore, he is a core developer of the multi-modal [SLAM], specifically the Radar modality.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Martin Jacquet: He is the core developer of the Neural SDF-NMPC and co-developer of the Composite CBF-based Safety Filter, and contributed towards their integration in the [UAstack].

<!-- chunk {"id": "body-0169", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Angelos Zacharia: He is the co-developer of the planning module. He contributed towards its integration in the [UAstack] and the legged robot experiments.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Marvin Harms: He is the core developer of the Composite CBF-based Safety Filter. He contributed towards its integration in the [UAstack] and the evaluations of the safety policies.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Albert Gassol Puigjaner: He is the core developer of the VLM-based reasoning part of the [UAstack] and contributed towards its integration in the [UAstack].

<!-- chunk {"id": "body-0172", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Philipp Weiss: Contributed towards the development of the hardware setup and conducting the field experiments.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Author contributions", "weight": 1.0} -->

Kostas Alexis: Contributed in the formulation of the idea, the [UAstack] architecture, and planning for all evaluations. Furthermore, he contributed to the planning, problem formulation, and algorithmic approach of each module in the [UAstack].

<!-- chunk {"id": "body-0174", "role": "body", "section": "Author contributions", "weight": 1.0} -->

All authors contributed to the writing of this manuscript.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Ethical considerations", "weight": 1.0} -->

This article does not contain any studies with human or animal participants.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Consent for publication", "weight": 1.0} -->

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Consent for publication", "weight": 1.0} -->

The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article: This work was supported by European Commission Horizon Europe grant agreements a) SPEAR (EC 101119774), b) DIGIFOREST (EC 101070405), c) SYNERGISE (EC 101121321), and d) AUTOASSESS (EC 101120732).
