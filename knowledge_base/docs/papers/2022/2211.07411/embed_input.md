<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Implications of Regret on Stability of Linear Dynamical Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The setting of an agent making decisions under uncertainty and under dynamic constraints is common for the fields of optimal control, reinforcement learning, and recently also for online learning. In the online learning setting, the quality of an agent's decision is often quantified by the concept of regret, comparing the performance of the chosen decisions to the best possible ones in hindsight. While regret is a useful performance measure, when dynamical systems are concerned, it is important to also assess the stability of the closed-loop system for a chosen policy. In this work, we show that for linear state feedback policies and linear systems subject to adversarial disturbances, linear regret implies asymptotic stability in both time-varying and time-invariant settings. Conversely, we also show that bounded input bounded state stability and summability of the state transition matrices imply linear regret.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A number of real-world problems can be cast into the framework of agents making optimal decisions under uncertainty and/or adversarial disturbances. In this setting, the agent has an associated dynamical system and at each timestep suffers an *a priori* unknown cost that depends on its state and input. In the case of perfect knowledge of the dynamics and the future costs, this can be turned into an optimal control problem and solved with one of the plethora of available methods. As is often the case, however, the dynamics, disturbances, and/or future costs are either entirely unknown or only partially known. This is the setting, for example, in reinforcement learning and approximate dynamic programming.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As agents make decisions "on-the-go", there is a need to quantify and compare the performance of various algorithms. Considering a closed-loop system with a given, possibly time-varying policy, one can study its asymptotic stability as an asymptotic metric. Another approach is to look into the problem through the lens of online optimization. An important metric in the literature of the latter is the notion of regret. Given a policy $\mu$, its regret $\mathcal{R}_{T}$, is defined as the difference between its accumulated cost over some time horizon $T$ and that of some benchmark policy $\pi$. It is often desirable to have sublinear growth of $\mathcal{R}_{T}$ with respect to $T$, which will achieve average convergence to the benchmark in the limit.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A special case of the optimal control problem, the linear quadratic regulator (LQR) has been extensively studied in this context. The results in show that the certainty equivalence approach can synthesize stable linear state feedback controllers as long as the model estimate errors are small enough. In the same spirit of certainty equivalence, the algorithms proposed in yield sublinear regret bounds by sequentially solving Riccati equations. The LQR problem with adversarial disturbances has been studied in in the presence of a prediction window, in to quantify the regret of robustness in the sense of $\mathcal{H}_{\infty}$ control, and in a regret-optimal setting in for unconstrained and in for constrained cases. The setting with general convex and differentiable cost functions with adversarial disturbances has been studied for linear time-invariant (LTI) and for linear time-varying (LTV) systems; algorithms that achieve sublinear regret bounds have been proposed for both classes of systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To study and analyze algorithms in both the control theoretic and online learning contexts, one needs to understand the relationship between regret and stability. While most online learning-inspired works seek sublinear regret in pursuit of suboptimality guarantees, it is unclear whether good performance in this aspect also implies stability. Conversely, it is not known what the absence of such guarantees means even for linear dynamical systems. In a recent work, the authors study the interconnection between bounded regret and closed-loop stability for non-linear systems in the absence of noise. In the current work, we consider linear systems subject to process noise and study the relationship between linear regret and stability. Our goal is to develop sufficient conditions under which regret guarantees of an algorithm imply stability of the closed-loop system and vice versa.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we consider generic, time-varying costs, LTV systems subject to adversarial disturbances with LTV state feedback policies, and also LTI systems as a special case. We study the connection between the regret of such policies and their closed-loop stability in the sense of bounded input-bounded state (BIBS) stability with respect to disturbances and asymptotic stability in the absence of disturbances. Under suitable assumptions, we show the following: For LTV systems and LTV state feedback policies linear regret implies asymptotic stability of the closed-loop system. Conversely, BIBS stability and absolute summability of the state transition matrices imply linear regret.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For LTI systems and LTI state feedback policies linear regret is attained if and only if the closed-loop system is asymptotically stable.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

An essential requirement for the results to hold is the "observability" of the state with respect to costs. We provide a counterexample of a notable case where the asymptotic stability implication of linear regret fails to hold when this assumption is violated. A numerical example to showcase the result for the LTI case is provided.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: For a square matrix $A$ the spectral radius and the spectral norm are denoted by $\rho{(A)}$, and $\| A\|$, respectively. For a vector $w \in {\mathbb{R}}^{n}$, $\| w\|$ denotes its Euclidean norm. ${\mathbb{R}}_{+}$ is the set of positive real numbers and $\mathbb{N}$ that of non-negative integers.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

The considered linear state feedback policies are such that the system matrix $F_{t}$ is full rank for all $t \in {\mathbb{N}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

We note that Assumption 2.5.i. is required for performance guarantees of the benchmark policy and corresponds to the stabilizability in the LTI case. Assumption 2.5.ii. excludes chaotic LTV systems in the sense of Li-Yorke and is always satisfied for LTI systems. It can be relaxed, but we introduce it here to keep the discussion simple. Assumption 2.5.iii. is standard in the discrete-time case to avoid deadbeat-type responses that imply a lack of uniqueness of the solutions backward in time.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

Assumption 2.5.iii. leads to the following lemma.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 2.7", "weight": 1.0} -->

(Stage Costs). There exist positive ${\overline{M},\underset{¯}{M}} \in {\mathbb{R}}_{+}$ and ${\overline{s},\underset{¯}{s}} \geq 1$, such that^33^3We consider throughout $\underset{¯}{s} = \overline{s} = 2$ without loss of generality. for all ${x \in {\mathbb{R}}^{n}},{u \in {\mathbb{R}}^{m}}$ and $t \in {\mathbb{N}}$,\The lower bound in the above assumption, which we refer to as the "observability" of the state with respect to cost, excludes cases when unstable states can be "hidden" in the cost. This condition is common in the literature and is also referred to as positive definiteness or detectability of the system with respect to stage costs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Relation to Tracking Problems", "weight": 1.0} -->

For completeness, we also point out a connection between the stability discussion below and tracking problems. Consider the problem of tracking an unknown, bounded, time-varying reference signal $r_{t} \in {\mathbb{R}}^{n}$ given system dynamics, where the agent has access to $r_{t}$ at timestep $t$, but not before. We can then write the state evolution of the tracking error ${\overset{\sim}{x}}_{t}:={x_{t} - r_{t}}$ as where $\nu_{t} \in {\mathbb{R}}^{n}$ can be considered as the disturbance of the modified system; note that $r_{t + 1}$ and $w_{t}$ are unknown at time $t$. If the assumptions above are satisfied the tracking problem can be treated as the regulation under the adversarial noise problem in Section 2.1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section, we derive our main results for LTV and LTI systems. We start with the following motivating example of discounted LQR as a particular case when an unstable system attains linear regret if Assumption 2.7 is violated.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

Consider the dynamics, with $A_{t} = A$, $B_{t} = B$ for all $t \in {\mathbb{N}}$, and the following cost function where $\alpha \in {}$ is a discount factor, $Q \in {\mathbb{R}}^{n \times n}$, $R \in {\mathbb{R}}^{m \times m}$ are positive definite matrices, and $P_{\alpha} \in {\mathbb{R}}^{n \times n}$ satisfies the following equation The above is the discrete algebraic Riccati equation (DARE) for the modified system $({\sqrt{\alpha}A},B)$ with cost matrices $Q$ and $\frac{R}{\alpha}$. The stage costs do not satisfy the condition in Assumption 2.7 as there exists no uniform lower bound.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

Consider now the certainty equivalent controller that minimises the cost assuming ${w_{t} = \mathbf{0}}\mspace{21mu}{{\forall t} \in {\mathbb{N}}}$. The optimal policy $\mu_{t}$ in this setting is then a linear state feedback, given by $\mu_{t} = {- {K_{\alpha}x_{t}}}$, where We make the hypothesis that the value function (cost-to-go) at time step $t$ associated with this policy is given by where $v_{t} \in {\mathbb{R}}^{n}$, $q_{t} \in {\mathbb{R}}$. At timestep $T$, it is easily verified with $v_{T} = \mathbf{0}$, $q_{T} = 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

Assuming the hypothesis is true for $t + 1$, the cost-to-go at $t$ is One can verify that the induction hypothesis is verified only if $P_{\alpha}$ satisfies the DARE for the modified system, and The cost under this linear state feedback policy can then be attained by applying the preceding recursion repeatedly and $F_{\alpha}:={A - {BK_{\alpha}}}$. It is known that for $\alpha$ small enough the closed-loop system matrix $F_{\alpha}$ may in fact be unstable. Consider the set, Then for some $\overline{\alpha} \in \Gamma$, and for $\sigma:={\overline{\alpha}{\| F_{\alpha}\|}}$ It is then evident that there exist ${C_{w},C_{0}} \in {\mathbb{R}}_{+}$, such that Moreover, such $C_{0}$ and $C_{w}$ exist for all costs of the form.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

Hence, for all such ${\{ c_{t}\}}_{t = 0}^{T}$, the regret will also attain the same bound. Thus, while the considered policy achieves linear regret, the closed-loop with the system is unstable.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

This example shows how the violation of Assumption 2.7 can make regret hide the instability of the system.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Linear Time-Varying Systems", "weight": 1.0} -->

The following theorem establishes the regret-stability relation for the time-varying policy ${\mu_{t}{(x_{t})}} = {- {K_{t}x_{t}}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

Note that inferring stability from regret requires not only stabilizability (Assumption 2.5.i.) but also certain conditions on the benchmark. Indeed to guarantee, it is necessary that a stabilizing policy exists in the feasible space of the benchmark. This holds here since the benchmark is the non-causal controller $\mathbf{u}^{\star}$ (dynamic regret), but weaker benchmarks that are constrained to specific policy classes can also be considered (policy regret).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Linear Time-Invariant Systems", "weight": 1.0} -->

In this section, we consider the optimal control problem of minimizing the cost subject to the LTI dynamics where $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$. The following establishes the relation between linear regret and stability in this setting.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

To visualize the necessary and sufficient condition in Theorem 3.4, a simple two-dimensional system with single input is considered. In particular, for $A = {\lbrack 1\quad 1;0\quad 1\rbrack}$ and $B = {\lbrack 1;0.5\rbrack}$, three LTI state feedback controllers are considered, $K_{1} = {\lbrack 0.2\quad 0.4\rbrack}$, $K_{2} = {\lbrack 0\quad 1\rbrack}$, and $K_{3} = {\lbrack{- 0.02}\quad 0.5\rbrack}$. These produce respectively, stable, marginally stable, and unstable closed-loop systems. The cost function is taken to be quadratic with $Q = {\lbrack 1.5\quad 0;0\quad 1.5\rbrack}$ and $R = 1$ as the state and input weighting matrices, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

The disturbance $w_{t}$ for all $0 \leq t < T$ is taken to be the normalized eigenvector of the closed-loop system matrix corresponding to the largest eigenvalue, to approximate the worst-case regret for the given policy. The time-averaged regret for each of the controllers is calculated for a time horizon ranging from $1$ to $100$ and is plotted in a logarithmic scale in Figure 1. Specifically, the average regret of the stable controller can be upper bounded by a constant, that of the marginally stable controller scales with $T$ and for the unstable one with a higher order of $T$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this work, we studied the interconnection of the notion of regret coming from online optimization and the control theoretic concept of stability. Given a linear state feedback policy that attains linear regret, and certain upper and lower bounds on the objective stage costs, we show that the closed-loop system is necessarily asymptotically stable, both for the time-varying and time-invariant cases. The converse result also holds given that the closed-loop system is BIBS stable and has absolute summable norms of its state transition matrices. The results can be used to directly prove the stability of algorithms with regret guarantees and vice versa. This work can be a stepping stone for the consideration of adaptive policies, under which the considered setting is no longer linear; this will allow the analysis of a wider range of online algorithms.
