<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Reference-Free, Long-Horizon Trajectory Optimization for Aggressive Autonomous Driving in Milliseconds

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicles must generate long-horizon and dynamically feasible trajectories in real time-even when operating at the limits of vehicle handling-to ensure safe operation in adverse conditions. However, existing work rarely quantifies the computational demands of generating such trajectories without prior references, warm starts and often defaults to low-fidelity models, compromising accuracy and control authority. We investigate the modeling and solver design choices that enable real-time solution of long-horizon, reference-free optimal control problems (OCPs) using full vehicle dynamics. To this end, we analyze vehicle stiffness properties to justify the OCP's integration scheme and show that lower-order A-stable methods consistently outperform alternatives, with solve time differences reaching two orders of magnitude. We show that robust nonlinear solver performance hinges on understanding barrier parameter update strategies and safeguarding techniques for Hessian indefiniteness, inherent in some interior point methods. Lastly, we propose a computationally efficient method for generating initial guesses using dynamic equilibrium, unlocking real-time performance and reducing initial infeasibility by up to four orders of magnitude.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensive benchmarking and high-fidelity BeamNG simulation demonstrate compute times as low as 55 ms over a 260 m horizon, including high-speed obstacle avoidance scenarios where drifting emerges as a necessary component of feasible trajectory generation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To ensure safety in all critical situations, autonomous vehicles must be engineered to exploit the absolute limits of their dynamic capabilities, pushing beyond the boundaries of normal vehicle operation. Existing work has established that intentionally pushing a vehicle beyond traditional operational limits not only expands the safety envelope but can often be the only feasible evasive maneuver. Such maneuvers require long-horizon and dynamically feasible planning for linking immediate actions to their downstream consequences in unforeseen situations. Unlocking this capability requires a paradigm shift from conventional short-horizon reference tracking to solving a reference-free, long-horizon optimal control problem (OCP) in real time (5-10 Hz). This paper presents a systematic investigation into the fundamental design choices required to construct such a framework, thereby expanding the operational envelope of autonomous vehicles.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Prior approaches underscore the complexity of solving the full nonlinear OCPs from scratch, identifying the underlying problems as highly sensitive to initial guesses and too computationally intensive for real-time deployment. This has led to a shared strategy across both high-performance racing and autonomous drifting: decoupling the problem into offline reference generation and online tracking. Even though they are successful in handling even pop-up obstacles, the core dependency of such approaches to an offline-generated reference precludes their adaptation to a dynamically changing course. Recent attempts toward real-time generation include a task-specific OCP to transition between drift equilibria, and reinforcement learning (RL) to generate drift trajectories. However, the former remains highly task-specific, while RL's reliance on training data makes its reliability in unfamiliar scenarios difficult to guarantee.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Although existing work excels at reference tracking, the foundational challenge of real-time reference generation from scratch remains largely unaddressed, favoring offline or task-specific solutions. As a consequence, critical design choices that directly impact real-time performance, such as an accurate and efficient numerical integrator, the nonlinear solver strategy, and a strategy for a generalizable initial guess, are rarely examined. This paper addresses this gap by presenting a systematic design of a trajectory optimization framework for solving the full nonlinear, reference-free OCP in real time. Our contributions are as follows: • Through extensive benchmarking, we show that, while interior point methods outperform sequential quadratic programming (SQP) approaches for trajectory generation, commonly used solvers like IPOPT are unsuitable for real-time use. Our findings reveal that robust and real-time performance emerges from carefully selected barrier update and numerical ill-conditioning handling strategies found in solvers like KNITRO.\• We analyze the stiffness properties of vehicle dynamics and establish a principled basis for selecting stable and computationally efficient integration schemes. Further, our evaluation of nine numerical integrators reveals computational performance differences of up to two orders of magnitude.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Critically, we demonstrate that due to system stiffness, lower-order A-stable methods surprisingly outperform higher-order, non-A-stable methods in terms of accuracy.\• We propose a strategy to generate a high-quality, reusable initial guess for the OCP by solving a single-node, box-constrained least-square problem formulation. Such a guess is computationally cheap to obtain, is by construction dynamically feasible, reduces total initial feasibility error for the optimizer by three to four orders of magnitude compared to an ill-informed guess, while enabling real-time performance. We then show the robustness of this guess by solving OCPs spanning both time-optimal racing and collision avoidance.\• We validate our approach on a critical collision avoidance scenario, where drifting around the obstacles is the only feasible solution. Our framework generates a drifting trajectory at highway speeds ($90$ km/hr) in real time ($72$ ms), while constraining emerging drift behavior renders the problem infeasible. To confirm real-world viability, we demonstrate successful tracking of trajectories for both racing and obstacle avoidance in a high-fidelity BeamNG simulation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

We use a single-track vehicle model in curvilinear coordinates, considering the wheel speed and load transfer dynamics in a curvilinear coordinate system. The vehicle's position is described by its arc length, $s$, and lateral error, $e$, relative to a reference path with curvature $k_{\mathrm{ref}}(s)$. The equations of motion are given: where the state $\mathbf{x}=[{r},{V},\beta,{V}_{\omega r},\Delta{F}_{z},{e},\Delta\psi,{s},t]^{T}$, the control $\mathbf{u}=[\delta,T_{\mathrm{comb}},T_{\mathrm{bf}}]^{T}$, and the independent variable $s$ is such that $\dot{s}=V\cos(\Delta\psi)/(1-k_{\mathrm{ref}}(s)e)$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

Here, $\Delta\psi$ is the velocity vector orientation error w.r.t. path, $r$, $V$, $\beta$ are the yaw rate, vehicle speed, and side slip angle respectively, $V_{\omega r}$ is the rear wheel longitudinal speed, $\Delta F_{z}$ is the dynamic load transfer (front to rear), $F_{x,net}=F_{xr}+F_{xf}\cos\delta-F_{yf}\sin\delta$ is the net longitudinal force, and $\delta$ is steering angle.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

We combine the engine torque $T_{\mathrm{\mathrm{eng}}}\geq 0$ and rear brake torque $T_{\mathrm{br}}\leq 0$ to $T_{\mathrm{comb}}$ such that $T_{\mathrm{eng}}=\max(0,T_{\mathrm{comb}})$ and $T_{\mathrm{br}}=\min(0,T_{\mathrm{comb}})$. As for the model parameters, $m$ is the vehicle mass, $I_{z}$ the inertia, $a,b,L,h_{cg}$ geometric parameters of the vehicle (front and rear distances from the center of mass, wheelbase, CG height), and $R_{w},I_{w}$ are the wheel radius and rear wheel inertia, respectively.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

To model tire forces $(F_{xf},F_{yf},F_{xr},F_{yr})$, we use the isotropic coupled slip brush Fiala model The magnitude of the tire forces $(F_{\textrm{total},f},F_{\textrm{total},r})$ are where $(\sigma_{f},\sigma_{r})$ are the total tire slips, and $(\sigma_{\textrm{sl},f},\sigma_{\textrm{sl},r})$ are the total slips as the tires begin fully sliding The tire loads $(F_{zf},F_{zr})$ depend on the static tire loads $(F_{\textrm{nom},zf},F_{\textrm{nom},zr})$ as $F_{zf}=F_{\textrm{nom},zf}-\Delta F_{z}$ and

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Minimum Time Discrete Optimal Control problem", "weight": 1.0} -->

We employ direct multiple shooting with both states and control as the decision variables of our optimization problem. The state and control variables are discretized for a constant $\Delta s_{k}:=s_{k+1}-s_{k}$. $\mathcal{F}$ is defined as a general map $\mathcal{F}:\mathbb{R}^{n_{x}}\times\mathbb{R}^{n_{x}}\times\mathbb{R}^{n_{u}}\times\mathbb{R}\to\mathbb{R}^{n_{x}}$ that approximates the next state $x_{k+1}$. Defining the lower and upper bounds on control $\underline{u},\overline{u}$ and its rate $\underline{\dot{u}},\overline{\dot{u}}$, the OCP is formulated as. We define a common objective of minimum time for both racing and collision avoidance studies as it serves well for both.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Minimum Time Discrete Optimal Control problem", "weight": 1.0} -->

Except for the variables fixed at boundary conditions(e.g., $s$, $t$, $e$), the above problem is a free initial $\mathbf{x}_{0}$ and final state $\mathbf{x}_{f}$ problem, which helps maintain a general structure. In addition to the track boundaries, we impose bounds on the vehicle's velocity, as this was empirically found to accelerate solver convergence. Furthermore, vehicle-specific control bounds and slew rate constraints are also enforced. The tire saturation constraints prevent the wheels from going beyond their slip limits for racing and can be relaxed for collision avoidance scenarios to allow full dynamic range. A small constant $\epsilon$ is introduced in the tire saturation constraints to prevent infeasibility from brief, instantaneous saturation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Interior Point Methods for Large Scale NLP", "weight": 1.0} -->

Although both sequential quadratic programming (SQP) and interior-point (IP) methods solve large-scale non-linear programming (NLP) problems like, recent benchmarks show the superior performance of IP solvers such as IPOPT and KNITRO over SQP alternatives like SNOPT, which lies in-line with our findings in Sec. VI. However, the robust performance of IP methods is contingent upon several key factors: the strategy for handling non-convexity (i.e., an indefinite Hessian), the barrier parameter update rule, and the choice of globalization technique to ensure convergence. Therefore, we present a brief overview of Interior-Point (IP) theory to accompany our discussion in Sec. VI on the various solver properties that help improve performance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Interior Point Methods for Large Scale NLP", "weight": 1.0} -->

The optimization problem in can be re-written as, where ${\eta}\in\mathbb{R}^{N\times n_{x}+n_{u}\times(N-1)}$ is the new stacked decision variable and $c$ is the cost function. All equality constraints are stacked into $c_{E}$, representing general non-linear equality constraints. Similarly, inequality constraints (track/path bounds), (control, control rate bounds), (tire saturation) can be stacked into $c_{I}\in\mathbb{R}^{I_{m}}$ representing general nonlinear inequality constraints. Slack variables $s_{i}\in\mathbb{R}^{I_{m}}$, $s_{i}>0$ and a barrier parameter $\mu$ are introduced. An IP algorithm solves a set of approximate barrier problems for a sequence of positive barrier parameters $\mu_{k}$ that converge to zero.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Interior Point Methods for Large Scale NLP", "weight": 1.0} -->

we write the KKT conditions for problem as: where $y$ and $z$ are vectors of Lagrange multipliers, $e=(1,...,1)^{T}$, $S=\text{diag}(s_{1},...,s_{m})$, $A_{E}$ and $A_{I}$ are the Jacobian matrices of constraints $c_{E}(\eta)$ and $c_{I}(\eta)$, respectively. Defining the Lagrangian $\mathcal{L}$, the merit function for measuring progress towards a feasible and optimal solution $\phi$, and the corresponding Newton step to update the primal and dual variables $\eta,s,y,z$ as follows: where $\nu>0$. If the matrix in eq is well defined in terms of inertia, then the step $d$ is a descent direction for the merit function $\phi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Interior Point Methods for Large Scale NLP", "weight": 1.0} -->

Through backtracking line search, step-length $\alpha$ can be computed, and the decision variables at the next iterate $\eta^{+},s^{+},y^{+},z^{+}$ can be obtained using: Our analysis in the results Sec. (VI) demonstrate how the treatment of bad inertia or indefiniteness of the Hessian matrix $\nabla_{\eta\eta}^{2}\mathcal{L}$ in the Newton step and the barrier parameter ($\mu$) update strategy, dictate solver performance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stiffness and Integrator Study", "weight": 1.0} -->

Implicit and explicit integration techniques are known to perform well for stiff and non-stiff ODEs, respectively. To inform our choice of integrator, we first calculate the stiffness ratio at each node along a converged time-optimal trajectory for an oval track. Given the dynamics map $f$, i.e. $\dot{x}(s)=f(x(s),u(s))$, the stiffness ratio $SR$ can be defined as the ratio of the magnitude of the fastest-decaying mode (largest real $\Re$ negative eigenvalue $\lambda_{j}$ magnitude) to the slowest-decaying mode (smallest real negative eigenvalue magnitude) of the Jacobian $J_{k}$ of $f$: We calculate a participation matrix using the right and left eigenvalues for the Jacobians $J_{k}$ and backtrack the contribution of each state at every node in the stiffness ratio.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stiffness and Integrator Study", "weight": 1.0} -->

*The results in Figure 2 show the system is conditionally stiff, with the $SR$ peaking above $4500$ during aggressive maneuvers, far exceeding the traditional stiff threshold of $10^{3}$.* This stiffness originates primarily from the fast dynamics of the sideslip angle ($\beta$), which is consistent with the vehicle's physical behavior during high-speed cornering. This result implies the need to use implicit numerical integrators to prevent destabilization of iterations during optimization.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stiffness and Integrator Study", "weight": 1.0} -->

We study the impact of different integrators for the map $\mathcal{F}$ in primarily on two metrics: (a) the solution accuracy compared to a ground truth, (b) the computational time required to solve the OCP. Each integrator is evaluated in combination with three solvers---IPOPT, KNITRO, and SNOPT. The test problem is a time-optimal $260$ m oval track trajectory ($N=100$), initialized from a dynamically feasible centerline guess. This study is motivated by the need to match an integrator's properties, such as its stability and order, with the underlying system dynamics and its characteristics, such as stiffness. We benchmark nine numerical integrators: explicit methods (RK2, RK4) and implicit methods (Implicit Euler, Backward Differentiation Formula (BDF) 4, 5, 6, Crank-Nicolson, Adams-Moulton 3-stage, and Gauss-Legendre 2-stage).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stiffness and Integrator Study", "weight": 1.0} -->

A key property for differentiating implicit schemes can be A-stability; an A-stable integrator guarantees that the numerical solution to a stable physical problem will not become unstable, regardless of the integration step size. We note that among the methods tested, only the Implicit Euler, Crank-Nicolson, and Gauss-Legendre methods are A-stable. The ground truth solution was generated with a 6th-order A-stable Gauss-Legendre-3s method, verified against CVODES integration solver in Casadi. Although they produced identical results, both were omitted from the benchmark study due to their prohibitive solve times.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Robust Initial Guess Formulation", "weight": 1.0} -->

A strategy for initializing complex OCPs is first to generate a dynamically consistent trajectory to serve as an initial guess. While a dynamically feasible guess can help initialize the main OCP, generating this guess itself requires solving another OCP of similar complexity. This approach effectively layers one complex optimization problem on top of another, increasing the overall computational burden and introducing further points of failure. To circumvent the complexity of generating a full trajectory guess, we propose a simple yet powerful initialization method.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Robust Initial Guess Formulation", "weight": 1.0} -->

We propose a box-constrained nonlinear least square problem minimizing the dynamic rates (subset of the full system state) given by $\dot{x}_{\mathrm{dyn}}=[\dot{r},\dot{V},\dot{\beta},\dot{\omega}_{r},\dot{\Delta{F}}_{z}]^{T}$, which is solved to an optimality cost of zero, ensuring feasibility of the dynamic part of the equations of motion. We restrict ourselves to finding a single dynamically feasible set of state and control pairs for a given vehicle, making it computationally cheap, and initialize the dynamic components ($x_{\mathrm{dyn}}$) at every node of the OCP with this pair.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Robust Initial Guess Formulation", "weight": 1.0} -->

Since direct multiple shooting is employed, that is every node has its own state and control variables, this computed state-control pair should satisfy the ${x_{\mathrm{dyn}}}_{k+1}=\mathcal{F}({x_{\mathrm{dyn}}}_{k+1},{x_{\mathrm{dyn}}}_{k},u_{k};\Delta s_{k})$ at every node of the OCP (as rates are zero) bringing down the feasibility error of the guess. The kinematic components $e,\Delta\phi$ are initialized with zeros representing centerline position, $s$ is known a priori, and $t$ is initialized by using an average velocity guess $V_{avg}$ and total path distance $s_{\mathrm{end}}-s_{0}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Robust Initial Guess Formulation", "weight": 1.0} -->

\leq\ {u}_{\mathrm{guess}}\ \leq\ \overline{u}\end{aligned}\right.$ | | | We emphasize that the cost function and bounds in the above problem can be customized to produce different responses; we opted to obtain a straight line driving condition and introduce $(V-V_{\omega_{r}})^{2}$ to minimize slip. The guess once computed for a vehicle can be fixed and is not required to be recomputed.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Results", "weight": 1.0} -->

We frame the OCP for a Lexus LC 500 vehicle model in MATLAB R2024b via CasADi interfaced with IPOPT, SNOPT, and KNITRO NLP solvers. The benchmarks were run on a desktop PC with a 5.7GHz AMD Ryzen 9 9950X processor, with Just-In-Time (JIT) compilation enabled for all results except those in Table I.

<!-- chunk {"id": "body-0027", "role": "body", "section": "VI-A Integrator and Solver Tandem Study Results", "weight": 1.0} -->

The comprehensive results for the integrator study introduced in Sec. IV are summarized in Figure 3, and Table I. Solution accuracy is quantified by the normalized root mean square error (NRMSE) for each control input $u_{j},j=1,2,3$, which is the standard root mean square error between the computed trajectory $u_{j}$ and the ground truth, $u_{j}^{*}$. Figure 3 illustrates the trade-off between solution accuracy and computational cost by plotting the maximum NRMSE % made in a control input against the CPU solve time for each integrator-solver pair (averaged over 10 consecutive solves of each combination). Table I provides a detailed breakdown of the CPU times for each integrator-solver pair. Note that rather than employing hidden internal Newton iterations to resolve the implicit dynamics at each step, the optimizer solves for the states, controls, and any multi-stage variables simultaneously as a single NLP problem.

<!-- chunk {"id": "body-0028", "role": "body", "section": "VI-A Integrator and Solver Tandem Study Results", "weight": 1.0} -->

We summarize our findings as follows:\Figure 3: (a) Different numerical integrators and optimization solver pairs plotted with NRMSE% depicting accuracy (Y-axis) and computation time (X-axis). (b) Iteration-wise converged time-optimal solution generated under 55ms iterations for an oval track starting from the introduced guess strategy, illustrating optimal vehicle path, states, and control sequences.

<!-- chunk {"id": "body-0029", "role": "body", "section": "VI-A Integrator and Solver Tandem Study Results", "weight": 1.0} -->

• Implicit vs Explicit methods: The results confirm the unsuitability of explicit integrators for this problem, aligning directly with our stiffness analysis (Sec. IV). The stiff dynamics impose severe penalties on explicit schemes, placing both RK2 and RK4 in the top-right quadrant of Figure 3(a), characterized by high computational cost and poor accuracy. None of the solvers converge to the optimal solution when using the single-stage RK2 method, as shown in Table I. Although KNITRO succeeds with the four-stage RK4, its solve time of $8.54$ seconds is prohibitive for real-time use as it is nearly $100$ times slower than the implicit Euler scheme.

<!-- chunk {"id": "body-0030", "role": "body", "section": "VI-A Integrator and Solver Tandem Study Results", "weight": 1.0} -->

• Accuracy and A-stability: A critical insight from Figure 3 (a) is that for this stiff dynamics, simply using a higher order integrator does not guarantee a more accurate solution. Instead, the property of A-stability emerges as the dominant factor. A clear pattern is visible among the A-stable implicit methods. As the order increases from the 1st-order implicit Euler ($3$--$5\%$ error) to the 2nd-order Crank-Nicholson ($<1\%$ error), and finally to the 4th-order Gauss-Legendre 2 ($0.1\%$ error), the solution accuracy consistently improves. Conversely, non-A-stable, higher-order methods like BDF 4-6 and Adams-Moulton 3-stage violate this trend, yielding larger errors than the second-order Crank-Nicholson.

<!-- chunk {"id": "body-0031", "role": "body", "section": "VI-A Integrator and Solver Tandem Study Results", "weight": 1.0} -->

• Computational Efficiency: To identify the best configuration for our problem, we fix an upper bound on the maximum NRMSE $\%$ to be $5\%$, and the upper bound on computational time to be $0.2$ seconds. Within these bounds, the combination of the A-stable implicit Euler integrator and the KNITRO solver performs best, achieving convergence in just $0.087$ seconds (Table I) with an error margin of $3-4\%$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "VI-A Integrator and Solver Tandem Study Results", "weight": 1.0} -->

• Solver Performance: As shown in Table I and Figure 3, the second-order IP solvers (KNITRO, IPOPT) exhibit superior robustness than the first-order SQP-based SNOPT, which frequently converges to suboptimal solutions. This performance gap underscores the importance of exact Hessian information for reliable convergence in highly nonlinear problems, where the quasi-Newton approximations employed by SNOPT appear insufficient. While both IP solvers demonstrate consistent robustness, KNITRO achieves notably faster solve times---often two to three times faster than IPOPT.

<!-- chunk {"id": "body-0033", "role": "body", "section": "VI-B Robust Initial Guess Results", "weight": 1.0} -->

Comp time gain (×) TABLE II: KNITRO per-segment performance: zero guess vs. robust initial guess. NS = evaluation/convergence failure Using the optimal integrator-solver pair (Implicit Euler with KNITRO) we found for our problem, we evaluate the impact of our robust initialization strategy (Sec. V) against an ill-informed, zero guess. The feasibility error representing the maximum constraint violation is computed for the time-optimal OCP around an oval track at the two guesses. The robust guess provides a starting point with an error of just $9\times 10^{-1}$; conversely, the ill-informed guess is strongly infeasible, beginning with an error of $6.7\times 10^{3}$. Moreover, when the same time-optimal problem is solved across the following robustness test for $10$ different racing track segments, a similar difference in initial feasibility error is observed. This four-order-of-magnitude decrease in initial infeasibility effectively transforms the optimization landscape, providing a better starting point for the optimizer.

<!-- chunk {"id": "body-0034", "role": "body", "section": "VI-B Robust Initial Guess Results", "weight": 1.0} -->

Figure 3 (b) illustrates the iteration-wise descent (light yellow to dark blue) towards the optimal solution that took only $55$ ms and $22$ iterations to converge. Particularly, the dynamic states and controls are initialized with the same constant $x_{\mathrm{guess}},u_{\mathrm{guess}}$ computed using the proposed guess formulation in Sec. V, from where the optimization proceeds towards an optimum.

<!-- chunk {"id": "body-0035", "role": "body", "section": "VI-B Robust Initial Guess Results", "weight": 1.0} -->

Further, to isolate the impact of the robust initial guess from the robustness of the optimizer, keeping the integrator-solver pair intact, we solve a time-optimal OCP on $10$ distinct $250$ m ($N=100$) segments of a racetrack, starting from the fixed robust guess and a zero guess (initializing all decision variables with $0$). The results, presented in Table II, highlight three critical findings. First, the robust guess is essential for convergence. The zero guess fails to find a solution in 30% of the cases (S01, S03, S05). Second, the robust guess enables real-time performance. The zero guess never meets the $200$ ms real-time target, with its fastest solve time being around $689$ ms, whereas the robust guess consistently delivers solutions in under $160$ ms. Finally, the proposed strategy is both efficient and generalizable; the same guess once computed works on all $10$ diverse segments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-C Optimization Solvers", "weight": 1.0} -->

Since SNOPT consistently produced sub-optimal solutions (Table I) in the integrator test study, we limit our discussion to the parameters that are imperative to stabilize and produce better performance for the IP Methods.\• Barrier Parameter Influence: The barrier parameter update strategy is a critical hyperparameter in IP methods, directly impacting convergence and solution quality. Our tests show both IP solvers are highly sensitive to this choice, with a poor selection leading to suboptimal or failed solutions (Table III). For IPOPT, we found its default monotone strategy frequently failed to converge across different tests, in contrast to the adaptive strategy, which was found to be more robust. A similar effect was observed for KNITRO, where the advanced dampmpc strategy---a safeguarded predictor-corrector rule---solved the problem in just $22$ iterations, while a basic monotone approach failed (Table III). Further details on various barrier strategies can be found in (excluded here for brevity).

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-D Emergency Collision Avoidance Test", "weight": 1.0} -->

We put our architecture to test on two high-speed ($90$ km/h) emergency collision avoidance scenarios similar to those. Figure 6 highlights the framework's versatility, showing it can autonomously generate either a stable, low-sideslip maneuver ($<58$ ms) for a forgiving scenario or a controlled drift ($>0.4$ rad sideslip, $<72$ ms) for a more critical one. We empirically prove this aggressive drift is the only viable solution, as reinstating the tire saturation constraints renders the problem infeasible. Despite the complexity, both trajectories were generated in under $72$ ms, confirming real-time performance. This showcases our framework's ability to act as a unified planner that obviates the need for specialized drift controllers while providing a real-time certificate of feasibility.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-D Emergency Collision Avoidance Test", "weight": 1.0} -->

Further, we generated similar high-speed oval racing and collision avoidance trajectories for a test all-terrain vehicle (ATV) to validate real-world plausibility. A full-fidelity model of this vehicle is simulated by BeamNG, and the optimal trajectories are generated using a low-fidelity, data-driven model (similar to ) trained on BeamNG data. We track the reference trajectory using a short-horizon Model Predictive Control (MPC) running online.

<!-- chunk {"id": "body-0039", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

We demonstrate that real-time, reference-free trajectory generation at the limits of vehicle handling is achievable through a principled initial guess strategy, integrator selection informed by system stiffness analysis, and tailored interior point solver techniques for barrier updates and nonconvexity handling. The framework was validated across multiple race track segments for time-optimal planning, and in a high-speed collision avoidance scenario that requires drift for feasibility. Future work will implement the proposed architecture on real-world race cars. We will investigate how the current stiffness analysis and equilibrium-based initial guess generalizes to other system dynamics.
