<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift

Topics include Reinforcement learning, Supervised learning, Learning, Policy gradients, Markov decision process, State space, Approximation error.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy gradient methods are among the most effective methods in challenging reinforcement learning problems with large state and/or action spaces. However, little is known about even their most basic theoretical convergence properties, including: if and how fast they converge to a globally optimal solution or how they cope with approximation error due to using a restricted class of parametric policies. This work provides provable characterizations of the computational, approximation, and sample size properties of policy gradient methods in the context of discounted Markov Decision Processes (MDPs). We focus on both: "tabular" policy parameterizations, where the optimal policy is contained in the class and where we show global convergence to the optimal policy; and parametric policy classes (considering both log-linear and neural policy classes), which may not contain the optimal policy and where we provide agnostic learning results. One central contribution of this work is in providing approximation guarantees that are average case - which avoid explicit worst-case dependencies on the size of state space - by making a formal connection to supervised learning under distribution shift. This characterization shows an important interplay between estimation error, approximation error, and exploration (as characterized through a precisely defined condition number).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods have a long history in the reinforcement learning (RL) literature and are an attractive class of algorithms as they are applicable to any differentiable policy parameterization; admit easy extensions to function approximation; easily incorporate structured state and action spaces; are easy to implement in a simulation based, model-free manner. Owing to their flexibility and generality, there has also been a flurry of improvements and refinements to make these ideas work robustly with deep neural network based approaches (see e.g. Schulman et al. ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the large body of empirical work around these methods, their convergence properties are only established at a relatively coarse level; in particular, the folklore guarantee is that these methods converge to a stationary point of the objective, assuming adequate smoothness properties hold and assuming either exact or unbiased estimates of a gradient can be obtained (with appropriate regularity conditions on the variance). However, this local convergence viewpoint does not address some of the most basic theoretical convergence questions, including: 1) if and how fast they converge to a globally optimal solution (say with a sufficiently rich policy class); 2) how they cope with approximation error due to using a restricted class of parametric policies; or 3) their finite sample behavior. These questions are the focus of this work.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, the results of this work place policy gradient methods under a solid theoretical footing, analogous to the global convergence guarantees of iterative value function based algorithms.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

This work focuses on first-order and quasi second-order policy gradient methods which directly work in the space of some parameterized policy class (rather than value-based approaches). We characterize the computational, approximation, and sample size properties of these methods in the context of a discounted Markov Decision Process (MDP). We focus: 1) *tabular policy parameterizations*, where there is one parameter per state-action pair so the policy class is complete in that it contains the optimal policy, and 2) *function approximation*, where we have a restricted class or parametric policies which may not contain the globally optimal policy. Note that policy gradient methods for discrete action MDPs work in the space of stochastic policies, which permits the policy class to be differentiable. We now discuss our contributions in the both of these contexts.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Projected Gradient Ascent on Simplex (Thm 4.1) $O\left(\frac{D_{\infty}^{2}{|\mathcal{S}|}{|\mathcal{A}|}}{{({1 - \gamma})}^{6}\epsilon^{2}} \right)$ Policy Gradient, softmax parameterization (Thm 5.1) Policy Gradient + log barrier regularization, softmax parameterization (Cor 5.1) $O\left(\frac{D_{\infty}^{2}{|\mathcal{S}|}^{2}{|\mathcal{A}|}^{2}}{{({1 - \gamma})}^{6}\epsilon^{2}} \right)$ Natural Policy Gradient (NPG), softmax parameterization (Thm 5.3) $\frac{2}{{({1 - \gamma})}^{2}\epsilon}$ Table 1: Iteration Complexities with Exact Gradients for the Tabular Case: A summary of

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

the number of iterations required by different algorithms to find a policy π such that V⋆ (s0) − Vπ (s0) ≤ ϵ for some fixed s0, assuming access to exact policy gradients.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

The first three algorithms optimize the objective 𝔼s ∼ μ [Vπ (s)], where μ is the starting state distribution for the algorithms. The MDP has |𝒮| states, |𝒜| actions, and discount factor 0 ≤ γ < 1. The quantity $D_{\infty}:={\max_{s}\left(\frac{d_{s_{0}}^{\pi^{\star}}{(s)}}{\mu{(s)}} \right)}$ is termed the distribution mismatch coefficient, where, roughly speaking, ds0π⋆ (s) is the fraction of time spent in state s when executing an optimal policy π⋆, starting from the state s0 (see). The NPG algorithm directly optimizes Vπ (s0) for any state s0. In contrast to the complexities of the previous three algorithms, NPG has no dependence on the coefficient D∞, nor does it depend on the choice of s0.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Both the MDP Experts Algorithm and MD-MPI algorithm (see Corollary 3 of their paper) also yield guarantees for the same update rule as NPG for the softmax parameterization, though at a worse rate. See Section 2 for further discussion.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Tabular case", "weight": 1.0} -->

We consider three algorithms: two of which are first order methods, projected gradient ascent (on the simplex) and gradient ascent (with a softmax policy parameterization); and the third algorithm, natural policy gradient ascent, can be viewed as a quasi second-order method (or preconditioned first-order method). Table 1 summarizes our main results in this case: upper bounds on the number of iterations taken by these algorithms to find an $\epsilon$-optimal policy, when we have access to exact policy gradients.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tabular case", "weight": 1.0} -->

Arguably, the most natural starting point for an analysis of policy gradient methods is to consider directly doing gradient ascent on the policy simplex itself and then to project back onto the simplex if the constraint is violated after a gradient update; we refer to this algorithm as projected gradient ascent on the simplex. Using a notion of gradient domination, our results provably show that any first-order stationary point of the value function results in an approximately optimal policy, under certain regularity assumptions; this allows for a global convergence analysis by directly appealing to standard results in the non-convex optimization literature.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Tabular case", "weight": 1.0} -->

A more practical and commonly used parameterization is the softmax parameterization, where the simplex constraint is explicitly enforced by the exponential parameterization, thus avoiding projections. This work provides the first global convergence guarantees using only first-order gradient information for the widely-used softmax parameterization. Our first result for this parameterization establishes the asymptotic convergence of the policy gradient algorithm; the analysis challenge here is that the optimal policy (which is deterministic) is attained by sending the softmax parameters to infinity.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Tabular case", "weight": 1.0} -->

In order to establish a finite time, convergence rate to optimality for the softmax parameterization, we then consider a *log barrier* regularizer and provide an iteration complexity bound that is polynomial in all relevant quantities. The use of our log barrier regularizer is critical to avoiding the issue of gradients becomingly vanishingly small at suboptimal near-deterministic policies, an issue of significant practical relevance. The log barrier regularizer can also be viewed as using a *relative* entropy regularizer; here, we note the general approach of entropy based regularization is common in practice (e.g. see ). One notable distinction, which we discuss later, is that our analysis is for the log barrier regularization rather than the entropy regularization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tabular case", "weight": 1.0} -->

For these aforementioned algorithms, our convergence rates depend on the optimization measure having coverage over the state space, as measured by the *distribution mismatch coefficient* $D_{\infty}$ (see Table 1 caption). In particular, for the convergence rates shown in Table 1 (for the aforementioned algorithms), we assume that the optimization objective is the expected (discounted) cumulative value where the initial state is sampled under some distribution, and $D_{\infty}$ is a measure of the coverage of this initial distribution. Furthermore, we provide a lower bound that shows such a dependence is unavoidable for first-order methods, even when exact gradients are available.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Tabular case", "weight": 1.0} -->

We then consider the Natural Policy Gradient (NPG) algorithm (also see Bagnell and Schneider; Peters and Schaal ), which can be considered a quasi second-order method due to the use of its particular preconditioner, and provide an iteration complexity to achieve an $\epsilon$-optimal policy that is at most $\frac{2}{{({1 - \gamma})}^{2}\epsilon}$ iterations, improving upon the previous related results of (see Section 2). Note the convergence rate has *no* dependence on the number of states or the number of actions, nor does it depend on the distribution mismatch coefficient $D_{\infty}$. We provide a simple and concise proof for the convergence rate analysis by extending the approach developed, which uses a mirror descent style of analysis and also handles the non-concavity of the policy optimization problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Tabular case", "weight": 1.0} -->

This fast and dimension free convergence rate shows how the variable preconditioner in the natural gradient method improves over the standard gradient ascent algorithm. The dimension free aspect of this convergence rate is worth reflecting, especially given the widespread use of the natural policy gradient algorithm along with variants such as the Trust Region Policy Optimization (TRPO) algorithm; our results may help to provide analysis of a more general family of entropy based algorithms (see for example Neu et al. ).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Tabular case", "weight": 1.0} -->

6.2) $\sqrt{\frac{{\kappa\epsilon_{stat}} + {D_{\infty}\epsilon_{approx}}}{{({1 - \gamma})}^{3}}} + \frac{1}{{({1 - \gamma})}\sqrt{T}}$ Table 2: Overview of Approximate Methods: The suboptimality, V⋆ (s0) − Vπ (s0), after T iterations for various approximate algorithms, which use different notions of approximation error (sample complexities are not directly considered but instead may be thought of as part of ϵ1 and ϵstat. See Section 2 for further discussion). Order notation is used to drop constants, and we assume |𝒜| = 2 for ease of exposition. For approximate dynamic programming methods, the relevant error is the worst case, ℓ∞-error in approximating a value function, e.g. ϵ∞ = maxs, a|Qπ (s, a) − Q̂π (s, a)|, where Q̂π is what an estimation oracle returns during the course of the algorithm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Tabular case", "weight": 1.0} -->

The second row (see Lemma 12 in Antos et al.) is a refinement of this approach, where ϵ1 is an ℓ1-average error in fitting the value functions under the fitting (state) distribution μ, and, roughly, C∞ is a worst case density ratio between the state visitation distribution of any non-stationary policy and the fitting distribution μ. For Conservative Policy Iteration, ϵ1 is a related ℓ1-average case fitting error with respect to a fitting distribution μ, and D∞ is as defined as before, in the caption of Table 1 (see also); here, D∞ ≤ C∞ (e.g. see Scherrer). For NPG, ϵstat and ϵapprox measure the excess risk (the regret) and approximation errors in fitting the values. Roughly speaking, ϵstat is the excess squared loss relative to the best fit (among an appropriately defined parametric class) under our fitting distribution (defined with respect to the state distribution μ). Here, ϵapprox is the approximation error: the minimal possible error (in our parametric class) under our fitting distribution.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Tabular case", "weight": 1.0} -->

The condition number κ is a relative eigenvalue condition between appropriately defined feature covariances with respect to the state visitation distribution of an optimal policy, ds0π⋆, and the state fitting distribution μ. See text for further discussion, and Section 6 for precise statements as well as a more general result not explicitly dependent on D∞.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

We now summarize our results with regards to policy gradient methods in the setting where we work with a restricted policy class, which may not contain the optimal policy. In this sense, these methods can be viewed as approximate methods. Table 2 provides a summary along with the comparisons to some relevant approximate dynamic programming methods.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

A long line of work in the function approximation setting focuses on mitigating the worst-case "$\ell_{\infty}$" guarantees that are inherent to approximate dynamic programming methods (see the first row in Table 2). The reason to focus on average case guarantees is that it supports the applicability of *supervised machine learning* methods to solve the underlying approximation problem. This is because supervised learning methods, like classification and regression, typically have bounds on the expected error under a distribution, as opposed to worst-case guarantees over all possible inputs.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

The existing literature largely consists of two lines of provable guarantees that attempt to mitigate the explicit $\ell_{\infty}$ error conditions of approximate dynamic programming: those methods which utilize a problem dependent parameter (the concentrability coefficient ) to provide more refined dynamic programming guarantees (e.g. see Munos; Szepesvári and Munos; Antos et al.; Farahmand et al. ) and those which work with a restricted policy class, making incremental updates, such as Conservative Policy Iteration (CPI), Policy Search by Dynamic Programming (PSDP), and MD-MPI Geist et al.. Both styles of approaches give guarantees based on worst-case density ratios, i.e. they depend on a maximum ratio between two different densities over the state space. As discussed, the assumptions in the latter class of algorithms are substantially weaker, in that the worst-case density ratio only depends on the state visitation distribution of an optimal policy (also see Table 2 caption and Section 2).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

With regards to function approximation, our main contribution is in providing performance bounds that, in some cases, have milder dependence on these density ratios. We precisely quantify an *approximation/estimation* error decomposition relevant for the analysis of the natural gradient method; this decomposition is stated in terms of the *compatible function approximation error* as introduced in Sutton et al.. More generally, we quantify our function approximation results in terms of a precisely quantified transfer error notion, based on approximation error under *distribution shift*. Table 2 shows a special case of our convergence rates of NPG, which is governed by four quantities: $\epsilon_{stat}$, $\epsilon_{approx}$, $\kappa$, and $D_{\infty}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

Let us discuss the important special case of log-linear policies (i.e. policies that take the softmax of linear functions in a given feature space) where the relevant quantities are as follows: $\epsilon_{stat}$ is a bound on the excess risk (the estimation error) in fitting linearly parameterized value functions, which can be driven to $0$ with more samples (at the usual statistical rate of $O{({1/\sqrt{N}})}$ where $N$ is the number of samples); $\epsilon_{approx}$ is the usual notion of average squared approximation error where the target function may not be perfectly representable by a linear function; $\kappa$ can be upper bounded with an inverse dependence on the minimal eigenvalue of the feature covariance matrix of the fitting measure (as such it can be viewed as a dimension dependent quantity but not necessarily state dependent); and $D_{\infty}$ is as before.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

For the realizable case, where all policies have values which are linear in the given features (such as in linear MDP models of ), we have that the approximation error $\epsilon_{approx}$ is $0$. Here, our guarantees yield a fully polynomial and sample efficient convergence guarantee, provided the condition number $\kappa$ is bounded. Importantly, there always exists a good (universal) initial measure that ensures $\kappa$ is bounded by a quantity that is only polynomial in the dimension of the features, $d$, as opposed to an explicit dependence on the size of the (infinite) state space (see Remark 6.3). Such a guarantee would not be implied by algorithms which depend on the coefficients $C_{\infty}$ or $D_{\infty}$.^11^1Bounding $C_{\infty}$ would require a restriction on the dynamics of the MDP (see Chen and Jiang and Section 2).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

Bounding $D_{\infty}$ would require an initial state distribution that is constructed using knowledge of $\pi^{\star}$, through $d^{\pi^{\star}}$. In contrast, $\kappa$ can be made $O{(d)}$, with an initial state distribution that only depends on the geometry of the features (and does not depend on any other properties of the MDP). See Remark 6.3.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Function Approximation", "weight": 1.0} -->

Our results are also suggestive that a broader class of incremental algorithms --- such as CPI, PSDP, and MD-MPI Geist et al. which make small changes to the policy from one iteration to the next --- may also permit a sharper analysis, where the dependence of worst-case density ratios can be avoided through an appropriate approximation/estimation decomposition; this is an interesting direction for future work (a point which we return to in Section 7). One significant advantage of NPG is that the explicit parametric policy representation in NPG (and other policy gradient methods) leads to a succinct policy representation in comparison to CPI, PSDP, or related boosting-style methods, where the representation complexity of the policy of the latter class of methods grows linearly in the number of iterations (since these methods add one policy to the ensemble per iteration). This representation complexity is likely why the latter class of algorithms are less widely used in practice.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Setting", "weight": 1.0} -->

A (finite) Markov Decision Process (MDP) $M = {(\mathcal{S},\mathcal{A},P,r,\gamma,\rho)}$ is specified: a finite state space $\mathcal{S}$; a finite action space $\mathcal{A}$; a transition model $P$ where $P{(\left. s' \middle| {s,a} \right.)}$ is the probability of transitioning into state $s'$ upon taking action $a$ in state $s$; a reward function $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack 0,1\rbrack}}$ where $r{(s,a)}$ is the immediate reward associated with taking action $a$ in state $s$; a discount factor $\gamma \in {\lbrack 0,1)}$; a starting state distribution $\rho$ over $\mathcal{S}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Setting", "weight": 1.0} -->

A deterministic, stationary policy $\pi:{\mathcal{S}\rightarrow\mathcal{A}}$ specifies a decision-making strategy in which the agent chooses actions adaptively based on the current state, i.e., $a_{t} = {\pi{(s_{t})}}$. The agent may also choose actions according to a stochastic policy $\pi:{\mathcal{S}\rightarrow{\Delta{(\mathcal{A})}}}$ (where $\Delta{(\mathcal{A})}$ is the probability simplex over $\mathcal{A}$), and, overloading notation, we write $a_{t} \sim \pi{( \cdot |s_{t})}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Setting", "weight": 1.0} -->

A policy induces a distribution over trajectories $\tau = {(s_{t},a_{t},r_{t})}_{t = 0}^{\infty}$, where $s_{0}$ is drawn from the starting state distribution $\rho$, and, for all subsequent timesteps $t$, $a_{t} \sim \pi{(\cdot |s_{t})}$ and $s_{t + 1} \sim P{(\cdot |s_{t},a_{t})}$. The value function $V^{\pi}:{\mathcal{S}\rightarrow{\mathbb{R}}}$ is defined as the discounted sum of future rewards starting at state $s$ and executing $\pi$, i.e. where the expectation is with respect to the randomness of the trajectory $\tau$ induced by $\pi$ in $M$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Setting", "weight": 1.0} -->

Since we assume that ${r{(s,a)}} \in {\lbrack 0,1\rbrack}$, we have $0 \leq {V^{\pi}{(s)}} \leq \frac{1}{1 - \gamma}$. We overload notation and define $V^{\pi}{(\rho)}$ as the expected value under the initial state distribution $\rho$, i.e.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Setting", "weight": 1.0} -->

The action-value (or Q-value) function $Q^{\pi}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ and the *advantage* function $A^{\pi}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ are defined as: The goal of the agent is to find a policy $\pi$ that maximizes the expected value from the initial state, i.e. the optimization problem the agent seeks to solve is: where the $\max$ is over all policies. The famous theorem of Bellman and Dreyfus shows there exists a policy $\pi^{\star}$ which simultaneously maximizes $V^{\pi}{(s_{0})}$, for all states $s_{0} \in \mathcal{S}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy Parameterizations", "weight": 1.0} -->

This work studies ascent methods for the optimization problem: where $\left. \{\pi_{\theta} \middle| {\theta \in \Theta}\} \right.$ is some class of parametric (stochastic) policies. We consider a number of different policy classes. The first two are *complete* in the sense that any stochastic policy can be represented in the class. The final class may be restrictive. These classes are as follows: *Direct parameterization:* The policies are parameterized by where $\theta \in {\Delta{(\mathcal{A})}^{|\mathcal{S}|}}$, i.e. $\theta$ is subject to $\theta_{s,a} \geq 0$ and ${\sum_{a \in \mathcal{A}}\theta_{s,a}} = 1$ for all $s \in \mathcal{S}$ and $a \in \mathcal{A}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Parameterizations", "weight": 1.0} -->

*Softmax parameterization:* For unconstrained $\theta \in {\mathbb{R}}^{{|\mathcal{S}|}{|\mathcal{A}|}}$, The softmax parameterization is also complete.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy Parameterizations", "weight": 1.0} -->

*Restricted parameterizations:* We also study parametric classes $\left. \{\pi_{\theta} \middle| {\theta \in \Theta}\} \right.$ that may not contain all stochastic policies. In particular, we pay close attention to both log-linear policy classes and neural policy classes (see Section 6). Here, the best we may hope for is an agnostic result where we do as well as the best policy in this class.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy Parameterizations", "weight": 1.0} -->

While the softmax parameterization is the more natural parametrization among the two complete policy classes, it is also informative to consider the direct parameterization.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy Parameterizations", "weight": 1.0} -->

It is worth explicitly noting that $V^{\pi_{\theta}}{(s)}$ is non-concave in $\theta$ for both the direct and the softmax parameterizations, so the standard tools of convex optimization are not applicable.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Policy gradients", "weight": 1.0} -->

In order to introduce these methods, it is useful to define the discounted state visitation distribution $d_{s_{0}}^{\pi}$ of a policy $\pi$ as: where $\Pr^{\pi}{({s_{t} = \left. s \middle| s_{0} \right.})}$ is the state visitation probability that $s_{t} = s$, after we execute $\pi$ starting at state $s_{0}$. Again, we overload notation and write: where $d_{\rho}^{\pi}$ is the discounted state visitation distribution under initial distribution $\rho$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Policy gradients", "weight": 1.0} -->

The policy gradient functional form (see e.g. Williams; Sutton et al.) is then: Furthermore, if we are working with a differentiable parameterization of $\pi_{\theta}{(\cdot |s)}$ that explicitly constrains $\pi_{\theta}{(\cdot |s)}$ to be in the simplex, i.e. $\pi_{\theta} \in {\Delta{(\mathcal{A})}^{|\mathcal{S}|}}$ for all $\theta$, then we also have: Note the above gradient expression (Equation 6) does not hold for the direct parameterization, while Equation 5 is valid. ^22^2This is due to ${\sum_{a}{{\nabla_{\theta}\pi_{\theta}}{(\left. a \middle| s \right.)}}} = 0$ not explicitly being maintained by the direct parameterization.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The distribution mismatch coefficient", "weight": 1.0} -->

We often characterize the difficulty of the exploration problem faced by our policy optimization algorithms when maximizing the objective $V^{\pi}{(\mu)}$ through the following notion of *distribution mismatch coefficient*.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Warmup: Constrained Tabular Parameterization", "weight": 1.0} -->

Our starting point is, arguably, the simplest first-order method: we directly take gradient ascent updates on the policy simplex itself and then project back onto the simplex if the constraints are violated after a gradient update. This algorithm is projected gradient ascent on the direct policy parametrization of the MDP, where the parameters are the state-action probabilities, i.e. $\theta_{s,a} = {\pi_{\theta}{(\left. a \middle| s \right.)}}$ (see ). As noted in Lemma 3.1, $V^{\pi_{\theta}}{(s)}$ is non-concave in the parameters $\pi_{\theta}$. Here, we first prove that $V^{\pi_{\theta}}{(\mu)}$ satisfies a Polyak-like gradient domination condition, and this tool helps in providing convergence rates. The basic approach was also used in the analysis of CPI; related gradient domination-like lemmas also appeared in Scherrer and Geist.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Warmup: Constrained Tabular Parameterization", "weight": 1.0} -->

It is instructive to consider this special case due to the connections it makes to the non-convex optimization literature. We also provide a lower bound that rules out algorithms whose runtime appeals to the curvature of saddle points (e.g. ).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Gradient Domination", "weight": 1.0} -->

Informally, we say a function $f{(\theta)}$ satisfies a gradient domination property if for all $\theta \in \Theta$, where $\theta^{\star} \in {{{argmax}_{\theta' \in \Theta}f}{(\theta')}}$ and where $G{(\theta)}$ is some suitable scalar notion of first-order stationarity, which can be considered a measure of how large the gradient is (see). Thus if one can find a $\theta$ that is (approximately) a first-order stationary point, then the parameter $\theta$ will be near optimal (in terms of function value). Such conditions are a standard device to establishing global convergence in non-convex optimization, as they effectively rule out the presence of bad critical points. In other words, given such a condition, quantifying the convergence rate for a specific algorithm, like say projected gradient ascent, will require quantifying the rate of its convergence to a first-order stationary point, for which one can invoke standard results from the optimization literature.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Gradient Domination", "weight": 1.0} -->

The following lemma shows that the direct policy parameterization satisfies a notion of gradient domination. This is the basic approach used in the analysis of CPI; a variant of this lemma also appears in Scherrer and Geist. We give a proof for completeness.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Gradient Domination", "weight": 1.0} -->

Even though we are interested in the value $V^{\pi}{(\rho)}$, it is helpful to consider the gradient with respect to another state distribution $\mu \in {\Delta{(\mathcal{S})}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Convergence Rates for Projected Gradient Ascent", "weight": 1.0} -->

Using this notion of gradient domination, we now give an iteration complexity bound for projected gradient ascent over the space of stochastic policies, i.e. over $\Delta{(\mathcal{A})}^{|\mathcal{S}|}$. The projected gradient ascent algorithm updates where $P_{\Delta{(\mathcal{A})}^{|\mathcal{S}|}}$ is the projection onto $\Delta{(\mathcal{A})}^{|\mathcal{S}|}$ in the Euclidean norm.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Lower Bound: Vanishing Gradients and Saddle Points", "weight": 1.0} -->

To understand the necessity of the distribution mismatch coefficient in Lemma 4.1. ‣ 4.1 Gradient Domination ‣ 4 Warmup: Constrained Tabular Parameterization ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift") and Theorem 4.1, let us first give an informal argument that some condition on the state distribution of $\pi$, or equivalently $\mu$, is necessary for stationarity to imply optimality. For example, in a sparse-reward MDP (where the agent is only rewarded upon visiting some small set of states), a policy that does not visit *any* rewarding states will have zero gradient, even though it is arbitrarily suboptimal in terms of values. Below, we give a more quantitative version of this intuition, which demonstrates that even if $\pi$ chooses all actions with reasonable probabilities (and hence the agent will visit all states if the MDP is connected), then there is an MDP where a large fraction of the policies $\pi$ have vanishingly small gradients, and yet these policies are highly suboptimal in terms of their value.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Lower Bound: Vanishing Gradients and Saddle Points", "weight": 1.0} -->

Concretely, consider the chain MDP of length $H + 2$ shown in Figure 2. The starting state of interest is state $s_{0}$ and the discount factor $\gamma = {H/{({H + 1})}}$. Suppose we work with the direct parameterization, where ${\pi_{\theta}{(\left. a \middle| s \right.)}} = \theta_{s,a}$ for $a = {a_{1},a_{2},a_{3}}$ and ${\pi_{\theta}{(\left. a_{4} \middle| s \right.)}} = {1 - \theta_{s,a_{1}} - \theta_{s,a_{2}} - \theta_{s,a_{3}}}$. Note we do not over-parameterize the policy.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Lower Bound: Vanishing Gradients and Saddle Points", "weight": 1.0} -->

For this MDP and policy structure, if we were to initialize the probabilities over actions, say deterministically, then there is an MDP (obtained by permuting the actions) where all the probabilities for $a_{1}$ will be less than $1/4$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Lower Bound: Vanishing Gradients and Saddle Points", "weight": 1.0} -->

The following result not only shows that the gradient is exponentially small in $H$, it also shows that many higher order derivatives, up to $O{({H/{\log H}})}$, are also exponentially small in $H$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

(Exact vs. Approximate Gradients) The chain MDP of Figure 2, is a common example where *sample* based estimates of gradients will be $0$ under random exploration strategies; there is an exponentially small in $H$ chance of hitting the goal state under a random exploration strategy. Note that this lemma is with regards to *exact* gradients. This suggests that even with exact computations (along with using exact higher order derivatives) we might expect numerical instabilities.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

(Comparison with the upper bound) The lower bound does not contradict the upper bound of Theorem 4.1. ‣ 4.1 Gradient Domination ‣ 4 Warmup: Constrained Tabular Parameterization ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift") (where a small gradient is turned into a small policy suboptimality bound), as the distribution mismatch coefficient, as defined in Definition 3.1. ‣ The distribution mismatch coefficient. ‣ 3 Setting ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift"), could be infinite in the chain MDP of Figure 2, since the start-state distribution is concentrated on one state only.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4.3", "weight": 1.0} -->

(Comparison with information-theoretic lower bounds) The lower bound here is *not information theoretic*, in that it does not present a hard problem instance for all algorithms. Indeed, exploration algorithms for tabular MDPs starting from $E^{3}$, RMAX and several subsequent works yield polynomial sample complexities for the chain MDP. Proposition 4.1. ‣ 4.3 A Lower Bound: Vanishing Gradients and Saddle Points ‣ 4 Warmup: Constrained Tabular Parameterization ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift") should be interpreted as a hardness result for the specific class of policy gradient like approaches that search for a policy with a small policy gradient, as these methods will find the initial parameters to be valid in terms of the size of (several orders of) gradients. In particular, it precludes any meaningful claims on global optimality, based just on the size of the policy gradients, without additional assumptions as discussed in the previous remark.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 4.3", "weight": 1.0} -->

The proof is provided in Appendix B.2. The lemma illustrates that lack of good exploration can indeed be detrimental in policy gradient algorithms, since the gradient can be small either due to $\pi$ being near-optimal, or, simply because $\pi$ does not visit advantageous states often enough. In this sense, it also demonstrates the necessity of the distribution mismatch coefficient in Lemma 4.1. ‣ 4.1 Gradient Domination ‣ 4 Warmup: Constrained Tabular Parameterization ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift").

<!-- chunk {"id": "body-0056", "role": "body", "section": "The Softmax Tabular Parameterization", "weight": 1.0} -->

We now consider the softmax policy parameterization. Here, we still have a non-concave optimization problem in general, as shown in Lemma 3.1, though we do show that global optimality can be reached under certain regularity conditions. From a practical perspective, the softmax parameterization of policies is preferable to the direct parameterization, since the parameters $\theta$ are unconstrained and standard unconstrained optimization algorithms can be employed. However, optimization over this policy class creates other challenges as we study in this section, as the optimal policy (which is deterministic) is attained by sending the parameters to infinity.

<!-- chunk {"id": "body-0057", "role": "body", "section": "The Softmax Tabular Parameterization", "weight": 1.0} -->

We study three algorithms for this problem. The first performs direct policy gradient ascent on the objective without modification, while the second adds a log barrier regularizer to keep the parameters from becoming too large, as a means to ensure adequate exploration. Finally, we study the natural policy gradient algorithm and establish a global optimality result with no dependence on the distribution mismatch coefficient or dimension-dependent factors.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Softmax Tabular Parameterization", "weight": 1.0} -->

For the softmax parameterization, the gradient takes the form: (see Lemma C.1 for a proof).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Asymptotic Convergence, without Regularization", "weight": 1.0} -->

Due to the exponential scaling with the parameters $\theta$ in the softmax parameterization, *any* policy that is nearly deterministic will have gradients close to $0$. In spite of this difficulty, we provide a positive result that gradient ascent asymptotically converges to the global optimum for the softmax parameterization.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 5.1", "weight": 1.0} -->

(Strict positivity of $\mu$ and exploration) Theorem 5.1. ‣ 5.1 Asymptotic Convergence, without Regularization ‣ 5 The Softmax Tabular Parameterization ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift") assumed that optimization distribution $\mu$ was *strictly* positive, i.e. ${\mu{(s)}} > 0$ for all states $s$. We leave it is an open question of whether or not gradient ascent will globally converge if this condition is not met. The concern is that if this condition is not met, then gradient ascent may not globally converge due to that $d_{\mu}^{\pi_{\theta}}{(s)}$ effectively scales down the learning rate for the parameters associated with state $s$ (see ).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 5.1", "weight": 1.0} -->

The complete proof is provided in the Appendix C.1. We now discuss the subtleties in the proof and show why the softmax parameterization precludes a direct application of the gradient domination lemma. In order to utilize the gradient domination property (in Lemma 4.1. ‣ 4.1 Gradient Domination ‣ 4 Warmup: Constrained Tabular Parameterization ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift")), we would desire to show that: ${{\nabla_{\pi}V^{\pi}}{(\mu)}}\rightarrow 0$. However, using the functional form of the softmax parameterization (see Lemma C.1) and, we have that: Hence, we see that even if ${{\nabla_{\theta}V^{\pi_{\theta}}}{(\mu)}}\rightarrow 0$, we are not guaranteed that ${{\nabla_{\pi}V^{\pi_{\theta}}}{(\mu)}}\rightarrow 0$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 5.1", "weight": 1.0} -->

We now briefly discuss the main technical challenges in the proof. The proof first shows that the sequence $V^{(t)}{(s)}$ is monotone increasing pointwise, i.e. for *every* state $s$, ${V^{({t + 1})}{(s)}} \geq {V^{(t)}{(s)}}$ (Lemma C.2⁢(𝑠)). ‣ C.1 Proofs for Section 5.1 ‣ Appendix C Proofs for Section 5 ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift")). This implies the existence of a limit $V^{(\infty)}{(s)}$ by the monotone convergence theorem (Lemma C.3).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 5.1", "weight": 1.0} -->

Based on the limiting quantities $V^{(\infty)}{(s)}$ and $Q^{(\infty)}{(s,a)}$, which we show exist, define the following limiting sets for each state $s$: The challenge is to then show that, for all states $s$, the set $I_{+}^{s}$ is the empty set, which would immediately imply ${V^{(\infty)}{(s)}} = {V^{\star}{(s)}}$. The proof proceeds by contradiction, assuming that $I_{+}^{s}$ is non-empty.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 5.1", "weight": 1.0} -->

Using that $I_{+}^{s}$ is non-empty and that the gradient tends to zero in the limit, i.e. ${{\nabla_{\theta}V^{\pi_{\theta}}}{(\mu)}}\rightarrow 0$, we have that for all $a \in I_{+}^{s}$, ${\pi^{(t)}{(\left. a \middle| s \right.)}}\rightarrow 0$ (see). This, along with the functional form of the softmax parameterization, implies that there must be divergence (in magnitude) among the set of parameters associated with *some* action $a$ at state $s$, i.e. that ${\max_{a \in \mathcal{A}}{|\theta_{s,a}^{(t)}|}}\rightarrow\infty$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 5.1", "weight": 1.0} -->

The primary technical challenge in the proof is to then use this divergence, along with the dynamics of gradient ascent, to show that $I_{+}^{s}$ is empty via a contradiction.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 5.1", "weight": 1.0} -->

We leave it as a question for future work as to characterizing the convergence rate, which we conjecture is exponentially slow in some of the relevant quantities, such as in terms of the size of state space. Here, we turn to a regularization based approach to ensure convergence at a polynomial rate in all relevant quantities.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Polynomial Convergence with Log Barrier Regularization", "weight": 1.0} -->

Due to the exponential scaling with the parameters $\theta$, policies can rapidly become near deterministic, when optimizing under the softmax parameterization, which can result in slow convergence. Indeed a key challenge in the asymptotic analysis in the previous section was to handle the growth of the absolute values of parameters as they tend to infinity. A common practical remedy for this is to use entropy-based regularization to keep the probabilities from getting too small, and we study gradient ascent on a similarly regularized objective in this section. Recall that the relative-entropy for distributions $p$ and $q$ is defined as: ${\text{KL}{(p,q)}}:={{\mathbb{E}}_{x \sim p}{\lbrack{- {{{{\log q}{(x)}}/p}{(x)}}}\rbrack}}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Polynomial Convergence with Log Barrier Regularization", "weight": 1.0} -->

a \middle| s \right.)}}}} + {\lambda{\log{|\mathcal{A}|}}}},$ | | | where $\lambda$ is a regularization parameter. The constant (i.e. the last term) is not relevant with regards to optimization. This regularizer is different from the more commonly utilized entropy regularizer as in Mnih et al., a point which we return to in Remark 5.2.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Polynomial Convergence with Log Barrier Regularization", "weight": 1.0} -->

The policy gradient ascent updates for $L_{\lambda}{(\theta)}$ are given: Our next theorem shows that approximate first-order stationary points of the entropy-regularized objective are approximately globally optimal, provided the regularization is sufficiently small.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

(Entropy vs. log barrier regularization) The more commonly considered regularizer is the entropy (also see Ahmed et al. for a more detailed empirical investigation), where the regularizer would be: Note the entropy is far less aggressive in penalizing small probabilities, in comparison to the log barrier, which is equivalent to the relative entropy. In particular, the entropy regularizer is always bounded between $0$ and $\log{|\mathcal{A}|}$, while the relative entropy (against the uniform distribution over actions), is bounded between $0$ and infinity, where it tends to infinity as probabilities tend to $0$. We leave it is an open question if a polynomial convergence rate ^55^5Here, ideally we would like to be poly in $|\mathcal{S}|$, $|\mathcal{A}|$, $1/{({1 - \gamma})}$, $1/\epsilon$, and the distribution mismatch coefficient, which we conjecture may not be possible.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

is achievable with the more common entropy regularizer; our polynomial convergence rate using the KL regularizer crucially relies on the aggressive nature in which the relative entropy prevents small probabilities (the proof shows that any action, with a positive advantage, has a significant probability for any near-stationary policy of the regularized objective).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Dimension-free Convergence of Natural Policy Gradient Ascent", "weight": 1.0} -->

We now show the Natural Policy Gradient algorithm, with the softmax parameterization, obtains an improved iteration complexity. The NPG algorithm defines a Fisher information matrix (induced by $\pi$), and performs gradient updates in the geometry induced by this matrix as follows: where $M^{\dagger}$ denotes the Moore-Penrose pseudoinverse of the matrix $M$. Throughout this section, we restrict to using the initial state distribution $\rho \in {\Delta{(\mathcal{S})}}$ in our update rule in (5.3) (so our optimization measure $\mu$ and the performance measure $\rho$ are identical).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Dimension-free Convergence of Natural Policy Gradient Ascent", "weight": 1.0} -->

Also, we restrict attention to states $s \in \mathcal{S}$ reachable from $\rho$, since, without loss of generality, we can exclude states that are not reachable under this start state distribution^66^6Specifically, we restrict the MDP to the set of states $\{{s \in \mathcal{S}}:{{{\exists\pi}\quad\text{such that}\quad{d_{\rho}^{\pi}{(s)}}} > 0}\}$..

<!-- chunk {"id": "body-0074", "role": "body", "section": "Dimension-free Convergence of Natural Policy Gradient Ascent", "weight": 1.0} -->

We leverage a particularly convenient form the update takes for the softmax parameterization (see Kakade ). For completeness, we provide a proof in Appendix C.3.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Function Approximation and Distribution Shift", "weight": 1.0} -->

We now analyze the case of using parametric policy classes: where $\Pi$ may not contain all stochastic policies (and it may not even contain an optimal policy). In contrast with the tabular results in the previous sections, the policy classes that we are often interested in are not fully expressive, e.g. $d \ll {{|\mathcal{S}|}{|\mathcal{A}|}}$ (indeed $|\mathcal{S}|$ or $|\mathcal{A}|$ need not even be finite for the results in this section); in this sense, we are in the regime of function approximation.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Function Approximation and Distribution Shift", "weight": 1.0} -->

We focus on obtaining *agnostic* results, where we seek to do as well as the best policy in this class (or as well as some other comparator policy). While we are interested in a solution to the (unconstrained) policy optimization problem (for a given initial distribution $\rho$), we will see that optimization with respect to a different distribution will be helpful, just as in the tabular case, We will consider variants of the NPG update rule (5.3): Our analysis will leverage a close connection between the NPG update rule (5.3) with the notion of *compatible function approximation*, as formalized in Kakade. Specifically, it can be easily seen that: where $w^{\star}$ is a minimizer of the following regression problem: The above is a straightforward consequence of the first order optimality conditions (see).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Function Approximation and Distribution Shift", "weight": 1.0} -->

The above regression problem can be viewed as "compatible" function approximation: we are approximating $A^{\pi_{\theta}}{(s,a)}$ using the $\nabla_{\theta}\log\pi_{\theta}{(\cdot |s)}$ as features. We also consider a variant of the above update rule, $Q$-NPG, where instead of using advantages in the above regression we use the $Q$-values.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Function Approximation and Distribution Shift", "weight": 1.0} -->

This viewpoint provides a methodology for approximate updates, where we can solve the relevant regression problems with samples. Our main results establish the effectiveness of NPG updates where there is error both due to statistical estimation (where we may not use exact gradients) and approximation (due to using a parameterized function class); in particular, we provide a novel estimation/approximation decomposition relevant for the NPG algorithm. For these algorithms, we will first consider log linear policies classes (as a special case) and then move on to more general policy classes (such as neural policy classes). Finally, it is worth remarking that the results herein provide one of the first provable approximation guarantees where the error conditions required do not have explicit worst case dependencies over the state space.

<!-- chunk {"id": "body-0079", "role": "body", "section": "NPG and $Q$-NPG Examples", "weight": 1.0} -->

In practice, the most common policy classes are of the form: where $f_{\theta}$ is a differentiable function. For example, the tabular softmax policy class is one where ${f_{\theta}{(s,a)}} = \theta_{s,a}$. Typically, $f_{\theta}$ is either a linear function or a neural network. Let us consider the NPG algorithm, and a variant $Q$-NPG, in each of these two cases.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Log-linear Policy Classes and Soft Policy Iteration", "weight": 1.0} -->

For any state-action pair $(s,a)$, suppose we have a feature mapping $\phi_{s,a} \in {\mathbb{R}}^{d}$. Each policy in the log-linear policy class is of the form: with $\theta \in {\mathbb{R}}^{d}$. Here, we can take ${f_{\theta}{(s,a)}} = {\theta \cdot \phi_{s,a}}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Log-linear Policy Classes and Soft Policy Iteration", "weight": 1.0} -->

With regards to compatible function approximation for the log-linear policy class, we have: that is, ${\overline{\phi}}_{s,a}^{\theta}$ is the centered version of $\phi_{s,a}$. With some abuse of notation, we accordingly also define ${\overline{\phi}}^{\pi}$ for any policy $\pi$. Here, using, the NPG update rule is equivalent to: (We have rescaled the learning rate $\eta$ in comparison to). Note that we recompute $w_{\star}$ for every update of $\theta$. Here, the compatible function approximation error measures the expressivity of our parameterization in how well linear functions of the parameterization can capture the policy's advantage function.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Log-linear Policy Classes and Soft Policy Iteration", "weight": 1.0} -->

We also consider a variant of the NPG update rule, termed *$Q$-NPG*, where: Note we do not center the features for $Q$-NPG; observe that $Q^{\pi}{(s,a)}$ is also not 0 in expectation under $\pi{(\cdot |s)}$, unlike the advantage function.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 6.1", "weight": 1.0} -->

(NPG/$Q$-NPG and Soft-Policy Iteration) We now see how we can view both NPG and $Q$-NPG as an incremental (soft) version of policy iteration, just as in Lemma 5.1 for the tabular case. Rather than writing the update rule in terms of the parameter $\theta$, we can write an equivalent update rule directly in terms of the (log-linear) policy $\pi$:\where $Z_{s}$ is normalization constant. While the policy update uses the original features $\phi$ instead of ${\overline{\phi}}^{\pi}$, whereas the quadratic error minimization is terms of the centered features ${\overline{\phi}}^{\pi}$, this distinction is not relevant due to that we may also instead use ${\overline{\phi}}^{\pi}$ (in the policy update) which would result in an equivalent update; the normalization makes the update invariant to (constant) translations of the features.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Remark 6.2", "weight": 1.0} -->

(On the equivalence of NPG and $Q$-NPG) If it is the case that the compatible function approximation error is $0$, then it straightforward to verify that the NPG and $Q$-NPG are equivalent algorithms, in that their corresponding policy updates will be equivalent to each other.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Neural Policy Classes", "weight": 1.0} -->

Now suppose $f_{\theta}{(s,a)}$ is a neural network parameterized by $\theta \in {\mathbb{R}}^{d}$, where the policy class $\Pi$ is of form. Observe: and, using, the NPG update rule is equivalent to: (Again, we have rescaled the learning rate $\eta$ in comparison to).

<!-- chunk {"id": "body-0086", "role": "body", "section": "$Q$-NPG: Performance Bounds for Log-Linear Policies", "weight": 1.0} -->

For a state-action distribution $\upsilon$, define: The iterates of the $Q$-NPG algorithm can be viewed as minimizing this loss under some (changing) distribution $\upsilon$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "$Q$-NPG: Performance Bounds for Log-Linear Policies", "weight": 1.0} -->

We now specify an approximate version of $Q$-NPG. It is helpful to consider a slightly more general version of the algorithm in the previous section, where instead of optimizing under a starting state distribution $\rho$, we have a different starting *state-action* distribution $\nu$. Analogous to the definition of the state visitation measure, $d_{\mu}^{\pi}$, we can define a visitation measure over states *and* actions induced by following $\pi$ after ${s_{0},a_{0}} \sim \nu$. We overload notation using $d_{\nu}^{\pi}$ to also refer to the state-action visitation measure; precisely, where $\Pr^{\pi}{({s_{t} = s},{a_{t} = \left.

<!-- chunk {"id": "body-0088", "role": "body", "section": "$Q$-NPG: Performance Bounds for Log-Linear Policies", "weight": 1.0} -->

a \middle| {s_{0},a_{0}} \right.})}$ is the probability that $s_{t} = s$ and $a_{t} = a$, after starting at state $s_{0}$, taking action $a_{0}$, and following $\pi$ thereafter. While we overload notation for visitation distributions ($d_{\mu}^{\pi}{(s)}$ and $d_{\nu}^{\pi}{(s,a)}$) for notational convenience, note that the state-action measure $d_{\nu}^{\pi}$ uses the subscript $\nu$, which is a state-action measure. $Q$-NPG will be defined with respect to the *on-policy* state action measure starting with ${s_{0},a_{0}} \sim \nu$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "$Q$-NPG: Performance Bounds for Log-Linear Policies", "weight": 1.0} -->

As per our convention, we define The approximate version of this algorithm is: where the above update rule also permits us to constrain the norm of the update direction $w^{(t)}$ (alternatively, we could use $\ell_{2}$ regularization as is also common in practice). The exact minimizer is denoted as: Note that $w_{\star}^{(t)}$ depends on the current parameter $\theta^{(t)}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "$Q$-NPG: Performance Bounds for Log-Linear Policies", "weight": 1.0} -->

Our analysis will take into account both the *excess risk* (often also referred to as estimation error) and the *transfer error*. Here, the excess risk will be due to that $w^{(t)}$ may not be equal $w_{\star}^{(t)}$, and the approximation error will be due to that even the best linear fit using $w_{\star}^{(t)}$ may not perfectly match the $Q$-values, i.e. $L{(w_{\star}^{(t)};\theta^{(t)};d^{(t)})}$ is unlikely to be $0$ in practical applications.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Assumption 6.1 (Estimation/Transfer errors)", "weight": 1.0} -->

Fix a state distribution $\rho$; a state-action distribution $\nu$; an arbitrary comparator policy $\pi^{\star}$ (not necessarily an optimal policy). With respect to $\pi^{\star}$, define the state-action measure $d^{\star}$ as i.e. $d^{\star}$ samples states from the comparators state visitation measure, $d_{\rho}^{\pi^{\star}}$ and actions from the uniform distribution. Let us permit the sequence of iterates $w^{},w^{},{\ldotsw^{({T - 1})}}$ used by the $Q$-NPG algorithm to be random, where the randomness could be due to sample-based, estimation error.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Assumption 6.1 (Estimation/Transfer errors)", "weight": 1.0} -->

Suppose the following holds for all $t < T$: (*Excess risk*) Assume that the estimation error is bounded as follows: Note that using a sample based approach we would expect $\epsilon_{stat} = {O{({1/\sqrt{N}})}}$ or better, where $N$ is the number of samples used to estimate. $w_{\star}^{(t)}$ We formalize this in Corollary 6.2.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Assumption 6.1 (Estimation/Transfer errors)", "weight": 1.0} -->

(*Transfer error*) Suppose that the best predictor $w_{\star}^{(t)}$ has an error bounded by $\epsilon_{bias}$, in expectation, with respect to the comparator's measure of $d^{\ast}$. Specifically, assume: We refer to $\epsilon_{bias}$ as the *transfer error* (or *transfer bias*); it is the error where relevant distribution is shifted to $d^{\star}$. For the softmax policy parameterization for tabular MDPs, $\epsilon_{bias} = 0$ (see remark 6.4 for another example).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Assumption 6.1 (Estimation/Transfer errors)", "weight": 1.0} -->

In both conditions, the expectations are with respect to the randomness in the sequence of iterates $w^{},w^{},{\ldotsw^{({T - 1})}}$, e.g. the approximate algorithm may be sample based.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Assumption 6.1 (Estimation/Transfer errors)", "weight": 1.0} -->

Shortly, we discuss how the transfer error relates to the more standard approximation-estimation decomposition. Importantly, with the transfer error, it is always defined with respect to a single, fixed measure, $d^{\star}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Assumption 6.2 (Relative condition number)", "weight": 1.0} -->

Consider the same $\rho$, $\nu$, and $\pi^{\star}$ as in Assumption 6.1. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift"). With respect to any state-action distribution $\upsilon$, define: Assume that $\kappa$ is finite.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Assumption 6.2 (Relative condition number)", "weight": 1.0} -->

Remark 6.3 discusses why it is reasonable to expect that $\kappa$ is not a quantity related to the size of the state space.^77^7Technically, we only need the relative condition number $\sup_{w \in {\mathbb{R}}^{d}}\frac{w^{\top}\Sigma_{d^{\star}}w}{w^{\top}\Sigma_{\pi^{(t)}}w}$ to be bounded for all $t$. We state this as a sufficient condition based on the initial distribution $\nu$ due to: this is more interpretable, and, as per Remark 6.3, this quantity can be bounded in a manner that is independent of the sequence of iterates produced by the algorithm.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Assumption 6.2 (Relative condition number)", "weight": 1.0} -->

Our main theorem below shows how the approximation error, the excess risk, and the conditioning, determine the final performance. Note that both the transfer error $\epsilon_{bias}$ and $\kappa$ are defined with respect to the comparator policy $\pi^{\star}$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 6.3", "weight": 1.0} -->

(Dimension dependence in $\kappa$ and the importance of $\nu$) It is reasonable to think about $\kappa$ as being dimension dependent (or worse), but it is not necessarily related to the size of the state space. For example, if ${\|\phi_{s,a}\|}_{2} \leq B$, then $\kappa \leq \frac{B^{2}}{\sigma_{\min}{({{\mathbb{E}}_{{s,a} \sim \nu}{\lbrack{\phi_{s,a}\phi_{s,a}^{\top}}\rbrack}})}}$ though this bound may be pessimistic. Here, we also see the importance of choice of $\nu$ in having a small (relative) condition number; in particular, this is the motivation for considering the generalization which allows for a starting state-action distribution $\nu$ vs. just a starting state distribution $\mu$ (as we did in the tabular case).

<!-- chunk {"id": "body-0100", "role": "body", "section": "Remark 6.3", "weight": 1.0} -->

Roughly speaking, we desire a $\nu$ which provides good coverage over the features. As the following lemma shows, there always exists a universal distribution $\nu$, which can be constructed only with knowledge of the feature set (without knowledge of $d^{\star}$), such that $\kappa \leq d$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Remark 6.4", "weight": 1.0} -->

($\epsilon_{bias} = 0$ for "linear" MDPs) In the recent linear MDP model of Jin et al.; Yang and Wang; Jiang et al., where the transition dynamics are low rank, we have that $\epsilon_{bias} = 0$ provided we use the features of the linear MDP. Our guarantees also permit model misspecification of linear MDPs, with non worst-case approximation error where $\epsilon_{bias} \neq 0$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Remark 6.5", "weight": 1.0} -->

(Comparison with Politex and EE-Politex) Compared with Politex, Assumption 6.2. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift") is substantially milder, in that it just assumes a good relative condition number for one policy rather than all possible policies (which cannot hold in general even for tabular MDPs). Changing this assumption to an analog of Assumption 6.2. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift") is the main improvement in the analysis of the EE-Politex algorithm. They provide a regret bound for the average reward setting, which is qualitatively different from the suboptimality bound in the discounted setting that we study. They provide a specialized result for linear function approximation, similar to Theorem 6.1.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Assumption 6.3 (Episodic Sampling Oracle)", "weight": 1.0} -->

For a fixed state-action distribution $\nu$, we assume the ability to: start at ${s_{0},a_{0}} \sim \nu$; continue to act thereafter in the MDP according to any policy $\pi$; and terminate this "rollout" when desired. With this oracle, it is straightforward to obtain unbiased samples of $Q^{\pi}{(s,a)}$ (or $A^{\pi}{(s,a)}$) under ${s,a} \sim d_{\nu}^{\pi}$ for any $\pi$; see Algorithms 1 and 3.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Assumption 6.3 (Episodic Sampling Oracle)", "weight": 1.0} -->

1:Starting state-action distribution ν. 3:Sample s, a ∼ dνπ as follows: at every timestep h, with probability γ, act according to π; else, accept (sh, ah) as the sample and proceed to Step 5. See. 4: From sh, ah, continue to execute π, and use a termination probability of 1 − γ. Upon termination, set $\hat{Q^{\pi}}{(s_{h},a_{h})}$ as the undiscounted sum of rewards from time h onwards. 5:return (sh, ah) and $\hat{Q^{\pi}}{(s_{h},a_{h})}$. Algorithm 1 Sampler: s, a ∼ dνπ and unbiased estimate of Qπ (s, a) Algorithm 2 provides a sample based version of the $Q$-NPG algorithm; it simply uses stochastic projected gradient ascent within each iteration. The following corollary shows this algorithm suffices to obtain an accurate sample based version of $Q$-NPG.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Remark 6.6", "weight": 1.0} -->

(Improving the scaling with $N$) Our current rate of convergence is $1/N^{1/4}$ due to our use of stochastic projected gradient ascent. Instead, for the least squares estimator, $\epsilon_{stat}$ would be $O{({d/N})}$ provided certain further regularity assumptions hold (a bound on the minimal eigenvalue of $\Sigma_{\nu}$ would be sufficient but not necessary. See Hsu et al. for such conditions). With such further assumptions, our rate of convergence would be $O{({1/\sqrt{N}})}$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "NPG: Performance Bounds for Smooth Policy Classes", "weight": 1.0} -->

We now return to the analyzing the standard NPG update rule, which uses advantages rather than $Q$-values (see Section 6.1). It is helpful to define where $\upsilon$ is state-action distribution, and the subscript of $A$ denotes the loss function uses advantages (rather than $Q$-values). The iterates of the NPG algorithm can be viewed as minimizing this loss under some appropriately chosen measure.

<!-- chunk {"id": "body-0107", "role": "body", "section": "NPG: Performance Bounds for Smooth Policy Classes", "weight": 1.0} -->

We now consider an approximate version of the NPG update rule: where again we use the on-policy, fitting distribution $d^{(t)}$. As with $Q$-NPG, we also permit the use of a starting state-action distribution $\nu$ as opposed to just a starting state distribution (see Remark 6.3). Again, we let $w_{\star}^{(t)}$ denote the minimizer, i.e. $w_{\star}^{(t)} \in {{{argmin}_{{\| w\|}_{2} \leq W}L_{A}}{(w;\theta^{(t)},d^{(t)})}}$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "NPG: Performance Bounds for Smooth Policy Classes", "weight": 1.0} -->

For this section, our analysis will focus on more general policy classes, beyond log-linear policy classes.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Assumption 6.4", "weight": 1.0} -->

(Policy Smoothness) Assume for all $s \in \mathcal{S}$ and $a \in \mathcal{A}$ that ${\log\pi_{\theta}}{(\left. a \middle| s \right.)}$ is a $\beta$-smooth function of $\theta$ (to recall the definition of smoothness, see ).

<!-- chunk {"id": "body-0110", "role": "body", "section": "Assumption 6.4", "weight": 1.0} -->

It is not to difficult to verify that the tabular softmax policy parameterization is a $1$-smooth policy class in the above sense. The more general class of log-linear policies is also smooth as we remark below.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Remark 6.7", "weight": 1.0} -->

(Smoothness of the log-linear policy class) For the log-linear policy class (see Section 6.1.1), smoothness is implied if the features $\phi$ have bounded Euclidean norm. Precisely, if the feature mapping $\phi$ satisfies ${\|\phi_{s,a}\|}_{2} \leq B$, then it is not difficult to verify that ${\log\pi_{\theta}}{(\left. a \middle| s \right.)}$ is a $B^{2}$-smooth function.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Remark 6.7", "weight": 1.0} -->

For any state-action distribution $\upsilon$, define: and, again, we use $\Sigma_{\upsilon}^{(t)}$ as shorthand for $\Sigma_{\upsilon}^{\theta^{(t)}}$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Assumption 6.5", "weight": 1.0} -->

(Estimation/Transfer/Conditioning) Fix a state distribution $\rho$; a state-action distribution $\nu$; an arbitrary comparator policy $\pi^{\star}$ (not necessarily an optimal policy). With respect to $\pi^{\star}$, define the state-action measure $d^{\star}$ as Note that, in comparison to Assumption 6.1. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift"), $d^{\star}$ is the state-action visitation measure of the comparator policy. Let us permit the sequence of iterates $w^{},w^{},{\ldotsw^{({T - 1})}}$ used by the NPG algorithm to be random, where the randomness could be due to sample-based, estimation error.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Assumption 6.5", "weight": 1.0} -->

Suppose the following holds for all $t < T$: (Excess risk) Assume the estimation error is bounded as: i.e. the above conditional expectation is bounded (with probability one).^88^8The use of a conditional expectation here (vs. the unconditional one in Assumption 6.1. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift")) permits the assumption to hold even in settings where we may reuse data in the sample-based approximation of $L_{A}$. Also, the expectation over the iterates allows a more natural assumption on the relative condition number, relevant for the more general case of smooth policies. As we see in Corollary 6.2, we can guarantee $\epsilon_{stat}$ to drop as $\sqrt{1/N}$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Assumption 6.5", "weight": 1.0} -->

(Transfer error) Suppose that: (Relative condition number) For all iterations $t$, assume the average relative condition number is bounded as follows: Note that term inside the expectation is a random quantity as $\theta^{(t)}$ is random.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Assumption 6.5", "weight": 1.0} -->

In the above conditions, the expectation is with respect to the randomness in the sequence of iterates $w^{},w^{},{\ldotsw^{({T - 1})}}$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Assumption 6.5", "weight": 1.0} -->

Analogous to our $Q$-NPG theorem, our main theorem for NPG shows how the transfer error is relevant in addition the statistical error $\epsilon_{stat}$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Remark 6.8", "weight": 1.0} -->

(The $|\mathcal{A}|$ dependence: NPG vs. $Q$-NPG) Observe there is no polynomial dependence on $|\mathcal{A}|$ in the rate for NPG (in constrast to Theorem 6.1); also observe that here we define $d^{\star}$ as the state-action distribution of $\pi^{\star}$ in Assumption 6.5, as opposed to a uniform distribution over the actions, as in Assumption 6.1. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift").

<!-- chunk {"id": "body-0119", "role": "body", "section": "Remark 6.8", "weight": 1.0} -->

The main difference arises in the analysis in that, even for $Q$-NPG, we need to bound the error in fitting the advantage estimates; this leads to the dependence on $|\mathcal{A}|$ (which can be removed with a path dependent bound, i.e. a bound which depends on the sequence of iterates produced by the algorithm)^99^9 For $Q$-NPG, we have to bound two distribution shift terms to both $\pi^{\star}$ and $\pi^{(t)}$ at step $t$ of the algorithm.. For NPG, the direct fitting of the advantage function sidesteps this conversion step. Note that the relative condition number assumption in $Q$-NPG (Assumption 6.2. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift")) is a weaker assumption, due to that it can be bounded independently of the path of the algorithm (see Remark 6.2.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Remark 6.8", "weight": 1.0} -->

‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift")), while NPG's centering of the features makes the assumption on the relative condition number depend on the path of the algorithm.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Remark 6.9", "weight": 1.0} -->

(Generalizing $Q$-NPG for smooth policies) A similar reasoning as the analysis here can be also used to establish a convergence result for the $Q$-NPG algorithm in this more general setting of smooth policy classes. Concretely, we can analyze the $Q$-NPG update described for neural policy classes in Section 6.1.2, assuming that the function $f_{\theta}$ is Lipschitz-continuous in $\theta$. Like for Theorem 6.2, the main modification is that Assumption 6.2. ‣ 6.2 𝑄-NPG: Performance Bounds for Log-Linear Policies ‣ 6 Function Approximation and Distribution Shift ‣ On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift") on relative condition numbers is now defined using the covariance matrix for the features $f_{\theta}{(s,a)}$, which depend on $\theta$, as opposed to some a feature map $\phi{(s,a)}$ in the log-linear case. The rest of the analysis follows with an appropriate adaptation of the results above.

<!-- chunk {"id": "body-0122", "role": "body", "section": "NPG Sample Complexity", "weight": 1.0} -->

Algorithm 4 provides a sample based version of the NPG algorithm, again using stochastic projected gradient ascent; it uses a slight modification of the $Q$-NPG algorithm to obtain unbiased gradient estimates. The following corollary shows that this algorithm provides an accurate sample based version of NPG.

<!-- chunk {"id": "body-0123", "role": "body", "section": "NPG Sample Complexity", "weight": 1.0} -->

1:Starting state-action distribution ν. 2:Set $\hat{Q^{\pi}} = 0$ and $\hat{V^{\pi}} = 0$. 3:Start at state s0 ∼ ν. Sample a0 ∼ ν(⋅|s0) (though do not necessarily execute a0). 4:(dνπ sampling) At every timestep h ≥ 0, With probability γ, execute ah, transition to sh + 1, and sample ah + 1 ∼ π(⋅|sh + 1). Else accept (sh, ah) as the sample and proceed to Step 5.

<!-- chunk {"id": "body-0124", "role": "body", "section": "NPG Sample Complexity", "weight": 1.0} -->

5: (Aπ (s, a) sampling) Set SampleQ = True with probability 1/2.

<!-- chunk {"id": "body-0125", "role": "body", "section": "NPG Sample Complexity", "weight": 1.0} -->

If SampleQ = True, execute ah at state sh and then continue executing π with a termination probability of 1 − γ. Upon termination, set $\hat{Q^{\pi}}$ as the undiscounted sum of rewards from time h onwards. Else sample ah′ ∼ π(⋅|sh). Then execute ah′ at state sh and then continue executing π with a termination probability of 1 − γ. Upon termination, set $\hat{V^{\pi}}$ as the undiscounted sum of rewards from time h onwards.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Analysis", "weight": 1.0} -->

We first proceed by providing a general analysis of NPG, for arbitrary sequences. We then specialize it to complete the proof of our two main theorems in this section.

<!-- chunk {"id": "body-0127", "role": "body", "section": "The NPG \"Regret Lemma\"", "weight": 1.0} -->

It is helpful for us to consider NPG more abstractly, as an update rule of the form We will now provide a lemma where $w^{(t)}$ is an *arbitrary* (bounded) sequence, which will be helpful when specialized.

<!-- chunk {"id": "body-0128", "role": "body", "section": "The NPG \"Regret Lemma\"", "weight": 1.0} -->

Recall a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is said to be $\beta$-smooth if for all ${x,x'} \in {\mathbb{R}}^{d}$: and, due to Taylor's theorem, recall that this implies: The following analysis of NPG is based on the mirror-descent approach developed, which motivates us to refer to it as a "regret lemma".

<!-- chunk {"id": "body-0129", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

Proof: (of Theorem 6.1) Using the NPG regret lemma (Lemma 6.2) and the smoothness of the log-linear policy class (see Example 6.7), where we have used our setting of $\eta$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

For the second term, let us now show that: To see this, first observe that a similar argument to the above leads to: where we use the notation ${\| x\|}_{M}^{2}:={x^{\top}Mx}$ for a matrix $M$ and a vector $x$. From the definition of $\kappa$, using that ${{({1 - \gamma})}\nu} \leq d_{\nu}^{\pi^{(t)}}$ (see).

<!-- chunk {"id": "body-0131", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

Due to that $w_{\star}^{(t)}$ minimizes $L{(w;\theta^{(t)},d^{(t)})}$ over the set $\mathcal{W}:={\{ w:{{\| w\|}_{2} \leq W}\}}$, for any $w \in \mathcal{W}$ the first-order optimality conditions for $w_{\star}^{(t)}$ imply that: Therefore, for any $w \in \mathcal{W}$, Noting that $w^{(t)} \in \mathcal{W}$ by construction in Algorithm 4 yields the claimed bound on the second term.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

Using the bounds on the first and second terms in and, along with concavity of the square root function, we have that: The proof is completed by substitution and using our assumptions on $\epsilon_{stat}$ and $\epsilon_{bias}$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

The following proof for the NPG algorithm follows along similar lines.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

Proof: (of Theorem 6.2) Using the NPG regret lemma and our setting of $\eta$, where the expectation is with respect to the sequence of iterates $w^{},w^{},{\ldotsw^{({T - 1})}}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

Again, we make the following decomposition of ${err}_{t}$: For the first term, where we have used the definition of $L_{A}{(w_{\star}^{(t)};\theta^{(t)},d^{\star})}$ in the last step.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

For the second term, a similar argument leads to: Define $\kappa^{(t)}:={\|{{(\Sigma_{\nu}^{(t)})}^{- {1/2}}\Sigma_{d^{\star}}{(\Sigma_{\nu}^{(t)})}^{- {1/2}}}\|}_{2}$, which is the relative condition number at iteration $t$. We have where the last step uses that $w_{\star}^{(t)}$ is a minimizer of $L_{A}$ over $\mathcal{W}$ and that $w^{(t)}$ is feasible as before (see the proof of Theorem 6.1). Now taking an expectation we have: where we have used our assumption on $\kappa$ and $\epsilon_{stat}$.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Proofs of Theorem 6.1 and 6.2", "weight": 1.0} -->

The proof is completed by substitution and using the concavity of the square root function.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Discussion", "weight": 1.5} -->

This work provides a systematic study of the convergence properties of policy optimization techniques, both in the tabular and the function approximation settings. At the core, our results imply that the non-convexity of the policy optimization problem is not the fundamental challenge for typical variants of the policy gradient approach. This is evidenced by the global convergence results which we establish and that demonstrate the relative niceness of the underlying optimization problem. At the same time, our results highlight that insufficient exploration can lead to the convergence to sub-optimal policies, as is also observed in practice; technically, we show how this is an issue of conditioning. Conversely, we can expect typical policy gradient algorithms to find the best policy from amongst those whose state-visitation distribution is adequately aligned with the policies we discover, provided a distribution-shifted notion of approximation error is small.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the tabular case, our results show that the nature and severity of the exploration/distribution mismatch term differs in different policy optimization approaches. For instance, we find that doing policy gradient in its standard form for both the direct and softmax parameterizations can be slow to converge, particularly in the face of distribution mismatch, even when policy gradients are computed exactly. Natural policy gradient, on the other hand, enjoys a fast dimension-free convergence when we are in tabular settings with exact gradients. On the other hand, for the function approximation setting, or when using finite samples, all algorithms suffer to some degree from the exploration issue captured through a conditioning effect.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Discussion", "weight": 1.5} -->

With regards to function approximation, the guarantees herein are the first provable results that permit average case approximation errors, where the guarantees do not have explicit worst case dependencies over the state space. These worst case dependencies are avoided by precisely characterizing an approximation/estimation error decomposition, where the relevant approximation error is under distribution shift to an optimal policies measure. Here, we see that successful function approximation relies on two key aspects: good conditioning (related to exploration) and low distribution-shifted, approximation error. In particular, these results identify the relevant measure of the expressivity of a policy class, for the natural policy gradient.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Discussion", "weight": 1.5} -->

With regards to sample size issues, we showed that simply using stochastic (projected) gradient ascent suffices for accurate policy optimization. However, in terms of improving sample efficiency and polynomial dependencies, there are number of important questions for future research, including variance reduction techniques along with data re-use.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Discussion", "weight": 1.5} -->

There are number of compelling directions for further study. The first is in understanding how to remove the density ratio guarantees among prior algorithms; our results are suggestive that the incremental policy optimization approaches, including CPI, PSDP, and MD-MPI Geist et al., may permit such an improved analysis. The question of understanding what representations are robust to distribution shift is well-motivated by the nature of our distribution-shifted, approximation error (the transfer error). Finally, we hope that policy optimization approaches can be combined with exploration approaches, so that, provably, these approaches can retain their robustness properties (in terms of their agnostic learning guarantees) while mitigating the need for a well conditioned initial starting distribution.
