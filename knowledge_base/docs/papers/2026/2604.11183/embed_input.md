<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Closed-loop Analysis of Linear Stochastic MPC with Risk-averse Constraints

Topics include Model predictive control, Predictive control, Probabilistic models, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Chance constraints are widely used in stochastic model predictive control (MPC) to enforce probabilistic state and input constraints in the presence of unbounded disturbances. However, they only restrict violation probabilities and do not account for the magnitude of rare but severe constraint violations. In this paper, we extend the indirect feedback approach for linear stochastic MPC from chance constraints to risk-averse constraints like the conditional value-at-risk. For the resulting risk-averse MPC scheme, we establish recursive feasibility and closed-loop constraint satisfaction. Furthermore, based on a stochastic dissipativity notion and suitable conditions on the terminal ingredients we show that (near)-optimality of the averaged closed-loop performance can be ensured.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The structured consideration of system uncertainty (either induced by plant-model mismatch or stemming from exogenous disturbances) is crucial in many control contexts. When stochastic optimal control or predictive control is considered, the consideration of chance constraints has become a standard tool, see, e.g.,. However, chance constraints do, in general, not allow to avoid rare outcomes with bad performance. Risk measures, on the other hand, are well suited to avoiding rare outcomes with bad performance. Examples include conditional value-at-risk, entropic value-at-risk and others. In previous work we analyzed stochastic MPC with risk-averse objectives. Moreover, suggest the consideration of risk-averse constraint formulations in stochastic MPC. Yet, to the best of our knowledge, the formal closed-loop analysis of stochastic MPC appears to be mostly limited to chance-constrained formulations, cf..

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

On this canvas, this paper makes first steps towards developing an analysis framework for stochastic MPC of linear systems subject to potentially non-Gaussian disturbances and considering generic risk-averse constraint formulations. In particular, we extend the indirect feedback approach presented in to the consideration of risk-averse constraints using risk measures. Furthermore, based on dissipativity notions for stochastic systems introduced, we provide a rigorous analysis of the averaged performance of the closed MPC loop for not necessarily quadratic cost functions. In contrast to, we provide a lower bound on the averaged performance defined by a stationary solution *and* we derive an upper bound which holds for general stage costs if the terminal ingredients are suitably chosen. The core contributions of the paper are twofold: (i) We extend the indirect feedback approach of to risk-averse constraint formulations using risk measures and to non-quadratic stage costs. (ii) Using stochastic dissipativity concepts, we derive a novel lower bound on the averaged performance of stochastic linear MPC whereby we do not require Gaussianity of the disturbance distribution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of this paper is structured as follows: Section II introduces the setting and problem formulation, while Section III recalls the indirect feedback approach. Section IV presents our main findings, while in Section V we focus on the special case of Gaussian uncertainty and quadratic stage costs. Section VI draws upon a numerical example to illustrate our findings, while the paper ends with conclusions in Section VII.

<!-- chunk {"id": "body-0006", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

Then, for an *i.i.d.* sequence $W,W,\ldots$ such that $W(k)$ is independent of $X(k)$ and $U(k)$ for all $k\in\mathbb{N}_{0}$, we consider linear stochastic systems of the form Here, the initial condition $X_{0}$, the states $X(k)$, the controls $U(k)$, and the noise $W(k)$ are considered to be random variables on the probability space $(\Omega,\mathcal{F},\mathbb{P})$, i.e., $X(k)\in\mathcal{R}(\Omega,\mathbb{R}^{n})$, $U(k)\in\mathcal{R}(\Omega,\mathbb{R}^{l})$, and $W(k)\in\mathcal{R}(\Omega,\mathbb{R}^{m})$ with for

<!-- chunk {"id": "body-0007", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

Furthermore, we assume that the control sequence $\mathbf{U}=(U,U,\ldots)$ is adapted to the stochastic filtration $(\mathcal{F}_{k})_{k\in\mathbb{N}_{0}}$ defined by The last condition can be seen as a a causality requirement, which guarantees that we only take past and present but not future events into account for our control design. Moreover, note that the setting above allows the disturbance $W(k)$ to be non-Gaussian.

<!-- chunk {"id": "body-0008", "role": "body", "section": "PROBLEM FORMULATION", "weight": 1.0} -->

To extend system to an optimal control problem we consider stage costs in expectation of the form where the deterministic stage costs $g:\mathbb{R}^{n}\times\mathbb{R}^{l}\to\mathbb{R}$ is a continuous function bounded from below. Additionally, we impose linear risk-averse constraints of the form Here, the mapping $\rho(Y)$ for $Y\in\mathcal{R}(\Omega,\mathbb{R})$ is a risk measure in the sense of the following definition.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INDIRECT-FEEDBACK STOCHASTIC MPC", "weight": 1.0} -->

To calculate an approximation of the solution to for $N=\infty$ we use an indirect-feedback stochastic MPC scheme, cf.. The idea of the indirect-feedback approach is to use a deterministic prediction $z(k)\in\mathbb{R}^{n}$ for evaluation of tightened constraints in open loop while the optimization of the cost is performed subject to the most recent state measurement.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INDIRECT-FEEDBACK STOCHASTIC MPC", "weight": 1.0} -->

To this end, we use a linear-affine feedback parametrization of the control during the open-loop optimization, i.e., in it holds that $U(k)=KX(k)+v_{k}$ for all $k\in\{0,\ldots,N-1\}$, where $K\in\mathbb{R}^{l\times n}$ is a fixed linear feedback-gain stabilizing the pair $(A,B)$ and $v_{k}\in\mathbb{V}\subseteq\mathbb{R}^{l}$ is the free control variable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INDIRECT-FEEDBACK STOCHASTIC MPC", "weight": 1.0} -->

Then, by defining the prediction $z(k)\in\mathbb{R}^{n}$ the full state can be written as $X(k)=z(k)+E(k)$ with Since for a given $z_{0}\in\mathbb{R}^{n}$ the dynamics are deterministic, we obtain Hence we can rewrite the risk-averse constraints as Note that since we fixed the feedback matrix $K$, the dynamics of $E$ from do not depend on the control input and thus the evolution of $E$ is not affect by the optimization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INDIRECT-FEEDBACK STOCHASTIC MPC", "weight": 1.0} -->

Note that in contrast to, in problem we added terminal ingredients, namely the terminal set $\mathbb{Z}_{f}$ and the terminal penalty $F(X)=\mathbb{E}[g_{f}(X)]$ with $g_{f}:\mathbb{R}^{n}\to\mathbb{R}$. Such terminal ingredients are common in MPC to ensure recursive feasibility and stability, cf., and will also be used to derive our closed-loop guarantees in Section IV. The resulting indirect feedback SMPC scheme is summarized in Algorithm 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "INDIRECT-FEEDBACK STOCHASTIC MPC", "weight": 1.0} -->

Input: Fixed stabilizing feedback K ∈ ℝl × n, feasible initial state X0. Measure the state x0 = X0(ω), calculate z0 = 𝔼[Xcl] and set Xcl(0, ω) = xj, Zcl(0, ω) = z0, E0 = X0 − z0. 1.) Solve the stochastic optimal control problem and obtain the solution v*:= (v0*, …, vN − 1*). 2.) Compute Ej + 1 = (A + BK)Ej + W(j), predict zj + 1 = (A + BK)zj + Bv0* + 𝔼[W(j)], and set Zcl(j + 1, ω) = zj + 1. 3.) Set Vcl(j, ω) = v0*, apply the feedback Ucl(j, ω) = Kxj + v0* to system and measure the next state xj + 1 = Xcl(j + 1, ω).

<!-- chunk {"id": "body-0014", "role": "body", "section": "INDIRECT-FEEDBACK STOCHASTIC MPC", "weight": 1.0} -->

Algorithm 1 Indirect feedback SMPC Note that due to the initializations at time $j=0$ we get However, while for times $j\geq 1$ it still holds that in general $Z^{cl}(j)=\mathbb{E}[X^{cl}(j)]$ would not hold anymore but only since the control value $U^{cl}(j,\omega)=v_{0}^{*}$ in Algorithm 1 depends on the current measurements through optimization. This particularly emphasizes that $Z^{cl}(j)$ is a random variable and that $Z^{cl}(j)$ as well as the closed-loop controls are depending on the whole history of states, i.e., $Z^{cl}(j+1)$ and $U^{cl}(j)$ are $F_{j}$-measurable.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark III.1", "weight": 1.0} -->

Note that the dynamics of $E$ from do not depend on $v$ and hence are independent of the optimization. Therefore the sequences $\rho(c_{i}^{\top}E(j))$ and $\rho(d_{i}^{\top}KE(j))$, which are necessary for constraint evaluation, can be computed offline in advance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark III.1", "weight": 1.0} -->

However, usually it is rather difficult to evaluate $\rho(c_{i}^{\top}E(j))$ and $\rho(d_{i}^{\top}KE(j))$ exactly unless we consider special cases as in Section V. One possibility to get at least an approximation of these terms is for example to use a Monte-Carlo sampling. Moreover, one could also further tighten the constraints if there exists sequences $\tilde{c}(j)$ and $\tilde{d}(j)$ such that holds. If such sequences are known, we can simply replace the terms $\rho(c_{i}^{\top}E(k))$ and $\rho(d_{i}^{\top}KE(k))$ in problem by $\tilde{c}(j)$ and $\tilde{d}(j)$. While this of course would lead to a more conservative formulation, the results of this paper still hold if the terminal set is constructed appropriately as explained after Theorem IV.2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "CLOSED-LOOP GUARANTEES", "weight": 1.0} -->

In this section we aim to provide closed-loop guarantees for Algorithm 1, particularly showing closed-loop constraint satisfaction and averaged (near-)optimality. Note that this algorithm does not use the simplification from the Gaussian setting from Section V and thus, our closed-loop guarantees are theoretically guaranteed for arbitrary initial conditions and distributions. Moreover, as we see in Section V all the assumptions made in this section can be satisfied in the linear-quadratic case, which enables us to transfer the derived results to the computationally more tractable Algorithm 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Recursive Feasibility", "weight": 1.0} -->

Before we deal with constraint satisfaction and optimality estimates, we first show that Algorithm 2 is recursively feasible, i.e., if we start with an initial condition $X_{0}$ for which the problem can be solved, then it can be solved for all subsequent steps of the MPC loop.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Recursive Feasibility", "weight": 1.0} -->

To this end, we make the following assumption, which is akin to \[6, Assumption 1\].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption IV.1", "weight": 1.0} -->

Using this assumption, we can establish recursive feasibility of Algorithm 2 in an analogous way to \[6, Theorem 1\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Constraint Satisfaction", "weight": 1.0} -->

Since in closed loop the value $z_{j}$ represents $\mathbb{E}[X^{cl}(j)\mid\mathcal{F}_{j-1}]$ rather than the unconditioned expectation $\mathbb{E}[X^{cl}(j)]$ it is not obvious that the proposed risk-averse constraints are satisfied in closed-loop. The following theorem shows that the considered restrictions in open loop are indeed sufficient to obtain closed-loop constraint satisfaction.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-C Averaged Performance Optimality", "weight": 1.0} -->

As the final part of our closed-loop analysis we will give optimality estimates for the averaged performance. These findings will be based on a stochastic dissipativity notion developed. There it was shown that in contrast to the deterministic setting (strict) dissipativity notions can be formulated on different layers, such as moments, distributions or random variables. However, in the following we will use the notion formulated with respect to random variables, which leads to the following stationarity concept.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption IV.7", "weight": 1.0} -->

There exists a stationary pair $(\mathbf{X}^{s},\mathbf{U}^{s})$ and a constant $C_{f}\geq 0$ such that for all $X\in\mathcal{R}(\Omega,\mathbb{R}^{n})$ and $v_{f}$ from Assumption IV.1 the inequality The following theorem introduces the upper bound on the asymptotic averaged performance based on this assumption.

<!-- chunk {"id": "body-0024", "role": "body", "section": "MOMENT-BASED REFORMULATION FOR LINEAR-QUADRATIC PROBLEMS WITH GAUSSIAN NOISE", "weight": 1.0} -->

Although our theory applies to general costs and disturbances, the open-loop problems are in general hard to solve. In this section, we make some simplifications that enable us to obtain an implementable version of Algorithm 1, which only uses information about the expectation and covariances of the appearing quantities.

<!-- chunk {"id": "body-0025", "role": "body", "section": "MOMENT-BASED REFORMULATION FOR LINEAR-QUADRATIC PROBLEMS WITH GAUSSIAN NOISE", "weight": 1.0} -->

We consider linear-quadratic stage costs of the form where $Q\in\mathbb{R}^{n\times n}$ is symmetric, positive semi-definite, and $R\in\mathbb{R}^{l\times l}$ is symmetric and positive definite. Furthermore, we consider a terminal penalty where $P$ is the solution of the Lyapunov equation Then, for a given measurement $x_{j}\in\mathbb{R}^{n}$ we can evaluate the cost in as Here, $\mu_{X}(k)=\mathbb{E}[X(k)]$, $\Sigma_{X}(k)=\text{Cov}(X(k))$, $\mu_{W}=\mathbb{E}[W(k)]$, and $\Sigma_{W}=\text{Cov}(W(k))$, and the initial condition is $(\mu_{X},\Sigma_{X})=(x_{j},0)$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "MOMENT-BASED REFORMULATION FOR LINEAR-QUADRATIC PROBLEMS WITH GAUSSIAN NOISE", "weight": 1.0} -->

Moreover, we assume that the disturbance follows a Gaussian distribution, i.e., $W(k)\sim\mathcal{N}(\mu_{W},\Sigma_{W})$ holds for all $j\in\mathbb{N}_{0}$, and consider the case that the risk measure $\rho(Y)$ defining the risk-averse constraints is one of the following mappings: The expected value The conditional value-at-risk The entropic value-at-risk where $M_{Y}(z)$ denotes the moment generating function of $Y$ at $z$, which we consider to exists.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark V.1", "weight": 1.0} -->

We want to emphasize that the constraint $\text{VaR}_{1-\alpha}(Y)\leq d$ is equivalent to $\mathbb{P}(Y\leq d)\geq 1-\alpha$. Hence, our setting does also include chance constraint formulations as a special case and thus it can be seen as a extension of in terms of the class of constraints.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark V.1", "weight": 1.0} -->

Since $W(k)$ has a Gaussian distribution, we can conclude that for an initial value $E_{0}=X_{0}-E[X_{0}]\sim\mathcal{N}(0,\Sigma_{E_{0}})$ the random variable $E$ from has a zero-mean Gaussian distribution for all times $k\in\mathbb{N}_{0}$, i.e, $E(k)\sim\mathcal{N}(0,\Sigma_{E}(k))$ with covariance Using this observation we can evaluate $\rho(c_{i}^{\top}E(j))$ and $\rho(d_{i}^{\top}KE(j))$ exactly, since for a random variable $Y\sim\mathcal{N}(\mu_{Y},\sigma_{Y}^{2})$ with mean $\mu_{Y}\in\mathbb{R}$ and variance

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark V.1", "weight": 1.0} -->

$\sigma_{Y}^{2}\in\mathbb{R}_{0}^{+}$ the risk measures -- can be written as where $\varphi(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^{2}}{2}}$ is the standard normal probability density function and $\Phi(x)$ is the standard normal cumulative distribution function.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark V.1", "weight": 1.0} -->

To construct the terminal set $\mathbb{Z}_{f}$ let us now assume that $\Sigma_{E_{0}}\preceq\Sigma_{E}^{s}$ holds, where $\Sigma_{E}^{s}$ is the solution of the Lyapunov equation Then we can conclude that $\Sigma_{E}(j)\preceq\Sigma_{E}^{s}$ holds for all $j\in\mathbb{N}_{0}$ and hence, Thus, assuming that and $0\in\mathbb{V}$ holds, the terminal set $\mathbb{Z}_{f}=\{0\}$ satisfies the conditions of Assumption IV.1 with $v_{f}=0$ since $(z^{s},v^{s})=$ is an equilibrium of the dynamic for $\mathbb{E}[W(k)]=0$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark V.1", "weight": 1.0} -->

The resulting moment-based open-loop problem can be summarized as and the corresponding MPC scheme is given in Algorithm 2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark V.1", "weight": 1.0} -->

Since the terminal set $\mathbb{Z}_{f}$ satisfies Assumption IV.1 we directly get recursive feasibility by Theorem IV.2 and closed-loop constraint satisfaction by Theorem IV.3. However, to ensure also the performance bounds from Section IV-C we need to show that stochastic dissipativity holds and Assumption IV.7 is satisfied for the terminal cost. For the simplified setting of this section this is shown by the following theorem and lemma.

<!-- chunk {"id": "body-0033", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

In this section we will illustrate our findings by a DC-DC-converter regulation problem, which was already used for case studies in stochastic MPC in The corresponding dynamics are of the form, where and $W(k)\sim\mathcal{N}(0,\Sigma_{W})$ with $\Sigma_{W}=0.1I_{2}\in\mathbb{R}^{2\times 2}$. Additionally, we consider quadratic costs of the form with $Q=\text{diag}$ and $R=5$ and impose a single risk-averse constraint on the first component given by where $\rho(Y)$ denotes one of the risk measures from equation -- with $1-\alpha=0.6$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

We clearly observe that the constraints are always satisfied, as predicted by Theorem IV.3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

Furthermore, for all $\alpha\in$, $Z\in\mathcal{R}(\Omega,\mathbb{R})$ it holds that Consequently, the restrictiveness of the constraints follows the same ordering, which is also observable in Figure 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

To compare the performance for different choices of $K$ in Algorithm 2, we constructed a second stabilizing feedback by solving the algebraic Ricatti equation for $\tilde{Q}:=0.01Q$ and $\tilde{R}:=200R$. We then ran Algorithm 2 again using these different choices of $K$, where the constraints in were defined using the conditional value-at-risk $\text{CVaR}_{0.6}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

As Corollary V.4 indicates, for $K=K^{*}$ the averaged performance should converge to the optimal stationary cost, as can be seen in Figure 2. However, for $K=\tilde{K}$, Corollary V.4 only guarantees that the averaged performance satisfies a suboptimal bound; convergence to the optimal stationary cost is therefore not ensured. Figure 2 shows that the averaged closed-loop performance indeed converges to a value deviating from the optimal stationary cost, demonstrating that the choice of $K$ affects the asymptotic performance of the closed-loop solution not only theoretically but also in practice.

<!-- chunk {"id": "body-0038", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We presented an indirect feedback approach for stochastic MPC with linear systems and general risk-averse constraints defined via risk measures. For this algorithm, we derived near-optimal performance bounds for general cost functions. Future research should focus on developing efficient implementations of Algorithm 1 without the simplifications introduced in Section V, constructing suitable terminal costs for the non-quadratic case, or extending the presented results to nonlinear systems, as in for the original chance-constrained algorithm.
