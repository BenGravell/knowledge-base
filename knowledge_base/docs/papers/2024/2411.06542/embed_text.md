## Introduction

Dexterous manipulation is full of contact-rich interactions, enabling various tasks through complex frictional interactions \[(https://arxiv.org/html/2411.06542v4#bib.bib1), (https://arxiv.org/html/2411.06542v4#bib.bib2)\]. Historically, the non-smooth nature of contact has precluded a range of planning and control methods that rely on gradients of the dynamics. Recent advances have utilized *contact smoothing* --- where non-smooth dynamics are replaced by a continuously differentiable proxy --- to great effect as surrogate dynamics models for *planning* through contact \[(https://arxiv.org/html/2411.06542v4#bib.bib3), (https://arxiv.org/html/2411.06542v4#bib.bib4), (https://arxiv.org/html/2411.06542v4#bib.bib5), (https://arxiv.org/html/2411.06542v4#bib.bib6)\]. One may hope, then, that smoothing enables the use gradient-based *control*.

Figure 1: These figures show snapshots of hardware experiments using LQR and open-loop controllers under perturbations to initial conditions of cylinder. The thick and thin lines represent the desired frame at the terminal time step and the current frame of the cylinder, respectively. While LQR outperforms open-loop in this example, a more comprehensive evaluation shows that LQR generally performs poorly. The hardware experiment videos can be found here.

This work suggests that the above hope may face significant obstacles. We introduce LQR control for contact-manipulation via contact smoothing. Furthermore, we present and analyze robust trajectory optimization, hoping that the generated trajectories are robust to the model errors accumulated by using a surrogate dynamics model for control, and thus more amenable to LQR. Then, we extensively evalute the performance of these methods, both in simulation and in hardware, on a bimanual whole-body manipulation as shown in Fig. (https://arxiv.org/html/2411.06542v4#S1.F1 "Figure 1 ‣ I Introduction ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). In short, we find:

> *Despite its efficacy in planning through contact, dynamical smoothing alone is unsatisfactory as a means to obtaining linear control policies.*

Finally, we identify the key factors leading to the inadequacies of linear control; namely, the *unilaterality* of contact, and the tendency of controllers to "push and pull" unless the dynamics are only very-slightly smoothed.

## Related Work

### II-A Planning through Contact

One approach to motion-planning through contact enforces contact dynamics by including linear complementarity constraints \[(https://arxiv.org/html/2411.06542v4#bib.bib7), (https://arxiv.org/html/2411.06542v4#bib.bib3), (https://arxiv.org/html/2411.06542v4#bib.bib8), (https://arxiv.org/html/2411.06542v4#bib.bib4), (https://arxiv.org/html/2411.06542v4#bib.bib9), (https://arxiv.org/html/2411.06542v4#bib.bib10)\]. Another popular method to address contacts is based on Mixed-Integer Programming (MIP) \[(https://arxiv.org/html/2411.06542v4#bib.bib11), (https://arxiv.org/html/2411.06542v4#bib.bib12), (https://arxiv.org/html/2411.06542v4#bib.bib13), (https://arxiv.org/html/2411.06542v4#bib.bib14), (https://arxiv.org/html/2411.06542v4#bib.bib15)\], where discrete variables encode contact modes. However, due to the inherent non-smoothness of contact dynamics, both methods suffer from poor scalability as the number of contact modes increases.

To tackle this, contact smoothing has been proposed, replacing exact dynamics models with surrogate models that obey second-order smoothness \[(https://arxiv.org/html/2411.06542v4#bib.bib3), (https://arxiv.org/html/2411.06542v4#bib.bib5), (https://arxiv.org/html/2411.06542v4#bib.bib16), (https://arxiv.org/html/2411.06542v4#bib.bib6)\]. This approach introduces a "force-at-a-distance" effect where gradients through the dynamics convey information about nearby contacts. Since gradients of the dynamics become continuous, gradient-based optimizers are able to find solutions more efficiently. Our work employs a log-barrier smoothing scheme \[(https://arxiv.org/html/2411.06542v4#bib.bib5), (https://arxiv.org/html/2411.06542v4#bib.bib6)\], which is more efficient compared to stochastic smoothing schemes \[(https://arxiv.org/html/2411.06542v4#bib.bib16), (https://arxiv.org/html/2411.06542v4#bib.bib17)\].

### II-B Control through Contact

Prior approaches to control through contact reason about contact modes \[(https://arxiv.org/html/2411.06542v4#bib.bib18), (https://arxiv.org/html/2411.06542v4#bib.bib19), (https://arxiv.org/html/2411.06542v4#bib.bib20), (https://arxiv.org/html/2411.06542v4#bib.bib21)\]. While these approaches can run in real time for simple systems with only a handful of contact modes, they have yet to scale to high-dimensional systems, multiple objects per scene, or contacts with objects of complex and/or irregular shapes due to the expensive computation.

In contrast, contact-smoothing offers a way to directly apply *smooth* control methods while being less constrained by the non-smoothness of contact dynamics, at the cost of introducing some smoothing bias \[(https://arxiv.org/html/2411.06542v4#bib.bib16)\]. In this work, we study LQR, which uses the underlying problem structure provided by contact smoothing, enabling its application to high-dimensional bimanual whole-body manipulation tasks.

### II-C Robust Planning through Contact

Previous work on robust planning through contact (e.g., \[(https://arxiv.org/html/2411.06542v4#bib.bib22)\]) generally falls into two approaches: *domain randomization*, which involves stochastic optimization over a fixed distribution of dynamics models \[(https://arxiv.org/html/2411.06542v4#bib.bib21), (https://arxiv.org/html/2411.06542v4#bib.bib23)\], and *worst-case optimization*, which focuses on performance under worst-case scenarios within an uncertainty set \[(https://arxiv.org/html/2411.06542v4#bib.bib24), (https://arxiv.org/html/2411.06542v4#bib.bib25), (https://arxiv.org/html/2411.06542v4#bib.bib26), (https://arxiv.org/html/2411.06542v4#bib.bib27)\]. These methods effectively handle parametric uncertainties in the system dynamics, such as mass and friction, but do not discuss shape uncertainty (e.g., the radius of a cylinder). Shape uncertainty is critical for generalized manipulation to avoid unexpected contact events, yet integrating it into system dynamics remains challenging.

In this work, we incorporate domain randomization with an emphasis on shape uncertainty for primitive objects. Using contact smoothing, our method incorporates smoothed collision dynamics, enabling robust optimization to consider shape uncertainty. We also hope that using our technique enables LQR to track reference trajectories more easily.

## Problem Statement

We focus on the manipulation of rigid objects. Throughout, we focus on bimanual tabletop manipulation, though in principle our approach extends beyond this regime.

### III-A Quasi-Dynamic Dynamics Model

We generate plans and linear feedback gains by considering a quasi-dynamic model of a robot manipulating a single rigid object \[(https://arxiv.org/html/2411.06542v4#bib.bib28)\]. We consider robots with $n_{a}$ actuated Degrees of Freedom (DoFs) and the objects with $n_{u}$ unactuated DoFs. We denote the configurations of the object and the robot as $\mathbf{q}^{u} \in {\mathbb{R}}^{n_{u}}$ and $\mathbf{q}^{a} \in {\mathbb{R}}^{n_{a}}$, respectively. In quasi-dynamics models, we assume velocities are small, and thus system states are the concatenation of both configurations $\mathbf{x}:=\mathbf{q}:=\left\lbrack {}_{}^{},{}_{}^{} \right\rbrack^{\top} \in {\mathbb{R}}^{n_{x}}$, where $n_{x} = {n_{u} + n_{a}}$. ^11^1Superscript $u$ stands for unactuated, and $a$ for actuated. We denote the change in system configuration from the current time step to the next time step as ${{\mathbf{δ}}\mathbf{q}}:=\left\lbrack {{\mathbf{δ}}{}_{}^{}},{{\mathbf{δ}}{}_{}^{}} \right\rbrack^{\top}$. We denote the control input as $\mathbf{u} \in {\mathbb{R}}^{n_{a}}$, defined as the commanded positions of the robot's joints. We consider the linear feedback law $\mathbf{u} = {\mathbf{v} + {\mathbf{K}\mathbf{\Delta}\mathbf{x}}}$ where $\mathbf{v} \in {\mathbb{R}}^{n_{a}}$ is the feedforward gain from trajectory optimization, $\mathbf{K} \in {\mathbb{R}}^{n_{a} \times n_{x}}$ is the feedback gain computed by LQR, and $\mathbf{\Delta}\mathbf{x}$ is the state error, or deviation from nomial trajectory.

### III-B Quasi-Dynamic Dynamics Model with Contact Smoothing

For computing ${\mathbf{δ}}\mathbf{q}$, we consider a log-barrier-smoothed formulation of quasi-dynamic dynamics from Eq. in \[(https://arxiv.org/html/2411.06542v4#bib.bib6)\]. We denote $\kappa$-smoothed forward dynamic map as

where $\kappa > 0$ is the user-defined barrier parameter. Smaller $\kappa$ corresponds to greater contact smoothing, and more "force at a distance" \[(https://arxiv.org/html/2411.06542v4#bib.bib6)\]. Recalling our notation $\mathbf{x} = \mathbf{q}$, the above can also be written as $\mathbf{x}_{t + 1} = {f_{\kappa}\left( \mathbf{x}_{t},\mathbf{u}_{t} \right)}$. When $\kappa$ does not change, we will simply write $f$ for $f_{\kappa}$.

Both our gradient descent-based trajectory optimizer and our synthesis of linear feedback rely on differentiation of the smoothed dynamics. Given ((https://arxiv.org/html/2411.06542v4#S3.E1 "Equation 1 ‣ III-B Quasi-Dynamic Dynamics Model with Contact Smoothing ‣ III Problem Statement ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")), we define derivatives:

See \[(https://arxiv.org/html/2411.06542v4#bib.bib6)\] for the complete derivation of ((https://arxiv.org/html/2411.06542v4#S3.E2 "Equation 2 ‣ III-B Quasi-Dynamic Dynamics Model with Contact Smoothing ‣ III Problem Statement ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")). Again, we use the shorthand $\mathbf{A} = \mathbf{A}_{\kappa}$ and $\mathbf{B} = \mathbf{B}_{\kappa}$.

### III-C Parametrized Quasi-Dynamic Dynamics Model

As described in Sec [II-C](https://arxiv.org/html/2411.06542v4#S2.SS3 "II-C Robust Planning through Contact ‣ II Related Work ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), we consider *uncertainty over the dynamics* induced by object uncertainty. These can be parameterized by a parameter $\mathbf{p} \in U \subseteq {\mathbb{R}}^{n_{p}}$ which enters into $f_{\kappa}$ in ((https://arxiv.org/html/2411.06542v4#S3.E1 "Equation 1 ‣ III-B Quasi-Dynamic Dynamics Model with Contact Smoothing ‣ III Problem Statement ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")). To lighten notation, we also let the parameter $\mathbf{p}$ encode an initial condition, $\mathbf{x}_{init}{(\mathbf{p})}$.

## Contact-Implicit Trajectory Optimization

In this section, we present both single-parameter and multi-parameter trajectory optimization baselines.

### IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT)

We formulate our optimal planning problem as follows.

$\min\limits_{{\{\mathbf{x}_{t}\}}_{t = 1}^{T},{\{\mathbf{v}_{t}\}}_{t = 0}^{T - 1}}$ $J\left( {\{\mathbf{x}_{t}\}}_{t = 1}^{T},{\{\mathbf{v}_{t}\}}_{t = 0}^{T - 1};\mathbf{p} \right)$ (3a)
s.t. ${\mathbf{x}_{t + 1} = {f\left( \mathbf{x}_{t},\mathbf{v}_{t};\mathbf{p} \right)}},{{\forall t} \in \mathcal{T}}$ (3b)
${{g\left( \mathbf{x}_{t},\mathbf{v}_{t};\mathbf{p} \right)} \leq \mathbf{0}},{{\forall t} \in \mathcal{T}}$ (3c)
${\mathbf{x}_{t} \in \mathcal{X}},{{\mathbf{v}_{t} \in \mathcal{V}},{{\forall t} \in \mathcal{T}}}$ (3d)
${\mathbf{x}_{0} = {\mathbf{x}_{init}(\mathbf{p})}},$ (3e)

where $\mathcal{T}:={\{ 0,\ldots,{T - 1}\}}$, $J$ is the trajectory-wise cost function, $f = f_{\kappa}$ is the contact dynamics of the system (see ((https://arxiv.org/html/2411.06542v4#S3.E1 "Equation 1 ‣ III-B Quasi-Dynamic Dynamics Model with Contact Smoothing ‣ III Problem Statement ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"))). $\mathbf{v}_{t}$ is the control input at time step $t$. ([3c](https://arxiv.org/html/2411.06542v4#S4.E3.3 "Equation 3c ‣ Equation 3 ‣ IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT) ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")) is used to impose inequality constraints involving $\mathbf{x}_{t}$ and $\mathbf{v}_{t}$ such as joint torque constraints and non-collision constraints. $\mathcal{X}$ and $\mathcal{V}$ represent a convex polytope, consisting of a finite number of linear inequality constraints for bounding the decision variables. In ([3e](https://arxiv.org/html/2411.06542v4#S4.E3.5 "Equation 3e ‣ Equation 3 ‣ IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT) ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")), the initial condition encoded by $\mathbf{p}^{i}$ determines the initial state $\mathbf{x}_{0}$ (see [Section III-C](https://arxiv.org/html/2411.06542v4#S3.SS3 "III-C Parametrized Quasi-Dynamic Dynamics Model ‣ III Problem Statement ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")).

### IV-B Multi-Parameter Trajectory Optimization (MP-TrajOPT)

An alternative to ((https://arxiv.org/html/2411.06542v4#Sx1.EGx1 "Equation 3 ‣ IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT) ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")) is a robust formulation over multiple parameters. We focus on the simplest approach: optimizing average performance on $N$ realizations ${(\mathbf{p}^{i})}_{1 \leq i \leq N}$, which for simplicity are manually chosen, inspired by \[(https://arxiv.org/html/2411.06542v4#bib.bib29), (https://arxiv.org/html/2411.06542v4#bib.bib21)\], using Sample Average Approximation (SAA) \[(https://arxiv.org/html/2411.06542v4#bib.bib30)\]. For each $\mathbf{p}^{i}$, we optimize over a corresponding trajectories ${(\mathbf{x}^{i})}_{1 \leq i \leq N}$.

$\min\limits_{\mathbf{X},{\{\mathbf{v}_{t}\}}_{t = 0}^{T - 1}}$ $\frac{1}{N}{\sum\limits_{i = 1}^{N}{J\left( {\{\mathbf{x}_{t}^{i}\}}_{t = 1}^{T},{\{\mathbf{v}_{t}\}}_{t = 0}^{T - 1};\mathbf{p}^{i} \right)}}$ (4a)
s.t. ${\mathbf{x}_{t + 1}^{i} = {f_{\kappa}\left( \mathbf{x}_{t}^{i},\mathbf{v}_{t};\mathbf{p}^{i} \right)}},{{{\forall t} \in \mathcal{T}},{{\forall i} \in \mathcal{I}}}$ (4b)
${{g\left( \mathbf{x}_{t}^{i},\mathbf{v}_{t};\mathbf{p}^{i} \right)} \leq \mathbf{0}},{{{\forall t} \in \mathcal{T}},{{\forall i} \in \mathcal{I}}}$ (4c)
${\mathbf{x}_{t}^{i} \in \mathcal{X}},{{\mathbf{v}_{t} \in \mathcal{V}},{{{\forall t} \in \mathcal{T}},{{\forall i} \in \mathcal{I}}}}$ (4d)
${\mathbf{x}_{0}^{i} = {\mathbf{x}_{init}\left( \mathbf{p}^{i} \right)}},{{\forall i} \in \mathcal{I}}$ (4e)

where $\mathbf{X}:={\{\mathbf{x}_{t}^{i},\forall t \in \mathcal{T},\forall i \in \mathcal{I}\}}$, $\mathcal{I}:={\{ 0,\ldots,{N - 1}\}}$. We emphasize that we do not have superscript $i$ on $\mathbf{v}_{t}$ because our objective is to design a single plan that succeeds on average over the $N$ parameters. Note that ((https://arxiv.org/html/2411.06542v4#Sx1.EGx2 "Equation 4 ‣ IV-B Multi-Parameter Trajectory Optimization (MP-TrajOPT) ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")) with $N = 1$ specializes to ((https://arxiv.org/html/2411.06542v4#Sx1.EGx1 "Equation 3 ‣ IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT) ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")). We call this SP-TrajOPT (Single- Parameter Trajectory Optimization) as it only considers a single parameter. For $N > 1$, we refer to the procedure as MP-TrajOPT (Multi-Parameter Trajectory Optimization).

## Feedback Synthesis via LQR

In this section, we present an approach to feedback gain synthesis by solving an LQR problem through linearizations of the contact smoothed dynamics.

Using ((https://arxiv.org/html/2411.06542v4#S3.E2 "Equation 2 ‣ III-B Quasi-Dynamic Dynamics Model with Contact Smoothing ‣ III Problem Statement ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")), we can compute LQR feedback gains $\mathbf{K}$. The objective of using LQR is to design a controller that can locally stabilize the system. In this work, we consider the following optimal control problem given $\mathbf{x}_{t}$ and ${\mathbf{v}_{t},t} \in \mathcal{T}$.

$\min\limits_{{\{{\mathbf{\Delta}\mathbf{v}_{t}}\}}_{t = 0}^{T - 1}}$ ${\sum\limits_{t = 1}^{T}\left\| {\mathbf{\Delta}\mathbf{x}_{t}} \right\|_{\mathbf{Q}_{t}}^{2}} + {\sum\limits_{t = 0}^{T - 1}\left\| {\mathbf{\Delta}\mathbf{v}_{t}} \right\|_{\mathbf{R}_{t}}^{2}}$ (5a)
s.t. ${{\mathbf{\Delta}\mathbf{x}_{t + 1}} = {{\mathbf{A}_{t}\mathbf{\Delta}\mathbf{x}_{t}} + {\mathbf{B}_{t}\mathbf{\Delta}\mathbf{v}_{t}}}},{t \in \mathcal{T}}$ (5b)
${\mathbf{\Delta}\mathbf{x}_{0}} = {\hat{\mathbf{x}} - \mathbf{x}_{0}}$ (5c)

where $\mathbf{Q}_{t} = \mathbf{Q}_{t}^{\top}$ is positive semidefinite and $\mathbf{R}_{t} = \mathbf{R}_{t}^{\top}$ is positive definite at $t$. $\hat{\mathbf{x}}$ is the measurement of states at $t = 0$. $\mathbf{A}_{t}$ and $\mathbf{B}_{t}$ are error dynamics, which are obtained by linearizing true nonlinear contact dynamics of the system $f$ around $\mathbf{x}_{t}$ and ${\mathbf{v}_{t},t} \in \mathcal{T}$ in accordance with Sec.[III-B](https://arxiv.org/html/2411.06542v4#S3.SS2 "III-B Quasi-Dynamic Dynamics Model with Contact Smoothing ‣ III Problem Statement ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). It is worth noting again that $\mathbf{A}_{t}$ and $\mathbf{B}_{t}$ convey local contact information of the system dynamics. We use Riccati recursion \[(https://arxiv.org/html/2411.06542v4#bib.bib31)\] to compute $\mathbf{K}$ for ((https://arxiv.org/html/2411.06542v4#Sx1.EGx3 "Equation 5 ‣ V Feedback Synthesis via LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")). All of the computation happens offline. Hence, there is no expensive computation online unlike other methods (e.g., model predictive control).

## Results

In this section, we demonstrate our proposed controller under various uncertainties such as perturbations of initial conditions and shape variations for a cylinder. Through this section, we answer the following questions.

How well do TrajOPT and LQR work?

To what extent does MP-TrajOPT improve the performance of LQR?

Under what circumstances do our proposed controllers succeed or fail?

Figure 2: Illustration of our pipeline for generating dataset. We first provide RRT with the number of reference trajectories, Ntest, and lower- and upper-bounds of x and v, denoted as $\underset{¯}{\lbrack\cdot\rbrack}$ and $\overline{\lbrack\cdot\rbrack}$, respectively. Next, RRT samples initial and desired terminal states of an object and robots and plans Ntest different trajectories {(xtrrt,vtrrt)i}i = 1Ntest. Then, our trajectory optimizers compute Ntest different trajectories of the object and the robots, {(xtopt,vtopt)i}i = 1Ntest using {(xtrrt,vtrrt)i}i = 1Ntest as warm-start. Finally, given {(xtopt,vtopt)i}i = 1Ntest, LQR module computes {(Ktlqr)i}i = 1Ntest locally.

TABLE I: Parameters of cylinders.

### VI-A Experimental Setup

Three sets of parameters are in Table [I](https://arxiv.org/html/2411.06542v4#S6.T1 "Table I ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). For SP-TrajOPT, we use the nominal "(a)" shape in that table; for MP-TrajOPT we use all $N = 3$ "(a)", "(b)" and "(c)" shapes.

Figure 3: Distribution of reference trajectories generated by RRT. Left: Histograms showing the distribution of the start and end configurations of the object in the RRT-generated trajectories. The goal object configuration of (0,0,−π) is indicated. Right: 3D visualization of start and end object configurations of reference trajectories. While x and y coordinates are randomized, θ is kept constant due to the cylinder’s rotational symmetry.

Our pipeline is depicted in Fig. (https://arxiv.org/html/2411.06542v4#S6.F2 "Figure 2 ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). We begin by sampling $N_{\text{test}} = 340$ reference trajectories using RRT in \[(https://arxiv.org/html/2411.06542v4#bib.bib6)\] with $N_{\text{test}}$ different initial and goal states. RRT uses the nominal "(a)" parameter in Table [I](https://arxiv.org/html/2411.06542v4#S6.T1 "Table I ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). These yield state and feedforward control input sequences, ${\{\left( \mathbf{x}_{t}^{\text{rrt}},\mathbf{v}_{t}^{\text{rrt}} \right)_{1 \leq t \leq T}^{n}\}}_{n = 1}^{N_{\text{test}}}$ as illustrated in Fig. (https://arxiv.org/html/2411.06542v4#S6.F3 "Figure 3 ‣ VI-A Experimental Setup ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). For each $n = {1,\ldots,N_{\text{test}}}$, we use $\{\left( \mathbf{x}_{t}^{\text{rrt}},\mathbf{v}_{t}^{\text{rrt}} \right)_{1 \leq t \leq T}^{n}\}$ as a warm-start for computing trajectory-optimized plans $\left( \mathbf{x}_{t}^{\text{opt}},\mathbf{v}_{t}^{\text{opt}} \right)_{1 \leq t \leq T}^{n}$. The horizons $T$ are determined by the RRT warm-start and vary across reference trajectories, but always lie in the range $T \in {\lbrack 4,64\rbrack}$ with a mean of $T = 26$.

For SP-TrajOPT, we solve ((https://arxiv.org/html/2411.06542v4#Sx1.EGx1 "Equation 3 ‣ IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT) ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")) under the nominal "(a)" parameter. For MP-TrajOPT, we solve ((https://arxiv.org/html/2411.06542v4#Sx1.EGx2 "Equation 4 ‣ IV-B Multi-Parameter Trajectory Optimization (MP-TrajOPT) ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")) for all $N = 3$ parameters (note that this produces $N$ sequences of states; we select $\mathbf{x}_{t}^{\text{opt}}$ to be the one under the nominal shape). Both use the following cost function:

where $\mathbf{Q}_{t} = {\text{diag}(10,10,10,0.1,0.1,0.1,0.1,0.1,0.1)}$, ${\mathbf{R}_{t} = {\text{diag}}},{{\forall t} \in {\lbrack 0,\ldots,{T - 1}\rbrack}}$, $\mathbf{Q}_{T} = {\text{diag}(1000,1000,1000,0.1,0.1,0.1,0.1,0.1,0.1)}$. We formulate trajectory optimization programs using Drake's MathematicalProgram \[(https://arxiv.org/html/2411.06542v4#bib.bib32)\] and solve them using SNOPT \[(https://arxiv.org/html/2411.06542v4#bib.bib33)\]. We optimize with dynamic smoothing parameter $\kappa = 10^{5}$. We use $h = 0.1$ seconds as the time step.

### VI-B Feedback Synthesis

For LQR, we compute gains ${\{\left( \mathbf{K}_{t}^{\text{lqr}} \right)^{i}\}}_{i = 1}^{N_{\text{test}}}$ from ${\{\left( \mathbf{x}_{t}^{\text{opt}},\mathbf{v}_{t}^{\text{opt}} \right)^{i}\}}_{i = 1}^{N_{\text{test}}}$. It means that, when the trajectories are supplied by SP- or MP-TrajOPT, gains are computed around the nominal parameter dynamics, (a) parameter in Table [I](https://arxiv.org/html/2411.06542v4#S6.T1 "Table I ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). We use $h = 0.1$ seconds as the time step, but use a smaller smoothing parameter, $\kappa = 800$, for smoother derivatives. We tune and set ${\mathbf{Q}_{t} = {\text{diag}(10,10,10,0.1,0.1,0.1,0.1,0.1,0.1)}},{{\mathbf{R}_{t} = {\text{diag}}},{{\forall t} \in {\lbrack 0,\ldots,{T - 1}\rbrack}}}$, $\mathbf{Q}_{T} = {\text{diag}(1000,1000,1000,0.1,0.1,0.1,0.1,0.1,0.1)}$ to achieve good performance across $N_{\text{test}}$ reference trajectories.

### VI-B1 Execution in Drake

While plans and gains are synthesized via smoothed quasi-dynamic dynamics, we evaluate performance in either (i) Drake or (ii) on real hardware. The planning/feedback synthesis phase returns a sequence of states, feedforward control inputs, and feedback gains at discrete knot points $\left( \left\{ \mathbf{x}_{t} \right\}_{t = 0}^{T},\left\{ \mathbf{v}_{t} \right\}_{t = 0}^{T - 1},\left\{ \mathbf{K}_{t} \right\}_{t = 0}^{T - 1} \right)$.

We adopt a higher control loop frequency in Drake simulations, which necessitates interpolation of these discrete-time quantities. To do so, we convert the knot points into continuous time using First-Order Hold (FOH): states $\mathbf{x}^{\text{FOH}}{(t)}$, feedforward control input $\mathbf{v}^{\text{FOH}}{(t)}$, and feedback control input trajectories $\mathbf{K}^{\text{FOH}}{(t)}$. For $\mathbf{K}^{\text{FOH}}{(t)}$, we interpolate elements of $\mathbf{K}_{t}$ using FOH. At each time step in a Drake simulation, we measure the state $\mathbf{x}^{\text{mea}}{(t)}$ and rollout out the controller ${\mathbf{u}{(t)}} = {{\mathbf{v}^{\text{FOH}}{(t)}} + {\mathbf{K}^{\text{FOH}}{(t)}\left( {{\mathbf{x}^{\text{mea}}{(t)}} - {\mathbf{x}^{\text{FOH}}{(t)}}} \right)}}$.

### VI-B2 Evaluation Metrics

To evaluate the performance of controllers, we define the following metrics:

$\delta_{\text{terminal}}:={d\left( \mathbf{x}_{T}^{u,\text{mea}},\mathbf{x}_{T}^{u,\text{reference}} \right)}$ (7a)
$\Delta_{\text{terminal}}:={\frac{1}{N_{\text{test}}}{\sum\limits_{i = 1}^{N_{\text{test}}}\delta_{\text{terminal}}^{i}}}$ (7b)
$\eta_{A}^{B}:=\frac{\Delta_{\text{terminal}}^{B}}{\Delta_{\text{terminal}}^{A}}$ (7c)

where $\delta_{\text{terminal}}$ is the tracking error at the terminal time step. The superscript $u$ extracts the elements corresponding to $\mathbf{q}^{u}$ and $\mathbf{x}_{T}^{u,\text{reference}}$ is the reference trajectory the controller tries to track. Through experiments, we consider $\mathbf{x}_{T}^{u,\text{reference}} = \mathbf{x}_{T}^{u,\text{rrt}}$. $d( \cdot, \cdot )$ computes the Cartesian and angular displacements between two object poses. Given $N_{\text{test}}$ reference trajectories computed from RRT, $\delta_{\text{terminal}}^{i}$ shows that it is the tracking error of the $i$-th result. $\Delta_{\text{terminal}}$ represents the average terminal tracking error over $N_{\text{test}}$ demonstrations. Given two $\Delta_{\text{terminal}}^{A}$ and $\Delta_{\text{terminal}}^{B}$ obtained from controller $A$ and $B$ respectively, relative cost, $\eta_{A}^{B}$ represents how much the tracking errors are different between controller $A$ and $B$.

### VI-B3 Hardware Setup

We use two 7-DoF Kuka iiwa arms for the hardware experiments. The robots run a joint impedance controller. We use a motion capture system to measure the state of the objects.

### VI-C Robustness Tests

To evaluate the robustness of controllers, we consider the perturbations to initial states and the radius of the cylinder.

### VI-C1 Robustness to Initial Condition

After we obtain ${\mathbf{x}^{\text{FOH}}{(t)}},{\mathbf{v}^{\text{FOH}}{(t)}},{\mathbf{K}^{\text{FOH}}{(t)}}$ (see Section [VI-B1](https://arxiv.org/html/2411.06542v4#S6.SS2.SSS1 "VI-B1 Execution in Drake ‣ VI-B Feedback Synthesis ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")), we add perturbations $\left( {\delta x},{\delta y},{\delta\theta} \right)$ to the initial states of cylinder in Drake (i.e., ${\text{x}^{u,\text{mea}}{}}\leftarrow{{\text{x}^{u,\text{mea}}{}} + {\lbrack{\delta x},{\delta y},{\delta\theta}\rbrack}^{\top}}$) and then we start rolling out the controller in Drake. We consider 50 points $(\delta x,\delta y,\delta\theta) \sim {Uniform}{\lbrack{\lbrack - \delta x_{0}, + \delta x_{0}\rbrack} \times {\lbrack - \delta y_{0}, + \delta y_{0}\rbrack} \times {\lbrack - \delta\theta_{0}, + \delta\theta_{0}\rbrack})}$ per reference trajectory where ${{\delta x_{0}} = {\delta y_{0}} = {0.025\ m}},{{\delta\theta_{0}} = {5\ {^\circ}}}$.

### VI-C2 Robustness to Variation in Shape

After we obtain ${\mathbf{x}^{\text{FOH}}{(t)}},{\mathbf{v}^{\text{FOH}}{(t)}},{\mathbf{K}^{\text{FOH}}{(t)}}$, we add perturbations $\delta r$ to the radius of cylinder, $r$, in Drake (i.e., $r\leftarrow{r + {\delta r}}$) and then we start rolling out the controller in Drake with this updated $r$. We consider 20 points $\delta r, \sim {Uniform}{\lbrack{\lbrack - \delta r_{0}, + \delta r_{0}\rbrack})}$ per reference trajectory where ${\delta r_{0}} = {0.01\ m}$.

### VI-D Results of SP-TrajOPT

Figure 4: Reference trajectories on which SP-TrajOPT ran successfully.

Fig. (https://arxiv.org/html/2411.06542v4#S6.F4 "Figure 4 ‣ VI-D Results of SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") shows the coverage of SP-TrajOPT. Fig. (https://arxiv.org/html/2411.06542v4#S6.F3 "Figure 3 ‣ VI-A Experimental Setup ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") and Fig. (https://arxiv.org/html/2411.06542v4#S6.F4 "Figure 4 ‣ VI-D Results of SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") shows that SP-TrajOPT could successfully converge given reference trajectories by RRT. The success rate of SP-TrajOPT given 340 reference trajectories is 82.8%. We believe that this success rate is relatively high compared to other contact-implicit trajectory optimization frameworks. We think this is because the contact complementarity constraints are implicitly imposed through $f_{\kappa}$ in our formulation. We also observe that the average position and orientation errors of the cylinder are reduced, from $0.18\ m$ and $71.9\ {^\circ}$ with RRT to $0.14\ m$ and $55.0\ {^\circ}$ with SP-TrajOPT, respectively. Hence, our SP-TrajOPT could successfully generate more optimal trajectories.

### VI-E Results of LQR with SP-TrajOPT

(a) Terminal position error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 0.046 m and 0.30 m, respectively.

(b) Terminal orientation error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 20.9 ∘ and 17.1 ∘.

Figure 5: We evaluate terminal pose tracking error δterminal of cylinder using SP-TrajOPT with / without LQR under perturbation of initial conditions. Note that cdf stands for cumulative distribution function.

(a) Terminal position error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 0.034 m and 0.21 m, respectively.

(b) Terminal orientation error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 19.7 ∘ and 20.2 ∘.

Figure 6: We evaluate terminal pose tracking error δterminal of cylinder using SP-TrajOPT with / without LQR under variation in shape.

### VI-E1 Perturbations to Initial Conditions

Fig. (https://arxiv.org/html/2411.06542v4#S6.F5 "Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") shows SP-TrajOPT and LQR across variations of initial conditions for the cylinder. In Fig. [5(a)](https://arxiv.org/html/2411.06542v4#S6.F5.sf1 "Figure 5(a) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), SP-TrajOPT outperforms LQR. In Fig. [5(b)](https://arxiv.org/html/2411.06542v4#S6.F5.sf2 "Figure 5(b) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), both controllers show similar performance while SP-TrajOPT with LQR shows slightly better $\Delta_{\text{terminal}}$.

### VI-E2 Perturbations to Shape

The results of perturbations to the radius of the cylinder are shown in Fig. (https://arxiv.org/html/2411.06542v4#S6.F6 "Figure 6 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). SP-TrajOPT outperforms SP-TrajOPT with LQR in both position and orientation tracking errors.

### VI-F Results of MP-TrajOPT

Figure 7: Reference trajectories on which MP-TrajOPT ran successfully.

Fig. (https://arxiv.org/html/2411.06542v4#S6.F7 "Figure 7 ‣ VI-F Results of MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") shows the coverage of MP-TrajOPT. Compared to the result of SP-TrajOPT in Fig. (https://arxiv.org/html/2411.06542v4#S6.F4 "Figure 4 ‣ VI-D Results of SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), we observe that MP-TrajOPT shows much smaller coverage. The success rate of MP-TrajOPT is 10.6 %, which is much lower than that of SP-TrajOPT. This is because MP-TrajOPT is much more complex than SP-TrajOPT, and thus, SNOPT might not be able to make any progress during optimization due to many reasons, such as poor scaling of the optimization problem.

### VI-G Results of LQR with MP-TrajOPT

(a) Terminal position error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 0.027 m and 0.10 m, respectively.

(b) Terminal orientation error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 8.9 ∘ and 5.2 ∘.

Figure 8: We evaluate terminal pose tracking error δterminal of cylinder using MP-TrajOPT with / without LQR under perturbation of initial conditions.

(a) Terminal position error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 0.019 m and 0.059 m, respectively.

(b) Terminal orientation error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 8.8 ∘ and 6.8 ∘.

Figure 9: We evaluate terminal pose tracking error δterminal of cylinder using MP-TrajOPT with / without LQR under variation in shape.

### VI-G1 Perturbations to Initial Conditions

The results of perturbations to initial conditions are shown in Fig. (https://arxiv.org/html/2411.06542v4#S6.F8 "Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). While MP-TrajOPT outperforms MP-TrajOPT with LQR in Fig. [8(a)](https://arxiv.org/html/2411.06542v4#S6.F8.sf1 "Figure 8(a) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), the relative cost in Fig. [8(a)](https://arxiv.org/html/2411.06542v4#S6.F8.sf1 "Figure 8(a) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 3.7$. Since $\eta$ in Fig. [5(a)](https://arxiv.org/html/2411.06542v4#S6.F5.sf1 "Figure 5(a) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 6.5$, we argue that MP-TrajOPT improves the LQR performance. For the orientation tracking error, Fig. [8(b)](https://arxiv.org/html/2411.06542v4#S6.F8.sf2 "Figure 8(b) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") shows that MP-TrajOPT with LQR outperforms MP-TrajOPT while in Fig. [5(b)](https://arxiv.org/html/2411.06542v4#S6.F5.sf2 "Figure 5(b) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), SP-TrajOPT outperforms SP-TrajOPT with LQR. Therefore, we observe that MP-TrajOPT introduces some robustness, resulting in improved LQR performance. Also, $\eta$ in Fig. [8(b)](https://arxiv.org/html/2411.06542v4#S6.F8.sf2 "Figure 8(b) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 0.58$ while $\eta$ in Fig. [5(b)](https://arxiv.org/html/2411.06542v4#S6.F5.sf2 "Figure 5(b) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 0.82$. Although our MP-TrajOPT is not designed to be robust against variation in initial conditions, the result suggests that the inherent robustness against parametric uncertainty of the model contributes to robustness under variation in initial conditions.

### VI-G2 Perturbations to Shape

The results are shown in Fig. (https://arxiv.org/html/2411.06542v4#S6.F9 "Figure 9 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). We observe that the performance of LQR improves. The relative cost in Fig. [9(a)](https://arxiv.org/html/2411.06542v4#S6.F9.sf1 "Figure 9(a) ‣ Figure 9 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") and Fig. [6(a)](https://arxiv.org/html/2411.06542v4#S6.F6.sf1 "Figure 6(a) ‣ Figure 6 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 3.1$ and $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 6.2$, respectively. Similarly, the relative cost in Fig. [9(b)](https://arxiv.org/html/2411.06542v4#S6.F9.sf2 "Figure 9(b) ‣ Figure 9 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") and Fig. [6(b)](https://arxiv.org/html/2411.06542v4#S6.F6.sf2 "Figure 6(b) ‣ Figure 6 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 0.77$ and $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 1.01$, respectively. Therefore, we observe that MP-TrajOPT and LQR work synergistically. However, these improvements can be observed only when MP-TrajOPT is solved, which is often difficult.

### VI-H Hardware Experiments

We implement two controllers, open-loop using SP-TrajOPT and LQR controllers, and evaluate their tracking performance in hardware experiments. As shown in Fig. (https://arxiv.org/html/2411.06542v4#S1.F1 "Figure 1 ‣ I Introduction ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), we observe that LQR could track the specific reference trajectory with perturbations to the initial states.

## Closer Look at LQR

### VII-A Results of Different Smoothing

(a) Simulation result of LQR with cylinder with κ = 160.

(b) Simulation result of LQR with cylinder with κ = 800.

Figure 10: Snapshots along a trajectory simulated in Drake. We implement LQR with the cylinder with different smoothing parameters κ for the same reference trajectory with the same initial condition perturbations. The snapshots show the cylinder frame and the desired frame at the terminal time step. Green lines represent contact forces. At t = 1.6 s, the right arm in Fig. 10(a) loses the contact and causes pulling motion while the right arm in Fig. 10(b) maintains the contact. As a result, LQR in Fig. 10(a) fails to track the reference trajectory while LQR in Fig. 10(b) could successfully track it.

(a) Terminal position error

(b) Terminal orientation error

Figure 11: Terminal pose tracking error Δterminal with different smoothing values κ using LQR with perturbations of initial conditions. In the figures, we show the bar indicating the mean and 95% confidence interval.

We discuss the relation between the behavior of LQR and the smoothing parameter $\kappa$. Here we have two results using LQR with $\kappa = 160$ (i.e., more smoothing) and $\kappa = 800$ (i.e., less smoothing) for the same reference trajectory with the same perturbations of initial conditions used in Section [VI-C1](https://arxiv.org/html/2411.06542v4#S6.SS3.SSS1 "VI-C1 Robustness to Initial Condition ‣ VI-C Robustness Tests ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"). Fig. (https://arxiv.org/html/2411.06542v4#S7.F10 "Figure 10 ‣ VII-A Results of Different Smoothing ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") shows the snapshots along the trajectory during the simulation in Drake.

With $\kappa = 160$, LQR makes the robot try to pull the cylinder even with no contact at $t = 1.6$ s in Fig. [10(a)](https://arxiv.org/html/2411.06542v4#S7.F10.sf1 "Figure 10(a) ‣ Figure 10 ‣ VII-A Results of Different Smoothing ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") due to large contact smoothing. Through the experiments, we observe that a common rule of thumb for designing LQR with good tracking performance is to choose a large $\kappa$ - if $\kappa$ is too small, the controller will cause undesired pushing and pulling motion of the robot as shown in Fig. (https://arxiv.org/html/2411.06542v4#S7.F11 "Figure 11 ‣ VII-A Results of Different Smoothing ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?").

### VII-B Fundamental Shortcomings of Linearization

Figure 12: Illustration of how LQR behaves in a 1D ball-pushing environment, where the red actuated ball tries to push the green unactuated ball using control inputs derived from LQR. The dotted balls in the left column denote the nominal state where linearization is done, and the solid balls illustrate the current state. The right columns illustrate the smoothed dynamics, linearized dynamics, and the optimal LQR solution according to linearization. The top row and bottom row illustrate two cases of disturbances, where the top row can be stabilized by pushing, but the bottom row requires pulling.

We here analyze why LQR does not work well on top of SP-TrajOPT-generated trajectories. One limitation of LQR is that the linearization does not sufficiently capture the *unilateral* nature of contact. To illustrate this, we consider a 1-step LQR problem in ((https://arxiv.org/html/2411.06542v4#Sx1.EGx6 "Equation 8 ‣ VII-B Fundamental Shortcomings of Linearization ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")),

$\min\limits_{\mathbf{\Delta}\mathbf{v}_{0}}$ $\left\| {\mathbf{\Delta}\mathbf{x}_{1}} \right\|_{\mathbf{P}_{1}}^{2}$ (8a)
s.t. ${{\mathbf{\Delta}\mathbf{x}_{1}} = {{\mathbf{A}_{0}\mathbf{\Delta}\mathbf{x}_{0}} + {\mathbf{B}_{0}\mathbf{\Delta}\mathbf{v}_{0}}}},$ (8b)
${{\mathbf{\Delta}\mathbf{x}_{0}} = {\hat{\mathbf{x}} - \mathbf{x}_{0}}}.$ (8c)

Consider a simple 1D block-pushing system (Fig. (https://arxiv.org/html/2411.06542v4#S7.F12 "Figure 12 ‣ VII-B Fundamental Shortcomings of Linearization ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")), where an actuated block is trying to push an unactuated block into a desired location. When we visualize the linearized dynamics in Fig. (https://arxiv.org/html/2411.06542v4#S7.F12 "Figure 12 ‣ VII-B Fundamental Shortcomings of Linearization ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), we can observe that in cases where the red ball must *push* to stabilize, this 1-step LQR takes a step in the right direction although overshooting occurs (Fig. (https://arxiv.org/html/2411.06542v4#S7.F12 "Figure 12 ‣ VII-B Fundamental Shortcomings of Linearization ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), top row). If we ask LQR to recover from overshooting (Fig. (https://arxiv.org/html/2411.06542v4#S7.F12 "Figure 12 ‣ VII-B Fundamental Shortcomings of Linearization ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), bottom row), however, a linearized model predicts that it can pull the object and take a step towards the opposite direction. Yet, due to the directional nature of contact, this has no effect on the unactuated ball. This mismatch between the linearized model and the true model leads to limitations of the LQR controller. We observe this pulling motion in Fig. (https://arxiv.org/html/2411.06542v4#S7.F10 "Figure 10 ‣ VII-A Results of Different Smoothing ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") in Section [VII-A](https://arxiv.org/html/2411.06542v4#S7.SS1 "VII-A Results of Different Smoothing ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?").

The symmetric nature of local linear models is fundamentally at odds with the unilateralness of contact. We address this challenge in \[(https://arxiv.org/html/2411.06542v4#bib.bib34)\], where we build a *trust region* in which the linearization is locally consistent with contact dynamics.

## Conclusion

Is linear feedback on smoothed dynamics sufficient for stabilizing contact-rich plans? Our analysis and experiments suggest that designing LQR for contact-rich plans does not work well in general. However, we observe that MP-TrajOPT enables LQR to improve its performance when MP-TrajOPT is solved, although MP-TrajOPT often fails to converge. Through this paper, we first present how contact smoothing technique can be used for designing trajectory optimization baselines and LQR. Then, we extensively conduct various experiments of LQR under different uncertainties. We hope that our analysis provides readers with insights into design of planners and controllers for contact-rich manipulation using differential simulators based on contact smoothing.
