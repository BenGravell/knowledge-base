<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?

Topics include Robotics, Robustness, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Designing planners and controllers for contact-rich manipulation is extremely challenging as contact violates the smoothness conditions that many gradient-based controller synthesis tools assume. Contact smoothing approximates a non-smooth system with a smooth one, allowing one to use these synthesis tools more effectively. However, applying classical control synthesis methods to smoothed contact dynamics remains relatively under-explored. This paper analyzes the efficacy of linear controller synthesis using differential simulators based on contact smoothing. We introduce natural baselines for leveraging contact smoothing to compute (a) open-loop plans robust to uncertain conditions and/or dynamics, and (b) feedback gains to stabilize around open-loop plans. Using robotic bimanual whole-body manipulation as a testbed, we perform extensive empirical experiments on over 300 trajectories and analyze why LQR seems insufficient for stabilizing contact-rich plans.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dexterous manipulation is full of contact-rich interactions, enabling various tasks through complex frictional interactions. Historically, the non-smooth nature of contact has precluded a range of planning and control methods that rely on gradients of the dynamics. Recent advances have utilized *contact smoothing* --- where non-smooth dynamics are replaced by a continuously differentiable proxy --- to great effect as surrogate dynamics models for *planning* through contact. One may hope, then, that smoothing enables the use gradient-based *control*.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work suggests that the above hope may face significant obstacles. We introduce LQR control for contact-manipulation via contact smoothing. Furthermore, we present and analyze robust trajectory optimization, hoping that the generated trajectories are robust to the model errors accumulated by using a surrogate dynamics model for control, and thus more amenable to LQR. Then, we extensively evalute the performance of these methods, both in simulation and in hardware, on a bimanual whole-body manipulation as shown in Fig..

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

> *Despite its efficacy in planning through contact, dynamical smoothing alone is unsatisfactory as a means to obtaining linear control policies.*

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we identify the key factors leading to the inadequacies of linear control; namely, the *unilaterality* of contact, and the tendency of controllers to "push and pull" unless the dynamics are only very-slightly smoothed.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Planning through Contact", "weight": 1.0} -->

One approach to motion-planning through contact enforces contact dynamics by including linear complementarity constraints. Another popular method to address contacts is based on Mixed-Integer Programming (MIP), where discrete variables encode contact modes. However, due to the inherent non-smoothness of contact dynamics, both methods suffer from poor scalability as the number of contact modes increases.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Planning through Contact", "weight": 1.0} -->

To tackle this, contact smoothing has been proposed, replacing exact dynamics models with surrogate models that obey second-order smoothness. This approach introduces a "force-at-a-distance" effect where gradients through the dynamics convey information about nearby contacts. Since gradients of the dynamics become continuous, gradient-based optimizers are able to find solutions more efficiently. Our work employs a log-barrier smoothing scheme, which is more efficient compared to stochastic smoothing schemes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Control through Contact", "weight": 1.0} -->

Prior approaches to control through contact reason about contact modes. While these approaches can run in real time for simple systems with only a handful of contact modes, they have yet to scale to high-dimensional systems, multiple objects per scene, or contacts with objects of complex and/or irregular shapes due to the expensive computation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Control through Contact", "weight": 1.0} -->

In contrast, contact-smoothing offers a way to directly apply *smooth* control methods while being less constrained by the non-smoothness of contact dynamics, at the cost of introducing some smoothing bias. In this work, we study LQR, which uses the underlying problem structure provided by contact smoothing, enabling its application to high-dimensional bimanual whole-body manipulation tasks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-C Robust Planning through Contact", "weight": 1.0} -->

Previous work on robust planning through contact generally falls into two approaches: *domain randomization*, which involves stochastic optimization over a fixed distribution of dynamics models, and *worst-case optimization*, which focuses on performance under worst-case scenarios within an uncertainty set. These methods effectively handle parametric uncertainties in the system dynamics, such as mass and friction, but do not discuss shape uncertainty (e.g., the radius of a cylinder). Shape uncertainty is critical for generalized manipulation to avoid unexpected contact events, yet integrating it into system dynamics remains challenging.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-C Robust Planning through Contact", "weight": 1.0} -->

In this work, we incorporate domain randomization with an emphasis on shape uncertainty for primitive objects. Using contact smoothing, our method incorporates smoothed collision dynamics, enabling robust optimization to consider shape uncertainty. We also hope that using our technique enables LQR to track reference trajectories more easily.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We focus on the manipulation of rigid objects. Throughout, we focus on bimanual tabletop manipulation, though in principle our approach extends beyond this regime.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Quasi-Dynamic Dynamics Model", "weight": 1.0} -->

We generate plans and linear feedback gains by considering a quasi-dynamic model of a robot manipulating a single rigid object. We consider robots with $n_{a}$ actuated Degrees of Freedom (DoFs) and the objects with $n_{u}$ unactuated DoFs. We denote the configurations of the object and the robot as $\mathbf{q}^{u} \in {\mathbb{R}}^{n_{u}}$ and $\mathbf{q}^{a} \in {\mathbb{R}}^{n_{a}}$, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Quasi-Dynamic Dynamics Model", "weight": 1.0} -->

We denote the control input as $\mathbf{u} \in {\mathbb{R}}^{n_{a}}$, defined as the commanded positions of the robot's joints. We consider the linear feedback law $\mathbf{u} = {\mathbf{v} + {\mathbf{K}\mathbf{\Delta}\mathbf{x}}}$ where $\mathbf{v} \in {\mathbb{R}}^{n_{a}}$ is the feedforward gain from trajectory optimization, $\mathbf{K} \in {\mathbb{R}}^{n_{a} \times n_{x}}$ is the feedback gain computed by LQR, and $\mathbf{\Delta}\mathbf{x}$ is the state error, or deviation from nomial trajectory.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Quasi-Dynamic Dynamics Model with Contact Smoothing", "weight": 1.0} -->

For computing ${\mathbf{δ}}\mathbf{q}$, we consider a log-barrier-smoothed formulation of quasi-dynamic dynamics from Eq.. We denote $\kappa$-smoothed forward dynamic map as

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Quasi-Dynamic Dynamics Model with Contact Smoothing", "weight": 1.0} -->

where $\kappa > 0$ is the user-defined barrier parameter. Smaller $\kappa$ corresponds to greater contact smoothing, and more "force at a distance". Recalling our notation $\mathbf{x} = \mathbf{q}$, the above can also be written as $\mathbf{x}_{t + 1} = {f_{\kappa}\left( \mathbf{x}_{t},\mathbf{u}_{t} \right)}$. When $\kappa$ does not change, we will simply write $f$ for $f_{\kappa}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Quasi-Dynamic Dynamics Model with Contact Smoothing", "weight": 1.0} -->

Both our gradient descent-based trajectory optimizer and our synthesis of linear feedback rely on differentiation of the smoothed dynamics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Quasi-Dynamic Dynamics Model with Contact Smoothing", "weight": 1.0} -->

See for the complete derivation of. Again, we use the shorthand $\mathbf{A} = \mathbf{A}_{\kappa}$ and $\mathbf{B} = \mathbf{B}_{\kappa}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Parametrized Quasi-Dynamic Dynamics Model", "weight": 1.0} -->

As described in Sec II-C, we consider *uncertainty over the dynamics* induced by object uncertainty. These can be parameterized by a parameter $\mathbf{p} \in U \subseteq {\mathbb{R}}^{n_{p}}$ which enters into $f_{\kappa}$. To lighten notation, we also let the parameter $\mathbf{p}$ encode an initial condition, $\mathbf{x}_{init}{(\mathbf{p})}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contact-Implicit Trajectory Optimization", "weight": 1.0} -->

In this section, we present both single-parameter and multi-parameter trajectory optimization baselines.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT)", "weight": 1.0} -->

We formulate our optimal planning problem as follows.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT)", "weight": 1.0} -->

where $\mathcal{T}:={\{ 0,\ldots,{T - 1}\}}$, $J$ is the trajectory-wise cost function, $f = f_{\kappa}$ is the contact dynamics of the system (see ). $\mathbf{v}_{t}$ is the control input at time step $t$. (3c ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")) is used to impose inequality constraints involving $\mathbf{x}_{t}$ and $\mathbf{v}_{t}$ such as joint torque constraints and non-collision constraints. $\mathcal{X}$ and $\mathcal{V}$ represent a convex polytope, consisting of a finite number of linear inequality constraints for bounding the decision variables.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Single-Parameter Trajectory Optimization (SP-TrajOPT)", "weight": 1.0} -->

In (3e ‣ IV Contact-Implicit Trajectory Optimization ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?")), the initial condition encoded by $\mathbf{p}^{i}$ determines the initial state $\mathbf{x}_{0}$ (see Section III-C).

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Multi-Parameter Trajectory Optimization (MP-TrajOPT)", "weight": 1.0} -->

An alternative to ) is a robust formulation over multiple parameters. We focus on the simplest approach: optimizing average performance on $N$ realizations ${(\mathbf{p}^{i})}_{1 \leq i \leq N}$, which for simplicity are manually chosen, inspired, using Sample Average Approximation (SAA). For each $\mathbf{p}^{i}$, we optimize over a corresponding trajectories ${(\mathbf{x}^{i})}_{1 \leq i \leq N}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Multi-Parameter Trajectory Optimization (MP-TrajOPT)", "weight": 1.0} -->

where $\mathbf{X}:={\{\mathbf{x}_{t}^{i},\forall t \in \mathcal{T},\forall i \in \mathcal{I}\}}$, $\mathcal{I}:={\{ 0,\ldots,{N - 1}\}}$. We emphasize that we do not have superscript $i$ on $\mathbf{v}_{t}$ because our objective is to design a single plan that succeeds on average over the $N$ parameters. Note that ) with $N = 1$ specializes to ). We call this SP-TrajOPT (Single- Parameter Trajectory Optimization) as it only considers a single parameter. For $N > 1$, we refer to the procedure as MP-TrajOPT (Multi-Parameter Trajectory Optimization).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Feedback Synthesis via LQR", "weight": 1.0} -->

In this section, we present an approach to feedback gain synthesis by solving an LQR problem through linearizations of the contact smoothed dynamics.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Feedback Synthesis via LQR", "weight": 1.0} -->

Using, we can compute LQR feedback gains $\mathbf{K}$. The objective of using LQR is to design a controller that can locally stabilize the system. In this work, we consider the following optimal control problem given $\mathbf{x}_{t}$ and ${\mathbf{v}_{t},t} \in \mathcal{T}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Feedback Synthesis via LQR", "weight": 1.0} -->

where $\mathbf{Q}_{t} = \mathbf{Q}_{t}^{\top}$ is positive semidefinite and $\mathbf{R}_{t} = \mathbf{R}_{t}^{\top}$ is positive definite at $t$. $\hat{\mathbf{x}}$ is the measurement of states at $t = 0$. $\mathbf{A}_{t}$ and $\mathbf{B}_{t}$ are error dynamics, which are obtained by linearizing true nonlinear contact dynamics of the system $f$ around $\mathbf{x}_{t}$ and ${\mathbf{v}_{t},t} \in \mathcal{T}$ in accordance with Sec.III-B. It is worth noting again that $\mathbf{A}_{t}$ and $\mathbf{B}_{t}$ convey local contact information of the system dynamics. We use Riccati recursion to compute $\mathbf{K}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Feedback Synthesis via LQR", "weight": 1.0} -->

All of the computation happens offline. Hence, there is no expensive computation online unlike other methods (e.g., model predictive control).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we demonstrate our proposed controller under various uncertainties such as perturbations of initial conditions and shape variations for a cylinder. Through this section, we answer the following questions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

How well do TrajOPT and LQR work?

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

To what extent does MP-TrajOPT improve the performance of LQR?

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

Under what circumstances do our proposed controllers succeed or fail?

<!-- chunk {"id": "body-0035", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Three sets of parameters are in Table I. For SP-TrajOPT, we use the nominal "(a)" shape in that table; for MP-TrajOPT we use all $N = 3$ "(a)", "(b)" and "(c)" shapes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

Our pipeline is depicted in Fig.. We begin by sampling $N_{\text{test}} = 340$ reference trajectories using RRT with $N_{\text{test}}$ different initial and goal states. RRT uses the nominal "(a)" parameter in Table I. These yield state and feedforward control input sequences, ${\{\left( \mathbf{x}_{t}^{\text{rrt}},\mathbf{v}_{t}^{\text{rrt}} \right)_{1 \leq t \leq T}^{n}\}}_{n = 1}^{N_{\text{test}}}$ as illustrated in Fig..

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

For SP-TrajOPT, we solve ) under the nominal "(a)" parameter. For MP-TrajOPT, we solve ) for all $N = 3$ parameters (note that this produces $N$ sequences of states; we select $\mathbf{x}_{t}^{\text{opt}}$ to be the one under the nominal shape).

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

where $\mathbf{Q}_{t} = {\text{diag}(10,10,10,0.1,0.1,0.1,0.1,0.1,0.1)}$, ${\mathbf{R}_{t} = {\text{diag}}},{{\forall t} \in {\lbrack 0,\ldots,{T - 1}\rbrack}}$, $\mathbf{Q}_{T} = {\text{diag}(1000,1000,1000,0.1,0.1,0.1,0.1,0.1,0.1)}$. We formulate trajectory optimization programs using Drake's MathematicalProgram and solve them using SNOPT. We optimize with dynamic smoothing parameter $\kappa = 10^{5}$. We use $h = 0.1$ seconds as the time step.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-B Feedback Synthesis", "weight": 1.0} -->

For LQR, we compute gains ${\{\left( \mathbf{K}_{t}^{\text{lqr}} \right)^{i}\}}_{i = 1}^{N_{\text{test}}}$ from ${\{\left( \mathbf{x}_{t}^{\text{opt}},\mathbf{v}_{t}^{\text{opt}} \right)^{i}\}}_{i = 1}^{N_{\text{test}}}$. It means that, when the trajectories are supplied by SP- or MP-TrajOPT, gains are computed around the nominal parameter dynamics, (a) parameter in Table I. We use $h = 0.1$ seconds as the time step, but use a smaller smoothing parameter, $\kappa = 800$, for smoother derivatives.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-B1 Execution in Drake", "weight": 1.0} -->

While plans and gains are synthesized via smoothed quasi-dynamic dynamics, we evaluate performance in either (i) Drake or (ii) on real hardware. The planning/feedback synthesis phase returns a sequence of states, feedforward control inputs, and feedback gains at discrete knot points $\left( \left\{ \mathbf{x}_{t} \right\}_{t = 0}^{T},\left\{ \mathbf{v}_{t} \right\}_{t = 0}^{T - 1},\left\{ \mathbf{K}_{t} \right\}_{t = 0}^{T - 1} \right)$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-B1 Execution in Drake", "weight": 1.0} -->

We adopt a higher control loop frequency in Drake simulations, which necessitates interpolation of these discrete-time quantities. To do so, we convert the knot points into continuous time using First-Order Hold (FOH): states $\mathbf{x}^{\text{FOH}}{(t)}$, feedforward control input $\mathbf{v}^{\text{FOH}}{(t)}$, and feedback control input trajectories $\mathbf{K}^{\text{FOH}}{(t)}$. For $\mathbf{K}^{\text{FOH}}{(t)}$, we interpolate elements of $\mathbf{K}_{t}$ using FOH.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B2 Evaluation Metrics", "weight": 1.0} -->

where $\delta_{\text{terminal}}$ is the tracking error at the terminal time step. The superscript $u$ extracts the elements corresponding to $\mathbf{q}^{u}$ and $\mathbf{x}_{T}^{u,\text{reference}}$ is the reference trajectory the controller tries to track. Through experiments, we consider $\mathbf{x}_{T}^{u,\text{reference}} = \mathbf{x}_{T}^{u,\text{rrt}}$. $d( \cdot, \cdot )$ computes the Cartesian and angular displacements between two object poses. Given $N_{\text{test}}$ reference trajectories computed from RRT, $\delta_{\text{terminal}}^{i}$ shows that it is the tracking error of the $i$-th result. $\Delta_{\text{terminal}}$ represents the average terminal tracking error over $N_{\text{test}}$ demonstrations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B2 Evaluation Metrics", "weight": 1.0} -->

Given two $\Delta_{\text{terminal}}^{A}$ and $\Delta_{\text{terminal}}^{B}$ obtained from controller $A$ and $B$ respectively, relative cost, $\eta_{A}^{B}$ represents how much the tracking errors are different between controller $A$ and $B$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B3 Hardware Setup", "weight": 1.0} -->

We use two 7-DoF Kuka iiwa arms for the hardware experiments. The robots run a joint impedance controller. We use a motion capture system to measure the state of the objects.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-C Robustness Tests", "weight": 1.0} -->

To evaluate the robustness of controllers, we consider the perturbations to initial states and the radius of the cylinder.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-C2 Robustness to Variation in Shape", "weight": 1.0} -->

After we obtain ${\mathbf{x}^{\text{FOH}}{(t)}},{\mathbf{v}^{\text{FOH}}{(t)}},{\mathbf{K}^{\text{FOH}}{(t)}}$, we add perturbations $\delta r$ to the radius of cylinder, $r$, in Drake (i.e., $r\leftarrow{r + {\delta r}}$) and then we start rolling out the controller in Drake with this updated $r$. We consider 20 points $\delta r, \sim {Uniform}{\lbrack{\lbrack - \delta r_{0}, + \delta r_{0}\rbrack})}$ per reference trajectory where ${\delta r_{0}} = {0.01\ m}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-D Results of SP-TrajOPT", "weight": 1.0} -->

Fig. shows the coverage of SP-TrajOPT. Fig. and Fig. shows that SP-TrajOPT could successfully converge given reference trajectories by RRT. The success rate of SP-TrajOPT given 340 reference trajectories is 82.8%. We believe that this success rate is relatively high compared to other contact-implicit trajectory optimization frameworks. We think this is because the contact complementarity constraints are implicitly imposed through $f_{\kappa}$ in our formulation. We also observe that the average position and orientation errors of the cylinder are reduced, from $0.18\ m$ and $71.9\ {^\circ}$ with RRT to $0.14\ m$ and $55.0\ {^\circ}$ with SP-TrajOPT, respectively. Hence, our SP-TrajOPT could successfully generate more optimal trajectories.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-E Results of LQR with SP-TrajOPT", "weight": 1.0} -->

(a) Terminal position error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 0.046 m and 0.30 m, respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-E Results of LQR with SP-TrajOPT", "weight": 1.0} -->

(b) Terminal orientation error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 20.9 ∘ and 17.1 ∘.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-E Results of LQR with SP-TrajOPT", "weight": 1.0} -->

(a) Terminal position error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 0.034 m and 0.21 m, respectively.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-E Results of LQR with SP-TrajOPT", "weight": 1.0} -->

(b) Terminal orientation error. Δterminal of SP-TrajOPT and SP-TrajOPT with LQR is 19.7 ∘ and 20.2 ∘.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-E1 Perturbations to Initial Conditions", "weight": 1.0} -->

Fig. shows SP-TrajOPT and LQR across variations of initial conditions for the cylinder. In Fig. 5(a) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), SP-TrajOPT outperforms LQR. In Fig. 5(b) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), both controllers show similar performance while SP-TrajOPT with LQR shows slightly better $\Delta_{\text{terminal}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-E2 Perturbations to Shape", "weight": 1.0} -->

The results of perturbations to the radius of the cylinder are shown in Fig.. SP-TrajOPT outperforms SP-TrajOPT with LQR in both position and orientation tracking errors.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-F Results of MP-TrajOPT", "weight": 1.0} -->

Fig. shows the coverage of MP-TrajOPT. Compared to the result of SP-TrajOPT in Fig., we observe that MP-TrajOPT shows much smaller coverage. The success rate of MP-TrajOPT is 10.6 %, which is much lower than that of SP-TrajOPT. This is because MP-TrajOPT is much more complex than SP-TrajOPT, and thus, SNOPT might not be able to make any progress during optimization due to many reasons, such as poor scaling of the optimization problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-G Results of LQR with MP-TrajOPT", "weight": 1.0} -->

(a) Terminal position error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 0.027 m and 0.10 m, respectively.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-G Results of LQR with MP-TrajOPT", "weight": 1.0} -->

(b) Terminal orientation error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 8.9 ∘ and 5.2 ∘.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-G Results of LQR with MP-TrajOPT", "weight": 1.0} -->

(a) Terminal position error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 0.019 m and 0.059 m, respectively.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-G Results of LQR with MP-TrajOPT", "weight": 1.0} -->

(b) Terminal orientation error. Δterminal of MP-TrajOPT and MP-TrajOPT with LQR is 8.8 ∘ and 6.8 ∘.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-G1 Perturbations to Initial Conditions", "weight": 1.0} -->

The results of perturbations to initial conditions are shown in Fig.. While MP-TrajOPT outperforms MP-TrajOPT with LQR in Fig. 8(a) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), the relative cost in Fig. 8(a) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 3.7$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-G1 Perturbations to Initial Conditions", "weight": 1.0} -->

Since $\eta$ in Fig. 5(a) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 6.5$, we argue that MP-TrajOPT improves the LQR performance. For the orientation tracking error, Fig. 8(b) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") shows that MP-TrajOPT with LQR outperforms MP-TrajOPT while in Fig. 5(b) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?"), SP-TrajOPT outperforms SP-TrajOPT with LQR.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-G1 Perturbations to Initial Conditions", "weight": 1.0} -->

Therefore, we observe that MP-TrajOPT introduces some robustness, resulting in improved LQR performance. Also, $\eta$ in Fig. 8(b) ‣ Figure 8 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 0.58$ while $\eta$ in Fig. 5(b) ‣ Figure 5 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 0.82$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-G1 Perturbations to Initial Conditions", "weight": 1.0} -->

Although our MP-TrajOPT is not designed to be robust against variation in initial conditions, the result suggests that the inherent robustness against parametric uncertainty of the model contributes to robustness under variation in initial conditions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-G2 Perturbations to Shape", "weight": 1.0} -->

The results are shown in Fig.. We observe that the performance of LQR improves. The relative cost in Fig. 9(a) ‣ Figure 9 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") and Fig. 6(a) ‣ Figure 6 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 3.1$ and $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 6.2$, respectively.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-G2 Perturbations to Shape", "weight": 1.0} -->

Similarly, the relative cost in Fig. 9(b) ‣ Figure 9 ‣ VI-G Results of LQR with MP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") and Fig. 6(b) ‣ Figure 6 ‣ VI-E Results of LQR with SP-TrajOPT ‣ VI Results ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") is $\eta_{\text{MP-TrajOPT}}^{\text{MP-TrajOPT + LQR}} = 0.77$ and $\eta_{\text{SP-TrajOPT}}^{\text{SP-TrajOPT + LQR}} = 1.01$, respectively. Therefore, we observe that MP-TrajOPT and LQR work synergistically. However, these improvements can be observed only when MP-TrajOPT is solved, which is often difficult.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VI-H Hardware Experiments", "weight": 1.0} -->

We implement two controllers, open-loop using SP-TrajOPT and LQR controllers, and evaluate their tracking performance in hardware experiments. As shown in Fig., we observe that LQR could track the specific reference trajectory with perturbations to the initial states.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VII-A Results of Different Smoothing", "weight": 1.0} -->

(a) Simulation result of LQR with cylinder with κ = 160.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VII-A Results of Different Smoothing", "weight": 1.0} -->

(b) Simulation result of LQR with cylinder with κ = 800.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VII-A Results of Different Smoothing", "weight": 1.0} -->

We discuss the relation between the behavior of LQR and the smoothing parameter $\kappa$. Here we have two results using LQR with $\kappa = 160$ (i.e., more smoothing) and $\kappa = 800$ (i.e., less smoothing) for the same reference trajectory with the same perturbations of initial conditions used in Section VI-C1. Fig. shows the snapshots along the trajectory during the simulation in Drake.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VII-A Results of Different Smoothing", "weight": 1.0} -->

With $\kappa = 160$, LQR makes the robot try to pull the cylinder even with no contact at $t = 1.6$ s in Fig. 10(a) ‣ Figure 10 ‣ VII-A Results of Different Smoothing ‣ VII A Closer Look at LQR ‣ Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans?") due to large contact smoothing. Through the experiments, we observe that a common rule of thumb for designing LQR with good tracking performance is to choose a large $\kappa$ - if $\kappa$ is too small, the controller will cause undesired pushing and pulling motion of the robot as shown in Fig..

<!-- chunk {"id": "body-0070", "role": "body", "section": "VII-B Fundamental Shortcomings of Linearization", "weight": 1.0} -->

We here analyze why LQR does not work well on top of SP-TrajOPT-generated trajectories. One limitation of LQR is that the linearization does not sufficiently capture the *unilateral* nature of contact. To illustrate this, we consider a 1-step LQR problem,

<!-- chunk {"id": "body-0071", "role": "body", "section": "VII-B Fundamental Shortcomings of Linearization", "weight": 1.0} -->

Consider a simple 1D block-pushing system, where an actuated block is trying to push an unactuated block into a desired location. When we visualize the linearized dynamics in Fig., we can observe that in cases where the red ball must *push* to stabilize, this 1-step LQR takes a step in the right direction although overshooting occurs. If we ask LQR to recover from overshooting, however, a linearized model predicts that it can pull the object and take a step towards the opposite direction. Yet, due to the directional nature of contact, this has no effect on the unactuated ball. This mismatch between the linearized model and the true model leads to limitations of the LQR controller. We observe this pulling motion in Fig. in Section VII-A.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VII-B Fundamental Shortcomings of Linearization", "weight": 1.0} -->

The symmetric nature of local linear models is fundamentally at odds with the unilateralness of contact. We address this challenge, where we build a *trust region* in which the linearization is locally consistent with contact dynamics.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Is linear feedback on smoothed dynamics sufficient for stabilizing contact-rich plans? Our analysis and experiments suggest that designing LQR for contact-rich plans does not work well in general. However, we observe that MP-TrajOPT enables LQR to improve its performance when MP-TrajOPT is solved, although MP-TrajOPT often fails to converge. Through this paper, we first present how contact smoothing technique can be used for designing trajectory optimization baselines and LQR. Then, we extensively conduct various experiments of LQR under different uncertainties. We hope that our analysis provides readers with insights into design of planners and controllers for contact-rich manipulation using differential simulators based on contact smoothing.
