<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sensing-Constrained LQG Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Linear-Quadratic-Gaussian (LQG) control is concerned with the design of an optimal controller and estimator for linear Gaussian systems with imperfect state information. Standard LQG assumes the set of sensor measurements, to be fed to the estimator, to be given. However, in many problems, arising in networked systems and robotics, one may not be able to use all the available sensors, due to power or payload constraints, or may be interested in using the smallest subset of sensors that guarantees the attainment of a desired control goal. In this paper, we introduce the sensing-constrained LQG control problem, in which one has to jointly design sensing, estimation, and control, under given constraints on the resources spent for sensing. We focus on the realistic case in which the sensing strategy has to be selected among a finite set of possible sensing modalities. While the computation of the optimal sensing strategy is intractable, we present the first scalable algorithm that computes a near-optimal sensing strategy with provable sub-optimality guarantees. To this end, we show that a separation principle holds, which allows the design of sensing, estimation, and control policies in isolation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We conclude the paper by discussing two applications of sensing-constrained LQG control, namely, sensing-constrained formation control and resource-constrained robot navigation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional approaches to control of systems with partially observable state assume the choice of sensors used to observe the system is given. The choice of sensors usually results from a preliminary design phase in which an expert designer selects a suitable sensor suite that accommodates estimation requirements (e.g., observability, desired estimation error) and system constraints (e.g., size, cost). Modern control applications, from large networked systems to miniaturized robotics systems, pose serious limitations to the applicability of this traditional paradigm. In large-scale networked systems (e.g., smart grids or robot swarms), in which new nodes are continuously added and removed from the network, a manual re-design of the sensors becomes cumbersome and expensive, and it is simply not scalable. In miniaturized robot systems, while the set of onboard sensors is fixed, it may be desirable to selectively activate only a subset of the sensors during different phases of operation, in order to minimize power consumption.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In both application scenarios, one usually has access to a (possibly large) list of potential sensors, but, due to resource constraints (e.g., cost, power), can only utilize a subset of them. Moreover, the need for online and large-scale sensor selection demands for automated approaches that efficiently select a subset of sensors to maximize system performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by these applications, in this paper we consider the problem of jointly designing control, estimation, and sensor selection for a system with partially observable state.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related work. One body of related work is *control over band-limited communication channels*, which investigates the trade-offs between communication constraints (e.g., data rate, quantization, delays) and control performance (e.g., stability) in networked control systems. Early work provides results on the impact of quantization, finite data rates, and separation principles for LQG design with communication constraints; more recent work focuses on privacy constraints. We refer the reader to the surveys. A second set of related work is *sensor selection and scheduling*, in which one has to select a (possibly time-varying) set of sensors in order to monitor a phenomenon of interest. Related literature includes approaches based on randomized sensor selection, dual volume sampling, convex relaxations, and submodularity. The third set of related works is *information-constrained (or information-regularized)* LQG control. Shafieepoorfard and Raginsky study rationally inattentive control laws for LQG control and discuss their effectiveness in stabilizing the system.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Tanaka and Mitter consider the co-design of sensing, control, and estimation, propose to augment the standard LQG cost with an information-theoretic regularizer, and derive an elegant solution based on semidefinite programming. The main difference between our proposal and is that we consider the case in which the choice of sensors, rather than being arbitrary, is restricted to a finite set of available sensors.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We extend the Linear-Quadratic-Gaussian (LQG) control to the case in which, besides designing an optimal controller and estimator, one has to select a set of sensors to be used to observe the system state. In particular, we formulate the *sensing-constrained* (finite-horizon) LQG problem as the joint design of an optimal control and estimation policy, as well as the selection of a subset of $k$ out of $N$ available sensors, that minimize the LQG objective, which quantifies tracking performance and control effort. We first leverage a separation principle to show that the design of sensing, control, and estimation, can be performed independently. While the computation of the optimal sensing strategy is combinatorial in nature, a key contribution of this paper is to provide the first scalable algorithm that computes a near-optimal sensing strategy with provable sub-optimality guarantees.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We motivate the importance of the sensing-constrained LQG problem, and demonstrate the effectiveness of the proposed algorithm in numerical experiments, by considering two application scenarios, namely, *sensing-constrained formation control* and *resource-constrained robot navigation*, which, due to page limitations, we include in the full version of this paper, located at the authors' websites. All proofs can be found also in the full version of this paper, located at the authors' websites.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sensing-Constrained LQG Control", "weight": 1.0} -->

In this section we formalize the sensing-constrained LQG control problem considered in this paper. We start by introducing the notions of *system*, *sensors*, and *control policies*.

<!-- chunk {"id": "body-0012", "role": "body", "section": "System", "weight": 1.0} -->

We consider a standard discrete-time (possibly time-varying) linear system with additive Gaussian noise: where $x_{t} \in {\mathbb{R}}^{n_{t}}$ represents the state of the system at time $t$, $u_{t} \in {\mathbb{R}}^{m_{t}}$ represents the control action, $w_{t}$ represents the process noise, and $T$ is a finite time horizon. In addition, we consider the system's initial condition $x_{1}$ to be a Gaussian random variable with covariance $\Sigma_{1|0}$, and $w_{t}$ to be a Gaussian random variable with mean zero and covariance $W_{t}$, such that $w_{t}$ is independent of $x_{1}$ and $w_{t'}$ for all $t' = {1,2,\ldots,T}$, $t' \neq t$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sensors", "weight": 1.0} -->

We consider the case where we have a (potentially large) set of available sensors, which take noisy linear observations of the system's state. In particular, let $\mathcal{V}$ be a set of indices such that each index $i \in \mathcal{V}$ uniquely identifies a sensor that can be used to observe the state of the system. We consider sensors of the form where $y_{i,t} \in {\mathbb{R}}^{p_{i,t}}$ represents the measurement of sensor $i$ at time $t$, and $v_{i,t}$ represents the measurement noise of sensor $i$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sensors", "weight": 1.0} -->

We assume $v_{i,t}$ to be a Gaussian random variable with mean zero and positive definite covariance $V_{i,t}$, such that $v_{i,t}$ is independent of $x_{1}$, and of $w_{t'}$ for any $t' \neq t$, and independent of $v_{i',t'}$ for all $t' \neq t$, and any $i' \in \mathcal{V}$, $i' \neq i$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sensors", "weight": 1.0} -->

In this paper we are interested in the case in which we cannot use all the available sensors, and as a result, we need to select a convenient subset of sensors in $\mathcal{V}$ to maximize our control performance (formalized in Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control") below).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Control policies", "weight": 1.0} -->

We consider control policies $u_{t}$ for all $t = {1,2,\ldots,T}$ that are only informed by the measurements collected by the active sensors: Such policies are called *admissible*.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Control policies", "weight": 1.0} -->

In this paper, we want to find a small set of active sensors $\mathcal{S}$, and admissible controllers ${u_{1}{(\mathcal{S})}},{u_{2}{(\mathcal{S})}},\ldots,{u_{T}{(\mathcal{S})}}$, to solve the following sensing-constrained LQG control problem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem 1 (Sensing-constrained LQG control)", "weight": 1.0} -->

Find a sensor set $\mathcal{S} \subset \mathcal{V}$ of cardinality at most $k$ to be active across all times $t = {1,2,\ldots,T}$, and control policies $u_{1:T}{(\mathcal{S})} \triangleq {\{ u_{1}{(\mathcal{S})},}$ $u_{2}{(\mathcal{S})},\ldots,u_{T}{(\mathcal{S})}\}$, that minimize the LQG cost function: where the state-cost matrices $Q_{1},Q_{2},\ldots,Q_{T}$ are positive semi-definite, the control-cost matrices $R_{1},R_{2},\ldots,R_{T}$ are positive definite, and the expectation is taken with respect to the initial condition $x_{1}$, the process noises

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem 1 (Sensing-constrained LQG control)", "weight": 1.0} -->

Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control") generalizes the imperfect state-information LQG control problem from the case where all sensors in $\mathcal{V}$ are active, and only optimal control policies are to be found \[19, Chapter 5\], to the case where only a few sensors in $\mathcal{V}$ can be active, and both optimal sensors and control policies are to be found jointly. While we already noticed that admissible control policies depend on the active sensor set $\mathcal{S}$, it is worth noticing that this in turn implies that the state evolution also depends on $\mathcal{S}$; for this reason we write $x_{t + 1}{(\mathcal{S})}$ in eq. (5. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control")). The intertwining between control and sensing calls for a joint design strategy. In the following section we focus on the design of a jointly optimal control and sensing solution to Problem 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem 1 (Sensing-constrained LQG control)", "weight": 1.0} -->

‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control").

<!-- chunk {"id": "body-0021", "role": "body", "section": "Joint Sensing and Control Design", "weight": 1.0} -->

In this section we first present a separation principle that decouples sensing, estimation, and control, and allows designing them in cascade (Section III-A). We then present a scalable algorithm for sensing and control design (Section III-B).

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Separability of Optimal Sensing and Control Design", "weight": 1.0} -->

We characterize the jointly optimal control and sensing solutions to Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), and prove that they can be found in two separate steps, where first the sensing design is computed, and second the corresponding optimal control design is found.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1 (Certainty equivalence principle)", "weight": 1.0} -->

The control gain matrices $K_{1},K_{2},\ldots,K_{T}$ are the same as the ones that make the controllers $(K_{1}x_{1}$, $K_{1}x_{2},\ldots,K_{T}x_{T})$ optimal for the perfect state-information version of Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), where the state $x_{t}$ is known to the controllers \[19, Chapter 4\].

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1 (Certainty equivalence principle)", "weight": 1.0} -->

1:Time horizon T, available sensor set 𝒱, covariance matrix Σ1|0 of initial condition x1; for all t = 1, 2, …, T, system matrix At, input matrix Bt, LQG cost matrices Qt and Rt, process noise covariance matrix Wt; and for all sensors i ∈ 𝒱, measurement matrix Ci, t, and measurement noise covariance matrix Vi, t. 2:Active sensors $\hat{\mathcal{S}}$, and control matrices K1, …, KT. 3:$\hat{\mathcal{S}}$ is returned by Algorithm 2 that finds a (possibly approximate) solution to the optimization problem in eq.; 4:K1, …, KT are computed using the recursion in eq.. Algorithm 1 Joint Sensing and Control design for Problem 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1 (Certainty equivalence principle)", "weight": 1.0} -->

Theorem 1. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control") decouples the design of the sensing from the controller design. Moreover, it suggests that once an optimal sensor set $\mathcal{S}^{\star}$ is found, then the optimal controllers are equal to $K_{t}{\hat{x}}_{t}{(\mathcal{S})}$, which correspond to the standard LQG control policy. This should not come as a surprise, since for a given sensing strategy, Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control") reduces to standard LQG control.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1 (Certainty equivalence principle)", "weight": 1.0} -->

We conclude this section with a remark providing a more intuitive interpretation of the sensor design step in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2 (Control-aware sensor design)", "weight": 1.0} -->

In order to provide more insight on the cost function in (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")), we rewrite it as: where in the first line we used the fact that ${\Sigma_{t|t}{(\mathcal{S})}} = {{\mathbb{E}}\left\lbrack {{({x_{t} - {{\hat{x}}_{t}{(\mathcal{S})}}})}{({x_{t} - {{\hat{x}}_{t}{(\mathcal{S})}}})}^{\mathsf{T}}} \right\rbrack}$, and in the second line we substituted the definition of $\Theta_{t} = {K_{t}^{\mathsf{T}}M_{t}K_{t}}$ from eq. (8.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2 (Control-aware sensor design)", "weight": 1.0} -->

‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2 (Control-aware sensor design)", "weight": 1.0} -->

From eq. (9. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")), it is clear that each term $\text{tr}{\lbrack{\Theta_{t}\Sigma_{t|t}{(\mathcal{S})}}\rbrack}$ captures the expected control mismatch between the imperfect state-information controller ${u_{t}{(\mathcal{S})}} = {K_{t}{\hat{x}}_{t}{(\mathcal{S})}}$ (which is only aware of the measurements from the active sensors) and the perfect state-information controller $K_{t}x_{t}$. This is an important distinction from the existing sensor selection literature.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2 (Control-aware sensor design)", "weight": 1.0} -->

In particular, while standard sensor selection attempts to minimize the estimation covariance, for instance by minimizing the proposed LQG cost formulation attempts to minimize the estimation error of only the informative states to the perfect state-information controller: for example, the contribution of all $x_{t} - {{\hat{x}}_{t}{(\mathcal{S})}}$ in the null space of $K_{t}$ to the total control mismatch in eq. (9. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) is zero. Hence, in contrast to minimizing the cost function in eq. (10. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")), minimizing the cost function in eq. (9. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) results to a control-aware sensing design.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Scalable Near-optimal Sensing and Control Design", "weight": 1.0} -->

This section proposes a practical design algorithm for Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"). The pseudo-code of the algorithm is presented in Algorithm 1. Algorithm 1 follows the result of Theorem 1. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control"), and jointly designs sensing and control by first computing an active sensor set (line 1 in Algorithm 1) and then computing the control policy (line 2 in Algorithm 1). We discuss each step of the design process in the rest of this section.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B1 Near-optimal Sensing design", "weight": 1.0} -->

The optimal sensor design can be computed by solving the optimization problem in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")). The problem is combinatorial in nature, since it requires to select a subset of elements of cardinality $k$ out of all the available sensors that induces the smallest cost.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B1 Near-optimal Sensing design", "weight": 1.0} -->

In this section we propose a greedy algorithm, whose pseudo-code is given in Algorithm 2, that computes a (possibly approximate) solution to the problem in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")). Our interest towards this greedy algorithm is motivated by the fact that it is scalable (in Section IV we show that its complexity is linear in the number of available sensors) and is provably close to the optimal solution of the problem in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) (we provide suboptimality bounds in Section IV).

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B1 Near-optimal Sensing design", "weight": 1.0} -->

Algorithm 2 computes the matrices $\Theta_{t}$ ($t = {1,2,\ldots,T}$) which appear in the cost function in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) (line 3). Note that these matrices are independent on the choice of sensors. The set of active sensors $\hat{\mathcal{S}}$ is initialized to the empty set (line 4). The "while loop" in line 5 will be executed $k$ times and at each time a sensor is greedily added to the set of active sensors $\hat{\mathcal{S}}$. In particular, the "for loop" in lines 6-14 computes the estimation covariance resulting by adding a sensor to the current active sensor set and the corresponding cost (line 13). Finally, the sensor inducing the smallest cost is selected (line 15) and added to the current set of active sensors (line 16).

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B2 Control policy design", "weight": 1.0} -->

The optimal control design is computed as in eq. (7. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")), where the control policy matrices $K_{1},K_{2},\ldots,K_{T}$ are obtained from the recursion in eq. (8. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")).

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B2 Control policy design", "weight": 1.0} -->

In the following section we characterize the approximation and running-time performance of Algorithm 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Performance Guarantees for Joint Sensing and Control Design", "weight": 1.0} -->

We prove that Algorithm 1 is the first scalable algorithm for the joint sensing and control design Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), and that it achieves a value for the LQG cost function in eq. (5. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control")) that is finitely close to the optimal. We start by introducing the notion of supermodularity ratio (Section IV-A), which will enable to bound the sub-optimality gap of Algorithm 1 (Section IV-B).

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Supermodularity ratio of monotone functions", "weight": 1.0} -->

We define the supermodularity ratio of monotone functions. We start with the notions of monotonicity and supermodularity.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Performance Analysis for Algorithm 1", "weight": 1.0} -->

We quantify Algorithm 1's running time, as well as, Algorithm 1's approximation performance, using the notion of supermodularity ratio introduced in Section IV-A. We conclude the section by showing that for appropriate LQG cost matrices $Q_{1},Q_{2},\ldots,Q_{T}$ and $R_{1},R_{2},\ldots,R_{T}$, Algorithm 1 achieves near-optimal approximate performance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Case 1 where $\\gamma_{g}$'s bound in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control\")) increases", "weight": 1.0} -->

When the fraction ${{\lambda_{\min}{({\sum_{t = 1}^{T}\Theta_{t}})}}/\lambda_{\max}}{({\sum_{t = 1}^{T}\Theta_{t}})}$ increases to $1$, then the right-hand-side in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) increases. Equivalently, the right-hand-side in ineq. (13.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Case 1 where $\\gamma_{g}$'s bound in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control\")) increases", "weight": 1.0} -->

To see this, consider for example that ${\lambda_{\max}{(\Theta_{t})}} = {\lambda_{\min}{(\Theta_{t})}} = \lambda$; then, the cost function in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) that Algorithm 1 minimizes to select the active sensor set becomes Overall, it is easier for Algorithm 1 to approximate a solution to Problem 1 as the cost function in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) becomes the cost function in the standard sensor selection problems where one minimizes the total estimation covariance as in eq. (10. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Case 2 where $\\gamma_{g}$'s bound in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control\")) increases", "weight": 1.0} -->

When either the numerators of the last two fractions in the right-hand-side of ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) increase or the denominators of the last two fractions in the right-hand-side of ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) decrease, then the right-hand-side in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) increases. In particular, the numerators of the last two fractions in right-hand-side of ineq. (13.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Case 2 where $\\gamma_{g}$'s bound in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control\")) increases", "weight": 1.0} -->

‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) capture the estimation quality when all available sensors in $\mathcal{V}$ are used, via the terms of the form $\lambda_{\min}{\lbrack{\Sigma_{t|t}{(\mathcal{V})}}\rbrack}$ and $\lambda_{\min}{\lbrack{{\overline{C}}_{i,t}\Sigma_{t|t}{(\mathcal{V})}{\overline{C}}_{i,t}^{\mathsf{T}}}\rbrack}$. Interestingly, this suggests that the right-hand-side of ineq. (13.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Case 2 where $\\gamma_{g}$'s bound in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control\")) increases", "weight": 1.0} -->

‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) increases when the available sensors in $\mathcal{V}$ are inefficient in achieving low estimation error, that is, when the terms of the form $\lambda_{\min}{\lbrack{\Sigma_{t|t}{(\mathcal{V})}}\rbrack}$ and $\lambda_{\min}{\lbrack{{\overline{C}}_{i,t}\Sigma_{t|t}{(\mathcal{V})}{\overline{C}}_{i,t}^{\mathsf{T}}}\rbrack}$ increase. Similarly, the denominators of the last two fractions in right-hand-side of ineq. (13.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Case 2 where $\\gamma_{g}$'s bound in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control\")) increases", "weight": 1.0} -->

‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) capture the estimation quality when no sensors are used, via the terms of the form $\lambda_{\max}{\lbrack{\Sigma_{t|t}{(\varnothing)}}\rbrack}$ and $\lambda_{\max}{\lbrack{{\overline{C}}_{i,t}\Sigma_{t|t}{(\varnothing)}{\overline{C}}_{i,t}^{\mathsf{T}}}\rbrack}$. This suggests that the right-hand-side of ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) increases when the measurement noise increases.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Case 2 where $\\gamma_{g}$'s bound in ineq. (13. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control\")) increases", "weight": 1.0} -->

We next give a control-level equivalent condition to Theorem 3. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")'s condition ${\sum_{t = 1}^{T}\Theta_{t}} \succ 0$ for non-zero ratio $\gamma_{g}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We consider two application scenarios for the proposed sensing-constrained LQG control framework: *sensing-constrained formation control* and *resource-constrained robot navigation*. We present a Monte Carlo analysis for both scenarios, which demonstrates that (i) the proposed sensor selection strategy is near-optimal, and in particular, the resulting LQG-cost (tracking performance) matches the optimal selection in all tested instances for which the optimal selection could be computed via a brute-force approach, (ii) a more naive selection which attempts to minimize the state estimation covariance (rather than the LQG cost) has degraded LQG tracking performance, often comparable to a random selection, (iii) in the considered instances, a clever selection of a small subset of sensors can ensure an LQG cost that is close to the one obtained by using all available sensors, hence providing an effective alternative for control under sensing constraints.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

(b) unmanned aerial robot Figure 1: Examples of applications of the proposed sensing-constrained LQG control framework: (a) sensing-constrained formation control and (b) resource-constrained robot navigation.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

Simulation setup. The first application scenario is illustrated in Fig. 1(a). A team of $n$ agents (blue triangles) moves in a 2D scenario. At time $t = 1$, the agents are randomly deployed in a ${{10m} \times 10}m$ square and their objective is to reach a target formation shape (red stars); in the example of Fig. 1(a) the desired formation has an hexagonal shape, while in general for a formation of $n$, the desired formation is an equilateral polygon with $n$ vertices.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

Each robot $i$ is equipped with a GPS receiver, which can measure the agent position $p_{i}$ with a covariance $V_{{gps},i} = {2 \cdot \mathbf{I}_{2}}$. Moreover, the agents are equipped with lidar sensors allowing each agent $i$ to measure the relative position of another agent $j$ with covariance $V_{{lidar},{ij}} = {0.1 \cdot \mathbf{I}_{2}}$. The agents have very limited on-board resources, hence they can only activate a subset of $k$ sensors. Hence, the goal is to select the subset of $k$ sensors, as well as to compute the control policy that ensure best tracking performance, as measured by the LQG objective.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

For our tests, we consider two problem setups. In the first setup, named *homogeneous formation control*, the LQG weigh matrix $Q$ is a block diagonal matrix with $4 \times 4$ blocks, with each block $i$ chosen as $Q_{i} = {0.1 \cdot \mathbf{I}_{4}}$; since each $4 \times 4$ block of $Q$ weights the tracking error of a robot, in the homogeneous case the tracking error of all agents is equally important. In the second setup, named *heterogeneous formation control*, the matrix $Q$ is chose as above, except for one of the agents, say robot 1, for which we choose $Q_{1} = {10 \cdot \mathbf{I}_{4}}$; this setup models the case in which each agent has a different role or importance, hence one weights differently the tracking error of the agents. In both cases the matrix $R$ is chosen to be the identity matrix. The simulation is carried on over $T$ time steps, and $T$ is also chosen as LQG horizon.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

Results are averaged over 100 Monte Carlo runs: at each run we randomize the initial estimation covariance $\Sigma_{1|0}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

Compared techniques. We compare five techniques. All techniques use an LQG-based estimator and controller, and they only differ by the selections of the sensors used. The first approach is the optimal sensor selection, denoted as optimal, which attains the minimum of the cost function in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")), and that we compute by enumerating all possible subsets; this brute-force approach is only viable when the number of available sensors is small. The second approach is a pseudo-random sensor selection, denoted as random^∗^, which selects all the GPS measurements and a random subset of the lidar measurements; note that we do not consider a fully random selection since in practice this often leads to an unobservable system, hence causing divergence of the LQG cost. The third approach, denoted as logdet, selects sensors so to minimize the average $\log\det$ of the estimation covariance over the horizon; this approach resembles and is agnostic to the control task.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

The fourth approach is the proposed sensor selection strategy, described in Algorithm 2, and is denoted as s-LQG. Finally, we also report the LQG performance when all sensors are selected. This approach is denoted as allSensors.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

Results. The results of our numerical analysis are reported in Fig. 2. When not specified otherwise, we consider a formation of $n = 4$ agents, which can only use a total of $k = 6$ sensors, and a control horizon $T = 20$. Fig. 2(a) shows the LQG cost attained by the compared techniques for increasing control horizon and for the homogeneous case. We note that, in all tested instance, the proposed approach s-LQG matches the optimal selection optimal, and both approaches are relatively close to allSensors, which selects all the available sensors ($\frac{n + n^{2}}{2}$). On the other hand logdet leads to worse tracking performance, and it is often close to the pseudo-random selection random^∗^. These considerations are confirmed by the heterogeneous setup, shown in Fig. 2(b).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

In this case the separation between the proposed approach and logdet becomes even larger; the intuition here is that the heterogeneous case rewards differently the tracking errors at different agents, hence while logdet attempts to equally reduce the estimation error across the formation, the proposed approach s-LQG selects sensors in a task-oriented fashion, since the matrices $\Theta_{t}$ for all $t = {1,2,\ldots,T}$ in the cost function in eq. (6. ‣ III-A Separability of Optimal Sensing and Control Design ‣ III Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control")) incorporate the LQG weight matrices.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

Fig. 2(c) shows the LQG cost attained by the compared techniques for increasing number of selected sensors $k$ and for the homogeneous case. We note that for increasing number of sensors all techniques converge to allSensors (the entire ground set is selected). As in the previous case, the proposed approach s-LQG matches the optimal selection optimal. Fig. 2(d) shows the same statistics for the heterogeneous case. We note that in this case logdet is inferior to s-LQG even in the case with small $k$. Moreover, an interesting fact is that s-LQG matches allSensors already for $k = 7$, meaning that the LQG performance of the sensing-constraint setup is indistinguishable from the one using all sensors; intuitively, in the heterogeneous case, adding more sensors may have marginal impact on the LQG cost (e.g., if the cost rewards a small tracking error for robot 1, it may be of little value to take a lidar measurement between robot 3 and 4).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

This further stresses the importance of the proposed framework as a parsimonious way to control a system with minimal resources.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Sensing-constrained formation control", "weight": 1.0} -->

Fig. 2(e) and Fig. 2(f) show the LQG cost attained by the compared techniques for increasing number of agents, in the homogeneous and heterogeneous case, respectively. To ensure observability, we consider $k = {{round}\left( {1.5n} \right)}$, i.e., we select a number of sensors $50\%$ larger than the smallest set of sensors that can make the system observable. We note that optimal quickly becomes intractable to compute, hence we omit values beyond $n = 4$. In both figures, the main observation is that the separation among the techniques increases with the number of agents, since the set of available sensors quickly increases with $n$. Interestingly, in the heterogeneous case s-LQG remains relatively close to allSensors, implying that for the purpose of LQG control, using a cleverly selected small subset of sensors still ensures excellent tracking performance.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Resource-constrained robot navigation", "weight": 1.0} -->

Simulation setup. The second application scenario is illustrated in Fig. 1(b). An unmanned aerial robot (UAV) moves in a 3D scenario, starting from a randomly selected initial location. The objective of the UAV is to land, and more specifically, it has to reach the position $\lbrack 0,\;0,\;0\rbrack$ with zero velocity. The UAV is modeled as a double-integrator, with state $x_{i} = {\lbrack{p_{i}v_{i}}\rbrack}^{\mathsf{T}} \in {\mathbb{R}}^{6}$ ($p_{i}$ is the 3D position of agent $i$, while $v_{i}$ is its velocity), and can control its own acceleration $u_{i} \in {\mathbb{R}}^{3}$; the process noise is chosen as $W = \mathbf{I}_{6}$. The UAV is equipped with multiple sensors.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Resource-constrained robot navigation", "weight": 1.0} -->

It has an on-board GPS receiver, measuring the UAV position $p_{i}$ with a covariance $2 \cdot \mathbf{I}_{3}$, and an altimeter, measuring only the last component of $p_{i}$ (altitude) with standard deviation $0.5m$. Moreover, the UAV can use a stereo camera to measure the relative position of $\ell$ landmarks on the ground; for the sake of the numerical example, we assume the location of each landmark to be known only approximately, and we associate to each landmark an uncertainty covariance (red ellipsoids in Fig. 1(b)), which is randomly generated at the beginning of each run. The UAV has limited on-board resources, hence it can only activate a subset of $k$ sensors. For instance, the resource-constraints may be due to the power consumption of the GPS and the altimeter, or may be due to computational constraints that prevent to run multiple object-detection algorithms to detect all landmarks on the ground.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Resource-constrained robot navigation", "weight": 1.0} -->

Similarly to the previous case, we phrase the problem as a sensing-constraint LQG problem, and we use $Q = {{diag}\left( {\lbrack{1e^{- 3}},{\;1e^{- 3}},\;10,{\;1e^{- 3}},{\;1e^{- 3}},\;10\rbrack} \right)}$ and $R = \mathbf{I}_{3}$. Note that the structure of $Q$ reflects the fact that during landing we are particularly interested in controlling the vertical direction and the vertical velocity (entries with larger weight in $Q$), while we are less interested in controlling accurately the horizontal position and velocity (assuming a sufficiently large landing site). In the following, we present results averaged over 100 Monte Carlo runs: in each run, we randomize the covariances describing the landmark position uncertainty.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Resource-constrained robot navigation", "weight": 1.0} -->

Compared techniques. We consider the five techniques discussed in the previous section. As in the formation control case, the pseudo-random selection random^∗^ always includes the GPS measurement (which alone ensures observability) and a random selection of the other available sensors.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Resource-constrained robot navigation", "weight": 1.0} -->

Results. The results of our numerical analysis are reported in Fig. 3. When not specified otherwise, we consider a total of $k = 3$ sensors to be selected, and a control horizon $T = 20$. Fig. 3(a) shows the LQG cost attained by the compared techniques for increasing control horizon. For visualization purposes we plot the cost normalized by the horizon, which makes more visible the differences among the techniques. Similarly to the formation control example, s-LQG matches the optimal selection optimal, while logdet and random^∗^ have suboptimal performance.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Resource-constrained robot navigation", "weight": 1.0} -->

Fig. 3(b) shows the LQG cost attained by the compared techniques for increasing number of selected sensors $k$. Clearly, all techniques converge to allSensors for increasing $k$, but in the regime in which few sensors are used s-LQG still outperforms alternative sensor selection schemes, and matches in all cases the optimal selection optimal.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this paper, we introduced the *sensing-constrained LQG control* Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), which is central in modern control applications that range from large-scale networked systems to miniaturized robotics networks. While the computation of the optimal sensing strategy is intractable, We provided the first scalable algorithm for Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), Algorithm 1, and under mild conditions on the system and LQG matrices, proved that Algorithm 1 computes a near-optimal sensing strategy with provable sub-optimality guarantees. To this end, we showed that a separation principle holds, which allows the design of sensing, estimation, and control policies in isolation. We motivated the importance of the sensing-constrained LQG Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), and demonstrated the effectiveness of Algorithm 1, by considering two application scenarios: *sensing-constrained formation control*, and *resource-constrained robot navigation*.
