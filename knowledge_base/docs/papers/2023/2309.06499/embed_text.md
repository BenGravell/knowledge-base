<!-- arxiv-full-text:v1 {"arxiv_id": "2309.06499", "source": "ar5iv"} -->

## Introduction

Autonomous robotic systems are exposed to various sources of uncertainty, such as noise in the robot's sensor readings or external disturbances, e.g., an unknown wind force acting on a quadrotor, as shown in Fig. 1. Considering uncertainty is thus crucial for safe operation of such robots. Safe and robust control synthesis under external disturbances has been thoroughly explored for a variety of robots with full state information. Observer-based Control Barrier Functions (CBFs) consider measurement uncertainties through bounded estimation errors. However, these methods do not consider the stochastic uncertainties that are commonly captured in probabilistic state estimation techniques deployed in practice, such as Kalman Filters (KFs). Such stochastic uncertainties have been considered for instance in the state-of-the-art chance-constrained nonlinear Model Predictive Control (MPC), which bounds the probability of undersired events. However, to make the method computationally tractable, theoretical safety guarantees are sacrificed. In this paper, we consider both uncertainties in the robot's motion and its observations. We aim to offer both safety guarantees under uncertainty as well as a practical solution.

In practice, state estimation pipelines are used to obtain a robot's belief that accounts for the uncertainty arising from stochastic motion and observations. Up to now, the Kalman filter (KF) is still one of the gold standards in robotic state estimation because of its simplicity and robustness. The extended KF (EKF), as its extension to nonlinear systems, is widely used for state estimation of robots such as quadrotors, legged robots or autonomous underwater vehicles. One of the key properties of KFs is that they not only provide an estimate about the robot's state but also quantify the uncertainty of that estimate through the covariance matrix. For instance, Fig. 1 illustrates a drone's localization uncertainty as a Gaussian level set (purple ellipsoid), i.e. a set containing the state with certain probability. In this work, we leverage both the mean state estimate and the covariance matrix.

Due to Gaussian state uncertainty, hard safety constraints on the system states are generally infeasible. This gives rise to a risk-aware perspective on safety: We consider specifications that bound the probability of violating safety constraints on the state. Fig. 1 shows a scenario in which a safety specification is encoded as "*the probability of leaving the safe region (red cuboid) should be less than 1%*".

Figure 1: An illustration of our experiments with a CrazyFlie 2.1 quadrotor operating in an uncertain environment. The drone is exposed to common real-world uncertainties such as noisy position measurements and unknown wind disturbances. The uncertainty in the state estimate is shown as a purple ellipsoid and the cuboid-shaped safe set is colored in red.

However, designing controllers that ensure satisfaction of such risk-aware safety specifications is challenging as it requires us to reason about the robot's belief instead of its state. Belief spaces in these applications suffer from the curse of dimensionality and are hybrid in nature as robots evolve in continuous time while sensors only provide measurements at discrete timesteps. To enable risk-aware control, we introduce Belief CBFs (BCBFs) that 1) serve as safety filters in the presence of real-world stochastic uncertainties, 2) provide theoretical safety guarantees under the hybrid nature of belief spaces, and 3) overcome the curse of dimensionality and allow real-time control for general robotic systems that employ EKFs as a state estimator. We evaluate our approach in experiments with a quadrotor that is exposed to external wind disturbances and varying sensing conditions, see Fig. 1.

### I-A Related Work

We review two relevant safety-critical control approaches for robotic systems under uncertainties -- CBFs and MPC.

Related work on observer-based CBFs assume a bounded uncertainty around the current estimate that is used to account for potential measurement errors,. However, these methods do not consider stochastic uncertainties that are commonly used in probabilistic state estimators. Measurement-robust CBFs use deterministic measurements and assume a given mapping from measurements to state estimates. In contrast, our BCBFs explicitly provide this mapping to handle stochastic measurements.

Control of stochastic systems using Kalman Filters as state estimator has been addressed in various settings. Chance-constrained nonlinear MPC (CCNMPC) enforce obstacle avoidance with a desired confidence level in which the uncertainty in the state estimate originates from an unscented KF. Unfortunately, solving NMPC problems in belief spaces is computationally expensive due to the curse of dimensionality. The problem was made tractable by neglecting the dynamics of the covariance through linearization around the last trajectory solution. However, this linearization is only valid when the subsequent trajectory does not significantly change. In contrast, the belief space planning approach SACBP operates in continuous-time through sequential action control (SAC). The authors model the belief dynamics as a hybrid dynamical system which we build upon. However, SACBP cannot ensure safety as constraints can only be included in the objective function.

In, invariance properties of deterministic CBFs are extended to systems that are described by stochastic differential equations (SDEs). The proposed stochastic CBFs handle uncertainty in the system's dynamics and also in the measurements. They guarantee safety under stochastic uncertainties by bounding the estimation errors in an EKF. This CBF is used for systems under sensor faults and attacks in as well as risk-bounded control in highway scenarios . Probabilistic safety barrier certificates (PrSBC) have been proposed in for multi-robot collision avoidance under uncertainty. However, the guarantees only hold for bounded uniform additive noise on the system dynamics and the observation model. Furthermore, the guarantees in only hold for continuous-time observations, which is generally not consistent with real-world robotic systems, e.g., when global positioning data is not available.

## Preliminaries

### II-A Control Barrier Functions

Consider a dynamical system in control affine form with state ${\mathbf{x}} \in \mathcal{X} \subseteq {\mathbb{R}}^{n}$ and control input ${\mathbf{u}} \in \mathcal{U} \subseteq {\mathbb{R}}^{m}$. A safe set $\mathcal{C}$ is constructed as the superlevel set of a continuously differentiable function $h:{\mathcal{X}\rightarrow{\mathbb{R}}}$ such that | | $\mathcal{C}$ | ${= \left\{ {{\mathbf{x}} \in \mathcal{X}}\mid{{h({\mathbf{x}})} \geq 0} \right\}},$ | | \(2\) | | | $\partial\mathcal{C}$ | ${= \left\{ {{\mathbf{x}} \in \mathcal{X}}\mid{{h({\mathbf{x}})} = 0} \right\}}.$ | | |

### Definition 1

A safe set $\mathcal{C}$ is forward invariant with respect to the system if for every initial condition ${\mathbf{x}{(t_{0})}} \in \mathcal{C}$ it holds that ${{\mathbf{x}{(t)}} \in \mathcal{C}},{{\forall t} \geq t_{0}}$.

A prominent approach to render a safe set forward invariant is to use CBFs.

### Definition 2

Given a set $\mathcal{C}$, defined by Eq., $h$ serves as a zeroing CBF for the system if $\forall\mathbf{x}$ satisfying ${{h(\mathbf{x})} \geq 0},{{\exists\mathbf{u}} \in \mathcal{U}}$ such that In case a valid CBF exists, it follows that a controller satisfying Eq. renders $\mathcal{C}$ forward invariant. However, this only holds for systems with relative degree $r_{b} = 1$ because ${{({{\partial h}/{\partial{\mathbf{x}}}})}{\mathbf{g}}} = \mathbf{0}$ otherwise, thus $\mathbf{u}$ would not appear in Eq.. For systems with $r_{b} > 1$, exponential CBFs (ECBFs) can be used to ensure forward invariance of $\mathcal{C}$. We leverage second order CBFs as a special case of ECBFs.

### Definition 3

Given a set $\mathcal{C}$ in Eq. and a system with relative degree $r_{b} = 2$, $h$ is called an exponential CBF, if there exists a gain vector ${\mathbf{ζ}} \in {\mathbb{R}}^{r_{b}}$ and $\mathbf{u} \in \mathcal{U}$ such that The gain vector can be obtained using classical tools from control theory such as, e.g., pole placement. A proof of forward invariance under ECBFs can be found.

### II-B Gaussian Belief States

Gaussian filters are a family of state estimators that describe a Bayesian approach in which the belief is constrained to follow a multivariate Gaussian (MVG). Its probability density function (pdf) is described by where ${\mathbf{μ}} \in {\mathbb{R}}^{n}$ is the mean vector and $\mathbf{\Sigma} = \mathbf{\Sigma}^{T} \in {\mathbb{R}}^{n \times n}$ is the positive semidefinite covariance matrix. The pdf in is uniquely described by the belief state ${\mathbf{b}} = \left\lbrack {\mathbf{μ}},{{vec}(\mathbf{\Sigma})} \right\rbrack^{T}$ where, due to symmetry, only the upper triangular matrix is stored which is encoded in the ${vec}{(\cdot)}$ operator. Thus, the dimensionality of the belief state $n_{b}$ increases quadratically with the state dimension $n$, i.e. $n_{b} = {\left({n^{2} + {3n}} \right)/2}$. If not mentioned explicitly otherwise, we refer to the belief state $\mathbf{b}$ as the belief.

### II-C Chance Constraints and Risk Measures

Chance constraints handle safety constraints under uncertainty by bounding the probability of undesired events. We use safety specifications in the form of half-spaces ${{\mathbf{α}}^{T}{\mathbf{x}}} \geq \beta$. Consider a Gaussian distributed random variable $\mathbf{x}$ with belief state $\mathbf{b}$. We calculate the probability of satisfying a half-space constraint as where ${erf}{(\cdot)}$ is the standard error function.

To quantify the outcome of violating a chance constraint ${\Pr\left\lbrack {{{\mathbf{α}}^{T}{\mathbf{x}}} \geq \beta} \right\rbrack} \geq {1 - \delta}$, we use the Value-at-Risk ($VaR$).

### Definition 4

The $VaR$ of a random variable $x \in {\mathbb{R}}$ with pdf $p(x)$ at level $\delta \in {(0,1\rbrack}$ is the $\left({1 - \delta} \right)$ quantile, i.e. $VaR$ allows us to formulate constraints that are qualitatively equivalent to chance constraints, i.e.

## Problem Setting

We consider the robot's stochastic motion and observations in the form where $\mathcal{Z} \subseteq {\mathbb{R}}^{\ell}$ is the observation space and ${\mathbf{w}},{\mathbf{v}}$ are the motion and observation noise, respectively. We model the robot's motion as a continuous-time differential equation. The observations are always provided in discrete time due to the sensor's sampling time. Especially for exteroceptive sensors like GPS, measurements occur much less frequently than the robot's control rate, encouraging us to consider discrete-time formulations. A reference controller, e.g. a controller that drives the robot to a goal state, is given as ${\mathbf{u}}_{\text{ref}}$.

### Problem 1

Given the stochastic dynamics , a reference controller $\mathbf{u}_{\text{ref}}$, a safe set $\mathcal{C}_{x} = \left\{ {\mathbf{x} \in \mathcal{X}}\mid{{{\mathbf{α}}^{T}\mathbf{x}} \geq \beta} \right\}$ defined in state space and a confidence level $\delta \in {(0,1\rbrack}$, synthesize a control law $\mathbf{u}$ that maps ${\mathbf{x} \times \mathbf{u}_{\text{ref}}}\mapsto\mathbf{u}$ such that at any time ${\Pr\left\lbrack {{\mathbf{x}{(t)}} \in \mathcal{C}_{x}} \right\rbrack} \geq {1 - \delta}$.

Ideally, to solve Problem 1, we would use the Bayes filter to capture the exact time evolution of the belief given an initial belief $p\left( {{\mathbf{x}}{(t_{0})}} \right)$, controls $\mathbf{u}$ and observations $\mathbf{z}$. However, exact belief calculations only exist in specialized cases which is why approximations need to be considered. Thus, we use an EKF as a tractable implementation of the Bayes filter in which beliefs are Gaussian. While the Gaussian belief of an EKF is exact for linear systems, it is only an approximation of the true belief in the nonlinear case. This assumption, however, is common in many practical scenarios, especially if the true probability distribution is unimodal. In future work, we aim to consider the mismatch between the modeled belief and the true belief.

To approach Problem 1, we reason about Gaussian belief states $\mathbf{b}$ instead of states $\mathbf{x}$ so that we can solve a relaxed problem under stochastic uncertainties. We propagate the belief through the nonlinear model in Eq. - by exploiting the fundamental EKF step that systems are linearized around the current mean.

### Assumption 1

To propagate the mean and covariance of a random variable $\mathbf{x}$ through a nonlinear function $\mathbf{η}$, we use a first-order Taylor series expansion We translate the safety specification over states in Problem 1 to a safe set over belief states where $h_{b}$ defines a risk-aware half-space | | $h_{b}({\mathbf{b}})$ | $:={{VaR}_{\delta}\left({{{\mathbf{α}}^{T}{\mathbf{x}}} - \beta} \right)}$ | | \(12\) | | | | ${= {{{\mathbf{α}}^{T}{\mathbf{μ}}} - \beta - {{erf}^{- 1}\left({1 - {2\delta}} \right)\sqrt{2{\mathbf{α}}^{T}\mathbf{\Sigma}{\mathbf{α}}}}}}.$ | | | Figure 2: A drone with uncertain position x and its pdf p (x) is moving in one dimension. A safety specification is defined as a bounded probability of collision with the wall. The resulting safe set over belief states is shown in blue and the current belief of the robot is depicted in red.

### Problem 2

Given the model - and a risk-aware safe set $\mathcal{C}_{b}$ defined over beliefs, find a control input $\mathbf{u}$ that renders $\mathcal{C}_{b}$ forward invariant.

By solving Problem 2, we ensure that the belief satisfies a $VaR$ formulation which is qualitatively equivalent (see Eq. ) to satisfying the chance constraint in Problem 1.

### Example

Consider a drone operating in one dimension with position $x \sim {\mathcal{N}\left(\mu,\sigma^{2} \right)}$, as shown in Fig. 2 and the Gaussian belief state $\mathbf{b} = \left\lbrack \mu,\sigma^{2} \right\rbrack^{T} \in {\mathbb{R}}^{2}$. A safety specification over states is to stay within the collision-free space with 90% probability, given by $\delta = 0.1$ and $\mathcal{C}_{x} = \left\{ {x \in {\mathbb{R}}}\mid{x \leq 2} \right\}$. The corresponding safe set $\mathcal{C}_{b}$ in belief space is defined through which is illustrated in blue in Fig. 2. In the depicted point in time, the belief state, shown as red circle, is right at the boundary of the safe set $\partial\mathcal{C}_{b}$ as the probability of colliding with the wall is exactly 10 %. Solving Problem 2 keeps the belief state (red circle) in $\mathcal{C}_{b}$ which in turn satisfies the original safety specification over states that $90\%$ of the drone's probability mass should be left of the wall.

## Risk-aware Control

Our solution to Problem 2 is divided into two main steps. First, we derive a stochastic hybrid system that accounts for uncertainties in the robot's motion and observations. Given this hybrid system describing the evolution of the robot's belief, we propose BCBFs to ensure forward invariance of our safe set defined over beliefs. BCBFs serve as a computationally efficient risk-aware safety filter that can be applied to various robotic systems under stochastic uncertainties.

### IV-A Hybrid Belief Dynamics

In the belief dynamics, it is important to distinguish between two evolutions: 1) The belief advances in continuous time as the state dynamics also evolve in continuous time. 2) At discrete timesteps $t_{k}$ when a new sensor observation is available, the belief changes instantaneously since the state distribution is conditioned on the measurement. This naturally leads to a hybrid dynamical system which is derived from a continuous-discrete EKF.

### IV-A1 Continuous-time Belief Dynamics

The continuous-time evolution of the belief directly follows from the derivation of the continuous EKF and is given by a set of ordinary differential equations (ODEs) where $\mathbf{A}$ is the Jacobian of the noise-free motion model in Eq. evaluated at the current mean $\mathbf{μ}$. For the design of BCBFs, the dynamics are required to be in control-affine form which has been proven to be true.

Since the belief vector $\mathbf{b}$ is comprised of the mean and the covariance matrix, we can express the continuous-time belief dynamics as a vector-valued ODE where ${\mathbf{f}}_{\Sigma} = {{vec}\left({\mathbf{F}}_{\Sigma} \right)}$ and ${\mathbf{g}}_{\Sigma} = {{vec}\left({\mathbf{G}}_{\Sigma} \right)}$ are the vector fields of Eq. in control-affine form. Note that ${\mathbf{G}}_{\Sigma} \in {\mathbb{R}}^{n \times n \times m}$ and, thus, the ${vec}{(\cdot)}$ operator maps it to a matrix ${\mathbf{g}}_{\Sigma} \in {\mathbb{R}}^{{{n{({n + 1})}}/2} \times m}$.

Consequently, if the control signal $\mathbf{u}$ is known, the belief at any point in time is obtained by forward integrating the belief dynamics in Eq.. However, when a new sensor reading is available, the belief changes instantaneously which is covered in the discrete-time Kalman update.

### IV-A2 Discrete-time Kalman Update

Every time a new observation ${\mathbf{z}}_{k}$ is available, we obtain the posterior distribution ${p\left({{{\mathbf{x}}\left(t_{k}^{+} \right)} \mid {{\mathbf{z}}_{1:{k - 1}},{\mathbf{z}}_{k}}} \right)} = {\mathcal{N}\left({\mathbf{μ}}^{+},\mathbf{\Sigma}^{+} \right)}$ by conditioning the prior distribution parameterized by ${\mathbf{b}}^{-} = {{\mathbf{b}}\left(t_{k}^{-} \right)}$ on ${\mathbf{z}}_{k}$. Note that $t_{k}^{-}$ is infinitesimal smaller than $t_{k} = t_{k}^{+}$. The conditioning leads to a discrete belief transition which is governed by the discrete-time Kalman update denote the Kalman gain and the Jacobian of the observation model, respectively. The measurement obtained at a discrete timestep is not known in advance which makes it generally difficult to do planning or control in belief space. However, the unknown measurement can be treated as a random variable making the measurement update stochastic.

### Proposition 1

Under Assumption 1, the innovation term ${\mathbf{θ}} = {\mathbf{K}\left({\mathbf{z}_{k} - {\mathbf{\ell}\left({\mathbf{μ}}^{-} \right)}} \right)}$ in Eq. is a random variable with distribution ${\mathbf{θ}} \sim {\mathcal{N}(\mathbf{0},\mathbf{\Lambda})}$ where The proof is straight-forward by applying Assumption 1 to the innovation term and is omitted for brevity.

Finally, combining the ODE in Eq. and the discrete-time Kalman update in Eq. leads to the hybrid system describing the evolution of the robot's belief over time. Fig. 3 illustrates an example trajectory of the belief. Our formulation has the advantage that we can allow arbitrary sampling times ${\deltat} = {t_{k} - t_{k - 1}}$. This is particularly useful for the analysis of scenarios where e.g., a sensor does not provide any information for a certain duration as in the case of GPS data inside a building.

### IV-B Belief Control Barrier Functions

The dynamical system $\mathcal{S}$ of the belief allows us to introduce BCBFs for safe control under stochastic uncertainties. BCBFs are defined similarly as CBFs, but they are defined over beliefs instead of states.

### Definition 5

(BCBF) Given a safe set $\mathcal{C}_{b}$ defined by Eq., $h_{b}(\mathbf{b})$ serves as a Belief Control Barrier Function (BCBF) for the stochastic dynamical system - if $\forall\mathbf{b}$ satisfying ${{h_{b}(\mathbf{b})} \geq 0},{{\exists\mathbf{u}} \in \mathcal{U}}$ such that Using this definition of a BCBF, the following theorem provides a condition for the forward invariance of the safe set $\mathcal{C}_{b}$ under the continuous-time evolution of the belief.

### Theorem 1

If a locally Lipschitz control input $\mathbf{u}{(t)}$ satisfies Eq. ${\forall t} \in {\lbrack t_{k},t_{k + 1})}$ for a given safe set with valid BCBF $h_{b}{(\mathbf{b})}$, then ${\Pr\left\lbrack {{h_{b}\left( {\mathbf{b}{(t)}} \right)} \geq 0} \right\rbrack} = 1$, provided that ${\mathbf{b}{(t_{k})}} \in \mathcal{C}_{b}$.

The proof is straight-forward since we only reason about the continuous-time evolution in the interval $\lbrack t_{k},t_{k + 1})$ in which the belief dynamics in Eq. are deterministic. Thus, interested readers are referred to the proof for traditional state-based CBFs.

Next, we analyze the effects of measurements on the forward invariance of $\mathcal{C}_{b}$. Since measurements are treated as random variables, we do not have control of the discrete belief transition. As a result, outlier measurements may cause the belief to leave the safe set $\mathcal{C}_{b}$ even though the considered state is safe, see Fig. 3. We show how to ensure forward invariance even in the presence of outlier measurements. To that end, we exploit the asymptotic stability of zeroing CBFs.

### Remark 1

Our BCBFs are zeroing CBFs that not only render $\mathcal{C}_{b}$ forward invariant but also asymptotically stable as the cont.-time belief dynamics are deterministic. Thus, if an initial belief is outside the safe set, it will be driven back to $\mathcal{C}_{b}$ over time.

In the following theorem, we derive an upper bound on the probability of leaving $\mathcal{C}_{b}$ under a discrete transition.

### Theorem 2

If the control input $\mathbf{u}{(t)}$ satisfies Eq., the probability of leaving the safe set under a discrete transition, i.e. $\Pr\left\lbrack {{h_{b}\left(\mathbf{b}^{+} \right)} < 0} \right\rbrack$, is bounded by with $\mathbf{\Lambda}$ defined as in Proposition 1 and *Proof:* Since $\mathbf{u}$ satisfies Eq. we know that ${h_{b}\left({\mathbf{b}}^{-} \right)} = {h_{b}\left({{\mathbf{b}}\left(t_{k}^{-} \right)} \right)} \geq 0$. Consequently, the value of the BCBF is in which we replace the posterior mean ${\mathbf{μ}}^{+}$ by its stochastic update equation from Proposition 1. Further, we add a covariance term that adds up to zero, which we rearrange to obtain $h_{b}\left({\mathbf{b}}^{-} \right)$. This yields a Gaussian distribution over possible BCBF values Finally, the probability that an outlier measurement causes the belief to leave $\mathcal{C}_{b}$ is calculated using as Theorem 2 provides us with a natural bound on the probability of leaving the safe set $\mathcal{C}_{b}$ under discrete sensor observations when the belief state ${\mathbf{b}}^{-}$ is on the boundary $\partial\mathcal{C}_{b}$. The derived natural bound only depends on our observation model $\mathbf{\ell}({\mathbf{x}})$, the noise covariance $\mathbf{R}$ and the prior covariance $\mathbf{\Sigma}^{-}$. Thus, the specific bound varies for different robotic systems and sensor types.

### Example

(Cont.) Consider the one-dimensional drone example introduced before. The drone is equipped with a sensor that provides noisy state observations $z_{k} = {{x{(t_{k})}} + v}$ where $v \sim {\mathcal{N}\left({{0,r} = 0.1} \right)}$. The prior variance is $\sigma^{-} = 0.3$ and a confidence level is set to ${1 - \delta} = 0.99$, then meaning that the probability of leaving $\mathcal{C}_{b}$ is at most 9 %. Note that this is a tight bound if the prior belief state is right at the boundary of the safe set and strictly smaller otherwise.

Figure 3: An example belief trajectory subject to an outlier measurement and the corresponding safe set shown as half-space. The initial belief b− is within the safe set 𝒞b whereas the posterior belief b+ leaves the safe set under the discrete transition. An asymptotically stable belief trajectory is shown in red while the true evolution of the state is shown in blue. The plot on the right shows value of hb (b), depicted in green.

Figure 3 shows a scenario in which the posterior belief ${\mathbf{b}}^{+}$ leaves the safe set due to an outlier measurement. Although the state $\mathbf{x}$ still satisfies the original half-space constraint at time $t_{k}$, the belief switches instantaneously from ${h_{b}\left( {\mathbf{b}}^{-} \right)} \geq 0$ to ${h_{b}\left( {\mathbf{b}}^{+} \right)} < 0$. This highlights the importance of keeping the belief state inside $\mathcal{C}_{b}$: Initially, the state $\mathbf{x}$ is considered to be safe, i.e. ${\mathbf{x}} \in \mathcal{C}_{x}$, but as time evolves, the only statement we can make is that the belief trajectory ${\mathbf{b}}{(t)}$ is asymptotically stable, see Remark 1. However, during this period $\mathbf{x}$ could leave $\mathcal{C}_{x}$ while the belief is driven back to $\mathcal{C}_{b}$ as shown in Fig. 3. We thus need to ensure that the belief state does not leave $\mathcal{C}_{b}$ in the first place, in order to guarantee that $\mathbf{x}$ remains in $\mathcal{C}_{x}$ with desired probability.

To ensure that the belief state does not leave $\mathcal{C}_{b}$, we modify $\mathcal{C}_{b}$ such that the probability of leaving $\mathcal{C}_{b}$ is bounded with a desired confidence. We define an augmented safe set ${\overset{\sim}{\mathcal{C}}}_{b} \subseteq \mathcal{C}_{b}$ with ${{\overset{\sim}{h}}_{b}({\mathbf{b}})} = {{h_{b}({\mathbf{b}})} - \gamma}$ for some $\gamma \geq 0$. This safe set is essentially a shrunk version of the original safe set $\mathcal{C}_{b}$. In the following theorem, we choose $\gamma$ such that the belief stays within $\mathcal{C}_{b}$ with desired probability.

### Theorem 3

The belief state $\mathbf{b}^{+}$ remains in the safe set $\mathcal{C}_{b}$ with probability ${\Pr\left\lbrack {\mathbf{b}^{+} \in \mathcal{C}_{b}} \right\rbrack} \geq {1 - \varepsilon}$ under the discrete reset map $\mathbf{b}^{+} = {\mathbf{\Delta}\left(\mathbf{b}^{-} \right)}$ if the control input $\mathbf{u}{(t)}$ satisfies Eq. for the function ${\overset{\sim}{h}}_{b}(\mathbf{b})$ (thus ${\overset{\sim}{h}}_{b}$ is a valid BCBF) and ${{\overset{\sim}{h}}_{b}\left(\mathbf{b}^{-} \right)} \geq 0$ for *Proof:* Similarly as for Th. 2, we calculate the probability of staying in the safe set $\mathcal{C}_{b}$ using Eq., Note that Theorem 3 provides probabilistic safety guarantees for the case that ${\mathbf{b}}^{-} \in {\overset{\sim}{\mathcal{C}}}_{b}$. If the posterior belief state ends up in the set $\mathcal{C}_{b} \smallsetminus {\overset{\sim}{\mathcal{C}}}_{b}$, it will be driven back to the augmented safe set if ${\overset{\sim}{h}}_{b}$ is a valid BCBF. If an outlier measurement occurs during this asymptotically stable convergence to ${\overset{\sim}{\mathcal{C}}}_{b}$, the natural bound in Theorem 2 holds. Once ${\mathbf{b}} \in {\overset{\sim}{\mathcal{C}}}_{b}$, the desired confidence in Theorem 3 holds again.

### IV-C Risk-aware control synthesis

To synthesize risk-aware control inputs under stochastic uncertainties arising from state estimation, we formulate the quadratic program (QP) | | ${\mathbf{u}}^{\ast} = \underset{{\mathbf{u}} \in \mathcal{U}}{\arg\min}$ | $\left({{\mathbf{u}} - {\mathbf{u}}_{\text{ref}}} \right)^{T}\left({{\mathbf{u}} - {\mathbf{u}}_{\text{ref}}} \right)$ | | \(25\) | | | s.t. | ${{\frac{\partial\overset{\sim}{h}}{\partial{\mathbf{b}}}\left({{{\mathbf{f}}_{b}({\mathbf{b}})} + {{\mathbf{g}}_{b}({\mathbf{b}}){\mathbf{u}}}} \right)} \geq {- {\overset{\sim}{h}({\mathbf{b}})}}},$ | | | where ${\mathbf{u}}_{\text{ref}}$ is a reference control input. This synthesis problem can be solved efficiently using off-the-shelf QP solvers.

Consider for example a quadrotor operating in 3D: It has 6 degrees of freedom (3D pose and orientation) and 4 control inputs (thrusters) which leads to a 12 dimensional state. Consequently, the belief state is of dimension ${\mathbf{b}} \in {\mathbb{R}}^{90}$ which is known as the curse of dimenionality and complicates the use of common optimization-based controllers such as MPC. We overcome the dimenionality problem of belief spaces by only optimizing over control inputs $\mathbf{u}$ which enables real-time applicability. The resulting control inputs satisfy the entire belief dynamics.

## Experiments

We evaluate our BCBFs in challenging scenarios in which uncertainties cannot be neglected^11^1Videos of our hardware experiments can be found in the supplementary material. Specifically, we show improved adherence to safety specifications through risk-awareness and computational efficiency over traditional CBFs and CCNMPC in simulations in Sec. V-A, safety under changing sensing conditions, such as sensor rates and measurement variances, in Sec. V-C, robustness to external disturbances as well as the generality to different sensor systems in Sec. V-D.

### V-A Safety analysis of BCBFs

### Setup

We compare our BCBFs to two baselines in an obstacle avoidance scenario. We consider a unicycle robot with state ${\mathbf{x}} = {\lbrack p_{x},p_{y},v,\varphi\rbrack}^{T}$ and dynamics and observations | | ${\overset{˙}{p}}_{y}$ | ${= {{v\sin(\varphi)} + w_{y}}},{\overset{˙}{\varphi} = {\omega + w_{\varphi}}}$ | | | | | ${\mathbf{z}}_{k}$ | $\left. = {\mathbf{x}}_{k} + {\mathbf{v}}_{k},{\mathbf{v}}_{k} \sim \mathcal{N}\left(\mathbf{0},{\mathbf{R}}) \right. \right).$ | | | Figure 4: Comparison of different control strategies for a two-dimensional avoidance scenario. The initial state follows a Gaussian distribution x0 ∼ 𝒩 ([0, 1.5, 0, 0], diag ([0.32, 0.22, 0.12, 0.12])) and the goal is. Simulated trajectories are shown in blue and the obstacle is depicted in red.

The nominal dynamics are corrupted by Gaussian noise ${\lbrack w_{x},w_{y},w_{v},w_{\varphi}\rbrack}^{T} \sim {\mathcal{N}(\mathbf{0},{\mathbf{Q}})}$ with motion noise ${\mathbf{Q}} = {{diag}\left(\left\lbrack 0.1^{2},0.1^{2},0.005^{2},0.005^{2} \right\rbrack \right)}$ and observation noise ${\mathbf{R}} = {{diag}{({\lbrack 0.2^{2},0.2^{2},0.1^{2},0.1^{2}\rbrack})}}$ with a sensor update rate of 10 Hz. The control input is given as ${\mathbf{u}} = {\lbrack a,\omega\rbrack}^{T}$. We obtain the belief dynamics in Eq. by applying the method described in Sec. IV-A where ${\mathbf{b}} \in {\mathbb{R}}^{14}$. The objective is to steer the robot towards a goal at $\lbrack 8,0\rbrack$ while avoiding collisions with a circular obstacle $\mathcal{O} = \left\{ {{\mathbf{p}} \in {\mathbb{R}}^{2}}\mid{{\parallel{{\mathbf{p}} - {\mathbf{c}}}\parallel}_{2} < r} \right\}$ where ${\mathbf{c}} = {\lbrack 5,0\rbrack}^{T}$ and $r = 1$ as shown in Fig. 4. The safety specification for collision avoidance is given as with $\delta = 0.01$. Due to the non-linearity of the obstacle description, we use the common approach to linearize Eq. around the mean state which is a strict overapproximation of the true collision condition as shown. The resulting risk-aware safe set is given by where ${VaR}_{\delta}{(\cdot)}$ with ${\mathbf{α}} = {\left({{\mathbf{μ}} - {\mathbf{c}}} \right)/{\parallel{{\mathbf{μ}} - {\mathbf{c}}}\parallel}_{2}}$ serves as a BCBF candidate. Due to a relative degree $r_{b} = 2$ in our BCBF candidate, we use second order formulations as in Eq..

We solve the resulting SDE using the DifferentialEquations.jl package in the Julia programming language. The reference control ${\mathbf{u}}_{\text{ref}}$ is given by a Linear-quadratic Regulator (LQR) that uses the mean estimate $\mathbf{μ}$ to steer the system towards the goal without any knowledge of the obstacle. The parameters chosen for the LQR are ${\mathbf{Q}}_{L} = {\text{diag}{\lbrack 10,5,5,5\rbrack}}$ and ${\mathbf{R}}_{L} = {\text{diag}{\lbrack 5,10\rbrack}}$. We compare two versions of BCBFs, namely one with only the natural bound ($\varepsilon = 0.5$) and one bounding the probability of leaving $\mathcal{C}_{b}$ by $\varepsilon = 0.01$.

### Baselines

We compare our BCBFs to two different baselines: 1.) Stochastic CBFs with incomplete state information which require cont.-time observations as well as a bounded estimation error. To enable continuous estimation, we use maximum likelihood observations between actual measurements which is not true in practice. The bounded estimation error was obtained by running a monte carlo study and take the maximum error. 2.) chance-constrained NMPC (CCNMPC) that formulates an MPC problem which includes Eq. as a constraint. Since MPC operates in discrete-time while we simulate a continuous system, we use a zero order hold to apply the control input. We run the MPC at 30 Hz and use a planning horizon of $N = 40$. The cost function is the same quadratic cost as in the reference LQR controller. 3.) In hardware experiments, we compare to a traditional state CBF that only considers the mean dynamics.

### Safety and computational efficiency

Figure 4 shows 100 simulated trajectories for different initial conditions sampled from a Gaussian while the quantitative results are summarized in Table I. BCBFs have the lowest number of collisions (0 for $\varepsilon = 0.01)$ and outperform both baselines. Interestingly, SCBFs cannot ensure safety almost surely as the assumption of cont.-time observations does not apply. Similarly, CCNMPC results in multiple collisions although it tries to satisfy the same safety specification. This is due to the fact that the optimization problem sometimes becomes infeasible in which case we need to relax the safety constraint. In, the authors reported that the percentage of infeasible solutions in their experiments was $2.8\%$. Infeasibility is not an issue for BCBFs, since they allow to formulate the control synthesis as QP over controls instead of a nonlinear program over states and controls, overcoming the curse of dimensionality. QP formulations are computationally efficient and can be run with up to 1kHz, see Table I.

### Effect of augmented safe set

We analyze the effect of the augmented safe set defined in Theorem 3. If no additional safety margin is used ($\varepsilon = 0.5$), the belief leaves $\mathcal{C}_{b}$ in $0.42\%$ of all simulated trajectories. When bounding the probability of leaving the safe set by ${\Pr{\lbrack{{h\left( {\mathbf{b}}^{+} \right)} < 0}\rbrack}} \leq 0.01$, the belief remains in $\mathcal{C}_{b}$ for all trajectories while keeping larger distances to the obstacle.

## collisions

TABLE I: Comparison of BCBFs to baselines.

### Control efficiency

Lastly, we evaluate the efficiency in terms of the average norm of the control input and the time $t_{g}$ to reach the goal. In this case CCNMPC is superior to all other approaches since it optimizes controls over a planning horizon whereas CBF approaches are purely reactive. This motivates to combine state-based MPC with BCBFs to achieve both, control efficiency and rigorous safety properties. In future work, we aim to explore this.

### V-B Setup of hardware experiment

We use the Bitcraze Crazyflie 2.1 quadrotor inside an OptiTrack motion capture (mocap) system, as shown in Fig. 1. The state of the drone is given as its 3D position $\mathbf{p}$ and velocity $\overset{˙}{\mathbf{p}}$. Its motion and observations are modeled as where ${\mathbf{u}} \in {\mathbb{R}}^{3}$ are the drone's desired accelerations and ${\mathbf{w}} \sim {\mathcal{N}(\mathbf{0},{\mathbf{Q}})}$ with a variance of $0.05^{2}$ along the diagonal of $\mathbf{Q}$. In our setting, we can only observe the drone's position $\mathbf{p}$. We add Gaussian noise ${\mathbf{v}} \sim {\mathcal{N}(\mathbf{0},{\mathbf{R}})}$ to the mocap data and reduce the sampling rate of the measurements. These parameters $\mathbf{R}$ and $f_{s}$ are varied throughout the experiments. We use the uncorrupted mocap data as ground truth to evaluate the performance of BCBFs.

We use the EKF in Sec. IV-A to obtain the belief dynamics with ${\mathbf{b}} \in {\mathbb{R}}^{27}$, where the ODE is discretized using Euler's scheme. We convert the desired acceleration $\mathbf{u}$ synthesized by our BCBFs into a setpoint consisting of desired roll and pitch angles as well as thrust for the real quadrotor using. Setpoints are sent to the Crazyflie at 100 Hz and tracked by the onboard PID controller which serves as ${\mathbf{u}}_{\text{ref}}$. We compare BCBFs only to traditional CBFs as we were not able to run CCNMPCs in real-time with our setup.

Figure 5: Ground truth trajectories of 20 different runs of Exp. I for CBFs and BCBFs. The sampling rate fs changes throughout the corridor segments. The measurement variances are given as R1 = diag [0.082, 0.082], R2 = diag [0.22, 0.22] and R3 = diag [0.152, 0.152], respectively.

### V-C Experiment I - Changing sensing conditions

In our first experiment, we showcase the robustness of BCBFs to changing sensing conditions. For that purpose, we navigate the drone along a U-shaped corridor as shown in Fig. 5. The corridor is the union of three polytopes. In each of the three polytopes, we change the measurement noise $\mathbf{R}$ and sampling rates $f_{s}$ according to Fig. 5. In the third polytope, we additionally place a circular obstacle to increase the difficulty of the scenario. The safety specification is given as an intersection of risk-aware half-spaces with a collision probability of $\delta = 0.05$. The half-spaces are given by the polytope representation of the corridor.

Figure 5 shows the ground truth trajectories of 20 different runs for a state-based CBF and a BCBF. It can be observed that the state-based approach cannot satisfy the safety specification whereas all 20 trajectories are collision free for the BCBF. Interestingly, there are no trajectories for the BCBF passing the obstacle on the right side since it is too risky to navigate through the narrow passage. As a consequence, the drone stops in front of the obstacle and slowly moves around the left side which took about 5-10 seconds. Although this behavior ensures safety, it highlights that a robot can get stuck in a local minimum when using a CBF approach. This could be overcome by combining BCBFs with a motion planner such as MPC.

### V-D Experiment II - External disturbances

In this experiment illustrated in Figure 1, we additionally study the effect of disturbances on the nominal dynamics. To that end, we define a safe set as a cuboid that we want the drone to stay in with 95% probability. The drone is exposed to both, sensing uncertainties as well as an external wind disturbance from a fan. Instead of position measurements, we measure the drone's velocity through an added optical flow sensor. These velocity measurements are given by Since we only measure the drone's velocity and neglect the global position measurements from mocap, there is an inevitable drift in the position estimate obtained from integrating the velocity. A human operator is generating reference acceleration commands ${\mathbf{u}}_{\text{ref}}$ using a gamepad and actively tries to steer the drone outside the safe set.

Figure 6 shows the mean belief trajectory as well as ground truth for the described setting. The ellipses indicate the position uncertainty at selected points in time. The drone moves towards the corners of the safety region in which the BCBF prevents the belief from leaving the safe set. Over time, the uncertainty in the position estimate grows due to the lack of a global positioning system and, thus, the drone gets increasingly cautious. The mean belief moves further towards the center of the safety region as this increases the likelihood of satisfying the safety specification. At all times, the ground-truth state stays within the safety region.

Figure 6: Illustration of Exp. II. The drone should stay within the safety region colored in grey while a wind disturbance (shown as red arrows) is acting on the drone. The ground truth trajectory is shown in blue and the mean belief trajectory is shown in black. The 95% confidence ellipses at selected points in time are depicted in purple.

## CONCLUSIONS AND FUTURE WORK

Our work enables risk-aware control synthesis for stochastic dynamical systems with incomplete state information by combining continuous-discrete EKFs with CBFs defined over Gaussian belief states. Instead of defining safety specifications as hard constraints on the state, we consider a risk-aware approach in which we bound the probability of violation. BCBFs are applicable to any robotic system in which the state estimate is provided by an EKF. Our simulation and hardware experiments show that BCBFs ensure that robots adhere to safety specifications in the presence of both, real-world motion and observation uncertainties.

In future, we aim to explore the combination of motion planners such as state-based MPC that only consider the mean estimate with our proposed BCBFs. In that way, we can ensure safety while enhancing control efficiency. We are also interested in extending our results to arbitrary belief distributions that can be represented using particles filters.
