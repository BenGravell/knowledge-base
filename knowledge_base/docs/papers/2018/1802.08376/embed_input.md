<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LQG Control and Sensing Co-Design

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate a Linear-Quadratic-Gaussian (LQG) control and sensing co-design problem, where one jointly designs sensing and control policies. We focus on the realistic case where the sensing design is selected among a finite set of available sensors, where each sensor is associated with a different cost (e.g., power consumption). We consider two dual problem instances: sensing-constrained LQG control, where one maximizes control performance subject to a sensor cost budget, and minimum-sensing LQG control, where one minimizes sensor cost subject to performance constraints. We prove no polynomial time algorithm guarantees across all problem instances a constant approximation factor from the optimal. Nonetheless, we present the first polynomial time algorithms with per-instance suboptimality guarantees. To this end, we leverage a separation principle, that partially decouples the design of sensing and control. Then, we frame LQG co-design as the optimization of approximately supermodular set functions; we develop novel algorithms to solve the problems; and we prove original results on the performance of the algorithms, and establish connections between their suboptimality and control-theoretic quantities.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We conclude the paper by discussing two applications, namely, sensing-constrained formation control and resource-constrained robot navigation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional approaches to systems control assume the choice of sensors fixed. The sensors usually result from a preliminary design phase in which an expert selects a suitable sensor suite that accommodates estimation requirements, and system constraints (e.g., power consumption). However, the control applications of the Internet of Things (IoT) and Battlefield Things (IoBT), pose serious limitations to the applicability of this traditional paradigm. Now, systems are not designed from scratch; instead, existing, standardized systems come together, along with their sensors, to form heterogeneous teams (such as robot teams), tasked with various control goals: from collaborative object manipulation to formation control. In such heterogeneous networked systems, where new nodes are continuously added and removed from the network, sensor redundancies are created, depending on the task at hand. At the same time, power, bandwidth, and/or computation constraints limit which sensors can be active Therefore, to optimize the network's operability and prolong its operation, one needs to decide which sensors are important for the task, and activate only these. Evidently, in large-scale networks a manual activation policy is not scalable. Thus, ones needs to develop automated approaches.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by this need, we consider the co-design of LQG control and sensor selection subject to sensor activation constraints. Particularly, we assume that the sensor constraints are captured by a prescribed budget (e.g., available battery power), and that each sensor is associated with an activation cost (e.g., power consumption).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work in control. Traditionally, the control literature has focused on co-designing control, estimation, actuation (i.e., actuator selection), and sensing (i.e., sensor selection).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

a) assume all sensors given and active (instead of choosing a few sensors to activate). They focus on the co-design of control and estimation over band-limited communication channels, and investigate trade-offs between communication constraints (e.g., quantization), and control performance (e.g., stability). In more detail, they provide results on the impact of quantization, and of finite data rates, as well as, on separation principles for LQG design with communication constraints. Recent works also focus on privacy constraints. For a comprehensive review on LQG control and estimation, we refer to.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

b) extend the focus of the above works, by focusing on the co-design of control, estimation, and sensing. Yet, the choice of each sensor can be arbitrary (instead, in our framework, a few sensors are activated from a given finite set of available ones). For example, propose the optimization of steady state LQG costs, subject to sparsity constraints on the sensor matrices and/or on the feedback control and estimation gains. Finally, augment the LQG cost with an information-theoretic regularizer, and design the sensors matrices using semi-definite programming.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

c) focus on sensor selection, but they do not consider control aspects (with the exception of, which we discuss below). Specifically, studies sensor placement to optimize maximum likelihood estimation over static parameters, whereas focus on optimizing Kalman filtering and batch estimation accuracy over non-static parameters. present sensor and actuator selection algorithms to optimize the average observability and controllability of systems; focuses on actuator placement for stability in uncertain systems. For additional relevant applications, we refer to. \[42, Chapter 6.1.3\] focuses on selecting a sensor for each edge of a consensus-type system for $\mathcal{H}_{2}$ optimization subject to sensor cost constraints, and sensor noise considerations (instead, we consider general systems). selects the location of a phasor measurement unit (PMU) on a single edge of an electrical network to minimize estimation error (each placement happens independently of the rest).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

study sensor placement to optimize a steady state LQG cost; although the latter case is similar to our framework (we optimize a finite horizon LQG cost, instead of a steady state), the authors focus only on a small-scale system with a few sensors, where a brute-force selection is viable, and no scalable algorithms are proposed (instead, our focus is on scalable approximation algorithms). Finally, studies an LQG control and scheduling co-design problem, where decoupled systems share a wireless sensor network, while power consumption constraints must be satisfied. Instead, we consider coupled systems, a framework that makes our co-design problem inapproximable in polynomial time, in contrast to 's, which is optimally solved in polynomial time.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work on set function optimization. In this paper, a few sensors must be activated among a set of available ones. This is a combinatorial problem, and we prove it inapproximable: across all problem instances, no polynomial time algorithm can guarantee a constant approximation factor from the optimal. Thus, to provide efficient algorithms with per-instance suboptimality bounds instead, we resort to tools from combinatorial optimization, which has been a successful paradigm on this front. Specifically, the literature on combinatorial optimization includes investigation into (i) supermodular optimization subject to cardinality constraints (where only a prescribed number of sensors can be active); (ii) supermodular optimization subject to cost constraints (where only sensor combinations that meet a prescribed budget can be active ---each sensor has a potentially different activation cost); and (iii) approximately supermodular optimization subject to cardinality constraints.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The literature does not cover approximately submodular optimization subject to cost constraints, which is the setup of interest in this paper; hence we herein develop algorithms and novel suboptimality bounds for this case.^11^1The transition from cardinality to cost constraints, in terms of providing efficient algorithms with provable suboptimality bounds, is non-trivial, as it is observed by comparing the widely different proof techniques, for the cardinality case, versus those considered in this paper, for the cost case.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions to control theory. We address an *LQG control and sensing co-design* problem. The problem extends LQG control to the case where, besides designing an optimal controller and estimator, one has to decide which sensors to activate, due to sensor cost constraints and a limited budget. That is, the sensor choice is restricted to a finite selection from the available sensors, rather than being arbitrary (for arbitrary sensing design, see ). And each sensor has a cost that captures the penalty incurred for using the sensor. Since different sensors (e.g., lidars, radars, cameras, lasers) have different power consumption, bandwidth utilization, and/or monetary value, we allow each sensor to have a different cost. We formulate two dual instances of the LQG co-design problem. The first, *sensing-constrained LQG control*, involves the joint design of control and sensing to minimize the LQG cost subject to a sensor cost budget. The second, *minimum-sensing LQG control*, involves the joint design of control and sensing to minimize the cost of the activated sensors subject to a desired LQG cost.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

To solve the proposed LQG problems, we first leverage a separation principle that partially decouples the control and sensor selection.^22^2The separation between control and sensor selection is proved with the same steps as the separation of control and estimation in standard LQG control theory; e.g., see proof of Lemma 1. As a negative result, we prove the optimal sensor selection is inapproximable in polynomial time by a constant suboptimality bound across all problem instances. Therefore, we develop algorithms with per-instance suboptimality bounds instead. Particularly, we frame the sensor selection as the optimization of approximately supermodular set functions, using the notion of supermodularity ratio introduced in 2006 in (see also ).^33^3The notion has met already increasing interest in the signal processing and control literature; see, for example,. Then, we provide the first polynomial time algorithms, which provably retrieve a close-to-optimal choice of sensors, and the corresponding optimal control policy.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, the suboptimality gaps of the algorithms depend on the supermodularity ratio $\gamma$ of the LQG cost, and we establish connections between $\gamma$ and control-theoretic quantities, providing computable lower bounds for $\gamma$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions to set function optimization. To prove the aforementioned results, we extend the literature on supermodular optimization. Particularly, we provide the first efficient algorithm for approximately supermodular optimization (e.g., LQG cost optimization) subject to cost constraints for subset selection (e.g., sensor selection). To this end, we use the algorithm, proposed for exactly supermodular optimization, and prove it maintains provable suboptimality bounds for even approximately supermodular optimization. Importantly, our bounds improve the previously known bounds for exactly supermodular optimization: our bounds become $1 - {1/e}$ for supermodular optimization, tightening the known ${1/2}{({1 - {1/e}})}$. Noticeably, $1 - {1/e}$ is the best possible bound in polynomial time for supermodular optimization subject to cardinality constraints.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

That way, our analysis equates the approximation difficulty of cost and cardinality constrained optimization for the first time (among all algorithms with at most quadratic running time).^44^4Other algorithms, that either achieve the $1 - {1/e}$ bound but are slower ($O{(n^{5})}$ instead of $O{(n^{2})}$ that ours is), or they achieve looser bounds with the same running time, such as the $1 - {1/\sqrt{e}}$, are found. That way, our results are relevant beyond sensing in control, such as in cost effective outbreak detection in networks.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similarly, we provide the first algorithm for minimal cost subset selection subject to desired bounds on an approximately supermodular function. The algorithm relies on a simplification of the algorithm. Leveraging our novel bounds, we show the algorithm is the first with provable suboptimality bounds given approximately supermodular functions. Notably, for exactly supermodular functions the bound recovers the well-known bound for cardinality minimization; that way, similarly to above, our analysis equates the approximation difficulty of cost and cardinality minimization for the first time.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Application examples. We demonstrate the effectiveness of the proposed algorithms in numerical experiments, by considering two application scenarios: *sensing-constrained formation control*, and *resource-constrained robot navigation*. We present a Monte Carlo analysis for both, which demonstrates that (i) the proposed sensor selection strategy is near-optimal, and, particularly, the resulting LQG cost matches the optimal selection in all tested instances for which the optimal selection could be computed via a brute-force approach; (ii) a more naive selection which attempts to minimize the state estimation error (rather than the LQG cost) has degraded LQG performance, often comparable to a random selection; and (iii) the selection of a small subset of sensors using the proposed algorithms ensures an LQG cost that is close to the one obtained by using all available sensors, hence providing an effective alternative for control under sensing constraints.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comparison with the preliminary results in (which coincides with the preprint ). This paper (which coincides with the preprint ) extends the preliminary results, and provides comprehensive presentation of the LQG co-design problem, by including both the *sensing-constrained LQG control* (introduced in ) and the *minimum-sensing LQG control* problem (not previously published). Moreover, we generalize the setup in to account for any sensor costs (in each sensor has unit cost, whereas herein sensors have different costs). Also, we extend the numerical analysis accordingly. Moreover, we prove the inapproximability of the problem. Most of the technical results (Theorems 1. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")-4. ‣ IV-C Performance analysis for Algorithm 3 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design"), and Algorithms 2-4) are novel, and have not been published.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Organization of the rest of the paper. Section II formulates the LQG control and sensing co-design problems. Section III presents a separation principle, the inapproximability theorem, and introduces the algorithms for the co-design problems. Section IV characterizes the performance of the algorithms, and establishes connections between their suboptimality bounds and control-theoretic quantities. Section V presents two examples of the co-design problems. Section VI concludes the paper. All proofs are given in the appendix.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation: LQG Control and Sensing Co-design", "weight": 1.0} -->

Here we formalize the LQG control and sensing co-design problem considered in this paper. Specifically, we present two "dual" statements of the problem: the *sensing-constrained LQG control*, and the *minimum-sensing LQG control*.

<!-- chunk {"id": "body-0023", "role": "body", "section": "System", "weight": 1.0} -->

We consider a discrete-time time-varying linear system with additive Gaussian noise,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sensors", "weight": 1.0} -->

We consider the availability of a (potentially large) set $\mathcal{V}$ of sensors, which can take noisy linear observations of the system's state. Particularly,

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sensors", "weight": 1.0} -->

When only a subset $\mathcal{S} \subseteq \mathcal{V}$ of the sensors is active for all $t = {1,2,\ldots,T}$, then the measurement model becomes

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sensors", "weight": 1.0} -->

Each sensor is associated with a (possibly different) cost, which captures, for example, the sensor's monetary cost, its power consumption, or its bandwidth utilization. Specifically, we denote the *cost of sensor* $i$ by ${c{(i)}} \geq 0$; and the *cost of a sensor set* $\mathcal{S}$ by $c{(\mathcal{S})}$, where we set

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B LQG co-design problems", "weight": 1.0} -->

We define two versions of the co-design problem: *sensing-constrained LQG control* and *minimum-sensing LQG control*.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B LQG co-design problems", "weight": 1.0} -->

where $Q_{1},\ldots,Q_{T}$ are known positive semi-definite matricies, $R_{1},\ldots,R_{T}$ are known positive definite matricies, and the expectation is taken with respect to $x_{1}$, $w_{1:T}$, and $v_{1:T}{(\mathcal{S})}$. Particularly, the *sensing-constrained LQG control* minimizes the LQG cost subject to a sensor cost budget, and the dual *minimum-sensing LQG control* minimizes the sensor cost subject to a desired LQG cost.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 1 (Sensing-constrained LQG control)", "weight": 1.0} -->

Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") models the practical case where we cannot activate all sensors (due to power, cost, or bandwidth constraints), and instead need to activate a few sensors to optimize control performance. If the budget is increased so all sensors can be active, then Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") reduces to standard LQG control.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem 2 (Minimum-sensing LQG control)", "weight": 1.0} -->

Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") models the practical case where one wants to design a system with a prescribed performance, while incurring in the smallest sensor cost.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Co-design Principles, Hardness, and Algorithms", "weight": 1.0} -->

We leverage a separation principle to derive that the optimization of the sensor set $\mathcal{S}$ and of the control policy $u_{1:T}{(\mathcal{S})}$ can happen in cascade. However, we show that optimizing for $\mathcal{S}$ is inapproximable in polynomial time. Nonetheless, we then present polynomial time algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") and Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") with provable per-instance suboptimality bounds. Particularly, the bounds are presented in Section IV.^55^5The novelty of the algorithms is also discussed in Section IV.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Separability of optimal sensing and control design", "weight": 1.0} -->

We characterize the jointly optimal control and sensing solutions for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") and Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"), and prove they can be found in two separate steps, where first the sensor set is found, and then the control policy is computed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 2 (Certainty equivalence principle)", "weight": 1.0} -->

The control gain matrices $K_{1},K_{2},\ldots,K_{T}$ are the same as the ones that make the controllers $(K_{1}x_{1}$, $K_{1}x_{2},\ldots,K_{T}x_{T})$ optimal for the perfect state-information version of Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"), where the state $x_{t}$ is known to the controllers \[1, Chapter 4\].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 2 (Certainty equivalence principle)", "weight": 1.0} -->

Theorem 1. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design") decouples the sensing design from the control policy design. Particularly, once an optimal sensor set $\mathcal{S}^{\star}$ is found, then the optimal controllers are equal to $K_{t}{\hat{x}}_{t}{(\mathcal{S}^{\star})}$, which correspond to the standard LQG control policy.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2 (Certainty equivalence principle)", "weight": 1.0} -->

An intuitive interpretation of the sensor design steps in eqs. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) and (12. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) follows next.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3 (Control-aware sensor design)", "weight": 1.0} -->

To provide insight on $\sum_{t = 1}^{T}{\text{tr}{\lbrack{\Theta_{t}\Sigma_{t|t}{(\mathcal{S})}}\rbrack}}$ in eqs. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) and (12. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")), we rewrite it as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3 (Control-aware sensor design)", "weight": 1.0} -->

‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")), each $\text{tr}{\lbrack{\Theta_{t}\Sigma_{t|t}{(\mathcal{S})}}\rbrack}$ captures the mismatch between the imperfect state-information controller ${u_{t}{(\mathcal{S})}} = {K_{t}{\hat{x}}_{t}{(\mathcal{S})}}$ (which is only aware of the measurements from the active sensors) and the perfect state-information controller $K_{t}x_{t}$. That is, while standard sensor selection minimizes the estimation covariance, for instance by minimizing

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3 (Control-aware sensor design)", "weight": 1.0} -->

the proposed LQG cost formulation selectively minimizes the estimation error focusing on the states that are most informative for control purposes. For example, the mismatch contribution in eq. (14. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) of any $x_{t} - {{\hat{x}}_{t}{(\mathcal{S})}}$ in the null space of $K_{t}$ is zero; accordingly, the proposed sensor design approach has no incentive in activating sensors to observe states which are irrelevant for control purposes.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

1:Horizon T; system in eq.; covariance Σ1|1; LQG cost matrices Qt and Rt in eq.; sensors in eq.; sensor budget b; sensor cost c (i), for all i ∈ 𝒱.
2:Active sensors $\hat{\mathcal{S}}$, and controls û1, û2, …, ûT.
4:Return $\hat{\mathcal{S}}$ returned by Algorithm 2, which finds a solution to the optimization problem in eq.;

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

Algorithm 1 Joint sensing and control design for Problem 1.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

We present a practical algorithm for the sensing-constrained LQG control Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") (Algorithm 1). The algorithm follows Theorem 1. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design"): it first computes a sensing design, and then a control design, as described below.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

Sensing design for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"). Theorem 1. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design") implies an optimal sensor design for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") can be computed by solving eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")). To this end, Algorithm 1 first computes $\Theta_{1},\Theta_{2},\ldots,\Theta_{T}$ (Algorithm 1's line 1). Next, since eq. (10.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) is inapproximable (Theorem 2. ‣ III-B Inapproximability of optimal sensing design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")), Algorithm 1 calls a greedy algorithm (Algorithm 2) to compute a solution to eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) (Algorithm 1's line 2).

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

Algorithm 2 computes a solution to eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) as follows: first, Algorithm 2 creates two candidate active sensor sets ${\hat{\mathcal{S}}}_{1}$ and ${\hat{\mathcal{S}}}_{2}$ (lines 3-4), of which only one will be selected as the solution to eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) (line 22). In more detail, Algorithm 2's line 3 lets ${\hat{\mathcal{S}}}_{1}$ be composed of a single sensor, namely the sensor $i \in \mathcal{V}$ that achieves the smallest value of the objective function in eq. (10.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) and has smaller cost than the budget $b$ (${c{(i)}} \leq b$). Then, Algorithm 2's line 4 initializes ${\hat{\mathcal{S}}}_{2}$ with the empty set, and after the construction of ${\hat{\mathcal{S}}}_{2}$ in Algorithm 2's lines 5--21, Algorithm 2's line 22 computes which of ${\hat{\mathcal{S}}}_{1}$ and ${\hat{\mathcal{S}}}_{2}$ achieves the smallest value for the objective function in eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")), and returns this set as the solution to eq. (10.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")).

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

Specifically, Algorithm 2's lines 5--21 construct ${\hat{\mathcal{S}}}_{2}$ as follows: at each iteration of the "while loop" (lines 5-18) a sensor is greedily added to ${\hat{\mathcal{S}}}_{2}$, as long as ${\hat{\mathcal{S}}}_{2}$'s cost does not exceed $b$. Particularly, for each remaining sensor $a$ in $\mathcal{V} \smallsetminus {\hat{\mathcal{S}}}_{2}$, the "for loop" (lines 6-14) computes first the estimation covariance resulting by adding $a$ in ${\hat{\mathcal{S}}}_{2}$, and then the marginal gain in the objective function in eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) (line 13).

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

Afterwards, the sensor inducing the largest marginal gain (normalized by the sensor's cost) is selected (line 15), and is added in ${\hat{\mathcal{S}}}_{2}$ (line 16). Finally, the "if" in lines 19-21 ensure ${\hat{\mathcal{S}}}_{2}$ has cost at most $b$, by removing last sensor added in ${\hat{\mathcal{S}}}_{2}$ if necessary.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

Control design for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"). Theorem 1. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design") implies that given a sensor set, the controls for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") can be computed according to the eq. (11. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")).

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-C Co-design algorithms for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

To this end, Algorithm 1 first computes $K_{1},K_{2},\ldots,K_{T}$ (line 3), and then, at each time $t = {1,2,\ldots,T}$, the Kalman estimate of the current state $x_{t}$ (line 4), and the corresponding control (line 5).

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-D Co-design algorithms for Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

This section presents a practical algorithm for Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") (Algorithm 3). Since the algorithm shares steps with Algorithm 1, we focus on the different ones.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-D Co-design algorithms for Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design\")", "weight": 1.0} -->

Particularly, as Algorithm 1 calls Algorithm 2 to solve eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")), similarly, Algorithm 3 calls Algorithm 4 to solve eq. (12. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")). Algorithm 4 is similar to Algorithm 2, with the difference that Algorithm 4 selects sensors until the upper bound $\overline{\kappa}$ in eq. (12. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) is met (Algorithm 4's line 3), whereas Algorithm 2 selects sensors up to the point the cost budget $b$ is violated (Algorithm 2's line 3).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Performance guarantees for LQG co-design", "weight": 1.0} -->

We now quantify the suboptimality and running time of Algorithms 1 and Algorithms 3. Particularly, we prove both algorithms enjoy per-instance suboptimality bounds,^66^6Instead of constant suboptimality bounds across all instances, which is impossible due to Theorem 2. ‣ III-B Inapproximability of optimal sensing design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design"). and run in quadratic time. To this end, we present a notion of supermodularity ratio (Definition 3. ‣ IV-A Supermodularity ratio ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design")), which we use to prove the suboptimality bounds. We then establish connections between the ratio and control-theoretic quantities (Theorem 5.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Performance guarantees for LQG co-design", "weight": 1.0} -->

‣ IV-D Conditions for γ_g>0 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design")), and conclude that the algorithms' suboptimality bounds are non-vanishing under control-theoretic conditions encountered in most real-world systems (Theorem 6. ‣ IV-D Conditions for γ_g>0 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design")).

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-A Supermodularity ratio", "weight": 1.0} -->

To present the definition of *supermodularity ratio*, we start by defining monotonicity and supermodularity.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Performance analysis for Algorithm 1", "weight": 1.0} -->

We quantify Algorithm 1's running time and suboptimality, using the notion of supermodularity ratio.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-B Performance analysis for Algorithm 1", "weight": 1.0} -->

${h^{\star} \triangleq {{{\min_{\mathcal{S} \subseteq {\mathcal{V},{u_{1:T}{(\mathcal{S})}}}}h}{\lbrack\mathcal{S},{u_{1:T}{(\mathcal{S})}}\rbrack}},s}}.t.{{c{(\mathcal{S})}} \leq b}$, i.e., the optimal value of Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design");

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-B Performance analysis for Algorithm 1", "weight": 1.0} -->

${b^{\star} \triangleq {{{\min_{\mathcal{S} \subseteq {\mathcal{V},{u_{1:T}{(\mathcal{S})}}}}c}{(\mathcal{S})}},s}}.t.{{h{\lbrack\mathcal{S},{u_{1:T}{(\mathcal{S})}}\rbrack}} \leq \kappa}$, i.e., the optimal value of Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design").

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 4 (Novelty of algorithm and bounds)", "weight": 1.0} -->

Algorithm 1 is the first scalable algorithm for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"). Notably, although Algorithm 2 (used in Algorithm 1) is the same as the Algorithm 1, the latter was introduced for *exactly supermodular* optimization, instead of *approximately supermodular optimization*, which is the optimization framework in this paper. Therefore, one of our contributions with Theorem 3. ‣ IV-B Performance analysis for Algorithm 1 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design") is to prove Algorithm 2 maintains suboptimality bounds even for approximately supermodular optimization. The novel bounds in Theorem 3.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 4 (Novelty of algorithm and bounds)", "weight": 1.0} -->

‣ IV-B Performance analysis for Algorithm 1 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design") also improve upon the previously known for exactly supermodular optimization: particularly, our bounds can become $1 - {1/e}$ for supermodular optimization (the closer ${c{(\hat{\mathcal{S}})}}/b$ is to 1), tightening the known ${1/2}{({1 - {1/e}})}$. Noticeably, $1 - {1/e}$ is the best possible bound in polynomial time for submodular optimization subject to *cardinality* constraints, instead of the general *cost* constraints in this paper. That way, our analysis equates the approximation difficulty of *cost* and *cardinality* constrained optimization for the first time (among all algorithms with at most quadratic running time in the number of available elements in $\mathcal{V}$, i.e., those, and ours).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 4 (Novelty of algorithm and bounds)", "weight": 1.0} -->

All in all, Theorem 3. ‣ IV-B Performance analysis for Algorithm 1 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design") guarantees that Algorithm 1 achieves a close-to-optimal solution for Problem 1. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"), whenever $\gamma_{g} > 0$. In Section IV-D we present conditions such that $\gamma_{g} > 0$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 4 (Novelty of algorithm and bounds)", "weight": 1.0} -->

Finally, Theorem 3. ‣ IV-B Performance analysis for Algorithm 1 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design") also quantifies the scalability of Algorithm 1. Particularly, Algorithm 1's running time $O{({{|\mathcal{V}|}^{2}Tn^{2.4}})}$ is in the worst-case quadratic in the number of available sensors $\mathcal{V}$ (when all must be chosen active), and linear in the Kalman filter's running time: specifically, the multiplier $Tn^{2.4}$ is due to the complexity of computing all $\Sigma_{t|t}$ for $t = {1,2,\ldots,T}$ \[1, Appendix E\].

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 5 (Novelty of algorithm and bound)", "weight": 1.0} -->

Algorithm 3 is the first scalable algorithm for Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design"). Importantly, Algorithm 4, used in Algorithm 3, is the first scalable algorithm with suboptimality guarantees for the problem of *minimal cost set selection* where a bound to an *approximately* supermodular $g$ must be met. Particularly, Algorithm 4, generalizes previous algorithms that focus instead on *minimal cardinality* set selection subject to bounds on an *exactly* supermodular function $g$ (in which case, $\gamma_{g} = 1$). Notably, for $\gamma_{g} = 1$, ineq. (19. ‣ IV-C Performance analysis for Algorithm 3 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design"))'s bound recovers the guarantee established in \[48, Theorem 1\].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 5 (Novelty of algorithm and bound)", "weight": 1.0} -->

All in all, ineq. (18. ‣ IV-C Performance analysis for Algorithm 3 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design")) implies Algorithm 3 returns a solution to Problem 2. ‣ II-B LQG co-design problems ‣ II Problem Formulation: LQG Control and Sensing Co-design ‣ LQG Control and Sensing Co-Design") with the prescribed LQG performance. And parallel to ineq. (17. ‣ IV-B Performance analysis for Algorithm 1 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design")), ineq. (19. ‣ IV-C Performance analysis for Algorithm 3 ‣ IV Performance guarantees for LQG co-design ‣ LQG Control and Sensing Co-Design")) implies for $\gamma_{g} > 0$ that Algorithm 3 achieves a close-to-optimal sensor cost.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-D Conditions for $\\gamma_{g} > 0$", "weight": 1.0} -->

We provide control-theoretic conditions such that $\gamma_{g}$ is non-zero, in which case both Algorithm 1 and Algorithm 3 guarantee a close-to-optimal performance. Particularly, we first prove that if ${\sum_{t = 1}^{T}\Theta_{t}} \succ 0$, then $\gamma_{g}$ is non-zero. Afterwards, we show the condition holds true in all problem instances one typically encounters in the real-world. Specifically, we prove ${\sum_{t = 1}^{T}\Theta_{t}} \succ 0$ holds whenever zero control would result in a suboptimal behavior for the system; that is, we prove ${\sum_{t = 1}^{T}\Theta_{t}} \succ 0$ holds in all systems where LQG control improves system performance.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical Evaluations", "weight": 1.0} -->

We consider two applications for the LQG control and sensing co-design framework: *formation control* and *autonomous navigation*. We present a Monte Carlo analysis for both, which demonstrates: (i) the proposed sensor selection strategy is near-optimal; particularly, the resulting LQG cost matches the optimal selection in all instances for which the optimal could be computed via a brute-force approach; (ii) a more naive selection which attempts to minimize the state estimation covariance (rather than the LQG cost) has degraded LQG performance, often comparable to a random selection; (iii) in the considered instances, a clever selection of a small subset of sensors can ensure an LQG cost that is close to the one obtained by using all available sensors, hence providing an effective alternative for control under sensing constraints.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

Simulation setup. The application scenario is illustrated in Fig. 2(a). A team of $n$ agents (blue triangles) moves in 2D. At $t = 1$, the agents are randomly deployed in a ${{10m} \times 10}m$ square. Their objective is to reach a target formation shape (red stars); in Fig. 2(a) the desired formation has an hexagonal shape, while in general for a formation of $n$, the desired formation is an equilateral polygon with $n$ vertices. Each robot is modeled as a double-integrator, with state $x_{i} = {\lbrack{p_{i}v_{i}}\rbrack}^{\mathsf{T}} \in {\mathbb{R}}^{4}$ ($p_{i}$ is agent $i$'s position, and $v_{i}$ its velocity), and can control its acceleration $u_{i} \in {\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

The process noise is a diagonal matrix $W = {{diag}\left( {\lbrack{1e^{- 2}},{\;1e^{- 2}},{\;1e^{- 4}},{\;1e^{- 4}}\rbrack} \right)}$. Each robot $i$ is equipped with a GPS, which measures the agent position $p_{i}$ with a covariance $V_{{gps},i} = {2 \cdot \mathbf{I}_{2}}$. Moreover, the agents are equipped with lidars allowing each agent $i$ to measure the relative position of another agent $j$ with covariance $V_{{lidar},{ij}} = {0.1 \cdot \mathbf{I}_{2}}$. The agents have limited on-board resources, hence they want to activate only $k$ sensors.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

For our tests, we consider two setups. In the first, named *homogeneous formation control*, the LQG weight matrix $Q$ is a block diagonal matrix with $4 \times 4$ blocks, and each block $i$ chosen as $Q_{i} = {0.1 \cdot \mathbf{I}_{4}}$; since each block of $Q$ weights equally the tracking error of a robot, in the homogeneous case the tracking error of all agents is equally important. In the second setup, named *heterogeneous formation control*, $Q$ is chose as above, except for one of the agents, say robot 1, for which we choose $Q_{1} = {10 \cdot \mathbf{I}_{4}}$; this setup models the case in which each agent has a different role or importance, hence one weights differently the tracking error of the agents. In both cases the matrix $R$ is chosen to be the identity matrix. The simulation is carried on over $T$ time steps, and $T$ is also chosen as LQG horizon.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

Results are averaged over 100 Monte Carlo runs: at each run we randomize the initial estimation covariance $\Sigma_{1|1}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

Compared techniques. We compare five techniques. All techniques use an LQG-based estimator and controller, and they only differ by the selections of the active sensors. The first approach is the optimal sensor selection, denoted as optimal, which attains the minimum in eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")), and which we compute by enumerating all possible subsets. The second approach is a pseudo-random sensor selection, denoted as random^∗^, which selects all the GPS measurements and a random subset of the lidar measurements. The third approach, denoted as logdet, selects sensors so to minimize the average $\log\det$ of the estimation covariance over the horizon; this approach resembles and is agnostic to the control task. The fourth approach is the proposed sensor selection strategy (Algorithm 2), and is denoted as s-LQG. Finally, we also report the LQG performance when all sensors are selected. This approach is denoted as allSensors.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

Results. The results of the numerical analysis are reported in Fig. 3. When not specified otherwise, we consider a formation of $n = 4$ agents, which can only use a total of $k = 6$ sensors, and a control horizon $T = 20$. Fig. 3(a) shows the LQG cost for the homogeneous case and for increasing horizon. We note that, in all tested instance, the proposed approach s-LQG matches the optimal selection optimal, and both approaches are relatively close to allSensors, which selects all the available sensors. On the other hand, logdet leads to worse tracking performance, and is often close to random^∗^. These considerations are confirmed by the heterogeneous setup, in Fig. 3(b).

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

In this case, the separation between our proposed approach and logdet becomes even larger; the intuition is that the heterogeneous case rewards differently the tracking errors at different agents, hence while logdet attempts to equally reduce the estimation error across the formation, the proposed approach s-LQG selects sensors in a task-oriented fashion, since the matrices $\Theta_{t}$ for all $t = {1,2,\ldots,T}$ in the cost function in eq. (10. ‣ III-A Separability of optimal sensing and control design ‣ III Co-design Principles, Hardness, and Algorithms ‣ LQG Control and Sensing Co-Design")) incorporate the LQG weight matrices.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

Fig. 3(c) shows the LQG cost attained for increasing number of selected sensors $k$ and for the homogeneous case. For increasing number of sensors all techniques converge to allSensors (since the entire ground set is selected). Fig. 3(d) shows the same statistics for the heterogeneous case. Now, s-LQG matches allSensors earlier, starting at $k = 7$; intuitively, in the heterogeneous case, adding more sensors may have marginal impact on the LQG cost (e.g., if the cost rewards a small tracking error for robot 1, it may be of little value to take a lidar measurement between robot 3 and 4). This further stresses the importance of the proposed framework as a parsimonious way to control a system with minimal resources.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-A Sensing-constrained formation control", "weight": 1.0} -->

Fig. 3(e) and Fig. 3(f) show the LQG cost attained by the compared techniques for increasing number of agents. optimal quickly becomes intractable to compute, hence we omit values beyond $n = 4$. In both figures, the separation among the techniques increases with the number of agents, since the set of available sensors quickly increases with $n$. In the heterogeneous case s-LQG remains relatively close to allSensors, implying that for the purpose of LQG control, using a cleverly selected small subset of sensors still ensures excellent tracking performance.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

Simulation setup. The second application scenario is illustrated in Fig. 2(b). An unmanned aerial robot (UAV) moves in a 3D space, starting from a randomly selected location. The objective of the UAV is to land, and specifically, to reach $\lbrack 0,\;0,\;0\rbrack$ with zero velocity. The UAV is modeled as a double-integrator, with state $x = {\lbrack{pv}\rbrack}^{\mathsf{T}} \in {\mathbb{R}}^{6}$ ($p$ is the position, while $v$ its velocity), and can control its acceleration $u \in {\mathbb{R}}^{3}$. The process noise is $W = \mathbf{I}_{6}$. The UAV is equipped with multiple sensors.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

It has an on-board GPS, measuring the UAV position $p$ with a covariance $2 \cdot \mathbf{I}_{3}$, and an altimeter, measuring only the last component of $p$ (altitude) with standard deviation $0.5m$. Moreover, the UAV can use a stereo camera to measure the relative position of $\ell$ landmarks on the ground; we assume the location of each landmark to be known approximately, and we associate to each landmark an uncertainty covariance (red ellipsoids in Fig. 2(b)), which is randomly generated at the beginning of each run. The UAV has limited on-board resources, hence it wants to use only a few of sensing modalities. For instance, the resource-constraints may be due to the power consumption of the GPS and the altimeter, or may be due to computational constraints that prevent to run multiple object-detection algorithms to detect all landmarks on the ground.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

We consider two sensing-constrained scenarios: (i) all sensors to have the same cost (equal to $1$), in which case, the UAV can activate at most $k$ sensors; (ii) the sensors to have heterogeneous costs: particularly, the GPS's cost is set equal to $3$; the altimeter's cost is set equal to 2; and each landmark's cost is set equal to $1$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

We use $Q = {{diag}\left( {\lbrack{1e^{- 3}},{\;1e^{- 3}},\;10,{\;1e^{- 3}},{\;1e^{- 3}},\;10\rbrack} \right)}$ and $R = \mathbf{I}_{3}$. The structure of $Q$ reflects the fact that during landing we are particularly interested in controlling the vertical direction and the vertical velocity (entries with larger weight in $Q$), while we are less interested in controlling accurately the horizontal position and velocity (assuming a sufficiently large landing site). In the following, we present results averaged over 100 Monte Carlo runs: in each run, we randomize the covariances describing the landmark position uncertainty.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

Compared techniques. We consider the five techniques discussed in the previous section.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

Results. The results of our numerical analysis are reported in Fig. 4 for the case where all sensors have the same sensor-cost, and in Fig. 5 for the case where sensors have different costs. When not specified otherwise, we consider a total of $k = 3$ sensors to be selected, and a control horizon $T = 20$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

In Fig. 4(a) we plot the LQG cost normalized by the horizon, which makes more visible the differences among the techniques. Similarly to the formation control example, s-LQG matches the optimal selection optimal, while logdet and random^∗^ have suboptimal performance. Fig. 4(b) shows the LQG cost attained by the compared techniques for increasing number of selected sensors $k$. All techniques converge to allSensors for increasing $k$, but in the regime in which few sensors are used s-LQG still outperforms alternative sensor selection schemes, and matches optimal.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-B Resource-constrained robot navigation", "weight": 1.0} -->

Fig. 5 shows the LQG cost attained by the compared techniques for increasing control horizon and various sensor cost budgets $b$. Similarly to Fig. 4, s-LQG has the same performance as optimal, whereas logdet and random^∗^ have suboptimal performance. Notably, for $b = 15$ all sensors can be chosen; for this reason in Fig. 5(d) all compared techniques (but the random) have the same performance.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We addressed an LQG control and sensing co-design problem, where one jointly designs control and sensing policies under resource constraints. The problem is central in modern IoT and IoBT control applications, ranging from large-scale networked systems to miniaturized robotic networks. Motivated by the inapproximability of the problem, we provided the first scalable algorithms with per-instance suboptimality bounds. Importantly, the bounds are non-vanishing under general control-theoretic conditions, encountered in most real-world systems. To this end, we also extended the literature on supermodular optimization: by providing scalable algorithms for optimizing approximately supermodular functions subject to heterogeneous cost constraints; and by providing novel suboptimality bounds that improve the known bounds even for exactly supermodular optimization.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

The paper opens several avenues for future research. First, the development of distributed implementations of the proposed algorithms would offer computational speedups. Second, other co-design problems are interesting to be explored, such as the co-design of control-sensing-actuation. Third, while we provide bounds on an approximate sensor design against optimal design, one could provide bounds against the case where all sensors are used. Finally, in adversarial or failure-prone scenarios, one must account for sensor failures; to this end, one could leverage recent results on *robust combinatorial optimization*.
