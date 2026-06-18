<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convergent iLQR for Safe Trajectory Planning and Control of Legged Robots

Topics include Robotics, Safety, Robustness, Planning, Control, Convergent iLQR.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In order to perform highly dynamic and agile maneuvers, legged robots typically spend time in underactuated domains (e.g. with feet off the ground) where the system has limited command of its acceleration and a constrained amount of time before transitioning to a new domain (e.g. foot touchdown). Meanwhile, these transitions can instantaneously change the system's state, possibly causing perturbations to be mapped arbitrarily far away from the target trajectory. These properties make it difficult for local feedback controllers to effectively recover from disturbances as the system evolves through underactuated domains and hybrid impact events. To address this, we utilize the fundamental solution matrix that characterizes the evolution of perturbations through a hybrid trajectory and its 2-norm, which represents the worst-case growth of perturbations. In this paper, the worst-case perturbation analysis is used to explicitly reason about the tracking performance of a hybrid trajectory and is incorporated in an iLQR framework to optimize a trajectory while taking into account the closed-loop convergence of the trajectory under an LQR tracking controller.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The generated convergent trajectories recover more effectively from perturbations, are more robust to large disturbances, and use less feedback control effort than trajectories generated with traditional methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Legged robotics research has increasingly focused on enabling highly dynamic and agile motions such as jumping, leaping, and landing. Implementing these capabilities reliably would improve legged robot performance in applications such as extraterrestrial or urban environment navigation where jumping up on ledges or leaping across chasms may be necessary. However, jumping and leaping are dangerous maneuvers, with failure often resulting in catastrophic outcomes for the robot.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

What makes these actions challenging is that they induce trajectories that are both hybrid and underactuated, which doubly contribute to the difficulty in controlling legged robots. Broadly speaking, a system is hybrid if it undergoes discrete changes in state and/or dynamics, and it is underactuated if there exists a direction of acceleration in state space that can not be commanded by any valid input \[, Ch. 1.2\]. Even when an underactuated system is controllable, driving the system to a desired target state may require significant time and control effort, neither of which may be readily available. For instance, a robot jumping in the air can not arbitrarily choose how much time it has until its feet touchdown on the ground. This means that the controller needs to spend a lot of effort to correct tracking errors prior to touchdown, or else discontinuous, unbounded saltation effects can cause arbitrarily large divergence if incoming errors are not sufficiently mitigated, e.g. with grazing impacts. Increasing control gains is one possible solution to improve stability, though that strategy comes at a large drawback of worsening robustness in the face of modelling errors and uncertainties\[, Ch.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

13\]. Instead, this work leverages nonlinearities in continuous and hybrid dynamics that make some trajectories easier to stabilize than others, even under equivalent feedback controllers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents a novel adaptation of the iLQR trajectory optimization algorithm that improves closed-loop convergence under an equivalent feedback controller (i.e. without changing the LQR controller weights), as demonstrated in Fig.. Our simulation results show that this convergent iLQR ($\chi$-iLQR) achieves three simultaneous improvements over standard iLQR: superior tracking performance from initial perturbations, reduced feedback control effort over the trajectory, and improved robustness to large initial errors. Compared to existing methods, $\chi$-iLQR has two additional key strengths. Firstly, it is based on an analysis that is simple to compute compared to methods such as sum-of-squares. Additionally, $\chi$-iLQR captures the local tracking performance of a closed-loop trajectory, which directly predicts experimental results.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Related Works", "weight": 1.0} -->

A strategy that has been used to enable dynamic yet precarious behaviors for legged robots is leveraging highly accurate, complex models and full-body trajectory optimization to plan precise motions. While these methods incorporate feedback controllers to stabilize the generated trajectories, there has been little focus on how these feedback controllers should be designed to stabilize closed-loop systems under error and uncertainty.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Related Works", "weight": 1.0} -->

Robust trajectory planning has been successfully implemented for smooth systems like wheeled robots, with some recent results being adapted to hybrid systems like legged robots. These works have focused on optimizing over uncertainties in system dynamics, such as unknown disturbances and modelling errors. For example, designs robust closed-loop trajectories for smooth systems by optimizing the volume reduction of an ellipsoidal disturbance set, but was not applied to hybrid systems. Risk-sensitive planning and control is an alternate method that optimizes over the variance of a cost distribution that evolves through the trajectory. Other approaches present trajectory optimization algorithms for legged robots over uncertain terrain and compute a forward reachable set to bound closed-loop errors. Many of these methods require the distribution of errors to be prespecified, which is not always clear how to tune. Additional actuation, such as reaction wheels or tails, also relieves the difficulties of underactuated systems. However, this comes with obvious tradeoffs of increased cost, size, and weight.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

Separately, consider the problem of quantifying the stability or convergence properties of a system. A very popular method is Lyapunov analysis, where the existence of a positive definite differentiable scalar function with negative definite derivatives, called the Lyapunov function, can guarantee asymptotic stability of the system. Lyapunov functions can be difficult to compute, particularly for hybrid systems, and can require methods such as sum-of-squares or machine learning to be tractable. A similar strategy known as control barrier functions, which restricts the system from entering some set of undesirable states, has been successfully implemented on legged robot hardware, but has the same drawback as Lyapunov functions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

A different strategy to analyze the stability and convergence of trajectories is contraction analysis, which tracks the distance between two close trajectories. If this distance monotonically decreases over the trajectory, then the system is contractive and asymptotic stability can be guaranteed. Contraction analysis has been incorporated into path planning and trajectory optimization algorithms on smooth systems, but applying contraction analysis to hybrid systems is difficult because many mechanical hybrid systems are not contractive at hybrid events. loosened the contraction criterion and optimized the stability of open-loop periodic orbits using monodromy matrix analysis. Here, we extend that work by generalizing to non-periodic trajectories under feedback control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Analysis and Planning for Hybrid Systems", "weight": 1.0} -->

This section defines a hybrid system and quantifies the performance of a closed-loop hybrid trajectory using linearized variational equations. With this analysis, we can generate a scalar measure of a trajectory's convergence which is then incorporated into a trajectory optimization framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Hybrid Systems", "weight": 1.0} -->

Hybrid systems are a class of dynamical systems that consist of continuous domains connected by hybrid events. Following the notation, we describe a hybrid system as a set of discrete modes $\{ I,J,\ldots,K\}$, each with a domain $D_{I}$ and a time-varying vector field $F_{I}$. $G_{(I,J)}$ is a guard that triggers a transition between mode $I$ and mode $J$ and $R_{(I,J)}$ is the reset map defining that transition.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Hybrid Systems", "weight": 1.0} -->

An execution of a hybrid system begins at an initial state $x_{0} \in D_{I}$. With input $u_{I}{(t,x)}$, the system obeys the dynamics $F_{I}$ on $D_{I}$. If the system reaches guard surface $G_{(I,J)}$, the reset map $R_{(I,J)}$ is applied and the system continues in domain $D_{J}$ under the corresponding dynamics defined by $F_{J}$. The flow $\phi{(t,t_{0},x_{0},U)}$ describes how the hybrid system evolves from some initial time $t_{0}$ and state $x_{0}$ until some final time $t$ under input sequence $U$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Linearized Variational Equations", "weight": 1.0} -->

For both continuous domains and hybrid transitions, linearized variational equations can be constructed to characterize the evolution of perturbations $\delta x$. In each continuous domain, the linearized variational equation is discretized from timestep $i$ to $i + 1$ and is ${\delta x_{i + 1}} \approx {{({A_{I} - {B_{I}K_{I}}})}\delta x_{i}}$ with $A_{I}$ and $B_{I}$ being the derivatives of the discretized dynamics in mode $I$ w.r.t. state $x_{i}$ and control inputs $u_{i}$, respectively, and $K_{I}$ are linear feedback gains. The feedback term drops out for open-loop systems. For hybrid events, the analogous variational equation is the saltation matrix $\Xi_{(I,J)}$, which describes the transition between modes $I$ and $J$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Linearized Variational Equations", "weight": 1.0} -->

The saltation matrix is the first-order approximation of the change in state perturbations from before the hybrid event at $\delta x{(t^{-})}$ to perturbations after $\delta x{(t^{+})}$, such that ${\delta x{(t^{+})}} \approx {\Xi_{(I,J)}\delta x{(t^{-})}}$. This linear approximation assumes that nearby trajectories undergo the same mode transition. Computing the saltation matrix relies on the derivatives of the reset and guard of the transition along with the dynamics in each mode, and is detailed.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Convergence Measure", "weight": 1.0} -->

To characterize the closeness of ${\overline{x}}_{f}$ and $x_{f}$, we utilize the fundamental solution matrix, $\Phi$. Following, the fundamental solution matrix is the linearized approximation ${\delta x_{f}} \approx {\Phi\delta x_{0}}$ and represents the transformation of error from the initial state to final state.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-C Convergence Measure", "weight": 1.0} -->

The fundamental solution matrix can be computed by sequentially composing the linearized variational equations in each continuous domain ($\overset{\sim}{A}:={A - {BK}}$) and the saltation matrices ($\Xi$) at each hybrid event.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-C Convergence Measure", "weight": 1.0} -->

Since the fundamental solution matrix captures the change in errors across a trajectory, the singular values of $\Phi$ characterize error change along principle axes of state space. The largest singular value, which is equivalent to the induced 2-norm of $\Phi$, describes the evolution of the most divergent direction of initial error $\delta x_{0}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Convergence Measure", "weight": 1.0} -->

$\chi$ is a continuous measure of local convergence, where smaller values of $\chi$ indicate stronger reduction of worst-case final errors. A value of $\chi < 1$ indicates errors in all directions will shrink.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-D iLQR for Hybrid Systems", "weight": 1.0} -->

The iterative linear quadratic regulator (iLQR) is a trajectory optimization method that also computes LQR feedback gains over the generated trajectory. iLQR is convenient because compared to other trajectory optimization methods like direct collocation, it is less computationally intensive and guarantees a feasible trajectory. We draw from recent work that adapts the iLQR algorithm for use on hybrid dynamical systems.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-D iLQR for Hybrid Systems", "weight": 1.0} -->

iLQR computes gradient and Hessian information of the cost, which results in a quadratic approximation of the cost function.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-D iLQR for Hybrid Systems", "weight": 1.0} -->

iLQR solves the optimal control problem by alternating between forward passes that simulate the system under a given control input sequence, and backward passes that solve for a new locally optimal control sequence. In the backward pass, the value function, which is the optimal cost to go at any timestep, is propagated through the trajectory in reverse, and gives locally optimal feedforward inputs and feedback gains at each timestep. Computing the value function relies on gradient and Hessian computations of the cost function and Jacobians of the dynamics, which equates to computing the linearized variational equations discussed in Sec. III-B. For much greater detail of iLQR for hybrid systems, see.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

Here we present a novel trajectory optimization algorithm called convergent iLQR or $\chi$-iLQR, summarized in Algorithm.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

where $Q_{\chi}$ is a scalar weighting parameter. Since $\chi$ is solely a function of states and inputs, iLQR uses gradient and Hessian information to make a quadratic approximation compatible with the other cost terms.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

Typically in iLQR, the cost function $J$ is evaluated after each forward pass, since it is only dependent on the states and inputs of the most recent trajectory. However, in this case the convergence measure portion of the cost function is dependent on the feedback gains generated by the algorithm. This means that the gradient and Hessian terms of the cost function rely on the feedback gains that are being updated at every timestep in the backward pass. Due to this, the cost function derivatives are highly coupled with the gains and become convoluted to compute.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

To resolve this, we propose executing two separate backward passes that each compute a different set of gains. We do this to preserve the convergence properties of iLQR, though other choices might be possible such as borrowing the previous set of gains under the assumption that the gains do not change significantly over iterations. First, the tracking backward pass computes the feedback gains that will be used as the LQR tracking controller gains and to compute the convergence measure. It is equivalent to the backward pass in standard iLQR using the cost function $J$, which solves the Riccati equation for the most recent trajectory. With the gains generated in the tracking backward pass $K_{t}$, the convergent cost function $J_{\chi}$ can be computed. The search backward pass takes $J_{\chi}$ from the tracking backward pass and computes the gradients of the convergent cost function with controller gains $K_{t}$. The feedforward inputs $k_{s}$ and the feedback gains $K_{s}$ from this pass are used to search for an improved trajectory in the forward pass.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

Since $J_{\chi}$ is returned by the tracking backward pass, a line search is performed after this function call to guarantee the reduction of the cost function $J_{\chi}$. If the line search condition is not satisfied, the forward pass and tracking backward pass are looped until the line search condition is passed.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

Within the search backward pass, iLQR requires computation of the gradient and Hessian of $\chi$. The derivatives of $\chi$ can be computed by leveraging the singular value decomposition of $\Phi = {USV^{T}}$ where $S$ is a diagonal matrix of singular values and the columns of $U$ and $V$ are the left and right singular vectors, respectively. $\chi$ is the largest singular value of $\Phi$ and let $u_{\chi}$ and $v_{\chi}$ be its corresponding left and right singular vectors.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

$\frac{\partial\Phi}{\partial x_{i}}$ in turn can be computed by using the product rule along with leveraging the fact that only ${\overset{\sim}{A}}_{i}$ and $\Xi_{(i,{i + 1})}$ are functions of $x_{i}$, and all other $\overset{\sim}{A}$ and $\Xi$ terms have zero derivatives with respect to $x_{i}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

Derivatives with respect to the input $u_{i}$ follow equivalently. To improve computational efficiency, $O_{i}$ at each timestep can be computed recursively during the forward pass and each $P_{i}$ can be computed recursively in the tracking backward pass. Since the rollout does not yet have feedback gain information, the initial $O$ values must be computed separately.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

until LineSearchIsSatisfied(Jχ) return X, U, M, Kt
Algorithm 1 Convergent iLQR Algorithm

<!-- chunk {"id": "body-0033", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

Because the scalar $\chi$ is derived from the norm of the matrix $\Phi$, the gradient of $\chi$ relies on computing a 3-dimensional tensor of ${\overset{\sim}{A}}_{i}$ and $\Xi$ derivatives, and the Hessian of $\chi$ is computed from a 4-dimensional tensor of matrix second derivatives. While recent work has enabled faster computation of second derivatives of dynamics which can aid in the computation of the 3-D tensor derivatives, computing 4-D tensor derivatives is generally untenable. Instead, numerical methods like finite differences for gradients and BFGS for Hessians can perform at reasonable speed. In order to approach real-time computation, it is likely that the full Hessian of $\chi$ is not necessary to find an appropriate search direction and that a partial computation or even leaving out the Hessian completely is sufficient to compute optimal trajectories. Future work will address this gap. Nonetheless, the algorithm in its current form can still be useful for offline planning for trajectories that are expected to have a high degree of risk, such as leaping across ledges or traversing narrow beams.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

In real-world applications, it can be acceptable for a robot to pause and plan a safe trajectory before executing these dangerous maneuvers.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Convergent iLQR", "weight": 1.0} -->

Mean Simulated Error Ratio
Mean Simulated Feedback Effort

<!-- chunk {"id": "body-0036", "role": "body", "section": "Examples and Results", "weight": 1.0} -->

In this section, we demonstrate the convergence improvements of our method on a spring hopper system and a planar quadruped robot model. Simulation results show that the improved convergence measure correlates with an improvement in average tracking performance, robustness to large disturbances, and feedback control effort. Both examples were implemented in MATLAB, with forward simulations using the `ode113` function. Cost function gradients were computed using, derivatives of ${\overset{\sim}{A}}_{i}$ and $\Xi_{(i,{i + 1})}$ were computed with finite differences, and Hessians were computed with BFGS.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A1 Rocket Hopper Model", "weight": 1.0} -->

This system is made up of a point mass body with a single massless spring leg. The state of the hopper is characterized by the positions $x_{B}$, $y_{B}$ of the body, the angle $\theta$ of the leg and their derivatives ${\overset{˙}{x}}_{B}$, ${\overset{˙}{y}}_{B}$, $\overset{˙}{\theta}$ such that the full state is a $6 \times 1$ vector. The system has two domains: an aerial phase $D_{1}$ and a stance phase $D_{2}$. Taking a constant ground height at zero gives a touchdown guard function $g_{}$ that is the height of the foot and a liftoff guard function $g_{}$ that is the ground reaction force applied by the spring leg. Both reset maps $R_{}$ and $R_{}$ are identity since position and velocity are continuous.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A1 Rocket Hopper Model", "weight": 1.0} -->

The system has two inputs: a hip actuation and an actuation in the direction of the leg. In the air, this allows the hopper to rotate the leg around the body and exert a propulsion in the direction of the leg, somewhat akin to a rocket, though this force can approximate forces from other legs or actuators. A small rotor inertia in the air ensures the dynamics are well-conditioned when controlling the massless leg. In stance, the hip torque and rocket force exert ground reaction forces on the body. The body mass of the hopper was chosen as 1 kg, spring constant as 250 N/m, and resting leg length as 0.75 m.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A2 Rocket Hopper Results", "weight": 1.0} -->

The objective for this system is to begin in the air at rest with a height of 2 m and end in the air at rest with the same height displaced 0.2 m horizontally. The system is given 1.5 s for this trajectory.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A2 Rocket Hopper Results", "weight": 1.0} -->

We generated four trials of paired trajectories with varied weighting parameters, shown in Table I, and compared the performance of the standard (vanilla) iLQR method (where $Q_{\chi} = 0$) to $\chi$-iLQR. There is no reference trajectory to track, so $Q_{i}$ is zero for all trials.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A2 Rocket Hopper Results", "weight": 1.0} -->

For 3 of these trials, vanilla iLQR generated a trajectory with $\chi > 1$, meaning the worst-case error direction was expansive, see Table I. $\chi$-iLQR decreases every convergence measure to below 1 so that all error directions are reduced over the trajectory. On average, $\chi$-iLQR decreased $\chi$ by 28.79% compared to the vanilla method.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A2 Rocket Hopper Results", "weight": 1.0} -->

To validate these trajectories, each closed-loop trajectory was simulated 100 times with equivalent small random initial perturbations in both positions and velocities with covariance matrix ${\text{cov}{(X_{0})}} = {10^{- 4}I}$. A small covariance was chosen so that the linearizations assumed in the convergence measure and LQR control are valid. For each simulation run, the initial error $\delta x_{0}$ and the final error $\delta x_{f}$ were recorded, along with the sequence of control inputs $V:={\{ v_{0},v_{1},\ldots,v_{N - 1}\}}$. Note that these inputs are distinct from the nominal feedforward inputs to the system $U$ because there is additional feedback effort exerted by the actuators.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A2 Rocket Hopper Results", "weight": 1.0} -->

Two values were recorded during each simulation run to characterize the convergence properties of the trajectories. The first is the error ratio, $E = \frac{\left\| {\delta x_{f}} \right\|_{2}}{\left\| {\delta x_{0}} \right\|_{2}}$ defined as the ratio of the final error 2-norm to the initial error 2-norm. A lower error ratio means better tracking performance, and $E < 1$ indicates a net reduction in error on average. The second value is the feedback effort, $F = {\sum_{i = 0}^{N - 1}{({v_{i} - u_{i}})}^{2}}$ which is the sum of squares of the difference between $V$ and $U$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A2 Rocket Hopper Results", "weight": 1.0} -->

Table I shows that the simulation results support our assertion that an improved convergence measure correlates with an improved mean tracking performance and feedback effort. The mean error ratio and feedback effort over the 100 simulations were both lower for trajectories generated with $\chi$-iLQR. The average improvement over the four trials was 19.30% for mean error ratio and 13.17% for feedback effort.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A2 Rocket Hopper Results", "weight": 1.0} -->

None of the simulated runs had an error ratio greater than one, which is sensible since the worst-case direction occurs with probability zero. However, even if none of the sampled initial errors aligned exactly with the worst-case direction predicted by the fundamental solution matrix, nearby initial error directions still see improvement in convergence, which explains the improvement in mean simulated error ratio.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Planar Quadruped", "weight": 1.0} -->

Here we demonstrate the improvements of $\chi$-iLQR on a more complex robot model akin a standard quadruped robot. The model is simplified as a planar quadruped, meaning that all movement occurs in the sagittal plane and the left-right pairs of legs are constrained to move identically.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B1 Planar Quadruped Model", "weight": 1.0} -->

In the sagittal plane, we can model the robot with 7 positional states. $x_{B}$, $y_{B}$, $\theta_{B}$ are the position and orientation of the body. The front and back sets of legs each have two states for the hip angle $\alpha_{f},\alpha_{b}$ and knee angle $\beta_{f},\beta_{b}$. Thus the full state is dimension 14.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B1 Planar Quadruped Model", "weight": 1.0} -->

This system has four domains: the aerial domain $D_{1}$, front stance domain $D_{2}$, back stance domain $D_{3}$, and full stance domain $D_{4}$. The impact guard function is the height of the foot and the guard function for liftoff is the vertical ground reaction force. The dynamics of the robot body in the aerial phase follow ballistic motion, while the legs are simplified to be massless while including the aforementioned rotor inertia. The impact reset map for each foot consists of a discrete update to the hip and knee velocities, while the body states are unchanged due to the massless legs. The liftoff reset map is identity. The input vector for this system is 4-dimensional to actuate the hip and knee joints.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B1 Planar Quadruped Model", "weight": 1.0} -->

In this model, parallel torsion springs are added to the knee joints. Parallel joint springs have been utilized to mimic tendons found in animals that increase the energy efficiency of legged locomotion. Due to the resonance of the natural spring dynamics, controlling these systems requires special care. For example, solved for optimal gait timings to leverage resonant spring frequencies. These spring models of legged robots are good candidates for $\chi$-iLQR because the dynamics of the stance phase depend strongly on the leg configuration at touchdown. Thus, a small error in leg states at touchdown can have a large effect on tracking performance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B1 Planar Quadruped Model", "weight": 1.0} -->

The inertial and dimensional properties were chosen to match the Ghost Robotics Spirit 40 quadruped. The added torsional knee spring has a spring constant ${75\text{~N}} \cdot \text{m} \cdot \text{rad}^{- 1}$ and rest angle 1.2 rad.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B2 Planar Quadruped Results", "weight": 1.0} -->

The trajectory optimization task for the planar quadruped is to generate a gait with a forward velocity of 0.25 m/s. The robot begins in the air with a body height of 0.3 m. The hip joints begin at an angle of 0.6 rad and the knee joints begin at 1.2 rad. The terminal target state is translated 0.0875 m in the x-direction from the initial state. The trajectory is given 0.35 s to execute. We choose to set a constant input weight of $R_{i} = {{5 \cdot 10^{- 4}}I}$. The terminal weight is $Q_{N} = {500I}$ and the convergence weight for $\chi$-iLQR is $Q_{\chi} = 1$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B2 Planar Quadruped Results", "weight": 1.0} -->

We set up a similar experiment to the prior example, with the addition of simulating over a range of covariance magnitudes. This is done to evaluate the basin of attraction of each trajectory over larger initial errors that introduce greater nonlinear effects. The two trajectories were evaluated with 6 sets of 100 paired simulation runs with random initial error covariance magnitudes of $10^{- 4}$, $5 \cdot 10^{- 4}$, $10^{- 3}$, $5 \cdot 10^{- 3}$, $10^{- 2}$, and $5 \cdot 10^{- 2}$ in each direction. The lowest covariance magnitude of $10^{- 4}$ approximates local linear behavior well, while $5 \cdot 10^{- 2}$ is the maximum magnitude before some trials begin with the robot's feet below the ground.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B2 Planar Quadruped Results", "weight": 1.0} -->

Table II shows the vanilla cost, convergence measure, mean simulated error ratio, and mean simulated feedback effort of the two trajectories at the covariance magnitude $10^{- 4}$. As expected, the vanilla cost of the convergent trajectory increases since its optimizing for a different cost function, while the convergence measure and simulation values improve. We argue that in dynamic legged locomotion, a costlier nominal trajectory can often be worth an improvement in the trajectory's robustness.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B2 Planar Quadruped Results", "weight": 1.0} -->

The mean simulated error ratio for the convergent trajectory at this small covariance magnitude was 28.23% less and the mean simulated feedback effort was 16.56% less. Fig. displays a histogram of the error ratio for each of the trials, with the convergent trajectory having improved performance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B2 Planar Quadruped Results", "weight": 1.0} -->

As the magnitude of initial errors grows, the performance of the LQR tracking controller becomes worse due to the increase in nonlinear effects. Fig. shows the simulation results for each trajectory over a range of initial error covariance magnitudes. Each pair of lines indicates the success rate of the respective closed-loop trajectories at maintaining error ratios of less than 50, 10, and 5 respectively. An error ratio of greater than 50 is representative of a catastrophic failure, which the vanilla trajectory encounters at a covariance magnitude of $5 \cdot 10^{- 4}$, while the convergent trajectory first experiences a failure at covariance magnitude $10^{- 2}$. This difference in performance suggests the convergent trajectory is more robust to larger initial errors and nonlinearities.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B2 Planar Quadruped Results", "weight": 1.0} -->

Even with the $\chi$-iLQR convergence improvements, the controller does not reduce errors in all directions. The simulation results show there was usually some error growth, which is reasonable since the body dynamics are fully unactuated in the aerial phase and the system undergoes multiple hybrid events. A combination of higher feedback gains and a global footstep planner could be able to grant this system full convergence. Even so, this work can be valuable to ensure that the system does not diverge too far from its target trajectory between iterations of a global planner.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we present a novel trajectory optimization method, $\chi$-iLQR that optimizes over the worst-case error growth of a hybrid trajectory. This method is based on the fundamental solution matrix, which maps the evolution of perturbations through a trajectory. Incorporating the saltation matrix into the fundamental solution matrix allows for straightforward handling of hybrid events. The simulation results presented on two legged robot models demonstrate that this method produces trajectories with improved tracking performance, decreased feedback actuation effort, and improved robustness to large perturbations. Even for a quadrupedal trajectory that was very difficult to track, $\chi$-iLQR produced a trajectory that was superior at avoiding failures.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Following this work, we aim to apply these principles to robot hardware and demonstrate robust performance for maneuvers such as leaping and flipping. We also aim to apply this work to other hybrid systems like robots that undergo stick-slip transitions. This work and its extensions will further enable robots to navigate complex, uncertain environments and unlock worlds for robots to explore.
