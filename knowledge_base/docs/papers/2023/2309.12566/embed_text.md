## Introduction

Trajectory optimization for motion or path planning is a fundamental problem in autonomous systems. Several requirements must be simultaneously considered for autonomous robot motion, path planning, navigation, and control. Examples include the specifications of mission objectives, examining the certifiable dynamical feasibility of a robot, ensuring collision avoidance, and considering the internal physical and communication constraints of autonomous robots.

In particular, generating an energy-efficient and collision-free safe trajectory is of the utmost importance during the process of autonomous vehicle driving, autonomous racing drone, unmanned aerial vehicles, electric vertical take-off and landing (eVTOL) urban air mobility (UAM), missile guidance, space vehicle control, and satellite attitude trajectory optimization

From an algorithmic perspective, the complexity of motion planning is NP-complete. Various computational methods have been proposed for motion planning, including sampling-based methods, nonlinear programming (NLP), sequential convex programming (SCP), differential dynamic programming (DDP), hybrid methods, and differential-flatness-based optimal control.

Optimization methods can explicitly perform safe and efficient trajectory generation for path and motion planning. The two most popular optimal path and motion planning methods for autonomous robots are gradient- and sampling-based methods for trajectory optimization. The former frequently assumes that the objective and constraint functions in a given planning problem are differentiable and can rapidly provide a locally optimal smooth trajectory. However, numerical and algorithmic computations of derivatives (gradient, Jacobian, Hessian, etc.) are not stable in the worst case; preconditioning and prescaling must be accompanied by and integrated into the solvers. In addition, integrating the outcomes of perception obtained from exteroceptive sensors such as LiDARs and cameras into collision-avoidance trajectory optimization requires additional computational effort in dynamic and unstructured environments.

Sampling-based methods for trajectory generation do not require function differentiability. Therefore, they are more constructive than the former gradient-based optimization methods for modelling obstacles without considering their shapes in the constrained optimization for collision-free path planning. In addition, sampling-based methods naturally perform explorations, thereby avoiding the local optima. However, derivative-free-sampling-based methods generally produce coarse trajectories with zigzagging and jerking movements. For example, rapidly exploring random trees (RRT) and probabilistic roadmap (PRM) methods generate coarse trajectories. To mitigate the drawbacks of gradient- and sampling-based methods while maintaining their advantages, a hybrid method that combines them can be considered, as proposed in.

Several open-source off-the-shelf libraries are available for implementing motion planning and trajectory optimization, which include Open Motion Planning Library (OMPL), Stochastic Trajectory Optimization for Motion Planning (STOMP), Search-Based Planning Library (SBPL), And Covariant Hamiltonian Optimization for Motion Planning (CHOMP).

The path integral (PI) for stochastic optimal control, which was first presented in, is another promising approach for sampling-based real-time optimal trajectory generation. In the path integral framework, the stochastic optimal control associated with trajectory optimization is transformed into a problem of evaluating a stochastic integral, for which Monte Carlo importance sampling methods are applied to approximate the integral. It is also closely related to the cross-entropy method for stochastic optimization and model-based reinforcement learning for decision making. The use of path integral control has recently become popular with advances in high-computational-capability embedded processing units and efficient Monte Carlo simulation techniques.

There are several variations of the PI control framework. The most widely used method in robotics and control applications is the model predictive path integral (MPPI) control, which provides a derivative-free sampling-based framework to solve finite-horizon constrained optimal control problems using predictive model-based random rollouts in path-integral approximations. However, despite its popularity, the performance and robustness of the MPPI are degraded in the presence of uncertainties in the simulated predictive model, similar to any other model-based optimal control method. To take the plant-model mismatches of simulated roll-outs into account, adaptive MPPI, learning-based MPPI and tube-based MPPI, uncertainty-averse MPPI, fault-tolerant MPPI, safety-critical MPPI using control barrier function (CBF), and covariance steering MPPI have been proposed. Risk-aware MPPI based on the conditional value-at-risk (CVaR) have also been investigated for motion planning with probabilistic estimation uncertainty in partially known environments.

The path integral (PI) control framework can also be combined with parametric and nonparametric policy search methods and improvements. For example, RRT is used to guide PI control for exploration and PI control is used to guide policy searches for open-loop control, parameterized movement primitives, and feedback control. To smoothen the sampled trajectories generated from the PI control, gradient-based optimization, such as DDP, is combined with MPPI, regularized policy optimization based on the cross-entropy method is used, and it is also suggested to smooth the resulting control sequences using a sliding window and a Savitzky-Golay filter (SGF) and introducing an additional penalty term corresponding to the time derivative of the action.

PI control is related to several other optimal control and reinforcement learning strategies. For example, variational methods of path integral optimal control are closely related to entropy-regularized optimal control and maximum entropy RL (MaxEnt RL). The path integral can be considered as a probabilistic inference for stochastic optimal control and reinforcement learning.

One of the most important technical issues in the practical application of path integral control is the sampling efficiency. Various importance sampling strategies have been suggested for rollouts in predictive optimal control. Several importance sampling (IS) algorithms exist with different performance costs and benefits, as surveyed in. Adaptive importance sampling (AIS) procedures are considered within the optimal control and MPPI control. In addition to the AIS algorithms, learned importance sampling, general Monte Carlo methods, and cross-entropy methods have been applied to PI-based stochastic optimal control.

Various case studies of PI-based optimal control have been published: autonomous driving, autonomous flying, space robotics, autonomous underwater vehicles, and robotic manipulation planning. Path integral strategies for optimal predictive control have also been adopted to visual servoing techniques. Recently, the MPPI was integrated into Robot Operating Systems 2 (ROS 2), an open-source production-grade robotics middleware framework.

We expect that more applications of path integral control will emerge, particularly with a focus on trajectory optimization of motion planning for autonomous systems such as mobile robots, autonomous vehicles, drones, and service robots. In addition, it has been shown that path integral control can be easily extended to the cooperative control of multi-agent systems.

There are still issues that must be addressed for scalable learning with safety guarantees in path integral control and its extended variations.

Exploration-exploitation tradeoff is still not trivial,

Comparisons of MPC-like open-loop control and parameterized state-feedback control should be further investigated as problem and task-specific policy parameterization itself is not trivial,

Extensions to output-feedback and dual control have not yet been studied, and

Extensions to cooperative and competitive multi-agent trajectory optimization with limited inter-agent measurements and information should be further investigated.

The remainder of this paper is organized as follows: Section II presents the overview of some path integral control methods. Section III reviews the theoretical background of path integral control and its variations. Section IV describes the algorithmic implementation of several optimal control methods that employ a path-integral control framework. In Section V, two MATLAB simulation case studies are presented to demonstrate the effectiveness of predictive path integral control. Section VI presents the four ROS2/Gazebo simulation results of trajectory optimization for autonomous mobile robots, in which MPPI-based local trajectory optimization methods are demonstrated for indoor and outdoor robot navigation. In Section VII, extensions of path integral control to policy search and learning, improving sampling efficiency, multi-agent decision making, and trajectory optimization of manifolds are discussed. Section VIII concludes the paper and suggests directions for future research and development of path-integral control, especially for autonomous mobile robots.

## Overview of path integral controllers

Figure 1: Hierarchical classification of various path integral control methods.

The standard CEM is a unified probabilistic approach for tackling combinatorial optimization, Monte-Carlo simulation, and machine learning challenges.

CEM-RL merges CEM and TD3 to enhance DRL, optimizing both performance and sample efficiency.

Constrained CEM is a safety-focused reinforcement learning method that learns feasible policies while effectively tracking and satisfying constraints.

This introduces a gradient-based optimization into the CEM framework to improve the convergence rate.

Decentralized CEM improves Cross-Entropy Method efficiency by employing a distributed ensemble of CEM instances to mitigate local optima traps.

MPPI leverages parallel optimization and generalized importance sampling for efficient navigation in nonlinear systems.

It enhances off-road navigation with an augmented state space and tailored controllers, offering improved performance and robustness.

It enhances MPPI by incorporating input-lifting and a novel action cost to effectively reduce command chattering in nonlinear control tasks.

It enhances robotic navigation by using a normal log-normal mixture for efficient and feasible trajectory sampling in complex environments.

Tube MPPI merges MPPI with Constrained Covariance Steering for robust, constraint-efficient trajectory optimization in stochastic systems.

This research develops a neural network-based, risk-aware method for off-road navigation, enhancing success and efficiency by analyzing empirical traction distributions.

GP-MPPI combines MPPI with sparse Gaussian Processes for improved autonomous navigation in complex environments by learning model uncertainties and disturbances, and optimizing local paths.

TABLE I: Types of CEM algorithms and their description.
TABLE I: Types of CEM algorithms and their description.
TABLE II: Types of MPPI algorithms and their description.

It is an algorithm that merges PI2-CMA to optimize policies and auto-tune exploration noise in reinforcement learning.

It examines the convergence of RL and black-box optimization in PI, introducing the efficient PIBB algorithm.

It is an advanced RL method that combines the gradient extraction principles of PI2-CMA with the feedback mechanism of DDP.

It reexamines PI2, linking it with evolution strategies and information-geometric optimization to refine its cost minimization approach using natural gradient descent.

It introduces PI2-CMA-KCCA, a RL algorithm that accelerates robot motor skill acquisition by using heuristic information from Kernel Canonical Correlation Analysis and CMA to guide Path Integral Policy Improvement.

Critic PI2 combine trajectory optimization and deep actor-critic learning in a model-based RL framework for improved efficiency in continuous control tasks.

TABLE III: Types of PI2-CMA algorithms and their description.

Path integral (PI) control methods stand at the forefront of contemporary research in stochastic optimal control and trajectory optimization. These techniques, primarily characterized by their robustness and versatility, have been developed to tackle complex control tasks under uncertainty. Central to these methods are Cross-Entropy Method (CEM), Model Predictive Path Integral (MPPI), and PI$^{2}$-CMA, each with distinct variations and algorithmic developments. In Fig. 1, we mentioned some hierarchical structure of path integral control methods. Below, we present a structured overview of these methods, outlining their types and key characteristics.

The Cross-Entropy Method is a probabilistic technique that iteratively refines control policies by minimizing a cost function and employing importance sampling. It has evolved significantly since its inception. Some of the CEM algorithms and there key characteristics are given in Table II. MPPI is an open-loop controller using the receding horizon scheme. It has been pivotal for real-time control with various developments focusing on improving efficiency and reducing computational load. Some of the MPPI algorithms and there key characteristics are given in Table II. PI$^{2}$-CMA represents an amalgamation of path integral control with Covariance Matrix Adaptation. It's especially suitable for problems where the cost landscape is highly non-convex or unknown. Some of the MPPI algorithms and there key characteristics are given in Table III.

## Path Integral Control: Theory

### III-A Stochastic optimal control

Controlled stochastic differential equation Consider a controlled stochastic differential equation of the following form:

where the initial condition is given by $X_{0} = x_{0} \in {\mathbb{R}}^{n}$, and $W_{t}$ is a standard Brownian motion. The solution to the SDE associated with the Markov policy $\pi:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{m}}$ is denoted by $X_{t}^{\pi}$.

Cost-to-go function For a given Markov policy $\pi$, the cost-to-go corresponding to policy $\pi$ is defined as

where $T > 0$ denotes the terminal time, $L:{{{\mathbb{R}} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$ denotes the running cost, and $\phi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ denotes the terminal cost.

Expected and optimal cost-to-go function The expected cost-to-go function is defined as

where the expectation is considered with respect to the probability of the solution trajectory for the SDE with an initial time and condition ${(t,x)} \in {{\mathbb{R}} \times {\mathbb{R}}^{n}}$. The goal of the stochastic optimal control is to determine the optimal policy.

The corresponding optimal cost-to-go function is defined as

for each ${(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$,

### III-B The Hamilton-Jacobi-Bellman equation

The Hamilton-Jacobi-Bellman equation for the optimal cost-to-go function is defined as follows

${(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$. where

is a backward evolution operator defined on the functions of the class $\mathcal{C}^{1} \times \mathcal{C}^{2}$. Additionally, the boundary condition is given by ${V^{*}{(T,x)}} = {\phi{(x)}}$.

### III-C Linearization of the HJB PDE

Control affine form and a quadratic cost As a special case of, we consider the controlled dynamics (diffusion process)

and the cost-to-go

where $X_{s}^{\pi}$ is the solution to the SDE for $s \in {\lbrack t,T\rbrack}$ with the initial condition $X_{t}^{\pi} = x_{t}$. In this study, we assume $G_{t}^{\pi} > 0$ for all $t \in {\lbrack 0,T\rbrack}$ and any (control) policy $\pi$.

### Remark

1\) $G_{t}^{\pi}$ is not adaptive with respect to the Brownian motion as it depends on $(X_{\tau}^{\pi})$ for $\tau > t$.

2\) The second term in is a stochastic integral with respect to the Brownian motion and it vanishes when taking expectation. This term will play an essential role when applying a change of measure. $\square$

The goal of stochastic optimal control for the dynamics and the cost-to-go is to determine an optimal policy that minimizes the expected cost-to-go with respect to the policy.

where the expectation $\mathbb{E}$ is considered with respect to the stochastic process $X_{t:T}^{\pi} \sim \mathcal{P}^{\pi}$ which is the (solution) path of SDE.

Theorem 1: The solution of the stochastic optimal control in and is given as

where $\pi{(t,x)}$ denotes an arbitrary Markov policy. $\blacksquare$

Because the solution represented in Theorem 1 is defined in terms of a path integral for which the expectation $\mathbb{E}$ is taken with respect to the random process $X_{t:T}^{\pi} \sim \mathcal{P}^{\pi}$, that is, the (solution) path of the SDE, this class of stochastic optimal control with control-affine dynamics and quadratic control costs is called the path integral (PI) control.

Solution of the HJB equation For stochastic optimal control of the dynamics and, the HJB equation can be rewritten as

with the boundary condition ${V^{*}{(T,x)}} = {\phi{(x)}}$. In addition, the optimal state-feedback controller is given by

Here, Markov policy $\pi$ is replaced by state-feedback control $u$ without loss of generality. The value (i.e., the optimal expected cost-to-go) function $V^{*}$ is defined as a solution to the second-order PDE

Linearization via exponential transformation We define an exponential transformation as follows:

that also belongs to class $\mathcal{C}^{1} \times \mathcal{C}^{2}$ provided $V^{*}{(t,x)}$ does. Applying the backward evolution operator of the *uncontrolled* process, that is, $u = 0$, to the function $\psi{(t,x)}$, we obtain

which is a linear PDE with the boundary condition ${\psi{(T,x)}} = {\exp{({- {{\phi{(x)}}/\lambda}})}}$. This linear PDE is known as the backward Chapman-Kolmogorov PDE.

### III-D The Feynman-Kac formula

The Feynman-Kac lemma provides a solution to the linear PDE

where ${\psi{(T,x_{T})}} = {\exp{({- {{\phi{(x)}}/\lambda}})}}$. In other words,

where the expectation $\mathbb{E}$ is taken with respect to the random process $X_{t:T}^{0} \sim \mathcal{P}^{0}$; that is, the (solution) path of the uncontrolled version of the SDE

and the uncontrolled cost-to-go is given by

which is again a nonadaptive random process. From the definition of $\psi$, this gives us a path-integral form for the value function:

${(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$.

### III-E Path integral for stochastic optimal control

Path integral control Although the Feynman-Kac formula presented in Section III-D provides a method to compute or approximate the value function, it is still not trivial to obtain an optimal Markov policy because the optimal controller in is defined in terms of the gradient of $V^{*}$, not by $V^{*}$. From and Theorem 1, combined with the path integral control theory, we have

where the initial condition is $X_{t}^{0} = x$. This is equivalent to in Theorem 1.

Information theoretic stochastic optimal control Regularized cost-to-go function

where $G_{t}^{0}$ is the state-dependent cost given in and $\frac{d\mathcal{P}^{\pi}}{d\mathcal{P}^{0}}$ is the Radon-Nikodym derivative^11^1This R-N derivative $\frac{d\mathcal{P}^{\pi}}{d\mathcal{P}^{0}}$ denotes the density of $\mathcal{P}^{\pi}$ relative to $\mathcal{P}^{0}$. We assume that $\mathcal{P}^{\pi}$ is absolutely continuous with respect to $\mathcal{P}^{0}$, denoted by $\mathcal{P}^{\pi} \ll \mathcal{P}^{0}$. for the probability measures $\mathcal{P}^{\pi}$ and $\mathcal{P}^{0}$. Total expected cost function

is known as the free energy of a stochastic control system. There is an additional cost term for the KL divergence between $\mathcal{P}^{\pi}$ and $\mathcal{P}^{0}$ which we can interpret as a control cost. From Girsanov's theorem, we obtain the following expression for the Radon-Nikodym derivative corresponding to the trajectories of the control-affine SDE.

where $u_{s} = {\pi{(s,X_{s}^{\pi})}}$ is the control input and the initial condition $X_{t}^{\pi} = X_{t}^{0} = x_{t}$ with an initial time $t \in {\lbrack 0,T\rbrack}$ can be arbitrary.

The goal of KL control is to determine a probability measure that minimizes the expected total cost

provided $\mathcal{V}_{t}^{*} = {\inf_{\mathcal{P} \in \mathbf{\Delta}^{\pi}}{\mathcal{V}_{t}{(\mathcal{P})}}}$ exists, where $\mathbf{\Delta}^{\pi}$ denotes the space of probability measures corresponding to a policy $\pi$.

Theorem 2: The optimal regularized cost-to-go has zero variance and is the same as the expected total cost

which is equivalent to given in Section III-D. $\blacksquare$

In addition, the Radon-Nikodym derivative is given by

and combining with the R-N derivative, we obtain

where $u_{s} = {\pi{(s,X_{s})}}$ is the control input following the policy $\pi:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{m}}$, and $\omega_{t}^{\pi}$ is known as the importance weight that is also a random process.

## Path Integral Control: Algorithms

### IV-A MC integration: Model-based rollout

Let a tuple $(\Omega,\mathcal{F},\mathcal{Q})$ be a probability space with a random variable $X$ and consider the function ${\ell{({\mathbf{X}})}} = {\int_{0}^{T}{L{({\mathbf{X}}_{t})}{dt}}}$ or ${\ell{(X)}} = {L{({\mathbf{X}}_{T})}}$. The main idea of path integral control is to compute the expectation

using sampling-based methods, such as Monte Carlo simulations. In principle, function $\ell:{\Omega\rightarrow{\mathbb{R}}}$ can be any arbitrary real-valued function. A well-known drawback of Monte Carlo (MC) integration is its high variance.

Importance sampling The goal of importance sampling in MC techniques is to minimize the variance in the MC estimation of integration, ${{\mathbb{E}}_{\mathcal{Q}}{\lbrack{\ell{({\mathbf{X}})}}\rbrack}} = {{\mathbb{E}}_{\mathcal{P}}{\lbrack{\ell{({\mathbf{X}})}\frac{d\mathcal{Q}}{d\mathcal{P}}}\rbrack}}$. To reduce the variance, we want to find a probability measure $\mathcal{P}$ on $(\Omega,\mathcal{F})$ with which an unbiased MC estimate for $\rho$ is given by

where the $i$th sampled path ${\mathbf{X}}_{i}$ is generated from density $\mathcal{P}$, denoted by ${\mathbf{X}}_{i} \sim \mathcal{P}$, for $i = {1,\ldots,N_{s}}$.

Multiple importance sampling Multiple-based probability measures can also be used for the MC estimation.

where ${\mathbf{X}}_{i}^{j} \sim \mathcal{P}^{j}$ for $i = {1,\ldots,N_{s}^{j}}$ and $j = {1,\ldots,N_{p}}$. Here, $N = {\sum_{j = 1}^{N_{p}}N_{s}^{j}}$ is the total number of sampled paths, and the reweighting function $\gamma^{j}:{\Omega\rightarrow{\mathbb{R}}}$ can be any function that satisfies the relation

which guarantees that the resulting MC estimation $\hat{\rho}$ is unbiased. For example, the flat function ${\gamma^{j}{({\mathbf{X}})}} = 1$ for all $\mathbf{X}$ or the balance-heuristic function ${\gamma^{j}{({\mathbf{X}})}} = {N/{\sum_{k = 1}^{N_{p}}{N_{s}^{j}\frac{d\mathcal{P}^{k}}{d\mathcal{P}^{j}}{({\mathbf{X}})}}}}$ can be employed.

### IV-B Cross entropy method for PI: KL control

The well-known cross-entropy (CE) method, which was originally invented for derivative-free optimization, can also be applied to trajectory generation by computing the following information theory optimization:

where the importance weight is defined as:

where $\overset{\sim}{\pi}$ is the baseline Markov policy. In addition, rewriting the cost function in the fourth row of as ${J^{\pi}{({\mathbf{X}})}}:={\omega^{\pi}{({\mathbf{X}})}{\ln\omega^{\pi}}{({\mathbf{X}})}}$, we have the following expectation minimization:

Alg. 1 summarizes the iterative procedures of CE for motion planning to solve the optimization problem using a sampling-based method.

1:Input: K: Number of samples
3:π0: Initial (trial) policy
4:while not converged do
5: Sample trajectories {X1, ⋯, XK} from 𝒫πi.
6: Determine the elite set threshold: γi = Jπi(Xκ)
7: where κ denotes the index of the Ke best
9: Compute the elite set of sampled-trajectories:
11: Update the policy:
12: $\pi^{i + 1} = {{\arg{\min\limits_{\pi}\frac{1}{|\mathcal{E}_{i}|}}}{\sum\limits_{{\mathbf{X}}_{k} \in \mathcal{E}_{i}}{J^{\pi}{({\mathbf{X}}_{k})}}}}$

### Remark

For expectation minimization in and Alg. 1, it is common to use a parameterization of the control policy $\pi$ or the resulting trajectory distribution $\mathcal{P}^{\pi}$ which can be rewritten as ${\mathcal{P}^{\pi}{(\mathbf{X})}} = {\mathcal{P}{(\mathbf{X};\theta)}}$. This parameterization results in a finite-dimensional optimization. $\square$

### IV-C MPC-like open-loop controller: MPPI

By applying time discretization with arithmetic manipulations to, the path integral control becomes

where $u$ is the nominal control input and $\delta u$ is the deviation control input for exploration. Here, the expectation is considered with respect to the probability measure $\mathcal{Q}$ of a path corresponding to policy $\pi$.

For implementation, the expectation is approximated using MC importance sampling as follows:

where $K$ is the number of sampled paths, and $G_{t}^{\pi_{k}}$ is the cost-to-go corresponding to the simulated trajectory following policy ${\pi_{k}{(t,x)}} = {{u{(t,x)}} + {\delta u_{k}{(t,x)}}}$ corresponding to the perturbed control inputs for $k = {1,2,\ldots,K}$. This path-integral control based on forward simulations is known as the model-predictive path integral (MPPI). By recursively applying MPPI, the control inputs can approach the optimal points. Alg. 2 summarizes the standard procedures for the MPPI.

1:Input: K: Number of samples
3:(u0,u1,…,uN − 1): Initial control sequence
4:while not terminated do
5: Generate random control variations δu
12: ${\overset{\sim}{u}}_{i,k} = {u_{i} + {\delta u_{i,k}}}$
18: $G_{i,k} = {G_{{i + 1},k} + {{\mathtt{c}\mathtt{o}\mathtt{s}\mathtt{t}}{(x_{i},{\overset{\sim}{u}}_{i,k})}}}$
22: $w_{i,k} = \frac{\exp{({- {G_{i,k}/\lambda}})}}{\sum_{\kappa = 1}^{K}{\exp{({- {G_{i,\kappa}/\lambda}})}}}$
23: $u_{i}\leftarrow{u_{i} + {\sum_{k = 1}^{K}{w_{i,k}\delta u_{i,k}}}}$
29: Update xinit, tinit by measurement
Algorithm 2 MPPI_control

### IV-D Parameterized state feedback controller

Although MPC-like open-loop control methods are easy to implement, they exhibit certain limitations. First, it can be inefficient for high-dimensional control spaces because a longer horizon results in a higher dimension of the decision variables. Second, it does not design a control law (i.e., policy), but computes a sequence of control inputs over a finite horizon, which means that whenever a new state is encountered, the entire computation should be repeated. Although a warm start can help solve this problem, it remains limited. Third, the trade-off between exploitation and exploration is not trivial.

As an alternative to open-loop controller design, a parameterized policy or control law can be iteratively updated or learned via model-based rollouts, from which the performance of a candidate policy of parameterization is evaluated, and the parameters are updated to improve the control performance. The main computation procedure is that from an estimate of the probability $P{(\left. {\mathbf{X}} \middle| x_{0} \right.)}$ of the sampled trajectories, we want to determine a parameterized policy $\pi_{t}{(\left. u_{t} \middle| {x_{t};\theta_{t}} \right.)}$ for each time $t < T$ that can reproduce the trajectory distribution $P{(\left. {\mathbf{X}} \middle| x_{0} \right.)}$, where $\theta_{t} \in \Theta$ denotes the parameter vector that defines a feedback policy $\pi_{t}$. In general, a feedback policy can be time varying, and if it is time invariant, then the time dependence can be removed; that is, $\theta = \theta_{t}$ for all times $t \in {\lbrack 0,T\rbrack}$. In this review paper, we consider only deterministic feedback policies, but the main idea can be trivially extended to probabilistic feedback policies^22^2An example of probabilistic feedback policy parameterization is a time-dependent Gaussian policy that is linear in the states, ${\pi_{t}{(\left. u_{t} \middle| {x_{t};\theta_{t}} \right.)}} \sim {\mathcal{N}{(\left. u_{t} \middle| {{k_{t} + {K_{t}x_{t}}},S_{t}} \right.)}}$, in which the parameter vector is $\theta_{t} = {(k_{t},K_{t},S_{t})}$ and updated by a weighted linear regression and the weighted sample-covariance matrix..

Linearly parameterized state feedback Consider

where $h:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n_{p}}}$ is a user-defined feature of the state feedback control law. Using the model-based forward simulations, a control parameter update rule can be applied as follows:

where $w_{k} = \frac{\exp\left( {- {\frac{1}{\lambda}G_{t}^{\pi_{k}}}} \right)}{\sum_{\kappa = 1}^{K}{\exp\left( {- {\frac{1}{\lambda}G_{t}^{\pi_{\kappa}}}} \right)}}$ is the weight for the $k$th sampled perturbation-parameter $\delta\theta_{k}$ of the linearly parameterized control law and ${\pi_{k}{(t,x)}} = {h{(x,t)}^{\top}{({\theta + {\delta\theta_{k}}})}}$ is the test or the exploration (search) policy.

Nonlinearly parameterized state feedback Consider

where the state-feedback control law is parameterized by the control parameter $\theta \in {\mathbb{R}}^{n_{p}}$. Using the model-based forward simulations, a control parameter update rule can be applied as follows:

where the weight is defined as follows:

with the weight $w_{k} = \frac{\exp\left( {- {\frac{1}{\lambda}G_{t}^{\pi_{k}}}} \right)}{\sum_{\kappa = 1}^{K}{\exp\left( {- {\frac{1}{\lambda}G_{t}^{\pi_{\kappa}}}} \right)}}$ and the exploration policy $\pi_{k} = {\pi{(t,x;{\theta + {\delta\theta_{k}}})}}$. Here, ${\lbrack \cdot \rbrack}^{\dagger}$ denotes the pseudoinverse.

### Remark (CE method for policy improvement)

Parameterized state feedback controls, such as and, can also be updated using CE methods. For example, ${\delta\theta_{k}} \sim {\mathcal{G}P{(0,\Sigma)}}$ is samples, the cost of simulated trajectories is evaluated with control parameters $\theta_{k} = {\theta + {\delta\theta_{k}}}$ for $k = {1,\ldots,K}$, the samples are sorted in ascending order according to the simulated costs, and the parameter is updated by weighted-averaging the sampled parameters $\delta\theta_{k}$ from the sorted elite set, $\theta\leftarrow{\theta + {{\mathtt{a}\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{a}\mathtt{g}\mathtt{e}}{({\delta\theta_{k}})}_{\mathtt{e}\mathtt{l}\mathtt{i}\mathtt{t}\mathtt{e}}}}$. In general, the covariance $\Sigma$ can be also updated by empirical covariance of the sampled parameters $\delta\theta_{k}$ from the sorted elite set, $\Sigma\leftarrow{\Sigma + {{\mathtt{a}\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{a}\mathtt{g}\mathtt{e}}{({\delta\theta_{k}\delta\theta_{k}^{\top}})}_{\mathtt{e}\mathtt{l}\mathtt{i}\mathtt{t}\mathtt{e}}}}$. $\square$

### IV-E Policy improvement with path integrals

Policy improvement with path integrals (PI$^{2}$) is presented in. The main idea of PI$^{2}$ is to iteratively update the policy parameters by averaging the sampled parameters in weights with the costs of the path integral corresponding to the simulated trajectories. Alg. 3 shows the pseudocode for the PI$^{2}$ Covariance Matrix Adaptation (PI$^{2}$-CMA) proposed in based on the CMA evolutionary strategy (CMAES). In, the PI$^{2}$-CMA was compared with CE methods and CMAES in terms of optimality, exploration capability, and convergence rate. Skipping the covariance adaptation step in Alg. 3 yields a vanilla PI$^{2}$. In, it was also shown that policy improvement methods based on PI$^{2}$ would outperform existing gradient-based policy search methods such as REINFORCE and NAC.

1:Input: K: Number of samples
4:while not terminated do
5: Generate random variables θi, k ∼ 𝒢P(θ,Σ)
6: Generate random initial conditions xinit
23: $w_{i,k} = \frac{\exp{({- {G_{i,k}/\lambda}})}}{\sum_{\kappa = 1}^{K}{\exp{({- {G_{i,\kappa}/\lambda}})}}}$
24: $\theta_{i} = {\sum_{k = 1}^{K}{w_{i,k}\theta_{i,k}}}$
25: $\Sigma_{i} = {\sum_{k = 1}^{K}{w_{i,k}{({\theta_{i,k} - \theta})}{({\theta_{i,k} - \theta})}^{\top}}}$
27: $\theta\leftarrow{\sum_{i = 0}^{N - 1}{\frac{N - i}{\sum_{j = 0}^{N - 1}{({N - j})}}\theta_{i}}}$
28: $\Sigma\leftarrow{\sum_{i = 0}^{N - 1}{\frac{N - i}{\sum_{j = 0}^{N - 1}{({N - j})}}\Sigma_{i}}}$

## Python and MATLAB Simulation Results

This section presents the simulation results of two different trajectory optimization problems: 1D cart-pole trajectory optimization and bicycle-like mobile robot trajectory tracking. The first case study demonstrates the simulation results for the cart-pole system, followed by the second numerical experiment showing the local trajectory tracking of a bicycle-like mobile robot with collision avoidance of dynamic obstacles^33^3Videos of simulation results are available at • [https://youtu.be/zxUN0y23qio](https://youtu.be/zxUN0y23qio) • [https://youtu.be/LrYvrgju_o8](https://youtu.be/LrYvrgju_o8). The details of the simulation setups and numerical optimal control problems are not presented here because of limited space, but they are available in the accompanying github page^44^4[https://github.com/iASL/pic-review.git](https://github.com/INHA-Autonomous-Systems-Laboratory-ASL/MATLAB-Simulation-An-Overview-of-Recent-Advances-in-Path-Integral-Control.git).

### V-A Cart-pole trajectory optimization

In this section, we consider trajectory optimization for set-point tracking in a one-dimensional (1D) cart-pole system. This system comprises an inverted pendulum mounted on a cart capable of moving along a unidirectional horizontal track. The primary goal is to achieve a swing-up motion of the pole and subsequently maintain its stability in an upright position through horizontal movements of the cart. We considered a quadratic form for the cost function associated with each state variable. To address this challenge of stabilizing a cart-pole system, we implemented several path integral methods including CEM, MPPI, and PI$^{2}$-CMA delineated in Algs. 1, 2, and 3, and investigated their performances with comparison to nonlinear model predictive control (NMPC).

Simulations are performed in Python environments. Fig. 4 illustrates the controlled trajectories of the cart-pole system under various control strategies. Fig. 4 depicts the force inputs derived from the application of each control method. These results demonstrate the effectiveness of the path integral control methods in achieving the desired control objectives for the cart-pole system. The comparative analysis of our results reveals distinct characteristics and performance efficiencies among the different path integral control methods. MPPI and CEM methods achieved better performance of stabilizing the pole as compared to NMPC and PI$^{2}$-CMA. Upon fine-tuning optimization parameters, MPPI achieved faster convergence in pole stabilization than CEM, given the same prediction horizon and sample size. Such enhanced performance of MPPI is further corroborated by its superior cost-to-go metrics, as shown in Fig. 4.

This comparison of four different PI-based control strategies stabilizing a cart-pole system reveals notable characteristics. CEM and MPPI result in smooth trajectories of the cart-pole position and lower accumulated cost-to-go, indicating better energy efficiency. In contrast, PI$^{2}$-CMA and NMPC result in more aggressive control input sequences with faster responses and larger overshoots in velocities, which might increase energy use and hasten actuator degradation. However, CEM and MPPI show higher rate of input changes, which would not be desirable for real hardware implementations. Of course, this jerking behavior of control actions can be relaxed by putting rate or ramp constraints in control inputs. The appropriate choice among these PI-based control strategies would heavily depend on the specific demands of the application, balancing multiple objectives such as efficiency, responsiveness, and operational durability.

Figure 2: Controlled trajectories of the 1D cart-pole using different methods of path integral control (CEM, MPPI,PI2-CMA) in comparison with nonlinear model predictive control (NMPC).
Figure 3: Control inputs resulting from different methods of path integral control (CEM, MPPI,PI2-CMA) and NMPC.
Figure 2: Controlled trajectories of the 1D cart-pole using different methods of path integral control (CEM, MPPI,PI2-CMA) in comparison with nonlinear model predictive control (NMPC).
Figure 3: Control inputs resulting from different methods of path integral control (CEM, MPPI,PI2-CMA) and NMPC.
Figure 4: Cost-to-go associated with different methods of path integral control (CEM, MPPI,PI2-CMA) and NMPC.

### V-B Path planning for bicycle-like mobile robot

The robot system we consider in this section is a mobile robot navigating in an environment with obstacles, aiming to follow a predefined path while avoiding collisions and staying inside a track. To evaluate the effectiveness of an MPPI controller for real-time trajectory generation with obstacle avoidance, we conducted a series of MATLAB simulations where two moving obstacles are considered in the 2D coordinates.

We implemented the MPPI controller described in Alg. 2 for bicycle-like mobile robot navigation over a track. Fig. 6 shows the robot's trajectory tracking while avoiding moving obstacles. Fig. 6 shows the forward and angular velocities of the robot required to follow the desired path by avoiding obstacles, which assesses the effectiveness of the controller in avoiding obstacles. The results demonstrated that the MPPI controller achieved successful trajectory generation and tracking, while effectively avoiding dynamic obstacles. Throughout the simulation of mobile robot path planning, MPPI controller showed robust obstacle avoidance capabilities, successfully navigating around obstacles, and minimizing the distance with its reference.

Figure 5: A capture of simulating local path planning and tracking with obstacle avoidance using an MPPI controller. An associated video of simulations is available at https://youtu.be/LrYvrgju_o8.
Figure 5: A capture of simulating local path planning and tracking with obstacle avoidance using an MPPI controller. An associated video of simulations is available at https://youtu.be/LrYvrgju_o8.
Figure 6: Forward and angular velocity trajectories resulting from a MPPI-based controller steering a bicycle-like mobile robot.

## MPPI-based Autonomous Mobile Robot Navigation in ROS2/Gazebo Environments

In this section, we consider two ROS2/Gazebo simulations of MPPI-based autonomous mobile robot navigation in a cafeteria environment and in a maze. We implement various path integral algorithms including MPPI, Smooth MPPI, and Log MPPI to enhance navigation and control in these complex scenarios. The SLAM toolbox is employed for mapping while Navigation2 (NAV2) is used for navigation within the ROS2 Gazebo simulation environment. These path integral control approaches are attractive because they are derivative-free and can be parallelized efficiently on both CPU and GPU machines. The simulations are conducted using a computing system equipped with Intel Core i7 CPU and NVIDIA GeForce RTX 3070 GPU. These simulations are executed within the Ubuntu 22.04 operating system, leveraging the ROS2 Humble simulation platform for comprehensive analysis. The following subsections provide the details of the simulation setups and results of different MPPI-based path planning algorithms in two different scenarios. The simulation frameworks and source codes used in this study are publicly available^55^5[https://github.com/iASL/pic-review.git](https://github.com/INHA-Autonomous-Systems-Laboratory-ASL/MATLAB-Simulation-An-Overview-of-Recent-Advances-in-Path-Integral-Control.git).

### VI-A Autonomous robot navigation in a cafeteria environment

In this subsection, we present the simulation results of the autonomous robot navigation using different MPPI-based path planning algorithms in a cafeteria environment. The primary objective of this ROS2/Gazebo simulation is to evaluate the performance of MPPI-based path planning algorithms for a task of navigating an indoor autonomous mobile robot serving foods at different tables while avoiding obstacles in a confined and dense indoor space.

### VI-A1 Experiment setup

For the autonomous indoor robot navigation scenario, we utilize an autonomous mobile robot equipped with the necessary sensors such as a LiDAR and a camera for environmental perception. The cafeteria environment is designed using a Gazebo, accurately replicating the challenges of indoor navigation, including cluttered spaces, narrow passages, and obstacles along a path generated by a global planner, such as NavFn, as shown in Fig. 9. All three path integral controllers run in a receding-horizon fashion with $100$-time steps of prediction horizon where each time-step corresponds to $0.1$ sec. The number of control rollouts is $1024$ and the number of sampled traction maps is $2000$ at the rate of $30$ Hz. It can also replan at $30$ Hz while sampling new control actions and maps.

Figure 7: ROS2/Gazebo simulation navigating an autonomous mobile robot in a cafeteria environment for which MPPI, Smooth MPPI, and Log MPPI are applied as local controllers.
Figure 8: Performance comparison of path integral controllers in terms of the longitudinal position (x).
Figure 7: ROS2/Gazebo simulation navigating an autonomous mobile robot in a cafeteria environment for which MPPI, Smooth MPPI, and Log MPPI are applied as local controllers.
Figure 8: Performance comparison of path integral controllers in terms of the longitudinal position (x).
Figure 9: Performance comparison of path integral controllers in terms of the orientation (θ).

In the simulated cafeteria scenario demonstrating the navigational efficiency in a dynamic service environment, as shown in Fig. 9, the robot is tasked to navigate a series of waypoints representing a service cycle. Commencing from the home coordinates $({{x = {- 5}},{{y = 0.51},{\theta = 0.01}}})$, the robot is required to proceed to the order-taking waypoint $({{x = {- 4.85}},{{y = {- 3.0}},{\theta = 0.01}}})$. Subsequently, it traverses to serve table 2 at the coordinates $({{x = 4.29},{{y = 2.64},{\theta = 0.01}}})$ and upon order collection, returned to the order-taking waypoint. The mission is completed when the robot serves table 3 at the coordinates $({{x = {- 0.6}},{{y = {- 1.99}},{\theta = 0.01}}})$ and returns to the order-taking location. The total navigational distance required for the service unit to traverse, beginning from its home location, involves a multi-point itinerary. Initially, it must travel to the order point, followed by a journey to table 2. Afterwards, it returns to the order point, from where it proceeds to serve table 3, and subsequently returns to the order-taking point. This entire route encompasses a distance of approximately 43.15 meters.

### VI-A2 Simulation results

The simulation results of autonomous robot navigation in a cafeteria environment are given in Fig. 9 and the accompanying video^66^6[https://youtu.be/3VChYScJ7oA](https://youtu.be/3VChYScJ7oA), to illustrate and compare the effectiveness of the three path integral controllers, MPPI, Smooth MPPI, and Log MPPI. In the simulated hotel navigation task, the performance of an autonomous delivery robot is evaluated using the NavFn global planner, in conjunction with three local planners: MPPI, Smooth MPPI, and Log MPPI. Figs. 9 and 9 demonstrate the longitudinal position and orientation tracking of the robot pose over time.

In the Gazebo simulations captured in Fig. 9, all three path integral controllers demonstrate remarkable indoor navigation capabilities for the differential-driving mobile robot, Turtlebot3. All three MPPI-based mobile robot navigation result in in smooth trajectory tracking while effectively avoiding obstacles and collisions in crowded café environments. Fig. 9 shows the performance of the robot's positional components plotted over time. Each trajectory---MPPI (red line), Smooth MPPI (dark blue line), and Log MPPI (yellow line)---is compared against the ground truth (dotted_light red, dotted dark blue, and dotted green lines respectively). Despite slight deviations, the path integral controllers maintained a closely matched orientation with the ground truth, signifying robust direction control. Fig. 9 shows the robot's orientation $(\theta)$ as guided by the NavFn global planner with the three local planners. Similar to Fig. 9, the tracking performance of the three algorithms is compared against the ground truth. In Figs. 9 and 9, the legends positioned in the top right corner display the Robot Operating System (ROS) topics pertaining to the robot's odometry and Gazebo ground truth data.

In the simulation study shown in Figs. 9, 9, and 9, all MPPI-based path integral algorithms demonstrated high precision in trajectory tracking. Notably, Smooth MPPI (represented by a dark blue line) maintained a trajectory closest to the ground truth, especially in the simulation's latter stages. While MPPI excelled in speed, taking less time, it exhibited higher positional and angular errors compared to Smooth MPPI and Log MPPI. Log MPPI required marginally more time than Smooth MPPI. However, in terms of both positional accuracy and angular orientation, Smooth MPPI outperformed both Log MPPI and MPPI. This highlights Smooth MPPI's superior balance of speed and precision in trajectory tracking in a cafeteria environment.

### VI-B Autonomous robot navigation in maze-solving environment

In this subsection, we detail the simulation outcomes of utilizing the different path integral controllers for the navigation of the robot in a maze-solving environment. The primary goal of a maze-solving robot is to autonomously navigate through a labyrinth from a starting point to a designated endpoint in the shortest time possible. It must efficiently map the maze, identify the optimal path, and adjust to obstacles using its onboard sensors and algorithms.

### VI-B1 Experimental setup

In our experiment, a simulated maze-solving robot was deployed in a ROS2/Gazebo environment, equipped with LiDAR and IMU sensors for navigation. The robot utilized the NavFn global planner for overall pathfinding and local controllers including MPPI, Smooth MPPI, and Log MPPI for fine-tuned maneuvering. Performance was assessed based on the robot's ability to discover the most efficient path to the maze center, measuring metrics such as completion time and path optimality. The path integral controllers ran in a receding-horizon fashion with 100-time steps; each step was 0.1 s. The number of control rollouts was 1024, and the number of sampled traction maps was 2000 at a rate of 30 Hz. It could also replan at 30 Hz while sampling new control actions and maps. The computational overhead of these algorithms remained reasonable, thereby ensuring real-time feasibility for practical applications.

In the simulated cafeteria scenario, as shown in Fig. 12, the autonomous robot was programmed to navigate from an initial location at coordinates $({{x = {- 5.18}},{{y = {- 6.58}},{\theta = 0.99}}})$ to a predetermined destination $({{x = 6.25},{{y = {- 1.47}},{\theta = 0.99}}})$. The cumulative distance from the starting home location to the designated end point is approximately 26.28 meters. The objective was to optimize the route for the shortest transit time, showcasing the robot's pathfinding proficiency in a complex simulated labyrinth.

Figure 10: ROS2/Gazebo simulation navigating an autonomous mobile robot in a maze-solving environment for which MPPI, Smooth MPPI, and Log MPPI are applied as local controllers.
Figure 11: Performance comparison of path integral controllers in terms of the longitudinal position (x).
Figure 10: ROS2/Gazebo simulation navigating an autonomous mobile robot in a maze-solving environment for which MPPI, Smooth MPPI, and Log MPPI are applied as local controllers.
Figure 11: Performance comparison of path integral controllers in terms of the longitudinal position (x).
Figure 12: Performance comparison of path integral controllers in terms of the orientation (θ).

### VI-B2 Simulation results

For the maze-solving task, the robots were similarly directed by the NavFn global planners, with the local planning algorithms tested for their path optimization efficiency. In the ROS2/Gazebo simulation, the maze-solving robot successfully navigated to the maze's center, with the NavFn global planner and MPPI local controller achieving the most efficient path in terms of time and distance. The Smooth MPPI and Log MPPI controllers also completed the maze with competitive times, demonstrating effective adaptability and robustness in pathfinding within the complex simulated environment. Fig. 12 and a simulation video^77^7[https://youtu.be/GyKDP3-NYA0](https://youtu.be/GyKDP3-NYA0) demonstrate the efficacy of the path integral controllers in navigating the maze-solving environment.

TABLE IV: Comparative performance metrics of different path integral controllers across different environments

Fig. 12 illustrates the robot's orientation in a maze-solving environment. The ground truth data (dotted lines) represents the ideal orientation path for maze navigation. It is evident from the graph that the Smooth MPPI (green line) and Log MPPI (blue line) algorithms maintained a consistent orientation close to the ground truth, while the MPPI (red line) displayed marginally increased variance. The robot's $x$-position component within in maze-solving environment is shown in Fig. 12, in which the ground truth path (dotted line) is tightly followed by all three algorithms. The Smooth MPPI (red line) and Log MPPI (green line) displayed almost identical performance, with MPPI (blue line) showing slight divergence yet still within an acceptable range for effective maze navigation. In evaluating speed and time efficiency, MPPI demonstrated superior performance, achieving the goal more swiftly compared to Log MPPI and Smooth MPPI. In Fig. 12, the legend in the top left corner illustrates the ROS topics of the robot's odometry, whereas in Fig. 12, the top right corner legend presents the ROS topics associated with Gazebo ground truth data.

The simulation results demonstrate that all considered path integral algorithms MPPI, Smooth MPPI, and Log MPPI perform robustly in trajectory optimization tasks for both hotel navigation and maze-solving scenarios. The angular orientation and position tracking graphs indicate that each algorithm is capable of closely following a predetermined ground truth trajectory with minimal deviation. However, minor differences in performance suggest that certain algorithms may be more suitable for specific applications, as given in Table IV. For instance, Log MPPI and Smooth MPPI's trajectory in the hotel navigation simulation suggests a potential for finer control in more predictable environments like cafeteria or warehouse environments, whereas MPPI showed promising results in the more dynamic and fast speed tracks or environments like maze-solving context or F1Tenth racing car competitions.

## Discussion and Future Directions

### VII-A Policy parameterization

There are multiple ways of policy parameterizations for state-feedback. For example, linear policies, radial basis function (RBF) networks, and dynamic movement primitives (DMPs) have been commonly used for policy representations and search in robotics and control.

Note that because the PI-based control and planning algorithms presented in Section IV are derivative-free, complex policy parameterization and optimization can be implemented without any additional effort (e.g., numerical differentiation computing gradients, Jacobians, and Hessians). This is one of the advantageous characteristics of sampling-based policy search and improvement methods such as PI.

### VII-B Path integral for guided policy search

The guided policy search (GPS), first proposed in, is a model-free policy-based reinforcement learning (RL). Pixel-to-torque end-to-end learning of visuomotor policies has recently become popular for RL in robotics. Compared with direct deep reinforcement learning, GPS has several advantages, such as faster convergence and better optimality. In the GPS, learning consists of two phases. The first phase involves determining a local guiding policy, in which a training set of controlled trajectories is generated. In the second phase, a complex global policy is determined via supervised learning, in which the expected KL divergence of the global policy from the guiding policy is minimized. The goal of the GPS framework is to solve an information-theoretic-constrained optimization of the following:

where the KL divergence $D_{KL}{({{\beta{({\mathbf{X}})}} \parallel {\pi{({\mathbf{X}};\theta)}}})}$ can be rewritten as:

A baseline (Markovian) policy $\beta{(\left. u_{i} \middle| x_{i} \right.)}$ is a local guiding policy used to generate sampled trajectories starting with a variety of initial conditions. A parameterized policy $\pi{(\left. u_{i} \middle| {x_{i};\theta} \right.)}$ is a high-dimensional global policy learned based on the sampled trajectories generated from the baseline policy $\beta$ in a supervisory manner by minimizing the KL divergence from the local policy.

The iterative procedure for a general GPS can be summarized as follows:\
*(Step 1)* Given $\hat{\theta}$, solve

*(Step 2)* Given $\hat{\beta}$, solve

*(Step 3)* Check convergence and repeat Steps 1 and 2 until a convergence criterion is satisfied.

Various methods have been considered to guide GPS policies. For example, gradient-based local optimal control methods such as DDP and iLQR and sampling-based local approximate optimal control methods such as PI and PI$^{2}$ can be used. Among others, we claim that because of their efficiency in exploration and fast convergence rate, PI-based sampling methods could be more appropriate as guiding policies for GPS.

### VII-C Model-based reinforcement learning using PI-based policy search and optimization

In control and robotics, model-based reinforcement learning (MBRL) has been widely investigated because of the potential benefits of data efficiency, effective exploration, and enhanced stability, compared to model-free RL. It is natural to consider methods of path integral control for policy search and optimization in MBRL. The most well-known method of MBRL is the Dyna algorithm that consists of two iterative learning steps: The first step is to collect data by applying the current policy and learn dynamics model. The second step is to learn or update parameterized policies with data generated from the learned model. The second step alone is known as model-based policy optimization (MBPO) that is particularly related to PI-based policy search and optimization. In other words, parameterized policies discussed in Sections IV-D, IV-E, and VII-A can be improved by using sampling-based path integral control methods for MBRL and MRPO.

### VII-D Sampling efficiency for variance reduction

Let us consider the importance weight defined in. Note that if the training policy $\pi$ is optimal, then all simulated trajectories have the same weight. To measure the quality of the sampling strategy, the effective sampling size (ESS) defined as

measures the variance of the importance weights and can be used to quantify the efficiency of a sampling method. A small ESS implies that the associated back-end tasks of estimation or control may result in a large variance. The most important sampling strategies suffer from decreasing ESS over time during prediction. Therefore, quantifying or approximating the ESS of a base-sampling strategy is a major problem in the application of path integral control.

### VII-E Extensions to multi-agent path planning

In the literature, there are only a few studies that extend PI control to the stochastic control of multi-agent systems (MASs): path integrals for centralized control, distributed control, and a two-player zero-sum stochastic differential game (SDG). A linearly solvable linearly solvable PI control algorithm is proposed for a networked MAS in and extended to safety-constrained cooperative control of MASs using the control barrier function (CBF) in which the barrier state augmented system is defined to take care of potential conflicts between control objectives and safety requirements.

In path planning and control for multi-agent systems, it is common to assume that dynamics are independent but costs are interdependent. Consider the cost-to-go function defined for agent $a$ as

where ${\overline{\pi}}_{a} = {(\pi_{a},\pi_{\nu{(a)}})}$ is the joint policy of the ego agent $a$ and its neighbourhood agent $\nu{(a)}$. Similarly the joint state and trajectory are defined as ${\overline{X}}_{a,s} = {(X_{a,s},X_{{\nu{(a)}},s})}$ and ${\overline{\mathbf{X}}}_{a,t} = {({\overline{X}}_{a,s})}_{s = t}^{T} = {(X_{a,s},X_{{\nu{(a)}},s})}_{s = t}^{T}$.

As we have observed throughout this paper for single-agent cases, from an algorithmic point of view, the most important computation is to approximate the weights corresponding to the likelihood ratios using MC sampling methods. Similarly, policy updates or improvements in multi-agent systems can be

where the probability weight is defined as

for which randomly perturbed policies $\pi_{a,k} = {\pi_{a} + {\delta\pi_{a,k}}}$ are used to simulate the controlled trajectories and compute the associated costs $G_{a,t}^{(\pi_{a,k},\pi_{\nu{(a)}})}$. Here, the learning process is assumed to be asynchronous, in the sense that the policies of the neighborhood agents $\nu{(a)}$ are fixed when updating the policy for agent $a$ in accordance with the simulation of the augmented trajectories ${\overline{\mathbf{X}}}_{a}$. Here, the individual agent's policy can be either MPC-like open-loop (feedforward) control inputs or parameterized (deterministic or stochastic) state-feedback controllers.

### VII-F MPPI for trajectory optimization on manifolds

Trajectory optimization using differential geometry is very common in robotics and has been studied under manifolds such as special orthogonal and Euclidean groups ${SO}{}$ and ${SE}{}$. In, gradient-based sequential convex programming on manifolds was used for trajectory optimization. It was expected that many theoretical and computational frameworks for the optimization of manifolds could be applied to robotic trajectory optimization.

Applying methods of sampling-based path integral control such as MPPI to trajectory optimization on manifolds is not trivial because it requires effective accelerated approaches to generate the sampled trajectories on manifolds and sampling trajectories on manifolds with kinematic constraints are not trivial. Thus, one could employ the methods used for unscented Kalman filtering on manifolds (UKF-M). We leave this research topic of sampling-based path integral control for trajectory optimization on manifolds for potential future work.

### VII-G Motion planning for mobile robots and manipulators

While policy parameterization discussed in Section VII-A has shown great success in robotic manipulators and locomotion control, policy parameterization is not trivial and even not appropriate for path planning or trajectory optimization for autonomous mobile robots. This is because optimal trajectory should be determined by considering the relative pose of the robot with respect to the obstacles and the goal pose as well as the robot's ego-pose. Such relative poses can be encoded into the associated optimal control problem (OCP) as constraints and feasibility of the OCP with a parameterized policy is hard to be guaranteed for mobile robot dynamic environment. This brings us a conclusion that it is more appropriate to use the MPC-like open-loop control inputs for trajectory optimization of mobile robots, which implies that MPPI and its variations would become more successful with autonomous mobile robot navigation than PI$^{2}$-based policy search and optimization.

## Conclusions

In this paper, we present an overview of the fundamental theoretical developments and recent advances in path integral control with a focus on sampling-based stochastic trajectory optimization. The theoretical and algorithmic frameworks of several optimal control methods employing the path integral control framework are provided, and their similarities and differences are reviewed. Python, MATLAB and ROS2/Gazebo simulation results are provided to demonstrate the effectiveness of various path integral control methods. Discussions on policy parameterization and optimization in policy search adopting path integral control, connections to model-based reinforcement learning, efficiency of sampling strategies, extending the path integral control framework to multi-agent optimal control problems, and path integral control for the trajectory optimization of manifolds are provided. We expect that sampling-based stochastic trajectory optimization employing path integral control can be applied to practical engineering problems, particularly for agile mobile robot navigation and control.
