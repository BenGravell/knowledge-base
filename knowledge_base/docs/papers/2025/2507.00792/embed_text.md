## Introduction

Modern robotics, computer graphics, and biomechanics often face the challenge of moving complex articulated structures, ranging from robotic arms to digital human characters, to achieve desired poses or movements (Keller et al., (https://arxiv.org/html/2507.00792v3#bib.bib18); Pechev, (https://arxiv.org/html/2507.00792v3#bib.bib39)). Accurate and efficient motion generation requires solving the inverse kinematics (IK) problem: determining a set of joint configurations that achieve a desired position or orientation of an end-effector (Murray et al., (https://arxiv.org/html/2507.00792v3#bib.bib34)). In many applications, from animating lifelike characters in virtual environments to controlling multi-joint robotic manipulators, IK provides the essential computational framework for translating high-level motion goals into precise joint movements (Murray et al., (https://arxiv.org/html/2507.00792v3#bib.bib34)).

Solving the IK problem is particularly acute in the generation of real-time, realistic movements for virtual human characters, where systems must simultaneously address speed, accuracy, and the physical and anatomical plausibility of human-like motion (Jiang et al., (https://arxiv.org/html/2507.00792v3#bib.bib17)). This is inherently challenging due to the complexity of the human skeleton, with its intricate assembly of joints and highly non-linear and interdependent degrees of freedom (Liu et al., [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib28)). In the field of humanoid robotics and virtual agents, this challenge is compounded, as systems must not only mimic the natural motion of the human body but also operate in real-time to enable seamless interaction and engagement (Montecillo-Puente et al., [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib32); Diomataris et al., [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib14); Sakka et al., [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib43)).

Traditional IK approaches, such as Jacobian-based iterative methods (Dulęba and Opałka, [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib15)), often struggle with local minima or require significant simplifications that compromise the naturalness of motion (Peiper, (https://arxiv.org/html/2507.00792v3#bib.bib40)). Furthermore, in a high degree of freedom system, even small numerical errors can propagate along the kinematic chain, leading to large discrepancies at the end effectors (Dulęba and Opałka, [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib15); Canutescu and Dunbrack, [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib13); Aristidou and Lasenby, (https://arxiv.org/html/2507.00792v3#bib.bib4)). This is especially critical when modeling human-like motion under multi-constraint conditions, where arbitrary and dynamic constraints, such as joint limits, collision avoidance, contact interactions, and expressive behavior, must be accommodated simultaneously (Sui et al., (https://arxiv.org/html/2507.00792v3#bib.bib44)), sometimes even in dynamic environments and real-time interactive applications involving human characters. These challenges highlight the need for IK solvers that can efficiently handle complex kinematic chains with multiple constraints while maintaining both accuracy and flexibility.

In this paper, we present a TensorFlow-based IK solver designed for the real-time generation of multi-constrained movements in virtual human characters. Emphasizing simplicity, speed, and accuracy, our approach leverages the automatic differentiation and just-in-time (JIT) compilation features of TensorFlow (Abadi et al., (https://arxiv.org/html/2507.00792v3#bib.bib2)) to formulate both forward and inverse kinematics as fully differentiable functions. This design not only accelerates the computation for complex kinematic chains but also allows the creation of arbitrarily complex objective functions that can be used to model any number of different end-effector constraints. Our solver is particularly well suited for a high degree of freedom human body models, where minimizing the error between target positions and computed joint configurations is challenging due to complex rotational dynamics and strict boundary conditions along the kinematic tree.

## Related Work

As one of the earliest approaches to inverse kinematics, analytical methods solve a set of closed-form equations to position an end effector at a specified target. While effective, these methods have historically relied on strong assumptions about a robot's specific structure (Peiper, (https://arxiv.org/html/2507.00792v3#bib.bib40)). More recently, analytical solutions have emerged that are independent of predefined structural constraints. Tian et al. ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib47)) proposed a solution for 7-DOF anthropomorphic manipulators by decomposing the problem into eight groups of arm configuration manifolds.

In contrast, numerical methods use iterative algorithms that converge to a solution based on an initial estimate. A fundamental numerical approach is the Moore-Penrose pseudo-inverse method, introduced by Barata and Hussein ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib5)), which determines joint configurations by minimizing the least-squares error between the current and desired end-effector positions. To improve stability, especially near singular configurations, Buss and Kim ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib12)) introduced the Selectively Damped Least Squares (SDLS) method, which dynamically adjusts the damping factor to mitigate instability.

Another widely used numerical technique is Cyclic Coordinate Descent (CCD) (Canutescu and Dunbrack, [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib13)), which is particularly useful in applications that require computational efficiency, such as real-time animation and robotics. CCD iteratively adjusts each joint in a kinematic chain, working backward from the end effector to the base to progressively minimize positional error.

Forward And Backward Reaching Inverse Kinematics (FABRIK) (Aristidou and Lasenby, (https://arxiv.org/html/2507.00792v3#bib.bib4)) refines joint positions by successively adjusting them in forward and backward passes along the kinematic chain. Unlike CCD, which rotates joints to minimize end-effector error, FABRIK directly manipulates joint positions while maintaining link constraints, resulting in smoother and more stable solutions. This makes it ideal for character animation and humanoid robotics applications where natural motion is essential.

Similarly, Interior Point OPTimizer (IPOPT) (Wachter, (https://arxiv.org/html/2507.00792v3#bib.bib48); Wächter and Biegler, (https://arxiv.org/html/2507.00792v3#bib.bib49)) is a primal-dual interior-point solver for large-scale nonlinear programming. It tackles a sequence of logarithmic-barrier sub-problems and uses a filter line-search to separately enforce decreases in constraint violation or objective value, which guarantees global convergence without resorting to merit functions. Each Newton step is complemented by second-order corrections, inertia-controlled linear solves and a dedicated feasibility-restoration phase, giving the method robustness even from poor initial guesses. This approach makes IPOPT a preferred choice for trajectory optimisation, process engineering and other engineering optimisation tasks where both scalability and numerical reliability are critical.

Further advances in real-time motion synthesis were made by Rakita et al. ((https://arxiv.org/html/2507.00792v3#bib.bib42)), who developed a method that ensures smooth, feasible manipulator motions while avoiding joint space discontinuities by framing inverse kinematics as a weighted sum nonlinear optimization problem. Similarly, Zhang et al. ((https://arxiv.org/html/2507.00792v3#bib.bib51)) proposed an approach based on constrained linear programming that incorporates joint bounds and velocity and acceleration bounds as inequality constraints to refine kinematic solutions. In addition, nonlinear solvers such as Sequential Quadratic Programming (SQP) (Boggs and Tolle, (https://arxiv.org/html/2507.00792v3#bib.bib10)) and Interior-Point Methods (IPM) (Nemirovski and Todd, [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib35)) have been used to efficiently solve multi-constraint inverse kinematic problems.

### Machine Learning Inverse Kinematic

Another important development in numerical inverse kinematics is the use of machine learning approaches to learn optimization-based techniques. Current implementations of inverse kinematics in the machine learning domain focus mainly on training neural networks to learn the IK problem from training data, and using these trained models during the inference phase to solve the IK problem for new, unseen end-effector targets (Bensadoun et al., (https://arxiv.org/html/2507.00792v3#bib.bib8)). As one of the earliest approaches, Köker et al. ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib22)) trained an artificial neural network (ANN) on five thousand trajectories and inferred cubic trajectories directly from the neural network output.

Building on this foundation, more recent advances have used deep learning architectures to improve the generalization and efficiency of inverse kinematics (IK) solutions. Levine et al. ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib23)) demonstrates the potential of deep reinforcement learning (RL) to solve IK problems in robotic manipulation tasks without requiring explicit kinematic modeling. By training policies to maximize task performance, RL-based IK methods can adapt to different environments and constraints.

A notable extension of this paradigm is the MAPPO IK algorithm proposed by Zhao et al. ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib52)), which uses multi-agent proximal policy optimization to simultaneously optimize position and posture control in six-degree-of-freedom manipulators. Unlike previous RL implementations that focus primarily on positional accuracy, this approach introduces a dual reward mechanism that combines Gaussian distance for positional accuracy and cosine distance for orientation alignment.

The challenge of solution multiplicity in redundant manipulators has inspired alternative machine learning frameworks. Bocsi et al. ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib9)) pioneered structured output learning using joint kernel support vector machines to model the probability distribution of end-effector positions and joint angles. By embedding sine/cosine joint angle transformations in kernel space, their method achieved 1.4 mm tracking accuracy on a 7-DOF Barrett WAM while maintaining temporal consistency across ambiguous configurations.

Hybrid analytic-statistical approaches have emerged to bridge the gap between model-based and data-driven methods. Nguyen and Marvel ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib36)) developed a Gaussian process framework that uses closed-form kinematic equations as prior distributions updated by Bayesian inference with optical motion capture data, significantly reducing calibration points compared to pure neural network approaches.

Recent innovations in neural architectures address inverse kinematics through hierarchical probability modeling. The IKNet framework by Bensadoun et al. ([\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib7)) uses variational autoencoder principles with Gaussian mixture models to sequentially sample joint configurations along the kinematic chain. By conditioning the probability distribution of each joint on previous angles and end-effector targets, the method generates multiple physically plausible solutions with high success rates.

Although powerful, Eapen et al. ((https://arxiv.org/html/2507.00792v3#bib.bib16)) showed that Gaussian regression and support vector machine algorithms often outperform neural network approaches for IK solutions.

## Architecture and Method

In this section, we describe the architecture and methodology of our IK solver. Our system consists of two main components: a pure, JIT-compiled forward kinematics (FK) module and an inverse kinematics solver that minimizes an objective function formulated from the IK error and additional biomechanical penalties. We first outline the forward kinematics formulation, then describe the inverse kinematics optimization framework, discuss the integration of TensorFlow for automatic differentiation and gradient descent, and finally explain the various objective functions used to enforce kinematic and task-specific constraints.

### Forward Kinematics

The FK module forms the basis of the solver by computing global transformations for a given human skeleton. A skeleton is loaded and represented as a tree structure with nodes corresponding to bones. A local transformation matrix is defined for each bone, and the FK computation uses these local transformations along with parent-child relationships to compute the global pose.

To update controlled bones, the forward kinematics (FK) model computes the global transformation of each joint in the kinematic tree from the local joint transformations. For a joint $i$ with parent index $p{(i)}$, its transformation $T_{i}$ is recursively computed as

where $L_{i} \in {\mathbb{R}}^{4 \times 4}$ is the fixed local transformation (encoding the length and rest pose of the bone), and $R_{i} \in {\mathbb{R}}^{4 \times 4}$ is the rotation matrix associated with the joint $i$.

The rotation matrix $R_{i}$ is derived from the Euler angles ${\mathbf{θ}} = {\lbrack\theta_{x},\theta_{y},\theta_{z}\rbrack}^{\top}$. Specifically, we compute the rotation matrices about the $x$-, $y$-, and $z$-axes as follows:

The combined rotation is then given by:

The FK is computed over the entire chain, resulting in a set of global transformations $\{ T_{i}\}$ that are used for further IK computations. This differentiable and modular FK pipeline ensures that gradients can be propagated back through the kinematic chain, a key requirement for the subsequent IK optimization.

### Inverse Kinematics

The inverse kinematics (IK) problem seeks the optimal set of joint angles $\mathbf{θ}$ that minimizes a given error function $J{({\mathbf{θ}})}$. An iterative gradient-descent-based optimization routine refines the angle vector over several iterations. At each iteration, the gradient of the objective function is computed with respect to the joint angles, and a learning rate is applied to update the solution while respecting the lower and upper bounds of the joint angles.

In our formulation, the objective function is constructed as:

where $J_{\text{main}}$ is the primary objective (typically enforcing the distance between the end-effector and the target) and the additional terms $\{ J_{k}\}$ incorporate further constraints such as orientation alignment or collision avoidance.

### TensorFlow Integration and Gradient Descent

Our implementation uses the TensorFlow framework to provide efficient automatic differentiation and just-in-time (JIT) compilation (Abadi et al., (https://arxiv.org/html/2507.00792v3#bib.bib2)). By expressing all kinematic computations as TensorFlow functions, we can compute gradients of the objective function $J{({\mathbf{θ}})}$ with respect to the joint angles $\mathbf{θ}$. In machine learning tasks, the gradient descent algorithm updates the joint angles by computing the gradient of the objective function and then applying the update rule:

where $\eta$ is the learning rate.

To improve convergence and stability, we use the Adam gradient descent algorithm (Kingma and Ba, [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib21)). Adam refines the gradient descent update rule by maintaining exponential moving averages of the gradients and their squares. At each iteration $t$, these moment estimates are computed as

with bias-corrected estimates given by:

The joint angles are then updated according to:

where $\epsilon$ is a small constant for numerical stability.

In addition to the standard Adam update, we incorporate a cautious modification to suppress unstable updates. Inspired by recent work on cautious optimizers (Liang et al., (https://arxiv.org/html/2507.00792v3#bib.bib24)), we compute a binary mask $M$ that retains only those coordinates where the bias-corrected momentum ${\hat{m}}_{t}$ and the gradient ${\nabla J}{({\mathbf{θ}}_{t})}$ share the same sign, i.e.,

where $\circ$ denotes the element-wise product and $\epsilon$ is a small constant for numerical stability. This mask is then applied to weight the momentum update, zeroing out contributions with inconsistent sign information. A compensatory scaling factor,

ensures that the overall update magnitude is preserved. Consequently, the cautious update

is used in place of ${\hat{m}}_{t}$ in the parameter update rule, leading to enhanced convergence and stability during training (Liang et al., (https://arxiv.org/html/2507.00792v3#bib.bib24)).

### Objective Functions

The design of the objective functions is critical to ensure both accuracy and natural motion. We implement several objective functions in our framework:

### Distance Objective

This term penalizes the Euclidean distance between the computed end-effector position and the target:

### Look-At Objective

To enforce a desired orientation, such as aligning a bone with a target direction, we define a look-at penalty:

where $\mathbf{d}_{b}{({\mathbf{θ}})}$ is the direction of the bone computed from the FK, and $\mathbf{d}_{t}$ is the target direction. The formulation involves modifications to the target point, enabling fine-tuning of the look-at behavior.

### Known Rotation Objective

For scenarios where a particular joint rotation is desired, we introduce a penalty that measures the deviation from a candidate rotation ${\mathbf{θ}}^{\ast}$:

with $N$ being the number of controlled degrees of freedom. A binary mask can be applied to focus the penalty on specific joints.

### Objective Combination

The overall IK optimization can performed by composing any of the above objectives. For example, for our evaluation, we combined all equations:

where $\lambda_{\text{dist}},\lambda_{\text{look}},\lambda_{\text{known}}$ are weights that balance the contribution of each objective.

The optimization process leverages the forward kinematics module to compute the global transformations, and the gradient descent module iteratively updates $\mathbf{θ}$ to minimize $J{({\mathbf{θ}})}$ subject to bound constraints:

Figure 1. Visualization of multiple combined objectives. The green ball is the target position, while the red ball has to be avoided. We combine the Distance Objective, a hand palm down Look-At Objective, an optional hand forward Look-At Objective and the motion planning Smoothness Objective. Full demo videos are available at https://hvoss-techfak.github.io/TF-JAX-IK/

### Extendability

This modular design allows for the easy integration of additional objectives and constraints, making the solver highly adaptable for various applications in the field of robotics and virtual agents. The following pseudo-code shows, on an example of the distance objective described in section [3.4](https://arxiv.org/html/2507.00792v3#S3.SS4.SSS0.Px1 "Distance Objective ‣ 3.4. Objective Functions ‣ 3. Architecture and Method ‣ Real-Time Inverse Kinematics for Generating Multi-Constrained Movements of Virtual Human Characters"), the ease of implementing new objective functions for the IK system. Through the use of JIT compiling and static arguments, arbitrarily complex functions can be created.

1:fksolver, target_point, bone_name
2:function distance_obj(fksolver, target_point, bone_name)
3: fk_bone ← fksolver (bone_name)
4: return ∥fk_bone − target_point∥
Algorithm 1 Distance Objective Function

### Stopping Criteria

The optimization loop in our IK solver incorporates three key stopping criteria to ensure both convergence and real-time performance. Let $t$ denote the current iteration, $N_{\max}$ the user-defined maximum number of iterations, and $J{({\mathbf{θ}}_{t})}$ the objective function value at iteration $t$.

### Iteration Count Criterion

The first criterion ensures that the solver does not run indefinitely by terminating the optimization when the number of iterations exceeds a predefined maximum:

### Error Threshold Criterion

The second criterion halts the optimization once the objective function (i.e., the error) falls below a specified threshold $\epsilon$:

### Dynamic Iteration Adjustment

In addition to the fixed iteration and error criteria, the solver dynamically adjusts the maximum allowed iterations based on the average computation time per iteration. Let $T_{\max}$ represent the maximum allowed total computation time and $\overline{t}$ the average time per iteration:

where $t_{i}$ is the computation time for the $i$-th iteration. The maximum allowed iterations, $N_{\text{allowed}}$, are then determined as:

Collectively, these stopping criteria ensure that the optimization process terminates either when a satisfactory solution is reached (i.e. when the error is sufficiently low), the iteration limit is met, or the time constraints are exceeded, thereby balancing computational efficiency and solution accuracy.

### Motion Planning

Our IK solver can be naturally extended to perform motion planning, finding smooth transitions between an initial pose and a target configuration through intermediate points. To achieve this, we introduce a trajectory consisting of the original position, a predefined number of intermediate subpoints, and the final target position. The goal is to optimize the entire trajectory simultaneously, resulting in natural and smooth motions.

To ensure smoothness throughout the planned trajectory, we generalize the smoothness objectives using finite differences. The generalized smoothness objective penalizes rapid changes in the trajectory of joint angles, formulated as:

where $n$ represents the order of the finite difference (velocity $n = 1$, acceleration $n = 2$, jerk $n = 3$), and $T$ is the total number of points in the trajectory.

The optimization framework combines this generalized smoothness objective with previously defined task-specific objectives (e.g., distance, look-at, known rotations, collision avoidance) to construct the complete motion-planning objective:

where the weights $\lambda_{\text{dist}},\lambda_{\text{look}},\lambda_{\text{known}},\lambda_{n}$ balance the influence of each term in the overall optimization.

The solver initializes a trajectory vector $\mathbf{θ}$ containing the joint angles for all points (initial, intermediate, and target). The Adam optimizer iteratively refines this trajectory by minimizing $J_{\text{trajectory}}{({\mathbf{θ}})}$ while adhering to joint-angle constraints:

This approach yields a smooth and natural motion sequence, with a variable amount of intermediate points, from the initial configuration to the final target, while adhering to all given objective functions. Figure (https://arxiv.org/html/2507.00792v3#S3.F1 "Figure 1 ‣ Objective Combination ‣ 3.4. Objective Functions ‣ 3. Architecture and Method ‣ Real-Time Inverse Kinematics for Generating Multi-Constrained Movements of Virtual Human Characters") shows a combination of multiple objectives together with the smoothness objective.

## Experimental Results

Avg. Time per Iteration (ms)

Table 1. Comparison of iteration times between the CPU and GPU configurations of both the TensorFlow and JAX implementation. In all fields we report the mean value with the respective standard deviation.

Time per Iteration (ms)

Table 2. Performance metrics for all four tested implementations both with the simple end effector target and the complex objective J (θ). In all fields we report the mean value with the respective standard deviation. For solving time, iterations, and time per iteration, lower is better. For success rate, higher is better.

To evaluate the performance of our proposed TensorFlow-based inverse kinematics solver, we performed objective comparisons against several established methods: Cyclic Coordinate Descent (CCD) (Canutescu and Dunbrack, [\[n. d.\]](https://arxiv.org/html/2507.00792v3#bib.bib13)), FABRIK (Aristidou and Lasenby, (https://arxiv.org/html/2507.00792v3#bib.bib4)), Interior Point OPTimizer (IPOPT) (Wachter, (https://arxiv.org/html/2507.00792v3#bib.bib48); Wächter and Biegler, (https://arxiv.org/html/2507.00792v3#bib.bib49)), and an implementation of our library in JAX with just-in-time (JIT) compilation. This JAX implementation is exactly the same as the TensorFlow version but replaces all TensorFlow calls with JAX calls. There are no other implementation differences and the resulting value outputs (apart from slight rounding differences) are exactly the same, given the same input seed. We also implemented our library in PyTorch using TorchScript. However, despite our best efforts, the code performed excessive recompilations during each iteration resulting in execution times of 10-20 seconds per target. For clarity, we therefore excluded the PyTorch implementation from further analysis.

Our experiments were conducted using the SMPLX skeleton (Pavlakos et al., (https://arxiv.org/html/2507.00792v3#bib.bib38)), a widely adopted standard for human body armatures in applications that require modeling complex joint behavior. In particular, we focused on the upper extremities, testing the bones ¡hand¿\_collar, ¡hand¿\_shoulder, ¡hand¿\_elbow and ¡hand¿\_wrist for both the left and right hand. This subset was chosen because of the challenging rotational dynamics at the wrist and the strict boundary conditions at the elbow.

Each method was evaluated using two types of IK targets. The first was a simple target end-effector position where the goal was to reach a certain target position with the index finger of the respective hand, while the second was a combination of the previously described objective functions $J{({\mathbf{θ}})}$ designed to encapsulate realistic human bone boundary constraints. In all experiments, the weight of $\lambda_{\text{dist}}$ and $\lambda_{\text{known}}$ was set to 1.0, while the weight of $\lambda_{\text{look}}$ was set to 0.1.

For consistency, each implementation was allowed a maximum of 500 iterations per run. Each run was concluded and reported as a success if the solving algorithm reached a total loss threshold of 0.005 or lower. If the implementation did not reach the threshold inside the 500 iterations limit, the run was considered a failure.

The experimental dataset was generated by first sampling one million target configurations around the SMPLX skeleton. We then filtered these to retain only those targets that could be successfully solved by any of the tested implementations, resulting in 24,531 valid configurations. To ensure a representative and evenly distributed set, we performed k-means clustering on the solved targets and selected 1010 centroids. Furthermore, to mitigate any initialization effects, measurements were taken only after the first ten targets had been processed, leaving us with 1000 sampled target locations. After each target, the SMPLX skeleton was reset to its original resting position, to not skew the iteration count between targets.

Performance metrics were computed by averaging the results over five independent runs per algorithm to account for any processing variations.

As both the JAX and TensorFlow implementation can be run with or without the GPU, we first measured the difference in iteration time for all targets with both the simple end effector and the objective function $J{({\mathbf{θ}})}$. Table (https://arxiv.org/html/2507.00792v3#S4.T1 "Table 1 ‣ 4. Experimental Results ‣ Real-Time Inverse Kinematics for Generating Multi-Constrained Movements of Virtual Human Characters") shows the average result over all 1000 targets. Here, both CPU configurations are faster than their GPU counterpart. Therefore, we use the CPU configuration of the JAX and TensorFlow solver for all of our performance metrics.

Table (https://arxiv.org/html/2507.00792v3#S4.T2 "Table 2 ‣ 4. Experimental Results ‣ Real-Time Inverse Kinematics for Generating Multi-Constrained Movements of Virtual Human Characters") summarizes the performance metrics for the tested algorithms under both objective formulations. Under the simpler IK objective (without the custom objective $J{({\mathbf{θ}})}$), the TensorFlow-based solver achieved a mean solution time of 8.06 ms with an average of 36.99 iterations and a success rate of 100%. The JAX implementation was competitive in iteration count (37.27 ± 17.76) and success rate (100%), although its solving time was slightly higher at 12.62 ms. In comparison, IPOPT had a notably lower iteration count of 13.24 ± 3.30, indicating rapid convergence in terms of iterations, but with a higher mean solving time of 164.73 ± 132.25 ms. Conversely, both CCD and FABRIK exhibited substantially lower performance under the simple end-effector objective; while CCD achieved a moderate solving time of 25.44 ms with a success rate of 91.19%, FABRIK performed noticeably worse, with a mean solving time of 85.28 ms.

When the custom objective function $J{({\mathbf{θ}})}$ was incorporated to simulate realistic human joint constraints, the performance gap between the methods became even more pronounced. Both CCD and FABRIK experienced substantial increases in computational cost, with mean solving times of 570.49 ms and 439.90 ms, respectively, and iteration counts approaching the maximum limit of 500 iterations per target; their success rates plummeted to under 1%, rendering them ineffective for applications requiring stringent adherence to biomechanical constraints. IPOPT's performance further deteriorated under the more challenging objective, with its solving time surging to 2759.28 ± 8045.75 ms and its iteration count averaging 44.52 ± 88.44, coupled with a slightly lower success rate of 96.50%. Both the JAX and TensorFlow implementations maintained robust performance; the JAX-based solver incurred a moderate solving time of 86.18 ms with an average of 67.09 iterations and a success rate of 99.60%, while the TensorFlow-based solver outperformed the others with a mean solving time of 43.55 ms, an iteration count of 67.40, and a success rate of 99.60%.

### Motion Planning Results

Table 3. Distance trajectory effector performance metrics for different numbers of points in a trajectory. In all fields we report the mean value with the respective standard deviation. For solving time lower is better. For success rate higher is better.

Table 4. Jtrajectory (θ) objective performance metrics for different numbers of points in a trajectory. In all fields we report the mean value with the respective standard deviation. For solving time lower is better. For success rate higher is better.

We evaluated our motion planning extension on the TensorFlow implementation by comparing two configurations: a simple distance-based objective applied to the trajectory end effector ${J_{\text{distance}}{({\mathbf{θ}})}} + {\sum_{n = 1}^{3}{J_{\text{smoothness}}^{(n)}{({\mathbf{θ}})}}}$, and the full trajectory objective $J_{\text{trajectory}}{({\mathbf{θ}})}$, which incorporates additional task-specific constraints and smoothness terms. We used the same weights for all hyperparameters as in the original experiment, except for the new parameter $\lambda_{n}$, which we set to 0.01. For both cases, we varied the number of trajectory points by testing no intermediate trajectory points, 5 trajectory points, and 10 trajectory points to assess the impact on solution time and success rate.

Table (https://arxiv.org/html/2507.00792v3#S4.T3 "Table 3 ‣ 4.1. Motion Planning Results ‣ 4. Experimental Results ‣ Real-Time Inverse Kinematics for Generating Multi-Constrained Movements of Virtual Human Characters") shows the performance of the distance-based objective as the number of trajectory points increases. With no intermediate points (i.e., a single-target configuration), the solver achieved an average solving time of 8.06 ms, a mean iteration count of 36.99 $\pm$ 17.52, and a success rate of 100%. When the trajectory was extended to 5 trajectory points, the solving time increased to 17.12 ms, the iteration count increased to 83.01 $\pm$ 57.81, while the success rate decreased slightly to 99.30%. With 10 points, the average solution time reached 21.16 ms, the iteration count increased to 102.65 $\pm$ 87.65, and the success rate lowered to 97.40%. Similarly, solving times under the full trajectory objective $J_{\text{trajectory}}{(\theta)}$ increased linearly with the number of trajectory points (see table (https://arxiv.org/html/2507.00792v3#S4.T4 "Table 4 ‣ 4.1. Motion Planning Results ‣ 4. Experimental Results ‣ Real-Time Inverse Kinematics for Generating Multi-Constrained Movements of Virtual Human Characters")). For the baseline case with no intermediate trajectory points, the solver recorded an average solving time of 43.55 ms, an average iteration count of 67.40 $\pm$ 46.00, and a success rate of 99.60%. With 5 intermediate points, the solving time nearly doubled to 88.88 ms, the iteration count increased to 128.19 $\pm$ 113.24, and the success rate dropped to 94.99%. When the number of trajectory points was increased to 10, the mean solving time increased to 162.83 ms, the average iteration count increased to 229.62 $\pm$ 178.41, and the success rate further decreased to 83.67%. This strong decrease in success rate can be partially explained by the strong increase in iteration count, as 71 of our samples exceeded the maximum iteration count of 500. Doubling the iteration count could therefore lead to improved success rates for higher numbers of intermediate trajectory points. Regardless, these results indicate that the solver remains highly robust and works well within real-time constraints even as the problem dimensionality increases, especially if only a small amount of objective functions is used.

## Discussion

Our experimental results demonstrate significant advantages of our TensorFlow-based inverse kinematics (IK) solver, particularly in terms of adaptability, computational speed, and reliability for complex systems with high degrees of freedom. Cyclic Coordinate Descent (CCD) methods, while efficient in simpler contexts, often encounter problems such as error accumulation and local minima when scaled up to more complex scenarios, especially under joint angle constraints (Xu et al., (https://arxiv.org/html/2507.00792v3#bib.bib50); Boulic and Kulpa, (https://arxiv.org/html/2507.00792v3#bib.bib11); Kenwright, (https://arxiv.org/html/2507.00792v3#bib.bib19)). These limitations are particularly pronounced in human motion modeling, which is characterized by intricate joint interdependencies and stringent biomechanical constraints. Similarly, FABRIK often exhibits inefficiencies and lower success rates when realistic boundary conditions and multiple concurrent constraints are enforced (Aristidou et al., (https://arxiv.org/html/2507.00792v3#bib.bib3); Martin et al., (https://arxiv.org/html/2507.00792v3#bib.bib30); Kenwright, (https://arxiv.org/html/2507.00792v3#bib.bib19); Tao et al., (https://arxiv.org/html/2507.00792v3#bib.bib45)).

IPOPT exhibited notable strengths in iteration efficiency, rapidly converging within fewer steps compared to all other implementations. This efficiency highlights IPOPT's effectiveness in navigating the optimization landscape quickly due to its interior-point method design, making it suitable for problems where the iteration cost is very high. However, IPOPT's computational overhead per iteration, presumably due to the high cost of computing Newtowns direction (Lin et al., (https://arxiv.org/html/2507.00792v3#bib.bib26)), proved to be a substantial drawback limiting its practicality in real-time applications or scenarios requiring high-frequency updates. Additionally, IPOPT demonstrated sensitivity to the complexity introduced by biomechanical constraints encoded in the custom objective function, leading to increased variability and occasional convergence issues, which impacted its overall reliability compared to methods specifically optimized for computational efficiency like our TensorFlow solver.

In computer animation and gaming, character rigs typically have many degrees of freedom and require highly responsive IK solutions to achieve believable and realistic motion (Kenwright, (https://arxiv.org/html/2507.00792v3#bib.bib20)). Our proposed solver effectively meets these interactive performance requirements without sacrificing realism. The modular design allows seamless integration of constraints such as contact points, gaze direction, or stylistic elements without requiring retraining or modification of the underlying IK algorithms. Particularly in virtual reality and telepresence applications, where sparse tracking data points are typically available, our solver could reliably infer complete full-body poses while respecting essential human kinematic constraints such as realistic elbow extension and knee flexion limits (Parger et al., (https://arxiv.org/html/2507.00792v3#bib.bib37)).

In humanoid robotics and virtual human simulation, it could generate complex movements on demand by optimizing joint motions to achieve goals such as balance, reaching, and obstacle avoidance. This on-demand optimization accelerates development and prototyping, as one of the major benefits of our differentiable solver is its extensibility via modular objective functions. In contrast to analytic or Jacobian pseudoinverse methods that struggle to handle multiple objectives simultaneously (Malik et al., (https://arxiv.org/html/2507.00792v3#bib.bib29)), our approach allows arbitrary constraints to be added as terms in the loss function. For instance, one can impose joint limit penalties, collision avoidance terms, or even soft biomechanical targets simply by including the corresponding differentiable cost functions in the optimization. The solver would then naturally balance all these objectives via the gradient descent process. This capability is akin to the penalty-based formulations in traditional IK solvers (Beeson and Ames, (https://arxiv.org/html/2507.00792v3#bib.bib6)), but implemented in a powerful unified end-to-end differentiable manner within TensorFlow. Consequently, our IK solver easily accommodates diverse tasks. For instance, achieving precise reaching motions while preserving human-like postures can be realized by combining an end-effector position loss with a reference pose similarity term. Adjustments to motion objectives require no additional retraining or specialized algorithmic modifications to the objective function itself. Additionally, because our method fundamentally relies on the provided kinematic model, it generalizes seamlessly across different character rigs and robotic manipulators. A single solver implementation can thus manage multiple distinct avatars or robotic systems without requiring model-specific training, eliminating the overhead typically associated with neural network-based IK solutions (Limoyo et al., (https://arxiv.org/html/2507.00792v3#bib.bib25)). Although we evaluated our IK solver on the different arm joints, this approach is fully extendable to arbitrary amounts of joints. In the future, we would like to use this approach to solve movements for the entire SMPLX skeleton and

## Limitations

Despite its advantages, the differentiable inverse kinematics (IK) solver has trade-offs, notably higher computational cost per frame compared to analytical methods or pre-trained neural networks. Unlike direct feedforward network solutions, our iterative optimization approach requires more computational time, especially for highly redundant systems or scenarios requiring precise accuracy. To mitigate this, we use TensorFlow's XLA JIT compilation to optimize the computational graph, including Jacobian computations through automatic differentiation, and warm start each frame with the previous solution to minimize iterations. Although our method converges in milliseconds, it remains somewhat slower per frame than specialized analytical IK methods or trained networks, which can provide solutions in microseconds. Also, this approach inherently runs the risk of converging to local minima due to the nonconvex optimization landscape. However, by incorporating physically realistic constraints such as joint bounds and continuity from previous frames, we can significantly reduce the likelihood of unnatural poses or sudden deviations. In challenging or abruptly changing goal scenarios, the use of random restarts or secondary goals can further improve robustness, although such measures were rarely required in our testing. Furthermore, our model currently relies on an accurate kinematic model for solving the inverse kinematic problem, which is not always available. This limitation could be resolved using recent work in adaptable kinematic models, but in our work, this is not yet realized (Ponton et al., (https://arxiv.org/html/2507.00792v3#bib.bib41); Tejwani et al., (https://arxiv.org/html/2507.00792v3#bib.bib46)).

Another limitation is the naturalness of the produced motion, especially for virtual agents. Although we already have objective functions that minimize the changes in velocity, acceleration, and jerk, this can lead to sudden changes or movements that do not feel natural to an outside observer. In the future, we could implement different learned objective functions that expand upon this problem by, for example, introducing GAN discriminators for natural human motion Men et al. ((https://arxiv.org/html/2507.00792v3#bib.bib31)), learned motion classificators from large datasets (Liu et al., (https://arxiv.org/html/2507.00792v3#bib.bib27)), or even motion retrieval systems that align the solving with human input data, similar to Mughal et al. ((https://arxiv.org/html/2507.00792v3#bib.bib33)).

## Conclusion

In this paper, we have presented a TensorFlow-based inverse kinematics solver that uses automatic differentiation and just-in-time compilation to solve complex, multi-constrained IK problems efficiently and accurately. By formulating both forward and inverse kinematics as differentiable functions, our approach addresses the challenges inherent in high-degree-of-freedom systems, such as error accumulation along kinematic chains and complicated joint dynamics. Our experimental evaluation has shown that the TensorFlow-based solver consistently outperforms established inverse kinematic methods. For both simple and custom IK targets, the proposed solver achieved rapid convergence with minimal iteration times and near-perfect success rates. In contrast, conventional methods such as CCD and FABRIK struggled under realistic boundary conditions, exhibiting significantly higher iteration counts and lower success rates. The performance of our JAX-based implementation, while competitive in simpler scenarios, could not match the efficiency of the TensorFlow approach under more demanding conditions.

These results underscore the practical advantages of modern differential approaches for real-time applications in robotics, computer graphics, and biomechanics. The flexibility to define arbitrary objective functions further broadens the solver's applicability in modeling complex joint rotations and enforcing realistic constraints. Future work may explore faster optimization and extension to additional kinematic models, solidifying the role of differentiable programming in advancing inverse kinematics solutions for complex articulated systems.
