<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MP-MPPI: A Motion Primitive Guided Sampling-Based Optimizer for Model Predictive Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper proposes a novel method that extends the Model Predictive Path Integral (MPPI) method with motion primitives for additional structured sampling, which enhances the convergence towards a globally optimal solution. By evaluating motion primitives and perturbed control sequences in a real-time sampling-based optimization loop, this work addresses the limitations of the path planning capabilities of sampling-based controllers. The algorithm is implemented on a quadcopter simulator and tested on an obstacle field navigation task. It is demonstrated that the proposed approach enhances exploration of the control space while maintaining the fast, reactive behavior required for real-time control.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The demand for robust, agile controllers has grown significantly in recent years, as researchers pivot to developing field robotic systems that work outside the laboratory, in unpredictable, real-world environments. The research community has increasingly been adopting agile quadcopter platforms as a benchmark to evaluate new control algorithms, given the requirements for fast, reactive controllers. Navigating challenging obstacle fields in this setting is particularly demanding, making it well-suited to evaluate novel control strategies. While professional quadcopter pilots train extensively to handle these challenging environments, classic path planning approaches often fail to handle the fast-moving, changing environments, and frequently fail to operate in real-time. Therefore, the development of controllers that bridge the gap between high-level planning and low-level control is essential for matching human performance in real-world environments. Model Predictive Control (MPC) bridges this gap by leveraging a system model to predict future states and optimize control inputs. The MPC problem is typically solved using gradient-based optimization to satisfy system constraints while minimizing a defined cost function.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, the growing capabilities of parallel computing have enabled the implementation of MPC on high-performance hardware, such as GPUs, allowing for faster and more scalable real-time control in complex robotic systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Path Integral (MPPI) is one such implementation that uses a sampling-based technique for optimization. MPPI works by sampling small perturbations on an initial control input and calculating the cost relating to some control objective for each perturbation. These perturbed control inputs are then fused with a higher weight given to lower cost perturbations, producing a new optimal control sequence. A strength with sampling-based methods is that they do not require differentiable system dynamics, allowing greater freedom to tailor the cost function to the problem at hand. The magnitude of the perturbations added to the initial control sequence naturally defines a maximum change in the control sequence per iteration. This limits how quickly the control input can be transformed into a new optimal control sequence when the environment changes, which can make the controller unresponsive and slow to adapt to new changes. While proven to be a powerful optimizer, this approach introduces challenges in balancing exploration and exploitation. Increasing the magnitude of the perturbations to increase global optimality often induces instability in the closed-loop system, resulting in a low-performance controller.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several methods have been proposed to increase the global optimality of the MPPI algorithm, while keeping the local optimization capability and cost function design freedoms. DIAL-MPC and MPOPI use the MPPI algorithm iteratively, from high noise to lower noise, to arrive at an optimal control input. This adds to the computation time and lowers the ability to parallelize effectively. The BiC-MPPI method introduced in Jung and Kim uses the MPPI algorithm bidirectionally to optimize the control input but requires invertible dynamics. Yan and Devasia ) proposed the o-MPPI approach, which changes the algorithm to sample outputs instead of inputs. This modification introduces a limitation, as it also requires invertible dynamics. Earlier work has also attempted to guide the samples with a higher-level planner, such as the RRT guided MPPI introduced in Tao et al.. However, in such approaches, the path planners often struggle with real-time performance, which makes replanning more difficult in dynamic environments. Some methods further diversified the parallelization of the MPPI algorithm, such as AERO MPPI and U-MPPI.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

These approaches run multiple parallel instances, optimizing multiple objectives at a time, but this lowers the available samples for each parallel instance, which can lead to lower optimality. Feature-based MPPI introduced in Homburger et al. samples around key features such as emergency braking, to allow quicker decisions in safety-critical situations. However, there is a limit to how many samples each feature can receive, which may reduce performance during normal operation. Recent approaches, such as Biased-MPPI, have focused on modifying the sampling distribution of the MPPI algorithm to improve performance, which extends the MPPI to allow arbitrary ancillary controllers to be included in the sampling distribution. Poyrazoglu et al. proposed the C-Uniformity MPPI method, which modifies the sampling distribution to a uniform distribution. Still, extensively altering the sampling distribution may negatively impact the performance and convergence of the MPPI algorithm, as potentially harmful biases can be introduced from increased variability of sampled inputs.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose Motion-Primitive-guided Model Predictive Path Integral (MP-MPPI). This is a low-cost, high-impact modification to the MPPI method that increases global optimality and exploration. In this proposed method, additional control sequences are generated as feasible lattice state motion primitives. These motion primitives serve as informative samples, improving the exploration of the control space. MP-MPPI samples these precomputed motion primitives alongside the standard MPPI perturbations and fuses them to achieve optimal control. An overview of the proposed method can be seen in Figure 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is shown in the following that the proposed method is: Suited for effective parallel implementation on GPUs. Able to achieve robust control of a simulated quadcopter. Of superior performance compared to the base MPPI algorithm in collision avoidance and obstacle field navigation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Methodology", "weight": 1.0} -->

The proposed MP-MPPI algorithm was realized by first developing a base MPPI solver. This initial solver was subsequently enhanced through the incorporation of motion primitive samples, resulting in the complete MP-MPPI solver capable of leveraging structured trajectory sampling for improved control performance.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Optimal Control Problem", "weight": 1.0} -->

The states $x_{t}$ and inputs $u_{t}$ are constrained by the sets $\mathcal{X}$, and $\mathcal{U}$, as well as needing to satisfy the constraints $x_{t+1}=f(x_{t},u_{t})$, where $f(x_{t},u_{t})$ is the system dynamics. $\ell_{f}$ is the final cost term, which only considers the final predicted state $x_{N}$ and can be used as a stabilizing cost to enforce a stable final state.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model Predictive Path Integral", "weight": 1.0} -->

Model Predictive Path Integral (MPPI) is an implementation of the MPC method, where a sampling-based method is used to optimize the control inputs. Samples are generated as perturbed trajectories by modifying the nominal control $u_{t}$ into the perturbed control variable $u_{t}^{(k)}=u_{t}+\epsilon_{t}^{(k)}$ for $k=1,\ldots,K$ where $\epsilon_{t}^{(k)}$ is a perturbation that is drawn from $\mathcal{N}(0,\Sigma)$. The perturbed control variables are then used to generate $K$ samples in the form of the perturbed trajectories $x_{t}^{(k)}$ by the numerical integration scheme where $f_{\mathrm{RK4}}$ is the Runge-Kutta 4th order integration method.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model Predictive Path Integral", "weight": 1.0} -->

The cost $S^{(k)}$ for each trajectory $x_{t}^{(k)}$ is defined as: The optimal control sequence $u_{t}$ can then be generated by performing a weighted sum of the perturbed controls $u_{t}^{(k)}$ following the update law where $w_{k}$ is the weight of the $k$-th perturbed control sequence and $\eta$ is the sum of all weights. The variable $\rho$ is the minimum of the cost $S^{(k)}$ over the $K$ samples, and is included for numerical stability and does not influence the optimality of the solution. The cost $S^{(k)}$ determines which input sequences are emphasized and which are discarded. The temperature variable $\lambda$ is a tuning variable that changes the way each perturbation is weighted. A larger $\lambda$ creates a more uniform weighting, while a smaller $\lambda$ approaches a hard selection of the least costly perturbed trajectory.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model Predictive Path Integral", "weight": 1.0} -->

The magnitude of the covariance matrix $\Sigma$ defines the rate of adaptation for the optimizer. A lower covariance matrix will lead to more locally optimal results, but decrease the rate of convergence, while a high magnitude covariance matrix increases the convergence speed, but can decrease the stability of the system.

<!-- chunk {"id": "body-0015", "role": "body", "section": "MP-MPPI: Motion-Primitive-guided MPPI", "weight": 1.0} -->

This section presents the proposed MP-MPPI extension to the MPPI method, where $N_{p}$ additional samples in the form of motion primitives are added. Motion primitives are sequences of control inputs that represent different types of motion, such as left- and right-turns, changes in velocity, etc..

<!-- chunk {"id": "body-0016", "role": "body", "section": "MP-MPPI: Motion-Primitive-guided MPPI", "weight": 1.0} -->

The motion primitive control sequences, denoted $u_{t}^{(p,j)}$ for the $j$-th motion primtive, produce the trajectories The control inputs $u_{t}^{(p,j)}$ are selected from the set of feasible control inputs $\mathcal{U}$, which ensures the dynamic feasibility of the motion primitives.

<!-- chunk {"id": "body-0017", "role": "body", "section": "MP-MPPI: Motion-Primitive-guided MPPI", "weight": 1.0} -->

State lattice motion primitives are used and are generated by solving the OCP for a change in position to a point reference. The OCP is solved for a set of $N_{p}$ point-references, which creates $N_{p}$ motion primitive samples $u_{t}^{(p,0)},\ldots u_{t}^{(p,N_{p}-1)}$. These motion primitive samples are combined with white noise samples $u_{t}^{},\ldots,u_{t}^{(M-1)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "MP-MPPI: Motion-Primitive-guided MPPI", "weight": 1.0} -->

In the optimization loop, $M$ samples $u_{\epsilon}^{0},\ldots,u_{\epsilon}^{M-1}$ are generated as perturbed control inputs $u_{t}^{(k)}=u_{t}+\epsilon_{t}^{(k)}$ with white noise $\epsilon^{k}$. $N_{p}$ samples are drawn from a library of precomputed motion primitives, denoted $u_{t}^{(p,j)}$. Each sample is a column of the matrix The cost function is evaluated in parallel for all elements in the vector, to obtain the costs $S^{(k)}$. Following the weighted sum update scheme from equations -, the optimal control sequence is computed as follows: where $K=M+N_{p}$ and $U^{(k)}$ is column $k$ of $U_{t}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "MP-MPPI: Motion-Primitive-guided MPPI", "weight": 1.0} -->

The full MP-MPPI algorithm can be seen in Algorithm 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "MP-MPPI: Motion-Primitive-guided MPPI", "weight": 1.0} -->

1:Current state xcurr, previous control sequence Uprev (shape M × Udim), motion primitives Up (shape Np × Udim), horizon N, number of noisy samples M, noise covariance Σ, temperature λ, number of motion primitives Np, actuator constraints umin and umax 2:Updated control sequence Unew 4:x0 ← xcurr ⊳ Generate noisy samples 9:Uϵ ← clip(Uϵ, umin, umax) ⊳ Construct combined sample set 15:ρ ← minkcost[k] ⊳ Compute weights 17: $w[k]\leftarrow\exp\!\Bigl(-\frac{1}{\lambda}\bigl(\mathrm{cost}[k]-\rho\bigr)\Bigr)$ 19:$\eta\leftarrow\sum_{k=1}^{K}w[k]$ ⊳ Update control sequence 22: $U_{\mathrm{new}}\leftarrow

<!-- chunk {"id": "body-0021", "role": "body", "section": "Case Study", "weight": 1.0} -->

The proposed method was implemented on a custom quadcopter simulator. The MP-MPPI algorithm was compiled using the JAX Python library and executed on an RTX 2000 Ada Laptop GPU. JAX is a Google-developed, JIT (Just-In-Time) compatible library for array-oriented numerical computations. This library was used to effectively implement a GPU-vectorized version of the proposed algorithm. The controller was tuned to run above $100\text{\,}\mathrm{Hz}$ with satisfactory performance for point reference tracking. To preserve and emphasize the real-time viability of the proposed method, we tuned the controller to be lightweight, based on parameters used in previous real-world MPPI implementations. The system was simulated using a discretized model with a time step of $10\text{\,}\mathrm{ms}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Case Study", "weight": 1.0} -->

The chosen drone model parameters and the hyperparameters for MPPI are shown in Table 1 and Table 2, respectively. The controller parameters in Table 2 are extended to include Table 3 to complete the MP-MPPI controller implementation. The parameters in Table 3 are used to generate the motion primitive library. For each value in the reference lattice, the OCP in is solved, creating the set of motion primitives, shown in Figure 2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Quadcopter Dynamics Model", "weight": 1.0} -->

Quadcopters are actuated by four propellers, producing forces and torques on the rigid quadcopter body ($u=[f_{B},\tau_{x},\tau_{y},\tau_{z}]^{T}$). In this paper, the dynamics model operates with these forces and torques directly. The dynamics model given by $\dot{x}=f(x,u)$ was developed based on rigid body equations of motion, with linear dynamics which describes linear motion of a system with mass $m$, where $p=[x,y,z]^{T}$ is the position in the inertial frame, $v$ is the velocity in the inertial frame, $q=[\eta,\sigma^{T}]^{T}$ is the unit quaternion of the body orientation and $g$ is the acceleration due to gravity. $f_{B}$ is the total thrust force in the body frame, which is pre-multiplied by the rotation matrix $R(q)$ to obtain the forces in the inertial frame.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Quadcopter Dynamics Model", "weight": 1.0} -->

Body torques $\tau_{B}$ produced are given by $[\tau_{x},\tau_{y},\tau_{z}$\]. The angular dynamics are described by the equations where $\omega$ is the angular velocity in body coordinates, and $\tau_{B}$ is a vector of all body torques. $J=\mathrm{diag}(I_{x},I_{y},I_{z})$ is the inertia matrix in body coordinates. The inertia matrix is diagonal due to the assumption of symmetry around the center of mass. The quaternion product is given by To enforce these model constraints when calculating the trajectory cost, a 4th order Runge-Kutta method (RK4) was used to integrate the differential equations shown in -. After each integration, the quaternions were normalized to ensure they represented the rotation in unit quaternions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Task Specific Cost Function", "weight": 1.0} -->

The cost function to be minimized was chosen to have a general quadratic form: where $\ell$ is the cost at a specific state. $x$ is the position, $v$ is the velocity, $q$ is the orientation and $\omega$ is the angular velocity. $x_{\mathrm{ref}}$ and $q_{\mathrm{ref}}$ are the commanded references. $c_{p}$, $c_{v}$, $c_{q}$ and $c_{\omega}$ are cost coefficients, $W$ is a diagonal matrix with input cost coefficients. $u$ is the input, and $u_{\mathrm{ref}}$ is the reference input required to sustain a stable hover. $u_{\mathrm{prev}}$ is the previously optimal control sequence, and $W_{\Delta}$ is a diagonal matrix with change-in-input cost coefficients. The cost coefficients work as regularization terms that penalize high angular and high linear velocity flight.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Task Specific Cost Function", "weight": 1.0} -->

Equally, a rapid change in inputs, or inputs far away from the reference input, can destabilize the controller, and are therefore penalized. The error function for the unit quaternion is given by where $[\eta_{1},\sigma_{1}^{T}]^{T}\cdot[\eta_{2},\sigma_{2}^{T}]^{T}=\eta_{1}\eta_{2}+\sigma_{1}^{T}\sigma_{2}$ is the quaternion inner product.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Task Specific Cost Function", "weight": 1.0} -->

It is noted that ${q\cdot q_{\mathrm{ref}}}=\cos(\tilde{\theta}/2)$ where $\tilde{\theta}$ is the rotation angle of the quaternion deviation $\tilde{q}=\bar{q}_{\mathrm{ref}}\otimes q=[\cos(\tilde{\theta}/2),\sin(\tilde{\theta}/2)\tilde{k}^{T}]^{T}$ where $\tilde{k}$ is the unit axis of rotation and $\bar{q}$ is the conjugate of $q$. It follows that $d_{q}(q,q_{\mathrm{ref}})=\sin^{2}(\tilde{\theta}/2)$. The unit quaternion cost term works to encourage upright and forward-facing flight.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Task Specific Cost Function", "weight": 1.0} -->

Motion Primitive Parameters Table 3: Parameter values used to generate the set of motion primitives.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Obstacle Avoidance", "weight": 1.0} -->

Obstacle avoidance is achieved through a cost modification of (3.2). Adding high cost to the trajectories that lead to collision means that those trajectories are effectively disregarded when calculating the updated control sequence. The new trajectory cost becomes where $c_{obs}$ is a penalty for colliding, $N_{\mathrm{obs}}$ is the number of obstacles and $\mathds{1}$ is the indicator function that returns 1 when $x_{j}^{k}\in C_{\text{obs}}$ and 0 otherwise. This function assumes that the obstacle geometry is accessible. To account for the physical dimensions of the drone, a safety distance $d_{\text{safe}}$ is included in the collision check.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Obstacle Field Navigation", "weight": 1.0} -->

Obstacle avoidance and navigation are evaluated on a dense obstacle field navigation task. An example is shown in Figure 3. The quadcopter has to navigate through 300 randomly placed pillars with a diameter of $1\text{\,}\mathrm{m}$, generated within a bounding box of $20\text{\,}\mathrm{m}$ by $100\text{\,}\mathrm{m}$. The drone is commanded to follow a moving point reference $10\text{\,}\mathrm{m}$ in front of the quadcopter on the center line of the obstacle field. Each simulation lasted for $5\text{\,}\mathrm{s}$ and started from a hovering state. The obstacle field navigation task was run 100 times, with the end positions, as well as the number of collisions, being recorded.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Obstacle Field Navigation", "weight": 1.0} -->

As seen in Figure 4, the MPPI algorithm navigated the obstacle field effectively with a mean traversal distance of $48.0\text{\,}\mathrm{m}$ and with a standard deviation of $18.0\text{\,}\mathrm{m}$. Adding 27 motion primitives (visualized in Figure 2) to create the MP-MPPI controller, increased the mean traversal distance to $66.6\text{\,}\mathrm{m}$, with a standard deviation of $12.6\text{\,}\mathrm{m}$. The MPPI controller collided once during the 100 runs, while the MP-MPPI controller managed to avoid any collisions. This demonstrated that the addition of a few motion primitives improved the obstacle field navigation in both total distance traversed and in collisions avoided. The MP-MPPI algorithm discovers trajectories that take it beyond its locally minimum solution, and further progress through the obstacle field.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Single Update Analysis", "weight": 1.0} -->

The MP-MPPI algorithm and the MPPI base algorithm are evaluated on reactivity, where both algorithms are compared in a scenario where the drone is moving towards a wall at $10\text{\,}\mathrm{m}\text{\,}{\mathrm{s}}^{-1}$ from a distance of $5\text{\,}\mathrm{m}$, and suddenly becomes aware of the obstacle. The controller performance can be seen in Figure 5.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Single Update Analysis", "weight": 1.0} -->

The MP-MPPI algorithm generates a trajectory that avoids collision with the wall, while the MPPI algorithm collides with it. This highlights how the motion primitive samples go into effect when the base MPPI algorithm is limited by the magnitude of the perturbations. The additional motion primitives inform the controller of solutions that might not be locally optimal, but represent the needed motion to avoid collision with the wall.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Controller Update Frequency", "weight": 1.0} -->

Agile robotic systems rely on rapid feedback for stable control, therefore the update frequency is also benchmarked. Figure 6 shows the update frequencies for a varying number of samples and prediction horizons. This shows that the computation times follow a linear trend with respect to the horizon length. It also shows that the algorithm effectively runs on a GPU, with only small differences in latency between using 1024 samples and 128 samples. This allows for the evaluation of additional motion primitive samples, with a limited effect on the update frequency.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

While the proposed MP-MPPI method demonstrates that a small selection of precomputed motion primitives can significantly increase the performance over the base MPPI algorithm, the extent of this effect has not been fully explored. While the convergence has been proven for arbitrary controllers, there is still the need to explore if these kinematically feasible building blocks provide better convergence and introduce less bias than an arbitrary controller would.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

A main limitation of this approach is that the balance between motion primitives and regular noisy samples becomes a design parameter that must be carefully tuned. Too many motion primitives can cause the controller to weight potentially suboptimal trajectories, thereby lowering performance and optimality. Future work may investigate if there is a method to generate the motion primitive library for specific tasks optimally.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we propose MP-MPPI, an enhanced version of the MPPI algorithm that improves global optimality by introducing exploratory motion primitives into the MPPI update law. The performance is evaluated in a quadcopter simulator, which indicated the method's ability to navigate highly cluttered environments. Obtained results demonstrated that in an unpredictable environment, MP-MPPI can adapt quickly and avoid collision, where the MPPI fails to do so.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The proposed MP-MPPI method is shown to be a low-cost, high-impact extension to the MPPI method, capable of running on lower-end parallel computing hardware, and thus it may serve as a low-cost method of achieving robustness in autonomous systems.
