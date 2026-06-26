<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Provably Safe Motion Planning under Unknown Disturbances

Topics include Motion planning, Safe planning, Chance constraints, Distributionally robust optimization, Uncertainty.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops a sampling-based motion-planning algorithm that learns Wasserstein ambiguity tubes from trajectory data to satisfy chance constraints under unknown disturbances. The paper connects probabilistic completeness with distributionally robust safety guarantees for uncertain robotic systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a provably safe sampling-based motion planning algorithm for robotic systems affected by random disturbances of unknown distribution. We consider systems with linear or linearizable dynamics evolving in workspace with arbitrary-shaped obstacles subject to state and control constraints. Safety requirements are formulated as chance-constraints. Our approach leverages data from trajectories of the system to learn a Wasserstein ambiguity tube, i.e., a sequence of ambiguity sets, which contains the trajectory of the system's state distribution with high confidence. This ambiguity tube is then used in a probabilistically complete algorithm to grow a sampling-based motion planning tree that respects the constraints of the problem. We show that learning several lower-dimensional ambiguity tubes instead of a single high-dimensional one effectively reduces the conservatism and boosts scalability. Additionally, we design an efficient bandit-based validity checker that remarkably increases the empirical performance of our approach without sacrificing probabilistic completeness. Case studies show our algorithm finds valid plans in cluttered environments under strict safety thresholds, outperforming state-of-the-art methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is a central problem in robotics, with applications spanning autonomous exploration, manufacturing, and surgical systems. Sampling-based methods have been particularly successful: by drawing random samples, they rapidly construct a search tree and return a collision-free trajectory from start to goal. Traditionally, these algorithms assume a known, deterministic model of the underlying system. In reality, however, robotic systems are subject to disturbances arising from unmodeled dynamics, actuator noise, environmental variability, or model mismatch. Prior work, spanning both sampling-based and trajectory optimization frameworks, has typically attempted to capture such uncertainties using bounded disturbance models or Gaussian noise assumptions, and to design motion plans that are robust under these models. Yet, these strategies are often conservative and rely on strong distributional assumptions that rarely hold in practice. In realistic settings, disturbances are stochastic with *unknown* or *partially known* distributions, making reliable planning significantly more challenging. This work aims to address this challenge by developing an efficient, data-driven motion planning framework that quantifies and propagates uncertainty directly from system data to produce provably safe trajectories.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work has increasingly focused on motion planning under uncertainty. Approaches based on bounded non-deterministic disturbances often yield overly conservative plans, as they ignore the low likelihood of extreme disturbance realizations. To incorporate probabilistic information, methods such as model disturbances as Gaussian and enforce chance constraints. In practice, however, the disturbance distribution is rarely known and must be learned from trajectory data. Distributionally robust methods address this by constructing ambiguity sets over (sets that contain) plausible distributions and planning against all distributions in these sets. While theoretically appealing, these approaches remain highly conservative (even when obstacles are convex), and the conservatism grows with environmental complexity, rendering them impractical for cluttered planning scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce an efficient planning algorithm for systems under unknown disturbance distributions. We use trajectory data to construct a *Wasserstein ambiguity tube*, a high-confidence sequence of ambiguity sets capturing stochastic evolution, and incorporate it into a sampling-based planner. We show that, for linear (or feedback-linearizable) systems, ambiguity propagation decouples from planning, allowing a single offline-learned tube with tight uncertainty characterization. Then, we enforce safety via chance constraints using the optimization-free worst-case collision checker of, enabling planning in cluttered environments and handling nonconvex constraints. The tube has infinite temporal length with finite confidence, removing the need to specify a planning horizon. We further develop complementary validity-checking procedures with distinct efficiency--conservatism trade-offs, and unify them through a multi-armed bandit framework that adaptively selects the appropriate checker. We prove soundness of both the tube construction and validity checking, as well as probabilistic completeness of the algorithm with respect to the tube, and show that leveraging multiple low-dimensional tubes significantly reduces data and computation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Benchmark results confirm the efficacy of the proposed algorithm in complex environments and its consistent outperformance of state-of-the-art methods.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this paper are five-fold: A sampling-based motion planning algorithm for linear systems with unknown additive disturbances that uses trajectory observation data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Proofs of soundness and probabilistic completeness for the planner under relaxed assumptions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

New theoretical results on the propagation of distributional ambiguity.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A tighter characterization of the size of data-driven ambiguity sets defined by the 1-Wasserstein distance than those used in the existing literature.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Three validity-checking methods trading off efficiency and conservativeness, each less conservative than existing work, as well as a multi-armed bandit scheme that adaptively selects among them.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comprehensive evaluation and benchmark studies demonstrating the efficacy of the approach and its advantages over the state-of-the-art approaches.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Classical chance-constrained motion planning assumes linear dynamics with additive Gaussian noise. presents a tree-based algorithm for uncertain linear systems with set-bounded disturbances around uncertain obstacles, while reduce conservatism by assuming a known Gaussian disturbance law and checking node validity via chance constraints.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

To generalize beyond Gaussian disturbances, proposes a distributionally robust approach using *moment ambiguity sets* built from the (assumed known) mean and covariance of the noise and initial state. For convex polytopic obstacles, the chance constraint reduces to a deterministic inequality, but at the cost of substantial conservatism. Moreover, admissible risk is allocated uniformly across obstacles regardless of proximity, which hinders planning in cluttered environments with high safety thresholds. mitigates this by allocating per-obstacle risk equal to its individual collision-probability upper bound, but the solution remains fairly conservative.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Other works use Wasserstein ambiguity sets, defined as balls centered on a nominal (often empirical) distribution. Unlike moment sets, Wasserstein sets shrink to a single distribution as samples grow, avoiding the irreducible conservatism of moment-based approaches. Early work focused on *static* sets; more recent work studies propagation through dynamical systems. characterizes when optimal-transport ambiguity sets are closed under linear and nonlinear mappings, and bound ambiguity propagation through linear stochastic systems. However, these bounds grow unbounded in time, ruling out long horizons. give conditions for time-bounded ambiguity under process and measurement noise, and provides a tighter bound leveraging the contractiveness of the dynamics. However, these results are still too conservative for linear robotic models and cluttered environments. In this work, we provide a tighter characterization: unlike, we learn an ambiguity tube of infinite length but finite radius that contains the state distribution over time with user-defined confidence.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Wasserstein sets have been used in sampling-based planning and in *model predictive control* (MPC), typically with the *conditional value at risk* (CVaR) measure for its coherence and tractability. robustifies linearized GP obstacle predictions via Wasserstein sets but provides no safety guarantee. applies nonlinear MPC with obstacles characterized by data-driven Wasserstein sets, and gives a convex tube-MPC reformulation for stochastic LTI systems under convex safety constraints. A key drawback of CVaR in these settings is that program complexity scales linearly with the sample count, which becomes prohibitive at the sample sizes needed for tight guarantees.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

We instead define collision risk as a chance constraint and use the optimization-free algorithm of to compute the exact worst-case collision probability. Unlike, this handles obstacles of arbitrary shape with cost independent of their number. Combined with our tighter ambiguity characterization, this enables planning in cluttered environments, control-effort limits (unlike ), and general non-convex constraints, with tube size and conservatism shrinking in the sample count.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Unlike, handles uncertainty in both robot and obstacles, using the Wasserstein distance between them as the risk measure, but assumes Gaussian disturbances. Its probabilistic completeness also requires a motion plan whose robot and obstacle supports never overlap, discarding probabilistic information. We prove probabilistic completeness under weaker assumptions by exploiting that information.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

We note that and, to our knowledge, all sampling-based planners using Wasserstein sets treat the set size as a tuning parameter rather than computing a size that guarantees containment, likely due to the sample and compute burden of formal guarantees. We address this by learning several lower-dimensional ambiguity tubes rather than one high-dimensional tube, often reducing sample and computational complexity by orders of magnitude.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Basic Notation", "weight": 1.0} -->

Consider the space $\mathbb{R}^{n}$ equipped with the Euclidean distance. Given a set $X\subseteq\mathbb{R}^{n}$ and a point $x\in\mathbb{R}^{n}$, we denote by $\text{dist}(x,X)$ the minimum Euclidean distance between $x$ and $X$, and by $\text{diam}(X)=\sup_{x,x^{\prime}\in X}\|x-x^{\prime}\|$ the diameter of $X$. We also denote by $X+x$ the *Minkowski sum* of the sets $X$ and $\{x\}$, and by $\mathds{1}_{X}(x)$ the indicator function of $X$, which returns $1$ if $x\in X$ and $0$ otherwise. We use bold symbols to denote random variables, e.g., $\boldsymbol{x}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Basic Notation", "weight": 1.0} -->

We define $\mathcal{D}(X)$ to be the set of Borel probability measures over the metric space $X$ such that $\int_{X}\|x\|\,dP(x)<\infty$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Basic Notation", "weight": 1.0} -->

Let $\boldsymbol{x}$ be distributed according to $P\in\mathcal{D}(X)$, and $X^{\prime}\subseteq X$ be Borel-measurable. We write $P(X^{\prime})\equiv P[\boldsymbol{x}\in X^{\prime}]$ to denote the measure of set $X^{\prime}$ with respect to $P$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Basic Notation", "weight": 1.0} -->

Given a probability distribution $P\in\mathcal{D}(X)$ and a measurable map $f:X\longrightarrow Y$, we denote by $f_{\#}P\in\mathcal{D}(Y)$ the *pushforward measure* of $P$ by $f$, i.e., the measure defined as $f_{\#}P(B):=P(f^{-1}(B))$ for all Borel sets $B\subseteq Y$, with $f^{-1}(B)$ denoting the pre-image of set $B$. When $Y\subseteq\mathbb{R}^{m}$ and $f$ is a linear transformation with matrix $M\in\mathbb{R}^{m\times n}$, we also use the notation $M_{\#}P\in\mathcal{D}(\mathbb{R}^{n})$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A Basic Notation", "weight": 1.0} -->

The $1$-*Wasserstein distance* between distributions $P,P^{\prime}\in\mathcal{D}(X)$ is then defined as where $\Pi(P,P^{\prime})$ is the set of probability distributions on $\mathcal{D}(X\times X)$ with marginals $P$ and $P^{\prime}$. We denote by $\text{supp}(P)$ the support of $P$ and by $\mathcal{M}_{q}(P):=\big(\mathbb{E}_{P}[\|\boldsymbol{x}\|^{q}]\big)^{1/q}$ the $q$-th moment of $P$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A Basic Notation", "weight": 1.0} -->

Finally, we let $\delta_{x}\in\mathcal{D}(X)$ be the Dirac measure located at $x\in X$ and we denote by $\mathbb{B}(\widehat{P},\varepsilon):=\{P\in\mathcal{D}(X):\mathcal{W}(P,\widehat{P})\leq\varepsilon\}$ the Wasserstein Ball with center (nominal distribution) $\widehat{P}\in\mathcal{D}(X)$ and radius $\varepsilon>0$. Given a set of $N$ i.i.d. samples $\{\hat{\boldsymbol{x}}^{(i)}\}_{i=1}^{N}$ from some distribution $P$, the corresponding *empirical distribution* is

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Kinodynamic Sampling-based Planners", "weight": 1.0} -->

Single-query sampling-based tree search algorithms construct a tree in the search space, which is the state space for kinodynamic systems without uncertainty. We aim to transform such planners into ones that handle unknown stochastic disturbances and uncertain initial distributions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Kinodynamic Sampling-based Planners", "weight": 1.0} -->

Alg. 1 shows a generic form of a tree-based planner for kinodynamical systems. It takes state space $X$, input space $U$, goal region $X_{goal}\subset X$, obstacle regions $X_{obs}\subset X$, an initial state $x_{init}\in X$, and a maximum planning time or iteration count (N) as input and returns a near-optimal solution if one is found. Search is performed by growing a motion tree in which states and the connections between them are stored as nodes in $\mathbb{V}$ and edges in $\mathbb{E}$, respectively. The six main subroutines for the planner are: sample, select, extend, validity check and goal check. In sample, a state is randomly sampled from the state space. Then, select chooses an existing node on the tree based on this sample. The node is extended by sampling a control and propagating the system's dynamics in extend. A validity check on this new state is conducted, at which point the new node is added to the tree.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Kinodynamic Sampling-based Planners", "weight": 1.0} -->

Then, goal check assesses whether or not the new node has reached the goal, in which case the algorithm returns the resulting path. If $\mathcal{X}$ is an asymptotically optimal planner, then the algorithm will terminate in finite time with probability $1$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Kinodynamic Sampling-based Planners", "weight": 1.0} -->

Input: X, U, Xgoal, Xobs, xinit, N Output: Valid Trajectory x1: T if one is found xrand, urand← Sample nselect← Select(xrand) nnew← Extend(nselect, urand) if ValidityCheck(nselect, nnew) then 𝔼 ← 𝔼 ∪ {edge(nselect, nnew)} if GoalCheck(nnew) then return ExtractPath(G, nnew); Algorithm 1 Generic Tree-based Planner 𝒳

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We focus on robotic systems whose motion can be described by the stochastic linear dynamics where $\boldsymbol{x}_{t}\in X\subseteq\mathbb{R}^{n}$ is the state at time $t\in\mathbb{N}_{0}$, $u_{t}\in U\subseteq\mathbb{R}^{m}$ is the control input, $A$, $B$, and $G$ are real matrices of appropriate dimensions, and $\boldsymbol{w}_{t}\in W\subset\mathbb{R}^{d}$ is an i.i.d. random disturbance (noise) with distribution $\boldsymbol{w}_{t}\sim P_{w}\in\mathcal{D}(W)$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this work, we consider the settings in which distributions of the noise $P_{w}$ and the initial state $P_{0}$ are *unknown*, but their supports $W$ and $X_{0}$ are known. This assumption is realistic and in fact commonly encountered in robotic systems operating under uncertainty. First, the linear time-invariant modeling assumption is justified by the fact that many robotic platforms are control‐affine and hence feedback‐linearizable. Second, our assumptions on $P_{0}$ and $P_{w}$ relax those in existing work, which often require not only the knowledge of these distributions but also that they be Gaussian. In lieu of not knowing $P_{w}$ and $P_{0}$, we assume that we have access to $N$ i.i.d.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The robot operates in workspace $\text{WS}\subset\mathbb{R}^{\text{ws}}$, where $n_{\text{ws}}\in\{2,3\}$, surrounded by workspace obstacles which it must avoid to reach a goal region. In addition to these obstacles, the state of the robot might be subject to constraints, such as velocity or rate limits. We represent all these workspace obstacles and state limits by the state-space *obstacle set* $X_{\text{obs}}\subset X$. Similarly, the goal region that the robot has to reach in the state space is denoted by $X_{\text{goal}}\subset X$. We allow $X_{\text{goal}}$ and $X_{\text{obs}}$ to have arbitrary shapes. Our goal is to motion plan for this robot with safety guarantees.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To enable stable robot motion, similar to, we consider feedback controllers of the form: where $K\in\mathbb{R}^{m\times n}$ is the feedback control gain, $\bar{u}_{t}\in\mathbb{R}^{m}$ is feedforward control, and $\bar{x}_{t}\in X$ is the *reference state*. The latter is described by the reference open-loop dynamics with arbitrary $\bar{x}_{0}$. Defining $A_{\text{cl}}:=A-BK$, the closed-loop dynamics of the system become Intuitively, given a sequence of feedforward controls, a reference trajectory is induced, and the controller in enables the robot to follow the nominal trajectory. We define a motion plan for this system to be a sequence of pairs $((\bar{u}_{t},\bar{x}_{t}))_{t=0}^{T}$ for some $T\in\mathbb{N}_{0}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Note that, given a motion plan $((\bar{u}_{t},\bar{x}_{t}))_{t=0}^{T}$, the evolution of system's state $\boldsymbol{x}_{t}$ is a stochastic process induced by distributions $P_{w}$ and $P_{0}$ and dynamics. We denote the distribution of $\boldsymbol{x}_{t}$ by $P_{t}$, i.e., $\boldsymbol{x}_{t}\sim P_{t}$. Similarly, since $\boldsymbol{u}_{t}$ depends on $\boldsymbol{x}_{t}$ through the feedback term, it is also a random variable.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Leveraging this dependence on $\boldsymbol{x}_{t}$, the control constraint $\boldsymbol{u}_{t}\in U$ is easily embedded into the collision-avoidance constraint $\boldsymbol{x}_{t}\notin X_{\text{obs}}$ by letting We assume that this is the case unless stated otherwise. In turn, Expression implies that $X_{\text{obs}}$ depends, in the general case, on $\bar{x}_{t}$ and $\bar{u}_{t}$. However, to simplify notation, we denote $X_{\text{obs}}\equiv X_{\text{obs}}(\bar{x}_{t},\bar{u}_{t})$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The probabilities of collision and of reaching the goal at time $t$ are given by Our objective is to generate a motion plan that guarantees that the robot avoids the obstacles, respects the control constraints, and reaches the goal with high probability. However, since $P_{w}$ and $P_{0}$ are unknown, we need to rely on the sample trajectories $\{(\hat{\boldsymbol{x}}^{(i)}_{0},\hat{\boldsymbol{x}}^{(i)}_{1},\ldots,\hat{\boldsymbol{x}}^{(i)}_{H})\}_{i=1}^{N}$ to reason about the probabilities. Such reasoning can be done with some confidence related to the distribution of the sample trajectories. We formulate this data driven, confidence-based motion planning problem as follows.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem 1 (Safe Motion Planning)", "weight": 1.0} -->

Note that, unlike the chance constraints in (7. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances")) that need to only hold stepwise, the confidence must hold over the entire trajectory of System.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Overview of the Approach", "weight": 1.0} -->

Problem 1. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances") is challenging due to the unknown distributions $P_{0}$ and $P_{w}$ and the non-convexity of $X_{\text{obs}}$ and $X_{\text{goal}}$. We propose a sampling-based algorithm that grows a probabilistically collision-free tree from start to goal. In Section IV, we use trajectory samples to learn, at each time step, an *ambiguity set* containing the unknown state distribution with high confidence; we call the resulting time sequence an *ambiguity tube* and prove its soundness. To grow the tree, we check constraints (7. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances")) at each node against the worst-case distribution in the corresponding ambiguity set (Section V). To reduce sample complexity and improve scalability, Section VI shows that leveraging several lower-dimensional ambiguity tubes, which reduce conservatism; the corresponding algorithms (Section VII) and analysis (Section VII-A) retain probabilistic completeness and solution guarantees while substantially lowering computational cost.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Overview of the Approach", "weight": 1.0} -->

Section VII presents the full motion planning algorithms, and Section VII-A proves their completeness and that every returned plan solves Problem 1. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances"). Finally, Section VIII evaluates our approach in simulation on two systems from the literature and compares it against. All proofs are in Appendix A.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 1 (Arbitrary Obstacles)", "weight": 1.0} -->

Unlike other works in which the obstacles are assumed polytopic and convex, our framework is able to handle obstacles of an arbitrary shape. This allows us to effectively find safe paths in cluttered environments and enforce control constraints without the need to employ conservative polytopic approximations. Furthermore, the collision probability that our method yields does not depend on the number of obstacles, unlike.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Construction and Dynamics of Ambiguity Sets", "weight": 1.0} -->

This section describes how to learn an ambiguity tube for trajectories of System. Using error dynamics, we first obtain a single tube independent of the feedforward control and reference state, showing that their effect reduces to a translation of the learned tube. We then construct ambiguity sets from samples of $\boldsymbol{x}_{t}$ and bound the growth of ambiguity over time, yielding an infinite-length tube.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Error Dynamics", "weight": 1.0} -->

We define the *state error* at time $t$ as $\boldsymbol{e}_{t}:=\boldsymbol{x}_{t}-\bar{x}_{t}$, which yields the error dynamics Doing this allows us to express $x_{t}$ as the superposition of the reference state, whose dynamics are deterministic, and the error, which evolves randomly and is independent of the feedforward control and reference dynamics. The distribution $P_{t}^{e}$ of $\boldsymbol{e}_{t}$ is therefore where '$*$' is the convolution operator, and with $P_{0}^{e}:=P_{0}*\delta_{-\bar{x}_{0}}$ by the definition of the error.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Data-Driven Ambiguity Sets", "weight": 1.0} -->

We now describe how to construct a *data-driven* ambiguity set $\mathcal{P}_{t}$ for $P_{t}$ from samples $\{\hat{\boldsymbol{x}}_{t}^{(i)}\}_{i=1}^{N}$ of $\boldsymbol{x}_{t}$ such that $P_{t}\in\mathcal{P}_{t}$ with high confidence. For readability, we drop the subscript $t$. Existing results ensure containment with user-defined confidence given a sufficiently large radius; in Lemma 2. ‣ IV-B Data-Driven Ambiguity Sets ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances"), we tighten this bound for the $1$-Wasserstein distance. We first state a technical lemma.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 2", "weight": 1.0} -->

This bound is tighter than the ones, as it relies on a one-sided McDiarmid inequality and leverages the $q$-th moment of the distribution instead of just its support. We also note that recent results might produce tighter ambiguity sets. Given that our approach is independent of the way the ambiguity sets have been constructed, we leave incorporating the bounds of for future research.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Ambiguity Dynamics and Error Ambiguity Tube", "weight": 1.0} -->

We now learn an ambiguity tube for the trajectories of $\boldsymbol{e}_{t}$ governed. Even when the ambiguity set for $P_{w}$ is small, directly propagating it via can cause it to grow by orders of magnitude. A naive alternative is to build a data-driven ambiguity set at each time step from samples of $\boldsymbol{e}_{t}$, but this has three issues: (i) it requires an a priori upper bound on the planning horizon, which is unknown in practice; (ii) storing samples at every time step is infeasible for realistic horizons, especially given the data needed for tight guarantees; and (iii) Lemma 2. ‣ IV-B Data-Driven Ambiguity Sets ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances") provides only pointwise confidences, so combining them via a union bound yields a trajectory-wide confidence that shrinks as the horizon grows.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C Ambiguity Dynamics and Error Ambiguity Tube", "weight": 1.0} -->

Our approach is an intermediate one that combines the best of both approaches: we obtain data-driven ambiguity sets at only some time steps and infer the rest from them via the system dynamics, yielding an ambiguity tube. We call such an inferred set a *derived* ambiguity set. To construct one at time $t$, we reuse the center of a data-driven set at some $\tau\neq t$ and quantify how the error distribution shifts between $\tau$ and $t$; Lemma 3. ‣ IV-C Ambiguity Dynamics and Error Ambiguity Tube ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances") gives this quantification.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 3", "weight": 1.0} -->

By Lemma 3. ‣ IV-C Ambiguity Dynamics and Error Ambiguity Tube ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances"), if $A_{\text{cl}}$ is stable, $\mathcal{W}(\widehat{P}_{\tau}^{e},P_{t}^{e})$ for $t\geq\tau$ can be made arbitrarily small by choosing $\tau$ large enough.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Hence, given an ambiguity set $\mathcal{P}_{\tau}^{e}=\mathbb{B}(\widehat{P}_{\tau}^{e},\varepsilon_{\tau})$ for sufficiently large $\tau$, the subsequent variation of $P_{t}^{e}$ around $\widehat{P}_{\tau}^{e}$ stays close to $\varepsilon_{\tau}$, and we can reuse $\widehat{P}_{\tau}^{e}$ as the center of $\mathcal{P}_{t}=\mathbb{B}(\widehat{P}_{\tau}^{e},\varepsilon_{t})$ for all $t\geq\tau$ without inflating $\varepsilon_{t}$. We thus need only finitely many data-driven sets, deriving the rest, which makes the approach suitable when the planning horizon is unknown a priori.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 3", "weight": 1.0} -->

This is also key, as shown later, to obtaining an ambiguity tube of arbitrary length with confidence independent of the horizon.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 3", "weight": 1.0} -->

In Alg. 2 we formalize the construction of the ambiguity tube $(\mathcal{P}_{t}^{e})_{t\in\mathbb{N}_{0}}$. Let $\tau_{1},\tau_{2},\dots,\tau_{J}\leq H$ be a set of $J<\infty$ time steps that Alg. 2 takes as inputs.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 3", "weight": 1.0} -->

For each $\tau_{j}$, Lines 2-4 construct a data-driven ambiguity set $\mathcal{P}_{\tau_{j}}^{e}:=\mathbb{B}(\widehat{P}_{\tau_{j}}^{e},\varepsilon_{\tau_{j}})$ from the samples of $e_{\tau_{j}}$, each with confidence $1-\beta/J$, as described in Section IV-B. Note that to this end we need to know $\text{diam}(\text{supp}(P_{\tau_{j}}^{e}))$, which we obtain by propagating the support of $P_{0}$ and $P_{w}$ through the dynamics ^22^2This is a well-understood problem for linear systems.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 3", "weight": 1.0} -->

‣ IV-C Ambiguity Dynamics and Error Ambiguity Tube ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances")). As a result, $\varepsilon_{t}$ is defined as the pointwise minimum of $J$ functions where the minimum is attained at each $\tau_{j}$, leading to the "sawtooth" shape shown in Fig. 1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The following theorem ensures that the constructed ambiguity tube contains the trajectories of the error's distribution.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Theorem 1. ‣ IV-C Ambiguity Dynamics and Error Ambiguity Tube ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances") guarantees that the confidence on the tube containing the entire trajectories of the distribution of the error does not depend on the planning horizon, but only on $J$. This makes it possible to obtain a tube of infinite length while keeping the confidence finite.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 4", "weight": 1.0} -->

It is easy to observe that as the number of samples goes to infinity, each ambiguity set $\mathcal{P}_{t}^{e}$ shrinks to the singleton $\{P_{t}^{e}\}$ with confidence $1-\beta$, thus eliminating the conservativeness of our approach. This is an advantage of using Wasserstein ambiguity sets over, for example, moment ambiguity sets.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 5 (Clustering Empirical Distributions)", "weight": 1.0} -->

By Lemma 2. ‣ IV-B Data-Driven Ambiguity Sets ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances"), the number of samples $N$ needed for $\mathcal{P}_{t}^{e}=\mathbb{B}(\widehat{P}_{t}^{e},\varepsilon_{t})$ to contain $P_{t}^{e}$ is inversely proportional to $\varepsilon_{t}$, so tight ambiguity sets require many samples, which are costly to store and compute.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 5 (Clustering Empirical Distributions)", "weight": 1.0} -->

To alleviate this, we apply scenario reduction to cluster the samples into a weighted set $\{(\hat{\boldsymbol{x}}^{(i)},\boldsymbol{a}_{i})\}_{i=1}^{N_{c}}$ and redefine the center of the ambiguity set as the discrete distribution $\widehat{P}_{t}^{e,c}:=\sum_{i=1}^{N_{c}}\boldsymbol{a}_{i}\delta_{\boldsymbol{\hat{x}}^{(i)}}.$ Quantifying the discrepancy $\mathcal{W}(\widehat{P}_{t}^{e},\widehat{P}_{t}^{e,c})$ between the empirical and clustered distributions and adding it to the radius, the triangle inequality yields We use k-means clustering, which minimizes the $2$-Wasserstein distance between

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 5 (Clustering Empirical Distributions)", "weight": 1.0} -->

For notational simplicity, we henceforth assume that all data-driven ambiguity sets are already clustered.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Validity Check", "weight": 1.0} -->

As discussed in Section II-B, sampling-based motion planning has three main steps: select, extend, and validity check (see Alg. 1). Having obtained an ambiguity tube in Section IV, we now use it to decide whether $\boldsymbol{x}_{t}$ satisfies the chance constraints (7a. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances")). We first formulate the basic validity checker in Alg. 3; Subsection V-A presents a more conservative but significantly faster variant, and Subsection V-B combines the two for strong empirical performance.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Validity Check", "weight": 1.0} -->

The basic validity checker proceeds as follows. Given $\mathcal{P}^{e}_{t}$ and the reference state $\bar{x}_{t}$, we form the state ambiguity set $\mathcal{P}_{t}$ via Proposition 1 and check collision chance constraint by checking the distributionally robust inequality Since $P_{t}^{e}\in\mathcal{P}_{t}^{e}$ by Theorem 1. ‣ IV-C Ambiguity Dynamics and Error Ambiguity Tube ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances"), implies the robot is collision-free. Goal condition is checked analogously via Due to the similarities in and, we only describe the algorithm to check Condition. Adapting it for the goal check is straightforward. When the center of the ambiguity set is an empirical distribution, \[17, Example 7\] provides a fast, optimization-free method based on the distances between the support points and the set. After clustering to reduce the support size (see Remark 5.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Validity Check", "weight": 1.0} -->

‣ IV-C Ambiguity Dynamics and Error Ambiguity Tube ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances")), $\widehat{P}_{t}$ is no longer empirical but a discrete distribution with rational weights $\boldsymbol{a}_{i}\in$. Interpreting it as an empirical distribution with repeated points lets us apply the same method.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Validity Check", "weight": 1.0} -->

The uncertainty quantification method relies on the fact that there exists a finitely-supported worst-case distribution $P^{*}_{t}$ that attains the minimum, i.e., and which is easily constructed by transporting mass from $\widehat{P}_{t}$ to $X_{\text{obs}}$ in a greedy fashion, i.e., transporting first the mass from the atoms of $\widehat{P}_{t}$ that are closer to $X_{\text{obs}}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Validity Check", "weight": 1.0} -->

Let $i_{0}-1$ be the maximum number of atoms that can be transported to $X_{\text{obs}}$ while satisfying the transport cost constraint $\mathcal{W}(\widehat{P}_{t},P^{*}_{t})\leq\varepsilon_{t}$, and $m_{0}$ be the maximum mass from $\hat{\boldsymbol{x}}^{(i_{0})}_{t}$that we can transport to $X_{\text{obs}}$ without violating this constraint, i.e.,

<!-- chunk {"id": "body-0065", "role": "body", "section": "Validity Check", "weight": 1.0} -->

$i_{0}:=\arg\max\left\{j\leq{N_{c}}:\sum_{i=1}^{j-1}\boldsymbol{a}_{i}\text{dist}(\hat{\boldsymbol{x}}^{(i)},X_{\text{obs}})\leq\varepsilon_{t}\right\}$, The worst-case distribution $P^{*}_{t}$ is obtained as the one supported on the atoms after the perturbation, which yields If this probability is higher than $p_{\text{safe}}$, we conclude that $\boldsymbol{x}_{t}$ is not in collision. Otherwise, the state is denoted valid. The pseudocode for the validity checking algorithm is given in Alg. 3 and depicted in Fig. 3.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Validity Check", "weight": 1.0} -->

Pt*[xt ∉ Xobs] > psafe then Algorithm 3 Validity Checking Via Probability Mass Transport Figure 3: Graphical explanation of Alg.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Validity Check", "weight": 1.0} -->

3. On the left, the the nominal distribution P̂t and the atoms {x̂, …, x̂} in its support. On the right, the worst-case distribution P*, supported on {x̂, x̂(2*), x̂(3*), x̂, x̂(4*), x̂}, and which minimizes the probability of xt belonging to Xobs. In this example x̂ ∈ Xobs, so it is not perturbed, and εt is such that it allows to fully transport x̂ and x̂ to the boundary of Xobs, but only the fraction m0 of mass from x̂, and no mass from x̂. Note that the set Xobs has arbitrary shape.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Validity Check", "weight": 1.0} -->

Note that Alg. 3 computes the exact worst-case probability of safety w.r.t. all distributions in the ambiguity set, instead of obtaining a lower bound. Furthermore, it is optimization-free, and only requires computing $N_{c}$ distances, making it relatively fast. Additionally, since it scales with $N_{c}$, namely, the number of atoms in $\widehat{P}_{t}$, clustering these samples can greatly improve the efficiency of the algorithm.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-A Lazy Validity Check", "weight": 1.0} -->

We propose an upper bound on the worst-case collision probability in that is faster to compute than the exact solution of Alg. 3. If the bound is below $p_{\text{safe}}$, we conclude the robot is collision-free; otherwise, we fall back on Alg. 3.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A Lazy Validity Check", "weight": 1.0} -->

The algorithm is as follows. We rely on having computed, in an offline fashion, a sequence of sets $(S^{e}_{t})_{t\in\mathbb{N}_{0}}$ such that For simplicity, we restrict ourselves to balls centered at the origin. In fact, we approximately compute the smallest balls that satisfy by optimizing their radius via the bisection algorithm. Then, at time-step $t$ of the planning phase, if the ball $S^{e}_{t}+\bar{x}_{t}$ does not intersect with any obstacle, we conclude that $x_{t}$ is not in collision. We denote the tube $(S^{e}_{t})_{t\in\mathbb{N}_{0}}$ as *confidence tube*, since it contains more than $p_{\text{safe}}$ probability mass from the trajectories of $P_{t}^{e}$ with high confidence, as we state in Lemma 4.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A Lazy Validity Check", "weight": 1.0} -->

‣ V-A Lazy Validity Check ‣ V Validity Check ‣ Provably Safe Motion Planning Under Unknown Disturbances"). The pseudocode for obtaining the confidence tube is described in Alg. 4.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-A Lazy Validity Check", "weight": 1.0} -->

Input: ℳp(Pw), ℳp(P0), β, {τj}j = 1J, (𝒫te = 𝔹(P̂te, εt))t ∈ ℕ0 from Alg 2, Acl, G Output: Confidence tube (Ste)t ∈ ℕ0 Obtain Sτje such that Ste ← Sτje for all t ∈ Ij; Algorithm 4 Obtain Confidence Tube Input: Xobs, (Ste)t ∈ ℕ0, t, x̄t if Xobs ∩ (Ste + x̄t) = ∅ then Algorithm 5 Lazy Validity Checking

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-B Hybrid Validity Checkers", "weight": 1.0} -->

Validity checking via probability mass transport (Alg. 3) and the lazy check (Alg. 5) trade off efficiency and accuracy: the lazy procedure is faster but more conservative. Relying solely on Alg. 5 can speed up "simpler" problems but underperform when less conservatism is needed, e.g., narrow passages. We therefore propose two hybrid algorithms that combine both methods, improving efficiency while preserving accuracy.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B1 Naive Hybrid", "weight": 1.0} -->

The naive method of improving efficiency is to first use the lazy validity checker, followed by Alg. 3 if Alg. 5 returns *invalid*. This allows the validity checker to quickly find solutions for "simpler" problems but also allowing it to find solutions for more "complex" problems.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-B1 Naive Hybrid", "weight": 1.0} -->

Since this Naive Hybrid validity checker first uses the more conservative Alg. 5 before Alg. 3, it is also sound. Its conservativeness follows that of Alg. 3.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-B2 Bandit-based Validity Checker", "weight": 1.0} -->

The Naive Hybrid method improves on either Alg. 3 or Alg. 5 alone, but is inefficient on nodes where both return invalid. We therefore propose Alg. 6, a bandit-based checker that decides whether to invoke Alg. 3 after Alg. 5 returns invalid. The idea is to cast this decision as a Bernoulli bandit that estimates the relative conservatism of the two checkers over partitions of the workspace.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-B2 Bandit-based Validity Checker", "weight": 1.0} -->

We first partition the interval $$. Then, for a state $\bar{x}_{t}$ determined invalid by Alg. 5, we estimate the volume of the confidence ball centered at $\bar{x}_{t}$ that intersects with obstacles. Then, we use a Bernoulli bandit to decide on whether to pull the other arm (use Alg. 3). In this way, each partition has a bandit arm with number of successes (and failures), namely, the frequency of deciding to use Alg. 3 after Alg. 5 returns invalid, and (not) being successful.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-B2 Bandit-based Validity Checker", "weight": 1.0} -->

At each iteration, if Alg. 3 returns invalid, we first calculate the volume ratio and determine into which partition of $$ this percentage falls. Then, we sample from a beta distribution $p\sim Beta(1+\alpha,1+\beta)$, where $\alpha$ is the number of successes and $\beta$ is the number of failures for that partition. Then, $p$ is compared to a random sample from a uniform distribution in $$ in order to decide on whether to call Alg. 3. Finally, if Alg. 3 is called, we update the arm's (partition) success or failure count based on the result of the validity checker.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-B2 Bandit-based Validity Checker", "weight": 1.0} -->

The Bandit-based Validity Checker stochastically chooses between Alg. 3 and Alg. 5. Since both of these methods are sound, the Bandit-based checker is also sound. In the worst case, it is as conservative as Alg. 3.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-B2 Bandit-based Validity Checker", "weight": 1.0} -->

Input: Xobs, (Ste)t ∈ ℕ0, (𝒫t)t ∈ ℕ0, psafe, t, x̄t isvalid← LazyValidityChecker(Xobs, (Ste)t ∈ ℕ0, t, x̄t); V% ← Vol((Ste + x̄t) ∩ Xobs)/Vol(Ste); r ∼ Unif, p ∼ Beta(Nsucc(i), Nfail(i)); isvalid← validity checking with Alg. 3; Algorithm 6 Bandit-based Validity Checking

<!-- chunk {"id": "body-0081", "role": "body", "section": "Lower-Dimensional Ambiguity sets", "weight": 1.0} -->

The sample complexity of learning an $n$-dimensional distribution scales as $\varepsilon\propto N^{-n}$, making tight guarantees impractical in high dimensions. Employing scenario reduction is similarly inefficient on large high-dimensional datasets, and mitigating methods such as clustering are not effective since the inflation factor needed to account for clustering error grows with dimension. Fortunately, in many cases it suffices to learn the projection of the state distribution onto a lower-dimensional subspace. For example, in a high-dimensional problem with a $2$-D workspace where $X_{\text{obs}}$ and $X_{\text{goal}}$ are defined by workspace obstacles and a goal region, only the robot's $2$-D position matters for the chance constraints in (7. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances")); the resulting ambiguity sets then scale as $N^{-2}$ rather than $N^{-n}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Lower-Dimensional Ambiguity sets", "weight": 1.0} -->

More generally, when $X_{\text{obs}}$ and $X_{\text{goal}}$ involve multiple constraints (e.g., on control or velocity), one can use several lower-dimensional ambiguity sets (one per constraint space) to improve sample and computational complexity while preserving safety. This section formalizes this idea, starting with the following generalization of Lemma 3. ‣ IV-C Ambiguity Dynamics and Error Ambiguity Tube ‣ IV Construction and Dynamics of Ambiguity Sets ‣ Provably Safe Motion Planning Under Unknown Disturbances").

<!-- chunk {"id": "body-0083", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 states that the obstacle (and goal) set decomposes into $L$ sets, each related to a set $Y_{\text{obs}}^{l}$ in some space $\mathbb{R}^{n_{l}}$, typically of smaller dimension than $X_{\text{obs}}^{l}$. This assumption does not reduce generality, as obstacle and goal sets of any shape can be expressed in this form.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Example 1", "weight": 1.0} -->

(b) Lower-dim ambiguity tube Figure 5: Exploiting lower-dimensional ambiguity tubes in Example 1. In (b), l = 1 and the spheres constitute the ambiguity tube for Pte, while the light-blue balls are the ambiguity tube for M1#Pte. Since the workspace obstacles only constrain the workspace position of the system, we learn an ambiguity tube directly for the position. Note that lower-dimensional ambiguity sets are not the projections of the higher-dimensional ones. In fact, they are way smaller.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-A Validity Checking using Lower-Dim. Ambiguity Tubes", "weight": 1.0} -->

We now use Assumption 1 and the lower-dimensional ambiguity tubes from Alg. 7 to check node validity (the goal check is analogous). For a node at time step $t$ with reference state $\bar{x}_{t}$, we form the state ambiguity sets $\mathcal{P}_{l,t}:=\mathbb{B}(\widehat{P}_{l,t},\varepsilon_{l,t})$, where $\widehat{P}_{l,t}=\widehat{P}_{l,t}^{e}*\delta_{M_{l}\bar{x}_{t}}$ for $l\in\{1,\dots,L\}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VI-A Validity Checking using Lower-Dim. Ambiguity Tubes", "weight": 1.0} -->

We then compute the worst-case non-collision probabilities $\min_{P\in\mathcal{P}_{l,t}}P(\mathbb{R}^{n_{l}}\setminus Y_{\text{obs}}^{l})$ via the method of Section V; the node is collision-free if their sum exceeds $p_{\text{safe}}-1+L$, and invalid otherwise. The goal is declared reached when $\sum_{l}\min_{P\in\mathcal{P}_{l,t}}P(\mathbb{R}^{n_{l}}\setminus Y_{\text{goal}}^{l})>p_{\text{safe}}-1+L$. Alg. 8 gives the pseudocode.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VI-A1 Lazy Check using Lower-dim Ambiguity Tubes", "weight": 1.0} -->

We adapt the lazy check in Section V-A to the lower-dimensional ambiguity tubes as described in Alg. 7. We compute $L$ *lower-dimensional confidence tubes*, where the $l$-th tube contains more than $p_{\text{safe}}$ probability mass of $M_{l}\boldsymbol{e}_{t}$ for all $t\in\mathbb{N}_{0}$, with overall confidence $1-\beta$. These tubes yield an efficient upper bound on the collision probability: if the bound falls below $1-p_{\text{safe}}$, the node is collision-free; otherwise, we fall back on Alg. 8.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VI-A1 Lazy Check using Lower-dim Ambiguity Tubes", "weight": 1.0} -->

The pseudocode is in Alg. 9. As in Alg. 5, we precompute sequences $(S^{e}_{l,t})_{t\in\mathbb{N}_{0}}$ for $l\in\{1,\dots,L\}$ such that restricting to balls centered at the origin and finding the (approximately) smallest valid radius by bisection. At time $t$, if no ball $S^{e}_{l,t}+M_{l}\bar{x}_{t}$ intersects $Y_{\text{obs}}^{l}$, the node is collision-free.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VI-A1 Lazy Check using Lower-dim Ambiguity Tubes", "weight": 1.0} -->

Input: ℳp(Pw), ℳp(P0), β, {τj}j = 1J, (𝒫l, te = 𝔹(P̂l, te, εl, t))t ∈ ℕ0, l ∈ {1, …, L} from Alg. 7, Acl, G, Ml for l ∈ {1, …, L} Output: Lower-dimensional confidence tubes (Sl, te)t ∈ ℕ0 for l ∈ {1, …, L} Obtain Sl, τje such that $\min\big\{P(S^{e}_{l,\tau_{j}}):P\in\mathbb{B}(\widehat{P}_{l,\tau_{j}}^{e},\bar{\varepsilon}_{l,\tau_{j}})\big\}>\dfrac{p_{\text{safe}}}{L}$; Algorithm 9 Construct Lower-Dim. Confidence Tubes

<!-- chunk {"id": "body-0090", "role": "body", "section": "WDR-$\\mathcal{X}$ Algorithm", "weight": 1.0} -->

In this section, we present our general motion planning framework, Wasserstein Distributionally Robust-$\mathcal{X}$ (WDR-$\mathcal{X}$), to solve Problem 1. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances"). Here, $\mathcal{X}$ is any tree-based kinodynamic sampling-based algorithm from Section II-B. Pseudocode is given in Alg. 10.^33^3If lower-dimensional ambiguity sets are used, the corresponding algorithms from Section VI apply instead.

<!-- chunk {"id": "body-0091", "role": "body", "section": "WDR-$\\mathcal{X}$ Algorithm", "weight": 1.0} -->

The framework operates in two phases: ambiguity set construction and planning. In the first phase (Lines 1--2), we learn ambiguity and confidence tubes from data via Algs. 2 and 4 (Section IV-B). Note that this phase needs to be done only once per system; the resulting tubes can be reused across planning queries and environments.

<!-- chunk {"id": "body-0092", "role": "body", "section": "WDR-$\\mathcal{X}$ Algorithm", "weight": 1.0} -->

In the second phase (Lines 4--10), we grow a motion tree as in Alg. 1. Each node is a nominal state evolving per, and Sample (Line 5), Select (Line 6), and Extend (Line 7) act on the nominal state via a randomly sampled feedforward control. A new node is added if it satisfies Constraint (7a. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances")), checked using the validity checkers of Section V on $(\mathcal{P}_{t}^{e})_{t\in\mathbb{N}_{0}}$ and $(S^{e}_{t})_{t\in\mathbb{N}_{0}}$ (Line 8). A solution is returned once a valid node satisfies Constraint (7b. ‣ III Problem Formulation ‣ Provably Safe Motion Planning Under Unknown Disturbances")) (Line 12).

<!-- chunk {"id": "body-0093", "role": "body", "section": "WDR-$\\mathcal{X}$ Algorithm", "weight": 1.0} -->

The planner performs the same subroutines as Alg. 1 for a deterministic linear system except in the validity check: all other subroutines act on the nominal state and feedforward dynamics, so we propagate only the nominal dynamics during tree search rather than the uncertainty. This enables much faster planning and replanning across environments for the same system, since the ambiguity tube is reused.

<!-- chunk {"id": "body-0094", "role": "body", "section": "WDR-$\\mathcal{X}$ Algorithm", "weight": 1.0} -->

Input: State space 𝒳, input space 𝒰, Xobs, Xgoal, ℳp(Pw), ℳp(P0), β, {τj}j = 1J, Acl, G, X0, W, $\{\hat{\boldsymbol{e}}^{(i)}_{\tau_{1}},\hat{\boldsymbol{e}}^{(i)}_{\tau_{2}},\ldots,\hat{\boldsymbol{e}}^{(i)}_{\tau_{J}}\}_{i=1}^{N}$, psafe, iterations N Phase 1: Offline Tube Construction Ambiguity Tubes (𝒫te)t ∈ ℕ0 using Alg.

<!-- chunk {"id": "body-0095", "role": "body", "section": "WDR-$\\mathcal{X}$ Algorithm", "weight": 1.0} -->

2; Confidence Tubes $(S^{e}_{t})_{t\in\mathbb{N}_{0}}usingAlg.~alg:confidence_balls$; 0.5em Phase 2: Online Planning x̄rand, ūrand← Sample; nselect← Select(xrand); nnew← Extend(nselect, ūrand); if ValidityCheck(nnew, (𝒫te)t ∈ ℕ0, (Ste)t ∈ ℕ0) then 𝔼 ← 𝔼 ∪ {edge(nselect, nnew)}; if nnew satifies Eq. (7b) then return ExtractPath(G, nnew); Planning with lower-dimensional ambiguity tubes follows the same logic as Alg. 10, with a few differences: in Line 1, the lower-dimensional ambiguity tubes $(\mathcal{P}_{l,t}^{e})_{t\in\mathbb{N}_{0}}$ for $l\in\{1,\dots,L\}$ are obtained via Alg.

<!-- chunk {"id": "body-0096", "role": "body", "section": "WDR-$\\mathcal{X}$ Algorithm", "weight": 1.0} -->

7; in Line 2, the confidence tubes $(S_{l,t}^{e})_{t\in\mathbb{N}_{0}}$ are obtained via Alg. 9; and in Line 9, validity is checked using Alg. 8, lazy check, or a hybrid of them as in Section V-B.

<!-- chunk {"id": "body-0097", "role": "body", "section": "VII-A Theoretical Analysis", "weight": 1.0} -->

In this section, we analyze the theoretical properties of our algorithmic framework. All proofs can be found in the Appendix. We first show that Alg. 10 is sound.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Theorem 4. ‣ VII-A Theoretical Analysis ‣ VII WDR-𝒳 Algorithm ‣ Provably Safe Motion Planning Under Unknown Disturbances") also applies to the hybrid validity checkers of Section V-B: first, the Naive Hybrid algorithm either deems a node valid via Alg. 5 or defers to Alg. 3. On the other hand, the Bandit-based algorithm always checks validity of a node via Alg. 3, which is less conservative, with positive probability. Furthermore, when an attempt to propagate a node is not allowed by the more conservative algorithm, the probability of using Alg. 3 in the next iteration increases. By these considerations, both hybrid algorithms inherit the probabilistic completeness property under the assumptions in Thm. 4. ‣ VII-A Theoretical Analysis ‣ VII WDR-𝒳 Algorithm ‣ Provably Safe Motion Planning Under Unknown Disturbances").

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 6", "weight": 1.0} -->

In the following two theorems, we conclude that Alg. 10, leveraging the lower-dimensional ambiguity tubes for validity checking, is also sound and probabilistically complete with respect to the conservatism of the collision checkers.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We evaluate the performance of our proposed method in several case studies and benchmarks. To put our results in perspective, we compare the following uncertainty propagation and collision-checking approaches: TS: moment-based distributionally robust-RRT.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Risk-Assigned: moment-based distributionally robust-RRT with risk allocation.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Particle-WDR-RRT: Alg. 10 with particle-based validity checker.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Confidence-WDR-RRT: Alg. 10 with confidence-region validty checker.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Hybrid-WDR-RRT: Alg. 10 with Naive Hybrid validity checker.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Bandit-WDR-RRT: Alg. 10 with Bandit-based validity Checker.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Evaluation", "weight": 1.0} -->

All algorithms were implemented in C++ with the Open Motion Planning Library (OMPL). We utilize kinodynamic RRT as the underlying planner for WDR-$\mathcal{X}$ for all experiments. The simulations were conducted single threaded on a machine with 3.7GHz CPU and 32GB of RAM.

<!-- chunk {"id": "body-0107", "role": "body", "section": "VIII-A 4-D Linear System", "weight": 1.0} -->

We first consider a 4-D linear system, subject to process noise and initial state uncertainty. We benchmark over four environment types spanning a diverse range of planning scenarios: (i) Scattered, with relatively sparse obstacles and ample free space; (ii) Cluttered, with dense obstacles and little free space; (iii) Narr('width'), a narrow-passage environment whose width we vary to assess the conservatism of the validity checkers; and (iv) Random, containing 10 obstacles of random width, height, and position. The Scattered, Cluttered, and Narr(1.5) environments are shown in Fig. 6.

<!-- chunk {"id": "body-0108", "role": "body", "section": "VIII-A 4-D Linear System", "weight": 1.0} -->

(c) Narrow Passage Narr(1.0) (d) Narrow Passage Narr(0.3) Figure 6: Benchmark environments for 4-D Linear System. Obstacles are shown in black and the goal region is shown in green. Representative plots of Monte carlo simulation of solution trajectories are shown in blue for Gaussian noise.

<!-- chunk {"id": "body-0109", "role": "body", "section": "VIII-A 4-D Linear System", "weight": 1.0} -->

4D Linear System with Gaussian Noise 4D Linear System with Non-Gaussian Noise TABLE I: Benchmark results for 4-D linear system over 100 runs. ‘Succ’ is the fraction of trials in which a valid path was found within 300 s; ‘Time’ is the mean planning time over successful trials; ‘–’ indicates no successful trial. Best success rate in each row is bold; among methods with equal success, the fastest is also bold.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VIII-A 4-D Linear System", "weight": 1.0} -->

The distributions (which are unknown to the planner) for the initial state $P_{0}$ and process noise $P_{w}$ are zero-mean Gaussians with covariances: Both $P_{0}$ and $P_{w}$ are truncated at $4$ standard deviations. Since the obstacles in are defined only in the workspace, it suffices to learn a single ambiguity tube for the 2-D projection of the state distribution. We achieve this using the formulation in Section VI with $L=1$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VIII-A 4-D Linear System", "weight": 1.0} -->

We also consider the same system with non-Gaussian noise, obtained by pushing a bi-variate uniform distribution through the map (b) Ours: Confidence Checker.

<!-- chunk {"id": "body-0112", "role": "body", "section": "VIII-A 4-D Linear System", "weight": 1.0} -->

Table I summarizes the results across all environments.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Comparison with baselines", "weight": 1.0} -->

The moment-based approaches exhibit two fundamental limitations that our method overcomes. First, their validity checkers inflate obstacles using analytic bounds derived from the first two moments of the state distribution. This over-approximation renders them overly conservative in constrained geometries: both baselines fail at Narr(0.3) and Narr(0.18) under Gaussian noise, whereas Bandit-WDR-RRT achieves 1.00 and 0.97 success, respectively. Further, under non-Gaussian noise, the moment bounds used by both baselines become overly conservative, where TS achieves only 3% success and Risk Allocation only 9% on the Random environment, compared to 76% for Bandit-WDR-RRT. More strikingly, both baselines fail at Narr(0.5) because the looser moment bounds over-approximate the state distribution's support, making the passage appear infeasible. In contrast, our Wasserstein ambiguity tube learns a distribution-free confidence set directly from samples, capturing the actual shape of the noise distribution rather than relying on moment surrogates, thus avoiding unnecessary conservatism regardless of the true distribution.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Comparison with baselines", "weight": 1.0} -->

It is important to note that our approach is inherently distributionally robust, meaning the true underlying noise distribution remains completely unknown to the planner. Because the ambiguity-tube constraints must guarantee safety for the worst-case distribution within the confidence set, our method naturally exhibits more conservative planning behaviors than would be observed if the exact distribution were known a priori. However, unlike the moment-based baselines that suffer from geometric over-approximation, our conservatism is tight with respect to the ambiguity set while providing sound safety guarantees under unknown distributions.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Comparison with baselines", "weight": 1.0} -->

In the easier environments (Scattered, Cluttered, wide narrow passages), where there is more free space and solutions are easier to find, the baselines achieve comparable success rates to our method and are faster due to their closed-form validity checks. This is expected: the analytic bounds are tight when the geometry is forgiving. However, our methods remain competitive even here: Confidence-WDR-RRT matches the baselines' speed at 0.01 s in these cases.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Comparison among WDR-RRT variants", "weight": 1.0} -->

Among our proposed validity checkers, the Particle-based variant is the most general but incurs high per-node evaluation cost (110--190 s mean planning time), making it impractical as a standalone checker. The Confidence-Region checker is fast (comparable to the baselines in easy environments) but inherits some conservatism from its geometric over-approximation, failing at Narr(0.18) under Gaussian noise and Narr(0.3) under non-Gaussian noise. The Hybrid checker alleviates this by falling back to particle evaluation near obstacles, but remains slower than necessary. Bandit-WDR-RRT offers the best balance: it adaptively allocates computational effort, matching or exceeding the success rate of all other variants while being 1.5--3$\times$ faster than Hybrid-WDR-RRT across environments.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Comparison among WDR-RRT variants", "weight": 1.0} -->

For each of the runs, the planned trajectories are validated via Monte Carlo simulation, with the found solution paths achieving between 99-100% success rate across trials, confirming that the ambiguity-tube constraints provide sound safety guarantees. Example trajectories for the Gaussian noise case are shown in Fig. 6.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Comparison among WDR-RRT variants", "weight": 1.0} -->

Fig. 7 visualizes the search trees grown after 60 s in Narr(0.18) under Gaussian noise. The moment-based checker produces trajectories that stays far from all obstacles and never enters the narrow passage. The Confidence-Region checker allows nodes closer to the walls but cannot go through the gap to reach the goal within the time limit. The Bandit checker successfully explores the passage and reaches the goal region, consistent with its 0.97 success rate in Table I.

<!-- chunk {"id": "body-0119", "role": "body", "section": "VIII-B 8-D Drone System", "weight": 1.0} -->

Finally, we show the scalability of our approach during planning with a 8-D drone system navigating on a 2D plane, i.e., $n=8$ and $n_{\text{ws}}=2$, and with $n_{u}=2$. In this example, we use the Stable Sparse RRT (SST) algorithm. The model is taken. The noise distribution is Gaussian with zero mean and covariance via $G$, a $4\times 2$ matrix mapping the 2D disturbance $\mathbf{w}$ into the 4D state: so that only the velocity states $(\dot{x},\dot{y})$ are directly perturbed; the position states $(x,y)$ are unaffected. The state-space covariance is then given by $W=GG^{\top}$, a $4\times 4$ matrix.

<!-- chunk {"id": "body-0120", "role": "body", "section": "VIII-B 8-D Drone System", "weight": 1.0} -->

We set the probability of safety to $p_{\text{safe}}=0.02$. In this case study, we consider both collision avoidance constraints with respect to the workspace obstacles and also control constraints, where we let $U=\{u\in\mathbb{R}^{m}:\|u\|\leq 0.025\}$. We also let the goal region be a physical location in the 2D workspace.

<!-- chunk {"id": "body-0121", "role": "body", "section": "VIII-B 8-D Drone System", "weight": 1.0} -->

Note that, although the system is high-dimensional, the goal and obstacles are related to the lower-dimensional spaces $\mathbb{R}^{\text{ws}}$ and $\mathbb{R}^{n_{u}}$. Because of this, we make use of the approach described in Section VI and learn two lower-dimensional ambiguity tubes: one for $M_{1\#}P_{t}^{e}$, related to the position of the drone and another for $-K_{\#}P_{t}^{e}$, related to the control effort.

<!-- chunk {"id": "body-0122", "role": "body", "section": "VIII-B 8-D Drone System", "weight": 1.0} -->

Table II and Fig. 8 show that Bandit-WDR-SST finds valid paths in all three environments, including the narrow passage, with planning times well under 60 s. The Monte Carlo simulations of the trajectories show a 100% success rate. The ability to handle an 8-D system with two separate lower-dimensional ambiguity tubes shows that the decomposition in Section VI directly enables tractable planning in higher-dimensional systems.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we presented a probabilistically complete tree-based framework for motion planning of linear and feedback-linearizable systems with additive random disturbances of unknown distribution. Our approach uses observations from previous trajectories to learn an ambiguity tube containing the state distribution at all times, then leverages this tube to find safe paths. We also presented a variant that learns several lower-dimensional tubes to reduce sample and computational complexity, and a bandit-based validity checker that adaptively chooses between a precise but slow checker and a conservative but fast one. Empirical evaluation demonstrates the effectiveness of our approach in finding safe paths and its superiority over state-of-the-art methods.
