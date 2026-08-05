<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Belief Control Barrier Functions for Risk-aware Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Ensuring safety in real-world robotic systems is often challenging due to unmodeled disturbances and noisy sensor measurements. To account for such stochastic uncertainties, many robotic systems leverage probabilistic state estimators such as Kalman filters to obtain a robot's belief, i.e. a probability distribution over possible states. We propose belief control barrier functions (BCBFs) to enable risk-aware control synthesis, leveraging all information provided by state estimators. This allows robots to stay in predefined safety regions with desired confidence under these stochastic uncertainties. BCBFs are general and can be applied to a variety of robotic systems that use extended Kalman filters as state estimator. We demonstrate BCBFs on a quadrotor that is exposed to external disturbances and varying sensing conditions. Our results show improved safety compared to traditional state-based approaches while allowing control frequencies of up to 1kHz.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robotic systems are exposed to various sources of uncertainty, such as noise in the robot's sensor readings or external disturbances, e.g., an unknown wind force acting on a quadrotor, as shown in Fig. 1. Considering uncertainty is thus crucial for safe operation of such robots. Safe and robust control synthesis under external disturbances has been thoroughly explored for a variety of robots with full state information. Observer-based Control Barrier Functions (CBFs) consider measurement uncertainties through bounded estimation errors. However, these methods do not consider the stochastic uncertainties that are commonly captured in probabilistic state estimation techniques deployed in practice, such as Kalman Filters (KFs). Such stochastic uncertainties have been considered for instance in the state-of-the-art chance-constrained nonlinear Model Predictive Control (MPC), which bounds the probability of undersired events. However, to make the method computationally tractable, theoretical safety guarantees are sacrificed. In this paper, we consider both uncertainties in the robot's motion and its observations. We aim to offer both safety guarantees under uncertainty as well as a practical solution.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, state estimation pipelines are used to obtain a robot's belief that accounts for the uncertainty arising from stochastic motion and observations. Up to now, the Kalman filter (KF) is still one of the gold standards in robotic state estimation because of its simplicity and robustness. The extended KF (EKF), as its extension to nonlinear systems, is widely used for state estimation of robots such as quadrotors, legged robots or autonomous underwater vehicles. One of the key properties of KFs is that they not only provide an estimate about the robot's state but also quantify the uncertainty of that estimate through the covariance matrix. For instance, Fig. 1 illustrates a drone's localization uncertainty as a Gaussian level set (purple ellipsoid), i.e. a set containing the state with certain probability. In this work, we leverage both the mean state estimate and the covariance matrix.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to Gaussian state uncertainty, hard safety constraints on the system states are generally infeasible. This gives rise to a risk-aware perspective on safety: We consider specifications that bound the probability of violating safety constraints on the state. Fig. 1 shows a scenario in which a safety specification is encoded as "*the probability of leaving the safe region (red cuboid) should be less than 1%*".

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, designing controllers that ensure satisfaction of such risk-aware safety specifications is challenging as it requires us to reason about the robot's belief instead of its state. Belief spaces in these applications suffer from the curse of dimensionality and are hybrid in nature as robots evolve in continuous time while sensors only provide measurements at discrete timesteps. To enable risk-aware control, we introduce Belief CBFs (BCBFs) that 1) serve as safety filters in the presence of real-world stochastic uncertainties, 2) provide theoretical safety guarantees under the hybrid nature of belief spaces, and 3) overcome the curse of dimensionality and allow real-time control for general robotic systems that employ EKFs as a state estimator. We evaluate our approach in experiments with a quadrotor that is exposed to external wind disturbances and varying sensing conditions, see Fig. 1.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

We review two relevant safety-critical control approaches for robotic systems under uncertainties -- CBFs and MPC.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Related work on observer-based CBFs assume a bounded uncertainty around the current estimate that is used to account for potential measurement errors,. However, these methods do not consider stochastic uncertainties that are commonly used in probabilistic state estimators. Measurement-robust CBFs use deterministic measurements and assume a given mapping from measurements to state estimates. In contrast, our BCBFs explicitly provide this mapping to handle stochastic measurements.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Control of stochastic systems using Kalman Filters as state estimator has been addressed in various settings. Chance-constrained nonlinear MPC (CCNMPC) enforce obstacle avoidance with a desired confidence level in which the uncertainty in the state estimate originates from an unscented KF. Unfortunately, solving NMPC problems in belief spaces is computationally expensive due to the curse of dimensionality. The problem was made tractable by neglecting the dynamics of the covariance through linearization around the last trajectory solution. However, this linearization is only valid when the subsequent trajectory does not significantly change. In contrast, the belief space planning approach SACBP operates in continuous-time through sequential action control (SAC). The authors model the belief dynamics as a hybrid dynamical system which we build upon. However, SACBP cannot ensure safety as constraints can only be included in the objective function.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

In, invariance properties of deterministic CBFs are extended to systems that are described by stochastic differential equations (SDEs). The proposed stochastic CBFs handle uncertainty in the system's dynamics and also in the measurements. They guarantee safety under stochastic uncertainties by bounding the estimation errors in an EKF. This CBF is used for systems under sensor faults and attacks in as well as risk-bounded control in highway scenarios. Probabilistic safety barrier certificates (PrSBC) have been proposed in for multi-robot collision avoidance under uncertainty. However, the guarantees only hold for bounded uniform additive noise on the system dynamics and the observation model. Furthermore, the guarantees in only hold for continuous-time observations, which is generally not consistent with real-world robotic systems, e.g., when global positioning data is not available.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Gaussian Belief States", "weight": 1.0} -->

Gaussian filters are a family of state estimators that describe a Bayesian approach in which the belief is constrained to follow a multivariate Gaussian (MVG). Its probability density function (pdf) is described by where ${\mathbf{μ}} \in {\mathbb{R}}^{n}$ is the mean vector and $\mathbf{\Sigma} = \mathbf{\Sigma}^{T} \in {\mathbb{R}}^{n \times n}$ is the positive semidefinite covariance matrix. The pdf in is uniquely described by the belief state ${\mathbf{b}} = \left\lbrack {\mathbf{μ}},{{vec}(\mathbf{\Sigma})} \right\rbrack^{T}$ where, due to symmetry, only the upper triangular matrix is stored which is encoded in the ${vec}{(\cdot)}$ operator.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Gaussian Belief States", "weight": 1.0} -->

Thus, the dimensionality of the belief state $n_{b}$ increases quadratically with the state dimension $n$, i.e. $n_{b} = {\left({n^{2} + {3n}} \right)/2}$. If not mentioned explicitly otherwise, we refer to the belief state $\mathbf{b}$ as the belief.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Chance Constraints and Risk Measures", "weight": 1.0} -->

Chance constraints handle safety constraints under uncertainty by bounding the probability of undesired events. We use safety specifications in the form of half-spaces ${{\mathbf{α}}^{T}{\mathbf{x}}} \geq \beta$. Consider a Gaussian distributed random variable $\mathbf{x}$ with belief state $\mathbf{b}$. We calculate the probability of satisfying a half-space constraint as where ${erf}{(\cdot)}$ is the standard error function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Chance Constraints and Risk Measures", "weight": 1.0} -->

To quantify the outcome of violating a chance constraint ${\Pr\left\lbrack {{{\mathbf{α}}^{T}{\mathbf{x}}} \geq \beta} \right\rbrack} \geq {1 - \delta}$, we use the Value-at-Risk ($VaR$).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We consider the robot's stochastic motion and observations in the form where $\mathcal{Z} \subseteq {\mathbb{R}}^{\ell}$ is the observation space and ${\mathbf{w}},{\mathbf{v}}$ are the motion and observation noise, respectively. We model the robot's motion as a continuous-time differential equation. The observations are always provided in discrete time due to the sensor's sampling time. Especially for exteroceptive sensors like GPS, measurements occur much less frequently than the robot's control rate, encouraging us to consider discrete-time formulations. A reference controller, e.g. a controller that drives the robot to a goal state, is given as ${\mathbf{u}}_{\text{ref}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Ideally, to solve Problem 1, we would use the Bayes filter to capture the exact time evolution of the belief given an initial belief $p\left( {{\mathbf{x}}{(t_{0})}} \right)$, controls $\mathbf{u}$ and observations $\mathbf{z}$. However, exact belief calculations only exist in specialized cases which is why approximations need to be considered. Thus, we use an EKF as a tractable implementation of the Bayes filter in which beliefs are Gaussian. While the Gaussian belief of an EKF is exact for linear systems, it is only an approximation of the true belief in the nonlinear case. This assumption, however, is common in many practical scenarios, especially if the true probability distribution is unimodal. In future work, we aim to consider the mismatch between the modeled belief and the true belief.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem 1", "weight": 1.0} -->

To approach Problem 1, we reason about Gaussian belief states $\mathbf{b}$ instead of states $\mathbf{x}$ so that we can solve a relaxed problem under stochastic uncertainties. We propagate the belief through the nonlinear model in Eq. - by exploiting the fundamental EKF step that systems are linearized around the current mean.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

A drone with uncertain position x and its pdf p (x) is moving in one dimension.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

A safety specification is defined as a bounded probability of collision with the wall. The resulting safe set over belief states is shown in blue and the current belief of the robot is depicted in red.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Given the model - and a risk-aware safe set $\mathcal{C}_{b}$ defined over beliefs, find a control input $\mathbf{u}$ that renders $\mathcal{C}_{b}$ forward invariant.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem 2", "weight": 1.0} -->

By solving Problem 2, we ensure that the belief satisfies a $VaR$ formulation which is qualitatively equivalent (see Eq. ) to satisfying the chance constraint in Problem 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example", "weight": 1.0} -->

Consider a drone operating in one dimension with position $x \sim {\mathcal{N}\left(\mu,\sigma^{2} \right)}$, as shown in Fig. 2 and the Gaussian belief state $\mathbf{b} = \left\lbrack \mu,\sigma^{2} \right\rbrack^{T} \in {\mathbb{R}}^{2}$. A safety specification over states is to stay within the collision-free space with 90% probability, given by $\delta = 0.1$ and $\mathcal{C}_{x} = \left\{ {x \in {\mathbb{R}}}\mid{x \leq 2} \right\}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example", "weight": 1.0} -->

The corresponding safe set $\mathcal{C}_{b}$ in belief space is defined through which is illustrated in blue in Fig. 2. In the depicted point in time, the belief state, shown as red circle, is right at the boundary of the safe set $\partial\mathcal{C}_{b}$ as the probability of colliding with the wall is exactly 10 %. Solving Problem 2 keeps the belief state (red circle) in $\mathcal{C}_{b}$ which in turn satisfies the original safety specification over states that $90\%$ of the drone's probability mass should be left of the wall.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Risk-aware Control", "weight": 1.0} -->

Our solution to Problem 2 is divided into two main steps. First, we derive a stochastic hybrid system that accounts for uncertainties in the robot's motion and observations. Given this hybrid system describing the evolution of the robot's belief, we propose BCBFs to ensure forward invariance of our safe set defined over beliefs. BCBFs serve as a computationally efficient risk-aware safety filter that can be applied to various robotic systems under stochastic uncertainties.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Hybrid Belief Dynamics", "weight": 1.0} -->

In the belief dynamics, it is important to distinguish between two evolutions: 1) The belief advances in continuous time as the state dynamics also evolve in continuous time. 2) At discrete timesteps $t_{k}$ when a new sensor observation is available, the belief changes instantaneously since the state distribution is conditioned on the measurement. This naturally leads to a hybrid dynamical system which is derived from a continuous-discrete EKF.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A1 Continuous-time Belief Dynamics", "weight": 1.0} -->

The continuous-time evolution of the belief directly follows from the derivation of the continuous EKF and is given by a set of ordinary differential equations (ODEs) where $\mathbf{A}$ is the Jacobian of the noise-free motion model in Eq. evaluated at the current mean $\mathbf{μ}$. For the design of BCBFs, the dynamics are required to be in control-affine form which has been proven to be true.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A1 Continuous-time Belief Dynamics", "weight": 1.0} -->

Consequently, if the control signal $\mathbf{u}$ is known, the belief at any point in time is obtained by forward integrating the belief dynamics in Eq.. However, when a new sensor reading is available, the belief changes instantaneously which is covered in the discrete-time Kalman update.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A2 Discrete-time Kalman Update", "weight": 1.0} -->

The conditioning leads to a discrete belief transition which is governed by the discrete-time Kalman update denote the Kalman gain and the Jacobian of the observation model, respectively. The measurement obtained at a discrete timestep is not known in advance which makes it generally difficult to do planning or control in belief space. However, the unknown measurement can be treated as a random variable making the measurement update stochastic.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Belief Control Barrier Functions", "weight": 1.0} -->

The dynamical system $\mathcal{S}$ of the belief allows us to introduce BCBFs for safe control under stochastic uncertainties. BCBFs are defined similarly as CBFs, but they are defined over beliefs instead of states.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Our BCBFs are zeroing CBFs that not only render $\mathcal{C}_{b}$ forward invariant but also asymptotically stable as the cont.-time belief dynamics are deterministic. Thus, if an initial belief is outside the safe set, it will be driven back to $\mathcal{C}_{b}$ over time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the following theorem, we derive an upper bound on the probability of leaving $\mathcal{C}_{b}$ under a discrete transition.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example", "weight": 1.0} -->

(Cont.) Consider the one-dimensional drone example introduced before. The drone is equipped with a sensor that provides noisy state observations $z_{k} = {{x{(t_{k})}} + v}$ where $v \sim {\mathcal{N}\left({{0,r} = 0.1} \right)}$. The prior variance is $\sigma^{-} = 0.3$ and a confidence level is set to ${1 - \delta} = 0.99$, then meaning that the probability of leaving $\mathcal{C}_{b}$ is at most 9 %. Note that this is a tight bound if the prior belief state is right at the boundary of the safe set and strictly smaller otherwise.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example", "weight": 1.0} -->

To ensure that the belief state does not leave $\mathcal{C}_{b}$, we modify $\mathcal{C}_{b}$ such that the probability of leaving $\mathcal{C}_{b}$ is bounded with a desired confidence. We define an augmented safe set ${\overset{\sim}{\mathcal{C}}}_{b} \subseteq \mathcal{C}_{b}$ with ${{\overset{\sim}{h}}_{b}({\mathbf{b}})} = {{h_{b}({\mathbf{b}})} - \gamma}$ for some $\gamma \geq 0$. This safe set is essentially a shrunk version of the original safe set $\mathcal{C}_{b}$. In the following theorem, we choose $\gamma$ such that the belief stays within $\mathcal{C}_{b}$ with desired probability.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Risk-aware control synthesis", "weight": 1.0} -->

Consider for example a quadrotor operating in 3D: It has 6 degrees of freedom (3D pose and orientation) and 4 control inputs (thrusters) which leads to a 12 dimensional state. Consequently, the belief state is of dimension ${\mathbf{b}} \in {\mathbb{R}}^{90}$ which is known as the curse of dimenionality and complicates the use of common optimization-based controllers such as MPC. We overcome the dimenionality problem of belief spaces by only optimizing over control inputs $\mathbf{u}$ which enables real-time applicability. The resulting control inputs satisfy the entire belief dynamics.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our BCBFs in challenging scenarios in which uncertainties cannot be neglected^11^1Videos of our hardware experiments can be found in the supplementary material. Specifically, we show improved adherence to safety specifications through risk-awareness and computational efficiency over traditional CBFs and CCNMPC in simulations in Sec. V-A, safety under changing sensing conditions, such as sensor rates and measurement variances, in Sec. V-C, robustness to external disturbances as well as the generality to different sensor systems in Sec. V-D.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Setup", "weight": 1.0} -->

\right).$ | | | Figure 4: Comparison of different control strategies for a two-dimensional avoidance scenario. The initial state follows a Gaussian distribution x0 ∼ 𝒩 ([0, 1.5, 0, 0], diag ([0.32, 0.22, 0.12, 0.12])) and the goal is. Simulated trajectories are shown in blue and the obstacle is depicted in red.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Setup", "weight": 1.0} -->

The control input is given as ${\mathbf{u}} = {\lbrack a,\omega\rbrack}^{T}$. We obtain the belief dynamics in Eq. by applying the method described in Sec. IV-A where ${\mathbf{b}} \in {\mathbb{R}}^{14}$. The objective is to steer the robot towards a goal at $\lbrack 8,0\rbrack$ while avoiding collisions with a circular obstacle $\mathcal{O} = \left\{ {{\mathbf{p}} \in {\mathbb{R}}^{2}}\mid{{\parallel{{\mathbf{p}} - {\mathbf{c}}}\parallel}_{2} < r} \right\}$ where ${\mathbf{c}} = {\lbrack 5,0\rbrack}^{T}$ and $r = 1$ as shown in Fig. 4. The safety specification for collision avoidance is given as with $\delta = 0.01$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Setup", "weight": 1.0} -->

Due to the non-linearity of the obstacle description, we use the common approach to linearize Eq. around the mean state which is a strict overapproximation of the true collision condition as shown. The resulting risk-aware safe set is given by where ${VaR}_{\delta}{(\cdot)}$ with ${\mathbf{α}} = {\left({{\mathbf{μ}} - {\mathbf{c}}} \right)/{\parallel{{\mathbf{μ}} - {\mathbf{c}}}\parallel}_{2}}$ serves as a BCBF candidate. Due to a relative degree $r_{b} = 2$ in our BCBF candidate, we use second order formulations as in Eq..

<!-- chunk {"id": "body-0039", "role": "body", "section": "Setup", "weight": 1.0} -->

We solve the resulting SDE using the DifferentialEquations.jl package in the Julia programming language. The reference control ${\mathbf{u}}_{\text{ref}}$ is given by a Linear-quadratic Regulator (LQR) that uses the mean estimate $\mathbf{μ}$ to steer the system towards the goal without any knowledge of the obstacle. The parameters chosen for the LQR are ${\mathbf{Q}}_{L} = {\text{diag}{\lbrack 10,5,5,5\rbrack}}$ and ${\mathbf{R}}_{L} = {\text{diag}{\lbrack 5,10\rbrack}}$. We compare two versions of BCBFs, namely one with only the natural bound ($\varepsilon = 0.5$) and one bounding the probability of leaving $\mathcal{C}_{b}$ by $\varepsilon = 0.01$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare our BCBFs to two different baselines: 1.) Stochastic CBFs with incomplete state information which require cont.-time observations as well as a bounded estimation error. To enable continuous estimation, we use maximum likelihood observations between actual measurements which is not true in practice. The bounded estimation error was obtained by running a monte carlo study and take the maximum error. 2.) chance-constrained NMPC (CCNMPC) that formulates an MPC problem which includes Eq. as a constraint. Since MPC operates in discrete-time while we simulate a continuous system, we use a zero order hold to apply the control input. We run the MPC at 30 Hz and use a planning horizon of $N = 40$. The cost function is the same quadratic cost as in the reference LQR controller. 3.) In hardware experiments, we compare to a traditional state CBF that only considers the mean dynamics.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Effect of augmented safe set", "weight": 1.0} -->

We analyze the effect of the augmented safe set defined in Theorem 3. If no additional safety margin is used ($\varepsilon = 0.5$), the belief leaves $\mathcal{C}_{b}$ in $0.42\%$ of all simulated trajectories. When bounding the probability of leaving the safe set by ${\Pr{\lbrack{{h\left( {\mathbf{b}}^{+} \right)} < 0}\rbrack}} \leq 0.01$, the belief remains in $\mathcal{C}_{b}$ for all trajectories while keeping larger distances to the obstacle.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Control efficiency", "weight": 1.0} -->

Lastly, we evaluate the efficiency in terms of the average norm of the control input and the time $t_{g}$ to reach the goal. In this case CCNMPC is superior to all other approaches since it optimizes controls over a planning horizon whereas CBF approaches are purely reactive. This motivates to combine state-based MPC with BCBFs to achieve both, control efficiency and rigorous safety properties. In future work, we aim to explore this.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B Setup of hardware experiment", "weight": 1.0} -->

We use the Bitcraze Crazyflie 2.1 quadrotor inside an OptiTrack motion capture (mocap) system, as shown in Fig. 1. The state of the drone is given as its 3D position $\mathbf{p}$ and velocity $\overset{˙}{\mathbf{p}}$. Its motion and observations are modeled as where ${\mathbf{u}} \in {\mathbb{R}}^{3}$ are the drone's desired accelerations and ${\mathbf{w}} \sim {\mathcal{N}(\mathbf{0},{\mathbf{Q}})}$ with a variance of $0.05^{2}$ along the diagonal of $\mathbf{Q}$. In our setting, we can only observe the drone's position $\mathbf{p}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Setup of hardware experiment", "weight": 1.0} -->

We add Gaussian noise ${\mathbf{v}} \sim {\mathcal{N}(\mathbf{0},{\mathbf{R}})}$ to the mocap data and reduce the sampling rate of the measurements. These parameters $\mathbf{R}$ and $f_{s}$ are varied throughout the experiments. We use the uncorrupted mocap data as ground truth to evaluate the performance of BCBFs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Setup of hardware experiment", "weight": 1.0} -->

We use the EKF in Sec. IV-A to obtain the belief dynamics with ${\mathbf{b}} \in {\mathbb{R}}^{27}$, where the ODE is discretized using Euler's scheme. We convert the desired acceleration $\mathbf{u}$ synthesized by our BCBFs into a setpoint consisting of desired roll and pitch angles as well as thrust for the real quadrotor using. Setpoints are sent to the Crazyflie at 100 Hz and tracked by the onboard PID controller which serves as ${\mathbf{u}}_{\text{ref}}$. We compare BCBFs only to traditional CBFs as we were not able to run CCNMPCs in real-time with our setup.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Experiment I - Changing sensing conditions", "weight": 1.0} -->

In our first experiment, we showcase the robustness of BCBFs to changing sensing conditions. For that purpose, we navigate the drone along a U-shaped corridor as shown in Fig. 5. The corridor is the union of three polytopes. In each of the three polytopes, we change the measurement noise $\mathbf{R}$ and sampling rates $f_{s}$ according to Fig. 5. In the third polytope, we additionally place a circular obstacle to increase the difficulty of the scenario. The safety specification is given as an intersection of risk-aware half-spaces with a collision probability of $\delta = 0.05$. The half-spaces are given by the polytope representation of the corridor.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-D Experiment II - External disturbances", "weight": 1.0} -->

In this experiment illustrated in Figure 1, we additionally study the effect of disturbances on the nominal dynamics. To that end, we define a safe set as a cuboid that we want the drone to stay in with 95% probability. The drone is exposed to both, sensing uncertainties as well as an external wind disturbance from a fan. Instead of position measurements, we measure the drone's velocity through an added optical flow sensor. These velocity measurements are given by Since we only measure the drone's velocity and neglect the global position measurements from mocap, there is an inevitable drift in the position estimate obtained from integrating the velocity. A human operator is generating reference acceleration commands ${\mathbf{u}}_{\text{ref}}$ using a gamepad and actively tries to steer the drone outside the safe set.

<!-- chunk {"id": "body-0048", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

Our work enables risk-aware control synthesis for stochastic dynamical systems with incomplete state information by combining continuous-discrete EKFs with CBFs defined over Gaussian belief states. Instead of defining safety specifications as hard constraints on the state, we consider a risk-aware approach in which we bound the probability of violation. BCBFs are applicable to any robotic system in which the state estimate is provided by an EKF. Our simulation and hardware experiments show that BCBFs ensure that robots adhere to safety specifications in the presence of both, real-world motion and observation uncertainties.

<!-- chunk {"id": "body-0049", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

In future, we aim to explore the combination of motion planners such as state-based MPC that only consider the mean estimate with our proposed BCBFs. In that way, we can ensure safety while enhancing control efficiency. We are also interested in extending our results to arbitrary belief distributions that can be represented using particles filters.
