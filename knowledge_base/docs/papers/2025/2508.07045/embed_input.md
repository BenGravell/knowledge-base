<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Data to Safe Mobile Robot Navigation: An Efficient and Modular Robust MPC Design Pipeline

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model predictive control (MPC) is a powerful strategy for planning and control in autonomous mobile robot navigation. However, ensuring safety in real-world deployments remains challenging due to the presence of disturbances and measurement noise. Existing approaches often rely on idealized assumptions, neglect the impact of noisy measurements, and simply heuristically guess unrealistic bounds. In this work, we present an efficient and modular robust MPC design pipeline that systematically addresses these limitations. The pipeline consists of an iterative procedure that leverages closed-loop experimental data to estimate disturbance bounds and synthesize a robust output-feedback MPC scheme. We provide the pipeline in the form of deterministic and reproducible code to synthesize the robust output-feedback MPC from data. We empirically demonstrate robust constraint satisfaction and recursive feasibility in quadrotor simulations using Gazebo.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mobile robots have significant potential to meet societal needs, for example, in autonomous search and rescue operations, intralogistics, and self-driving vehicles. These applications require robots to navigate autonomously while avoiding collisions. To address this challenge, various planning techniques have been developed, including reactive, sampling-based, and optimization-based methods. These planners typically use nonlinear dynamical system models, which, despite their accuracy, cannot capture all real-world behaviors, leading to model uncertainty. In addition, real-world experiments cannot provide accurate state information and only noisy estimates can be derived from sensor data. If not explicitly considered, such errors can jeopardize robot safety, potentially causing crashes. Therefore, this work aims to ensure collision-free navigation despite uncertainties in the nonlinear robot model.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several methods have been proposed to handle model uncertainty and ensure safe motion planning. These include control barrier functions, reachability-based methods, and model predictive control (MPC). MPC approaches can be categorized into stochastic MPC, providing probabilistic safety guarantees, and robust MPC, offering deterministic safety guarantees.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work focuses on robust MPC, optimizing trajectories to remain feasible and collision-free under worst-case disturbances. To mitigate conservatism, feedback controllers are used, for example in funnel-based approaches and tube MPC. For nonlinear robot dynamics, recent approaches leverage contraction metrics to derive bounds on the tracking error that are then leveraged in the MPC, see.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing robust MPC schemes requires knowledge of the worst-case model uncertainty, which includes disturbances, parametric uncertainty, and measurement noise. State-of-the-art methods often assume simplified uncertainty sets, such as linear drag models, norm-bounded wind disturbances, and polytopic wind disturbances and mass uncertainty. These assumptions can be satisfied in simulations, but are not realistic in experimental environments. Although, e.g. has empirically demonstrated safety in hardware experiments using a quadrotor, this also relied on heuristically added safety margins of over half a meter. To facilitate the reliable deployment of robust MPC in real-world applications, this work aims to infer bounds on the model uncertainty directly from noisy measured data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Obtaining accurate and realistic bounds on uncertainties is crucial for the performance and reliability of robust MPC schemes. Methods to quantify model uncertainty include learning-based approaches such as Gaussian Processes (GPs) and neural networks, which use statistical tools to provide probabilistic bounds. However, these tools rely on strong assumptions about the distribution of the noise and can typically not deal with noisy inputs (cf. ). Distribution-agnostic conformal prediction offers another approach, though it requires samples of the uncertainty. Set-membership estimation also provides distribution-agnostic bounds, but is susceptible to outliers. In general, the key challenge in quantifying uncertainty relates to the fact that the model error and states are not measured. Popular approaches for estimation include the extended Kalman filter and particle filter, but they suffer from linearized approximations or sample inefficiency, respectively. Moving horizon estimation (MHE) \[13, Chap. 4\] is a modern optimization-based estimation method, which can be applied to general nonlinear robot dynamics to compute optimal estimates.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, despite the strong theoretical foundation of robust MPC, applications typically rely on simplifying assumptions about the model uncertainty that do not accurately reflect experiments. To overcome these limitations and move towards efficient and reliable applications of robust MPC, we contribute an efficient and modular design pipeline, which is visualized in Figure 1. Our main contributions are: Uncertainty quantification: A scheme to determine bounds on the model uncertainty for general nonlinear systems using a simple iteration involving an MHE formulation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A robust output-feedback MPC-based planning and tracking framework (ROHMPC) that ensures safety and recursive feasibility in the presence of disturbances and measurement noise (Theorem 1).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

An efficient, modular, and reproducible software pipeline, identifying model uncertainty, computing robust and terminal ingredients, yielding a robust MPC implementation that can be directly deployed.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply the pipeline in simulation experiments with the Gazebo *RotorS* package including significant structural model mismatch and noisy measurements, yielding an empirically safe robust MPC within 2 hours.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

General approach: We use a robust output-feedback MPC formulation to ensure collision avoidance despite the presence of disturbances and measurement noise. This formulation tightens the constraints based on the impact of the worst-case disturbance on the system. Correspondingly, we would like to obtain a bound in the form ${\bm{w}}\in{\mathcal{W}}$ and ${\bm{\eta}}\in{\mathcal{H}}$, with polytopic disturbance and noise sets ${\mathcal{W}}$, ${\mathcal{H}}$. However, the sets ${\mathcal{W}}$ and ${\mathcal{H}}$ are not trivial to obtain since both ${\bm{w}}$ and ${\bm{\eta}}$ cannot be directly measured on the real system. Therefore, we propose a method to offline estimate ${\mathcal{W}}$ and ${\mathcal{H}}$ using an iterative MHE approach, as described in Section III.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

These bounds are then used in the robust output-feedback MPC design described in Section IV. This section also provides the theoretical analysis of the scheme, ensuring recursive feasibility, robust constraint satisfaction, and a bounded tracking error. Finally, Section V demonstrates the results of the proposed uncertainty quantification method and the closed-loop properties of the ROHMPC scheme using a quadrotor simulation in Gazebo.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Uncertainty quantification for general nonlinear systems", "weight": 1.0} -->

Given model and a time series of IO data $({\bm{u}},{\bm{y}})$ of length ${T^{\mathrm{M}}}$, the goal of this section is to quantify the model uncertainty, i.e., estimate disturbance ${\bm{w}}$ and measurement noise ${\bm{\eta}}$. Specifically, we find estimated values ${\hat{\bm{w}}}$ and ${\hat{{\bm{\eta}}}}$ using the following formulation: which is a receding horizon estimation scheme with prediction horizon ${T^{\mathrm{H}}}$ and weighting matrices $Q$ and $R$, comparable to MHE \[13, Chap. 4\].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Uncertainty quantification for general nonlinear systems", "weight": 1.0} -->

To obtain estimates ${\hat{\bm{w}}}$ and ${\hat{{\bm{\eta}}}}$ that are representative of the real ${\bm{w}}$ and ${\bm{\eta}}$ encountered during closed-loop experiments, it is beneficial to cover a large part of the state-input space ${\mathcal{Z}}$. This requires a larger data length ${T^{\mathrm{M}}}$. However, collecting more data increases the computational complexity. To prevent intractability of, we use a receding horizon implementation with horizon length ${T^{\mathrm{H}}}<{T^{\mathrm{M}}}$. Weighting matrices $Q$ and $R$ should reflect the inverse covariance matrices of the disturbance and measurement noise. Since their exact values are unknown, we repeatedly solve and update $Q$ and $R$ until convergence of their eigenvalues. This iteration is comparable to the expectation-maximization (EM) algorithm classically used for identification.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Uncertainty quantification for general nonlinear systems", "weight": 1.0} -->

In particular, the optimized cost in is proportional to the neg-log likelihood (assuming noise is Gaussian distributed), and as we see in the experiments (Sec. V), this iteration monotonically improves estimates. After this loop, we compute the bounding box ${\hat{{\mathcal{W}}}}$ containing all estimated disturbance samples ${\hat{\bm{w}}}_{{\tau|t}},\tau=\frac{{T^{\mathrm{H}}}}{2},t\in[0,{T^{\mathrm{M}}}]$, since the estimated values in the middle of the horizon are the most accurate, and set the model bias ${\hat{\bm{w}}^{\mathrm{b}}}$ equal to its center. The bias can be used to increase the accuracy of the nominal model. Bounding box ${\hat{{\mathcal{H}}}}$ is computed similarly, however, centered around $\bm{0}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Robust output-feedback MPC design", "weight": 1.0} -->

The goal of this section is to describe the robust MPC design that ensures safe and autonomous navigation towards ${\bm{p}^{\mathrm{g}}}$ while robustly avoiding collisions in the presence of ${\bm{w}}$ and ${\bm{\eta}}$. To this end, we summarize the robust output-feedback MPC theory described in and connect it to the uncertainty quantification method from previous section. Furthermore, we propose the ROHMPC scheme, which is based on the HMPC framework, using a co-designed planning MPC (PMPC) and tracking MPC (TMPC) scheme. The PMPC formulation only requires an adjusted model and tightening margins. Therefore, the focus in this section is on the robust TMPC design. Section IV-A describes the offline robust output-feedback design. This includes the combined design of an observer and an incremental Lyapunov function with the corresponding feedback law.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Robust output-feedback MPC design", "weight": 1.0} -->

The upper bound of this Lyapunov function, called the tube size, is used to formulate a simple constraint-tightening TMPC scheme in Section IV-B. Section IV-C describes the offline design of suitable terminal ingredients used to prove robust constraint satisfaction and recursive feasibility of the ROHMPC scheme in Section IV-D.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Offline robust output-feedback design", "weight": 1.0} -->

The main challenge in designing robust output-feedback MPC schemes is to guarantee that the closed-loop system satisfies the original constraints in the presence of disturbances and measurement noise. To solve this problem, we compute an estimated state ${\hat{\bm{x}}}$ based on noisy measurements ${\bm{y}}$ and make sure that both controller error ${\bm{\delta}}\coloneqq{\hat{\bm{x}}}-{\bm{z}}$, with respect to nominal trajectory ${\bm{z}}$, and observer error ${\bm{\epsilon}}\coloneqq{\bm{x}}-{\hat{\bm{x}}}$, with respect to actual state ${\bm{x}}$, are bounded.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that one could use a state-dependent metric to reduce conservatism. In this case, evaluating the geodesic ${{\bm{\gamma}}^{\mathrm{x}}(s)}$ and the Lyapunov function ${V^{\delta}({{\hat{\bm{x}}},{\bm{z}}})}$ would require solving an optimization problem. Since we Since we require the evaluation of ${V^{\delta}({{\hat{\bm{x}}},{\bm{z}}})}$ in the terminal set constraint (15h), this would have resulted in a significant increase in the computational demand. In the special case of a constant feedback matrix ${K^{\delta}}$, the control law reduces to ${\bm{v}}+{K^{\delta}}{\bm{\delta}}$, which is also leveraged in the experiments later.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We bound ${V^{\delta}({{\hat{\bm{x}}},{\bm{z}}})}$ from above by tube size $s$ as with $\dot{s}_{\tau}=-\rho s_{\tau}+{\bar{w}^{\mathrm{o}}}$. Thus, controller error ${\bm{\delta}}$ is bounded by tube size $s$. Furthermore, $s$ grows with bounded factor ${\bar{w}^{\mathrm{o}}}>0$ and contracts with rate $\rho$. Due to its $\rho$-contractivity, $s$ cannot grow unbounded, making it suitable as a constraint tightening factor for system constraints (II) and obstacle avoidance constraints.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To show constraint satisfaction for ${\bm{x}}$, we also need to account for the difference between ${\hat{\bm{x}}}$ and ${\bm{x}}$. By the UQ method in Section III, we know that the measurement noise is bounded, i.e., ${\hat{{\bm{\eta}}}}\in{\hat{{\mathcal{H}}}}$. Combined with observer, we can construct a constant tube $\epsilon$ bounding ${\bm{\epsilon}}$ as Thus, we ensure satisfaction of constraints in (II) and by tightening the constraints on the nominal trajectory $z$ proportional to the two error bounds $\epsilon,s$ using suitable constraint tightening constants.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The SDP optimizes for the smallest constraint tightening constants ${c_{j}^{\mathrm{s}}},{c_{j}^{\mathrm{s,o}}},j\in{\mathbb{N}_{[1,{n^{\mathrm{s}}}]}}$, with and ${c^{\mathrm{o}}}$. This is imposed by the combination of (7a), (7d), (7e), (7f), and (7g). To avoid conservatism in certain directions of the state space, the constraint tightening constants are normalized by their corresponding constant constraint intervals ${c_{j}^{\mathrm{c,s}}}$ and ${c^{\mathrm{c,o}}}$ in (7a). In this case, ${c^{\mathrm{c,o}}}$ represents the minimum desired distance to obstacles. Moreover, $c^{\epsilon}$ is a penalty term to reduce $\epsilon$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Offline terminal ingredients design", "weight": 1.0} -->

The goal of this section is to find a terminal control law that renders ${\mathcal{X}^{\mathrm{f}}}({\bm{x}^{\mathrm{r}}})$ invariant and ensures that we know a lower bound on the decrease of ${{\mathcal{J}}^{\mathrm{f}}}({\bm{z}},{\bm{x}^{\mathrm{r}}})$ over time. These properties are used to prove the recursive feasibility and trajectory tracking in Section IV-D, respectively.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Results", "weight": 1.0} -->

This section first presents relevant implementation details (Section V-A) and continues with the results of the proposed uncertainty quantification method (Section V-B), the robust output-feedback design and tightening calibration (Section V-C), and ROHMPC scheme (Section V-D).

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Implementation details", "weight": 1.0} -->

This section provides the nominal quadrotor model and its corresponding constraints in Section V-A1, the model uncertainty description in Section V-A2, and the software setup used to generate the results in the next sections in Section V-A3.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A1 Quadrotor model and constraints", "weight": 1.0} -->

The nominal quadrotor model is based: with states including 3D positions in inertial frame ${\mathcal{I}}$, ZYX Euler angles, velocities and angular velocities in the body frame, thrust and torques defined as a linear function of the inputs ${\bm{u}}=[t_{0},t_{1},t_{2},t_{3}]^{\top}$ in which $t_{i}$ is the thrust of rotor $i$, gravitational constant $g=9.8124$, mass $m=0.617$, inertia matrix $I=\operatorname{diag}(0.00164,0.00184,0.0030)$, and coordinate and rate rotation matrices ${\prescript{{\mathcal{I}}}{{\mathcal{B}}}{{\mathcal{R}^{\mathrm{c}}}}}$ and

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A1 Quadrotor model and constraints", "weight": 1.0} -->

${\prescript{{\mathcal{I}}}{{\mathcal{B}}}{{\mathcal{R}^{\mathrm{r}}}}}$ to convert coordinates and rates from body to inertial frame. Sine, cosine, and tangent functions are defined as $s\theta=\sin(\theta)$, $c\theta=\cos(\theta)$, $t\theta=\tan(\theta)$, for example.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A3 Software setup", "weight": 1.0} -->

The code corresponding to In constructing the software pipeline, special care was taken to ensure modularity and reproducibility. One aspect to highlight is the fact that the code contains an adjusted version of the open-source stack Agilicious in order to ensure deterministic *RotorS* simulation results. Moreover, the results are trivial to reproduce as a Docker container is provided, in line with the recommendation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A3 Software setup", "weight": 1.0} -->

The results presented in the next sections are generated using a Dell XPS 15 laptop with a 12-core 2.60GHz Intel i7-10750H CPU. We leverage the ACADOS SQP solver to solve UQ problem, Mosek to solve SDP, and the ForcesPro NLP solver to solve PMPC problem and TMPC problem.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Uncertainty quantification", "weight": 1.0} -->

Recall that the purpose of solving UQ problem is to find bounding boxes ${\hat{{\mathcal{W}}}}$ and ${\hat{{\mathcal{H}}}}$ that are used in the robust output-feedback MPC design in Section IV. We solve using IO data obtained by flying 4 different trajectories using the built-in MPC in Agilicious in the *RotorS* simulator. These trajectories are designed to cover a relevant part of the state-input space and consist of clockwise and counter-clockwise circles and lemniscates with radius 1 m and frequency 0.3 Hz.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Uncertainty quantification", "weight": 1.0} -->

Note that there is a fundamental limitation in estimating ${\bm{w}},{\bm{\eta}}$ using: ${\bm{y}}$ can be explained by both the effect of ${\bm{w}}$ and ${\bm{\eta}}$, which introduces ambiguity. As a result, the solution to practically converges to either explaining ${\bm{y}}$ mainly by ${\bm{w}}$ or by ${\bm{\eta}}$, depending on the initialization of $Q$ and $R$. To mitigate this issue, we start from $Q={I^{{n^{\mathrm{x}}}}}$ and $R={I^{{n^{\mathrm{\eta}}}}}$ and assume that ${\mathcal{H}}$ is known, i.e., it can be derived from the sensor datasheets, and add them as constraints to. In this work, we use the bounds in (V-A2).

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-C Robust output-feedback design", "weight": 1.0} -->

Based on ${\hat{{\mathcal{W}}}}$ and ${\mathcal{H}}$ from the previous section, we solve in 295 s. While the resulting feedback ${\kappa^{\delta}}$ robustly stabilizes the system, the corresponding constraint tightening is overly conservative. To reduce conservatism, we empirically determine the constants used for constraint tightening - $\rho$, ${\bar{w}^{\mathrm{o}}}$, and $\epsilon$ - corresponding to the optimized feedback ${\kappa^{\delta}}$ and Lyapunov function ${V^{\delta}({{\hat{\bm{x}}},{\bm{z}}})}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-C Robust output-feedback design", "weight": 1.0} -->

To calibrate $\rho$, we track a nominal stable reference trajectory with feedback controller and observer and record the nominal reference and the estimated states over time. Using this data, we can compute the tightest s-tube over multiple steps, as visualized in Figure 3. We repeat this process for multiple grid points of $\rho$ and pick $\rho$ with the smallest tightening. This computation takes 3.5 s using a nominal reference duration of 10 s sampled with the simulator, estimation, and feedback frequency of 500 Hz, and gives $\rho=12.5$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C Robust output-feedback design", "weight": 1.0} -->

Given a calibrated $\rho$, we can calibrate ${\bar{w}^{\mathrm{o}}}$ and $\epsilon$ by comparing the estimated state with the one-step ahead predictions of a closed-loop nominal MPC scheme and the ground truth state, respectively. In this simulation, the ground truth state is available. However, in reality one has to pick the more conservative value for epsilon given by SDP. This calibration takes 30.5 s in total, for 144 s of flight time sampled at the TMPC sampling frequency of 100 Hz for ${\bar{w}^{\mathrm{o}}}$ and sampled at 500 Hz for $\epsilon$. The resulting values are ${\bar{w}^{\mathrm{o}}}=0.0337$ and $\epsilon=0.00345$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C Robust output-feedback design", "weight": 1.0} -->

The trajectories used to calibrate ${\bar{w}^{\mathrm{o}}}$ and $\epsilon$ are more aggressive than the ones produced by the ROHMPC framework described next, so they are reasonable to use to guarantee safety.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-D Closed-loop ROHMPC simulation", "weight": 1.0} -->

Given the calibrated tightening constants $\rho$, ${\bar{w}^{\mathrm{o}}}$, and $\epsilon$, we can compute $\alpha$ used for the tightening in the PMPC and run the closed-loop ROHMPC scheme. The goal of this scheme is to fly the quadrotor from a starting position to a goal position and safely avoid the obstacle in between. Figure 4 visualizes the relevant part of the traversed trajectory (close to the obstacle) and shows that the closed-loop system stays within the total TMPC tube, accurately follows the plan, and safely avoids the obstacle. Furthermore, the total TMPC tube does not grow further than the tube used to tighten the constraints in the PMPC, and all tubes are contained in the obstacle-free space. Finally, the closed-loop system is empirically shown to guarantee constraint satisfaction and recursive feasibility.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Guaranteeing safety on autonomous mobile robots is a challenging topic, especially in the presence of disturbances and measurement noise. Whereas other approaches typically assume specific disturbance effects or known, sometimes unrealistic, bounds on the disturbances and do not consider measurement noise, the aim of this work is to take a step toward relaxing these assumptions and work towards reproducible and robust results on real robotic systems. Therefore, this paper proposed a robust MPC design pipeline to guarantee robust constraint satisfaction and recursive feasibility. Furthermore, it verified these properties using a reproducible software stack in a closed-loop simulation of the proposed ROHMPC framework.
