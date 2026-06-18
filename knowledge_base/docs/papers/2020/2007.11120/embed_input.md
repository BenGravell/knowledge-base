<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Linear Convergence of Policy Gradient Methods for Finite MDPs

Topics include Policy iteration, Optimization, Policy gradients.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We revisit the finite time analysis of policy gradient methods in the one of the simplest settings: finite state and action MDPs with a policy class consisting of all stochastic policies and with exact gradient evaluations. There has been some recent work viewing this setting as an instance of smooth non-linear optimization problems and showing sub-linear convergence rates with small step-sizes. Here, we take a different perspective based on connections with policy iteration and show that many variants of policy gradient methods succeed with large step-sizes and attain a linear rate of convergence.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods, dating back to the works of, along with their modern variants, have emerged as one of the most effective classes of algorithms for solving challenging reinforcement learning problems with impressive empirical success. Despite this, little was known about their global convergence properties, as these methods search over a parameterized class of policies by performing (stochastic) gradient descent on a scalar loss function that is typically non-convex.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This has changed recently with several recent papers analysing the global convergence properties of policy gradient methods. Our earlier work identifies properties for general MDPs which guarantee that (despite non-convexity) the optimization landscape does not suffer from spurious local optima, thereby implying convergence of policy gradient methods to globally optimal solutions. Though that work does not consider specific algorithms, some convergence rates for follow easily from the framework (e.g. a sub-linear convergence rate for tabular MDPs using projected gradient descent with natural parameterization). The most comprehensive analysis of convergence rates appears in Agarwal et al., showing results for different combinations of policy parametrization (natural and softmax policies), algorithms (projected and natural gradient descent) as well as entropy regularization^11^1Agarwal et al. also go beyond tabular MDPs to give results for a compatible function approximation setting. Shani et al. focus on analyzing trust region optimization methods based on mirror descent, giving rates for both unregularized and regularized tabular MDPs. Essentially all of these papers view policy optimization as instances of general smooth nonlinear optimization problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The analyses suggest small step-sizes to control for the error due to local linearization and show convergence to an $\epsilon$--optimal policy within either $O\left( \frac{1}{\epsilon} \right)$ or $O\left( \frac{1}{\epsilon^{2}} \right)$ iterations, depending on the precise algorithm used.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we revisit the finite time analysis of policy gradient methods in the simplest setting: finite state and action MDPs with a policy class consisting of all stochastic policies and with exact gradient evaluations. This setting was covered in the aforementioned works of Bhandari and Russo; Agarwal et al.; Shani et al.. Instead of viewing the problem through the lens of nonlinear optimization, we take a policy iteration perspective. We highlight that many forms of policy gradient can work with extremely large stepsizes and attain a *linear* rate of convergence, meaning they require only $O{({\log\left( {1/\epsilon} \right)})}$ iterations to reach an $\epsilon$--optimal policy. At the core of our ideas is a connection between policy gradients and policy iteration, which underlies the analysis in Bhandari and Russo.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For finite MDPs, we show that this leads to an extremely simple analysis covering many different first-order methods applied to the policy gradient objective, including projected gradient descent, Frank-Wolfe, mirror descent, and natural gradient descent. In an idealized setting where step-sizes are set by line search, a one paragraph proof applies to all algorithms. For natural gradient algorithms, a slightly longer calculation studies a specific step-size sequence. In the final section of this paper, we also discuss a setting of approximate line search as well as natural gradient methods with entropy regularization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Scope and purpose of this work", "weight": 1.0} -->

It is possible that readers might find our setting of tabular MDPs with access to exact gradients somewhat limited. It is worth noting that recent works of have all compared the convergence rates of different policy gradient methods in this setting. Our work clarifies that with exact gradient evaluations, much faster convergence rates can be achieved with larger step-sizes. The results on line search based step-size selection are especially idealized, but show that classical non-linear optimization techniques would automatically select larger step sizes and attain linear convergence rates.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Scope and purpose of this work", "weight": 1.0} -->

Small step-sizes may be critical for controlling approximation errors and stabilizing algorithms in practical settings. Studying such issues likely requires a model that focuses on approximation errors and incomplete policy classes. Our work instead offers a clear understanding of what to expect in a setting without these challenges.

<!-- chunk {"id": "body-0010", "role": "body", "section": "On concurrent work", "weight": 1.0} -->

We remark on the concurrent works of which also show linear convergence of exact policy gradient methods for entropy regularized tabular MDPs with softmax policies and exact gradients. The main motivation behind these works is to theoretically characterize the benefits of using entropy based regularizers to obtain faster convergence rates. While both analyze different variants (simple gradients vs natural gradients), using entropy regularization seems crucial to their results. Another key difference is that unlike, our proof techniques rely on a direct connection between policy gradients and policy iteration, leading to concise proofs that are applicable to a broad range of algorithms along with transparent bounds with a clear dependence on all relevant constants. Instead of leveraging sophisticated algebra, our focus is on giving readers a clear understanding.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider a Markov decision process (MDP), which is a six-tuple $(\mathcal{S},\mathcal{A},g,P,\gamma,\rho)$, consisting of a state space $\mathcal{S}$, action space $\mathcal{A}$, cost function $g$, transition kernel $P$, discount factor $\gamma \in {}$ and initial distribution $\rho$. We assume the state space $\mathcal{S}$ to be finite and index the states as $\mathcal{S} = {\{ s_{1},\cdots,s_{n}\}}$. For each state $s \in \mathcal{S}$, we assume that there is a finite set of $k$ arms to choose from and take the action space, $\mathcal{A} = \Delta^{k - 1}$ to be the set of all probability distributions over those $k$ arms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

That is, any action $a \in \mathcal{A}$ is a probability vector where each component $a_{i}$ denotes the probability of taking the $i$-th action. The transition kernel $P$ specifies the probability $P{(\left. s^{\prime} \middle| {s,a} \right.)}$ of transitioning to a state $s^{\prime}$ upon choosing action $a$ in state $s$. The cost function ${g{(s,a)}} \in {\mathbb{R}}$ denotes the instantaneous expected cost incurred when selecting action $a$ in state $s$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $e_{i}$ is the $i$-th standard basis vector, representing one of the $k$ possible arms. We assume that costs are non-negative, meaning ${g{(s,e_{i})}} \geq 0$ for all $s \in \mathcal{S}$ and $i \in {\{ 1,\ldots,k\}}$. This holds without loss of generality, as one can always add the same large constant to the cost of each state and action without changing the decision problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Cost-to-go functions and Bellman operators", "weight": 1.0} -->

A stationary policy $\pi:{\mathcal{S}\rightarrow\mathcal{A}}$ selects a distribution over the $k - 1$ dimensional simplex, $\Delta^{k - 1}$ for each state $s \in \mathcal{S}$. We use the notation $\pi{(s,i)}$ to denote the probability of selecting action $i$ in state $s$ under policy $\pi$. Let $\Pi$ denote the set of all stationary policies over the simplex,

<!-- chunk {"id": "body-0015", "role": "body", "section": "Cost-to-go functions and Bellman operators", "weight": 1.0} -->

As the per-step costs are uniformly bounded, so are the cost-to-go functions. Define the Bellman operator $T_{\pi}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ under policy $\pi$ and the Bellman optimality operator $T:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ as,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Cost-to-go functions and Bellman operators", "weight": 1.0} -->

Note that the Bellman optimality operator can be equivalently defined as ${{({TJ})}{(s)}} = {{\min_{\pi \in \Pi}{({T_{\pi}J})}}{(s)}}$. The cost-to-go function under policy $\pi$ is the unique solution to the Bellman equation, $J_{\pi} = {T_{\pi}J_{\pi}}$. Similarly, the optimal cost-to-go function, $J^{\ast}$ which satisfies ${J^{\ast}{(s)}} = {{\min_{\pi}J_{\pi}}{(s)}}$ for all $s \in \mathcal{S}$, is the unique fixed point of $T$ and that there is at least one optimal policy, $\pi^{\ast} \in \Pi$ that attains this minimum for every $s \in \mathcal{S}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Cost-to-go functions and Bellman operators", "weight": 1.0} -->

From the above definitions, it is simple to check that: $J_{\pi} = {T_{\pi}J_{\pi}} \succeq {TJ_{\pi}}$ for any $\pi \in \Pi$. We will use this inequality repeatedly throughout our analysis.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Cost-to-go functions and Bellman operators", "weight": 1.0} -->

measures the cumulative expected cost of taking action $a$ in state $s$ and applying $\pi$ thereafter.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Cost-to-go functions and Bellman operators", "weight": 1.0} -->

Note that for any policy ${\pi \in \Pi},{s \in \mathcal{S}}$ and $a \in \Delta^{k - 1}$, linearity of the cost and transitions functions in implies that the Q-function is linear in $a$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Loss function and initial distribution", "weight": 1.0} -->

Policy gradient methods seek to minimize the scalar loss function

<!-- chunk {"id": "body-0021", "role": "body", "section": "Loss function and initial distribution", "weight": 1.0} -->

in which the states are weighted by their initial probabilities under $\rho$ and we have normalized costs by $({1 - \gamma})$ for convenience. We assume throughout that $\rho$ is supported on $\mathcal{S}$, meaning that ${\rho{(s)}} > 0$ for all $s \in \mathcal{S}$ which implies that $\pi \in {{{\arg\min}_{\overline{\pi}}\ell}{(\overline{\pi})}}$ if and only if $\pi \in {{{\arg\min}_{\overline{\pi}}J_{\overline{\pi}}}{(s)}{\forall s}} \in \mathcal{S}$. Assuming an exploratory initial distribution is critical as it is well known that, in the absence of strong assumptions on the transition kernel, policy gradient methods can fail catastrophically if applied without some form of intelligent exploration. See for a simple example and the discussions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Linear convergence of policy iteration", "weight": 1.0} -->

We briefly revisit the classic policy iteration algorithm as our analysis of policy gradient methods is intricately tied to it. Starting from an initial policy $\pi$, policy iteration first evaluates the corresponding cost-to-go function $Q_{\pi}$, and then updates to a new policy $\pi^{+}$ such that

<!-- chunk {"id": "body-0023", "role": "body", "section": "Linear convergence of policy iteration", "weight": 1.0} -->

In terms of the Bellman operators, this can be equivalently expressed as, ${T_{\pi^{+}}J_{\pi}} = {TJ_{\pi}}$. A simple analysis of policy iteration follows by using the monotonicity and contraction properties of the Bellman operators. Observe that

<!-- chunk {"id": "body-0024", "role": "body", "section": "Linear convergence of policy iteration", "weight": 1.0} -->

Inductively applying $T_{\pi^{+}}$ to each side and using the monotonicity property yields a policy improvement property,

<!-- chunk {"id": "body-0025", "role": "body", "section": "Linear convergence of policy iteration", "weight": 1.0} -->

using the contraction property. From this, we conclude that policy iteration converges to the optimal policy at a linear rate. Let ${\{\pi^{t}\}}_{t \geq 0}$ be the set of policies produced by policy iteration. Then iterating over shows

<!-- chunk {"id": "body-0026", "role": "body", "section": "Linear convergence of policy iteration", "weight": 1.0} -->

In fact, policy iteration can sometime also converge quadratically in the limit.

<!-- chunk {"id": "body-0027", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

Recently, Bhandari and Russo analyze the optimization landscape of the policy gradient objective $\ell{( \cdot )}$ for general MDPs and policy classes. A starting point of that analysis is rewriting the policy gradient theorem in a form that emphasizes the illuminating connections between policy gradient and policy iteration. We specialize that presentation to the tabular setting and argue that several first-order methods applied to the policy gradient loss $\ell{( \cdot )}$ will essentially perform a soft policy iteration update and hence converge at a geometric rate, similar to policy iteration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

For any policy $\pi \in \Pi$, consider the weighed policy iteration or "Bellman" objective, defined as

<!-- chunk {"id": "body-0029", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

where $e_{i}$ denotes the $i$-th standard basis vector, denoting one of the $k$ arms, ${\langle v,u\rangle}_{W} = {\sum_{s = 1}^{n}{\sum_{i = 1}^{k}{v{(s,i)}u{(s,i)}W{(s,i)}}}}$ denotes the $W$-weighted inner product and $\eta_{\pi} \times 1$ denotes a weighting that places weight ${\eta_{\pi}{(s)}} \cdot 1$ on any state-action pair $(s,i)$. Recall that since ${\rho{(s)}} > 0$ by assumption, ${\eta_{\pi}{(s)}} > 0$ for all $s \in \mathcal{S}$ and hence the policy iteration update can be equivalently written as optimizing the Bellman objective,

<!-- chunk {"id": "body-0030", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

It is worth emphasizing that the Bellman cost function is a single period objective, considering the cost-to-go of following $\overline{\pi}$ for a single period and following $\pi$ thereafter. A policy gradient theorem connects gradients of the infinite horizon cost function $\ell{( \cdot )}$ to gradients of the single period Bellman objective underlying policy iteration. In particular, we have the following lemma from Bhandari and Russo, which is essentially a restatement of the classical version.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

We write all algorithms in terms of their evolution in the space of policies $\Pi$. Several of them could instead be viewed as operating in the space of parameters for some parameterized policy class. We discuss this in Remark 1. ‣ Exact line search. ‣ 5 Policy gradient methods for finite MDPs"), but keep our formulation and results focused on the space of policies $\Pi$. Note that $\Pi = {\Delta^{k - 1} \times \cdots \times \Delta^{k - 1}}$ is the $n$-fold product of the probability simplex. This form of the policy class will cause policy gradient updates to decouple across states.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

: Starting with some policy $\pi \in \Pi$, an iteration of the Frank-Wolfe algorithm computes

<!-- chunk {"id": "body-0033", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

and then updates the policy to $\pi^{\prime} = {{{({1 - \alpha})}\pi} + {\alpha\pi^{+}}}$ for $\alpha \in {\lbrack 0,1\rbrack}$. We use the notation $\pi^{+}$ in as it is exactly the policy iteration update to $\pi$ so *Frank-Wolfe mimics a soft-policy iteration step*, akin to the conservative policy iteration update^22^2A generalized version of Frank-Wolfe was studied in under the name of "Boosted Policy Search" to show global optimality guarantees for any locally optimal policy. in Kakade and Langford. Note, the minimization problem in decouples across states to optimize a linear objective over the probability simplex, so

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

: Starting with some policy $\pi \in \Pi$, an iteration of the projected gradient descent algorithm with constant stepsize $\alpha$ updates to the solution of the following regularized problem

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

As $\alpha\rightarrow\infty$ (the regularization term tends to zero), $\pi^{\prime}$ converges to the solution of, which is exactly the policy iteration update as noted above.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

which is a gradient step followed by projection onto the probability simplex. Note that from an implementation perspective, projections onto the probability simplex involves a computationally efficient ($\mathcal{O}{({k{\log k}})}$) soft-thresholding operation.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

: The mirror descent method adapts to the geometry of the probability simplex by using a non-euclidean regularizer.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

where $D_{KL}{(p||q)} = \sum_{i = 1}^{k}p_{i}{\log\left( {p_{i}/q_{i}} \right)}$ denotes the KL divergence. It is well know that the solution to this optimization problem is the exponentiated gradient update,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

Again, we can see that $\pi^{\prime}$ converges to a policy iteration update as $\alpha\rightarrow\infty$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

Natural policy gradient and TRPO.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

: We consider the natural policy gradient (NPG) algorithm of Kakade which is closely related to the widely used TRPO algorithm of Schulman et al.. We focus on NPG applied to the softmax parameterization for which it is actually an instance of mirror descent with a specific regularizer.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

using a regularizer that penalizes changes to the action distribution at states in proportion to their occupancy measure $\eta_{\pi}$. As discussed above, it is well known that this KL divergence regularized problem is solved by an exponentiated weights update for each state $s \in {\{ 1,\ldots,n\}}$,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

Note that as compared to, this update rule is independent of the state occupancy measure $\eta_{\pi}$. A potential source of confusion is that natural policy gradient is usually described as steepest descent in a variable metric defined by the Fisher information matrix induced by the current policy^33^3This is equivalent to mirror descent under some conditions Raskutti and Mukherjee.,

<!-- chunk {"id": "body-0044", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

where $M^{\dagger}$ denotes the pseudoinverse of matrix $M$. Readers can check that the exponentiated update in matches the explicit formula for the NPG update with softmax policies as given in Kakade and Agarwal et al..

<!-- chunk {"id": "body-0045", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

Step-size selection is an important issue for most first order methods. Each of the algorithms above can be applied with a sequence of stepsizes ${\{\alpha_{t}\}}_{t \geq 0}$ to produce a sequence of policies ${\{\pi^{t}\}}_{t \geq 0}$. We define one stepsize selection rule below.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Exact line search", "weight": 1.0} -->

At iteration $t$, the update rules for each of the algorithms described above actually specify a new policy $\pi_{\alpha}^{t + 1}$ for a range of stepsizes, $\alpha \geq 0$. We consider an idealized stepsize rule using *exact line search*, which directly optimizes over this choice of stepsize at each iteration, selecting $\pi^{t + 1} = \pi_{\alpha^{\ast}}^{t + 1}$ where $\alpha^{\ast} = {{{\arg\min}_{\alpha}\ell}{(\pi_{\alpha}^{t + 1})}}$ whenever this minimizer exists. More generally, we define

<!-- chunk {"id": "body-0047", "role": "body", "section": "Exact line search", "weight": 1.0} -->

Under NPG, $\{\pi_{\alpha}^{t + 1}\}$ is a curve where $\pi_{0}^{t + 1} = \pi^{t}$ and $\pi_{\alpha}^{t + 1}\rightarrow\pi_{+}^{t}$ as $\alpha\rightarrow\infty$. Since $\pi_{+}^{t}$ is not attainable under any fixed $\alpha$, this curve is not closed. By taking the closure, and defining line search via, certain formulas become cleaner. Of course, it is also possible to nearly solve without taking the closure and obtain essentially the same results. We elaborate on this in the discussion that follows our main result in Theorem 1. ‣ 6 Main result: geometric convergence").

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 1 (Policy parameterization and infima vs minima)", "weight": 1.0} -->

We chose to work with the class of all stochastic policies $\Pi$ (often termed as natural parameterization) as opposed to some parameterized policy classes, which are more commonly used in practice. For example, a policy gradient algorithm might search over the parameter $\theta \in {\mathbb{R}}^{n \times k}$ of a softmax policy $\pi_{\theta} \in \Pi$, defined by ${\pi_{\theta}{(s,i)}} \propto e^{\theta_{s,i}}$. For example, consider the TRPO algorithm proposed by which uses a locally linearization of $\ell{(\pi)}$, forms the regularized minimization problem, and then updates the parameter of a softmax policy $\pi_{\theta}$ by solving

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 1 (Policy parameterization and infima vs minima)", "weight": 1.0} -->

We could define similar versions of projected gradient descent or Frank-Wolfe, which also linearize $\ell{(\pi)}$, but then optimize the resulting local approximation only over parameterized policies. Since the class of softmax policies can approximate any stochastic policy to arbitrary precision, this is nearly the same as optimizing over the policy class $\Pi$. Studying $\Pi$ directly makes mathematical analysis easier, because it is closed. For example, it contains an optimal policy, whereas any softmax policy $\pi_{\theta}$ can only come infinitesimally close to an optimal policy. In practice, optimization problems are never solved beyond machine precision, so we don't view the distinction between infimum and minimum to be relevant to the paper's main insights. We caution the reader that our results do not apply to more naive gradient methods that directly linearize $\ell{(\pi_{\theta})}$ with respect to $\theta$. In that case, a gradient update to $\theta$ may not approximate a policy iteration update, no matter how large the stepsize is chosen to be.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 1 (Policy parameterization and infima vs minima)", "weight": 1.0} -->

In fact, such methods may perform badly due to issues of poor conditioning.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

So far, we have described different variants of policy gradient methods for tabular MDPs. For large step-sizes, all these algorithms essentially make a policy iteration update. Hence, intuitively, it is reasonable to expect that their convergence behavior closely resembles that of policy iteration rather than that of gradient descent for smooth objectives. We quantify this precisely in Theorem 1. ‣ 6 Main result: geometric convergence") below.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Our first result confirms that all of the algorithms we presented in the previous section converge geometrically when step-sizes are set by exact line search on $\ell{( \cdot )}$. Again, the idea is that a policy gradient step is a policy iteration update for an appropriate choice of stepsize. Our proof effectively uses that exact line search updates make at least as much progress in reducing $\ell{( \cdot )}$ as a policy iteration update. The mismatch between the policy gradient loss $\ell{( \cdot )}$, which governs the stepsize choice, and the maximum norm, which governs policy iteration convergence, is the source of the term ${\min_{s \in \mathcal{S}}\rho}{(s)}$ in the bound. We further elaborate on this issue in the discussion that follows Theorem 1. ‣ 6 Main result: geometric convergence").

<!-- chunk {"id": "body-0053", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Our second and third results show that dependence on the initial distribution in the bounds can be avoided by forcing the algorithm to use large stepsizes. A simple result in part (b) applies to the Frank-Wolfe algorithm with a constant stepsize, which gives performance improvement in max norm. This bound follows by essentially making a minor modification to the linear convergence result of policy iteration as reviewed in Section 3. Recall that we already showed a Frank-Wolfe update to be exactly equivalent to a soft policy iteration update,

<!-- chunk {"id": "body-0054", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Given this close connection, a simple argument shows that an $\alpha$-step Frank-Wolfe update offers at least a fraction of the performance improvement offered by a policy iteration update,

<!-- chunk {"id": "body-0055", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

which implies the result. A comparison between parts (a) and (b) suggest that for $\alpha \geq {1/{|\mathcal{S}|}}$, Frank-Wolfe with exact line search might converge slowly as compared to the constant step-size version in the worst case.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

For softmax policies and exact gradient evaluations, we show in part (c) that NPG with an adaptive step-size sequence converges to an $\epsilon$ optimal policy in $O{({\log\left( {1/\epsilon} \right)})}$ iterations. The error term, $\epsilon$, is inversely related to the step-size and reflects the fact that NPG updates with finite step-sizes only approximately resemble the policy iteration updates^44^4More precisely, our proof shows that in this case, the NPG update is equivalent to a soft policy iteration update upto some additive error.. As we take the step-size to infinity, we recover the same result as one would expect for policy iteration. Compared to the first result in part (a) which applies with exact line search, the result in part (c) is useful in the sense that it gives a precise quantification of how large the step-sizes need to be for linear convergence to hold.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 2", "weight": 1.0} -->

For the result in part (c), note that for the softmax parameterization, ${\pi_{\theta}{(s,i)}} > 0$ for any $\theta \in {\mathbb{R}}^{n \times k}$. So, ${\pi^{t}{(s,i_{t}^{\ast})}} > 0$ for all $t$. A similar result can also be obtained without the need of adaptive step-sizes by considering entropy regularized MDPs. This is discussed below.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

The following discussion is based primarily on feedback of the reviewers. We thank them for their valuable inputs.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

Dependence on $\rho_{\min}$ for exact line search result:\
Readers will note that proof of our result in part (a) of Theorem 1. ‣ 6 Main result: geometric convergence") also shows that,

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

where $\rho_{\min} = {{\min_{s \in \mathcal{S}}\rho}{(s)}}$. A natural question to ask is whether the presence of the factor of $\rho_{\min}$ in the geometric rate is merely an artifact of our analysis technique and if in practice, line search always ends up picking the policy iteration update corresponding to $\alpha = 1$. In Figure 1 above, we plot the line search objective,

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

for a Frank-Wolfe update for a randomly generated^55^5We generated many random MDPs to compare updates of policy iteration with those of Frank-Wolfe using grid search and found many cases where these differ. Details of only one such example is given to illustrate our point. MPD with two states and three actions. For a given choice of $(P,g,\rho)$ and policy $\pi$ (see Appendix B for details), we observe that $\ell{(\pi_{\alpha})}$ is non-monotonic in $\alpha$ and therefore exact line-search does often select smaller step-sizes as compared to the greedy update $({\alpha = 1})$. Although we do not show a lower bound, this example suggests that a factor of $\rho_{\min}$ in the bound here might be unavoidable.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

On inexact line search: Though our result in part (a) of Theorem 1. ‣ 6 Main result: geometric convergence") focuses on an idealized setting with exact line search, we do note that a similar result can also be obtained if we can ensure, say using inexact line search, that the improvement in total cost $\ell{( \cdot )}$ at every update is at least a fraction of the improvement offered by exact line search.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

For example, if we select a step-size sequence ${\{\alpha_{t}\}}_{t \geq 0}$ which offers half the possible improvement at every update, meaning ${{\ell{(\pi^{t})}} - {\ell{(\pi_{\alpha_{t}}^{t + 1})}}} \geq {{({1/2})}{({{\ell{(\pi^{t})}} - {\inf_{\alpha^{\prime}}{\ell{(\pi_{\alpha^{\prime}}^{t + 1})}}}})}}$, then our result in part (a) follows with an extra factor of $\frac{1}{2}$ in the bound. One essentially needs to modify the first step in the proof (Equation (12: Exact line-search: ‣ 6.1 Proof of Theorem 1 ‣ 6 Main result: geometric convergence"))) and the rest is same.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

A linear convergence result can also be obtained if the sequence of policies, ${\{\pi^{t}\}}_{t \geq 0}$, obtained via inexact line search offer approximately the same improvement as a policy iteration update, i.e. ${\ell{(\pi^{t + 1})}} \leq {{\ell{(\pi_{+}^{t})}} + \delta}$ holds uniformly for some $\delta > 0$. In this case, a bound similar to that in part (a) will hold with an additional scaled bias term of $\delta/{({1 - \gamma})}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

NPG with softmax policies for regularized MDPs:\
Recall that the result in part (c) uses an adaptive step-size sequence $\alpha_{t}{(s)}$ that depends on $\pi^{t}{(s,i_{t}^{\ast})}$, probability under the randomized policy at iteration $t$ assigned to the action $i_{t}^{\ast}$ prescribed by policy iteration. This dependence is a bit undesirable and can be removed by considering entropy regularized MDPs. Entropy regularization prevents policies from picking near deterministic actions and essentially lower bounds $\pi^{t}{(s,i_{t}^{\ast})}$. Rather than presenting a lengthy re-derivation of the result in part (c), we sketch a simple argument essentially based on some past work on the theory of regularized MDPs, to show linear convergence with a particular choice of step-size. Although this result in Equation is almost identical to the one in Cen et al., our ideas, based on connections to policy iteration, considerably simplify the proof.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

A common way to enforce regularization is by adding a small penalty to the cost function,

<!-- chunk {"id": "body-0067", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

Similar to, a quick calculation using the policy gradient theorem reveals that an NPG update for a $\lambda$-regularized MDP solves the following problem,

<!-- chunk {"id": "body-0068", "role": "body", "section": "Discussion of results", "weight": 1.5} -->

where ${\mathcal{H}{({\pi{(s)}})}} = {\sum_{i = 1}^{k}{\pi{(s,i)}{\log\pi}{(s,i)}}}$ is the negative entropy. Importantly, $T^{\lambda}{( \cdot )}$ can also be shown to be a monotone and $\gamma$-contraction in the maximum norm with a unique fixed point, $J^{\ast,\lambda}$ such that ${\|{J^{\ast,\lambda} - J^{\ast}}\|}_{\infty} \leq \frac{\lambda{\log k}}{({1 - \gamma})}$. See for details. Therefore, similar to the proof of policy iteration in Section 3, we can obtain a geometric convergence result for NPG with softmax policies and a constant step-size of $\alpha = {1/\lambda}$,

<!-- chunk {"id": "body-0069", "role": "body", "section": "Part (a): Exact line-search", "weight": 1.0} -->

Under each algorithm and at each iteration $t$, the policy iteration update $\pi_{+}^{t}$ is contained in the class $\Pi^{t + 1}$ introduced in Equation. Therefore, for each algorithm,

<!-- chunk {"id": "body-0070", "role": "body", "section": "Part (b): Constant stepsize Frank-Wolfe", "weight": 1.0} -->

The proof here follows the analysis of policy iteration reviewed in Section 3.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Part (b): Constant stepsize Frank-Wolfe", "weight": 1.0} -->

where $\pi_{+}^{t}$ is the policy iteration update to $\pi^{t}$. Thus, starting from a feasible policy $\pi^{0} \in \Pi$, we always maintain feasibility for $\alpha \in {(0,1\rbrack}$. By linearity of the cost and transition functions as shown, we have that for any state $s$,

<!-- chunk {"id": "body-0072", "role": "body", "section": "Part (b): Constant stepsize Frank-Wolfe", "weight": 1.0} -->

Therefore, from (13: Constant stepsize Frank-Wolfe: ‣ 6.1 Proof of Theorem 1 ‣ 6 Main result: geometric convergence")), we get

<!-- chunk {"id": "body-0073", "role": "body", "section": "Part (b): Constant stepsize Frank-Wolfe", "weight": 1.0} -->

Subtracting $J^{\ast}$ from both sides shows

<!-- chunk {"id": "body-0074", "role": "body", "section": "Part (b): Constant stepsize Frank-Wolfe", "weight": 1.0} -->

Since the above inequality holds element wise,

<!-- chunk {"id": "body-0075", "role": "body", "section": "Part (c): Proof for natural policy gradient with softmax policies and adaptive step-sizes", "weight": 1.0} -->

Our proof strategy shows that for any state $s \in \mathcal{S}$, an NPG update with step-size $\alpha_{t}{(s)}$ decreases the probability of sub-optimal actions by a multiplicative factor. Informally, the set of sub-optimal actions per state can be understood to be the set of actions with action gap^66^6The action gap of any action $i \in {\{ 1,\ldots,k\}}$ is the difference between Q-values when compared to the optimal action. larger than some threshold. Essentially, this shows the NPG update is equivalent to a soft policy iteration update upto a small additive error. We divide the proof into three steps.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Step 1: NPG update for sub-optimal actions", "weight": 1.0} -->

Fix some state $s \in \mathcal{S}$. Without loss of generality, we assume the following ordering on the Q-values: ${Q^{t}{(s,1)}} < {Q^{t}{(s,2)}\ldots} < {Q^{t}{(s,k)}}$ which implies that action 1 is optimal in state $s$ under policy $\pi^{t}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Step 1: NPG update for sub-optimal actions", "weight": 1.0} -->

The set $O_{t}^{-}{(s)}$ can be interpreted as the set of sub-optimal actions with the action gap, ${Q^{t}{(s,i)}} - {Q^{t}{(s,1)}}$, larger than the threshold $\epsilon/c$. Similarly, $O_{t}^{+}{(s)}$ can be interpreted to be the set of nearly optimal actions according to policy $\pi^{t}$. The following lemma (proved in Appendix A) shows that NPG updates decrease the probability of playing sub-optimal actions by a multiplicative factor.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Step 2: NPG updates as soft policy iteration", "weight": 1.0} -->

The policy iteration update, ${\pi_{+}^{t}{(s)}} = {{{\arg\min}_{i \in {\{ 1,2,\ldots,k\}}}Q^{t}}{(s,i)}}$, puts entire mass on the best action (according to Q-values of the current policy) and zeros out the probability of playing other actions. On the other hand, Lemma 2 shows how an NPG update with appropriate stepsize decays the probabilities of sub-optimal actions (in the set $O_{t}^{-}{(s)}$) by a multiplicative factor instead of zeroing them out^77^7This defintion of sub-optimal actions based on action gap threshold, $\epsilon/c$, is essentially an artifact that we are taking gradient steps with finite step-sizes.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Step 2: NPG updates as soft policy iteration", "weight": 1.0} -->

As ${\alpha_{t}{(s)}}\rightarrow{\infty{\forall s}} \in \mathcal{S}$, an NPG update is exactly equal to a policy iteration update.. This resembles a soft-policy iteration update for the set of actions $O_{t}^{-}{(s)}$. We formalize this intuition in the following lemma which characterizes the progress made by an NPG update vis-a-vis a policy iteration update.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Step 3: Completing the proof", "weight": 1.0} -->

Lemma 3. ‣ Step 2: NPG updates as soft policy iteration: ‣ 6.1 Proof of Theorem 1 ‣ 6 Main result: geometric convergence") clearly quantifies the relationship between an NPG update with step-size $\alpha_{t}$ and a soft policy iteration update with an additive error $\frac{\epsilon}{c}$. With this connection, we give a simple proof of geometric convergence for the natural policy gradient method. First, we claim that ${J_{\pi^{t + 1}}{(s)}} \leq {J_{\pi^{t}}{(s)}}$. To see this, recall from Section 5 that an NPG update with step-size $\alpha{(s)}$ can equivalently be written as,

<!-- chunk {"id": "body-0081", "role": "body", "section": "Step 3: Completing the proof", "weight": 1.0} -->

But staying at the current policy, i.e. taking $a = {\pi^{t}{(s)}}$ is feasible for the optimization problem above. Therefore,

<!-- chunk {"id": "body-0082", "role": "body", "section": "Step 3: Completing the proof", "weight": 1.0} -->

Using this along with Lemma 3. ‣ Step 2: NPG updates as soft policy iteration: ‣ 6.1 Proof of Theorem 1 ‣ 6 Main result: geometric convergence"), we get

<!-- chunk {"id": "body-0083", "role": "body", "section": "Step 3: Completing the proof", "weight": 1.0} -->

Subtracting $J^{\ast}$ from both sides and rearranging terms gives,

<!-- chunk {"id": "body-0084", "role": "body", "section": "Step 3: Completing the proof", "weight": 1.0} -->

As the above inequality holds element wise, we use the contractivity property of $T{( \cdot )}$ as shown in to get

<!-- chunk {"id": "body-0085", "role": "body", "section": "Step 3: Completing the proof", "weight": 1.0} -->

Iterating over the above equation and rewriting $\left( {\frac{1}{2} + \frac{\gamma}{2}} \right) = \left( {1 - {\frac{1}{2}{({1 - \gamma})}}} \right)$ gives us our desired result. ∎

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we use illuminating connections with policy iteration as shown in Bhandari and Russo to show how many variants of policy gradient algorithms with large step-sizes and exact gradient evaluations converge geometrically fast for tabular MDPs. An interesting question for future work is whether these results can be extended to function approximation settings where the policy class might be restricted, for example in Agarwal et al.. Another interesting question is whether our results hold in settings where unbiased estimates of the value functions are obtained via sampling. Here some exciting progress has been recently made for the undiscounted (average cost setting) in for ergodic MDPs, by leveraging connections to approximate policy iteration.
