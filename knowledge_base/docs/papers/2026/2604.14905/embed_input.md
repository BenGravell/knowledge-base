<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-driven Linear Quadratic Integral Control: A Convex Formulation and Policy Gradient Approach

Topics include Convex optimization, Policy gradients, Optimal control, Distributed systems, Optimization, Control, Data-driven, Linear quadratic, Integral control, LQI, Linear quadratic regulator, DGU.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper studies the data-driven synthesis of linear quadratic integral (LQI) controllers for continuous-time systems. The objective is to achieve optimal state-feedback control with integral action for reference tracking using only measured data. To this end, we derive a data-driven closed-loop parameterization of the augmented dynamics that incorporates the integral state while relying solely on input-state-output measurements of the underlying system. Based on this parameterization, a data-driven convex optimization problem is formulated whose solution yields the optimal linear quadratic regulator (LQR) feedback gain for the augmented system without explicit knowledge of the system matrices. In addition, a policy gradient flow is derived to compute the optimal controller within the space of stabilizing gains. The proposed approach enables data-driven optimal tracking control while avoiding explicit state augmentation in the data collection phase. The effectiveness of the method is demonstrated through a numerical example involving a distributed generation unit (DGU) in a DC microgrid.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in data-driven control enable the synthesis of optimal controllers directly from measurement data, bypassing the need for exact system models \[undef\]. Many data-driven approaches consider the infinite--horizon linear quadratic regulator (LQR) that regulates the state to zero by minimizing an objective that achieves a compromise between transient performance and control effort. To achieve robust output tracking of a reference signal, an integral action can be incorporated to the LQR control law to complement the proportional action, referred to as linear quadratic integral (LQI) control. This paper focuses on data-driven LQI control by utilizing convex optimization and policy gradient methods, aiming to achieve optimal tracking performance while relying solely on input--state--output measurements.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Literature review", "weight": 1.0} -->

This section reviews relevant literature on LQI and PID synthesis via LQR, as well as data-driven convex optimization and policy gradient methods for LQR.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Literature review", "weight": 1.0} -->

LQI control was first introduced in \[undefa\] to achieve asymptotic tracking of constant reference signals. Since then, it has been widely applied across various domains, including aerospace \[undefb\], power grids \[undefc\], and process control \[undefd\] for tracking time-varying reference signals. At its core, the LQI control law consists of a static state-feedback controller augmented with an integral action that accumulates the tracking error between the output and the reference signal \[undefa\]. The synthesis of a stabilizing LQI control law can be achieved by augmenting the system dynamics with an integral state and subsequently applying LQR design methods, such as convex optimization \[undefe, undeff\] or policy gradient approaches \[undefg, undefh\].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Literature review", "weight": 1.0} -->

The LQI controller is often compared to the classical proportional-integral-derivative (PID) controller, as both involve feedback of the integrated tracking error. A linear system in closed loop with a PID controller can be equivalently represented as an augmented linear system controlled by a static state-feedback controller \[undefi\] or a static output-feedback controller \[undefj, Chapter 7\]. These controllers can then be designed using classical methods, such as the LQR. However, recovering the original PID gains from the feedback gains of the augmented system is generally challenging, for example, because a corresponding set of PID gains may not exist or may not be unique \[undefi\]. The work of \[undefk\] shows that, for single-input single-output (SISO) systems, the original PID gains can always be reconstructed if the input and output matrices are orthogonal. The structural constraints inherent to PID control make its synthesis challenging \[undefl\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Literature review", "weight": 1.0} -->

For instance, there is no convex reparameterization available for PID gain synthesis, and the set of stabilizing PID gains may not be path-connected, which prevents the use of policy gradient methods. We stress that LQI control does not have such restrictions and the design of a stabilizing control law boils down to solving the LQR problem of the augmented system. This, however, comes at the cost of requiring full-state measurements during control. Policy gradient solutions for dynamic output feedback without feedthrough that minimizes the LQR objective are discussed in \[undefm\]. This class of output-feedback controllers includes observer-based state-feedback controllers as a special case, but excludes PID controllers that incorporate a feedthrough term.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Literature review", "weight": 1.0} -->

In the context of data-driven optimal control, \[undef\] presents a parameterization of a linear system in closed loop with state-feedback controller using only input-state data and a matrix satisfying a matrix equality. An advancement of this parameterization is the sample covariance parameterization presented in \[undefn, undefo\], resulting in data matrices independent of the sample size. These representations laid the foundation for numerous data-driven LQR methods, including convex optimization approaches \[undef, undefp\] and policy gradient methods \[undefq, undefn\].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

The main contributions of this paper are summarized as follows: A data-driven closed-loop parameterization for the synthesis of LQI controllers is introduced, enabling the direct design of optimal tracking controllers from measured data of the underlying system.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

Based on this parameterization, a convex optimization problem and a policy gradient flow are derived whose solution yields the optimal LQR feedback gain for the augmented system and, consequently, the stabilizing LQI controller gain.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

The proposed approach is validated through a representative numerical example involving a distributed generation unit (DGU) in a DC microgrid.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Organization", "weight": 1.0} -->

Preliminaries are presented in Section II. Section III introduces the data-driven parameterization, the convex program, and the policy gradient flow. Simulation results of a DGU are presented in Section IV. Finally, the paper ends with a conclusion in Section V.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Linear Quadratic Regulator", "weight": 1.0} -->

The infinite-horizon linear LQR problem is formulated as where $Q\succeq 0$ and $R\succ 0$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The system $(A,B)$ is stabilizable and the pair $(A,\sqrt{Q})$ is detectable.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 holds throughout. The optimal solution to is the controller $u=-K^{*}x=-R^{-1}B^{\top}P^{*}x$, where $P^{*}$ is the unique positive definite solution of the CARE Moreover, the closed-loop matrix $A-BK^{*}$ is Hurwitz. The optimal controller $K^{*}$ is also the solution to which admits a convex reformulation \[undefe\]. The set of Hurwitz stable feedback gains of system $(A,B)$ is denoted by and is open, unbounded, and path-connected \[undefr, Section 3\]. The policy gradient flow of the LQR problem is defined as where $P_{K}$ and $W_{K}$ are the solutions to Lyapunov equations respectively. The gradient flow generates unique trajectories $K(t)$ within $\mathcal{K}$ that converges to $K^{*}$ for $t\to\infty$ \[undefs\].

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Linear Quadratic Integral Control", "weight": 1.0} -->

We present the LQI control from \[undefa\]. To enforce asymptotic tracking of a reference signal $r\in\mathbb{R}^{p}$, the integral state is incorporated to the system, yielding Define the aggregated state as $x_{a}:=\begin{bmatrix}x\\z\end{bmatrix}\in\mathbb{R}^{n+p}$. A linear state-feedback control for is where $K=\begin{bmatrix}K_{\mathrm{PD}}&K_{\mathrm{I}}\end{bmatrix}\in\mathbb{R}^{m\times(n+p)}$, and $K_{\mathrm{PD}}\in\mathbb{R}^{m\times n}$ and $K_{\mathrm{I}}\in\mathbb{R}^{m\times p}$ denote the proportional and derivative and integral feedbacks gains, respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Linear Quadratic Integral Control", "weight": 1.0} -->

Let $\bar{x}_{a}=\begin{bmatrix}\bar{x}^{\top}&\bar{z}^{\top}\end{bmatrix}^{\top}$ be an equilibrium point, and define the error variable $\tilde{x}_{a}:=x_{a}-\bar{x}_{a}$ (see \[undefd\] for details). In error coordinates, the augmented dynamics can be written as Under $\tilde{u}=-K\tilde{x}_{a}$, the closed-loop system becomes If $A_{a}-B_{a}K$ is Hurwitz and the reference signal is constant, then $y(t)\to r$ for $t\to\infty$. The LQI controller for original system can be synthesized by computing the optimal LQR feedback $K^{*}$ for the augmented system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Data-driven Closed-loop Parameterizations", "weight": 1.0} -->

We next summarize the continuous-time closed-loop parameterization of \[undef\], adapted to the sampled covariance parameterization in \[undefn\]. Consider a sequence of $T\in\mathbb{N}$ measurements of state, input, and state derivative trajectories of system (1a), sampled at interval $\Delta>0$, These matrices satisfy Define the associated sample covariance matrices to as whose dimensions are independent of the sample size $T$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Following \[undeft\], to avoid state-derivative measurements and mitigate noise amplification caused by numerical differentiation, the data matrices can be replaced by respectively. These matrices result from integrating the stacked system over each interval $[t_{i},t_{i}+\delta]=[\Delta(i-1),\Delta(i-1)+\delta],i\in\{1,\dots,T\}$. Hence, the linear relation $\overset{\scriptscriptstyle\Delta}{X}=A\tilde{X}+B\tilde{U}$ holds, and substituting by to compute does not alter the subsequent results.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation and Approach", "weight": 1.0} -->

In this section, we first analyze the augmented system and clarify the relation of LQI control to classical PI(D) control. We then develop a data-driven closed-loop parameterization, followed by the formulation of the convex program and the policy gradient flow. The main objective of the paper is the following.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Objective 1", "weight": 1.0} -->

Formulate a convex optimization problem and a policy gradient flow, using only data from the original system, to synthesize the optimal LQR state-feedback gain for the augmented system.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Objective 1", "weight": 1.0} -->

Let $Q_{a}=\operatorname{diag}(Q_{x},Q_{z})$ be the weighting matrix for the augmented state $\tilde{x}_{a}$, where $Q_{x}\succeq 0$ corresponds to original state $\tilde{x}$ and $Q_{z}\succ 0$ to the integral state $\tilde{z}$. ^22^2Choosing $Q_{z}\succ 0$ ensures that the zero eigenvalues introduced by the integrator dynamics are observable through $\sqrt{Q_{z}}$ and thus reflected in the cost, which is natural for the LQI problem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

These conditions ensure that the optimal LQR controller stabilizes the augmented system. The following lemmas characterize necessary and sufficient conditions on the system matrices of the original system such that Assumption 2 holds.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Relation to Proportional Integral Derivative Control", "weight": 1.0} -->

In this subsection, we clarify the relation of LQI control to PI(D) control. The PID control law is where $K_{\mathrm{P}}\in\mathbb{R}^{m\times p}$, $K_{\mathrm{I}}\in\mathbb{R}^{m\times p}$, and $K_{\mathrm{D}}\in\mathbb{R}^{m\times p}$, and falls into the class of dynamic output feedback controllers with feedthrough.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Relation to Proportional Integral Derivative Control", "weight": 1.0} -->

In error coordinates, the control law can be rewritten as Substituting the system dynamics (1a) into yields Hence, the PID control law can be represented by a state-feedback controller of the augmented system where $\tilde{K}=\begin{bmatrix}\tilde{K}_{\mathrm{PD}}&\tilde{K}_{\mathrm{I}}\end{bmatrix}\in\mathbb{R}^{m\times(n+p)}$, and Note that the derivative action in the original control law is absorbed into the proportional feedback gain $\tilde{K}_{\mathrm{PD}}$ of the augmented system. This also explains the presence of the derivative component in $K_{\mathrm{PD}}$. Following \, stabilizing PID gains can be obtained by first solving the LQR problem for the augmented system to obtain $\tilde{K}$ and subsequently reconstructing the original PID gains by solving the nonlinear equations.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Relation to Proportional Integral Derivative Control", "weight": 1.0} -->

However, the nonlinear mapping introduces significant difficulties, as there may exist a finite number, infinitely many, or no PID gains satisfying the equations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Relation to Proportional Integral Derivative Control", "weight": 1.0} -->

We now consider the PI case, obtained by setting $K_{\mathrm{D}}=0$. Analogous to, the augmented closed-loop system under with $K_{\mathrm{D}}=0$ in error coordinates is where $\hat{K}=\begin{bmatrix}K_{\mathrm{P}}C&K_{\mathrm{I}}\end{bmatrix}\in\mathbb{R}^{m\times(n+p)}$. Hence, PI control can be interpreted as a structurally constrained state-feedback controller for the augmented system. The gain block acting on the original state $\tilde{x}$ must factor as $K_{\mathrm{P}}C$, which restricts it to the row space of $C$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Relation to Proportional Integral Derivative Control", "weight": 1.0} -->

In contrast, the optimal LQI gain $K^{*}=\begin{bmatrix}K_{\mathrm{PD}}^{*}&K_{\mathrm{I}}^{*}\end{bmatrix}$ obtained from the LQR problem for $(A_{a},B_{a})$ generally does not admit such a factorization.^33^3We note that if $C$ is square and invertible ($p=n$), the constraint $K_{\mathrm{PD}}=K_{\mathrm{P}}C$ imposes no restriction, and PI control recovers full-state feedback LQI control. Unless $K_{\mathrm{PD}}^{*}$ happens to lie in the row space of $C$, the achievable performance under PI control is strictly inferior to that of the full-state-feedback LQI design.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Relation to Proportional Integral Derivative Control", "weight": 1.0} -->

This structural restriction has significant consequences for controller synthesis. The set of stabilizing PI gains may fail to be path-connected \[undefl, Section 4.3\], precluding the usage of policy gradient methods. Moreover, there exists no convex reparametrization of the problem when using the closed-loop matrix of. This difficulty is well documented in the literature and reflects the inherent challenge of synthesizing fixed-structure output feedback controllers such as PI(D) control \[undefl\].

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Data-driven Parameterization", "weight": 1.0} -->

Next, we introduce a data-driven closed-loop parameterization of the augmented system. Analogous to and, we define the data matrices which satisfy $\overline{Y}=C\overline{X}$. For the integral variant mentioned in Remark 1, $Y$ has to be substituted by The following assumption ensures that the data fully characterizes the system and holds throughout the paper.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

By \[undeft, Lemma 4\], Assumption 3 holds under piece-wise constant inputs that are persistently exciting of order $n+1$, which requires $T\geq(m+1)n+m$ samples. Hence, if the order of the system dynamics is known, Assumption 3 can be enforced a priori through a suitable choice of the excitation input before conducting the experiment.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Convex Program", "weight": 1.0} -->

Next, we adapt the convex program to the data-driven representation of the augmented system.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Projected Policy Gradient Flow", "weight": 1.0} -->

In this subsection, we formulate the projected policy gradient flow for the data-driven representation. Let $\mathcal{G}$ denote the set of all $G\in\mathbb{R}^{(n+m)\times(n+p)}$ satisfying (34b) and rendering the closed-loop matrix Hurwitz, i.e., Analogous to the model-based case in \[undefs\], the LQR cost function of the system parameterized in terms of $G$ is defined as the matrix function where $P_{G}\in\mathbb{R}^{n+p}$ is the solution of the Lyapunov Equation The function $f_{G}$ exhibits favorable analytical properties for the well-definedness of its gradient flow. In particular, over $\mathcal{G}$, $f_{G}$ is real analytic and coercive.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Projected Policy Gradient Flow", "weight": 1.0} -->

Real analyticity ensures smoothness of arbitrary order, while coercivity ensures that $f_{G}\to\infty$ as $G\to\partial\mathcal{G}$, implying compact sublevel sets.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We consider a single bus of a DC microgrid that comprises a DGU with a controller and a constant-impedance load, following \[undefy\]. The control architecture resembles an LQI controller, where the states are fed back proportionally, and an additional integral state is introduced to ensure asymptotic tracking of the reference voltage. The closed-loop system is depicted in Fig. 1. The objective is to regulate the bus voltage $v$ to a reference voltage $r$ via the input voltage $u$ of the buck converter. The load is modeled as a constant admittance $Y$, while the buck converter is represented by an averaged model consisting of a controllable voltage source followed by an RLC filter.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The DGU with the load obeys the open-loop dynamics where $v\in\mathbb{R}$ denotes the bus voltage and $i\in\mathbb{R}$ the filter current. The measured output is the bus voltage, yielding the output matrix $C=\begin{bmatrix}1&0\end{bmatrix}$. The DGU controller has the LQI structure $u=-K_{\mathrm{PD}}\left[\begin{smallmatrix}v\\i\end{smallmatrix}\right]-K_{\mathrm{I}}\int_{0}^{t}r(\tau)-v(\tau)\mathrm{d}\tau$, where $K_{\mathrm{PD}}\in\mathbb{R}^{1\times 2}$ and $K_{\mathrm{I}}\in\mathbb{R}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

For the LQR design of the augmented system, the weighting matrices are chosen as $R=1$ and $Q_{a}=\operatorname{diag}$ to achieve fast tracking of the voltage reference.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Since the system parameters are assumed to be unknown, e.g., the load may vary with time, the required data matrices are obtained from input-state-output measurements. To this end, a randomly generated input signal, piecewise constant over intervals of $0.02\text{\,}\mathrm{s}$, is applied to the system. A total of $T=10$ samples are recorded using a sampling interval of $\delta=$0.1\text{\,}\mathrm{s}$$. From these measurements, the data matrices and are constructed to compute the sample covariance matrices $\overline{X},\overline{U},\overline{X}^{\prime}$, and $\overline{Y}$. By Theorem 2, these matrices can be used to parameterize the closed-loop system. For numerical simulation, the system dynamics are integrated using ode45 in MATLAB with default settings. As a ground truth, the optimal gain $K^{\star}$ is computed from the exact augmented model using the lqr function in MATLAB.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Using the proposed data-driven approaches of Theorem 3 and Theorem 4, we compute the feedback gain $K=\begin{bmatrix}K_{\mathrm{PD}}&K_{\mathrm{I}}\end{bmatrix}$ that minimizes the LQR objective of the augmented system. In Fig. 2, the voltage $v(t)$ and the input $u(t)$ are shown. Within the first second, data is collected in open loop as described above. After the first second, the problem is solved to obtain $K^{*}\approx\begin{bmatrix}0.409&1.164&-9.997\end{bmatrix}$, where $\|K^{\star}-K^{*}\|_{F}=4.3\times 10^{-4}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

From $1\text{\,}\mathrm{s}$ to $4\text{\,}\mathrm{s}$, the system is controlled in closed loop with the gain $K^{*}$, where the reference voltage $r(t)$ changes from $400\text{\,}\mathrm{V}$ to $600\text{\,}\mathrm{V}$ to $200\text{\,}\mathrm{V}$ at the time instances $t=$2\text{\,}\mathrm{s}$$ and $t=$3\text{\,}\mathrm{s}$$. The trajectory $v(t)$ in Fig. 2 shows that the reference voltage is tracked by the bus voltage.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In Fig. 3, the normalized residuals $\frac{\|K(t)-K^{\star}\|_{F}}{\|K-K^{\star}\|_{F}}$ of the projected policy gradient flow are shown for the initial stabilizing gains $K_{1}=\begin{bmatrix}0.5&0.1&-50\end{bmatrix}$, $K_{2}=\begin{bmatrix}5&1&-15\end{bmatrix}$, and $K_{3}=\begin{bmatrix}0&0&-1\end{bmatrix}$. The initial values $G$ are computed using (34b), while the trajectories $G(t)$ are obtained form the projected gradient flow, yielding the depicted trajectory $K(t)=-\overline{U}G(t)$. The learning rate $\alpha$ is chosen sufficiently large and only scales the time axis.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

For all initializations, the residuals converge linearly to zero, consistent with the model-based setting \[undefs\].

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

As an outlook, Fig. 4 shows the voltage trajectories for different feedback gains under time-varying loads. The load admittance changes form $Y=$0.02\text{\,}\mathrm{S}$$ to $Y=$0.001\text{\,}\mathrm{S}$$ at $t=$0.5\text{\,}\mathrm{s}$$, and then to $Y=$0.1\text{\,}\mathrm{S}$$ at $t=$2.5\text{\,}\mathrm{s}$$. Moreover, the reference voltage changes from $400\text{\,}\mathrm{V}$ to $410\text{\,}\mathrm{V}$ at $t=$1.5\text{\,}\mathrm{s}$$. The LQR gain $K^{*}$, computed for the nominal load $Y=$0.02\text{\,}\mathrm{S}$$, achieves fast tracking without overshoot.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In contrast, $K_{1}$ provides fast tracking due to its large integrator gain but results in significant overshoot at $t=$0.5\text{\,}\mathrm{s}$$ and $t=$2.5\text{\,}\mathrm{s}$$. The gain $K_{2}$ eliminates overshoot but yields slower reference tracking. The gain $K_{3}$ contains only an integrator term, resulting in slow tracking and insufficient damping of the system dynamics.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The final controller in Fig. 4 implements the policy gradient flow in closed loop, yielding a nonlinear dynamic state-feedback controller that adapts the gain toward the LQR optimal gain corresponding to the current load. In the simulations, we used the model-based policy gradient for simplicity, but the data-driven variant can be applied online using the matrices $\overline{X},\overline{U},\overline{X}^{\prime}$, and $\overline{Y}$ collected online with exploration noise. No formal stability guarantees are provided for the considered controllers, as the system is time-varying due to the load changes. A stability analysis of the LQR policy gradient flow in closed loop with a linear time-varying system can be found in \[undefz\].

<!-- chunk {"id": "body-0046", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Nevertheless, the piecewise-constant load scenario is well suited for policy-gradient-based adaptation. Each load level corresponds to an associated LQR feedback gain, and with a sufficiently large learning rate, the policy gradient flow quickly adapts the feedback gain to the optimal value corresponding to the current load. As a result, the controller regulates the new equilibrium with a near-optimal gain for most of the time between load changes, thereby approximately minimizing the infinite-horizon LQR cost over each time interval.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper introduced a data-driven approach for the synthesis of LQI controllers for continuous-time systems. Using a closed-loop data-driven parameterization, we derived a convex optimization problem that enables the computation of the optimal LQR feedback gain of the augmented system directly from measured data. In addition, a policy gradient flow was introduced to compute the optimal controller within the set of stabilizing gains. The effectiveness of the proposed approach was illustrated using a DGU with an LQI controller in a DC microgrid. Future work will focus on extending the proposed approach to scenarios with process and measurement noise, as well as time-varying system dynamics.
