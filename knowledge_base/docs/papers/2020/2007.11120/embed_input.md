<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Linear Convergence of Policy Gradient Methods for Finite MDPs

Topics include Policy iteration, Optimization, Policy gradients.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We revisit the finite time analysis of policy gradient methods in the one of the simplest settings: finite state and action MDPs with a policy class consisting of all stochastic policies and with exact gradient evaluations. There has been some recent work viewing this setting as an instance of smooth non-linear optimization problems and showing sub-linear convergence rates with small step-sizes. Here, we take a different perspective based on connections with policy iteration and show that many variants of policy gradient methods succeed with large step-sizes and attain a linear rate of convergence.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods, dating back to the works of [williams1992simple,baxter1999direct,sutton2000policy,marbach2001simulation], along with their modern variants [kakade2002natural, silver2014deterministic], have emerged as one of the most effective classes of algorithms for solving challenging reinforcement learning problems with impressive empirical success [schulman2015trust,schulman2017proximal]. Despite this, little was known about their global convergence properties, as these methods search over a parameterized class of policies by performing (stochastic) gradient descent on a scalar loss function that is typically non-convex.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This has changed recently with several recent papers analysing the global convergence properties of policy gradient methods. Our earlier work identifies properties for general MDPs which guarantee that (despite non-convexity) the optimization landscape does not suffer from spurious local optima, thereby implying convergence of policy gradient methods to globally optimal solutions [bhandari2019global]. Though that work does not consider specific algorithms, some convergence rates for follow easily from the framework (e.g. a sub-linear convergence rate for tabular MDPs using projected gradient descent with natural parameterization). The most comprehensive analysis of convergence rates appears in [agarwal2019optimality], showing results for different combinations of policy parametrization (natural and softmax policies), algorithms (projected and natural gradient descent) as well as entropy regularization also go beyond tabular MDPs to give results for a compatible function approximation setting. [shani2019adaptive] focus on analyzing trust region optimization methods [schulman2015trust, schulman2017proximal] based on mirror descent [beck2003mirror], giving rates for both unregularized and regularized tabular MDPs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Essentially all of these papers view policy optimization as instances of general smooth nonlinear optimization problems. The analyses suggest small step-sizes to control for the error due to local linearization and show convergence to an $\epsilon$optimal policy within either $O\left(\frac{1}{\epsilon}\right)$ or $O\left(\frac{1}{\epsilon^2}\right)$iterations, depending on the precise algorithm used.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we revisit the finite time analysis of policy gradient methods in the simplest setting: finite state and action MDPs with a policy class consisting of all stochastic policies and with exact gradient evaluations. This setting was covered in the aforementioned works of [bhandari2019global, agarwal2019optimality,shani2019adaptive]. Instead of viewing the problem through the lens of nonlinear optimization, we take a policy iteration perspective. We highlight that many forms of policy gradient can work with extremely large stepsizes and attain a linear rate of convergence, meaning they require only $O(\log(1/\epsilon))$ iterations to reach an $\epsilon$optimal policy. At the core of our ideas is a connection between policy gradients and policy iteration, which underlies the analysis in [bhandari2019global].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For finite MDPs, we show that this leads to an extremely simple analysis covering many different first-order methods applied to the policy gradient objective, including projected gradient descent, Frank-Wolfe, mirror descent, and natural gradient descent. In an idealized setting where step-sizes are set by line search, a one paragraph proof applies to all algorithms. For natural gradient algorithms, a slightly longer calculation studies a specific step-size sequence. In the final section of this paper, we also discuss a setting of approximate line search as well as natural gradient methods with entropy regularization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scope and purpose of this work: It is possible that readers might find our setting of tabular MDPs with access to exact gradients somewhat limited. It is worth noting that recent works of [agarwal2019optimality,shani2019adaptive,cen2020fast,mei2020global]have all compared the convergence rates of different policy gradient methods in this setting. Our work clarifies that with exact gradient evaluations, much faster convergence rates can be achieved with larger step-sizes. The results on line search based step-size selection are especially idealized, but show that classical non-linear optimization techniques would automatically select larger step sizes and attain linear convergence rates.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Small step-sizes may be critical for controlling approximation errors and stabilizing algorithms in practical settings. Studying such issues likely requires a model that focuses on approximation errors and incomplete policy classes. Our work instead offers a clear understanding of what to expect in a setting without these challenges.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We remark on the concurrent works of [cen2020fast, mei2020global] which also show linear convergence of exact policy gradient methods for entropy regularized tabular MDPs with softmax policies and exact gradients. The main motivation behind these works is to theoretically characterize the benefits of using entropy based regularizers to obtain faster convergence rates. While both analyze different variants (simple gradients vs natural gradients), using entropy regularization seems crucial to their results. Another key difference is that unlike [cen2020fast,mei2020global], our proof techniques rely on a direct connection between policy gradients and policy iteration, leading to concise proofs that are applicable to a broad range of algorithms along with transparent bounds with a clear dependence on all relevant constants. Instead of leveraging sophisticated algebra, our focus is on giving readers a clear understanding.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider a Markov decision process (MDP), which is a six-tuple $\left(\mathcal{S}, \mathcal{A}, g, P, \gamma, \rho \right)$, consisting of a state space $\mathcal{S}$, action space $\mathcal{A}$, cost function $g$, transition kernel $P$, discount factor $\gamma \in $ and initial distribution $\rho$. We assume the state space $\mathcal{S}$ to be finite and index the states as $\mathcal{S} = \{s_1,\cdots, s_n\}$. For each state $s\in \mathcal{S}$, we assume that there is a finite set of $k$ arms to choose from and take the action space, $\mathcal{A} = \Delta^{k-1}$ to be the set of all probability distributions over those $k$ arms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

That is, any action $a \in \mathcal{A}$ is a probability vector where each component $a_i$ denotes the probability of taking the $i$-th action. The transition kernel $P$ specifies the probability $P(s'|s,a)$ of transitioning to a state $s'$ upon choosing action $a$ in state $s$. The cost function $g(s,a)\in \mathbb{R}$ denotes the instantaneous expected cost incurred when selecting action $a$ in state $s$. Cost and transition functions can be naturally extended to functions on the probability simplex by defining: where $e_i$ is the $i$-th standard basis vector, representing one of the $k$ possible arms. We assume that costs are non-negative, meaning $ g(s,e_i) \geq 0 $ for all $s \in \mathcal{S}$ and $i \in \{1, \ldots, k\}$. This holds without loss of generality, as one can always add the same large constant to the cost of each state and action without changing the decision problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Cost-to-go functions and Bellman operators. A stationary policy $\pi: \mathcal{S} \to \mathcal{A}$ selects a distribution over the $k-1$ dimensional simplex, $\Delta^{k-1}$ for each state $s \in \mathcal{S}$. We use the notation $\pi(s,i)$ to denote the probability of selecting action $i$ in state $s$ under policy $\pi$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Define the Bellman operator $T_{\pi}: \mathbb{R}^n \to \mathbb{R}^n$ under policy $\pi$ and the Bellman optimality operator $T: \mathbb{R}^n \to \mathbb{R}^n$ as, \left(T_{\pi} J\right)(s) &:= g(s, \pi(s)) + \gamma \sum_{s' \in \mathcal{S}} P(s' | s, \pi(s)) J(s') \\\left(T J\right)(s) &:= \min_{a \in \mathcal{A}} \left[g(s,a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) J(s') \right].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Note that the Bellman optimality operator can be equivalently defined as $(TJ)(s) = \min_{\pi \in \Pi} (T_{\pi}J)(s)$. The cost-to-go function under policy $\pi$ is the unique solution to the Bellman equation, $J_\pi = T_{\pi} J_\pi$. Similarly, the optimal cost-to-go function, $J^*$ which satisfies $J^*(s) = \min_{\pi} J_{\pi}(s)$ for all $s\in \mathcal{S}$, is the unique fixed point of $T$ and that there is at least one optimal policy, $\pi^* \in \Pi$ that attains this minimum for every $s\in \mathcal{S}$. From the above definitions, it is simple to check that: $J_{\pi}=T_{\pi}J_{\pi} \succeq T J_{\pi}$ for any $\pi\in\Pi$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We will use this inequality repeatedly throughout our analysis.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our analysis uses a few basic properties of Bellman operators, see [bertsekas1995dynamic] or [puterman2014markov] for proofs. Under the assumption that per-period costs are bounded, $T$ and $T_{\pi}$ are monotone, meaning the element-wise inequality $J \preceq J'$ implies $TJ\preceq TJ'$ and $T_{\pi}J \preceq T_{\pi}J'$. They are also contraction operators with respect to the maximum norm. That is, $\| TJ - TJ' \|_{\infty} \leq \gamma \|J - J' \|_{\infty}$ and $\| T_{\pi} J - T_{\pi}J' \|_{\infty} \leq \gamma \|J - J' \|_{\infty}$ hold for for any $J,J' \in \mathbb{R}^n$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The state-action cost-to-go function under policy $\pi\in \Pi$, $$Q_{\pi}(s,a)= g(s,a)+ \gamma \sum_{s' \in \mathcal{S}} P(s'\mid s,a) J_{\pi}(s'),$$ measures the cumulative expected cost of taking action $a$ in state $s$ and applying $\pi$ thereafter. For any polices $\pi,\pi'\in \Pi$, we have the following relations: Note that for any policy $\pi \in \Pi, s \in \mathcal{S}$ and $a \in \Delta^{k-1}$, linearity of the cost and transitions functions in [eq: tabular costs and transitions\_ch3] implies that the Q-function is linear in $a$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

$$Q_{\pi}(s,a) = \sum_{i=1}^k Q_{\pi}(s,e_i) a_i = \langle Q_{\pi}(s,\cdot), a \rangle$$ Loss function and initial distribution. Policy gradient methods seek to minimize the scalar loss function $$\ell(\pi)= (1-\gamma)\sum_{s \in \mathcal{S}} J_{\pi}(s) \, \rho(s),$$ in which the states are weighted by their initial probabilities under $\rho$ and we have normalized costs by $(1-\gamma)$ for convenience.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We assume throughout that $\rho$ is supported on $\mathcal{S}$, meaning that $\rho(s)>0$ for all $s\in \mathcal{S}$ which implies that $\pi \in \argmin_{\bar{\pi}} \ell(\bar{\pi})$ if and only if $\pi\in\argmin_{\bar{\pi} } J_{\bar{\pi}}(s) \,\,\, \forall \, s \in \mathcal{S}$. Assuming an exploratory initial distribution is critical as it is well known that, in the absence of strong assumptions on the transition kernel, policy gradient methods can fail catastrophically if applied without some form of intelligent exploration. See [thrun1992cient, kakade2002approximately] for a simple example and the discussions in [agarwal2019optimality, bhandari2019global].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

State distributions. We define the discounted state occupancy measure under any policy $\pi$ and initial state distribution $\rho$ as: $$\eta_{\pi} = (1-\gamma)\sum_{t=0}^{\infty} \gamma^{t} \rho P_{\pi}^t = (1-\gamma) \rho (I - \gamma P_\pi)^{-1},$$ where $\eta_{\pi}$ and $\rho$ are both row vectors, $P_{\pi} \in \mathbb{R}^{n\times n}$ denotes the Markov transition matrix under $\pi$, i.e. $P_{\pi} = (P(s'| s, \pi(s)))_{s,s'\in \mathcal{S}}$ and $P_{\pi}^t$ denotes its $t$-step counterpart. Thus, $\eta_{\pi}$ is essentially the discounted fraction of time the system spends in a given state.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Note that we have $\eta_{\pi}(s) \geq (1-\gamma) \rho(s) > 0$ as we assumed $\rho(s) > 0$ for all $s \in \mathcal{S}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Linear convergence of policy iteration", "weight": 1.0} -->

We briefly revisit the classic policy iteration algorithm as our analysis of policy gradient methods is intricately tied to it. Starting from an initial policy $\pi$, policy iteration first evaluates the corresponding cost-to-go function $Q_{\pi}$, and then updates to a new policy $\pi^+$ such that $$\pi^+(s) \in \argmin_{a\in \mathcal{A}} \, Q_{\pi}(s,a) \quad \forall \, s\in \mathcal{S}.$$ In terms of the Bellman operators, this can be equivalently expressed as, $T_{\pi^+} J_{\pi} = TJ_{\pi}$. A simple analysis of policy iteration follows by using the monotonicity and contraction properties of the Bellman operators.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Linear convergence of policy iteration", "weight": 1.0} -->

Observe that Inductively applying $T_{\pi^+}$ to each side and using the monotonicity property yields a policy improvement property, J_{\pi} \succeq T_{\pi^+} J_{\pi} \succeq T^{2}_{\pi^+} J_{\pi} \succeq \cdots \succeq J_{\pi^+}.

<!-- chunk {"id": "body-0025", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

Recently, [bhandari2019global] analyze the optimization landscape of the policy gradient objective $\ell(\cdot)$ for general MDPs and policy classes. A starting point of that analysis is rewriting the policy gradient theorem in a form that emphasizes the illuminating connections between policy gradient and policy iteration. We specialize that presentation to the tabular setting and argue that several first-order methods applied to the policy gradient loss $\ell(\cdot)$ will essentially perform a soft policy iterationupdate and hence converge at a geometric rate, similar to policy iteration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

that places weight $\eta_{\pi}(s) \cdot 1$ on any state-action pair $(s,i)$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

Recall that since $\rho(s)>0$ by assumption, $\eta_{\pi}(s) > 0$ for all $s \in \mathcal{S}$ and hence the policy iteration update can be equivalently written as optimizing the Bellman objective, $$\pi^+ = \argmin_{{\bar{\pi}} \in \Pi} \mathcal{B}({\bar{\pi}} | \eta_{\pi}, J_{\pi}).$$ It is worth emphasizing that the Bellman cost function is a single period objective, considering the cost-to-go of following ${\bar{\pi}}$ for a single period and following $\pi$ thereafter. A policy gradient theorem connects gradients of the infinite horizon cost function $\ell(\cdot)$ to gradients of the single period Bellman objective underlying policy iteration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

In particular, we have the following lemma from [bhandari2019global], which is essentially a restatement of the classical version by [sutton2000policy, sutton2018reinforcement].

<!-- chunk {"id": "body-0029", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

Presentation of the policy gradient theorem in terms of the Bellman objective clarifies an important connection we can interpret $\nabla \ell(\pi)$ as gradient of the weighted policy iteration objective. What is special about the tabular setting, relative to the general problems considered by [bhandari2019global], is that the weighted policy iteration objective is linear. In the following section, we use this connection to show that various first-order methods applied to $\ell(\cdot)$ can optimize the Bellman objective $\mathcal{B}(\cdot | \eta_{\pi}, J_{\pi})$to optimality in a single update with large (and possibly infinite) step-sizes; equivalent to a policy iteration update. For finitely large step-sizes, a simple argument establishes equivalence between a policy gradient step and a soft policy iteration update, again implying geometric convergence.

<!-- chunk {"id": "body-0030", "role": "body", "section": "A sharp connection between policy gradient and policy iteration", "weight": 1.0} -->

Note that for tabular MDPs, a policy iteration step is simple as it reduces to solving a linear optimization problem over the probability simplex, and the optimal solution is to select the best action for each state.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

We write all algorithms in terms of their evolution in the space of policies $\Pi$. Several of them could instead be viewed as operating in the space of parameters for some parameterized policy class. We discuss this in Remark [rem:parameterization], but keep our formulation and results focused on the space of policies $\Pi$. Note that $\Pi = \Delta^{k-1} \times \cdots \times \Delta^{k-1}$ is the $n$-fold product of the probability simplex. This form of the policy class will cause policy gradient updates to decouple across states.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

- Starting with some policy $\pi\in \Pi$, an iteration of the Frank-Wolfe algorithm computes \pi^+ = \argmin_{{\bar{\pi}} \in \Pi} \, \langle \nabla\ell(\pi), {\bar{\pi}} \rangle = \argmin_{{\bar{\pi}} \in \Pi} \, \langle Q_{\pi}, {\bar{\pi}} \rangle_{\eta_{\pi} \times 1} - and then updates the policy to $\pi' =(1-\alpha) \pi + \alpha \pi^+$ for $\alpha \in $. We use the notation $\pi^+$ in [eq: tabular-franke-wolfe-optimization] as it is exactly the policy iteration update to $\pi$ so Frank-Wolfe mimics a soft-policy iteration step, akin to the conservative policy iteration update A generalized version of Frank-Wolfe was studied in under the name of Boosted Policy Search to show global optimality guarantees for any locally optimal policy.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

- in [kakade2002approximately]. Note, the minimization problem in [eq: tabular-franke-wolfe-optimization] decouples across states to optimize a linear objective over the probability simplex, so $$\pi^{+}(s) \in \argmin_{d \in \Delta^{k-1}} \, d^{\top} Q_{\pi}(s, \cdot)$$ - is a point-mass that places all weight on $\argmin_{i} Q_{\pi}(s, e_i)$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

- As $\alpha \to \infty$ (the regularization term tends to zero), $\pi'$ converges to the solution of [eq: tabular-franke-wolfe-optimization], which is exactly the policy iteration update as noted above. For intermediate values of $\alpha$, the projected gradient update decouples across states and takes the form: $$\pi'(s) = {\rm Proj}_{2, \Delta^{k-1}}(\pi(s) - \alpha Q_{\pi}(s, \cdot))$$ - which is a gradient step followed by projection onto the probability simplex. Note that from an implementation perspective, projections onto the probability simplex involves a computationally efficient ($\mathcal{O}(k \log k)$) soft-thresholding operation [duchi2008efficient]. - The mirror descent method adapts to the geometry of the probability simplex by using a non-euclidean regularizer.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

It is well know that the solution to this optimization problem is the exponentiated gradient update [bubeck2015convex], $$\pi'(s,i) = \frac{\pi(s,i) \cdot \exp\{ -\alpha \eta_{\pi}(s) Q_{\pi}(s,e_i) \} }{ \sum_{j=1}^{k} \pi(s,j) \cdot \exp\{ -\alpha \eta_{\pi}(s) Q_{\pi}(s,e_j) \}}.$$ - Again, we can see that $\pi'$ converges to a policy iteration update as $\alpha \to \infty$. - We consider the natural policy gradient (NPG) algorithm of [kakade2002natural] which is closely related to the widely used TRPO algorithm of [schulman2015trust]. We focus on NPG applied to the softmax parameterization for which it is actually an instance of mirror descent with a specific regularizer.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

KL}({\bar{\pi}}_s \, || \, \pi_s) - using a regularizer that penalizes changes to the action distribution at states in proportion to their occupancy measure $\eta_{\pi}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

As discussed above, it is well known that this KL divergence regularized problem is solved by an exponentiated weights update for each state $s\in \{1,\ldots, n \}$, \pi'(s,i) = \left(\frac{\pi(s,i) \cdot \exp\{ -\alpha Q_{\pi}(s,e_i) \} }{ \sum_{j=1}^{k} \pi(s,j) \cdot \exp\{ -\alpha Q_{\pi}(s,e_j) \} }\right). - Note that as compared to [eq:mirror\_descent\_update], this update rule is independent of the state occupancy measure $\eta_{\pi}$. A potential source of confusion is that natural policy gradient is usually described as steepest descent in a variable metric defined by the Fisher information matrix induced by the current policy mirror descent under some conditions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

\pi' &= \pi + \alpha F(\pi)^{\dagger} \nabla \ell(\pi) \\F(\pi) &= \sum_{s,i} \eta_{\pi}(s) \pi(s,i) \left[\nabla \log \pi(s,i) \left(\nabla \log \pi(s,i) \right)^\top \right] - where $M^{\dagger}$ denotes the pseudoinverse of matrix $M$. Readers can check that the exponentiated update in [eq:NPG\_update] matches the explicit formula for the NPG update with softmax policies as given in [kakade2002natural] and [agarwal2019optimality].

<!-- chunk {"id": "body-0039", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

Step-size selection is an important issue for most first order methods. Each of the algorithms above can be applied with a sequence of stepsizes $\{\alpha_{t}\}_{t \geq 0}$ to produce a sequence of policies $\{\pi^t \}_{t \geq 0}$. We define one stepsize selection rule below.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

Exact line search. At iteration $t$, the update rules for each of the algorithms described above actually specify a new policy $\pi^{t+1}_{\alpha}$ for a range of stepsizes, $\alpha \geq 0$. We consider an idealized stepsize rule using exact line search, which directly optimizes over this choice of stepsize at each iteration, selecting $\pi^{t+1} = \pi^{t+1}_{\alpha^*}$ where $\alpha^* = \argmin_{\alpha} \ell(\pi^{t+1}_{\alpha})$ whenever this minimizer exists. More generally, we define where $\Pi^{t+1} = {\rm Closure}(\{ \pi_{\alpha}^{t+1}\})$ denotes the closed curve of policies traced out by varying $\alpha$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

For Frank-Wolfe, $\Pi^{t+1} = \{ \alpha \pi^t + (1-\alpha) \pi^t_+: \alpha \in \} $ is the line segment connecting the current policy $\pi^t$ and its policy iteration update $\pi^t_+$. Under NPG, $\{\pi^{t+1}_{\alpha} \}$ is a curve where $\pi^{t+1}_{0}=\pi^t$ and $\pi^{t+1}_{\alpha} \to \pi^t_+$ as $\alpha \to \infty$. Since $\pi^t_+$ is not attainable under any fixed $\alpha$, this curve is not closed. By taking the closure, and defining line search via [eq: exact linesearch], certain formulas become cleaner. Of course, it is also possible to nearly solve [eq: exact linesearch] without taking the closure and obtain essentially the same results.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

We elaborate on this in the discussion that follows our main result in Theorem [thm: tabular rates].

<!-- chunk {"id": "body-0043", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

We chose to work with the class of all stochastic policies $\Pi$ (often termed as natural parameterization) as opposed to some parameterized policy classes, which are more commonly used in practice. For example, a policy gradient algorithm might search over the parameter $\theta \in \mathbb{R}^{n\times k}$ of a softmax policy $\pi_{\theta} \in \Pi$, defined by $\pi_{\theta}(s,i) \propto e^{\theta_{s,i}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

For example, consider the TRPO algorithm proposed by [schulman2015trust] which uses a locally linearization of $\ell(\pi)$, forms the regularized minimization problem in [eq:NPGupdateform], and then updates the parameter of a softmax policy $\pi_{\theta}$ by solving $$\argmin_{{\overline{\theta}}} \,\, \langle Q_{\pi_{\theta}}, \pi_{{\overline{\theta}}} \rangle_{\eta_{\pi_{\theta}} \times 1} + \frac{1}{\alpha}\sum_{s=1}^{n} \eta_{\pi_{\theta}}(s) D_{\rm KL}(\pi_{{\overline{\theta}}}(s) \, || \, \pi_{\theta}(s)).$$ We could define similar versions of projected gradient descent or Frank-Wolfe, which also linearize

<!-- chunk {"id": "body-0045", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

$\ell(\pi)$, but then optimize the resulting local approximation only over parameterized policies.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Policy gradient methods for finite MDPs", "weight": 1.0} -->

Since the class of softmax policies can approximate any stochastic policy to arbitrary precision, this is nearly the same as optimizing over the policy class $\Pi$. Studying $\Pi$ directly makes mathematical analysis easier, because it is closed. For example, it contains an optimal policy, whereas any softmax policy $\pi_{\theta}$ can only come infinitesimally close to an optimal policy. In practice, optimization problems are never solved beyond machine precision, so we don't view the distinction between infimum and minimum to be relevant to the paper's main insights. We caution the reader that our results do not apply to more naive gradient methods that directly linearize $\ell(\pi_{\theta})$ with respect to $\theta$. In that case, a gradient update to $\theta$ may not approximate a policy iteration update, no matter how large the stepsize is chosen to be. In fact, such methods may perform badly due to issues of poor conditioning [kakade2002natural].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

So far, we have described different variants of policy gradient methods for tabular MDPs. For large step-sizes, all these algorithms essentially make a policy iteration update. Hence, intuitively, it is reasonable to expect that their convergence behavior closely resembles that of policy iteration rather than that of gradient descent for smooth objectives. We quantify this precisely in Theorem [thm: tabular rates]below.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Our first result confirms that all of the algorithms we presented in the previous section converge geometrically when step-sizes are set by exact line search on $\ell(\cdot)$. Again, the idea is that a policy gradient step is a policy iteration update for an appropriate choice of stepsize. Our proof effectively uses that exact line search updates make at least as much progress in reducing $\ell(\cdot)$ as a policy iteration update. The mismatch between the policy gradient loss $\ell(\cdot)$, which governs the stepsize choice, and the maximum norm, which governs policy iteration convergence, is the source of the term $\min_{s\in \mathcal{S}} \rho(s)$ in the bound. We further elaborate on this issue in the discussion that follows Theorem [thm: tabular rates].

<!-- chunk {"id": "body-0049", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Our second and third results show that dependence on the initial distribution in the bounds can be avoided by forcing the algorithm to use large stepsizes. A simple result in part (b) applies to the Frank-Wolfe algorithm with a constant stepsize, which gives performance improvement in max norm. This bound follows by essentially making a minor modification to the linear convergence result of policy iteration as reviewed in Section [sec: background]. Recall that we already showed a Frank-Wolfe update to be exactly equivalent to a soft policy iteration update, Given this close connection, a simple argument shows that an $\alpha$-step Frank-Wolfe update offers at least a fraction of the performance improvement offered by a policy iteration update, $$J_{\pi^{t+1}} \preceq (1-\alpha) J_{\pi^t} + \alpha T J_{\pi^t}$$ which implies the result. A comparison between parts (a) and (b) suggest that for $\alpha \geq 1/|\mathcal{S}|$, Frank-Wolfe with exact line search might converge slowly as compared to the constant step-size version in the worst case.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

For softmax policies and exact gradient evaluations, we show in part (c) that NPG with an adaptive step-size sequence converges to an $\epsilon$ optimal policy in $O(\log(1/\epsilon))$ iterations. The error term, $\epsilon$, is inversely related to the step-size and reflects the fact that NPG updates with finite step-sizes only approximately resemble the policy iteration updates More precisely, our proof shows that in this case, the NPG update is equivalent to a soft policy iteration update upto some additive error.. As we take the step-size to infinity, we recover the same result as one would expect for policy iteration. Compared to the first result in part (a) which applies with exact line search, the result in part (c) is useful in the sense that it gives a precise quantification of how large the step-sizes need to be for linear convergence to hold.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

[Geometric convergence]thmgeometricthm Suppose one of the first-order algorithms in Section [sec:algorithms] is applied to minimize $\ell(\pi)$ over $\pi \in \Pi$ with step-size sequence $\{\alpha_t\}_{t\geq0}$. Let $\pi^0$ denote the initial policy and $\{\pi^{t}\}_{t\geq0}$ denote the sequence of iterates. The following bounds apply.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

- Exact line search. If either Frank-Wolfe, projected gradient descent, mirror descent, or NPG is applied with step-sizes chosen by exact line search as in [eq: exact linesearch], then $$\| J_{\pi^t} - J^* \|_{\infty} \leq \Big(1- \min_{s \in \mathcal{S}} \rho(s) (1-\gamma)\Big)^t \frac{\| J_{\pi^0} - J^* \|_{\infty} }{\min_{s \in \mathcal{S}} \rho(s)}.$$ - Constant step-size Frank-Wolfe.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Under Frank-Wolfe with constant step-size $\alpha\in (0,1]$, $$\| J_{\pi^t} - J^* \|_{\infty} \leq (1-\alpha(1-\gamma))^t \| J_{\pi^0} - J^* \|_{\infty}.$$ - Natural policy gradient with softmax policies and adaptive step-size. Fix any $\epsilon>0$. Let $i^*_t = \argmin_{i} Q_{\pi^t}(s,i)$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Suppose that NPG is performed with an adaptive step-size sequence, $$\alpha_t(s) \geq \frac{2}{(1-\gamma) \epsilon} \log(\frac{2}{\pi^t(s,i^*_t)}).$$ $$\norm{J_{\pi^t}-J^*}_{\infty} \leq \left(\frac{1+\gamma}{2} \right)^t \norm{J_{\pi^0}-J^*}_{\infty} + \epsilon.$$ For the result in part (c), note that for the softmax parameterization, $\pi_{\theta}(s,i) > 0$ for any $\theta \in \mathbb{R}^{n \times k}$. So, $\pi^t(s,i^*_t) > 0$ for all $t$. A similar result can also be obtained without the need of adaptive step-sizes by considering entropy regularized MDPs.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Discussion of results: The following discussion is based primarily on feedback of the reviewers. We thank them for their valuable inputs.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

- Dependence on $\rho_{\min}$ for exact line search result: Readers will note that proof of our result in part (a) of Theorem [thm: tabular rates] also shows that, $$\ell(\pi^{t+1}) - \ell(\pi^*) \leq \left(1 - \rho_{\min} (1-\gamma)\right)^t \left[\ell(\pi^0) - \ell(\pi^*) \right].$$ - where $\rho_{\min} = \min_{s \in \mathcal{S}} \rho(s)$. A natural question to ask is whether the presence of the factor of $\rho_{\min}$ in the geometric rate is merely an artifact of our analysis technique and if in practice, line search always ends up picking the policy iteration update corresponding to $\alpha=1$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

In Figure [fig:fw\_grid] above, we plot the line search objective, $$\{\ell(\pi_{\alpha}): \pi_{\alpha} = \alpha \pi + (1-\alpha) \pi_{+}, \, \alpha \in \},$$ - for a Frank-Wolfe update for a randomly generated We generated many random MDPs to compare updates of policy iteration with those of Frank-Wolfe using grid search and found many cases where these differ. Details of only one such example is given to illustrate our point. - MPD with two states and three actions. For a given choice of $(P, g, \rho)$ and policy $\pi$ (see Appendix [appendix\_1] for details), we observe that $\ell(\pi_{\alpha})$ is non-monotonic in $\alpha$ and therefore exact line-search does often select smaller step-sizes as compared to the greedy update $(\alpha=1)$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Although we do not show a lower bound, this example suggests that a factor of $\rho_{\min}$ in the bound here might be unavoidable.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

- Line search objective for a Frank-Wolfe update for a two state three action MDP is non-monotonic with a minimum at $\alpha = 0.83$. Therefore, exact line search picks a smaller step-size than the greedy update, i.e. $\pi_{\alpha^*}\neq\pi_{+}$. - On inexact line search: Though our result in part (a) of Theorem [thm: tabular rates] focuses on an idealized setting with exact line search, we do note that a similar result can also be obtained if we can ensure, say using inexact line search, that the improvement in total cost $\ell(\cdot)$ at every update is at least a fraction of the improvement offered by exact line search.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

For example, if we select a step-size sequence $\{\alpha_t\}_{t \geq 0}$ which offers half the possible improvement at every update, meaning $\ell(\pi^t) - \ell(\pi^{t+1}_{\alpha_t}) \geq (1/2)(\ell(\pi^t) - \inf_{\alpha'} \ell(\pi^{t+1}_{\alpha'}))$, then our result in part (a) follows with an extra factor of $\frac{1}{2}$ in the bound. One essentially needs to modify the first step in the proof (Equation [eq:exact\_vs\_inexact\_linesearch]) and the rest is same.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

A linear convergence result can also be obtained if the sequence of policies, $\{\pi^t\}_{t \geq 0}$, obtained via inexact line search offer approximately the same improvement as a policy iteration update, i.e. $\ell(\pi^{t+1}) \leq \ell(\pi^t_+) + \delta$ holds uniformly for some $\delta>0$. In this case, a bound similar to that in part (a) will hold with an additional scaled bias term of $\delta/(1-\gamma)$. - NPG with softmax policies for regularized MDPs: Recall that the result in part (c) uses an adaptive step-size sequence $\alpha_t(s)$ that depends on $\pi^t(s,i^*_t)$, probability under the randomized policy at iteration $t$ assigned to the action $i^*_t$ prescribed by policy iteration. This dependence is a bit undesirable and can be removed by considering entropy regularized MDPs.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Entropy regularization prevents policies from picking near deterministic actions and essentially lower bounds $\pi^t(s,i^*_t)$. Rather than presenting a lengthy re-derivation of the result in part (c), we sketch a simple argument essentially based on some past work on the theory of regularized MDPs [neu2017unified,geist2019theory], to show linear convergence with a particular choice of step-size. Although this result in Equation [eq:regmdpresult] is almost identical to the one in [cen2020fast], our ideas, based on connections to policy iteration, considerably simplify the proof.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

A common way to enforce regularization is by adding a small penalty to the cost function, $$g^{\lambda}(s,a) = \sum_{i=1}^k \left(g(s,e_i)a_i + \lambda \log(a_i)\right)$$ - for some parameter $\lambda > 0$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

- Similar to [eq:NPGupdateform], a quick calculation using the policy gradient theorem reveals that an NPG update for a $\lambda$-regularized MDP solves the following problem, \argmin_{\bar{\pi} \in \Pi} \, \langle \nabla \ell^{\lambda}(\pi), \bar{\pi} \rangle \, + \frac{1}{\alpha} \sum_{s \in \mathcal{S}} \eta_{\pi}(s) D_{\rm KL}(\bar{\pi}_s || \pi_s) - for any $\alpha \leq 1/\lambda$ with $\langle \nabla \ell^{\lambda}(\pi), \bar{\pi} \rangle = \langle Q^{\lambda}_{\pi} + \lambda \log \pi, \bar{\pi} \rangle_{\eta_{\pi} \times 1}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

For $\alpha = 1/\lambda$, these updates take a particularly simple form of $\pi'(s) = \text{Softmax}\left(\frac{-Q^{\lambda}_{\pi}(s,\cdot)}{\lambda}\right)$. This update can alternatively be viewed as a policy iteration update with respect to a regularized Bellman optimality operator, $T^{\lambda}(\cdot)$ defined: (T^{\lambda} J^{\lambda}_{\pi})(s) = \min_{\bar{\pi} \in \Pi} \,\, \langle Q^{\lambda}_{\pi}(s,\cdot), \bar{\pi}(s) \rangle + \lambda \mathcal{H}(\bar{\pi(s)}). - where $\mathcal{H}(\pi(s))=\sum_{i=1}^k \pi(s,i) \log \pi(s,i)$ is the negative entropy.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Main result: geometric convergence", "weight": 1.0} -->

Importantly, $T^{\lambda}(\cdot)$ can also be shown to be a monotone and $\gamma$-contraction in the maximum norm with a unique fixed point, $J^{*, \lambda}$ such that $\|J^{*,\lambda} - J^*\|_{\infty} \leq \frac{\lambda \log k}{(1-\gamma)}$. See [geist2019theory] for details. Therefore, similar to the proof of policy iteration in Section [sec: background], we can obtain a geometric convergence result for NPG with softmax policies and a constant step-size of $\alpha=1/\lambda$, $$\|J_{\pi^t} - J^*\|_{\infty} \leq \gamma^t \|J_{\pi^0} - J^*\|_{\infty} + \frac{2\lambda \log k}{(1-\gamma)^2}.$$

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we use illuminating connections with policy iteration as shown in [bhandari2019global] to show how many variants of policy gradient algorithms with large step-sizes and exact gradient evaluations converge geometrically fast for tabular MDPs. An interesting question for future work is whether these results can be extended to function approximation settings where the policy class might be restricted, for example in [agarwal2019optimality]. Another interesting question is whether our results hold in settings where unbiased estimates of the value functions are obtained via sampling. Here some exciting progress has been recently made for the undiscounted (average cost setting) in [abbasi2019politex,hao2020provably]for ergodic MDPs, by leveraging connections to approximate policy iteration.
