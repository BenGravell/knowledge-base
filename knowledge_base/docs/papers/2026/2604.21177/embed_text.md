<!-- arxiv-full-text:v1 {"arxiv_id": "2604.21177", "source": "arxiv-html"} -->

## Introduction

Dealing with environmental model uncertainty is crucial for practical decision-making problems. Robust Markov decision processes (RMDPs) provide a framework for designing policies that are robust to such uncertainty, where transition kernels and cost functions are chosen adversarially from an uncertainty set. Recently, projected subgradient descent (PSD) has emerged as a popular approach for solving RMDPs. PSD methods are particularly appealing for their broad applicability: they accommodate general uncertainty sets for which subgradients can be efficiently computed (e.g., finite sets), whereas traditional dynamic programming (DP) methods typically require stronger structural assumptions on the uncertainty set.

Existing RMDP literature guarantees the performance of PSD by establishing the *subgradient dominance property*, under which every stationary point is globally optimal. These results appear mathematically sound, as they sidestep classical NP-hardness results for RMDPs, such as those of Wiesemann et al., by assuming access to exact subgradients. Unfortunately, we show that this line of analysis is flawed, rendering the claimed PSD guarantees invalid. In particular, we prove that the RMDP objective is not subgradient-dominant in general. Even a very simple RMDP with a finite uncertainty set of cardinality two admits a suboptimal strict local minimum, and PSD can get stuck in its neighborhood (\\crefexample:RMDP-failure).

Moreover, we establish a stronger negative result: finding an $\varepsilon$-optimal policy can be NP-hard even in settings where subgradients are efficiently computable, namely (i) finite transition uncertainty sets (\\crefproposition:NP-hardness) and (ii) $sa$-rectangular finite transition uncertainty sets with finite cost uncertainty sets (\\crefproposition:NP-hard-sa-rect). This hardness result rules out polynomial-time algorithms for approximately solving general RMDPs unless $\text{P}=\text{NP}$.

Despite these negative results, PSD can succeed under additional structure. We identify two sufficient conditions under which PSD finds $\varepsilon$-optimal policies (\\creftheorem:PSD-succeeds): when, for each policy, either the worst-case transition kernel or the worst-case action-value function is unique. These conditions cover several previously studied settings, including regularized RMDPs, $sa$- and $r$-rectangular uncertainty sets, cost-robust MDPs and convex MDPs. A summary of our results is provided in \\creftable:results-summary. Overall, our findings clarify existing misunderstandings about PSD in RMDPs and provide precise conditions under which its guarantees can be restored.

The remainder of the paper is organized as follows. \\crefsec:problem-setup introduces the RMDP formulation and the PSD algorithm. \\crefsec:failure of PSD presents our negative results for finite uncertainty sets. \\crefsec:PSD-succeeds establishes sufficient conditions for the success of PSD. Finally, \\crefsec:discussion situates our contributions within the related literature and discusses the limitations of our work.

\rowcolorgray!15 Finite 𝒫 × Singleton 𝒞 \rowcolorgray!15 sa-rectangular finite 𝒫 × Finite 𝒞 Robust constrained MDPs with rectangular 𝒫 Worst-case transition kernel is unique for each policy (\crefassm:unique-worst-case-occupancy) Yes (\creftheorem:PSD-succeeds) Worst-case Q function is unique for each policy (\crefassm:unique-robust-value) Yes (\creftheorem:PSD-succeeds) sa and r-rectangular RMDPs Table 1: Summary of the subgradient dominance property across different RMDP settings. 𝒞 and 𝒫 denote the cost and transition uncertainty sets, respectively. PSD is guaranteed to find ε-optimal policies in settings marked “Yes”, while those marked “No” are NP-hard even to approximate (\crefproposition:NP-hardness,proposition:NP-hard-sa-rect). Highlighted settings were previously believed to be subgradient-dominant.

## Preliminaries

### Basic notation

The probability simplex over a finite set $\mathcal{S}$ is denoted by $\Delta(\mathcal{S})$. For an integer $n$, let $[n]\vcentcolon\nolinebreak\mkern-1.2mu=\left\{1,\dots,n\right\}$. We define $\mathbf{0}\vcentcolon\nolinebreak\mkern-1.2mu=(0,\ldots,0)^{\top}$ and $\mathbf{1}\vcentcolon\nolinebreak\mkern-1.2mu=(1,\ldots,1)^{\top}$. For a set $\mathcal{X}\subset\mathbb{R}^{d}$, we define $\operatorname{dist}(\mathbf{0};\mathcal{X})\vcentcolon\nolinebreak\mkern-1.2mu=\inf_{x\in\mathcal{X}}\lVert x\rVert_{2}$. For $\mathcal{X}\subset\mathbb{R}^{d}$, $\operatorname{conv}\mathcal{X}$ denotes its convex hull. $\delta_{\mathcal{X}}(x)$ denotes the indicator function which takes value $0$ if $x\in\mathcal{X}$ and $+\infty$ otherwise. All scalar operations and inequalities applied to vectors or functions are understood elementwise.

For a function $f:\mathbb{R}^{d}\to\mathbb{R}$, we let $\partial f(x)$ denote the set of Fréchet subgradients of $f$ at $x\in\mathbb{R}^{d}$. If $\partial f(x)$ is a singleton, we denote its element by $\nabla f(x)$ and refer to it as the gradient of $f$ at $x$. A point $x$ is said to be *stationary* for $f$ if $\mathbf{0}\in\partial f(x)$.

### Robust MDPs

An infinite-horizon tabular RMDP is defined by a tuple $(\mathcal{S},\mathcal{A},\mu,\gamma,\mathcal{U})$, where $\mathcal{S}$ and $\mathcal{A}$ are finite state and action spaces, respectively; $\mu\in\Delta(\mathcal{S})$ is the initial state distribution; and $\gamma\in[0,1)$ is the discount factor. The set $\mathcal{U}$ is a compact uncertainty set of cost functions and transition kernels. We refer to a pair $(c,P)\in\mathcal{U}$ as a *model*. For each $(c,P)\in\mathcal{U}$, the cost function $c:\mathcal{S}\times\mathcal{A}\to$ specifies the cost of taking action $a$ in state $s$, and the transition kernel $P$ satisfies $P(\cdot\mid s,a)\in\Delta(\mathcal{S})$.

When the uncertainty set decomposes as $\mathcal{U}=\mathcal{C}\times\mathcal{P}$, we use $\mathcal{C}$ and $\mathcal{P}$ to denote the cost and transition sets, respectively. If both $\mathcal{C}$ and $\mathcal{P}$ are singletons, the RMDP reduces to a standard MDP. If $\mathcal{P}$ is a singleton, the problem is known as a *cost-robust MDP*, which encompasses a variety of decision-making problems (e.g., convex MDPs; see \\crefsec:PSD-succeeds-general-cost).

A (stationary Markov) policy $\pi$ is a probability kernel such that $\pi(\cdot\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s)\in\Delta(\mathcal{A})$ specifies the action distribution at state $s\in\mathcal{S}$. The set of all policies is denoted by $\Pi\subset\mathbb{R}^{|\mathcal{S}|\times|\mathcal{A}|}$, which corresponds to the *direct parameterization* policy class.

Given a transition kernel $P$, the occupancy measure $d^{\pi}_{P}\in\mathcal{S}\times\mathcal{A}\to\mathbb{R}$ represents the expected $\gamma$-discounted visitation frequency of each state--action pair under policy: where the expectation is taken over trajectories generated by $s_{0}\sim\mu$, $a_{h}\sim\pi(\cdot\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s_{h})$, and $s_{h+1}\sim P(\cdot\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s_{h},a_{h})$. The induced state occupancy measure is defined as $\overline{d}^{\pi}_{P}(s)\vcentcolon\nolinebreak\mkern-1.2mu=\sum_{a\in\mathcal{A}}d^{\pi}_{P}(s,a)$.

The value function $V^{\pi}_{c,P}:\mathcal{S}\to\mathbb{R}$ (and the action-value function $Q^{\pi}_{c,P}:\mathcal{S}\times\mathcal{A}\to\mathbb{R}$) represents the expected total cost under policy $\pi$ starting from a state $s$ (and from a state--action pair $(s,a)$, respectively). They are the unique solution to the following *Bellman equations*: | | $\displaystyle V^{\pi}_{c,P}(s)$ | $\displaystyle=c^{\pi}(s)+\gamma\sum_{s^{\prime}\in\mathcal{S}}P^{\pi}(s^{\prime}\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s)V^{\pi}_{c,P}(s^{\prime})\quad\forall s\in\mathcal{S}$ | | \(1\) | | | $\displaystyle\text{and}\quad Q^{\pi}_{c,P}(s,a)$ | $\displaystyle=c(s,a)+\gamma\sum_{s^{\prime}\in\mathcal{S}}P\left(s^{\prime}\mathchoice{\>}{\>}{\,}{\,}\middle|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s,a\right)V^{\pi}_{c,P}(s^{\prime})\quad\forall(s,a)\in\mathcal{S}\times\mathcal{A}\ $ | | | where we use shorthands $c^{\pi}(s)\vcentcolon\nolinebreak\mkern-1.2mu=\sum_{a}\pi(a\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s)c(s,a)$ and $P^{\pi}(s^{\prime}\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s)\vcentcolon\nolinebreak\mkern-1.2mu=\sum_{a}P(s^{\prime}\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s,a)\pi(a\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}s)$. We define the advantage function as $A^{\pi}_{c,P}(s,a)\vcentcolon\nolinebreak\mkern-1.2mu=V^{\pi}_{c,P}(s)-Q^{\pi}_{c,P}(s,a)$.

The robust total cost of a policy $\pi$ is defined as If $\mathcal{U}=\mathcal{C}\times\mathcal{P}$ and either $\mathcal{C}$ or $\mathcal{P}$ is a singleton, we write $\mathcal{U}=\mathcal{C}$ or $\mathcal{U}=\mathcal{P}$ for simplicity. We denote $J_{c,P}\vcentcolon\nolinebreak\mkern-1.2mu=J_{\{(c,P)\}}$ as the total cost under a fixed model and refer to $J_{\mathcal{U}}$ as the robust total cost.

The goal of an RMDP is to identify an optimal policy $\pi^{\star}$ that minimizes the robust total cost: We call a policy $\pi$ *$\varepsilon$-optimal* if it satisfies $J_{\mathcal{U}}(\pi)-J_{\mathcal{U}}(\pi^{\star})\leq\varepsilon$.

### Rectangularity for Transition Uncertainty Sets

Without any assumptions on the transition set $\mathcal{P}$, computing the robust total cost $J_{\mathcal{P}}(\pi)$ is NP-hard, even to approximate. A widely adopted regularity condition is $sa$-rectangularity, defined as: Here, $\times_{s,a}$ denotes the Cartesian product over all state--action pairs. Intuitively, $sa$-rectangularity allows the adversary to choose worst-case transitions independently for each state--action pair.

Because this assumption can yield overly conservative policies, several works have proposed weaker notions of rectangularity, most notably *$s$-rectangularity* and *$r$-rectangularity*: Here, $\phi(s,a)\in\Delta([r])$ and $w_{i}(\cdot)\in\Delta(\mathcal{S})$. Unlike $sa$-rectangularity, $s$-rectangular uncertainty sets allow the adversary to select worst-case transitions independently across states, but not across actions. The $r$-rectangular structure resembles low-rank MDP models, in which the transition kernel admits a linear decomposition via a feature map $\phi$ of dimension $r$. Although both notions relax $sa$-rectangularity, they are mutually exclusive: neither $s$-rectangularity nor $r$-rectangularity contains the other.

These forms of rectangularity enable efficient computation of the robust total cost $J_{\mathcal{P}}(\pi)$ using dynamic programming (DP) methods. Moreover, an $\varepsilon$-optimal policy can be computed in time polynomial in $|\mathcal{S}|$, $|\mathcal{A}|$, $(1-\gamma)^{-1}$, $\log\varepsilon^{-1}$, and the description length of $\mathcal{P}$.

### Projected Subgradient Descent for Robust MDPs

Beyond DP methods for rectangular uncertainty sets, an alternative line of work has explored *projected subgradient descent* (PSD) for solving RMDPs. Unlike DP-based approaches, PSD does not rely on strong structural assumptions on the uncertainty sets $\mathcal{C}$ or $\mathcal{P}$; instead, it requires access only to a worst-case policy subgradient. This flexibility makes PSD applicable to classes of RMDPs that are not amenable to DP methods. For instance, when the transition set is finite (e.g., $\mathcal{P}=\{P_{1},P_{2}\}$), PSD is applicable whereas DP methods generally are not.

At iteration $t\in\mathbb{N}$, PSD updates $\pi_{t}$ to a new policy $\pi_{t+1}$: where $\eta>0$ is the learning rate and $\operatorname{Proj}_{\Pi}$ denotes the Euclidean projection onto $\Pi$, which can be implemented efficiently. The subgradient $g_{t}$ can be efficiently computed when a worst-case model in \\crefeq:RMDP is available:

### Lemma 2.1

Let $\mathcal{U}^{\pi}\vcentcolon\nolinebreak\mkern-1.2mu=\operatorname*{arg\,max}_{(c,P)\in\mathcal{U}}J_{c,P}(\pi)$ denote the set of worst-case models under policy $\pi$. For any $\pi\in\Pi$, it holds that eq:J-subgradient follows from a version of Danskin's theorem (\\creflemma:danskin's theorem in \\crefappendix:useful-lemmas) and \\crefeq:J-gradient is known as the *policy gradient theorem*.

The convergence behavior of the PSD update in \\crefeq:pol-grad-update can be analyzed using the *Moreau envelope* of *weakly convex* functions.

### Definition 2.2 (Moreau envelope)

For a function $f:\mathbb{R}^{d}\to\mathbb{R}$ and a parameter $\nu>0$, the Moreau envelope is defined by $\operatorname{M}_{\nu}\circ\;f:\mathbb{R}^{d}\to\mathbb{R}$ such that The minimal point is called the proximal point: $\operatorname{Prox}_{\nu f}(x)=\operatorname*{arg\,min}_{y\in\mathbb{R}^{d}}\left\{f(y)+\frac{1}{2\nu}\left\lVert x-y\right\rVert^{2}_{2}\right\}$.

### Definition 2.3

A function $f:\mathbb{R}^{d}\to\mathbb{R}$ is called $\omega$-weakly convex if there exists $\omega\geq 0$ such that $f(\cdot)+\frac{\omega}{2}\left\lVert\cdot\right\rVert_{2}^{2}$ is convex.

Weak convexity is a mild regularity condition satisfied by many functions in optimization. In particular, the pointwise maximum of smooth functions is weakly convex; hence, the robust total cost $J_{\mathcal{U}}$ is weakly convex. The Moreau envelope provides a smooth approximation of a weakly convex function. Specifically, if $f$ is proper and $\omega$-weakly convex, then for any $\nu\in(0,1/\omega)$, the Moreau envelope $\operatorname{M}_{\nu}\circ\;f$ is differentiable, with gradient given: Combining \\crefeq:Moreau-grad with the definition of the Moreau envelope yields Thus, a small Moreau-envelope gradient implies that $x$ is close to a point $\operatorname{Prox}_{\nu f}(x)$ that is nearly stationary for $f$. For further discussion of weakly convex functions and the Moreau envelope, see Davis and Drusvyatskiy; Renaud et al.; Rockafellar and Wets.

Applying these tools to RMDPs yields convergence guarantees for PSD. Define the extended objective $\macc@depth\@ne\macc@set@skewchar\macc@nested@a 111{J}_{\mathcal{U}}:\pi\in\mathbb{R}^{|\mathcal{S}|\times|\mathcal{A}|}\mapsto J_{\mathcal{U}}(\pi)+\delta_{\Pi}(\pi)$ which extends the domain of the robust total cost to $\mathbb{R}^{|\mathcal{S}|\times|\mathcal{A}|}$. Standard analyses of PSD for weakly convex functions imply that the iterates produced by \\crefeq:pol-grad-update converge to near-stationary points of the Moreau envelope (see \\crefsec:subgrad-dom-Moreau-derivation).

### Lemma 2.4

When $\eta=1/\sqrt{T}$, the PSD iterates in \\crefeq:pol-grad-update satisfies that Together with \\crefeq:Moreau-grad-to-subgrad, \\creflemma:stationary-convergence implies that there exists an iterate $\pi_{t}$ that lies close to a proximal point which is nearly stationary for $\macc@depth\@ne\macc@set@skewchar\macc@nested@a 111{J}_{\mathcal{U}}$.

## Failure of Projected Subgradient Descent in Robust MDPs

Because the total cost function is nonconvex in the policy parameterization, the stationarity guarantee in \\creflemma:stationary-convergence alone does not imply near-optimality. To bridge this gap, prior works have attempted to establish the *subgradient dominance* property for the robust total cost $J_{\mathcal{U}}$:^11^1Wang et al. adopts the formulation in \\crefeq:subgrad-dom-Moreau, while Kitamura et al. uses the stronger form in \\crefeq:strong-subgrad-dom. Both notions are sufficient to guarantee that PSD efficiently finds an $\varepsilon$-optimal policy.

### Definition 3.1 (Subgradient dominance)

The robust total cost $J_{\mathcal{U}}$ is said to be *subgradient-dominant* with constant $D>0$ if, for every $\pi\in\Pi$, In the standard MDP setting where $\mathcal{U}$ is a singleton, this condition reduces to the classical *gradient dominance* property, which is known to hold. {assumption} The initial distribution $\mu$ has full support, i.e., $\mu(s)>0$ for all $s\in\mathcal{S}$.

### Lemma 3.2

When $\mathcal{U}$ is a singleton and \\crefassumption:init-dist holds^22^2Such coverage condition is necessary to ensure the global convergence of policy gradient methods., the total cost function $J_{\mathcal{U}}$ satisfies \\crefeq:strong-subgrad-dom with constant $D=((1-\gamma)\min_{s}\mu(s))^{-1}$.

Intuitively, the quantity $G(\pi)$ measures the first-order stationarity of $\pi$ with respect to the robust objective. Using the Lipschitz continuity of $J_{\mathcal{U}}$, one can relate $G(\pi)$ to the gradient norm of the Moreau envelope, yielding the following inequality (see \\crefsec:subgrad-dom-Moreau-derivation for details): Consequently, if the robust total cost $J_{\mathcal{U}}$ is subgradient-dominant, then combining \\creflemma:stationary-convergence with \\crefeq:subgrad-dom-Moreau guarantees that PSD converges to an $\varepsilon$-optimal policy in $O(\varepsilon^{-4})$ policy updates.

### Counterexample Where PSD Fails

Consider RMDPs with uncertainty only in the transition kernel, i.e., $\mathcal{U}=\mathcal{P}$. Several prior works claim that, under the full-support assumption on the initial distribution (\\crefassumption:init-dist), the robust total cost $J_{\mathcal{P}}$ is subgradient-dominant for any compact uncertainty set $\mathcal{P}$. We show that these claims are incorrect. In fact, the robust total cost need not be subgradient-dominant even for a simple transition set. Specifically, when $\lvert\mathcal{P}\rvert=2$, the function $J_{\mathcal{P}}$ can already admit a suboptimal strict local minimum. The technical errors in the prior analyses are explained in \\crefsec:proof-error-in-prior-work. [A deterministic RMDP with 𝒫 = {P1, P2}. Transitioning from state s+ incurs a cost of +1.] {subfigure}[Robust total cost landscape with γ = 0.9.] Figure 1: An RMDP example where PSD fails (left) and the corresponding robust total cost landscape (right). The policy ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\pi_{2}}$, which always selects action ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}a_{2}}$, is a strictly suboptimal local minimum. Details are provided in \crefexample:RMDP-failure.

### Example 3.3 (An RMDP where PSD fails)

Consider a deterministic RMDP with three states $(s_{1},s_{2},s_{+})$, two actions $({\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}a_{1}},{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}a_{2}})$, and two transition kernels $\mathcal{P}=\{P_{1},P_{2}\}$, as illustrated in \\creffig:nonrect (left). We set the discount factor to $\gamma=0.9$ and the initial distribution to $\mu(s_{1})=\mu(s_{2})=0.45$, which satisfies \\crefassumption:init-dist. Let ${\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\tilde{\pi}_{1}}$ and ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}_{2}}$ denote the policies that always choose ${\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}a_{1}}$ and ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}a_{2}}$, respectively. The policy ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}_{2}}$ deliberately visits the costly state $s_{+}$ and therefore incurs a larger robust total cost than ${\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\tilde{\pi}_{1}}$. For this instance, the following proposition holds. The proof is given in \\crefsec:proof-of-psd-trap.

### Proposition 3.4

The following two claims hold in the example instance: ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}_{2}}$ is a suboptimal strict local minimum of $J_{\mathcal{P}}$ satisfying $0.505=J_{\mathcal{P}}({\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}_{2}})>J_{\mathcal{P}}({\color[rgb]{0,0,1}\definecolor[named]{pgfstrokecolor}{rgb}{0,0,1}\tilde{\pi}_{1}})=0.1$.

For all sufficiently small $\eta>0$, when initialized at ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}_{2}}$, the PSD update $\pi_{t+1}=\operatorname{Proj}_{\Pi}\left(\pi_{t}-\eta g_{t}\right)$ with any $g_{t}\in\partial J_{\mathcal{P}}(\pi_{t})$ satisfy $\|\pi_{t}-{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}_{2}}\|_{\infty}\leq 3\eta$ for all $t\geq 0$.

This result formally shows that $J_{\mathcal{P}}$ is not subgradient-dominant. Indeed, if it held, then \\crefeq:subgrad-dom-Moreau would imply that every local minimum is global, and \\creflemma:stationary-convergence would guarantee that PSD with sufficiently small $\eta$ converges to a global minimum. However, the first claim shows that ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}_{2}}$ is a strict local minimum that is not global, while the second claim shows that PSD can remain trapped near this suboptimal point. Both conclusions contradict subgradient dominance. These facts are also illustrated empirically in \\creffig:nonrect (right), which shows the landscape of the robust total cost function.

### \\texorpdfstringNP-hardness of $\varepsilon$-Optimal Policy IdentificationNP-hardness of ε-Optimal Policy Identification

Since PSD fails to find an $\varepsilon$-optimal policy under general uncertainty sets, a natural question is whether any algorithm can efficiently identify an $\varepsilon$-optimal policy in such settings. Unfortunately, the answer is negative. Even when the transition set is finite and policy evaluation can be performed efficiently, identifying an $\varepsilon$-optimal policy is NP-hard.

### Proposition 3.5 (Hardness for finite $\mathcal{P}$ and singleton $\mathcal{C}$)

For any $\varepsilon\leq 0.5\gamma^{3}(1-\gamma)^{-1}$, finding an $\varepsilon$-optimal policy in RMDPs with a finite transition set and a singleton cost set is NP-hard.

The proof is based on a reduction from the 3-SAT problem (see \\crefsec:proof-of-NP-hard). We discuss the differences from prior NP-hardness results for RMDPs in \\crefsec:discussion. In this setting, since the uncertainty set is finite, both the robust total cost and its subgradients can be approximated to $\delta$ accuracy in time polynomial in $|\mathcal{S}|$, $|\mathcal{A}|$, $(1-\gamma)^{-1}$, $\log\delta^{-1}$, and $\lvert\mathcal{U}\rvert$.

As a byproduct, we obtain an additional hardness result for RMDPs with a rectangular transition set and a finite cost set. This setting is especially relevant for *robust constrained MDPs* (RCMDPs), in which a policy must satisfy multiple robust constraints: Here, $c_{0},\ldots,c_{N}$ are the objective and constraint cost functions, and $b>0$ is a constraint threshold. When $\mathcal{P}$ is rectangular, the constraint term $\max_{n\in[N]}J_{c_{n},\mathcal{P}}(\pi)$ corresponds to an RMDP with a rectangular transition set and a non-rectangular (finite) cost set $\mathcal{C}=\{c_{1},\ldots,c_{N}\}$.

Recent work by Kitamura et al. proposes a PSD-based algorithm for RMDPs with a general transition set and a finite cost set, suggesting an efficient approach for solving RCMDPs. However, the following \\crefproposition:NP-hard-sa-rect shows that their results are incorrect. In particular, even when the transition set is $sa$-rectangular and finite, identifying an $\varepsilon$-optimal policy remains NP-hard, which in turn implies NP-hardness of solving RCMDPs.

### Proposition 3.6 (Hardness for $sa$-rectangular $\mathcal{P}$ and finite $\mathcal{C}$)

For any $\varepsilon\leq 0.5\gamma^{2}(1-\gamma)^{-1}$, finding an $\varepsilon$-optimal policy in RMDPs with an $sa$-rectangular finite transition set and a finite cost set is NP-hard. Moreover, determining the feasibility of RCMDPs with $sa$-rectangular $\mathcal{P}$ is NP-hard.

The proof constructs an RMDP with an $sa$-rectangular transition set and a finite cost set that simulates the RMDP instance in \\crefproposition:NP-hardness. Full details are provided in \\crefsec:proof-of-NP-hard.

## Sufficient Conditions When Projected Subgradient Descent Succeeds

Although PSD can fail for general RMDPs, it succeeds under additional conditions. In this section, we identify two sufficient conditions under which the subgradient dominance property (12. ‣ 3 Failure of Projected Subgradient Descent in Robust MDPs ‣ Revisiting Subgradient Dominance in Robust MDPs: Counterexamples, Hardness, and Sufficient Conditions")) holds.

Let $\mathcal{P}^{\pi}\vcentcolon\nolinebreak\mkern-1.2mu=\{P\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}(c,P)\in\mathcal{U}^{\pi}\}$ be the set of worst-case transition kernels under policy $\pi$. $\mathcal{P}^{\pi}$ is a singleton for any $\pi\in\Pi$. {assumption} Let $\mathcal{Q}^{\pi}\vcentcolon\nolinebreak\mkern-1.2mu=\{Q^{\pi}_{c,P}\mathchoice{\>}{\>}{\,}{\,}|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}(c,P)\in\mathcal{U}^{\pi}\}$ be the set of worst-case action-value functions under policy $\pi$. $\mathcal{Q}^{\pi}$ is a singleton for any $\pi\in\Pi$.

Our assumptions are motivated by the failure mode of PSD in \\crefexample:RMDP-failure. Intuitively, suboptimal local minima can arise when different worst-case models prescribe conflicting local directions toward the global optimum. Our assumptions rule out such conflict. \\Crefassm:unique-robust-value requires all active worst-case models to induce the same action-value function, so by \\crefeq:J-gradient they agree on the local improvement direction. \\Crefassm:unique-worst-case-occupancy requires agreement only at the transition level, since conflict in the cost is known not to create this pathology. The following theorem shows that either condition is sufficient for subgradient dominance.

### Theorem 4.1 (Sufficient conditions for subgradient dominance)

Under the full-support initial distribution (\\crefassumption:init-dist), the robust total cost $J_{\mathcal{U}}$ is subgradient-dominant with constant $D=((1-\gamma)\min_{s}\mu(s))^{-1}$ if either of \\crefassm:unique-worst-case-occupancy or 4 holds.

### Proof 4.2

For simplicity, we prove the result in the case where $\mathcal{U}^{\pi}$ is finite, say $\mathcal{U}^{\pi}=\left\{(c_{1},P_{1}),\dots,(c_{k},P_{k})\right\}$. The infinite case is analogous, replacing convex combinations over $[k]$ by probability measures over $\mathcal{U}^{\pi}$. It holds that, where (a) uses $J_{\mathcal{U}}(\pi^{\star})\geq J_{c,P}(\pi^{\star})$ for any $(c,P)$, (b) uses the performance difference lemma for MDPs (\\creflemma:performance-difference), and (c) holds since the minimum is attained at an extreme point of the simplex.

### When $\mathcal{P}^{\pi}$ is a singleton (\\crefassm:unique-worst-case-occupancy)

Let $P\in\mathcal{P}^{\pi}$ be the unique worst-case transition kernel under $\pi$. The right-hand side of \\crefeq:alpha-min-expression is bounded as where (a) uses $\overline{d}^{\pi^{\star}}_{P}(s)/\overline{d}^{\pi}_{P}(s)\leq 1/(1-\gamma)\mu(s)$ and (b) uses $A^{\pi}_{c,P}(s,a)=\sum_{a^{\prime}}\pi(a^{\prime}|s)Q^{\pi}_{c,P}(s,a^{\prime})-Q^{\pi}_{c,P}(s,a)$ and introduces $D\vcentcolon\nolinebreak\mkern-1.2mu=((1-\gamma)\min_{s}\mu(s))^{-1}$. The equality (c) follows from the convex hull expression of $\partial J_{\mathcal{U}}(\pi)$ (\\creflemma:policy subgradient). This proves \\creftheorem:PSD-succeeds under \\crefassm:unique-worst-case-occupancy.

### When $\mathcal{Q}^{\pi}$ is a singleton (\\crefassm:unique-robust-value)

Let $Q^{\pi}_{\mathcal{U}}\in\mathcal{Q}^{\pi}$ be the unique worst-case action-value function under $\pi$. Note that the advantage function is also unique and denoted by $A^{\pi}_{\mathcal{U}}(s,a)\vcentcolon\nolinebreak\mkern-1.2mu=\sum_{a^{\prime}}\pi(a^{\prime}|s)Q^{\pi}_{\mathcal{U}}(s,a^{\prime})-Q^{\pi}_{\mathcal{U}}(s,a)$. Then, the right-hand side of \\crefeq:alpha-min-expression is bounded as where (a), (b), and (c) follow similarly as in the previous case. This concludes the proof.

Combining \\creftheorem:PSD-succeeds with the stationarity guarantee in \\creflemma:stationary-convergence and the Moreau-envelope bound \\crefeq:subgrad-dom-Moreau, we obtain the following convergence guarantee.

### Corollary 4.3 (PSD convergence in RMDPs)

Suppose that \\crefassumption:init-dist holds and either of \\crefassm:unique-worst-case-occupancy or 4 holds. When $\eta=1/\sqrt{T}$, the PSD updates in \\crefeq:pol-grad-update satisfies that Here, $D^{\prime}$ is defined in \\crefeq:subgrad-dom-Moreau. This result ensures that PSD identifies an $\varepsilon$-optimal policy in $\mathcal{O}(\varepsilon^{-4})$ iterations under either of \\crefassm:unique-worst-case-occupancy,assm:unique-robust-value, which restores the algorithmic guarantee claimed by prior works.

In the following subsections, we discuss concrete settings in which each assumption holds. Clearly, the standard MDP setting with a singleton uncertainty set $\mathcal{U}=\{(c,P)\}$ satisfies both assumptions. Nonetheless, \\crefassm:unique-worst-case-occupancy and 4 are independent: neither implies the other as follows, and each applies to different classes of RMDPs. A formal proof is provided in \\crefsec:proof of independence.

### Proposition 4.4

There exist RMDP instances that satisfy only one of \\crefassm:unique-worst-case-occupancy and 4.

### Regularized RMDPs \\texorpdfstring(\\crefassm:unique-worst-case-occupancy,assm:unique-robust-value)(Assumptions 11 and 12)

Both \\crefassm:unique-worst-case-occupancy,assm:unique-robust-value are trivially satisfied when the worst-case model is unique for every policy $\pi$, i.e., when $\lvert\mathcal{U}^{\pi}\rvert=1$. A common approach to enforcing $\lvert\mathcal{U}^{\pi}\rvert=1$ is to introduce convex regularization that renders the adversary's objective strongly convex, thereby guaranteeing a unique worst-case model. For example, Yang et al. study the following KL-regularized problem: where $P_{0}$ is a nominal transition kernel and $\tau>0$ is a regularization parameter. When $\mathcal{P}$ is $sa$-rectangular with $\mathcal{P}_{s,a}=\Delta(\mathcal{S})$, the worst-case transition for $\pi$ is unique and satisfies While most existing results focus on rectangular uncertainty sets, the assumption $\lvert\mathcal{U}^{\pi}\rvert=1$ itself does not require rectangularity. As an example, consider the following $\ell_{2}$ regularization on $P$: where $\lVert\cdot\rVert_{F}$ denotes the Frobenius norm. Since the total cost $J_{P}(\pi)$ is weakly concave in $P$ due to its smoothness, the regularized objective becomes strongly concave for sufficiently large $\tau$. Consequently, for sufficiently large $\tau$, the worst-case transition kernel is unique even when $\mathcal{P}$ is non-rectangular. Characterizing broader classes of non-rectangular uncertainty sets that satisfy $\lvert\mathcal{U}^{\pi}\rvert=1$ is an interesting direction for future work.

### Cost-robust MDPs and Convex MDPs (\\texorpdfstring\\crefassm:unique-worst-case-occupancyAssumption 11)

assm:unique-worst-case-occupancy is also satisfied in cost-robust MDPs, where uncertainty lies solely in the cost function, that is, when $\mathcal{U}=\mathcal{C}$ for a compact cost set $\mathcal{C}$.

Cost-robust MDPs are closely related to *convex MDPs*, which study optimization problems that are convex in the occupancy measure under a fixed $P$: Convex MDPs generalize diverse decision-making problems, including skill learning, inverse reinforcement learning, imitation learning, pure exploration, and constrained MDPs. We refer readers to Zahavy et al. for a comprehensive overview.

Clearly, convex MDPs generalize cost-robust MDPs via $f(d)=\max_{c\in\mathcal{C}}\sum_{s,a}d(s,a)c(s,a)$. Conversely, cost-robust MDPs also include convex MDPs. Let $f^{*}(g)\vcentcolon\nolinebreak\mkern-1.2mu=\sup_{d\in\operatorname{dom}f}\sum_{s,a}g(s,a)d(s,a)-f(d)$ denote the convex conjugate of $f$. Then, the convex MDP problem can be rewritten as where (a) follows from the one-to-one mapping between $d^{\pi}_{M}$ and $\pi$, (b) uses definition of the convex conjugate, and (c) uses the one-to-one mapping again and substitutes a cost set $\mathcal{C}=\left\{c\in\mathbb{R}^{|\mathcal{S}||\mathcal{A}|}\mathchoice{\>}{\>}{\,}{\,}\middle|\allowbreak\mathchoice{\>}{\>}{\,}{\,}\mathopen{}c(s,a)=g(s,a)-f^{*}(g),g\in\operatorname{dom}f^{*}\right\}$. This equivalence shows that convex MDPs satisfy \\crefassm:unique-worst-case-occupancy and thus enjoys the subgradient dominance property.

We finally note that extending convex MDPs to include transition uncertainty breaks subgradient dominance, even when $\mathcal{P}$ is $sa$-rectangular. Since convex MDPs subsume constrained MDPs, the extended setting encompasses the NP-hard RCMDP instances shown in \\crefproposition:NP-hard-sa-rect.

### \\texorpdfstring$r$r-Rectangular RMDPs (\\texorpdfstring\\crefassm:unique-robust-valueAssumption 12)

It is well known that $sa$-rectangular RMDPs satisfy $\lvert\mathcal{Q}^{\pi}\rvert=1$ for every policy $\pi$, and therefore meet \\crefassm:unique-robust-value. We show that this property extends to the strictly more general class of $r$-rectangular RMDPs.

### Proposition 4.5

assm:unique-robust-value holds under $r$-rectangularity.

### Proof 4.6

For simplicity, we consider the case where the cost set $\mathcal{C}$ is a singleton, so that $\mathcal{U}=\mathcal{P}$. The extension to nontrivial cost sets is straightforward.

Recall the definition of $r$-rectangularity in \\crefeq:r-rectangular. Let $\mathcal{P}^{\pi}=\operatorname*{arg\,max}_{P\in\mathcal{P}}J_{P}(\pi)$ denote the set of worst-case transition kernels under $\pi$. For any $P\in\mathcal{P}^{\pi}$, the Bellman equation yields In the last part, the term $\beta_{i}$ is known to be unique for all $P\in\mathcal{P}^{\pi}$. Consequently, \\crefeq:r-rec-bellman implies that $Q^{\pi}_{P}$ is unique for all $P\in\mathcal{P}^{\pi}$.

## Related Work and Open Questions

This paper corrects a prevailing misconception that PSD is guaranteed to find $\varepsilon$-optimal policies in general RMDPs. We construct an explicit counterexample in which PSD converges to a suboptimal policy (\\crefsec:failure of PSD) and identify two sufficient conditions---\\crefassm:unique-worst-case-occupancy,assm:unique-robust-value---under which RMDPs satisfy the subgradient dominance property (\\crefsec:PSD-succeeds). This section situates our contributions within the existing literature on RMDPs and discusses the limitations of our results.

### Hardness of approximate optimization

While the hardness of solving RMDPs has long been recognized, it has remained unclear whether finding an $\varepsilon$-optimal policy is hard even when the robust total cost and its subgradients are efficiently computable. This ambiguity has led to incorrect convergence claims for PSD under general uncertainty sets.

The seminal work of Wiesemann et al. shows that evaluating the objective of general RMDPs is strongly NP-hard, but does not provide the hardness of policy optimization. Bagnell et al. establish NP-hardness of policy optimization only for deterministic optimal policies. Mannor et al. claim hardness of approximate optimization under general uncertainty sets; however, the proof is inaccessible, and it is unclear whether the hardness is due to evaluation or optimization. More recently, Ou and Bi prove NP-hardness of finding an optimal policy for finite uncertainty sets, but do not address approximate optimization.

In contrast, our results (\\crefproposition:NP-hardness,proposition:NP-hard-sa-rect) establish NP-hardness of $\varepsilon$-optimal policy identification in two settings that admit efficient computation of both the robust total cost and its subgradients: (i) RMDPs with a finite transition set, and (ii) RMDPs with a finite $sa$-rectangular transition set and a finite cost set. Additionally, our \\crefexample:RMDP-failure demonstrates a concrete failure case of PSD in the finite uncertainty set setting, further corroborating our hardness results.

### First-order methods for RMDPs

Several works have established performance guarantees for first-order methods in specific classes of RMDPs. Li et al. prove global convergence of state-wise mirror descent for $sa$-rectangular uncertainty sets, while Wang and Zou analyze PSD for $R$-contamination uncertainty sets, which are also $sa$-rectangular. More recently, convex MDPs have been shown to satisfy subgradient dominance due to an underlying hidden convexity structure.

All of these settings are captured by the sufficient conditions identified in \\crefsec:PSD-succeeds. In addition, we show that $r$-rectangular and regularized RMDPs satisfy our conditions, that were not previously known to admit subgradient dominance.

### Open questions

Our sufficient conditions do not cover $s$-rectangular RMDPs, despite the existence of efficient DP-based algorithms for this setting. This gap makes the $s$-rectangular case particularly intriguing: while DP can efficiently solve such RMDPs, whether PSD converges to globally optimal policies remains open.

We conjecture that $s$-rectangular RMDPs satisfy the subgradient dominance property and that dominance can hold under conditions weaker than \\crefassm:unique-worst-case-occupancy,assm:unique-robust-value. The following proposition shows that these assumptions are not necessary.

### Proposition 5.1

There exist $s$-rectangular RMDPs that satisfy the subgradient dominance property but satisfy neither \\crefassm:unique-worst-case-occupancy nor \\crefassm:unique-robust-value.

The proof is provided in \\crefsec:proof of independence. Identifying weaker conditions that encompass $s$-rectangular RMDPs while unifying the settings in \\crefsec:PSD-succeeds is an interesting direction for future work.
