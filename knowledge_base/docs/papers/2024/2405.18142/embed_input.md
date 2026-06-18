<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Distributionally Robust System Level Synthesis

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel approach for the control of uncertain, linear time-invariant systems, which are perturbed by potentially unbounded, additive disturbances. We propose a doubly robust data-driven state-feedback controller to ensure reliable performance against both model mismatch and disturbance distribution uncertainty. Our controller, which leverages the System Level Synthesis parameterization, is designed as the solution to a distributionally robust finite-horizon optimal control problem. The goal is to minimize a cost function while satisfying constraints against the worst-case realization of the uncertainty, which is quantified using distributional ambiguity sets. The latter are defined as balls in the Wasserstein metric centered on the predictive empirical distribution computed from a set of collected trajectory data. By harnessing techniques from robust control and distributionally robust optimization, we characterize the distributional shift between the predictive and the actual closed-loop distributions, and highlight its dependency on the model mismatch and the uncertainty about the disturbance distribution. We also provide bounds on the number of samples required to achieve a desired confidence level and propose a tractable approximate formulation for the doubly robust data-driven controller.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To demonstrate the effectiveness of our approach, we present a numerical example showcasing the performance of the proposed algorithm.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dealing with uncertainty is a fundamental challenge in many control applications. Oftentimes, the dynamics of the system and the distribution of the disturbance acting on it are unknown and should be accounted. Robust and stochastic approaches have been developed in the last two decades to specifically address both types of uncertainty. Robust methods assume bounded uncertainties and solve a worst-case optimization problem to provide guarantees against any possible realization of the uncertainty. Formulations have been developed to account for uncertainties in both the model and the realization of the disturbance. However, since robust approaches account for all possible realizations of the uncertainties, they neglect any available distributional information, leading to conservative control policies.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic methods can reduce this conservatism by imposing constraints that must be satisfied with a certain probability. However, analytical solutions in the stochastic setting can be obtained only under specific assumptions about the distribution of the uncertainty. Alternatively, randomized methods such as the sample average approximation and the scenario approach can be used to reformulate the stochastic problem into large, but finite-dimensional, deterministic optimization problems. These methods can handle generic distributions and can be applied in the presence of uncertainty in both the dynamics and in the disturbance, as long as these distributions are accessible through sampling. However, sampling-based approaches require a large amount of data to provide tight probabilistic guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following recent developements in the Distributionally Robust (DR) optimization literature, controllers based on DR formulations have been designed to blend the properties of robust and stochastic approaches. Similarly to the stochastic approach, the realizations of the disturbance come from a distribution. However, the distribution is uncertain and is allowed to vary within an ambiguity set; the goal is to optimize the controller performance against the worst-case distribution. The DR approach has been applied in the control setting mainly to provide robustness against additive uncertainties. Typically, current approaches require having access to the *true* model of the systems' dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Departing from prior work, we address the situation where an *approximate model* of the dynamics is given, e.g., it can be obtained from some identification procedure. We are also provided with a limited amount of historical input-state *trajectory data*, which are collected based on possibly closed-loop experiments, and can be used to characterize the disturbance distribution. A major challenge in this setting is that the model mismatch i) leads to erroneous predictions of the system evolution, and ii) makes designing a feedback controller harder. In addition, it also iii) affects our ability to recover the true disturbances from input-state trajectory data. On top of that, we only have access to a finite number of data. These factors will inevitably induce a significant *distribution shift* between the predicted and the actual closed-loop control performance. To address this issue, proposed an open-loop data-driven DR model predictive control formulation that robustly handles uncertainty in both the dynamics and the additive disturbance. Instead, here we study the closed-loop finite-horizon setting with state feedback and probabilistic state and input constraints.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the closed-loop setting is more challenging since it induces additional distribution shifts due to the model uncertainty, which is a well known problem in data-driven control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are the following.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Closed-loop DR formulation: We propose a new distributionally robust data-driven state-feedback controller that is robust against model mismatches and uncertainty in the disturbance distribution. Given a set of input-state data collected from the system and a nominal model of the dynamics, we build the empirical predictive closed-loop distribution of states and inputs for the class of state-feedback controllers. Using the Wasserstein metric, we define an ambiguity set centered around the empirical predictive distribution. Utilizing tools from robust System Level Synthesis (SLS) and DR optimization, we pose the controller design problem as a stochastic optimization problem with respect to the worst-case probability distribution within the ambiguity set. Unlike typical DR optimization settings, where the disturbance is unaffected by the decisions, the presence of feedback changes the statistics of the closed-loop input and state distribution. As a result, we need to allow both the center and the radius of the ambiguity set to depend on the decision variables, i.e., the SLS parameters.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distribution shift characterization: We characterize the distributional shift between the predictive and the actual closed-loop distributions by upper bounding their Wasserstein distance. Hence, by carefully selecting the radius of the ambiguity set, we guarantee that the DR controller is robust against the actual closed-loop distribution with a prescribed confidence level.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Doubly robust solution: Using robust SLS and DR optimization techniques we derive a tractable Linear Programming formulation for the DR optimization problem for piece-wise affine cost and constraint functions. We name it *doubly robust* to highlight its ability to handle model mismatches and small sample sizes. To demonstrate the effectiveness of our approach, we present a numerical example showcasing the performance of the proposed controller.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. In Section 2 we define the problem setting and introduce the SLS formalism. In Section 2.2 we derive the Sample Average Approximation and in Section 2.3 we formally state the distributionally robust control problem. Section 3 analyzes the distributional shift and Section 4 derives a tractable problem formulation for the class of piece-wise linear convex cost and constraint functions. Section 5 describes how to extend the proposed framework to handle arbitrary initial conditions and an affine SLS parametrization. In Section 6 we provide a numerical example that showcases the effectiveness of the proposed algorithm in a range of scenarios. Section 7 concludes the paper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Further related work", "weight": 1.0} -->

Distributionally robust control under known dynamics has been studied extensively. Van Parys et al. address the control of constrained stochastic linear systems with additive uncertainty under DR chance- and CVaR-constraints with second-order moment specifications. The authors in tackle DR model predictive control formulations under moment-based ambiguity sets for the additive disturbance. Taskesen et al. address distributionally robust linear quadratic control with unknown noise distributions within Wasserstein ambiguity sets, as a generalization of the classical Linear-Quadratic-Gaussian control problem. Data-driven DR model predictive control formulation with Wasserstein ambiguity sets has been analyzed. McAllister and Esfahani show how the DR model predictive control formulation can recover important closed-loop properties of both robust and stochastic approaches. Hakobyan and Yang tackle the partially observable case proposing a characterization of the Wasserstein ambiguity set based on the Gelbrich bound of the Wasserstein distance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Further related work", "weight": 1.0} -->

In the case of unknown dynamics, data-driven formulations typically use the data to account for unknown dynamics. The disturbance can be assumed come from a distribution or worst-case. In data-driven DR formulations were considered. They either require full knowledge of the true disturbance distribution or they do not account for the effect of disturbance on the closed-loop trajectories.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Further related work", "weight": 1.0} -->

Our paper leverages tools from System Level Synthesis (SLS), a convex parameterization for feedback design. This setting provides similar advantages to the disturbance affine feedback framework of Goulart et al. and the input-output parametrization of Furieri et al.. The SLS framework also allows for efficient robust control design under model uncertainty, e.g., using ideas from small-gain theory. Brouillon et al. consider a DR controller design using the SLS framework, but they require full knowledge of the true dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider a discrete-time linear time-invariant (LTI) system

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

with (fully measurable) state $x_{k} \in {\mathbb{R}}^{n}$, control input $u_{k} \in {\mathbb{R}}^{m}$. The system is affected by the additive disturbance $w_{k} \in {\mathbb{R}}^{n}$ distributed according to some unknown probability distribution ${\mathbb{P}}_{w}$ defined over the unknown and possibly unbounded support set $\mathcal{W} \subseteq {\mathbb{R}}^{n}$. We are interested in a finite-horizon optimal control problem over some horizon $T$. For this reason, we introduce the following batch notation

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where we concatenate the states, inputs, and disturbances of the system into stacked vectors

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The batch system matrices are defined similarly

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

which maps $x_{0:T}$ to its delayed version $\begin{bmatrix}
\end{bmatrix}^{\top}$. It consists of $T + {1 \times T} + 1$ blocks.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Our objective is to design a policy $\pi$ that minimizes a cost function while satisfying certain specifications. Here, we focus on causal linear state-feedback policies $\pi$ of the form

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where $\mathcal{K}$ is a block-triangular feedback matrix

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We could extend this setup to include an affine term. We can treat it similarly to the feedback term for the initial state, more details in Section 5.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Now, we can formulate the following finite horizon stochastic optimal control problem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The distribution of the disturbance $\mathbf{w}$ and the system dynamics are both assumed to be uncertain, which makes solving challenging. Instead, we assume that we have access to trajectory data generated by system.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1 (Data collection)", "weight": 1.0} -->

We have access to trajectory data in the form of a dataset $\mathcal{D}^{N,{T + 1}}$, comprising $N$ independent $T + 1$-step state-input trajectories $\{\mathbf{x}^{i},\mathbf{u}^{i}\}$, $i = {1,\ldots,N}$, that have been collected by applying inputs $\mathbf{u}^{i}$ of length $T$ to the system. The corresponding initial conditions and disturbances are denoted by

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1 (Data collection)", "weight": 1.0} -->

The initial condition is deterministic and fixed $x_{0}^{i} = x_{0}$, $i = {1,\ldots,N}$ and the same for the trajectory collection phase and the controller deployment phase.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1 (Data collection)", "weight": 1.0} -->

The assumption of fixed $x_{0}$ is for streamlining the presentation. We can relax this requirement and allow $x_{0}$ to vary, see Section 5. We further assume that the true system matrices $A$ and $B$ are unknown, but known to lie within a ball around some nominal system matrices $\hat{A}$ and $\hat{B}$

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 1 (Data collection)", "weight": 1.0} -->

for some ${e_{A},e_{B}} > 0$, where we recall that $\parallel \cdot \parallel$ denotes the $\ell_{1}$ induced norm. The nominal system dynamics $\hat{\mathcal{M}} = \begin{bmatrix}
\hat{\mathcal{A}} & \hat{\mathcal{B}}
\end{bmatrix}$, and thus the model error ${\Delta\mathcal{M}}:=\begin{bmatrix}
{\Delta\mathcal{A}} & {\Delta\mathcal{B}}
\end{bmatrix}$ have the same block diagonal structure as the true $\mathcal{M}$. For clarity of exposition we are assuming here that this bound is deterministic.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1 (Role of data)", "weight": 1.0} -->

In this paper, we use the state-input data to obtain (approximate) disturbance samples (see ). To simplify the presentation, the nominal model $\hat{\mathcal{M}}$ and the bounds $\epsilon_{A},\epsilon_{B}$ are assumed to be given a priori. However, we could use the same data to also perform system identification and obtain such a nominal estimate $\hat{\mathcal{M}}$. In such a case, the uncertainty bounds would hold in a probabilistic sense. The results of this paper can be extended to this setting.

<!-- chunk {"id": "body-0032", "role": "body", "section": "System Level Synthesis", "weight": 1.0} -->

Under, the dynamics can be rewritten as

<!-- chunk {"id": "body-0033", "role": "body", "section": "System Level Synthesis", "weight": 1.0} -->

Note that optimizing over the linear gains $\mathcal{K}$ in is a non-convex problem in general. To deal with this issue, we adopt the SLS framework.

<!-- chunk {"id": "body-0034", "role": "body", "section": "System Level Synthesis", "weight": 1.0} -->

where we define $\Phi:=\begin{bmatrix}
\Phi_{x}^{\top} & \Phi_{u}^{\top}
\end{bmatrix}^{\top}$. By causality, both maps have block-triangular structure

<!-- chunk {"id": "body-0035", "role": "body", "section": "System Level Synthesis", "weight": 1.0} -->

The core idea is to re-parameterize policy and perform the controller synthesis directly on the closed-loop system response matrices $\Phi$ that appear, instead of the state feedback map $\mathcal{K}$. By identifying, the linear feedback parameterization is equivalent to the SLS parameterization under the transformation

<!-- chunk {"id": "body-0036", "role": "body", "section": "System Level Synthesis", "weight": 1.0} -->

when the following condition holds

<!-- chunk {"id": "body-0037", "role": "body", "section": "System Level Synthesis", "weight": 1.0} -->

Note that the above constraint cannot be enforced explicitly as it requires knowledge of the true system matrices $A$, $B$, which are unknown. Since we only have access to the nominal system matrices $\hat{A}$, $\hat{B}$, we replace constraint with

<!-- chunk {"id": "body-0038", "role": "body", "section": "System Level Synthesis", "weight": 1.0} -->

We account for the model error in Section 2.3.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sample Average Approximation", "weight": 1.0} -->

Without any robustness considerations, an effective approach to solving problem is to replace the expectations with the nominal empirical means. This is also known as Sample Average Approximation (SAA). Given $N$ trajectory samples and the nominal model $\hat{\mathcal{M}}$, we can construct a nominal empirical distribution for the disturbances

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sample Average Approximation", "weight": 1.0} -->

where we use $\overline{\mathbb{P}}$ to denote empirical distributions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Sample Average Approximation", "weight": 1.0} -->

Having access to disturbance samples we can simulate the closed-loop performance of a state-feedback policy $\pi:{\mathcal{K} = {\Phi_{u}\Phi_{x}^{- 1}}}$, using the nominal dynamics $\hat{\mathcal{M}}$. Define the empirical predictive distribution of inputs and states as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Sample Average Approximation", "weight": 1.0} -->

The superscript $\hat{\mathcal{M}}$ denotes that we are relying on the nominal model to construct the empirical distribution of the disturbances in and for the system forward simulation, while the subscript $\pi$ denotes the state-feedback policy induced by the feedback matrix $\mathcal{K}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Sample Average Approximation", "weight": 1.0} -->

Following the SAA approach, we optimize the empirical predicted performance, by taking the expectations in the cost and in the constraint with respect to the nominal empirical predictive distribution ${\overline{\mathbb{P}}}_{\pi}^{\hat{\mathcal{M}}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Sample Average Approximation", "weight": 1.0} -->

The SAA formulation has the advantage of being tractable and having strong asymptotic performance guarantees. However, in the presence of model mismatch and when the number of samples $N$ is small, the SAA approach can overfit to the wrong model $(\hat{\mathcal{A}},\hat{\mathcal{B}})$ and the samples ${\mathbf{x}}^{i},{\mathbf{u}}^{i}$, for $i \leq N$, leading to optimistically biased solutions, which is referred to as the optimizer's curse in the optimization literature. This can result in a large discrepancy between the in-sample predicted performance and the out-of-sample closed-loop performance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Sample Average Approximation", "weight": 1.0} -->

This *distribution shift* is a consequence of the fact that, while approximating the true closed-loop distribution ${\mathbb{P}}_{\pi}^{\mathcal{M}}$ by computing the nominal empirical predictive distribution ${\overline{\mathbb{P}}}_{\pi}^{\hat{\mathcal{M}}}$ as, we are wrongfully assuming that i) the nominal model $\hat{\mathcal{M}}$ is an accurate representation of the true unknown model $\mathcal{M}$ and ii) the empirical distribution of the disturbance ${\overline{\mathbb{P}}}_{\hat{\mathbf{w}}}$ obtained from $N$ samples is an accurate representation of the true disturbance distribution ${\mathbb{P}}_{\mathbf{w}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

In practice, the nominal empirical predictive distribution ${\overline{\mathbb{P}}}_{\pi}^{\hat{\mathcal{M}}}$ will inevitably differ from the true closed-loop distribution ${\mathbb{P}}_{\pi}^{\mathcal{M}}$ due to model mismatch and the limited number of samples available. To account for this distribution shift, we follow a distributionally robust approach. We robustify problem against uncertainty in the predictive distribution, by optimizing over the worst-case expectation within a set of probability distributions, which we refer to as an ambiguity set.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

In this paper, we consider ambiguity sets constructed using the Wasserstein metric. The Wasserstein metric is a popular choice for defining ambiguity sets as it can handle distributions with arbitrary supports, including finitely supported ones, making it computationally tractable for data-driven applications. Other types of ambiguity sets, such as those based on the Kullback-Leibler divergence or the total variation distance, may have drawbacks such as not being defined for distributions with different supports. Using the Wasserstein metric, an ambiguity set of radius $\varepsilon > 0$ around a probability measure $\mathbb{P}$ can be defined as

<!-- chunk {"id": "body-0048", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

where the Wasserstein distance $d_{W}{( \cdot, \cdot )}$ is defined. Here, we consider ambiguity sets $\mathcal{B}^{\varepsilon}{({\overline{\mathbb{P}}}_{\pi}^{\hat{\mathcal{M}}})}$, centered around the empirical predictive distribution ${\overline{\mathbb{P}}}_{\pi}^{\hat{\mathcal{M}}}$ with radius $\varepsilon$. Typically, in DR optimization, the radius $\varepsilon$ is a constant and usually treated as a design parameter. In contrast, here we allow $\varepsilon$ to depend on the optimization variables, that is ${\varepsilon:={\varepsilon{(\Phi)}}}.$ Hence, both the ambiguity set center and its radius depend on the closed-loop responses $\Phi$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

By appropriately choosing the function $\varepsilon{(\Phi)}$ we can ensure that the ambiguity set contains the true closed-loop distribution, i.e.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

This would not be possible with a constant radius.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

A DR version of the finite-horizon stochastic optimization problem can now be written as

<!-- chunk {"id": "body-0052", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

In Section 3, we characterize the distribution shift $d_{W}{({\overline{\mathbb{P}}}_{\pi}^{\hat{\mathcal{M}}},{\mathbb{P}}_{\pi}^{\mathcal{M}})}$ as a function of the optimization variable $\Phi$ and provide potential candidate functions for $\varepsilon{(\Phi)}$ so that is satisfied. In this case, solving will provide a control policy that is robust against all the distributions contained in the ambiguity set, including the true (unknown) closed-loop one.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

Informally, this will allow us to claim that if the distributionally robust problem is feasible and its minimizer $\pi^{DR}$, attains a cost $J^{DR}{(\pi^{DR})}$, then, with high confidence, $\pi^{DR}$ is a feasible solution for the original Problem and the resulting cost $J{(\pi^{DR})}$ is upper bounded by the computed $J^{DR}{(\pi^{DR})}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

As is common in robust optimization, the worst-case in the cost and in the constraint are formulated independently, possibly introducing conservatism as the optimization problem optimizes against two separate worst-case distributions.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Distributionally robust formulation", "weight": 1.0} -->

To characterize the distribution shift, we require a technical assumption on the distribution of the multi-step disturbance vector $\mathbf{w}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 2 (Light-tail assumption)", "weight": 1.0} -->

This assumption is a condition on the decay rate of the tail of the probability distribution ${\mathbb{P}}_{\mathbf{w}}$ and is satisfied when $\mathbf{w}$ is sub-Gaussian or when $\mathcal{W}$ is compact. It is required to obtain the finite-sample concentration bound of Lemma 3 below.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Assumption 2 (Light-tail assumption)", "weight": 1.0} -->

Even with an accurate radius $\varepsilon$, we still need to solve. This requires reformulating in a way that makes the solution computationally practical. The main difficulty is that the ambiguity set depends on the optimization variables $\Phi_{x}$ and $\Phi_{u}$, as well as the model uncertainty $\Delta\mathcal{M}$. In Section 4, we employ techniques inspired by robust control (small-gain theory) to obtain such a reformulation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Characterization of the distribution shift", "weight": 1.0} -->

In this section, we upper bound the Wasserstein distance $d_{W}\left( {\overline{\mathbb{P}}}_{\pi}^{\hat{\mathcal{M}}},{\mathbb{P}}_{\pi}^{\mathcal{M}} \right)$ between the predictive empirical distribution and the actual closed-loop one. Since the empirical distribution is a random quantity, we can only provide an upper bound that holds with high probability.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Characterization of the distribution shift", "weight": 1.0} -->

Let us first characterize the actual closed-loop distribution ${\mathbb{P}}_{\pi}^{\mathcal{M}}$ under policy. Note that the nominal system responses $\Phi$, satisfy the affine constraint for the inaccurate nominal dynamics $\hat{\mathcal{M}}$ instead of true model $\mathcal{M}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Characterization of the distribution shift", "weight": 1.0} -->

Following the steps of Section 2.3, we can provide an exact expression for the effect of model mismatch.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Characterization of the distribution shift", "weight": 1.0} -->

where $R_{\Phi} = \left( {I + {\PhiZ\Delta\mathcal{M}}} \right)^{- 1}$. Due to the lower block-triangular structure (consequence of the causality requirement of the controller $\mathcal{K}$) the inverse always exists.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Characterization of the distribution shift", "weight": 1.0} -->

Comparing to, there are two sources of distribution shift: i) the model mismatch $\Delta\mathcal{M}$, and ii) the disturbance distribution uncertainty as we only have a finite number of samples. This distinction becomes transparent by leveraging the triangle inequality, leading to

<!-- chunk {"id": "body-0063", "role": "body", "section": "Characterization of the distribution shift", "weight": 1.0} -->

is the true (unknown) disturbance that affected the sampling of the input-state trajectories ${\mathbf{x}}^{i}$, ${\mathbf{u}}^{i}$, of dataset $\mathcal{D}^{N,T}$. We define

<!-- chunk {"id": "body-0064", "role": "body", "section": "Characterization of the distribution shift", "weight": 1.0} -->

This distribution could have been obtained using the true (unknown) dynamics $\mathcal{M}$, however, since we do not know the true model $\mathcal{M}$, we do not have access to the empirical closed-loop distribution ${\overline{\mathbb{P}}}_{\pi}^{\mathcal{M}}$; we only use it as an intermediate quantity for controlling the distribution shift induced by the closed-loop policy.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 2", "weight": 1.0} -->

If the data in Assumption 1. ‣ 2 Problem formulation ‣ Data-Driven Distributionally Robust System Level Synthesis") is collected using some (known or unknown) controller with closed-loop map $\Phi^{\text{old}}$, as often required in safety-critical applications, we can write

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 2", "weight": 1.0} -->

which highlights that this component can be small when the new controller is close to the one used in the data collection. Note that the right-hand side expression arises implicitly via the data $\mathbf{x}^{i},\mathbf{u}^{i}$ on the left-hand side. We do not need explicit access to a closed-loop map $\Phi^{\text{old}}$. This term could be useful in an episodic learning-based control setting, where the controller is updated across episodes.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The second component captures the distributional shift due to the Wasserstein distance $d_{W}\left( {\overline{\mathbb{P}}}_{\mathbf{w}},{\mathbb{P}}_{\mathbf{w}} \right)$ between the true distribution and the finite-sample empirical distribution of the disturbance. This component persists under zero model error and goes to zero only if the empirical distribution ${\overline{\mathbb{P}}}_{\mathbf{w}}$ approaches the true one ${\mathbb{P}}_{\mathbf{w}}$, i.e., as the number of samples $N$ goes to infinity.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Note that both components depend on the actual closed-loop responses $R_{\Phi}\Phi$. As the model mismatch $\Delta\mathcal{M}$ gets smaller, the closed-loop responses get closer to the nominal ones. In the following, we upper-bound every component separately.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Tractable reformulation", "weight": 1.0} -->

In this section, we use the result of Theorems 1. ‣ 3 Characterization of the distribution shift ‣ Data-Driven Distributionally Robust System Level Synthesis"), 2. ‣ 3 Characterization of the distribution shift ‣ Data-Driven Distributionally Robust System Level Synthesis") to obtain a tractable reformulation that approximates problem. We focus on the class of piece-wise affine cost and constraint functions. In particular, we consider cost functions of the form

<!-- chunk {"id": "body-0070", "role": "body", "section": "Tractable reformulation", "weight": 1.0} -->

for some $N_{J} > 0$. The constraint function is defined similarly

<!-- chunk {"id": "body-0071", "role": "body", "section": "Tractable reformulation", "weight": 1.0} -->

for some $N_{L} \geq 0$. We argue that the above functions describe rich cost and constraint function classes, including $\ell_{1}$-norm objectives, e.g. $\|\mathbf{y}\|$. Dealing with other function classes, such as quadratic, would require changing the type ambiguity set (type-$2$ Wasserstein distance, e.g. ), and lead to a more complex reformulation in presence of model mismatch. We leave that for future work.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Tractable reformulation", "weight": 1.0} -->

As observed from Theorem 1. ‣ 3 Characterization of the distribution shift ‣ Data-Driven Distributionally Robust System Level Synthesis"), the distance between the predictive and actual closed-loop distributions depends on the decision variable $\Phi$. Moreover, the model uncertainty further complicates this coupling, inducing nonlinearities. To deal with the latter, we appeal to small-gain techniques inspired by robust control and recent advances in robust SLS. In particular, we impose a small-gain condition on the maximum allowed magnitude of the system responses $\Phi$, with the gain scaling inversely proportional to the model error. We control the gain using a hyperparameter $\gamma > 0$, over which we optimize.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

We address here the more general case where we allow for arbitrary initial conditions in the data collection and control phases. Following the convention of Assumption 1. ‣ 2 Problem formulation ‣ Data-Driven Distributionally Robust System Level Synthesis"), let

<!-- chunk {"id": "body-0074", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

where $x_{0}^{i}$ is allowed to vary across different data collection experiments.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

We adapt the nominal empirical prediction in as follows

<!-- chunk {"id": "body-0076", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

$x_{0}^{i}$ the initial condition of the $i^{th}$ trajectory in the dataset and $x_{0}$ the new initial condition for the control task. The resulting empirical predictive distribution is defined in the same way as in eq..

<!-- chunk {"id": "body-0077", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

Similarly, we can write the empirical (finite-sample) version of the true closed-loop distribution, for a new initial condition ${\overline{x}}_{0}$ as in but with

<!-- chunk {"id": "body-0078", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

Following a similar derivation as in Section 3, we can decompose the distance using the triangle inequality. The component related to the model mismatch can be upper-bounded following the same procedure as in Lemma 1.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

The bound on the component related to the disturbance distribution uncertainty is unaffected by the new initial condition. This is clear by noting that the first entry of the vectors $\overset{\sim}{\mathbf{w}}$ and ${\mathbf{w}}^{i} + {\overset{\sim}{\mathbf{x}}}_{0}^{i}$ is the same and equal to the known new initial condition for the control task $x_{0}$. With a slight abuse of notation let

<!-- chunk {"id": "body-0080", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

Then, we recover the same bound as in Lemma 2.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Arbitrary initial conditions", "weight": 1.0} -->

Following the derivations in Section 4, we can formulate the small-gain bound for arbitrary initial conditions as follows.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Affine SLS formulation", "weight": 1.0} -->

The results presented in this paper can be naturally extend to the affine system level parametrization formulation. Allowing for a disturbance-affine feedback can be useful for tracking tasks and it can be employed to derive tube-based model predictive control formulations. Whenever the initial condition is not zero, the state-feedback policy ${\mathbf{u}} = {\mathcal{K}{\mathbf{x}}}$ is already equivalent to an affine feedback policy. It is possible, see e.g., to introduce an explicit affine term that does not rely on the initial condition being non-zero, we can augment the dynamics to accommodate extended state and disturbance vectors. The interpretation of the bound remains similar as in the case of linear feedback, but with the extra affine term in the control input.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We highlight the need of robustness against model mismatch and finite sample of the disturbance distribution by means of numerical examples. We do that by showing how the doubly robust formulation can handle perturbations in the model and uncertainty related to limited sample sizes much better than the SAA approach. Our results show that the robustness is not detrimental for the performances of the controller even when the model mismatch is not as large as expected, thus making the doubly robust formulation a viable control design option even when no specific robustness guarantees are required.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Numerical example", "weight": 1.0} -->

with additive disturbance ${\mathbf{w}}_{k} \sim {\mathcal{N}{(0,{0.05I})}}$, and initial conditions $x_{0} = \begin{bmatrix}
\end{bmatrix}^{\top}$. We consider a horizon $T = 10$ and a cost function that regulates the system to the origin

<!-- chunk {"id": "body-0085", "role": "body", "section": "Numerical example", "weight": 1.0} -->

where $\parallel \cdot \parallel$ denotes the $\ell_{1}$ norm, with matrices $\mathbf{Q}$ and $\mathbf{R}$ block diagonal matrices with blocks $Q = \begin{bmatrix}
\end{bmatrix}$ and and $R = \begin{bmatrix}
\end{bmatrix}$ respectively. We add a constraint that, at each timestep $k = {1,\ldots,T}$, constraints the first coordinate of the state to be smaller than $0.8$, i.e.,

<!-- chunk {"id": "body-0086", "role": "body", "section": "Numerical example", "weight": 1.0} -->

This is imposed using the CVaR formulation with $\beta = 0.3$. We assume that we have access to a dataset $\mathcal{D}^{N,T}$ comprising $N = 20$ trajectories of length $T$. These trajectories have been collected from the system starting from the initial conditions $x_{0}$ and applying a state-feedback matrix $K = \begin{bmatrix}
\end{bmatrix}$, i.e. ${\mathbf{u}}_{k}^{i} = {K{\mathbf{x}}_{k}^{i}}$, $k = {1,\ldots,T}$, $i = {1,\ldots,N}$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We also assume we are given nominal system matrices

<!-- chunk {"id": "body-0088", "role": "body", "section": "Numerical example", "weight": 1.0} -->

resulting in mismatches $\epsilon_{A} = \epsilon_{B} = 0.03$. While we assume that the values of $\epsilon_{A}$ and $\epsilon_{B}$ are known, the true dynamics remain unknown. This reflects the practical situations where estimates of the system matrices are obtained through identification, with (often statistical) bounds on the errors. While we consider here the bound on the model error to be known and deterministic, probabilistic bounds can be easily integrated, see for example. In all the simulations we fix the value of $\kappa = 0.005$, this parameter needs to be tuned in practice, for example via cross-validation, see e.g.. We are solving the problem for multiple fixed values of $\gamma \in {}$ and pick the solution that results in the lowest robust optimization cost $J^{RR}$ of Problem 27. ‣ 4 Tractable reformulation ‣ Data-Driven Distributionally Robust System Level Synthesis").

<!-- chunk {"id": "body-0089", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We first compare the optimal solutions of the RR and SAA approaches. In Fig. 1 we compare the predicted optimal trajectories for both algorithms. We can observe that the SAA algorithm plans much more aggressive trajectories. In Fig. 2 we show the closed-loop trajectories produced by the respective controller on the true system for $100$ new realization of the random disturbance vector.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In the previous example, the model uncertainty severely affects the behavior of the plant dominating the closed-loop performance. That is because the sign of the elements $A_{12}$ and $B_{2}$ of the state and input matrix can be flipped resulting in different behaviors. In the following example, we demonstrate the performance obtained for random model mismatch realizations. We do so by sampling random model mismatch matrices $\DeltaA_{p}$, $\DeltaB_{p}$, $p = {1,\ldots,50}$ that are scaled to obtain an uniform random distribution of model mismatches norms ${{\|{\DeltaA_{p}}\|},{\|{\DeltaB_{p}}\|}} \in {\mathcal{U}{\lbrack 0,0.03\rbrack}}$. For every sample of model mismatch we have an independent dataset of $N = 20$ trajectories collected from the true system and we validate the performance against $100$ validation trajectories.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In Fig. 3 we can observe the distribution across the $50$ model realizations of the empirical (over the $100$ validation trajectories) validation cost and CVaR values. The CVaR constraint is to be considered violated if it is larger than $0$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We can observe that, while the optimization costs, i.e. relative to the predicted optimal trajectories, of the SAA are the lowest, the resulting controllers lead to very large validation cost and CVaR values when deployed on the true (unknown) dynamics. Conversely, the RR optimization results in higher optimization costs, that, following Theorem 2. ‣ 3 Characterization of the distribution shift ‣ Data-Driven Distributionally Robust System Level Synthesis"), provide an upper bound on the validation cost attained on the real system. This fact is corroborated by the validation cost attained by the RR. We can make a similar statement for the CVaR constraint that is consistently violated by the SAA and always satisfied by the RR approach. The RR is therefore able to effectively robustify against the distributional shift induced by both the model mismatch and by the offline dataset limited size. This analysis shows that the RR approach is not too conservative with respect to the SAA even when the model error is not fundamentally altering the plant behavior, while it is always able to maintain robustness against the distribution shift.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Numerical example", "weight": 1.0} -->

While some improvement could be obtained for the SAA by increasing the number of samples, which would reduce its sensitivity to the uncertainty in the disturbance distribution, the SAA algorithm does not have a principled way to robustify against the model mismatch.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We remark that, for large values of $\epsilon_{A}$ and $\epsilon_{B}$, the robust problem might be infeasible. This fact is worsened by the suboptimalities introduced by the reformulation that can make the constraints harder to satisfy. A potential solution is to use smaller values for epsilon, e.g. by refining the quality of the available model with further identification experiments, or by collecting more state input trajectories to reduce the uncertainty about the disturbance distribution.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented a novel distributionally robust state-feedback data-driven controller for uncertain discrete-time linear time-invariant systems affected by unknown additive disturbances. We formulated the problem as a stochastic optimization problem with respect to the worst-case probability distribution within an ambiguity set centered on the empirical nominal predictive distribution. Utilizing tools from robust System Level Synthesis and Distributionally Robust optimization we characterized how the controller affects the distributional shift between the predictive and the closed-loop distributions in the presence of uncertainty about both the dynamics and the disturbance distribution. This allowed to bound the size of the decision-dependent ambiguity set, providing finite-sample probabilistic guarantees on the worst-case expectation and CVaR constraint in the presence of uncertainty about both the dynamics and the disturbance distribution.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We derived a tractable Linear Programming formulation for the DR optimization problem for piece-wise affine cost and constraint functions, and demonstrated through numerical examples the effectiveness of the proposed doubly robust approach against the distributional shift which allow to safely control the system without significantly increasing the attained cost, even in presence of model mismatches and very limited information regarding the disturbance distribution.\
Future work focuses on extending this framework to the episodic setting, where the controller and the model are iteratively updated exploiting the collected data.
