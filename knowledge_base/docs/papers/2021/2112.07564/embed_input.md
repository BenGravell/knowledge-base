<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Linear Quadratic Control with Risk Constraints

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new risk-constrained formulation of the classical Linear Quadratic (LQ) stochastic control problem for general partially-observed systems. Our framework is motivated by the fact that the risk-neutral LQ controllers, although optimal in expectation, might be ineffective under relatively infrequent, yet statistically significant extreme events. To effectively trade between average and extreme event performance, we introduce a new risk constraint, which explicitly restricts the total expected predictive variance of the state penalty by a user-prescribed level. We show that, under certain conditions on the process noise, the optimal risk-aware controller can be evaluated explicitly and in closed form. In fact, it is affine relative to the minimum mean square error (mmse) state estimate. The affine term pushes the state away from directions where the noise exhibits heavy tails, by exploiting the third-order moment~(skewness) of the noise. The linear term regulates the state more strictly in riskier directions, where both the prediction error (conditional) covariance and the state penalty are simultaneously large; this is achieved by inflating the state penalty within a new filtered Riccati difference equation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also prove that the new risk-aware controller is internally stable, regardless of parameter tuning, in the special cases of i) fully-observed systems, and ii) partially-observed systems with Gaussian noise. The properties of the proposed risk-aware LQ framework are lastly illustrated via indicative numerical examples.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the problem of Linear Quadratic (LQ) stochastic control, one is typically interested in optimizing average control performance for linear systems of the form

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $x_{t} \in {\mathbb{R}}^{n}$ is the state, $y_{t} \in {\mathbb{R}}^{m}$ is the measured output, $u_{t}$ is input, and $w_{t}$, $v_{t}$ are process and measurement noise disturbances. A standard approach is to minimize the expectation of the following quadratic cost comprising of stage-wise input and state penalties up to a horizon $N$

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where matrices $Q,R$ are design choices.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

While LQ control has been a standard approach to controlling stochastic systems, it only focuses on *average* performance, which might be an insufficient objective when dealing with critical applications. Examples of such applications appear naturally in many areas, including wireless industrial control, energy, finance, robotics, networking, and safety, to name a few. Indeed, occurrence of less probable, non-typical or unexpected events might lead the underlying dynamical system to experience shocks with possibly catastrophic consequences, e.g., a drone diverging too much from a given trajectory in a hostile environment, or an autonomous vehicle crashing onto a wall or hitting a pedestrian. In such situations, design of effective *risk-aware* control policies is highly desirable, systematically compensating for those extreme events, at the cost of slightly sacrificing average performance under nominal conditions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To highlight the usefulness of a risk-aware control policy, let us consider the following simple, motivating example. Let $x_{k + 1} = {x_{k} + u_{k} + w_{k + 1}}$ model an aerial robot, moving along a line. Assume that the process noise $w_{k}$ is i.i.d. Bernoulli, taking the values $\beta > 2$ with probability $1/\beta$ and $0$ with probability $1 - {1/\beta}$. This noise represents shocks, e.g., wind gusts, that can occur with some small probability. We would then like to minimize the LQR cost ${\mathbb{E}}{\sum_{t = 0}^{N}{\{ x_{t}^{2}\}}}$, i.e., the total displacement of the robot over a horizon of $N$ time steps.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this case, the LQR optimal controller is $u_{k}^{LQR} = {{- x_{k}} - 1}$, where ${- 1} \equiv {- {{\mathbb{E}}w_{k}}}$ cancels the mean of the process noise. We see that the LQR solution is risk-neutral, as it does not account for the fact that the shock $\beta$ could be arbitrarily large. On the other hand, the risk-aware LQR formulation proposed in this work results in a family of optimal controllers of the form

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\mu$ controls the trade-off between average performance and risk. As $\mu$ increases, we move from the risk-neutral to the maximally risk-aware controller ${u_{t}^{\ast}{(\infty)}} = {{- x_{t}} - {\beta/2}}$, which treats the noise as adversarial---see Fig. 1 and by the ARL under grant DCIST CRA W911NF-17-2-0181.").

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In both classical and recent literature in linear-quadratic problems, risk awareness in estimation and control is typically achieved by replacing the respective random cost with its exponentiation. Yet, the resulting stochastic control problem might not be well-defined for general classes of noise distributions, as it requires the moment generating function of the cost to be finite. Thus, heavy-tailed or skewed distributions, which are precisely those exhibiting high risk, are naturally excluded. Also, even if the expectation of the exponential cost is finite, it does not lead to a general, closed-form and interpretable solution. A notable exception is that of Gaussian noise, also known as the Linear Exponential Quadratic Gaussian (LEQG) problem, which does enjoy a simple closed-form solution. Apparently though, the Gaussian assumption is unable to capture distributions with asymmetric (skewed) structure, as in the above example.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

--New Risk-Constrained Formulation. We introduce a new risk-constrained formulation for the problem of LQ control in the case of partially-observed systems. The standard LQ objective is minimized subject to a total expected predictive variance risk constraint with respect to the state penalties. By tuning the risk constraint, we can trade between average performance and statistical variability of the state penalties.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

--General Noise Models. Contrary to the LEQG approach, our risk-constrained formulation is well-defined for general noise distributions, provided the associated fourth-order moments of the process noise are finite; thus, heavy-tailed or skewed noises are supported within our framework. For fully-observed systems, the optimal control law can be explicitly characterized under the same condition of finite fourth-order moments. In the case of general partially-observed systems, in order to characterize the optimal controller, we require the additional sufficient condition that all higher-order moments of the process noise exist. In any case, we do not require the existence of a moment generating function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Characterization of Optimal Risk-Aware Controls. Under the aforementioned regularity conditions on the process noise, the constrained LQ problem admits a closed-form solution with a natural interpretation. The optimal risk-aware feedback controller is affine with respect to the optimal observer. The affine component pushes the state away from directions where the state prediction error exhibits (skewed) heavy tails. Meanwhile, the state feedback gain satisfies a new risk-aware filtered Riccati recursion, in which the state penalty is inflated in riskier directions, where both the (conditional) covariance of the state prediction error and the state penalty are simultaneously larger. Interestingly, the separation principle holds, in the sense that the optimal observer is the minimum mean-square error estimator, which is designed independently of the control objective. To explicitly compute the parameters of the affine optimal control law, it is required to track several conditional moments, which might be a hard problem in general.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

--Explicit Risk-Aware LQR and LQG controllers. In the special case of fully-observed systems (Linear Quadratic Regulator (LQR)) we can explicitly compute the optimal control law. The same is true for the case of partially-observed systems with Gaussian noise (Linear Quadratic Gaussian (LQG) control). Further, we show that our optimal risk-aware controllers are always stable, under standard controllability/observability conditions. Interestingly, by appropriate re-parameterization, our risk-aware LQR problem is equivalent to a generalized risk-neutral LQR problem with a tracking objective. Essentially, this implies that risk-neutral LQR formulations can provide inherent risk-averse behavior, as long as the involved parameters are selected in a principled way, as presented herein. A similar property holds for the risk-aware LQG problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Risk-Constrained LQ Formulation", "weight": 1.0} -->

Consider system (1 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), where $x_{t} \in {\mathbb{R}}^{n}$ is the state, $u_{t} \in {\mathbb{R}}^{p}$ is the control signal, and $y_{t} \in {\mathbb{R}}^{m}$ is the measured output. Matrix $A \in {\mathbb{R}}^{n \times n}$ is the state transition matrix, $B \in {\mathbb{R}}^{n \times p}$ is the input matrix, and $C \in {\mathbb{R}}^{m \times n}$ is the output matrix. We assume that the initial value $x_{0}$ is deterministic and fixed.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Risk-Constrained LQ Formulation", "weight": 1.0} -->

Signal $w_{t} \in {\mathbb{R}}^{n}$ is a random process noise, while $v_{t} \in {\mathbb{R}}^{m}$ is a random measurement noise. The process $(w_{t},v_{t})$ is assumed to be i.i.d across time, but it can have any joint distribution (possibly non-Gaussian). For $t \geq 0$, let $\mathcal{F}_{t} = {\sigma\left( y_{0:t},u_{0:t} \right)}$ be the $\sigma$-algebra generated by all observables up to time $t$, and let $\mathcal{F}_{- 1}$ be the trivial $\sigma$-algebra.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Risk-Constrained LQ Formulation", "weight": 1.0} -->

Based on this notation, $u_{t}$ is $\mathcal{F}_{t}$-measurable, while $(w_{t + 1},v_{t + 1})$ is independent of $\mathcal{F}_{t}$. We also make an additional assumption on the process noise.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1 (Noise Regularity)", "weight": 1.0} -->

The above mild regularity condition is required for our risk measure to be well-defined. It is satisfied by general noise distributions, including many heavy-tailed ones. Denote the mean of the noise by $\overline{w} \triangleq {{\mathbb{E}}w_{k}}$ and its variance by $W \triangleq {{\mathbb{E}}{({w_{k} - \overline{w}})}{({w_{k} - \overline{w}})}^{\prime}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1 (Noise Regularity)", "weight": 1.0} -->

As discussed in Section 1 and by the ARL under grant DCIST CRA W911NF-17-2-0181."), the classical LQ problem is risk-neutral, since it optimizes performance only on average. Still, even if average performance is good, the state can grow arbitrarily large under less probable, yet extreme events. In other words, the state can exhibit large variability. To deal with this issue, we propose a risk-constrained formulation of the LQ control problem, posed as

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1 (Noise Regularity)", "weight": 1.0} -->

where $u = u_{0:{N - 1}}$ are the inputs from time $0$ up to time $N - 1$, for some horizon $N \in {\mathbb{N}}$. For each $t$, the causality constraint on $u_{t}$ restricts the inputs to the space of $\mathcal{F}_{t}$-measurable random vectors of appropriate dimension with bounded fourth-order moments, denoted as $\mathcal{L}_{4}{(\mathcal{F}_{t})}$. Here, the risk measure adopted is the *(cumulative expected) predictive variance* of the state cost. The predictive variance incorporates information about the tail and skewness of the penalty $x_{t}^{\prime}Qx_{t}$. This forces the controller to take higher-order noise statistics into account, mitigating the effect of rare though large noise values. Hence, our risk-aware LQ formulation not only forces the state $x_{t}$ to be close to zero, but also explicitly restricts its variability.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1 (Noise Regularity)", "weight": 1.0} -->

The initial state is fixed (for simplicity), so there is no associated risk term for $t = 0$. The fourth-order integrability constraint on the inputs along with Assumption 1. ‣ 2 Risk-Constrained LQ Formulation ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.") are sufficient to guarantee that the cumulative expected predictive variance is well-defined.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1 (Input integrability)", "weight": 1.0} -->

The fourth-order integrability condition $u_{t} \in {\mathcal{L}_{4}{(\mathcal{F}_{t})}}$ on the inputs is stricter compared with the risk-neutral formulation, where only square-integrability is needed. In the general case of partially-observed systems, this condition is needed to guarantee that the constraint in (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) is well-defined. However, in many cases of interest, this condition is not essential.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1 (Input integrability)", "weight": 1.0} -->

For example, in the fully observed case (Section 5 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), we can pose problem (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) with the constraint $u_{t} \in {\mathcal{L}_{2}{(\mathcal{F}_{t})}}$ and the optimal control is still guaranteed to be in $\mathcal{L}_{4}{(\mathcal{F}_{t})}$; this is a byproduct of the noise regularity Assumption 1. ‣ 2 Risk-Constrained LQ Formulation ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.").

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1 (Input integrability)", "weight": 1.0} -->

The same holds for the case of partially-observed systems with Gaussian noise (Section 7 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). $\diamond$

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1 (Input integrability)", "weight": 1.0} -->

Problem (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) offers a simple and interpretable way to control the trade-off between average performance and risk. By simply decreasing $\epsilon$, we increase risk-awareness. Inspired by standard risk-aware formulations, in the above optimization problem our risk definition is tied to the specific state penalty $x_{t}^{\prime}Qx_{t}$. However, all of our results are still valid if we employ the predictive variance of a different quadratic form, e.g., the norm of the state, $\left\| x_{t} \right\|_{2}^{2}$, in the constraint. In the following sections, we characterize the optimal controllers in the case of general partially-observed systems. We also provide explicit, finite-dimensional control laws for the case of i) fully-observed systems with general noise, which we term risk-aware LQR controllers; and ii) partially-observed systems with Gaussian noise, which we term risk-aware LQG controllers.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

The solution procedure of the risk-aware dynamic program (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) consists of the following steps. First, we ensure the well-definiteness of (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), also showing that (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) can be equivalently expressed as a sequential variational Quadratically Contrained Quadratic Program (QCQP), or, more precisely, as a Quadratically Constrained LQ (QC-LQ) problem (Proposition 1. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

Then, we exploit Lagrangian duality (Theorem 1. ‣ 4 Lagrangian Duality ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) to solve (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) exactly and in closed form. More specifically, we first derive an explicit expression for the optimal risk-aware controller (Theorems 4. ‣ 5.1 Recovery of Primal-Optimal Solutions ‣ 5 Optimal Risk-Aware LQR Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181."), 5.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

‣ 6 Optimal Risk-Aware LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181."), 7. ‣ 7 Optimal Risk-Aware LQG Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), given an arbitrary but fixed Lagrange multiplier. Then, we show how an optimal Lagrange multiplier may be efficiently discovered via trivial bisection (Theorem 2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

‣ 4 Lagrangian Duality ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

Since we are dealing with partially observed systems, we can only approximately estimate the current state $x_{t}$ based on the information $\mathcal{F}_{t}$ collected so far. Define the state estimate and the state prediction at time $t$ respectively as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

Note that both values are mean-square optimal, i.e. they minimize the mean square estimation error (prediction error respectively). Under Assumption 1. ‣ 2 Risk-Constrained LQ Formulation ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.") on $w_{t}$, and since $u_{t} \in {\mathcal{L}_{4}{(\mathcal{F}_{t})}}$ both expectations are well-defined. The state prediction and the state estimate are related via the expression

<!-- chunk {"id": "body-0033", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

The innovation (or prediction) error is defined as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

Both errors are martingale differences, satisfying the mean conditions ${{{\mathbb{E}}{(\left. e_{t} \middle| \mathcal{F}_{t - 1} \right.)}} = 0},{{{\mathbb{E}}{(\left. \delta_{t} \middle| \mathcal{F}_{t - 1} \right.)}} = 0}$. Note that in the general case of non-Gaussian noise, the innovation error $\delta_{t}$ is not i.i.d. and not independent of the past in general.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Quadratic Reformulation of Risk-Constrained LQ Control", "weight": 1.0} -->

In the following result, we show that the predictive variance constraint has an underlying quadratic structure.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Lagrangian Duality", "weight": 1.0} -->

To tackle problem (3 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), we now consider the variational Lagrangian $\mathcal{L}_{}:{{{{{\mathcal{L}_{2}{(\mathcal{F}_{0})}} \times \cdots \times \mathcal{L}_{2}}{(\mathcal{F}_{N - 1})}} \times {\mathbb{R}}_{+}}\rightarrow{\mathbb{R}}}$ of the sequential QCQP (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), defined as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Lagrangian Duality", "weight": 1.0} -->

where $\mu \in {\mathbb{R}}_{+}$ is a multiplier associated with the variational risk constraint of (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). Hereafter, problem (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) will be called the primal problem.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Lagrangian Duality", "weight": 1.0} -->

Accordingly, the dual function $D:{{\mathbb{R}}_{+}\rightarrow{\lbrack{- \infty},\infty)}}$ is additionally defined as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Lagrangian Duality", "weight": 1.0} -->

where the implicit feasible set $\mathcal{U}_{0}$ obeys ($k \leq {N - 1}$)

<!-- chunk {"id": "body-0040", "role": "body", "section": "Lagrangian Duality", "weight": 1.0} -->

and contains the constraints of (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) that have not been dualized in the construction of the Lagrangian in (8 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). Note that it is always the case that $D \leq J^{\ast}$ on ${\mathbb{R}}_{+}$, where $J^{\ast} \in {\lbrack 0,\infty\rbrack}$ denotes the optimal value of the primal problem (6.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Lagrangian Duality", "weight": 1.0} -->

‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). Then, the optimal value of the always concave dual problem

<!-- chunk {"id": "body-0042", "role": "body", "section": "Lagrangian Duality", "weight": 1.0} -->

Leveraging Lagrangian duality, we may now state the following result, which provides sufficient optimality conditions for the QCQP (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). The proof is omitted, as it follows as direct application of \[49, Theorem 4.10\].

<!-- chunk {"id": "body-0043", "role": "body", "section": "Optimal Risk-Aware LQR Control", "weight": 1.0} -->

Let us study first the simpler case of fully-observed systems, where $y_{k} = x_{k}$, i.e. there is no measurement noise $v_{k} = 0$ and the output matrix is the identity $C = I$. This problem is the risk-constrained version of the classical Linear Quadratic Regulator (LQR) problem. In this case, the conditional moments in Proposition 1. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.") can be simplified significantly leading to an optimal control law which is easy to interpret, providing intuition for the solution of the general risk-aware LQ problem.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Optimal Risk-Aware LQR Control", "weight": 1.0} -->

Let $\mu \geq 0$ be arbitrary but fixed. First, we may simplify the form of the Lagrangian $\mathcal{L}_{}$ and express it within a canonical dynamic programming framework. In this respect, we have the following straightforward, but key result.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 2 (Relation to LQR with tracking)", "weight": 1.0} -->

The Lagrangian (12. ‣ 5 Optimal Risk-Aware LQR Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) has the structure of a generalized LQR problem with a tracking objective. Substituting for $m_{3} = {QM_{3}}$, where

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 2 (Relation to LQR with tracking)", "weight": 1.0} -->

we can rewrite the stage cost as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 2 (Relation to LQR with tracking)", "weight": 1.0} -->

i.e., the state penalty is quadratic and consists of two distinct terms. The first one, i.e., ${({x_{t} + {\muM_{3}}})}^{\prime}Q{({x_{t} + {\muM_{3}}})}$ is a tracking error term that forces the state to be close to the static target $- {\muM_{3}}$. Informally, in the case of skewed noise, by tracking $- {\muM_{3}}$ we pre-compensate for directions in which the distribution of the noise has heavy tails. This decreases the statistical variability of the predicted stage cost. The second term, $x_{t}^{\prime}{({4\muQWQ})}x_{t}$, is a standard quadratic penalty term; notice that, contrary to the risk-neutral case, the covariance of the noise $W$ now affects the penalty term.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 2 (Relation to LQR with tracking)", "weight": 1.0} -->

Informally, this term penalizes state directions which not only lead to high cost but are also more sensitive to noise, as captured by the product $QWQ$. Hence, the risk-neutral LQR framework can exhibit inherent risk-averse properties, provided that its parameters are selected in a principled way. Of course, selecting those parameters *a priori* is not trivial. $\diamond$

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 2 (Relation to LQR with tracking)", "weight": 1.0} -->

The structure of the Lagrangian as suggested by Lemma 1. ‣ 5 Optimal Risk-Aware LQR Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.") enables us to derive both a closed-form expression for its minimum and an explicit optimal control policy. To this end, define the optimal cost-to-go at stage $k \leq {N - 1}$ as

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 2 (Relation to LQR with tracking)", "weight": 1.0} -->

where we omit the constant components of the Lagrangian. Under this definition, it is true that

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 2 (Relation to LQR with tracking)", "weight": 1.0} -->

We may now derive the complete solution to (9 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), which provides optimal risk-aware control policies for every multiplier $\mu \geq 0$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 2 (Controllability)", "weight": 1.0} -->

The pair $(A,B)$ is stabilizable, the pair $(A,Q^{1/2})$ is detectable, matrix $Q \succeq 0$ is positive semi-definite and matrix $R \succ 0$ is positive definite.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Recovery of Primal-Optimal Solutions", "weight": 1.0} -->

Up to now we have discussed the properties of the optimal controller given a fixed $\mu \geq 0$. In what follows, we show how to compute an optimal multiplier $\mu^{\ast}$ based on Theorems 1. ‣ 4 Lagrangian Duality ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181."), 2. ‣ 4 Lagrangian Duality ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181."). For any fixed $\mu \geq 0$, we provide a closed-form expression for evaluating the risk functional $J_{R}{({u^{\ast}{(\mu)}})}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Recovery of Primal-Optimal Solutions", "weight": 1.0} -->

Moreover, we show that $J_{R}{({u^{\ast}{( \cdot )}})}$ is a continuous function of $\mu$. Hence, if Slater's condition is satisfied, then based on Theorem 2. ‣ 4 Lagrangian Duality ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181."), we can find the optimal multiplier $\mu^{\ast}$ by trivially applying bisection on $\mu$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Recovery of Primal-Optimal Solutions", "weight": 1.0} -->

The evaluation of the risk constraint functional $J_{R}{({u^{\ast}{(\mu)}})}$ may be performed in a recursive fashion, as the following result suggests.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Optimal Risk-Aware LQ Control", "weight": 1.0} -->

In this section we study problem (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) in its full generality, when we only have access to partial state measurements. Fix a Lagrange multiplier $\mu \geq 0$ and recall the definition of Lagrangian $\mathcal{L}_{}$ in (8 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). Before we derive the optimal control law, let us simplify the form of the Lagrangian $\mathcal{L}_{}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Optimal Risk-Aware LQ Control", "weight": 1.0} -->

For brevity, denote the information up to time $t$ (extended state) by $z_{t} = {(y_{0:t},u_{0:{t - 1}})}$, $z_{0} = y_{0}$. Then, we get the following result.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Recovery of Primal-Optimal Solutions", "weight": 1.0} -->

In this subsection, we provide a closed-form expression to evaluate the risk functional $J_{R}{({u^{\ast}{(\mu)}})}$. Moreover, we show that $J_{R}{({u^{\ast}{( \cdot )}})}$ is a continuous function of $\mu$. Similar to the fully-observed case, if Slater's condition is satisfied, then we can find the optimal multiplier $\mu^{\ast}$ by trivially applying bisection.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Optimal Risk-Aware LQG Control", "weight": 1.0} -->

In the special case of Gaussian measurement and process noise, the innovation error $\delta_{t}$ is actually independent of the past $\mathcal{F}_{t - 1}$. Therefore, the moments defined in Proposition 1. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.") are deterministic, and the recursive formulas for the control policy and the risk-evaluation can be simplified dramatically. In this section, we focus on exactly this case and provide explicit formulas for optimal risk-aware LQG controllers.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Assumption 4 (Gaussian Noise)", "weight": 1.0} -->

The process noise and measurement noise $w_{k},v_{k}$ are jointly i.i.d. Gaussian with mean $\overline{w},\, 0$ respectively and covariance

<!-- chunk {"id": "body-0061", "role": "body", "section": "Assumption 5 (Observability)", "weight": 1.0} -->

The pair $(A,C)$ is detectable, the pair $(A,W^{1/2})$ is stabilizable, and the covariance of the measurement noise is strictly positive definite $S \succ 0$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Assumption 5 (Observability)", "weight": 1.0} -->

To prove stability let us assume that we start estimating/controlling the system at some arbitrary time $t_{0} < N$ instead of $0$, with $x_{t_{0}}$ deterministic and known. Based on this, all recursions in the statement of Theorem 7. ‣ 7 Optimal Risk-Aware LQG Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.") are extended to hold for any $t = {t_{0},\ldots,N}$, with ${W_{t_{0}} = 0},{{\hat{x}}_{t_{0}|t_{0}} = x_{t_{0}}}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 5 (Observability)", "weight": 1.0} -->

We will prove that stability is achieved as we let the initial state $t_{0}$ and the horizon $N$ go to $- \infty$ and $+ \infty$ respectively.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 5 (Observability)", "weight": 1.0} -->

To simplify the proof, we also assume that the state penalty is strictly positive definite $Q \succ 0$. The proof can be extended to the case $Q \succeq 0$ at the cost of more complicated arguments, but we omit it in this paper-see proof in the Appendix for discussion.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

Consider a flying robot that moves on a horizontal plane, i.e., the Euclidean space ${\mathbb{R}}^{2}$. We assume that its linearized dynamics can be abstracted by a double integrator as

<!-- chunk {"id": "body-0066", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

where $T_{s} = 0.5$ is the sampling time, $x_{k,1}$, $x_{k,3}$ are the position coordinates, $x_{k,2}$, $x_{k,4}$ the respective velocities and $\eta_{k}$ is the acceleration input. Let $d_{k}$ be a wind disturbance force that acts on the robot, which is modeled as follows: We assume that $d_{k,1}$ constitutes the dominant wind direction with non-zero mean and large variability, while the orthogonal direction $d_{k,2}$ is a weak wind direction with zero mean and small variability. We model $d_{k,1}$ as a mixture of two gaussians $\mathcal{N}{}$, $\mathcal{N}{}$ with weights $0.8$ and $0.2$, respectively. This bimodal distribution models the presence of infrequent but large wind gusts.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

The weak direction $d_{k,2}$ is modeled as zero-mean Gaussian $\mathcal{N}{}$. If we cancel the mean of $d_{k}$ by applying $\eta_{k} = {u_{k} - {{\mathbb{E}}d_{k}}}$, then the system can be re-written in terms of (1 and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), where $w_{k} = {B{({d_{k} - {{\mathbb{E}}d_{k}}})}}$ is now a zero-mean disturbance $\overline{w} = 0$, and $u_{k}$ is the exogenous input.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

Consider now the LQR problem with parameters

<!-- chunk {"id": "body-0069", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

and a horizon of length $N = 5000$. We primarily compare our risk-aware LQR formulation with the classical, risk-neutral LQR via simulations. To tune our controller, we vary $\mu$ in (18. ‣ 5 Optimal Risk-Aware LQR Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) directly instead of varying $\epsilon$. We also (heuristically) compare our controller with the exponential (LEQG) method, even though the noise is not Gaussian, by plugging in the second order statistics $W$. Let the tuning parameter of LEQG be $\theta$. Note that the exponential problem is well defined only if $\theta < 0.001276$ (roughly), where the "neurotic breakdown" occurs. For the purpose of comparison, we simulate all schemes under the same noise sequence $w_{0:N}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

In Fig. 2 and by the ARL under grant DCIST CRA W911NF-17-2-0181."), we see the evolution of the state penalty terms $x_{k}^{\prime}Qx_{k}$, for the first $50$ time steps, under the different control schemes. By slightly sacrificing performance under small wind forces, our risk-aware LQR controller forces the state to have less variability and protects the robot against large gusts. On the other hand, the state penalty can grow very large under the risk-neutral and LEQG schemes. This behavior is illustrated more clearly in Fig. 3 and by the ARL under grant DCIST CRA W911NF-17-2-0181."), where we present the time-empirical cumulative distribution of the state penalties for all $N$ time steps. The time-empirical "probability" of suffering large state penalties is drastically smaller compared to LQR or LEQG.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

To better illustrate how the proposed risk-aware controller works, we also discuss the evolution of the position $x_{k,1}$ and the input $u_{k,1}$, as shown in Fig. 4 and by the ARL under grant DCIST CRA W911NF-17-2-0181."), for the first $50$ steps. First, we observe that the controller pushes the state $x_{k,1}$ towards negative values, away from the direction of the large gusts. Second, notice that we penalize $x_{k,3}$ more in $Q$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

In fact, the risk-neutral LQR results in the steady state gains $K_{{LQR},11} = {- 0.697}$, $K_{{LQR},12} = {- 1.201}$, $K_{{LQR},23} = {- 0.925}$, $K_{{LQR},24} = {- 1.376}$, i.e., it is stricter with direction $x_{k,3}$. However, $x_{k,1}$ exhibits more variability due to the strong wind direction. In contrast, our risk-aware scheme adapts to the noise in a principled way.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Simulations And Discussion", "weight": 1.0} -->

Due to the inflation term $\muQWQ$, our scheme returns the steady-state gains $K_{11} = {- 2.1008}$, $K_{12} = {- 2.2132}$, $K_{23} = {- 1.1161}$, $K_{24} = {- 1.5131}$, which means that the risky direction $x_{k,1}$ is controlled more strictly. Naturally, being more cautious with the state leads to higher control effort, as shown in Fig. 4 and by the ARL under grant DCIST CRA W911NF-17-2-0181."). Lastly, although the LEQG controller is also more state-cautious, it is agnostic to the heavy tails of the wind distribution. Hence, it still suffers from large perturbation due to the wind gusts.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Risk-aware LQG control", "weight": 1.0} -->

In this section we evaluate the risk-aware LQG controller developed in Section 7 and by the ARL under grant DCIST CRA W911NF-17-2-0181."). We use the penalty matrices

<!-- chunk {"id": "body-0075", "role": "body", "section": "Risk-aware LQG control", "weight": 1.0} -->

However, the process noise is now mean-zero Gaussian, with $d_{k,1} \sim {\mathcal{N}{}}$ and $d_{k,2} \sim {\mathcal{N}{}}$. For the measurement model, we assume

<!-- chunk {"id": "body-0076", "role": "body", "section": "Risk-aware LQG control", "weight": 1.0} -->

which implies that we have access to position measurements. We compare our risk-aware LQG controller with the risk-neutral LQG and the LEQG schemes. For the LEQG scheme, we used the non-delayed version \[Th 10.5\].

<!-- chunk {"id": "body-0077", "role": "body", "section": "Risk-aware LQG control", "weight": 1.0} -->

We simulated the system for a horizon of length $N = 3000$. The evolution of the state penalties for the first $50$ time steps is shown in Fig. 5 and by the ARL under grant DCIST CRA W911NF-17-2-0181."). As expected from (34. ‣ 7 Optimal Risk-Aware LQG Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), the controller regulates the state more strictly compared to the risk-neutral LQG controller, by inflating the $Q$ matrix. Note that contrary to the fully-observed example, the noise is zero-mean Gaussian here, hence, there is no affine term in the optimal controller. We observed that the LEQG controller has similar behavior for small values of the exponential parameter $\theta$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Risk-aware LQG control", "weight": 1.0} -->

A more detailed comparison is shown in Fig. 6 and by the ARL under grant DCIST CRA W911NF-17-2-0181."), where the time-empirical cumulative distributions of the state penalties and the input penalties over $3000$ time steps are shown. As we require our controller to be more risk-aware (we increase $\mu$), the state penalties become smaller since the risky directions of the state are regulated more strictly. Naturally, regulating the state more strictly requires more control effort, hence the input penalties become larger. As we approach the maximally-risk aware controller ($\mu = 100$), we achieve the smallest state penalties but the largest input penalties.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Risk-aware LQG control", "weight": 1.0} -->

For small exponential parameters $\theta$ (below $0.006$) a similar behavior is observed in the case of the LEQG controller. As we increase $\theta$, the state is regulated more strictly at the expense of increased control effort. We achieve the smallest state penalties for roughly $\theta = 0.006$. After this value, the tradeoff between control effort and state regulation becomes worse; for example, here both the state penalties and the input penalties increase as we increase $\theta$ past $0.006$. In fact, as $\theta$ approaches the "neurotic breakdown" point, e.g. for $\theta = 0.01$, both penalties become excessively large. This might be expected since the LEQG maximally risk-aware controller is very conservative, treating the noise as being adversarial rather than being stochastic, which is a different regime. On the contrary, our risk-aware LQG controller is well-behaved regardless the value of $\mu$. Hence it is more easy to tune and offers a wider variety of tradeoff curves between control effort and state regulation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Risk-aware LQG control", "weight": 1.0} -->

For example, if we compare the risk-aware LQG controller for $\mu = 0.5$ and the LEQG controller for $\theta = 0.006$, then the risk-aware LQG controller achieves similar state penalties with less control effort.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We studied a novel risk-aware formulation of the classical Linear Quadratic control problem, where we minimize average performance, subject to predictive variance constraints. This gives rise to risk-aware controllers which trade between average performance and protection against uncommon but strong random disturbances. Our formulation is well-defined for general noise distributions, without requiring the existence of the respective moment generating functions. We characterized the optimal control laws for general partially-observed systems, which are affine with respect to the minimum mean-square state estimate. We provided explicit risk-aware control formulas for the special cases of i) fully-observed systems and ii) Gaussian noise. The optimal controllers are easy to tune and are internally stable under standard controllability/observability conditions.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Moving forward, there are numerous interesting research directions. First, our formulation places more emphasis on regulating the state at the cost of increased control effort. To mitigate this, we could potentially include input power constraints in the quadratic formulation (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). Another open problem is explicitly computing the optimal control (29. ‣ 6 Optimal Risk-Aware LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")) in the case of partially-observed systems with non-Gaussian noise. Providing explicit closed-form expressions in this case is a hard problem, since it requires tracking of conditional moments.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

However, it might be possible to provide computational methods, which solve the problem approximately. Lastly, our predictive variance constraint is based on one-step-ahead prediction. In some cases, this might make our controller more myopic. Increasing the prediction horizon, however, might not always preserve the quadratic form of the constraint. In future work, we would also like to address this issue.
