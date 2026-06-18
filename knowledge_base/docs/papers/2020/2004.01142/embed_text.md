## Introduction

Motion planning algorithms generate optimal open-loop trajectories for robots to follow; however, any uncertainty in the system can potentially drive the robot far away from the desired path. For instance, quadrotors experience blade-flapping and induced drag forces that are dependent on the velocity, ground effects that are dependent on the altitude, and external wind effects that are often unaccounted for by the motion planner,. Accurate modeling of these uncertainty effects on system dynamics can be very expensive and time-consuming. A widely accepted approach to account for uncertainty in motion planning is through feedback \[2, Chapter 8\]. In practice, ancillary tracking controllers or model predictive control (MPC) schemes are employed to alleviate this problem. However, the presence of the uncertainties is not explicitly considered in the control design process, and instead the performance is achieved with hand-tuned controller parameters and experimental validation. Without valid safety certificates, the uncertainty might drive the system unstable and far enough away from the desired trajectory, resulting in collisions with obstacles, Fig. 1a.

Robust trajectory tracking controllers using classical Lyapunov stability theory have been designed for helicopters, hovercraft, marine vehicles, and several other autonomous robots, which exhibit nonlinear behavior. These approaches rely on backstepping techniques, sliding-mode control, passivity-based control, or other robust nonlinear control design tools \[6, Chapter 14\]. However, the classical methods do not provide a 'one size fits all' procedure for the constructive design of tracking controllers for a large class of nonlinear systems. Unless the problem has a very specific structure that can be exploited, a control Lyapunov function (CLF) has to be found which can be prohibitively difficult for general nonlinear systems because the feasibility conditions do not appear as linear matrix inequalities (LMI), unlike in case of linear systems.

Advances in computational resources and optimization toolboxes available to autonomous robots have led to active developments in the field of robust MPC. The two large classes of methods of interest are min-max MPC and tube-based MPC. Min-max MPC approaches consider the worst-case disturbance that can affect the system making them overly conservative. If the uncertainty is too large or the robot is planning over a long horizon, a min-max MPC based approach may even render the optimization infeasible. Tube-based MPC methods address these issues by employing an ancillary controller to attenuate disturbances and ensure that the robot stays inside of a 'tube' around the desired trajectory. However, with the exception of, these methods assume the existence of a stabilizing ancillary controller and its region of attraction along the desired trajectory. Moreover, the resulting tubes are of fixed width, which may be overly conservative depending on the operating conditions (see Fig. 1b). This issue is partly addressed for feedback linearizable systems in by using sliding-mode boundary layer control to construct tubes of any desired size during the MPC optimization procedure. Furthermore, unlike classical methods, the MPC-based approaches while applicable to larger class of systems incur a heavy computational load and are not always amenable to real-time applications.

Figure 1: Although the planned path is collision free (purple), the robot’s actual trajectory (dashed-blue) might lead to a collision with the obstacles (gray) in the environment due to model discrepancies or external disturbances. (b) A feedback policy ensures that the robot stays inside of the (orange) tube which is too wide to pass between the obstacles without colliding (c) The safe feedback controller proposed in this paper guarantees that the robot’s trajectory never escapes the tube, which itself is also collision-free.

Contraction theory-based approaches bridge the gap between classical and optimization-based methods, and provide a constructive control design procedure for nonlinear systems. In, the authors introduce contraction analysis as tool for studying stability of nonlinear systems using differential geometry. In particular, the authors show that the 'contracting' or convergent nature of solutions to nonlinear systems can be derived from the differential dynamics of the system. Since the differential dynamics for nonlinear systems are of linear-time varying (LTV) form, all the results from linear systems theory can be leveraged for nonlinear systems through the contraction analysis framework. In, constructive control design techniques from linear systems theory can be used to find a control contraction metric (CCM), which is analogous to CLFs in the differential framework. This is significantly easier than directly finding the CLFs for nonlinear systems, because the feasibility conditions for CCMs are represented as LMIs. In, a design procedure for synthesizing CCM-based controllers is given, which induces fixed-width tubes in the presence of bounded external disturbances, excluding modeling uncertainties. However, as discussed before, fixed-width tubes might result in infeasibility of the problem and result in more work for the planner to find a more conservative path that produces feasible tubes. More recently, in a model reference control architecture in conjunction with CCM-based feedback is proposed for handling uncertainties in the system.

In this paper, we present an approach for safe feedback motion planning for control-affine nonlinear systems that relies on contraction theory-based solution for exponential stabilizability around trajectories and $\mathcal{L}_{1}$-adaptive control for handling uncertainties and providing guarantees for transient performance and robustness. In $\mathcal{L}_{1}$ control architecture, estimation is decoupled from control, thereby allowing for arbitrarily fast adaptation subject only to hardware limitations,. The $\mathcal{L}_{1}$ control has been successfully implemented on NASA's AirStar 5.5% subscale generic transport aircraft model, Calspan's Learjet, and unmmaned aerial vehicles. In, the authors presented the analysis for the $\mathcal{L}_{1}$-adaptive control architecture with nonlinear time-varying reference systems. However, the stabilizability of the nominal nonlinear model and associated safety certificates were simply assumed. In this paper, we present a constructive design of feedback strategy for nonlinear systems using CCMs and $\mathcal{L}_{1}$-adaptive control that provides strong guarantees of transient performance and robustness for a large class of control-affine nonlinear systems. Furthermore, we show how this control architecture induces tubes that can be flexibly changed to ensure safety based on the uncertainty in the system and the environment. In particular, this flexibility is provided by the architecture of the $\mathcal{L}_{1}$-adaptive control by decoupling the control loop from the estimation loop. In this way, the width of the certifiable tubes can be adjusted allowing the safe operation of a robot in tight confines.

The manuscript is organized as follows. The problem statement and the assumptions are provided in Section 2. A brief introduction to contraction theory is provided in Section 3. The proposed controller in presented in Section 4 and the stability analysis of the closed-loop system is provided in Section 5. Finally, in Section 6 the results of numerical experimentation are provided.

### Notation

The notation in this paper follows typical conventions used in the controls and robotics communities, but we list a few operations and terms explicitly in this section. The set of non-negative reals is denoted by ${\mathbb{R}}_{\geq 0}$. The set of real matrices is denoted by ${\mathbb{R}}^{m \times n}$ with dimensions ${m,n} \in {\mathbb{N}}$. The set of real symmetric matrices is denoted by ${\mathbb{S}}^{n} \subset {\mathbb{R}}^{n \times n}$. We denote an $n \times n$ identity matrix by ${\mathbb{I}}_{n}$ and a $m$-column vector of ones by $\mathbb{1}_{m}$. Given any matrix $R \in {\mathbb{R}}^{n \times n}$, $\lbrack R\rbrack_{\mathbb{S}} = {\left( {R + R^{\top}} \right)/2} \in {\mathbb{S}}^{n}$ denotes its symmetric part. The largest and smallest eigenvalue for a square matrix $A$ is denoted by $\overline{\lambda}{(A)}$ and $\underset{¯}{\lambda}{(A)}$ respectively. The positive definiteness of a square matrix $A$ is given by the inequality $A \succ 0$. The smallest non-zero singular value for a matrix $B \in {\mathbb{R}}^{n \times m}$ is denoted by ${\underset{¯}{\sigma}}_{> 0}{(B)}$. We denote the Pontryagin set difference between two sets ${\mathcal{A},\mathcal{B}} \subseteq {\mathbb{R}}^{n}$ as $\mathcal{A} \ominus \mathcal{B}$. The $| \cdot |$ represents the absolute value of a scalar and $\left. \parallel \cdot \parallel \right.$ represents the Euclidean norm for vectors and induced vector norm for matrices, unless otherwise denoted. The Laplace transform and its inverse of a function $f{(t)}$ is denoted by $\mathcal{L}{\lbrack{f{(t)}}\rbrack}$ and $\mathcal{L}^{- 1}{\lbrack{f{(t)}}\rbrack}$ respectively. Given a matrix-valued function ${M{(x)}} \in {\mathbb{R}}^{n \times n}$ and a vector-valued function ${f{(x)}} \in {\mathbb{R}}^{n}$, we denote the directional derivative of $M{(x)}$ with respect to $f{(x)}$ by ${\partial_{f}{M{(x)}}} = {\sum_{i = 1}^{n}{{({\partial{{M{(x)}}/{\partial x_{i}}}})}f_{i}{(x)}}}$, where $f_{i}{(x)}$ is the $i^{th}$ element of $f{(x)}$. We denote by $\mathcal{L}_{\infty}{(\mathcal{S})}$ the set of functions $f:{\mathcal{S} \subset {\mathbb{R}}\rightarrow{\mathbb{R}}^{n}}$ which satisfy ${\left. \parallel f\parallel \right._{\mathcal{L}_{\infty}} = {\sup_{x \in \mathcal{S}}\left. \parallel{f{(x)}}\parallel \right.} < \infty},$ where $\left. \parallel \cdot \parallel \right.$ is a Euclidean norm. Additionally, for any $g \in {\mathbb{R}}\rightarrow{\mathbb{R}}^{n}$ we define the truncated $\mathcal{L}_{\infty}$-norm as ${\left. \parallel g\parallel \right._{\mathcal{L}_{\infty}}^{\lbrack 0,\tau\rbrack} = {\sup_{t \in {\lbrack 0,\tau\rbrack}}\left. \parallel{g{(t)}}\parallel \right.}},$ for some finite $\tau > 0$. We denote by $\mathcal{L}_{1}{(\mathcal{S})}$ the set of functions $f:{\mathcal{S} \subset {\mathbb{R}}\rightarrow{\mathbb{R}}^{n}}$ satisfying ${\left. \parallel f\parallel \right._{\mathcal{L}_{1}} = {\int_{\mathcal{S}}{\left. \parallel{f{(x)}}\parallel \right.{dx}}} < \infty}.$ For any $g \in {\mathcal{L}_{1}{({\mathbb{R}}_{\geq 0})}}$, the truncated $\mathcal{L}_{1}$ norm is defined analogously.

## Problem Statement

We consider systems for which the evolution of dynamics can be represented as

with initial condition ${x{}} = x_{0}$, where ${x{(t)}} \in {\mathbb{R}}^{n}$ is the system state and ${u{(t)}} \in {\mathbb{R}}^{m}$ is the control input. The functions ${f{(x)}} \in {\mathbb{R}}^{n}$ and ${B{(x)}} \in {\mathbb{R}}^{n \times m}$ are known, and ${h{(t,x)}} \in {\mathbb{R}}^{m}$ represents the uncertainties. The unperturbed/nominal dynamics ($h \equiv 0$) are therefore represented as

Consider a desired control trajectory ${u^{\star}{(t)}} \in {\mathbb{R}}^{m}$ and the induced desired state trajectory ${x^{\star}{(t)}} \in {\mathbb{R}}^{n}$ from any planner based on unperturbed/nominal dynamics

Together, $({x^{\star}{(t)}},{u^{\star}{(t)}})$ is referred to as the desired state-input trajectory pair. The planner ensures that the desired state-trajectory $x^{\star}{(t)}$ remains in a compact safe set $\mathcal{X} \subset {\mathbb{R}}^{n}$, for all $t \geq 0$.

The goal is to design a control input $u{(t)}$ so that the state $x{(t)}$ of the uncertain system in remains 'close' to the desired trajectory $x^{\star}{(t)}$ while also ensuring ${x{(t)}} \in \mathcal{X}$, for all $t \geq 0$. In order to rigorously define the notion of 'closeness', we need the following definition:

### Definition 2.1

Given a positive scalar $\rho$ and the desired state trajectory $x^{\star}{(t)}$, $\Omega{(\rho,{x^{\star}{(t)}})}$ denotes the $\rho$-norm ball around $x^{\star}{(t)}$, i.e.

Clearly $\Omega{(\rho,{x^{\star}{(t)}})}$ induces a tube centered around $x^{\star}{(t)}$, where the tube is given by

with $\rho > 0$ as the radius.

The problem under consideration can now be stated as follows: Given the desired trajectory ${x^{\star}{(t)}} \in \mathcal{X}$ and a positive scalar $\rho$, design a control input $u{(t)}$ such that the state of the uncertain system satisfies:

Note the condition that ${\Omega{(\rho,{x^{\star}{(t)}})}} \subset \mathcal{X}$ is dependent on the desired trajectory $x^{\star}{(t)}$ (given by the planner) and the tube width $\rho$ (chosen by the user). To ensure that this control-independent condition is satisfied, we place the following assumption.

### Assumption 2.1

Given the positive scalar $\rho$, the desired state trajectory satisfies ${x^{\star}{(t)}} \in \mathcal{X}_{\rho}$, for all $t \geq 0$, where

### Remark 2.1

The implication of Assumption 2.1 is that if the state trajectory satisfies ${{x{(t)}} - {x^{\star}{(t)}}} \in {\mathcal{B}{(\rho)}}$ and ${x^{\star}{(t)}} \in \mathcal{X}_{\rho}$, for all $t \geq 0$, then the definition of the Pontryagin set difference implies that ${x{(t)}} \in {\Omega{(\rho,{x^{\star}{(t)}})}} \subset \mathcal{X}$, for all $t \geq 0$.

### Assumption 2.2

The desired control/input trajectory satisfies

with the upper bound $\Delta_{u^{\star}}$ known.

Note that the bound $\Delta_{u^{\star}}$ is obtained from the planner, which provides the desired state-input trajectory in. Next, we place assumptions on the boundedness and continuity properties of the system functions and uncertainties.

### Assumption 2.3

The known functions ${f{(x)}} \in {\mathbb{R}}^{n}$ and ${B{(x)}} \in {\mathbb{R}}^{n \times m}$ are bounded and continuously differentiable with bounded derivatives, satisfying

for all $x \in {\mathcal{O}{(\rho)}}$, where $b_{j}{(x)}$ is the $j^{\text{th}}$ column of $B{(x)}$ and the bounds are assumed to be known.

### Assumption 2.4

The uncertainty $h{(t,x)}$ is bounded and continuously differentiable in both $x$ and $t$ with bounded derivatives, satisfying

for all $x \in {\mathcal{O}{(\rho)}}$ and $t \geq 0$, where the bounds are assumed to be known.

### Assumption 2.5

The input gain matrix $B{(x)}$ has full column rank. Furthermore, the Moore-Penrose inverse of $B{(x)}$ defined as ${B^{\dagger}{(x)}} = {\left( {B^{\top}{(x)}B{(x)}} \right)^{- 1}B^{\top}{(x)}}$ satisfies the following bounds

## Preliminaries on Contraction Theory

Contraction theory allows to synthesize feedback laws so that, in the absence of uncertainties, the state of the unperturbed/nominal dynamics in tracks a feasible desired trajectory $x^{\star}{(t)}$. We begin with the notion of universal exponential stabilizability.

### Definition 3.1 (\[18\])

Consider a desired state-input trajectory pair $({x^{\star}{(t)}},{u^{\star}{(t)}})$ satisfying Eq. 3. Suppose there exist scalars ${\lambda,R} > 0$ and a feedback operator $k_{c}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{m}}$ can be constructed such that the trajectory $x{(t)}$ of the unperturbed dynamics ${\overset{˙}{x}{(t)}} = {\overline{F}{({x{(t)}},{u_{c}{(t)}})}}$ with control ${u_{c}{(t)}} = {{u^{\star}{(t)}} + {k_{c}{({x^{\star}{(t)}},{x{(t)}})}}}$ satisfies

Then, the system with the unperturbed dynamics is said to be Universally Exponentially Stabilizable (UES) with rate $\lambda$ and overshoot $R$.

With the notion of UES defined, we now proceed to examine how UES may be established for a given system. For the compact safe set $\mathcal{X} \subset \mathcal{R}^{n}$ defined in Section 2, let $T_{x}\mathcal{X}$ be the tangent space of $\mathcal{X}$ at $x \in \mathcal{X}$. Consequently, we denote by ${T\mathcal{X}} = {{\overset{˙}{\bigcup}}_{x \in \mathcal{X}}T_{x}\mathcal{X}}$ the tangent bundle of $\mathcal{X}$, where $\overset{˙}{\bigcup}$ denotes the disjoint union. Details on differential geometric notions used in the manuscript may be found in. The variational dynamics of the unperturbed/nominal system in may be written as \[27, Chapter 3\]

with ${\delta_{x}{}} = x_{0}$, where we have dropped the temporal dependencies for brevity. Here, ${\delta_{x}{(t)}} \in {T_{x{(t)}}\mathcal{X}}$, ${\delta_{u}{(t)}} \in {T_{u{(t)}}{\mathbb{R}}^{m}}$, $u{\lbrack j\rbrack}{(t)}$ is the $j^{th}$ element of the control vector and ${b_{j}{(x)}} \in {\mathbb{R}}^{n}$ is the $j^{th}$ column of $B{(x)}$.

### Definition 3.2

Consider the differential dynamics in. Suppose there exist positive scalars $\lambda$, $\underset{¯}{\alpha}$, $\overline{\alpha}$, $0 < \underset{¯}{\alpha} < \overline{\alpha} < \infty$, and a smooth^22^2Throughout the manuscript, by smooth we mean the class $\mathcal{C}^{\infty}$ of functions defined on appropriate domains. function $M:{{\mathbb{R}}^{n}\rightarrow{\mathbb{S}}^{n}}$ such that for all ${(x,\delta_{x})} \in {T\mathcal{X}}$ one has

${{\underset{¯}{\alpha}{\mathbb{I}}_{n}} \preceq {M{(x)}} \preceq {{\mathbb{I}}_{n}\overline{\alpha}}},$ (8a)
${\delta_{x}^{\top}M{(x)}B{(x)}} = 0\Rightarrow$
${{\delta_{x}^{\top}\left( {{\partial_{f}{M{(x)}}} + \left\lbrack {M{(x)}\frac{\partial{f{(x)}}}{\partial x}} \right\rbrack_{\mathbb{S}} + {2\lambdaM{(x)}}} \right)\delta_{x}} \leq 0},$ (8b)
${{{{\partial_{b_{j}}{M{(x)}}} + \left\lbrack {M{(x)}\frac{\partial{b_{j}{(x)}}}{\partial x}} \right\rbrack_{\mathbb{S}}} = 0},{j \in {\{ 1,\ldots,m\}}}}.$ (8c)

Then, the function $M{(x)}$ is defined to be the Control Contraction Metric (CCM) for the nominal/unperturbed dynamics.

### Theorem 3.1 (\[18, 15\])

Given positive scalars $\lambda$, and $\underset{¯}{\alpha} \leq \overline{\alpha} < \infty$, suppose there exists a CCM $M{(x)}$ for the nominal/unperturbed dynamics in Eq. 2. Then, given any desired state-input trajectory $({x^{\star}{(t)}},{u^{\star}{(t)}})$ as in Eq. 3, there exists a feedback operator $k_{c}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{m}}$ such that the trajectory $x{(t)}$ of the unperturbed dynamics ${\overset{˙}{x}{(t)}} = {\overline{F}{({x{(t)}},{u_{c}{(t)}})}}$ with control ${u{(t)}} = {{u^{\star}{(t)}} + {k_{c}{({x^{\star}{(t)}},{x{(t)}})}}}$ is UES with respect to $x^{\star}{(t)}$ with the overshoot of $R = {\overline{\alpha}/\underset{¯}{\alpha}}$ in the sense of Definition 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach").

The central idea to this result is that the function ${V{(x,\delta_{x})}}:={\delta_{x}^{\top}M{(x)}\delta_{x}}$ can be interpreted as a differential Lyapunov function and the conditions in Eq. 8 ensure that ${\overset{˙}{V}{(x,\delta_{x})}} \leq {- {2\lambdaV{(x,\delta_{x})}}}$ for all ${(x,\delta_{x})} \in {T\mathcal{X}}$. We place the following assumption on the known/unperturbed dynamics.

### Assumption 3.1

The nominal/unperturbed dynamics in Eq. 2 admit a CCM $M{(x)}$ for all $x \in \mathcal{X}$ with positive scalars $\lambda$, $\underset{¯}{\alpha}$, and $\overline{\alpha}$, as in Definition 3.2.

Using Theorem 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") it is straightforward to conclude that the consequence of this assumption is that any desired state-input trajectory can be tracked by the nominal/unperturbed dynamics in the sense of Definition 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") with rate $\lambda$ and overshoot $R = {\overline{\alpha}/\underset{¯}{\alpha}}$. Let $\Xi{(p,q)}$ be the set of smooth curves connecting any two points ${p,q} \in \mathcal{X}$. Then using the Riemannian metric $M$, the length of any curve $\gamma \in {\Xi{(p,q)}}$ is given by the following expression

where ${\gamma_{s}{(s)}} = {\partial{{\gamma{(s)}}/{\partial s}}}$. By definition, the minimizing geodesic $\overline{\gamma}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$ satisfies the following relationship

where $d{(p,q)}$ refers to the Riemannian distance between the two points $p$ and $q$. Existence of the minimizing geodesic is guaranteed by the Hopf-Rinow theorem. The Riemannian energy between the two points is defined using the Riemannian distance as the following quantity

Further details on Riemannian geometry may be found in. A direct and straightforward consequence of Assumption 3.1 is that

The proof for this relationship can be found in Lemma A.3. We will rely on the Riemannian energy's interpretation as a control Lyapunov function for the presented methodology. This interpretation was initially presented in.

### Remark 3.1

Thus far we have only established the existence of feedback control operators and not constructed any. In fact, as explained in \[15, Sec. VI.A\], any controller may be chosen as long as the following set membership is established

The precise choice of the controller we use will be presented later in the manuscript.

## Contraction Theory Based $\mathcal{L}_{1}$-Adaptive Control

In this section we introduce the structure of the proposed controller for the uncertain nonlinear system in Eq. 1. Consider the following feedback decomposition

where $u_{c}:{{\mathbb{R}}_{\geq 0}\rightarrow{\mathbb{R}}^{m}}$ is the contraction theory based control designed to guarantee UES (Definition 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach")) of the nominal dynamics in Eq. 2, and $u_{a}:{{\mathbb{R}}_{\geq 0}\rightarrow{\mathbb{R}}^{m}}$ is the $\mathcal{L}_{1}$ control signal. The overall architecture of the proposed feedback is illustrated in Fig. 2. We refer to the uncertain system in Eq. 1 with the feedback law Eq. 13 as the $\mathcal{L}_{1}$ closed-loop system. Before we proceed with the description of the individual components of the controller, we introduce the following list of constants that are of importance for the results and analyses presented in this paper:

where $\mathcal{O}{(\rho)}$ is defined in Eq. 5; $\Delta_{u^{\star}}$ is defined in Assumption 2.2; $\Delta_{f}$, $\Delta_{f_{x}}$, $\Delta_{B}$, $\Delta_{B_{x}}$, $\Delta_{b_{x}}$, are defined in Assumption 2.3; $\Delta_{h}$, $\Delta_{h_{t}}$, $\Delta_{h_{x}}$ are defined in Assumption 2.4; $\Delta_{B^{\dagger}}$ and $\Delta_{B_{x}^{\dagger}}$ are defined in Assumption 2.5; $\overline{\alpha}$ and $\underset{¯}{\alpha}$ are defined in Assumption 3.1; and $F{(x)}$ is defined as

where ${W{(x)}} = {M{(x)}^{- 1}}$ is referred to as the dual metric and ${L{(x)}^{\top}L{(x)}} = {W{(x)}}$.

Figure 2: Architecture of CCM-based ℒ1-adaptive control

### Contraction theory based control: $u_{c}\hspace{0pt}{(t)}$

As mentioned in Section 3, under Assumption 3.1, Theorem 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") guarantees the existence of a feedback law which renders the nominal dynamics in Eq. 2 UES. In particular, we propose the following law

where, for the the feedback term, we use the law constructed in \[18, Sec. 5.1\], which is the solution to the following quadratic program:

$k_{c}{(x^{\star}{(t)},x{(t)})} = \underset{k \in {\mathbb{R}}^{m}}{\arg\min}\left. \parallel k\parallel \right.^{2},$ (25a)
${{{\text{s.t.~}2{\overline{\gamma}}_{s}^{\top}{(1,t)}M{({x{(t)}})}{\overset{˙}{x}}_{k}{(t)}} - {2{\overline{\gamma}}_{s}^{\top}{(0,t)}M{({x^{\star}{(t)}})}{\overset{˙}{x}}^{\star}{(t)}}} \leq {- {2\lambda\mathcal{E}{({x^{\star}{(t)}},{x{(t)}})}}}},$ (25b)

in which $M{( \cdot )}$ is the CCM (Definition 3.2), $\overline{\gamma}{(s,t)}$, $s \in {\lbrack 0,1\rbrack}$, is the minimizing geodesic with ${\overline{\gamma}{(1,t)}} = {x_{k}{(t)}}$ and ${\overline{\gamma}{(0,t)}} = {x^{\star}{(t)}}$. As previously defined, the desired state-input pair satisfies ${{\overset{˙}{x}}^{\star}{(t)}} = {\overline{F}{({x^{\star}{(t)}},{u^{\star}{(t)}})}}$ with the nominal dynamics defined in Eq. 2. Additionally, ${{\overset{˙}{x}}_{k}{(t)}} = {\overline{F}{({x{(t)}},{{u^{\star}{(t)}} + k})}}$.

### Remark 4.1

As explained by the authors in \[18, Sec. 5.1\], the solution to the quadratic program in (25 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach")) can be obtained analytically given the minimizing geodesic $\overline{\gamma}{( \cdot,t)}$. Alternatively, one may use the differential controller proposed in, albeit at the expense of an increase in the control effort.

### $\mathcal{L}_{1}$-adaptive control: $u_{a}\hspace{0pt}{(t)}$

The computation of the signal $u_{a}{(t)}$ depends on three components illustrated in Fig. 2, namely, the state-predictor, the adaptation law, and a low-pass filter. Similar to, we define the state-predictor as

with ${\hat{x}{}} = x_{0}$, and where ${\hat{x}{(t)}} \in {\mathbb{R}}^{n}$ is the state of the predictor, ${\overset{\sim}{x}{(t)}} = {{\hat{x}{(t)}} - {x{(t)}}}$ is the state prediction error, and $A_{m} \in {\mathbb{R}}^{n \times n}$ is an arbitrary Hurwitz matrix.

The uncertainty estimate $\hat{\sigma}{(t)}$ in Eq. 26 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") is governed by the following adaptation law

where $\Gamma > 0$ is the adaptation rate, $\mathcal{H} = \left. \{{y \in {\mathbb{R}}^{m}} \middle| {\left. \parallel y\parallel \right. \leq \Delta_{h}}\} \right.$ is the set to which the uncertainty estimate is restricted to remain in with $\Delta_{h}$ defined in Assumption 2.4. Furthermore, ${\mathbb{S}}^{n} \ni P \succ 0$, is the solution to the Lyapunov equation ${{A_{m}^{\top}P} + {PA_{m}}} = {- Q}$, for some ${\mathbb{S}}^{n} \ni Q \succ 0$. Moreover, $\operatorname{Proj}_{\mathcal{H}}{( \cdot, \cdot )}$ is the projection operator standard in adaptive control literature,.

Finally, the control law $u_{a}{(t)}$ is defined as the following Laplace transform

where $C{(s)}$ is a low-pass filter with bandwidth $\omega$ and satisfies ${C{}} = {\mathbb{I}}_{m}$. Note that there is an abuse of notation when we denote both the geodesic interval parameter and the Laplace variable by $s$. The delineation between the two is clear from the context.

### Filter bandwidth and adaptation rate

The design of the $\mathcal{L}_{1}$-adaptive controller involves the design of a strictly proper and stable low-pass filter $C{(s)}$ with ${C{}} = {\mathbb{I}}_{m}$. Let the bandwidth of this filter be $\omega$. In the manuscript, for the sake of simplicity, we choose ${C{(s)}} = {\frac{\omega}{s + \omega}{\mathbb{I}}_{m}}$. As we will see in Section 5, the bandwidth $\omega$ of the low-pass filter $C{(s)}$ in Eq. 28 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") and the adaptation rate $\Gamma$ in Eq. 27 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") are design parameters which can be thought of as 'tuning-knobs'. However, these entities need to satisfy a few conditions mentioned below. The reasoning behind these conditions will be made clear in the subsequent section.

Suppose that Assumption 3.1 holds. Then, for arbitrarily chosen positive scalars $\epsilon$ and $\rho_{a}$, define

Furthermore, suppose that Assumptions 2.1-2.5 hold. Define

${\zeta_{1}{(\omega)}} =$ ${2\rho\Delta_{B}\frac{\overline{\alpha}}{\underset{¯}{\alpha}}\left( {\frac{\Delta_{h}}{\left| {{2\lambda} - \omega} \right|} + \frac{\Delta_{h_{t}} + {\Delta_{h_{x}}\Delta_{{\overset{˙}{x}}_{r}}}}{2\lambda\omega}} \right)},$ (31a)
${\zeta_{2}{(\omega)}} =$ ${\overline{\alpha}\Delta_{\Psi_{x}}\left( {\frac{\Delta_{h}}{\left| {{2\lambda} - \omega} \right|} + \frac{\Delta_{h_{t}} + {\Delta_{h_{x}}\Delta_{{\overset{˙}{x}}_{r}}}}{2\lambda\omega}} \right)},$ (31b)
${\zeta_{3}{(\omega)}} =$ ${\overline{\alpha}\Delta_{h_{x}}\left( \frac{{4\lambda\Delta_{B}} + \Delta_{\overset{˙}{\Psi}}}{\lambda\omega} \right)},$ (31c)
where $\Delta_{{\overset{˙}{x}}_{r}}$, $\Delta_{\Psi_{x}}$, and $\Delta_{\overset{˙}{\Psi}}$, are known positive scalars defined in Eqs. 17, 15 and 22 respectively.

Then, the bandwidth $\omega$ of the low-pass filter $C{(s)}$ and the adaptation rate need to verify the following conditions

$\rho_{r}^{2} \geq$ ${\frac{\mathcal{E}{(x_{0}^{\star},x_{0})}}{\underset{¯}{\alpha}} + {\zeta_{1}{(\omega)}}},$ (32a)
$\underset{¯}{\alpha} >$ ${{\zeta_{2}{(\omega)}} + {\zeta_{3}{(\omega)}}},$ (32b)
$\sqrt{\Gamma} >$ $\frac{\Delta_{\theta}}{\rho_{a}{({\underset{¯}{\alpha} - {\zeta_{2}{(\omega)}} - {\zeta_{3}{(\omega)}}})}},$ (32c)

where $\Delta_{\theta}$ is another known positive scalar defined in Eq. 21.

### Remark 4.2

Based on the definition of $\rho_{r}$ in Eq. 30 and the bounds on the Riemannian energy $\mathcal{E}{({x^{\star}{(t)}},{x{(t)}})}$ in Eq. 12, the inequality $\rho_{r}^{2} > {{\mathcal{E}{(x_{0}^{\star},x_{0})}}/\underset{¯}{\alpha}}$ holds. Furthermore, since $\zeta_{1}{(\omega)}$, $\zeta_{2}{(\omega)}$, and $\zeta_{3}{(\omega)}$, all converge to zero as $\omega$ increases, the bandwidth conditions in (32a)-(32b) can always be satisfied by choosing a large enough $\omega$.

## Performance Analysis

In this section we analyze the performance of the uncertain system in Eq. 1 with the $\mathcal{L}_{1}$ control feedback $u{(t)}$ defined in Eq. 13. As in, to derive the bounds between the desired trajectory $x^{\star}{(t)}$ and the state $x{(t)}$ of the uncertain system, we first introduce the following intermediate system, which we refer to as the reference system:

where $k_{c}$ is defined in Eq. 25 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") using $x_{r}$ in place of $x$. The main feature of the reference system is that it defines the the best achievable performance, given the perfect knowledge of uncertainty, i.e. it reflects that the cancellation of the uncertainty $h{(t,{x_{r}{(t)}})}$ can happen only within the bandwidth of the low-pass filter.

The analysis consists of two parts: we first derive bounds between the desired trajectory and the reference system $\|{{x^{\star}{(t)}} - {x_{r}{(t)}}}\|$. Then we derive the bounds between the states of the reference system and the actual system $\left. \parallel{{x_{r}{(t)}} - {x{(t)}}}\parallel \right.$. Recall that we refer to the actual system as the $\mathcal{L}_{1}$ closed loop system, which is given by Eq. 1 with the control law in Eq. 13. Finally, the triangle inequality produces the desired bound on $\left. \parallel{{x^{\star}{(t)}} - {x{(t)}}}\parallel \right.$. In this way, the reference system behaves as an 'anchor system' for the analysis. These bounds are illustrated in Fig. 3. Furthermore, we provide the justification of treating the bandwidth $\omega$ of $C{(s)}$ and the adaptation rate $\Gamma$ as tuning-knobs. Indeed, the upcoming analysis will show that we can ensure that ${x{(t)}} \in {\Omega{(\rho,{x^{\star}{(t)}})}}$ (see Eq. 4) for all $t \geq 0$.

We begin with the bound between the reference system state and desired state trajectory. This corresponds to the green tube in Fig. 3. The proofs for all the claims in this section are provided in Appendix B.

### Lemma 5.1

Let all the assumptions hold and let $\rho_{r}$ be as defined in Eq. 30. If the conditions in (32a)-(32b) hold, then for any desired state trajectory $x^{\star}{(t)}$ the state $x_{r}{(t)}$ of the reference system in satisfies

and is uniformly ultimately bounded as

where the ultimate bound is defined as

Next, we compute the bounds between the reference system in Eq. 33 and the $\mathcal{L}_{1}$ closed-loop system (Eq. 1 with Eq. 13).

### Lemma 5.2

Suppose that the stated assumptions and the conditions in Eq. 32 hold. Additionally, assume that the trajectory of the $\mathcal{L}_{1}$ closed-loop system satisfies ${x{(t)}} \in {\Omega{(\rho,{x^{\star}{(t)}})}}$, for all $t \in {\lbrack 0,\tau\rbrack}$, for some $\tau > 0$, with $\Omega{(\rho,{x^{\star}{(t)}})}$ and $\rho$ defined in Eq. 4 and Eq. 30, respectively. Then,

where $\rho_{a}$ is given in Eq. 30.

Figure 3: The bounds/tubes for the analysis of the CCM based ℒ1-adaptive controller.

We now use Lemmas 5.1-5.2 to state the main result of the paper.

### Theorem 5.1

Suppose that the stated assumptions and conditions in Eq. 32 hold. Consider a desired state trajectory $x^{\star}{(t)}$ as in and the state of the $\mathcal{L}_{1}$ closed-loop system defined via and. Then we have

and is uniformly ultimately bounded as

Here, the ultimate bound is defined as

where the positive scalars $\rho$ and $\rho_{a}$ are defined in, and $\mu{(\omega,T)}$ is defined in Lemma 5.1.

### Discussion

A few critical comments are in order for the performance analysis. The main result in Theorem 5.1 provides uniform ultimate bounds. Let us first discuss the implication of the uniform bound $\rho$ in Eq. 37. As per the definition in Eq. 30, $\rho = {\rho_{r} + \rho_{a}}$. It is evident from the definition that $\rho$ is lower bounded by the initial condition difference $\left. \parallel{x_{0}^{\star} - x_{0}}\parallel \right.$ and the positive scalars $\underset{¯}{\alpha}$ and $\overline{\alpha}$ which are associated with the CCM $M{(x)}$ of the nominal dynamics. Furthermore, as per the proof of Lemma 5.2, since $\rho_{a} \propto {1/\sqrt{\Gamma}}$, the adaptation rate $\Gamma$ can be increased to the maximum value allowable by the computation hardware to guarantee the smallest $\rho_{a}$, and thus, the smallest uniform bound $\rho$. However, the fact remains that the uniform bound $\rho$ guaranteed by the $\mathcal{L}_{1}$-controller for the tracking remains lower bounded by $\left. \parallel{x_{0}^{\star} - x_{0}}\parallel \right.$. The only way this bound can be further reduced is if the underlying planner which provides the desired state-input pair $({x^{\star}{(t)}},{u^{\star}{(t)}})$ can minimize $\left. \parallel{x_{0}^{\star} - x_{0}}\parallel \right.$.

Theorem 5.1 also provides the (uniform) ultimate bound via $\delta{(\omega,T)}$ defined in Eq. 39. As already mentioned, $\rho_{a} \propto {1/\sqrt{\Gamma}}$. Furthermore, from the definition of $\zeta_{1}{(\omega)}$ in Eq. 31a, it is evident that by choosing a large enough $\omega$, there will always exist a known $0 < T < \infty$ such that ${\delta{(\omega,t)}} \leq \overline{\rho}$, for all $t \geq T$, for any chosen $\overline{\delta} > 0$. Therefore, we can always arbitrarily shrink the tube $\mathcal{O}{(\overline{\delta})}$ by choosing appropriate bandwidth $\omega$ and rate of adaptation $\Gamma$. This feature of the CCM-based $\mathcal{L}_{1}$-controller is very advantageous, since, for example, this capability will allow the safe navigation of a robot through tight and cluttered environments. This improved performance, however, comes at the cost of reduced robustness. There exists a trade-off between performance and robustness that should be taken into consideration. As aforementioned, performance (radius of tubes around $x^{\star}{(t)}$) depends on $\Gamma$ and $\omega$. The rate of adaptation $\Gamma$ is obviously limited by the available computational hardware. More importantly, the role of the low-pass filter $C{(s)}$ in the $\mathcal{L}_{1}$-control architecture (Fig. 2) is to decouple the control loop from the estimation loop. Thus, increasing the bandwidth $\omega$ of $C{(s)}$ in order to get a tighter tube will lead to the $u_{a}{(t)}$ component of the $\mathcal{L}_{1}$-input to behave as a high-gain signal, thus possibly sacrificing desired robustness levels. Therefore, this trade-off must always be taken into account during the planning phase.

## Simulation Results

We provide two illustrative examples. In the first example, we consider the non-feedback linearizable system from and synthesize the controller to ensure safe regulation around the equilibrium point. We also show the effect of uniform ultimate bounds discussed in the previous section, if the system were to start far away from the equilibrium. In the second example, we consider the system from and ensure safety in a motion planning context during trajectory tracking. In particular we show how altering the tube parameters affects the choice in the filter bandwidth and adaptation rate.

### Non-feedback Linearizable Systems

Consider the system with the structure defined in Eq. 1 and the system functions given by

where the state ${x{(t)}} = {\lbrack{x_{1}{(t)}x_{2}{(t)}x_{3}{(t)}}\rbrack}^{\top}$. The dual metric ${W{(x)}} = {M{(x)}^{- 1}}$ satisfying the conditions in Eqs. 8a, 8b and 8c was found using the sum-of-squares programming toolbox SumOfSquares.jl, optimization software JuMP, and the optimization solver, as

The metric satisfies a convergence rate $\lambda = 1.0$ and is uniformly bounded in the set $\mathcal{X} = \left. \{{y \in {\mathbb{R}}^{3}} \middle| {\left. \parallel y\parallel \right._{\infty} \leq 0.1}\} \right.$ with $\overline{\alpha} = 5.88$ and $\underset{¯}{\alpha} = 3.85$. Now, suppose that the system is experiencing sinusoidal disturbances of the form: ${h{(t)}} = {0.1{\sin{({2t})}}}$. We chose the initial condition of the system as $x_{0} = {{\lbrack{1 - 1\ 1}\rbrack}^{\top} \times 10^{- 2}}$ and the desired state as $x^{\star} = {\lbrack 0\ 0\ 0\rbrack}^{\top}$. Incidentally, the desired state is also the equilibrium point of the system which means that the desired control is ${u^{\star}{(t)}} \equiv 0$.

Figure 4: Comparison of controller performance between (a) pure CCM-based feedback, and a (b) CCM-based ℒ1 architecture. The green and orange shaded regions signify the induced Ω (ρr,x⋆) and Ω (ρ,x⋆) tubes respectively. The dashed green and orange lines signify the uniform ultimate bounds μ (ω,T) and δ (ω,T) evaluated at every timestep.

A pure CCM-based feedback strategy produces the oscillatory behavior, seen in Fig. 4a. A CCM-based $\mathcal{L}_{1}$-adaptive controller is designed in Fig. 4b for tube widths $\epsilon = 0.01$ and $\rho_{a} = 0.01$. The filter bandwidth and adaptation rate required to achieve this level of performance were chosen as $\omega = 50$ and $\Gamma = {5 \times 10^{6}}$ respectively by satisfying the conditions in Eq. 32. Notice that the bounds are far more conservative than the actual behavior of the system. In fact, the error in tracking is uniformly bounded as $\left. \parallel x\parallel \right._{\mathcal{L}_{\infty}} < 0.02$. Additionally, notice that the uniform ultimate bounds of the reference system tube from Eq. 36 and the actual system tube from Eq. 39 shrink with time and are essentially 'forgetting' the initial conditions of the system.

### Safe Tubes for Motion Planning

Consider the system with the structure defined in Eq. 1 and the system functions given by

where the state ${x{(t)}} = {\lbrack{x_{1}{(t)}x_{2}{(t)}}\rbrack}^{\top}$. Since this particular system is feedback linearizable, it admits a constant (or flat) dual metric for all $x \in {\mathbb{R}}^{2}$. The value of the dual metric and the associated convergence parameter is computed in and provided here for completeness:

Similar to, we chose the initial condition of the system as $x_{0} = {\lbrack{3.4 - 2.4}\rbrack}^{\top}$ and the target state as as $x^{\star} = {\lbrack 0\ 0\rbrack}^{\top}$. The desired state and control trajectory pair was computed using the iterative LQR solver provided by with the parameters $Q = {0.5{\mathbb{I}}_{2}}$ and $R = 1.0$. Suppose the system is affected by uncertainties of the form: ${h{(t,x)}} = {{- {2{\sin{({2t})}}}} - {0.1\left. \parallel{x{(t)}}\parallel \right.}}$, consisting of both time and state dependent terms. Depending on the desired level of tracking performance or closeness to obstacles in the environment, the user will pick the tube parameters $\epsilon$ and $\rho_{a}$ as defined in Eq. 30. In Fig. 5, we illustrate the trade-offs between choosing a tighter $\rho_{a}$ (Fig. 5a) versus a tighter $\epsilon$ (Fig. 5c) for this system.

Figure 5: Relationship between the choice of tube parameters ϵ and ρa and the controller parameters ω and Γ through the conditions defined in Eq. 32. For clarity the initial conditions for the desired trajectory and the actual system in this illustration are assumed to be the same.

In Fig. 6b, we observe the performance and robustness benefits of using CCM-based $\mathcal{L}_{1}$-adaptive control. Not only does the system track the desired trajectory closely, but also avoids colliding with obstacles (unlike in Fig. 6a) through an appropriate choice of tube parameters.

Figure 6: Comparison of performance and robustness between (a) pure CCM-based feedback, and (a) CCM-based ℒ1 architecture with tube parameters ϵ = 0.4 and ρa = 0.1. The dashed black line shows the desired trajectory designed by a planner, the gray polygon is an obstacle, and the orange shaded region is the safe tube given by Ω (ρ,x⋆ (t)). The behavior of the system under pure CCM-based feedback has been overlaid as a dashed red line in (b) for clarity.

## Conclusion and Future Work

We present a control methodology to enable safe and guaranteed feedback motion planning. The presented work relies on differential geometric contraction theory and $\mathcal{L}_{1}$-adaptive control. The proposed controller enables the apriori computation of uniform and ultimate-bounds which act as safety-certificates. These safety certificates induce 'tubes' which can be taken into account by any planner of choice. In this way, the safety of the system/robot is always guaranteed in the presence of model and environmental uncertainties. Furthermore, by using the control law's filter bandwidth and rate of adaptation as tuning knobs, the width of the safety tubes can be adjusted. Future research will deal with the incorporation of learning into the proposed control framework. This will lead to improved performance since the underlying planner will have access to improved model knowledge. More importantly, the controller proposed in this work will keep the learning process safe because of the apriori specified and guaranteed bounds during the transient phase. Further investigations will be undertaken to extend this framework to enable safe planning and control using a reduced-order model to enable fast planning.
