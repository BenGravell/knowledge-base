<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Tube MPC for Nonlinear Systems

Topics include Model predictive control, Predictive control, Robustness, Uncertainty, Computational complexity, Online algorithms, Offline algorithms, Optimization, Control, DTMPC, Robust model predictive control, RMPC, Nonlinear systems, Obstacle avoidance.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modeling error or external disturbances can severely degrade the performance of Model Predictive Control (MPC) in real-world scenarios. Robust MPC (RMPC) addresses this limitation by optimizing over feedback policies but at the expense of increased computational complexity. Tube MPC is an approximate solution strategy in which a robust controller, designed offline, keeps the system in an invariant tube around a desired nominal trajectory, generated online. Naturally, this decomposition is suboptimal, especially for systems with changing objectives or operating conditions. In addition, many tube MPC approaches are unable to capture state-dependent uncertainty due to the complexity of calculating invariant tubes, resulting in overly-conservative approximations. This work presents the Dynamic Tube MPC (DTMPC) framework for nonlinear systems where both the tube geometry and open-loop trajectory are optimized simultaneously. By using boundary layer sliding control, the tube geometry can be expressed as a simple relation between control parameters and uncertainty bound; enabling the tube geometry dynamics to be added to the nominal MPC optimization with minimal increase in computational complexity. In addition, DTMPC is able to leverage state-dependent uncertainty to reduce conservativeness and improve optimization feasibility.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

DTMPC is demonstrated to robustly perform obstacle avoidance and modify the tube geometry in response to obstacle proximity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Model predictive control (MPC) has become a core control strategy because of its natural ability to handle constraints and balance competing objectives. Heavy reliance on a model though makes MPC susceptible to modeling error and external disturbances, often leading to poor performance or instability. Robust MPC (RMPC) addresses this limitation (at the expense of additional computational complexity) by optimizing over control policies instead of open-loop control actions. Tube MPC is a tractable alternative that decomposes RMPC into an offline robust controller design and online open-loop MPC problem. However, this decoupled design strategy restricts the tube geometry (i.e., feedback controller) to be fixed for all operating conditions, which can lead to suboptimal performance. This article presents a framework for nonlinear systems where the tube geometry and open-loop reference trajectory are designed simultaneously online, giving the optimization an additional degree of freedom to satisfy constraints or changing objectives.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Tube MPC for nonlinear systems has been an active area of research. For example, hierarchical MPC, reachability theory, sliding mode control, sum-of-square optimization, and Control Contraction Metrics have all been recently used in nonlinear tube MPC. These approaches try to maximize robustness by minimizing tube size given control constraints and bounds on uncertainty. However, minimizing tube size typically results in a high-bandwidth controller that responds aggressively to measurement noise or external disturbances. For mobile systems that use onboard sensing for estimation or perception, this type of response can severely degrade performance or cause a catastrophic failure. Further, the performance reduction often depends on the current operating environment so modifying the tube geometry online would be advantageous. While there is a precedent for optimizing tube geometry in linear MPC, the relationship between tube geometry and control parameters for nonlinear systems is often too complex to put in a form suitable for real-time optimization. The approach described herein circumvents this issue by providing a simple and exact description of how the tube geometry, control parameters, and uncertainty are related, enabling the tube geometry to be optimized in real-time.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The primary contribution of this work is a tube MPC framework for nonlinear systems that simultaneously optimizes tube geometry and open-loop reference trajectories in the presence of uncertainty. The proposed framework leverages the simplicity and strong robustness properties of time-varying boundary layer sliding control to establish a connection between tube geometry, control parameters, and uncertainty. Specifically, the tube geometry can be described by a simple first-order differential equation that is a function of control bandwidth and uncertainty bound. This allows the development of a framework with several desirable properties. First, the tube geometry can be easily optimized, with minimal increase in computational complexity, by treating the control bandwidth as a decision variable and augmenting the state vector with the tube geometry dynamics. Second, the uncertainty bound in the tube dynamics can be made state-dependent, allowing the optimizer to make smarter decisions about which states to avoid given the system's current state and proximity to constraints. And third, less conservative tubes can be constructed by combining the tube and tracking error dynamics. Simulation results demonstrate DTMPC's ability to optimize the tube geometry, via modulating control bandwidth and/or utilize knowledge of state-dependent uncertainty, to robustly avoid obstacles.

<!-- chunk {"id": "body-0007", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

A number of works have been published on the stability, feasibility, and performance of linear tube MPC. While this is an effective strategy to achieve robustness, decoupling the nominal MPC problem and controller design is suboptimal. Rakovic̀ et al. showed that the region of attraction can be enlarged by parameterizing the problem with the open-loop trajectory and tube size. The authors presented the homothetic tube MPC (HTMPC) algorithm that treated the state and control tubes as homothetic copies of a fixed cross-section shape, enabling the problem to be parameterized by the tube's centers (i.e., open-loop trajectory) and a cross-section scaling factor. The work was extended to tubes with varying shapes, known as elastic tube MPC (ETMPC), but at the expense of computational complexity. Both HTMPC and ETMPC possess strong theoretical properties and have the potential to significantly improve performance but a nonlinear extension has yet to be developed.

<!-- chunk {"id": "body-0008", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Recent theoretical and computational advances in nonlinear control design and invariant set computation has aided in the development of new nonlinear tube MPC techniques. Mayne et al. proposed a two-tier MPC architecture where the nominal MPC problem, with tightened constraints, is solved followed by an ancillary problem that drives the current state to the nominal trajectory. Linear reachability theory is another strategy but tends to be overly conservative because nonlinearities are treated as disturbances. Because of its strong robustness properties, a number of works have proposed using sliding mode control as an ancillary controller. The work by Muske et al. is of particular interest because the parameters of the sliding surface were optimized within the MPC optimization to achieve minimum time state convergence. Majumdar et al. constructed ancillary controllers for nonlinear systems via sum-of-squares (SOS) optimization that minimized funnel size (akin to a tube). The method, however, required a pre-specified trajectory library and an extremely time consuming offline computation phase. Singh et al. proposed using Control Contraction Metrics to construct tubes and showed their approach increases the region of feasibility for the optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

All of the aforementioned works fall into the category of rigid tube MPC (i.e., fixed tube size) so are inherently suboptimal. Further, these approaches tend to produce overly conservative tubes because they cannot leverage knowledge of state-dependent uncertainty.

<!-- chunk {"id": "body-0010", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

This work uses boundary layer sliding control to address the suboptimality and conservatism of the aforementioned techniques for nonlinear systems. This is accomplished: 1) incorporating the tube geometry into the optimization, subsequently bridging the gap between linear and nonlinear homothetic/elastic tube MPC; 2) leveraging knowledge of state-dependent uncertainty; and 3) combining the tube and error dynamics to reduce the spread of possible trajectories.

<!-- chunk {"id": "body-0011", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

Consider a nonlinear, time-invariant, and control affine system given by (omitting the time argument)

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Note that the model error bound in assumption 1 is state-dependent, which can be leveraged to construct less conservative tubes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The standard RMPC formulation involves a minimax optimization to construct a feedback policy $\pi:{{{\mathbb{X}} \times {\mathbb{R}}}\rightarrow{\mathbb{U}}}$ where $x \in {\mathbb{X}}$ and $u \in {\mathbb{U}}$ are the allowable states and control inputs, respectively. However, optimizing over arbitrary functions is not tractable and discretization suffers from the curse of dimensionality. The standard approach taken in tube MPC is to change the decision variable from control policy $\pi$ to open-loop control input $u^{\ast}$. In order to achieve this re-parameterization, the following assumption is made about the structure of the control policy $\pi$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The control policy $\pi$ takes the form\
$\pi = {u^{\ast} + {\kappa{(x,x^{\ast})}}}$ where $u^{\ast}$ and $x^{\ast}$ are the open-loop input and reference trajectory, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

In the tube MPC literature $\kappa$ is known as the ancillary controller and is typically designed offline. The role of the ancillary controller is to ensure the state $x$ remains in a robust control invariant (RCI) tube around the nominal trajectory $x^{\ast}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

This section reviews time-varying boundary layer sliding control, provides analysis supporting its use as an ancillary controller, and shows how the DTMPC framework leverages its properties. As reviewed in Section II, sliding mode control has been extensively used for nonlinear tube MPC because of its simplicity and strong robustness properties. Unlike other control strategies, sliding mode control completely cancels any bounded modeling error or external disturbance (reducing the RCI tube to zero). However, complete cancellation comes at the cost of high-frequency discontinuous control making it impractical for many real systems; a number of version that ensure continuity in the control signal have since been developed. Note that the boundary layer controller was originally developed in and is only presented here for completeness. Before proceeding the following assumption is made.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The system given by Equation 1 has the same number of outputs to be controlled as inputs. More precisely, the dynamic can be expressed as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Note that assumption 4 requires system Equation 1 to be either feedback linearizable or minimum phase. While many systems fall into one of these categories, future work will extend DTMPC to more general nonlinear systems.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

In sliding mode control, a sliding manifold $\mathcal{S}_{i}$ is defined such that $s_{i} = 0$ for all time once the manifold is reached. This condition guarantees the tracking error goes to zero exponentially via Equation 3. It can be shown that a discontinuous controller is required to ensure the manifold $\mathcal{S}_{i}$ is reached in finite time and is invariant to uncertainty. However, high-frequency discontinuous control can, among other things, excite unmodeled high-frequency dynamics and shorten actuator life span.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

One strategy to smooth the control input is to introduce a boundary layer around the switching surface. Specifically, let the boundary layer be defined as $\mathcal{B}_{i}:={\{ x:{{|s_{i}|} \leq \Phi_{i}}\}}$ where $\Phi_{i}$ is the boundary layer thickness. If $\Phi_{i}$ is time varying, then the boundary layer can be made attractive if the following differential equation is satisfied

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

where $\eta_{i}$ dictates the convergence rate to the sliding surface. Differentiating Equation 3,

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

Stacking Equation 6 for each output, the vector version is obtained

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

Note that $F$ and $B$ are stacked versions of the dynamics and input matrix, respectively, that correspond to the output variables. If the output variables are chosen to be the full state vector (i.e., state feedback linearization), then $F$ and $B$ simply become the dynamics and input matrix in Equation 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

Let the controller take the form

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

where sat$( \cdot )$ is the saturation function and the division is element-wise. Then, for ${|s|} > \Phi$, the boundary layer is attractive if

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

Addition information can be inferred by considering the sliding variable dynamics inside the boundary. Again substituting Equation 8 into Equation 7 with ${|s|} \leq \Phi$,

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

where again the division is element-wise. Alternatively, Equation 10 can be written as

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

which is a first order filter with cutoff frequency $\frac{K{(x^{\ast})}}{\Phi}$. Let $\alpha$ be the desired cutoff frequency, then, leveraging Equation 9, one obtains

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Sliding Control", "weight": 1.0} -->

Thus, the final control law is given by Equation 8, Equation 9, and Equation 13.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Discussion", "weight": 1.0} -->

The boundary layer sliding controller in Equation 8 allows us to establish several key properties at the core of DTMPC.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Overview", "weight": 1.0} -->

This section presents the DTMPC algorithm and discusses its properties. DTMPC is a unique algorithm because of its ability to change the tube geometry to meet changing objectives and to leverage state-dependent uncertainty to maximize performance. This section first presents a constraint tightening procedure necessary to prevent constraint violation due to uncertainty. Next, optimizing the tube geometry by adding the control bandwidth as a decision variable is discussed. Lastly, the non-convex formulation of DTMPC is presented. Before proceeding, the following assumption is made about the form of the state and actuator constraints.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

The state and actuator constraints take the form

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

where $\parallel \cdot \parallel$ is the 2-norm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

Many physical systems posses these type of constrains so the above assumption is not overly restrictive.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Constraint Tightening", "weight": 1.0} -->

State and actuator constraints must be modified to account for the nonzero tracking error and control input caused by model error and disturbances. The following corollary establishes the modified state constraint.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C Optimized Tube Geometry", "weight": 1.0} -->

For many autonomous systems, the ability to react to changing operating conditions is crucial for maximizing performance. For instance, a UAV performing obstacle avoidance should modify the aggressiveness of the controller based on the current obstacle density to minimize expended energy. Formally, the tube geometry must be added as a decision variable in the optimization to achieve this behavior. DTMPC is able to optimize the tube geometry because of the simple relationship between the tube geometry, control bandwidth, and level of uncertainty given by Equation 13. This is one of the distinguishing features of DTMPC since other state-of-the-art nonlinear tube MPC algorithms are not able to establish an explicit relationship like Equation 13.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-C Optimized Tube Geometry", "weight": 1.0} -->

In Section IV, it was shown that the control bandwidth $\alpha$ is responsible for how the uncertainty affects the sliding variable $s$. Subsequently, the choice of $\alpha$ influences the tube geometry (via Equation 13) and control gain (via Equation 9). In order to maintain continuity in the control signal, the tube geometry dynamics are augmented such that $\alpha$ and $\Phi$ remain smooth. More precisely, the augmented tube dynamics are

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C Optimized Tube Geometry", "weight": 1.0} -->

where $v \in {\mathbb{V}}$ is an artificial input that will serve as an additional decision variable in the optimization. It is easy to show that the above set of differential equations is stable so long as $\alpha$ remains positive.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-D Complete Formulation", "weight": 1.0} -->

With Corollary 1. ‣ V-B Constraint Tightening ‣ V DYNAMIC TUBE MPC ‣ Dynamic Tube MPC for Nonlinear Systems") and 2. ‣ V-B Constraint Tightening ‣ V DYNAMIC TUBE MPC ‣ Dynamic Tube MPC for Nonlinear Systems") establishing the tightened state and actuator constraints, the Dynamic Tube MPC optimization can now be formulated as

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem 1", "weight": 1.0} -->

where $\check{\cdot}$ denotes the internal variables in the optimization; $\Omega$ is the tube geometry with matrices $A_{c}$ and $B_{c}$ given by putting Equation 3 into controllable canonical form; $\overline{\mathbb{X}}$ and $\overline{\mathbb{U}}$ are the tightened state and actuator constraints; and $\ell$ and $h$ are the quadratic state and terminal cost. The output of DTMPC is an optimal open-loop (i.e., feedforward) control input $u^{\ast}$, trajectory $x^{\ast}$, and control bandwidth $\alpha^{\ast}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Problem 1", "weight": 1.0} -->

DTMPC is inherently a non-convex optimization problem because of the nonlinear dynamics. However, non-convexity is a fundamental characteristic of nonlinear tube MPC and a number of approximate solution procedures have been proposed. The key takeaway, though, is that Problem 1 is a nonlinear tube MPC algorithm that simultaneously optimizes the open-loop trajectory and tube geometry, eliminating the duality gap in standard tube MPC. Furthermore, conservativeness can be reduced since Problem 1 is able to leverage state-dependent uncertainty to select an open-loop trajectory based on the structure of the uncertainty and proximity to constraints. The benefits of these properties, in addition to combining the tube geometry and error dynamics, will be demonstrated in Section VIII.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-A Overview", "weight": 1.0} -->

Collision avoidance is a fundamental capability for many autonomous systems, and is an ideal domain to test DTMPC for two reasons. First, enough safety margin must be allocated to prevent collisions when model error or disturbances are present. More precisely, the optimizer must leverage knowledge of the peak tracking error (given by the tube geometry) to prevent collisions. The robustness of DTMPC and ability to utilize knowledge of state dependent uncertainty can thus be demonstrated. Second, many real-world operating environments have variable obstacle densities so the tube geometry can be optimized in response to a changing environment. The rest of this section presents the model and formal optimal control problem.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B Model", "weight": 1.0} -->

This work uses a double integrator model with nonlinear drag, which describes the dynamics of many mechanical systems. Let $r = \left\lbrack {r_{x}r_{y}r_{z}} \right\rbrack^{T}$ be the inertial position of the system that is to be tracked. The dynamics are

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B Model", "weight": 1.0} -->

where $g \in {\mathbb{R}}^{3}$ is the gravity vector, $C_{d}$ is the unknown but bounded drag coefficient ($0 \leq C_{d} \leq {\overline{C}}_{d}$), and $d$ is a bounded disturbance (${|d|} \leq D$). From Equation 8, the control law is

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-C Collision Avoidance DTMPC", "weight": 1.0} -->

Let $H$, $p_{c}$, and $r_{o}$ denote the shape, location, and size of an obstacle. The minimum control effort DTMPC optimization with collision avoidance for system Equation 28 is formulated as

<!-- chunk {"id": "body-0046", "role": "body", "section": "Problem 2", "weight": 1.0} -->

where again $\check{\cdot}$ denotes the internal variables of the optimization, $| \cdot |$ is the element-wise absolute value, $\underset{¯}{\alpha}$ and $\overline{\alpha}$ are the upper and lower bounds of the control bandwidth, ${\overset{˙}{r}}_{m}$ is the peak desired speed, $v_{m}$ is the max artificial input, and $N_{o}$ is the number of obstacles.

<!-- chunk {"id": "body-0047", "role": "body", "section": "SIMULATION ENVIRONMENT", "weight": 1.0} -->

DTMPC was tested in simulation to demonstrate its ability to optimize tube geometry and utilize knowledge of state-dependent uncertainty through an environment with obstacles. The obstacles were placed non-uniformly to emulate a changing operating condition (i.e., dense/open environment). In order to emphasize both characteristics of DTMPC, three test cases were conducted. First, the bandwidth was optimized when both the model and obstacle locations were completely known. Second, the bandwidth was again optimized with a known model but the obstacle locations were unknown, requiring a receding horizon implementation. Third, state-dependent uncertainty is considered but control bandwidth is kept constant. Nothing about the formulation prevents optimizing bandwidth and leveraging state-dependent uncertainty simultaneously in a receding horizon fashion, this decoupling is only for clarity. The tracking error Equation 14. ‣ IV-C Discussion ‣ IV BOUNDARY LAYER SLIDING CONTROL ‣ Dynamic Tube MPC for Nonlinear Systems") is used to tighten the obstacle and velocity constraint.

<!-- chunk {"id": "body-0048", "role": "body", "section": "SIMULATION ENVIRONMENT", "weight": 1.0} -->

Problem 2 is non-convex due to the nonlinear dynamics and non-convex obstacle constraints so sequential convex programming, similar to that, was used to obtain a solution. The optimization was initialized with a naïve straight-line solution and solved using YALMIP and MOSEK in MATLAB. If large perturbations to the initial guess are required to find a feasible solution, then warm starting the optimization with a better initial guess (possibly provided by a global geometric planner) might be necessary. For the cases tested in this work, the optimization converged within three to four iterations -- fast enough for real-time applications. The simulation parameters are summarized in Table I.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VIII-A Optimized Tube Geometry", "weight": 1.0} -->

The first test scenario for DTMPC highlights its ability to simultaneously optimize an open-loop trajectory and tube geometry in a known environment with obstacles placed non-uniformly. Fig. 3 shows the open-loop trajectory (multi-color), tube geometry (black), and obstacles (grey) when DTMPC optimizes both the trajectory and tube geometry. The color of the trajectory indicates the spatial variation of the control bandwidth, where low- and high-bandwidth are mapped to dark blue and yellow, respectively. It is clear that the bandwidth changes dramatically along the trajectory, especially in the vicinity of obstacles. The insets in Fig. 3 show that high-bandwidth (compact tube geometry) is used for the narrow gap and slalom and low-bandwidth (large tube geometry) for open space. Hence, high-bandwidth control is only used when the system is in close proximity to constraints (i.e., obstacles), consequently limiting aggressive control inputs to only when they are absolutely necessary. Thus, DTMPC can react to varying operating conditions by modifying the trajectory and tube geometry appropriately.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VIII-A Optimized Tube Geometry", "weight": 1.0} -->

Since the tube geometry changes dramatically along the trajectory, it is important to verify that the tube remains invariant. This was tested by conducting 1000 simulations of the closed-loop system with a disturbance profile sampled uniformly from the disturbance set $\mathbb{D}$. Fig. 3 shows the nominal trajectory (red), each closed-loop trial run (blue), tube geometry (black), and obstacles (grey). The inserts show that the state stays within the tube, even as the geometry changes, which verifies that the time-varying tube remains invariant.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VIII-B Receding Horizon Optimized Tube Geometry", "weight": 1.0} -->

In many situations the operating environment is not completely known and requires a receding horizon implementation. The second test scenario for DTMPC highlights its ability to simultaneously optimize an open-loop trajectory and tube geometry in a unknown environment. Fig. 4 shows a receding horizon implementation of DTMPC where only a subset of obstacles are known (dark-grey) and the rest are unknown (light-grey). The bandwidth along the trajectory is visualized with the color map where low- and high-bandwidth are mapped to dark blue and yellow. The first planned trajectory (Fig. 4a) uses high-bandwidth at the narrow gap and low-bandwidth in open space. When the second and third set of obstacles are observed, Fig. 4b and Fig. 4c respectively, DTMPC modifies the trajectory to again use high-bandwidth when in close-proximity to newly discovered obstacles. This further demonstrates DTMPC's ability to construct an optimized trajectory and tube geometry in response to new obstacles.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VIII-C State-Dependent Uncertainty", "weight": 1.0} -->

The third test scenario for DTMPC highlights its ability to leverage knowledge of state-dependent uncertainty, in this case arising from an unknown drag coefficient. From Equation 31, the uncertainty scales with the square of the velocity so higher speeds increase uncertainty. Fig. 5 shows the open-loop trajectory (multi-color), tube geometry (black), and obstacles (grey) when DTMPC leverages state-dependent uncertainty. The color of the trajectory is an indication of the instantaneous speed, where low and high speed are mapped to black and peach, respectively. It is clear that DTMPC generates a speed profile modulated by proximity to obstacles. For instance, using the insets in Fig. 5, the speed is lower (darker) when the trajectory goes through the narrow gap and around the other obstacles; reducing uncertainty and tightening the tube geometry. Further, the speed is higher (lighter) when in the open, subsequently increasing uncertainty causing the tube geometry to expand.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VIII-C State-Dependent Uncertainty", "weight": 1.0} -->

If the state-dependent uncertainty is just assumed to be bounded, a simplification often made out of necessity in other tube MPC algorithms, the tube geometry is so large that, for this obstacle field, the optimization is infeasible with the same straight-line initialization as DTMPC. Hence, DTMPC is able to leverage knowledge of state-dependent uncertainty to reduce conservatism and improve feasibility.

<!-- chunk {"id": "body-0054", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This work presented the Dynamic Tube MPC (DTMPC) algorithm that addresses a number of shortcomings of existing nonlinear tube MPC algorithms. First, the open-loop MPC optimization is augmented with the tube geometry dynamics enabling the trajectory and tube to be optimized simultaneously. Second, DTMPC is able to utilize state-dependent uncertainty to reduce conservativeness and improve optimization feasibility. And third, the tube geometry and error dynamics can be combined to further reduce conservativeness. All three of these properties were made possible by leveraging the simplicity and robustness of boundary layer sliding control. Simulation results showed that DTMPC is able to control the tube geometry size, by changing control bandwidth or leveraging state-dependent uncertainty, in response to changing operating conditions. Future work includes expanding DTMPC to more general nonlinear systems.
