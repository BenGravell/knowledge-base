<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments

Topics include Model predictive control, Predictive control, Motion planning, Robotics, Safety, Robustness, Deep learning, Optimization, Planning, Control, Learning, DRO, Conditional value at risk.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safety is a core challenge of autonomous robot motion planning, especially in the presence of dynamic and uncertain obstacles. Many recent results use learning and deep learning-based motion planners and prediction modules to predict multiple possible obstacle trajectories and generate obstacle-aware ego robot plans. However, planners that ignore the inherent uncertainties in such predictions incur collision risks and lack formal safety guarantees. In this paper, we present a computationally efficient safety filtering solution to reduce the collision risk of ego robot motion plans using multiple samples of obstacle trajectory predictions. The proposed approach reformulates the collision avoidance problem by computing safe halfspaces based on obstacle sample trajectories using distributionally robust optimization (DRO) techniques. The safe halfspaces are used in a model predictive control (MPC)-like safety filter to apply corrections to the reference ego trajectory thereby promoting safer planning. The efficacy and computational efficiency of our approach are demonstrated through numerical simulations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robots have many application areas including autonomous driving, warehouse management and logistics, drone delivery, and agriculture. A core challenge facing autonomous robots is navigation in dynamic and uncertain environments, i.e. in the presence of moving obstacles whose future motion cannot be predicted exactly. This scenario complicates the robot safety requirements: the ego robot must presume the dynamic obstacles' intentions and predict their future trajectories for use in computing its own motion plan. Thus, safety hinges on how accurately the dynamic obstacles' behavior can be predicted. Failing to account for prediction uncertainties may incur undue risk of severe collisions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Various methods have been studied for predicting how obstacles will behave, but it is still an active area of research. In, a hidden Markov model is used for better understanding urban scenarios for autonomous vehicles (AVs). In another work, uses a support vector machine and Bayesian filtering to predict lane change intentions for AVs. Furthermore, deep learning approaches have also been used. End-to-end motion planners, such as, implicitly account for future predictions, but they fail to explicitly capture the environment uncertainties which may lead to collisions. FIERY generates a birds-eye-view probabilistic future predictions map which estimates environmental uncertainties, but it still requires a formal approach to use this data to enforce safety. In, a neural network ensemble is employed to estimate prediction uncertainty and identify rare cases. However, ensembles are resource-intensive to train and deploy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based methods are commonly used to formally guarantee safety requirements. For obstacle motion with additive noise, proposes a solution that uses noise samples to create an empirical distribution. It then formulates a *distributionally robust optimization* (DRO) problem to ensure safety and avoid collisions under any distribution that is "close" to the empirical one. However, this method solves a non-convex problem which is computationally demanding and not suitable for real-time operation. Another recent solution uses conformal prediction to guarantee safety when using learning-based planners. Here, prediction regions that satisfy a given probability bound are found and used in an MPC optimization problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A related approach to enforcing safety uses a *safety filter*. Instead of adding constraints to one of the modules of the autonomy stack, a standalone module takes the reference trajectory from the motion planner and outputs a corrected *filtered* trajectory, as illustrated in Figure 1. The filtered motion plan is guaranteed to satisfy certain safety requirements. Safety filters have been used in *deterministic* settings for autonomous racing, multi-agent motion planning, and autonomous driving to filter unsafe learning-based motion plans.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planners with prediction uncertainty often suffer from two issues. 1) They consider average behavior or limit the chance of unsafe events. These are suitable for real-time deployment but fail under edge cases (in the prediction distribution tail). 2) They rigorously tackle uncertainties and edge cases, but they are computationally intensive. In this work, we address this gap by proposing a computationally efficient solution using axiomatic risk theory to handle uncertainties and deal with edge cases. We assume that the ego robot has a planned reference trajectory and samples of the obstacles' future trajectories (e.g. through). Our solution starts by finding safe halfspaces based on a distributionally robust conditional value-at-risk (${DR} - {CVaR}$) risk metric for each obstacle. Then, the ${DR} - {CVaR}$ safe halfspaces are used in an MPC-based safety filter to enforce safety. The main contributions of this work are: We extend the notion of a safe halfspace and define data-driven ${DR} - {CVaR}$ safe halfspaces that bound the risk of violating a safety specification.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We verify the efficiency of the ${DR} - {CVaR}$ halfspaces through a numerical analysis and show that they can be computed in a few milliseconds with up to a few hundred samples.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We formulate an MPC-based safety filter that uses the ${DR} - {CVaR}$ safe halfspaces to constrain the motion planning problem and bound collision risks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the efficacy of our solution and its ability to handle edge-cases through numerical simulations in a variety of motion planning scenarios.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Motion Planning Safety Filtering Problem", "weight": 1.0} -->

We consider the problem of motion planning for an ego robot in the presence of $N_{ob}$ dynamic obstacles whose future behavior is uncertain. The ego robot dynamics are assumed linear and described: where $x_{t} \in {\mathbb{R}}^{n}$ is the robot state at time $t$, $u_{t} \in {\mathbb{R}}^{m}$ is the control, ${A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times m}}$ are the state and input matrices, $y \in {\mathbb{R}}^{d}$ is the position, and $C \in {\mathbb{R}}^{d \times n}$ is the matrix that extracts the position from the state. For simplicity, we consider 2D position ($d = 2$), but the results can be easily extended to 3D. The ego robot geometry is assumed to be a convex and compact set denoted by $\mathcal{A}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Motion Planning Safety Filtering Problem", "weight": 1.0} -->

We also assume that the ego robot has a desired reference trajectory over a horizon of length $T$ given by ${\mathcal{T}^{r}{(t)}}:={\{{x^{r}{(t)}},\ldots,{x^{r}{({t + T})}}\}}$. This reference trajectory may be obtained from any planning module (e.g. neural network, sampling-based or optimization-based methods, etc.).

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Motion Planning Safety Filtering Problem", "weight": 1.0} -->

Each obstacle is modeled as a convex and compact set $\mathcal{O}_{i}\forall i \in {\lbrack 1:N_{ob}\rbrack}$. Their dynamics are unknown and the motion is uncertain. Furthermore, the prediction distribution is inherently unknown. Instead, we assume access to a module that can generate *sample predictions* of the obstacles' trajectories. The $s$-th sample trajectory of the $i$-th obstacle for a horizon of $T$ time steps is given by ${\mathcal{T}_{i}^{s}{(t)}}:={\{{p_{i}^{s}{(t)}},\ldots,{p_{i}^{s}{({t + T})}}\}}$ and includes only position information ($p_{i}^{s} \in {\mathbb{R}}^{d}$).

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Motion Planning Safety Filtering Problem", "weight": 1.0} -->

An autonomy stack may pass the reference trajectory directly to a tracking controller (Figure 1 faded red arrow) while assuming that it accounts for the obstacles' future trajectories. However, safety requirements desired in a reference trajectory may not be guaranteed, especially if the planner is based on a neural network. A formal safety guarantee is defined as follows.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem 1 (Motion Planning Safety Filtering)", "weight": 1.0} -->

Given an ego reference trajectory $\mathcal{T}^{r}{(t)}$ and obstacle trajectory samples $\mathcal{T}_{i}^{s}{(t)},s \in {\lbrack 1:N_{s}\rbrack}$ for every obstacle $i \in {\lbrack 1:N_{ob}\rbrack}$, find a filtered ego trajectory that ensures the safety of the ego robot per Definition 1. ‣ II-A Motion Planning Safety Filtering Problem ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments").

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem 1 (Motion Planning Safety Filtering)", "weight": 1.0} -->

We now proceed with specifying the adopted risk metric $\mathcal{R}$ for the motion planning problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Signed Collision Loss Function", "weight": 1.0} -->

Consider an ego robot and a single dynamic obstacle. The position of the ego robot is denoted by $y$, the ego reference position is denoted by $y^{r}$, and the obstacle position is denoted by $p$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Signed Collision Loss Function", "weight": 1.0} -->

The deterministic collision avoidance condition is given by ${{({y \oplus \mathcal{A}})} \cap {({p \oplus \mathcal{O}})}} = \varnothing$. Using computational geometry arguments and convexifying the constraint via a separating hyperplane, as in \[16, III-A.2\], we have: where $z$ is any chosen unit vector per.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Signed Collision Loss Function", "weight": 1.0} -->

The constraint is sufficient for ensuring collision avoidance for a deterministic system. Additionally, we can define a deterministic *safe halfspace* such that if $y \in \mathcal{H}$, then $y$ is collision free and satisfies. For the deterministic case, the parameters $h,g$ of $\mathcal{H}$ can be directly mapped to the values. Furthermore, using $\mathcal{H}$ we can define a signed distance function that quantifies the violation or satisfaction amount of a point relative to the collision avoidance constraint. In particular, consider the following loss function: For an obstacle position $p$, if ${\ell{(p)}} \geq 0$ then $p$ intrudes into the safe halfspace $\mathcal{H}$ and $\ell{(p)}$ is the intrusion amount. Otherwise, the obstacle is $|{\ell{(p)}}|$ units away from the boundary of the safe halfspace.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Collision Avoidance using DR-CVaR Safe Halfspaces", "weight": 1.0} -->

When the obstacle position is a random variable $\mathbf{p}$, is ill-posed and the loss becomes a random variable $\ell{({\mathbf{p}})}$. We now define a risk-based safe halfspace with respect to a risk metric $\mathcal{R}$ applied to $\ell{({\mathbf{p}})}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider an ego reference position $y^{r} = {\lbrack{- 0.9},{- 0.8}\rbrack}^{\top}$ and a nominal obstacle at $p = {\lbrack 0.5,0\rbrack}^{\top}$ both of radius $r = 0.3$. Figure 2 illustrates safe halfspaces using the expected value (mean), $CVaR$ and ${DR} - {CVaR}$ risk metrics with $h = {{({p - y^{r}})}/\left. \parallel{p - y^{r}}\parallel \right.}$ as depicted by the arrow. The halfspaces use 100 samples of the obstacle position sampled from the Gaussian random vector $\mathcal{N}{(p,{diag{(0.01,0.01)}})}$ where $diag{( \cdot )}$ is the diagonal matrix.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1", "weight": 1.0} -->

We use $\alpha = 0.2$, $\delta = 0.1$, and $\epsilon \in {\{ 0.05,0.1,0.2\}}$. As $\epsilon$ increases, the Wasserstein ball becomes larger, including more distributions, and hence the ${DR} - {CVaR}$ halfspaces become more conservative. When $\epsilon\rightarrow 0$, the ${DR} - {CVaR}$ safe halfspace converges to the $CVaR$ case. Here, $y^{r}$ is safe with respect to all halfspaces except the ${DR} - {CVaR}$ with $\epsilon = 0.2$. Note that increasing $\delta$ relaxes the safety constraint and would make the halfspaces less conservative.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-D DR-CVaR Safe Halfspace Guarantees", "weight": 1.0} -->

If the position of the ego robot is constrained to the DR-CVaR safe halfspaces, we obtain a safety guarantee that bounds collision risk, however, we require a technical assumption on the lightness of the tails^11^1This assumption hold trivially if $\Xi$ is compact. Since the distribution in our case represents the position of the obstacle, then $\Xi$ is compact as obstacles can always be limited to a finite detection range. for the underlying true probability distribution ${\mathbb{P}}_{true}$ of predicted obstacle positions. Thus, we have the following lemma.

<!-- chunk {"id": "body-0024", "role": "body", "section": "MPC-Based Safety Filter with DR-CVaR Safe Halfspaces", "weight": 1.0} -->

We now return to the safe motion planning problem described in Problem 1. ‣ II-A Motion Planning Safety Filtering Problem ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments"). Our solution has two steps: Computing the safe halfspaces: We interpret the safety constraint ${\mathcal{R}{(\mathcal{T}^{r})}} \leq \delta$ from Definition 1. ‣ II-A Motion Planning Safety Filtering Problem ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments") point-wise in time and per obstacle. Thus, the obstacle trajectory samples are used to solve (5.

<!-- chunk {"id": "body-0025", "role": "body", "section": "MPC-Based Safety Filter with DR-CVaR Safe Halfspaces", "weight": 1.0} -->

‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) per obstacle per time step over the horizon $T$ resulting in $\mathcal{H}_{i}^{dr}{(t + t')}\forall i \in {\lbrack 1:N_{ob}\rbrack},t' \in {\lbrack 1:T\rbrack}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "MPC-Based Safety Filter with DR-CVaR Safe Halfspaces", "weight": 1.0} -->

MPC Filter: The computed halfspaces are used as constraints in an MPC optimization problem that computes a minimally deviating trajectory from the reference trajectory. The MPC optimization problem is formalized below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 2 (MPC-Based Safety Filter)", "weight": 1.0} -->

Given an ego reference trajectory $\mathcal{T}^{r}{(t_{0})}$ at time $t_{0}$ and linear ego vehicle dynamics, find the filtered trajectory ${\mathcal{T}{(t_{0})}} = {\{{x{(t_{0})}},\ldots,{x{({t_{0} + T})}}\}}$ for the ego vehicle that satisfies the ${DR} - {CVaR}$ safe halfspaces $\mathcal{H}_{i}^{dr}{(t)},t \in {\lbrack t_{0} + 1:t_{0} + T\rbrack}$, by solving the finite-horizon optimization problem (11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) with the objective function (10.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 2 (MPC-Based Safety Filter)", "weight": 1.0} -->

‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")). with $\forall t \in {\lbrack t_{0} + 1:t_{0} + T\rbrack}$. Here, ${\mathcal{Y}{(t)}} \subseteq {\mathbb{R}}^{d}$ is a convex position constraint for the ego robot (e.g. environment bounds), ${\mathcal{U}{(t)}} \subseteq {\mathbb{R}}^{m}$ is the convex control input constraint set, and $R \in {\mathbb{R}}^{n \times n}$, $Q \in {\mathbb{R}}^{m \times m}$ are symmetric, positive semidefinite cost matrices.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 2 (MPC-Based Safety Filter)", "weight": 1.0} -->

The MPC safety filter 11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments") is a quadratic program (QP) and can be modeled with tools such as CVXPY and solved with many solvers, such as ECOS.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We assume that (11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) is always feasible at $t = 0$. The conjunction in (11d. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) may become empty or unreachable due to $\mathcal{U}{(t)}$ rendering the problem infeasible. In this work, we use the most recent optimal control $u^{\ast}{(t)}$ from solving (11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) and proceed with the next available control, $u^{\ast}{({t + 1})}$, until the problem is solved again or we run out ($u^{\ast}{({{t + T} - 1})}$).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Future works will address alternative infeasibility handling approaches.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We analyze the ${DR} - {CVaR}$ safe halfspace computation time and perform numerical simulations. All experiments use CVXPY with ECOS and were executed on a Dell Precision 7520 computer with an Intel Xeon E3-1535M v6 CPU and 32GB RAM. Experiment code can be found: Figure 3: DR − CVaR safe halfspace computation time TABLE I: CVaR and DR − CVaR safe halfspace average Solve and Call times (ms).

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Computation Cost Analysis", "weight": 1.0} -->

We perform a numerical analysis for the ${DR} - {CVaR}$ safe halfspace computation time. We find the safe halfspaces as done in Example 1 for various number of samples $N_{s}$. For each $N_{s}$, (5. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) is solved 500 times with different random samples. We report three times: 1) the CVXPY reported setup time (Setup Time), 2) the CVXPY reported solver solve time (Solve Time), and 3) the time for executing the CVXPY solve method (Call Time). The results, in milliseconds, are reported in Figure 3. Since (5.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Computation Cost Analysis", "weight": 1.0} -->

‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) is a linear program (LP), it can be solved efficiently within a few milliseconds even for a few hundred samples. The Call Time includes a large overhead not captured by the Setup Time. Additionally, we compare the mean times for finding the ${DR} - {CVaR}$ and $CVaR$ safe halfspaces in Table I. This reveals that while the Solve Time is only about 50% higher for the ${DR} - {CVaR}$ problem, the Call Time grows quickly compared to $CVaR$. We conclude that the ${DR} - {CVaR}$ safe halfspace formulation is suitable for real-time operation especially if a solver is used directly.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B1 Simulation Setup", "weight": 1.0} -->

We model the ego and obstacle geometries as circles of radii $r_{\mathcal{A}} = r_{\mathcal{O}} = 0.3$. The ego robot uses double integrator dynamics with ${{A = \begin{bmatrix} \end{bmatrix}},{B = \begin{bmatrix} \end{bmatrix}}},$ and $C = \begin{bmatrix} \end{bmatrix}$ where $T_{s} = 0.2$sec is the discrete time step. The reference trajectory is generated using an obstacle-agnostic MPC-based motion planner with a target goal state. Its details are not discussed since our safety filter is agnostic to the chosen motion planning algorithm. Unbeknown to the ego robot, the obstacles are single integrators with ${A = I_{2}},{{B = {I_{2}T_{s}}},{C = I_{2}}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B1 Simulation Setup", "weight": 1.0} -->

Sample trajectories are generated by adding a Gaussian random noise $\mathcal{N}{(\mathbb{0}_{2},{diag{(0.01,0.01)}})}$ to a nominal trajectory that keeps the vehicle aligned with the x-axis at a desired speed. However, when realizing the true position of the obstacle, a Laplace distribution with the same mean and covariance as the Gaussian is sampled. We use $T = 10$, $\alpha = 0.2$, $\delta = 0.1$, and $\epsilon = 0.05$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B2 Filtering in Different Scenarios", "weight": 1.0} -->

We use three types of reach-avoid motion planning scenarios: 1) Head-on collision, 2) Overtaking, and 3) Intersection. The left column of Figure 4 overlays the trajectories of one experiment using safe halfspaces based on the mean value, $CVaR$, and ${DR} - {CVaR}$ risk metrics. In all three cases, trajectories using ${DR} - {CVaR}$ safe halfspaces achieve the lowest risk, while those using the expected value-based safe halfspace have the highest risk.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B2 Filtering in Different Scenarios", "weight": 1.0} -->

To demonstrate the advantage of using ${DR} - {CVaR}$ halfspaces, we perform a Monte Carlo simulation repeating each experiment 300 times. The distance to collision $\left. \parallel{y - p}\parallel \right. - r_{\mathcal{A}} - r_{\mathcal{O}}$ is plotted in the right column of Figures 4 with the last row showing a box plot zoomed-in view. Clearly, the performance using safe halfspaces based on the mean value result in more frequent collisions in all three cases. In the box plot, the worst-case scenario using the mean value safe halfspace is around $- 0.45$. With this collision amount, both the ego robot and obstacle would be significantly damaged. The worst-case collision using $CVaR$ results in a $- 0.22$ distance to collision. Here, it may lead to a less severe collision. On the other had, in all three cases, the ${DR} - {CVaR}$ safe halfspace-based formulations avoid collisions with the ego vehicle, avoiding the obstacle even in the worst case scenario.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B2 Filtering in Different Scenarios", "weight": 1.0} -->

Thus, our proposed solution can secure the robot's safety and systematically reduce collision risks, even with edge cases in the prediction distribution tail.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B3 Safety Filtering With Multiple Obstacles", "weight": 1.0} -->

Consider the motion planning problem in Figure 5, where the ego robot must avoid 3 obstacles. Figure 5 plots the overall trajectories as well as the ${DR} - {CVaR}$ safe halfspaces (green polytopes). Since the MPC safety filter is a QP, it can be solved efficiently in a few milliseconds. Here, the filter call time takes 7ms on average. The safety filter becomes infeasible only once, so we fall back to the previously computed set of optimal controls. This is illustrated at time step 5 when the ego robot is not inside any of the green safe polytopes. Throughout the experiment, the robot remains sufficiently far away from the obstacles and successfully reaches its goal.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work we presented a solution that improves a robot's safety when operating in a dynamic environment with prediction uncertainties. We posed a DRO problem that computes ${DR} - {CVaR}$ safe halfspaces that bound the $CVaR$ of a signed collision distance under any distribution close the empirical one based on data. These halfspaces are then used as linear constraints in an MPC safety filter that corrects the ego reference trajectory. We performed a numerical analysis on the ${DR} - {CVaR}$ safe halfspaces and demonstrated that 1) they can be computed in milliseconds, and 2) they can improve safety in edge cases. Future directions include a better approach to handling MPC infeasibilities, relaxations of the halfspaces to trade-off safety for performance, and an implementation of the approach on physical hardware.
