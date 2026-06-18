<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-Constrained Linear-Quadratic Regulators

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new risk-constrained reformulation of the standard Linear Quadratic Regulator (LQR) problem. Our framework is motivated by the fact that the classical (risk-neutral) LQR controller, although optimal in expectation, might be ineffective under relatively infrequent, yet statistically significant (risky) events. To effectively trade between average and extreme event performance, we introduce a new risk constraint, which explicitly restricts the total expected predictive variance of the state penalty by a user-prescribed level. We show that, under rather minimal conditions on the process noise (i.e., finite fourth-order moments), the optimal risk-aware controller can be evaluated explicitly and in closed form. In fact, it is affine relative to the state, and is always internally stable regardless of parameter tuning. Our new risk-aware controller: i) pushes the state away from directions where the noise exhibits heavy tails, by exploiting the third-order moment (skewness) of the noise; ii) inflates the state penalty in riskier directions, where both the noise covariance and the state penalty are simultaneously large. The properties of the proposed risk-aware LQR framework are also illustrated via indicative numerical examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Achieving good performance in expectation is often insufficient in the design of stochastic control systems, especially when dealing with modern, critical applications. Examples appear naturally in many areas, including wireless industrial control, energy, finance, robotics, networking, and safety, to name a few. Indeed, occurrence of less probable, non-typical or unexpected events might lead the underlying dynamical system to experience shocks with possibly catastrophic consequences, e.g., a drone diverging too much from a given trajectory in a hostile environment, or an autonomous vehicle crashing onto a wall or hitting a pedestrian. In such situations, design of effective *risk-aware* control policies is highly desirable, systematically compensating for those extreme events, at the cost of slightly sacrificing average performance under nominal conditions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

To highlight the usefulness of a risk-aware control policy, let us consider the following simple, motivating example. Let $x_{k + 1} = {x_{k} + u_{k} + w_{k + 1}}$ model an aerial robot, moving along a line. Assume that the process noise $w_{k}$ is i.i.d. Bernoulli, taking the values $\beta > 2$ with probability $1/\beta$ and $0$ with probability $1 - {1/\beta}$. This noise represents shocks, e.g., wind gusts, that can occur with some small probability. We would then like to minimize the LQR cost ${\mathbb{E}}{\sum_{t = 0}^{N}{\{ x_{t}^{2}\}}}$, i.e., the total displacement of the robot over a horizon of $N$ time steps.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this case, the LQR optimal controller is $u_{k}^{LQR} = {{- x_{k}} - 1}$, where ${- 1} \equiv {- {{\mathbb{E}}w_{k}}}$ cancels the mean of the process noise. We see that the LQR solution is risk-neutral, as it does not account for the fact that the shock $\beta$ could be arbitrarily large. On the other hand, the risk-aware LQR formulation proposed in this work results in a family of optimal controllers of the form

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\mu$ controls the trade-off between average performance and risk. As $\mu$ increases, we move from the risk-neutral to the maximally risk-aware controller ${u_{t}^{\ast}{(\infty)}} = {{- x_{t}} - {\beta/2}}$, which treats the noise as adversarial---see Fig. 1.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In both classical and recent literature in linear-quadratic problems, risk awareness in estimation and control is typically achieved by replacing the respective random cost with its exponentiation. Yet, the resulting stochastic control problem might not be well-defined for general classes of noise distributions, as it requires the moment generating function of the cost to be finite. Thus, heavy-tailed or skewed distributions, which are precisely those exhibiting high risk, are naturally excluded. Also, even if the expectation of the exponential cost is finite, it does not lead to a general, closed-form and interpretable solution. A notable exception is that of a Gaussian process noise, also known as the Linear Exponential Quadratic Gaussian (LEQG) problem, which does enjoy a simple closed-form solution. Apparently though, the Gaussian assumption is unable to capture distributions with asymmetric (skewed) structure, as in the above example.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a new risk-aware reformulation of the LQR problem, in which the standard LQR objective is minimized subject to an explicit and tunable risk constraint. Our contributions are as follows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

--New Risk Measure. We introduce the cumulative expected one-step predictive variance of the associated state penalty as a new risk measure for LQR control. In this way, our risk-constraint formulation ensures not only a small LQR cost, but also guaranteed statistical variability of the state penalty.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Optimal Risk-Aware Controls & Stability. We show that our new risk-constrained formulation results in a quadratically constrained LQR problem (Proposition 1. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")), which admits an explicit closed-form solution with a natural interpretation. The optimal risk-aware feedback controller is affine with respect to the system state (Theorems 2. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators") & 3. ‣ III-C Recovery of Primal-Optimal Solutions ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")). The affine component of the control law pushes the state away from directions where the noise exhibits (skewed) heavy tails. Meanwhile, the state feedback gain satisfies a new risk-aware Riccati recursion, in which the state penalty is inflated in riskier directions, where both the noise covariance and state penalty are simultaneously larger.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Further, we show that our optimal risk-aware controller is always stable, under standard LQR conditions (Corollary 1. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Arbitrary Noise Model. Contrary to the LEQG approach, our results are valid for arbitrary noise distributions, provided the associated fourth-order moments are finite; thus, heavy-tailed or skewed noises are supported within our framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Relation to LQR with Tracking. We show that, by appropriate re-parameterization, our risk-aware LQR problem is equivalent to a generalized risk-neutral LQR problem with a tracking objective. Essentially, this implies that risk-neutral LQR formulations can provide inherent risk-averse behavior, as long as the involved parameters are selected in a principled way, as presented herein.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work: Risk-aware optimization has been studied in a wide variety of decision making contexts. The basic idea is to replace expectations by more general functionals, called risk measures, purposed to effectively quantify the statistical volatility of the involved random cost function, in addition to mean performance. Typical examples are mean-variance functionals, mean-semideviations, and Conditional Value-at-Risk (CVaR).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the case of control systems, apart form the aforementioned exponential approach, CVaR optimization techniques have also been considered for risk-aware constraint satisfaction. Although CVaR captures variability and tail events well, CVaR optimization problems rarely enjoy closed-form expressions. Approximations are usually required to make computations tractable, e.g., process noise and controls are assumed to be finite-valued, thus excluding the LQR setting. Predictive variance constraints have also been used as a measure of risk in portfolio optimization. Different from our paper, the noise is assumed to be Gaussian and the variance is with respect to linear stage costs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another related concept is that of robust control, where the system model is unknown. The objective is to optimally control the true system under worst case model uncertainty. When there is no model uncertainty, in the case of stochastic process noise, robust controllers usually reduce to their risk-neutral LQR counterparts. On the contrary, in risk-aware control, extreme noise events are part of the system model. Even if the system is exactly modeled, we would still need to consider risk-aware control if the process noise is heavy-tailed or highly variable. From this point of view, robustness and risk are orthogonal concepts. Interestingly, in the case of adversarial noise, there is a connection between robust and maximally risk-aware controllers.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: The transpose operation is denoted by ${( \cdot )}^{\prime}$. If $x_{k},\ldots,x_{t}$ is a sequence of vectors, then $x_{k:t}$ denotes the batch vector of all $x_{i}$ for $k \leq i \leq t$. The $\sigma$-algebra generated by a random vector $x$ is denoted by $\sigma{(x)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Risk-Constrained LQR Formulation", "weight": 1.0} -->

Consider a discrete-time linear system in state-space form evolving according to the stochastic difference equation

<!-- chunk {"id": "body-0019", "role": "body", "section": "Risk-Constrained LQR Formulation", "weight": 1.0} -->

where $x_{t} \in {\mathbb{R}}^{n}$ is the state, $u_{t} \in {\mathbb{R}}^{p}$ is an exogenous control signal, $A$ is the state transition matrix, and $B$ is the input matrix. We assume that the initial value $x_{0}$ is deterministic and fixed. Signal $w_{t} \in {\mathbb{R}}^{n}$ is a random process noise (not necessarily Gaussian) and is assumed to be i.i.d. For $t \geq 0$, let $\mathcal{F}_{t} = {\sigma\left( x_{0:t},u_{0:t} \right)}$ be the $\sigma$-algebra generated by all observables up to time $t$, and let $\mathcal{F}_{- 1}$ be the trivial $\sigma$-algebra.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Risk-Constrained LQR Formulation", "weight": 1.0} -->

Based on this notation, $x_{t},u_{t},w_{t}$ are $\mathcal{F}_{t}$-measurable, while $w_{t + 1}$ is independent of $\mathcal{F}_{t}$. We also make an additional assumption on the process noise, as follows.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1 (Noise Regularity)", "weight": 1.0} -->

The above condition is mild and satisfied by very general noise distributions, including many heavy-tailed ones. Denote the mean of the noise by $\overline{w} \triangleq {{\mathbb{E}}w_{k}}$ and its variance by $W \triangleq {{\mathbb{E}}{({w_{k} - \overline{w}})}{({w_{k} - \overline{w}})}^{\prime}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1 (Noise Regularity)", "weight": 1.0} -->

In the classical risk-neutral formulation of the LQR problem, one is interested in the multistage stochastic program

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1 (Noise Regularity)", "weight": 1.0} -->

where $u = u_{0:{N - 1}}$ are the inputs from time $0$ up to time $N - 1$, for some horizon $N \in {\mathbb{N}}$. For each $t$, the causality constraint on $u_{t}$ restricts the inputs to the space of square-integrable $\mathcal{F}_{t}$-measurable vector-valued random elements of appropriate dimension, denoted as $\mathcal{L}_{2}{(\mathcal{F}_{t})}$. It also guarantees that the optimization problem is well-defined and with finite cost. In order for the optimal LQR controller to be well-behaved and stable as the horizon $N$ grows, we also make the following standard assumption.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2 (LQR)", "weight": 1.0} -->

The pair $(A,B)$ is stabilizable, the pair $(A,Q^{1/2})$ is detectable, matrix $Q \succeq 0$ is positive semi-definite and matrix $R \succ 0$ is positive definite.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2 (LQR)", "weight": 1.0} -->

As mentioned above, the classical LQR problem is risk-neutral, since it optimizes performance only on average. Still, even if the average performance is good, the state can grow arbitrarily large under less probable, yet extreme events. In other words, the state can exhibit large variability. To deal with this issue, we propose a risk-constrained formulation of the LQR problem, posed as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2 (LQR)", "weight": 1.0} -->

Here, the risk measure adopted is the cumulative expected predictive variance of the state cost. The predictive variance incorporates information about the tail and skewness of the penalty $x_{t}^{\prime}Qx_{t}$. This forces the controller to take higher-order noise statistics into account, mitigating the effect of rare though large noise values. Hence, our risk-aware LQR formulation not only forces the state $x_{t}$ to be close to zero, but also explicitly restricts its variability.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2 (LQR)", "weight": 1.0} -->

Problem offers a simple and interpretable way to control the trade-off between average performance and risk. By simply decreasing $\epsilon$, we increase risk-awareness. Inspired by standard risk-aware formulations, in the above optimization problem our risk definition is tied to the specific state penalty $x_{t}^{\prime}Qx_{t}$ of the LQR. However, all of our results are still valid if we employ the predictive variance of a different quadratic form, e.g., the norm of the state, $\left\| x_{t} \right\|^{2}$, in the constraint---see Section V. Lastly, note that the initial state is fixed (for simplicity), so there is no associated risk term for $t = 0$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2 (LQR)", "weight": 1.0} -->

In the next section, we show that the risk constraint of can be rewritten in quadratic form. This will allow us to solve problem using duality theory and obtain a closed-form solution, exploiting higher-order noise moments.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimal Risk-Aware LQR Controllers", "weight": 1.0} -->

The analysis of the risk-aware dynamic program consists of the following steps. First, we ensure the well-definiteness of, also showing that can be equivalently reexpressed as a sequential variational Quadratically Contrained Quadratic Program (QCQP), or, more precisely, as a Quadratically Constrained LQR (QC-LQR) problem (Proposition 1. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")). Then, we exploit Lagrangian duality (Theorem 1. ‣ III-A Lagrangian Duality ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")) to solve exactly and in closed form. More specifically, we first derive an explicit expression for the optimal risk-aware controller (Theorem 2. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")), given an arbitrary but fixed Lagrange multiplier. Then, we show how an optimal Lagrange multiplier may be efficiently discovered via trivial bisection (Theorem 3.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimal Risk-Aware LQR Controllers", "weight": 1.0} -->

‣ III-C Recovery of Primal-Optimal Solutions ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators") and Proposition 2. ‣ III-C Recovery of Primal-Optimal Solutions ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")).

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Lagrangian Duality", "weight": 1.0} -->

To tackle problem, we now consider the variational Lagrangian $\mathcal{L}_{}:{{{{{\mathcal{L}_{2}{(\mathcal{F}_{0})}} \times \cdots \times \mathcal{L}_{2}}{(\mathcal{F}_{N - 1})}} \times {\mathbb{R}}_{+}}\rightarrow{\mathbb{R}}}$ of the sequential QCQP (4. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")), defined as

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Lagrangian Duality", "weight": 1.0} -->

where $\mu \in {\mathbb{R}}_{+}$ is a multiplier associated with the variational risk constraint of (4. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")). Hereafter, problem (4. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")) will be called the primal problem. Accordingly, the dual function $D:{{\mathbb{R}}_{+}\rightarrow{\lbrack{- \infty},\infty)}}$ is additionally defined as

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Lagrangian Duality", "weight": 1.0} -->

where the implicit feasible set $\mathcal{U}_{0}$ obeys ($k \leq {N - 1}$)

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Lagrangian Duality", "weight": 1.0} -->

and contains the constraints of (4. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")) that have not been dualized in the construction of the Lagrangian. Note that it is always the case that $D \leq J^{\ast}$ on ${\mathbb{R}}_{+}$, where $J^{\ast} \in {\lbrack 0,\infty\rbrack}$ denotes the optimal value of the primal problem (4. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")). Then, the optimal value of the always concave dual problem

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Lagrangian Duality", "weight": 1.0} -->

Leveraging Lagrangian duality, we may now state the following result, which provides sufficient optimality conditions for the QCQP (4. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")). The proof is omitted, as it follows as direct application of \[39, Theorem 4.10\].

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Optimal Risk-Aware Control Policies", "weight": 1.0} -->

Let $\mu \geq 0$ be arbitrary but fixed. First, we may simplify the form of the Lagrangian $\mathcal{L}_{}$ and express it within a canonical dynamic programming framework. In this respect, we have the following, almost obvious, but important result.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1 (Relation to generalized LQR with tracking)", "weight": 1.0} -->

The Lagrangian (8. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")) has the structure of a generalized LQR problem with a tracking objective. By completing the squares we can rewrite the stage cost $g_{t}{(x_{t},u_{t},\mu)}$ as

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 1 (Relation to generalized LQR with tracking)", "weight": 1.0} -->

i.e., the state penalty is quadratic and consists of two distinct terms. The first one, i.e., ${({x_{t} + {2\muM_{3}}})}^{\prime}Q{({x_{t} + {2\muM_{3}}})}$ is a tracking error term that forces the state to be close to the static target $- {2\muM_{3}}$. Informally, in the case of skewed noise, by tracking $- {2\muM_{3}}$ we pre-compensate for directions in which the distribution of the noise has heavy tails. This decreases the statistical variability of the predicted stage cost. The second term, $x_{t}^{\prime}{({4\muQWQ})}x_{t}$, is a standard quadratic penalty term; notice that, contrary to the risk-neutral case, the covariance of the noise $W$ now affects the penalty term.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 1 (Relation to generalized LQR with tracking)", "weight": 1.0} -->

Informally, this term penalizes state directions which not only lead to high cost but are also more sensitive to noise, as captured by the product $QWQ$. Hence, the risk-neutral LQR framework can exhibit inherent risk-averse properties, provided that its parameters are selected in a principled way. Of course, selecting those parameters *a priori* is not trivial.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 1 (Relation to generalized LQR with tracking)", "weight": 1.0} -->

The structure of the Lagrangian as suggested by Lemma 1. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators") enables us to derive both a closed-form expression for its minimum and an explicit optimal control policy. To this end, define the optimal cost-to-go at stage $k \leq {N - 1}$ as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 1 (Relation to generalized LQR with tracking)", "weight": 1.0} -->

where we omit the constant components of the Lagrangian. Under this definition, it is true that

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 1 (Relation to generalized LQR with tracking)", "weight": 1.0} -->

We may now derive the complete solution to, which is one of the main results of this paper, and provides optimal risk-aware control policies for every fixed multiplier $\mu \geq 0$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Recovery of Primal-Optimal Solutions", "weight": 1.0} -->

From Theorem 2. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators"), we know how to compute the relaxed optimal input $u^{\ast}{(\mu)}$, for any given multiplier $\mu \geq 0$. But the risk constraint of the primal problem (4. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")) is the only one that has been dualized in the construction of the Lagrangian. Then, it turns out that we can also compute an optimal multiplier $\mu^{\ast}$ via bisection, thus providing a complete solution to the primal problem.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C Recovery of Primal-Optimal Solutions", "weight": 1.0} -->

We exploit the fact that, under the relaxed optimal policy $u^{\ast}{( \cdot )}$, both the LQR cost $J{({u^{\ast}{( \cdot )}})}$ and the risk functional $J_{R}{({u^{\ast}{( \cdot )}})}$ are monotone functions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

Consider a flying robot that moves on a horizontal plane, i.e., the Euclidean space ${\mathbb{R}}^{2}$. We assume that its linearized dynamics can be abstracted by a double integrator as

<!-- chunk {"id": "body-0046", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

where $T_{s} = 0.5$ is the sampling time, $x_{k,1}$, $x_{k,3}$ are the position coordinates, $x_{k,2}$, $x_{k,4}$ the respective velocities and $v_{k}$ is the acceleration input. Let $d_{k}$ be a wind disturbance force that acts on the robot, which is modeled as follows: We assume that $d_{k,1}$ constitutes the dominant wind direction with non-zero mean and large variability, while the orthogonal direction $d_{k,2}$ is a weak wind direction with zero mean and small variability. We model $d_{k,1}$ as a mixture of two gaussians $\mathcal{N}{}$, $\mathcal{N}{}$ with weights $0.8$ and $0.2$, respectively. This bimodal distribution models the presence of infrequent but large wind gusts.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

Consider now the LQR problem with parameters

<!-- chunk {"id": "body-0048", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

and a horizon of length $N = 5000$. We primarily compare our risk-aware LQR formulation with the classical, risk-neutral LQR via simulations. To tune our controller, we vary $\mu$ in (17. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")) directly instead of varying $\epsilon$. We also (heuristically) compare our controller with the exponential (LEQG) method, even though the noise is not Gaussian, by plugging in the second order statistics $W$. Let the tuning parameter of LEQG be $\theta$. Note that the exponential problem is well defined only if $\theta < 0.001276$ (roughly), where the "neurotic breakdown" occurs. For the purpose of comparison, we simulate all schemes under the same noise sequence $w_{0:N}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

In Fig. 2, we see the evolution of the state penalty terms $x_{k}^{\prime}Qx_{k}$, for the first $50$ time steps, under the different control schemes. By slightly sacrificing performance under small wind forces, our risk-aware LQR controller forces the state to have less variability and, thus, protects the robot against large gusts. On the other hand, the state of the robot state can grow very large under the risk-neutral and LEQG schemes. This behavior is illustrated even more clearly in Fig. 3, where we present the time-empirical cumulative distribution of the state penalties for all $N$ time steps. The time-empirical "probability" of suffering large state penalties is drastically smaller compared to LQR or LEQG.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

To better illustrate how the proposed risk-aware controller works, we also discuss the evolution of the position $x_{k,1}$ and the input $u_{k,1}$, as shown in Fig. 4, for the first $50$ steps. First, we observe that the controller pushes the state $x_{k,1}$ towards negative values, away from the direction of the large gusts. Second, notice that we penalize $x_{k,3}$ more in $Q$. In fact, the risk-neutral LQR results in the steady state gains $K_{{LQR},11} = {- 0.697}$, $K_{{LQR},12} = {- 1.201}$, $K_{{LQR},23} = {- 0.925}$, $K_{{LQR},24} = {- 1.376}$, i.e., it is stricter with direction $x_{k,3}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

However, $x_{k,1}$ exhibits more variability due to the strong wind direction. In contrast, our risk-aware scheme adapts to the noise in a principled way. Due to the inflation term $\muQWQ$, our scheme returns the steady-state gains $K_{11} = {- 2.1008}$, $K_{12} = {- 2.2132}$, $K_{23} = {- 1.1161}$, $K_{24} = {- 1.5131}$, which means that the risky direction $x_{k,1}$ is controlled more strictly. Naturally, being more cautious with the state leads to higher control effort. Lastly, although the LEQG controller is also more state-cautious, it is agnostic to the heavy tails of the wind distribution. Hence, it still suffers from large perturbation due to the wind gusts.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We presented a new risk-aware reformulation of the classical LQR problem, where we introduce a new risk measure to be used as an explicit and tunable risk constraint, along with the standard LQR objective. By restricting the expected cumulative predictive variance of the state penalties, we can decrease the variability of the state at will, protecting the system against uncommon but strong random disturbances. The optimal controller enjoys a simple closed-form expression with clear interpretation, is always stable and is easy to tune. Our scheme works for arbitrary noise process distributions, as long as the corresponding fourth-order moments are finite.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Moving forward, our framework opens up many directions for extensions and future research. First, we would like to note that our analysis does not depend on the constraints having the same matrix $Q$ as in the cost. In fact, we can define our risk constraint as

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

where $Q_{c}$ is a design choice. Proposition 1. ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators") still holds, in the sense that the constraint can be rewritten as a quadratic one. This implies that, thanks to its simplicity, the predictive variance constraint can be easily incorporated in more general problems, e.g., MPC or classical constrained-LQR, adding a risk-aware flavor to them. Another possibility is to employ stage-wise constraints of the form

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this case, the optimal controller will be similar to (17. ‣ III-B Optimal Risk-Aware Control Policies ‣ III Optimal Risk-Aware LQR Controllers ‣ Risk-Constrained Linear-Quadratic Regulators")), but will depend on multiple Lagrange multipliers that can be optimized with primal-dual algorithms. Lastly, our predictive variance constraint is based on one-step-ahead prediction. In some cases, careless selection of $Q_{c}$ might make our controller more myopic. At the same time, though, increasing the prediction horizon might not always preserve the quadratic form of the constraint. In future work, we would also like to address this issue.
