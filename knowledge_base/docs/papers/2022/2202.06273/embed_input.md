<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Continuous Occupancy Mapping in Dynamic Environments Using Particles

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Particle-based dynamic occupancy maps were proposed in recent years to model the obstacles in dynamic environments. Current particle-based maps describe the occupancy status in discrete grid form and suffer from the grid size problem, wherein a large grid size is unfavorable for motion planning, while a small grid size lowers efficiency and causes gaps and inconsistencies. To tackle this problem, this paper generalizes the particle-based map into continuous space and builds an efficient 3D egocentric local map. A dual-structure subspace division paradigm, composed of a voxel subspace division and a novel pyramid-like subspace division, is proposed to propagate particles and update the map efficiently with the consideration of occlusions. The occupancy status of an arbitrary point in the map space can then be estimated with the particles' weights. To further enhance the performance of simultaneously modeling static and dynamic obstacles and minimize noise, an initial velocity estimation approach and a mixture model are utilized. Experimental results show that our map can effectively and efficiently model both dynamic obstacles and static obstacles.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compared to the state-of-the-art grid-form particle-based map, our map enables continuous occupancy estimation and substantially improves the performance in different resolutions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The particle-based map is originally proposed in for dynamic and unstructured environments. Particles with position and velocity states are used to approximate both dynamic obstacles and static obstacles on the basis of sequential Monte Carlo (SMC) filtering. In recent works, introduces the theory of random finite set (RFS) to particle-based maps. The probability hypothesis density (PHD) filter is applied to predict and update the particles and estimate the dynamics of the grids in the map. Later, improve the particle-based maps by considering the mixture model, semantic information and high-level occupancy status inference, respectively. Due to the ability to model complex-shaped static and dynamic obstacles simultaneously, particle-based maps draw more attention in representing dynamic environments. Currently, the input form of particle-based maps is the ray-casting-generated measurement grid map originated from the first work, and thus the map is discretized with grids. This discrete form inhibits the state estimation resolution and brings the grid size problem, namely: large grids lead to a low resolution that is unfavorable for motion planning, while small grids increase the computation requirements and may cause gaps and inconsistencies.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Besides, desktop GPUs are required to run the particle-based maps in real-time, and a more efficient map is needed for applications in small-scale robotic systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work proposes a dual-structure particle-based (DSP) map, a continuous dynamic occupancy map free from the grid size problem. The input of the map is the raw point cloud rather than the measurement grid map. A novel dual-structure map building paradigm, composed of a voxel subspace division for particle storage and resampling and a dynamic pyramid-like subspace division for occlusion-aware particle update, is proposed to model the local environment with particles that have continuous states. Under the Gaussian noise assumption, we demonstrate that this updating paradigm is effective and computationally efficient. To reduce the noise in simultaneously modeling static and dynamic obstacles, the importance of newborn particles is addressed by using non-Gaussian initial velocity estimation and a mixture model that adaptively allocates the number of static and dynamic particles. With a complete process of prediction, update, birth, and resampling of particles in the continuous space, the occupancy status at an arbitrary point in the map can be estimated using onboard CPU devices.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the experimental tests, we first evaluated the dynamic obstacle velocity estimation precision of the map. Then the ablation study was conducted to identify the mapping parameters. Subsequently, comparison tests were carried out, involving a state-of-the-art particle-based dynamic occupancy map and a widely used static occupancy map. Results show that our map has the best occupancy status estimation performance in dynamic environments and competitive performance with in static environments. Furthermore, we verified the DSP map in obstacle avoidance tasks of a mini quadrotor in different environments. To the best of the authors' knowledge, this is the first continuous particle-based occupancy map and the first dynamic occupancy map that can be applied to small-scale robotic systems like quadrotors.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this work include: A novel dual-structure particle-based map building paradigm that enables continuous mapping of the occupancy status in dynamic environments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The leverage of initial velocity estimation and an efficient mixture model to reduce noise in modeling static and dynamic obstacles simultaneously.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The complete procedures of building a DSP map that can be applied to onboard computing devices of small-scale robotic systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The released code at including an example application in ROS.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remaining content is organized as follows: Section II describes the related work. Section III presents the background knowledge of our map. Section IV explains the formulations of the world model and gives an overview of mapping procedures. Section V expresses the mapping procedures with the dual structure. In Section VI, more components for mapping are discussed. Section VII presents some implementation details. The experimental results and the conclusion are described in Section VIII and Section IX, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Discrete Map and Continuous Map", "weight": 1.0} -->

Environment representation is fundamental to obstacle avoidance of robotics systems. One of the most popular representation approaches is occupancy mapping, which originated from and is capable of modeling cluttered environments. Grid map (2D or 3D) is a kind of computationally efficient form to realize occupancy mapping. The environment is usually divided into discrete grids, and the occupancy status of each grid is updated with the ray casting algorithm. The size of the grids, however, is difficult to determine. Large grids lead to a low resolution that is unfavorable for motion planning. Small grids increase the computation requirements and cause gaps and inconsistencies when the input point clouds are sparse or noisy. To avoid the grid size problem and allow arbitrary resolutions, the paradigm of building the map with continuous occupancy probability kernels rather than grids is proposed. Free space and occupied points or segments are first generated with the input point clouds and then used to update the parameters in the kernel functions. The occupancy status at an arbitrary position can then be estimated with nearby kernels.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Occupancy Maps in Dynamic Environments", "weight": 1.0} -->

The maps mentioned above are built under the assumption that the environment is static. As the robotic systems were deployed in dynamic environments, improvements have to be made to instantly represent the occupancy position of dynamic obstacles, such as pedestrians and other robots, and, even further, to predict the future positions of dynamic obstacles. An intuitive approach is to leverage independent detection and tracking of moving objects (DATMO) to model the dynamic obstacles and utilize static occupancy maps still to represent the other objects. A prerequisite of DATMO is that the detection and shape models of the dynamic obstacles are well-trained, which conflicts with the unknown environment characters in many tasks. In addition, difficulties in data association and the trail noise caused by obstacles movements in the static map are intractable. Therefore, improving the map itself directly by considering the dynamic obstacle assumption is required, and the dynamic occupancy map emerges accordingly.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Occupancy Maps in Dynamic Environments", "weight": 1.0} -->

Early dynamic occupancy maps treat the dynamic obstacles, such as pedestrians and robots, as spurious data in the map, and detect and remove the data to build a robust static map. Starting from the latest decade, research works considering modeling the dynamics, mostly velocities, of the obstacles in the map have been carried out to improve the obstacle avoidance performance in dynamic environments. Various methods have been proposed in these works. Some apply the dynamic obstacle assumption to the existing structures of static occupancy maps. For example, adopts optical-flow-based motion maps to estimate the velocity of grids and improves the Gaussian process occupancy map to adapt to dynamic environments. further improves by learning dynamic areas with stochastic variational inference. In, point clouds from lidar are clustered and filtered to estimate the velocities of dynamic obstacles. The estimation is applied to generate non-stationary kernels in the Hilbert space to build the dynamic Hilbert map. With the popularity of deep learning methods, some recent works adopt neural networks to predict the velocity of each grid in a grid map, or future occupancy status,.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

The particle-based map originates from the autonomous driving area. In a particle-based map, an obstacle is regarded as a set of point objects and the particles with velocities are used to model the point objects. Compared to the dynamic occupancy maps in II-B, the particle-based map is originally proposed for dynamic environments and has a stronger potential to improve the mapping performance in complex and highly dynamic environments. Nuss et al. improves by introducing the RFS theory and deriving map-building procedures with the PHD filter and the Bernoulli filter. The improved map can be built in real-time in 2D space with GPU devices. Later, generalizes to 3D space.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

In a cluttered environment with dynamic and static obstacles, multiple point objects, dynamic or static, need to be modeled, and denoising is of great importance. Two approaches are usually adopted to reduce the noise. The first approach is to use a mixture model, which includes a separate static model and a dynamic model, to update the states of static and dynamic point objects independently. The mixture model works as dual PHD filters or the grid-level inference. Another approach is to apply additional information to reduce the noise in the updating procedure. For instance, adds an extra semantic grid channel in the input to generate particles with semantic labels and update with the semantic association.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

The above particle-based maps are still grid maps. Measurement grids generated by the ray casting method are adopted as the input, and the environment is described with discretized 2D or 3D girds. This discretized expression suffers from the grid size problem mentioned in Section I. The grid size also limits the state estimation resolution of the obstacles. Therefore, a continuous particle-based occupancy map is required. In addition, since numerous particles are used, state-of-the-art particle-based maps usually rely on Desktop GPU devices for computation. To deploy the particle-based map on small-scale robotic systems, improving computational efficiency is necessary.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

RFS, RFS composed of point objects at time k.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

RFS composed of point objects in a voxel subspace and a pyramid subspace, respectively, with index i at time k.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

RFS composed of measurement points at time k.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

RFS composed of survived objects from k − 1 to k.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

RFS composed of newborn objects from k − 1 to k.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

RFS composed of the detected objects and clutter at k.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

State vector of an element or an object with index i.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

State vector of a measurement point with index i.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Point object coordinate in Cartesian coordinate system.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Point object coordinate in sphere coordinate system.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

The map space. Visible space in the map space.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Voxel subspace and pyramid subspace with index i.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

The weight of a particle with index i at time k.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Detection and survival probability of an object.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Number of point objects and measurement points at k.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Number of voxel subspaces and pyramid subspaces.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Number of newborn particles from a measurement point.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Allowed max particle number in 𝕄 after resampling.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Allowed max particle number in 𝕍i after resampling.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Coefficients in the mixture motion model.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Intensity of the newborn objects and clusters.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Side length or resolution of a voxel subspace.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

The number of adjacent pyramids on each side in 𝔸xk.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Resolution of the voxel filter for point cloud pre-process.

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

The radius of the robot sphere model.

<!-- chunk {"id": "body-0044", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Horizontal and vertical angle of the FOV.

<!-- chunk {"id": "body-0045", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Gaussian noise covariance matrix in prediction step.

<!-- chunk {"id": "body-0046", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Weight sum of dynamic particles in a voxel subspace.

<!-- chunk {"id": "body-0047", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Weight sum of static particles in a voxel subspace.

<!-- chunk {"id": "body-0048", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Weight sum of all the particles in a voxel subspace.

<!-- chunk {"id": "body-0049", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Function to calculate the absolute velocity value.

<!-- chunk {"id": "body-0050", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Mass function and probability function in DST.

<!-- chunk {"id": "body-0051", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Belief function and plausibility function in DST.

<!-- chunk {"id": "body-0052", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

State transition density function of a single object.

<!-- chunk {"id": "body-0053", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Measurement likelihood function of a single object.

<!-- chunk {"id": "body-0054", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

State transition function of a single point object.

<!-- chunk {"id": "body-0055", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Measurement function of a single point object.

<!-- chunk {"id": "body-0056", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Function that defines the measurement noise matrix.

<!-- chunk {"id": "body-0057", "role": "body", "section": "II-C Particle-based Dynamic Occupancy Maps", "weight": 1.0} -->

Function that defines the standard deviation on each axis.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-A Random Finite Set", "weight": 1.0} -->

An RFS is a finite set-valued random variable. The number and the states of the elements in an RFS are random but finite. Let X denote an RFS and ${\mathbf{x}}^{(i)} \in {\mathbb{M}}$ denote the state vector of an element in X. $\mathbb{M}$ is ${\mathbf{x}}^{(i)}$'s state space, e.g., map space. Then X is expressed as: where $N \in {\mathbb{N}}$ is a random variable representing elements number in X and is called the cardinality of X. Specially, when $N = 0$, X is $\varnothing$. A common usage of the RFS is in the multi-object tracking area, where ${\mathbf{x}}^{(i)}$ is usually the state of an object and X is the set composed of the states of all objects. $N$ varies as objects appear and disappear in the tracking range.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-B PHD", "weight": 1.0} -->

PHD is a first moment of an RFS and is raised to describe the multi-object density. The PHD of X at a state $\mathbf{x}$ is defined as: where $\mathbf{E}{\lbrack \cdot \rbrack}$ is the expectation and $\delta{(\cdot)}$ is the Dirac function^11^1Dirac function: ${{\delta{({\mathbf{x}})}} = 0},{{\text{if}{\mathbf{x}}} \neq \mathbf{0}}$; ${\int{\delta{({\mathbf{x}})}\text{d}{\mathbf{x}}}} = 1$..

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-B PHD", "weight": 1.0} -->

Two important properties of PHD are used in this work. The first property is that the integral of PHD is the expectation of the cardinality of X, which can be expressed as where $|\text{X}|$ represents the cardinality of X.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-C PHD Filter", "weight": 1.0} -->

The PHD filter is an efficient filter that propagates the PHD in the prediction and the update step, and can be used to handle multiple object tracking problems. Let $\text{X}_{k - 1}$ and $\text{X}_{k}$ denote the RFS composed of object states at time step $k - 1$ and $k$, respectively. Suppose $\text{Z}_{k}$ is the RFS composed of measurements, i.e., point cloud, to the objects at time $k$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-C PHD Filter", "weight": 1.0} -->

In the prediction step of a typical PHD filter, the prior object states RFS $\text{X}_{k|{k - 1}}$ can be treated as the union of two independent subsets, which is $\text{X}_{k|{k - 1}} = {\text{S}_{k|{k - 1}} \cup \text{B}_{k|{k - 1}}}$, where $\text{S}_{k|{k - 1}}$ represents the persistent objects from the $\text{X}_{k - 1}$, and $\text{B}_{k|{k - 1}}$ is the newly born objects. Note $\text{S}_{k|{k - 1}}$ and $\text{B}_{k|{k - 1}}$ are distinguished by birth time. They are both in map space $\mathbb{M}$ but don't share any element.

<!-- chunk {"id": "body-0063", "role": "body", "section": "III-C PHD Filter", "weight": 1.0} -->

Let $D_{\text{S}_{k|{k - 1}}}{({\mathbf{x}}_{k})}$ and $D_{\text{B}_{k|{k - 1}}}{({\mathbf{x}}_{k})}$ denote the PHD at ${\mathbf{x}}_{k}$ of RFS $\text{S}_{k|{k - 1}}$ and $\text{B}_{k|{k - 1}}$, respectively. Considering the property and the MBM and PPP models, the general PHD filter is described as: where Equation and show the prediction step, and Equation and present the update step. $\pi_{k|{k - 1}}{(\cdot)}$ is the state transition density of a single object and $g_{k}{(\cdot)}$ is the single object measurement likelihood.

<!-- chunk {"id": "body-0064", "role": "body", "section": "III-D SMC-PHD Filter", "weight": 1.0} -->

Sequential Monte Carlo PHD (SMC-PHD) filter uses particles to represent PHD and is an efficient implementation of the PHD filter. Each particle has a weight and a state vector with the same dimension as an object's state. With the particles, the posterior PHD of X at time $k - 1$ is approximated by where $L_{k - 1}$ is the number of particles at time step $k - 1$, $w_{k - 1}^{(i)}$ is the weight of particle with index $(i)$, and ${\overset{\sim}{\mathbf{x}}}_{k - 1}^{(i)}$ denotes the state vector of particle $(i)$. We distinguish the state of an object and the state of a particle with the tilde notation.

<!-- chunk {"id": "body-0065", "role": "body", "section": "III-D SMC-PHD Filter", "weight": 1.0} -->

In the update step, substitute $D_{\text{X}_{k - 1}}{({\mathbf{x}}_{k - 1})}$ in Equations and with the particle representation in the last row of. The posterior PHD at $k$ is reformed into the summation of particles, which is where the particle state ${\overset{\sim}{\mathbf{x}}}_{k}^{(i)}$ remains the same as in the prediction step and the weight $w_{k}^{(i)}$ is given: The SMC-PHD filter estimates the PHD of X by iterative prediction with Equation to and update with Equation to. Details can be found.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

Our DSP map is an egocentric map built on multi-object tracking at the point object level in a continuous neighborhood space. Let $\mathbb{M}$ denote the neighborhood map space of the robot. $\mathbb{M}$ is a real space that has a cuboid boundary with size $(l_{x},l_{y},l_{z})$. The size can be set according to the range of the utilized sensors or the requirements from the motion planner. At the center of the cuboid is the robot. We consider the obstacles in $\mathbb{M}$ as point objects, similar to. Fig. 1(a) reveals the relation between obstacles and point objects. One obstacle can correspond to multiple point objects. The point objects are used to estimate the occupancy status at an arbitrary position in the map. Since the occupancy status rather than the state of each obstacle is more important in an occupancy map, the mapping from point objects to obstacles is omitted and the assumption that all the point objects move independently is made. The same assumption is used in the existing works on particle-based maps.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

For the reason that the obstacles are unknown, the number of the point objects in $\mathbb{M}$ and their states are random but finite. Therefore, these point objects can be modeled as an RFS. At a discrete time $k$, the RFS composed of the point object states is represented as where $N_{k}$ is the number of point objects at time $k$, and $\mathbf{x}$ with index from $1$ to $N_{k}$ is the state vector of a point object. The state vector is given by the 3D position and velocity, namely where the subscripts $\{ x,y,z\}$ are used to represent the axes in Cartesian coordinate. The core of building the DSP map is to use the SMC-PHD filter to track the point objects in 3D continuous space and estimate $\text{X}_{k}$'s PHD, which is then used to estimate the occupancy status of the map.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

To realize effective and efficient SMC-PHD filtering in the continuous space, we divide $\mathbb{M}$ into two types of subspaces, i.e., the cubic voxel subspaces and the pyramid-like subspaces, by the position dimensions. The voxel subspaces are used for data storage and particle resampling. The pyramid-like subspaces are applied to handle limited sensor FOV and inevitable occlusions in the continuous space, and realize efficient particle update. Details are presented in Section V. The following describes how to acquire the subspaces and defines the sub-RFSs divided accordingly with the subspaces.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

The voxel subspaces are divided in the cartesian coordinate (Fig. 1(c)). The voxels can fill up $\mathbb{M}$ but have no overlaps with each other. Assume the resolution of the voxel is $l$. Then the number of the voxels is $N_{v} = \frac{l_{x} \cdot l_{y} \cdot l_{z}}{l^{3}}$. Let ${\mathbb{V}}_{i}$ denote the $i^{th}$ voxel subspace. Then $\text{X}_{k}$ can be described as the union of these sub-RFSs, which is Since the voxels have no overlaps, any two sub-RFSs don't share a point object, and thus, the sub-RFSs are independent.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

In the SMC-PHD filter, the voxel subspaces are used to resample the particles in $\mathbb{M}$ in a uniform manner, which is described in Section V-D. In addition, these voxel subspaces are used to index and store the particles for efficiency purposes, as described in Section VII.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

For the reason that the field of view (FOV) of a sensor is usually limited, and the occlusion prevents observations of the area behind obstacles, only a part of $\mathbb{M}$ is visible. Let ${\mathbb{M}}^{f} \subset {\mathbb{M}}$ denote the visible space. ${\mathbb{M}}^{f}$ must be distinguished from the occluded space to realize map updating. However, the voxel subspaces have a limited resolution and cannot continuously express ${\mathbb{M}}^{f}$. Thus, another division structure is still required.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

Inspired by the perspective projection model for sensors, we also divide $\mathbb{M}$ into pyramid-like subspaces in the spherical coordinate (Fig. 1(d)). These subspaces are divided dynamically and uniformly in the sensor frame when the robot pose is given. (Details can be found in Section VII and Algorithm 2 in the Appendix.) The real shape of a pyramid-like subspace is composed of four near-triangular faces and one face on the map boundary face. For simplification, we loosely name the subspace as pyramid subspace in the following content.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

In the spherical coordinate, the azimuth angle range is $\left\lbrack 0,{2\pi} \right\rbrack$ and the zenith angle range is $\lbrack 0,\pi\rbrack$. Suppose the angle interval of the pyramid division, namely the pyramid angle, is $\theta > 0$. The number of these subspaces is $N_{p} = \frac{{2\pi} \cdot \pi}{\theta^{2}}$. To make $N_{p}$ an integer, $\theta$ satisfies ${I\theta} = \pi$, where $I \in {{\mathbb{N}} +}$. Denote by ${\mathbb{P}}_{i}$ the $i^{th}$ pyramid subspace, and by $\text{X}_{k}^{({\mathbb{P}}_{i})}$ the RFS composed of point objects in ${\mathbb{P}}_{i}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

$\text{X}_{k}$ satisfies The measurement of the point objects is the point cloud from sensors, such as stereo cameras or Lidars. The points in the point cloud at time $k$ form a measurement RFS $\text{Z}_{k}$. In analogy to the point objects, $\text{Z}_{k}$ is written as where $M_{k}$ represents the number of the measurement points, and each measurement point $\mathbf{z}$ consists of the 3D position, which is With the measurement points and the pyramid-like subspaces, we can determine the visible space ${\mathbb{M}}^{f}$ and occluded space. As is shown in green in Fig. 3. (a) and (b), ${\mathbb{M}}^{f}$ is the union of the free space and obstacle surface in each pyramid subspace in the FOV. Denote the visible space of pyramid subspace ${\mathbb{P}}_{i}$ by ${\mathbb{P}}_{i}^{f}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

When the pyramid angle $\theta$ of ${\mathbb{P}}_{i}$ equals the angular resolution of the sensor, there is either one or no measurement point in ${\mathbb{P}}_{i}$. If there is one point $\mathbf{z}$, the subspace behind the measurement point is occluded (painted in gray in Fig. 3), while the rest space is the visible pyramid subspace ${\mathbb{P}}_{i}^{f}$. ${\mathbb{P}}_{i}^{f} \subset {\mathbb{P}}_{i}$ and the length of ${\mathbb{P}}_{i}^{f}$ is $|{\mathbf{z}}|$. If there is no measurement point, ${\mathbb{P}}_{i}^{f} = {\mathbb{P}}_{i}$. Suppose the FOV is $\theta_{h} \times \theta_{v}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

The number of ${\mathbb{P}}_{i}^{f}$ is $N_{f} = \frac{\theta_{h}\theta_{v}}{\theta^{2}}$. Since the FOV usually cannot cover the whole neighborhood space, $N_{f} < N_{p}$. Then ${\mathbb{M}}^{f} = {{\mathbb{P}}_{1}^{f} \cup \cdots \cup {\mathbb{P}}_{N_{f}}^{f}}$, and $\text{Z}_{k}$ can be divided into subsets with these visible pyramid subspaces, which is With the measurement $\text{Z}_{k}$, the PHD of $\text{X}_{k}$ is updated by using the SMC-PHD filter. The hollow circles with velocity arrows in Subfigures (b), (c), and (d) in Fig. 1 show the particles used in the SMC-PHD filter.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-A World Model", "weight": 1.0} -->

The basic element in our map is the particle.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-B System Overview", "weight": 1.0} -->

An overview of the procedures to build our DSP map can be found in Fig. 2. The core procedure is filtering the PHD of $\text{X}_{k}$ with the SMC-PHD filter. In the SMC-PHD filter, the prediction step and update step iteratively update the PHD. The particle birth step generates new particles and is then used in the prediction step. A resampling step is added after the update step to prevent degeneration and control the maximum number of particles. The pyramid subspace division is used in the update step to distinguish visible space and improve computational efficiency. The voxel subspace division is used in the resampling step to realize efficient and uniform particle resampling. Details about the SMC-PHD filtering procedure in our map can be found in Section V. The filtered result is particles with position and velocity states. Then the map output can be calculated with the particles into two forms designed for motion planning. The first form is the current occupancy status, and the second is the prediction of future occupancy status. An initial velocity estimation procedure is introduced to reduce the noise in mapping. Details about the output and initial velocity estimation are presented in Section VI.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-B System Overview", "weight": 1.0} -->

The particles used in all the procedures are stored in the voxel subspaces.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Mapping with Dual Structure", "weight": 1.0} -->

This section presents the core procedures to build our map with the dual-structure space divisions, including prediction, update, particle birth, and resampling steps. The prediction and the particle birth are conducted in space $\mathbb{M}$. In the update step, the pyramid subspaces ${\mathbb{P}}_{i}$ are utilized to update the point objects' PHD efficiently. The voxel subspaces ${\mathbb{V}}_{i}$ are adopted in the resampling step.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-A Prediction", "weight": 1.0} -->

The prediction step predict the prior PHD of $\text{X}_{k|{k - 1}}$ and the general form has been described in Section III-D. In our map, the motion model of a single point object is defined by the constant velocity (CV) model, then a point object ${\mathbf{x}}_{k}$ that survived from $k - 1$ is predicted: where $\mathbf{I}$ is the identity matrix and $\mathbf{ξ}$ is the noise. The noise is supposed to obey a Gaussian distribution with a covariance $\mathbf{Q}$, which is ${\mathbf{ξ}} \sim {\mathcal{N}{(0,{\mathbf{Q}})}}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-A Prediction", "weight": 1.0} -->

Then the state transition density in Equation turns to a Gaussian probability density: Thus, from Equation to, $\pi_{k|{k - 1}}{(\left. {\mathbf{x}}_{k} \middle| {\overset{\sim}{\mathbf{x}}}_{k - 1}^{(i)} \right.)}$ can be sampled by particles using the Gaussian probability density, and ${\overset{\sim}{\mathbf{x}}}_{s,{k|{k - 1}}}^{(i)}$ in Equation is given by where $\mathbf{u}$ is a noise sampled from $\mathcal{N}{(0,{\mathbf{Q}})}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-A Prediction", "weight": 1.0} -->

The weight and state of newborn particles in Equation are described later in Section V-C.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-B Update", "weight": 1.0} -->

The update step utilizes the measurement $\text{Z}_{k}$ to get the posterior PHD of $\text{X}_{k}$. Two major points are addressed in the update step. The first point is to tackle the limited FOV and the occlusion. Since the FOV of a sensor is usually limited, and the occlusion prevents observations to the area behind obstacles, $\text{Z}_{k}$ can only be in the visible space ${\mathbb{M}}^{f}$ defined in Section IV. The objects that do not belong to ${\mathbb{M}}^{f}$ are in an unknown area and should not be updated; otherwise, their existence probability will be falsely reduced.

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-B Update", "weight": 1.0} -->

The second point is to reduce the computational complexity. It should be noted that $\text{C}_{k}{({\mathbf{z}}_{k})}$ in Equation and is controlled by ${\mathbf{z}}_{k}$, and thus, for every $w_{k}^{(i)}$, $\text{C}_{k}{({\mathbf{z}}_{k})}$ can be shared for the same ${\mathbf{z}}_{k}$. Therefore, to calculate all the required $\text{C}_{k}{({\mathbf{z}}_{k})}$, the multiplication operation and PDF calculation calculation in should be performed $L_{k} \cdot M_{k}$ times, where $M_{k}$ is the cardinality of $\text{Z}_{k}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-B Update", "weight": 1.0} -->

In addition, considering the summation operations in Equation and, another $L_{k} \cdot M_{k}$ times of multiplication, division and PDF calculation operations should be performed. The algorithmic complexity is $O{({L_{k}M_{k}})}$. In an unknown environment, there could be many obstacles and over a million particles can be required to approximate the states of the point objects. Hence, $L_{k} \cdot M_{k}$ can be very large, and the efficiency of the map is not adequate. The following considers using the pyramid subspaces to reduce the complexity.

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-B Update", "weight": 1.0} -->

Considering the measurement noise of the commonly used point cloud sensors, such as depth camera and Lidar, the single object measurement likelihood $g_{k}{(\cdot)}$ can be assumed as a Gaussian distribution, which is where ${f_{R}{({\mathbf{x}}_{k})}} = {\left\lbrack {\mathbf{I}}_{3 \times 3},0_{3 \times 3} \right\rbrack \cdot {\mathbf{x}}_{k}}$ since the measurement is only position. Unlike the prediction covariance $\mathbf{Q}$, the measurement covariance $R{({\mathbf{x}}_{k})}$ is usually not constant but related to the distance $d_{k}$ of the obstacle in regular sensor models.

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-B Update", "weight": 1.0} -->

With the coordinates in the sphere coordinate system, the covariance turns to ${R{({\mathbf{x}}_{k})}} = {\rho^{2}{(r_{k})}{\mathbf{I}}_{3 \times 3}}$ and $g_{k}{(\left. {\mathbf{z}}_{k} \middle| {\mathbf{x}}_{k} \right.)}$ can then be rewritten as where $z_{k,i}$ and $p_{k,i}$ are the single-axis position of a measurement and an object, respectively, at time $k$, which are described in and.

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-B Update", "weight": 1.0} -->

{\mathbf{z}}_{k} \middle| {\mathbf{x}}_{k} \right.)}} \leq \epsilon \approx 0$. Note the formula in the square root symbol in Eq. or should be in the range $\lbrack 0,1\rbrack$, which generally holds given real-world sensor parameters and robot size. Special cases when $\theta_{v}$ is near $\pi$ or $\rho{(r_{k})}$ is very large can make the condition invalid. Then the strategy of increasing $r_{min}$ or decreasing $\theta_{v}$ in the map can be adopted to make the condition valid. The strategy increases the sphere model size or decreases the pyramid number, and thus, sacrifices part of the space to be updated.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-B Update", "weight": 1.0} -->

If the measurement variances on each axis are not identical, the upper envelope of the variances can be taken as $\rho{(r_{k})}$, and the above inference still holds. If the measurement errors on each axis are not independent, Equations to cannot hold but the derived result can be used as an approximation to determine $n$. In the following context, we suppose the measurement errors on each axis are independent.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-C Particle Birth", "weight": 1.0} -->

Following the method, we generate newborn particles with measurement points $\text{Z}_{k}$. Since $\text{Z}_{k} \in {\mathbb{M}}_{f}$, the newborn particles are also in ${\mathbb{M}}_{f}$. For measurement point ${\mathbf{z}}_{k} \in \text{Z}_{k}$, we generate particles with a number of $L_{b}$. Then the number of newborn particles in total is $M_{k}L_{b}$. The position of each newborn particle is sampled from the Gaussian noise model in Eq.. Normally, the velocity of the newborn particle is randomly sampled in a feasible velocity range. However, this random sampling leads to heavy noise, and the convergence speed is slow.

<!-- chunk {"id": "body-0092", "role": "body", "section": "V-C Particle Birth", "weight": 1.0} -->

Thus we sample the velocity of each newborn particle through an initial velocity estimation method, which is described in Section VI-A and VI-B. The weight of these particles are set to be $\frac{v_{k|{k - 1}}^{b}}{M_{k}L_{b}}$, where $v_{k|{k - 1}}^{b} = {\int{\gamma_{k|{k - 1}}{({\mathbf{x}}_{k})}{d{\mathbf{x}}_{k}}}}$ is a parameter that controls the expected number of newborn objects.

<!-- chunk {"id": "body-0093", "role": "body", "section": "V-C Particle Birth", "weight": 1.0} -->

According to, the weight of the newborn particle is calculated separately in the update step. Then the weight update Equations and are reformed to represent the survived particles and the newborn particles separately: where $L_{s,k}^{{\mathbb{A}}^{{\mathbf{z}}_{k}}} \leq L_{k}^{{\mathbb{A}}^{{\mathbf{z}}_{k}}}$ is the number of survived particles whose activation space includes ${\mathbf{z}}_{k}$. $w_{b,{k|{k - 1}}}^{(j)}$ is the prior weight of the newborn particle and is $\frac{v_{k|{k - 1}}^{b}}{M_{k}L_{b}}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "V-D Resampling", "weight": 1.0} -->

Then the resampling is conducted by rejection sampling in each voxel subspace. The voxel subspace rather than the whole map is used. The reason is that if an area contains only low-weight particles, rejection sampling in the whole map may reject all these particles and decrease the occupancy probability of the area falsely. Let $L_{max}^{\mathbb{V}}$ and $L_{max}$ denote the allowed maximum number of particles in a voxel subspace and in the map, respectively, after resampling. $L_{max} = {L_{max}^{\mathbb{V}}N_{v}}$. Then the number of particles after resampling is The weight of the particles in ${\mathbb{V}}_{j}$ after resampling is identically

<!-- chunk {"id": "body-0095", "role": "body", "section": "Extensions in Mapping", "weight": 1.0} -->

This section proposes some important extension modules. Firstly, the initial velocity estimation module for newborn particles and a mixture model composed of a static model and a constant velocity model are proposed to reduce the noise in mapping. Then the occupancy status estimation and future status prediction modules, which generate the output designed for motion planning, are expressed. Finally, several useful extra extensions are discussed.

<!-- chunk {"id": "body-0096", "role": "body", "section": "VI-A Initial Velocity Estimation", "weight": 1.0} -->

The particle-based maps model the obstacles as point objects. This model is very friendly with particle-based tracking but works only at the sub-object level, which will cause non-negligible noise when the obstacle has a relatively large volume. Specifically, the noise is caused by the false update of the particles. Fig. 4 (a) illustrates the false update. The false update leads to many particles with a large weight but a wrong velocity, and further causes heavy noise in predicting the occupancy status of the area out of the FOV or at a future time. When the velocity of the newborn particle is randomly generated, the particle false update problem occurs frequently.

<!-- chunk {"id": "body-0097", "role": "body", "section": "VI-A Initial Velocity Estimation", "weight": 1.0} -->

To alleviate the problem and reduce noise, we add an object-level estimation by considering initial velocities for the newborn particles. The procedures to acquire the initial velocities from two adjacent point clouds are shown in Fig. 4 (b). The point cloud that obviously belongs to static obstacles, like the ground, is segmented by considering the height dimension and assigned zero velocity. The rest point cloud is clustered, and the result clusters are matched with the clusters extracted from the last frame. Then the velocity of each cluster can be estimated by differentiating the position of the matched clusters' centers. We use the Euclidean cluster extraction based on k-d tree for clustering and the Kuhn-Munkras (KM) algorithm for matching. In the matching process, the position of the cluster center and the number of points in the cluster are used as features. If a cluster at time $k$ cannot be matched, this cluster is regarded as a new obstacle, and no velocity estimation result is assigned.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VI-A Initial Velocity Estimation", "weight": 1.0} -->

The velocity estimated by position differentiating between two adjacent inputs is quite noisy because of three main reasons. The first reason is that the position error of the point cloud measurement is amplified and propagated to the velocity estimation by differentiating. The second reason is that the position of a cluster center varies when using point clouds observed from different angles, and the third is that the clustering and matching result might contain many errors in complex environments. We have assumed that the measurement noise of the point cloud is Gaussian noise. Thus the noise caused by the first reason is still Gaussian noise. However, the noise caused by the latter two reasons can be very random. Therefore, the estimated velocity cannot be regarded as the velocity measurement and utilized in the update step. We thus adopt this estimated velocity as a reference of initial particle velocities in the particle birth step on the basis of a mixture model. Details are presented in Section VI-B.

<!-- chunk {"id": "body-0099", "role": "body", "section": "VI-B Mixture Model", "weight": 1.0} -->

To further reduce the noise caused by the false update and model static objects better, we adopt a mixture model. The mixture model supposes the state of a point object is the combination of two components, i.e., ${\mathbf{x}}_{k} = {{\lambda_{1}{\mathbf{x}}_{k,d}} + {\lambda_{2}{\mathbf{x}}_{k,s}}}$. $\lambda_{1}$ and $\lambda_{2}$ are weight coefficients that satisfy ${\lambda_{1} + \lambda_{2}} = 1$. ${\mathbf{x}}_{k,d}$ is a dynamic object state component. ${\mathbf{x}}_{k,s}$ is a static object state component with zero velocity. Since the environment is unknown, the value of $\lambda_{1}$ and $\lambda_{2}$ should not be fixed but should be updated in the filtering process.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VI-B Mixture Model", "weight": 1.0} -->

We assume that the objects in one voxel subspace, a small subspace, have the same weight coefficients. In each voxel subspace, the dynamic object states and the static object states can be regarded as two independent RFSs, $\text{X}_{d}^{({\mathbb{V}})}$ and $\text{X}_{s}^{({\mathbb{V}})}$, respectively. Then $\lambda_{1}$ and $\lambda_{2}$ is estimated by the ratio between $|\text{X}_{d}^{({\mathbb{V}})}|$ and $|\text{X}_{s}^{({\mathbb{V}})}|$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "VI-B Mixture Model", "weight": 1.0} -->

In the particle birth step, the velocities of the newborn particles are assigned based on $\lambda_{1}$ and $\lambda_{2}$ in the corresponding voxel subspace, and the initial velocity estimation results in Section VI-A. If a measurement point is labeled static, e.g., the ground, in the initial velocity estimation procedure, the velocities of the particles generated from this point are all zero. Otherwise, the mixture model is used. The number of dynamic particles generated from a measurement point is $\lambda_{1}L_{b}$, and the number of static particles is $\lambda_{2}L_{b}$. According to the discussion of estimation noise in Section VI-A, the velocities of dynamic particles are composed of two parts: velocities sampled from a Gaussian distribution and random velocities. Since real-world sensors usually contain heavy noise, we set a large variance for the Gaussian distribution, and the particles with random velocities take $0.5\lambda_{1}L_{b}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "VI-B Mixture Model", "weight": 1.0} -->

If too few particles exist in the voxel subspace where the measurement point belongs, e.g., the situation when the voxel subspace is observed for the first time, an initial guess of $\lambda_{1} = \lambda_{2} = 0.5$ is used.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VI-C Occupancy Status Estimation", "weight": 1.0} -->

At an arbitrary point $\mathbf{p}$ in the map, the occupancy status is estimated by the cardinality expectation of point objects in a small neighborhood space of $\mathbf{p}$. Assume the point objects representing an obstacle are uniformly distributed in the space occupied by the obstacle and has no overlap. The distance between two adjacent point objects is $l'$. Then, in a cubic neighborhood space with side length $l'$ and centered by $\mathbf{p}$, there should be either one or no point object. In our case, the point cloud is pre-filtered by a voxel filter with resolution $Res$. Thus, $l' = {Res}$. Denote the cubic neighborhood space by ${\mathbb{V}}_{p}$ and the RSF composed of the point objects in ${\mathbb{V}}_{p}$ by $\text{X}_{k}^{{\mathbb{V}}_{p}}$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VI-C Occupancy Status Estimation", "weight": 1.0} -->

According to Equation and, the expectation of the cardinality of $\text{X}_{k}^{{\mathbb{V}}_{p}}$ is calculated with which is the weight summation of particles in ${\mathbb{V}}_{p}$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VI-C Occupancy Status Estimation", "weight": 1.0} -->

If $l > l'$, the estimated point object number $\mathbf{E}{\lbrack{|\text{X}_{k}^{({\mathbb{V}}_{i})}|}\rbrack}$ can be larger than one even if the estimation has no error. If ${\mathbf{E}{\lbrack{|\text{X}_{k}^{({\mathbb{V}}_{i})}|}\rbrack}} > 1$, ${P_{occ}{({\mathbb{V}}_{i})}} = 1$ is adopted. With the occupancy probability, a probability threshold can then be used to get a binary occupancy status, i.e., occupied or free. Fig. 5 shows an example occupancy estimation result in a scenario with a static obstacle and a dynamic obstacle. The voxelized map is shown in Subfigure (d).

<!-- chunk {"id": "body-0106", "role": "body", "section": "VI-C Occupancy Status Estimation", "weight": 1.0} -->

It should be noted that this voxelized map doesn't suffer from the grid size problem because the mapping process is realized in the continuous space.

<!-- chunk {"id": "body-0107", "role": "body", "section": "VI-D Future Occupancy Status Prediction", "weight": 1.0} -->

Predicting the future occupancy status is very useful for motion planning in dynamic environments. In our DSP map, the future occupancy status prediction is fulfilled by predicting the position of the particles according to the motion model in and, and then using and for occupancy status estimation. Fig. 6 presents the future occupancy estimation results of the map shown in Fig. 5. The occupancy status of the static obstacle, the tree, almost stays the same in each plot. The occupied position of the dynamic obstacle, the pedestrian, is predicted to move down with the CV model. The occupied grids are spreading, and their occupancy probabilities are getting lower as the prediction time increases. The reason is the uncertainty in velocity estimation, which is reflected by the variance of particles' velocities. The estimation uncertainty also causes noise in other parts of the plots. Since future occupancy status prediction in dynamic environments has inevitable uncertainty, the predicted occupancy probability can be used as the risk in motion planning algorithms.

<!-- chunk {"id": "body-0108", "role": "body", "section": "VI-E DSP Static Map", "weight": 1.0} -->

By assuming the point objects as static objects and using only the static model described in Section VI-B, the DSP map turns to a static map, named the DSP-Static map. In this case, the number of particles used in this map can be very small since the velocity dimension is not considered, which means the DSP-Static map is more computationally efficient. Compared to the voxel map for static environments, the DSP-Static map is continuous and free from the voxel size problem. In the experiment section, the DSP-Static map is also tested.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Implementation", "weight": 1.0} -->

This section describes an implementation of the DSP map. The implementation includes the data structure to realize subspace division and particle storage, and the specific algorithms used to build the DSP map.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VII-A Data Structure", "weight": 1.0} -->

The number of particles in the map can be up to one million. Thus, storage and operation of the particles are important to efficiency. Three techniques are utilized to improve efficiency: 1) The voxel subspaces are used to store particles while the pyramid subspaces only store the indexes of particles; 2) Large arrays with preallocated size rather than unordered sets, which represent RFSs natively, are used to store elements in an RFS; 3) The operations of adding and deleting particles are simplified using a flag variable. The first technique is to reduce memory consumption, while the second is to avoid dynamic memory allocation and increase the cache hit rate. The last technique is employed to simplify operations on particles. Detailed data structure can be found in Appendix D.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VII-B Mapping Algorithms", "weight": 1.0} -->

A flowchart showing the order of the algorithms used for mapping is presented in Fig. 7. After the input point cloud is pre-filtered by a voxel filter with resolution $Res$ and transformed to the map frame, two threads are opened to run the particle initial velocity estimation in parallel with prediction, update and resampling. Resampling, occupancy estimation and mixture model coefficients calculation are conducted in one loop to improve efficiency. Future occupancy status prediction is not shown but is realized by predicting particle states to more future times in the prediction step. Detailed algorithms can be found in Appendix E.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

This section first evaluates the velocity estimation precision of the DSP map since velocity estimation ability is a major difference between static maps and dynamic maps. Then the DSP map is tested with different parameters to evaluate the effect of the parameters on mapping performance and identify the best parameter values. With the identified parameter values, the mapping performance is further compared with existing works in different simulation worlds with different resolutions. To test the practicality of using the DSP map on robotics platforms, we also show computational efficiency comparison results on an NVIDIA Jetson board. Finally, a demo of using this map for drone obstacle avoidance is presented.

<!-- chunk {"id": "body-0113", "role": "body", "section": "VIII-A Velocity Estimation", "weight": 1.0} -->

The velocity estimation experiments were conducted with the data collected in an indoor testing field with the Nokov motion capture system. An Intel Realsense d435 camera was fixed at an edge of the testing field to collect the point cloud. Two pedestrians, wearing helmets with markers, walked around in the testing field, and their trajectories estimated by the motion capture system were recorded synchronously with the point cloud. The experiments can be divided into two groups. In the first group, the pedestrians tried to walk at a constant velocity. In the second group, the pedestrians walked randomly and freely. Fig. 8 (a) shows the data collection scenario.

<!-- chunk {"id": "body-0114", "role": "body", "section": "VIII-A Velocity Estimation", "weight": 1.0} -->

We compared the velocities estimated by four different point-cloud-based methods. The first method differentiates the center position of two matched clusters, and no filter is adopted. The matching is achieved by the KM algorithm. The second is a multi-object tracker realized by the KM algorithm and Kalman Filters (KF) with a CV model. The input of the KF is the center positions of matched clusters. The third method is the DSP map with the suffix "Random", whose newborn particles have random velocities. The fourth method is the DSP map with the suffix "Dynamic", whose newborn particles consider initial velocity estimation. Since our maps do not explicitly segment the objects, the state of a pedestrian was estimated with the particle cluster near the pedestrian's real position. Table II presents the estimation results of the two groups. We consider a pedestrian walking from one side of the testing field to another a tracklet. Over thirty tracklets were collected in each group. Fig. 9 shows the velocity estimation curves of a typical tracklet.

<!-- chunk {"id": "body-0115", "role": "body", "section": "VIII-A Velocity Estimation", "weight": 1.0} -->

Three metrics are used for evaluation. The root mean square error (RMSE) reflects the estimation precision evaluated with the mean of the velocity estimation distribution and the ground truth from the motion capture system. The Var. is the mean variance of the different axes on every point. The differentiating method outputs a single value rather than a distribution, and thus a dash is placed in its Var. in Table II. For a particle-based map, a large variance means the particles would disperse to a large scale of the area and cause much noise in the map. Mean Bhattacharyya distance (MBD) measures the similarity between the estimated and ground-truth velocity distribution. MBD considers both mean value and variance and is a composite metric. The results in Table II show that DSP-Dynamic performs best with all three metrics. The differentiated velocity has a large RMSE, and the error can be huge sometimes, as Fig. 9 shows. Using KF can reduce the error, but the Var. is over 30% larger than that of DSP-Dynamic, and the MBD is over 12% larger.

<!-- chunk {"id": "body-0116", "role": "body", "section": "VIII-A Velocity Estimation", "weight": 1.0} -->

Compared to DSP-random, DSP dynamic decreases over 14% on RMSE, over 68% on Var., and over 34% on MBD, showing the importance of the initial velocity estimation.

<!-- chunk {"id": "body-0117", "role": "body", "section": "VIII-B Mapping with Different Parameters", "weight": 1.0} -->

Inspired, we evaluated the occupancy mapping performance by assessing the binary classification results, i.e., free or occupied, of the voxel subspaces. The metrics include average precision, recall, F1-Score^22^2F1-Score $= \frac{{{2precision} \cdot r}ecall}{{precision} + {recall}}$ is a balanced metric of precision and recall., and time consumption of a complete mapping process. The tested parameters include maximum particle number $L_{max}$, the voxel size $Res$ of the voxel filter for the point cloud pre-process before mapping, the pyramid subspace angle $\theta$, and the voxel subspace size $l$. When $Res$ is larger, the measurement point number $M_{k}$ is smaller. Each parameter was tested with three levels. A full factorial experiment was conducted with data collected in the pedestrian street world (Fig. 8 (d)), where both static and dynamic obstacles exist. The world is built in the Gazebo^33^3Gazebo simulation software: simulation software.

<!-- chunk {"id": "body-0118", "role": "body", "section": "VIII-B Mapping with Different Parameters", "weight": 1.0} -->

A simulated IRIS quadrotor with a Realsense camera is controlled manually to collect point cloud and pose data for mapping.

<!-- chunk {"id": "body-0119", "role": "body", "section": "VIII-B Mapping with Different Parameters", "weight": 1.0} -->

To generate the ground truth occupancy map, we densely and uniformly sampled points from the mesh surfaces of the static objects in the world and generated a Euclidean Distance Field (EDF) for the objects using the sampled points. The EDF changes caused by pedestrians are updated online at each evaluation step using the mesh and pose of the pedestrians. A voxel subspace was considered occupied if the distance value at the voxel's center position was no larger than $\frac{l}{2}$ and free otherwise. We also added a label array to distinguish the observed and unobserved labels of the voxels. The array is updated using the ray-casting approach with dense rays. Only the observed voxels were considered in the evaluation.

<!-- chunk {"id": "body-0120", "role": "body", "section": "VIII-B Mapping with Different Parameters", "weight": 1.0} -->

The result is shown in Fig. 10 (a). When $L_{max}$ increases from 0.8 million to 2.4 million, the precision does not have a noticeable change, while the average time consumption increases from 50 ms to 160 ms. The recall rises from 0.22 to 0.30 when $L_{max}$ increases to 1.6 million but almost remains unchanged when $L_{max}$ increases further. The F1-Score has the same trend as the recall. Raising $Res$ leads to fewer measurement points in the point cloud and shows a positive effect on precision but a negative effect on recall. The balanced metric F1-Score reaches the maximum value of 0.38 when $Res$ is 0.1 m. The time consumption decreases as $Res$ increases.

<!-- chunk {"id": "body-0121", "role": "body", "section": "VIII-B Mapping with Different Parameters", "weight": 1.0} -->

The pyramid subspace angle $\theta$ slightly affects precision, recall, and F1-Score. The F1-Score increases merely 0.005 when $\theta$ grows from one degree to five degrees. Meanwhile, the time consumption increases from 67 ms to 144 ms. The voxel subspace size $l$ positively correlates to all the metrics. When $l$ is larger, the number of voxels to classify is less, and the occupancy status of a voxel is easier to determine because more measurement points and particles are contained in one voxel. As a result, the precision, recall, and F1-Score all improve. However, a larger voxel size is usually unfavorable in motion planning. The time consumption rises because the particle operations in Algorithm 1 are slower with more particles in one voxel subspace.

<!-- chunk {"id": "body-0122", "role": "body", "section": "VIII-B Mapping with Different Parameters", "weight": 1.0} -->

To achieve the best F1-Score with an acceptable time consumption (about 100 ms), $L_{max} = {1.6 \times 10^{6}}$, ${Res} = 0.1$, and $\theta = 3^{\circ}$ are chosen. We further compare the performance of our map with other maps using different resolutions in the following experiment.

<!-- chunk {"id": "body-0123", "role": "body", "section": "VIII-C Mapping Performance Comparison", "weight": 1.0} -->

In this experiment, we compared our DSP map with a static local occupancy map named Ewok and a state-of-the-art particle-based dynamic occupancy map named K3DOM. K3DOM is the only 3D dynamic occupancy map with a released code currently. We also compared our map with two variants: one uses newborn particles with random velocities and considers the constant velocity model only, i.e., extensions in Section VI-A and VI-B are not adopted; another uses static newborn particles and considers the static motion model, i.e., the extension in Section VI-E. To distinguish the variants, we call our map with particle initial velocity estimation and mixture model DSP-Dynamic map, and the variants DSP-Random map and DSP-static map, respectively.

<!-- chunk {"id": "body-0124", "role": "body", "section": "VIII-C Mapping Performance Comparison", "weight": 1.0} -->

K3DOM runs on NVIDIA RTX 2060 GPU, and the rest maps run on AMD Ryzen 4800HS CPU in the tests. The map size $(l_{x},l_{y},l_{z})$ is (10 m, 10 m, 6 m). The rest parameters in K3DOM and Ewok remain the same as the original settings in the released code. No voxel filter is used for point cloud pre-processing in K3DOM and Ewok to reach their best performances. In DSP map and its variants, the initial weight of the particle is $0.0001$. Three different voxel sizes, from 0.1 m to 0.3 m, were tested in the simulation worlds shown in Fig. 8 (b) to (d). Using different occupancy probability thresholds, which determine the binary status, i.e., occupied or free, we draw precision-recall curves in Fig 10 (b). Snapshots of different maps can be found in Fig. 11 and Fig. 12.

<!-- chunk {"id": "body-0125", "role": "body", "section": "VIII-C Mapping Performance Comparison", "weight": 1.0} -->

In Fig 10 (b), a larger area under the curve (AUC) suggests a better overall performance in classifying the occupancy status with different thresholds. The specific AUC values are presented in Table III. The DSP-Dynamic map has the largest AUC in the two worlds with pedestrians and a comparable AUC with Ewok and DSP static map in the static forest world. When the voxel size is 0.1 m and 0.2 m, the recall of Ewok and K3DOM is relatively low because of the gaps and inconsistencies in high-resolution grid maps. Red dashed boxes in Fig. 11 illustrate the gaps and inconsistencies. In Fig. 12, the areas in the red ellipses show that Ewok has noticeable trail noise, which can lower the precision, when the voxel size is 0.3 m. The dynamic occupancy map K3DOM has less trail noise. In comparison, our DSP-Dynamic map doesn't suffer from gaps, inconsistencies, or trail noise.

<!-- chunk {"id": "body-0126", "role": "body", "section": "VIII-C Mapping Performance Comparison", "weight": 1.0} -->

DSP-Random, which doesn't have initial velocity estimation and uses only the CV model, has obvious noise in the area out of FOV, especially when representing static obstacles. Column (e) in Fig. 11 shows the noise. Consequently, the AUC of DSP-Random is the smallest in the forest world. DSP-Static adopts only the static motion model and achieves the best AUC in the forest world when the voxel size is 0.2 m and 0.3 m. However, it cannot predict the future occupancy status of dynamic obstacles, and the AUCs in the worlds with pedestrians are smaller than DSP-Dynamic. The red rectangles in Column (f) in Fig. 11 and Fig. 12 show the predicted occupancy status of a pedestrian out of the FOV in the DSP-Dynamic map.

<!-- chunk {"id": "body-0127", "role": "body", "section": "VIII-C Mapping Performance Comparison", "weight": 1.0} -->

Table IV shows the best F1-Score, i.e., the highest classification performance that each map reaches with different probability thresholds in Fig 10 (b). When the testing scenario is the forest world, and the voxel size is 0.3 m, the DSP-Dynamic map's score is slightly lower than the DSP-Static map's. In all other situations, DSP-Dynamic has the highest best F1-Score. Note in the pedestrian square world, where only dynamic obstacles exist, the dynamic map K3DOM has a lower best F1-Score than the static map Ewok when the voxel size is 0.3 m. The reason is that although Ewok has a low precision due to its heavy trail noise, its recall rate is higher than K3DOM's. However, from Table III, it can be seen that the AUC, which evaluates the overall classification performance when using different occupancy probability thresholds, of K3DOM is still higher than that of Ewok.

<!-- chunk {"id": "body-0128", "role": "body", "section": "VIII-C Mapping Performance Comparison", "weight": 1.0} -->

The average F1-score and AUC of our DSP-Dynamic map in different worlds with different resolutions are 0.46 and 0.47, respectively. In comparison, the average F1-score and AUC of the existing particle-based dynamic occupancy map K3DOM are 0.33 and 0.37, respectively. Our map increases the F1-score by 39.4% and AUC by 27.0%. If only the two worlds that contain dynamic obstacles are considered, the average F1-score and AUC increase from 0.24 to 0.39 (62.5% increase) and 0.27 to 0.40 (48.1% increase), respectively.

<!-- chunk {"id": "body-0129", "role": "body", "section": "VIII-D Robotics Platform Efficiency Tests", "weight": 1.0} -->

This section first compares the efficiency of Ewok, K3DOM, and our DSP map (with particle initial velocity estimation and mixture motion model) on NVIDIA Jetson Xavier NX, which is a small computing board widely used on robotics platforms. Xavier NX has a 384-core NVIDIA Volta GPU with 48 Tensor Cores and a 6-core NVIDIA Carmel ARM v8.2 CPU. K3DOM runs on the GPU, and the rest maps run on the CPU. The average time consumption of each map with different voxel sizes is shown in Fig. 13. The map size in the test is (10 m, 10 m, 6 m).

<!-- chunk {"id": "body-0130", "role": "body", "section": "VIII-D Robotics Platform Efficiency Tests", "weight": 1.0} -->

When the voxel size is 0.1 m, our DSP map is the fastest. The existing particle-based dynamic occupancy map K3DOM is 4.5 times slower than the DSP map. The static map Ewok runs fastest when the voxel size is 0.2 m or 0.3 m. K3DOM is the second fastest, and our DSP map is the slowest. However, with the results in Fig. 10 (a), we can further raise the computational efficiency of our map by sacrificing a little performance on the F1-Score. Fig. 10 (a) indicates that decreasing the pyramid subspace angle $\theta$ from $3^{\circ}$ to $1^{\circ}$ can reduce the computation time while the F1-Score drops merely 1%. In addition, increasing the filter voxel size $Res$ from 0.1 m to 0.15 m can also reduce the computation time, and the F1-Score decreases 12% accordingly.

<!-- chunk {"id": "body-0131", "role": "body", "section": "VIII-D Robotics Platform Efficiency Tests", "weight": 1.0} -->

If $\theta = 1^{\circ}$ is used in the tests on Xavier NX, the DSP map's computation time is only 0.56 times that of K3DOM's when the voxel size is 0.2 m and is close to K3DOM's when the voxel size is 0.3 m. If ${Res} = {0.15m}$ is further adopted, the DSP map's computation time is shorter than the K3DOM's for all tested voxel sizes.

<!-- chunk {"id": "body-0132", "role": "body", "section": "VIII-D Robotics Platform Efficiency Tests", "weight": 1.0} -->

We also tested the computation efficiency of our DSP map on two other onboard computers for robotics platforms: an Intel NUC with a Core i7-10710u CPU and an Up core board with an Intel Atom x5-z8350 CPU. When $\theta = 1^{\circ}$ and ${Res} = 0.15$ m are adopted, and the voxel size is $0.2$ m, the average time consumption on the two boards is about 133 ms and 254 ms, respectively. For robotics obstacle avoidance tasks without fast movement, a smaller map can be used to reduce time consumption. For example, when the map size is reduced to (8 m, 8 m, 3 m), the average time consumption on the Up core board is below 150 ms.

<!-- chunk {"id": "body-0133", "role": "body", "section": "VIII-D Robotics Platform Efficiency Tests", "weight": 1.0} -->

In Appendix B, we present a test with omnidirectional and multi-channel Lidar point cloud data. The time consumption is about two times when using point cloud data from the Realsense camera, which has a limited FOV. Improvements in computational efficiency will be conducted further to realize real-time mapping with multi-channel Lidars.

<!-- chunk {"id": "body-0134", "role": "body", "section": "VIII-E Applications", "weight": 1.0} -->

Fig. 14 presents several snapshots of building the DSP-Dynamic map in different scenarios. The localization was realized by a Realsense T265 tracking camera, and the point cloud was from a Realsense d435 camera. To further demonstrate the effectiveness and efficiency of our map in robotic systems. We deployed the DSP-Dynamic map on a mini quadrotor with a weight of only 320 grams and utilized a sampling-based motion planning method to realize obstacle avoidance in environments with static and dynamic obstacles. The method samples motion primitives and evaluates the collision risk of each motion primitive with the current and predicted particles in the DSP-Dynamic map. Details can be found. The point cloud was collected from a Realsense d435 camera, and everything, including mapping and motion planning, was performed on the CPU of a low-cost Up core computing board. Fig. 15 shows the testing scenarios. The testing demos can be found at Figure 15: The testing scenarios for obstacle avoidance. (a) and (b) are dynamic environments. (c) is a static environment. Red rectangles outline the quadrotor.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents a novel dual-structure particle-based 3D local map, named DSP (dynamic) map, that allows continuous occupancy mapping of dynamic environments. Voxel subspaces and pyramid-like subspaces are adopted to achieve efficient updates in continuous space. The initial velocity estimation and a mixture model are considered to reduce noise. Experiments show that the DSP map can increase the dynamic obstacle velocity estimation performance by over 30% on MBD, compared to other tested point-cloud-based methods. In occupancy status estimation tests, the DSP map increases the F1-Score of the state-of-the-art particle-based occupancy map from 0.33 to 0.46 (39.4% increase) and the AUC from 0.37 to 0.47 (27.0% increase) on average. Furthermore, efficiency tests and a real-world application demo demonstrated the broad prospect of this map in obstacle avoidance tasks of small-scale robotic systems. Future works will consider two main points. The first is to introduce semantic information to this map to better identify and model different obstacles and further predict their future states with multiple hypotheses.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The second is to connect this dynamic local map to a global static map to achieve global mapping in dynamic environments.
