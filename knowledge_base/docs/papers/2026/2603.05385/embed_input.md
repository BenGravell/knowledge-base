<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accelerating Sampling-Based Control via Learned Linear Koopman Dynamics

Topics include Robotics, Vehicles, Real-time systems, Online algorithms, Sampling-based methods, Control, Sampling, Model predictive path integral control, DKO.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents an efficient model predictive path integral (MPPI) control framework for systems with complex nonlinear dynamics. To improve the computational efficiency of classic MPPI while preserving control performance, we replace the nonlinear dynamics used for trajectory propagation with a learned linear deep Koopman operator (DKO) model, enabling faster rollout and more efficient trajectory sampling. The DKO dynamics are learned directly from interaction data, eliminating the need for analytical system models. The resulting controller, termed MPPI-DK, is evaluated in simulation on pendulum balancing and surface vehicle navigation tasks, and validated on hardware through reference-tracking experiments on a quadruped robot. Experimental results demonstrate that MPPI-DK achieves control performance close to MPPI with true dynamics while substantially reducing computational cost, enabling efficient real-time control on robotic platforms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The control of complex robotic systems with nonlinear and high-dimensional dynamics remains a fundamental challenge in robotics, particularly for tasks that demand rapid responses, aggressive maneuvers, and real-time decision-making. Model predictive control (MPC) provides a systematic framework for handling state and input constraints while optimizing performance over a receding horizon. However, when applied to highly nonlinear systems operating at high control frequencies, MPC often incurs significant computational overhead due to repeated online optimization and nonlinear dynamics propagation. This computational burden can limit its practicality in real-time robotic applications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To improve scalability in highly nonlinear dynamics settings, model predictive path integral (MPPI) control has emerged as a powerful information-theoretic approach to stochastic optimal control. Instead of solving a deterministic optimization problem at each step, MPPI performs Monte Carlo trajectory sampling to approximate the optimal control update, naturally accommodating nonlinear dynamics and nonconvex cost functions. Its sampling-based structure is well-suited for parallel computation and has enabled successful applications in aggressive autonomous driving, aerial robotics, and legged locomotion.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these advantages, a fundamental limitation of MPPI is its reliance on repeatedly propagating nonlinear system dynamics during trajectory sampling. For systems with computationally expensive models or constrained onboard resources, this repeated forward simulation can significantly limit the achievable control frequency and hinder scalability. To alleviate this bottleneck, recent work has explored the use of data-driven dynamics models as surrogates for exact nonlinear dynamics within MPC frameworks. Deep neural network (DNN) models, in particular, provide strong expressive capability for approximating complex dynamics. However, their repeated forward evaluation within sampling-based controllers can still impose considerable computational cost, especially when the learned models are highly nonlinear.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative perspective of data-driven dynamics learning is using the Koopman operator theory, which provides a linear representation of nonlinear dynamical systems in a lifted (higher-dimensional) space. By embedding the original state into a space of observable functions, the nonlinear evolution can be approximated by linear dynamics, enabling the use of efficient linear system tools. Extended dynamic mode decomposition (EDMD) formalizes this idea using manually designed lifting functions, but its practical success depends heavily on careful selection of lifting functions. To overcome the limitations of manually chosen lifting functions, deep Koopman operator (DKO) methods employ deep neural networks to learn lifting functions directly from data. These approaches have demonstrated strong empirical performance in approximating nonlinear dynamics and have been integrated with model-based controllers such as MPC or model-based reinforcement learning. Importantly, Koopman-based linear models enable fast state propagation using matrix multiplications, which is particularly attractive for sampling-based control methods like MPPI.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although Koopman operator--based methods have been extensively studied for dynamics identification and prediction, their use as computational accelerators for real-time sampling-based control remains relatively underexplored. Motivated by this gap, we propose a framework that integrates linear DKO dynamics with MPPI control to improve the computational efficiency of sampling-based optimal control for complex nonlinear robotic systems. The central idea is to replace repeated nonlinear dynamics evaluations during MPPI rollouts with efficient linear state propagation in the learned Koopman lifted space, while preserving compatibility with stochastic sampling and general nonconvex cost functions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Koopman-accelerated MPPI formulation: We develop an MPPI controller based on learned linear DKO dynamics, enabling efficient trajectory propagation by exploiting linear structure in the lifted space.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efficient sampling via lifted-state propagation: During trajectory rollouts, lifted states are propagated using learned linear operators rather than repeatedly evaluating deep neural networks, substantially reducing computational cost when the lifting function is highly nonlinear.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comprehensive evaluation and GPU acceleration: The proposed framework is validated on an inverted pendulum, a surface vehicle navigation task, and real-world experiments on a quadruped robot, demonstrating favorable trade-offs between computational efficiency and control performance compared to MPPI with true nonlinear dynamics and MPC with learned models. We further show that the MPPI-DK framework naturally leverages parallel computation, achieving significant speedups when deployed on GPU hardware.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. Section II formulates the problem and introduces the necessary preliminaries. Section III presents the proposed framework. Section IV provides numerical simulation results, and Section V demonstrates the approach on a quadruped robot platform. Finally, Section VI concludes the paper.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations. $\parallel \cdot \parallel$ denotes the Euclidean norm. For a matrix $A \in {\mathbb{R}}^{n \times m}$, $A^{\prime}$ denotes its transpose and $A^{\dagger}$ denotes its Moore--Penrose pseudoinverse.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Problem and Preliminaries", "weight": 1.0} -->

This section first formulates the problem considered in this paper. It then briefly reviews the DKO framework for data-driven dynamics approximation. Finally, the classic MPPI control method is introduced as a candidate solution to the formulated problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Problem Formulation", "weight": 1.0} -->

where $t = {0,1,2,\cdots}$ denotes the time index, ${\mathbf{x}{(t)}} \in \mathcal{X} \subset {\mathbb{R}}^{n}$ is the system state, and ${\mathbf{f}}:{{\mathcal{X} \times \mathcal{V}}\rightarrow\mathcal{X}}$ is a time-invariant nonlinear mapping. The applied control input ${\mathbf{v}{(t)}} \in \mathcal{V} \subset {\mathbb{R}}^{m}$ is subject to disturbances and is given by

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Problem Formulation", "weight": 1.0} -->

We assume that the nonlinear dynamics in can be represented by a finite-dimensional linear Koopman dynamics, given by

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Problem Formulation", "weight": 1.0} -->

The problem of interest is twofold: (i) to estimate the DKO dynamics in from state--input data generated by the original system, and (ii) to utilize the learned model to compute a finite-horizon control sequence

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Problem Formulation", "weight": 1.0} -->

where $c:{\mathcal{X}\rightarrow{\mathbb{R}}}$ and $\phi:{\mathcal{X}\rightarrow{\mathbb{R}}}$ denote the stage and terminal cost functions, respectively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Dynamics Learning using DKO", "weight": 1.0} -->

One approach to approximate is through the DKO framework. Specifically, the system dynamics in can be rewritten in a lifted linear representation as

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Dynamics Learning using DKO", "weight": 1.0} -->

where describes the evolution in the lifted space and assumes the existence of a linear mapping between $\mathbf{x}{({t + 1})}$ and its lifted states ${\mathbf{g}}{({\mathbf{x}{({t + 1})}},{\mathbf{θ}}^{\ast})}$. A detailed estimation error analysis of can be found. To approximate -, consider a dataset of observed state--input--next-state tuples

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Dynamics Learning using DKO", "weight": 1.0} -->

where $\mathbf{x}_{i}^{+}$ denotes the successor state obtained by applying input $\mathbf{v}_{i}$ to the true dynamics at state $\mathbf{x}_{i}$. The data tuples may be unordered and may originate from multiple trajectories. The dataset index set is denoted by $\mathcal{I}_{D} = {\{ 1,2,\cdots,M\}}$. Throughout this paper, $(\mathbf{x}_{t},\mathbf{v}_{t})$ denotes a fixed state--input pair, whereas $({\mathbf{x}{(t)}},{\mathbf{v}{(t)}})$ represents time-varying variables.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Dynamics Learning using DKO", "weight": 1.0} -->

where the loss function is defined as

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Dynamics Learning using DKO", "weight": 1.0} -->

Here, the first term of $\mathbf{L}_{f}$ are introduced to approximate, while the second term enforces the reconstruction. At iteration $k$, let ${\mathbf{θ}}_{k}$ be the estimation of ${\mathbf{θ}}^{\ast}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Dynamics Learning using DKO", "weight": 1.0} -->

are constant matrices determined by ${\mathbf{θ}}_{k}$. The convergence properties of - are analyzed.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C MPPI control", "weight": 1.0} -->

The classic MPPI controller solves the stochastic optimal control problem in by enforcing the true system dynamics in instead of the Koopman dynamics constraint. At each time step $t$, MPPI operates in a receding-horizon manner, performing Monte Carlo rollouts to generate $N$ sampled trajectories, each propagated forward using the system dynamics over a finite prediction horizon $T$. Let $n \in {\{ 1,2,\cdots,N\}}$ denote the index of sampled trajectories, and $\mathcal{T}_{n}$ represents the $n$-th sampled trajectory. The cumulative cost over the finite prediction horizon $T$ (the cost-to-go) of $\mathcal{T}_{n}$ is defined as

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C MPPI control", "weight": 1.0} -->

where $\delta\mathbf{u}_{n}{(s)}$ denotes zero-mean Gaussian noise corresponding to $\mathbf{u}{(s)}$ at the $n$-th trajectory and $\hat{c}$ denotes the instantaneous running cost. The running cost consists of a state-dependent cost $\overset{\sim}{c}$ and a quadratic control penalty, and is given by

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C MPPI control", "weight": 1.0} -->

which $S_{\min}$ is the minimum cost among all rollouts, introduced to improve numerical stability, and $\lambda$ is the inverse temperature parameter governing the selectiveness of the weighting scheme.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C MPPI control", "weight": 1.0} -->

After applying the update rule in at each iteration, the resulting control sequence is optionally smoothed using a Savitzky--Golay filter. In a receding-horizon manner, only the first control input $\mathbf{u}{(t)}$ is applied to the system, while the remaining sequence is used as a warm start for the subsequent optimization step.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Methodology", "weight": 1.0} -->

This section presents an iterative procedure for solving. At any time $t$, the learned DKO dynamics are expressed as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Methodology", "weight": 1.0} -->

where $A^{\ast}$, $B^{\ast}$, $C^{\ast}$, ${\mathbf{θ}}^{\ast}$ are obtained from the DKO updating rule in - using the training dataset $\mathcal{D}$. In this work, $\mathcal{D}$ is collected by applying uniformly sampled control inputs to the true dynamical system. In practice, the dataset may also be gathered using an MPPI controller initialized with a preliminary DKO model, or from demonstrations provided by a human operator in real-world experiments.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Methodology", "weight": 1.0} -->

Based on the learned linear DKO dynamics, we develop an MPPI controller built upon the Koopman model, referred to as MPPI with deep Koopman operator dynamics (MPPI-DK), which is summarized in Algorithm 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

During the trajectory sampling process in the proposed MPPI-DK algorithm, once the state $\mathbf{x}$ is updated, the corresponding lifted state $\mathbf{g}{(\mathbf{x},{\mathbf{θ}}^{\ast})}$ is propagated using the learned linear Koopman dynamics matrices $A^{\ast}$ and $B^{\ast}$, rather than being recomputed through the DNN $\mathbf{g}{(\mathbf{x},{\mathbf{θ}}^{\ast})}$. This substitution reduces the computational burden and improves sampling efficiency, particularly when $\mathbf{g}$ is complex.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Simulations", "weight": 1.0} -->

In this section, we first evaluate the proposed approach on a simulated inverted pendulum balancing task to analyze the impact of key parameters on control performance. We then validate the method on a surface vehicle navigation task, using the classic MPPI with the true system dynamics as a benchmark. This comparison enables a systematic assessment of the computational efficiency gains achieved by the linear DKO dynamics, as well as the performance trade-offs introduced by model approximation errors. All DNNs are trained using the Adam optimizer.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Pendulum Balancing", "weight": 1.0} -->

In this task, the controller is required to swing up the pendulum and stabilize it at the upright equilibrium, given any arbitrary initial state. We focus on examining how the training data and the structure of the DNN lifting function $\mathbf{g}$ in the DKO dynamics, including the number of neurons and the lifted state dimension, affect the performance of the proposed MPPI-DK controller. The dynamics of the inverted pendulum are given by

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Pendulum Balancing", "weight": 1.0} -->

where $g = {{10m}/s^{2}}$, $m = {1kg}$, and $l = {1m}$ represent the gravity acceleration, the mass of the pendulum, and the length of the pendulum, respectively, and ${\Deltat} = {0.05s}$ denotes the discretization step. Here, the system state is defined as ${{\mathbf{x}}{(t)}} = {\lbrack{\theta{(t)}},{\overset{˙}{\theta}{(t)}}\rbrack}^{\prime}$ with the lower bound and upper bound of ${\lbrack{- \pi},{- 8}\rbrack}^{\prime}$ and ${\lbrack\pi,8\rbrack}^{\prime}$, respectively, and $u{(t)}$ denotes the continuous scalar torque input, constrained between $- 2$ and $2$. The state dependent cost function is defined as

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Pendulum Balancing", "weight": 1.0} -->

For each episode, the initial state ${\mathbf{x}}{}$ is uniformly sampled from the interval between ${\lbrack{- \pi},{- 1}\rbrack}^{\prime}$ and ${\lbrack\pi,1\rbrack}^{\prime}$, and the episode is terminated when $t > 200$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Pendulum Balancing", "weight": 1.0} -->

Setup. Training data: To evaluate the effect of training data on the performance of the proposed MPPI-DK controller, we construct two training datasets. The first dataset is generated by applying control inputs uniformly sampled from the interval $\lbrack{- 2},2\rbrack$. The second dataset augments the first by incorporating expert demonstrations obtained from an MPC controller capable of completing the pendulum balancing task, with an expert-to-non-expert data ratio of $1:1$. Lifting functions: We further investigate the control performance of MPPI-DK under different architectures of the lifting function $\mathbf{g}$. The evaluated network structure, including the hidden layer sizes and the lifted state dimension (i.e., the output dimension of the DNN), is summarized in Table I.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Pendulum Balancing", "weight": 1.0} -->

To ensure a fair comparison, we evaluate the state-dependent costs of trajectories initialized from a challenging state $\mathbf{x}_{0} = {\lbrack\pi,0.1\rbrack}^{\prime}$ (downward) and converging to the target state ${\lbrack 0,0\rbrack}^{\prime}$. The results are compared across different training datasets and lifting function architectures, as well as against classic MPPI using as a benchmark. Both methods use identical parameters: $T = 20$, $N = 2000$, $\Sigma = 1.0$, $\lambda = 0.1$. Although this specific initial condition is chosen for evaluation, the proposed method is applicable to arbitrary initial states. The experiment is repeated over $5$ independent trials to mitigate the effects of randomness in DNN training.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Pendulum Balancing", "weight": 1.0} -->

As shown in Figs. 1--2, increasing the number of neurons results in faster convergence of the MPPI-DK controller to the goal state, with control inputs becoming more aggressive and trajectories more closely matching those generated by classic MPPI using the true system dynamics. In contrast, increasing the lifting dimension or augmenting the training set with expert demonstrations does not consistently improve control performance in the pendulum balancing task.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Surface Vehicle Navigation", "weight": 1.0} -->

For this task, the controller is designed to steer the surface vehicle toward a desired goal position. The acceleration dynamics of the simulated surface vehicle are given by

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Surface Vehicle Navigation", "weight": 1.0} -->

Setup. The complete system state is defined as ${\mathbf{x}{(t)}} = {\lbrack{\mathbf{p}{(t)}^{\prime}},{\mathbf{s}{(t)}^{\prime}}\rbrack}^{\prime}$. The goal of this simulation is to drive the surface vehivle from given initial state $\mathbf{x}_{0} = {\lbrack 20,10,{\pi/3},0,0,0\rbrack}^{\prime}$ to goal state $\mathbf{x}_{goal} = {\lbrack 0,0,{\pi/2},0,0,0\rbrack}^{\prime}$, for which we define the stage cost function

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Surface Vehicle Navigation", "weight": 1.0} -->

Because the kinematic evolution is straightforward once the dynamics in are known, our DKO learning objective focuses on identifying the mapping between $\mathbf{s}{({t + 1})}$ and $({\mathbf{s}{(t)}},{\mathbf{u}{(t)}})$. Accordingly, the function $\mathbf{g}$ is constructed following the architecture in Table I, using $256$ neurons per hidden layer and a lifting dimension of $8$. The tuples $(\mathbf{s}_{t},\mathbf{u}_{t},\mathbf{s}_{t + 1})$ are collected by applying control inputs uniformly sampled from the interval between ${\lbrack{- 1},{- 1}\rbrack}^{\prime}$ and ${\lbrack 1,1\rbrack}^{\prime}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Surface Vehicle Navigation", "weight": 1.0} -->

To evaluate computational efficiency, we compare MPPI-DK with classic MPPI using the true system dynamics. We further compare MPPI-DK with an MPC controller based on the same learned DKO dynamics to assess control performance under identical model approximation errors. MPPI-DK and classic MPPI share the same cost function and parameters: $T = 20$, $N = 600$, $\Sigma = {{diag}{(0.8,0.8)}}$, and $\lambda = 20$. For MPC, the prediction horizon is set to $T = 30$. Furthermore, we implement the proposed method on a GPU to enable parallel trajectory sampling and further improve computational efficiency. To mitigate the effects of randomness in DNN training, all experiments are repeated over $4$ independent trials.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Surface Vehicle Navigation", "weight": 1.0} -->

As shown in Fig. 3, the proposed approach achieves tracking performance close to classic MPPI with access to the true system dynamics. The computational performance is summarized in Table II. When executed on a CPU, MPPI-DK exhibits lower per-step computation time than classic MPPI, while remaining more computationally intensive than MPC based on the same learned DKO dynamics. In contrast, with GPU-enabled parallel sampling, MPPI-DK achieves significantly higher computational efficiency than MPC implemented using the identical DKO model and the classic MPPI.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

We evaluate the proposed approach on a reference-tracking task using the quadruped robot Unitree Go1 platform. The quadruped robot is modeled with state

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

where $x$ and $y$ denote the robot global position, $\theta$ is the yaw angle, $v_{x}$, $v_{y}$ are the body-frame linear velocities obtained from the world-frame velocities by

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

The centroidal momentum state is defined as $\mathbf{h} = {\lbrack l_{x},l_{y},w_{m}\rbrack}^{\prime} \in {\mathbb{R}}^{3}$, where $l_{x} = {m\overset{˙}{x}}$, $l_{y} = {m\overset{˙}{y}}$ denote the linear momenta about the center of mass (CoM), and $w_{m} = {I_{zz}\overset{˙}{\theta}}$ denotes the angular centroidal momentum about the CoM. Here, $m = {12kg}$ is the robot mass, and $I_{zz} = {{0.9kg}/m^{2}}$ is the yaw moment of inertia about the CoM. The control input

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

denotes the commanded forward and lateral accelerations in the body frame, and the desired yaw angular acceleration, respectively. The control input is constrained between ${\lbrack{- 1},{- 1},{- 1}\rbrack}^{\prime}$ and ${\lbrack 1,1,1\rbrack}^{\prime}$. The centroidal momentum dynamics are given by

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

Task-Oriented State Definition. The control objective is to drive the quadruped to the desired goal pose ${\lbrack x_{\text{goal}},y_{\text{goal}},\theta_{\text{goal}}\rbrack}^{\prime} = {\lbrack 1.5,0,0\rbrack}^{\prime}$. Since the task primarily depends on the base motion, we adopt an $8$-dimensional task-oriented state defined as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

Setup. To learn the DKO dynamics for the mapping between $({\mathbf{s}{(t)}},{\mathbf{u}{(t)}})$ and $\mathbf{s}{({t + 1})}$, we generate training tuples $(\mathbf{s}_{t},\mathbf{u}_{t},\mathbf{s}_{t}^{+})$ by applying uniformly sampled control inputs to the quadruped system. The DKO lifting network is constructed following the architecture specified in Table I, with $256$ neurons per layer and a lifting dimension of $10$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

To evaluate the control performance of the proposed MPPI-DK controller, we compare it against classic MPPI using the true robot dynamics as a benchmark. Both controllers are implemented with parallel trajectory sampling on GPU using identical parameters: $T = 40$, $N = 900$, $\Sigma = {diag{(0.18,0.18,0.18)}}$, and $\lambda = {0.5{std}{(S)}}$, where ${std}{(S)}$ denotes the standard deviation of the cumulative trajectory costs across the sampled rollouts at each control step. This adaptive temperature improves numerical stability and balances exploration and exploitation during trajectory optimization. The per-step computation time, average tracking error along the trajectory, final state tracking error, and success rate are reported in Table III over $10$ different initial states.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experiments Results", "weight": 1.0} -->

As shown in Table III, both MPPI-DK and classic MPPI complete the task for all $10$ different initial states. MPPI-DK achieves lower per-step computation time and reaches a final state slightly closer to the goal, while producing smoother control inputs. Furthermore, a representative trajectory generated by the proposed method is illustrated in Fig. 4.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We introduced a deep Koopman dynamics-based MPPI framework, termed MPPI-DK, that improves the trajectory sampling efficiency of classic MPPI for robotic systems with complex nonlinear dynamics. The proposed approach replaces nonlinear system dynamics with a learned linear Koopman dynamics for the classic MPPI, enabling faster rollout while preserving control performance. The effectiveness of MPPI-DK was first analyzed on a pendulum balancing task to examine the impact of key DKO parameters. It was further evaluated on a surface vehicle navigation task, where it achieved performance comparable to MPPI with access to the true dynamics while requiring lower computational cost.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

The scalability and practical applicability of the approach were demonstrated on hardware through reference-tracking experiments on a quadruped robot. In these experiments, MPPI-DK guided the robot to the desired position with accuracy close to MPPI using the true system dynamics. These results indicate that learning structured linear DKO dynamics for sampling-based control offers a promising direction for improving computational efficiency in robotic systems with complex nonlinear dynamics.
