<!-- arxiv-full-text:v1 {"arxiv_id": "2604.14905", "source": "arxiv-html"} -->

## Introduction

Recent advances in data-driven control enable the synthesis of optimal controllers directly from measurement data, bypassing the need for exact system models \[undef\]. Many data-driven approaches consider the infinite--horizon linear quadratic regulator (LQR) that regulates the state to zero by minimizing an objective that achieves a compromise between transient performance and control effort. To achieve robust output tracking of a reference signal, an integral action can be incorporated to the LQR control law to complement the proportional action, referred to as linear quadratic integral (LQI) control. This paper focuses on data-driven LQI control by utilizing convex optimization and policy gradient methods, aiming to achieve optimal tracking performance while relying solely on input--state--output measurements.

### Literature review

This section reviews relevant literature on LQI and PID synthesis via LQR, as well as data-driven convex optimization and policy gradient methods for LQR.

LQI control was first introduced in \[undefa\] to achieve asymptotic tracking of constant reference signals. Since then, it has been widely applied across various domains, including aerospace \[undefb\], power grids \[undefc\], and process control \[undefd\] for tracking time-varying reference signals. At its core, the LQI control law consists of a static state-feedback controller augmented with an integral action that accumulates the tracking error between the output and the reference signal \[undefa\]. The synthesis of a stabilizing LQI control law can be achieved by augmenting the system dynamics with an integral state and subsequently applying LQR design methods, such as convex optimization \[undefe, undeff\] or policy gradient approaches \[undefg, undefh\].

The LQI controller is often compared to the classical proportional-integral-derivative (PID) controller, as both involve feedback of the integrated tracking error. A linear system in closed loop with a PID controller can be equivalently represented as an augmented linear system controlled by a static state-feedback controller \[undefi\] or a static output-feedback controller \[undefj, Chapter 7\]. These controllers can then be designed using classical methods, such as the LQR. However, recovering the original PID gains from the feedback gains of the augmented system is generally challenging, for example, because a corresponding set of PID gains may not exist or may not be unique \[undefi\]. The work of \[undefk\] shows that, for single-input single-output (SISO) systems, the original PID gains can always be reconstructed if the input and output matrices are orthogonal. The structural constraints inherent to PID control make its synthesis challenging \[undefl\]. For instance, there is no convex reparameterization available for PID gain synthesis, and the set of stabilizing PID gains may not be path-connected, which prevents the use of policy gradient methods. We stress that LQI control does not have such restrictions and the design of a stabilizing control law boils down to solving the LQR problem of the augmented system. This, however, comes at the cost of requiring full-state measurements during control. Policy gradient solutions for dynamic output feedback without feedthrough that minimizes the LQR objective are discussed in \[undefm\]. This class of output-feedback controllers includes observer-based state-feedback controllers as a special case, but excludes PID controllers that incorporate a feedthrough term.

In the context of data-driven optimal control, \[undef\] presents a parameterization of a linear system in closed loop with state-feedback controller using only input-state data and a matrix satisfying a matrix equality. An advancement of this parameterization is the sample covariance parameterization presented in \[undefn, undefo\], resulting in data matrices independent of the sample size. These representations laid the foundation for numerous data-driven LQR methods, including convex optimization approaches \[undef, undefp\] and policy gradient methods \[undefq, undefn\].

### Contributions

The main contributions of this paper are summarized as follows: A data-driven closed-loop parameterization for the synthesis of LQI controllers is introduced, enabling the direct design of optimal tracking controllers from measured data of the underlying system.

Based on this parameterization, a convex optimization problem and a policy gradient flow are derived whose solution yields the optimal LQR feedback gain for the augmented system and, consequently, the stabilizing LQI controller gain.

The proposed approach is validated through a representative numerical example involving a distributed generation unit (DGU) in a DC microgrid.

### Paper Organization

Preliminaries are presented in Section II. Section III introduces the data-driven parameterization, the convex program, and the policy gradient flow. Simulation results of a DGU are presented in Section IV. Finally, the paper ends with a conclusion in Section V.

### Notation

The set of real numbers is denoted by $\mathbb{R}$. The identity matrix of dimension $n\times n$ is given by $I_{n}$, and $0_{n,p}$ denotes the $n\times p$ zero matrix. For a matrix $A$, its transpose, trace, and Frobenius norm are denoted by $A^{\top}$, $tr(A)$, and $\|A\|_{F}$, respectively. The operator $\operatorname{diag}(\cdot)$ constructs a block-diagonal matrix from its arguments. A symmetric positive definite (semidefinite) matrix $A$ is denoted by $A\succ 0$ ($A\succeq 0$). The Moore-Penrose pseudoinverse of a matrix $A$ is denoted by $A^{\dagger}$, and its nullspace is denoted by $\ker(A)$. The eigenvalues of a square matrix $A$ are denoted by $\lambda_{i}(A)$, and their real parts by $\operatorname{Re}(\lambda_{i})$. A square matrix is Hurwitz if all its eigenvalues have strictly negative real parts.

## Preliminaries

We consider the linear time-invariant system where $x(t)\in\mathbb{R}^{n}$, $u(t)\in\mathbb{R}^{m}$, and $y\in\mathbb{R}^{p}$.^11^1Henceforth, explicit time dependency of variables is omitted for readability when clear from the context.

### II-A Linear Quadratic Regulator

The infinite-horizon linear LQR problem is formulated as where $Q\succeq 0$ and $R\succ 0$.

### Assumption 1

The system $(A,B)$ is stabilizable and the pair $(A,\sqrt{Q})$ is detectable.

Assumption 1 holds throughout. The optimal solution to is the controller $u=-K^{*}x=-R^{-1}B^{\top}P^{*}x$, where $P^{*}$ is the unique positive definite solution of the CARE Moreover, the closed-loop matrix $A-BK^{*}$ is Hurwitz. The optimal controller $K^{*}$ is also the solution to which admits a convex reformulation \[undefe\]. The set of Hurwitz stable feedback gains of system $(A,B)$ is denoted by and is open, unbounded, and path-connected \[undefr, Section 3\]. The policy gradient flow of the LQR problem is defined as where $P_{K}$ and $W_{K}$ are the solutions to Lyapunov equations respectively. The gradient flow generates unique trajectories $K(t)$ within $\mathcal{K}$ that converges to $K^{*}$ for $t\to\infty$ \[undefs\].

### II-B Linear Quadratic Integral Control

We present the LQI control from \[undefa\]. To enforce asymptotic tracking of a reference signal $r\in\mathbb{R}^{p}$, the integral state is incorporated to the system, yielding Define the aggregated state as $x_{a}:=\begin{bmatrix}x\\z\end{bmatrix}\in\mathbb{R}^{n+p}$. A linear state-feedback control for is where $K=\begin{bmatrix}K_{\mathrm{PD}}&K_{\mathrm{I}}\end{bmatrix}\in\mathbb{R}^{m\times(n+p)}$, and $K_{\mathrm{PD}}\in\mathbb{R}^{m\times n}$ and $K_{\mathrm{I}}\in\mathbb{R}^{m\times p}$ denote the proportional and derivative and integral feedbacks gains, respectively. Let $\bar{x}_{a}=\begin{bmatrix}\bar{x}^{\top}&\bar{z}^{\top}\end{bmatrix}^{\top}$ be an equilibrium point, and define the error variable $\tilde{x}_{a}:=x_{a}-\bar{x}_{a}$ (see \[undefd\] for details). In error coordinates, the augmented dynamics can be written as Under $\tilde{u}=-K\tilde{x}_{a}$, the closed-loop system becomes If $A_{a}-B_{a}K$ is Hurwitz and the reference signal is constant, then $y(t)\to r$ for $t\to\infty$. The LQI controller for original system can be synthesized by computing the optimal LQR feedback $K^{*}$ for the augmented system.

### II-C Data-driven Closed-loop Parameterizations

We next summarize the continuous-time closed-loop parameterization of \[undef\], adapted to the sampled covariance parameterization in \[undefn\]. Consider a sequence of $T\in\mathbb{N}$ measurements of state, input, and state derivative trajectories of system (1a), sampled at interval $\Delta>0$, These matrices satisfy Define the associated sample covariance matrices to as whose dimensions are independent of the sample size $T$.

### Theorem 1

Let $\operatorname{rank}\left[\begin{smallmatrix}\overline{U}\\\overline{X}\end{smallmatrix}\right]=n+m$ hold. Then, the closed-loop system $\dot{x}=(A-BK)x$ admits the equivalent data-driven representation where $G\in\mathbb{R}^{(n+m)\times n}$.

The proof follows from \[undef, Theorem 2 and Remark 2\] together with \[undefn, Lemma 1\], and is omitted for brevity.

### Remark 1

Following \[undeft\], to avoid state-derivative measurements and mitigate noise amplification caused by numerical differentiation, the data matrices can be replaced by respectively. These matrices result from integrating the stacked system over each interval $[t_{i},t_{i}+\delta]=[\Delta(i-1),\Delta(i-1)+\delta],i\in\{1,\dots,T\}$. Hence, the linear relation $\overset{\scriptscriptstyle\Delta}{X}=A\tilde{X}+B\tilde{U}$ holds, and substituting by to compute does not alter the subsequent results.

## Problem Formulation and Approach

In this section, we first analyze the augmented system and clarify the relation of LQI control to classical PI(D) control. We then develop a data-driven closed-loop parameterization, followed by the formulation of the convex program and the policy gradient flow. The main objective of the paper is the following.

### Objective 1

Formulate a convex optimization problem and a policy gradient flow, using only data from the original system, to synthesize the optimal LQR state-feedback gain for the augmented system.

Let $Q_{a}=\operatorname{diag}(Q_{x},Q_{z})$ be the weighting matrix for the augmented state $\tilde{x}_{a}$, where $Q_{x}\succeq 0$ corresponds to original state $\tilde{x}$ and $Q_{z}\succ 0$ to the integral state $\tilde{z}$. ^22^2Choosing $Q_{z}\succ 0$ ensures that the zero eigenvalues introduced by the integrator dynamics are observable through $\sqrt{Q_{z}}$ and thus reflected in the cost, which is natural for the LQI problem.

### Assumption 2

The system $(A_{a},B_{a})$ is stabilizable and the pair $(A_{a},\sqrt{Q_{a}})$ is detectable.

These conditions ensure that the optimal LQR controller stabilizes the augmented system. The following lemmas characterize necessary and sufficient conditions on the system matrices of the original system such that Assumption 2 holds.

### Lemma 1

The system $(A_{a},B_{a})$ is stabilizable if and only if $(A,B)$ is stabilizable and

### Proof

By the Popov--Belevitch--Hautus (PBH) test \[undefu, Theorem 14.3\], $(A_{a},B_{a})$ is stabilizable if and only if for every eigenvalue $\lambda\in\mathbb{C}$ of $A_{a}$ with $\operatorname{Re}(\lambda)\geq 0$ the matrix has full row rank $n+p$. Consider the case $\lambda\neq 0$. Since $\lambda I_{p}$ is nonsingular, $\operatorname{rank}M(\lambda)=p+\operatorname{rank}\begin{bmatrix}\lambda I_{n}-A&B\end{bmatrix}$. Hence, $\operatorname{rank}M(\lambda)=n+p$ if and only if $\operatorname{rank}\begin{bmatrix}\lambda I_{n}-A&B\end{bmatrix}=n$ which is precisely the condition for stabilizability of $(A,B)$. For the case $\lambda=0$, $M$ has full row rank if and only if $\operatorname{rank}M=\operatorname{rank}\big[\begin{smallmatrix}A&B\\C&0\end{smallmatrix}\big]=n+p$. Combining both cases completes the proof. ∎ Condition implies that $p\leq m$ and that both $C$ and $B$ must have rank $p$. Thus, to satisfy Assumption 2, the number of control inputs must be at least as many as the number of outputs to be tracked.

### Lemma 2

The system $(A_{a},\sqrt{Q})$ is detectable if and only if $(A,\left[\begin{smallmatrix}C\\\sqrt{(Q_{x})}\end{smallmatrix}\right])$ is detectable.

### Proof

By the PBH test \[undefu, Theorem 16.6\], $(A_{a},\sqrt{Q})$ is detectable if and only if only if for every eigenvalue $\lambda\in\mathbb{C}$ of $A_{a}$ with $\operatorname{Re}(\lambda)\geq 0$ the matrix has full column rank. Let $\begin{bmatrix}x\\z\end{bmatrix}$ lie in the nullspace of $N$. Then, equivalently, $(A-\lambda I_{n})x=0,-Cx-\lambda z=0,\sqrt{Q_{x}}x=0$ and $\sqrt{Q_{z}}z=0$. Since $Q_{z}\succ 0$, $z=0$, hence $Cx=0$. Thus full column rank of $N$ holds if and only if for all $\operatorname{Re}(\lambda)\geq 0$, i.e., $(A,\left[\begin{smallmatrix}C\\\sqrt{(Q_{x})}\end{smallmatrix}\right])$ is detectable. ∎ Note that Lemma 2 states that no eigenvector corresponding to an unstable eigenvalue of $A$ must lie simultaneously in the nullspaces of $C$ and $Q_{x}$.

### III-A Relation to Proportional Integral Derivative Control

In this subsection, we clarify the relation of LQI control to PI(D) control. The PID control law is where $K_{\mathrm{P}}\in\mathbb{R}^{m\times p}$, $K_{\mathrm{I}}\in\mathbb{R}^{m\times p}$, and $K_{\mathrm{D}}\in\mathbb{R}^{m\times p}$, and falls into the class of dynamic output feedback controllers with feedthrough. In error coordinates, the control law can be rewritten as Substituting the system dynamics (1a) into yields Hence, the PID control law can be represented by a state-feedback controller of the augmented system where $\tilde{K}=\begin{bmatrix}\tilde{K}_{\mathrm{PD}}&\tilde{K}_{\mathrm{I}}\end{bmatrix}\in\mathbb{R}^{m\times(n+p)}$, and Note that the derivative action in the original control law is absorbed into the proportional feedback gain $\tilde{K}_{\mathrm{PD}}$ of the augmented system. This also explains the presence of the derivative component in $K_{\mathrm{PD}}$. Following \, stabilizing PID gains can be obtained by first solving the LQR problem for the augmented system to obtain $\tilde{K}$ and subsequently reconstructing the original PID gains by solving the nonlinear equations. However, the nonlinear mapping introduces significant difficulties, as there may exist a finite number, infinitely many, or no PID gains satisfying the equations.

We now consider the PI case, obtained by setting $K_{\mathrm{D}}=0$. Analogous to, the augmented closed-loop system under with $K_{\mathrm{D}}=0$ in error coordinates is where $\hat{K}=\begin{bmatrix}K_{\mathrm{P}}C&K_{\mathrm{I}}\end{bmatrix}\in\mathbb{R}^{m\times(n+p)}$. Hence, PI control can be interpreted as a structurally constrained state-feedback controller for the augmented system. The gain block acting on the original state $\tilde{x}$ must factor as $K_{\mathrm{P}}C$, which restricts it to the row space of $C$. In contrast, the optimal LQI gain $K^{*}=\begin{bmatrix}K_{\mathrm{PD}}^{*}&K_{\mathrm{I}}^{*}\end{bmatrix}$ obtained from the LQR problem for $(A_{a},B_{a})$ generally does not admit such a factorization.^33^3We note that if $C$ is square and invertible ($p=n$), the constraint $K_{\mathrm{PD}}=K_{\mathrm{P}}C$ imposes no restriction, and PI control recovers full-state feedback LQI control. Unless $K_{\mathrm{PD}}^{*}$ happens to lie in the row space of $C$, the achievable performance under PI control is strictly inferior to that of the full-state-feedback LQI design.

This structural restriction has significant consequences for controller synthesis. The set of stabilizing PI gains may fail to be path-connected \[undefl, Section 4.3\], precluding the usage of policy gradient methods. Moreover, there exists no convex reparametrization of the problem when using the closed-loop matrix of. This difficulty is well documented in the literature and reflects the inherent challenge of synthesizing fixed-structure output feedback controllers such as PI(D) control \[undefl\].

### III-B Data-driven Parameterization

Next, we introduce a data-driven closed-loop parameterization of the augmented system. Analogous to and, we define the data matrices which satisfy $\overline{Y}=C\overline{X}$. For the integral variant mentioned in Remark 1, $Y$ has to be substituted by The following assumption ensures that the data fully characterizes the system and holds throughout the paper.

### Assumption 3

The matrix $\begin{bmatrix}\overline{U}\\\overline{X}\end{bmatrix}$ has rank $n+m$.

By \[undeft, Lemma 4\], Assumption 3 holds under piece-wise constant inputs that are persistently exciting of order $n+1$, which requires $T\geq(m+1)n+m$ samples. Hence, if the order of the system dynamics is known, Assumption 3 can be enforced a priori through a suitable choice of the excitation input before conducting the experiment.

### Theorem 2

The augmented closed-loop system admits the equivalent data-driven representation where $G\in\mathbb{R}^{(n+m)\times(n+p)}$. Particularly, $K=-\overline{U}G$.

### Proof

The closed-loop matrix of is Moreover, due to and $\overline{Y}\!\!=\!C\overline{X}$, the measured data satisfy By Assumption 3 and the Rouché--Capelli theorem \[undefv, Th. 2.38\], the linear system (34b) is consistent. Therefore, for any $K=\begin{bmatrix}K_{\mathrm{PD}}&K_{\mathrm{I}}\end{bmatrix}\in\mathbb{R}^{m\times(n+p)}$, there exists a $G$ satisfying (34b). Hence, U G = \[- KPD- KI\] = -K.$\qed\endIEEEproof\par\par\par Hence,everyclosed-loopmatrix$A_a-B_aK$admitsadata-drivenparameterizationthroughsome$G$satisfying$\[In0n,p\] = X G$.\par\par\begin{remark}Note that the augmented closed-loop math:closed_aug can be represented by data matrices $\overline{X},\overline{U},\overline{X}^{\prime}$, and $\overline{Y}$ of the underlying system math:sys1 without measuring the integral state $\tilde{z}$. Hence, the controller $K$ can be designed based on data, but the control law in original coordinates $u=-K_{\mathrm{PD}}x-K_{\mathrm{I}}\int_{0}^{t}r(\tau)-y(\tau)\mathrm{d}\tau$ \end{remark}\par\par$

### III-C Convex Program

Next, we adapt the convex program to the data-driven representation of the augmented system.

### Theorem 3

The optimal LQR feedback gain of system is $K^{*}=-\overline{U}Z^{*}(W^{*})^{-1}$, where $Z^{*}\in\mathbb{R}^{(n+m)\times(n+p)}$ and $W^{*}\in\mathbb{R}^{(n+p)\times(n+p)}$ minimize the convex program

### Proof

Substituting into and using the cyclic property of the trace operator yields By substituting $Z=GW$, the constraint (39b) becomes affine in $(Z,W)$. However, the cost term $\operatorname{tr}\!\big(R^{1/2}\overline{U}ZW^{-1}Z^{\top}\overline{U}^{\top}R^{1/2}\big)$ remains nonconvex. To obtain the convex program, we introduce the epigraph variable $S=S^{\top}$ and upper bound this term as which is enforced via (38b), obtained by a Schur complement argument. The relation $G^{*}=Z^{*}(W^{*})^{-1}$ follows from the substitution and $W^{*}=(P^{*})^{-1}\succ 0$, and the optimal gain is recovered as $K^{*}=-\overline{U}Z^{*}(W^{*})^{-1}$. ∎ Note that every feasible solution of the convex program yields a feedback gain such that $A_{a}-B_{a}K$ is Hurwitz.

### III-D Projected Policy Gradient Flow

In this subsection, we formulate the projected policy gradient flow for the data-driven representation. Let $\mathcal{G}$ denote the set of all $G\in\mathbb{R}^{(n+m)\times(n+p)}$ satisfying (34b) and rendering the closed-loop matrix Hurwitz, i.e., Analogous to the model-based case in \[undefs\], the LQR cost function of the system parameterized in terms of $G$ is defined as the matrix function where $P_{G}\in\mathbb{R}^{n+p}$ is the solution of the Lyapunov Equation The function $f_{G}$ exhibits favorable analytical properties for the well-definedness of its gradient flow. In particular, over $\mathcal{G}$, $f_{G}$ is real analytic and coercive. Real analyticity ensures smoothness of arbitrary order, while coercivity ensures that $f_{G}\to\infty$ as $G\to\partial\mathcal{G}$, implying compact sublevel sets.

### Proposition 1

Let $G\in\mathcal{G}$. Then, the gradient of the LQR cost with respect to $G$ is where $P_{G}$ and $W_{G}=W_{G}^{\top}\in\mathbb{R}^{n+p}$ satisfy and

### Proof

The function is a composition of smooth functions, i.e., $G\mapsto P_{G}\mapsto\operatorname{tr}(P_{G})$. The differential of with respect to $G$ is given by where $F=dG^{\top}(\overline{U}^{\top}R\overline{U}G+\left[\begin{smallmatrix}\overline{X}^{\prime}\\-\overline{Y}\end{smallmatrix}\right]^{\top}P_{G})$.^44^4For matrix differentials, see \[undefw, Section 1\]. Since $G\in\mathcal{G}$, the solution to is Thus, by using the cyclic invariance of the trace operator, the differential of the LQR cost is The integral in is the solution to, yielding $df_{G}=2\operatorname{tr}(FW_{G})$, implying. ∎ The following lemma establishes uniqueness of the stationary point of the cost function on its domain.

### Lemma 3

The function $f_{G}$ admits a unique stationary point $G^{*}$ on $\mathcal{G}$. The corresponding feedback gain $K^{*}=-\overline{U}G^{*}$ is the optimal LQR gain of the system.

### Proof

By definition, $\left[\begin{smallmatrix}\overline{X}^{\prime}\\-\overline{Y}\end{smallmatrix}\right]G$ is Hurwitz for all $G\in\mathcal{G}$, implying that the solution to the Lyapunov equation is given by Hence, using and inserting into $\nabla f_{G}=0$ leads to By Assumption 3, the square matrix $\left[\begin{smallmatrix}\overline{X}\\\overline{U}\end{smallmatrix}\right]$ is invertible. Left-multiplying the inverse of $\left[\begin{smallmatrix}\overline{X}\\\overline{U}\end{smallmatrix}\right]^{\top}$ to yields where the second block row is $RK=B_{a}^{\top}P_{G}$. Since $P_{G}$ is the unique solution of the Lyapunov equation for all $G\in\mathcal{G}$ and $R\succ 0$, it follows that $K^{*}=R^{-1}B_{a}^{\top}P_{G^{*}}$. ∎ To ensure that the linear equality constraint $\overline{X}G=\begin{bmatrix}I_{n}&0_{n,p}\end{bmatrix}$ is preserved along the gradient flow, we project the gradient $\nabla f_{G}$ onto the tangent space of $\mathcal{G}$, i.e., onto $\operatorname{ker}(\overline{X})$, using the orthogonal projection where $\overline{X}^{\dagger}=\overline{X}^{\top}(\overline{X}\overline{X}^{\top})^{-1}$ is the right inverse of $\overline{X}$. As an orthogonal projection, $\Pi$ is symmetric and idempotent, implying its eigenvalues lie in $\{0,1\}$ and $\Pi\succeq 0$ \[undefx, 1.1.P5\].

### Theorem 4

The projected gradient flow converges to $G^{*}$, i.e., $G(t)\to G^{*}$ for $t\to\infty$.

### Proof

Let $V(G)=f_{G}-f_{G^{*}}$ be the Lyapunov candidate. Since $P_{G}\succeq 0$, $f_{G}=\operatorname{tr}(P_{G})=\sum_{i}\lambda_{i}(P_{G})\geq 0$. This implies with Lemma 3, $V(G^{*})=0$ and $V(G)>0$ for all $G\in\mathcal{G}\setminus\{G^{*}\}$. The time derivative of $V(G)$ along is By Lemma 3, $\dot{V}(G)=0$ holds only for $G=G^{*}$. Since $\dot{V}(G)<0$ for all $G\in\mathcal{G}\setminus\{G^{*}\}$, $V(G)$ is a Lyapunov function, implying asymptotic stability of $G^{*}$. Moreover, $G(t)$ remains in the compact sublevel set $\{G\in\mathcal{G}\mid f_{G}\leq f_{G}\}$ for any $G\in\mathcal{G}$, because $V(G)$ is nonincreasing along $G(t)$. It follows that $G(t)$ yields stabilizing feedback gains $K(t)$ for all $t\geq 0$. Consequently, the region of attraction of $G^{*}$ is $\mathcal{G}$. ∎

## Simulation Results

We consider a single bus of a DC microgrid that comprises a DGU with a controller and a constant-impedance load, following \[undefy\]. The control architecture resembles an LQI controller, where the states are fed back proportionally, and an additional integral state is introduced to ensure asymptotic tracking of the reference voltage. The closed-loop system is depicted in Fig. 1. The objective is to regulate the bus voltage $v$ to a reference voltage $r$ via the input voltage $u$ of the buck converter. The load is modeled as a constant admittance $Y$, while the buck converter is represented by an averaged model consisting of a controllable voltage source followed by an RLC filter. Filter and load parameters are $R=$0.2\text{\,}\mathrm{\SIUnitSymbolOhm}$$, $L=$2\text{\,}\mathrm{mH}$$, and $C=$2\text{\,}\mathrm{mF}$$, and $Y=$0.02\text{\,}\mathrm{S}$$.

Figure 1: DGU in closed-loop with the LQI controller.

The DGU with the load obeys the open-loop dynamics where $v\in\mathbb{R}$ denotes the bus voltage and $i\in\mathbb{R}$ the filter current. The measured output is the bus voltage, yielding the output matrix $C=\begin{bmatrix}1&0\end{bmatrix}$. The DGU controller has the LQI structure $u=-K_{\mathrm{PD}}\left[\begin{smallmatrix}v\\i\end{smallmatrix}\right]-K_{\mathrm{I}}\int_{0}^{t}r(\tau)-v(\tau)\mathrm{d}\tau$, where $K_{\mathrm{PD}}\in\mathbb{R}^{1\times 2}$ and $K_{\mathrm{I}}\in\mathbb{R}$. For the LQR design of the augmented system, the weighting matrices are chosen as $R=1$ and $Q_{a}=\operatorname{diag}$ to achieve fast tracking of the voltage reference.

Since the system parameters are assumed to be unknown, e.g., the load may vary with time, the required data matrices are obtained from input-state-output measurements. To this end, a randomly generated input signal, piecewise constant over intervals of $0.02\text{\,}\mathrm{s}$, is applied to the system. A total of $T=10$ samples are recorded using a sampling interval of $\delta=$0.1\text{\,}\mathrm{s}$$. From these measurements, the data matrices and are constructed to compute the sample covariance matrices $\overline{X},\overline{U},\overline{X}^{\prime}$, and $\overline{Y}$. By Theorem 2, these matrices can be used to parameterize the closed-loop system. For numerical simulation, the system dynamics are integrated using ode45 in MATLAB with default settings. As a ground truth, the optimal gain $K^{\star}$ is computed from the exact augmented model using the lqr function in MATLAB.

Using the proposed data-driven approaches of Theorem 3 and Theorem 4, we compute the feedback gain $K=\begin{bmatrix}K_{\mathrm{PD}}&K_{\mathrm{I}}\end{bmatrix}$ that minimizes the LQR objective of the augmented system. In Fig. 2, the voltage $v(t)$ and the input $u(t)$ are shown. Within the first second, data is collected in open loop as described above. After the first second, the problem is solved to obtain $K^{*}\approx\begin{bmatrix}0.409&1.164&-9.997\end{bmatrix}$, where $\|K^{\star}-K^{*}\|_{F}=4.3\times 10^{-4}$. From $1\text{\,}\mathrm{s}$ to $4\text{\,}\mathrm{s}$, the system is controlled in closed loop with the gain $K^{*}$, where the reference voltage $r(t)$ changes from $400\text{\,}\mathrm{V}$ to $600\text{\,}\mathrm{V}$ to $200\text{\,}\mathrm{V}$ at the time instances $t=$2\text{\,}\mathrm{s}$$ and $t=$3\text{\,}\mathrm{s}$$. The trajectory $v(t)$ in Fig. 2 shows that the reference voltage is tracked by the bus voltage.

Figure 2: Trajectories of the bus voltage v(t) and input u(t) during open-loop data collection and closed-loop control.

Figure 3: Normalized residuals $\frac{\|K(t)-K^{\star}\|_{F}}{\|K-K^{\star}\|_{F}}$ of the projected gradient flow for initial gains K ∈ {K1, K2, K3}.

In Fig. 3, the normalized residuals $\frac{\|K(t)-K^{\star}\|_{F}}{\|K-K^{\star}\|_{F}}$ of the projected policy gradient flow are shown for the initial stabilizing gains $K_{1}=\begin{bmatrix}0.5&0.1&-50\end{bmatrix}$, $K_{2}=\begin{bmatrix}5&1&-15\end{bmatrix}$, and $K_{3}=\begin{bmatrix}0&0&-1\end{bmatrix}$. The initial values $G$ are computed using (34b), while the trajectories $G(t)$ are obtained form the projected gradient flow, yielding the depicted trajectory $K(t)=-\overline{U}G(t)$. The learning rate $\alpha$ is chosen sufficiently large and only scales the time axis. For all initializations, the residuals converge linearly to zero, consistent with the model-based setting \[undefs\].

Figure 4: Trajectories of the voltage v(t) for a time-varying load and different LQI controllers.

As an outlook, Fig. 4 shows the voltage trajectories for different feedback gains under time-varying loads. The load admittance changes form $Y=$0.02\text{\,}\mathrm{S}$$ to $Y=$0.001\text{\,}\mathrm{S}$$ at $t=$0.5\text{\,}\mathrm{s}$$, and then to $Y=$0.1\text{\,}\mathrm{S}$$ at $t=$2.5\text{\,}\mathrm{s}$$. Moreover, the reference voltage changes from $400\text{\,}\mathrm{V}$ to $410\text{\,}\mathrm{V}$ at $t=$1.5\text{\,}\mathrm{s}$$. The LQR gain $K^{*}$, computed for the nominal load $Y=$0.02\text{\,}\mathrm{S}$$, achieves fast tracking without overshoot. In contrast, $K_{1}$ provides fast tracking due to its large integrator gain but results in significant overshoot at $t=$0.5\text{\,}\mathrm{s}$$ and $t=$2.5\text{\,}\mathrm{s}$$. The gain $K_{2}$ eliminates overshoot but yields slower reference tracking. The gain $K_{3}$ contains only an integrator term, resulting in slow tracking and insufficient damping of the system dynamics.

The final controller in Fig. 4 implements the policy gradient flow in closed loop , yielding a nonlinear dynamic state-feedback controller that adapts the gain toward the LQR optimal gain corresponding to the current load. In the simulations, we used the model-based policy gradient for simplicity, but the data-driven variant can be applied online using the matrices $\overline{X},\overline{U},\overline{X}^{\prime}$, and $\overline{Y}$ collected online with exploration noise. No formal stability guarantees are provided for the considered controllers, as the system is time-varying due to the load changes. A stability analysis of the LQR policy gradient flow in closed loop with a linear time-varying system can be found in \[undefz\].

Nevertheless, the piecewise-constant load scenario is well suited for policy-gradient-based adaptation. Each load level corresponds to an associated LQR feedback gain, and with a sufficiently large learning rate, the policy gradient flow quickly adapts the feedback gain to the optimal value corresponding to the current load. As a result, the controller regulates the new equilibrium with a near-optimal gain for most of the time between load changes, thereby approximately minimizing the infinite-horizon LQR cost over each time interval.

## Conclusion

This paper introduced a data-driven approach for the synthesis of LQI controllers for continuous-time systems. Using a closed-loop data-driven parameterization, we derived a convex optimization problem that enables the computation of the optimal LQR feedback gain of the augmented system directly from measured data. In addition, a policy gradient flow was introduced to compute the optimal controller within the set of stabilizing gains. The effectiveness of the proposed approach was illustrated using a DGU with an LQI controller in a DC microgrid. Future work will focus on extending the proposed approach to scenarios with process and measurement noise, as well as time-varying system dynamics.
