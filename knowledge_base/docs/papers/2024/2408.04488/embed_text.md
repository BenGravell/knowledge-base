## Introduction

Modern techniques in control theory and optimization have significantly shaped the landscape of our physical and digital infrastructure, encompassing data centers, power grids, and supply chains. However, many of these systems involve a range of objective functions dictated by stakeholder input. For example, control methods have recently been employed to manage power distribution in plug-in electric vehicles. By optimizing a handcrafted objective function, Lu et al. ((https://arxiv.org/html/2408.04488v2#bib.bib25)) demonstrated that their control policy enhanced system efficiency and improved vehicle response. These multi-objective considerations are prevalent in other control applications as well. In dynamic asset allocation, the objective is to minimize the risk (or variance) of a portfolio while simultaneously achieving a target return (Sridharan et al. (https://arxiv.org/html/2408.04488v2#bib.bib33)). In supply chain settings such as dynamic production planning, the goal is to minimize operating costs, which include production costs, holding costs, and penalties for unmet demand. Finally, in energy management systems operating smart grids, algorithms are used to minimize energy consumption and cost while also considering reliability and reducing environmental impacts (Shaikh et al. (https://arxiv.org/html/2408.04488v2#bib.bib32), Yang and Wang (https://arxiv.org/html/2408.04488v2#bib.bib39)).

Traditional approaches to settings with competing objectives often rely on ad-hoc rules of thumb, heuristics, or stakeholder input to craft a single objective function. However, this method obscures the intricate relationship between different metrics, making it challenging to navigate tradeoffs without a clear understanding of each objective's relative performance. Furthermore, there typically is no single best "ranking" or a clear scalar objective function to determine which tradeoffs are preferable. Instead of focusing on a fixed solution, a better approach is to be preference agnostic, returning a set of solutions rather than a single one. To this end, we consider the measure of Pareto optimality (see [Definition 2.1](https://arxiv.org/html/2408.04488v2#S2.Thmtheorem1 "Definition 2.1 (Pareto optimal) ‣ 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation")), where a solution is Pareto optimal if it is nondominated by any other solution across all objectives. This creates new challenges for algorithm design and computation, since $(i)$ it is not clear how to identify a solution within the Pareto front (the set of Pareto optimal solutions) in non-convex domains \\srseditlike control problems, and $({ii})$ the Pareto front is continuous, and any discrete approximation requires that it is sufficiently smooth (Das and Dennis (https://arxiv.org/html/2408.04488v2#bib.bib9)). Thus motivated, this paper seeks to answer the following questions:

How can we characterize and approximate the Pareto front of solutions in multi-objective control? What is the computational complexity? How do these algorithms extend when the system dynamics are unknown and the certainty equivalence control is used?

### Our Contributions

Approximation of the Pareto front in an inverted pendulum problem. The x-axis denotes performance on the first objective minimizing the distance to the upright position, and the y-axis performance on the second objective of the cumulative acceleration. Performance is normalized to fall in where lower values correspond to better performance. Each point corresponds to a control in the Pareto front, where we used the algorithm in Section 4 with known dynamics matrices and ϵ = 10−1.5.

Recent work has studied multi-objective reinforcement learning with either a finite horizon, or an infinite horizon with discounted costs (Liu et al. (https://arxiv.org/html/2408.04488v2#bib.bib23)). However, there has been little development for its use in un-discounted infinite horizon decision-making settings, which presents additional theoretical challenges concerning stability. To make progress towards this, we consider the most canonical infinite-horizon problem, the Linear Quadratic Regulator (LQR) (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)). This work provides rigorous guarantees, showing that while LQR is non-convex, directly using simple scalarization and discretization techniques already used in practice leads to a uniform approximation of the Pareto front. The main contributions are as follows:

Characterizing the Pareto front of \\srseditmulti-objective LQR ([Theorem 3.6](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem6 "Theorem 3.6 ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR")). \\srsedit Our first contribution is structural, establishing that the Pareto front for multi-objective LQR is characterized by linear scalarization. In particular, we highlight that any Pareto optimal control is optimal for a single objective LQR problem where the cost matrices are a weighted combination of the original cost matrices. While it is clear for LQR that the objective is linear in the costs, it was previously unknown if this extends to characterizing the Pareto front. This result extends the technique of linear scalarization to non-convex domains and has broad applications in other control problems (see [Section 8](https://arxiv.org/html/2408.04488v2#S8 "8 Sufficiency of Linear Scalarization with Unique Solutions") for more details).

Algorithm for approximating the Pareto front ([Theorem 6.1](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem1 "Theorem 6.1 ‣ Algorithm ‣ 6 Main Results on MObjLQR")). The previous characterization illuminates a straightforward algorithm to approximate the Pareto front using discretization. Given any desired accuracy $\epsilon$, create an $\epsilon$-net of the set of scalarization parameters and solve for the optimal control on each discretized scalarization point. \\srseditIndeed, this algorithm has been used for decades in empirical work, without any rigorous theoretical guarantees (Logist et al. (https://arxiv.org/html/2408.04488v2#bib.bib24)). To establish this guarantees an approximation to the Pareto front, we show the smoothness of the Pareto front relative to shifts in the scalarization. \\srsdeleteThis result builds on existing work showing sensitivity to solutions of the algebraic Riccati equation in Mania et al. ((https://arxiv.org/html/2408.04488v2#bib.bib27)), which we extend to consider perturbations in the cost matrices. See [Section 1.1](https://arxiv.org/html/2408.04488v2#S1.SS1 "1.1 Our Contributions ‣ 1 Introduction") for a demonstration of the algorithm in a multi-objective pendulum problem.

Extension using certainty equivalence under unknown system dynamics ([Theorem 6.3](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem3 "Theorem 6.3 ‣ Algorithm ‣ 6.1 Certainty Equivalence ‣ 6 Main Results on MObjLQR")). In our last contribution, we extend the previous discussion to domains where the system dynamics are unknown and replaced with estimates. We highlight how our guarantees and algorithm extend when using certainty equivalence so long as the approximation errors to the system dynamics are of the same order as the desired approximation guarantee for the Pareto front.

We believe that the methods developed here will likely be useful for settings such as congestion control (Bartoszewicz and Leśniewski (https://arxiv.org/html/2408.04488v2#bib.bib6)), queuing systems (Bonald and Roberts (https://arxiv.org/html/2408.04488v2#bib.bib7)), inventory control (aka Newsvendor) (Parlar and Kevin Weng (https://arxiv.org/html/2408.04488v2#bib.bib31)), and others given the applicability of decision-making problems with linear dynamics. More broadly, the techniques in this work merge ideas from semi-definite programming, optimal control, and mathematical optimization. \\srseditThese techniques ultimately provide a theoretical justification for a simple algorithm already used in practice for characterizing the Pareto front (Logist et al. (https://arxiv.org/html/2408.04488v2#bib.bib24)), since they use existing solution methods for single objective LQR problems (Alessio and Bemporad (https://arxiv.org/html/2408.04488v2#bib.bib2)).

### Paper Organization

We next survey the related literature. In [Section 2](https://arxiv.org/html/2408.04488v2#S2 "2 Preliminary and Notation") we present background concepts and formally introduce the multi-objective LQR (MObjLQR) problem. In [Section 3](https://arxiv.org/html/2408.04488v2#S3 "3 Sufficiency of Linear Scalarization for MObjLQR") we outline the sufficiency of linear scalarization for LQR, our characterization result for the Pareto front. We describe our approximation algorithm to the Pareto front in [Section 4](https://arxiv.org/html/2408.04488v2#S4 "4 Approximating the Pareto Frontier of MObjLQR"). In [Section 5](https://arxiv.org/html/2408.04488v2#S5 "5 Perturbation Theory for the Discrete Riccati Equation") we provide sensitivity analysis for the discrete algebraic Riccati equation, and in [Section 6](https://arxiv.org/html/2408.04488v2#S6 "6 Main Results on MObjLQR") use this to show the smoothness of the Pareto front relative to perturbations in the linear scalarization parameter. Unless otherwise specified, auxiliary lemmas and proofs are deferred to the Appendix.

### Related Work

Our paper builds on a rich body of literature spanning control theory, operations research, and optimization. We consider multi-objective optimization in the context of the linear quadratic regulator (LQR) problem. Below we highlight the most closely related works as they touch on optimal control and multi-objective optimization, but see Anderson and Moore ((https://arxiv.org/html/2408.04488v2#bib.bib3)) for classical references in control theory and Miettinen ((https://arxiv.org/html/2408.04488v2#bib.bib29)) for the concept of Pareto optimality in other multi-objective optimization problems.

### Characterizing the Pareto frontier for control systems

Numerous studies have focused on characterizing the Pareto front for control systems (Logist et al. (https://arxiv.org/html/2408.04488v2#bib.bib24), Li and Burger (https://arxiv.org/html/2408.04488v2#bib.bib20), Van Erdeghem et al. (https://arxiv.org/html/2408.04488v2#bib.bib36), Li (https://arxiv.org/html/2408.04488v2#bib.bib19), Koussoulas and Leondes (https://arxiv.org/html/2408.04488v2#bib.bib17), Nair et al. (https://arxiv.org/html/2408.04488v2#bib.bib30)). The vast majority of the literature avoids using linear scalarization, instead using Chebyshev scalarization or the $\epsilon$-constraint method, since they are known to characterize the Pareto front even in non-convex settings (Miettinen (https://arxiv.org/html/2408.04488v2#bib.bib29)). In fact, it is often commented that while linear scalarization is more natural and practical, it is unknown whether it is sufficient to characterize the Pareto front in LQR, or whether the Pareto front is smooth (Logist et al. (https://arxiv.org/html/2408.04488v2#bib.bib24), Das and Dennis (https://arxiv.org/html/2408.04488v2#bib.bib9)). Our work provides an affirmative answer to this fundamental question. Since these alternative scalarization methods do not retain the structure of the optimal LQR policy (whose solution is easily computed as a function of the algebraic Riccati equation, see [Lemma 2.2](https://arxiv.org/html/2408.04488v2#S2.Thmtheorem2 "Lemma 2.2 ‣ 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation")), the literature has focused on designing computationally efficient algorithms that approximate the true solution. In contrast, our methodology leverages existing solution techniques for solving single objective LQR problems (Alessio and Bemporad (https://arxiv.org/html/2408.04488v2#bib.bib2)).

### Empirical applications of multi-objective control

There have been several papers investigating the empirical use of linear scalarization or other multi-objective optimization techniques in a control context. Genov and Kralov ((https://arxiv.org/html/2408.04488v2#bib.bib12)), Ye and Zheng ((https://arxiv.org/html/2408.04488v2#bib.bib40)) considers control for vehicle suspension, using linear scalarization and optimizing the weights to achieve a minimum performance on specific metrics. Giacomán-Zarzar et al. ((https://arxiv.org/html/2408.04488v2#bib.bib13)) considers a similar study in an aircraft dynamics problem. Wu et al. ((https://arxiv.org/html/2408.04488v2#bib.bib38)) considers optimal control of linear switched systems, and uses linear scalarization weighted based on which control problem is active, but does not consider explicit notions of Pareto optimality. Our work complements this literature by providing a rigorous theoretical justification to their empirical approach on using linear scalarization, alongside the smoothness of the Pareto front. Van Moffaert et al. ((https://arxiv.org/html/2408.04488v2#bib.bib37)) considers the use of Chebyshev scalarization, another scalarization technique, in the context of multi-objective reinforcement learning. As a follow-up, Kaya and Maurer ((https://arxiv.org/html/2408.04488v2#bib.bib14)) provides a numerical algorithm to learn the optimal control using Chebyshev scalarization and includes experiments on healthcare applications.

### Data-driven control

A separate line of work studies data-driven control with a single objective function. Fazel et al. ((https://arxiv.org/html/2408.04488v2#bib.bib10)) explores the global convergence of policy gradient methods for LQR, leveraging a convex formulation of the LQR objective. In a different setting, Mania et al. ((https://arxiv.org/html/2408.04488v2#bib.bib27)) shows approximation guarantees of certainty equivalence for LQR assuming fixed estimated dynamics matrices, and in doing so provides sensitivity bounds on solutions to the algebraic Riccati equation. Data-driven LQR has been studied either in unknown systems with access to samples (Arora et al. (https://arxiv.org/html/2408.04488v2#bib.bib4), Cohen et al. (https://arxiv.org/html/2408.04488v2#bib.bib8)), with advice or predictions (Yu et al. (https://arxiv.org/html/2408.04488v2#bib.bib41), Li et al. (https://arxiv.org/html/2408.04488v2#bib.bib21), Zhang et al. (https://arxiv.org/html/2408.04488v2#bib.bib42)), or under adversarial models (Agarwal et al. (https://arxiv.org/html/2408.04488v2#bib.bib1), Li et al. (https://arxiv.org/html/2408.04488v2#bib.bib22)).

## Preliminary and Notation

### Notation

We denote ${\lbrack m\rbrack} = {\{ 1,\ldots,m\}}$ and let $\Delta{({\lbrack m\rbrack})}$ be the set of vectors $w \in {\mathbb{R}}_{\geq 0}^{m}$ with ${\parallel w\parallel}_{1} = 1$. We let $\lambda_{i}{(A)}$ denote the $i$'th eigenvalues of a matrix $A$ ordered to be non-increasing in absolute value and $\sigma_{i}{(A)}$ to be the $i$'th singular value, again ordered to be non-increasing. We introduce shorthand notation and let $\sigma_{\min}{(A)}$, $\sigma_{\max}{(A)}$ denote the minimum and maximum singular values respectively. We further denote $\rho{(A)}$ to denote the spectral radius of a matrix $A$. All matrix norms correspond to the spectral operator norm unless otherwise indicated. \\srseditLastly, we let $O{}$ denote absolute constants. See [Table 1](https://arxiv.org/html/2408.04488v2#S7.T1) for a full table of notation.

### Multi-Objective LQR

The standard linear quadratic regulator (LQR) problem is parameterized by the dynamics matrices $A \in {\mathbb{R}}^{n \times n}$ and $B \in {\mathbb{R}}^{n \times d}$. We assume for simplicity that $n \geq d$, although the approximation guarantees scale with $\min{\{ n,d\}}$. After taking control $u_{t}$ at timestep $t$ in state $x_{t}$, the state evolves to the new state $x_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$. Typically, LQR is defined with a single quadratic cost dictated by the matrices $(Q,R)$. However, we are interested in the control of LQR with multiple cost matrices, ${(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}}$, where each $Q_{i} \in {\mathbb{R}}^{n \times n}$ and $R_{i} \in {\mathbb{R}}^{d \times d}$. \\srseditFirst, it is well known that the solution to any single objective LQR problem is linear (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)). While it is not immediately clear that it suffices to consider linear controls for multi-objective LQR, we will later see that this restriction is without loss of generality. Hence, we restrict our attention to linear controls of the form $u_{t} = {Kx_{t}}$ for some matrix $K \in {\mathbb{R}}^{n \times d}$. We let

denote the cost of \\srseditcontrol $K$ for fixed cost matrices $Q$ and $R$, where $x_{t}$ and $u_{t}$ denote the state and action at timestep $t$ respectively. The expectation is taken over the initial state, which we assume to be $x_{0} \sim {N{(0,I_{n})}}$ for simplicity. To ensure tractability we make the following assumption: {assumption} We assume that $(A,B)$ are stabilizable and that each ${(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}}$ are positive definite. Since rescaling $(Q_{i},R_{i})$ does not change the optimal control, we can assume without loss of generality that for all $i \in {\lbrack m\rbrack}$, both ${{\sigma_{\min}{(Q_{i})}},{\sigma_{\min}{(R_{i})}}} \geq 1$. For the remainder of the paper we assume [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") holds. Note that [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") implies that $(A,Q^{1/2})$ is detectable (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)). Since the system is assumed to be stable we let

denote the set of stabilizing controls. Hence, the goal of multi-objective LQR (henceforth MObjLQR) is to find the set of controls that optimize the following problem:

The "optimal" control, in this case, is unclear since the control which optimizes $(Q_{j},R_{j})$ for a particular $j \in {\lbrack m\rbrack}$ will not necessarily have strong performance for $(Q_{i},R_{i})$ for $i \neq j$. However, for the case when $m = 1$ (or equivalently, there are fixed cost matrices $Q$ and $R$), the optimal policy is given by the linear feedback control $u_{t} = {Kx_{t}}$ where

and $P$ is the positive definite solution to the discrete algebraic Riccati equation:

We use the notation $\text{dare}{(A,B,Q,R)}$ to denote the unique positive semidefinite solution to [Equation 5](https://arxiv.org/html/2408.04488v2#S2.E5 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") for a given $A,B,Q,R$ (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)). We finally assume without loss of generality that ${\sigma_{\min}{(P)}} \geq 1$ (note that this is achieved by [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation"), see [Lemma 10.8](https://arxiv.org/html/2408.04488v2#S10.Thmtheorem8 "Lemma 10.8 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") and Garloff ((https://arxiv.org/html/2408.04488v2#bib.bib11))).

### Pareto Optimality and Linear Scalarization

Our goal is to find controls $K \in \mathcal{S}$ with strong performance uniformly across the objective functions ${\mathcal{L}_{i}{(K)}}\operatorname{:-}{\mathcal{L}_{i}{(K,Q_{i},R_{i})}}$ for $i \in {\lbrack m\rbrack}$. \\srseditTo introduce a notion of optimality we consider Pareto optimality, whereby a control $K$ is said to be Pareto optimal whenever there is no other control that uniformly dominates it across the set of cost matrices. This can be equivalently defined as a partial order over cost vectors ${\overset{\rightarrow}{\mathcal{L}}{(K)}}\operatorname{:-}{\{{\mathcal{L}_{1}{(K)}},\ldots,{\mathcal{L}_{m}{(K)}}\}} \in {\mathbb{R}}_{\geq 0}^{m}$, where the set of Pareto optimal controls is the maximal set according to the natural partial order over vectors.

### Definition 2.1 (Pareto optimal)

A control $K \in \mathcal{S}$ is said to be Pareto optimal if there does not exist another $K^{\prime} \in \mathcal{S}$ such that ${\mathcal{L}_{i}{(K^{\prime})}} \leq {\mathcal{L}_{i}{(K)}}$ for all $i \in {\lbrack m\rbrack}$ and ${\mathcal{L}_{j}{(K^{\prime})}} < {\mathcal{L}_{j}{(K)}}$ for at least one index $j \in {\lbrack m\rbrack}$. We let $\text{PF}{(\mathcal{S})}$ denote the set of all Pareto optimal controls in $\mathcal{S}$, i.e.

In the case of a single objective, $\text{PF}{(\mathcal{S})}$ reduces to the unique optimal solution to a single objective LQR problem.

A common technique to solve for a solution in $\text{PF}{(\mathcal{S})}$ is to pick a weight $w \in {\Delta{({\lbrack m\rbrack})}}$ and optimize the so-called linear scalarization problem with parameter $w$:

where we overload notation here and use $\mathcal{L}_{w}{( \cdot )}$ to denote the $w$-weighted loss $w^{\top}\overset{\rightarrow}{\mathcal{L}}{(K)}$. However, we will establish that if $K \in \mathcal{S}$ is stable, then each $\mathcal{L}_{i}{(K)}$ is linear in the cost matrices.

### Lemma 2.2

For any stable control $K \in \mathcal{S}$ we have

### Proof 2.3

Proof By definition, ${\mathcal{L}_{w}{(K)}} = {\sum_{i}{w_{i}\mathcal{L}_{i}{(K)}}}$. Moreover, each individual cost at timestep $t$ satisfies

The result follows using a simple interchange argument between the sum and the limit with respect to $T$ since each term is bounded by the assumption that $K \in \mathcal{S}$ is stable. \\Halmos

The previous lemma highlights that [Eq. 7](https://arxiv.org/html/2408.04488v2#S2.E7 "In 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation") is equivalent to a single objective LQR problem with cost matrices $(Q_{w},R_{w})$. \\srseditHerein lies our first key insight: solving a weighted combination of LQR objectives is no harder than a single objective LQR problem, retaining the structure that the optimal control is determined by the solution to a Riccati equation. Indeed, if $K_{w}$ is the optimizer of $\mathcal{L}_{w}{( \cdot )}$, then

via [Eq. 4](https://arxiv.org/html/2408.04488v2#S2.E4 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") and $P_{w} = {\text{dare}{(A,B,Q_{w},R_{w})}}$. Next we consider the set of controls which optimize a linear scalarization problem $\mathcal{L}_{w}{(K)}$ for fixed $w \in {\Delta{({\lbrack m\rbrack})}}$.

### Definition 2.4 (Convex Coverage Set)

The convex coverage set is defined as

We note that computing an element in $\text{CCS}{(\mathcal{S})}$ for MObjLQR is no harder than that for a single objective LQR problem since \\srseditby [Lemma 2.2](https://arxiv.org/html/2408.04488v2#S2.Thmtheorem2 "Lemma 2.2 ‣ 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation"), linear scalarization preserves the property that the optimal control is linear and dictated by the solution of the discrete algebraic Riccati equation. This is in stark contrast to other scalarization methods (e.g. Chebyshev scalarization or the $\epsilon$-constraint method) (Miettinen (https://arxiv.org/html/2408.04488v2#bib.bib29)). It moreover allows for algorithms to use existing tools and solvers to efficiently compute the optimal control (Alessio and Bemporad (https://arxiv.org/html/2408.04488v2#bib.bib2)). Before seeing how this can be exploited to design a discrete approximation to the Pareto front, we first investigate the sufficiency of linear scalarization for MObjLQR to establish that ${\text{CCS}{(\mathcal{S})}} = {\text{PF}{(\mathcal{S})}}$.

## Sufficiency of Linear Scalarization for MObjLQR

In [Equation 7](https://arxiv.org/html/2408.04488v2#S2.E7 "In 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation") we introduced the concept of linear scalarization, a common approach for obtaining a solution in the Pareto front by optimizing a weighted combination of the objectives. We will momentarily see that this yields a solution in the Pareto front whenever the optimal solution is unique. Moreover, this fully characterizes the Pareto front whenever the cost functions and constraint set are convex (Miettinen (https://arxiv.org/html/2408.04488v2#bib.bib29)). Unfortunately, the set of stable controls $\mathcal{S}$ is non-convex (see Lemma 2 in (Fazel et al. (https://arxiv.org/html/2408.04488v2#bib.bib10))), and so this result does not directly apply to MObjLQR.

In this section, we present an alternative approach for establishing the sufficiency of linear scalarization in non-convex multi-objective problems. We use a lifting technique, a surjective reformulation of the non-convex optimization problem as a convex one. In [Section 8](https://arxiv.org/html/2408.04488v2#S8 "8 Sufficiency of Linear Scalarization with Unique Solutions") we provide an alternative geometric proof and other non-convex multi-objective optimization problems for which this technique applies.

Since the discussion in this section applies to multi-objective optimization more broadly, we temporarily consider optimization problems of the form:

Note that we do not impose any assumptions on $f_{i}{(x)}$ or $X$. With this the Pareto front $\text{PF}{(X)}$ is defined as the set of solutions $x$ which are Pareto optimal, i.e. there exists no other $x^{\prime} \in X$ with ${f_{i}{(x^{\prime})}} \leq {f_{i}{(x)}}$ for all $i \in {\lbrack m\rbrack}$ with one of the inequalities being strict. The convex coverage set is similarly defined as:

Before showing the sufficiency of linear scalarization for characterizing the Pareto front, we first establish that linear scalarization yields solutions that belong in the Pareto front whenever $w > 0$ or the optimal solution is unique.

### Lemma 3.1

Suppose that $w \in {\Delta{({\lbrack m\rbrack})}}$ and that $x$ optimizes $\min_{x^{\prime} \in X}{\sum_{i}{w_{i}f_{i}{(x^{\prime})}}}$, i.e. $x \in {\text{CCS}{(X)}}$. Then if either:

$w_{i} > 0$ for all $i \in {\lbrack m\rbrack}$,

$x$ is the unique solution,

we have that $x \in {\text{PF}{(X)}}$, i.e. ${\text{CCS}{(X)}} \subseteq {\text{PF}{(X)}}$.

### Proof 3.2

Proof Case I: Suppose that $w_{i} > 0$ for all $i$ and that $x$ is not Pareto optimal. Then there exists another solution $x^{\prime}$ such that ${f_{i}{(x^{\prime})}} \leq {f_{i}{(x)}}$ for all $i \in {\lbrack m\rbrack}$ with one of them being strict. Then by taking the weighted sum, ${\sum_{i}{w_{i}f_{i}{(x^{\prime})}}} < {\sum_{i}{w_{i}f_{i}{(x)}}}$ contradicting optimality of $x$.

Case II: Suppose that $x$ is unique and not Pareto optimal. Then there exists another solution $x^{\prime}$ such that ${f_{i}{(x^{\prime})}} \leq {f_{i}{(x)}}$ for all $i \in {\lbrack m\rbrack}$ with one of them being strict. Then we have that ${\sum_{i}{w_{i}f_{i}{(x^{\prime})}}} \leq {\sum_{i}{w_{i}f_{i}{(x)}}}$ contradicting the uniqueness of $x$. \\Halmos

We next restate a theorem from Miettinen ((https://arxiv.org/html/2408.04488v2#bib.bib29)), showing that when the losses and constraint set are convex, any solution in the Pareto front can be found using linear scalarization.

### Theorem 3.3 (Theorem 3.14 of Miettinen ([1999](https://arxiv.org/html/2408.04488v2#bib.bib29)))

Suppose that $f_{i}{( \cdot )}$ is convex for each $i \in {\lbrack m\rbrack}$ and $X$ is convex. Then if $x$ is Pareto optimal there exists $w \in {\Delta{({\lbrack m\rbrack})}}$ such that $x$ solves the linear scalarization problem for $w$, $x \in {{\arg\min}_{x^{\prime} \in X}{\sum_{i}{w_{i}f_{i}{(x^{\prime})}}}}$. Hence, ${\text{PF}{(X)}} \subseteq {\text{CCS}{(X)}}$.

Important to note is that it is not necessarily true that ${\text{CCS}{(X)}} = {\text{PF}{(X)}}$. This arises because solutions to linear scalarization need not be unique, even with convex objective functions. However, [Theorem 3.3](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem3 "Theorem 3.3 (Theorem 3.14 of Miettinen ) ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") and [Lemma 3.1](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem1 "Lemma 3.1 ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") imply that ${\text{CCS}{(X)}} = {\text{PF}{(X)}}$ whenever $f_{i}{( \cdot )}$ and $X$ are all convex and the linear scalarization solution is always unique.

In fact, [Theorem 3.3](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem3 "Theorem 3.3 (Theorem 3.14 of Miettinen ) ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") immediately implies that restricting to linear controls is without loss of generality for MObjLQR. Indeed, it is well known that the LQR objective is convex in the (potentially non-linear) control inputs $u = {(u_{t})}_{t \in {\mathbb{N}}} \in \mathcal{U}$. Combined with the fact that $\mathcal{U}$ is convex, we immediately have that ${\text{PF}{(\mathcal{U})}} = {\text{CCS}{(\mathcal{U})}}$. However, ${\text{CCS}{(\mathcal{U})}} = {\text{CCS}{(\mathcal{S})}}$ due to the optimality of linear controls for any fixed LQR problem (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)). Hence, the more interesting question we focus on in this paper is whether the Pareto front over linear controls $\text{PF}{(\mathcal{S})}$ equals the Pareto front over non-linear controls $\text{PF}{(\mathcal{U})}$, a corollary of our characterization result.

Unfortunately, the set of stable linear controls $\mathcal{S}$ is non-convex (see Lemma 2 in Fazel et al. ((https://arxiv.org/html/2408.04488v2#bib.bib10)) for relevant discussion). We next provide a surprising result on the sufficiency of linear scalarization for MObjLQR, providing a non-convex example where the sufficiency of linear scalarization still holds.

### Lifting Argument for MObjLQR

While the constraint set $\mathcal{S}$ of stable controls for LQR is non-convex, it does have a well-known convex parametrization arising by reformulating the solution to the discrete algebraic Riccati equation as linear matrix inequalities (Balakrishnan and Vandenberghe (https://arxiv.org/html/2408.04488v2#bib.bib5)). Hence, we first focus on a lifting technique, where the non-convex optimization problem is lifted to an equivalent one in a higher dimension which preserves the objective value. We show that such a parametrization is sufficient for showing that ${\text{PF}{(X)}} \subseteq {\text{CCS}{(X)}}$. In [Theorem 3.6](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem6 "Theorem 3.6 ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") we apply this to MObjLQR.

### Theorem 3.4 (Lifted Multi-Objective Optimization)

Consider multi-objective optimization problems of the form:

$g_{i}{(y)}$ and $Y$ are all convex,

there exists $h:{X\rightarrow Y}$ which is surjective and satisfies ${f_{i}{(x)}} = {g_{i}{({h{(x)}})}}$ for all $x \in X$.

Then if $x \in X$ is Pareto optimal there exists $w \in {\Delta{({\lbrack m\rbrack})}}$ such that $x$ minimizes $\sum_{i}{w_{i}f_{i}{(x)}}$. Hence, ${\text{PF}{(X)}} \subseteq {\text{CCS}{(X)}}$.

### Proof 3.5

Proof Suppose that $x \in X$ is Pareto optimal. This implies that ${h{(x)}} = y$ is Pareto optimal in the second optimization problem. To see this, suppose not and let $y^{\prime}$ be such that ${g_{i}{(y^{\prime})}} \leq {g_{i}{(y)}}$ and one of them strict. Since $h$ is surjective, let $x^{\prime} \in X$ be any value such that ${h{(x^{\prime})}} = y^{\prime}$. Then we also have that ${f_{i}{(x^{\prime})}} = {g_{i}{(y^{\prime})}} \leq {f_{i}{(x)}} = {g_{i}{(y)}}$ with one of them being strict, contradicting the fact that $x$ is Pareto optimal.

Now since $h{(x)}$ is Pareto optimal in the second optimization problem, by [Theorem 3.3](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem3 "Theorem 3.3 (Theorem 3.14 of Miettinen ) ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") we know that ${\exists w} \in {\Delta{({\lbrack m\rbrack})}}$ such that $h{(x)}$ minimizes $\sum_{i}{w_{i}g_{i}{(y)}}$. This also implies that $x$ minimizes $\sum_{i}{w_{i}f_{i}{(x)}}$ since if some $x^{\prime}$ has ${\sum_{i}{w_{i}f_{i}{(x^{\prime})}}} < {\sum_{i}{w_{i}f_{i}{(x)}}}$ we also get ${\sum_{i}{w_{i}g_{i}{({h{(x^{\prime})}})}}} < {\sum_{i}{w_{i}g_{i}{({h{(x)}})}}}$ contradicting the optimality of $h{(x)}$. \\Halmos

Using [Theorem 3.4](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem4 "Theorem 3.4 (Lifted Multi-Objective Optimization) ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") and a convex parameterization of the linear matrix inequalities dictating the discrete algebraic Riccati equations we are finally able to show the sufficiency of linear scalarization for MObjLQR. \\srsdeleteIn particular, combining [Theorem 3.4](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem4 "Theorem 3.4 (Lifted Multi-Objective Optimization) ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR"), the uniqueness of solutions to LQR, [Lemma 3.1](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem1 "Lemma 3.1 ‣ 3 Sufficiency of Linear Scalarization for MObjLQR"), and the convex parameterization, we can establish that ${\text{PF}{(\mathcal{S})}} = {\text{CCS}{(\mathcal{S})}}$. We note that the forthcoming semidefinite program and its dual was explored in Balakrishnan and Vandenberghe ((https://arxiv.org/html/2408.04488v2#bib.bib5)).

### Theorem 3.6

Let $K \in \mathcal{S}$ be a stable control. Then $K$ is Pareto optimal if and only if there exists $w \in {\Delta{({\lbrack m\rbrack})}}$ such that $K$ is optimal on $\mathcal{L}{(K,Q_{w},R_{w})}$ where $Q_{w} = {\sum_{i}{w_{i}Q_{i}}}$ and $R_{w} = {\sum_{i}{w_{i}R_{i}}}$. In particular, ${\text{PF}{(\mathcal{S})}} = {\text{CCS}{(\mathcal{S})}}$.

### Proof 3.7

Proof We use the lifting argument from [Theorem 3.4](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem4 "Theorem 3.4 (Lifted Multi-Objective Optimization) ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") and a semi-definite programming formulation of LQR. Consider the following convex program:

This optimization problem is of the form $\min{\{ g_{i}{(y)}\}}_{i \in {\lbrack m\rbrack}}$ subject to $y \in Y$ where both $g_{i}{(y)}$ and the constraint set $Y$ are convex. Hence, to use [Theorem 3.4](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem4 "Theorem 3.4 (Lifted Multi-Objective Optimization) ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") we just need to show a surjection between $\mathcal{S}$ and the set of $L,P,G$ satisfying the constraints and that it preserves the objective value. Before giving the mapping we first introduce notation and set $P = {\text{dlyape}{({A + {BK}},I)}}$ as the solution to the discrete Lyapunov equation:

Note that there exists a unique positive definite solution whenever $({A + {BK}})$ is stable (i.e. $K \in \mathcal{S}$) (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)).

We construct the mapping as follows. Given a $K \in \mathcal{S}$ we set: ${{(i)}P} = {\text{dlyape}{({A + {BK}},I)}}$, ${{({ii})}L} = {KP}$, and ${{({iii})}G} = {P - I}$.

Surjectivity: Let $L,P,G$ be arbitrary feasible values. Since $P \succ 0$ we know that $P$ is invertible and so we can set $K = {LP^{- 1}}$. Furthermore, we know that $G = {P - I}$ is the only feasible solution for fixed $P$. Lastly, we note that the final constraint of [Eq. 12](https://arxiv.org/html/2408.04488v2#S3.E12 "In Proof 3.7 ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") is the Schur complement of the equation

However, plugging in that $L = {KP}$ we observe that

Combined with $P \succ 0$ we know the unique feasible solution is $P = {\text{dlyape}{({A + {BK}},I)}}$ Anderson and Moore ((https://arxiv.org/html/2408.04488v2#bib.bib3)).

Preserves Objective Value: We remark that the LQR cost can be written as ${\mathcal{L}_{i}{(K)}} = {{Tr}{({{({Q_{i} + {K^{\top}R_{i}K}})}P})}}$ where $P = {\text{dlyape}{({A + {BK}},I)}}$ (see [Lemma 10.14](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.14 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas")). However, we also have by definition of the mapping:

Together with [Theorem 3.4](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem4 "Theorem 3.4 (Lifted Multi-Objective Optimization) ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") this shows that ${\text{PF}{(\mathcal{S})}} \subseteq {\text{CCS}{(\mathcal{S})}}$. To show the reverse direction we note that the optimal solution to a LQR problem is always unique under [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") and the fact that $Q_{w}$ and $R_{w}$ must be positive definite since they are a weighted combination of positive definite matrices (see Theorem 2.4-2 in Lewis et al. ((https://arxiv.org/html/2408.04488v2#bib.bib18))), and [Lemma 2.2](https://arxiv.org/html/2408.04488v2#S2.Thmtheorem2 "Lemma 2.2 ‣ 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation"). \\Halmos

## Approximating the Pareto Frontier of MObjLQR

In [Section 3](https://arxiv.org/html/2408.04488v2#S3 "3 Sufficiency of Linear Scalarization for MObjLQR") we highlighted that the Pareto front for MObjLQR can be characterized through the use of linear scalarization ([Eq. 7](https://arxiv.org/html/2408.04488v2#S2.E7 "In 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation")). More specifically, if we denote $K_{w}$ as the unique optimal control for a given scalarization parameter $w \in {\Delta{({\lbrack m\rbrack})}}$, i.e.

then we can rewrite the Pareto front as

We first note that computing $K_{w}$ for a given $w \in {\Delta{({\lbrack m\rbrack})}}$ reduces to solving a single objective LQR problem via [Lemma 2.2](https://arxiv.org/html/2408.04488v2#S2.Thmtheorem2 "Lemma 2.2 ‣ 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation"), and so each $K_{w}$ is specified by:

where $P_{w} = {\text{dare}{(A,B,Q_{w},R_{w})}}$. This crucially avoids issues of other scalarization techniques since linear scalarization retains the property that the optimal solution is governed by the Riccati equations. While computing $\text{PF}{(\mathcal{S})}$ requires enumerating over the set of weight vectors, it immediately leads to a natural algorithm to approximate the Pareto front by discretizing the set of weights. However, this technique is only effective under appropriate sensitivity and smoothness properties. In fact, Das and Dennis ((https://arxiv.org/html/2408.04488v2#bib.bib9)) provides examples of convex Pareto fronts where a uniform weight discretization does not provide a uniform approximation guarantee. Establishing these properties is a key aspect of our contribution. We outline the main algorithm next.

### Algorithm

Let $N_{\epsilon}$ be an $\epsilon$-net of $\Delta{({\lbrack m\rbrack})}$ such that for any $w \in {\Delta{({\lbrack m\rbrack})}}$ there exists $w_{\epsilon} \in N_{\epsilon}$ with ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Note that ${|N_{\epsilon}|} = {O{(\epsilon^{- m})}}$. Let

Computing $\text{PF}_{\epsilon}{(\mathcal{S})}$ requires only $O{(\epsilon^{- m})}$ calls to a LQR solution oracle ([Lemma 2.2](https://arxiv.org/html/2408.04488v2#S2.Thmtheorem2 "Lemma 2.2 ‣ 2.2 Pareto Optimality and Linear Scalarization ‣ 2 Preliminary and Notation")). \\srseditOur goal will be to show that given an arbitrary $K = K_{w}$ for $w \in {\Delta{({\lbrack m\rbrack})}}$ in the Pareto front there is a $K_{\epsilon} \in {\text{PF}_{\epsilon}{(\mathcal{S})}}$ such that:

where $\lesssim$ omits polynomial dependence on the input matrices ${(A,B,{(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}})}.$ The second measure is stronger, requiring that the returned control approximates the loss of $K$ uniformly across the different objectives for $i \in {\lbrack m\rbrack}$. We will later extend this idea to include certainty equivalence, where the dynamics matrices $A$ and $B$ are unknown and instead replaced with estimates $\hat{A}$ and $\hat{B}$. Before giving a formal statement of the result as well as its proof, we first highlight a necessary component of our analysis.

Let $w \in {\Delta{({\lbrack m\rbrack})}}$ be arbitrary and set $w_{\epsilon} \in N_{\epsilon}$ such that ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Consider the controls $K$ and $K_{\epsilon}$ which optimize $\mathcal{L}_{w}{( \cdot )}$ and $\mathcal{L}_{w_{\epsilon}}{( \cdot )}$ respectively. Note that $K$ and $K_{\epsilon}$ are both described uniquely in terms of the solutions to $\text{dare}{(A,B,Q_{w},R_{w})}$ and $\text{dare}{(A,B,Q_{w_{\epsilon}},R_{w_{\epsilon}})}$. Consider the weighted approximation objective. Applying the triangle inequality yields:

To bound the second term we use the fact that $(Q_{w},R_{w})$ and $(Q_{w_{\epsilon}},R_{w_{\epsilon}})$ are close as well as the definition of the LQR objective in [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation"). To bound the first term, we use the fact that ${\mathcal{L}_{w}{(K)}} = {{Tr}{(P)}}$ where $P = {\text{dare}{(A,B,Q_{w},R_{w})}}$ (see [Lemma 10.14](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.14 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas")). Similarly, ${\mathcal{L}_{w_{\epsilon}}{(K_{\epsilon})}} = {{Tr}{(P_{\epsilon})}}$ for $P_{\epsilon} = {\text{dare}{(A,B,Q_{w_{\epsilon}},R_{w_{\epsilon}})}}$. Hence we have:

Thus, in order to prove our approximation guarantees we first need to present perturbation theory for the solution to discrete Riccati equations for a bound on $\parallel{P - P_{\epsilon}}\parallel$, which we delve into in [Section 5](https://arxiv.org/html/2408.04488v2#S5 "5 Perturbation Theory for the Discrete Riccati Equation") before discussing the main results and their proof in [Section 6](https://arxiv.org/html/2408.04488v2#S6 "6 Main Results on MObjLQR").

## Perturbation Theory for the Discrete Riccati Equation

As discussed in Section (https://arxiv.org/html/2408.04488v2#S4 "4 Approximating the Pareto Frontier of MObjLQR"), a necessary aspect of our analysis is presenting perturbation theory for solutions to the discrete algebraic Riccati equation as we adjust problem parameters. More specifically, let $P = {\text{dare}{(A,B,Q,R)}}$ and $P_{\epsilon} = {\text{dare}{(A_{\epsilon},B_{\epsilon},Q_{\epsilon},R_{\epsilon})}}$, \\srseditwhere each pair of matrices have difference bounded above by $\epsilon$ (i.e. ${\parallel{A - A_{\epsilon}}\parallel} \leq \epsilon$, etc). Our goal will be to show that ${\parallel{P - P_{\epsilon}}\parallel} \lesssim \epsilon$ for sufficiently small $\epsilon$. Our result builds on and extends the operator-theoretic proofs of Konstantinov et al. ((https://arxiv.org/html/2408.04488v2#bib.bib16)), Mania et al. ((https://arxiv.org/html/2408.04488v2#bib.bib27)) to additionally consider perturbations in the cost matrices $Q$ and $R$.

### Notation

We use $\Delta_{M} = {M - M_{\epsilon}}$ to denote the difference in matrices, where $M$ can vary. We also denote ${\parallel \cdot \parallel}_{+} = {{\parallel \cdot \parallel} + 1}$, and let $R_{\max} = {1 + {\max{\{{\parallel R^{- 1}\parallel},{\parallel R_{\epsilon}^{- 1}\parallel}\}}}}$. We set $L = {A + {BK}}$ and use

to denote the rate of growth of the Lyapunov matrix $L = {A + {BK}}$.

In other words, $\tau{(L,\rho)}$ is the smallest value such that ${\parallel L^{k}\parallel} \leq {\tau{(L,\rho)}\rho^{k}}$ for all $k \geq 0$. Note that $\tau{(L,\rho)}$ may be infinite depending on the value of $\rho$. However, due to Gelfand's formula if $\rho$ is larger than $\rho{(L)}$ then $\tau{(L,\rho)}$ is guaranteed to be finite (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)). Moreover, if $L$ is stable then we can always pick $\rho < 1$ such that $\tau{(L,\rho)}$ is finite. At a high level, $\tau{(L,\rho)}$ quantifies the rate at which the control $K$ drives the state to zero, so the less stable the closed loop system is, the larger this term becomes. See Tu et al. ((https://arxiv.org/html/2408.04488v2#bib.bib35)), Mania et al. ((https://arxiv.org/html/2408.04488v2#bib.bib27)) for more details. Our primary goal in this section will be to establish the following:

### Theorem 5.1

Let $P = {\text{dare}{(A,B,Q,R)}}$ and $P_{\epsilon} = {\text{dare}{(A_{\epsilon},B_{\epsilon},Q_{\epsilon},R_{\epsilon})}}$. We assume that $(A,B)$ are stabilizable, $R$ and $R_{\epsilon}$ are positive definite, ${\sigma_{\min}{(P)}} \geq 1$, and ${\max{\{{\parallel\Delta_{A}\parallel},{\parallel\Delta_{B}\parallel},{\parallel\Delta_{Q}\parallel},{\parallel\Delta_{R}\parallel}\}}} \leq \epsilon$. Then:

Upon first glance, it might seem that [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") is sufficient to help show \\srseditthe uniform approximation guarantee to $\text{PF}{(\mathcal{S})}$ of our algorithm. However, for a given $w \in {\Delta{({\lbrack m\rbrack})}}$ we will set $P = {\text{dare}{(A,B,Q_{w},R_{w})}}$ and $P_{\epsilon} = {\text{dare}{(A,B,Q_{w_{\epsilon}},R_{w_{\epsilon}})}}$, where $w_{\epsilon} \in N_{\epsilon}$ is the point in the $\epsilon -$net with ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. The guarantees in [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") will then be given in terms of constants depending on $(A,B,Q_{w},R_{w})$, instead of on the input matrices $(A,B,{(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}})$. We address this issue in [Section 5.2](https://arxiv.org/html/2408.04488v2#S5.SS2 "5.2 Upper Bounds on Control and Stability Margin ‣ 5 Perturbation Theory for the Discrete Riccati Equation"). Before giving the proof of [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") in [Section 5.1](https://arxiv.org/html/2408.04488v2#S5.SS1 "5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation") we first give a brief proof sketch.

*Proof Sketch.* Denote by $F{(X,A,B,Q,R)}$ as the matrix expression

Note that solving the Riccati equation associated with $(A,B,Q,R)$ corresponds to finding the unique positive definite matrix $X$ such that ${F{(X,A,B,Q,R)}} = 0$. Let $\Delta_{P} = {P_{\epsilon} - P}$. Since $P$ and $P_{\epsilon}$ solve respective $\text{dare}{( \cdot )}$ equations we have that ${F{(P,A,B,Q,R)}} = 0$ and ${F{(P_{\epsilon},A_{\epsilon},B_{\epsilon},Q_{\epsilon},R_{\epsilon})}} = 0$.

We will start by constructing an operator $\Phi{(X)}$ such that any fixed point $X$ satisfying $X = {\Phi{(X)}}$ must be equal to $\Delta_{P}$. However, to show that $\Phi$ has a fixed point, we consider a set $S_{\nu}$ of matrices satisfying ${\parallel X\parallel} \leq \nu$. We will show that $\Phi$ maps $S_{\nu}$ onto itself, and is a contraction. Hence, $\Phi$ has a fixed point equal to $\Delta_{P}$, and since $\Delta_{P} \in S_{\nu}$ must satisfy ${\parallel\Delta_{P}\parallel} \leq \nu$. The proof finishes by selecting $\nu = {O{(\epsilon)}}$.

### Proof of [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation")

### Proof 5.2

Proof For convenience we use $S = {BR^{- 1}B^{\top}}$ and $S_{\epsilon} = {B_{\epsilon}R_{\epsilon}^{- 1}B_{\epsilon}^{\top}}$. For any matrix $X$ such that $I + {S{({P + X})}}$ is invertible, note that

where $L = {A + {BK}}$. This follows from adding $F{(P,A,B,Q,R)}$ which is equal to zero to the right-hand side of [Eq. 20](https://arxiv.org/html/2408.04488v2#S5.E20 "In Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation") and using that ${{({I + {BR^{- 1}B^{\top}P}})}^{- 1}A} = {A + {BK}}$. Denote ${\mathcal{T}{(X)}} = {X - {L^{\top}XL}}$ and ${\mathcal{H}{(X)}} = {L^{\top}X{({I + {S{({P + X})}}})}^{- 1}SXL}$. Then [Eq. 20](https://arxiv.org/html/2408.04488v2#S5.E20 "In Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation") says that

Since [Eq. 20](https://arxiv.org/html/2408.04488v2#S5.E20 "In Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation") is satisfied for any matrix $X$ such that $I + {S{({P + X})}}$ is invertible the matrix equation

has a unique symmetric solution $X$ such that ${P + X} \succeq 0$. This solution is $X = \Delta_{P}$ because any solution must satisfy that ${F{({P + X},A_{\epsilon},B_{\epsilon},Q_{\epsilon},R_{\epsilon})}} = 0$.

Note that the linear map $\mathcal{T}:{X\rightarrow{X - {L^{\top}XL}}}$ has eigenvalues equal to $1 - {\lambda_{i}\lambda_{j}}$ where $\lambda_{i}$ and $\lambda_{j}$ are eigenvalues of the matrix $L$. Since $L = {A + {BK}}$ is stable, the linear map $\mathcal{T}$ is invertible. We define

Then solving for $X$ in [Eq. 21](https://arxiv.org/html/2408.04488v2#S5.E21 "In Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation") is equivalent to finding an $X$ satisfying ${P + X} \succeq 0$ with $X = {\Phi{(X)}}$. Thus we have that $\Phi$ has a unique symmetric fixed point $X$ such that ${P + X} \succeq 0$ and that is $X = \Delta_{P}$.

The remainder of the proof is focused on establishing that $\Phi{(X)}$ has a fixed point with bounded norm. Let ${\Delta_{A} = {A - A_{\epsilon}}},{{\Delta_{B} = {B - B_{\epsilon}}},{\Delta_{Q} = {Q - Q_{\epsilon}}}}$, $\Delta_{R} = {R - R_{\epsilon}}$, and $\Delta_{S} = {S - S_{\epsilon}}$. Define the set

By assumption we have that ${{\parallel\Delta_{A}\parallel},{\parallel\Delta_{B}\parallel},{\parallel\Delta_{Q}\parallel},{\parallel\Delta_{R}\parallel}} \leq \epsilon$. Hence, we also have that:

where in the last line we used $\epsilon \leq {\parallel B\parallel}$. However, we also have

Combining this with before we have ${\parallel\Delta_{S}\parallel} \leq {4{\parallel B\parallel}_{+}^{2}R_{\max}^{2}\epsilon}$.

With this in hand, we next show that $\Phi$ maps $\mathcal{S}_{\nu}$ to itself, and is a contraction. The Banach fixed point theorem then implies that $\Phi$ has a fixed point, and that fixed point must belong to $\mathcal{S}_{\nu}$.

### Lemma 5.3

Suppose that ${X,X_{1}},$ and $X_{2}$ are in $\mathcal{S}_{\nu}$ for $\nu \leq {\min{\{ 1,{\parallel S\parallel}^{- 1}\}}}$. Moreover, suppose $\epsilon \leq {\min{\{ 1,{\parallel B\parallel}\}}}$ and ${\sigma_{min}{(P)}} \geq 1$. Then:

### Proof 5.4

Proof First we upper bound the operator norm of the linear operator $\mathcal{T}^{- 1}$.

### Lemma 5.5

denote the rate of growth of a matrix $M$. Then we have that

### Proof 5.6

Proof Since $L$ is a stable matrix, $\mathcal{T}$ is invertible. Moreover, whenever $L$ is stable and ${X - {L^{\top}XL}} = M$ for some matrix $M$ we know that $X = {\sum_{k}{{(L^{k})}^{\top}ML^{k}}}$ due to properties of solutions to Lyapunov equations (Anderson and Moore (https://arxiv.org/html/2408.04488v2#bib.bib3)). Hence we have that:

where in the final line we used that $\tau{(L,\rho)}$ is the supremum and the geometric sum. \\Halmos

Next we recall that ${\mathcal{H}{(X)}} = {L^{\top}X{({I + {S{({P + X})}}})}^{- 1}SXL}$. Using [Lemma 10.1](https://arxiv.org/html/2408.04488v2#S10.Thmtheorem1 "Lemma 10.1 (Lemma 7 of Mania et al. ) ‣ 10.1 Matrix Properties ‣ 10 Auxilary Lemmas") we have that

Let $P_{X}$ denote $P + X$ and consider the difference ${F{(P_{X},A,B,Q,R)}} - {F{(P_{X},A_{\epsilon},B_{\epsilon},Q_{\epsilon},R_{\epsilon})}}$. Using [Eq. 19](https://arxiv.org/html/2408.04488v2#S5.E19 "In Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") we have that

By again using [Lemma 10.1](https://arxiv.org/html/2408.04488v2#S10.Thmtheorem1 "Lemma 10.1 (Lemma 7 of Mania et al. ) ‣ 10.1 Matrix Properties ‣ 10 Auxilary Lemmas"),

However, since $X \in \mathcal{S}_{\nu}$ we have ${\parallel X\parallel} \leq \nu$ and ${\parallel P_{X}\parallel} \leq {{\parallel P\parallel} + \nu}$. Additionally, as $\nu \leq 1$ we have ${{\parallel P_{X}\parallel} \leq {1 + {\parallel P\parallel}}}.$ Moreover, we also assume $\epsilon \leq {\parallel B\parallel}$. Therefore,

Next up we show the bound on $\parallel{{\Phi{(X_{1})}} - {\Phi{(X_{2})}}}\parallel$. Denote ${\mathcal{G}{(X)}} = {{F{(P_{X},A,B,Q,R)}} - {F{(P_{X},A_{\epsilon},B_{\epsilon},Q_{\epsilon},R_{\epsilon})}}}$. Note that

However, ${\parallel\mathcal{T}^{- 1}\parallel} \leq \frac{\tau{(L,\rho)}^{2}}{1 - \rho^{2}}$ from [Lemma 5.5](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem5 "Lemma 5.5 ‣ Proof 5.4 ‣ Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation"). We thus deal with the other two terms individually. Using algebraic manipulations, we have if $\Delta_{X} = {X_{1} - X_{2}}$:

Using [Lemma 10.1](https://arxiv.org/html/2408.04488v2#S10.Thmtheorem1 "Lemma 10.1 (Lemma 7 of Mania et al. ) ‣ 10.1 Matrix Properties ‣ 10 Auxilary Lemmas"), the fact that ${{({I + {YX}})}^{- 1}Y} = {Y{({I + {XY}})}^{- 1}}$, and assumption that $\nu \leq {\parallel S\parallel}^{- 1}$ to get:

Lastly we need to deal with the $\mathcal{G}$ terms. We start off by noting that

where we use the fact that ${\parallel X\parallel} \leq \nu \leq {1/2}$ and $P \succeq I$. Using the definition of $\mathcal{G}$ via [Eq. 19](https://arxiv.org/html/2408.04488v2#S5.E19 "In Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") as well as the representation above:

where we have defined:

Moreover, we have that

Therefore, after some cumbersome algebra we are able to show that:

Combining all of the different terms with $\epsilon \leq {\parallel B\parallel}$, ${\parallel S_{\epsilon}\parallel} \leq {1 + {\parallel S\parallel}}$, and ${\parallel\Delta_{S}\parallel} \leq {4\epsilon{\parallel B\parallel}_{+}^{2}R_{\max}^{2}}$ yields:

Using [Lemma 5.3](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem3 "Lemma 5.3 ‣ Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation"), we are able to finish the proof of [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") as follows. We first establish that $\Phi$ maps $\mathcal{S}_{\nu}$ to $\mathcal{S}_{\nu}$. To see this, note that by [Lemma 5.3](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem3 "Lemma 5.3 ‣ Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation"),

However, $\epsilon$ is chosen such that $\epsilon \leq {\frac{1}{4}C_{1}^{- 1}C_{2}^{- 1}}$ so that ${C_{1}\nu} \leq \frac{1}{2}$. Moreover, we also have that $\nu \leq \frac{1}{2}$ and ${\parallel S\parallel}^{- 1}$ by the bound on $\epsilon$. Thus we find that ${\parallel{\Phi{(X)}}\parallel} \leq \nu$ and so $\Phi$ maps $\mathcal{S}_{\nu}$ to itself.

Next we show that $\Phi$ is a contraction over $\mathcal{S}_{\nu}$. By the choice of $\epsilon$ and [Lemma 5.3](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem3 "Lemma 5.3 ‣ Proof 5.2 ‣ 5.1 Proof of Theorem 5.1 ‣ 5 Perturbation Theory for the Discrete Riccati Equation"),

Hence, $\Phi$ has a fixed point in $\mathcal{S}_{\nu}$ by the Banach fixed point theorem since $\mathcal{S}_{\nu}$ is a closed set. However, as established before the fixed point of $\Phi$ is precisely $\Delta_{P}$. Therefore, $\Delta_{P}$ is in $\mathcal{S}_{\nu}$ and hence ${\parallel\Delta_{P}\parallel} \leq \nu = {2C_{2}\epsilon}$. The final bound follows by plugging in the appropriate constants and verifying that the upper bound on $\epsilon$ satisfies the earlier inequalities. \\Halmos

### Upper Bounds on Control and Stability Margin

Unfortunately, [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") does not immediately suffice for showing \\srseditour algorithm uniformly approximates $\text{PF}{(\mathcal{S})}$. Recall the proof sketch that we had established earlier, and denote by $K$ as the optimal control to $\mathcal{L}_{w}{( \cdot )}$ for a given scalarization parameter $w \in {\Delta{({\lbrack m\rbrack})}}$ and $K_{\epsilon}$ the optimal control to $\mathcal{L}_{w_{\epsilon}}{( \cdot )}$ for $w_{\epsilon} \in N_{\epsilon}$ with ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Let $P = {\text{dare}{(A,B,Q_{w},R_{w})}}$ and $P_{\epsilon} = {\text{dare}{(A,B,Q_{w_{\epsilon}},R_{w_{\epsilon}})}}$. A direct application of [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") will provide guarantees on $\parallel{P - P_{\epsilon}}\parallel$ presented in terms of ${\parallel P\parallel}_{+},{\parallel{A + {BK}}\parallel}_{+}$, ${\parallel Q_{w}\parallel}_{+}$, and $\tau{({A + {BK}},\rho)}$. All of these parameters directly depend on the choice of $w \in {\Delta{({\lbrack m\rbrack})}}$ for the linear scalarization. Thus, in order to provide guarantees that only scale in terms of the input matrices $(A,B,{(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}})$ we first need to provide upper bounds on each of the terms appearing in the bounds of [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") which would depend on the choice of $w \in {\Delta{({\lbrack m\rbrack})}}$. We establish these bounds in the following lemma, before later considering the stability margins across the Pareto front.

### Lemma 5.7

Since the proof is mostly algebraic, we omit it here and present it in [Section 9](https://arxiv.org/html/2408.04488v2#S9 "9 Omitted Proofs from Main Text"). We also note that the right-hand side bounds on $P_{\max}$ and $K_{\max}$ depend only on $(A,B,{(Q_{i},R_{i})}_{i \in {\lbrack m\rbrack}})$ and hence can be computed directly in terms of the input matrices.

Next, we tackle the stability margin $\tau{({A + {BK}},\rho)}$ which appears in the bounds of [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation"). When using it to establish \\srseditthe performance guarantee for our algorithm we will let $K = K_{w}$ for a particular choice of scalarization parameter $w \in {\Delta{({\lbrack m\rbrack})}}$. Hence, we need to provide an upper bound on ${\max_{w \in {\Delta{({\lbrack m\rbrack})}}}\tau}{({A + {BK_{w}}},\rho)}$. First note that since each control $K = K_{w}$ in the Pareto front is stable, there exists a $\gamma$ such that ${\rho{({A + {BK_{w}}})}} < \gamma$ (which then implies that ${\tau{({A + {BK_{w}}},\gamma)}} < \infty$). One attempt might be to establish uniform stability bounds over all stable controls, i.e. $\sup_{K \in \mathcal{S}}{\tau{({A + {BK}},\gamma)}}$. \\srseditHowever, there might be a sequence of stable controls whose stability margin tends toward zero. We next establish using a continuity argument that it is possible to provide a uniform stability margin over the Pareto front since $\Delta{({\lbrack m\rbrack})}$ is closed and $\tau{({A + {BK_{w}}},\rho)}$ is continuous with respect to the scalarization parameter.

### Lemma 5.8

There exists a $\overline{\gamma}$ such that ${\rho{({A + {BK_{w}}})}} \leq \overline{\gamma} < 1$ for all $K_{w} \in {\text{PF}{(\mathcal{S})}}$. Defining

we also have that $\overline{\tau} < \infty$.

### Proof 5.9

Proof Such a $\overline{\gamma}$ exists since the map $w\rightarrow{\rho{({A + {BK_{w}}})}}$ is continuous (see [Lemma 10.10](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.10 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas")), each ${\rho{({A + {BK_{w}}})}} < 1$ by assumption, and that $\Delta{({\lbrack m\rbrack})}$ is a compact set. To show that $\overline{\tau} < \infty$ we note that each $\tau{({A + {BK_{w}}},\rho)}$ is non-increasing in $\rho$. Moreover, ${\tau{({A + {BK_{w}}},{\rho{({A + {BK_{w}}})}})}} < \infty$ using Gelfand's formula. Together this implies that ${\tau{({A + {BK_{w}}},\overline{\gamma})}} \leq {\tau{({A + {BK_{w}}},{\rho{({A + {BK_{w}}})}})}} < \infty$. \\Halmos

We now use [Lemma 5.7](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem7 "Lemma 5.7 ‣ 5.2 Upper Bounds on Control and Stability Margin ‣ 5 Perturbation Theory for the Discrete Riccati Equation") and [Lemma 5.8](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem8 "Lemma 5.8 ‣ 5.2 Upper Bounds on Control and Stability Margin ‣ 5 Perturbation Theory for the Discrete Riccati Equation") together with [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") to provide an interpretable bound on the sensitivity of solutions to the discrete algebraic Riccati equation over the Pareto front which does not depend on the choice of linear scalarization parameter $w \in {\Delta{({\lbrack m\rbrack})}}$. Note that we allow for perturbations in the dynamics matrices $A$ and $B$ as we will later use this when showing an equivalent approximation guarantee to the Pareto front with the use of certainty equivalence.

### Corollary 5.10

Consider an arbitrary $w$ and $w_{\epsilon}$ in $\Delta{({\lbrack m\rbrack})}$ such that ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Further denote $P = {\text{dare}{(A,B,Q_{w},R_{w})}}$ and $P_{\epsilon} = {\text{dare}{(A_{\epsilon},B_{\epsilon},Q_{w_{\epsilon}},R_{w_{\epsilon}})}}$. Suppose that [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") holds and ${\max{\{{\parallel\Delta_{A}\parallel},{\parallel\Delta_{B}\parallel}\}}} \leq \epsilon$. Denote

Then we have that

### Proof 5.11

Proof First note that

Similarly, ${\parallel{R_{w} - R_{w_{\epsilon}}}\parallel} \leq {\epsilon{\max_{j}{\parallel R_{j}\parallel}}}$. Both ($R_{w},Q_{w}$) and $(R_{w_{\epsilon}},Q_{w_{\epsilon}})$ are also positive definite by [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation"). Furthermore, ${\parallel P\parallel}_{+} \leq P_{\max}$, ${\parallel L\parallel} = {\parallel{A + {BK}}\parallel} \leq {{\parallel A\parallel} + {{\parallel B\parallel}K_{\max}}} \leq {{\parallel A\parallel}_{+}{\parallel B\parallel}_{+}K_{\max}}$. Hence using [Theorem 5.1](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem1 "Theorem 5.1 ‣ Notation. ‣ 5 Perturbation Theory for the Discrete Riccati Equation") we have if:

The final bound follows from [Lemma 5.7](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem7 "Lemma 5.7 ‣ 5.2 Upper Bounds on Control and Stability Margin ‣ 5 Perturbation Theory for the Discrete Riccati Equation") and algebraic manipulations. \\Halmos

## Main Results on MObjLQR

Together with the characterization result (establishing that linear scalarization is sufficient for enumerating the Pareto front in MObjLQR) and the previous discussion on the sensitivity analysis to solutions to the algebraic Riccati equation, we are now ready to formally present and prove \\srseditour approximation guarantee to $\text{PF}{(\mathcal{S})}$. This enables us to demonstrate that a straightforward algorithm, which discretizes the scalarization parameters, is sufficient to uniformly approximate the Pareto front (Logist et al. (https://arxiv.org/html/2408.04488v2#bib.bib24)). Additionally, our algorithm leverages computational oracles for solving single-objective LQR problems (Alessio and Bemporad (https://arxiv.org/html/2408.04488v2#bib.bib2)). In [Section 6.1](https://arxiv.org/html/2408.04488v2#S6.SS1 "6.1 Certainty Equivalence ‣ 6 Main Results on MObjLQR") we extend this approach to incorporate certainty equivalence, allowing the algorithm to handle unknown system dynamics by using estimates. Before giving a formal statement of the theorem we first recall our algorithm.

### Algorithm

Let $N_{\epsilon}$ be an $\epsilon$-net of $\Delta{({\lbrack m\rbrack})}$ such that for any $w \in {\Delta{({\lbrack m\rbrack})}}$ there exists $w_{\epsilon} \in N_{\epsilon}$ with ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Note that ${|N_{\epsilon}|} = {O{(\epsilon^{- m})}}$. Compute

Our first result highlights that for sufficiently small $\epsilon$ our algorithm provides an $\epsilon$ approximation to $\text{PF}{(\mathcal{S})}$ under both the weighted and uniform approximation guarantees. Indeed we have the following:

### Theorem 6.1

Suppose that [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") holds and that

Then for any $K \in {\text{PF}{(\mathcal{S})}}$ there exists a $K_{\epsilon} \in {\text{PF}_{\epsilon}{(\mathcal{S})}}$ with:

Before presenting the proof, we begin with a discussion of the result. First, we emphasize that the exact form of the bounds, such as the polynomial dependence on $\Gamma$ and the stability margins $\overline{\tau}$ and $\overline{\gamma}$, can likely be improved. Additionally, it might be possible to relax the stability condition from [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") to notions of $(\ell,\nu)$ controllability, as discussed in Mania et al. ((https://arxiv.org/html/2408.04488v2#bib.bib27)). The bounds in [Theorem 6.1](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem1 "Theorem 6.1 ‣ Algorithm ‣ 6 Main Results on MObjLQR") deteriorate as the system becomes more unstable (i.e. $\overline{\gamma}\rightarrow 1$). However, to the best of our knowledge, [Theorem 6.1](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem1 "Theorem 6.1 ‣ Algorithm ‣ 6 Main Results on MObjLQR") provides the first uniform approximation guarantee for the Pareto front of MObjLQR. Furthermore, our algorithm is computationally efficient, requiring only $O{(\epsilon^{- m})}$ calls to a single objective LQR solution oracle.

### Proof 6.2

Proof Let $K \in {\text{PF}{(\mathcal{S})}}$ be arbitrary, then by [Theorem 3.6](https://arxiv.org/html/2408.04488v2#S3.Thmtheorem6 "Theorem 3.6 ‣ 3.1 Lifting Argument for MObjLQR ‣ 3 Sufficiency of Linear Scalarization for MObjLQR") we know there exists a $w \in {\Delta{({\lbrack m\rbrack})}}$ such that $K$ optimizes $\mathcal{L}_{w}{( \cdot )}$. Since $N_{\epsilon}$ is an $\epsilon$-net of $\Delta{({\lbrack m\rbrack})}$, let $w_{\epsilon} \in N_{\epsilon}$ be such that ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Set $K_{\epsilon}$ as the control in $\text{PF}_{\epsilon}{(\mathcal{S})}$ which optimizes $\mathcal{L}_{w_{\epsilon}}{( \cdot )}$. Denote by $P = {\text{dare}{(A,B,Q_{w},R_{w})}}$ and $P_{\epsilon} = {\text{dare}{(A,B,Q_{w_{\epsilon}},R_{w_{\epsilon}})}}$. Applying [Corollary 5.10](https://arxiv.org/html/2408.04488v2#S5. "Corollary 5.10 ‣ 5.2 Upper Bounds on Control and Stability Margin ‣ 5 Perturbation Theory for the Discrete Riccati Equation") and the assumption on $\epsilon$,

As shown in [Lemma 10.23](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.23 (Adapted from Proposition 1 of Mania et al. ) ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") (stated in the Appendix),

Weighted Error Bound: Using the triangle inequality,

Note that this implicitly uses that $K_{\epsilon}$ stabilizes the system so that $\mathcal{L}_{w}{(K_{\epsilon})}$ is finite. For the first term we use [Lemma 10.14](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.14 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") (showing alternative representations of $\mathcal{L}{(K)}$) and the Von-Neumann trace inequality to have

Using [Eq. 24](https://arxiv.org/html/2408.04488v2#S6.E24 "In Proof 6.2 ‣ Algorithm ‣ 6 Main Results on MObjLQR") we hence have the first term is bounded by

For the second term, denote by $P_{K_{\epsilon}}^{L} = {\text{dlyape}{({A + {BK_{\epsilon}}},I)}}$. Then using [Lemma 10.14](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.14 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") again we have

However, from [Lemma 5.7](https://arxiv.org/html/2408.04488v2#S5.Thmtheorem7 "Lemma 5.7 ‣ 5.2 Upper Bounds on Control and Stability Margin ‣ 5 Perturbation Theory for the Discrete Riccati Equation") we know that ${\parallel K_{\epsilon}\parallel} \leq K_{max}$. Similarly by [Lemma 10.12](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.12 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") (establishing that solutions to the Lyapunov equation are bounded by the stability margin),

Combining these terms yields the first result.

Entry-Wise Error Bound: We first note by [Lemma 10.18](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.18 (Lemma 6 of Fazel et al. ) ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas"), which bounds ${\mathcal{L}_{i}{(K_{\epsilon})}} - {\mathcal{L}_{i}{(K)}}$ in terms of $K - K_{\epsilon}$ as follows:

where $P_{K_{\epsilon}}^{L} = {\text{dlyape}{({A + {BK_{\epsilon}}},I)}}$, $P_{K} = {\text{dlyape}{({({A + {BK}})}^{\top},{Q_{i} + {K^{\top}R_{i}K}})}}$, and $E_{K} = {{{({R_{i} + {B^{\top}P_{K}^{L}B}})}K} - {B^{\top}P_{K}^{L}A}}$. Using the Von-Neumann trace inequality we obtain

From [Eq. 25](https://arxiv.org/html/2408.04488v2#S6.E25 "In Proof 6.2 ‣ Algorithm ‣ 6 Main Results on MObjLQR"), ${\parallel{K - K_{\epsilon}}\parallel} \leq {O{}\frac{{\overline{\tau}}^{2}}{1 - {\overline{\gamma}}^{2}}\Gamma^{12}\epsilon}$ Moreover, by [Lemma 10.12](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.12 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas")

since $K_{\epsilon} \in {\text{PF}{(\mathcal{S})}}$. Next we note that ${\parallel E_{K}\parallel} \leq {2\Gamma^{3}{\parallel P_{K}\parallel}}$. Again using [Lemma 10.12](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.12 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") we have

Combining all of the terms gives the final result. \\Halmos

### Certainty Equivalence

So far we have considered the scenario where the dynamics matrices $(A,B)$ are known to the algorithm in advance. This raises an important question: how do estimation errors in the input matrices $A$ and $B$ impact the downstream approximation errors of the Pareto front? To address this, we employ the simplest method for controlling a dynamical system with unknown transitions: certainty equivalence. A model of the system is constructed, and the control policy is designed by treating this fitted model as the true system. Although this method is straightforward, its efficiency is not guaranteed a priori, as small modeling errors could lead to undesirable stability behavior and varied objective performance. In this section, we demonstrate that when the approximation errors in the dynamics are of the same order as the desired approximation errors in the Pareto front, the straightforward extension of the algorithm from [Section 4](https://arxiv.org/html/2408.04488v2#S4 "4 Approximating the Pareto Frontier of MObjLQR") with the inclusion of certainty equivalence provides a uniform approximation guarantee to the Pareto front.

In the following we assume the algorithm has access to estimates $\hat{A}$ and $\hat{B}$ for $A$ and $B$ respectively. We further denote:

as the commensurate LQR cost ([Eq. 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation")) where $A$ and $B$ are replaced with $\hat{A}$ and $\hat{B}$. We similarly overload notation and use ${{\hat{\mathcal{L}}}_{i}{(K)}}\operatorname{:-}{\hat{\mathcal{L}}{(K,Q_{i},R_{i})}}$ and ${{\hat{\mathcal{L}}}_{w}{(K)}}\operatorname{:-}{\hat{\mathcal{L}}{(K,Q_{w},R_{w})}}$. Before stating the main results we describe the algorithm similar to [Section 4](https://arxiv.org/html/2408.04488v2#S4 "4 Approximating the Pareto Frontier of MObjLQR") but instead using certainty equivalence for the optimal control on the scalarization points.

### Algorithm

Let $N_{\epsilon}$ be an $\epsilon$-net of $\Delta{({\lbrack m\rbrack})}$ such that for any $w \in {\Delta{({\lbrack m\rbrack})}}$ there exists $w_{\epsilon} \in N_{\epsilon}$ with ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Note that ${|N_{\epsilon}|} = {O{(\epsilon^{- m})}}$. Compute

where we denote ${\hat{K}}_{w}$ as the optimizer to ${\hat{\mathcal{L}}}_{w}{( \cdot )}$. We will show that so long as $\parallel{A - \hat{A}}\parallel$ and $\parallel{B - \hat{B}}\parallel$ are bounded above by $\epsilon$, we can obtain an $\epsilon$ approximation to the Pareto front. A major technical contribution of this section is establishing that the learned control $\hat{K}$ remains stable under the true dynamics dictated by $A$ and $B$.

### Theorem 6.3

Suppose that ${\parallel\Delta_{A}\parallel} \leq \epsilon$ and ${\parallel\Delta_{B}\parallel} \leq \epsilon$, [Equation 1](https://arxiv.org/html/2408.04488v2#S2.E1 "In 2.1 Multi-Objective LQR ‣ 2 Preliminary and Notation") holds, and that

Then for every $K \in {\text{PF}{(\mathcal{S})}}$ there exists a ${\hat{K}}_{\epsilon} \in {{\hat{\text{PF}}}_{\epsilon}{(\mathcal{S})}}$ which also stabilizes $(A,B)$ and has:

Note here that we look for approximation errors on the true LQR objective $\mathcal{L}{( \cdot )}$ subject to the nominal dynamics dictated by $A$ and $B$, instead of the estimated ones. An additional technical detail for this result is verifying that $\mathcal{L}_{w}{({\hat{K}}_{\epsilon})}$ is well defined and finite, since ${\hat{K}}_{\epsilon}$ is only known to stabilize $(\hat{A},\hat{B})$ and not necessarily the nominal dynamics $(A,B)$. We will show for sufficiently small $\epsilon$ that ${\hat{K}}_{\epsilon}$ indeed stabilizes the system. This additional requirement for stability is the primary driver of why [Theorem 6.3](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem3 "Theorem 6.3 ‣ Algorithm ‣ 6.1 Certainty Equivalence ‣ 6 Main Results on MObjLQR") requires $\epsilon$ to be smaller than that of [Theorem 6.1](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem1 "Theorem 6.1 ‣ Algorithm ‣ 6 Main Results on MObjLQR").

### Proof 6.4

Proof We start with the following lemma establishing that replacing $(A,B)$ with $(\hat{A},\hat{B})$ yields $O{(\epsilon)}$ approximations for the optimal controllers with fixed cost matrices. Indeed, we have:

### Lemma 6.5

For all $w \in {\Delta{({\lbrack m\rbrack})}}$ suppose that $K$ optimizes $\mathcal{L}_{w}{( \cdot )}$ and $\hat{K}$ optimizes ${\hat{\mathcal{L}}}_{w}{( \cdot )}$. Then for every $i \in {\lbrack m\rbrack}$ we have:

### Proof 6.6

Proof Using [Lemma 10.18](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.18 (Lemma 6 of Fazel et al. ) ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") we have that:

where $P_{\hat{K}}^{L} = {\text{dlyape}{({A + {B\hat{K}}},I)}}$, $P_{K} = {\text{dlyape}{({({A + {BK}})}^{\top},{Q_{i} + {K^{\top}R_{i}K}})}}$, and $E_{K} = {{{({R_{i} + {B^{\top}P_{K}B}})}K} - {B^{\top}P_{K}A}}$. Hence we have, denoting $\Delta_{K} = {\hat{K} - K}$,

We deal with the terms one by one. First notice that ${\parallel E_{K}\parallel} \leq {2\Gamma^{3}{\parallel P_{K}\parallel}}$ and by [Lemma 10.12](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.12 ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") that

However, using [Corollary 5.10](https://arxiv.org/html/2408.04488v2#S5. "Corollary 5.10 ‣ 5.2 Upper Bounds on Control and Stability Margin ‣ 5 Perturbation Theory for the Discrete Riccati Equation") to establish sensitivity on the solutions to $\text{dare}{(A,B,Q_{w},R_{w})}$ and $\text{dare}{(\hat{A},\hat{B},Q_{w_{\epsilon}},R_{w_{\epsilon}})}$ as well as [Lemma 10.23](https://arxiv.org/html/2408.04488v2#S10. "Lemma 10.23 (Adapted from Proposition 1 of Mania et al. ) ‣ 10.2 LQR Properties ‣ 10 Auxilary Lemmas") we have the following:

Thus we have that:

Combining all of the terms gives the result. \\Halmos

With the previous lemma in hand, [Theorem 6.3](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem3 "Theorem 6.3 ‣ Algorithm ‣ 6.1 Certainty Equivalence ‣ 6 Main Results on MObjLQR") follows via the triangle inequality, [Lemma 6.5](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem5 "Lemma 6.5 ‣ Proof 6.4 ‣ Algorithm ‣ 6.1 Certainty Equivalence ‣ 6 Main Results on MObjLQR"), and [Theorem 6.1](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem1 "Theorem 6.1 ‣ Algorithm ‣ 6 Main Results on MObjLQR"). For example, let $K \in {\text{PF}{(\mathcal{S})}}$ be arbitrary and $w \in {\Delta{({\lbrack m\rbrack})}}$ such that $K$ optimizes $\mathcal{L}_{w}{( \cdot )}$. Since $N_{\epsilon}$ is an $\epsilon$-net of $\Delta{({\lbrack m\rbrack})}$ let $w_{\epsilon} \in N_{\epsilon}$ with ${\parallel{w - w_{\epsilon}}\parallel}_{1} \leq \epsilon$. Denote by ${\hat{K}}_{\epsilon}$ as the control which optimizes ${\hat{\mathcal{L}}}_{w_{\epsilon}}{( \cdot )}$ and $K_{\epsilon}$ the control which optimizes $\mathcal{L}_{w_{\epsilon}}{( \cdot )}$. Note that $K_{\epsilon} \in {\text{PF}_{\epsilon}{(\mathcal{S})}}$. For the first property we have

The first term is bounded by [Theorem 6.1](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem1 "Theorem 6.1 ‣ Algorithm ‣ 6 Main Results on MObjLQR"), and the second via [Lemma 6.5](https://arxiv.org/html/2408.04488v2#S6.Thmtheorem5 "Lemma 6.5 ‣ Proof 6.4 ‣ Algorithm ‣ 6.1 Certainty Equivalence ‣ 6 Main Results on MObjLQR"). The entry wise approximation gap is proven identically. \\Halmos

## Conclusion

In this paper, we discussed the Linear Quadratic Regulator (LQR), a prevalent model in control theory with applications spanning fields such as energy management and robotics. Traditional LQR methodologies focus on optimizing a predefined combination of objectives, which can obscure the relationship between individual metrics and complicate the identification of optimal tradeoffs. Addressing this limitation, we demonstrated the sufficiency of linear scalarization in enumerating the Pareto front in multi-objective LQR. Furthermore, we established that an exhaustive search over an $\epsilon$-discretized set of weights yields an $\epsilon$ approximation to the Pareto front. Notably, our algorithm is already used in practice without theoretical justification, and this work serves to resolve this open problem in the literature. Follow-ups to this work include investigating the impact of the theoretical results on $(i)$ affine constraints on the control inputs $u$ and states $x$, and $({ii})$ the role of partial observability.
