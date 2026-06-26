<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-Averse Trajectory Optimization via Sample Average Approximation

Topics include Trajectory optimization, Robotics, Uncertainty, Online algorithms, Optimization, Planning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization under uncertainty underpins a wide range of applications in robotics. However, existing methods are limited in terms of reasoning about sources of epistemic and aleatoric uncertainty, space and time correlations, nonlinear dynamics, and non-convex constraints. In this work, we first introduce a continuous-time planning formulation with an average-value-at-risk constraint over the entire planning horizon. Then, we propose a sample-based approximation that unlocks an efficient and general-purpose algorithm for risk-averse trajectory optimization. We prove that the method is asymptotically optimal and derive finite-sample error bounds. Simulations demonstrate the high speed and reliability of the approach on problems with stochasticity in nonlinear dynamics, obstacle fields, interactions, and terrain parameters.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accounting for uncertainty in the design of decision-making systems is key to achieving reliable robotics autonomy. Indeed, modern autonomy stacks account for uncertainty, whether it comes from noisy sensor measurements (e.g., due to perceptually-degraded conditions or a lack of features ), dynamics (e.g., due to disturbances and difficult-to-characterize nonlinearities ), properties of the environment (e.g., due to unknown terrain properties for legged robots and Mars rovers ), or interactions with other agents (e.g., in autonomous driving ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although trajectory optimization under uncertainty underpins a wide range of applications, existing approaches often make simplifying assumptions and approximations that reduce the range of problems they can reliably deal. Specifically, there is a lack of methods capable of simultaneously handling sources of aleatoric uncertainty (e.g., external disturbances) and epistemic uncertainty (e.g., a drone transporting a payload of uncertain mass that introduces time correlations over the state trajectory) that depend on state and control variables (e.g., interactions between different agents), uncertainty of arbitrary (non-Gaussian) distribution correlated over time and space (e.g., uncertain terrain properties), uncertain nonlinear dynamics and non-convex constraints, trajectory-wise constraints that bound the risk of constraints violations over the entire duration of the problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As distinct systems may need specific numerical schemes, such methods should also have discretization-independent guarantees. Table I summarizes the capabilities of existing methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce an efficient risk-averse trajectory optimization algorithm satisfying the previous desiderata: First, we propose a risk-averse planning formulation with average-value-at-risk (AV@R) constraints enforced over the entire planning horizon. This formulation is applicable to a wide range of robotics problems with sources of aleatoric and epistemic uncertainty. Its continuous-time nature guides the design of algorithms whose properties are independent of the chosen time discretization scheme (see Remark 2. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")). Enforcing AV@R constraints enables accounting for tail events and facilitates numerical resolution due to their convexity properties (Remark 3. ‣ VII Numerical resolution ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")). In addition, solving this formulation gives feasible solutions to notoriously challenging problems with joint chance constraints (Remark 1). ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, we propose a sample-based approximation rooted in the sample average approximation approach. We derive asymptotic optimality guarantees (Theorem 1. ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")) and finite-sample error bounds (Lemma 1. ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")) for this reformulation. The analysis relies on mild assumptions ((A1) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")-(A4) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")), which enables considering a wide range of uncertainty sources that introduce spatial and temporal correlations and depend on state and control variables. The resulting approximated problem is smooth and sparse, facilitating efficient numerical resolution using off-the-shelf optimization tools.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we show the reliability and speed of the proposed approach on problems with uncertain nonlinear dynamics, obstacle fields, interactions, and terrain parameters.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work indicates that risk-averse planning problems can be efficiently tackled via trajectory optimization. These findings challenge the popular belief that Monte-Carlo-based planning methods are computationally expensive. The key is a particular AV@R-constrained formulation which, when coupled with a sample-based approximation and a smooth, sparse reformulation, unlocks the use of readily available optimization tools that enable efficient numerical resolution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Risk functions", "weight": 1.0} -->

Let $(\Omega,\mathcal{G},{\mathbb{P}})$ be a probability space and $Z:{\Omega\rightarrow{\mathbb{R}}}$ be a random variable encoding constraints of the form $Z \leq 0$. For instance, $Z$ may denote the minimum negative distance to obstacles and $Z \leq 0$ may denote obstacle avoidance constraints, see Figure 1. In practice, enforcing constraints with $\mathbb{P}$-probability one (i.e., ${Z{(\omega)}} \leq 0$ for $\mathbb{P}$-almost all $\omega \in \Omega$) is infeasible, e.g., if disturbances are Gaussian-distributed and have unbounded support. Thus, we may enforce risk constraints instead.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Risk functions", "weight": 1.0} -->

We define the Value-at-Risk (V@R) and Average Value-at-Risk (AV@R)^11^1The AV@R is also often referred to as the Conditional Value-at-Risk (CV@R) in the literature, since ${\text{AV@R}_{\alpha}{(Z)}} = {{\mathbb{E}}{\lbrack{\left. Z \middle| Z \right. \geq {\text{V@R}_{\alpha}{(Z)}}}\rbrack}}$ under certain regularity assumptions \[54, Theorem 6.2\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Risk functions", "weight": 1.0} -->

at risk level $\alpha \in {}$ as $\text{V@R}_{\alpha}{(Z)}$ is the $({1 - \alpha})$-quantile of $Z$ ($Z > {\text{V@R}_{\alpha}{(Z)}}$ with probability less than $\alpha$) and $\text{AV@R}_{\alpha}{(Z)}$ is the expected value of values of $Z$ larger than $\text{V@R}_{\alpha}{(Z)}$ \[54, Theorem 6.2\]. These risk functions yield two types of inequality constraints.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

This formulation of OCP captures a broad range of robotics applications, see Section VIII for examples. OCP is challenging to solve due to the non-convexity of $G$, the AV@R risk constraint (5b), the non-Gaussianity of the state trajectory $x_{u}$, and the dependency of all quantities on both epistemic uncertainty (modeled by the uncertain parameters $\xi$) and aleatoric uncertainty (modeled with the SDE in (5d)).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

By, the AV@R constraint (5b) in OCP is equivalent to so all constraints in OCP are expected value constraints. Thus, solving OCP amounts to evaluating expectations, which is generally challenging as it involves a nonlinear SDE and general nonlinear constraints functions. We propose a tractable approximation in Section V ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation"). Next, we discuss important considerations motivating this formulation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 1 (joint chance constraints (CCs))", "weight": 1.0} -->

Solving OCP yields feasible solutions to problems with joint CCs. Indeed, given a constraint ${G{({x_{u}{(t)}},\xi)}} \leq \, 0$ that should hold at all times jointly with high probability $1 - \alpha$, we can define the joint CC Thanks to and, a conservative formulation of the joint CC. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")) is the corresponding constraint (5b) in OCP. Thus, by appropriately defining $G$ and solving OCP, constraints that often appear in robotics can be enforced with high probability over the entire state trajectory, see Section VIII.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 2 (pointwise-in-time risk constraints)", "weight": 1.0} -->

instead (e.g., as in ) does not bound the risk of constraints violation over the entire trajectory. Similarly, pointwise-in-time chance constraints (e.g., as in ) do not bound the probability of constraints violations over the entire planning horizon. Further, transposing discrete-time risk-averse control strategies to full-horizon settings via Boole's inequality may lead to infeasibility as the resolution of the time discretization increases, see for further discussion. Placing the time-wise supremum inside the AV@R constraint (5b) and accounting for time correlations is key to obtaining trajectory-wise constraints satisfaction guarantees.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 1 (obstacle avoidance constraints)", "weight": 1.0} -->

For example, spherical obstacles at $o_{j}$ of radii $r_{j}$ can be described by ${d_{\mathcal{O}_{j}}{(x)}} = {{\|{x - o_{j}}\|} - r_{j}}$. The fact that $d_{\mathcal{O}_{j}}$ depends on randomness $\omega \in \Omega$ via the uncertain parameters $\xi{(\omega)}$ allows capturing obstacles of uncertain position and shape. For example, ellipsoidal obstacles centered at $o_{j}$ of shape matrices $Q_{j}$ can be encoded by the SDFs Collision avoidance joint CCs can be written as By defining the $N$ constraints function $G_{j} = {- d_{\mathcal{O}_{j}}}$, so that the obstacle avoidance joint CC (10. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")) is equivalent to.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1 (obstacle avoidance constraints)", "weight": 1.0} -->

‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")). Thus, by Remark 1). ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation"), a conservative reformulation of (10.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Sample average approximation (SAA)", "weight": 1.0} -->

$\delta_{M} > 0$ is a padding constant that decreases as the number of samples $M$ increases (in practice, we set $\delta_{M}$ to a small value, see Theorem 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sample average approximation (SAA)", "weight": 1.0} -->

‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")). This approximation is inspired from the sample average approximation (SAA) method, which was recently extended to problems with equality constraints that often appear in robotics applications. To the best of our knowledge, this approximation has not been applied to continuous-time problems taking the form of OCP.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sample average approximation (SAA)", "weight": 1.0} -->

Given $M$ samples $\omega^{i} \in \Omega$ of the uncertainty, which define $M$ sample paths of the Brownian motion $W{(\omega^{i})}$, of the uncertain parameters $\xi{(\omega^{i})}$, and of the initial conditions $x_{0}{(\omega^{i})}$, the approximation $\text{𝐒𝐎𝐂𝐏}_{M}{(\overline{\omega})}$ is a tractable deterministic trajectory optimization problem, see Section VII. In the next section, we study the theoretical properties of this approach.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Depending on the samples $\omega^{i}$, the computed control trajectories $u_{M}{(\overline{\omega})}$ that solve $\text{𝐒𝐎𝐂𝐏}_{M}{(\overline{\omega})}$ will be different. What can we say about the quality of these solutions? We provide analysis that relies on the following mild assumptions.: The drift and diffusion coefficients $b$ and $\sigma$ are continuous.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

there is a bounded constant $L \geq 0$ such that for all ${x,y} \in {\mathbb{R}}^{n}$, all ${u,v} \in U$, and all values $\xi \in {\mathbb{R}}^{q}$,: The control space $\mathcal{U} \subset {L^{2}{({\lbrack 0,T\rbrack},U)}}$ can be identified with a compact subset of ${\mathbb{R}}^{z}$ for some $z \in {\mathbb{N}}$.: The uncertain initial state $x_{0}$ and parameters $\xi$ are $\mathcal{F}_{0}$-measurable and square-integrable.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

(A1) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") is standard and guarantees the existence and uniqueness of solutions to (SDE). (A2) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") corresponds to standard smoothness assumptions of the cost and constraints functions. The constraints functions $G$ and $H$ can always be composed with a smooth cut-off function whose support contains the statespace of interest to ensure the satisfaction of the boundedness condition in (A2) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation"). (A3) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") states that the control space $\mathcal{U}$ is finite-dimensional, which is an assumption that is satisfied in practical applications once a numerical resolution scheme is selected. In particular, (A3) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") holds for the space of stepwise-constant control inputs $\mathcal{U} = {}$ that we use in this work.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

(A4) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") makes rigorous the interpretation of $x_{0}$ and $\xi$ as sources of epistemic uncertainty: (A4) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") states that the uncertain initial state $x_{0}$ and parameters $\xi$ are randomized at the beginning of the episode and are independent of the Brownian motion $W$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

To describe the distance between solutions to $\text{𝐒𝐎𝐂𝐏}_{M}$ and to OCP, given non-empty compact sets ${A,B} \subseteq \mathcal{U}$, we define As defined above, $\mathbb{D}$ satisfies the property that $A \subseteq B$ if ${{\mathbb{D}}{(A,B)}} = 0$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Thus, if we show that the solution sets $S_{M}{(\overline{\omega})}$ and $S$ of $\text{𝐒𝐎𝐂𝐏}_{M}{(\overline{\omega})}$ of OCP satisfy ${{\mathbb{D}}{({S_{M}{(\overline{\omega})}},S)}} = 0$, then we can conclude that ${S_{M}{(\overline{\omega})}} \subseteq S$, i.e., any optimal solution of $\text{𝐒𝐎𝐂𝐏}_{M}{(\overline{\omega})}$ is an optimal solution of the original problem OCP. Theorem 1. ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") below states that this result holds with probability one in the limit as the sample size $M$ increases.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical resolution", "weight": 1.0} -->

Theorem 1. ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") justifies approximating OCP using samples $\omega^{i}$ and searching for solutions to the deterministic relaxation $\text{𝐒𝐎𝐂𝐏}_{M}{(\overline{\omega})}$ instead. In this section, we describe a numerical method for efficiently computing solutions to $\text{𝐒𝐎𝐂𝐏}_{M}{(\overline{\omega})}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical resolution", "weight": 1.0} -->

Control space parameterization: We optimize over open-loop controls $u$ parameterized by $S \in {\mathbb{N}}$ stepwise-constant inputs $u_{s}$ of duration ${\Delta t} = {T/S}$, described by the set This set $\mathcal{U}$ clearly satisfies (A3) ‣ VI Theoretical analysis ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation"), since it can be identified with a compact set of ${\mathbb{R}}^{Sm}$. Note that any square-integrable open-loop control $u$ can be approximated arbitrarily well by some $u \in \mathcal{U}$ by increasing $S$, so this class of function is expressive.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical resolution", "weight": 1.0} -->

Alternatively, one could also optimize over certain classes of closed-loop controllers (e.g., controls of the form $u = {\overline{u} + {Kx}}$); an approach that is common in the literature.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Numerical resolution", "weight": 1.0} -->

The SDE constraint (19f) can be either explicitly enforced by optimizing over both state variables $x_{u}^{i}{({k\Delta t})}$ and control variables $u{({k\Delta t})}$ and enforcing (19f), or implicitely by only optimizing over the control variables $u{({k\Delta t})}$ that parameterize the state trajectory via (19f). In this work, we opt for the latter as it reduces the number of variables, albeit at a potential reduction in numerical stability. As shown, the alternative option of parameterizing both state particles and control variables could also be computationally efficient.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical resolution", "weight": 1.0} -->

By introducing $M$ additional variables $y_{i} \in {\mathbb{R}}$, the inequality constraints (19d) are equivalent to the set of the constraints Note that these constraints are smooth if every $G_{j}$ is smooth.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical resolution", "weight": 1.0} -->

Numerical resolution: With this reformulation, $\hat{\text{𝐒𝐎𝐂𝐏}}$ can be solved using reliable off-the-shelf optimization tools such as IPOPT. In this work, we leverage sequential convex programming (SCP). SCP consists of solving a sequence of convex approximations of $\hat{\text{𝐒𝐎𝐂𝐏}}$ until convergence. The main appeal in using SCP is that it typically only requires a few convex approximations of the original non-convex program to reach accurate solutions. Since the set of constraints is sparse, the convex approximations of $\hat{\text{𝐒𝐎𝐂𝐏}}$ can be efficiently solved. In contrast, interior-point-methods for non-convex programming may take a larger number of small steps that each require evaluating gradients and hessians of the original program. Since this gradient-hessian evaluation is potentially the computational bottleneck in solving $\hat{\text{𝐒𝐎𝐂𝐏}}$, SCP is a promising solution scheme for this class of problems. See for further details on SCP for trajectory optimization.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3 (AV@R vs chance constraints)", "weight": 1.0} -->

Beyond the ability to account for tail events, the smoothness of the reformulation in motivates enforcing AV@R constraints instead of chance constraints that are often used in the literature. Indeed, a typical chance constraint ${{\mathbb{P}}{({{\sup_{t}{G{({x_{u}{(t)}},\xi)}}} > 0})}} \leq \alpha$ is equivalently written as ${{\mathbb{E}}{\lbrack{\mathbf{1}_{(0,\infty)}{({\sup_{t}{G{({x_{u}{(t)}},\xi)}}})}}\rbrack}} \leq \alpha$, where ${\mathbf{1}_{(0,\infty)}{(z)}} = 1$ if $z > 0$ and $0$ otherwise. This constraint only takes a simple form in particular cases.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 3 (AV@R vs chance constraints)", "weight": 1.0} -->

Approximating this chance constraint from samples would give which is not smooth since $\mathbf{1}_{(0,\infty)}{(\cdot)}$ is a step function. To solve the resulting problem with gradient-based methods, one would need to formulate and solve smooth approximations instead, or solve the problem multiple times with different constraints paddings, which is computationally expensive. In contrast, the reformulation in is smooth and exact (up to errors from the sample-based and discrete-time approximations), which allows efficient numerical resolution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3 (AV@R vs chance constraints)", "weight": 1.0} -->

Example 1. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation") (obstacle avoidance constraints). With $M$ samples of the state trajectory $x_{u}^{i}$ and of the obstacles $\mathcal{O}_{j}{(\xi^{i})}$, the AV@R constraint in (12. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")) can be approximated with the set of constraints with ${G_{j}{({x_{u}^{i}{({k\Delta t})}},\xi^{i})}} = {- {d_{\mathcal{O}_{j}{(\xi^{i})}}{({x_{u}^{i}{({k\Delta t})}})}}}$. This formulation applies to general obstacle representations and can be specialized to particular obstacle shapes.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3 (AV@R vs chance constraints)", "weight": 1.0} -->

For example, if the $N$ uncertain obstacles $\mathcal{O}_{j}$ are spheres of uncertain radii $r_{j}$ and centers $o_{j}$, then the last term in is for all $i,j,k$, where ${(r_{j}^{i},o_{j}^{i})} = {{(r_{j},o_{j})}{(\omega^{i})}}$ are $M$ iid samples. If the obstacles are ellipsoidal as in (9. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")), then becomes for all $i,j,k$. This gives a set of differentiable constraints that can be passed to a non-convex optimization algorithm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3 (AV@R vs chance constraints)", "weight": 1.0} -->

We note that potential corner-cutting due to the time discretization of the AV@R constraint is easily addressed via different methods, e.g., with the approach, by enforcing (19d) on a finer grid, or by padding obstacles.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Applications and results", "weight": 1.0} -->

We apply the proposed approach to three challenging planning problems with diverse sources of uncertainty. Code is available.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Applications and results", "weight": 1.0} -->

1\) Drone planning with uncertain obstacles. The state is $x = {(p,\overset{˙}{p})} \in {\mathbb{R}}^{6}$, the input is $u \in {\mathbb{R}}^{3}$. Dynamics are given by and ${\sigma{(x,u,\omega)}} = {\frac{1}{m{(\omega)}}{(0_{3 \times 3},{\beta_{\sigma}I_{3 \times 3}})}^{\top}}$. The drone transports an uncertain payload, modeled by assuming that the total mass $m$ of the system follows a uniform distribution. $(\beta_{\text{drag}},\beta_{\sigma})$ are drag and diffusion coefficients and $K$ is a feedback gain. We consider three uncertain ellipsoidal obstacles whose shape matrices have uncertain axes distributed according to a uniform distribution, and enforce collision avoidance constraints as described in Example 1. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation").

<!-- chunk {"id": "body-0041", "role": "body", "section": "Applications and results", "weight": 1.0} -->

The objective is reaching a goal (${H{({x{(T)}})}} = {{x{(T)}} - x_{\text{g}}}$) while minimizing control effort ${\ell{(x,u)}} = {u^{\top}Ru}$ and satisfying collision avoidance constraints at risk level $\alpha$ as in (12. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")). This nonlinear system has sources of aleatoric (disturbances modeled as a Wiener process) and epistemic (mass and obstacles) uncertainty, which makes solving the problem with classical approaches challenging.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Applications and results", "weight": 1.0} -->

We formulate the sample-based approximation with $S = 20$ nodes and solve it with SCP. We present an example of results in Figure 1 ($M = 50$, $\alpha = {10\%}$) with the trajectory samples $x_{u}^{i}$ obtained at convergence. We report the associated Monte-Carlo histogram of the negative minimum distance over $t \in {\lbrack 0,T\rbrack}$ in (11. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")) with the mean, $\text{V@R}_{\alpha}$ and $\text{AV@R}_{\alpha}$ minimum values of (11. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation")). The average-value-at-risk of collision is below $0$, indicating that the solution of SOCP is feasible for OCP.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Applications and results", "weight": 1.0} -->

Sensitivity to risk parameter: We run the approach ($\text{SAA}_{\alpha}$) for different values of $\alpha$ each and report results in Table II. The $\text{AV@R}_{\alpha}$ constraint is approximately satisfied ($\text{AV@R}_{\alpha} \approx 0$) for each value of $\alpha$. As a result, the associated joint chance constraints for collision avoidance are satisfied, since the percentage of constraints violations is always below $\alpha$, validating the discussion in Remark 1). ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation"). Safer behavior is obtained for smaller values of $\alpha$, effectively balancing the tradeoff between the efficiency and the risk of constraints violations.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Applications and results", "weight": 1.0} -->

Comparisons: The proposed approach ($\text{SAA}_{\alpha}$) yields trajectories that closely match desired safety risk levels. In contrast, a baseline that neglects uncertainty (Deterministic) often violates constraints. We also compare with a method (Gaussian$_{\alpha}$) that bounds the total probability of constraints violation below $\alpha$ using Boole's inequality. This baseline uses an approximate Gaussian-distributed state representation and optimizes over the risk allocation, see the appendix for details. Due to the approximate uncertainty representation and the use of Boole's inequality (thus neglecting time and space correlations of uncertainty), this baseline is overly conservative.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Applications and results", "weight": 1.0} -->

Computation time: In Figure 2, we report total computation times for different sample sizes $M \in {\{ 20,30,50\}}$ (we report the median over $30$ runs with $\alpha = {5\%}$, evaluated on a laptop with an i7-10710U CPU (1.10 GHz) and 16 GB of RAM). We use a zero initial guess ${\overline{u}}_{s} = 0$ and stop after $10$ SCP iterations, which is sufficient to obtain a final SCP iteration error ${{\|{u^{k} - u^{k - 1}}\|}/{\| u^{k}\|}} \leq {1\%}$. Albeit our implementation is written in Python (with JAX and OSQP ), computation times are reasonable and amenable to real-time applications. Computation time scales roughly linearly in the sample size. Parallelization on a GPU could enable using a larger sample size $M$ while retaining speed, albeit results show that using a small sample size suffices to obtain feasible solutions.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Applications and results", "weight": 1.0} -->

The objective is reaching a destination $p_{\text{ego}}^{\text{des}}$ (${H{({x{(T)}})}} = {{p_{\text{ego}}{(T)}} - p_{\text{ego}}^{\text{des}}}$) while minimizing control effort ${\ell{(x,u)}} = {u^{\top}Ru}$ and maintaining a minimum separation distance $d_{\text{sep}}$ This constraint is reformulated as described in Example 1. ‣ IV Problem formulation ‣ Risk-Averse Trajectory Optimization via Sample Average Approximation"). The resulting OCP problem combines sources of aleatoric (from the Wiener process disturbances) and epistemic uncertainty (from the pedestrian's uncertain behavior and initial pose).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Applications and results", "weight": 1.0} -->

We discretize the problem with $S = 20$ nodes and report results in Figure 3 and Table II. Reducing the risk parameter $\alpha$ yields safer trajectories that maintain a larger distance with the pedestrian at the expense of greater control effort. For all values of $\alpha$, the AV@R constraints and corresponding joint chance constraints are satisfied. In contrast, the joint-chance-constrained baseline with optimal risk allocation (Gaussian$_{\alpha}$) is overly conservative, whereas a baseline that neglects uncertainty (Deterministic) is unable to maintain a safe separation distance with the pedestrian at all times. Computation times are close to those for the drone planning problem in Figure 2 (see the appendix), again demonstrating the real-time capabilities of the proposed approach.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Applications and results", "weight": 1.0} -->

Characterizing terrain adhesion properties (i.e., terramechanics) is challenging and is often done via data-driven approaches. For instance, Cunningham et al. fit Gaussian processes to observed data for slip prediction. Thus, we model the soil properties at the contact point $p_{\text{foot},x}{(q)}$ given by the system's kinematics with the Random Fourier Features ${\mu{(q,\omega)}} = {\overline{\mu} + {\sum_{n = 1}^{30}{\omega_{n,1}{\cos{({{{\omega_{n,2} \cdot p_{\text{foot},x}}{(q)}} + \omega_{n,3}})}}}}}$ for some Figure 4: Samples from μ. randomized parameters $\omega$ following a uniform distribution, see Figure 4. The coefficient $\mu$ encodes epistemic uncertainty varying over space, which is more realistic than assuming a constant friction coefficient as.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Applications and results", "weight": 1.0} -->

As discussed in Section II, this type of uncertainty is challenging to deal.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Applications and results", "weight": 1.0} -->

The objective consists of jumping as far as possible (i.e., ${\varphi{({x{(T)}})}} = {- {p_{x}{(T)}}}$) while minimizing the control effort ${\ell{(x,u)}} = {\| u\|}_{2}^{2}$ and limiting the risk of slippage (27c). The resulting problem clearly takes the form of OCP with no dynamics uncertainty (i.e., $\sigma = 0$). Indeed, an important source of uncertainty in legged locomotion comes from uncertain terrain properties due to imperfect perception or inherent uncertainty in the problem. We are not aware of prior work in trajectory optimization tackling this formulation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Applications and results", "weight": 1.0} -->

We solve the sampled problems (using $S = M = 30$) with IPOPT and report results in Figure 5. By reducing the risk parameter $\alpha$, the proposed trajectory optimizer is more cautious to avoid slip and returns shorter jumps, with slippage probability bounded by $\alpha$. In contrast, a deterministic baseline that only considers the mean terrain parameter ${\mu{(x,\omega)}} = \overline{\mu}$ returns longer jumps but violates constraints $50\%$ of the time.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed an efficient method for risk-averse trajectory optimization. This algorithm hinges on a continuous-time formulation with average-value-at-risk constraints. By approximating the problem using samples, we obtain a smooth, sparse program that allows for efficient numerical resolution. We demonstrated the speed and reliability of the method on problems with sources of epistemic and aleatoric uncertainty that are challenging to tackle with existing approaches.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Due to its generality in handling uncertain nonlinear dynamics and constraints, this work opens exciting future research directions. In particular, the approach could be interfaced with learned models: obstacles could be implicitly represented as deep SDFs or neural radiance fields, deep trajectory forecasting models could be used for planning in autonomous driving, learned terramechanics models could allow more robust legged locomotion, and dynamics could learned online, either to improve control performance or for active data-gathering under risk constraints.
