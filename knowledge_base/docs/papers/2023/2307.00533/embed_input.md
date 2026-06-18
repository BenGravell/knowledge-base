<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Representing Robot Geometry as Distance Fields: Applications to Whole-Body Manipulation

Topics include Robot kinematics, Signed distance, Distance queries, Robot manipulation, Collision avoidance, Trajectory optimization, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Represents articulated robot geometry with differentiable distance fields built from per-link signed-distance models and kinematic structure. This gives optimization-based manipulation and collision avoidance access to smooth robot-surface distance queries in task and joint spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we propose a novel approach to represent robot geometry as distance fields (RDF) that extends the principle of signed distance fields (SDFs) to articulated kinematic chains. Our method employs a combination of Bernstein polynomials to encode the signed distance for each robot link with high accuracy and efficiency while ensuring the mathematical continuity and differentiability of SDFs. We further leverage the kinematics chain of the robot to produce the SDF representation in joint space, allowing robust distance queries in arbitrary joint configurations. The proposed RDF representation is differentiable and smooth in both task and joint spaces, enabling its direct integration to optimization problems. Additionally, the 0-level set of the robot corresponds to the robot surface, which can be seamlessly integrated into whole-body manipulation tasks. We conduct various experiments in both simulations and with 7-axis Franka Emika robots, comparing against baseline methods, and demonstrating its effectiveness in collision avoidance and whole-body manipulation tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In robotics, the representation of a robot commonly relies on low-dimensional states, like joint configuration and end-effector poses. However, this low-dimensional representation lacks internal structure details and is insensitive to external factors, limiting the ability to interact with the environment and respond to real-world. To handle this problem, some geometric representations have been proposed, like primitives and meshes, with various applications. However, they either make simplified assumptions or require significant computational resources to obtain a detailed model.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural idea for handling this problem is to encode the geometry of the robot as signed distance fields (SDFs). Several studies in computer vision and graphics have shown the advantages of such a representation. Not only does it offer continuous distance information but also exhibits query efficiency. \\colorblackHowever, despite several robot representations that can be transformed into SDFs, they are either inaccurate (sphere), computationally complex (mesh), or memory-consuming (voxel SDF). Besides, the SDF representation for articulated objects remains a challenge due to the nonlinear and high dimensionality.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

blackFollowing existing robot representations like spheres and meshes, we exploit the kinematic structure to represent the distance fields of robots. In contrast to existing methods that encode the robot shape as its joint angle configuration, we adopt a configuration-agnostic approach during the learning phase and utilize the kinematic chain of the robot during the inference phase. This approach simplifies the problem by learning the SDF for each robot link, reducing the dimensionality, and making it robust and reliable for different joint values. During the inference phase, the kinematic information is used to retrieve the SDF values. We utilize Bernstein polynomials as the basis function to represent SDF for each link of the robot for storage and computation efficiency, with facilitated differentiability in task space and joint angle space.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Representing robot geometry as distance fields (RDF) has multiple advantages. First, it provides a continuous and smooth distance representation, granting easy access to derivatives. This characteristic is particularly well-suited for robot optimization problems such as motion planning and collision avoidance. Further, RDF representation encodes the robot geometry implicitly and decouples from spatial resolutions, enabling whole-body manipulation at any scale without explicitly defining surface points. Finally, RDF allows computationally efficient and precise distance query, which is crucial for various robot applications that require precise perception and quick response, especially in dynamic environments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We experimentally demonstrate the capabilities of our RDF in three aspects. First, we provide a quantitative comparison of the produced distance fields against other representative methods, showing the advantage of our approach. Then, we conduct collision avoidance experiments to show the real-time control performance. Finally, we present a novel formulation that leverages the RDF representation for manipulation tasks requiring contact, by generalizing the robot's Jacobian matrix from its end-effector to the 0-level set of SDF. We demonstrate the effectiveness of this approach in a dual-arm lifting task, showing how our RDF representation can be seamlessly integrated into first and second-order optimization problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a simple and flexible structure that leverages Bernstein polynomials to encode SDFs, showing high accuracy and efficiency while ensuring continuity and differentiability.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proposed SDF representation is further extended to articulated robots by leveraging the kinematics chain, allowing robust interpolation/extrapolation to any joint configuration while keeping the above properties.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the effectiveness of our RDF representation in experiments and show how to integrate it into optimization problems for whole-body manipulation tasks without defining any points on the robot surface.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Learning Robot Geometry as Distance Fields", "weight": 1.0} -->

In this section, we present our approach to represent the robot geometry as distance fields. Specifically, we first encode the SDF of each robot link through concatenated Bernstein polynomials and then extend it to the whole body based on the robot kinematic chain.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Kinematic Transformation of SDFs", "weight": 1.0} -->

Consider a robot with $C$ degrees of freedom and $K$ links, characterized by joint angles ${\mathbf{q}} = {\{ q_{1},q_{2},\cdots,q_{C}\}}$ and shapes $\mathbf{\mathrm{\Omega}} = {\{\mathrm{\Omega}_{1},\mathrm{\Omega}_{2},\cdots,\mathrm{\Omega}_{K}\}}$. The distance field to represent the robot geometry is the minimum of all links SDFs, which can be written as

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Kinematic Transformation of SDFs", "weight": 1.0} -->

where $f_{\mathrm{\Omega}_{k}^{b}}$ is the SDF of link $\mathrm{\Omega}_{k}$ in the robot base frame.^22^2\\textcolorblackThe $\text{min}{( \cdot )}$ in might cause discontinuous gradient when the closest link changes. A differentiable smooth version of this function can be utilized to avoid this issue. The SDF value for point $\mathbf{p}$ in the robot base frame $f_{\mathrm{\Omega}_{k}^{b}}$ can be computed through the rigid transformation of SDFs, which involves transforming the query points as

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Kinematic Transformation of SDFs", "weight": 1.0} -->

where ${{{}_{}^{}{}_{}^{}}{({\mathbf{q}})}} \in {{\mathbb{S}}{\mathbb{E}}{}}$ denotes a matrix dependent on $\mathbf{q}$ that performs the transformation from the frame of the $k$-th link to the base frame of the robot. The computation of these transformation matrices can be achieved using the kinematics chain of the robot, typically represented by Denavit-Hartenberg parameters.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Representing SDFs using Bernstein polynomials", "weight": 1.0} -->

Basis functions have been widely used in encoding trajectories in robotics, such as in dynamical movement primitives (DMP) or probabilistic movement primitives (ProMP), see for a review. They provide a continuous, differentiable, and smooth representation of the trajectory, ensuring the encoded motion appears natural without abrupt changes. This compact parameterization also enables efficient storage and computation while accurately capturing complex motions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Representing SDFs using Bernstein polynomials", "weight": 1.0} -->

Drawing inspiration from these studies, we propose the adoption of geometric primitives, a three-dimensional extension of basis functions, to represent the SDF of each link of the robot. By leveraging basis functions with multivariate inputs, we aim to preserve the aforementioned advantages. In this work, we employ Bernstein polynomials, however, other types of basis functions could alternatively be considered, such as Radial Basis Functions (RBF) for infinite differentiability or Fourier basis functions for multiresolution encoding, see for a review.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Representing SDFs using Bernstein polynomials", "weight": 1.0} -->

The SDF $f_{\mathrm{\Omega}_{k}}$ for a point ${\mathbf{p}}^{k}$ described in the frame of the robot link $\mathrm{\Omega}_{k}$ can be represented as a weighted combination of N basis functions as

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Representing SDFs using Bernstein polynomials", "weight": 1.0} -->

in analytic form, where $t \in {\lbrack 0,1\rbrack}$ is a normalized location of the point. Consequently, the derivative of the $n$-th basis function can be expressed as

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Representing SDFs using Bernstein polynomials", "weight": 1.0} -->

and the derivatives of $\mathbf{\Psi}$ are analytically given by

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Representing SDFs using Bernstein polynomials", "weight": 1.0} -->

For $T$ data points denoted as ${\mathbf{P}} \in {\mathbb{R}}^{T \times 3}$ and their corresponding distance values denoted as ${\mathbf{f}} \in {\mathbb{R}}^{T}$, the weight tensor $\mathbf{w}$ can be learned through least square regression as ${\mathbf{w}}^{*} = {{({\mathbf{\Psi}^{T}\mathbf{\Psi}})}^{- 1}\mathbf{\Psi}^{T}{\mathbf{f}}}$, where $\mathbf{\Psi} \in {\mathbb{R}}^{T \times N^{3}}$ contains all basis functions and points in a concatenated form. Computing the inverse of large matrices can be computationally expensive and suffer from memory issues. Instead of a batch evaluation, a recursive formulation can be used, providing exactly the same result\\textcolorblack.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Representing SDFs using Bernstein polynomials", "weight": 1.0} -->

To do so, we define a new parameter ${\mathbf{B}} = {({\mathbf{\Psi}^{\top}\mathbf{\Psi}})}^{- 1}$ and process the data sequentially by sampling a small batch of points $\{\overset{\sim}{\mathbf{P}},\overset{\sim}{\mathbf{f}}\}$ and updating the learned weights when new data points become available. The whole process is depicted in Algorithm, and a 2D example is shown in Fig.. After obtaining the optimal weights ${\mathbf{w}}^{*}$, the distance can be decoded efficiently with during inference. Similarly, this efficiency also extends the gradients, thanks to the analytic form of the polynomial structure^33^3We refer readers to for details about basis functions encoding with multidimensional inputs..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To demonstrate the effectiveness of the proposed method, we conduct several numerical comparisons against baseline methods.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Implement details. We build the distance field for the Franka Emika Robot with 7 articulations and 9 links (the fingertips of the gripper are ignored). The superposition weights of Bernstein polynomials are separately trained for each robot link. Specifically, we assume a cubic volume around each link to sample training data. The positions of points inside the volume are normalized to $\lbrack 0,1\rbrack$ and points outside the volume are projected onto the boundary and the distance is approximated by summing the distances from the projected point to the boundary. All operations are implemented with the batch operation and run on an Nvidia GeForce RTX3060 GPU. The training data is generated following DeepSDF ^44^4we use the library mesh_to_sdf for implementation..

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Effectiveness of basis functions in encoding SDFs. We first compare the proposed Bernstein Polynomial (BP) method with two other representative state-of-the-art approaches: a volumetric-based method, TT-SVD which utilizes tensor decomposition to compress voxelized SDFs, and a neural network (NN) based method. We evaluate the Chamfer Distance (CD), inference time and model size. For the TT-SVD method, we set the maximum rank $R$ to 40. For the neural network, we found it could not represent the SDF well with the same number of data points we used ($2.56 \times 10^{5}$), so we additionally trained it with 10 times more data for a more detailed comparison. We report the result of our lightweight model (with 8 basis functions) and precise model (with 24 basis functions) in Table I. Our approach shows competitive accuracy and efficiency with a more compact structure. Although TT-SVD shows a lower mean CD, it exhibits a higher max CD, indicating sensitivity to high-frequency data. Besides, it represents discrete SDFs while our method is continuous and differentiable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We find BP and NN can encode the shape of the robot links accurately with similar CD. However, our method based on recursive ridge regression shows higher data efficiency. Additionally, our approach offers other benefits. The weights learned by BP correspond to the key points, which directly provide interpretable and controllable parameters. Besides, it also provides a simple and efficient way to compute analytical gradients by directly leveraging the derivatives of the basis functions. The continuity and smoothness of the gradient are also guaranteed by construction.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Quality of RDF. We further compare our approach with several common approaches to represent the geometry of the robot.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Spheres have closed-form signed distance functions and we use 55 spheres to approximate the robot. For meshes, we compute the signed distance by finding the closest vertex and normal, which is another widely used approach. The coarse mesh has 1,249 vertices while the precise mesh has 74,647 vertices. Following Neural-JSDF, we report the mean absolute error (MAE) and root mean square error (RMSE) for points near the robot surface (within 0.03m) and points far away (over 0.03m) in Table II.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The comparison between Neural-JSDF and other approaches demonstrates the importance of the kinematic chain (K.C.) in modeling accurate RDF. With our non-optimized implementation, the computation time is higher for our method, but it is still at the millisecond level, allowing real-time behavior with high frequency. Although coarse mesh has a more precise shape than spheres, it still fails to represent an accurate distance field, since the choice of closest point and normal estimation are usually inaccurate and noisy. Methods incorporating kinematic chain and SDF (NN $+$ K.C. and BP $+$ K.C.) improve the accuracy compared to primitive-based and mesh-based methods. The average MAE for these methods is about $1\text{mm}$, which is accurate enough for tasks that require establishing contacts with the environment. Figure also shows the distance and gradient produced by several methods, highlighting the smoothness of our approach.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Robot Experiments", "weight": 1.0} -->

In this section, we illustrate the effectiveness of our RDF representation through two dual-arm robot tasks: 1) Collision Avoidance: While a robot arm tries to reach a target, it must avoid colliding with another. 2) Dual-arm Lifting: Two robot arms collaborate to lift a large box that cannot be grasped conventionally. The objective is to plan a pair of joint configurations for both arms such that they can establish contact with the box by exploiting their whole bodies to reach and lift the box.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Collision Avoidance", "weight": 1.0} -->

In this section, we integrate the learned distance fields for collision avoidance, which is crucial in motion planning tasks. Specifically, we exploit an augmented quadratic Programming (QP) algorithm to ensure self-collision avoidance between two robot arms during task execution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Collision Avoidance", "weight": 1.0} -->

The self-collision avoidance experiments are conducted in both simulation and real-world scenarios. In simulation, the goal for both arms is to reach their respective target position while the right arm should actively avoid collision with the left arm. The real-world experiment is conducted with a reactive controller, where the left arm is manually moved by a human operator in gravity-compensated mode, serving as a dynamic obstacle for the right arm. For both experiments, we randomly sampled 256 points on the surface of the left arm as the input of RDF for the right arm and then used the minimal distance produced for self-collision avoidance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Collision Avoidance", "weight": 1.0} -->

We conducted simulation experiments 100 times, utilizing different initial states for both robot arms, and compared our proposed method with sphere-based, mesh-based and NN-based representations. Results are presented in Table III. The time cost represents the average time for solving the QP problem once. For Neural-JSDF, we observed large distance errors with unsuccessful results.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Collision Avoidance", "weight": 1.0} -->

As collision avoidance was established as a hard constraint in the QP controller, all methods exhibited collision-free behavior whenever the QP solver converged to a solution. Nevertheless, attributing to the accuracy and smoothness, our method demonstrated the highest success rate $({87\%})$ in reaching, as well as the lowest probability $({12\%})$ of not finding a solution for the QP solver, which also led to a shorter planning time. The left $1\%$ case is that the QP solver found a solution but the two arms blocked each other. The poor performance of mesh-based representation and neural networks indicates the importance of continuous gradient, which makes the optimizer find solutions more easily and more efficiently. Figures and depict the collision avoidance process in simulation and real-world, showing our method enables the robot arm to respond to the environment and avoid collisions (see also accompanying video).

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Dual-arm Lifting", "weight": 1.0} -->

In this experiment, our focus is on the manipulation of a large box using a dual manipulator, utilizing the whole surface of the last four links of the robot. Our underlying assumption is that the contact points on the object are already predetermined, and the robot has the freedom to establish contacts automatically based on the SDF representation without sampling any surface points on the robot.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Dual-arm Lifting", "weight": 1.0} -->

regularize the solution near the robot's initial configuration, and joint limit residuals ${\mathbf{r}}_{j}^{\text{max}}$ and ${\mathbf{r}}_{j}^{\text{min}}$ to consider joint angle limits, defined as

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Dual-arm Lifting", "weight": 1.0} -->

where ${{\mathbf{f}}{({\mathbf{p}},{\mathbf{q}})}} \in {\mathbb{R}}^{T}$ represents the spatial distance between points $\mathbf{p}$ and the robot surface at configuration $\mathbf{q}$. In this context, ${\mathbf{p}}_{c}$ represents predefined contact points on the object, while ${\mathbf{p}}_{i}$ denotes the points uniformly selected within the box for collision avoidance purposes. ${\mathbf{q}}_{\text{min}},{\mathbf{q}}_{\text{max}}$ are the physical joint limits and ${\mathbf{q}}_{\text{init}}$ is the robot initial joint configuration. The optimization is solved using the Gauss-Newton algorithm as

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Dual-arm Lifting", "weight": 1.0} -->

We optimize the problem in batch to accelerate the planning procedure with random initialized configurations. Trajectories from initial to goal configurations are interpolated through cubic splines. A joint impedance controller is adopted in conjunction with a smaller desired box size during the planning phase to generate sufficient force at contact points. The lifting action is accomplished by elevating the fourth joint of the robot, which is positioned immediately before the potential contact links.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Dual-arm Lifting", "weight": 1.0} -->

black We report the success rate among 50 planned joint configurations for both arms and the average planning time in Table IV. A configuration is considered successful if it respects all the termination conditions with the exact robot model. Since batch optimization is usually accompanied by a larger memory overhead, we only selected the sphere-based method and our lightweight model for comparison. Our method shows significant improvement in terms of both success rate and computation time, which is attributed to the more accurate robot model compared to the sphere-based representation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Dual-arm Lifting", "weight": 1.0} -->

black Methods Sphere-based BP (N=8) Success Rate 36% 77% Time (per valid configuration) 0.98 0.46
TABLE IV: Results for dual-arm lifting task.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Dual-arm Lifting", "weight": 1.0} -->

The experimental results of the real robot implementation are presented in Fig. V-B. In Experiments 1-3, the robot exhibits the capability to use its last four links to contact the object. These experiments provide empirical evidence of the generalization capability of the method across various poses. In experiments 4 and 5, the robot is constrained to utilize specific links for contacts. Specifically, the contact is limited to the sixth link in experiment 4, while in experiment 5, it is restricted to the seventh link. This restriction narrows down the valid solutions, requiring the robot to adapt its approach accordingly. The optimization problem is still able to find appropriate solutions. It can be attributed to the infinite resolution of the robot arm and the smooth representation provided by the distance field, which enables the optimization algorithm to navigate the constrained search space more effectively, leading to successful solutions even in scenarios with limited contact options.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we proposed a novel approach to represent the geometry of a robot as distance fields. We leveraged the kinematic structure of the robot to generalize configuration-agnostic signed distance functions that remain valid for arbitrary robot configurations, which enables more effective learning and more accurate inference of distance fields. The SDF for each link of the robot is represented by a combination of piecewise multivariate polynomials, ensuring interpretability, compactness and smoothness while remaining competitive in terms of efficiency and accuracy. The approach provides analytic derivatives that can directly be used for gradient-based (or higher-order) optimization techniques. Experiments in collision avoidance have shown the effectiveness of our representation. Furthermore, we have demonstrated how to integrate this representation into whole-body manipulation tasks, by defining cost functions based on the SDF of the robot.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are some limitations that should be acknowledged. First, the capability of basis functions to highly complex shapes has not been thoroughly investigated. Secondly, we simplified the lifting task by planning joint configurations, without considering the dynamic model. Finally, the representation could be further applied to other complex manipulation tasks, such as pushing and pivoting, by estimating the interaction forces between SDFs and formulating it as an optimization problem. We plan to explore this research direction in future work.
