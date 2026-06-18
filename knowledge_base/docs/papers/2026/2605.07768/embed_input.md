<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems

Topics include Model predictive control, Predictive control, Robustness, Uncertainty, Optimization, Planning, Control, Learning, SMPC, Probably approximately correct, Distributional robustness, DR.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate interactive trajectory planning subject to uncertainty in the decisions of surrounding agents. To control the ego-agent, we aim to first learn the decision distribution and solve a Stochastic Model Predictive Control (SMPC) problem. To account for errors in the learned distribution, we show that it is possible to utilize Probably Approximately Correct (PAC) learning in combination with Distributionally Robust (DR) optimization to obtain a solution which accounts for the errors induced by the learning model. The results indicate that our PAC learning-based DR-MPC framework provides a method to interpolate between a robust MPC and an omnipotent SMPC, based on the available number of samples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory planning is a crucial component of many robotic applications, such as manipulators, drones, and Autonomous Vehicles (AVs) (blackmore2011chance; borrelli2004collision; schouwenaars2001mixed). Although much work has been dedicated towards this topic, the arguably most difficult challenge still remains: Safe and efficient planning in environments with exogenous agents, e.g humans. A major challenge to this end is the fact that the actions of the robot and humans can have an inherent influence on each other. Poor treatment of this interaction leads to an incorrect human motion model, which could significantly hinder performance and compromise safety, e.g., causing dead-locks or collisions. Some examples of interactive trajectory planning are displayed in Fig. 1. Further, safety and efficiency can be conflicting objectives. A conservative planner may ensure high safety standards but could impair or even halt operations. Similarly, a more daring planner may attain higher performance, but could endanger nearby humans. Hence, an ideal robotic system should trade-off risk-minimization with performance-maximization while accurately assessing interactions between itself and humans.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, Model Predictive Control (MPC), combined with Machine Learning (ML), has gathered much attention in recent years.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Outline and Contribution", "weight": 1.0} -->

In this work, we extend the learning-based DR-MPC framework to allow for more complex models. In particular, we show that this extension allows for trajectory planning applications that consider both interactive decisions and provide rigorous uncertainty quantification. To this end, we leverage excess risk bounds from Probably Approximately Correct (PAC) learning to construct valid ambiguity sets for interactive human decision models. Finally, we demonstrate our learning-based DR-MPC in an interactive trajectory planning scenario and compare performance and constraint satisfaction with its robust and stochastic counterparts. In a broader sense, this work presents a step towards learning-based and efficient interactive trajectory planning with rigorous safety guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Trajectory Planning Problem", "weight": 1.0} -->

In this section, we first present the general SMPC-based trajectory planning problem. A key step involves formulating the problem over a scenario tree based on the possible human decisions. In a later section, we reformulate this problem as a learning-based Distributionally Robust Optimal Control Problem. To refer to the ego-agent we utilize subscript $e$. For clarity, we consider a single human agent, referred to with subscript $h$. However, the presented framework is applicable to any number of human agents.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Ego- and Human-agent Dynamics", "weight": 1.0} -->

Indeed, the aim of the MPC problem is to obtain the ego-agent control actions $\mathbf{u}_{e}$. Following the approach, e.g schuurmans2023general; chen2022interactive, the human control actions are characterized by a predefined set of control laws, each associated with a specific interactive decision. The decision-making process is modeled as a discrete random variable $\mathbf{y} \in {\mathbb{Y}} = {\{ y_{1},\ldots,y_{d}\}}$, where $d = {|{\mathbb{Y}}|}$. In, e.g., the road crossing scenario in Fig. 1, a human driver may, e.g., consider: $y_{1}$ corresponding to breaking, and $y_{2}$ corresponding to driving through the crossing. To consider interactions, the distribution of the decisions is dependent on the states of both the ego- and human-agent as,

<!-- chunk {"id": "body-0008", "role": "body", "section": "Ego- and Human-agent Dynamics", "weight": 1.0} -->

with absolute constant parameters $\theta$. The human control actions are then obtained by sampling a stochastic control law $\kappa:{{{\mathbb{R}}^{N_{h,x}} \times {\mathbb{Y}}}\mapsto{\mathbb{R}}^{N_{h,u}}}$. As in prior work, $f_{h}$ and $\kappa$ are assumed to be available apriori while $\mathbf{p}_{\theta}{(\overline{\mathbf{x}})}$ is considered unknown. In, e.g., the road crossing scenario of Fig. 1, $f_{h}$ can, e.g., be chosen as a kinematic model, while $\kappa$ may be a set of human driver models, e.g., IDM.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Ego- and Human-agent Dynamics", "weight": 1.0} -->

While one might wish to also learn these functions, this problem setting already has the following attractive properties: 1.) Through the decision distribution, we explicitly account for the multimodality of interactive trajectory planning, in turn often reflecting the largest source of uncertainty, see, e.g., Fig. 1. 2.) With a tractable $\mathbf{p}{(\overline{\mathbf{x}})}$ this model is well suited for gradient-based optimizers, enabling interactive planning. 3.) As we will soon show, we may obtain rigorous uncertainty quantification with a learning-based $\mathbf{p}_{\theta}{(\left. \mathbf{y} \middle| \overline{\mathbf{x}} \right.)}$. Considering uncertainty in $f_{h}$ and $\kappa$ is a topic we consider of particular interest for future work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Stochastic Model Predictive Control on Scenario Trees", "weight": 1.0} -->

The SMPC problem is formulated over a finite, discrete-time horizon $k = {0,\ldots,N}$. As $|{\mathbb{Y}}|$ is finite, we can enumerate the human control actions and construct a directed scenario tree over the horizon. We will refer to nodes with the index $\iota \in {\mathbb{N}} = {\{ 0,\ldots,N_{\iota}\}}$. The tree starts from its root $\iota = 0$ and terminates at it's leaf nodes $\iota \in {\mathbb{N}}_{f}$. To describe the parent of a node we utilize $\Pr{(\iota)}$, and similarly for the set of children ${Ch}{(\iota)}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Stochastic Model Predictive Control on Scenario Trees", "weight": 1.0} -->

Further, to ease notation, we introduce $\iota^{+}$ as a single node that is a direct descendant of $\iota$, i.e., $\iota = {\Pr{(\iota^{+})}}$ and $\iota^{+} \in {{Ch}{(\iota)}}$. An example with ${|{\mathbb{Y}}|} = 2$ is displayed in Fig. 2.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Stochastic Model Predictive Control on Scenario Trees", "weight": 1.0} -->

Each node contains the joint state ${\overline{\mathbf{x}}}_{\iota}$ and each node, excluding leaf nodes, contains the ego-control actions $\mathbf{u}_{e,\iota}$ and a random variable $\mathbf{y}_{\iota}$. Allowing a small notational abuse, we define $y_{\iota^{+}}$ as the human decision at node $\iota$ responsible for the transition to node $\iota^{+}$. Hence, we may describe the joint state dynamics as follows,

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stochastic Model Predictive Control on Scenario Trees", "weight": 1.0} -->

The dynamics are repeated for all nodes, excluding leaf nodes, producing all states in the scenario tree $\overline{\mathbf{X}} = {\lbrack{\overline{\mathbf{x}}}_{\iota}\rbrack}_{{\forall\iota} \in {\mathbb{N}}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stochastic Model Predictive Control on Scenario Trees", "weight": 1.0} -->

Here, the distance between the two agents is measured by ${dist}:{{{\mathbb{R}}^{N_{e,x}} \times {\mathbb{R}}^{N_{h,x}}}\mapsto{\mathbb{R}}}$ and $d_{safe} \in {\mathbb{R}}^{+}$ is an additional safety margin. Indeed, the states of the human agent are uncertain due to the random variables $\mathbf{Y}$. To constrain the probability of encountering any collisions over the horizon, we may introduce a chance constraint as,

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stochastic Model Predictive Control on Scenario Trees", "weight": 1.0} -->

where $\varepsilon \in {\lbrack 0,1\rbrack}$ is an accepted probability threshold.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stochastic Model Predictive Control on Scenario Trees", "weight": 1.0} -->

which includes: expected cost (5a), dynamics (5b), human decision distribution (5c), chance constraint (5d), ego-vehicle constraints (5e) and boundary constraints (5f). Indeed, our aim is to solve the above problem for $\mathbf{U}_{e}$ from the current traffic state $\overline{\mathbf{x}}{(t)}$. One can obtain a tractable version of the above problem by reformulating (5a) and (5d), as, e.g., borve2025tight, and learning the parameterized distribution $\mathbf{p}_{\theta}$. However, to obtain rigorous guarantees we additionally need to quantify how well we are able to learn $\mathbf{p}_{\theta}$. In the following sections, we propose a method to quantify this error utilizing ambiguity sets and further show that such ambiguity sets may be used to construct a tractable distributionally robust optimal control problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Machine Learning Problem", "weight": 1.0} -->

In the following section, we present the ML problem for learning the decision distribution. We further discuss generalization bounds on the learning scheme in the form of excess risk bounds.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Basic Definitions", "weight": 1.0} -->

We consider a classification problem with random variables $\mathbf{y} \in {\mathbb{Y}} = {\{ y_{1},y_{2},\ldots,y_{d}\}}$ and $\mathbf{x} \in {\mathbb{X}} \subseteq {\mathbb{R}}^{n_{x}}$ with a joint distribution ${(\mathbf{x},\mathbf{y})} \sim \mathcal{D}$. More precisely, we consider the joint distribution which is absolutely continuous with respect to $\mathbf{x}$ as,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Basic Definitions", "weight": 1.0} -->

where ${\mathbf{p}_{\theta}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}} \in \mathcal{P}_{\theta}$ is the conditional label distribution and $\theta \in {\mathbb{R}}^{n_{x}}$ are absolute constant parameters. In our MPC setting, $\mathbf{y}$ are labels corresponding to a decision and $\mathbf{x}$ are state-dependent features. Indeed, we aim to obtain an estimate of the conditional distribution by utilizing functions ${{\hat{\mathbf{p}}}_{\theta}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}} \in \mathcal{F}_{\theta}$. To this end, we define a risk measure utilizing the cross-entropy, i.e.,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Basic Definitions", "weight": 1.0} -->

where $\mathbf{1}_{\mathbf{y} = y_{i}}$ is an indicator function for $\mathbf{y} = y_{i}$. The ERM is then obtained by solving the following optimization problem,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Basic Definitions", "weight": 1.0} -->

Naturally, since the estimate ${\hat{\mathbf{p}}}_{\theta}$ is based on a finite sample of $\mathcal{D}$, the above problem will not return the true distribution. Indeed, we desire a result that is as close to the true distribution as possible. The following section provides a framework for measuring this discrepancy in terms of how well ${\hat{\mathbf{p}}}_{\theta}$ minimizes the risk.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Excess Risk Bounds", "weight": 1.0} -->

Much work has been dedicated towards deriving bounds on the excess risk for many different machine learning algorithms. Bounds on the excess risk typically take the form of,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Excess Risk Bounds", "weight": 1.0} -->

for some ${r{(n,\alpha)}} \in {\mathbb{R}}^{+}$, depending on the number of samples $n$, and some probability threshold $\alpha \in {\lbrack 0,1\rbrack}$. Similar to prior work in DR-MPC, we will assume uniform convergence, which we state more formally with the following assumption.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1 (Uniform Convergence)", "weight": 1.0} -->

Consider the setting of Subsection 3.1 with risk measure $\mathcal{R}_{\mathcal{D}}$ of $\mathbf{p}_{\theta}$ and empirical estimator $\mathcal{R}_{\mathbb{D}}$. Uniform convergence implies,

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 1 (Uniform Convergence)", "weight": 1.0} -->

Bounds of the type are additionally challenging in the setting of Section 3.1 since the risk is unbounded, but may be obtained by imposing constraints on the random variable $\mathbf{x}$ and $\theta$. Different approaches, e.g., VC-dimensions (vapnik2015uniform), Rademacher complexity (bartlett2002rademacher) or PAC-Bayes bounds (mcallester1998some), yield different constraints with varying restrictiveness in different applications. Note that our approach is flexible with regard to the choice of bound and may be adapted based on $\mathcal{P}_{\theta}$ and $\mathcal{F}_{\theta}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Assumption 1 ‣ 3.2 Excess Risk Bounds ‣ 3 Machine Learning Problem ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems") implies that the empirical risk of the ERM converges to the true risk of the true distribution. In the problem setting of Subsection 3.1, this assumption is satisfied if the function class $\mathcal{F}_{\theta}$ is complex enough to include the true distribution $\mathbf{p}_{\theta}$, i.e., $\mathcal{P}_{\theta} \subseteq \mathcal{F}_{\theta}$. This assumption is identical in principle to prior work, e.g., schuurmans2023general, while allowing us to consider larger families for $\mathcal{P}_{\theta}$ and $\mathcal{F}_{\theta}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example Problem Formulation", "weight": 1.0} -->

To provide an early intuition for the learning setting, we describe a simple interactive distribution example that will be used later in the simulation study. We will consider a case where $\mathbf{y} \in {\{{- 1},1\}}$ is conditionally Bernoulli distributed as,

<!-- chunk {"id": "body-0028", "role": "body", "section": "Ambiguity sets from Excess Risk", "weight": 1.0} -->

In this section, we will transform our empirical risk bound to a bound on the generalization error of the conditional distribution estimate. To this end, we will construct ambiguity sets that are suitable for obtaining a tractable DR-MPC problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Ambiguity sets from Excess Risk", "weight": 1.0} -->

A natural approach to account for uncertainty in the distribution estimate is to consider a set of distributions in a certain neighborhood of the estimate. Such sets are often referred to as divergence-based ambiguity sets and typically take the form,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Ambiguity sets from Excess Risk", "weight": 1.0} -->

where $\hat{P}$ is a probability estimate, ${{\mathfrak{d}}{(P,\hat{P})}} \in {\mathbb{R}}$ is a divergence measure, and $\epsilon \in {\mathbb{R}}^{+}$ determines the size of the neighborhood (rahimian2019distributionally). Often, $\epsilon$ is selected to ensure probabilistic guarantees on the true distribution's inclusion within the set. We will now show that cross-entropy-based risk measures are closely related to divergence-based ambiguity sets with the following proposition.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Learning-based Distributionally Robust Model Predictive Control", "weight": 1.0} -->

With an ambiguity set that quantifies the discrepancy between the true and estimated conditional distributions, our aim is now to solve, accounting for the worst-case distribution in the ambiguity set. To this end, we will reformulate the objective (5a) and chance constraints (5d) using nested risk measures. Formally defining and proving all reformulations in this section requires an extensive review of the existing literature. Hence, we aim to discuss key properties of the reformulations and refer the interested reader to, e.g., schuurmans2023general; sopasakis2019risk; rahimian2019distributionally; shapiro2021lectures for risk measures and DRO, and sopasakis2019risk; chen2022interactive for nested risk.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Risk Measures in Distributionally Robust Optimization", "weight": 1.0} -->

As is well explored in the literature, e.g., shapiro2021lectures, the KL-divergence-based ambiguity sets can be expressed with an equivalent conic representation. In the case of (15 ‣ 4 Ambiguity sets from Excess Risk ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems")) the conic representation becomes,

<!-- chunk {"id": "body-0033", "role": "body", "section": "Risk Measures in Distributionally Robust Optimization", "weight": 1.0} -->

where $\mathcal{K}$ is a closed, convex cone, $\nu$ are auxiliary variables, $E$, $F$ are matrices, and $b_{\hat{\theta}}{(x)}$ is a vector-valued function that contains ${\hat{\mathbf{p}}}_{\theta}$. Importantly, as $\mathcal{A}_{n,\alpha}$ is convex and conic in $\mathbf{p}$ and $\nu$, we can construct a coherent, conditional risk measure for a random quantity $\mathbf{Z} \in {\mathbb{R}}^{d}$ as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Risk Measures in Distributionally Robust Optimization", "weight": 1.0} -->

Provided that strong duality holds, problem can equivalently be expressed as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Observe that in the scenario tree setting of Section 2, will be conditioned on the state ${\overline{\mathbf{x}}}_{\iota}$ with $\mathbf{Z}_{{Ch}{(\iota)}}$. Hence, the above risk measure describes the expected $\mathbf{Z}_{{Ch}{(\iota)}}$, subject to the worst-case $\mathbf{p} \in {\mathcal{A}_{n,\alpha}{({\overline{\mathbf{x}}}_{\iota})}}$, which in turn describes the probability of transitions from $\iota$ to $\iota^{+} \in {{Ch}{(\iota)}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Nested Risk Measures over Scenario Trees", "weight": 1.0} -->

The conditional risk measure can be utilized for a single $\iota$ with children ${Ch}{(\iota)}$. To obtain a distributionally robust version of (5a) and (5d) we need a risk measure that treats all nodes in the scenario tree. To this end, we utilize the nested risk formulation of sopasakis2019risk.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Nested Risk Objective", "weight": 1.0} -->

Observe that expanding the expectation with respect to $\mathbf{Y}$ in (5a) yields

<!-- chunk {"id": "body-0038", "role": "body", "section": "Nested Risk Objective", "weight": 1.0} -->

Given that $\ell$ and $\ell_{f}$ are lower semi-continuous and level-bounded over a closed set, we can formulate for each expectation to construct a version of (5a) that treats the nested risk as,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Nested Risk Objective", "weight": 1.0} -->

where ${\overline{\rho}}_{|{( \cdot )}}$ denotes the nested risk objective. As further detailed in sopasakis2019risk, given that is coherent, the nested risk objective omits a tractable dual-reformulation. To this end, a crucial step is to observe that we may consider a recursive formulation of the conditional risk measure in the form

<!-- chunk {"id": "body-0040", "role": "body", "section": "Nested Risk Objective", "weight": 1.0} -->

In the case of leaf nodes $\iota^{+} \in {{Ch}{(\iota)}} \subseteq {\mathbb{N}}_{f}$, we naturally have $\gamma_{\iota} = {\rho_{|{\overline{\mathbf{x}}}_{\iota}}\left\lbrack {\ell_{f}{(x_{\iota^{+}})}_{{Ch}{(\iota)}}} \right\rbrack}$. Hence, each $\gamma_{\iota}$ measures the risk of all subsequent reachable nodes in the tree. Expressing for each node in the tree, we can obtain the following reformulation of the nested risk objective,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Nested Risk Constraints", "weight": 1.0} -->

We will now derive the corresponding distributionally robust chance constraints of (5d), utilizing the same nested risk framework. Following borve2025tight, we may express an outer approximation of the joint chance constraints over the scenario tree as,

<!-- chunk {"id": "body-0042", "role": "body", "section": "Nested Risk Constraints", "weight": 1.0} -->

where $\mathbb{1}_{{\mathbb{R}}^{+}}:{{\mathbb{R}}\mapsto{\{ 0,1\}}}$ is an indicator function of the positive real line, and ${\sigma_{b,\beta}{(x)}} = {b/{({1 + {\exp{({- {\betax}})}}})}}$ is a sigmoid function. Here, (i) follows from Boole's inequality and (ii) follows by picking $b$ and $\beta$ such that $\sigma_{b,\beta} \in {{Epi}\, 1_{{\mathbb{R}}^{+}}}$, where $Epi$ denotes the epigraph. One can directly observe that the result of has a similar structure to that of the objective.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Nested Risk Constraints", "weight": 1.0} -->

As $\sigma_{b,\beta} \circ g$ is continuous and level bounded over a closed set, the reformulation of the nested risk chance constraints follows in a similar manner to that of the nested risk objective. For brevity, we forego repeating the same arguments. Similar to the objective, we will introduce auxiliary variables, $\delta_{\iota} \in {\mathbb{R}}$, $\Delta = {\lbrack\delta_{\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$, to describe the corresponding version of and $\mu_{\iota}$, $M = {\lbrack\mu_{\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$ to describe the dual variables of the conditional risk measures.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nested Risk Constraints", "weight": 1.0} -->

To again ease notation, we introduce a set $\Omega_{\sigma_{b,\beta} \circ g}$ to gather the constraints of the corresponding nested risk chance constraints.

<!-- chunk {"id": "body-0045", "role": "body", "section": "DR-MPC Problem Formulation", "weight": 1.0} -->

With a Distributionally robust formulation of (5a) and (5d) we can now construct the complete DR-MPC problem.

<!-- chunk {"id": "body-0046", "role": "body", "section": "DR-MPC Problem Formulation", "weight": 1.0} -->

Here, (23a) describes the distributionally robust objective with corresponding constraints (23d), (23b) describes the dynamics, (23c) describes the distributionally robust, joint chance constraints, (23e) describes ego-agent limitations, and (23f) describes the boundary conditions. In a closed-loop setting, is solved at each discrete time, given the current traffic state $\overline{\mathbf{x}}{(t)}$, with the ego-agent applying each $\mathbf{u}_{e,0}$. In an open-loop setting, is solved once to obtain the control actions for the entire horizon $\mathbf{U}_{e}$, applying the corresponding actions over the discrete horizon.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Simulation Study", "weight": 1.0} -->

We will now demonstrate our methods in an interactive trajectory planning example. To emphasize the properties of proposed method, we will consider a simple road crossing case between an Autonomous System (AS) and a human, see Fig. 3(a). To directly compare the result of the different optimization problems, we will investigate statistical results with the ego-agent adopting an open-loop control strategy.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reference Controllers", "weight": 1.0} -->

As a reference for the DR-MPC scheme, we will utilize two alternative MPC designs for solving problem. First, a robust version (R-MPC), which does not utilize an estimate of $\mathbf{p}_{\theta}$ and instead accounts for all possible $\mathbf{x}_{h}$ given $f_{h}$ and $\kappa$, i.e., the collision avoidance constraints are not relaxed in any node, regardless of probability. Similarly, the objective is not weighted based on the probability of each respective node. Second, a stochastic version utilizing the ground truth distribution (GT-SMPC). This problem directly solves, with the expected cost and joint chance-constraint. More details of this reformulation is available in borve2025tight.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Implementation", "weight": 1.0} -->

Both and were formulated in $CasADi$ (casadi) and solved with $IPOPT$ (ipopt). The simulations ran on a laptop equipped with a 12th Gen Intel(R) Core(TM) i7-12850HX CPU and 32 GB of RAM.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simulation Specifications", "weight": 1.0} -->

The human agent may pick from two available decisions: $y_{1}$, corresponding to a breaking maneuver, and $y_{2}$, corresponding to tracking a reference $\mathbf{x}_{ref}$. The control law $\kappa$ is based on the Intelligent Driver Model (IDM), tuned for aggressive brake ($y_{1}$) and smooth reference tracking ($y_{2}$). For the decision distribution we consider a case with $\mathbf{x} = {- {\lbrack{p_{e}/v_{e}},{p_{h}/v_{h}}\rbrack}}$, i.e., reflecting the signed time for the respective agent to reach the intersection, with $\mathbf{p}_{\theta}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}$ defined as in where $\theta = {\lbrack 3,3\rbrack}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Learner and Control Design", "weight": 1.0} -->

Indeed, the number of nodes, and further the number of variables scales exponentially with the length of the prediction horizon. In practice, scenario reduction strategies are often used to tackle this issue (jacobsen2025combined). In this study however, we aim to demonstrate the statistical properties, in reference to the ground-truth distribution. Hence, we opt for a relatively small $N = 6$, with a relatively large ${\Deltat} = 1.0$ to balance computational complexity.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Learner and Control Design", "weight": 1.0} -->

See Table 1 for numerical values. As desired, this yields a challenging scenario, where the ego-vehicle is forced to take risk to improve performance. For the learner we will again consider the setting of Subsection 3.3, with basic definitions in Subsection 3.1. We will further consider Euclidean norms with $B = \sqrt{18}$, and $R = \sqrt{18}$, and $n$ i.i.d measurements of $x_{i}$ and $y_{i}$, assumed available offline. For the ambiguity set of Proposition 3 ‣ 4 Ambiguity sets from Excess Risk ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems"), we consider ${{\eta{(r)}} = \sqrt{r}},{r \in {\lbrack 0,1\rbrack}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Learner and Control Design", "weight": 1.0} -->

As displayed in Table 2 we will investigate the solutions of the DR-MPC as the number of data points, and correspondingly as ${\hat{\mathbf{p}}}_{\theta}$ and $r{(\alpha,n)}$, vary.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Fig. 3(b) provides a qualitative evaluation of the controller properties by displaying the predicted inter-vehicle distance ("Distance Margin"), the probability of violating the distance constraint ("Violation Probability"), and the velocity profiles of the respective vehicles. For a quantitative evaluation we may directly compute metrics by propagating the ground-truth distribution over the respective solutions $\mathbf{X}_{e}$ and $\mathbf{U}_{e}$. To this end, we consider: Expected Cost as the objective function subject to $\mathbf{p}_{\theta}$; Crossing Rate as the rate of which the ego-vehicle crosses before the human; Stopping Rate as the rate of which the human crosses before the ego-vehicle, and Violation Rate as the rate of which the constraint $g$ is violated. The results are displayed in Table 2. The R-MPC baseline attains violation free trajectory plans, but simultaneously obtains a remarkably high expected cost and low crossing rate. The omnipotent GT-SMPC manages to take the highest risk, and correspondingly achieve the highest performance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Recall that the GT-SMPC is not practically realizable as it is assumed to have access to the ground-truth distribution. The result for the DR-MPC can be observed to converge from the R-MPC, towards the GT-SMPC as the number of samples tends towards infinity, across all metrics.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

The results indicate that the DR-MPC controllers provides a practically realizable method to interpolate between the R-MPC, and GT-SMPC methods based on the available number of samples $n$. The fact that the DR-MPC with $n = 10^{3}$ provides a significant improvement over the robust controller, indicate that there exist some highly unlikely scenarios that significantly strain the performance of the R-MPC. However, we simultaneously observe that convergence towards the GT-SMPC with $n$ is slow. This could indicate that Propositions 1 ‣ 3.3 Example Problem Formulation ‣ 3 Machine Learning Problem ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems") and 3 ‣ 4 Ambiguity sets from Excess Risk ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems") are excessively conservative. Formulating tighter bounds for these propositions could be particularly interesting for practical applications. Further applications of this work could also consider different types of estimators, e.g., neural networks.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We are additionally interested in rigorously investigating conditions for control guarantees, such as stability, recursive feasibility and probabilistic constraint satisfaction.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

The authors thank Deepthi Pathare, Stefan Börjesson, Markus Gerdin, and Sten Elling Tingstad Jacobsen for insightful discussions concerning the research topic.
