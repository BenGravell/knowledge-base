<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Nonlinear Model Predictive Control Framework Using Reference Generic Terminal Ingredients - Extended Version

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present a quasi infinite horizon nonlinear model predictive control (MPC) scheme for tracking of generic reference trajectories. This scheme is applicable to nonlinear systems, which are locally incrementally stabilizable. For such systems, we provide a reference generic offline procedure to compute an incrementally stabilizing feedback with a continuously parameterized quadratic quasi infinite horizon terminal cost. As a result we get a nonlinear reference tracking MPC scheme with a valid terminal cost for general reachable reference trajectories without increasing the online computational complexity. As a corollary, the terminal cost can also be used to design nonlinear MPC schemes that reliably operate under online changing conditions, including unreachable reference signals. The practicality of this approach is demonstrated with a benchmark example. This paper is an extended version of the accepted paper, and contains additional details regarding \textit{robust} trajectory tracking (App.~B), continuous-time dynamics (App.~C), output tracking stage costs (App.~D) and the connection to incremental system properties (App.~A).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control (MPC) is a well established control method, that computes the control input by repeatedly solving an optimization problem online. The main advantages of MPC are the ability to cope with general nonlinear dynamics, hard state and input constraints, and the inclusion of performance criteria. In MPC (theory), recursive feasibility and closed-loop stability of a desirable setpoint are usually ensured by including suitable terminal ingredients (terminal set and terminal cost) in the optimization problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many applications, the control goal goes beyond the stabilization of a pre-determined setpoint. These practical challenges include tracking of changing reference setpoints, stabilization of dynamic trajectories, output regulation and general economic optimal operation. There exist many promising ideas to tackle these issues in MPC, for example by simultaneously optimizing an artificial reference. However, most of these approaches are limited in some form to linear systems and/or setpoint stabilization. The computation of suitable terminal ingredients seems to be a bottleneck for the practical extension of these methods to nonlinear systems and dynamic trajectories. We bridge this gap, by providing a reference generic offline computation for the terminal ingredients. Thus, we can provide practical schemes for nonlinear systems subject to changing operating conditions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contribution", "weight": 1.0} -->

In this work, we provide a reference generic offline procedure to compute a parameterized terminal cost. This procedure is applicable to both setpoint or trajectory stabilization. The feasibility of this approach requires local incremental stabilizability of the nonlinear dynamics. The existing design procedures use the linearization around the considered setpoint or trajectory to locally establish properties of the nonlinear systems. In a similar spirit, we consider the linearization of the nonlinear system dynamics around all possible points in the constraint set and describe the dynamics analogous to quasi-linear parameter-varying (LPV) systems. With this description, we formulate the desired properties on the linearized dynamics and provide suitable LMIs to compute the parameter dependent terminal cost and controller. In closed-loop operation we have a quadratic terminal cost with an ellipsoidal terminal constraint directly available. This provides a generalization of the offline computations in to generic references. We employ the proposed method in an evasive maneuver test for a car and show that the design of suitable reference generic terminal ingredients can significantly improve the control performance compared to MPC schemes with terminal equality constraints or without terminal constraints.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contribution", "weight": 1.0} -->

Given these terminal ingredients, we can extend existing tracking MPC schemes, such as to nonlinear system dynamics and optimal periodic operation, which is a fundamental step towards practical nonlinear MPC schemes. In particular, we provide a nonlinear periodic tracking MPC scheme for exogenous output signals as an extension to.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Outline", "weight": 1.0} -->

The remainder of this paper is structured as follows: Section II presents the reference tracking MPC scheme based on the proposed parameterized terminal ingredients. Section III provides a constructive procedure to design parametric terminal ingredients independent of the considered reference. Section IV shows how the resulting parameterized terminal ingredients can be used to extend existing MPC schemes for changing operation conditions to nonlinear system dynamics and periodic operation. Section V shows the practicality of this procedure with numerical examples. Section VI concludes the paper. In the appendix, these results are extended to robust trajectory tracking (App. -B), continuous-time dynamics (App. -C), and output tracking stage costs (App. -D). In addition, the connection between the generic terminal ingredients and incremental system properties is discussed (App. -A Incremental exponential stabilizability ‣ A nonlinear model predictive control framework using reference generic terminal ingredients - extended version")).

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Notation", "weight": 1.0} -->

The quadratic norm with respect to a positive definite matrix $Q = Q^{\top}$ is denoted by ${\| x\|}_{Q}^{2} = {x^{\top}Qx}$. The minimal and maximal eigenvalue of a symmetric matrix $Q = Q^{\top}$ is denoted by $\lambda_{\min}{(Q)}$ and $\lambda_{\max}{(Q)}$, respectively. The identity matrix is $I_{n} \in {\mathbb{R}}^{n \times n}$. The interior of a set $\mathcal{X}$ is denoted by $\text{int}{(\mathcal{X})}$. The vertices of a polytopic set $\Theta$ are denoted by $\theta_{i} \in {\text{Vert}{(\Theta)}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Setup", "weight": 1.0} -->

We consider the following nonlinear discrete-time system

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Setup", "weight": 1.0} -->

with the state $x \in {\mathbb{R}}^{n}$, control input $u \in {\mathbb{R}}^{m}$, and time step $t \in {\mathbb{N}}$. The extension of the following derivation to continuous-time dynamics is detailed in Appendix -C. We impose point-wise in time constraints on the state and input

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Setup", "weight": 1.0} -->

with some compact^11^1The derivations can be extended to time-varying constraint sets $\mathcal{Z}{(t)}$ and dynamics $f{(x,u,t)}$. The consideration of non-compact constraint sets may require additional uniformity conditions on the nonlinear dynamics. set $\mathcal{Z}$. We consider the following assumption regarding the reference signal ${r = {(x_{r},u_{r})} \in {\mathbb{R}}^{n + m}}.$

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

This assumption characterizes that the reference trajectory $r$ is reachable, i.e., follows the dynamics $f$ and lies (strictly) in the constraint set $\mathcal{Z}$. If the reference trajectory is not reachable it is possible to enforce these constraints on an artificial reference trajectory which can be included in the MPC optimization problem, compare Section IV.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The set $\mathcal{R}{(r)}$ can be modified to incorporate additional incremental input constraints ${\|{{u_{r}{({t + 1})}} - {u_{r}{(t)}}}\|}_{\infty} \leq \epsilon$. Setpoints are included as a special case, with ${\mathcal{R}{(r)}} = r$ and the steady-state manifold $\mathcal{Z}_{r}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Terminal cost and terminal set", "weight": 1.0} -->

Denote the tracking error by ${e_{r}{(t)}} = {{x{(t)}} - {x_{r}{(t)}}}$. The control goal is to stabilize the tracking error ${e_{r}{(t)}} = 0$ and achieve constraint satisfaction ${({x{(t)}},{u{(t)}})} \in \mathcal{Z}$, ${\forall t} \geq 0$. To this end we define the quadratic reference tracking stage cost

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Terminal cost and terminal set", "weight": 1.0} -->

with positive definite weighting matrices $Q,R$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 2", "weight": 1.0} -->

As discussed in the introduction, we need suitable terminal ingredients to ensure stability and recursive feasibility for the closed-loop system.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

For $r = r^{+} = 0$ this reduces to the standard conditions. For a given trajectory $r$, this implies time-varying terminal ingredients, compare. Designing suitable^22^2In principle, this assumption can always be satisfied with a terminal equality constraint ${\mathcal{X}_{f}{(r)}} = x_{r}$. However, this can lead to numerical problems, and decrease performance and robustness of the MPC scheme. In addition, tracking schemes such as, typically require a non-vanishing terminal set size $\alpha$ to ensure exponential stability, compare Section IV. terminal ingredients that satisfy this assumption is the main contribution of this paper and is discussed in more detail in the Section III.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Assumption 1 implies that the reference $r{(t)}$ is contained within a control invariant subset $\mathcal{Z}_{\infty} \subseteq \mathcal{Z}_{r}$. Thus, Assumption 2 could be relaxed, such that the conditions only need to be satisfied for points $r \in \mathcal{Z}_{\infty}$. The exact characterization of the set $\mathcal{Z}_{\infty}$ is, however, challenging and thus we consider the stricter^33^3If there exists a fixed constant $T_{0}$, such that ${{r{({t + k})}} \in \mathcal{Z}_{r}},{{\forall k} \in {\lbrack 0,T_{0}\rbrack}}$, implies ${r{(t)}} \in \mathcal{Z}_{\infty}$, then the conditions in Assumption 2 are not stricter. However, if we use a convex overapproximation (Prop.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 3", "weight": 1.0} -->

1) and/or parameterize the matrices $P_{f},K_{f}$, then this may introduce additional conservatism. conditions as formulated in Assumption 2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-D Preliminary results", "weight": 1.0} -->

The MPC scheme is based on the following (standard) MPC optimization problem

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-D Preliminary results", "weight": 1.0} -->

The solution to this optimization problem are the value function $V$ and the optimal input trajectory $u^{\ast}{( \cdot |t)}$. In closed-loop operation we apply the first part of the optimized input trajectory to the system, leading to the following closed loop

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-D Preliminary results", "weight": 1.0} -->

The following theorem summarizes the standard theoretical properties of the closed-loop system.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 4", "weight": 1.0} -->

A powerful alternative to the proposed quasi-infinite horizon reference tracking MPC scheme would be a reference tracking MPC scheme without terminal ingredients (${V_{f}{(x,r)}} = 0$, ${\mathcal{X}_{f}{(r)}} = \mathcal{X}$). If it is possible to design terminal ingredients (Ass. 2), the value function of such an MPC scheme without terminal constraints is locally bounded by $V{(x{(t)},r{( \cdot |t)})} \leq \gamma\ell{(x,u,r)}$, with a suitable constant $\gamma$, compare \[22, Prop. 2\]. Thus, an MPC scheme without terminal constraints enjoys similar closed-loop properties to Theorem 1, provided a sufficiently large prediction horizon $N$ is used, compare \[22, Thm. 2\]. One of the core advantages of including suitably designed terminal ingredients is that we can implement the MPC scheme with a short prediction horizon $N$. On the other hand, if the reference is not reachable (Ass.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 4", "weight": 1.0} -->

1), MPC schemes without terminal constraints can still be successfully applied \[22, Thm. 4\], which is in general not the case for MPC schemes with terminal constraints.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Reference generic offline computations", "weight": 1.0} -->

This section provides a reference generic offline computation to design terminal ingredients for nonlinear reference tracking MPC. In Lemma 1 we provide sufficient conditions for the terminal ingredients based on properties of the linearization. Then, two approaches based on LMI computations are described to compute the terminal ingredients, based on Lemma 2 and Proposition 1. After that, a procedure to obtain a non conservative terminal set size $\alpha$ is discussed. Finally, the overall offline procedure is summarized in Algorithm 2. For the special case of setpoint tracking, existing methods are discussed in relation to the proposed procedure. In Appendix -C and -D, these results are extended to continuous-time dynamics and output tracking stage costs, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Sufficient conditions based on the linearization", "weight": 1.0} -->

We denote the Jacobian of $f$ evaluated around an arbitrary point $r \in \mathcal{Z}_{r}$ by

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Sufficient conditions based on the linearization", "weight": 1.0} -->

The following lemma establishes local incremental properties of the nonlinear system dynamics based on the linearization.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Quasi-LPV based procedure", "weight": 1.0} -->

Lemma 1 states that matrices satisfying inequality also satisfy Assumption 2 with a suitable terminal set size $\alpha$. In the following, we formulate computationally tractable optimization problems to compute matrices that satisfy the conditions in Lemma 1. The following Lemma transforms the conditions in to be linear in the arguments.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 5", "weight": 1.0} -->

One solution to this problem would be sum-of-squares (SOS) optimization. Assuming $A,B$ are polynomial, consider matrices $X,Y$ polynomial in $r$ (with a specified order $d$) and ensure that the matrix in is SOS. A similar approach is suggested in to find a control contraction metric (CCM) for continuous-time systems (which is a strongly related problem). This approach is not pursued here since most systems require a polynomial of high order to approximate the nonlinear dynamics and the computational complexity grows exponentially in $n^{d}$, thus prohibiting the practical application. The connection between CCM and LPV gain-scheduling design is discussed.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 5", "weight": 1.0} -->

We approach this problem from the perspective of quasi-LPV systems and gain-scheduling. First, write the Jacobian as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 5", "weight": 1.0} -->

with some nonlinear (continuously differentiable) parameters $\theta \in {\mathbb{R}}^{p}$. This can always be achieved with $p \leq {n{({n + m})}}$. We impose the same structure on the optimization variables with

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 6", "weight": 1.0} -->

For input affine systems of the form ${f{(x,u)}} = {{f_{x}{(x)}} + {Bu}}$, the Jacobian and correspondingly the parameters $\theta_{i}$ only depend on $x_{r}$. Thus, the resulting terminal ingredients are solely parameterized by the state $x_{r}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Using the parameterization -, contains only a finite number of optimization variables, but still needs to be verified for all ${r \in \mathcal{Z}_{r}},{r^{+} \in {\mathcal{R}{(r)}}}$. There are two options to deal with this: convexifying the problem or gridding the constraint set.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B1 Convexify", "weight": 1.0} -->

In order to convexify, we match the constraint sets $\mathcal{Z}_{r},{\mathcal{R}{(r)}}$ on the reference $r$ to polytopic constraint sets $\Theta,\Omega$ on the parameters $\theta$. The polytopic sets $\Theta,{\Omega{(\theta)}}$ need to satisfy

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B1 Convexify", "weight": 1.0} -->

which consists of $6^{p}$ vertices. The following proposition provides a simple convex procedure to compute a terminal cost, by solving a finite number of LMIs.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 7", "weight": 1.0} -->

The result in Proposition 1 remains valid, if the set $\overline{\Theta}$ in is replaced by the set $\overline{\Theta} = {\Theta \times {({\Theta \oplus \Omega})}}$. This set has only $4^{p}$ vertices and the induced conservatism of this approximation is negligible if $\Omega$ is small compared to $\Theta$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B2 Gridding", "weight": 1.0} -->

A common heuristic to ensure that parameter dependent LMIs such as hold for all $(r,r^{+})$ is to consider the constraints on sufficiently many sample points in the constraint set, compare e.g. \[28, Sec. 4.2\]. Due to continuity, the constraint is typically satisfied on the full constraint set if it holds on a sufficiently fine grid. For this method it is crucial that satisfaction of (4a) is verified by using a fine grid (compare Algorithm 1).

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B2 Gridding", "weight": 1.0} -->

The gridding consists of a grid over all possible state and input combinations $(r,r^{+})$, i.e., all considered points satisfy

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B2 Gridding", "weight": 1.0} -->

For the simple structure $\mathcal{R}{(r)}$ in Assumption 1 this can be achieved by gridding $r$, computing $x_{r}^{+} = {f{(x_{r},u_{r})}}$, and considering all $u_{r}^{+}$, such that ${(x_{r}^{+},u_{r}^{+})} \in \mathcal{Z}_{r}$ and ${({f{(x_{r}^{+},u_{r}^{+})}},{\overset{\sim}{u}}_{r})} \in \mathcal{Z}_{r}$ with some ${\overset{\sim}{u}}_{r}$. This approach does not introduce additional conservatism, but is computationally challenging for high dimensional systems. As discussed in Remark 1 we can include additional constraints on the reference, which makes the offline computation less conservative.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B2 Gridding", "weight": 1.0} -->

If some parameters, e.g. $u_{r}$, enter the LMIs affinely and are subject to polytopic constraints, it suffices to consider the vertices of the corresponding constraint set.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B2 Gridding", "weight": 1.0} -->

The advantage of the convex procedure (compared to the gridding) is that it typically scales better with the system dimension. This comes at the cost of additional conservatism due to the construction of the set $\overline{\Theta}$ and the additional multi-convexity constraint (20d). The computational demand can be reduced by considering (block-)diagonal multipliers $\Lambda_{i} = {\lambda_{i}I}$. It can often be beneficial to consider a combination of the two approaches, i.e. grid in some dimensions and conservatively convexify in others. The advantages and applicability of both approaches are explored in more detail in the numerical examples in Section V.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B2 Gridding", "weight": 1.0} -->

The main result is that we can formulate the offline design procedure similar to the gain scheduling synthesis of (quasi)-LPV systems and thus can draw on a well established field to formulate^55^5If the parameters $\theta_{i}$ are chosen based on a vertex representation (${\theta_{i} \geq 0},{{\sum_{i = 1}^{p}\theta_{i}} = 1}$) the multi-convexity condition (20d) can be replaced by positivity conditions of the polynomials, compare for example. In a convexification with an additional matrix is considered. More elaborate methods to formulate LPV synthesis with finite LMIs can be found. offline LMI procedures, compare.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Non-conservative terminal set size $\\alpha$", "weight": 1.0} -->

The terminal set size $\alpha$ derived in Lemma 1 can be quite conservative. In the following we illustrate how a non conservative value $\alpha$ can be computed (given $P_{f}$ and $K_{f}$).

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C1 Constraint satisfaction - $\\alpha_{2}$", "weight": 1.0} -->

Assume that we have polytopic constraints of the form $\mathcal{Z} = \left. \{{r = {(x,u)}} \middle| {{L_{r}r} \leq l}\} \right.$. The constant $\alpha_{2}$, with the property that $\alpha \leq \alpha_{2}$ implies constraint satisfaction (4b), can be computed with

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C1 Constraint satisfaction - $\\alpha_{2}$", "weight": 1.0} -->

This problem can be efficiently solved by girdding the constraint set $\mathcal{Z}_{r}$, solving the resulting linear program (LP) for each point $r$ and taking the minimum. In the special case that $P_{f},K_{f}$ are constant this reduces to one small scale LP.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C2 Local Stability - $\\alpha_{1}$", "weight": 1.0} -->

Determining a non-conservative constant $\alpha_{1}$, related to the local Lyapunov function $V_{f}$ can be significantly more difficult. For comparison, in the setpoint stabilization case a non-convex optimization problem is formulated to check whether (4a) holds for a specific value of $\alpha_{1}$, compare \[12, Rk. 3.1\]. In a similar fashion, we consider the following algorithm^66^6Algorithm 1 can be thought of as a sampling based strategy to solve this non-convex optimization problem considered in \[12, Rk. 3.1\]. Using standard convex solvers, like sequential quadratic programming (SQP), yield a faster solution, but can get stuck in local minima. This is dangerous for this problem, since the local minima correspond to values $\alpha$ that do not satisfy Assumption 2. Alternatively, nonlinear Lipschitz-like bounds can be used to reduce the conservatism, compare (which, however, also use sampling).

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C2 Local Stability - $\\alpha_{1}$", "weight": 1.0} -->

1:Given a candidate constant α1:
2:Grid: Select (r,r+) satisfying
4:Generate random vectors Δ xi: with ∥Δ xi∥Pf (r)2 ≤ α1.
Algorithm 1 Offline computation - Local stability α1

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C2 Local Stability - $\\alpha_{1}$", "weight": 1.0} -->

Starting with $\alpha_{1} = \alpha_{2}$, the value $\alpha_{1}$ is iteratively decreased until all considered combination ($r,r^{+},x_{i}$) satisfy (4a).

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-C2 Local Stability - $\\alpha_{1}$", "weight": 1.0} -->

The overall offline procedure to compute the terminal ingredients (Ass.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-C2 Local Stability - $\\alpha_{1}$", "weight": 1.0} -->

1:Define θ corresponding to the linearization.
2:LMI computation using gridding or convexification:
3:Convex: Determine hyperbox sets Θ, Ω satisfying.
4: Solve using $\overline{\Theta}$ according to or Remark 7.
5:Gridding: Select (ri,ri+) satisfying.
6: Solve for all (ri,ri+).
7:Compute size of the terminal set α = min {α1, α2}:
8: a):compute α1 using Algorithm 1 (or ),
Algorithm 2 Offline computation

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-C2 Local Stability - $\\alpha_{1}$", "weight": 1.0} -->

The presented offline procedure is considerably more involved than for example the computation for one specific setpoint. We emphasize that this procedure only has to be completed once and we need no repeated offline computations to account for changing operation conditions. Furthermore, the applicability to nonlinear systems with the corresponding computational effort offline is detailed with numerical examples in Section V.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-D Setpoint tracking", "weight": 1.0} -->

Now we discuss setpoint tracking, which is included in the previous derivation as a special case with $\mathcal{Z}_{r}$ such that ${(x_{r},u_{r})} \in \mathcal{Z}_{r}$ implies $x_{r} = {f{(x_{r},u_{r})}}$ and ${\mathcal{R}{(r)}} = r$. Note, that both presented approaches significantly simplify in this case. For the gridding approach it suffices to grid along the steady-state manifold $\mathcal{Z}_{r}$ which is typically low dimensional. In the convex approach (Prop. 1) we have $\theta^{+} = \theta$ and thus we only consider the $2^{p}$ vertices of $\Theta$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-D Setpoint tracking", "weight": 1.0} -->

Compared to the dynamic reference tracking problem, the problem of tracking a setpoint has received a lot of attention in the literature and many solutions have been suggested.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-D Setpoint tracking", "weight": 1.0} -->

One of the first attempts to solve this issue is the usage of a pseudo linearization. There, a nonlinear state and input transformation is sought, such that the linearization of the transformed system around the setpoints is constant and thus constant terminal ingredients can be used. This approach seems unpractical, since there is no easy or simple method to compute such a pseudo linearization.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-D Setpoint tracking", "weight": 1.0} -->

In the steady-state manifold $\mathcal{Z}_{r}$ is partitioned into sets. In each set the nonlinear system is described as an LTV system and a constant terminal cost and controller are computed. Correspondingly, in closed-loop operation under changing setpoints the terminal cost matrix $P_{f}$ is piece-wise constant. This might cause numerical problems in the optimization, since the cost is not differentiable with respect to the reference $r$. Furthermore, the (manual) partitioning of the steady-state manifold seems difficult for general MIMO systems (if the dimension of the steady-state manifold is larger than one). In comparison, Algorithm 2 yields continuously parameterized terminal ingredients, thus avoiding the need for user defined partitioning and piece-wise definitions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-D Setpoint tracking", "weight": 1.0} -->

In \[9, Remark 8\] it was proposed to compute a continuously parameterized controller $K_{f}{(r)}$ by analytically using a pole-placement formula and solving the corresponding Lyapunov^77^7In, the terminal cost $V_{f}$ is computed for a (differentiable) economic stage cost $\ell{(x,u)}$ (not necessarily quadratic), compare also. The computation of the terminal cost is decomposed into a linear and quadratic term, compare. Computing the quadratic term of this economic terminal cost is equivalent to computing a quadratic terminal cost for a quadratic stage cost (Ass 2). equation to obtain $P_{f}{(r)}$. The resulting terminal ingredients are quite similar to the proposed ones. However, this procedure cannot be directly translated into a simple optimization problem and might hence not be tractable.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Nonlinear MPC subject to changing operation conditions", "weight": 1.0} -->

Many control problems are more general than the reference tracking considered in Section II. One challenge includes tracking and output regulation with exogenous signals in order to accommodate online changing operation conditions. For this set of problems, the reference $r$ might not satisfy Assumption 1 (due to sudden changes and unreachable signals), compare. More generally, the minimization of a possibly online changing and non-convex economic cost is a (non-trivial) control problem which is often encountered, compare. One promising method to solve these problems is the simultaneous optimization of an artificial reference, as done. Compared to a standard reference tracking MPC formulation such as, these schemes ensure recursive feasibility despite changes in exogenous signals (such as the desired output reference or the economic cost). In this section, we show how the reference generic terminal ingredients can be used to design nonlinear MPC schemes that reliably operate under changing operating conditions, as an extension and combination of the ideas. In particular, we present a scheme that exponentially stabilizes the periodic trajectory which best tracks an exogenous output signal.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Nonlinear MPC subject to changing operation conditions", "weight": 1.0} -->

The extension of the economic MPC schemes to periodic artificial trajectories based on the reference generic terminal ingredients is beyond the scope of this work and part of current research.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Nonlinear periodic tracking MPC subject to changing exogenous output references", "weight": 1.0} -->

We assume that at time $t$ an exogenous $T$-periodic output reference signal $y_{e}{( \cdot |t)} \in {\mathbb{R}}^{p \times T}$ is given. For some $T$-periodic reference $r{( \cdot |t)} = {(x_{r}{( \cdot |t)},u_{r}{( \cdot |t)})} \in {\mathbb{R}}^{{({n + m})} \times T}$, we define the tracking cost with respect to this output signal $y_{e}$ by

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-A Nonlinear periodic tracking MPC subject to changing exogenous output references", "weight": 1.0} -->

with a bounded nonlinear output function $h:{\mathcal{Z}_{r}\rightarrow{\mathbb{R}}^{p}}$. The objective is to stabilize the feasible $T$-periodic reference trajectory $r$, that minimizes $J_{T}$. In the issue of stabilizing the optimal setpoint for piece-wise constant output signals has been investigated. In periodic trajectories have been considered for the special case of linear systems. By combining these methods with the proposed terminal ingredients, we can design a nonlinear MPC scheme that stabilizes the optimal periodic^88^8 In the case of setpoint tracking ($T = 1$), the MPC scheme reduces to. As discussed in Section III-D, the proposed procedure can be used to design suitable terminal ingredients for setpoints. trajectory for periodic output reference signals, compare. The scheme is based on the following optimization problem

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-A Nonlinear periodic tracking MPC subject to changing exogenous output references", "weight": 1.0} -->

This scheme is recursively feasible, independent of the output reference signal $y_{e}$. Furthermore, if the exogenous signal $y_{e}$ is $T$-periodic the closed-loop system is stable. Additionally, if a convexity and continuity condition on the set of feasible periodic orbits and the output function $h$ is satisfied \[19, Ass. 5\], then the optimal reachable periodic trajectory is (uniformly) exponentially stable for the resulting closed-loop system. Thus, the terminal ingredients enable us to implement a nonlinear version of the tracking scheme, that ensures exponential stability of the optimal (periodic) operation. More details on the theoretical properties and numerical examples can be found. Although the consideration of general non-periodic trajectories is still an open issue, we conjecture that the approach can be extended to any class of finitely parameterized reference trajectories.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

The following examples show the applicability of the proposed method to nonlinear systems and the closed-loop performance improvement when including suitable terminal ingredients. We first illustrate the basic procedure at the example of a periodic reference tracking task for a continuous stirred-tank reactor (CSTR). Then we demonstrate the advantages of using suitable terminal ingredients with (robust) trajectory tracking and an evasive maneuver test for a car. Additional examples, including tracking of periodic output signals (Sec. IV-A) with a nonlinear ball and plate system can be found.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Numerical examples", "weight": 1.0} -->

In the following examples, the offline computation is done with an Intel Core i7 using the semidefinite programming (SDP) solver SeDuMi-1.3 and the online optimization is done with CasADi. The offline computation can be done using both the discrete-time formulation (Sec. III) or the continuous-time formulation (Appendix -C). Hence, we also compare the performance of these different formulations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "System model", "weight": 1.0} -->

We consider a continuous-time model of a continuous stirred-tank reactor (CSTR)

<!-- chunk {"id": "body-0065", "role": "body", "section": "System model", "weight": 1.0} -->

where $x_{1},x_{2},x_{3}$ correspond to the concentration of the reaction, the desired product, waste product and $u$ is related to the heat flux through the cooling jacket, compare, \[37, Sec. 3.4\]. The constraints are

<!-- chunk {"id": "body-0066", "role": "body", "section": "System model", "weight": 1.0} -->

The discrete-time model is defined with explicit Runge-Kutta discretization of order $4$ and a sampling time^99^9 In \[37, Sec. 3.4\] a sampling time of $h = 0.1$ is used. However, with the considered fourth order explicit Runge-Kutta discretization, a sampling time of $h = 0.1$ does not preserve stability of the continuous-time system. of $h = 0.01$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "System model", "weight": 1.0} -->

For this system, periodic operation is economically beneficial, compare. Thus, we consider the problem of tracking reachable periodic reference trajectories $r$ (Assumption 1), corresponding to the economic operation of the plant.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Offline computations", "weight": 1.0} -->

In the following, we illustrate the reference generic offline computation for this system. We consider the standard quadratic tracking stage cost with $Q = I_{3}$, $R = 10$ and use $\epsilon = 0.1$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Offline computations", "weight": 1.0} -->

For the continuous-time system, the Jacobian contains four nonlinear terms, yielding the parameters

<!-- chunk {"id": "body-0070", "role": "body", "section": "Offline computations", "weight": 1.0} -->

The input $u_{r}$ enters the LMIs affinely. Thus, we only consider the two vertices of $u_{r}$ and grid $(x_{1},x_{3})$ using $10^{2}$ points.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Offline computations", "weight": 1.0} -->

For the discrete-time system, the explicit description of the nonlinear dynamics $f$ and the corresponding Jacobian ${A{(r)}},{B{(r)}}$ is complex. Thus, we directly define the non-constant^1010^10 The derivatives $\partial{f_{3}/{\partial r}}$, $\partial{f_{1}/{\partial x_{2}}}$, and $\partial{f_{2}/{\partial x_{2}}}$ are constant. components of the Jacobian $A,B$ as the parameters $\theta \in {\mathbb{R}}^{6}$. We compute the hyperbox sets ${\Theta,\Omega} \subseteq {\mathbb{R}}^{6}$ satisfying numerically. For the discrete-time convex approach the polytopic description $\overline{\Theta}$ and the hyperbox description $\Theta \times \Omega$ (Remark 7) are considered.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Offline computations", "weight": 1.0} -->

For the gridding, ${(x_{1},x_{3},u_{r},u_{r}^{+})} \in {\mathbb{R}}^{4}$ is gridded using $10^{4}$ points, of which approximately $8.000$ satisfy the conditions and are considered in the optimization problem.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Offline computations", "weight": 1.0} -->

The computational demand and the performance of the different methods are detailed in Table I. As expected, the gridding approach yields the smallest and least conservative terminal cost. For this example, the convex discrete-time approach (Prop. 1) seems less favorable, which is mainly due to the simple description of the parameters. Due to the small sampling time $h$ and correspondingly small set $\Omega$, the more detailed description $\overline{\Theta}$ only marginally improves the performance but significantly increases the offline computational demand. Furthermore, the continuous-time formulation can be computed more efficiently. We note, that the parameters $Q,R,h$, are chosen, such that the continuous-time control law is also stabilizing for the discrete-time implementation. In particular, if $R$ is decreased or $h$ increased, the terminal ingredients based on the continuous-time formulation do not satisfy Assumption 2 with a piece wise constant input. Such considerations are not necessary for the discrete-time formulation, compare Remark 14 in Appendix -C.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Offline computations", "weight": 1.0} -->

#LMIs

<!-- chunk {"id": "body-0075", "role": "body", "section": "Offline computations", "weight": 1.0} -->

In the following, we consider the discrete-time terminal ingredients based on Lemma 2. Computing $\alpha_{2} = 0.02$ using requires $30$ s. Executing Algorithm 1 to ensure that $\alpha = 0.02$ is valid takes $10$ min using ${2 \cdot 20^{4} \cdot 100} = {3.2 \cdot 10^{7}}$ samples.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Offline computations", "weight": 1.0} -->

In Figure 1 we can see an exemplary periodic trajectory and the corresponding terminal set^1111^11If $\alpha$ would be recomputed for the specific trajectory $r$, we would get $\alpha = 0.1$. This conservatism is a result of the fact, that the previously computed value $\alpha$ needs to be valid for every reachable reference trajectory (Ass. 1).. The period length is $T = 1144$, which corresponds to $11.44s$, compare \[37, Sec. 3.4\].

<!-- chunk {"id": "body-0077", "role": "body", "section": "Offline computations", "weight": 1.0} -->

We wish to emphasize that this offline computation is only done once and requires no explicit knowledge of the specific trajectory or its period length $T$. This is in contrast to the existing methods, such as which would compute terminal ingredients for a specific reference trajectory and thus could not deal with online changing operation conditions (e.g. due to changes in the price signal ).

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-B Automated driving - robust reference tracking", "weight": 1.0} -->

The following example shows the applicability of the proposed procedure to nonlinear robust reference tracking and demonstrates the performance improvement of including suitable terminal ingredients.

<!-- chunk {"id": "body-0079", "role": "body", "section": "System model", "weight": 1.0} -->

We consider a nonlinear kinematic bicycle model of a car

<!-- chunk {"id": "body-0080", "role": "body", "section": "System model", "weight": 1.0} -->

with the position $z_{i}$, the inertial heading $\psi$, the velocity $v$, the front steering angle $\delta$, the acceleration $a$ and the change in the steering angle $u_{\delta}$. The model constants $l_{f} = 1.4$ and $l_{r} = 1.5$ represent the distance of the center of mass to the front and rear axle. More details on kinematic bicycle models can be found. The (non-compact) constraint sets are given by

<!-- chunk {"id": "body-0081", "role": "body", "section": "Offline computations", "weight": 1.0} -->

We consider the stage cost $Q = I_{5}$, $R = I_{2}$ and $\epsilon = 0.1$ and use an Euler discretization with the step size $h = {2ms}$. Computing the linearization and using a quasi-LPV parameterization results in $\theta \in {\mathbb{R}}^{8}$, where the parameters $\theta$ consist of trigonometric functions in $\Psi,\delta$ and are linear in the velocity $v$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Offline computations", "weight": 1.0} -->

For this example, the convex approach (Prop. 1) is not feasible, since the simple and conservative hyperbox^1212^12This description does not take into account that $\sin{({\psi + \beta})}$ and $\cos{({\psi + \beta})}$ cannot be zero simultaneously. This issue can be circumvented by considering a more detailed description of $\Theta$, e.g. using coupled ellipsoidal constraints. description $\theta \in \Theta$ includes linearized dynamics which are not stabilizable.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Offline computations", "weight": 1.0} -->

For the gridding, we consider both the discrete-time and a continuous-time formulation (compare Appendix -C). In the continuous-time formulation $a$ and $u_{\delta}$ enter the LMIs affinely. Thus, we only consider the $2^{2} = 4$ vertices of $(a,u_{\delta})$ and grid $(\psi,v,\delta)$ using $10^{3}$ points. For the discrete-time formulation the LMIs are not affine in $u_{\delta}$ and thus we grid $(\psi,v,\delta,u_{\delta})$ using $10^{3} \cdot 5$ points and consider the two vertices of $a$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Offline computations", "weight": 1.0} -->

The dimensions of the corresponding LMI-blocks are ${{({{2n} + m})} \times {({{2n} + m})}} = {12 \times 12}$ and ${{({{3n} + m})} \times {({{3n} + m})}} = {17 \times 17}$, respectively. The following table captures the weighting of the terminal cost and the computational effort of the proposed approach. Method Continuous-Time Discrete-time (Lemma. 4) (Lemma. 2) $\#$LMIs-blocks ${10^{3} \cdot 2^{2}} = {4 \cdot 10^{3}}$ ${10^{3} \cdot 5 \cdot 2} = 10^{4}$ comp.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Remark 8", "weight": 1.0} -->

For the considered example and parameters, the continuous-time terminal cost is also valid for a zero-order hold discrete-time implementation with $h = {2ms}$. This is in general not the case. For example if $R = 10^{- 4}$ or $h = {10ms}$ is chosen, the terminal ingredients based on the continuous-time offline optimization are not stabilizing for the discrete-time system. If the continuous-time offline procedure is used, the computation (and thus verification) of $\alpha$ for the discrete-time system using Algorithm 1 is crucial. This issue is also discussed in Remark 14 of Appendix -C.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Remark 8", "weight": 1.0} -->

In the following, we only consider the discrete-time terminal ingredients based on Lemma 2. Executing Algorithm 1 to ensure that $\alpha_{1} = 10^{4}$ is valid takes $25$ min using ${20^{3} \cdot 10^{2} \cdot 100} = {8 \cdot 10^{7}}$ samples.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

In order to demonstrate the applicability of the proposed tracking MPC scheme, we consider an evasive maneuver test (compare ISO norm 3888-2 ). In this scenario a car is driving with $v = {{20m}/s}$ and performs two consecutive lane changes to simulate the avoidance of a possible obstacle. The basic setup, with a feasible reference trajectory $r$, additional path constraints^1313^13Ideally, these constraints should restrict the overall position of the vehicle. For simplicity we treat them as (time-varying) polytopic constraints on $z_{2}$, that require the $z_{2}$ position to be within a margin of $\pm {35cm}$. $\mathcal{X}$ and the terminal set (projected on $z_{1} \times z_{2}$) can be seen in Figure 2. The terminal set size is restricted by the input constraint on $u_{\delta}$ and the path constraint $\mathcal{X}$, yielding the terminal set size $\alpha = \alpha_{2} \approx 10^{2}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

For comparison, we also computed a terminal cost for this specific given trajectory based on an LTV description. The generic offline computation results in a roughly five times larger terminal cost, which gives an indication of the conservatism.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

In order to show that the proposed approach can be applied under realistic conditions, we consider additive disturbances ${w{(t)}} \in {\mathbb{R}}^{n}$ and a prediction horizon of $N = 10$. To ensure robust constraint satisfaction, we use the constraint tightening method proposed, which is based on the achievable contraction^1414^14This property is verified by computing a terminal cost, which is valid on the full constraint set $\mathcal{Z}$, compare Prop. 2 Incremental exponential stabilizability ‣ A nonlinear model predictive control framework using reference generic terminal ingredients - extended version") and App. -B. Analogous to the computation of $\alpha$, the numerical value of $\rho$ can be ascertained using Alg. 1. rate $\rho = 0.9995$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

To ensure robust recursive feasibility, the terminal set needs to be robust positively invariant, which can be ensured for ${\|{w{(t)}}\|} \leq \hat{w} = {1.82 \cdot 10^{- 5}} = {{9.1 \cdot 10^{- 3}}h}$, compare in Proposition 4 of Appendix -B. The constraints are tightened over the prediction horizon with a scalar using the method in

<!-- chunk {"id": "body-0091", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

with $\epsilon = {2.5 \cdot 10^{- 4}}$. The resulting robust tracking MPC scheme guarantees (uniform) practical exponential stability and robust constraint satisfaction, for details see Appendix -B and.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

We simulated the closed-loop MPC using random disturbances ${\|{w{(t)}}\|} = \hat{w}$ and compared the performance to MPC without terminal constraints ($V_{f} = 0$, UC, ) and MPC with terminal equality constraint (${\mathcal{X}_{f}{(r)}} = x_{r}$, TEC). To enable a comparison of the computational demand we fixed the number of iterations in CasADi to $1$ per time step, resulting in online computation time of approx $13$ ms for all three approaches. The corresponding results can be seen in Figures 3 and 4.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

The closed-loop performance (as measured by the tracking stage cost ^1515^15If we ignore the input tracking stage cost and only consider ${\|{x - x_{r}}\|}_{Q}^{2}$ as the performance, then the TEC has only $13\%$ of the tracking error of QINF and UC has $30$-times the tracking error. If, for some reason, we would only be interested in the tracking error in the input ${\|{u - u_{r}}\|}_{R}^{2}$, then UC has only $48\%$ of the error of QINF and TEC has $4.5 \cdot 10^{3}$ times the error of QINF. ) of UC and TEC are $10$ and $3.000$ times larger than the proposed scheme with the terminal cost (QINF), compare Figure 3.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

Specifically, the MPC without terminal constraints (UC) has a significant (growing) tracking error in the position (see Figure 4), since the UC with a short horizon typically leads to a slower convergence with smaller control action (as stability is not explicitly enforced). On the other side, the terminal equality constraint MPC (TEC) has large deadbeat like input oscillations, which is a result of the terminal constraint with the short prediction horizon. UC and TEC achieve a similar performance to QINF with $N = 10$, if the prediction horizon^1616^16For this second comparison, we did not limit the number of iterations for UC and TEC, since we were unable to achieve a similar performance with UC using only $1$ iterations (which may be due to the lack of a good warmstart). is increased to $N = 23$ and $N = 59$, respectively. This increases the online computational demand compared to QINF by $100\%$ and $300\%$, respectively.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Robust trajectory tracking - Evasive maneuver test", "weight": 1.0} -->

The proposed MPC scheme robustly achieves a small tracking error with a short prediction horizon. This shows that including (suitable) terminal ingredients significantly reduces the tracking error and improves the closed-loop performance, as also articulated.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented a procedure to compute terminal ingredients for nonlinear reference tracking MPC schemes offline. The main novelty in this approach is that the offline computation only needs to be done once, irrespective of the setpoint or trajectory to be stabilized. This is possible by computing parameterized terminal ingredients and approximating the nonlinear system locally as a quasi-LPV system, with the reference trajectory to be stabilized as the parameter. Furthermore, we have shown that the reference generic offline computation enables us to design nonlinear MPC schemes that ensure optimal periodic operation despite online changing operation conditions. We have demonstrated the applicability and advantages of the proposed procedure with numerical examples.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The extension of the proposed procedure to large scale nonlinear distributed systems using a seperable formulation is part of future work.
