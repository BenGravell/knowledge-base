<!-- arxiv-full-text:v1 {"arxiv_id": "2303.10260", "source": "arxiv-html"} -->

## Introduction

Linear quadratic tracking (LQT) is the natural generalization of the optimal linear quadratic regulator (LQR) for the setting where the goal is not to drive the state to the origin but to a certain reference. The reference trajectory need not be necessarily time-invariant and in the classic formulation of the problem is known in advance. This is a reasonable assumption in many practical applications, such as aircraft tracking of a predetermined trajectory or precision control in industrial process engineering. However, in other scenarios, for example, in tracking the output of a secondary agent whose dynamics are unknown and/or the measurements are imperfect, the prediction of the next reference point is non-trivial. In these cases the reference trajectory is only revealed sequentially, after the action has been taken, suggesting the need for an online or adaptive algorithm that will learn or adapt to the dynamics of the reference-generating agent.

In this letter, we study the LQT problem with an unknown reference trajectory. We pose the problem in the framework of online convex optimization (OCO) subject to the dynamics constraint of the system. In particular, the tracking problem is recast into an equivalent regulation problem with a redefined state that evolves with linear dynamics subject to additive adversarial disturbances. In the spirit of online decision-making under computational and memory constraints, our goal is to develop a gradient-based algorithm that is fast and simple to implement and requires no large memory. To this end, we show how classical online gradient descent (OGD) may fail to achieve optimal tracking and propose a modified algorithm, called SS-OGD (steady state OGD) that is guaranteed to achieve the goal under mild conditions. Given the online nature of the algorithm, its performance is quantified through the means of dynamic regret that compares the accumulated finite time cost of a given algorithm to that of an optimal benchmark that solves the LQT problem with an *a priori* knowledge of the reference trajectory. We provide a dynamic regret bound that scales linearly with the path length of the reference trajectory.

The LQT problem for sequentially revealed adversarial reference states is studied mostly with policy regret guarantees, with one of the first works suggesting a relatively computationally heavy algorithm. In a more recent line of work the authors introduce a memory-based, gradient descent algorithm and in tackle the constrained tracking problem. Several works also provide dynamic regret guarantees for tracking of unknown targets, however, their settings differ from ours. In, the authors analyze an output tracking scheme but assume an iterative setting, while in a window of predictions is available. Without predictions, their regret order is determined by that of a fixed oracle controller. In, the authors also provide a lower bound for the dynamic regret in terms of the reference path length, matching the same order as our proposed scheme. Gradient-based algorithms, as the ones we study, have also been developed in the context of online feedback optimization. There, in contrast to our setting, the dynamics are generally assumed to be unknown, but, crucially, the cost functions are fixed over the horizon, and the regret is not analyzed. Several recent works, e.g., consider a similar setting with time-varying costs. These, however, are allowed to be estimated offline by training, incompatible with our setting, and without regret guarantees.

Notation: The set of positive real numbers is denoted by ${\mathbb{R}}_{+}$ and that of non-negative integers by $\mathbb{N}$. For a matrix $W$ the spectral radius and the spectral norm are denoted by $\rho{(W)}$, and $\| W\|$, respectively, and $\lambda_{min}{(W)}$ denotes its minimum eigenvalue. We define $\lambda_{W}:=\frac{1 + {\rho{(W)}}}{2}$; one can show that if ${\rho{(W)}} < 1$, there exists a $c_{W} \in {\mathbb{R}}_{+}$ such that for all $k \geq 1$ ${\| W^{k}\|} \leq {c_{W}\lambda_{W}^{k}}$. For a given vector $x$, its Euclidean norm is denoted by $\| x\|$, and the one weighted by some matrix $Q$ by ${\| x\|}_{Q} = \sqrt{x^{\top}Qx}$.

## Problem Statement

Consider the discrete-time linear time-invariant (LTI) dynamical system, given by where $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$ are the state and input vectors respectively, and ${A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times m}}$ are *known* system matrices. The goal of the optimal LQT problem is the tracking of a time-varying signal $r_{t} \in {\mathbb{R}}^{n}$, such that the cost is minimized for some weighting matrices $Q \in {\mathbb{R}}^{n \times n}$ and $R \in {\mathbb{R}}^{m \times m}$, and where $P \in {\mathbb{R}}^{n \times n}$ is the solution of the discrete algebraic Riccati equation (DARE)^11^1The final cost matrix is taken to be $P$ for simplicity. For other values of the terminal cost matrix the results still hold up to an additional constant.

The LQT problem can be recast into an equivalent LQR formulation by considering instead the dynamics with $e_{t}:={x_{t} - r_{t}}$ and $w_{t}:={{Ar_{t}} - r_{t + 1}}$ for all $t \in {\mathbb{N}}$, and the corresponding cost function When the reference trajectory $r_{t}$, $t \in {\mathbb{N}}$ is known at the initial time a closed form solution for the optimal controller that solves the following optimization problem can be obtained This controller, often referred to as the optimal offline noncausal controller, can be represented as a linear feedback on the current state and the future reference.

Departing from the classical formulation of tracking control, we assume that the reference signal is *unknown* and is only revealed sequentially after the control input has been applied, similar to the adversarial tracking framework. In particular, for each time step $0 \leq t < T$: The state $x_{t}$ and the reference state $r_{t}$ are observed, The agent decides on an input $u_{t}$, The environment decides on the next reference $r_{t + 1}$, which, in turn, determines $w_{t}$. The error state then evolves according to, incurring the following cost for the agent Note that the online cost, depends on the current input $u_{t}$ and the unknown disturbance $w_{t}$, and is therefore unknown to the decision maker at timestep $t$; it is revealed only at time $t + 1$, after the input $u_{t}$ has been applied to the system. Our problem formulation fits the online learning framework, with the extra challenge of inherent dynamics. The goal of the controller is then to minimize the online cumulative cost^22^2For consistency we require ${c_{T - 1}{(e_{T - 1},u_{T - 1})}}:={{\|{{Ae_{T - 1}} + {Bu_{T - 1}} + w_{T - 1}}\|}_{P}^{2} + {\| u_{T - 1}\|}_{R}^{2}}$. To forego unnecessary cluttering of the notation, the separate treatment of the last timestep is implied implicitly.

This is the same as the LQR cost without the initial state, implying that the minimizers of both problems coincide.

We quantify the finite-time performance of the algorithm through the means of dynamic regret. Consider a policy $\pi:{\mathcal{I}\rightarrow{\mathbb{R}}^{m}}$, mapping from the available information set, $\mathcal{I}$, to the control input space. Its dynamic regret, given a disturbance signal $w$, is defined as where $u^{\pi}$ is the input generated by $\pi$ and $u^{\star}$ is given.

We allow the trajectory ${r_{t},t} \in {\mathbb{N}}$ to be arbitrary, as long as it remains bounded.

### Assumption 1 (Bounded trajectory)

There exists a $\overline{R} \in {\mathbb{R}}_{+}$, such that ${\| r_{t}\|} \leq \overline{R}$ for all $t \in {\mathbb{N}}$.

The more abruptly a trajectory changes, the harder it is to achieve good tracking performance, especially if the trajectory is unknown beforehand. To capture this inherent complexity of the problem with dynamic regret, we use the well-established notion of path length,.

### Definition 2.1 (Path Length)

The path length of a reference trajectory $r_{0:T} \in {\mathbb{R}}^{n{({T + 1})}}$ is ${L{(T)}} = {\sum_{t = 0}^{T - 1}{\|{\Delta r_{t}}\|}}$, where ${\Delta r_{t}} = {r_{t + 1} - r_{t}}$.

For more random and abrupt changes in the trajectory, the path length is higher, and one expects the performance of an online algorithm to deteriorate. Likewise, an efficient algorithm should improve as path length decreases. This is captured quantitatively by showing at least a linear dependence of the algorithm's regret on the path length. One can instead choose the complexity term to be the path length of the artificial disturbances $w_{0:{T - 1}} \in {\mathbb{R}}^{n{(T)}}$. The resulting path length will then decrease the closer the reference dynamics are to the given system in a certain operator norm, but will scale linearly with time in the case of a constant mismatch between the two. Since we only assume bounded references, we allow for potentially random references without any underlying dynamics. Hence, we choose $L{(T)}$ as our complexity term. Under the following standard assumptions on stabilisability and detectablity the LQR problem is well-posed.

### Assumption 2 (LQR is well-posed)

The system $(A,B)$ is stabilisable, the pair $(Q^{\frac{1}{2}},A)$ is detectable and $R \succ 0$.

## The SS-OGD Algorithm

We consider a control law of the following form where $K = {{({R + {B^{\top}PB}})}^{- 1}B^{\top}PA}$ is fixed to the optimal LQR gain, and $v_{t}$ is a correction term that should account for the unknown disturbances; we will employ online learning techniques to update the latter term.

We investigate the performance of online gradient descent based algorithms. Consider the following "naive" update where $v_{t}$ is updated in the opposite direction of the gradient of the most recent cost. Here $\alpha \in R_{+}$ is the step size and the recursion starts from some $v_{0} \in {\mathbb{R}}^{m}$. As the online objective is quadratic, the gradient is available in a closed form and the update can be represented as $v_{t} = {v_{t - 1} - {2\alpha{({{Ru_{t - 1}} + {B^{\top}Qe_{t}}})}}}$. For the case of a constant reference signal and an underactuated system, the algorithm can converge to a point that is not necessarily the optimal one with respect to infinite horizon cost minimization. This is due to the greedy behavior of the update that does not take into account future dynamics. In this section, we propose a simple modification to this myopic OGD update, called SS-OGD that accounts for this shortcoming.

To motivate the SS-OGD update, we consider the steady state solution of in closed-loop with the affine control law when we fix $v_{i} = \overline{v}$ and $r_{i} = \overline{r}$ for all subsequent timesteps $i \geq t$. Defining $S:={{({{I - A} + {BK}})}^{- 1}B}$, a closed form solution for the steady state and input is given by ^33^3Note that $\overline{x}$ and $\overline{u}$ are both defined for a given $\overline{v}$ and $\overline{r}$. The dependence is left for simplicity One can then find the $\overline{v}$ which will recover the optimal steady state solution by minimizing the time-averaged infinite horizon steady state cost. For $\overline{x}$ and $\overline{u}$ defined as, this is equivalent to minimizing whose gradient is given by Since $r$ is, in general not constant, and the steady state condition is not satisfied, we suggest a new OGD-like update rule on the bias term $v_{t}$ that is a modified version of the gradient. Specifically, the feedback on the steady state error, $\overline{x} - \overline{r}$, is replaced with the measured error, $x_{t} - r_{t}$, and the steady state input, $\overline{u}$, with the latest applied input, $u_{t - 1}$. This results in the following update, named SS-OGD The cost $c$ in is defined for the steady state $\overline{x}$ and input $\overline{u}$ and is thus decoupled from the true online cost $c_{t}$ in that reflects the current $e_{t}$ and $u_{t}$. These are, in general, not at a steady state and $r_{t}$ is not constant. Thus, $c$ is only an auxiliary, hallucinated cost to construct the update.

### Lemma 3.1

Under Assumption 2 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees"), is strictly convex in $\overline{v}$ for any $K \in {\mathbb{R}}^{m \times n}$, for which ${\rho{({A - {BK}})}} < 1$.

### Proof 3.2

If the matrix $I - {KS}$ is singular, there exists a $v \in {\mathbb{R}}^{n}$, such that $v = {KSv}$. Then, for $x = {Sv}$, at steady state $x = {{Ax} + {B{({{KSv} - {Kx}})}}} = {Ax}$. Given the detectability condition of the pair $(Q^{\frac{1}{2}},A)$, for any unstable, or marginally stable mode of $A$, the matrix $Q \succ 0$. This ensures that the matrix ${S^{\top}QS} + {{({I - {KS}})}^{\top}R{({I - {KS}})}}$ is positive definite, which is equivalent to the strong convexity of.

The modifications from the standard OGD can be interpreted as incorporating the dynamics information in the update rule. As we show in the following, this ensures that in the limit, if the algorithm is stable and the reference signal is constant, the SS-OGD converges to the same point as the solution of the LQR problem minimizing. Moreover, through the feedback on the state $e_{t}$ and input $u_{t - 1}$, the update rule incorporates a proportional integral (*PI*) control on the measured state. This is demonstrated on a quadrotor control example in Section 5, where, with the inherent integrator dynamics of the quadrotor, the SS-OGD achieves a zero steady state error in tracking a position reference signal with a constant rate of change.

To study the SS-OGD update rule, we introduce the following evolution of the combined system optimizer dynamics where $z_{t}:={\lbrack{v_{t}^{\top}e_{t}^{\top}}\rbrack}^{\top}$, the matrices $\overset{\sim}{A} \in {\mathbb{R}}^{p \times p}$ and $\overset{\sim}{B} \in {\mathbb{R}}^{p \times n}$ are defined in Appendix 7 and $p:={m + n}$.

### Assumption 3

The step size $\alpha > 0$ is such that ${\rho{(\overset{\sim}{A})}} < 1$.

Since all the variables in $\overset{\sim}{A}$ are known *a priori*, we show that there always exists an $\alpha$ satisfying this assumption and provide a sufficient condition in Appendix 7.

The following theorem shows that, for a constant $w_{t} = \overline{w}$ for all $0 \leq t < T$, SS-OGD update converges to the solution of with $r_{T + 1}:=r_{T}$. The solution of can be interpreted as the steady state and steady state input that minimize the infinite horizon time-averaged cost.

### Theorem 3.3

Under Assumptions 2 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees") and 3, if $w_{t} = \overline{w}$ for all $t \in {\mathbb{N}}$, the steady state of coincides with the solution of.

The proof of the theorem is provided in Appendix 8. As a corollary, for a constant signal $r_{t} = \overline{r}$, the update converges to the solution of. Note that this is not always true for the naive OGD update, as its fixed point for a fixed disturbance is not necessarily the same as.

## Regret Analysis

To characterize the effectiveness of the algorithm for time-varying signals and to provide finite time guarantees, we analyze its dynamic regret and show that it scales with the path length. The next theorem summarizes this main result.

### Theorem 4.1

Under Assumptions 1 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees"), 2 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees") and 3, the dynamic regret of the SS-OGD algorithm scales with the path length The proof of the theorem is provided in Section 4.1 after some auxiliary results.

### Lemma 4.2

(Cost Difference Lemma) For any two policies $\pi_{1},\pi_{2}$ where $e_{t}^{\pi_{2}}$ is the state at time $t$ achieved by applying the policy $\pi_{2}$, $u_{t}^{\pi_{2}}$ is the input generated by the policy $\pi_{2}$ at time t, ${\mathcal{Q}_{t}^{\pi_{1}}{(e,u)}} = {{\| e\|}_{Q}^{2} + {\| u\|}_{R}^{2} + {J_{t + 1}{({{Ae} + {Bu} + w_{t}},u^{\pi_{1}})}}}$ is the Q-function for policy $\pi_{1}$ and $J_{i}{(e_{i},u)}$ is the cost-to-go at time step $i$, with initial state $e_{i}$ and control signal $u$.

The proof is omitted, as it is identical to the one for Markov decision processes. The following result for a general policy $\pi$ akin to the result in follows.

### Lemma 4.3

Under Assumption 2 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees"), given the system dynamics and cost function, the dynamic regret of any policy $\pi$ is given by where $u_{t}^{\pi}$ and $u_{t}^{\star}$ denote the inputs generated by $\pi$, and the optimal policy, both evaluated at the policy state $e_{t}^{\pi}$ at time $t$.

### Proof 4.4

Let $\mathcal{Q}_{t}^{\star}{(e,u)}$ be the optimal Q-function, associated with the optimal control law $u_{t}^{\star}$. Then, using Lemma 4.2 the dynamic regret of the policy $\pi$ is given by i.e., a sum of differences of $\mathcal{Q}_{t}^{\star}$, evaluated at $u_{t}^{\pi}$ and $u^{\star}$, its minimizer. For an input, $u \in {\mathbb{R}}^{m}$, and some $f \in {\mathbb{R}}^{m}$, $g \in {\mathbb{R}}$ where the last equality follows from the closed form of $J_{t + 1}{(x,u^{\star})}$ as an extended quadratic function of $x$. Thus, since $u_{t}^{\star}$ minimizes an extended quadratic function, ${{\mathcal{Q}_{t}^{\star}{(e_{t}^{\pi},u_{t}^{\pi})}} - {\mathcal{Q}_{t}^{\star}{(e_{t}^{\pi},u_{t}^{\star})}}} = {\|{u_{t}^{\pi} - u_{t}^{\star}}\|}_{({R + {B^{T}PB}})}^{2}$.

For future references, we also recall the Cauchy Product inequality defined for two finite series ${\{ a_{i}\}}_{i = 1}^{T}$ and ${\{ b_{i}\}}_{i = 1}^{T}$:

### Proof of Theorem 4.1

As Lemma 4.3 suggests, the dynamic regret depends on the stepwise control input difference, where ${\Delta w_{i,t}} = {w_{i} - w_{t}}$ and for all $0 \leq t \leq i < T$, We proceed by bounding each of the above terms separately.

Term $s_{\mathbf{2},t}$: This captures the deviation of the artificial disturbance term from the one fixed at timestep $t$. By noting that $\Delta w_{i,t}$ can be represented as a telescopic sum, Term $s_{\mathbf{3},t}$: This captures the effect of truncating the infinite horizon problem to a finite one where $\overline{R}$ is defined in Assumption 1 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees").

Term $s_{\mathbf{1},t}$: This captures the cost of performing a gradient step in the direction of the steady state solution instead of the full solution, for a fixed $w_{t}$. Note that $- {\sum_{i = t}^{\infty}{K_{w}^{i,t}w_{t}}}$ is the solution of the following infinite horizon optimization problem and is independent of the initial state which is equivalent to. Hence, by Theorem 3.3 where ${\hat{z}}_{t} = {\lbrack{{\hat{v}}_{t}^{\top}{\hat{e}}_{t}^{\top}}\rbrack}^{\top}:={{({I - \overset{\sim}{A}})}^{- 1}\overset{\sim}{B}w_{t}}$ is the steady state of the SS-OGD dynamics for a given $w_{t}$. This term captures the difference between the SS-OGD update term $v_{t}$ and the steady state value ${\hat{v}}_{t}$ for that timestep. We look at the evolution of the augmented state difference; for all $0 < t \leq T$ Then $\varepsilon_{t} = {{{\overset{\sim}{A}}^{t}\varepsilon_{0}} + {\sum_{i = 0}^{t - 1}{{\overset{\sim}{A}}^{i}\left({{\hat{z}}_{t - i - 1} - {\hat{z}}_{t - i}} \right)}}}$ for a given time step $0 \leq t \leq T$. Under Assumption 3 Defining $h = {\left\| {\left({I - \overset{\sim}{A}} \right)^{- 1}\overset{\sim}{B}} \right\|\left({{\| A\|} + 1} \right)}$, $b = {{{({h + 1})}\overline{R}} + {\| x_{0}\|} + {\| v_{0}\|}}$, and $\overline{\varepsilon} = {c_{\overset{\sim}{A}}\left({b + \frac{2\overline{R}h}{1 - \lambda_{\overset{\sim}{A}}}} \right)}$ There exist ${s_{2},s_{3}} \in {\mathbb{R}}_{+}$, such that ${s_{2,t} \leq s_{2}},{s_{3,t} \leq s_{3}}$ and from $s_{1,t} \leq \overline{\varepsilon}$ for all $t \in {\mathbb{N}}$. Using Lemma 4.3 and denoting $\overline{P} = {4{\|{R + {B^{\top}PB}}\|}}$ Note that, unlike the regret bound of the FOSS algorithm, the constant multiplying $L{(T)}$ above does not depend on $\overline{R}$, but only on system parameters. This implies that the complexity term captures only the relative distance of the references and is not amplified by their upper bounds.

### Steady State Benchmark

Given Theorem 3.3, one can also compare SS-OGD to the steady state optimal solution for each timestep. Consider for all $0 \leq t < T$, where ${\hat{e}}_{t}$ and ${\hat{v}}_{t}$ solve. This steady state controller can be interpreted as an optimal benchmark that is decoupled from the system dynamics, has access to the current cost $c_{t}$, and hence to the one step ahead reference, $r_{t + 1}$, and solves for its optimal, steady state solution. The following Lemma provides a side result on the regret of the SS-OGD algorithm with respect to the steady state controller, ${\mathcal{R}_{SS}^{{SS} - {OGD}}{(w,e_{0})}}:={{J{(e_{0},u^{{SS} - {OGD}})}} - {J{(e_{0},\hat{u})}}}$.

### Lemma 4.5

Under Assumptions 1 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees"), 2 ‣ 2 Problem Statement ‣ Online Linear Quadratic Tracking with Regret Guarantees"), and 3, the regret of the SS-OGD algorithm with respect to the steady state benchmark scales with the reference path length

### Proof 4.6

The regret can be expressed as a function of the combined error state $\varepsilon$ evolving according to. Defining ${\overset{\sim}{Q}}_{i}:=\overset{\sim}{Q}$ for all $0 \leq i < T$ and ${\overset{\sim}{Q}}_{T}$ as in in Appendix 7 using and ${\|{\hat{z}}_{t}\|} \leq {{h\overline{R}},{\forall t}}$. Then using, and the Cauchy Product inequality.

## Numerical Example

The SS-OGD algorithm is implemented on a linearized quadrotor model in closed-loop with a *PI* velocity controller, to track a reference trajectory in two dimensions. In particular, we consider the following model where the state $x:=\begin{bmatrix} \end{bmatrix}^{\top}$ contains the horizontal position, velocity, the roll and pitch angles of the quadrotor, and the input $u:=\begin{bmatrix} \end{bmatrix}^{\top}$ sets the target horizontal velocities. We take $Q = {\operatorname{diag}}$ and $R = {0.1 \cdot I}$.

In the first experiment, the drone tracks the shape of the letters IFA for an a priori unknown reference with a fixed $\Delta r_{t}$ for all timesteps. SS-OGD's performance is compared to that of the causal CE controller that solves for the time-averaged infinite horizon steady state cost by fixing all future references to $r_{t}$, i.e. ${r_{i} = r_{t}},{t < i < T}$. This is equivalent to solving and fixing $r_{t + 1} = r_{t}$. The CE controller does not have access to $r_{t + 1}$, as opposed to the steady state benchmark . The results in Figure 2 show that even though the CE controller appears to be tracking the reference better in the $(p_{x},p_{y})$ plot, the time plot reveals that it lags behind the reference trajectory, resulting in around $3$ times higher regret, compared to SS-OGD. As the reference signal has a constant rate of change, the double integrator dynamics of the open loop transfer function from the error to the state, allow SS-OGD to achieve perfect position tracking. When this is not the case SS-OGD again outperforms the CE controller.

Figure 1: Tracking a 2-D shape with a quadrotor model. The horizontal position plot (left panel) shows the apparent better tracking of the CE controller. However, the time plot (top right panel) shows its visible time lag; by contrast SS-OGD quickly converges to the reference. This leads to a lower rate of regret for SS-OGD (bottom right panel).

Figure 2: Empirical regret of SS-OGD with a finite reference path length converges to a finite value, as expected from the theoretical bound.

In a second experiment the empirical worst-case regret as a function $T$ is calculated. For each $T$, $60$ random reference signals are simulated and the highest value of regret is noted. The references are generated such that $\|{\Delta r_{t}}\|$ decreases with a constant factor of $0.99$. This ensures a finite path length and therefore a finite regret in the limit, as shown in Figure 2, and in agreement with the upper bound in Theorem 4.1.

## Conclusion

In this letter, we reformulate the online LQT problem as an online control problem subject to adversarial disturbances. Within this framework, we propose a novel online gradient descent-based algorithm, called SS-OGD, and show that its dynamic regret scales with the path length of the reference signal. We validate the results on numerical examples with a quadrotor model. The improvement of the regret coefficients, as well as the case where the references are generated by some unknown dynamics is left to be studied in future work.

## System-Optimizer Dynamics

The combined system-optimizer dynamics matrices are where $M:={2\left({{S^{T}QB} + {{({I - {KS}})}^{\top}R}} \right)}$, and $H:={2{({{S^{T}Q{({A - {BK}})}} - {{({I - {KS}})}^{\top}RK}})}}$. The objective function in can be equivalently written as $z_{t}^{\top}\overset{\sim}{Q}z_{t}$ for $0 < t < T$ and as $z_{T}^{\top}{\overset{\sim}{Q}}_{T}z_{T}$ for $t = T$, where Consider the coordinate transformation ${\overset{\sim}{A}}_{V}:={V\overset{\sim}{A}V^{- 1}}$ with $\overline{M}:={M + {HS}} = {2\left({{S^{\top}QS} + {{({I - {KS}})}^{\top}R{({I - {KS}})}}} \right)}$ positive definite, as shown in Lemma 3.1. Using the small gain theorem for interconnected systems, the following, along with $\alpha < {{2/\rho}{(\overline{M})}}$ is a sufficient condition for the stability of ${\overset{\sim}{A}}_{V}$ and therefore of the dynamics Since $A - {BK}$ is stable, there always exists an arbitrarily small $\alpha > 0$ such that the above is fulfilled.

## Proof of Theorem 3.3

Given a disturbance vector $w_{t}$ and a bias input $v$, the steady state of the dynamics with the control law is given by $e = {{Sv} + {\hat{S}w_{t}}}$, where $\hat{S}:={({{I - A} + {BK}})}^{- 1}$. Substituting this in the objective function of, one can confirm that the $v$ that minimizes that cost is the unique (as shown in Lemma 3.1) solution of ${\left({{S^{\top}QS} + {{({I - {KS}})}^{T}R{({I - {KS}})}}} \right)v} = {\left({{{({I - {KS}})}^{\top}RK\hat{S}} - {S^{\top}Q\hat{S}}} \right)w_{t}}$. Using the definition of $\overset{\sim}{A}$, the steady state $\hat{v}$ of the SS-OGD update for a constant $w_{t}$ solves $0 = {{M\hat{v}} + {H{({{S\hat{v}} + {\hat{S}w_{t}}})}} + {2S^{\top}Qw_{t}}}$. Then Since ${I + {{({A - {BK}})}\hat{S}}} = \hat{S}$, and $S = {\hat{S}B}$, the two equations coincide, leading to the unique steady state solution $\hat{v}$.
