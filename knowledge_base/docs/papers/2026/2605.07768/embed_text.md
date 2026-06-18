## Introduction

Trajectory planning is a crucial component of many robotic applications, such as manipulators, drones, and Autonomous Vehicles (AVs) (blackmore2011chance; borrelli2004collision; schouwenaars2001mixed). Although much work has been dedicated towards this topic, the arguably most difficult challenge still remains: Safe and efficient planning in environments with exogenous agents, e.g humans. A major challenge to this end is the fact that the actions of the robot and humans can have an inherent influence on each other. Poor treatment of this interaction leads to an incorrect human motion model, which could significantly hinder performance and compromise safety , e.g., causing dead-locks or collisions. Some examples of interactive trajectory planning are displayed in Fig. 1. Further, safety and efficiency can be conflicting objectives. A conservative planner may ensure high safety standards but could impair or even halt operations. Similarly, a more daring planner may attain higher performance, but could endanger nearby humans. Hence, an ideal robotic system should trade-off risk-minimization with performance-maximization while accurately assessing interactions between itself and humans. To this end, Model Predictive Control (MPC), combined with Machine Learning (ML), has gathered much attention in recent years.

Figure 1: Interactive trajectory planning examples. The ego-agent (green) needs to negotiate with a human agent (yellow). Arrows indicate a discrete number of feasible alternatives in corresponding color.

### Related Work

A wide range of methods has been applied to this problem setting. In this paper, we will only discuss optimization-based methods and refer the interested reader to lavalle2006planning for others. MPC optimizes performance metrics over a future horizon, subject to different model-based constraints, e.g., dynamics, actuator limitations, and collision avoidance. A compelling property of MPC is that it can be possible to establish rigorous guarantees , e.g., optimality and constraint satisfaction, under the model assumptions. In dynamic environments, the collision avoidance constraints are heavily dependent on an accurate model of the surroundings. However, human movement is notoriously challenging to model, can be inherently uncertain and, in the case of interactions, depend on the robot's own motion. Recently, large-scale ML models have displayed impressive performance for human trajectory predictions with uncertainty estimates (salzmann2020trajectron++). Such ML predictors have further been incorporated with Stochastic MPC (SMPC) to obtain a trade-off between performance and probabilistic collision avoidance satisfaction (nair2022stochastic). However, interactive planning is often lost, as large-scale ML predictors are difficult to integrate with the gradient-based optimizers used for MPC. Further, as the uncertainty quantification is heuristic, rigorous probabilistic constraint satisfaction is often lost. Some recent works has successfully integrated large-scale ML models (borve2023interaction), but without rigorously accounting for errors in the ML predictor. Rigorous constraint satisfaction has also been obtained with large-scale ML (lindemann2023safe). However, the guarantees hold only under assumptions that disregard interactions. Of particular interest to this work is schuurmans2023general, that utilize Distributionally Robust Optimization (DRO) and treat humans as Markov Systems with a discrete, finite set of available decisions. A learning-based Distributionally Robust MPC (DR-MPC) is then utilized to obtain probabilistic guarantees on collision avoidance with respect to human decision making. A crucial component of this approach is the construction of ambiguity sets that contain the true human model with high probability. However, the utilized theoretical framework does not allow for ML models that are complex enough to describe interactions.

### Outline and Contribution

In this work, we extend the learning-based DR-MPC framework to allow for more complex models. In particular, we show that this extension allows for trajectory planning applications that consider both interactive decisions and provide rigorous uncertainty quantification. To this end, we leverage excess risk bounds from Probably Approximately Correct (PAC) learning to construct valid ambiguity sets for interactive human decision models. Finally, we demonstrate our learning-based DR-MPC in an interactive trajectory planning scenario and compare performance and constraint satisfaction with its robust and stochastic counterparts. In a broader sense, this work presents a step towards learning-based and efficient interactive trajectory planning with rigorous safety guarantees.

## Trajectory Planning Problem

In this section, we first present the general SMPC-based trajectory planning problem. A key step involves formulating the problem over a scenario tree based on the possible human decisions. In a later section, we reformulate this problem as a learning-based Distributionally Robust Optimal Control Problem. To refer to the ego-agent we utilize subscript $e$. For clarity, we consider a single human agent, referred to with subscript $h$. However, the presented framework is applicable to any number of human agents.

### Ego- and Human-agent Dynamics

We consider the ego-agent state $\mathbf{x}_{e} \in {\mathbb{X}}_{e} \subseteq {\mathbb{R}}^{N_{e,x}}$ and control actions $\mathbf{u}_{e} \in {\mathbb{U}}_{e} \subseteq {\mathbb{R}}^{N_{e,u}}$ with continuously differentiable, potentially non-linear, discrete-time dynamics $f_{e}:{{{\mathbb{R}}^{N_{e,x}} \times {\mathbb{R}}^{N_{e,u}}}\mapsto{\mathbb{R}}^{N_{e,x}}}$. The human-agent is considered in a similar fashion with $\mathbf{x}_{h} \in {\mathbb{R}}^{N_{h,x}}$, $\mathbf{u}_{h} \in {\mathbb{R}}^{N_{h,u}}$, and $f_{h}:{{{\mathbb{R}}^{N_{h,x}} \times {\mathbb{R}}^{N_{h,u}}}\mapsto{\mathbb{R}}^{N_{h,x}}}$. For notational convenience, we concatenate these attributes as $\overline{\mathbf{x}} = {\lbrack\mathbf{x}_{e}^{\top},\mathbf{x}_{h}^{\top}\rbrack}^{\top}$, $\overline{\mathbf{u}} = {\lbrack\mathbf{u}_{e}^{\top},\mathbf{u}_{h}^{\top}\rbrack}^{\top}$, $f = {\lbrack f_{e}^{\top},f_{h}^{\top}\rbrack}^{\top}$.

Indeed, the aim of the MPC problem is to obtain the ego-agent control actions $\mathbf{u}_{e}$. Following the approach , e.g schuurmans2023general; chen2022interactive, the human control actions are characterized by a predefined set of control laws, each associated with a specific interactive decision. The decision-making process is modeled as a discrete random variable $\mathbf{y} \in {\mathbb{Y}} = {\{ y_{1},\ldots,y_{d}\}}$, where $d = {|{\mathbb{Y}}|}$. In, e.g., the road crossing scenario in Fig. 1, a human driver may, e.g., consider: $y_{1}$ corresponding to breaking, and $y_{2}$ corresponding to driving through the crossing. To consider interactions, the distribution of the decisions is dependent on the states of both the ego- and human-agent as,

with absolute constant parameters $\theta$. The human control actions are then obtained by sampling a stochastic control law $\kappa:{{{\mathbb{R}}^{N_{h,x}} \times {\mathbb{Y}}}\mapsto{\mathbb{R}}^{N_{h,u}}}$. As in prior work, $f_{h}$ and $\kappa$ are assumed to be available apriori while $\mathbf{p}_{\theta}{(\overline{\mathbf{x}})}$ is considered unknown. In, e.g., the road crossing scenario of Fig. 1, $f_{h}$ can, e.g., be chosen as a kinematic model, while $\kappa$ may be a set of human driver models, e.g., IDM. While one might wish to also learn these functions, this problem setting already has the following attractive properties: 1.) Through the decision distribution, we explicitly account for the multimodality of interactive trajectory planning, in turn often reflecting the largest source of uncertainty, see, e.g., Fig. 1. 2.) With a tractable $\mathbf{p}{(\overline{\mathbf{x}})}$ this model is well suited for gradient-based optimizers, enabling interactive planning. 3.) As we will soon show, we may obtain rigorous uncertainty quantification with a learning-based $\mathbf{p}_{\theta}{(\left. \mathbf{y} \middle| \overline{\mathbf{x}} \right.)}$. Considering uncertainty in $f_{h}$ and $\kappa$ is a topic we consider of particular interest for future work.

### Stochastic Model Predictive Control on Scenario Trees

Figure 2: Example of a scenario tree for |𝕐| = 2.

The SMPC problem is formulated over a finite, discrete-time horizon $k = {0,\ldots,N}$. As $|{\mathbb{Y}}|$ is finite, we can enumerate the human control actions and construct a directed scenario tree over the horizon. We will refer to nodes with the index $\iota \in {\mathbb{N}} = {\{ 0,\ldots,N_{\iota}\}}$. The tree starts from its root $\iota = 0$ and terminates at it's leaf nodes $\iota \in {\mathbb{N}}_{f}$. To describe the parent of a node we utilize $\Pr{(\iota)}$, and similarly for the set of children ${Ch}{(\iota)}$. Further, to ease notation, we introduce $\iota^{+}$ as a single node that is a direct descendant of $\iota$, i.e., $\iota = {\Pr{(\iota^{+})}}$ and $\iota^{+} \in {{Ch}{(\iota)}}$. An example with ${|{\mathbb{Y}}|} = 2$ is displayed in Fig. 2.

Each node contains the joint state ${\overline{\mathbf{x}}}_{\iota}$ and each node, excluding leaf nodes, contains the ego-control actions $\mathbf{u}_{e,\iota}$ and a random variable $\mathbf{y}_{\iota}$. Allowing a small notational abuse, we define $y_{\iota^{+}}$ as the human decision at node $\iota$ responsible for the transition to node $\iota^{+}$. Hence, we may describe the joint state dynamics as follows,

The dynamics are repeated for all nodes, excluding leaf nodes, producing all states in the scenario tree $\overline{\mathbf{X}} = {\lbrack{\overline{\mathbf{x}}}_{\iota}\rbrack}_{{\forall\iota} \in {\mathbb{N}}}$. We may similarly define $\mathbf{X}_{e} = {\lbrack\mathbf{x}_{e,\iota}\rbrack}_{{\forall\iota} \in {\mathbb{N}}}$, $\mathbf{U}_{e} = {\lbrack\mathbf{u}_{e,\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$, and $\mathbf{Y} = {\lbrack\mathbf{y}_{\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$. Ensuring collision avoidance amounts to ensuring that there exists a positive distance between the space occupied by each agent, for all nodes in the tree. We may describe this with the following scalar-valued constraints.

Here, the distance between the two agents is measured by ${dist}:{{{\mathbb{R}}^{N_{e,x}} \times {\mathbb{R}}^{N_{h,x}}}\mapsto{\mathbb{R}}}$ and $d_{safe} \in {\mathbb{R}}^{+}$ is an additional safety margin. Indeed, the states of the human agent are uncertain due to the random variables $\mathbf{Y}$. To constrain the probability of encountering any collisions over the horizon, we may introduce a chance constraint as,

where $\varepsilon \in {\lbrack 0,1\rbrack}$ is an accepted probability threshold.

Lastly, the SMPC problem considers a stage cost $\ell:{{{\mathbb{R}}^{N_{e,x}} \times {\mathbb{R}}^{N_{e,u}}}\mapsto{\mathbb{R}}}$, terminal cost $\ell_{f}:{{\mathbb{R}}^{N_{e,x}}\mapsto{\mathbb{R}}}$ and a terminal set ${\mathbb{X}}_{e,f}$. This finally yields the complete SMPC problem formulation over the scenario tree as,

$\min\limits_{\mathbf{U}_{e}}$ ${\mathbb{E}}_{\mathbf{Y}|\overline{\mathbf{X}}}\left\lbrack {{\sum\limits_{\iota \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}{\ell{(\mathbf{x}_{e,\iota},\mathbf{u}_{e,\iota})}}} + {\sum\limits_{\iota \in {\mathbb{N}}_{f}}{\ell_{f}{(\mathbf{x}_{e,\iota})}}}} \right\rbrack$ (5a)
${s.t}.$ ${{\overline{\mathbf{x}}}_{\iota^{+}} = {f{({{{\overline{\mathbf{x}}}_{\iota},\left. {\overline{\mathbf{u}}}_{\iota} \middle| \mathbf{y}_{\iota} \right.} = y_{\iota^{+}}})}}},{{{\forall\iota^{+}} \in {{Ch}{(\iota)}}},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}}$ (5b)
${\mathbf{y}_{\iota} \sim {\mathbf{p}_{\theta}{(\left. \mathbf{y}_{\iota} \middle| \mathbf{x}_{\iota} \right.)}}},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$ (5c)
${{\mathbb{P}}_{\mathbf{Y}|\overline{\mathbf{X}}}\left\lbrack {{\underset{\iota\in{{\mathbb{N}}\smallsetminus{\{ 0\}}}}{\bigcup}g{({\overline{\mathbf{x}}}_{\iota})}} \geq \left. 0 \middle| {\overline{\mathbf{x}}}_{0} \right.} \right\rbrack} \leq \varepsilon$ (5d)
${\mathbf{x}_{e,\iota} \in {\mathbb{X}}_{e}},{{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}};{{\mathbf{u}_{e,\iota} \in {\mathbb{U}}_{e}},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}}}$ (5e)
${{\overline{\mathbf{x}}}_{0} = {\overline{\mathbf{x}}{(t)}}};{{\mathbf{x}_{e,\iota} \in {\mathbb{X}}_{e,f}},{{\forall\iota} \in {\mathbb{N}}_{f}}}$ (5f)

which includes: expected cost (5a), dynamics (5b), human decision distribution (5c), chance constraint (5d), ego-vehicle constraints (5e) and boundary constraints (5f). Indeed, our aim is to solve the above problem for $\mathbf{U}_{e}$ from the current traffic state $\overline{\mathbf{x}}{(t)}$. One can obtain a tractable version of the above problem by reformulating (5a) and (5d), as , e.g., borve2025tight, and learning the parameterized distribution $\mathbf{p}_{\theta}$. However, to obtain rigorous guarantees we additionally need to quantify how well we are able to learn $\mathbf{p}_{\theta}$. In the following sections, we propose a method to quantify this error utilizing ambiguity sets and further show that such ambiguity sets may be used to construct a tractable distributionally robust optimal control problem.

## Machine Learning Problem

In the following section, we present the ML problem for learning the decision distribution. We further discuss generalization bounds on the learning scheme in the form of excess risk bounds.

### Basic Definitions

We consider a classification problem with random variables $\mathbf{y} \in {\mathbb{Y}} = {\{ y_{1},y_{2},\ldots,y_{d}\}}$ and $\mathbf{x} \in {\mathbb{X}} \subseteq {\mathbb{R}}^{n_{x}}$ with a joint distribution ${(\mathbf{x},\mathbf{y})} \sim \mathcal{D}$. More precisely, we consider the joint distribution which is absolutely continuous with respect to $\mathbf{x}$ as,

where ${\mathbf{p}_{\theta}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}} \in \mathcal{P}_{\theta}$ is the conditional label distribution and $\theta \in {\mathbb{R}}^{n_{x}}$ are absolute constant parameters. In our MPC setting, $\mathbf{y}$ are labels corresponding to a decision and $\mathbf{x}$ are state-dependent features. Indeed, we aim to obtain an estimate of the conditional distribution by utilizing functions ${{\hat{\mathbf{p}}}_{\theta}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}} \in \mathcal{F}_{\theta}$. To this end, we define a risk measure utilizing the cross-entropy, i.e.,

where $H{(p,q)}$ notes the cross-entropy between two distributions $(p,q)$ and ${\hat{\mathbf{P}}}_{\theta} = {\mathbf{p}{(\mathbf{x})}{\hat{\mathbf{p}}}_{\theta}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}}$. With $n$ i.i.d samples from $\mathcal{D}$ we utilize empirical risk minimization (ERM) by constructing a training set ${\mathbb{D}} = {\{{(x_{i},y_{i})}\}}_{i = 1}^{n}$, and defining an empirical risk measure,

where $\mathbf{1}_{\mathbf{y} = y_{i}}$ is an indicator function for $\mathbf{y} = y_{i}$. The ERM is then obtained by solving the following optimization problem,

Naturally, since the estimate ${\hat{\mathbf{p}}}_{\theta}$ is based on a finite sample of $\mathcal{D}$, the above problem will not return the true distribution. Indeed, we desire a result that is as close to the true distribution as possible. The following section provides a framework for measuring this discrepancy in terms of how well ${\hat{\mathbf{p}}}_{\theta}$ minimizes the risk.

### Excess Risk Bounds

Much work has been dedicated towards deriving bounds on the excess risk for many different machine learning algorithms. Bounds on the excess risk typically take the form of,

for some ${r{(n,\alpha)}} \in {\mathbb{R}}^{+}$, depending on the number of samples $n$, and some probability threshold $\alpha \in {\lbrack 0,1\rbrack}$. Similar to prior work in DR-MPC, we will assume uniform convergence, which we state more formally with the following assumption.

### Assumption 1 (Uniform Convergence)

Consider the setting of Subsection 3.1 with risk measure $\mathcal{R}_{\mathcal{D}}$ of $\mathbf{p}_{\theta}$ and empirical estimator $\mathcal{R}_{\mathbb{D}}$. Uniform convergence implies,

for any $\epsilon \geq 0$.

Bounds of the type are additionally challenging in the setting of Section 3.1 since the risk is unbounded, but may be obtained by imposing constraints on the random variable $\mathbf{x}$ and $\theta$. Different approaches, e.g., VC-dimensions (vapnik2015uniform), Rademacher complexity (bartlett2002rademacher) or PAC-Bayes bounds (mcallester1998some), yield different constraints with varying restrictiveness in different applications. Note that our approach is flexible with regard to the choice of bound and may be adapted based on $\mathcal{P}_{\theta}$ and $\mathcal{F}_{\theta}$.

### Remark 1

Assumption 1 ‣ 3.2 Excess Risk Bounds ‣ 3 Machine Learning Problem ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems") implies that the empirical risk of the ERM converges to the true risk of the true distribution. In the problem setting of Subsection 3.1, this assumption is satisfied if the function class $\mathcal{F}_{\theta}$ is complex enough to include the true distribution $\mathbf{p}_{\theta}$, i.e., $\mathcal{P}_{\theta} \subseteq \mathcal{F}_{\theta}$. This assumption is identical in principle to prior work, e.g., schuurmans2023general, while allowing us to consider larger families for $\mathcal{P}_{\theta}$ and $\mathcal{F}_{\theta}$.

### Example Problem Formulation

To provide an early intuition for the learning setting, we describe a simple interactive distribution example that will be used later in the simulation study. We will consider a case where $\mathbf{y} \in {\{{- 1},1\}}$ is conditionally Bernoulli distributed as,

where ${\sigma{(z)}} = \frac{1}{1 + {\exp{(z)}}}$ and the parameters $\theta$ are unknown. Additionally, considering constraints on the random variable $\mathbf{x} \in {\mathbb{B}}_{\mathbf{x}} = {\{\mathbf{x}:{{\|\mathbf{x}\|} \leq B}\}}$ and the parameters $\theta \in {\mathbb{B}}_{\theta} = {\{\theta:{{\|\theta\|} \leq R}\}}$, we may utilize a Rademacher complexity bound on the excess risk. We summarize the result with the following proposition.

### Proposition 1 (Excess risk bound example)

Consider the above learning problem with definitions in Subsection 3.1, $\mathbf{x} \in {\mathbb{B}}_{\mathbb{X}}$, ERM, and $\mathcal{F}_{\theta} = {\{{\sigma{({y{\langle x,\theta\rangle}})}}:{{\|\theta\|} \leq R}\}}$. Under Assumption 1 ‣ 3.2 Excess Risk Bounds ‣ 3 Machine Learning Problem ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems"), we may bound the excess risk as,

which holds with probability $1 - \alpha$.

Proof: Application of bartlett2002rademacher.

## Ambiguity sets from Excess Risk

In this section, we will transform our empirical risk bound to a bound on the generalization error of the conditional distribution estimate. To this end, we will construct ambiguity sets that are suitable for obtaining a tractable DR-MPC problem.

A natural approach to account for uncertainty in the distribution estimate is to consider a set of distributions in a certain neighborhood of the estimate. Such sets are often referred to as divergence-based ambiguity sets and typically take the form,

where $\hat{P}$ is a probability estimate, ${{\mathfrak{d}}{(P,\hat{P})}} \in {\mathbb{R}}$ is a divergence measure, and $\epsilon \in {\mathbb{R}}^{+}$ determines the size of the neighborhood (rahimian2019distributionally). Often, $\epsilon$ is selected to ensure probabilistic guarantees on the true distribution's inclusion within the set. We will now show that cross-entropy-based risk measures are closely related to divergence-based ambiguity sets with the following proposition.

### Proposition 2

(Ambiguity Set from Excess Risk)\
Consider the setting of Subsections 3.1, 3.2 where the learning problem has a well defined bound on the excess risk $r{(n,\alpha)}$ as . We may then consider the following ambiguity set,

where $D_{KL}$ is the KL-divergence and $\mathbf{P}_{\theta} \in \mathcal{A}_{\alpha,n}$ with $1 - \alpha$.

Proof: From the definition of the cross entropy we have,

where ${H{(p)}} = {{\mathbb{E}}_{p}{\lbrack{- {\log p}}\rbrack}}$ is the entropy of a distribution $p$. Hence,

Inserting in yields the desired result,

Proposition 2 shows that the excess cross-entropy-based risk provides an ambiguity set for the joint distribution of $\mathbf{x}$ and $\mathbf{y}$. However, problem treats the conditional distribution of $\mathbf{y}$. Further, including does not produce a tractable SMPC problem as: (i) $\mathbf{p}{(\mathbf{x})}$ may be unknown; (ii) The KL-divergence lacks tractable reformulations for many $\mathbf{P}_{\theta}{(\mathbf{x},\mathbf{y})}$ and ${\hat{\mathbf{P}}}_{\theta}{(\mathbf{x},\mathbf{y})}$. To address these issues, we construct an ambiguity set for the conditional distribution with the following proposition.

### Proposition 3 (Conditional Ambiguity Set)

Consider the setting of Section 3.1 where the learning problem has a well defined bound on the excess risk $r{(n,\alpha)}$, as described . For a given $x$ and an ERM of the conditional distribution ${\hat{\mathbf{p}}}_{\theta}{(\left. \mathbf{y} \middle| x \right.)}$, we propose the following ambiguity set.

for which the following holds,

where $\eta:{{\lbrack 0,1\rbrack}\mapsto{\lbrack 0,1\rbrack}}$ is increasing on its domain.

Proof: Expanding the KL-divergence between $\mathbf{P}_{\theta}$ and ${\hat{\mathbf{P}}}_{\theta}$ yields,

which integrates over continuous features $x$ and sums over the discrete labels $y_{i}$. For notational convenience, we introduce $\mathbf{z} = D_{KL}\left( \mathbf{p}_{\theta}{(\mathbf{y}|\mathbf{x})}||{\hat{\mathbf{p}}}_{\theta}{(\mathbf{y}|\mathbf{x})} \right)$ where ${\mathbb{E}}_{\mathbf{x}}{\lbrack\mathbf{z}\rbrack} = D_{KL}\left( \mathbf{P}_{\theta}||{\hat{\mathbf{P}}}_{\theta} \right)$. From the definition of the KL divergence, we have $\mathbf{z} \in {\lbrack 0,\infty)}$ and may consider Markov's inequality as

for some $t \geq 0$. Together with the result of Proposition 2, we consider two dependent events,

By definition, we have ${{\mathbb{P}}{(A)}} \in {\lbrack 0,1\rbrack}$, and by Proposition 2 we have ${{\mathbb{P}}{(A)}} \geq {({1 - \alpha})}$. Event B, where ${{\mathbb{P}}{(B)}} \in {\lbrack 0,1\rbrack}$, describes the complement of with ${{\mathbb{P}}{(B)}} > {1 - \frac{{\mathbb{E}}_{\mathbb{X}}{\lbrack\mathbf{z}\rbrack}}{t}}$. Hence,

We may pick any $t \geq 0$ and consider $t = {\eta{(r)}}$, where $\eta:{{\lbrack 0,1\rbrack}\mapsto{\lbrack 0,1\rbrack}}$ is increasing on its domain. Bayes theorem then gives,

Inserting the definition of B and $\mathbf{z}$, we obtain,

## Learning-based Distributionally Robust Model Predictive Control

With an ambiguity set that quantifies the discrepancy between the true and estimated conditional distributions, our aim is now to solve, accounting for the worst-case distribution in the ambiguity set. To this end, we will reformulate the objective (5a) and chance constraints (5d) using nested risk measures. Formally defining and proving all reformulations in this section requires an extensive review of the existing literature. Hence, we aim to discuss key properties of the reformulations and refer the interested reader to, e.g., schuurmans2023general; sopasakis2019risk; rahimian2019distributionally; shapiro2021lectures for risk measures and DRO, and sopasakis2019risk; chen2022interactive for nested risk. To further ease notation, we will use ${( \cdot )}_{{Ch}{(\iota)}} = {\lbrack{( \cdot )}_{\iota^{+}}\rbrack}_{{\forall\iota^{+}} \in {{Ch}{(\iota)}}}$ to refer to a vector of all ${( \cdot )}_{\iota^{+}}$ children of a node $\iota$.

### Risk Measures in Distributionally Robust Optimization

As is well explored in the literature, e.g., shapiro2021lectures, the KL-divergence-based ambiguity sets can be expressed with an equivalent conic representation. In the case of (15 ‣ 4 Ambiguity sets from Excess Risk ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems")) the conic representation becomes,

where $\mathcal{K}$ is a closed, convex cone, $\nu$ are auxiliary variables, $E$, $F$ are matrices, and $b_{\hat{\theta}}{(x)}$ is a vector-valued function that contains ${\hat{\mathbf{p}}}_{\theta}$. Importantly, as $\mathcal{A}_{n,\alpha}$ is convex and conic in $\mathbf{p}$ and $\nu$, we can construct a coherent, conditional risk measure for a random quantity $\mathbf{Z} \in {\mathbb{R}}^{d}$ as

Provided that strong duality holds, problem can equivalently be expressed as

where $\mathcal{K}^{\ast}$ is the dual cone of $\mathcal{K}$.

### Remark 2

Observe that in the scenario tree setting of Section 2, will be conditioned on the state ${\overline{\mathbf{x}}}_{\iota}$ with $\mathbf{Z}_{{Ch}{(\iota)}}$. Hence, the above risk measure describes the expected $\mathbf{Z}_{{Ch}{(\iota)}}$, subject to the worst-case $\mathbf{p} \in {\mathcal{A}_{n,\alpha}{({\overline{\mathbf{x}}}_{\iota})}}$, which in turn describes the probability of transitions from $\iota$ to $\iota^{+} \in {{Ch}{(\iota)}}$.

### Nested Risk Measures over Scenario Trees

The conditional risk measure can be utilized for a single $\iota$ with children ${Ch}{(\iota)}$. To obtain a distributionally robust version of (5a) and (5d) we need a risk measure that treats all nodes in the scenario tree. To this end, we utilize the nested risk formulation of sopasakis2019risk.

### Nested Risk Objective

Observe that expanding the expectation with respect to $\mathbf{Y}$ in (5a) yields

Given that $\ell$ and $\ell_{f}$ are lower semi-continuous and level-bounded over a closed set, we can formulate for each expectation to construct a version of (5a) that treats the nested risk as,

where ${\overline{\rho}}_{|{( \cdot )}}$ denotes the nested risk objective. As further detailed in sopasakis2019risk, given that is coherent, the nested risk objective omits a tractable dual-reformulation. To this end, a crucial step is to observe that we may consider a recursive formulation of the conditional risk measure in the form

In the case of leaf nodes $\iota^{+} \in {{Ch}{(\iota)}} \subseteq {\mathbb{N}}_{f}$, we naturally have $\gamma_{\iota} = {\rho_{|{\overline{\mathbf{x}}}_{\iota}}\left\lbrack {\ell_{f}{(x_{\iota^{+}})}_{{Ch}{(\iota)}}} \right\rbrack}$. Hence, each $\gamma_{\iota}$ measures the risk of all subsequent reachable nodes in the tree. Expressing for each node in the tree , we can obtain the following reformulation of the nested risk objective,

${{{\min\limits_{\mathbf{U}_{e},\Gamma,\Lambda}\ell}{(\mathbf{x}_{e,0},\mathbf{u}_{e,0})}} + \gamma_{0}}\mspace{216mu}$ (21a)
& {s.t.{{{\lambda_{\iota}^{\top}b_{\hat{\theta}}{({\overline{\mathbf{x}}}_{\iota})}} \leq \gamma_{\iota}},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}}} \\
& {{{E^{\top}\lambda_{\iota}} = {\gamma_{{Ch}{(\iota)}} + {\ell{(\mathbf{x}_{e,\iota^{+}},\mathbf{u}_{e,\iota^{+}})}_{{Ch}{(\iota)}}}}},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\Pr{({\mathbb{N}}_{f})}}}}} \\
& {{{E^{\top}\lambda_{\iota}} = {\ell_{f}{(\mathbf{x}_{e})}_{{Ch}{(\iota)}}}},{{\forall\iota} \in {\Pr{({\mathbb{N}}_{f})}}}} \\
& {{{F^{\top}\lambda_{\iota}} = 0},{{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}};{{\lambda_{\iota} \succeq_{\mathcal{K}^{\ast}}0},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}}}}

where $\Gamma = {\lbrack\gamma_{\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$ and $\Lambda = {\lbrack\lambda_{\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$ gathers the additional optimization variables. The full proof is available in sopasakis2019risk with an applied version in chen2022interactive. To ease notation, we gather all constraints (21b) with $\Omega_{\ell,\ell_{f}} = {\{{(\overline{\mathbf{X}},\mathbf{U}_{e},\Gamma,\Lambda)}:{{\text{(}\text{)}}\left| {\overline{\mathbf{x}}}_{0} \right.}\}}$.

### Nested Risk Constraints

We will now derive the corresponding distributionally robust chance constraints of (5d), utilizing the same nested risk framework. Following borve2025tight, we may express an outer approximation of the joint chance constraints over the scenario tree as,

where $\mathbb{1}_{{\mathbb{R}}^{+}}:{{\mathbb{R}}\mapsto{\{ 0,1\}}}$ is an indicator function of the positive real line, and ${\sigma_{b,\beta}{(x)}} = {b/{({1 + {\exp{({- {\betax}})}}})}}$ is a sigmoid function. Here, (i) follows from Boole's inequality and (ii) follows by picking $b$ and $\beta$ such that $\sigma_{b,\beta} \in {{Epi}\, 1_{{\mathbb{R}}^{+}}}$, where $Epi$ denotes the epigraph. One can directly observe that the result of has a similar structure to that of the objective. As $\sigma_{b,\beta} \circ g$ is continuous and level bounded over a closed set, the reformulation of the nested risk chance constraints follows in a similar manner to that of the nested risk objective. For brevity, we forego repeating the same arguments. Similar to the objective, we will introduce auxiliary variables, $\delta_{\iota} \in {\mathbb{R}}$, $\Delta = {\lbrack\delta_{\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$, to describe the corresponding version of and $\mu_{\iota}$, $M = {\lbrack\mu_{\iota}\rbrack}_{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}$ to describe the dual variables of the conditional risk measures. To again ease notation, we introduce a set $\Omega_{\sigma_{b,\beta} \circ g}$ to gather the constraints of the corresponding nested risk chance constraints.

### DR-MPC Problem Formulation

With a Distributionally robust formulation of (5a) and (5d) we can now construct the complete DR-MPC problem.

$\min\limits_{\substack{\mathbf{U}_{e},\Gamma,\Lambda \\ \Delta,M}}$ ${\ell{(\mathbf{x}_{e,0},\mathbf{u}_{e,0})}} + \gamma_{0}$ (23a)
${s.t}.$ ${{\overline{\mathbf{x}}}_{\iota^{+}} = {f{({{{\overline{\mathbf{x}}}_{\iota},\left. {\overline{\mathbf{u}}}_{\iota} \middle| \mathbf{y}_{\iota} \right.} = y_{\iota^{+}}})}}},{{{\forall\iota^{+}} \in {{Ch}{(\iota)}}},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}}$ (23b)
${\delta_{0} \leq \varepsilon};{{(\overline{\mathbf{X}},\mathbf{U}_{e},\Delta,M)} \in \Omega_{\sigma_{b,\beta} \circ g}}$ (23c)
${(\overline{\mathbf{X}},\mathbf{U}_{e},\Gamma,\Lambda)} \in \Omega_{\ell,\ell_{f}}$ (23d)
${\mathbf{x}_{e,\iota} \in {\mathbb{X}}_{e}},{{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}};{{\mathbf{u}_{e,\iota} \in {\mathbb{U}}_{e}},{{\forall\iota} \in {{\mathbb{N}} \smallsetminus {\mathbb{N}}_{f}}}}}$ (23e)
${{{\overline{\mathbf{x}}}_{0} = {\overline{\mathbf{x}}{(t)}}};{{\mathbf{x}_{e,\iota} \in {\mathbb{X}}_{e,f}},{{\forall\iota} \in {\mathbb{N}}_{f}}}}.$ (23f)

Here, (23a) describes the distributionally robust objective with corresponding constraints (23d), (23b) describes the dynamics, (23c) describes the distributionally robust, joint chance constraints, (23e) describes ego-agent limitations, and (23f) describes the boundary conditions. In a closed-loop setting, is solved at each discrete time, given the current traffic state $\overline{\mathbf{x}}{(t)}$, with the ego-agent applying each $\mathbf{u}_{e,0}$. In an open-loop setting, is solved once to obtain the control actions for the entire horizon $\mathbf{U}_{e}$, applying the corresponding actions over the discrete horizon.

## Simulation Study

(a) Initial simulation setup.

Figure 3: Road crossing case. Each color indicates a path through the scenario tree, from root- to leaf node.

We will now demonstrate our methods in an interactive trajectory planning example. To emphasize the properties of proposed method, we will consider a simple road crossing case between an Autonomous System (AS) and a human, see Fig. 3(a). To directly compare the result of the different optimization problems, we will investigate statistical results with the ego-agent adopting an open-loop control strategy.

### Reference Controllers

As a reference for the DR-MPC scheme, we will utilize two alternative MPC designs for solving problem. First, a robust version (R-MPC), which does not utilize an estimate of $\mathbf{p}_{\theta}$ and instead accounts for all possible $\mathbf{x}_{h}$ given $f_{h}$ and $\kappa$, i.e., the collision avoidance constraints are not relaxed in any node, regardless of probability. Similarly, the objective is not weighted based on the probability of each respective node. Second, a stochastic version utilizing the ground truth distribution (GT-SMPC). This problem directly solves, with the expected cost and joint chance-constraint. More details of this reformulation is available in borve2025tight.

### Implementation

Both and were formulated in $CasADi$ (casadi) and solved with $IPOPT$ (ipopt). The simulations ran on a laptop equipped with a 12th Gen Intel(R) Core(TM) i7-12850HX CPU and 32 GB of RAM.

### Simulation Specifications

Each agent $i \in {\{ e,h\}}$ is modeled as a one dimensional double integrator with states $\mathbf{x}_{i} = {\lbrack p_{i},v_{i}\rbrack}^{\top}$, control $\mathbf{u}_{i} = {\lbrack a_{i}\rbrack}$, and discrete time dynamics ${f_{i}{(\mathbf{x}_{i},\mathbf{u}_{i})}} = {\lbrack{p_{i} + {v_{i}\Deltat}},{v_{i} + {a_{i}\Deltat}}\rbrack}^{\top}$. In particular, $p_{i}$ reflects each agents position along their road, with the crossing placed in the origin. Both agents are initialized $15\ m$ away from the crossing at $20\ {{km}\ h^{- 1}}$. The human agent may pick from two available decisions: $y_{1}$, corresponding to a breaking maneuver, and $y_{2}$, corresponding to tracking a reference $\mathbf{x}_{ref}$. The control law $\kappa$ is based on the Intelligent Driver Model (IDM), tuned for aggressive brake ($y_{1}$) and smooth reference tracking ($y_{2}$). For the decision distribution we consider a case with $\mathbf{x} = {- {\lbrack{p_{e}/v_{e}},{p_{h}/v_{h}}\rbrack}}$, i.e., reflecting the signed time for the respective agent to reach the intersection, with $\mathbf{p}_{\theta}{(\left. \mathbf{y} \middle| \mathbf{x} \right.)}$ defined as in where $\theta = {\lbrack 3,3\rbrack}$.

### Learner and Control Design

Upper state bound

Lower state bound

Upper control bound

Lower control bound

Table 1: Shared Controller Parameters

Indeed, the number of nodes, and further the number of variables scales exponentially with the length of the prediction horizon. In practice, scenario reduction strategies are often used to tackle this issue (jacobsen2025combined). In this study however, we aim to demonstrate the statistical properties, in reference to the ground-truth distribution. Hence, we opt for a relatively small $N = 6$, with a relatively large ${\Deltat} = 1.0$ to balance computational complexity. All MPCs consider ${\mathbb{X}}_{e} = {\mathbb{X}}_{e,f} = {\{\mathbf{x}:{\underset{¯}{\mathbf{x}} \leq \mathbf{x} \leq \overline{\mathbf{x}}}\}}$ and ${\mathbb{U}}_{e} = {\{\mathbf{u}:{\underset{¯}{\mathbf{u}} \leq \mathbf{u} \leq \overline{\mathbf{u}}}\}}$, with ${\ell{(\mathbf{x}_{e},\mathbf{u}_{e})}} = {{\mathbf{x}_{e}^{\top}{\mathbf{Q}\mathbf{x}}_{e}} + {\mathbf{u}_{e}{\mathbf{R}\mathbf{u}}_{e}}}$ and ${\ell_{f}{(\mathbf{x}_{e})}} = {\mathbf{x}_{e}^{T}{\mathbf{P}\mathbf{x}}_{e}}$. See Table 1 for numerical values. As desired, this yields a challenging scenario, where the ego-vehicle is forced to take risk to improve performance. For the learner we will again consider the setting of Subsection 3.3, with basic definitions in Subsection 3.1. We will further consider Euclidean norms with $B = \sqrt{18}$, and $R = \sqrt{18}$, and $n$ i.i.d measurements of $x_{i}$ and $y_{i}$, assumed available offline. For the ambiguity set of Proposition 3 ‣ 4 Ambiguity sets from Excess Risk ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems"), we consider ${{\eta{(r)}} = \sqrt{r}},{r \in {\lbrack 0,1\rbrack}}$. As displayed in Table 2 we will investigate the solutions of the DR-MPC as the number of data points, and correspondingly as ${\hat{\mathbf{p}}}_{\theta}$ and $r{(\alpha,n)}$, vary.

### Evaluation

Fig. 3(b) provides a qualitative evaluation of the controller properties by displaying the predicted inter-vehicle distance ("Distance Margin"), the probability of violating the distance constraint ("Violation Probability"), and the velocity profiles of the respective vehicles. For a quantitative evaluation we may directly compute metrics by propagating the ground-truth distribution over the respective solutions $\mathbf{X}_{e}$ and $\mathbf{U}_{e}$. To this end, we consider: Expected Cost as the objective function subject to $\mathbf{p}_{\theta}$; Crossing Rate as the rate of which the ego-vehicle crosses before the human; Stopping Rate as the rate of which the human crosses before the ego-vehicle, and Violation Rate as the rate of which the constraint $g$ is violated. The results are displayed in Table 2. The R-MPC baseline attains violation free trajectory plans, but simultaneously obtains a remarkably high expected cost and low crossing rate. The omnipotent GT-SMPC manages to take the highest risk, and correspondingly achieve the highest performance. Recall that the GT-SMPC is not practically realizable as it is assumed to have access to the ground-truth distribution. The result for the DR-MPC can be observed to converge from the R-MPC, towards the GT-SMPC as the number of samples tends towards infinity, across all metrics.

Table 2: Evaluation of Road Crossing Scenario.

### Conclusions and Future Work

The results indicate that the DR-MPC controllers provides a practically realizable method to interpolate between the R-MPC, and GT-SMPC methods based on the available number of samples $n$. The fact that the DR-MPC with $n = 10^{3}$ provides a significant improvement over the robust controller, indicate that there exist some highly unlikely scenarios that significantly strain the performance of the R-MPC. However, we simultaneously observe that convergence towards the GT-SMPC with $n$ is slow. This could indicate that Propositions 1 ‣ 3.3 Example Problem Formulation ‣ 3 Machine Learning Problem ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems") and 3 ‣ 4 Ambiguity sets from Excess Risk ‣ Interactive Trajectory Planning with Learning-based Distributionally Robust Model Predictive Control and Markov Systems") are excessively conservative. Formulating tighter bounds for these propositions could be particularly interesting for practical applications. Further applications of this work could also consider different types of estimators, e.g., neural networks. We are additionally interested in rigorously investigating conditions for control guarantees, such as stability, recursive feasibility and probabilistic constraint satisfaction.

The authors thank Deepthi Pathare, Stefan Börjesson, Markus Gerdin, and Sten Elling Tingstad Jacobsen for insightful discussions concerning the research topic.
