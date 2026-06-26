<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Contraction L1-Adaptive Control Using Gaussian Processes

Topics include Aerial robotics, Safety, Gaussian processes, Bayesian methods, Regression, Control, Learning, GP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present CL_1-GP, a control framework that enables safe simultaneous learning and control for systems subject to uncertainties. The two main constituents are contraction theory-based L_1 (CL_1) control and Bayesian learning in the form of Gaussian process (GP) regression. The CL_1 controller ensures that control objectives are met while providing safety certificates. Furthermore, CL_1-GP incorporates any available data into a GP model of uncertainties, which improves performance and enables the motion planner to achieve optimality safely. This way, the safe operation of the system is always guaranteed, even during the learning transients. We provide a few illustrative examples for the safe learning and control of planar quadrotor systems in a variety of environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A majority of planning algorithms based on model predictive control (MPC) and model-based reinforcement learning (MBRL) compute optimal control sequences using a nominal or learned system model. However, models have inaccuracies and the robot may behave sub-optimally. In the worst cases, the system will become unstable or collide with obstacles. These model inaccuracies have especially serious consequences for safety-critical systems. Machine learning (ML) algorithms have been proven to be potent tools for learning complex and accurate models in robotics, improving performance. However, the robot's safety during the learning transients is not always guaranteed. For instance, a robot may enter unsafe regions while collecting data because it does not take into account the model inaccuracies.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control-theoretic approaches that offer safety certificates based on Lyapunov functions and robust control invariant sets are gaining popularity in the context of safe robot learning. Many recent safe-learning examples establish the notion of asymptotic stability with control-theoretic tools \[16, Chapter 3\]. Although critically important, asymptotic stability by itself is not sufficient for the safe operation of robots. Safety must be guaranteed during the learning process with transient bounds. Techniques like uncertainty propagation have been proposed to characterize transient performance using learned statistical models. However, methods based on uncertainty propagation are often approximate, computationally expensive for planning, and do not provide apriori certificates of safety.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We propose a learning-based control framework using robust adaptive control theory for nonlinear systems that ensures improvement of optimality and performance while simultaneously guaranteeing safety which we refer to as $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ control. The safety guarantees are composed of apriori computable transient performance bounds and robustness margins. We rely on Bayesian learning in the form of GP regression to learn the state and time-dependent model uncertainties from noisy measurements. We use the predictive distribution provided by GP learning to compute high-probability error bounds for the estimated uncertainties. These estimates are then incorporated within the $\mathcal{C}\mathcal{L}_{1}$ robust adaptive control framework recently presented. Our $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ control framework is planner-agnostic and is designed to work with any planner capable of generating desired state and control trajectories using the known (learned or nominal) model.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

This feature enables the framework to be used in conjunction with many popular planning algorithms such as differential dynamic programming, model predictive path integral control, and sampling-based planners, among many others.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

A critical feature of the $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ framework is that it enables MBRL algorithms to achieve optimality as learning progresses but the safety is guaranteed at all times regardless of the quality of the learned model. We define safety using the performance bounds and the robustness margins associated with the controller. The performance bounds quantify how far the system trajectory may deviate from the desired trajectory based on the amount of unmodeled uncertainty. The robustness of the controlled system is a function of the available sensors, actuators, and computational hardware. The $\mathcal{C}\mathcal{L}_{1}$ controller provides a sensible approach to balance the trade-off between performance and robustness requirements for safe navigation. However, this trade-off implies that for a specification of robustness margins there is limit on how tight the performance bounds can get. Our framework addresses this problem by using model learning to reduce the effect of the uncertainty which results in tighter performance bounds than would be possible with alone.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Moreover, the improved model knowledge and the tighter performance bounds are then incorporated into the planner used by the MBRL algorithm to generate more optimal but still safe trajectories as shown in Figure 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The functions $f{(x)}$, $B{(x)}$, and $h{(\xi,x)}$ are continuous, bounded, and Lipschitz in $x$, uniformly in $\xi$, for all $\xi \in {\mathbb{R}}^{l}$, and for all $x \in D \subset {\mathbb{R}}^{n}$, where $D$ is a compact set which can be arbitrarily large. Moreover, $B{(x)}$ has full column rank for all $x \in D$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

For the planning problem to be feasible with respect to the robot's dynamic capabilities, we provide the following definition.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

Given any tube width $\rho > 0$ and planning horizon $\lbrack 0,T_{f}\rbrack$, $0 < T_{f} \leq \infty$, the planner produces a state-input pair $({x_{d}{(t)}},{u_{d}{(t)}})$ such that the induced tube $\mathcal{O}_{x_{d}}{(\rho)}$ defined in satisfies Furthermore, the desired control input $u_{d}{(t)}$ satisfies with the upper bound known.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

Given any $\rho > 0$, based on Assumptions 2.1-2.3, we have that for all $\xi \in {\mathbb{R}}^{l}$ and the compact convex set $\mathcal{X} \subset {\mathbb{R}}^{n}$ where where ${\lbrack b\rbrack}_{\cdot,j}{(x)}$ denotes the $j^{th}$ column of $B{(x)}$, ${B^{\dagger}{(x)}} = {\left({B^{\top}{(x)}B{(x)}} \right)^{- 1}B^{\top}{(x)}}$ denotes the Moore-Penrose inverse which is guaranteed to exist by Assumption 2.1, and $\nabla$ denotes the gradient with respect to the sub-scripted variable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

Problem Statement: Given the learned probabilistic estimates of the uncertainty $h{(\xi,x)}$, any desired state-input pair $({x_{d}{(t)}},{u_{d}{(t)}})$, $t \in {\lbrack 0,T_{f}\rbrack}$, designed by a planner using the nominal dynamics, and the desired robustness margins, the goal is to design the control input $u{(t)}$ that guarantees the existence of an apriori computable tube-width $\rho$ so that the state of the uncertain dynamics in satisfies ${x{(t)}} \in {\Omega{(\rho,{x_{d}{(t)}})}} \subset {\mathcal{O}_{x_{d}}{(\rho)}}$ with high probability, for all $t \geq 0$, from all initial conditions $x_{0} \in D = \mathcal{X}$, while satisfying the robustness requirements.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

Importantly, the existence of the pre-computable tubes should not depend on the quality of the learned estimates, thus ensuring that safety remains decoupled from learning. The learning should only affect the performance bounds and the optimality of the planned trajectory.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

We now discuss the two constituent components of the $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ control, namely Bayesian learning and the $\mathcal{C}\mathcal{L}_{1}$ control.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Bayesian learning", "weight": 1.0} -->

The probabilistic estimates of the uncertainty $h{({\xi{(t)}},{x{(t)}})}$ in are learned using GP regression. We place the following assumption to compute the prediction error bounds.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

The assumption that the uncertainty is a sample from a GP with a known prior is less conservative than requiring the uncertainty to be a member of the reproducing kernel Hilbert space (RKHS) associated with the kernel. For example, sample functions of GPs with squared-exponential (SE) kernels correspond to continuous functions, whereas the associated RKHS space contains only analytic functions. Moreover, the constants assumed to exist in Assumption 2.4 are easily computable, for example, for the often used squared-exponential (SE) kernel.

<!-- chunk {"id": "body-0018", "role": "body", "section": "$\\mathcal{C}\\mathcal{L}_{1}$control", "weight": 1.0} -->

In the presented methodology, the control input $u{(t)}$ is computed using the $\mathcal{C}\mathcal{L}_{1}$ control as presented. The $\mathcal{C}\mathcal{L}_{1}$ control can be decomposed as where $u_{c}{(t)}$ is the control input designed for the known dynamics and relies on the contraction theoretic notion of Riemannian energy, whereas $u_{a}{(t)}$ is the adaptive control input designed based on the $\mathcal{L}_{1}$ adaptive control theory and is tasked with compensating for the model uncertainties.

<!-- chunk {"id": "body-0019", "role": "body", "section": "$\\mathcal{C}\\mathcal{L}_{1}$control", "weight": 1.0} -->

The existence of the $u_{c}{(t)}$ input relies on the existence of the control contraction metric (CCM), which is defined to be any smooth function $M{(x)}$, satisfying for all ${(x,\delta_{x})} \in {T\mathcal{X}}$ (the tangent bundle of $\mathcal{X}$): for some scalars $\lambda > 0$, $0 < \underset{¯}{\alpha} < \overline{\alpha} < \infty$. Here ${\lbrack b\rbrack}_{\cdot,j}$ denotes the $j^{th}$ column of $B{(x)}$ and $\partial_{f}{M{(x)}}$ denotes the directional derivative of $M{(x)}$ with respect to $f{(x)}$. The same holds for $\partial_{{\lbrack b\rbrack}_{\cdot,j}}{M{(x)}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "$\\mathcal{C}\\mathcal{L}_{1}$control", "weight": 1.0} -->

Moreover, ${\lbrack A\rbrack}_{\mathbb{S}}$ denotes the symmetric part of the matrix $A$. Further details are presented in and. Note that the synthesis of the CCM $M{(x)}$ depends only on the nominal dynamics and can be computed offline. We place the following assumption.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

The nominal dynamics $\overline{F}$ in admit a CCM $M{(x)}$, for all $x \in \mathcal{X}$, and for some positive constants $\lambda$, $\underset{¯}{\alpha}$, and $\overline{\alpha}$ as.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

The $\mathcal{L}_{1}$ adaptive control input $u_{a}{(t)}$ in relies on three components: the state-predictor, the adaptation law, and the control law. The state-predictor is given by where $\hat{x}{(t)}$ is the state of the predictor, ${\overset{\sim}{x}{(t)}} = {{\hat{x}{(t)}} - {x{(t)}}}$ is the state prediction error, and $A_{m} \in {\mathbb{R}}^{n \times n}$ is an arbitrary Hurwitz matrix. The uncertainty estimate $\hat{\mu}{(t)}$ is driven by the state prediction error via the following adaptation law where $\Gamma > 0$ is the adaptation rate, $\mathcal{H} = \left. \{{y \in {\mathbb{R}}^{m}} \middle| {\left. \parallel y\parallel \right.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

\leq \Delta_{h}}\} \right.$ is the conservative set within which the uncertainty estimate is restricted to lie in with $\Delta_{h}$ defined. Additionally, ${\mathbb{S}}^{n} \ni P \succ 0$ is the solution to the Lyapunov equation ${{A_{m}^{\top}P} + {PA_{m}}} = {- Q}$, for some ${\mathbb{S}}^{n} \ni Q \succ 0$. Finally, $\text{Proj}_{\mathcal{H}}{(\cdot, \cdot)}$ is the standard projection operator. Finally, the input $u_{a}{(t)}$ is defined via the following control law presented using the Laplace transform where $C{(s)}$ is a low-pass filter with bandwidth $\omega$ and satisfies ${C{}} = {\mathbb{I}}_{m}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

Note that we use the variable $s$ to represent both the Laplace variable and the geodesic parameter. The distinction is clear from context.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

We now briefly explain how the $\mathcal{C}\mathcal{L}_{1}$ guarantees safety by the existence of pre-computable tubes using only the available conservative knowledge presented in Assumptions 2.1 and 2.2, i.e., without any learning.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

defined in Assumption 2.6; and $Z{(x)}$ is defined as where ${W{(x)}} = {M{(x)}^{- 1}}$ is referred to as the dual metric and ${L{(x)}^{\top}L{(x)}} = {W{(x)}}$, and these entities are guaranteed to exist due to the positive definiteness of the CCM $M{(x)}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

As before, $\partial_{f}{W{(x)}}$ denotes the directional derivative of the dual metric $W{(x)}$ with respect to $f{(x)}$. Furthermore, $\left. \parallel{sC{(s)}}\parallel \right._{\mathcal{L}_{1}}$ denotes the $\mathcal{L}_{1}$ function norm of the impulse response of $sC{(s)}$ \[14, Sec. A.7\]. Finally, for any real-valued matrices $A$ and $B$, with $B$ square, ${\underset{¯}{\sigma}}_{> 0}{(A)}$, $\overline{\lambda}{(B)}$, and $\underset{¯}{\lambda}{(B)}$, denote the smallest singular-value of $A$, and the largest and smallest eigenvalues of $B$, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

For the purposes of analysis, we need the following constants using which we further define Note that $\kappa_{1} - \kappa_{3}$ are monotonically increasing as a function of the conservative known bounds $\Delta_{h}$, $\Delta_{h_{x}}$, and $\Delta_{h_{\xi}}$, and vanish for zero uncertainty bounds.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 2.6", "weight": 1.0} -->

The rate of adaptation $\Gamma$ in and filter bandwidth $\omega$ in then need to satisfy Since the constants ${{\zeta_{1}{(\omega)}},{\zeta_{2}{(\omega)}},{\zeta_{3}{(\omega)}}} \propto {1/\omega}$, the conditions in can always be satisfied by choosing an appropriately large adaptation rate $\Gamma$ and filter bandwidth $\omega$. The following result quantifies the existence of safe tubes around any desired state $x_{d}{(t)}$. The detailed proof of the following theorem can be found in \[19, Thm. 5.1\].

<!-- chunk {"id": "body-0030", "role": "body", "section": "$\\mathcal{C}\\mathcal{L}_{1}$-$\\mathcal{G}\\mathcal{P}$: Riemannian Energy $\\mathcal{L}_{1}$with Gaussian Process Learning", "weight": 1.0} -->

Given the posterior distribution of ${h{(z)}} = {h{(\xi,x)}}$, we may re-write the uncertain dynamics in as where ${\hat{F}{(\xi,x,u)}} = {{f{(x)}} + {B{(x)}{({u + {\nu_{N}{(\xi,x)}}})}}}$ represents the learned dynamics, which we obtain by adding and subtracting $\nu_{N}{(\xi,x)}$ within the control channel. Here, we denote As, $F{(\xi,x,u)}$ represents the actual dynamics, but now $\hat{F}{(\xi,x,u)}$ represents the learned dynamics as opposed to $\overline{F}{(\xi,x)}$ representing the conservative nominal model.

<!-- chunk {"id": "body-0031", "role": "body", "section": "$\\mathcal{C}\\mathcal{L}_{1}$-$\\mathcal{G}\\mathcal{P}$: Riemannian Energy $\\mathcal{L}_{1}$with Gaussian Process Learning", "weight": 1.0} -->

Consider a desired state-input pair $({x_{d}{(t)}},{u_{d}{(t)}})$, which is now designed by the planner using the learned dynamics $\hat{F}$, i.e., ${{\overset{˙}{x}}_{d}{(t)}} = {\hat{F}{({\xi{(t)}},{x_{d}{(t)}},{u_{d}{(t)}})}}$, as opposed to the nominal dynamics $\overline{F}$. Note that $\hat{F}$ contains the nominal dynamics and the mean dynamics of the GP predictive distribution. That is, $\hat{F}$ is deterministic, and therefore any planner that is being used does not have to rely on uncertainty propagation to ensure safety.

<!-- chunk {"id": "body-0032", "role": "body", "section": "$\\mathcal{C}\\mathcal{L}_{1}$-$\\mathcal{G}\\mathcal{P}$: Riemannian Energy $\\mathcal{L}_{1}$with Gaussian Process Learning", "weight": 1.0} -->

The goal now is to design the input $u{(t)}$ such that the state $x{(t)}$ of tracks $x_{d}{(t)}$ while remaining inside of pre-computable tube with high probability. Similar to the $\mathcal{C}\mathcal{L}_{1}$ input, the $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ input is composed as where the individual components mirror those in and, but are now designed for the learning-based representation of the dynamics.

<!-- chunk {"id": "body-0033", "role": "body", "section": "$\\mathcal{C}\\mathcal{L}_{1}$-$\\mathcal{G}\\mathcal{P}$: Riemannian Energy $\\mathcal{L}_{1}$with Gaussian Process Learning", "weight": 1.0} -->

However, the major distinction is that ${\hat{u}}_{c,\hat{F}}{(t)}$ is designed to track $x_{d}{(t)}$ using the learned dynamics $\hat{F}$ (as opposed to the nominal dynamics $\overline{F}$), and the adaptive input ${\hat{u}}_{a,\hat{F}}{(t)}$ now compensates for the remainder uncertainty $h - \nu_{N}$ as opposed to the uncertainty $h$. Therefore, we need to quantify the 'size' of the remainder uncertainty $h - \nu_{N}$ for controller design. For this purpose, we will use the posterior distributions of the uncertainty and its derivatives in and, respectively, to compute high probability estimates of these bounds. In particular, we use the recent results. We begin by presenting the following definition.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We provide an illustrative example of a 6-DOF planar quadrotor at different levels during the learning process using a variety of motion planners. The dynamics of the vehicle can be expressed in the following control-affine form following: Figure 3: The decay of the uncertainty bounds based on the high-probability prediction-error bounds from Eq. 24 with the growth of the dataset. where $p_{x},p_{z}$ is the position of the quadrotor in the $x - z$ plane; $v_{x},v_{z}$ are the velocities of the quadrotor in the body frame; $\theta,\overset{˙}{\theta}$ are the pitch angle and rate; $g$ is the gravitational constant; and $u_{F}$ and $u_{M}$ are the thrust and moment control inputs respectively. Additionally, the planar quadrotor is required to always meet the following state constraints: The contraction metric is synthesized using a sum-of-squares programming approach described.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In the following examples, we consider that the unmodeled uncertainty is given by The first component of the uncertainty affects the total thrust and is indicative of an off-trim control and drag-like parasitic force, whereas the second component is a time-varying disturbance that is injected into the moment input channel. Recall that the time-varying parameter from Eq. 1 is simply ${\xi{(t)}} = t$. In each of the examples we show the evolution of the safety guarantees across three learning episodes and the resulting improvement in performance and optimality. The dataset is generated by using Latin hypercube sampling across the state space, but one could also use sophisticated exploration techniques to safely gather data based on our framework. Prior to learning, the bounds on the uncertainty and its growth over the state-space are conservatively estimated as Figure 4: Planar quadrotor flight across an obstacle forest with (a) only a deterministic knowledge of the uncertainty, (b) model learned with N = 25 dataset, (c) model learned with N = 100 dataset.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

One can analytically verify that the true bounds of the uncertainty are indeed lower than our estimates: where $\mathcal{X}$ is defined using the state contraint set in Eq. 38. In the first two examples, we begin with a simplified architecture of the $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ input where the learned estimates are only used to improve performance and optimality with respect to the nominal model. That is, the planner does not incorporate the learned updates. Later in third example, we provide a sim for the complete $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ architecture but in a simplified environment. We consider three instances/episodes during the learning transients with $N = 0$, $N = 25$ and $N = 100$ samples.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The corresponding uncertainty bounds for each episode are shown in Figure 3. The results presented use $\delta = 0.1$ and $\tau = {{1e} - 8}$ for the terms defined in Theorem 3.1, therefore the performance bounds indicated in the figures hold with probability at least $0.9$. The examples were simulated using the Julia programming language and the Pluto reactive environment.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 4.1 (Obstacle Forest)", "weight": 1.0} -->

The quadrotor is tasked to safely fly across a forest of convex polygonal obstacles from the origin to position 20 meters away while minimizing the following discrete-time objective where $x_{k}$ is the state at the $k^{\text{th}}$ time-instant, $x_{\text{goal}}$ is the goal state, and $Q$ and $Q_{f}$ are positive definite diagonal matrices. In this example, we use MPPI to generate the feasible trajectories based on the pre-computed tube size. MPPI was configured to generate 500 trajectory rollouts at a frequency of 50 Hz with a prediction horizon of 2 seconds. The tubes depicted in Figure 4 are only a projection of the tube $\mathcal{O}_{x_{d}}$ onto the vehicle position but they also extend into the rest of the state-space limiting the overall maneuverability of the quadrotor. For instance when the tube-size is $\rho = 0.6$, the maximum pitch angle is approximately $\pm$ 11 degrees instead of the full $\pm$ 45 degrees pitch that the contraction metric was initially designed.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 4.1 (Obstacle Forest)", "weight": 1.0} -->

Initially in Figure 4a, the model knowledge is poor and the tubes guaranteed by $\mathcal{C}\mathcal{L}_{1}$ control are conservative based only on the deterministic knowledge of the uncertainty, with a tube size of $\rho = 0.6$. This lack of knowledge results in a circuitous path that takes over about 27 seconds for the vehicle to safely traverse. As the data is incorporated into the model, the performance improvement can be seen in Figure 4. The trajectory shown in Figure 4b has a tube radius of $\rho = 0.35$ and has a duration of 16 seconds. In Figure 4c, the trajectory has a tube radius of $\rho = 0.1$, and the vehicle can navigate the environment to the final position in only 14 seconds. Note that after incorporating the learned model, both the $\mathcal{L}_{1}$ filter bandwidth and the adaptation rate are reduced to improve the robustness margin of the closed-loop system and lower the computational burden of the controller.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 4.2 (Bug-Trap)", "weight": 1.0} -->

In this example, the quadrotor must safely escape a box trap from the origin and arrive at a point on the other side of the trap. For such problems, complete or probabilistically complete planners are the algorithms of choice since other methods typically get stuck at a local minimum and never reach the goal. We use the popular sampling-based planner BIT\* with the two-point boundary value problem solved using ALTRO. For the sake of simplicity, our implementation of BIT\* only samples in the position space and the remaining states are assumed to be zero at each sample, but this can be relaxed if the planner is constructed following the approach described. BIT\* is configured with a batch-size of 500 samples and a total of 10 batches. Similar to Example 4.1. ‣ 4 Simulation Results ‣ Contraction ℒ₁-Adaptive Control using Gaussian Processes"), each of the simulations in Figure 5 show the safe navigation using the tube bounds during different instances of the learning process.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 4.3 (Improving Optimality)", "weight": 1.0} -->

In the previous two examples, the learned model was simply used to compensate for the uncertainty and was not explicitly used to generate desired trajectories that exploit the newly learned model. In this example, the trajectory optimization solver uses the mean dynamics of the GP predictive function from Eq. 6 to improve the quality of the solution. The quadrotor is tasked to fly from the origin to $$ in 10 seconds while minimizing the following LQR objective: where $x_{k}$ and $u_{k}$ are the state and controls at the $k^{\text{th}}$ time-instant, $x_{\text{goal}}$ is the goal state, and $Q$, $R$ and $Q_{f}$ are positive definite diagonal matrices. Only the state constraints from Eq. 38 are active and no other obstacles are present so that we can clearly see the improvement in optimality. In Figure 6a, the vehicle can only reach a maximum of $0.4$ m/s in the body $z -$axis and must therefore exploit the remaining maneuverability in its body $x -$axis to fly to the goal location.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 4.3 (Improving Optimality)", "weight": 1.0} -->

This results in a zig-zag flight path with large oscillations in the vehicle pitch. As the learned model is incorporated in Figures 6b and 6c, the solver arrives at smoother solutions which don't oscillate as much as the first episode. In Figure 6c, the vehicle is capable of reaching much faster speeds in its body $z -$axis and therefore plans a much more straightforward path to the goal.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have presented the $\mathcal{C}\mathcal{L}_{1}$-$\mathcal{G}\mathcal{P}$ framework, which enables safe simultaneous learning and control. The safety of the method is certified by the tracking error bounds produced by the ancillary $\mathcal{C}\mathcal{L}_{1}$ controller. The learning is performed using Gaussian process regression. The learned Gaussian process model can be used to generate high probability uniform error bounds, which are incorporated into the controller to improve the tracking error bounds. Future work will extend the architecture to leverage the tracking error bounds in the path planning phase. The bounds are used to ensure safety, but can also be extended to provide worst case estimates for both the uncertainty reduction and cost associated with a desired trajectory. Finally, the guarantees will be extended to a larger class of nonlinear systems, explored in output feedback formulation, and other possible generalizations.
