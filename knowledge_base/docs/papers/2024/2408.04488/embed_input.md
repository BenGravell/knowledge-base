<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multi-Objective LQR with Linear Scalarization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The framework of decision-making, modeled as a Markov Decision Process (MDP), typically assumes a single objective. However, practical scenarios often involve tradeoffs between multiple objectives. We address this in the Linear Quadratic Regulator (LQR), a canonical continuous, infinite horizon MDP. First, we establish that the Pareto front for LQR is characterized by linear scalarization: a convex combination of objectives recovers all tradeoff points, making multi-objective LQR reducible to single-objective problems. This highlights an important instance where linear scalarization suffices for a non-convex problem. Second, we show the Pareto front is smooth, in that an epsilon perturbation of a scalarization parameter yields an epsilon approximation to the objective. These results inspire a simple algorithm to approximate the Pareto front via grid search over scalarization parameters, where each optimization problem retains the computational efficiency of single-objective LQR. Lastly, we extend the analysis to certainty equivalence, where unknown dynamics are replaced with estimates.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern techniques in control theory and optimization have significantly shaped the landscape of our physical and digital infrastructure, encompassing data centers, power grids, and supply chains. However, many of these systems involve a range of objective functions dictated by stakeholder input. For example, control methods have recently been employed to manage power distribution in plug-in electric vehicles. By optimizing a handcrafted objective function, Lu et al., demonstrated that their control policy enhanced system efficiency and improved vehicle response. These multi-objective considerations are prevalent in other control applications as well. In dynamic asset allocation, the objective is to minimize the risk (or variance) of a portfolio while simultaneously achieving a target return. In supply chain settings such as dynamic production planning, the goal is to minimize operating costs, which include production costs, holding costs, and penalties for unmet demand. Finally, in energy management systems operating smart grids, algorithms are used to minimize energy consumption and cost while also considering reliability and reducing environmental impacts.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional approaches to settings with competing objectives often rely on ad-hoc rules of thumb, heuristics, or stakeholder input to craft a single objective function. However, this method obscures the intricate relationship between different metrics, making it challenging to navigate tradeoffs without a clear understanding of each objective's relative performance. Furthermore, there typically does not exist a single best "ranking" or a clear scalar objective function to determine which tradeoffs are preferable. Instead of focusing on a fixed solution, a better approach is to be preference agnostic, returning a set of solutions rather than a single one. To this end, we consider the measure of Pareto optimality (see Definition 2.1. ‣ 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation ‣ Multi-Objective LQR with Linear Scalarization")), where a solution is Pareto optimal if it is nondominated by any other solution across all objectives.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This creates new challenges for algorithm design and computation, since $(i)$ it is not clear how to identify a solution within the Pareto front (the set of Pareto optimal solutions) in non-convex domains, and $({ii})$ the Pareto front is continuous, and any discrete approximation requires that it is sufficiently smooth. Thus motivated, this paper seeks to answer the following questions: How can we characterize and approximate the Pareto front of solutions in multi-objective LQR? What is the computational complexity? How do these algorithms extend when the system dynamics are unknown and the certainty equivalence control is used?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Recent work has studied multi-objective reinforcement learning with either a finite horizon, or an infinite horizon with discounted costs. However, there has been little development for its use in un-discounted infinite horizon decision-making settings, which presents additional theoretical challenges concerning stability. To make progress towards this, we consider the most canonical infinite-horizon problem, the Linear Quadratic Regulator (LQR). This work provides rigorous guarantees, showing that while LQR is non-convex, directly using simple scalarization and discretization techniques already used in practice leads to a uniform approximation of the Pareto front. The main contributions are as follows: Characterizing the Pareto front of MObjLQR (Theorem 3.4). Our first contribution is structural, establishing that the Pareto front is characterized by linear scalarization. In particular, we highlight that any Pareto optimal control is optimal for a single objective LQR problem where the cost matrices are a weighted combination of the original cost matrices. This extends the technique of linear scalarization to non-convex domains and has broad applications in other control problems (see Appendix B for more details).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Algorithm for approximating the Pareto front (Theorem 6.1). The previous characterization illuminates a straightforward algorithm to approximate the Pareto front using discretization. Given any desired accuracy $\epsilon$, create an $\epsilon$-net of the set of scalarization parameters and solve for the optimal control on each discretized scalarization point. To establish this guarantees an approximation to the Pareto front, we show the smoothness of the Pareto front relative to shifts in the scalarization. This result builds on existing work showing sensitivity to solutions of the algebraic Riccati equation in Mania et al. which we extend to consider perturbations in the cost matrices. See Fig. 1 for a demonstration of the algorithm in a multi-objective pendulum problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Extension using certainty equivalence under unknown system dynamics (Theorem 6.2). In our last contribution we extend the previous discussion to domains where the system dynamics are unknown and replaced with estimates. We highlight how our guarantees and algorithm extend when using certainty equivalence so long as the approximation errors to the system dynamics are of the same order as the desired approximation guarantee for the Pareto front.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We believe that the methods developed here will likely be useful for settings such as congestion control, queueing systems, inventory control (aka Newsvendor), and others given the applicability of decision-making problems with linear dynamics. More broadly, the techniques in this work merge ideas from semi-definite programming, optimal control, and mathematical optimization. These techniques ultimately provide a theoretical justification for a simple algorithm already used in practice for characterizing the Pareto front, since they use existing solution methods for single objective LQR problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

We next survey the related literature. In Section 2 we present background concepts and formally introduce multi-objective LQR (MObjLQR). In Section 3 we outline the sufficiency of linear scalarization for LQR, our characterization result for the Pareto front. We describe our approximation algorithm to the Pareto front in Section 4. In Section 5 we provide sensitivity analysis for the discrete algebraic Riccati equation, and in Section 6 use this to show smoothness of the Pareto front relative to perturbations in the linear scalarization parameter. Unless otherwise specified, auxiliary lemmas and proofs are deferred to the Appendix.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Characterizing Pareto frontier for control systems", "weight": 1.0} -->

Numerous studies have focused on characterizing the Pareto front for control systems. The vast majority of the literature avoids using linear scalarization, instead using Chebyshev scalarization or the $\epsilon$-constraint method, since they are known to characterize the Pareto front even in non-convex settings. In fact, it is often commented that while linear scalarization is more natural, it is unknown whether it is sufficient to characterize the Pareto front in LQR, or whether the Pareto front is smooth. Our work provides an affirmative answer to this fundamental question. Since these alternative scalarization methods do not retain the structure of the optimal LQR policy (whose solution is easily computed as a function of the algebraic Riccati equation, see Lemma 2.2), the literature has focused on designing computationally efficient algorithms that approximate the true solution. In contrast, our methodology leverages existing solution methodology for solving single objective LQR problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Empirical applications of multi-objective control", "weight": 1.0} -->

There have been several papers investigating the empirical use of linear scalarization or other multi-objective optimization techniques in a control context. Genov and Kralov Ye and Zheng, considers control for vehicle suspension, using linear scalarization and optimizing the weights to achieve a minimum performance on specific metrics. Giacomán-Zarzar et al., considers a similar study in an aircraft dynamics problem. Wu et al., considers optimal control of linear switched systems, and uses linear scalarization weighted based on which control problem is active, but does not consider explicit notions of Pareto optimality. Our work complements this literature by providing a rigorous theoretical justification to their empirical approach on using linear scalarization, alongside the smoothness of the Pareto front. Van Moffaert et al., considers the use of Chebyshev scalarization, another scalarization technique, in the context of multi-objective reinforcement learning. As a follow up, Kaya and Maurer, provides a numerical algorithm to learn the optimal control using Chebyshev scalarization and includes experiments on healthcare applications.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Policy gradient algorithms for LQR and certainty equivalence", "weight": 1.0} -->

Much of our technical work is grounded in the studies of Fazel et al., and Mania et al.,. Fazel et al., explores the global convergence of policy gradient methods for LQR, leveraging the convex formulation of the LQR objective. We employ this convex formulation in our lifting argument to demonstrate the sufficiency of linear scalarization in Theorem 3.4. In a different setting, Mania et al., shows approximation guarantees of certainty equivalence for LQR, and in doing so provide interpretable sensitivity bounds on solutions to the algebraic Riccati equation. We modify and extend their proof to additionally account for perturbations in the cost matrices.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Multi-Objective LQR", "weight": 1.0} -->

The standard linear quadratic regulator (LQR) problem is parameterized by the dynamics matrices $A \in {\mathbb{R}}^{n \times n}$ and $B \in {\mathbb{R}}^{n \times d}$. We assume for simplicity that $n \geq d$, although the approximation guarantees scale with $\min{\{ n,d\}}$. After taking control $u_{t}$ at timestep $t$ in state $x_{t}$, the state evolves to the new state $x_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$. Typically, LQR is defined with a single quadratic cost dictated by the matrices $(Q,R)$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Multi-Objective LQR", "weight": 1.0} -->

However, we are interested in the control of LQR with multiple cost matrices, ${(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}}$, where each $Q_{i} \in {\mathbb{R}}^{n \times n}$ and $R_{i} \in {\mathbb{R}}^{d \times d}$. Since the solution to any single objective LQR problem is linear and we want to use the same control across all objectives $i \in {\lbrack m\rbrack}$, we restrict our attention to linear controls of the form $u_{t} = {Kx_{t}}$ for some matrix $K \in {\mathbb{R}}^{n \times d}$. We let denote the cost of $K$ for fixed cost matrices $Q$ and $R$, where $x_{t}$ and $u_{t}$ denote the state and action at timestep $t$ respectively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Multi-Objective LQR", "weight": 1.0} -->

The expectation is taken over the initial state, which we assume to be $x_{0} \sim {N{(0,I_{n})}}$ for simplicity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We assume that $(A,B)$ are stabilizable and that each ${(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}}$ are positive definite. Since rescaling $(Q_{i},R_{i})$ does not change the optimal control, we can assume without loss of generality that for all $i \in {\lbrack m\rbrack}$, both ${{\sigma_{\min}{(Q_{i})}},{\sigma_{\min}{(R_{i})}}} \geq 1$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

For the remainder of the paper we assume Assumption 1 holds. Note that Assumption 1 implies that $(A,Q^{1/2})$ is detectable. Since the system is assumed to be stable we let denote the set of stabilizing controls. Hence, the goal of multi-objective LQR (MObjLQR) is to find the set of controls that optimize the following problem: The "optimal" control in this case is unclear since the control which optimizes $(Q_{j},R_{j})$ for a particular $j \in {\lbrack m\rbrack}$ will not necessarily have strong performance for $(Q_{i},R_{i})$ for $i \neq j$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

However, for the case when $m = 1$ (or equivalently, there are fixed cost matrices $Q$ and $R$), the optimal policy is given by the linear feedback control $u_{t} = {Kx_{t}}$ where and $P$ is the positive definite solution to the discrete algebraic Riccati equation: We use the notation $\text{dare}{(A,B,Q,R)}$ to denote the unique positive semidefinite solution to Equation 5 for a given $A,B,Q,R$. We assume without loss of generality that ${\sigma_{\min}{(P)}} \geq 1$ (note that this is achieved by Assumption 1, see Lemma D.5 and Garloff,).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Pareto Optimality and Linear Scalarization", "weight": 1.0} -->

Our goal is to find controls $K \in \mathcal{S}$ with strong performance uniformly across the objective functions ${\mathcal{L}_{i}{(K)}}\operatorname{:-}{\mathcal{L}_{i}{(K,Q_{i},R_{i})}}$ for $i \in {\lbrack m\rbrack}$. To introduce a notion of optimality we consider Pareto optimality, whereby a control $K$ is said to be Pareto optimal whenever there is no other control which uniformly dominates it across all cost matrices.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Pareto Optimality and Linear Scalarization", "weight": 1.0} -->

This can be equivalently defined as a partial order over cost vectors ${\overset{\rightarrow}{\mathcal{L}}{(K)}}\operatorname{:-}{\{{\mathcal{L}_{1}{(K)}},\ldots,{\mathcal{L}_{m}{(K)}}\}} \in {\mathbb{R}}_{\geq 0}^{m}$, where the set of Pareto optimal controls is the maximal set according to the natural partial order over vectors.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sufficiency of Linear Scalarization for MObjLQR", "weight": 1.0} -->

In Equation 7 we introduced the concept of linear scalarization, a common approach for obtaining a solution in the Pareto front by optimizing a weighted combination of the objectives. We will momentarily see that this yields a solution in the Pareto front whenever the optimal solution is unique. Moreover, this fully characterizes the Pareto front whenever the cost functions and constraint set are convex. Unfortunately, the set of stable controls $\mathcal{S}$ is non-convex (see Lemma 2 in ), and so this result does not directly apply to MObjLQR.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sufficiency of Linear Scalarization for MObjLQR", "weight": 1.0} -->

In this section, we present an alternative approach for establishing the sufficiency of linear scalarization in non-convex multi-objective problems. We use a lifting technique, a surjective reformulation of the non-convex optimization problem as a convex one. In Appendix B we provide an alternative geometric proof and other non-convex multi-objective optimization problems for which this characterization technique applies.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sufficiency of Linear Scalarization for MObjLQR", "weight": 1.0} -->

Since the discussion in this section applies to generic multi-objective optimization, we temporarily consider optimization problems of the form: Note that we do not impose any assumptions on $f_{i}{(x)}$ or $X$. With this the Pareto front $\text{PF}{(X)}$ is defined as the set of solutions $x$ which are Pareto optimal, i.e. there exists no other $x' \in X$ with ${f_{i}{(x')}} \leq {f_{i}{(x)}}$ for all $i \in {\lbrack m\rbrack}$ with one of the inequalities being strict. The convex coverage set is similarly defined as: Before showing the sufficiency of linear scalarization for enumerating the Pareto front, we first establish that linear scalarization yields solutions that belong in the Pareto front whenever $w > 0$ or the optimal solution is unique.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Lifting Argument for MObjLQR", "weight": 1.0} -->

While the constraint set $\mathcal{S}$ of stable controls for LQR is non-convex, it does have a well-known convex parametrization arising by reformulating the solution to the discrete algebraic Riccati equation as linear matrix inequalities. Hence, we first focus on a lifting technique, where the non-convex optimization problem is lifted to an equivalent one in a higher dimension which preserves the objective value. We show that such a parametrization is sufficient for showing that ${\text{PF}{(X)}} \subseteq {\text{CCS}{(X)}}$. In Theorem 3.4 we apply this to MObjLQR.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Approximating the Pareto Frontier of MObjLQR", "weight": 1.0} -->

In Section 3 we highlighted that the Pareto front for MObjLQR can be enumerated through the use of linear scalarization (Eq. 7). More specifically, if we denote $K_{w}$ as the unique optimal control for a given scalarization parameter $w \in {\Delta{({\lbrack m\rbrack})}}$, i.e. then we can rewrite the Pareto front as We first note that computing $K_{w}$ for a given $w \in {\Delta{({\lbrack m\rbrack})}}$ reduces to solving a single objective LQR problem via Lemma 2.2, and so each $K_{w}$ is specified: where $P_{w} = {\text{dare}{(A,B,Q_{w},R_{w})}}$. This crucially avoids issues of other scalarization techniques since linear scalarization retains the property that the optimal solution is governed by the Riccati equations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Approximating the Pareto Frontier of MObjLQR", "weight": 1.0} -->

While computing $\text{PF}{(\mathcal{S})}$ requires enumerating over the set of weight vectors, it immediately leads to a natural algorithm to approximate the Pareto front by discretizing the set of weights. However, this technique is only effective under appropriate sensitivity and smoothness properties. In fact, Das and Dennis, provides examples of convex Pareto fronts where a uniform weight discretization does not provide a uniform approximation guarantee. Establishing these properties is a key aspect of our contribution. We outline the main algorithm next.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Our goal will be to show that given an arbitrary $K = K_{w}$ for $w \in {\Delta{({\lbrack m\rbrack})}}$ in the Pareto front there is a $K_{\epsilon} \in {\text{PF}_{\epsilon}{(\mathcal{S})}}$ such that: The second measure is stronger, requiring that the returned control approximates the loss of $K$ uniformly across the different objectives for $i \in {\lbrack m\rbrack}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Informal Theorem 1", "weight": 1.0} -->

Suppose that $\epsilon \leq {O{}}$ and construct $\text{PF}_{\epsilon}{(\mathcal{S})}$ as in Eq. 16. Given any $K \in {\text{PF}{(\mathcal{S})}}$ there exists a $K_{\epsilon} \in {\text{PF}_{\epsilon}{(\mathcal{S})}}$: We will later extend 1 to include certainty equivalence, where the dynamics matrices $A$ and $B$ are unknown and instead replaced with estimates $\hat{A}$ and $\hat{B}$. Before giving a formal statement of the result as well as its proof, we first highlight a necessary component of our analysis.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Informal Theorem 1", "weight": 1.0} -->

Hence we have: Thus, in order to prove our approximation guarantees we first need to present perturbation theory for the solution to discrete Riccati equations for a bound on $\parallel{P - P_{\epsilon}}\parallel$, which we delve into in Section 5 before discussing the main results and their proof in Section 6.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Perturbation Theory for Discrete Riccati Equation", "weight": 1.0} -->

As discussed in Section 4, a necessary aspect of our analysis is presenting perturbation theory for solutions to the discrete algebraic Riccati equation as we adjust problem parameters. More specifically, let $P = {\text{dare}{(A,B,Q,R)}}$ and $P_{\epsilon} = {\text{dare}{(A_{\epsilon},B_{\epsilon},Q_{\epsilon},R_{\epsilon})}}$, where each pair of matrices have difference bounded above by $\epsilon$ (i.e. ${\parallel{A - A_{\epsilon}}\parallel} \leq \epsilon$, etc). Our goal will be to show that ${\parallel{P - P_{\epsilon}}\parallel} \leq {O{(\epsilon)}}$ so long as $\epsilon \leq {O{}}$, where $O{( \cdot )}$ drops polynomial factors depending on the input matrices $(A,B,Q,R)$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Perturbation Theory for Discrete Riccati Equation", "weight": 1.0} -->

Our result builds on and extends the operator-theoretic proofs of Konstantinov et al. Mania et al., to additionally consider perturbations in the cost matrices $Q$ and $R$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Upper Bounds on Control and Stability Margin", "weight": 1.0} -->

A direct application of Theorem 5.1 will provide guarantees on $\parallel{P - P_{\epsilon}}\parallel$ presented in terms of ${\parallel P\parallel}_{+},{\parallel{A + {BK}}\parallel}_{+}$, ${\parallel Q_{w}\parallel}_{+}$, and $\tau{({A + {BK}},\rho)}$. All of these parameters directly depend on the choice of $w \in {\Delta{({\lbrack m\rbrack})}}$ for the linear scalarization. Thus, in order to provide guarantees that only scale in terms of the input matrices $(A,B,{(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}})$ we first need to provide upper bounds on each of the terms appearing in the bounds of Theorem 5.1 which would depend on the choice of $w \in {\Delta{({\lbrack m\rbrack})}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Upper Bounds on Control and Stability Margin", "weight": 1.0} -->

We establish these bounds in the following lemma, before later considering the stability margins across the Pareto front.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Results on MObjLQR", "weight": 1.0} -->

Together with the characterization result (establishing that linear scalarization is sufficient for enumerating the Pareto front in MObjLQR) and the previous discussion on the sensitivity analysis to solutions to the algebraic Riccati equation, we are now ready to formally present and prove 1. This enables us to demonstrate that a straightforward algorithm, which discretizes the scalarization parameters, is sufficient to uniformly approximate the Pareto front. Additionally, our algorithm leverages computational oracles for solving single-objective LQR problems. In Section 6.1 we extend this approach to incorporate certainty equivalence, allowing the algorithm to handle unknown system dynamics by using estimates. Before giving a formal statement of the theorem we first recall our algorithm for approximating the Pareto front.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Compute Our first result highlights that so long as $\epsilon \leq {O{}}$, where $O{(\cdot)}$ hides polynomial constants depending on the input matrices $(A,B,{(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}})$, our algorithm provides an $O{(\epsilon)}$ approximation to $\text{PF}{(\mathcal{S})}$ under both the weighted and uniform approximation guarantees.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Certainty Equivalence", "weight": 1.0} -->

So far we have considered the scenario where the dynamics matrices $(A,B)$ are known to the algorithm in advance. This raises an important question: how do estimation errors in the input matrices $A$ and $B$ impact the downstream approximation errors of the Pareto front? To address this, we employ the simplest method for controlling a dynamical system with unknown transitions: certainty equivalence. A model of the system is constructed, and the control policy is designed by treating this fitted model as the true system. Although this method is straightforward, its efficiency is not guaranteed a priori, as small modeling errors could lead to undesirable stability behavior and varied objective performance. In this section, we demonstrate that when the approximation errors in the dynamics are of the same order as the desired approximation errors in the Pareto front, the straightforward extension of the algorithm from Section 4 with the inclusion of certainty equivalence provides a uniform approximation guarantee to the Pareto front.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Certainty Equivalence", "weight": 1.0} -->

In the following we assume the algorithm has access to estimates $\hat{A}$ and $\hat{B}$ for $A$ and $B$ respectively. We further denote: as the commensurate LQR cost (Eq. 1) where $A$ and $B$ are replaced with $\hat{A}$ and $\hat{B}$. We similarly overload notation and use ${{\hat{\mathcal{L}}}_{i}{(K)}}\operatorname{:-}{\hat{\mathcal{L}}{(K,Q_{i},R_{i})}}$ and ${{\hat{\mathcal{L}}}_{w}{(K)}}\operatorname{:-}{\hat{\mathcal{L}}{(K,Q_{w},R_{w})}}$. Before stating the main results we describe the algorithm similar to Section 4 but instead using certainty equivalence for the optimal control on the scalarization points.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We will show that so long as $\parallel{A - \hat{A}}\parallel$ and $\parallel{B - \hat{B}}\parallel$ are bounded above by $\epsilon$, we can obtain an $O{(\epsilon)}$ approximation to the Pareto front. A major technical contribution of this section is establishing that the learned control $\hat{K}$ remains stable under the true dynamics dictated by $A$ and $B$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we discussed the Linear Quadratic Regulator (LQR), a prevalent model in control theory with applications spanning fields such as energy management and robotics. Traditional LQR methodologies focus on optimizing a predefined combination of objectives, which can obscure the relationship between individual metrics and complicate the identification of optimal tradeoffs. Addressing this limitation, we demonstrated the sufficiency of linear scalarization in enumerating the Pareto front in multi-objective LQR. Furthermore, we established that an exhaustive search over an $\epsilon$-discretized set of weights yields an $O{(\epsilon)}$ approximation to the Pareto front. Notably, our algorithm is already used in practice without theoretical justification, and this work serves to resolve this open problem in the literature. Follow-ups to this work include investigating the impact of the theoretical results on $(i)$ affine constraints on the control inputs $u$ and states $x$, and $({ii})$ the role of partial observability.
