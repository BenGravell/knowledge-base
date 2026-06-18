## Introduction

We consider the problem of safely learning the dynamics of controlled continuous-time stochastic systems from discrete-time observations of trajectory data. This setting is common in applications such as robotics, finance, and healthcare, where system dynamics are only partially known and must be estimated from data. A key challenge in these applications is ensuring safety during both the learning phase and subsequent deployment \[Bonalli et al., (https://arxiv.org/html/2506.02754v3#bib.bib78 "Sequential Convex Programming for Non-linear Stochastic Optimal Control"); Lew et al., (https://arxiv.org/html/2506.02754v3#bib.bib79 "Sample Average Approximation for Stochastic Programming with Equality Constraints")\]. As an example, consider an autonomous robot navigating a partially known and turbulent environment, as illustrated in Figure (https://arxiv.org/html/2506.02754v3#S1.F1 "Figure 1 ‣ Outline of contributions. ‣ 1 Introduction ‣ Safely Learning Controlled Stochastic Dynamics"). While the deterministic part of the dynamics may be approximately modeled using prior knowledge, the stochastic disturbances (represented by the brown region in Figure (https://arxiv.org/html/2506.02754v3#S1.F1 "Figure 1 ‣ Outline of contributions. ‣ 1 Introduction ‣ Safely Learning Controlled Stochastic Dynamics")) due to wind or sensor noise are often unknown and must be learned. Collecting data through naive exploration can result in unsafe trajectories, potentially causing damage to the system or its environment. A second example arises in financial portfolio management, where the drift component of asset prices may be known from historical data, but market volatility remains uncertain. Safety here may correspond to the requirement that the portfolio value stays above a critical threshold with high probability, simulating portfolio loss aversion in risk-sensitive financial decision-making. These examples highlight a common need: learning stochastic dynamics of a system from data, while ensuring safety throughout the process. This requires ensuring that all executed trajectories remain within a predefined safe region with high probability. In addition, at deployment time, the learned model should enable prediction of whether a proposed control input satisfies the safety requirements, including those not encountered during training \[Wabersich and Zeilinger, (https://arxiv.org/html/2506.02754v3#bib.bib62 "A predictive safety filter for learning-based control of constrained nonlinear dynamical systems"); Lindemann et al., (https://arxiv.org/html/2506.02754v3#bib.bib36 "Safe planning in dynamic environments using conformal prediction")\].

### Outline of contributions

The contributions of this work are as follows.

Safe learning method. We derive a method that safely learns controlled stochastic dynamics, where safety is defined as the requirement that system trajectories remain within a designated set of safe states with high probability. Our approach incrementally expands the known safe control set by selecting novel controls to evaluate, collecting corresponding trajectory data, and refining three models: a dynamics model for predicting state evolution, a safety model that estimates the probability of remaining within the safe region, and a reset model that captures the probability of returning the system to its initial state distribution, enabling repeated safe exploration under uncertainty. Alongside these models, we refine uncertainty estimates using kernel-based confidence bounds. After training, these models enable prediction of dynamics, safety, and reset feasibility for any given control, including those not seen during training.

Provably safe exploration and adaptive estimation rates. We prove that the proposed method guarantees safety and derive learning rates for system estimation, with rates that are adaptive to the Sobolev regularity of the underlying dynamics. Crucially, our approach requires only smooth dynamics (with respect to time, state, and control variables) and an initial non-empty set of known safe controls. These mild assumptions make the method applicable to a broad range of complex real-world systems subject to stochastic disturbances, found in diverse areas including robotics, fluid flow control, and chemical reaction control \[Martin and Salaün, (https://arxiv.org/html/2506.02754v3#bib.bib39 "The true role of accelerometer feedback in quadrotor control"); Plappert et al., (https://arxiv.org/html/2506.02754v3#bib.bib44 "Multi-goal reinforcement learning: challenging robotics environments and request for research"); Morton et al., (https://arxiv.org/html/2506.02754v3#bib.bib41 "Deep dynamical modeling and control of unsteady fluid flows"); Peters et al., (https://arxiv.org/html/2506.02754v3#bib.bib46 "Causal models for dynamical systems"); Fu et al., (https://arxiv.org/html/2506.02754v3#bib.bib21 "Mobile aloha: learning bimanual mobile manipulation using low-cost whole-body teleoperation"); Wei et al., (https://arxiv.org/html/2506.02754v3#bib.bib66 "DiffPhyCon: a generative approach to control complex physical systems")\].

Experimental validation. We empirically demonstrate the performance of the approach in terms of safety, estimation accuracy, and computational efficiency. Specifically, we evaluate it on a benchmark two-dimensional stochastic dynamical system evolving in a bounded, safety-critical environment under stochastic perturbations (see Figure (https://arxiv.org/html/2506.02754v3#S1.F1 "Figure 1 ‣ Outline of contributions. ‣ 1 Introduction ‣ Safely Learning Controlled Stochastic Dynamics")). An open-source Python implementation is provided (available at github.com/lmotte/dynamics-safe-learn).

Figure 1: Illustration of a complex, smooth dynamical system under deterministic conditions (left) and stochastic conditions with unknown disturbances (right). Shown are 100 simulated trajectories under three different controls. Ignoring stochastic disturbances (e.g., wind turbulence) can lead to unsafe trajectories (right), emphasizing the necessity of safe estimation methods that explicitly account for uncertainty.

## Background

We formalize the problem of safely learning controlled stochastic dynamical systems as follows.

### Controlled SDE

Let $X$ be a dynamical system governed by a non-linear, $n$-dimensional controlled SDE \[Bonalli and Bonnet, (https://arxiv.org/html/2506.02754v3#bib.bib81 "First-order Pontryagin Maximum Principle for Risk-averse Stochastic Optimal Control Problems"); Lew et al., (https://arxiv.org/html/2506.02754v3#bib.bib80 "Risk-averse Trajectory Optimization via Sample Average Approximation")\],

Here, $T_{\max} > 0$ is the fixed time horizon, $(b,a)$ are functions mapping ${\mathbb{R}}^{n} \times {\mathbb{R}}^{d}$ to ${\mathbb{R}}^{n} \times {\mathbb{R}}^{n \times n}$, $W{(t)}$ is an $n$-dimensional standard Brownian motion, $p_{0}$ is an initial probability density over ${\mathbb{R}}^{n}$, and $\mathcal{H} \subseteq {\mathcal{F}{({{\lbrack 0,T_{\max}\rbrack} \times {\mathbb{R}}^{n}},{\mathbb{R}}^{d})}}$ is a finite-dimensional set of admissible controls, where $\mathcal{F}{({{\lbrack 0,T_{\max}\rbrack} \times {\mathbb{R}}^{n}},{\mathbb{R}}^{d})}$ denotes the space of measurable functions from ${\lbrack 0,T_{\max}\rbrack} \times {\mathbb{R}}^{n}$ to ${\mathbb{R}}^{d}$.

### Example 1 (Second-order dynamical system)

captures second-order dynamics under control $u$ and state-dependent diffusion $a\left( {X{(t)}} \right)$. Real-world examples include drones navigating turbulent environments (where $u$ represents thrust or steering, and $a{( \cdot )}$ models wind turbulence), fluid-dynamical systems \[Batchelor, (https://arxiv.org/html/2506.02754v3#bib.bib74 "An introduction to fluid dynamics")\], and molecular dynamics (where $u$ captures external forces such as optical traps, and $a{( \cdot )}$ reflects spatially varying thermal fluctuations \[Volpe and Volpe, (https://arxiv.org/html/2506.02754v3#bib.bib59 "Simulation of a brownian particle in an optical trap"); Marago et al., (https://arxiv.org/html/2506.02754v3#bib.bib38 "Optical trapping and manipulation of nanostructures"); Pesce et al., (https://arxiv.org/html/2506.02754v3#bib.bib43 "Optical tweezers: theory and practice")\]).

### Safety-critical environments

Let $g:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be a function that partitions the state space into safe and unsafe regions. The safe region is given by $\{{x \in {\mathbb{R}}^{n}}:{{g{(x)}} \geq 0}\}$, while the unsafe region is given by $\{{x \in {\mathbb{R}}^{n}}:{{g{(x)}} < 0}\}$.

### Safe control

Let $X_{u}$ denote the solution to Eq. ((https://arxiv.org/html/2506.02754v3#S2.E1 "In Controlled SDE. ‣ 2 Background ‣ Safely Learning Controlled Stochastic Dynamics")) under the control $u \in \mathcal{H}$ (well-defined by existence and uniqueness; see Sec.3 in Bonalli and Rudi \[(https://arxiv.org/html/2506.02754v3#bib.bib8 "Non-parametric learning of stochastic differential equations with non-asymptotic fast rates of convergence")\]). Let $u_{\theta}:{{{\lbrack 0,T_{\max}\rbrack} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{d}}$ denote a family of controls parameterized by $\theta \in D \subset {\mathbb{R}}^{m}$, where $D$ is a compact subset of ${\mathbb{R}}^{m}$. Such a finite-dimensional parameterization is a mild assumption that is widely prevalent in many real-world applications, including robotics \[Berkenkamp et al., (https://arxiv.org/html/2506.02754v3#bib.bib6 "Safe model-based reinforcement learning with stability guarantees")\], process control \[Seborg et al., (https://arxiv.org/html/2506.02754v3#bib.bib75 "Process dynamics and control")\], and financial engineering \[Merton, (https://arxiv.org/html/2506.02754v3#bib.bib76 "Optimum consumption and portfolio rules in a continuous-time model")\].

We define the safety level of the control $u_{\theta}$ at time $t \in {\lbrack 0,T_{\max}\rbrack}$ as

We define the safety level up to time $T \in {\lbrack 0,T_{\max}\rbrack}$ of the control $u_{\theta}$ as

### Learning problem

We formulate the problem of safely learning controlled stochastic dynamical systems as the estimation of the probability density map

where $p_{\theta}{(t,x)}$ is the density of the state $X_{u_{\theta}}{(t)}$ under control $u_{\theta}$, well-defined by standard existence and uniqueness results (see Sec.3 in Bonalli and Rudi \[(https://arxiv.org/html/2506.02754v3#bib.bib8 "Non-parametric learning of stochastic differential equations with non-asymptotic fast rates of convergence")\]). To estimate this density, we collect a dataset of trajectories

where each $w_{i}^{k}$ denotes an independent Brownian motion sample path driving the stochastic trajectory, and $M_{k}$ denotes the number of time steps in trajectory $k$. All controls $u_{\theta_{k}}$ are required to be safe. Specifically, the minimal probability of remaining within the safe region up to the time horizons ${(T_{k})}_{k = 1}^{K} = {(t_{M_{k}})}_{k = 1}^{K}$ is constrained by

This problem poses a fundamental challenge due to the coupling between learning and safety: accurately estimating the density $p_{\theta}$ requires data, but collecting data must respect safety constraints defined by $s^{\infty}$, which themselves depend on the very dynamics encoded in $p_{\theta}$.

### Related work

Safe learning in control systems under uncertainty is a central topic in reinforcement learning, with methods built on assumptions such as known dynamics \[Hewing et al., (https://arxiv.org/html/2506.02754v3#bib.bib26 "Learning-based model predictive control: toward safe learning in control")\], controllability \[Turchetta et al., (https://arxiv.org/html/2506.02754v3#bib.bib55 "Safe exploration in finite markov decision processes with gaussian processes"); Mania et al., (https://arxiv.org/html/2506.02754v3#bib.bib37 "Active learning for nonlinear system identification with guarantees"); Selim et al., (https://arxiv.org/html/2506.02754v3#bib.bib48 "Safe reinforcement learning using black-box reachability analysis")\], or recovery policies \[Hans et al., (https://arxiv.org/html/2506.02754v3#bib.bib25 "Safe exploration for reinforcement learning."); Moldovan and Abbeel, (https://arxiv.org/html/2506.02754v3#bib.bib40 "Safe exploration in markov decision processes")\].

Much of the literature focuses on discrete-time or discrete-state systems modeled as Markov Decision Processes (MDPs), where risk-sensitive and safe exploration techniques have been developed \[Coraluppi and Marcus, (https://arxiv.org/html/2506.02754v3#bib.bib14 "Risk-sensitive and minimax control of discrete-time, finite-state markov decision processes"); Geibel and Wysotzki, (https://arxiv.org/html/2506.02754v3#bib.bib23 "Risk-sensitive reinforcement learning applied to control under constraints"); Moldovan and Abbeel, (https://arxiv.org/html/2506.02754v3#bib.bib40 "Safe exploration in markov decision processes"); Garcia and Fernández, (https://arxiv.org/html/2506.02754v3#bib.bib22 "Safe exploration of state and action spaces in reinforcement learning")\]. Among these, Safe Bayesian Optimization (BO) methods stand out for providing some of the strongest high-confidence safety guarantees during exploration \[Sui et al., (https://arxiv.org/html/2506.02754v3#bib.bib52 "Safe exploration for optimization with gaussian processes"), (https://arxiv.org/html/2506.02754v3#bib.bib53 "Stagewise safe bayesian optimization with gaussian processes"); Bottero et al., (https://arxiv.org/html/2506.02754v3#bib.bib9 "Information-theoretic safe exploration with gaussian processes"); Li et al., (https://arxiv.org/html/2506.02754v3#bib.bib35 "Safe time-varying optimization based on gaussian processes with spatio-temporal kernel")\], particularly in MDP settings with known dynamics or access to safety level evaluations \[Turchetta et al., (https://arxiv.org/html/2506.02754v3#bib.bib55 "Safe exploration in finite markov decision processes with gaussian processes"), (https://arxiv.org/html/2506.02754v3#bib.bib56 "Safe exploration for interactive machine learning")\]. In continuous domains, early work focused on designing control policies that avoid unsafe regions \[Akametalu et al., (https://arxiv.org/html/2506.02754v3#bib.bib19 "Reachability-based safe learning with gaussian processes"); Koller et al., (https://arxiv.org/html/2506.02754v3#bib.bib31 "Learning-based model predictive control for safe exploration")\], while more recent approaches incorporate offline learning and online adaptation for nonlinear systems \[Lew et al., (https://arxiv.org/html/2506.02754v3#bib.bib33 "Safe active dynamics learning and control: a sequential exploration–exploitation framework")\]. Stability-based guarantees via Lyapunov theory offer formal certification but often require full dynamics knowledge \[Berkenkamp et al., (https://arxiv.org/html/2506.02754v3#bib.bib6 "Safe model-based reinforcement learning with stability guarantees"); Richards et al., (https://arxiv.org/html/2506.02754v3#bib.bib47 "The lyapunov neural network: adaptive stability certification for safe learning of dynamical systems")\]. Safe BO has also been adapted to continuous settings \[Sukhija et al., (https://arxiv.org/html/2506.02754v3#bib.bib54 "GoSafeOpt: scalable safe exploration for global optimization of dynamical systems"); Prajapat et al., (https://arxiv.org/html/2506.02754v3#bib.bib45 "Safe guaranteed exploration for non-linear systems")\], under assumptions such as access to dynamics, safety oracles, or specific control-theoretic properties. Joint estimation of both dynamics and safety remains comparatively underexplored, particularly in continuous-time settings \[Ahmadi et al., (https://arxiv.org/html/2506.02754v3#bib.bib2 "Safely learning dynamical systems from short trajectories"); Dalal et al., (https://arxiv.org/html/2506.02754v3#bib.bib15 "Safe exploration in continuous action spaces"); Wabersich and Zeilinger, [2018b](https://arxiv.org/html/2506.02754v3#bib.bib60 "Safe exploration of nonlinear dynamical systems: a predictive safety filter for reinforcement learning"); Fisac et al., (https://arxiv.org/html/2506.02754v3#bib.bib20 "A general safety framework for learning-based control in uncertain robotic systems"); Wabersich and Zeilinger, [2018a](https://arxiv.org/html/2506.02754v3#bib.bib61 "Linear model predictive safety certification for learning-based control"); Khojasteh et al., (https://arxiv.org/html/2506.02754v3#bib.bib32 "Probabilistic safety constraints for learned high relative degree system dynamics"); Wagener et al., (https://arxiv.org/html/2506.02754v3#bib.bib64 "Safe reinforcement learning using advantage-based intervention"); Wachi and Sui, (https://arxiv.org/html/2506.02754v3#bib.bib63 "Safe reinforcement learning in constrained markov decision processes"); Gu et al., (https://arxiv.org/html/2506.02754v3#bib.bib24 "A review of safe reinforcement learning: methods, theory and applications")\].

In contrast to much of the literature, we assume no prior model of the system dynamics or safety function. Instead, we jointly explore and learn both the stochastic dynamics and the safety probabilities from trajectory data. Our method applies to broad classes of continuous-time, continuous-state stochastic systems, and provides provable guarantees on both safety and estimation accuracy. To the best of our knowledge, no prior work provides joint safe exploration and density estimation guarantees in this setting.

## Assumptions

As formalized by the No-Free-Lunch Theorem \[Devroye et al., (https://arxiv.org/html/2506.02754v3#bib.bib17 "A probabilistic theory of pattern recognition")\], learning is only possible under prior assumptions. We now state and discuss the key assumptions used in this work.

### Assumption (A1) (Initial safe controls)

For $\varepsilon \in {\lbrack 0,1\rbrack}$, a non-empty set $S_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$ is provided such that

This assumption ensures that at least one control is known to be safe at the outset, allowing safe exploration to begin. In fact, $S_{0}$ may be as small as a singleton; only one known safe control is required. Without such a point, safe learning cannot be initiated. We express the assumption in set form to allow for larger safe sets, which can accelerate exploration while preserving guarantees. This is a standard assumption in the literature of safe UCB methods \[Sui et al., (https://arxiv.org/html/2506.02754v3#bib.bib52 "Safe exploration for optimization with gaussian processes"); Turchetta et al., (https://arxiv.org/html/2506.02754v3#bib.bib55 "Safe exploration in finite markov decision processes with gaussian processes"); Berkenkamp et al., (https://arxiv.org/html/2506.02754v3#bib.bib6 "Safe model-based reinforcement learning with stability guarantees")\], and is realistic in many applications including robotics \[Sukhija et al., (https://arxiv.org/html/2506.02754v3#bib.bib54 "GoSafeOpt: scalable safe exploration for global optimization of dynamical systems")\] and safety-critical process control \[Qin and Badgwell, (https://arxiv.org/html/2506.02754v3#bib.bib77 "A survey of industrial model predictive control technology")\], where systems naturally start in safe conditions, e.g., $S_{0} = {\{{(0,\theta)}:{\theta \in D}\}}$.

### Resetting control

Let $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ define a region in the state space from which resets are feasible. Specifically, if ${h{({X{(t)}})}} \geq 0$, then it is feasible to reset the system to the initial distribution $p_{0}$. Formally, this means there exists a mechanism (or control) that reinitializes the system from the current state $X{(t)}$ to a new state independently sampled from $p_{0}$. We define the reset level at time $t \in {\lbrack 0,T_{\max}\rbrack}$ for a given control $u_{\theta}$ as

The function $h$ delimits a region of the state space from which resets are feasible. Larger reset regions correspond to greater operational flexibility. In simulated environments, where resets are effectively cost-free, the reset region can cover the entire state space ${\mathbb{R}}^{n}$. In contrast, real-world systems typically require substantial resources or manual intervention, making resets feasible only in restricted regions (e.g., near the original distribution $p_{0}$).

### Assumption (A2) (Initial resetting controls)

For $\xi \in {\lbrack 0,1\rbrack}$, a non-empty set $R_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$ is provided such that

This assumption guarantees the existence of at least one control capable of returning the system to the reset region with high probability. Assumption [(A2)](https://arxiv.org/html/2506.02754v3#Thmassumption2 "Assumption (A2) (Initial resetting controls). ‣ Resetting control. ‣ 3 Assumptions ‣ Safely Learning Controlled Stochastic Dynamics") enables the generation of independent sample paths starting from the same initial conditions, which is crucial for evaluating variance and managing uncertainty during safe exploration. As with Assumption [(A1)](https://arxiv.org/html/2506.02754v3#Thmassumption1 "Assumption (A1) (Initial safe controls). ‣ 3 Assumptions ‣ Safely Learning Controlled Stochastic Dynamics"), one known reset point is sufficient, though larger reset sets accelerate learning. A simple case is $R_{0} = {\{{(0,\theta)}:{\theta \in D}\}}$, corresponding to systems that can always be reset from the initial condition. In practice, reset feasibility depends on system constraints: for instance, batch chemical reactors can often be reset only in early phases, before irreversible reactions occur \[Seborg et al., (https://arxiv.org/html/2506.02754v3#bib.bib75 "Process dynamics and control")\]. In contrast, many autonomous systems like drones or driving robots can usually be reset, at least during training.

### Assumption (A3) (Smoothness of system dynamics)

The map $p$ lies in the Sobolev space $H^{\nu}{({\mathbb{R}}^{n + m + 1})}$ with $\nu > {\frac{1}{2}{\max{(n,{m + 1})}}}$, where $n$ and $m$ denote the state and control parameter dimensions, respectively. Moreover, ${\sup_{x \in {\mathbb{R}}^{n}}\left\| {p{( \cdot, \cdot,x)}} \right\|_{H^{\nu}{({\mathbb{R}}^{m + 1})}}} < {+ \infty}$, ${\sup_{{(\theta,t)} \in {D \times {\lbrack 0,T_{\max}\rbrack}}}{\|{p{(\theta,t, \cdot )}}\|}_{H^{\nu}{({\mathbb{R}}^{n})}}} < \infty$.

This smoothness assumption ensures that the system dynamics are sufficiently regular for our purposes. It is standard in statistical learning theory and underpins our convergence guarantees \[Pillaud-Vivien et al., (https://arxiv.org/html/2506.02754v3#bib.bib65 "Statistical optimality of stochastic gradient descent on hard learning problems through multiple passes")\]. Sobolev regularity of the drift and diffusion terms in the underlying stochastic differential equation is expected to imply Sobolev regularity of the resulting state densities under standard conditions. This follows from classical results in parabolic PDE theory, where solutions typically gain regularity relative to the coefficients, roughly two derivatives in space and one in time. A formal analysis of this connection is beyond the scope of the present work and is left for future investigation (see Bonalli and Rudi \[(https://arxiv.org/html/2506.02754v3#bib.bib8 "Non-parametric learning of stochastic differential equations with non-asymptotic fast rates of convergence")\] for related results).

## Proposed method

We propose a method for safely exploring and learning system dynamics over a parameterized control space $\mathcal{H} = {\{ u_{\theta}\mid{\theta \in D \subset {\mathbb{R}}^{m}}\}}$. Following the safe UCB framework \[Sui et al., (https://arxiv.org/html/2506.02754v3#bib.bib52 "Safe exploration for optimization with gaussian processes"), (https://arxiv.org/html/2506.02754v3#bib.bib53 "Stagewise safe bayesian optimization with gaussian processes"); Bottero et al., (https://arxiv.org/html/2506.02754v3#bib.bib9 "Information-theoretic safe exploration with gaussian processes")\], our goal is to select controls that reduce model uncertainty while ensuring, with high probability, that trajectories (i) remain within the safe region and (ii) end in the reset region. We jointly learn three models: a dynamics model (state densities), a safety model (safety probabilities), and a reset model (reset probabilities), each equipped with confidence bounds from a shared kernel. This enables active exploration under high-probability constraints. After training, the learned models support inference on unseen inputs and yield a certified control set that can be deployed with safety guarantees.

The known safe-resettable set is expanded iteratively by alternating between system estimation (Section [4.2](https://arxiv.org/html/2506.02754v3#S4.SS2 "4.2 System estimation ‣ 4 Proposed method ‣ Safely Learning Controlled Stochastic Dynamics")) and safe sampling (Section [4.3](https://arxiv.org/html/2506.02754v3#S4.SS3 "4.3 Safe sampling ‣ 4 Proposed method ‣ Safely Learning Controlled Stochastic Dynamics")), leveraging prior knowledge of the initial safe and reset sets as well as the regularity of the dynamics ${(\theta,t,x)}\mapsto{p_{\theta}{(t,x)}}$.

A step-by-step breakdown of the overall method is provided in Appendix [B](https://arxiv.org/html/2506.02754v3#A2 "Appendix B Implementation details ‣ Safely Learning Controlled Stochastic Dynamics"), with algorithm tables for each module and their computational complexities.

### Initialization

Let $N \in {\mathbb{N}}$ denote the current iteration. We initialize at $N = 0$ using the known safe set $S_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$ and reset set $R_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$. We define the initial safe-resettable set

We select ${(\theta_{0},t_{0},T_{0})} \in \Gamma_{0}$, ensuring that the control is known to be safe over $\lbrack 0,T_{0}\rbrack$ and ends in the reset region.

### System estimation

In this step, we update the dynamics, safety, and reset models based on the observed trajectories, and compute predictive uncertainty for each.

### Estimation at $(\theta_{N},t_{N})$

At iteration $N$, the control $u_{\theta_{N}}$ is evaluated using $Q$ stochastic trajectories. Here, $N$ indexes the iteration, and $i$ indexes the $i$-th trajectory simulated under that control, each corresponding to an independent sample $w_{i}^{N}$ of the Brownian motion driving the system. We collect the samples ${({X_{u_{\theta_{N}}}{(w_{i}^{N},t_{N})}})}_{i = 1}^{Q}$ and estimate the state density at $(\theta_{N},t_{N})$ using a kernel density estimator:

where ${\rho_{R}{(x)}} \triangleq {R^{n/2}{\| x\|}^{- {n/2}}B_{n/2}{({2\piR{\| x\|}})}}$, $R > 0$, and $B_{n/2}$ is the Bessel $J$ function of order $n/2$ (See Bonalli and Rudi \[(https://arxiv.org/html/2506.02754v3#bib.bib8 "Non-parametric learning of stochastic differential equations with non-asymptotic fast rates of convergence")\]).

We then compute estimates of the safety and reset probabilities

Let the collection of values at all observed points $\left( {(\theta_{i},t_{i})} \right)_{i = 1}^{N}$ be

### Model update

We fit kernel ridge regressors for the density, safety, and reset functions using a Matérn kernel $k$ (with Sobolev smoothness $\nu$) and regularization $\lambda > 0$

where ${k{(\theta,t)}} \triangleq {({k{({(\theta,t)},{(\theta_{i},t_{i})})}})}_{i = 1}^{N}$, $K \triangleq {({k{({(\theta_{i},t_{i})},{(\theta_{j},t_{j})})}})}_{{i,j} = 1}^{N}$, and $\lambda$ is a regularization term. Although training data consist of discrete-time observations, learned regression models are defined over continuous time, a distinction seldom addressed in the literature.

The predictive uncertainty at $(\theta,t)$ is given by

### Safe sampling

We now select a new point to sample by maximizing uncertainty over the safe-resettable region.

### Feasibility criteria

A point $(\theta,t,T)$ is feasible if (i) $t \leq T$, (ii) the system remains safe up to time $T$, i.e., ${s^{\infty}{(\theta,T)}} \geq {1 - \varepsilon}$, and (iii) the trajectory ends in the reset region with high probability, i.e., ${r{(\theta,T)}} \geq {1 - \xi}$.

We implement these constraints via lower confidence bounds (LCBs)

where ${\beta_{N}^{s},\beta_{N}^{r}} > 0$ are confidence parameters set from known upper bounds on the RKHS norms of the safety and reset functions (see Remark (https://arxiv.org/html/2506.02754v3#Thmremark1 "Remark 1. ‣ Stopping rule. ‣ 4.3 Safe sampling ‣ 4 Proposed method ‣ Safely Learning Controlled Stochastic Dynamics")).

We then define the safe-resettable feasible set

### Sampling rule

We choose the next $(\theta_{N + 1},t_{N + 1},T_{N + 1})$ by maximizing uncertainty over the feasible set

Optimization is performed using discretization or gradient-based methods. Several computational techniques for efficient optimization are presented in the Appendix (see Algorithm (https://arxiv.org/html/2506.02754v3#algorithm4 "In Efficient sampling algorithm. ‣ B.2 Safe sampling ‣ Appendix B Implementation details ‣ Safely Learning Controlled Stochastic Dynamics")).

### Stopping rule

We stop the exploration once the maximum uncertainty over the feasible set falls below a threshold $\eta > 0$

ensuring that exploration concludes once the models reaches the desired level of accuracy.

### Remark 1

The derivation in Appendix [A.7](https://arxiv.org/html/2506.02754v3#A1.SS7 "A.7 Proof of safe learning of controlled Sobolev dynamics ‣ Appendix A Proofs ‣ Safely Learning Controlled Stochastic Dynamics") shows that the confidence parameters depend on upper bounds of the RKHS norms of the safety and reset functions. These bounds may be available from prior knowledge of the system's regularity. We view this prior knowledge as a reasonable minimal assumption for guaranteeing safe learning under unknown dynamics. When unavailable, the bounds can be conservatively overestimated, ensuring safety but potentially leading to slower exploration. Developing adaptive strategies to estimate these quantities without prior knowledge is a promising direction for future work, for instance through online adaptation via the doubling trick \[Shalev-Shwartz and others, (https://arxiv.org/html/2506.02754v3#bib.bib34 "Online learning and online convex optimization")\].

## Safety and estimation guarantees for Sobolev dynamics

Safety and exploration guarantees for safe kernelized UCB methods have been developed in prior work \[Sui et al., (https://arxiv.org/html/2506.02754v3#bib.bib52 "Safe exploration for optimization with gaussian processes"), (https://arxiv.org/html/2506.02754v3#bib.bib53 "Stagewise safe bayesian optimization with gaussian processes"); Bottero et al., (https://arxiv.org/html/2506.02754v3#bib.bib9 "Information-theoretic safe exploration with gaussian processes")\], grounded in kernelized bandit theory \[Srinivas et al., (https://arxiv.org/html/2506.02754v3#bib.bib51 "Gaussian process optimization in the bandit setting: no regret and experimental design"); Valko et al., (https://arxiv.org/html/2506.02754v3#bib.bib58 "Finite-time analysis of kernelised contextual bandits"); Janz et al., (https://arxiv.org/html/2506.02754v3#bib.bib28 "Bandit optimisation of functions in the matérn kernel rkhs")\], which in turn builds on linear bandit results \[Dani et al., (https://arxiv.org/html/2506.02754v3#bib.bib16 "Stochastic linear optimization under bandit feedback."); Auer, (https://arxiv.org/html/2506.02754v3#bib.bib4 "Using confidence bounds for exploitation-exploration trade-offs")\]. Building on this foundation, we establish novel theoretical guarantees for safe exploration and dynamics estimation under Sobolev regularity. Complete proofs are deferred to Appendix [A](https://arxiv.org/html/2506.02754v3#A1 "Appendix A Proofs ‣ Safely Learning Controlled Stochastic Dynamics").

### Theorem 5.1 (Safely learning controlled Sobolev dynamics)

Let $\eta > 0$, and assume Assumptions [(A1)](https://arxiv.org/html/2506.02754v3#Thmassumption1 "Assumption (A1) (Initial safe controls). ‣ 3 Assumptions ‣ Safely Learning Controlled Stochastic Dynamics")--[(A3)](https://arxiv.org/html/2506.02754v3#Thmassumption3 "Assumption (A3) (Smoothness of system dynamics). ‣ Resetting control. ‣ 3 Assumptions ‣ Safely Learning Controlled Stochastic Dynamics") hold. Set $R = Q^{1/{({n + {2\nu}})}}$ and $\lambda = N^{- 1}$. Then there exist constants ${c_{1},\ldots,c_{5}} > 0$, independent of $N,Q,\delta,\eta$, such that if

then the stopping condition ${{\max_{{(\theta,t,T)} \in \Gamma_{N}}\sigma_{N}}{(\theta,t)}} < \eta$ is satisfied after at most $N \leq {c_{2}\eta^{- {2/{({1 - \alpha})}}}}$ iterations for any $\alpha > {{({m + 1})}/{({m + 1 + {2\nu}})}}$. Moreover:

(Safety): All selected triples $(\theta_{i},t_{i},T_{i})$ satisfy ${s^{\infty}{(\theta_{i},T_{i})}} \geq {1 - \varepsilon}$ and ${r{(\theta_{i},T_{i})}} \geq {1 - \xi}$, providing safety guarantees during training. Moreover, the final set $\Gamma_{N}$ includes only controls meeting these thresholds and can thus serve as a certified safe set for deployment.

(Estimation guarantees): For all ${(\theta,t,T)} \in \Gamma_{N}$,

This result ensures that our method both respects safety constraints and achieves convergence rates adaptive to the system's Sobolev regularity. The condition on $Q$ provides a lower bound on the number of trajectory samples $Q$ required per control to guarantee the prescribed confidence level. Up to logarithmic factors, it requires

where $n$ is the state dimension and $\nu$ the Sobolev regularity. For instance, when the system is sufficiently regular with $\nu \geq {n + m + 1}$, the algorithm terminates in at most $N = {\mathcal{O}{(\eta^{- 3})}}$ iterations, assuming $Q \gtrsim N^{3}$. Although we do not analyze the size of $\Gamma_{N}$, its structure can be inferred from the available uncertainty estimates; a formal characterization of $\Gamma_{N}$ is left to future work.

## Numerical experiments

We evaluate our method on a representative smooth nonlinear stochastic system. Specifically, the experiments aim to assess the following: (i) satisfaction of safety and reset constraints, (ii) efficiency of exploration under different safety thresholds, (iii) prediction accuracy for dynamics, safety, and reset maps, (iv) computational cost and scalability.

### System and environment

We consider a 2D second-order dynamical system whose acceleration is directly controlled by the input. The system evolves according to the controlled SDE

where ${X{(t)}} \in {\mathbb{R}}^{2}$, ${V{(t)}} \in {\mathbb{R}}^{2}$ denote position and velocity, $u$ is the control function, and $W_{t}$ is a Brownian motion. The noise amplitude $a{(X)}$ is spatially dependent:

with $X_{c} = {}$, $\sigma = 2$, and $A = 5$. The initial state follows $\mathcal{N}{(0,{\sigma_{0}I_{{\mathbb{R}}^{2}}})}$ with $\sigma_{0} = 0.1$, and the maximal time horizon is $T_{\max} = 20$. The system evolves within the bounded safe region ${({- 10},10)}^{2}$, and each trajectory must end in the reset region defined as a disk of radius 2.5 centered at the origin. Such models arise in robotics and autonomous navigation, involving trajectory control with localized disturbances (e.g., slippery or uneven terrain). Figure (https://arxiv.org/html/2506.02754v3#S1.F1 "Figure 1 ‣ Outline of contributions. ‣ 1 Introduction ‣ Safely Learning Controlled Stochastic Dynamics") illustrates the effect of such state-dependent noise through 100 trajectories generated under different controls.

### Control space

Controls are parameterized as sequences of $m$ fixed accelerations of magnitude $v$, applied in directions $(\theta_{1},\ldots,\theta_{m})$. During the exploration phase $({0 \leq t \leq T_{explo}})$, each direction $\theta_{i}$ is applied over intervals of equal length, yielding

with damping term $- V$ ensuring velocity convergence. For $({t > T_{explo}})$, a feedback controller steers the system toward $\mu_{0}$:

with damping factor $\kappa > 0$. Controls are clipped to keep the system within the safe region. We set $v = 2.0$, $\kappa = 0.5$, $m = 2$, $T_{explo} = 6$, and $n_{\text{steps}} = 500$.

### Method's hyperparameters

Our method depends on several hyperparameters that govern safety thresholds $(\varepsilon,\xi)$, confidence levels $(\beta_{s},\beta_{r})$, kernel smoothness $(\lambda,\gamma)$, and bandwidth $R$, with distinct values for estimating dynamics and constraints. We test ${(\varepsilon,\xi)} \in {\{ 0.1,\, 0.3,\, 0.5,\infty\}}$, with 1000 iterations and initial safe control $({- {\pi/3}},{\pi/3})$. Candidate selection for uncertainty maximization is restricted to a local subset for efficiency (Appendix [B](https://arxiv.org/html/2506.02754v3#A2 "Appendix B Implementation details ‣ Safely Learning Controlled Stochastic Dynamics"), Algorithm (https://arxiv.org/html/2506.02754v3#algorithm4 "In Efficient sampling algorithm. ‣ B.2 Safe sampling ‣ Appendix B Implementation details ‣ Safely Learning Controlled Stochastic Dynamics")). A detailed discussion of each hyperparameter's role, tuning procedure, and practical heuristics is provided in Appendix [B.3](https://arxiv.org/html/2506.02754v3#A2.SS3 "B.3 Role and tuning of hyperparameters ‣ Appendix B Implementation details ‣ Safely Learning Controlled Stochastic Dynamics").

Figure 2: One trajectory per selected control after 1000 iterations for various thresholds.

### Safe exploration

Figure (https://arxiv.org/html/2506.02754v3#S6.F2 "Figure 2 ‣ Method’s hyperparameters. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics") displays one trajectory per selected control after 1000 iterations, under various threshold settings ($\varepsilon = \xi \in {\{ 0.1,0.3,0.5,{+ \infty}\}}$). In Figure (https://arxiv.org/html/2506.02754v3#S6.F3 "Figure 3 ‣ Safe exploration. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics"), the top row displays the learned safety level maps while the bottom row shows the corresponding reset probability maps for various threshold pairs $\varepsilon = \xi$, with values increasing from left to right in $\{ 0.1,\, 0.3,\, 0.5,{+ \infty}\}$. Our approach only accepts candidate controls whose predicted safety and reset probabilities (estimated via 200-path Monte Carlo simulations) exceed the predefined thresholds. By filtering only controls meeting the safety criteria, exploration is confined to a safe region with a chosen probability of staying safe. Overall, these visualizations highlight how increasing the threshold values influences control selection, providing insights into the trade-off between exploration and safety.

Figure 3: Safety (top row) and reset (bottom row) probabilities over iterations for various thresholds.

### Exploration rate and coverage

In Figure (https://arxiv.org/html/2506.02754v3#S6.F4 "Figure 4 ‣ Exploration rate and coverage. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics"), we plot the selected controls after 1000 iterations for various threshold pairs $\varepsilon = \xi$, with values increasing from left to right in $\{ 0.1,\, 0.3,\, 0.5,{+ \infty}\}$. Figures (https://arxiv.org/html/2506.02754v3#S6.F2 "Figure 2 ‣ Method’s hyperparameters. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics") and (https://arxiv.org/html/2506.02754v3#S6.F4 "Figure 4 ‣ Exploration rate and coverage. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics") clearly illustrate the exploration-safety trade-off. Relaxing thresholds leads to broader control coverage and faster information gain, but with decreased safety guarantees. Conversely, strict thresholds restrict exploration, particularly around regions with safety or reset probabilities close to the specified thresholds. This aligns with the intuition supported by our theoretical analysis: sample complexity tends to increase in regions where smaller uncertainty is required to proceed safely. As a result, these regions act as bottlenecks, slowing down the process and potentially stopping exploration within the connected component that satisfies the constraints and includes the initial safe control. Additional results on information gain across iterations are provided in Appendix [C.2](https://arxiv.org/html/2506.02754v3#A3.SS2 "C.2 Information gain over iterations ‣ Appendix C Additional experimental results ‣ Safely Learning Controlled Stochastic Dynamics").

Figure 4: Control coverage for various thresholds.

### Safety and reset level prediction

In Table (https://arxiv.org/html/2506.02754v3#S6.T1 "Table 1 ‣ Safety and reset level prediction. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics"), we quantify the accuracy of the learned model for various threshold pairs $\varepsilon = \xi$ in $\{ 0.1,\, 0.3,\, 0.5,{+ \infty}\}$ by evaluating the prediction quality of the safety and reset levels over 1000 predictions. We report the mean squared error (MSE) and the standard deviation, with the ground truth provided by Monte Carlo estimates based on 100 samples (displayed in Figure (https://arxiv.org/html/2506.02754v3#S6.F5 "Figure 5 ‣ Dynamics prediction. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics")). In Figure (https://arxiv.org/html/2506.02754v3#S6.F6 "Figure 6 ‣ Computational considerations. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics"), we plot the learned safety and reset maps, whose accuracies can be qualitatively assessed by comparing their values with those in Figure (https://arxiv.org/html/2506.02754v3#S6.F5 "Figure 5 ‣ Dynamics prediction. ‣ 6 Numerical experiments ‣ Safely Learning Controlled Stochastic Dynamics"). As expected, prediction accuracy improves as safety constraints are relaxed, due to the broader coverage of the control space.

Table 1: Safety and reset level prediction error statistics (MSE ± Std. Dev.)

### Dynamics prediction

To verify that our method captures the underlying system dynamics, we compare predicted trajectory densities with ground-truth trajectories under known-safe controls. Qualitative results show close agreement in both mean and variance. Full visualizations and evaluation details are provided in Appendix [C.1](https://arxiv.org/html/2506.02754v3#A3.SS1 "C.1 Dynamics prediction accuracy ‣ Appendix C Additional experimental results ‣ Safely Learning Controlled Stochastic Dynamics").

Figure 5: Ground-truth safety (left) and reset (right) probabilities estimated via 100 Monte Carlo samples for 1000 randomly selected controls.

### Computational considerations

Our method runs end-to-end in under 32 minutes on standard hardware, covering candidate selection, simulation, evaluation, and model updates. Appendix [B.4](https://arxiv.org/html/2506.02754v3#A2.SS4 "B.4 Computational considerations ‣ Appendix B Implementation details ‣ Safely Learning Controlled Stochastic Dynamics") provides runtimes, hardware specs, and potential optimizations (e.g., sketching, parallelization), confirming the method's practicality on standard hardware.

Figure 6: Learned safety (top row) and reset (bottom row) level maps for various thresholds.

## Conclusion

We introduced a provably safe and efficient method for learning controlled stochastic dynamics from trajectory data. By leveraging kernel-based confidence bounds and smoothness assumptions, our method incrementally expands an initial safe control set, ensuring that all trajectories remain within predefined safety regions throughout the learning process. Theoretical guarantees were established for both safety and estimation accuracy, with learning rates that adapt to the Sobolev regularity of the true dynamics. Numerical experiments corroborate our theoretical findings regarding safety and estimation accuracy. By tuning the safety ($\varepsilon$) and reset ($\xi$) thresholds, users can explicitly control the trade-off between conservative safety satisfaction and exploratory behavior. While our experimental validation focuses on a low-dimensional setting, the theoretical results scale with dimension: the convergence rates for the proposed estimators decrease polynomially with dimension and can mitigate the curse of dimensionality under sufficient smoothness. This makes the method applicable to higher-dimensional systems, which we plan to investigate in future work. Further research will include validation on physical systems (e.g., autonomous robots), improved scalability through fast kernel methods (e.g., sketching or incremental updates), comparisons with safe RL baselines, systematic analyses of kernel and threshold selection, and extensions to handle abrupt dynamics and non-diffusive disturbances such as jump processes arising in pedestrian--vehicle interactions and hybrid systems. These developments will further support applications in safety-critical control and decision-making under uncertainty.
