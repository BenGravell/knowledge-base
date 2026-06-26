<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Family of Iterative Gauss-Newton Shooting Methods for Nonlinear Optimal Control

Topics include Trajectory optimization, Multiple shooting, Gauss-Newton methods, Nonlinear optimal control, Iterative linear quadratic regulator, iLQR.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a unified family of iterative Gauss-Newton multiple-shooting methods for nonlinear optimal control, covering single and multiple shooting variants within a common framework with analysis of convergence and computational tradeoffs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces a family of iterative algorithms for unconstrained nonlinear optimal control. We generalize the well-known iLQR algorithm to different multiple-shooting variants, combining advantages like straight-forward initialization and a closed-loop forward integration. All algorithms have similar computational complexity, i.e. linear complexity in the time horizon, and can be derived in the same computational framework. We compare the full-step variants of our algorithms and present several simulation examples, including a high-dimensional underactuated robot subject to contact switches. Simulation results show that our multiple-shooting algorithms can achieve faster convergence, better local contraction rates and much shorter runtimes than classical iLQR, which makes them a superior choice for nonlinear model predictive control applications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "I-A Overview and Motivation", "weight": 1.0} -->

In this paper, we discuss a family of iterative Gauss-Newton shooting methods for numerically solving unconstrained optimal control problems, and illustrate the effectiveness of our algorithms with various robotics examples. We outline the connection between a number of 'direct' optimal control methods and Gauss-Newton methods from the class of Differential Dynamic Programming (DDP) algorithms. Additionally, we present a natural extension arising from this connection and introduce a family of hybrid Gauss-Newton Multiple Shooting methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Overview and Motivation", "weight": 1.0} -->

In direct approaches to optimal control, infinite-dimensional optimal control problems are transcribed into finite dimensional Nonlinear Programs (NLPs). Two prominent ways of transcription by 'shooting' are direct single shooting (SS) and direct multiple shooting (MS), which differ in the choice of decision variables. In single shooting, solely the control inputs are the decision variables. Generally speaking, the control trajectory is discretized in a piece-wise polynomial fashion (for simplicity, we focus on piece-wise constant controls in this paper, c.f. Fig. 1a). A corresponding state trajectory is obtained by means of numerical forward integration of the system dynamics, starting at a given initial state. SS is often called a 'sequential' approach. In multiple shooting, the same discretization scheme is employed for the control inputs, but additionally, intermediate states are added to the decision variables. This provides several advantages, but requires the introduction of additional matching constraints to ensure continuity of the state trajectory. The technique of introducing these additional degrees of freedom into the original problem, combined with adding matching constraints, is called *lifting*, and results in a 'simultaneous' method.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Overview and Motivation", "weight": 1.0} -->

The formulation of both SS and MS as standard NLPs is straightforward and any state-of-the-art NLP solvers can be used to solve them. It is important to note that under the assumption of having a piece-wise polynomial control parameterization, the intrinsic sparsity structure of the underlying optimal control problem of both SS and MS allow them to achieve linear time complexity by performing a Riccati recursion.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Overview and Motivation", "weight": 1.0} -->

Classical single shooting often does not perform well for unstable systems due to the pure open-loop forward integration of the system dynamics. In DDP, this is handled by doing a closed-loop forward integration, using a feedforward plus a time-varying state-feedback control law. The Riccati backward sweep designs time-varying feedback gains on the fly without additional computational cost. DDP is an exact-Hessian method, requiring the computation of second derivatives of the dynamics. While this gives the algorithm quadratic convergence, this can be impractical for use in systems with complex dynamics. For that reason, Hessian-approximating variants of DDP have become quite popular in the robotics community.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Overview and Motivation", "weight": 1.0} -->

An important Hessian-approximating variant of DDP is the *iterative Linear-Quadratic Regulator* (iLQR), which is also known as *Sequential Linear Quadratic Optimal Control*. This method can be classified as closed-loop single shooting using a Gauss-Newton Hessian approximation and a Riccati backward sweep to solve linear-quadratic (LQ) subproblems. The Gauss-Newton Hessian approximation is based on the assumption that the objective function can be locally approximated as a sum of quadratic terms, and requires only first-order derivatives of the system dynamics. This comes at the cost of giving only linear convergence, however. The Gauss-Newton approach can be lifted, too, which has for example been shown. While it initially appears to be a drawback to increase the number of decision variables, it is important to emphasize that the lifted problem can be solved at approximately the same computational cost as the original non-lifted problem, and can lead to a significant increase of convergence speed. Therefore, the fundamental motivation for this paper is to combine the benefits of iLQR with a multiple-shooting approach.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

In this work, we derive a lifted equivalent of iLQR, called *Gauss-Newton Multiple Shooting* (GNMS), which introduces the intermediate states as additional decision variables. Next, we extend this relationship to form an entire family of open-loop multiple-shooting algorithms, denoted GNMS($M$), and closed-loop multiple shooting algorithms, denoted as iLQR-GNMS($M$). The latter is shown to be a generalization of iLQR and can be considered multiple-shooting iLQR. We outline the relationship between these algorithms and existing methods. We give simulation examples including a complex underactuated robot and compare the performance of the full-step algorithms using data gained from hardware experiments. Furthermore, we show the benefits of iLQR-GNMS($M$) methods for nonlinear model predictive control.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-C Outline", "weight": 1.0} -->

This paper is structured as follows. In Section II, we derive GNMS, and present the basic update routine for state and control trajectories. Using these update equations, we generalize iLQR and GNMS to a family of algorithms in Section III. Section IV showcases several simulation results, based on data gained from hardware experiments. A discussion and outlook concludes the paper in Section V.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Gauss-Newton Multiple Shooting", "weight": 1.0} -->

In the following, a brief derivation of the unconstrained Gauss-Newton Multiple Shooting method is presented. We show the derivation using an intuitive value-function approach in the style of in order to highlight the close relationship between GNMS and iLQR. However, from the beginning, we lift the optimization problem and introduce intermediate states as additional decision variables besides the controls. In that sense, having each control decision variable accompanied with a state-decision variable, GNMS is closely related to the original multiple-shooting algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gauss-Newton Multiple Shooting", "weight": 1.0} -->

Consider the following discrete-time, finite-horizon, nonlinear optimal control problem with state-vector $\mathbf{x}_{n} \in {\mathbb{R}}^{m}$ and control input vector $\mathbf{u}_{n} \in {\mathbb{R}}^{p}$. Let $L_{n}$ be the intermediate cost at time-step $n$ and $\Phi{(\mathbf{x}_{N})}$ the terminal cost at the time horizon $N$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Forming LQ subproblems", "weight": 1.0} -->

The optimal control law is computed in an iterative way.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Forming LQ subproblems", "weight": 1.0} -->

In the first iteration, $k = 0$, the LQ problem is hence constructed around the initial guesses for $\mathbf{X}^{\lbrack 0\rbrack}$, $\mathbf{U}^{\lbrack 0\rbrack}$. Possible initialization strategies are summarized in Section III-D.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Forming LQ subproblems", "weight": 1.0} -->

At each iteration, we numerically forward integrate all multiple shooting intervals using the respective control inputs $\mathbf{u}_{n}^{\lbrack k\rbrack}$, starting at every state ${\mathbf{x}_{n}^{\lbrack k\rbrack}{\forall n}} = {0,1,\ldots,{N - 1}}$. Fig. 1c shows a sketch of the multiple-shooting intervals in GNMS, where the resulting state at the end of each interval is denoted $\mathbf{F}^{\lbrack k\rbrack}{(\mathbf{x}_{n}^{\lbrack k\rbrack},\mathbf{u}_{n}^{\lbrack k\rbrack})}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Forming LQ subproblems", "weight": 1.0} -->

Accordingly, we define the 'defect' between the integrated trajectory segment and the next intermediate state $\mathbf{x}_{n + 1}^{\lbrack k\rbrack}$ as Defining state and control increments $\delta\mathbf{x}_{n}^{\lbrack k\rbrack}$ and $\delta\mathbf{u}_{n}^{\lbrack k\rbrack}$ for every single time-stage $n$, we can write the nonlinear system dynamics constraint in terms of the simulated interval as which can also be considered a matching condition which ensures the continuity of the state trajectory w.r.t. state and control increments. Performing a first-order Taylor expansion of Equation w.r.t.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Forming LQ subproblems", "weight": 1.0} -->

$\delta\mathbf{x}_{n}^{\lbrack k\rbrack}$ and $\delta\mathbf{u}_{n}^{\lbrack k\rbrack}$, denoting the sensitivities w.r.t state and control $\mathbf{A}_{n}$ and $\mathbf{B}_{n}$ and taking into account the defects as defined by Equation, results in the following affine system dynamics constraint Analogously performing a second-order Taylor expansion of the nonlinear cost function gives rise to the following LQ optimal control problem where we assume ${\mathbf{Q}_{n}\text{,}\mathbf{Q}_{N}} \geq 0$ and $\mathbf{R}_{n} > 0$. Here, and in the following subsection, we drop the superscript indices $\lbrack k\rbrack$ for better readability.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Computing the Optimal Control by Riccati Recursion", "weight": 1.0} -->

Considering the LQ subproblem -, the optimal control and state updates can be computed using a value-function approach. Assume a quadratic value function of the form with weighting matrices $\mathbf{S}_{n} \in {\mathbb{R}}^{m \times m}$, $\mathbf{s}_{n} \in {\mathbb{R}}^{m \times 1}$ and $s_{n} \in {\mathbb{R}}$. The optimal control update can be derived by minimizing the value function $V_{n}$ as a function of $\delta\mathbf{x}_{n}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Computing the Optimal Control by Riccati Recursion", "weight": 1.0} -->

As Equation is quadratic in $\delta\mathbf{x}_{n + 1}$ at time $n + 1$, it remains quadratic during back-propagation in time, given the affine system dynamics and the linear-quadratic cost in Equations -. Due to Bellman's Principle of Optimality, the optimal control $\delta\mathbf{u}_{n}^{\ast}$ at time $n$ can be computed from Inserting Equation and the affine system dynamics and minimizing the overall expression w.r.t. $\delta\mathbf{u}_{n}$ leads to an optimal control update of the form where we have defined and ${{\mathbf{B}_{n}^{\top}\mathbf{S}_{n + 1}\mathbf{B}_{n}} + \mathbf{R}_{n}} > 0$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Computing the Optimal Control by Riccati Recursion", "weight": 1.0} -->

For the final time-step $N$ we obtain the terminal conditions $\mathbf{S}_{N} = \mathbf{Q}_{N}$, $\mathbf{s}_{N} = \mathbf{q}_{N}$ and $s_{N} = q_{N}$, and the recursion is subsequently swept backwards. Note that Equation does not contribute to the control update and can therefore be omitted in practice.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Updating State and Control Trajectories", "weight": 1.0} -->

Finally, using Equations and, and readopting the superscript indices $\lbrack k\rbrack$ for the iteration count, we obtain equations for a forward sweep resulting in a full-step update for the control and state decision variables $\mathbf{X}^{\lbrack{k + 1}\rbrack}$, $\mathbf{U}^{\lbrack{k + 1}\rbrack}$ with initial condition $\mathbf{x}_{0}^{\lbrack{k + 1}\rbrack} = \mathbf{x}_{init}$. The updated decision variables are dynamically consistent w.r.t. the LQ subproblem dynamics. The nonlinear optimal control problem is solved iteratively, starting from Section II-A and solving LQ subproblems at each iteration, until convergence.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Family of iLQR-GNMS Algorithms", "weight": 1.0} -->

Equations and present the GNMS update rule where all states and controls (except for $\mathbf{x}_{init}$) are decision variables. For every time-step, both states and controls are updated using a linear forward sweep. Considering Equations and, we can now draw connections between GNMS and other existing algorithms and extend them to a bigger family of 'hybrid' variants.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Connection to iLQR and Single Shooting", "weight": 1.0} -->

Interestingly, full-step iLQR employs the very same control update rule as in Equation. In fact, GNMS can be transcribed into iLQR by substituting the state update equation with a numeric forward integration of the nonlinear system using the time-varying state-feedback control law provided by Equation. In this case, the forward integration naturally results in a dynamically consistent state trajectory, all defects $\mathbf{d}_{n}$ become zero and the formulation from section II-B drops back to the well-known iLQR Riccati recursion. Moreover, standard unconstrained single shooting can be recovered by additionally ignoring the state feedback gains and running the forward-integration purely open-loop.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Hybrid Algorithms", "weight": 1.0} -->

Consider a case where the overall time horizon $N$ is split into an integer number of multiple shooting intervals $M$ with length $l$ and $1 < M < N$, while the control input discretization is kept at its original resolution. Without loss of generality, let us assume that the MS integration intervals start at time indices $i \in \mathcal{I}$, with $\mathcal{I} = {\{ 0,l,{2l},\ldots\}}$. Fig. 1d sketches an example of such a hybrid case with $l = 3$. Every interval is simulated using the nonlinear system dynamics and the initial states and controls $\mathbf{x}_{i}^{\lbrack k\rbrack}$ and $\mathbf{u}_{i}^{\lbrack k\rbrack}$. All $\mathbf{x}_{j}^{\lbrack k\rbrack}$ with $j \notin \mathcal{I}$ are *overwritten* by the integration.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Hybrid Algorithms", "weight": 1.0} -->

For an open-loop forward integration, $\mathbf{U}^{\lbrack k\rbrack}$ remains as is, but for a closed-loop forward integration, we additionally overwrite all $\mathbf{u}_{j}^{\lbrack k\rbrack}$ with $j \notin \mathcal{I}$ using the given feedback control law. Note that in this case, the defect equation remains valid, but is zero along the multiple-shooting intervals. The only non-zero defects occur at ${\mathbf{d}_{{i + l} - 1}^{\lbrack k\rbrack},i} \in \mathcal{I}$. In this setting, the LQ approximation, Riccati recursion and state- and control updates - can be performed as described before. This gives rise to two 'hybrid' GNMS variants: *GNMS(M)*, using solely the feedforward control and thus performing an open-loop forward integration on each of the $M$ multiple shooting intervals, which themselves are multiples of the control interval.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Hybrid Algorithms", "weight": 1.0} -->

Herewith, standard single shooting is the limit case GNMS.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Hybrid Algorithms", "weight": 1.0} -->

*iLQR-GNMS(M)*, using the full state feedback controller and a closed-loop forward integration of each multiple-shooting interval. In other words, this is equivalent to a multiple-shooting variant of iLQR. The standard iLQR algorithm is the limit case of iLQR-GNMS, with only one multiple-shooting interval.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Hybrid Algorithms", "weight": 1.0} -->

Note that both GNMS($N$) and iLQR-GNMS($N$), with the number of multiple shooting-intervals being equal to the number of stages, revert to the standard GNMS formulation as introduced in Section II. Table I provides a compact overview of the algorithmic variants and compares their features. overwrite states by integration need stable initial policy TABLE I: An overview of different GNMS-type methods.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Main Iteration and Implementation", "weight": 1.0} -->

We emphasize that all algorithmic variants feature linear complexity in the time horizon, $O{(N)}$. All algorithms execute almost identical linear algebra operations during one major iteration and therefore have very similar computational effort. Since the discussed family of GNMS algorithms only differs in a few features, it can be summarized in one framework, given in Algorithm 1. From a software-engineering perspective, the algorithmic variants are easy to implement and can all be treated at once, given a proper design of classes and interfaces. We provide an open-source C++ implementation of all discussed algorithms.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Initialization", "weight": 1.0} -->

The GNMS variants listed in Table I differ in their requirements for initialization. For iLQR and SS, the nominal state (and control) input trajectories are first updated through a forward integration. This implies that for unstable systems, an initialization with a stabilizing initial control policy, which keeps the first rollout in the vicinity of the expected optimum, is essential. For iLQR, the initially provided state trajectory $\mathbf{X}^{\lbrack 0\rbrack}$ serves as state reference trajectory for the feedback controller. For SS, it is irrelevant, except for the initial state. Common choices for SS and iLQR initial guesses are policies that stabilize the given initial state or draw the system towards the goal state, for example simple LQR or PD controllers. Generally, the increased efforts for initial guess design for SS and iLQR can be a significant disadvantage. In the worst case, a poor initial guess can lead to a local minimum with a solution far from desired behavior.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Initialization", "weight": 1.0} -->

Multiple-shooting algorithms, by contrast, offer greater flexibility and simplicity at initial guess design, and are often more robust w.r.t. bad initial policies. It is a well known fact that the convergence of multiple-shooting methods can be accelerated through an 'educated' initial guess, such as direct interpolation between initial and desired final state. For the hybrid algorithms iLQR-GNMS($M$) and GNMS($M$) it often depends on the system characteristics if a stabilizing control policy is required, or if the multiple-shooting intervals are short enough to prevent significant divergence during integration. In the video attachment, we show two simulation examples where initialization with a bad state-feedback controller significantly extends the runtime of iLQR compared to GNMS, or even causes iLQR to fail.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Initialization", "weight": 1.0} -->

Note that, when all possible GNMS variants are initialized with a dynamically consistent state trajectory and corresponding control trajectory, the defects for the first iteration are zero and the feedforward control updates are identical.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Initialization", "weight": 1.0} -->

- Nonlinear dynamics, cost function and initial state xi n i t as given in - - Initial state trajectory X - Initial feedforward trajectory U - (Initial feedback law, if applicable) - maximum total constraint violation dm a x - minimum relative cost change Jm i nr e l - set iteration count k = 0 - split time horizon N into M MS integration intervals of length l, each starting at an index i ∈ ℐ, ℐ = {0, l, 2 l, …} - Initial multiple-shooting rollouts - simulate M intervals using the nonlinear system dynamics and initial states and controls xi and ui, overwrite all xj and uj for j ∉ ℐ - compute defects dn according to Equation. Repeat (main iteration) - Linearize the dynamics along the trajectories, obtain the affine constraint - Quadratize cost function along the trajectories to obtain Riccati backward sweep - Backwards solve the Riccati-like difference equations - with boundary conditions SN = QN and sN = qN Linear forward sweep - compute state and control solution candidates X[k + 1] and U[k + 1] by forward sweeping Equations and.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Initialization", "weight": 1.0} -->

Rollout multiple-shooting intervals IF(open loop shooting) - set feedback gain in Equation to zero. - simulate M shooting intervals using nonlin. dynamics, controller and initial states and controls xi[k + 1] and ui[k + 1] ∈ ℐ, overwrite all xj[k + 1] and uj[k + 1] for j ∉ ℐ - compute defects dn[k + 1] according to Equation - compute cost J[k + 1] by evaluating Equation - increment iteration count k Algorithm 1 Generalized iLQR-GNMS(M) Algorithm

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A An Illustrative, One-Dimensional System", "weight": 1.0} -->

As an illustrative example, we present a simple one-dimensional system, which is slightly nonlinear, unstable and constructed to help the reader build an intuition about the methods. The system dynamics are $\overset{˙}{x} = {{{({1 + x})}x} + u}$, ${x{}} = 1.5$ and discretized with ${\Deltat} = 0.01$ s, $N = 300$. The cost function is defined as quadratic cost of form with desired terminal state $\mathbf{x}_{N}^{des} = 0$, $\mathbf{Q}_{N} = 10$ and $\mathbf{R}_{n} = 0.01$. Fig. 2 shows results for iLQR, GNMS and the hybrid variants with five multiple-shooting intervals, GNMS and iLQR-GNMS. We plot the state, control and defect trajectories for the first iteration of the algorithms, along with the initial guess and the converged solution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A An Illustrative, One-Dimensional System", "weight": 1.0} -->

The state and control trajectories illustrate the relationship between the algorithms: the multiple-shooting intervals of GNMS and iLQR-GNMS start with states and controls lying on the respective GNMS trajectories. For GNMS, the system is simulated open-loop, the controls are identical to GNMS, and the state trajectories on the multiple-shooting intervals start to diverge. By contrast, for iLQR-GNMS, in every multiple-shooting interval both state and control trajectories converge asymptotically towards the simulated iLQR state and control trajectories. For the hybrid variants, a defect occurs every 0.6s, for GNMS, the defect is evenly distributed across all time intervals. Due to the long shooting-intervals, GNMS requires one iteration more to catch up with the other algorithms in terms of overall cost. Importantly, the control update plot shows that the asymptotic contraction rates, which are defined as are not the same. In this example, GNMS and GNMS show better contraction than iLQR. Asymptotic contraction rates are investigated in more detail in Section IV-C.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Quadruped Trot Optimization Example", "weight": 1.0} -->

The quadrupedal robot 'HyQ' is an 18 DoF, floating-base underactuated robot subject to contacts with the environment, c.f. Fig. 3. In this paper, the contacts are not Figure 3: The quadruped HyQ incorporated as constraints, but added to the system dynamics using an explicit contact model. We employ a static, plain environment and a 'soft' contact model, consisting of a nonlinear spring in surface-normal direction and a nonlinear damping term. The contact model is detailed. Using this formulation, the contact force is a function of the current robot state only. It is clear that such a soft contact model presents only a rough approximation of the complicated physics of contact, and also introduces a number of potential disadvantages such as increased stiffness and nonlinearity of the combined system dynamics. However, the contact model allows a straight-forward computation of derivatives, which creates an ideal test-bed for comparing our shooting algorithms. We obtain exact discrete sensitivities $\mathbf{A}_{n}$ and $\mathbf{B}_{n}$ through evaluating a sensitivity differential equation on the multiple-shooting intervals.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Quadruped Trot Optimization Example", "weight": 1.0} -->

The example task considered is the optimization of a periodic trotting gait. To achieve the trotting gait, we impose a time-varying quadratic penalty on the leg joint positions. Furthermore, we penalize the intermediate and final position of the robot's trunk and the intermediate and final velocities of the leg joints. For an in-depth description of the cost modelling to achieve different gait patterns the reader is referred to. In the following, the trotting gait optimization is used to compare the algorithms developed in this paper. For a meaningful comparison, we initialize all algorithms with identical state trajectories and control policies. The initial guess corresponds to standing still in a steady state. We optimize over 36 states, 12 control inputs and a total time horizon of 2.5 seconds with $N = 2500$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Quadruped Trot Optimization Example", "weight": 1.0} -->

Fig. 4 compares iLQR, GNMS, and iLQR-GNMS($M$) with three different numbers of multiple-shooting intervals in terms of cost descent, control update norms and total defects. Note that SS and GNMS($M$) are unstable due to the strong instability of the system. All remaining algorithms converge to the same minimum within 20 iterations. iLQR and iLQR-GNMS show short phases of increasing cost, which we accept in this simulation example. Since the provided initial guess is dynamically consistent, the initial defects are zero. GNMS, having the largest number of multiple-shooting intervals, also shows the largest total defect sum after the first iteration. The multiple-shooting iLQR methods, all having significantly fewer continuity constraints to enforce, feature a lower total defect.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Quadruped Trot Optimization Example", "weight": 1.0} -->

As expected for a Gauss-Newton method, all approaches show linear convergence. Considering the control update norms, we see that GNMS and iLQR feature a similar contraction rate for this example. In fact, the contraction rate of GNMS is slightly better, which is visually hard to distinguish here, but is detailed in following example. For the hybrid multiple-shooting iLQR variants, we observe a significantly better contraction rate than for both iLQR and GNMS. When applying an identical termination criterion based on the relative change of the cost function and a defect threshold to all algorithms, all lifted methods converge in fewer iterations than iLQR. Furthermore, all displayed iLQR-GNMS($M$) variants converge notably faster than GNMS. Screen recordings of the optimized trotting motions are provided in the video attachment.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Local Contraction Rates for Quadruped Trot Tracking", "weight": 1.0} -->

While Section IV-B gives an optimization example for a single motion, starting with an initial guess far from the optimal solution, we now show a comparison based on statistical data from $1000$ runs: the trotting gait from Section IV-B is now considered in a tracking MPC problem. All algorithms are initialized with an optimal, dynamically consistent solution, but the initial state is locally perturbed. The state perturbations are sampled from the hardware-experiments detailed. For every perturbation, we let different algorithms iterate until convergence. Fig. 5 compares average asymptotic contraction rates for four different algorithms. It shows the normalized difference between a fully converged optimal feedforward trajectory and trajectories obtained at previous iterations. Furthermore it shows first-order regressions approximating the local contraction rates, in terms of the slopes of the difference norms in the semi-logarithmic plot. It can be seen that GNMS outperforms iLQR in terms of local contraction rate.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Local Contraction Rates for Quadruped Trot Tracking", "weight": 1.0} -->

GNMS shows a contraction rate similar to GNMS. The example indicates better local convergence for iLQR-GNMS than for classical iLQR, GNMS and GNMS.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Local Contraction Rates for Quadruped Trot Tracking", "weight": 1.0} -->

Fig. 6 generalizes the result from Fig. 5 for a range of multiple-shooting intervals $M$, showing numerically approximated asymptotic contraction rates, Equation, as a function of $M$. Again, GNMS($M$) is unstable for overly long multiple-shooting intervals, similar to the limiting case open-loop single shooting. For closed-loop shooting, the asymptotic contraction rates for all multiple-shooting variants are better than for iLQR, and the contraction rates for the hybrid variants outperform the limiting case GNMS. In this example, the relative improvement over iLQR is up to a factor two. Note that the resulting iLQR-GNMS($M$) contraction rates differ slightly from the ones in Fig. 4 for $M = {25,50,100}$, which is due to the different problem setting. However, both experiments exhibit the same trend.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-D Nonlinear MPC on HyQ", "weight": 1.0} -->

The suitability of iLQR for nonlinear model-predictive control (NMPC) in robotics applications has been shown many times before,. In this section, we show that GNMS and its hybrid variants are even more promising for NMPC applications. First, they converge faster to the optimal solution, c.f. Section IV-C. A second advantage of the multiple-shooting variants of the presented algorithms is that the forward integrations can be parallelized. Therefore, the achievable MPC cycle time decreases approximately linearly with the number of available CPU cores. By combining faster update rates with better contraction rate, our multiple-shooting algorithms outperform classical iLQR-NMPC.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Nonlinear MPC on HyQ", "weight": 1.0} -->

In the following simulation example, we compare the NMPC performance of our Gauss-Newton shooting algorithms against iLQR-NMPC in a HyQ simulation environment. In each NMPC cycle, we run an adapted version of the main iteration in Algorithm 1 and 'warm-start' it with the previous solution. In such a setting, we can separate an NMPC iteration into a 'preparation' and a 'feedback' phase, thus minimizing the latency between receiving a state-measurement and sending an updated policy to the control system. Our NMPC loop is described in Algorithm 2.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Nonlinear MPC on HyQ", "weight": 1.0} -->

- cost function and system dynamics. - receding MPC time horizon N - number of multiple-shooting intervals M with length l - initial state and control trajectories X = {x0, x1, …, xN} U = {u0, u1, …, uN − 1}, state-feedback controller un (x) of form - get state measurement xm e a s. - forward integrate system dynamics with x0 = xm e a s on the first multiple-shooting interval, compute A0, …, l − 1, B0, …, l − 1, defect dl − 1 - quadratize cost function around X and U for control stages 1, …, l − 1. - solve LQ optimal control problem using a Riccati backward sweep - retrieve updated control policy un+ (x) and updated trajectories U+, X+.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Nonlinear MPC on HyQ", "weight": 1.0} -->

- send policy un+ (x) and X+ to the control system - forward integrate system dynamics for the multiple-shooting intervals 1 to M, obtain sensitivities Al, … AN − 1, Bl, …, BN − 1 - quadratize cost function around X, U for multiple-shooting intervals l to N. Algorithm 2 iLQR-GNMS(M)-NMPC Algorithm In this experiment, we run a trotting gait on HyQ, in closed-loop MPC in a simulation environment. For the NMPC optimal control problem, we choose a time-step size of 4 ms and $N = 125$. We parallelize the integration of all multiple-shooting intervals and the sensitivity computation on four cores, and run both simulator and MPC controller on the same notebook equipped with an Intel Core i7 (2.8 GHz) processor. For four different algorithmic combinations, we record the executed trot under identical conditions for 18 seconds and compute the resulting accumulated intermediate cost. A summary of the achieved average cost and NMPC frequencies is given in Fig. 7. In these experiments, iLQR results in the highest accumulated cost.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Nonlinear MPC on HyQ", "weight": 1.0} -->

The multiple-shooting variants outperform iLQR, with relative cost differences up to 5%. At the same time, due to shorter runtimes, the multiple-shooting variants achieve up to 40% higher MPC frequencies, with a maximum of 103 Hz.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-D Nonlinear MPC on HyQ", "weight": 1.0} -->

In our simulation, all four algorithm variants run in a stable and robust fashion. The relatively small cost difference is an indicator of better convergence, but the main reason why the multiple-shooting variants should be preferred over iLQR in real-world applications, is the superior control bandwidth. The algorithms in this paper have been validated in hardware experiments on two different quadruped platforms, where a variety of motions and gaits was implemented. However, a in-depth description of the experimental setups, the optimized computational framework and practical tuning considerations are beyond the scope of this paper. The interested reader is therefore referred to, where we apply the GNMS-algorithm for full-body NMPC on the quadrupeds HyQ and ANYmal, explain the robotic setup in detail and present a variety of hardware experiments. As outlook, a video sequence of GNMS-NMPC running on hardware is provided in the attachment.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion and Outlook", "weight": 1.5} -->

In this paper, we have shown how the well-known iLQR algorithm can be lifted and transformed into Gauss-Newton Multiple Shooting, GNMS. We have generalized the concept to form a family of Gauss-Newton shooting algorithms, which can be distinguished into sequential and simultaneous algorithms and closed and open-loop algorithms. Some algorithms partially overwrite decision variables by means of a numeric forward integration. All presented variants have approximately the same computational cost and feature linear time-complexity. Furthermore, all discussed algorithms share a large number of computational routines, and it is not difficult to implement all of the presented variants in a single software framework.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion and Outlook", "weight": 1.5} -->

We have compared the performance of the algorithms in different simulation experiments, which indicate that the lifted algorithms can outperform classical iLQR. While not included in this paper for reasons of compactness, similar results were obtained for other rigid-body dynamic systems including a 6 DoF fixed-base arm model. A more fundamental investigation for formalizing the conditions that result in improved convergence rates for GNMS($M$) and iLQR-GNMS($M$) is subject to ongoing work.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion and Outlook", "weight": 1.5} -->

In the application examples, we limited the comparison to full-step variants of all considered algorithms. However, for even more nonlinear dynamics or cost functions, where the LQ optimal control problem is a bad approximation to the nonlinear problem, a globalization strategy may be required. For single-shooting methods, a straight-forward solution is to employ a line-search scheme. This is simple to implement, as it is sufficient to search over the cost for different control update step-sizes. For multiple-shooting approaches, however, there are additional continuity constraints, and we need to line-search over a merit-function which trades off the costs and defects. It is typically required to introduce additional tuning variables or to implement a complex filter-scheme. Our open-source reference implementation provides a line-search scheme using a simple merit function.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion and Outlook", "weight": 1.5} -->

For complex robot trajectory optimization problems, we do not recommend to generally prioritize one of the presented algorithms over another. While the multiple-shooting algorithms allow for advanced initialization strategies and are more robust w.r.t. bad initial guesses, they may require slightly more tuning efforts when the full-step algorithm is not sufficient. By contrast, in NMPC applications with well-defined cost functions and using warm-starting, additional globalization steps are rarely required at all. Here, our multiple-shooting algorithms offer significant advantages, better local contraction rates and much shorter runtimes.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and Outlook", "weight": 1.5} -->

The focus of this paper is on unconstrained optimal control problems without general (in)equality path constraints. It is obvious that the lifting approach naturally transfers to equality-constrained variants of iLQR, such as. The inclusion of general (in)equality path constraints is part of ongoing work. One option to include them in the existing framework is to replace the standard Riccati backward sweep with a dedicated solver for constrained LQ optimal control problems. In this way, general (in)equality path constraints can be included while keeping linear time-complexity.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and Outlook", "weight": 1.5} -->

While this work treats algorithms using a Gauss-Newton Hessian approximation, it similarly transfers to exact-Hessian approaches, resulting in a multiple-shooting DDP algorithm combining the advantages of simultaneous methods, quadratic convergence and closed-loop integration.
