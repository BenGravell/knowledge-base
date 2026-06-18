## Introduction

Autonomous robots have many application areas including autonomous driving, warehouse management and logistics, drone delivery, and agriculture. A core challenge facing autonomous robots is navigation in dynamic and uncertain environments, i.e. in the presence of moving obstacles whose future motion cannot be predicted exactly. This scenario complicates the robot safety requirements: the ego robot must presume the dynamic obstacles' intentions and predict their future trajectories for use in computing its own motion plan. Thus, safety hinges on how accurately the dynamic obstacles' behavior can be predicted. Failing to account for prediction uncertainties may incur undue risk of severe collisions.

Various methods have been studied for predicting how obstacles will behave, but it is still an active area of research. In, a hidden Markov model is used for better understanding urban scenarios for autonomous vehicles (AVs). In another work, uses a support vector machine and Bayesian filtering to predict lane change intentions for AVs. Furthermore, deep learning approaches have also been used. End-to-end motion planners, such as, implicitly account for future predictions, but they fail to explicitly capture the environment uncertainties which may lead to collisions. FIERY generates a birds-eye-view probabilistic future predictions map which estimates environmental uncertainties, but it still requires a formal approach to use this data to enforce safety. In, a neural network ensemble is employed to estimate prediction uncertainty and identify rare cases. However, ensembles are resource-intensive to train and deploy.

Figure 1: An autonomy stack with the proposed Safety Filter module. The module intercepts the reference trajectory and corrects it to enforce the safety requirement.

Optimization-based methods are commonly used to formally guarantee safety requirements. For obstacle motion with additive noise, proposes a solution that uses noise samples to create an empirical distribution. It then formulates a *distributionally robust optimization* (DRO) problem to ensure safety and avoid collisions under any distribution that is "close" to the empirical one. However, this method solves a non-convex problem which is computationally demanding and not suitable for real-time operation. Another recent solution uses conformal prediction to guarantee safety when using learning-based planners. Here, prediction regions that satisfy a given probability bound are found and used in an MPC optimization problem.

A related approach to enforcing safety uses a *safety filter*. Instead of adding constraints to one of the modules of the autonomy stack, a standalone module takes the reference trajectory from the motion planner and outputs a corrected *filtered* trajectory, as illustrated in Figure 1. The filtered motion plan is guaranteed to satisfy certain safety requirements. Safety filters have been used in *deterministic* settings for autonomous racing, multi-agent motion planning, and autonomous driving to filter unsafe learning-based motion plans.

Motion planners with prediction uncertainty often suffer from two issues. 1) They consider average behavior or limit the chance of unsafe events. These are suitable for real-time deployment but fail under edge cases (in the prediction distribution tail). 2) They rigorously tackle uncertainties and edge cases, but they are computationally intensive. In this work, we address this gap by proposing a computationally efficient solution using axiomatic risk theory to handle uncertainties and deal with edge cases. We assume that the ego robot has a planned reference trajectory and samples of the obstacles' future trajectories (e.g. through ). Our solution starts by finding safe halfspaces based on a distributionally robust conditional value-at-risk (${DR} - {CVaR}$) risk metric for each obstacle. Then, the ${DR} - {CVaR}$ safe halfspaces are used in an MPC-based safety filter to enforce safety. The main contributions of this work are:

We extend the notion of a safe halfspace and define data-driven ${DR} - {CVaR}$ safe halfspaces that bound the risk of violating a safety specification.

We verify the efficiency of the ${DR} - {CVaR}$ halfspaces through a numerical analysis and show that they can be computed in a few milliseconds with up to a few hundred samples.

We formulate an MPC-based safety filter that uses the ${DR} - {CVaR}$ safe halfspaces to constrain the motion planning problem and bound collision risks.

We demonstrate the efficacy of our solution and its ability to handle edge-cases through numerical simulations in a variety of motion planning scenarios.

## Notation

The $d$-dimensional zero vector (matrix) and identity matrix are denoted by $\mathbb{0}_{d}$ ($\mathbb{0}_{d,d}$) and $I_{d}$, respectively. We use $a:b$ to denote all integers between $a \in {\mathbb{Z}}$ and $b \in {\mathbb{Z}}$ (inclusive). The Minkowski sum is denoted by $\oplus$. The transpose of a vector or matrix is denoted by ${( \cdot )}^{\top}$. The inner product of vectors $z_{1}$ and $z_{2}$ is denoted by ${z_{1} \cdot z_{2}} = {z_{1}^{\top}z_{2}}$. The support function of a compact set $\mathcal{C}$ is given by ${S_{\mathcal{C}}{(z)}}:={\sup_{x \in \mathcal{C}}{z \cdot x}}$. Random variables/vectors are denoted in ${\mathbf{b}}{\mathbf{o}}{\mathbf{l}}{\mathbf{d}}$ and ${\mathbb{E}}{\lbrack \cdot \rbrack}$ is the expected value operator. Given a loss $\mathbf{l}$, the $CVaR$ metric is ${{CVaR}_{\alpha}^{\mathbb{P}}{({\mathbf{l}})}}:={\inf_{\tau \in {\mathbb{R}}}{{\mathbb{E}}^{\mathbb{P}}{\lbrack{\tau + {\frac{1}{\alpha}{\max{\{{{\mathbf{l}} - \tau},0\}}}}}\rbrack}}}$ which is evaluated with respect to the $\alpha$ worst-cases of the distribution $\mathbb{P}$ (the $1 - \alpha$ quantile in the upper tail). For $N_{s}$ samples of the loss $\{ l^{1},\ldots,l^{N_{s}}\}$, we use a sample average approximation to evaluate the expected value in the $CVaR$ metric:\
${{{CVaR}_{\alpha}^{\mathbb{P}}{({\mathbf{l}})}} \approx {\inf_{\tau \in {\mathbb{R}}}{\frac{1}{N_{s}}{\sum_{i = 1}^{N_{s}}{({\tau + {\frac{1}{\alpha}{\max{\{{l^{i} - \tau},0\}}}}})}}}}}.$

## DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles

### II-A Motion Planning Safety Filtering Problem

We consider the problem of motion planning for an ego robot in the presence of $N_{ob}$ dynamic obstacles whose future behavior is uncertain. The ego robot dynamics are assumed linear and described by:

where $x_{t} \in {\mathbb{R}}^{n}$ is the robot state at time $t$, $u_{t} \in {\mathbb{R}}^{m}$ is the control, ${A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times m}}$ are the state and input matrices, $y \in {\mathbb{R}}^{d}$ is the position, and $C \in {\mathbb{R}}^{d \times n}$ is the matrix that extracts the position from the state. For simplicity, we consider 2D position ($d = 2$), but the results can be easily extended to 3D. The ego robot geometry is assumed to be a convex and compact set denoted by $\mathcal{A}$. We also assume that the ego robot has a desired reference trajectory over a horizon of length $T$ given by ${\mathcal{T}^{r}{(t)}}:={\{{x^{r}{(t)}},\ldots,{x^{r}{({t + T})}}\}}$. This reference trajectory may be obtained from any planning module (e.g. neural network, sampling-based or optimization-based methods, etc.).

Each obstacle is modeled as a convex and compact set $\mathcal{O}_{i}\forall i \in {\lbrack 1:N_{ob}\rbrack}$. Their dynamics are unknown and the motion is uncertain. Furthermore, the prediction distribution is inherently unknown. Instead, we assume access to a module that can generate *sample predictions* of the obstacles' trajectories. The $s$-th sample trajectory of the $i$-th obstacle for a horizon of $T$ time steps is given by ${\mathcal{T}_{i}^{s}{(t)}}:={\{{p_{i}^{s}{(t)}},\ldots,{p_{i}^{s}{({t + T})}}\}}$ and includes only position information ($p_{i}^{s} \in {\mathbb{R}}^{d}$).

An autonomy stack may pass the reference trajectory directly to a tracking controller (Figure 1 faded red arrow) while assuming that it accounts for the obstacles' future trajectories. However, safety requirements desired in a reference trajectory may not be guaranteed, especially if the planner is based on a neural network. A formal safety guarantee is defined as follows.

### Definition 1 (Safety Guarantee)

Given a reference trajectory $\mathcal{T}^{r}$, a chosen risk metric $\mathcal{R}$, and a risk bound $\delta$, safety is guaranteed iff ${\mathcal{R}{(\mathcal{T}^{r})}} \leq \delta$.

To enforce this notion of safety, we advocate for the usage of a safety filter that takes a reference trajectory and outputs a filtered trajectory as depicted in Figure 1. This safety filtering problem is formalized below.

### Problem 1 (Motion Planning Safety Filtering)

Given an ego reference trajectory $\mathcal{T}^{r}{(t)}$ and obstacle trajectory samples $\mathcal{T}_{i}^{s}{(t)},s \in {\lbrack 1:N_{s}\rbrack}$ for every obstacle $i \in {\lbrack 1:N_{ob}\rbrack}$, find a filtered ego trajectory that ensures the safety of the ego robot per Definition 1. ‣ II-A Motion Planning Safety Filtering Problem ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments").

We now proceed with specifying the adopted risk metric $\mathcal{R}$ for the motion planning problem.

### II-B Signed Collision Loss Function

Consider an ego robot and a single dynamic obstacle. The position of the ego robot is denoted by $y$, the ego reference position is denoted by $y^{r}$, and the obstacle position is denoted by $p$.

The deterministic collision avoidance condition is given by ${{({y \oplus \mathcal{A}})} \cap {({p \oplus \mathcal{O}})}} = \varnothing$. Using computational geometry arguments and convexifying the constraint via a separating hyperplane, as in \[16, III-A.2\], we have:

where $z$ is any chosen unit vector per.

The constraint is sufficient for ensuring collision avoidance for a deterministic system. Additionally, we can define a deterministic *safe halfspace*

such that if $y \in \mathcal{H}$, then $y$ is collision free and satisfies. For the deterministic case, the parameters $h,g$ of $\mathcal{H}$ can be directly mapped to the values in. Furthermore, using $\mathcal{H}$ we can define a signed distance function that quantifies the violation or satisfaction amount of a point relative to the collision avoidance constraint. In particular, consider the following loss function:

For an obstacle position $p$, if ${\ell{(p)}} \geq 0$ then $p$ intrudes into the safe halfspace $\mathcal{H}$ and $\ell{(p)}$ is the intrusion amount. Otherwise, the obstacle is $|{\ell{(p)}}|$ units away from the boundary of the safe halfspace.

### II-C Collision Avoidance using DR-CVaR Safe Halfspaces

When the obstacle position is a random variable $\mathbf{p}$, is ill-posed and the loss becomes a random variable $\ell{({\mathbf{p}})}$. We now define a risk-based safe halfspace with respect to a risk metric $\mathcal{R}$ applied to $\ell{({\mathbf{p}})}$.

### Definition 2 (Risk-Based Safe Halfspace)

Given a halfspace normal $h$ and a risk metric $\mathcal{R}$, a risk-based halfspace is given by $\mathcal{H}^{\mathcal{R}}:={\{ p\mid{{{h \cdot p} + \overset{\sim}{g}} \leq 0}\}}$, where $\overset{\sim}{g} = {g^{\ast} - {({{S_{\mathcal{O}}{(h)}} + {S_{- \mathcal{A}}{(h)}}})}}$, and $g^{\ast}$ is the optimal value of the following optimization problem:

subject to ${{\mathcal{R}{({\ell{({\mathbf{p}})}})}} \leq \delta}.$ (4b)

It is common to approximate the distribution of $\mathbf{p}$ or $\ell{({\mathbf{p}})}$ then pose (4b. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) as a chance constraint on the probability of collision hence bounding the value-at-risk (VaR) (e.g. ). However, VaR is not a coherent risk metric in the sense of Artzner et al. \[20, Def 2.4\]. Meanwhile, $CVaR$ is a coherent risk metric that has been advocated for in robotics. Intuitively, $CVaR$ measures the expected cost in the tail of the distribution. Thus, it not only accounts for the *frequency* of undesirable events, but also their *severity*.

Since we only have samples of $\mathbf{p}$ generated by the prediction module, and its underlying distribution is unknown, we use a data-driven *distributionally robust* $CVaR$ risk metric, i.e. ${DR} - {CVaR}$, in (4b. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")). In particular, the samples of $\mathbf{p}$ define an empirical distribution $\hat{\mathbb{P}}$. But, instead of treating $\hat{\mathbb{P}}$ as the true distribution, which can give large sampling errors for small $N_{s}$, we consider a Wasserstein distance-based ambiguity set $\mathcal{P}$ around $\hat{\mathbb{P}}$. Formally, $\mathcal{P} = {{\mathbb{B}}_{\epsilon}{(\hat{\mathbb{P}})}}:={\{{{\mathbb{Q}} \in {\mathcal{M}{(\Xi)}}}\mid{{d_{w}{(\hat{\mathbb{P}},{\mathbb{Q}})}} \leq \epsilon}\}}$ is the Wasserstein ball containing all distributions with a Wasserstein distance of at most $\epsilon$ from $\hat{\mathbb{P}}$. Here, $\mathcal{M}{(\Xi)}$ is the set of all finite mean distributions supported on $\Xi$ and $d_{w}{( \cdot, \cdot )}$ is the Wasserstein distance. Consider ${{\mathbb{Q}}_{1},{\mathbb{Q}}_{2}} \in {\mathcal{M}{(\Xi)}}$ and a norm $\left. \parallel \cdot \parallel \right.$ (we use the 2-norm), the Wassertein distance is defined by ${d_{w}{({\mathbb{Q}}_{1},{\mathbb{Q}}_{2})}}:={\int_{\Xi^{2}}{\left. \parallel{\xi_{1} - \xi_{2}}\parallel \right.\Pi{({d\xi_{1}},{d\xi_{2}})}}}$ where $\Pi$ is a joint distribution of $\xi_{1}$ and $\xi$ with marginals ${\mathbb{Q}}_{1}$ and ${\mathbb{Q}}_{2}$ respectively \[23, Definition 3.1\]. Intuitively, the Wasserstein distance represents the minimum transportation cost of transporting mass from one distribution into another. Accordingly, a ${DR} - {CVaR}$ safe halfspace is defined as follows.

### Definition 3 (DR-CVaR Safe Halfspace)

Consider an empirical distribution $\hat{\mathbb{P}}$ supported on samples of a predicted obstacle position, a Wasserstein-based ambiguity set $\mathcal{P} = {{\mathbb{B}}_{\epsilon}{(\hat{\mathbb{P}})}}$ and a halfspace normal $h$. The ${DR} - {CVaR}$ safe halfspace is defined as $\mathcal{H}^{dr}:={\{ p\mid{{{h \cdot p} + g^{\ast}} \leq 0}\}}$ where $g^{\ast}$ is the optimal value of the following optimization problem:

subject to ${{{DR} - {CVaR}}_{\alpha}^{\epsilon}{({\ell{({\mathbf{p}})}})}} \leq \delta$ (5b)

where ${{{DR} - {CVaR}}_{\alpha}^{\epsilon}{({\ell{(\mathbf{p})}})}}:={\sup_{{\mathbb{P}} \in \mathcal{P}}{{CVaR}_{\alpha}^{\mathbb{P}}{({\ell{(\mathbf{p})}})}}}$.

Here, (5b. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) is an infinite dimensional constraint. However, since $\ell$ is affine, we can utilize tools from to obtain a finite-dimensional convex reformulation.

### Proposition 1

The optimization problem (5. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) with the support $\Xi:={\{ p\mid{{Vp} \leq v}\}}$ for the random variable $\mathbf{p}$ admits the finite-dimensional reformulation:

where $\left. \parallel \cdot \parallel \right._{\ast}$ is the dual norm.

### Proof

Using the $CVaR$ definition with we have:

${CVaR}_{\alpha}^{\mathbb{P}}{({\ell{({\mathbf{p}})}})}$ (7a)
$= {\inf\limits_{\tau}{{\mathbb{E}}^{\mathbb{P}}\left\lbrack {\max\left( {{- \frac{{h \cdot {\mathbf{p}}} + \overset{\sim}{g}}{\alpha}} + {{({1 - \frac{1}{\alpha}})}\tau}},\tau \right)} \right\rbrack}}$ (7b)
$= {\inf\limits_{\tau}{{\mathbb{E}}^{\mathbb{P}}\left\lbrack \underset{{\mathbb{M}}:=}{\underbrace{\max\limits_{k}⁡\left( {{a_{k}{\mathbf{p}}}+{b_{k}\overset{\sim}{g}}+{c_{k}\tau}} \right)}} \right\rbrack}}$ (7c)

where $k \in {\{ 1,2\}}$ and $a_{1} = \frac{- h}{\alpha}$, $b_{1} = \frac{- 1}{\alpha}$, $c_{1} = {1 - \frac{1}{\alpha}}$, $a_{2} = \mathbb{0}_{d}$, $b_{2} = 0$, $c_{2} = 1$. Then, the ${DR} - {CVaR}$ constraint (5b. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) becomes

where the last line follows by the minimax inequality ${\sup{\inf{( \cdot )}}} \leq {\inf{\sup{( \cdot )}}}$. The worst-case expectation ($WCE$) term matches that from \[23, \] with piecewise affine loss functions in the random variable $\mathbf{p}$ and hence applying \[23, Corollary 5.1-(i)\] results in. ∎

### Example 1

Consider an ego reference position $y^{r} = {\lbrack{- 0.9},{- 0.8}\rbrack}^{\top}$ and a nominal obstacle at $p = {\lbrack 0.5,0\rbrack}^{\top}$ both of radius $r = 0.3$. Figure 2 illustrates safe halfspaces using the expected value (mean), $CVaR$ and ${DR} - {CVaR}$ risk metrics with $h = {{({p - y^{r}})}/\left. \parallel{p - y^{r}}\parallel \right.}$ as depicted by the arrow. The halfspaces use 100 samples of the obstacle position sampled from the Gaussian random vector $\mathcal{N}{(p,{diag{(0.01,0.01)}})}$ where $diag{( \cdot )}$ is the diagonal matrix. We use $\alpha = 0.2$, $\delta = 0.1$, and $\epsilon \in {\{ 0.05,0.1,0.2\}}$. As $\epsilon$ increases, the Wasserstein ball becomes larger, including more distributions, and hence the ${DR} - {CVaR}$ halfspaces become more conservative. When $\epsilon\rightarrow 0$, the ${DR} - {CVaR}$ safe halfspace converges to the $CVaR$ case. Here, $y^{r}$ is safe with respect to all halfspaces except the ${DR} - {CVaR}$ with $\epsilon = 0.2$. Note that increasing $\delta$ relaxes the safety constraint and would make the halfspaces less conservative.

Figure 2: Comparison between safe halfspaces based on the mean, CVaR, and DR − CVaR with different ϵ values.

### II-D DR-CVaR Safe Halfspace Guarantees

If the position of the ego robot is constrained to the DR-CVaR safe halfspaces, we obtain a safety guarantee that bounds collision risk, however, we require a technical assumption on the lightness of the tails^11^1This assumption hold trivially if $\Xi$ is compact. Since the distribution in our case represents the position of the obstacle, then $\Xi$ is compact as obstacles can always be limited to a finite detection range. for the underlying true probability distribution ${\mathbb{P}}_{true}$ of predicted obstacle positions. Thus, we have the following lemma.

### Lemma 1 (Concentration Inequality \[24, Theorem 2\])

For a light-tailed distribution ${\mathbb{P}}_{true}$ with $\chi:={{\mathbb{E}}^{{\mathbb{P}}_{true}}{\lbrack{\text{exp}{({\|\mathbf{p}\|}^{\rho})}}\rbrack}} < \infty$ for $\rho > 1$ \[23, Assumption 3.3\] or $\rho > 0$ per, we have

where $\beta$ is a constant term that depends on $\chi,\rho,N_{s}$, and $\epsilon$. Alternatively, ${{\mathbb{P}}{({{\mathbb{P}}_{true} \in {{\mathbb{B}}_{\epsilon}{(\hat{\mathbb{P}})}}})}} \geq {1 - \beta}$ for a carefully chosen value of $N_{s}$.

Therefore, for a desired concentration bound, it is possible to compute a minimum value of $N_{s}$ to guarantee that satisfying the ${DR} - {CVaR}$ constraint (5b. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) ensures the satisfaction of the $CVaR$ variant of it for the true distribution with probability $1 - \beta$. However, this theoretical guarantee is usually quite conservative and generally requires $N_{s}$ to be large making computationally expensive. Instead, we advocate for treating ${\epsilon,N_{s}},$ and $\delta$ as tuneable parameters to achieve a desired safety level that can be validated experimentally.

## MPC-Based Safety Filter with DR-CVaR Safe Halfspaces

We now return to the safe motion planning problem described in Problem 1. ‣ II-A Motion Planning Safety Filtering Problem ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments"). Our solution has two steps:

Computing the safe halfspaces: We interpret the safety constraint ${\mathcal{R}{(\mathcal{T}^{r})}} \leq \delta$ from Definition 1. ‣ II-A Motion Planning Safety Filtering Problem ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments") point-wise in time and per obstacle. Thus, the obstacle trajectory samples are used to solve (5. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) per obstacle per time step over the horizon $T$ resulting in $\mathcal{H}_{i}^{dr}{(t + t^{\prime})}\forall i \in {\lbrack 1:N_{ob}\rbrack},t^{\prime} \in {\lbrack 1:T\rbrack}$.

MPC Filter: The computed halfspaces are used as constraints in an MPC optimization problem that computes a minimally deviating trajectory from the reference trajectory. The MPC optimization problem is formalized below.

### Problem 2 (MPC-Based Safety Filter)

Given an ego reference trajectory $\mathcal{T}^{r}{(t_{0})}$ at time $t_{0}$ and linear ego vehicle dynamics, find the filtered trajectory ${\mathcal{T}{(t_{0})}} = {\{{x{(t_{0})}},\ldots,{x{({t_{0} + T})}}\}}$ for the ego vehicle that satisfies the ${DR} - {CVaR}$ safe halfspaces $\mathcal{H}_{i}^{dr}{(t)},t \in {\lbrack t_{0} + 1:t_{0} + T\rbrack}$, by solving the finite-horizon optimization problem (11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) with the objective function (10. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")).

$\min\limits_{x,u}$ $J\left( x\left( t_{0}:t_{0} + T \right),u\left( t_{0}:t_{0} + T - 1 \right) \right)$ (11a)
subject to $(),u(t) \in \mathcal{U}(t)\forall t \in \left\lbrack t_{0}:t_{0} + T - 1 \right\rbrack$ (11b)
${{()},{x\left( t_{0} \right)}} = {x^{r}\left( t_{0} \right)}$ (11c)
${y(t)} \in {{\mathcal{Y}(t)} \cap \left( {\bigcap\limits_{i = 1}^{N_{ob}}{\mathcal{H}_{i}^{dr}(t)}} \right)}$ (11d)

with $\forall t \in {\lbrack t_{0} + 1:t_{0} + T\rbrack}$. Here, ${\mathcal{Y}{(t)}} \subseteq {\mathbb{R}}^{d}$ is a convex position constraint for the ego robot (e.g. environment bounds), ${\mathcal{U}{(t)}} \subseteq {\mathbb{R}}^{m}$ is the convex control input constraint set, and $R \in {\mathbb{R}}^{n \times n}$, $Q \in {\mathbb{R}}^{m \times m}$ are symmetric, positive semidefinite cost matrices.

The MPC safety filter 11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments") is a quadratic program (QP) and can be modeled with tools such as CVXPY and solved with many solvers, such as ECOS.

### Remark 1

We assume that (11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) is always feasible at $t = 0$. The conjunction in (11d. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) may become empty or unreachable due to $\mathcal{U}{(t)}$ rendering the problem infeasible. In this work, we use the most recent optimal control $u^{\ast}{(t)}$ from solving (11. ‣ III MPC-Based Safety Filter with DR-CVaR Safe Halfspaces ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) and proceed with the next available control, $u^{\ast}{({t + 1})}$, until the problem is solved again or we run out ($u^{\ast}{({{t + T} - 1})}$). Future works will address alternative infeasibility handling approaches.

## Numerical Validation

We analyze the ${DR} - {CVaR}$ safe halfspace computation time and perform numerical simulations. All experiments use CVXPY with ECOS and were executed on a Dell Precision 7520 computer with an Intel Xeon E3-1535M v6 CPU and 32GB RAM. Experiment code can be found at: [https://github.com/TSummersLab/dr-cvar-safety_filtering](https://github.com/TSummersLab/dr-cvar-safety_filtering).

Figure 3: DR − CVaR safe halfspace computation time

TABLE I: CVaR and DR − CVaR safe halfspace average Solve and Call times (ms).

### IV-A Computation Cost Analysis

We perform a numerical analysis for the ${DR} - {CVaR}$ safe halfspace computation time. We find the safe halfspaces as done in Example 1 for various number of samples $N_{s}$. For each $N_{s}$, (5. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) is solved 500 times with different random samples. We report three times: 1) the CVXPY reported setup time (Setup Time), 2) the CVXPY reported solver solve time (Solve Time), and 3) the time for executing the CVXPY solve method (Call Time). The results, in milliseconds, are reported in Figure 3. Since (5. ‣ II-C Collision Avoidance using DR-CVaR Safe Halfspaces ‣ II DR-CVaR Safe Motion Planning with Uncertain Dynamic Obstacles ‣ Distributionally Robust CVaR-Based Safety Filtering for Motion Planning in Uncertain Environments")) is a linear program (LP), it can be solved efficiently within a few milliseconds even for a few hundred samples. The Call Time includes a large overhead not captured by the Setup Time. Additionally, we compare the mean times for finding the ${DR} - {CVaR}$ and $CVaR$ safe halfspaces in Table I. This reveals that while the Solve Time is only about 50% higher for the ${DR} - {CVaR}$ problem, the Call Time grows quickly compared to $CVaR$. We conclude that the ${DR} - {CVaR}$ safe halfspace formulation is suitable for real-time operation especially if a solver is used directly.

### IV-B Motion Planning Safety Filtering Simulations

### IV-B1 Simulation Setup

We model the ego and obstacle geometries as circles of radii $r_{\mathcal{A}} = r_{\mathcal{O}} = 0.3$. The ego robot uses double integrator dynamics with ${{A = \begin{bmatrix}
\end{bmatrix}},{B = \begin{bmatrix}
\end{bmatrix}}},$ and $C = \begin{bmatrix}
\end{bmatrix}$ where $T_{s} = 0.2$sec is the discrete time step. The reference trajectory is generated using an obstacle-agnostic MPC-based motion planner with a target goal state. Its details are not discussed since our safety filter is agnostic to the chosen motion planning algorithm. Unbeknown to the ego robot, the obstacles are single integrators with ${A = I_{2}},{{B = {I_{2}T_{s}}},{C = I_{2}}}$. Sample trajectories are generated by adding a Gaussian random noise $\mathcal{N}{(\mathbb{0}_{2},{diag{(0.01,0.01)}})}$ to a nominal trajectory that keeps the vehicle aligned with the x-axis at a desired speed. However, when realizing the true position of the obstacle, a Laplace distribution with the same mean and covariance as the Gaussian is sampled. We use $T = 10$, $\alpha = 0.2$, $\delta = 0.1$, and $\epsilon = 0.05$.

### IV-B2 Filtering in Different Scenarios

We use three types of reach-avoid motion planning scenarios: 1) Head-on collision, 2) Overtaking, and 3) Intersection. The left column of Figure 4 overlays the trajectories of one experiment using safe halfspaces based on the mean value, $CVaR$, and ${DR} - {CVaR}$ risk metrics. In all three cases, trajectories using ${DR} - {CVaR}$ safe halfspaces achieve the lowest risk, while those using the expected value-based safe halfspace have the highest risk.

Figure 4: Motion Planning Scenarios and their distance to collision statistics across 300 Monte Carlo simulation. Red: Mean safe halfspace ℋ𝔼. Blue: CVaR safe halfspace ℋc v a r. Green: DR − CVaR safe halfspace ℋd r Black: Obstacle.

To demonstrate the advantage of using ${DR} - {CVaR}$ halfspaces, we perform a Monte Carlo simulation repeating each experiment 300 times. The distance to collision $\left. \parallel{y - p}\parallel \right. - r_{\mathcal{A}} - r_{\mathcal{O}}$ is plotted in the right column of Figures 4 with the last row showing a box plot zoomed-in view. Clearly, the performance using safe halfspaces based on the mean value result in more frequent collisions in all three cases. In the box plot, the worst-case scenario using the mean value safe halfspace is around $- 0.45$. With this collision amount, both the ego robot and obstacle would be significantly damaged. The worst-case collision using $CVaR$ results in a $- 0.22$ distance to collision. Here, it may lead to a less severe collision. On the other had, in all three cases, the ${DR} - {CVaR}$ safe halfspace-based formulations avoid collisions with the ego vehicle, avoiding the obstacle even in the worst case scenario. Thus, our proposed solution can secure the robot's safety and systematically reduce collision risks, even with edge cases in the prediction distribution tail.

### IV-B3 Safety Filtering With Multiple Obstacles

Consider the motion planning problem in Figure 5, where the ego robot must avoid 3 obstacles. Figure 5 plots the overall trajectories as well as the ${DR} - {CVaR}$ safe halfspaces (green polytopes). Since the MPC safety filter is a QP, it can be solved efficiently in a few milliseconds. Here, the filter call time takes 7ms on average. The safety filter becomes infeasible only once, so we fall back to the previously computed set of optimal controls. This is illustrated at time step 5 when the ego robot is not inside any of the green safe polytopes. Throughout the experiment, the robot remains sufficiently far away from the obstacles and successfully reaches its goal.

Figure 5: Collision Avoidance with Multiple Obstacles. Green polytopes: DR − CVaR safe halfspaces. Blue: ego. All other colors: obstacles

## Conclusion

In this work we presented a solution that improves a robot's safety when operating in a dynamic environment with prediction uncertainties. We posed a DRO problem that computes ${DR} - {CVaR}$ safe halfspaces that bound the $CVaR$ of a signed collision distance under any distribution close the empirical one based on data. These halfspaces are then used as linear constraints in an MPC safety filter that corrects the ego reference trajectory. We performed a numerical analysis on the ${DR} - {CVaR}$ safe halfspaces and demonstrated that 1) they can be computed in milliseconds, and 2) they can improve safety in edge cases. Future directions include a better approach to handling MPC infeasibilities, relaxations of the halfspaces to trade-off safety for performance, and an implementation of the approach on physical hardware.
