<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Online Linear Quadratic Tracking with Regret Guarantees

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Online learning algorithms for dynamical systems provide finite time guarantees for control in the presence of sequentially revealed cost functions. We pose the classical linear quadratic tracking problem in the framework of online optimization where the time-varying reference state is unknown a priori and is revealed after the applied control input. We show the equivalence of this problem to the control of linear systems subject to adversarial disturbances and propose a novel online gradient descent based algorithm to achieve efficient tracking in finite time. We provide a dynamic regret upper bound scaling linearly with the path length of the reference trajectory and a numerical example to corroborate the theoretical guarantees.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear quadratic tracking (LQT) is the natural generalization of the optimal linear quadratic regulator (LQR) for the setting where the goal is not to drive the state to the origin but to a certain reference. The reference trajectory need not be necessarily time-invariant and in the classic formulation of the problem is known in advance. This is a reasonable assumption in many practical applications, such as aircraft tracking of a predetermined trajectory or precision control in industrial process engineering. However, in other scenarios, for example, in tracking the output of a secondary agent whose dynamics are unknown and/or the measurements are imperfect, the prediction of the next reference point is non-trivial. In these cases the reference trajectory is only revealed sequentially, after the action has been taken, suggesting the need for an online or adaptive algorithm that will learn or adapt to the dynamics of the reference-generating agent.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this letter, we study the LQT problem with an unknown reference trajectory. We pose the problem in the framework of online convex optimization (OCO) subject to the dynamics constraint of the system. In particular, the tracking problem is recast into an equivalent regulation problem with a redefined state that evolves with linear dynamics subject to additive adversarial disturbances. In the spirit of online decision-making under computational and memory constraints, our goal is to develop a gradient-based algorithm that is fast and simple to implement and requires no large memory. To this end, we show how classical online gradient descent (OGD) may fail to achieve optimal tracking and propose a modified algorithm, called SS-OGD (steady state OGD) that is guaranteed to achieve the goal under mild conditions. Given the online nature of the algorithm, its performance is quantified through the means of dynamic regret that compares the accumulated finite time cost of a given algorithm to that of an optimal benchmark that solves the LQT problem with an *a priori* knowledge of the reference trajectory. We provide a dynamic regret bound that scales linearly with the path length of the reference trajectory.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The LQT problem for sequentially revealed adversarial reference states is studied mostly with policy regret guarantees, with one of the first works suggesting a relatively computationally heavy algorithm. In a more recent line of work the authors introduce a memory-based, gradient descent algorithm and in tackle the constrained tracking problem. Several works also provide dynamic regret guarantees for tracking of unknown targets, however, their settings differ from ours. In, the authors analyze an output tracking scheme but assume an iterative setting, while in a window of predictions is available. Without predictions, their regret order is determined by that of a fixed oracle controller. In, the authors also provide a lower bound for the dynamic regret in terms of the reference path length, matching the same order as our proposed scheme. Gradient-based algorithms, as the ones we study, have also been developed in the context of online feedback optimization. There, in contrast to our setting, the dynamics are generally assumed to be unknown, but, crucially, the cost functions are fixed over the horizon, and the regret is not analyzed. Several recent works, e.g., consider a similar setting with time-varying costs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These, however, are allowed to be estimated offline by training, incompatible with our setting, and without regret guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Consider the discrete-time linear time-invariant (LTI) dynamical system, given by where $x_{t} \in {\mathbb{R}}^{n}$ and $u_{t} \in {\mathbb{R}}^{m}$ are the state and input vectors respectively, and ${A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times m}}$ are *known* system matrices.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The goal of the optimal LQT problem is the tracking of a time-varying signal $r_{t} \in {\mathbb{R}}^{n}$, such that the cost is minimized for some weighting matrices $Q \in {\mathbb{R}}^{n \times n}$ and $R \in {\mathbb{R}}^{m \times m}$, and where $P \in {\mathbb{R}}^{n \times n}$ is the solution of the discrete algebraic Riccati equation (DARE)^11^1The final cost matrix is taken to be $P$ for simplicity. For other values of the terminal cost matrix the results still hold up to an additional constant.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The LQT problem can be recast into an equivalent LQR formulation by considering instead the dynamics with $e_{t}:={x_{t} - r_{t}}$ and $w_{t}:={{Ar_{t}} - r_{t + 1}}$ for all $t \in {\mathbb{N}}$, and the corresponding cost function When the reference trajectory $r_{t}$, $t \in {\mathbb{N}}$ is known at the initial time a closed form solution for the optimal controller that solves the following optimization problem can be obtained This controller, often referred to as the optimal offline noncausal controller, can be represented as a linear feedback on the current state and the future reference.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Departing from the classical formulation of tracking control, we assume that the reference signal is *unknown* and is only revealed sequentially after the control input has been applied, similar to the adversarial tracking framework. In particular, for each time step $0 \leq t < T$: The state $x_{t}$ and the reference state $r_{t}$ are observed, The agent decides on an input $u_{t}$, The environment decides on the next reference $r_{t + 1}$, which, in turn, determines $w_{t}$. The error state then evolves according to, incurring the following cost for the agent Note that the online cost, depends on the current input $u_{t}$ and the unknown disturbance $w_{t}$, and is therefore unknown to the decision maker at timestep $t$; it is revealed only at time $t + 1$, after the input $u_{t}$ has been applied to the system. Our problem formulation fits the online learning framework, with the extra challenge of inherent dynamics.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The goal of the controller is then to minimize the online cumulative cost^22^2For consistency we require ${c_{T - 1}{(e_{T - 1},u_{T - 1})}}:={{\|{{Ae_{T - 1}} + {Bu_{T - 1}} + w_{T - 1}}\|}_{P}^{2} + {\| u_{T - 1}\|}_{R}^{2}}$. To forego unnecessary cluttering of the notation, the separate treatment of the last timestep is implied implicitly.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

This is the same as the LQR cost without the initial state, implying that the minimizers of both problems coincide.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We quantify the finite-time performance of the algorithm through the means of dynamic regret. Consider a policy $\pi:{\mathcal{I}\rightarrow{\mathbb{R}}^{m}}$, mapping from the available information set, $\mathcal{I}$, to the control input space. Its dynamic regret, given a disturbance signal $w$, is defined as where $u^{\pi}$ is the input generated by $\pi$ and $u^{\star}$ is given.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We allow the trajectory ${r_{t},t} \in {\mathbb{N}}$ to be arbitrary, as long as it remains bounded.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1 (Bounded trajectory)", "weight": 1.0} -->

The more abruptly a trajectory changes, the harder it is to achieve good tracking performance, especially if the trajectory is unknown beforehand. To capture this inherent complexity of the problem with dynamic regret, we use the well-established notion of path length,.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2 (LQR is well-posed)", "weight": 1.0} -->

The system $(A,B)$ is stabilisable, the pair $(Q^{\frac{1}{2}},A)$ is detectable and $R \succ 0$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The SS-OGD Algorithm", "weight": 1.0} -->

We consider a control law of the following form where $K = {{({R + {B^{\top}PB}})}^{- 1}B^{\top}PA}$ is fixed to the optimal LQR gain, and $v_{t}$ is a correction term that should account for the unknown disturbances; we will employ online learning techniques to update the latter term.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The SS-OGD Algorithm", "weight": 1.0} -->

We investigate the performance of online gradient descent based algorithms. Consider the following "naive" update where $v_{t}$ is updated in the opposite direction of the gradient of the most recent cost. Here $\alpha \in R_{+}$ is the step size and the recursion starts from some $v_{0} \in {\mathbb{R}}^{m}$. As the online objective is quadratic, the gradient is available in a closed form and the update can be represented as $v_{t} = {v_{t - 1} - {2\alpha{({{Ru_{t - 1}} + {B^{\top}Qe_{t}}})}}}$. For the case of a constant reference signal and an underactuated system, the algorithm can converge to a point that is not necessarily the optimal one with respect to infinite horizon cost minimization. This is due to the greedy behavior of the update that does not take into account future dynamics. In this section, we propose a simple modification to this myopic OGD update, called SS-OGD that accounts for this shortcoming.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The SS-OGD Algorithm", "weight": 1.0} -->

To motivate the SS-OGD update, we consider the steady state solution of in closed-loop with the affine control law when we fix $v_{i} = \overline{v}$ and $r_{i} = \overline{r}$ for all subsequent timesteps $i \geq t$. Defining $S:={{({{I - A} + {BK}})}^{- 1}B}$, a closed form solution for the steady state and input is given by ^33^3Note that $\overline{x}$ and $\overline{u}$ are both defined for a given $\overline{v}$ and $\overline{r}$. The dependence is left for simplicity One can then find the $\overline{v}$ which will recover the optimal steady state solution by minimizing the time-averaged infinite horizon steady state cost.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The SS-OGD Algorithm", "weight": 1.0} -->

For $\overline{x}$ and $\overline{u}$ defined as, this is equivalent to minimizing whose gradient is given by Since $r$ is, in general not constant, and the steady state condition is not satisfied, we suggest a new OGD-like update rule on the bias term $v_{t}$ that is a modified version of the gradient. Specifically, the feedback on the steady state error, $\overline{x} - \overline{r}$, is replaced with the measured error, $x_{t} - r_{t}$, and the steady state input, $\overline{u}$, with the latest applied input, $u_{t - 1}$. This results in the following update, named SS-OGD The cost $c$ in is defined for the steady state $\overline{x}$ and input $\overline{u}$ and is thus decoupled from the true online cost $c_{t}$ in that reflects the current $e_{t}$ and $u_{t}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The SS-OGD Algorithm", "weight": 1.0} -->

These are, in general, not at a steady state and $r_{t}$ is not constant. Thus, $c$ is only an auxiliary, hallucinated cost to construct the update.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Since all the variables in $\overset{\sim}{A}$ are known *a priori*, we show that there always exists an $\alpha$ satisfying this assumption and provide a sufficient condition in Appendix 7.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The following theorem shows that, for a constant $w_{t} = \overline{w}$ for all $0 \leq t < T$, SS-OGD update converges to the solution of with $r_{T + 1}:=r_{T}$. The solution of can be interpreted as the steady state and steady state input that minimize the infinite horizon time-averaged cost.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

To characterize the effectiveness of the algorithm for time-varying signals and to provide finite time guarantees, we analyze its dynamic regret and show that it scales with the path length. The next theorem summarizes this main result.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Steady State Benchmark", "weight": 1.0} -->

Given Theorem 3.3, one can also compare SS-OGD to the steady state optimal solution for each timestep. Consider for all $0 \leq t < T$, where ${\hat{e}}_{t}$ and ${\hat{v}}_{t}$ solve. This steady state controller can be interpreted as an optimal benchmark that is decoupled from the system dynamics, has access to the current cost $c_{t}$, and hence to the one step ahead reference, $r_{t + 1}$, and solves for its optimal, steady state solution. The following Lemma provides a side result on the regret of the SS-OGD algorithm with respect to the steady state controller, ${\mathcal{R}_{SS}^{{SS} - {OGD}}{(w,e_{0})}}:={{J{(e_{0},u^{{SS} - {OGD}})}} - {J{(e_{0},\hat{u})}}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

The SS-OGD algorithm is implemented on a linearized quadrotor model in closed-loop with a *PI* velocity controller, to track a reference trajectory in two dimensions. In particular, we consider the following model where the state $x:=\begin{bmatrix} \end{bmatrix}^{\top}$ contains the horizontal position, velocity, the roll and pitch angles of the quadrotor, and the input $u:=\begin{bmatrix} \end{bmatrix}^{\top}$ sets the target horizontal velocities. We take $Q = {\operatorname{diag}}$ and $R = {0.1 \cdot I}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

In the first experiment, the drone tracks the shape of the letters IFA for an a priori unknown reference with a fixed $\Delta r_{t}$ for all timesteps. SS-OGD's performance is compared to that of the causal CE controller that solves for the time-averaged infinite horizon steady state cost by fixing all future references to $r_{t}$, i.e. ${r_{i} = r_{t}},{t < i < T}$. This is equivalent to solving and fixing $r_{t + 1} = r_{t}$. The CE controller does not have access to $r_{t + 1}$, as opposed to the steady state benchmark. The results in Figure 2 show that even though the CE controller appears to be tracking the reference better in the $(p_{x},p_{y})$ plot, the time plot reveals that it lags behind the reference trajectory, resulting in around $3$ times higher regret, compared to SS-OGD.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

As the reference signal has a constant rate of change, the double integrator dynamics of the open loop transfer function from the error to the state, allow SS-OGD to achieve perfect position tracking. When this is not the case SS-OGD again outperforms the CE controller.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

In a second experiment the empirical worst-case regret as a function $T$ is calculated. For each $T$, $60$ random reference signals are simulated and the highest value of regret is noted. The references are generated such that $\|{\Delta r_{t}}\|$ decreases with a constant factor of $0.99$. This ensures a finite path length and therefore a finite regret in the limit, as shown in Figure 2, and in agreement with the upper bound in Theorem 4.1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this letter, we reformulate the online LQT problem as an online control problem subject to adversarial disturbances. Within this framework, we propose a novel online gradient descent-based algorithm, called SS-OGD, and show that its dynamic regret scales with the path length of the reference signal. We validate the results on numerical examples with a quadrotor model. The improvement of the regret coefficients, as well as the case where the references are generated by some unknown dynamics is left to be studied in future work.
