<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Revisiting Subgradient Dominance in Robust MDPs: Counterexamples, Hardness, and Sufficient Conditions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Projected subgradient descent (PSD) has gained popularity for solving robust Markov decision processes (RMDPs) because it applies to a broader class of uncertainty sets than traditional dynamic programming. Existing work claims that RMDPs with a general compact uncertainty set satisfy the subgradient dominance property, under which exact PSD converges to an epsilon-optimal policy in a polynomial number of updates. We show that these claims are incorrect. Even when the uncertainty set has cardinality two, the RMDP objective is not subgradient-dominant and can admit suboptimal strict local minima. Moreover, we prove that finding an epsilon-optimal policy can be NP-hard even in settings where subgradients are efficiently computable: (i) finite transition uncertainty sets and (ii) sa-rectangular finite transition uncertainty sets with finite cost uncertainty sets. Finally, we identify two conditions under which RMDPs do satisfy subgradient dominance: when, for each policy, either the worst-case transition kernel or the worst-case action-value function is unique.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dealing with environmental model uncertainty is crucial for practical decision-making problems. Robust Markov decision processes (RMDPs) provide a framework for designing policies that are robust to such uncertainty, where transition kernels and cost functions are chosen adversarially from an uncertainty set. Recently, projected subgradient descent (PSD) has emerged as a popular approach for solving RMDPs. PSD methods are particularly appealing for their broad applicability: they accommodate general uncertainty sets for which subgradients can be efficiently computed (e.g., finite sets), whereas traditional dynamic programming (DP) methods typically require stronger structural assumptions on the uncertainty set.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing RMDP literature guarantees the performance of PSD by establishing the *subgradient dominance property*, under which every stationary point is globally optimal. These results appear mathematically sound, as they sidestep classical NP-hardness results for RMDPs, such as those of Wiesemann et al., by assuming access to exact subgradients. Unfortunately, we show that this line of analysis is flawed, rendering the claimed PSD guarantees invalid. In particular, we prove that the RMDP objective is not subgradient-dominant in general. Even a very simple RMDP with a finite uncertainty set of cardinality two admits a suboptimal strict local minimum, and PSD can get stuck in its neighborhood (\\crefexample:RMDP-failure).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, we establish a stronger negative result: finding an $\varepsilon$-optimal policy can be NP-hard even in settings where subgradients are efficiently computable, namely (i) finite transition uncertainty sets (\\crefproposition:NP-hardness) and (ii) $sa$-rectangular finite transition uncertainty sets with finite cost uncertainty sets (\\crefproposition:NP-hard-sa-rect). This hardness result rules out polynomial-time algorithms for approximately solving general RMDPs unless $\text{P} = \text{NP}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite these negative results, PSD can succeed under additional structure. We identify two sufficient conditions under which PSD finds $\varepsilon$-optimal policies (\\creftheorem:PSD-succeeds): when, for each policy, either the worst-case transition kernel or the worst-case action-value function is unique. These conditions cover several previously studied settings, including regularized RMDPs, $sa$- and $r$-rectangular uncertainty sets, cost-robust MDPs and convex MDPs. A summary of our results is provided in \\creftable:results-summary. Overall, our findings clarify existing misunderstandings about PSD in RMDPs and provide precise conditions under which its guarantees can be restored.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. \\crefsec:problem-setup introduces the RMDP formulation and the PSD algorithm. \\crefsec:failure of PSD presents our negative results for finite uncertainty sets. \\crefsec:PSD-succeeds establishes sufficient conditions for the success of PSD. Finally, \\crefsec:discussion situates our contributions within the related literature and discusses the limitations of our work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

\rowcolorgray!15 s a-rectangular finite 𝒫 × Finite 𝒞
Robust constrained MDPs with rectangular 𝒫

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Worst-case transition kernel is unique for each policy (\crefassm:unique-worst-case-occupancy)
Yes (\creftheorem:PSD-succeeds)

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Worst-case Q function is unique for each policy (\crefassm:unique-robust-value)
Yes (\creftheorem:PSD-succeeds)
s a and r-rectangular RMDPs

<!-- chunk {"id": "body-0011", "role": "body", "section": "Basic notation", "weight": 1.0} -->

$\delta_{\mathcal{X}}{(x)}$ denotes the indicator function which takes value $0$ if $x \in \mathcal{X}$ and $+ \infty$ otherwise. All scalar operations and inequalities applied to vectors or functions are understood elementwise.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Basic notation", "weight": 1.0} -->

For a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, we let $\partial{f{(x)}}$ denote the set of Fréchet subgradients of $f$ at $x \in {\mathbb{R}}^{d}$. If $\partial{f{(x)}}$ is a singleton, we denote its element by ${\nabla f}{(x)}$ and refer to it as the gradient of $f$ at $x$. A point $x$ is said to be *stationary* for $f$ if $\mathbf{0} \in {\partial{f{(x)}}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Robust MDPs", "weight": 1.0} -->

An infinite-horizon tabular RMDP is defined by a tuple $(\mathcal{S},\mathcal{A},\mu,\gamma,\mathcal{U})$, where $\mathcal{S}$ and $\mathcal{A}$ are finite state and action spaces, respectively; $\mu \in {\Delta{(\mathcal{S})}}$ is the initial state distribution; and $\gamma \in {\lbrack 0,1)}$ is the discount factor. The set $\mathcal{U}$ is a compact uncertainty set of cost functions and transition kernels. We refer to a pair ${(c,P)} \in \mathcal{U}$ as a *model*.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Robust MDPs", "weight": 1.0} -->

For each ${(c,P)} \in \mathcal{U}$, the cost function $c:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$ specifies the cost of taking action $a$ in state $s$, and the transition kernel $P$ satisfies $P{( \cdot \mid s,a)} \in \Delta{(\mathcal{S})}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Robust MDPs", "weight": 1.0} -->

When the uncertainty set decomposes as $\mathcal{U} = {\mathcal{C} \times \mathcal{P}}$, we use $\mathcal{C}$ and $\mathcal{P}$ to denote the cost and transition sets, respectively. If both $\mathcal{C}$ and $\mathcal{P}$ are singletons, the RMDP reduces to a standard MDP. If $\mathcal{P}$ is a singleton, the problem is known as a *cost-robust MDP*, which encompasses a variety of decision-making problems (e.g., convex MDPs; see \\crefsec:PSD-succeeds-general-cost).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Robust MDPs", "weight": 1.0} -->

A (stationary Markov) policy $\pi$ is a probability kernel such that $\pi{( \cdot |{s)} \in \Delta{(\mathcal{A})}}$ specifies the action distribution at state $s \in \mathcal{S}$. The set of all policies is denoted by $\Pi \subset {\mathbb{R}}^{{|\mathcal{S}|} \times {|\mathcal{A}|}}$, which corresponds to the *direct parameterization* policy class.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Robust MDPs", "weight": 1.0} -->

The value function $V_{c,P}^{\pi}:{\mathcal{S}\rightarrow{\mathbb{R}}}$ (and the action-value function $Q_{c,P}^{\pi}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$) represents the expected total cost under policy $\pi$ starting from a state $s$ (and from a state--action pair $(s,a)$, respectively).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Robust MDPs", "weight": 1.0} -->

The robust total cost of a policy $\pi$ is defined as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Rectangularity for Transition Uncertainty Sets", "weight": 1.0} -->

Without any assumptions on the transition set $\mathcal{P}$, computing the robust total cost $J_{\mathcal{P}}{(\pi)}$ is NP-hard, even to approximate.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Rectangularity for Transition Uncertainty Sets", "weight": 1.0} -->

Here, $\times_{s,a}$ denotes the Cartesian product over all state--action pairs. Intuitively, $sa$-rectangularity allows the adversary to choose worst-case transitions independently for each state--action pair.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Rectangularity for Transition Uncertainty Sets", "weight": 1.0} -->

Here, ${\phi{(s,a)}} \in {\Delta{({\lbrack r\rbrack})}}$ and ${w_{i}{( \cdot )}} \in {\Delta{(\mathcal{S})}}$. Unlike $sa$-rectangularity, $s$-rectangular uncertainty sets allow the adversary to select worst-case transitions independently across states, but not across actions. The $r$-rectangular structure resembles low-rank MDP models, in which the transition kernel admits a linear decomposition via a feature map $\phi$ of dimension $r$. Although both notions relax $sa$-rectangularity, they are mutually exclusive: neither $s$-rectangularity nor $r$-rectangularity contains the other.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Rectangularity for Transition Uncertainty Sets", "weight": 1.0} -->

These forms of rectangularity enable efficient computation of the robust total cost $J_{\mathcal{P}}{(\pi)}$ using dynamic programming (DP) methods. Moreover, an $\varepsilon$-optimal policy can be computed in time polynomial in $|\mathcal{S}|$, $|\mathcal{A}|$, ${({1 - \gamma})}^{- 1}$, $\log\varepsilon^{- 1}$, and the description length of $\mathcal{P}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Projected Subgradient Descent for Robust MDPs", "weight": 1.0} -->

Beyond DP methods for rectangular uncertainty sets, an alternative line of work has explored *projected subgradient descent* (PSD) for solving RMDPs. Unlike DP-based approaches, PSD does not rely on strong structural assumptions on the uncertainty sets $\mathcal{C}$ or $\mathcal{P}$; instead, it requires access only to a worst-case policy subgradient. This flexibility makes PSD applicable to classes of RMDPs that are not amenable to DP methods. For instance, when the transition set is finite (e.g., $\mathcal{P} = {\{ P_{1},P_{2}\}}$), PSD is applicable whereas DP methods generally are not.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Projected Subgradient Descent for Robust MDPs", "weight": 1.0} -->

where $\eta > 0$ is the learning rate and ${Proj}_{\Pi}$ denotes the Euclidean projection onto $\Pi$, which can be implemented efficiently.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Failure of Projected Subgradient Descent in Robust MDPs", "weight": 1.0} -->

Because the total cost function is nonconvex in the policy parameterization, the stationarity guarantee in \\creflemma:stationary-convergence alone does not imply near-optimality. To bridge this gap, prior works have attempted to establish the *subgradient dominance* property for the robust total cost $J_{\mathcal{U}}$:^11^1Wang et al. adopts the formulation in \\crefeq:subgrad-dom-Moreau, while Kitamura et al. uses the stronger form in \\crefeq:strong-subgrad-dom. Both notions are sufficient to guarantee that PSD efficiently finds an $\varepsilon$-optimal policy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Counterexample Where PSD Fails", "weight": 1.0} -->

Consider RMDPs with uncertainty only in the transition kernel, i.e., $\mathcal{U} = \mathcal{P}$. Several prior works claim that, under the full-support assumption on the initial distribution (\\crefassumption:init-dist), the robust total cost $J_{\mathcal{P}}$ is subgradient-dominant for any compact uncertainty set $\mathcal{P}$. We show that these claims are incorrect. In fact, the robust total cost need not be subgradient-dominant even for a simple transition set. Specifically, when ${|\mathcal{P}|} = 2$, the function $J_{\mathcal{P}}$ can already admit a suboptimal strict local minimum. The technical errors in the prior analyses are explained in \\crefsec:proof-error-in-prior-work.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Counterexample Where PSD Fails", "weight": 1.0} -->

[A deterministic RMDP with 𝒫 = {P1, P2}. Transitioning from state s+ incurs a cost of + 1. ] {subfigure}[Robust total cost landscape with γ = 0.9.]
Figure 1: An RMDP example where PSD fails (left) and the corresponding robust total cost landscape (right). The policy π2, which always selects action a2, is a strictly suboptimal local minimum. Details are provided in \crefexample:RMDP-failure.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 3.3 (An RMDP where PSD fails)", "weight": 1.0} -->

The policy ${\overset{\sim}{\pi}}_{2}$ deliberately visits the costly state $s_{+}$ and therefore incurs a larger robust total cost than ${\overset{\sim}{\pi}}_{1}$. For this instance, the following proposition holds. The proof is given in \\crefsec:proof-of-psd-trap.

<!-- chunk {"id": "body-0029", "role": "body", "section": "\\\\texorpdfstringNP-hardness of $\\varepsilon$-Optimal Policy IdentificationNP-hardness of ε-Optimal Policy Identification", "weight": 1.0} -->

Since PSD fails to find an $\varepsilon$-optimal policy under general uncertainty sets, a natural question is whether any algorithm can efficiently identify an $\varepsilon$-optimal policy in such settings. Unfortunately, the answer is negative. Even when the transition set is finite and policy evaluation can be performed efficiently, identifying an $\varepsilon$-optimal policy is NP-hard.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sufficient Conditions When Projected Subgradient Descent Succeeds", "weight": 1.0} -->

Although PSD can fail for general RMDPs, it succeeds under additional conditions. In this section, we identify two sufficient conditions under which the subgradient dominance property (12. ‣ 3 Failure of Projected Subgradient Descent in Robust MDPs ‣ Revisiting Subgradient Dominance in Robust MDPs: Counterexamples, Hardness, and Sufficient Conditions")) holds.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sufficient Conditions When Projected Subgradient Descent Succeeds", "weight": 1.0} -->

Our assumptions are motivated by the failure mode of PSD in \\crefexample:RMDP-failure. Intuitively, suboptimal local minima can arise when different worst-case models prescribe conflicting local directions toward the global optimum. Our assumptions rule out such conflict. \\Crefassm:unique-robust-value requires all active worst-case models to induce the same action-value function, so by \\crefeq:J-gradient they agree on the local improvement direction. \\Crefassm:unique-worst-case-occupancy requires agreement only at the transition level, since conflict in the cost is known not to create this pathology. The following theorem shows that either condition is sufficient for subgradient dominance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "When $\\mathcal{P}^{\\pi}$ is a singleton (\\\\crefassm:unique-worst-case-occupancy)", "weight": 1.0} -->

Let $P \in \mathcal{P}^{\pi}$ be the unique worst-case transition kernel under $\pi$. The right-hand side of \\crefeq:alpha-min-expression is bounded as

<!-- chunk {"id": "body-0033", "role": "body", "section": "When $\\mathcal{Q}^{\\pi}$ is a singleton (\\\\crefassm:unique-robust-value)", "weight": 1.0} -->

where (a), (b), and (c) follow similarly as in the previous case. This concludes the proof.

<!-- chunk {"id": "body-0034", "role": "body", "section": "When $\\mathcal{Q}^{\\pi}$ is a singleton (\\\\crefassm:unique-robust-value)", "weight": 1.0} -->

Combining \\creftheorem:PSD-succeeds with the stationarity guarantee in \\creflemma:stationary-convergence and the Moreau-envelope bound \\crefeq:subgrad-dom-Moreau, we obtain the following convergence guarantee.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Regularized RMDPs \\\\texorpdfstring(\\\\crefassm:unique-worst-case-occupancy,assm:unique-robust-value)(Assumptions 11 and 12)", "weight": 1.0} -->

Both \\crefassm:unique-worst-case-occupancy,assm:unique-robust-value are trivially satisfied when the worst-case model is unique for every policy $\pi$, i.e., when ${|\mathcal{U}^{\pi}|} = 1$. A common approach to enforcing ${|\mathcal{U}^{\pi}|} = 1$ is to introduce convex regularization that renders the adversary's objective strongly convex, thereby guaranteeing a unique worst-case model. For example, Yang et al.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Regularized RMDPs \\\\texorpdfstring(\\\\crefassm:unique-worst-case-occupancy,assm:unique-robust-value)(Assumptions 11 and 12)", "weight": 1.0} -->

where $P_{0}$ is a nominal transition kernel and $\tau > 0$ is a regularization parameter. When $\mathcal{P}$ is $sa$-rectangular with $\mathcal{P}_{s,a} = {\Delta{(\mathcal{S})}}$, the worst-case transition for $\pi$ is unique and satisfies

<!-- chunk {"id": "body-0037", "role": "body", "section": "Regularized RMDPs \\\\texorpdfstring(\\\\crefassm:unique-worst-case-occupancy,assm:unique-robust-value)(Assumptions 11 and 12)", "weight": 1.0} -->

While most existing results focus on rectangular uncertainty sets, the assumption ${|\mathcal{U}^{\pi}|} = 1$ itself does not require rectangularity.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Regularized RMDPs \\\\texorpdfstring(\\\\crefassm:unique-worst-case-occupancy,assm:unique-robust-value)(Assumptions 11 and 12)", "weight": 1.0} -->

where ${\parallel \cdot \parallel}_{F}$ denotes the Frobenius norm. Since the total cost $J_{P}{(\pi)}$ is weakly concave in $P$ due to its smoothness, the regularized objective becomes strongly concave for sufficiently large $\tau$. Consequently, for sufficiently large $\tau$, the worst-case transition kernel is unique even when $\mathcal{P}$ is non-rectangular. Characterizing broader classes of non-rectangular uncertainty sets that satisfy ${|\mathcal{U}^{\pi}|} = 1$ is an interesting direction for future work.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Cost-robust MDPs and Convex MDPs (\\\\texorpdfstring\\\\crefassm:unique-worst-case-occupancyAssumption 11)", "weight": 1.0} -->

assm:unique-worst-case-occupancy is also satisfied in cost-robust MDPs, where uncertainty lies solely in the cost function, that is, when $\mathcal{U} = \mathcal{C}$ for a compact cost set $\mathcal{C}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Cost-robust MDPs and Convex MDPs (\\\\texorpdfstring\\\\crefassm:unique-worst-case-occupancyAssumption 11)", "weight": 1.0} -->

Convex MDPs generalize diverse decision-making problems, including skill learning, inverse reinforcement learning, imitation learning, pure exploration, and constrained MDPs. We refer readers to Zahavy et al. for a comprehensive overview.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Cost-robust MDPs and Convex MDPs (\\\\texorpdfstring\\\\crefassm:unique-worst-case-occupancyAssumption 11)", "weight": 1.0} -->

Clearly, convex MDPs generalize cost-robust MDPs via ${f{(d)}} = {\max_{c \in \mathcal{C}}{\sum_{s,a}{d{(s,a)}c{(s,a)}}}}$. Conversely, cost-robust MDPs also include convex MDPs. Let $f^{\ast}{(g)}: = \sup_{d \in {{dom}f}}\sum_{s,a}g{(s,a)}d{(s,a)} - f{(d)}$ denote the convex conjugate of $f$. Then, the convex MDP problem can be rewritten as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Cost-robust MDPs and Convex MDPs (\\\\texorpdfstring\\\\crefassm:unique-worst-case-occupancyAssumption 11)", "weight": 1.0} -->

where (a) follows from the one-to-one mapping between $d_{M}^{\pi}$ and $\pi$, (b) uses definition of the convex conjugate, and (c) uses the one-to-one mapping again and substitutes a cost set $\mathcal{C} = \left\{ c \in {\mathbb{R}}^{{|\mathcal{S}|}{|\mathcal{A}|}} \middle| \left. c{(s,a)} = g{(s,a)} - f^{\ast}{(g)},g \in {dom}f^{\ast} \right\} \right.$. This equivalence shows that convex MDPs satisfy \\crefassm:unique-worst-case-occupancy and thus enjoys the subgradient dominance property.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Cost-robust MDPs and Convex MDPs (\\\\texorpdfstring\\\\crefassm:unique-worst-case-occupancyAssumption 11)", "weight": 1.0} -->

We finally note that extending convex MDPs to include transition uncertainty breaks subgradient dominance, even when $\mathcal{P}$ is $sa$-rectangular. Since convex MDPs subsume constrained MDPs, the extended setting encompasses the NP-hard RCMDP instances shown in \\crefproposition:NP-hard-sa-rect.

<!-- chunk {"id": "body-0044", "role": "body", "section": "\\\\texorpdfstring$r$r-Rectangular RMDPs (\\\\texorpdfstring\\\\crefassm:unique-robust-valueAssumption 12)", "weight": 1.0} -->

It is well known that $sa$-rectangular RMDPs satisfy ${|\mathcal{Q}^{\pi}|} = 1$ for every policy $\pi$, and therefore meet \\crefassm:unique-robust-value. We show that this property extends to the strictly more general class of $r$-rectangular RMDPs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Hardness of approximate optimization", "weight": 1.0} -->

While the hardness of solving RMDPs has long been recognized, it has remained unclear whether finding an $\varepsilon$-optimal policy is hard even when the robust total cost and its subgradients are efficiently computable. This ambiguity has led to incorrect convergence claims for PSD under general uncertainty sets.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Hardness of approximate optimization", "weight": 1.0} -->

The seminal work of Wiesemann et al. shows that evaluating the objective of general RMDPs is strongly NP-hard, but does not provide the hardness of policy optimization. Bagnell et al. establish NP-hardness of policy optimization only for deterministic optimal policies. Mannor et al. claim hardness of approximate optimization under general uncertainty sets; however, the proof is inaccessible, and it is unclear whether the hardness is due to evaluation or optimization. More recently, Ou and Bi prove NP-hardness of finding an optimal policy for finite uncertainty sets, but do not address approximate optimization.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hardness of approximate optimization", "weight": 1.0} -->

In contrast, our results (\\crefproposition:NP-hardness,proposition:NP-hard-sa-rect) establish NP-hardness of $\varepsilon$-optimal policy identification in two settings that admit efficient computation of both the robust total cost and its subgradients: (i) RMDPs with a finite transition set, and (ii) RMDPs with a finite $sa$-rectangular transition set and a finite cost set. Additionally, our \\crefexample:RMDP-failure demonstrates a concrete failure case of PSD in the finite uncertainty set setting, further corroborating our hardness results.

<!-- chunk {"id": "body-0048", "role": "body", "section": "First-order methods for RMDPs", "weight": 1.0} -->

Several works have established performance guarantees for first-order methods in specific classes of RMDPs. Li et al. prove global convergence of state-wise mirror descent for $sa$-rectangular uncertainty sets, while Wang and Zou analyze PSD for $R$-contamination uncertainty sets, which are also $sa$-rectangular. More recently, convex MDPs have been shown to satisfy subgradient dominance due to an underlying hidden convexity structure.

<!-- chunk {"id": "body-0049", "role": "body", "section": "First-order methods for RMDPs", "weight": 1.0} -->

All of these settings are captured by the sufficient conditions identified in \\crefsec:PSD-succeeds. In addition, we show that $r$-rectangular and regularized RMDPs satisfy our conditions, that were not previously known to admit subgradient dominance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Open questions", "weight": 1.0} -->

Our sufficient conditions do not cover $s$-rectangular RMDPs, despite the existence of efficient DP-based algorithms for this setting. This gap makes the $s$-rectangular case particularly intriguing: while DP can efficiently solve such RMDPs, whether PSD converges to globally optimal policies remains open.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Open questions", "weight": 1.0} -->

We conjecture that $s$-rectangular RMDPs satisfy the subgradient dominance property and that dominance can hold under conditions weaker than \\crefassm:unique-worst-case-occupancy,assm:unique-robust-value. The following proposition shows that these assumptions are not necessary.
