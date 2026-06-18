<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DBaS-Log-MPPI: Efficient and Safe Trajectory Optimization via Barrier States

Topics include Model predictive path integral control, Trajectory optimization, Safety, Barrier states, Constraint satisfaction.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Integrates logarithmic barrier states (DBaS) into the dynamics, providing smooth cost shaping that discourages safety constraint violations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Optimizing trajectory costs for nonlinear control systems remains a significant challenge. Model Predictive Control (MPC), particularly sampling-based approaches such as the Model Predictive Path Integral (MPPI) method, has recently demonstrated considerable success by leveraging parallel computing to efficiently evaluate numerous trajectories. However, MPPI often struggles to balance safe navigation in constrained environments with effective exploration in open spaces, leading to infeasibility in cluttered conditions. To address these limitations, we propose DBaS-Log-MPPI, a novel algorithm that integrates Discrete Barrier States (DBaS) to ensure safety while enabling adaptive exploration with enhanced feasibility. Our method is efficiently validated through three simulation missions and one real-world experiment, involving a 2D quadrotor and a ground vehicle navigating through cluttered obstacles. We demonstrate that our algorithm surpasses both Vanilla MPPI and Log-MPPI, achieving higher success rates, lower tracking errors, and a conservative average speed.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

With the increasing focus on robotic control, designing safe and reliable control methods for autonomous robots operating in unknown environments---while maintaining real-time performance---remains a significant challenge. Successful navigation requires robots to accurately detect both static and dynamic obstacles, including convex and non-convex shapes, using appropriate sensors. Moreover, robots must dynamically re-plan their trajectories to avoid local optima, prevent collisions, and reach their target locations efficiently. These requirements give rise to a complex control optimization problem that is inherently difficult to solve in real-time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Model predictive control (MPC), a well-established control framework, offers robust navigation capabilities by handling obstacles under both hard and soft system constraints. MPC employs a receding horizon strategy to generate a sequence of control inputs over a predefined prediction window. Only the first input is executed, while the remaining inputs serve as warm starts for subsequent optimization steps. MPC methods can be broadly categorized into gradient-based and sampling-based approaches. Gradient-based MPC leverages optimization techniques to generate smooth, collision-free trajectories while enforcing system constraints. However, this approach relies on strong assumptions, such as the differentiability and convexity of cost functions, system constraints, and obstacle geometries---assumptions that often limit real-world applicability. Recent efforts to address nonconvexity include reformulating non-differentiable constraints into differentiable forms and constructing convex hulls in cost maps. However, these solutions remain computationally demanding.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In contrast, sampling-based MPC, such as the model predictive path integral (MPPI), circumvents gradient computations and efficiently handles nonconvex environments. By evaluating trajectories sampled from a probability distribution, MPPI explores diverse state-space possibilities to identify optimal paths. However, its performance is highly dependent on the sampling distribution and remains susceptible to local optima. Inspired, we propose an enhanced MPPI framework that employs a normal-log-normal mixture distribution to improve trajectory sampling efficiency and enhance adaptive exploration around local optima. Furthermore, we simplify safety constraints by integrating barrier states, transforming the original optimization constraints into a state stabilization problem. This reformulation reduces optimization complexity, enabling our method to outperform MPPI-based approaches in both computational efficiency and navigation performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper is organized as follows: Section III introduces the fundamentals of MPPI and barrier states. Section IV presents the proposed DBaS-Log-MPPI method. In Section V, we validate our approach in simulation with 2D quadrotor and ground vehicle, comparing its performance against Vanilla MPPI and log-MPPI. Furthermore, we demonstrate our method's real-time performance in a real-world experiment on the ground vehicle "Antelope", showcasing the effectiveness in challenging trajectory tracking scenarios.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Related Works", "weight": 1.0} -->

Real-time robotic navigation in the presence of cluttered obstacles is challenging, necessitating rapid adaptation to both static and dynamic obstacles and the ability to reliably reach goals without becoming trapped in local optima. Current approaches to tackle this task primarily fall into two categories: control-oriented methods and learning-based approaches.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Related Works", "weight": 1.0} -->

Control-oriented approaches, notably Model Predictive Control (MPC), address robotic navigation by solving constrained optimization problems online over a finite horizon. Prior to MPC, classical control methods such as the Linear Quadratic Regulator (LQR) provided optimal open-loop solutions for trajectory tracking tasks. However, these approaches are limited due to their offline computational nature and inability to handle dynamic obstacles and environmental uncertainties in real-time. Moreover, LQR inherently assumes linear system dynamics or requires linearization for nonlinear scenarios, making it unsuitable for complex, nonlinear, high-dimensional systems. Finite-horizon LQR or MPC extend these capabilities by solving constrained optimization problems online, explicitly managing state and input constraints. Gradient-based MPC methods necessitate differentiable constraints and cost functions, enabling smooth control sequences. However, these methods impose strong assumptions such as differentiability and convexity of cost functions, thus limiting their applicability in scenarios involving non-convex and non-differentiable objectives. Several approaches have been developed to overcome these limitations. For example, introduced computationally efficient stochastic MPC using chance constraints that activate only when necessary. proposed data partitioning from LiDAR sensors into convex shapes to enforce convexity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

Sampling-based MPC methods, such as Model Predictive Path Integral (MPPI), mitigate these issues by employing stochastic sampling without strict differentiability and convexity requirements. Nonetheless, MPPI methods can produce non-smooth trajectories and potentially infeasible control sequences, particularly due to poor sampling distributions. Addressing these issues, modified the sampling distribution strategically, while proposed methods to smooth control sequences.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

Alternatively, learning-based methods, primarily represented by reinforcement learning (RL), offer promising directions to tackle these navigation challenges. RL utilizes offline data-driven optimization during training, circumventing computationally intensive online optimization, thus enhancing real-time performance compared to MPC. Despite these advantages, training RL agents for effective obstacle avoidance remains challenging because obstacle avoidance objectives are typically represented as soft costs within reward functions. This presents difficulty in enforcing strict safety constraints. Control Barrier Functions (CBFs) have emerged as robust safety mechanisms integrated with RL as safety filters, ensuring trajectories remain within predefined safe sets during training and deployment. Nonetheless, RL methods encounter significant performance degradation due to environmental perturbations, particularly when policies trained in simulation are transferred to real-world robotic systems. Efforts to improve safety and robustness of RL through adaptive control were presented. Other methods such as domain randomization and meta-learning have been utilized to enhance long-term robustness and safety but may lack ability to robustify RL policies instantly without the prior knowledge of the uncertainties.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

We consider a discrete-time nonlinear control system described by

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

where $x_{k} \in {\mathbb{R}}^{n}$ denotes the state at time $k$, and the control sequence with dimension $m$ over time horizon $N$ is given by

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

The resulting state trajectory is denoted by

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

The objective is to find a control sequence $U$ that steers the system from an initial state $x_{c}$ to a desired terminal state $x_{f}$ while avoiding collisions and satisfying constraints. Unlike gradient-based Model Predictive Control (MPC) approaches, the Model Predictive Path Integral (MPPI) method avoids derivative computations, making it suitable for highly nonlinear, non-convex objectives.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

where $\phi{(x_{N})}$ is the terminal cost, $q{(x_{k})}$ is a state-dependent running cost, $R$ is a positive definite control weighting matrix, and $v_{k} = {u_{k} + {\delta u_{k}}}$ with ${\delta u_{k}} \sim {\mathcal{N}{(0,\Sigma_{u})}}$ representing the injected noise.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

At each time step, MPPI generates $M$ trajectories in parallel by perturbing the control inputs. The cost-to-go for a sampled trajectory $\tau$ is defined as

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

where $\gamma$ governs the influence of the control cost.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A MPPI-Based Control with Constraints", "weight": 1.0} -->

where $\rho = {{\min_{m}\overset{\sim}{S}}{(\tau_{k,m})}}$ and $\lambda > 0$ is the inverse temperature parameter. Finally, a smoothing operation (e.g., Savitzky--Golay filtering) is applied to reduce noise, and the control input $u_{0}^{\ast}$ is applied in a receding horizon framework.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Discrete Barrier States for Safety", "weight": 1.0} -->

Safety is ensured if the state remains within a safe set $S \subset {\mathbb{R}}^{n}$ for all time steps. Traditional Control Barrier Functions (CBFs) enforce safety through solving complex optimization problems, while barrier states provide a more intuitive and direct representation of safety constraints by explicitly encoding the collision assessment into states, which can be more flexible and computational effective in handling dynamic environments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Discrete Barrier States for Safety", "weight": 1.0} -->

Our approach embeds safety constraints into the system dynamics via DBaS. We define a barrier function $B:{S\rightarrow{\mathbb{R}}}$ that is smooth and strongly convex on the interior of $S$ and diverges as the state approaches the boundary $\partial S$. Composing $B$ with a function $h{(x)}$ that characterizes the safety condition, we define the barrier state as

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Discrete Barrier States for Safety", "weight": 1.0} -->

To integrate safety, we augment the state with the barrier state to form an extended state ${\hat{x}}_{k} = \begin{bmatrix}
\end{bmatrix}$. The safety-embedded system dynamics are then given by

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Discrete Barrier States for Safety", "weight": 1.0} -->

where $\gamma \in {}$ is a tunable parameter and $x_{d}$ denotes the desired equilibrium. For multiple constraints, a fused barrier state is constructed and appended to the state. The system is safe if and only if ${\beta{(x_{k})}} < \infty$ for all $k$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "DBaS-Log-MPPI", "weight": 1.0} -->

In this section, we will introduce the detailed algorithm of DBaS-Log-MPPI, the block diagram could be referred to Fig..

<!-- chunk {"id": "body-0025", "role": "body", "section": "DBaS-Log-MPPI", "weight": 1.0} -->

Integrating of Barrier States: By embedding barrier states into the system dynamics, safety concerns are directly addressed as part of the controlled states. This allows the controller to maintain safety as the cost of these barrier states is incorporated into the running cost, replacing the traditional collision impulse-indicator cost. This ensures that safety is inherently and comprehensively considered in the optimization process.

<!-- chunk {"id": "body-0026", "role": "body", "section": "DBaS-Log-MPPI", "weight": 1.0} -->

Adaptive Exploration: The cost mechanism guides our adaptive exploration strategy. As the trajectories closer to obstacles incur higher running costs, reflecting increased collision risk. To circumvent local optima---often encountered without finely tuned injected noise variance---the algorithm automatically increases the exploration rate from the dynamic running cost, encouraging diverse trajectory sampling and facilitating the discovery of approximately optimal trajectories. Once the initial broad search identifies promising regions, the exploration rate is reduced in subsequent steps, enabling precise convergence to near-optimal solutions while preserving safety guarantees.

<!-- chunk {"id": "body-0027", "role": "body", "section": "DBaS-Log-MPPI", "weight": 1.0} -->

Enhanced Feasibility with Log-sampling Strategy: While adaptive exploration with a larger covariance matrix $\Sigma_{u}$ can lead to input chattering and potential violations of system constraints, particularly in cluttered and input-constrained environments, the Log-sampling strategy offers a significant improvement. This strategy employs a mixture of normal and Log-normal distributions ($\mathcal{N}\mathcal{L}\mathcal{N}$ mixture) for trajectory sampling, ensuring more efficient state-space exploration with lower variance. By respecting system constraints and reducing the risk of local minima, the Log-sampling strategy enhances feasibility and achieves superior performance with fewer samples.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A DBaS augmentation with the running cost", "weight": 1.0} -->

In the Vanilla MPPI framework, constraints are typically evaluated using weighted indicator terms. These terms impose an impulse-like penalty upon constraint violation, effectively acting as a hybrid approach between hard and soft constraints. However, this method has a critical limitation: it provides no risk information until a constraint is actually violated. This poses significant challenges for trajectory optimization, particularly in scenarios involving narrow passages or high speeds. Specifically, until a collision is predicted to occur, all trajectories are evaluated solely based on state-dependent costs, without any consideration of proximity to constraints or potential risks. This lack of proactive safety assessment can lead to unsafe trajectories in complex environments, as illustrated in Fig. 3(a) in the results section. To address this limitation, we propose the following Discrete Barrier State augmentation in the running cost.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A DBaS augmentation with the running cost", "weight": 1.0} -->

Starting at each loop, the control input perturbations $\delta u_{k}$ and their corresponding trajectories are sampled according to the desired exploration rate (introduced in SectonIV-B), guided by the DBaS augmented system dynamics. The DBaS ensures that all sampled trajectories remain safe by embedding safety constraints directly into the system dynamics.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A DBaS augmentation with the running cost", "weight": 1.0} -->

where ${\hat{x}}_{k}$ represents the augmented system state embedded with the DBaS. The stochastic sampling of candidate trajectories and their subsequent cost evaluations remain unchanged, ensuring that the convergence behavior of the Model Predictive Path Integral (MPPI) algorithm is preserved. The integration of DBaS does not compromise the asymptotic convergence properties of MPPI, as it seamlessly incorporates safety considerations into the cost structure. This approach guarantees strict constraint satisfaction while maintaining the stability, robustness, and convergence guarantees inherent to the underlying optimization framework.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A DBaS augmentation with the running cost", "weight": 1.0} -->

Additionally, DBaS provides a significant advantage in controlling high relative-degree systems, where constraints at the output level are influenced through multiple derivatives of the control input. Traditional methods often require defining barrier functions at higher derivatives and incorporating carefully chosen exponential terms to achieve exponential stability of constraint enforcement. In contrast, DBaS leverages costate dynamics to naturally encapsulate the interdependencies between states and constraints.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A DBaS augmentation with the running cost", "weight": 1.0} -->

By sampling the barrier state alongside the perturbed input at each time step, we ensure that safety constraints are satisfied throughout the trajectory without the computational burden of solving the barrier state equation at every iteration.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A DBaS augmentation with the running cost", "weight": 1.0} -->

where the term ${C_{B}{(\hat{X})}} = {\sum_{k = 0}^{N}{R_{B}w{(x_{k})}}}$ represents the barrier state cost along the trajectory. $R_{B}$ is the cost weight on the barrier state. The barrier state itself is inherently positive, so there is no need to square it to ensure positive definiteness in the cost term. The cost-to-go function implies that collisions are penalized in the sampled trajectory, even though only the first control instance is applied to the system (as described in ).

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Adaptive trajectory sampling", "weight": 1.0} -->

$M$ trajectories are sampled using the same covariance matrix $\Sigma_{u}$ to derive "near-optimal" controls in the Vanilla MPPI. This approach takes the advantage of high computational efficiency by avoiding the need for explicit gradient calculations, as required in traditional optimization methods.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Adaptive trajectory sampling", "weight": 1.0} -->

Using a relatively small $\Sigma_{u}$ facilitates fine trajectory evaluation in loosely-constrained tasks, as most sampled trajectories are closely clustered. However, in tightly-constrained scenarios, this limited exploration can result in entrapment in local optima. The controller fails to explore sufficient portions of the state space, making it difficult to identify feasible paths through narrow gaps or complex obstacles. A detailed visual explanation could be found in Fig. 3(b) in the results section.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Adaptive trajectory sampling", "weight": 1.0} -->

Using a relatively large $\Sigma_{u}$ increases the likelihood of finding a feasible path in tightly-constrained scenarios, as the sampled trajectories explore a broader hyper-space of the controller. However, this approach can underperform in open spaces, where widely dispersed trajectories lead to coarse optimization results rather than precise path-following with accurate tracking. Additionally, excessive exploration can introduce input chattering and increase the risk of violating system constraints. A detailed visual explanation could be found in Fig. 3(c) in the results section.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Adaptive trajectory sampling", "weight": 1.0} -->

We propose an adaptive trajectory sampling framework leveraging the DBaS property to ensure constraint satisfaction. By embedding DBaS into the nominal state, we ensure constraints are inherently satisfied, enabling flexible adjustment of $\Sigma_{u}$ in tightly constrained environments. As the system nears forbidden regions, the barrier function $h{(x_{k})}$ decreases, causing ${B \circ h}{(x_{k})}$ to grow significantly, thereby increasing $w{({\hat{x}}_{k})}$. To balance exploration and precision, we introduce an adaptive exploration rate $S_{e}$, defining the injected disturbance $\delta{\hat{u}}_{k}$ as a $\mathcal{N}\mathcal{L}\mathcal{N}{(0,{S_{e}\Sigma_{u}})}$ distribution (introduced in SectionIV-C).

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Adaptive trajectory sampling", "weight": 1.0} -->

where $\mu \in {}$ is the coarseness factor, which determines the accuracy of trajectory tracking in free space. To prevent overly aggressive exploration, a Logarithmic function is applied to $S_{e}$. This is particularly important in tightly-constrained scenarios, where the barrier cost increases rapidly as the system approaches obstacles or limits. The Logarithmic transformation ensures smooth and controlled exploration behavior.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Adaptive trajectory sampling", "weight": 1.0} -->

After each optimization step, the barrier cost $C_{B}{({\hat{X}}^{\ast})}$ is evaluated for the trajectory using the current optimal control input ${\mathbb{U}}^{\ast}$, dynamically adjusting $S_{e}$ to maintain a balance between exploration and constraint satisfaction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Enhanced feasibility with Log-sampling strategy", "weight": 1.0} -->

Augmenting DBaS with adaptive trajectory sampling has demonstrated strong performance in obstacle avoidance tasks. However, systems operating at high speeds may still face "emergency avoidance" scenarios when fast-approaching obstacles, due to the limited prediction horizon $N$. Infeasibility arises when the explored trajectories cannot turn or brake quickly enough within the constrained sampling space. The Log-sampling strategy addresses this limitation by employing a mixture of normal and Log-normal distributions for trajectory sampling. This approach enhances exploration efficiency, enabling faster and more feasible responses to cluttered obstacles, particularly in high-speed scenarios. By combining DBaS with Log-sampling, the framework achieves improved robustness and feasibility in complex, time-critical environments.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Enhanced feasibility with Log-sampling strategy", "weight": 1.0} -->

The detailed injected disturbance $\delta{\hat{u}}_{k}$ is sampled under this distribution ${\delta{\hat{u}}_{k}} \sim {\mathcal{N}\mathcal{L}\mathcal{N}{(\mu_{nln},\sigma_{nln})}}$. It is pointed out that even if ${\mu_{n} = 0},$ $\mu_{nln} = 0$, indicating $\delta{\hat{u}}_{k}$ would be a symmetric distribution around 0. Even with a same value of $\mu$, normal distribution would explore less action space and state space compared to normal-log-normal distribution.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-D MPPI-DBaS with adaptive exploration algorithm", "weight": 1.0} -->

Consistent with the approach outlined in Fig., we present the detailed DBaS-Log-MPPI Algorithm as above.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we design three distinct navigation missions in simulation to evaluate the proposed algorithm's performance for a quadrotor and a ground vehicle. For each mission, 100 experiments are conducted, and the results are summarized in Table I. Key metrics include task success rate (collision-free), relative path tracking error, and average tracking speed.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Additionally, the algorithm is implemented on the "Antelope" ground vehicle in a real-world scenario. The experiments demonstrate the algorithm's effectiveness in performing safe trajectory optimization in challenging navigation tasks.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Quadrotor navigation simulation", "weight": 1.0} -->

We first design a simulation scenario for the 2D quadrotor experiment.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Quadrotor navigation simulation", "weight": 1.0} -->

where $\mathbf{x}_{\mathbf{k}} = {\lbrack x,z,\theta,v_{x},v_{z}\rbrack}$ represents the position $x$, position $z$, pitch $\theta$, velocity $v_{x}$ and velocity $v_{z}$ expressed in the world frame. The control $\mathbf{u}_{\mathbf{k}} = {\lbrack\omega,u_{t}\rbrack}$ represents the control signal of pitch rate and throttle (thrust force over gravity) with limits of $\lbrack{\pm {{4rad}/s}},{\pm {0.981N}}\rbrack$. The quadrotor are set with 0.4$m$ frame length, 0.5$kg$ mass, 0.005$kgm^{2}$ moment of inertia. The gravity $g$ is set to 9.81$m/s^{2}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Quadrotor navigation simulation", "weight": 1.0} -->

We propose a specific quadrotor model where collision detection is facilitated by defining seven shape points. These shape points are positioned at both propellers and each quarter points along the frame.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Quadrotor navigation simulation", "weight": 1.0} -->

where $x_{i}$ denotes the shape points and $x_{c}^{i}$ is the center of $i$th circle obstacle with radius of $r_{c}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Quadrotor navigation simulation", "weight": 1.0} -->

Sampling covariance matrix $\Sigma_{u}$ are set as $\begin{bmatrix}
\end{bmatrix}$, $\gamma$ are set to be 2 for all three algorithms. Coarseness factor $\mu$ is set to be 0.4 in DBaS-Log-MPPI. The real-time execution is carried out on an NVIDIA GeForce GTX 3070 laptop GPU, where all algorithms were written in Python. The prediction time horizon $N$ is set to 20 steps, the sampling time $\Delta t$ is set to be 0.02$s$ and parallel sampled trajectories number $M$ is set to 1024. The average processing time is 0.017 s, with no significant differences observed among the three algorithms.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A Quadrotor navigation simulation", "weight": 1.0} -->

The 2D quadrotor is tasked with navigating through three obstacles (each with a radius of 0.8$m$) positioned along the trajectory with narrow gaps, at a reference speed of 1$m/s$. The mission configuration and results are illustrated in Table I and Fig..

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-A Quadrotor navigation simulation", "weight": 1.0} -->

Vanilla MPPI, without fine-tuning, struggles significantly in this challenging scenario, achieving a 0% success rate with collisions occurring in all trials, as shown in Fig. 3(a). Log-MPPI achieves a modest success rate of 43% in Mission 2. However, without the adaptive exploration proposed in our algorithm, Log-MPPI often becomes trapped in local optima (Fig. 3(b)), or detour with high tracking error (Fig. 3(c)). In contrast, our DBaS-Log-MPPI algorithm achieves a 100% success rate, as demonstrated in Fig. 3(d). It exhibits the smallest tracking error (2.889$m$) and an average tracking velocity of 0.721$m/s$, which is lower than Log-MPPI due to its continuous collision risk assessment. This indicates that the DBaS implementation leads to a more conservative yet safer tracking speed, as it avoids impulse-like penalties upon constraint violations in scenarios where high speed is not demanded.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Ground vehicle navigation simulation", "weight": 1.0} -->

We then design simulation scenarios for the ground vehicle experiment.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Ground vehicle navigation simulation", "weight": 1.0} -->

where $\mathbf{x}_{\mathbf{k}} = {\lbrack x_{k},y_{k},\theta_{k},v_{k}\rbrack}$ represents the position $x$, position $y$, heading angle $\theta$ and linear velocity $v$ expressed in the world frame. The control $\mathbf{u}_{\mathbf{k}} = {\lbrack\phi,a\rbrack}$ denotes the control signal of steering angle and acceleration with limits of $\lbrack{\pm {1.013rad}},{\pm {{2m}/s^{2}}}\rbrack$. We propose a specific vehicle model for this purpose, where collision detection is facilitated by defining eight shape points on the vehicle's geometric model---a rectangle with a length of 4 meters and a width of 3 meters. These shape points are positioned at the corners and midpoints along each side of the rectangle.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Ground vehicle navigation simulation", "weight": 1.0} -->

where $x_{i}$ denotes the shape points and $x_{c}^{i}$ is the center of $i$th circle obstacle with radius of $r_{c}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B Ground vehicle navigation simulation", "weight": 1.0} -->

Sampling covariance matrix $\Sigma_{u}$ are set as $\begin{bmatrix}
\end{bmatrix}$, $\gamma$ are set to be 2 for all three algorithms. Coarseness factor $\mu$ is set to be 0.4 in DBaS-Log-MPPI. The real-time execution is carried out on an NVIDIA GeForce GTX 3070 laptop GPU, where all algorithms were written in Python. The prediction time horizon $N$ is set to 20 steps, the sampling time $\Delta t$ is set to be 0.02$s$ and parallel sampled trajectories number $M$ is set to 1024. The average processing time is 0.015 s, with no significant differences observed among the three algorithms.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B Ground vehicle navigation simulation", "weight": 1.0} -->

The ground vehicle is tasked with navigating through five obstacles (each with a radius of 4.3$m$) positioned along the trajectory with narrow gaps, at reference speeds of 5$m/s$ in Mission 2 and 8$m/s$ in Mission 3, respectively. The results are summarized in Table I. Details of obstacle avoidance in successful trials for Mission 2 of our algorithm are illustrated in Fig..

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B Ground vehicle navigation simulation", "weight": 1.0} -->

In Mission 2, both Log-MPPI and the proposed algorithm outperform Vanilla MPPI, achieving success rates of 74% and 100%, respectively. Although Vanilla MPPI achieves the highest tracking speed due to its coarse search strategy, our proposed algorithm demonstrates the lowest tracking error, further emphasizing its robust performance assurance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-B Ground vehicle navigation simulation", "weight": 1.0} -->

In Mission 3, the reference speed is more relentless at 8 m/s. Both our algorithm and Log-MPPI exhibit lower success rates compared to Mission 2, while Vanilla MPPI fails completely. On successful trials, the tracking errors for both our algorithm and Log-MPPI are reduced, as the vehicle can recover to the reference trajectory more quickly at higher speeds. However, Log-MPPI approaches obstacles at shorter distances, resulting in smaller tracking error and low average speed due to sharp turns and abrupt detours.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-C Ground vehicle real-world demonstration", "weight": 1.0} -->

Subsequently, we experimentally validated the proposed control strategies in real-world on our ground vehicle, "Antelope" (Fig. 5(a)), for achieving Mission 2 as collision-free navigation in a 2.5$m$ $\times$ 1.9$m$ indoor cluttered environment without prior environmental information.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-C Ground vehicle real-world demonstration", "weight": 1.0} -->

As illustrated in Fig. 5(b), the ground vehicle ("Antelope"), obstacles (constructed using colorful pads), and planned trajectory (marked by red curves) are scaled down by a factor of approximately 1:16 from the simulation scenarios in Mission 2/3. Note that the "Antelope" employs Mecanum wheels; thus, we emulate an Ackermann steering system by applying differential outputs to its original kinematic model. The Luster FZMotion motion capture system (cameras mounted at a high elevation in Fig. 5(b)) is used to obtain ground truth position of obstacles and state value of "Antelope" for post-experiment performance evaluation only.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-C Ground vehicle real-world demonstration", "weight": 1.0} -->

A LiDAR sensor (Livox Mid-360) integrated with FAST-LIO2 is deployed on the "Antelope" to construct a local point cloud map, enabling obstacle pose estimation during the experiment (Fig. 5(c)). The point cloud map is then converted into the 2D grid map for real-time trajectory optimization. All algorithms are deployed on an NVIDIA Jetson Orin Nano with 67 TOPS on 1024 GPU cores and a 1.7 GHz CPU frequency. The trajectories are visualized as follows: Vanilla MPPI as yellow curve, Log-MPPI as blue curve, and our algorithm as green curve. Similar to the Mission 2 results, Vanilla MPPI frequently fails in obstacle avoidance, whereas our algorithm surpasses Log-MPPI with lower tracking error (Fig. 5(d)).

<!-- chunk {"id": "body-0062", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This paper presents a novel DBaS-Log-MPPI controller that adaptively explores the action space through effective sampling within barrier states embedded in dynamics ensuring safety guarantees. The integration of the barrier state enables the proposed algorithm with continuous collision risk assessment. Furthermore, the adaptive exploration mechanism enhances sampling diversity and coverage, particularly in proximity to obstacles. Extensive validation through three simulation missions and one real-world experiment demonstrates that the proposed algorithm achieves a higher success rate, lower tracking errors, and more conservative tracking velocities compared to baseline methods.

<!-- chunk {"id": "body-0063", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Future work will focus on refining the controller by developing more comprehensive safety barrier formulations and extending its application to complex control scenarios, such as multi-agent planning. Additionally, we plan to implement the algorithm on advanced robotic platforms, including 3D quadrotors and quadruped robots, which present broader action spaces and challenges in sampling effective trajectories.
