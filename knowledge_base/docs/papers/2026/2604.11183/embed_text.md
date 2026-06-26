## INTRODUCTION

The structured consideration of system uncertainty (either induced by plant-model mismatch or stemming from exogenous disturbances) is crucial in many control contexts. When stochastic optimal control or predictive control is considered, the consideration of chance constraints has become a standard tool, see, e.g.,. However, chance constraints do, in general, not allow to avoid rare outcomes with bad performance. Risk measures, on the other hand, are well suited to avoiding rare outcomes with bad performance. Examples include conditional value-at-risk, entropic value-at-risk and others. In previous work we analyzed stochastic MPC with risk-averse objectives. Moreover, suggest the consideration of risk-averse constraint formulations in stochastic MPC. Yet, to the best of our knowledge, the formal closed-loop analysis of stochastic MPC appears to be mostly limited to chance-constrained formulations, cf..

On this canvas, this paper makes first steps towards developing an analysis framework for stochastic MPC of linear systems subject to potentially non-Gaussian disturbances and considering generic risk-averse constraint formulations. In particular, we extend the indirect feedback approach presented in to the consideration of risk-averse constraints using risk measures. Furthermore, based on dissipativity notions for stochastic systems introduced , we provide a rigorous analysis of the averaged performance of the closed MPC loop for not necessarily quadratic cost functions. In contrast to, we provide a lower bound on the averaged performance defined by a stationary solution *and* we derive an upper bound which holds for general stage costs if the terminal ingredients are suitably chosen. The core contributions of the paper are twofold: (i) We extend the indirect feedback approach of to risk-averse constraint formulations using risk measures and to non-quadratic stage costs. (ii) Using stochastic dissipativity concepts, we derive a novel lower bound on the averaged performance of stochastic linear MPC whereby we do not require Gaussianity of the disturbance distribution.

The remainder of this paper is structured as follows: Section II introduces the setting and problem formulation, while Section III recalls the indirect feedback approach . Section IV presents our main findings, while in Section V we focus on the special case of Gaussian uncertainty and quadratic stage costs. Section VI draws upon a numerical example to illustrate our findings, while the paper ends with conclusions in Section VII.

## PROBLEM FORMULATION

Let $A\in\mathbb{R}^{n\times n}$, $B\in\mathbb{R}^{n\times l}$, such that the pair $(A,B)$ is controllable. Then, for an *i.i.d.* sequence $W,W,\ldots$ such that $W(k)$ is independent of $X(k)$ and $U(k)$ for all $k\in\mathbb{N}_{0}$, we consider linear stochastic systems of the form Here, the initial condition $X_{0}$, the states $X(k)$, the controls $U(k)$, and the noise $W(k)$ are considered to be random variables on the probability space $(\Omega,\mathcal{F},\mathbb{P})$, i.e., $X(k)\in\mathcal{R}(\Omega,\mathbb{R}^{n})$, $U(k)\in\mathcal{R}(\Omega,\mathbb{R}^{l})$, and $W(k)\in\mathcal{R}(\Omega,\mathbb{R}^{m})$ with for $\mathcal{Y}=\mathbb{R}^{n}$, $\mathbb{R}^{l}$, or $\mathbb{R}^{m}$, where $\mathcal{B}(\mathcal{Y})$ denotes the Borel $\sigma$-algebra on $\mathcal{Y}$. Furthermore, we assume that the control sequence $\mathbf{U}=(U,U,\ldots)$ is adapted to the stochastic filtration $(\mathcal{F}_{k})_{k\in\mathbb{N}_{0}}$ defined by The last condition can be seen as a a causality requirement, which guarantees that we only take past and present but not future events into account for our control design. Moreover, note that the setting above allows the disturbance $W(k)$ to be non-Gaussian.

To extend system to an optimal control problem we consider stage costs in expectation of the form where the deterministic stage costs $g:\mathbb{R}^{n}\times\mathbb{R}^{l}\to\mathbb{R}$ is a continuous function bounded from below. Additionally, we impose linear risk-averse constraints of the form Here, the mapping $\rho(Y)$ for $Y\in\mathcal{R}(\Omega,\mathbb{R})$ is a risk measure in the sense of the following definition.

### Definition II.1

A mapping $\rho:\mathcal{R}(\Omega,\mathbb{R})\to\mathbb{R}\cup\{+\infty\}$ is called *risk measure* if it is *translative*, i.e., $\rho(Y+C)=\rho(Y)+c$ for all $Y\in\mathcal{R}(\Omega,\mathbb{R})$ and $c\in\mathbb{R}$.

*monotone*, i.e., $\rho(Y_{1})\geq\rho(Y_{2})$ for all $Y_{1},Y_{2}\in\mathcal{R}(\Omega,\mathbb{R})$ with $Y_{1}\geq Y_{2}$ almost surely.\Furthermore, we assume that the risk measure is law-invariant, i.e., $\rho(Y)=\rho(Z)$ for all $Y\sim Z$.

Commonly used law-invariant risk measures are, e.g., the value-at-risk or the conditional value-at-risk, which we will discuss in Section V.

Then, the stochastic optimal control problem with horizon $N\in\mathbb{N}\cup\{\infty\}$ reads for which we want to approximate a solution on the infinite-horizon that satisfies the risk-averse constraints for all times.

## INDIRECT-FEEDBACK STOCHASTIC MPC

To calculate an approximation of the solution to for $N=\infty$ we use an indirect-feedback stochastic MPC scheme, cf.. The idea of the indirect-feedback approach is to use a deterministic prediction $z(k)\in\mathbb{R}^{n}$ for evaluation of tightened constraints in open loop while the optimization of the cost is performed subject to the most recent state measurement.

To this end, we use a linear-affine feedback parametrization of the control during the open-loop optimization, i.e., in it holds that $U(k)=KX(k)+v_{k}$ for all $k\in\{0,\ldots,N-1\}$, where $K\in\mathbb{R}^{l\times n}$ is a fixed linear feedback-gain stabilizing the pair $(A,B)$ and $v_{k}\in\mathbb{V}\subseteq\mathbb{R}^{l}$ is the free control variable. Then, by defining the prediction $z(k)\in\mathbb{R}^{n}$ the full state can be written as $X(k)=z(k)+E(k)$ with Since for a given $z_{0}\in\mathbb{R}^{n}$ the dynamics are deterministic, we obtain Hence we can rewrite the risk-averse constraints as Note that since we fixed the feedback matrix $K$, the dynamics of $E$ from do not depend on the control input and thus the evolution of $E$ is not affect by the optimization. Using the feedback parametrization $U(k)=KX(k)+v_{k}$ and prediction $z(k)$ the resulting open-loop problem on horizon $N\in\mathbb{N}$ with initial values $x_{j}\in\mathbb{R}^{n}$, $z_{j}\in\mathbb{R}^{n}$, $E_{j}\in\mathcal{R}(\Omega,\mathbb{R}^{n})$ reads | | $\displaystyle\min_{\mathbf{v}}\sum_{k=0}^{N-1}$ | $\displaystyle\ell(X(k),U(k))+F(X(N))$ | | \(11\) | | | $\displaystyle s.t.\penalty 10000\ X(k+1)$ | $\displaystyle=(A+BK)X(k)+Bv_{k}+W(k)$ | | | | | $\displaystyle z(k+1)$ | $\displaystyle=(A+BK)z(k)+Bv_{k}+\mathbb{E}[W(k)]$ | | | | | $\displaystyle U(k)$ | $\displaystyle=KX(k)+v_{k},\penalty 10000\ v_{k}\in\mathbb{V},\penalty 10000\ z(N)\in\mathbb{Z}_{f}$ | | | | | $\displaystyle X$ | $\displaystyle=x_{j},\penalty 10000\ z=z_{j},E=E_{j}$ | | | | | $\displaystyle c_{i}^{\top}z(k)$ | $\displaystyle\leq p_{i}-\rho(c_{i}^{\top}E(k)),i=1,\ldots,m_{x}$ | | | | | $\displaystyle d_{i}^{\top}(Kz(k)+v_{k})$ | $\displaystyle\leq q_{i}-\rho(d_{i}^{\top}KE(k)),i=1,\ldots,m_{x}$ | | | we denote the optimal value function on horizon $N\in\mathbb{N}$ corresponding to this problem. Note that in contrast to, in problem we added terminal ingredients, namely the terminal set $\mathbb{Z}_{f}$ and the terminal penalty $F(X)=\mathbb{E}[g_{f}(X)]$ with $g_{f}:\mathbb{R}^{n}\to\mathbb{R}$. Such terminal ingredients are common in MPC to ensure recursive feasibility and stability, cf., and will also be used to derive our closed-loop guarantees in Section IV. The resulting indirect feedback SMPC scheme is summarized in Algorithm 1.

Input: Fixed stabilizing feedback K ∈ ℝl × n, feasible initial state X0. Measure the state x0 = X0(ω), calculate z0 = 𝔼[Xcl] and set Xcl(0, ω) = xj, Zcl(0, ω) = z0, E0 = X0 − z0. 1.) Solve the stochastic optimal control problem and obtain the solution v*:= (v0*, …, vN − 1*). 2.) Compute Ej + 1 = (A + BK)Ej + W(j), predict zj + 1 = (A + BK)zj + Bv0* + 𝔼[W(j)], and set Zcl(j + 1, ω) = zj + 1. 3.) Set Vcl(j, ω) = v0*, apply the feedback Ucl(j, ω) = Kxj + v0* to system and measure the next state xj + 1 = Xcl(j + 1, ω). Algorithm 1 Indirect feedback SMPC Note that due to the initializations at time $j=0$ we get However, while for times $j\geq 1$ it still holds that in general $Z^{cl}(j)=\mathbb{E}[X^{cl}(j)]$ would not hold anymore but only since the control value $U^{cl}(j,\omega)=v_{0}^{*}$ in Algorithm 1 depends on the current measurements through optimization. This particularly emphasizes that $Z^{cl}(j)$ is a random variable and that $Z^{cl}(j)$ as well as the closed-loop controls are depending on the whole history of states, i.e., $Z^{cl}(j+1)$ and $U^{cl}(j)$ are $F_{j}$-measurable.

### Remark III.1

Note that the dynamics of $E$ from do not depend on $v$ and hence are independent of the optimization. Therefore the sequences $\rho(c_{i}^{\top}E(j))$ and $\rho(d_{i}^{\top}KE(j))$, which are necessary for constraint evaluation, can be computed offline in advance.

However, usually it is rather difficult to evaluate $\rho(c_{i}^{\top}E(j))$ and $\rho(d_{i}^{\top}KE(j))$ exactly unless we consider special cases as in Section V. One possibility to get at least an approximation of these terms is for example to use a Monte-Carlo sampling. Moreover, one could also further tighten the constraints if there exists sequences $\tilde{c}(j)$ and $\tilde{d}(j)$ such that holds. If such sequences are known, we can simply replace the terms $\rho(c_{i}^{\top}E(k))$ and $\rho(d_{i}^{\top}KE(k))$ in problem by $\tilde{c}(j)$ and $\tilde{d}(j)$. While this of course would lead to a more conservative formulation, the results of this paper still hold if the terminal set is constructed appropriately as explained after Theorem IV.2.

## CLOSED-LOOP GUARANTEES

In this section we aim to provide closed-loop guarantees for Algorithm 1, particularly showing closed-loop constraint satisfaction and averaged (near-)optimality. Note that this algorithm does not use the simplification from the Gaussian setting from Section V and thus, our closed-loop guarantees are theoretically guaranteed for arbitrary initial conditions and distributions. Moreover, as we see in Section V all the assumptions made in this section can be satisfied in the linear-quadratic case, which enables us to transfer the derived results to the computationally more tractable Algorithm 2.

### IV-A Recursive Feasibility

Before we deal with constraint satisfaction and optimality estimates, we first show that Algorithm 2 is recursively feasible, i.e., if we start with an initial condition $X_{0}$ for which the problem can be solved, then it can be solved for all subsequent steps of the MPC loop.

To this end, we make the following assumption, which is akin to \[6, Assumption 1\].

### Assumption IV.1

There exists $\mathbb{Z}_{f}\neq\emptyset$ such that holds for all $z\in\mathbb{Z}_{f}$.

There exists $v_{f}\in\mathbb{V}$ such that holds for all $z\in\mathbb{Z}_{f}$.

Using this assumption, we can establish recursive feasibility of Algorithm 2 in an analogous way to \[6, Theorem 1\].

### Theorem IV.2

If problem is feasible for the initial condition $z_{0}=\mathbb{E}[X_{0}]$, then Algorithm 1 is recursive feasible, i.e., feasible for all times $j\in\mathbb{N}_{0}$.

### Proof

Let $\mathbf{v}^{*}=(v_{0}^{*},\ldots,v_{N-1}^{*})$ be an optimal solution of problem at time $j\in\mathbb{N}_{0}$. Then, by Assumption IV.7 the sequence satisfies the constraints in for z_j+1 = (A+BK) z_j + Bv_0\^\* + E\[W(j)\] and all $x_{j}\in\mathbb{R}^{n}$. Hence $\tilde{\mathbf{v}}$ is an admissible control sequence for time $j+1$, which proves the claim since problem is feasible at time $j=0$ by assumption. ∎ Note that since the feedback $K\in\mathbb{R}^{l\times n}$ stabilizes the pair $(A,B)$ there exists a distribution $P^{s}_{E}$ such that $E(j)$ converges in distribution to $P^{s}_{E}$ for suitable $E_{0}$, i.e, $E(j)\xrightarrow{d}P_{E}^{s}$ for $j\to\infty$. Hence, the suprema in Assumption IV.1 exist if the initial value $E_{0}$ is not degenerated, since the risk measure $r$ is assumed to be law-invariant.

Furthermore, if one uses an upper bound on the risk as explained in Remark III.1 we must also consider this in the construction of the terminal set $\mathbb{Z}_{f}$ by replacing $\rho(c_{i}^{\top}E(j))$ with $\tilde{c}(j)$ and $\rho(d_{i}^{\top}KE(j))$ with $\tilde{d}(j)$ respectively.

### IV-B Constraint Satisfaction

Since in closed loop the value $z_{j}$ represents $\mathbb{E}[X^{cl}(j)\mid\mathcal{F}_{j-1}]$ rather than the unconditioned expectation $\mathbb{E}[X^{cl}(j)]$ it is not obvious that the proposed risk-averse constraints are satisfied in closed-loop. The following theorem shows that the considered restrictions in open loop are indeed sufficient to obtain closed-loop constraint satisfaction.

### Theorem IV.3

The risk-averse constraints are satisfied in closed loop, i.e., holds for all times $j\in\mathbb{N}_{0}$, where $X^{cl}(j)$ and $U^{cl}(j)$ are generated pointwisely according to Algorithm 2.

### Proof

For the closed-loop states and controls from Algorithm 1 it holds that Furthermore, due to the proposed risk-averse constraints in the open-loop problem we can conclude that holds almost surely.

Hence, we get by monotonicity and translativity of the risk measure, cf. Definition II.1, that holds for all $j\in\mathbb{N}_{0}$. ∎ Note that the proof for the constraint satisfaction relies on the fact that we can split the closed-loop state into a stochastic part $E(j)$, which is independent of the control, and a nominal part $z(j)$, which we can restrict almost surely in a suitable way. Hence, we conjecture that our results can also be obtained for different splittings and parametrizations of the control which leads to a splitting with the same properties.

### IV-C Averaged Performance Optimality

As the final part of our closed-loop analysis we will give optimality estimates for the averaged performance. These findings will be based on a stochastic dissipativity notion developed . There it was shown that in contrast to the deterministic setting (strict) dissipativity notions can be formulated on different layers, such as moments, distributions or random variables. However, in the following we will use the notion formulated with respect to random variables, which leads to the following stationarity concept.

### Definition IV.4

A pair of stochastic processes $(\mathbf{X}^{s},\mathbf{U}^{s})$ given by with $U^{s}(k)=\pi^{s}(X^{s}(k))$ is called stationary for system if $X^{s}(k)$ and $U^{s}(k)$ satisfy the constraints for all times $k\in\mathbb{N}_{0}$ and there exist probability distributions $P^{s}_{X}$, $P^{s}_{U}$, and $P^{s}_{X,U}$ with for all $k\in\mathbb{N}_{0}$.

Using this definition of a stationary process as the replacement of the deterministic steady state, we can define stochastic dissipativity in the following way, where we denote by $\ell(\mathbf{X}^{s},\mathbf{U}^{s})$ the stage costs of the stationary pair, which are independent of $k$ due to the stationarity of the distributions.

### Definition IV.5

Consider a pair of stationary stochastic processes $(\mathbf{X}^{s},\mathbf{U}^{s})$ with $|\ell(\mathbf{X}^{s},\mathbf{U}^{s})|<\infty$. Then, we call the stochastic optimal control problem stochastically dissipative at $(\mathbf{X}^{s},\mathbf{U}^{s})$, if there exists a law-invariant storage function $\lambda:\mathcal{R}(\Omega,\mathbb{R}^{n})\to\mathbb{R}$ bounded from below such that holds for all $k\in\mathbb{N}_{0}$ and all $X(k)$, $U(k)$ satisfying and the constraints.

Based on stochastic dissipativity we can now establish a lower bound on the asymptotic averaged performance for all admissible control sequences $\mathbf{U}$ of problem. Here, for a given control sequence $\mathbf{U}$ and initial state $X_{0}$ we denote by $X_{\mathbf{U}}(k,X_{0})$ the solution to at time $k$.

### Theorem IV.6

Assume that the stochastic optimal control problem is dissipative at $(\mathbf{X}^{s},\mathbf{U}^{s})$. Then, it holds that for all $\mathbf{U}$ and $X_{0}$ such that $U(k)$ and $X_{\mathbf{U}}(k,X_{0})$ satisfy the constraints and the filtration condition for all $k\in\mathbb{N}_{0}$.

### Proof

By dissipativity we know that there exists a uniform lower bound $-C^{l}_{\lambda}<0$ on $\lambda$ such that which proves the claim by letting $K$ go to infinity. ∎ Note that the lower bound from Theorem IV.6 also holds for the closed-loop solution $(\mathbf{X}^{cl},\mathbf{U}^{cl})$ since it satisfies the constraints due to Theorem IV.3.

Next we will show that we can also bound the closed-loop performance from above given suitable terminal ingredients as defined in the following assumption.

### Assumption IV.7

There exists a stationary pair $(\mathbf{X}^{s},\mathbf{U}^{s})$ and a constant $C_{f}\geq 0$ such that for all $X\in\mathcal{R}(\Omega,\mathbb{R}^{n})$ and $v_{f}$ from Assumption IV.1 the inequality The following theorem introduces the upper bound on the asymptotic averaged performance based on this assumption.

### Theorem IV.8

Let Assumption IV.7 hold. Then, it holds that

### Proof

Consider a given measurement $x_{j}=X^{cl}(j,\omega)\in\mathbb{R}^{n}$, prediction $z_{j}=Z^{cl}(j,\omega)$, and $E_{j}\in\mathcal{R}(\Omega,\mathbb{R}^{n})$, and assume that holds, where $\mathcal{V}_{N}$ the optimal value function to problem. Furthermore, set Since $\tilde{\mathbf{v}}=(v_{1}^{*},\ldots,v_{N-1}^{*},v_{f})$ with $v_{f}\in\mathbb{V}$ from Assumption IV.1 is admissible for time $j+1$, cf. Theorem IV.2, we then get Using Assumption IV.7 this implies Taking the expectation yields and thus, we get where $C_{g}\in\mathbb{R}$ is a lower bound on the deterministic stage costs $g$. ∎ To conclude the findings of this section, the following result combines Theorem IV.6 and Theorem IV.8 to show (near-)optimality of closed-loop solutions in the averaged performance sense.

### Corollary IV.9

Let Assumptions IV.1 and IV.7 hold and assume that the stochastic optimal control problem is stochastically dissipative at $(\mathbf{X}^{s},\mathbf{U}^{s})$. Then, the closed-loop solution from Algorithm 1 has near-optimal averaged performance, i.e., Moreover, if $C_{f}=0$ holds in Assumption IV.7, then the closed-loop solution has optimal averaged performance, i.e.,

### Proof

Follows by Theorem IV.6 and Theorem IV.8. ∎

## MOMENT-BASED REFORMULATION FOR LINEAR-QUADRATIC PROBLEMS WITH GAUSSIAN NOISE

Although our theory applies to general costs and disturbances, the open-loop problems are in general hard to solve. In this section, we make some simplifications that enable us to obtain an implementable version of Algorithm 1, which only uses information about the expectation and covariances of the appearing quantities.

We consider linear-quadratic stage costs of the form where $Q\in\mathbb{R}^{n\times n}$ is symmetric, positive semi-definite, and $R\in\mathbb{R}^{l\times l}$ is symmetric and positive definite. Furthermore, we consider a terminal penalty where $P$ is the solution of the Lyapunov equation Then, for a given measurement $x_{j}\in\mathbb{R}^{n}$ we can evaluate the cost in as Here, $\mu_{X}(k)=\mathbb{E}[X(k)]$, $\Sigma_{X}(k)=\text{Cov}(X(k))$, $\mu_{W}=\mathbb{E}[W(k)]$, and $\Sigma_{W}=\text{Cov}(W(k))$, and the initial condition is $(\mu_{X},\Sigma_{X})=(x_{j},0)$.

Moreover, we assume that the disturbance follows a Gaussian distribution, i.e., $W(k)\sim\mathcal{N}(\mu_{W},\Sigma_{W})$ holds for all $j\in\mathbb{N}_{0}$, and consider the case that the risk measure $\rho(Y)$ defining the risk-averse constraints is one of the following mappings: The expected value The conditional value-at-risk The entropic value-at-risk where $M_{Y}(z)$ denotes the moment generating function of $Y$ at $z$, which we consider to exists.

### Remark V.1

We want to emphasize that the constraint $\text{VaR}_{1-\alpha}(Y)\leq d$ is equivalent to $\mathbb{P}(Y\leq d)\geq 1-\alpha$. Hence, our setting does also include chance constraint formulations as a special case and thus it can be seen as a extension of in terms of the class of constraints.

Since $W(k)$ has a Gaussian distribution, we can conclude that for an initial value $E_{0}=X_{0}-E[X_{0}]\sim\mathcal{N}(0,\Sigma_{E_{0}})$ the random variable $E$ from has a zero-mean Gaussian distribution for all times $k\in\mathbb{N}_{0}$, i.e, $E(k)\sim\mathcal{N}(0,\Sigma_{E}(k))$ with covariance Using this observation we can evaluate $\rho(c_{i}^{\top}E(j))$ and $\rho(d_{i}^{\top}KE(j))$ exactly, since for a random variable $Y\sim\mathcal{N}(\mu_{Y},\sigma_{Y}^{2})$ with mean $\mu_{Y}\in\mathbb{R}$ and variance $\sigma_{Y}^{2}\in\mathbb{R}_{0}^{+}$ the risk measures -- can be written as where $\varphi(x)=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^{2}}{2}}$ is the standard normal probability density function and $\Phi(x)$ is the standard normal cumulative distribution function.

To construct the terminal set $\mathbb{Z}_{f}$ let us now assume that $\Sigma_{E_{0}}\preceq\Sigma_{E}^{s}$ holds, where $\Sigma_{E}^{s}$ is the solution of the Lyapunov equation Then we can conclude that $\Sigma_{E}(j)\preceq\Sigma_{E}^{s}$ holds for all $j\in\mathbb{N}_{0}$ and hence, Thus, assuming that and $0\in\mathbb{V}$ holds, the terminal set $\mathbb{Z}_{f}=\{0\}$ satisfies the conditions of Assumption IV.1 with $v_{f}=0$ since $(z^{s},v^{s})=$ is an equilibrium of the dynamic for $\mathbb{E}[W(k)]=0$.

The resulting moment-based open-loop problem can be summarized as and the corresponding MPC scheme is given in Algorithm 2.

Since the terminal set $\mathbb{Z}_{f}$ satisfies Assumption IV.1 we directly get recursive feasibility by Theorem IV.2 and closed-loop constraint satisfaction by Theorem IV.3. However, to ensure also the performance bounds from Section IV-C we need to show that stochastic dissipativity holds and Assumption IV.7 is satisfied for the terminal cost . For the simplified setting of this section this is shown by the following theorem and lemma.

### Theorem V.2

Let $P^{*}$ be the solution of the discrete-time algebraic Riccati equation and set $K^{*}:=-(R+B^{\top}P^{*}B)^{-1}B^{\top}P^{*}A$. Furthermore, let $\Sigma_{X}^{s}$ be the solution of and assume that holds. Then there exits a stationary pair $(\mathbf{X}^{s},\mathbf{U}^{s})$ with $U^{s}(k)=K^{*}X^{s}(k)$, $X\sim\mathcal{N}(0,\Sigma_{X}^{s})$ for all $k\in\mathbb{N}_{0}$, and such that the stochastic optimal control problem under the simplifications of this section is stochastically dissipative.

### Proof

By \[14, Theorem 3.11\] we can conclude that the stochastic optimal control problem with the linear-quadratic structure of this section and without constraints is stochastically dissipative at $(\mathbf{X}^{s},\mathbf{U}^{s})$. However, since the stationary pair $(\mathbf{X}^{s},\mathbf{U}^{s})$ satisfies the constraints due to the assumption , the constrained problem is also stochastically dissipative at $(\mathbf{X}^{s},\mathbf{U}^{s})$. ∎

### Lemma V.3

The terminal cost $F(X)=\mathbb{E}[X^{\top}PX]$ with $P$ from equation satisfies Assumption IV.7 for $v_{f}=0$ and $(\mathbf{X}^{s},\mathbf{U}^{s})$ from Theorem V.2.

### Proof

Using the relation from and that $X$ and $W(N)$ are independent, we obtain for all $X\in\mathcal{R}(\Omega,\mathbb{R}^{n})$ that with $C_{f}={\rm Tr\,}((P-P^{*})\Sigma_{W})\geq 0$. Note that $C_{f}\geq 0$ must hold since stochastic dissipativity implies that the stationary pair $(\mathbf{X}^{s},\mathbf{U}^{s})$ has optimal stationary cost, cf. \[14, Theorem 5.2\]. ∎ Based on these two results the following corollary summarizes the implications from Corollary IV.9 for the linear-quadratic Gaussian setting of this section.

### Corollary V.4

Let the simplifications of this section and the assumptions of Theorem V.2 hold. Then, we obtain Moreover, if we choose $K=K^{*}$ as the fixed linear feedback we get Input: Fixed stabilizing feedback K ∈ ℝl × n, feasible initial state X0 ∼ 𝒩(μX0, ΣX0) with ΣX0 ≼ ΣEs. Measure the state x0 = X0(ω), set z0 = μX0, ΣE0 = ΣX0, Xcl(0, ω) = x0, Zcl(0, ω) = z0. 1.) Solve the stochastic optimal control problem and obtain the solution v*:= (v0*, …, vN − 1*). 2.) Compute ΣEj + 1 = (A + BK)ΣEj(A + BK)⊤, predict zj + 1 = (A + BK)zj + Bv0*, and set Zcl(j + 1, ω) = zj + 1. 3.) Set Vcl(j, ω) = v0*, apply the feedback Ucl(j, ω) = Kxj + v0* to system and measure the next state xj + 1 = Xcl(j + 1, ω). Algorithm 2 Moment-based indirect feedback SMPC

## NUMERICAL EXAMPLE

In this section we will illustrate our findings by a DC-DC-converter regulation problem, which was already used for case studies in stochastic MPC in The corresponding dynamics are of the form, where and $W(k)\sim\mathcal{N}(0,\Sigma_{W})$ with $\Sigma_{W}=0.1I_{2}\in\mathbb{R}^{2\times 2}$. Additionally, we consider quadratic costs of the form with $Q=\text{diag}$ and $R=5$ and impose a single risk-averse constraint on the first component given by where $\rho(Y)$ denotes one of the risk measures from equation -- with $1-\alpha=0.6$.

To obtain the closed-loop quantities, we generated 15 000 samples using Algorithm 2 with $K=K^{*}$ from Theorem V.2 and a deterministic initial value $X_{0}=(1.8,1.5)^{\top}$. Figure 1 shows the evolution of $\mathbb{E}[X^{cl}_{1}(k)]$, $\text{VaR}_{0.6}(X^{cl}_{1}(k))$, $\text{CVaR}_{0.6}(X^{cl}_{1}(k))$, and $\text{EVaR}_{0.6}(X^{cl}_{1}(k))$ for different choices of $\rho\in\{\mathbb{E}$, $\text{VaR}_{0.6}$, $\text{CVaR}_{0.6}$, $\text{EVaR}_{0.6}\}$. We clearly observe that the constraints are always satisfied, as predicted by Theorem IV.3.

Furthermore, for all $\alpha\in$, $Z\in\mathcal{R}(\Omega,\mathbb{R})$ it holds that Consequently, the restrictiveness of the constraints follows the same ordering, which is also observable in Figure 1.

Figure 1: Evolution of 𝔼[X1cl(k)] (blue), VaR0.6(X1cl(k)) (orange), CVaR0.6(X1cl(k)) (green), and EVaR0.6(X1cl(k)) (red) as well as the upper constraint bound p = 2 (dashed black). The subplots (top to bottom) correspond to the constraints with ρ = 𝔼, ρ = VaR0.6, ρ = CVaR0.6, and ρ = EVaR0.6, respectively.

To compare the performance for different choices of $K$ in Algorithm 2, we constructed a second stabilizing feedback by solving the algebraic Ricatti equation for $\tilde{Q}:=0.01Q$ and $\tilde{R}:=200R$. We then ran Algorithm 2 again using these different choices of $K$, where the constraints in were defined using the conditional value-at-risk $\text{CVaR}_{0.6}$.

As Corollary V.4 indicates, for $K=K^{*}$ the averaged performance should converge to the optimal stationary cost, as can be seen in Figure 2. However, for $K=\tilde{K}$, Corollary V.4 only guarantees that the averaged performance satisfies a suboptimal bound; convergence to the optimal stationary cost is therefore not ensured. Figure 2 shows that the averaged closed-loop performance indeed converges to a value deviating from the optimal stationary cost, demonstrating that the choice of $K$ affects the asymptotic performance of the closed-loop solution not only theoretically but also in practice.

Figure 2: Averaged closed-loop performance of Algorithm 2 for K = K* (blue) and K = K̃ (green) if choosing ρ = VaR0.6 in as well as the optimal stationary cost (red dashed).

## CONCLUSION

We presented an indirect feedback approach for stochastic MPC with linear systems and general risk-averse constraints defined via risk measures. For this algorithm, we derived near-optimal performance bounds for general cost functions. Future research should focus on developing efficient implementations of Algorithm 1 without the simplifications introduced in Section V, constructing suitable terminal costs for the non-quadratic case, or extending the presented results to nonlinear systems, as in for the original chance-constrained algorithm.
