## Introduction

Model Predictive Control (MPC) is an algorithmic approach that enables highly dynamic online control for robots subject to actuator and state constraints. However, while MPC has been deployed quite successfully in both academia and industry, its application is often hindered by computational limitations. This challenge is amplified when dealing with tiny, low-cost, low-power robots, as their onboard microcontroller units (MCUs) feature orders-of-magnitude less RAM, flash memory, and processor speed compared to the CPUs and GPUs available on larger robots. Consequently, many examples of intelligent behaviors executed on these tiny platforms rely on off-board compute. For deployment on such limited computational platforms, which also often lack full hardware support for floating-point arithmetic, an ideal MPC solver should be division-free, use only static memory allocation, and support warm starting to take advantage of computation at previous time steps. Compiled code should also have a low memory footprint and be easily verifiable through an interface to a high-level language (e.g., Python).

Moreover, while many embedded solvers today focus solely on quadratic programming (QP), second-order cone programs (SOCPs) represent a significantly richer class of tractable convex optimization problems, strictly generalizing linear and quadratic ones while remaining efficiently solvable due to their symmetric, self-dual structure. Many problems that appear nonconvex admit exact or lifted SOCP reformulations. Such problems also arise naturally in robotic and aerospace control problems involving friction, attitude, and thrust limits. As such, an ideal embedded MPC solver should natively support SOCPs while efficiently addressing their computational demands.

Figure 1: We demonstrate our solver using a 27 gram nano quadrotor, the Crazyflie. Top: we track a descending helical reference (red) with its position subject to a 45∘ second-order cone glideslope. This requires the aircraft to perform a spiral landing maneuver (blue). Bottom: we design a predictive safety filter to guarantee safe maneuvers within a box-shaped space (blue) regardless of the nominal controller behavior (red).

TABLE I: Comparison of general-purpose and model predictive control solvers.

Table I compares commonly used SOCP and QP solvers to illustrate how well they align with these design criteria. Several efficient optimization solvers and techniques suitable for embedded MPC have emerged in recent years, with notable software packages including OSQP, CVXGEN, ECOS, and SCS. However, because many of these are not purpose-built for MPC, they either do not easily support warm starting, don't take advantage of problem or sparsity structure, are not designed to easily enable embedded deployment, or some combination of these issues. In contrast, while TinyMPC is the first MPC solver tailored for dynamic tiny robot control on MCUs, it (as well as OSQP and CVXGEN) only supports QPs. TinyMPC also lacked a convenient high-level programming interface.

To address these shortcomings, in this work, we develop Conic-TinyMPC. Our contributions include: 1) support for conic constraints, focusing on SOCPs (Section III), a critical need for many real-world robotics applications; and 2) an open-source code generation software package with Python, MATLAB, and Julia interfaces to both ease the deployment of embedded MPC, as well as provide code generation and solution verification examples (Section IV).

We present microcontroller benchmarks (Section V-A) demonstrating up to a two-order-of-magnitude speedup and one-order of-magnitude reduction in memory usage over state-of-the-art embedded QP and SOCP solvers. We also validate our solver's deployed performance through hardware experiments on a 27g Crazyflie quadrotor (Section V-B), including trajectory tracking with conic constraints. Our open-source code is available at [https://tinympc.org](https://tinympc.org).

## Background

### II-A The Linear-Quadratic Regulator

The linear-quadratic regulator (LQR) problem is an optimal control problem in which a quadratic cost function is minimized subject to linear (or affine) dynamics constraints:

where $x_{k} \in {\mathbb{R}}^{n}$, $u_{k} \in {\mathbb{R}}^{m}$ are the state and control at time step $k$, $N$ is the number of time steps, $A_{k} \in {\mathbb{R}}^{n \times n}$, $B_{k} \in {\mathbb{R}}^{n \times m}$, and $c_{k} \in {\mathbb{R}}^{n}$ define the system dynamics, $Q_{k} \succeq 0$, $R_{k} \succ 0$, and $Q_{N} \succeq 0$ are symmetric cost-weighting matrices and $q_{k}$ and $r_{k}$ are linear cost vectors. Equation is a classical problem in the field of optimal control whose solution is an affine feedback controller:

Feedback and feedback terms ($K_{k}$, $d_{k}$) are found by solving the discrete-time Riccati equation backward in time, starting with $P_{N} = Q_{N}$ and $p_{N} = q_{N}$, where $P_{k}$ and $p_{k}$ are the quadratic and linear terms of the cost-to-go function:\

### II-B Convex Model-Predictive Control

Convex MPC extends this to admit additional convex constraints on the states and controls (as shown in blue):

where $\mathcal{X}$ and $\mathcal{U}$ are convex sets. The convexity of this problem means that it can be solved efficiently and reliably, enabling real-time deployment in a variety of control applications, including autonomous rocket landings, legged locomotion, and autonomous driving.

When $\mathcal{X}$ and $\mathcal{U}$ can be expressed as linear constraints, is a QP. When $\mathcal{X}$ and $\mathcal{U}$ can be expressed as both linear and second-order cone constraints, is an SOCP, and can be put into the standard form (where $\mathcal{K}$ is a cone):

The addition of the final constraints in blue separate the SOCP from the QP. Further analysis, including feasibility and stability guarantees can be found in.

### II-C Alternating Direction Method of Multipliers (ADMM)

We provide a very brief summary of ADMM here and refer readers to for more details. Given a generic optimization problem (with $f$ and $\mathcal{C}$ convex):

we can form the equivalent problem, introducing slack $z$, and indicator function $I_{\mathcal{C}}$:

The augmented Lagrangian of the transformed problem (7 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")) is (with Lagrange multiplier $\lambda$ and scalar penalty weight $\rho$):

If we perform alternating minimization of (8 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")) with respect to $x$ and $z$, we arrive at the three-step ADMM iteration,

where the last step is a gradient-ascent update on the Lagrange multiplier. These steps can be iterated until a desired convergence tolerance is achieved.

In the special cases of QPs and SOCPs, each step of the ADMM algorithm becomes very simple to compute: the primal update is the solution to a linear system, the slack update is a linear or conic projection, and the dual update is simply scaled vector addition. As such, the computational complexity of the three steps for QPs and SOCPs is:

$\mathcal{O}{(n^{3})}$ for the primal update (9 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")),

$\mathcal{O}{(n^{2})}$ for the slack update (10 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")),

and $\mathcal{O}{(n)}$ for the dual update (11 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")).

Due to this simplicity, ADMM-based QP and SOCP solvers have demonstrated state-of-the-art results.

### II-D TinyMPC

TinyMPC, exploits properties of the MPC problem through pre-computation and caching with an ADMM framework to efficiently solve this problem via three assumptions:

The dynamical system can be modeled as linear time invariant, with fixed ${A,B,{c{\forall k}}} \in {\lbrack 0,N)}$;

The quadratic cost can be modeled with fixed hessians, ${Q,{R{\forall k}}} \in {\lbrack 0,N)}$, $Q_{N}$; and

The finite horizon LQR feedback gain and cost-to-go Hessian, $K_{k},P_{k}$, can be effectively approximated by the solution to the infinite-horizon LQR solution, ${K_{\text{inf}},{P_{\text{inf}}{\forall k}}} \in {\lbrack 0,N\rbrack}$.

We provide a brief summary of the approach and refer to for more details. TinyMPC splits the standard LQR problem from all additional state and input constraints via ADMM. The primal update, (9 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")), becomes:

where we use scaled dual variables $y$ and $g$ and for convenience and the following are defined:

This enables a slight simplification to (11 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")), where we substitute the dual variables with their scaled forms and eliminate $\rho$. As a result, the scaled dual variables $y_{k}$ and $g_{k}$ are always equal to the difference between the primal and slack variables, which is a convergence criteria that now does not need to be recalculated during convergence checks.

As has the same form as, it can be solved efficiently through a backwards Riccati recursion followed by an affine dynamics roll-out of the resulting policy,. The slack update remains a projection onto the feasible set:

where the superscript denotes the variable at the subsequent ADMM iteration, and the dual update becomes:

Given a long enough horizon, the Riccati recursion converges to the solution of the infinite-horizon LQR problem. exploits this property and assumes that the single infinite horizon gain, $K_{\text{inf}}$, and cost-to-go Hessian, $P_{\text{inf}}$, sufficiently approximate the time-varying values, $K_{k},P_{k}$. Combining this approximation with our assumption of fixed $A,B,c,Q,Q_{N},R$ matrices enables us to drastically simplify the Riccati recursion not only easing its computational complexity, but also greatly reducing its memory footprint as we only need to cache $A,B,c,Q,Q_{N},R,K_{\text{inf}},P_{\text{inf}}$, along with a handful of other precomputed and cached constants:

Using these terms, the LQR backward pass simplifies to:

which only requires matrix-vector products to compute, reducing computational complexity of the primal update from $\mathcal{O}{(n^{3})}$ to $\mathcal{O}{(n^{2})}$, drastically reducing online computation time, and avoiding online division entirely. We note that $C_{3}$ and $C_{4}$ are derived in addition to $C_{1}$ and $C_{2}$ from to support dynamics with the additional constant term $c$.

Finally, we note that ADMM solvers like OSQP adaptively scale the penalty term $\rho$ in (8 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")) for performance. However, this requires performing additional matrix factorizations. To avoid this, pre-compute and cache sets of matrices corresponding to several values of $\rho$, which we refer to as the set $\lbrack\varrho\rbrack$. Online, the solver switches between these values of $\rho$, and their respective cached matrices, based on the values of the primal and dual residuals using heuristics adapted from OSQP.^11^1We also note that recent work proposes additional schemes to adapt $\rho$ with finer-grained updates. We will integrate this advance into our open-source conic framework in future work.

## The Conic-TinyMPC Solver

As noted in, the slack update in (10 ‣ II Background ‣ Code Generation and Conic Constraints for Model-Predictive Control on Microcontrollers with Conic-TinyMPC")) can be expressed as the operator $\Pi$, which projects the slack variable onto its feasible set. More generally, this projection step can be defined for any convex set. Because the ADMM algorithm naturally isolates the projection subproblem, any convex set with a computationally efficient projection operator can be seamlessly incorporated into our framework. Conveniently, many standard convex cones admit simple closed-form projection operators. We demonstrate this by example in the remainder of this section.

We first note that projection onto a linear inequality constraint, or equivalently, projection of a point $z$ to a hyperplane $\mathcal{H} = {\{ x:{{\langle x,a\rangle} = b}\}}$, can be written as follows:

For constant bounds on variables, such as the case of position, velocity, or control limits, $(l,u)$, this can be reduced to a projection onto a set of upper and lower bounds:

This projection approach extends to conic problems in the same manner. We can, for example, define the second-order cone ("ice-cream cone") as follows:

The second-order cone also admits a closed-form and compact projection operator:

where $v = {\lbrack z_{1},\ldots,z_{n - 1}\rbrack}^{\intercal}$ and $a = z_{n}$. Here, ${{z_{i},i} = 1},{\ldots,n}$ is any vector subset of the state or control slack variables. In principle, other cones can also be implemented, e.g. the cone of $n \times n$ positive semi-definite matrices ("semi-definite cone"). Algorithm 1 summarizes the overall algorithm.

## Code Generation

To enable the community to more easily leverage Conic-TinyMPC, we have developed a code-generation tool with Python, MATLAB, and Julia interfaces that produces dependency-free C++ code for easy deployment. We hope that through such interfaces, and our additional examples, available alongside our open-source code, the community can quickly prototype and deploy our solver onto their tiny robot systems.

function offline precompute(input)
for ρ ∈ [𝜚] form cache via, Ki n f, Pi n f,
function online solve(input)
Select ρ ∈ [𝜚] and associated cached terms
while not converged do
p1: N − 1, d1: N − 1 ← Backward pass via ()
x1: N, u1: N − 1 ← Forward pass via ()
//Slack and Dual Updates
q1: N, r1: N − 1, pN ← Update linear cost terms return x1: N, u1: N − 1

## Create the solver object
solver = tinympc.TinyMPC()
## Initialize the solver
solver.setup(N, A, B, c, Q, R, bnds, socs, options)
## Generate code
solver.codegen(output_dir)
Listing 1: A minimal Python script to generate MPC problem code.

## Set initial state
tinympcgen.set_x0(np.array([0.5, 0, 0, 0]))
## Solve the problem
solution = tinympcgen.solve()
## Get the solution
controls = solution["controls"]
Listing 2: An example Python script to run the generated code.

#include "tinympc.hpp"
#include "tiny_data_workspace.hpp"
int main(int argc, char **argv) {
tiny_solve(&amp;solver); // Solve the problem
Listing 3: A simple C++ program that loads the problem data from tiny_data_workspace.hpp and solves the problem.

// Update initial/feedback state
tiny_set_x0(&amp;solver, x0_new);
// Update trajectory reference
tiny_set_x_ref(&amp;solver, xref_new);
tiny_set_bound_constraints(&amp;solver, xmin_new, xmax_new, umin_new, umax_new);
Listing 4: Directly updating parameters of the MPC problem in C++.

tiny data workspace.cpp
tiny main.cpp
Figure 2: The tree structure of the generated code. The main program is stored in tiny main.cpp.

In the remainder of this section, we describe our code-generation interfaces through examples and code listings using our Python interface and note that the process is nearly identical in MATLAB and Julia.

Listing 1 shows how to generate problem-specific code. The setup function initializes the problem with specific data, namely: time horizon ($N$), system model ($A$, $B$, and $c$), cost weights ($Q$ and $R$), linear and conic constraint parameters (bnds and socs), and solver options. For example, users may set primal and dual tolerances, or the maximum number of ADMM iterations. This kind of parameter tuning is often critical for returning a usable solution within real-time limits for particular systems of interest. The codegen function is then used to generate the custom-tailored code.

Users may choose to compile code for their host system either manually or through our interface for ease of testing when cumbersome to build in C++. Listing 2 shows an example script that loads the generated code library, solves the problem, then retrieves the solution. The reference trajectory and initial state may be set using set_x_ref, set_u_ref, and set_x0, and may be done on the microcontroller using the C++ equivalents. Additional wrapped functions exist for overwriting constraint parameters.

The directory structure of the resulting generated C++ code is shown in Fig. 2. The solver's source code and associated headers are in the tinympc subdirectory. The generated code is compact and does not rely on dynamic memory allocation, making it particularly suitable for embedded use cases. An example program is located in tiny_main.cpp. This program imports workspace data from the tiny_data_workspace.hpp header and then solves the given problem (Listing 3).

We also offer functions to update the initial state, reference trajectories, and constraints on the states and inputs using wrapper functions, which are essential in MPC settings (see Listing 4 for a number of examples).

We note that the Python interface not only allows users to generate C++ code that may be run on a microcontroller, but it also allows the user to run TinyMPC functions directly in Python. This enables users to investigate the solver in a desktop environment before switching to a microcontroller. In future work, we also hope to build on these Python interfaces to enable us to build a complete MicroPython library, for even easier use on microcontrollers. Finally, we remind the reader that similar features, functions, and interfaces exist through our MATLAB and Julia interfaces.

## Experiments

We benchmark the performance of the generated code from Conic-TinyMPC through a sets of microcontroller benchmarks and control tasks running onboard a 27 gram Crazyflie quadrotor to demonstrate TinyMPC's effectiveness in real-world deployed conditions. All experiments are available with our open-source code for reproducibility.

### V-A Microcontroller Benchmarks

### V-A1 Predictive Safety Filtering

We first formulate a QP with box constraints on states and controls to act as a predictive safety filter for a nominal task policy as in. We compare the solution times and memory usage of Conic-TinyMPC against the state-of-the-art OSQP QP solver, utilizing both solvers' Python code generation interfaces, while varying the state and horizon dimensions. We benchmark on a STM32F405 Adafruit Feather board, which has an ARM Cortex-M4 operating at 168 MHz with 1 MB of flash memory and 128 kB of RAM, very similar to computational hardware on the Crazyflie 2.1 used for our later hardware experiments in Section V-B.

(a) Predictive Safety Filtering

(b) Rocket Soft Landing

Figure 3: (a) Predictive safety filtering performance comparison between Conic-TinyMPC and OSQP on an STM32F405 Feather board. Top row shows average iteration times, bottom row shows memory usage. Left column: time horizon kept constant at N = 10 while state dimension n ranged from 2 to 32 and input dimension was set to half of the state dimension. Right column: state and control input held constant at n = 10 and m = 5 while N ranged from 4 to 100. Error bars represent maximum and minimum time taken per iteration for all MPC steps. Black dotted lines denote memory thresholds. (b) Rocket soft-landing performance comparison between Conic-TinyMPC, ECOS, and SCS using a Teensy 4.1 development board. Top plot shows memory usage, bottom plot shows average iteration times. In this SOCP-based experiment n = 6 and m = 3 while N varied from 2 to 256. Error bars represent maximum and minimum time taken per iteration for all MPC steps performed. Black dotted lines denote memory thresholds.

Fig. 3(a) shows the total program size and the average execution times per iteration. Conic-TinyMPC uses drastically less memory and exhibits significant speed-ups over OSQP. For varying states, Conic-TinyMPC achieves up to 20.4× faster execution, while for varying time horizons, it achieves up to 7.2× faster execution. Moreover, the reduction in memory usage allows Conic-TinyMPC to solve real-time optimal control of complex systems with long time horizons. In particular, Conic-TinyMPC was able to handle time horizons of up to 100 knot points, whereas OSQP surpassed the 128 kB memory capacity of the at a time horizon of only $N = 32$. Additionally, Conic-TinyMPC demonstrated scalability to larger state dimensions up to $n = 32$, whereas OSQP encountered memory limitations beyond $n = 28$.

### V-A2 Rocket Soft-Landing

The second benchmark is a rocket soft-landing problem which requires a rocket to land with small final velocity at a desired position, resulting in a conic glide-scope constraint. We benchmark the performance of Conic-TinyMPC again via it's Python code generation against ECOS and SCS, state-of-the-art SOCP solvers, using CVXPYgen's code generation interface. All solver options were set to equivalent values wherever possible and all tolerances were set to $0.01$.

Here we benchmark on a Teensy 4.1 development board, which has an ARM Cortex-M7 microcontroller operating at 600 MHz, with 7.75 MB of flash memory, 512 kB of tightly coupled static RAM, and an additional 512 kB of tightly coupled dynamic RAM. The increased compute and memory capacity of the Teensy was particularly important to enable us to benchmark against ECOS and SCS, and enabled us to collect more overall data as the largest SOCP problem involved 2301 decision variables as well as 1530 linear equality constraints, 1530 linear inequality constraints, and 255 second-order cone constraints. However, we note that Conic-TinyMPC, even for this larger problem, could still fit on the more constrained Adafruit Feather used in the prior benchmark, as well as on the constrained MCU found on the Crazyflie 2.1, which we demonstrate via our hardware experiments in Section V-B.

Fig. 3(b) shows the amount of statically and dynamically allocated memory and the average execution times per iteration for varying time horizon. Conic-TinyMPC outperforms SCS and ECOS in execution time and memory, achieving an average speed-up of 13.8x over SCS and 142.7x over ECOS. Conic-TinyMPC performed no dynamic allocation while SCS and ECOS dynamically allocated the workspace at the beginning due to the use of the CVXPYgen interface, causing them to exceed the total available RAM during execution. Without using the CVXPYgen interface, the dynamically allocated workspace must instead be stored statically, far exceeding the static memory limit. This severely limited SCS and ECOS, with both solvers exceeding total memory limits at $N = 64$, while Conic-TinyMPC can scale to $N = 256$.

### V-A3 Early Termination

High-rate real-time control requires a solver to return a solution within a strict time window. Table II shows the trajectory-tracking performance of each solver on the rocket soft-landing problem with four different control step durations, resulting in four different time budgets. We solve the same problem as in V-A2, except that each solver must return within the specified time budget. The maximum number of iterations for each solver was determined based on the average time per iteration for each solver with $N = 16$ (Fig. 3(b)). For example, when given 20ms to solve the problem, the maximum number of solver iterations for ECOS, SCS, and Conic-TinyMPC were 3, 33, and 444, respectively. This represents a factor of 11x to 148x more solver iterations for Conic-TinyMPC. Table II reports two different metrics: A) the total control input violation on box and SOC constraints and B) the landing error (defined as the norm of the deviation between the final and goal states).

ECOS successfully solved to convergence only when given 1000ms, impractical for most real-time control tasks. It failed in subsequent cases due to its limited speed and inability to warm start, with zero iterations completed within 2ms. On the other hand, even though SCS and Conic-TinyMPC were both unable to solve the problem to full convergence at every iteration for shorter time budgets, Conic-TinyMPC was able to utilize its increased number of iterations and warm starting to maintain low constraint violation and landing error. This resulted in Conic-TinyMPC outperforming SCS for all scenarios with a 1.6x to 2.4x reduction in landing error and, most critically, while SCS violated constraints across all time budgets, Conic-TinyMPC only appreciably did so for the shortest 2ms time budget.

TABLE II: Solver performance comparison with different solution-time budgets. Within 20ms (N = 16), the maximum number of solver iterations for ECOS, SCS, and TinyMPC are 3, 33, and 444, respectively. ECOS was not able to complete a single optimization iteration within 2ms.

### V-B Robot Hardware Experiments

Next, we demonstrate the efficacy of our solver for real-time execution of dynamic control tasks on a Crazyflie 2.1, a 27 gram quadrotor with an ARM Cortex-M4 (STM32F405) clocked at 168 MHz with 192 kB of SRAM and 1 MB of flash. We present three experiments detailing the high performance of Conic-TinyMPC for dynamic control tasks requiring the online solution to QPs and SOCPs: 1) predictive safety filtering to enable safe control of fundamentally unsafe policies, 2) attitude/thrust vector regulation with thrust-cone constraints, and 3) tracking a spiral landing trajectory with conic constraints and a constraint-violating helical reference.

We note that for the problem sizes required for these experiments, OSQP, SCS, and ECOS all could not fit within the memory available on this MCU and, as such, cannot be used as baselines. Instead, we compare against the Brescianini and Mellinger reactive controllers included with the Crazyflie firmware. These controllers often clip the control input to meet hardware constraints. For all experiments, we ran all controllers with their default parameters and attached an optical flow deck to the Crazyflie to perform state estimation fully onboard the robot.

In all experiments, we linearized the quadrotor's 6-DOF dynamics about a hover, representing the quadrotor as a point mass with a thrust vector input, and representing its attitude with a quaternion using the formulation in. This problem has state dimension $n = 12$ and $m = 4$, representing the quadrotor's full state and PWM motor commands. It is worth noting that the Crazyflie platform offers a great chance to test the controller's robustness due to its high model uncertainty and rapidly depleting battery power (only 5-15 minutes of flight). Under the restricted budget, our Conic-TinyMPC ran at 50 Hz with at most 20 ADMM iterations per call, using a fast reactive controller to track the predicted next state.

### V-B1 Predictive Safety Filtering

We use a nominal PD controller and formulate a predictive safety filtering problem as a QP, similar to V-A. The Crazyflie was commanded to follow a sinusoidal path along a single axis with an amplitude of 1.2 m (Fig. 1 bottom), which was then tracked with both a nominal PD controller (red) and by Conic-TinyMPC (blue) using a horizon of 20 knot points and box constraints at $\pm$`<!-- -->`{=html}0.6 m. The box constraints represent safety limits on the quadrotor's operating space. Conic-TinyMPC is able to successfully respect the safety limits, handling them by slowing to a stop and hovering at the boundaries of the constraints until the reference trajectory comes back around and sends the Crazyflie to the other side of the boundary. This experiment demonstrates Conic-TinyMPC's ability to act as a safety layer for unsafe policies.

Figure 4: Attitude/thrust vector regulating performance of different controllers on the Crazyflie. While Conic-TinyMPC was able to constrain the aircraft attitude within the bounds (dashed lines for 0.25 and 0.2 radians), Brescianini and Mellinger exhibited large attitude deviations, causing failures.

### V-B2 Attitude and Thrust-Vector Regulation

In many controllers for vertical take-off and landing (VTOL) aircraft, the thrust vector is constrained to lie within a cone. We formulated an SOCP-based MPC problem for the Crazyflie that incorporates such a constraint, implicitly constraining the drone's attitude. We used the Brescianini, Mellinger, and Conic-TinyMPC controllers to track an aggressive maneuver (drawing a circle in the air very quickly) to determine if the cone constraint was limiting the Crazyflie's attitude. As depicted in Fig. 4, Conic-TinyMPC was able to successfully limit the Crazyflie's attitude to two different maximum values (0.2 and 0.25 radians). Conversely, the baselines exhibited significant attitude deviations, resulting in failures. It is important to note that one can only reduce the attitude deviations of these myopic baselines through careful gain tuning, without any guarantees, while Conic-TinyMPC allows them to be specified explicitly as constraints.^22^2We note that thrust-cone constraints are particularly valuable for Conic-TinyMPC on quadrotors, as the solver relies on linearized dynamics with small-angle approximations, which are only valid within a fixed region of the state space. As such, enforcing a thrust-cone constraint helps ensure that the system remains within this valid operating region, which is essential for maintaining stability during control tasks.

### V-B3 Conically Constrained Spiral Landing

Planetary landing problems typically include a glideslope constraint to ensure sufficient elevation during approach and to prevent the spacecraft from crashing into terrain. Fig. 1 top demonstrates the ability of Conic-TinyMPC to handle the planetary landing glideslope constraint of a spacecraft. The reference trajectory is a descending cylindrical spiral (red) which we tracked with Conic-TinyMPC and no position constraints. We then added a conic constraint to restrict the Crazyflie's position to within a 45^∘^ cone originating from the center of the cylindrical reference trajectory. Conic-TinyMPC restricts the Crazyflie from leaving the cone defined by the glideslope constraint, resulting in a spiral landing maneuver (blue).

## Conclusions and Future Work

In this paper, we develop Conic-TinyMPC, an open-source, high-speed, structure-exploiting, alternating direction method of multipliers (ADMM) solver targeting low-power embedded conic control applications. We also present a code-generation framework with high level Python, MATLAB, and Julia interfaces that makes it easy to use our solver. We demonstrate the performance of Conic-TinyMPC through a series of experiments including a number of microcontroller benchmarks, and hardware deployments using a 27 gram Crazyflie quadrotor.

There are several directions for future work. One of particular note is that our approach, like that of, relies on fixed (set of) linearizations, which may not capture all robotic systems well. To address this, we plan to explore recent work that models the nonlinear-to-linear gap as an antagonistic disturbance using reachability analysis, enabling us to more safely support nonlinear systems.
