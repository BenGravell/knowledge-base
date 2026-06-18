<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Optimization to Control: Quasi Policy Iteration

Topics include Convex optimization, Policy iteration, Value iteration, Computational complexity, Optimization, Control, QPI, Adopt the quasi-Newton method, QNM, Markov decision process, Hessian matrix.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent control algorithms for Markov decision processes (MDPs) have been designed using an implicit analogy with well-established optimization algorithms. In this paper, we adopt the quasi-Newton method (QNM) from convex optimization to introduce a novel control algorithm coined as quasi-policy iteration (QPI). In particular, QPI is based on a novel approximation of the ``Hessian'' matrix in the policy iteration algorithm, which exploits two linear structural constraints specific to MDPs and allows for the incorporation of prior information on the transition probability kernel. While the proposed algorithm has the same computational complexity as value iteration, it exhibits an empirical convergence behavior similar to that of QNM with a low sensitivity to the discount factor.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of control, or the decision-making problem as it is also known within the operations research community, has been the subject of much research since the introduction of the Bellman principle of optimality in the late 1950s \[bellman1957markovian\]. In particular, the connection between control algorithms for Markov decision processes (MDPs) and optimization algorithms has been noticed since the late 1970s \[puterman1979convergence\]: Value iteration (VI) \[bellman1957markovian\] can be seen as an instance of gradient descent (GD) algorithm, and policy iteration (PI) \[howard1960dynamic\] is an instance of the Newton method (NM).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recent works have used the relationship mentioned above to develop new control algorithms, with faster convergence and/or lower complexity, inspired by their counterparts for solving optimization problems \[grand2021convex, vieillard2019connections\]. In case of *model-based* (a.k.a. planning, with access to the model of the MDP) algorithms, the combination of the VI algorithm with Polyak momentum \[polyak1964some\], Nesterov acceleration \[nesterov1983method\], and Anderson acceleration \[anderson1965iterative\] have been explored in \[goyal2019first\] and \[zhang2020globally\]. More recently, Halpern anchoring acceleration \[halpern1967fixed\] has been used to introduce the Anchored VI algorithm \[lee2024accelerating\], which in particular exhibits an $\mathcal{O}{({1/k})}$-rate for large values of discount factor and even for $\gamma = 1$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Also of notice is the Generalized Second-Order VI algorithm \[kamanchi2021generalized\] which applies NM on a *smoothed* version of the Bellman operator. For *model-free* (a.k.a. learning, with access to samples from the MDP) algorithms, Speedy Q-Learning \[ghavamzadeh2011speedy\], Momentum Q-Learning \[weng2020momentum\], and Nesterov Stochastic Approximation \[devraj2019matrix\] are among the algorithms that use the idea of momentum for accelerating stochastic GD algorithm \[yang2016unified, kidambi2018insufficiency, liu2018accelerating, allen2017katyusha\] in order to achieve a better rate of convergence compared to standard Q-learning (QL). Moreover, the Zap Q-Learning algorithm \[devraj2017zap\] can be thought of as a second-order learning algorithm which was inspired by the stochastic Newton-Raphson (SNR) algorithm \[ruppert1985newton\].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We note that all of the aforementioned connections have been focused on *finite* state-action MDPs. When it comes to infinite (continuous) state-action spaces, except in special cases such as linear--quadratic regulators (LQR), one needs to resort to finite-dimensional approximation techniques for computational purposes. This approximation may be at the modeling level by aggregation (discretization) of the state and action spaces, which readily falls into the finite state-action MDP setting \[ref:Bert_disc_75, ref:Powell_07\]. Alternatively, one may directly approximate the value function via finite parametrization and minimizing (a proxy of) the residual of its fixed-point characterization based on the Bellman principle of optimality \[ref:Bert_abstract, szepesvari2022algorithms\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Examples of such include linear parameterization \[ref:Bert_temporal, \], or nonlinear parameterization, for instance, neural network architectures \[ref:Bert_neuro-dynamic, SCHMIDHUBER2015, sutton2018reinforcement\] or max-plus approximation \[, GONCALVES2021109623, ref:FDP_TAC, ref:FDP_NeurIPS amin2025fitted\]. We also note that there is an alternative characterization of the original function as the solution to an infinite-dimensional linear program \[ref:HL1\], paving the way for approximation techniques via finite tractable convex optimization \[ref:VanRoy_MP, ref:HL2, ref:Moh_SIOPT\]. With this view of the literature, it is worth noting that one can cast almost all of these approximation techniques as the solution to a finite-dimensional fixed-point or convex optimization problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hessian approximation via structural information: QPI is based on a novel approximation of the "Hessian" matrix in the PI algorithm by exploiting two linear structural constraints specific to MDPs and by allowing for the incorporation of prior information on the transition probability kernel of the MDP (Theorem 3.1. ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")). In the special case of incorporating a uniform prior for the transition kernel, QPI can be viewed as a modification of the standard VI using two novel directions with adaptive step-sizes (Corollary 3.2. ‣ 3.2.1. The prior ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convergence and sensitivity to discount factor: The per-iteration computational complexity of QPI is the same as VI, and its linear convergence can be guaranteed by safeguarding against standard VI (Theorem 3.1. ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) or backtracking (Lemma 3.3. ‣ 3.2.2. Implementation via backtracking ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")). However, in our numerical simulations with random and structured MDPs, QPI exhibits an empirical behavior similar to QNMs with the convergence rate being less sensitive to the discount factor.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Local superlinear convergence: We provide a modified implementation of QPI which also incorporates the secant-type constraints in approximation of the Hessian to guarantee the local superlinear convergence (Theorem 3.4. ‣ 3.2.3. Modified implementation with superlinear convergence ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extension to model-free control (a.k.a. RL): We also introduce the quasi-policy learning (QPL) algorithm, the stochastic version of QPI, as a novel model-free algorithm with guaranteed convergence and the same per-iteration complexity as standard Q-learning (QL) algorithm (Theorem 3.5. ‣ 3.3. Extension to model-free control: QPL algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. In Section, we describe the optimal control problem of MDPs. In Section ‣ From Optimization to Control: Quasi Policy Iteration"), we introduce and analyze the model-based QPI algorithm and its model-free extension, the QPL algorithm. All the technical proofs are provided in Section. The performance of these algorithms is then compared with multiple control algorithms via extensive numerical experiments in Section. Section concludes the paper by providing some final remarks.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations. For a vector $v \in {\mathbb{R}}^{n}$, we use $v{(i)}$ and ${\lbrack v\rbrack}{(i)}$ to denote its $i$-th element. Similarly, $M{(i,j)}$ and ${\lbrack M\rbrack}{(i,j)}$ denote the element in row $i$ and column $j$ of the matrix $M \in {\mathbb{R}}^{m \times n}$. We use $\cdot^{\top}$ to denote the transpose of a vector/matrix. We use $\left. \parallel \cdot \parallel{}_{2} \right.$ and $\left. \parallel \cdot \parallel{}_{\infty} \right.$ to denote the 2-norm and $\infty$-norm of a vector, respectively. We use $\left. \parallel \cdot \parallel{}_{2} \right.$ and $\left.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

\parallel \cdot \parallel{}_{F} \right.$ for the induced 2-norm and the Frobenius norm of a matrix, respectively. Let $x \sim {\mathbb{P}}$ be a random variable with distribution $\mathbb{P}$. We particularly use $\hat{x} \sim {\mathbb{P}}$ to denote *a sample of the random variable $x$* drawn from the distribution $\mathbb{P}$. We use $\mathbf{1}$ and $\mathbf{0}$ to denote the all-one and all-zero vectors, respectively. $I$ and $E = \mathbf{1}\mathbf{1}^{\top}$ denote the identity and all-one matrices, respectively. We denote the $i$-th unit vector by $e_{i}$, that is, the vector with its $i$-th element equal to $1$ and all other elements equal to $0$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimal control of MDPs", "weight": 1.0} -->

A common formulation of the control problem relies on the concept of *Markov decision processes* (MDPs). MDPs are a powerful modeling framework for stochastic environments that can be controlled to minimize some measure of cost. An MDP is a tuple $(\mathcal{S},\mathcal{A},{\mathbb{P}},c,\gamma)$, where $\mathcal{S}$ and $\mathcal{A}$ are the state space and action space, respectively. The transition kernel $\mathbb{P}$ encapsulates the state dynamics: for each triplet ${(s,a,s^{+})} \in {\mathcal{S} \times \mathcal{A} \times \mathcal{S}}$, it gives the probability ${\mathbb{P}}{(\left. s^{+} \middle| {s,a} \right.)}$ of the transition to state $s^{+}$ given that the system is in state $s$ and the chosen control is $a$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimal control of MDPs", "weight": 1.0} -->

The cost function $c:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, bounded from below, represents the cost $c{(s,a)}$ of taking the control action $a$ while the system is in state $s$. The discount factor $\gamma \in {}$ can be seen as a trade-off parameter between short- and long-term costs. *In this study, we consider tabular MDPs with a finite state-action space.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimal control of MDPs", "weight": 1.0} -->

to be the *greedy policy w.r.t. $v$*. Similarly, for a Q-function $q$, define $\pi_{q}:{\mathcal{S}\rightarrow\mathcal{A}}$ by

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimal control of MDPs", "weight": 1.0} -->

to be the *greedy policy w.r.t. $q$*. The problem of interest is to control the MDP optimally, that is, to find the optimal policy $\pi^{\ast}$ with the optimal value/Q-function

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimal control of MDPs", "weight": 1.0} -->

so that the expected, discounted, infinite-horizon cost is minimized. Let us also note that the optimal policy, i.e., the minimizer of the preceding optimization problems, is the greedy policy w.r.t. $v^{\star}$ and $q^{\star}$, that is, $\pi^{\star} = \pi_{v^{\star}} = \pi_{q^{\star}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal control of MDPs", "weight": 1.0} -->

Interestingly, the optimal value/Q-function introduced in can be equivalently characterized as the fixed-point of the corresponding Bellman operators. This fixed-point characterization is the basis for the class of value iteration algorithms. To be precise, we have $v^{\star} = {T{(v^{\star})}}$, i.e.,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal control of MDPs", "weight": 1.0} -->

with ${\hat{s}}^{+} \sim {\mathbb{P}}{( \cdot |s,a)}$ being a *sample* of the next state drawn from the distribution ${\mathbb{P}}{( \cdot |s,a)}$ for the pair $(s,a)$. We note that the expectation in is w.r.t. ${\hat{s}}^{+}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Quasi-Policy Iteration (QPI)", "weight": 1.0} -->

In this section, we develop and analyze the quasi-policy iteration (QPI) algorithm for model-based control problems and its extension, the quasi-policy learning (QPL) algorithm, for model-free control problems.^22^2In this paper, the terminologies of "model-free" and "model-based" indicate the available information (oracle), i.e., whether we have access to the model or only the system trajectory (samples). We note that this is different from the common terminologies in the RL literature where these terms refer to the solution approach, i.e., whether we identify the model along the way (model-based RL) or directly solve the Bellman equation to find the value function (model-free RL). These algorithms, as the name suggests, are inspired by quasi-Newton methods (QNMs) from convex optimization. For this reason, we begin with a brief overview of the connection between optimization and control algorithms, as well as QNMs, to motivate the algorithms developed in this study.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

Two classical algorithms for solving the optimal control problem of MDPs are value iteration (VI) and policy iteration (PI), which are instances of gradient descent (GD) and Newton method (NM), respectively, as we mentioned above. To be precise, consider the unconstrained minimization problem

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

where $f:{{\mathbb{R}}^{\ell}\rightarrow{\mathbb{R}}}$ is twice continuously differentiable and strongly convex, and let ${g{(x)}} = {{\nabla f}{(x)}}$ and ${H{(x)}} = {{\nabla^{2}f}{(x)}}$ be the gradient and Hessian of $f$ evaluated at $x$. Then, by defining ${g{(v)}} ≔ {v - {T{(v)}}}$, one can see that the VI update rule \[bellman1957markovian\]

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

where $\alpha_{k}$ is the step-size. Similarly, by defining ${H{(v)}} ≔ {I - {\gammaP^{\pi_{v}}}}$, the PI update rule \[puterman2014markov, Prop. 6.5.1\]

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

where $\alpha_{k}$ is again the step-size.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

The VI algorithm converges linearly with rate $\gamma$ owing to the fact that the operator $T$ is a $\gamma$-contraction in the $\infty$-norm \[puterman2014markov, Prop. 6.2.4\]. The PI algorithm, on the other hand, outputs the optimal policy in a finite number of iterations \[puterman2014markov, Thm. 6.4.2\]. Moreover, the algorithm has a local *quadratic* rate of convergence when initiated in a small enough neighborhood around the optimal solution \[bertsekas2022lessons, gargiani2022dynamic\]. The faster convergence of PI compared to VI, however, comes with a higher per-iteration computational complexity: The per-iteration complexities of VI and PI are $\mathcal{O}{({n^{2}m})}$ and $\mathcal{O}{({{n^{2}m} + n^{3}})}$, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

The extra $\mathcal{O}{(n^{3})}$ complexity is due to the policy evaluation step, i.e., solving a linear system of equations; see also the matrix inversion in the characterization above. Not surprisingly, we see the same convergence-complexity trade-off between GD and NM. While NM has a better convergence rate compared to GD, it suffers from a higher per-iteration computational cost. GD, with a proper choice of step-size, converges *linearly* \[bubeck2015convex, Thm. 3.12\] with $O{(\ell)}$ per-iteration complexity (disregarding the complexity of gradient oracle). On the other hand, NM, with a proper choice of step-size, has a local *quadratic* convergence rate \[bubeck2015convex, Thm. 5.3\] with $O{(\ell^{3})}$ per-iteration complexity, assuming direct inversion (and disregarding the complexity of gradient and Hessian oracles).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

QNMs are a class of methods that allow for a trade-off between computational complexity and (local) convergence rate. To do so, these methods use a Newton-type update rule

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

where ${\overset{\sim}{H}}_{k}$ is an *approximation* of the true Hessian ${\nabla^{2}f}{(x_{k})}$ at iteration $k$. Different QNMs use different approximations of the Hessian. A generic approximation scheme in QNMs is

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

which minimizes the distance (in Frobenius norm) to a given prior $H_{prior}$ subject to $j$ ($\geq 1$) linear constraints specified by ${r_{i},b_{i}} \in {\mathbb{R}}^{\ell}$. This leads to the approximation ${\overset{\sim}{H}}_{k}$ being a rank-$j$ update of the prior $H_{prior}$, i.e.,

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

where ${R = {(r_{1},\ldots,r_{j})}},{B = {(b_{1},\ldots,b_{j})} \in {\mathbb{R}}^{\ell \times j}}$. Hence, ${\overset{\sim}{H}}_{k}^{- 1}$ can be easily computed based on $H_{prior}^{- 1}$ using the Woodbury formula. Different choices of the prior and the linear constraints in the generic approximation scheme above lead to different QNMs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

For example, by choosing the so-called *secant conditions* with $r_{i} = {x_{{k - i} + 1} - x_{k - i}}$ and $b_{i} = {{{\nabla f}{(x_{{k - i} + 1})}} - {{\nabla f}{(x_{k - i})}}}$ as linear constraints and $H_{prior} = I$ as the prior, we derive Anderson mixing with memory $j$ \[anderson1965iterative\], while by using a single secant condition with $j = 1$ and choosing $H_{prior} = {\overset{\sim}{H}}_{k - 1}$ as the prior, we derive QNM with Broyden approximation \[broyden1965class\].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimization vs. Control", "weight": 1.0} -->

In what follows, we use a similar idea and propose the *quasi-policy iteration (QPI)* algorithm by incorporating a computationally efficient approximation of the "Hessian" $H = {I - {\gammaP}}$ in the PI algorithm. We note that the authors in \[geist2018anderson, zhang2020globally, sun2021damped\] also propose the combination of Anderson mixing with optimal control algorithms. However, the QPI algorithm is fundamentally different in the sense that it approximates the transition matrix $P$ using a different set of constraints that are specific to the optimal control algorithms.

<!-- chunk {"id": "body-0035", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

(Recall that $c^{\pi_{v_{k}}}$ and $P^{\pi_{v_{k}}}$ are the stage cost and the state transition matrix of the greedy policy $\pi_{v_{k}}$ w.r.t. $v_{k}$, respectively.) Recall the PI update rule

<!-- chunk {"id": "body-0036", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

Inspired by the QNM approximation scheme ), we propose the generic QPI update rule

<!-- chunk {"id": "body-0037", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

Observe that instead of approximating the complete Hessian $H_{k} ≔ {({I - {\gammaP_{k}}})}^{- 1}$ similar to standard QNMs, we are only approximating $P_{k}$. This choice particularly allows us to exploit the problem structure in order to form novel constraints and prior as we discuss next.

<!-- chunk {"id": "body-0038", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

Regarding the constraints, the problem structure gives us two linear equality constraints: First, $P_{k}$ is a row stochastic matrix, i.e., we have the *global* structural constraint

<!-- chunk {"id": "body-0039", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

and hence we can set $r_{1} = b_{1} = \mathbf{1}$. Second, we can use the fact that the Bellman operator $T$ is piece-wise affine. In particular, from the definition of the Bellman operator, it follows that ${T{(v)}} = {c^{\pi_{v}} + {\gammaP^{\pi_{v}}v}}$. Thus, we have the *local* structural constraint

<!-- chunk {"id": "body-0040", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

and we can set $r_{2} = v_{k}$ and $b_{2} = {\gamma^{- 1}{({T_{k} - c_{k}})}}$. Note that, unlike the standard secant conditions in QNMs, the constraints ) and ) hold *exactly*. Incorporating these constraints, we propose the approximation

<!-- chunk {"id": "body-0041", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

The update rule ) using the approximation ) is, however, not necessarily a contraction. The same problem also arises in similar algorithms such as Anderson accelerated VI \[zhang2020globally\] and Nesterov accelerated VI \[goyal2019first\]. Here, we follow the standard solution for this problem, that is, safeguarding the QPI update against the standard VI update based on the Bellman error

<!-- chunk {"id": "body-0042", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

To be precise, at each iteration $k = {0,1,\ldots}$, we consider the *safeguarded* QPI update rule as follows

<!-- chunk {"id": "body-0043", "role": "body", "section": "QPI Algorithm", "weight": 1.0} -->

The following theorem summarizes the discussion above by providing the QPI update rule explicitly (see Section 4.1 for the proof).

<!-- chunk {"id": "body-0044", "role": "body", "section": "The prior", "weight": 1.0} -->

Next to be addressed is the choice of $P_{prior}$. First, note that for a fixed prior in all iterations, computation of $\tau_{k}$ and ${\overset{\sim}{P}}_{k}$ in (14b. ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) is not needed since the update (14a. ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) only requires ${\overset{\sim}{G}}_{k}$. The first choice for such a fixed prior is to exploit the available knowledge on the structure of the MDP. For instance, one can set $P_{prior} = P^{\mu}$ with $\mu$ being the stochastic policy choosing actions uniformly at random (so that $P_{prior}$ is the average over actions of and has the same sparsity pattern as the true transition kernel of the MDP).

<!-- chunk {"id": "body-0045", "role": "body", "section": "The prior", "weight": 1.0} -->

A computationally advantageous choice for the prior is the uniform distribution $P_{prior} = {\frac{1}{n}E} = {\frac{1}{n}\mathbf{1}\mathbf{1}^{\top}}$ for which the update rule can be simplified significantly (see Section 4.2

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implementation via backtracking", "weight": 1.0} -->

The QPI update rule (14a. ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) can be alternatively implemented without safeguarding. The proposed alternative again exploits the fact that the VI update leads to contraction in the Bellman error and combines that with the *backtracking* approach from optimization. To be precise, let us rewrite the QPI update rule (14a. ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Implementation via backtracking", "weight": 1.0} -->

and introduce a step-size $\alpha_{k}$ as follows

<!-- chunk {"id": "body-0048", "role": "body", "section": "Implementation via backtracking", "weight": 1.0} -->

Then, at each iteration $k$, we introduce an inner iteration that finds the step-size $\alpha_{k}$ via backtracking such that $\theta_{k + 1} \leq {\gamma^{\prime}\theta_{k}}$ for a chosen $\gamma^{\prime} \in {(\gamma,1)}$. For instance, at each iteration $k$, we can set

<!-- chunk {"id": "body-0049", "role": "body", "section": "Implementation via backtracking", "weight": 1.0} -->

We note that the preceding backtracking scheme is guaranteed to terminate if $v_{k} \neq v^{\star}$ (i.e, $\theta_{k} \neq 0$). Indeed, we have (see Section 4.3

<!-- chunk {"id": "body-0050", "role": "body", "section": "Modified implementation with superlinear convergence", "weight": 1.0} -->

For the proposed QPI scheme to achieve the classic local *superlinear* convergence of the class of QNMs, we need to modify the approximation ) to also include secant-type conditions. To this end, for $k \geq 1$, we consider a modified approximations as follows

<!-- chunk {"id": "body-0051", "role": "body", "section": "Modified implementation with superlinear convergence", "weight": 1.0} -->

with the corresponding gain matrix

<!-- chunk {"id": "body-0052", "role": "body", "section": "Modified implementation with superlinear convergence", "weight": 1.0} -->

Above, the only difference between (18a ‣ From Optimization to Control: Quasi Policy Iteration")) and (18b ‣ From Optimization to Control: Quasi Policy Iteration")) is the omission of the *local structural* constraint in (18b ‣ From Optimization to Control: Quasi Policy Iteration")). We note that the condition $\pi_{v_{k}} = \pi_{v_{k - 1}}$ implies that $v_{k}$ and $v_{k - 1}$ have the same greedy policy and hence lie on the same affine region of the map $T$ (recall that $T$ is piece-wise affine). Therefore, the selection rule is to avoid "constraint collision" between the *local structural* and the *secant* constraints when $\pi_{v_{k}} \neq \pi_{v_{k - 1}}$. Also, observe that in both approximations the prior is the previous approximation ${\overset{\sim}{P}}_{k - 1}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Modified implementation with superlinear convergence", "weight": 1.0} -->

Most importantly, note that the solution ${\overset{\sim}{P}}_{k}$ is a low-rank (rank-three, at most) update of ${\overset{\sim}{P}}_{k - 1}$; c.f. the optimization ) and its solution ). This means that ${\overset{\sim}{G}}_{k}$ can also be computed with a low cost using the Woodbury formula and ${\overset{\sim}{G}}_{k - 1} = {({I - {\gamma{\overset{\sim}{P}}_{k - 1}}})}^{- 1}$. Our next result concerns the convergence of the proposed modified implementation of the QPI algorithm (see Section 4.4

<!-- chunk {"id": "body-0054", "role": "body", "section": "Other constraints", "weight": 1.0} -->

We finish this section with the following remark. One can also add extra constraints to the minimization problem ) to impose a particular structure on the approximate transition matrix ${\overset{\sim}{P}}_{k}$. For instance, a natural constraint is to require this matrix to be entry-wise non-negative so that ${\overset{\sim}{P}}_{k}$ is indeed a probability transition matrix; or, one can impose a sparsity pattern on ${\overset{\sim}{P}}_{k}$ using the existing knowledge on the structure of the MDP. However, incorporating such information may lead to the problem ) not having a closed-form and/or low-rank solution, and hence undermining the computational efficiency of the proposed algorithm. In this regard, we note that the problem ) has a closed-form solution which is a rank-one update of the prior; see ${\overset{\sim}{P}}_{k}$ in (14b. ‣ 3.2. QPI Algorithm ‣ 3.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Other constraints", "weight": 1.0} -->

Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

We now introduce the quasi-policy learning (QPL) algorithm as the extension of QPI for model-free control problems with access to samples through a generative model. For simplicity, we limit the following discussion to the extension of the QPI algorithm (. ‣ 3.2.1. The prior ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) with a uniform prior. However, we note that the extension can be similarly applied to the QPI algorithm (. ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) with the generic prior.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

The basic idea is to implement the stochastic version of the QPI update rule *for the Q-function* using the samples. In particular, similar to the approximation ), we use an approximation of the state-action transition matrix under the greedy policy w.r.t. the Q-function $q_{k}$ at each iteration $k$. However, the *local* structural constraint is in this case formed based on the *sampled* Bellman operator $\hat{T}{( \cdot )}$, evaluated at the sampled next states ${\hat{s}}_{k}^{+}$ at iteration $k$, as a surrogate for the Bellman operator $T{( \cdot )}$. To be precise, let

<!-- chunk {"id": "body-0058", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

at each iteration $k$. Also, let $c \in {\mathbb{R}}^{nm}$ be the vector of stage cost (with the same state-action ordering as the Q-function $q_{k} \in {\mathbb{R}}^{nm}$). We note that since the proposed QPL algorithm is synchronous with one sample for each state-action pair in each iteration, we have access to the complete stage cost $c$ after the first iteration and can treat it as an input to the algorithm. The approximate state-action transition matrix ${\overset{\sim}{P}}_{k}$ at each iteration $k$ is then formed as follows

<!-- chunk {"id": "body-0059", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

The minimization problem above also has a closed-form solution as a rank-one update of the prior, which allows us to compute ${\overset{\sim}{G}}_{k} = {({I - {\gamma{\overset{\sim}{P}}_{k}}})}^{- 1}$ efficiently using Woodbury formula. Having ${\overset{\sim}{G}}_{k}$ at hand, we can consider the update rule

<!-- chunk {"id": "body-0060", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

where $\alpha_{k}$ is the diminishing learning rate of the algorithm, e.g., $\alpha_{k} = {1/{({k + 1})}}$. However, similar to the model-based case, the update rule ) is not convergent. To address this issue, we consider a convex combination of the update rule ) with the "standard" synchronous Q-learning (QL) update rule^33^3This is the so-called *synchronous* update of the Q-function in *all* state-action pairs in each iteration, corresponding to the *parallel sampling model* introduced by \[kearns1998finite\]. \[watkins1992q, kearns1998finite\]

<!-- chunk {"id": "body-0061", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

with a diminishing effect. That is, we consider the update rule

<!-- chunk {"id": "body-0062", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

We note that the bound $M$ is chosen using the fact that for any row stochastic matrix $P$ and $G = {({1 - {\gammaP}})}^{- 1}$, we have

<!-- chunk {"id": "body-0063", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

and the generic bound $\left\| q^{\pi} \right\|_{\infty} \leq {\left\| c \right\|_{\infty}/{({1 - \gamma})}}$ for the value $q^{\pi}$ of any policy $\pi$. The update rule of the model-free QPL algorithm in its generic form is hence

<!-- chunk {"id": "body-0064", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

In particular, by using the uniform prior $P_{prior} = {\frac{1}{nm}E}$, the QPL update rule reduces to

<!-- chunk {"id": "body-0065", "role": "body", "section": "Extension to model-free control: QPL algorithm", "weight": 1.0} -->

Observe that in this case QPL uses the two additional vectors $c - {\hat{T}}_{k}$ and the all-one vector $\mathbf{1}$ with adaptive coefficients in its update rule. The following theorem summarizes properties of the proposed QPL algorithm (see Section 4.5 for the proof).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 3.6 (Asynchronous QPL)", "weight": 1.0} -->

The proposed QPL update rule ) can also be implemented in an asynchronous fashion. To be precise, this requires forming the approximate state-action transition matrix ${\overset{\sim}{P}}_{k}$ based on a single sample $(s_{k},a_{k},{\hat{s}}_{k}^{+},{c{(s_{k},a_{k})}})$ as follows

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 3.6 (Asynchronous QPL)", "weight": 1.0} -->

Cf. approximation ). In particular, by using the uniform prior $P_{prior} = {\frac{1}{nm}E}$, the corresponding update rule reads as

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 3.6 (Asynchronous QPL)", "weight": 1.0} -->

where the scalar coefficients are given by

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 3.6 (Asynchronous QPL)", "weight": 1.0} -->

Note that the preceding update rule leads to an update in all entries of the Q-function $q_{k}$ in each iteration.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Simulations", "weight": 1.0} -->

We now compare the performance of the proposed algorithms with that of the standard existing algorithms for the optimal control of different MDPs. See Appendix A for a description of the considered MDPs. To this end, we first focus on the proposed algorithms with uniform priors corresponding to update rules (. ‣ 3.2.1. The prior ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) and ) in Sections 5.1 and 5.2, respectively. The results of numerical experiments with alternative priors are then reported in Section 5.3.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

For model-based algorithms we consider two MDPs: a randomly generated Garnet MDP \[archibald1995generation\] and the Healthcare MDP \[goyal2019first\] with an *absorbing* state. The proposed QPI algorithm (. ‣ 3.2.1. The prior ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")) is compared with the following algorithms: VI (value iteration); NVI (VI with Nesterov acceleration) \[goyal2019first\]; AVI (VI with Anderson acceleration) \[geist2018anderson\]; and, PI (policy iteration). For AVI, we use a memory of one leading to a rank-one update (of the identity matrix) for approximating the Hessian so that it is comparable with the rank-one update of the uniform distribution for approximating the transition matrix in QPI. See Appendix B for the exact update rules of NVI and AVI.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

We note that since NVI and AVI are not guaranteed to converge, we safeguard them using VI (using the same safeguarding rule ) used for QPI). All the algorithms are initialized by $v_{0} = \mathbf{0}$ with termination condition $\left\| {v_{k} - {T{(v_{k})}}} \right\|_{\infty} \leq 10^{- 6}$. The results of the simulations are provided in Figures and.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Model-based algorithms", "weight": 1.0} -->

In Figure, VI, NVI, and AVI show a linear convergence with a rate depending on $\gamma$ in both MDPs. In particular, as we increase $\gamma$ from $0.9$ to $0.999$, we observe more than a tenfold increase in the number of iterations required for these algorithms to terminate. This is expected since these algorithms only use first-order information and their convergence rate is determined by $\gamma$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

For model-free algorithms we also consider two MDPs: again a randomly generated Garnet MDP \[archibald1995generation\] and the Graph MDP \[devraj2017zap\]. The proposed QPL algorithm ) with $\alpha_{k} = \frac{1}{({k + 1})}$ and $\beta_{k} = \frac{1}{{({k + 1})}^{0.1}}$ is compared with the following algorithms: QL (Q-learning) as in ) with $\alpha_{k} = \frac{1}{({k + 1})}$; SQL (speedy QL) \[ghavamzadeh2011speedy\]; and, ZQL (zap QL) \[devraj2017zap\]. See Appendix B for the exact update rules of SQL and ZQL.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

All the algorithms are initialized by $q_{0} = \mathbf{0}_{nm}$ and terminated after $K = 10^{4}$ iterations with a synchronous sampling of all state-action pairs at each iteration. For each algorithm, we report the *average* of the Bellman error $\left\| {q_{k} - {T{(q_{k})}}} \right\|_{\infty}$ over 20 runs of the algorithm. The results of the simulations are provided in Figure and Table.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

Table 1. The running time (in seconds) of the model-free algorithms over K = 104 iterations (averaged over 20 runs) for γ = 0.9 corresponding to Figure 3.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

As can be seen in Figures 3(a) and 3(b), the performance of QL and SQL (the first-order methods) deteriorates as $\gamma$ increases for both MDPs. However, for these MDPs, ZQL (the second-order method that estimates the transition matrix by averaging over the samples) leads to almost the same error level after a fixed number of iterations for different values of $\gamma$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Model-free algorithms", "weight": 1.0} -->

Finally, we note that the running times reported in Table also align with the corresponding theoretical time complexities of these algorithms. In particular, QPL and SQL require almost the same amount of time, which is slightly more than QL and less than ZQL. (We report the runtime only for $\gamma = 0.9$ because it is independent of $\gamma$). Note that the time required for generating the samples is reported separately in Table, which is indeed the dominating factor in the actual runtime of the model-free algorithms.

<!-- chunk {"id": "body-0079", "role": "body", "section": "QPI and QPL with different priors", "weight": 1.0} -->

Figures and report the result of our numerical simulations for the QPI and QPL algorithms, respectively, with the three choices of the prior: (i) QPI/L-A with a uniform prior $P_{prior} \propto \mathbf{1}\mathbf{1}^{\top}$, (ii) QPI/L-B with recursive prior $P_{prior} = {\overset{\sim}{P}}_{k - 1}$, and (iii) QPI/L-$\mu$ with prior $P_{prior} = P^{\mu}$ and $\mu$ being the stochastic policy choosing actions uniformly at random so that the prior has the same sparsity pattern as the true transition probability matrix.

<!-- chunk {"id": "body-0080", "role": "body", "section": "QPI and QPL with different priors", "weight": 1.0} -->

As depicted in Figures 4(a) and 5(a), the experiments with alternative priors shows no improvement in the performance of the QPI and QPL algorithms in comparison with the uniform prior for random Garnet MDPs. For structured MDPs, however, we observe contradictory results as shown in Figures 4(b) and 5(b): Using a structured prior leads to a significant improvement in the performance of the (model-based) QPI algorithm for Healthcare MDP, while using a structured prior significantly deteriorates the performance of the (model-free) QPL algorithm for Graph MDP.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Limitations and Future Research", "weight": 1.5} -->

In this paper, we proposed the model-based quasi-policy iteration (QPI) algorithm and its model-free counterpart, the quasi-policy learning (QPL) algorithm. The proposed algorithms were particularly inspired by the quasi-Newton methods and employed a novel approximation of the "Hessian" by using two new linear constraints specific to MDPs.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Limitations and Future Research", "weight": 1.5} -->

The main drawback of the proposed algorithms, similar to other accelerated VI schemes in the literature, is the need for safeguarding to ensure convergence. Our experiments in Section showed examples of MDPs in which the safeguard is activated. Our modified implementation of Section 3.2.2 ‣ From Optimization to Control: Quasi Policy Iteration") guarantees the linear convergence while removing the need for safeguarding and using backtracking instead. Another possible solution is the use of the operator splitting method introduced in \[NEURIPS2022_fa809df3\] for policy evaluation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Limitations and Future Research", "weight": 1.5} -->

1\], which is difficult to achieve for a low-rank approximation ${\overset{\sim}{P}}_{k}$ of $P_{k}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Limitations and Future Research", "weight": 1.5} -->

Another limitation of the current work is the lack of a theoretical guarantee for the empirically observed improvement in the convergence rate, particularly for the model-based QPI algorithm. The main difficulty to be addressed is the fact that the linear constraints in ) are not the standard secant conditions used in QNMs. The modified implementation of Section 3.2.3 ‣ From Optimization to Control: Quasi Policy Iteration") partially addresses this issue by including the secant conditions in its approximation. An interesting result, however, is the establishment of a local superlinear convergence rate for QPI without imposing the secant condition. Another possibility is to use the results for Anderson acceleration in \[Evans2020\] to establish an improved linear rate for convergence. To that end, similar to what is done in \[sun2021damped\], one needs to use a smoothed version of the Bellman operator, e.g., by replacing the *max* operation with a *soft-max* operation in the Bellman operator.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Limitations and Future Research", "weight": 1.5} -->

The proposed algorithms in this study heavily rely on the approximation ) of the transition matrix. As we discussed, this approximation easily allows for incorporation of different priors, e.g., a prior with the same sparsity pattern as the true transition matrix, or, the recursive prior. However, our numerical simulations using these alternative priors did not demonstrate a clear improvement in the performance of the proposed algorithms, highlighting the need for further investigation on other MDPs. In this regard, we also note that the main drawback of the approximation ) is that it does not allow for a computationally efficient incorporation of other constraints, such as non-negativity constraints. A promising future research direction is the development of alternative approximation schemes that allow such constraints to be included at a reasonable computational cost.
