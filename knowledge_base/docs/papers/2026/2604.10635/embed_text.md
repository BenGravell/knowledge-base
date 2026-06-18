## Introduction

The linear quadratic regulation (LQR) problem serves as a fundamental research topic within the realm of control theory, whose optimal controller has a static state-feedback form. During the past few years, theoretical analysis work targeting the LQR control has made substantial progress, laying the foundation for policy structures \[20 control")\], convergence guarantees, efficiency improvements, and sample complexity. However, due to the practical challenges of obtaining full state information, output-feedback control warrants further investigation as a more realistic and significant controller design approach.

Some recent works have studied the optimization landscape of static output-feedback control. The necessary and sufficient conditions for the stability of static output-feedback (SOF) controllers are derived by bridging the error between state-feedback gain and output-feedback gain. On the other hand, further research has delved into the optimization landscape of dynamic output-feedback linear quadratic regulation (dLQR). proved the observable stationary point of dLQR is unique. proposed an alternative policy parameterization using the past input-output trajectory of finite length as feedback and established a global convergence guarantee. Robustness constraints have been incorporated in the design of dynamical controllers, where the feasible set of stabilizing controllers is proved to have at most two connected components. The global optimality of the standard $H_{\infty}$ robust control with non-degenerated stabilizing dynamical structures is further considered , which reveals that all Clarke stationary points are globally optimal despite the non-smoothness of $H_{\infty}$ cost function. For stochastic dynamics, the linear quadratic Gaussian (LQG) problem is analyzed from the perspectives of the connectivity of stabilizing controllers and the structure of stationary points \[20 control")\]. For unknown systems, model-free learning methods have been designed for dLQR with convergence and optimality analysis.

Although static output-feedback LQR offers greater design flexibility, observer-based output-feedback can achieve performance closer to that of full state-feedback control by leveraging reconstructed state information. This advantage stems from the separation principle, which enables independent pole placement for state observers and feedback controllers. Given that pole locations dominate the convergence rate of estimation error and the performance deviation from the state-feedback control, such structural decoupling has important theoretical significance. However, for policy gradient method of solving LQG, it has been demonstrated in LQG problems that the gradients of the objective function with respect to the controller and observer are not separable. Based on the derived gradients, policy gradient methods demonstrate efficacy in optimizing the controller-observer pair for observer-based dynamic LQR (OD-LQR) problems through dynamical system augmentation. However, the analysis there overlooks the transient performance and hence cannot guarantee the optimality. Moreover, existing works only focus on developing numerical solutions. They lack rigorous analysis of both the optimality conditions and the effect of the transient quadratic performance on the optimization landscape.

In this work, we investigate the stationary point of dynamic output-feedback LQR control with a state observer, providing novel insights into the optimality conditions of observer-based LQR. Our main theoretical results are summarized as follows:

We derive an analytical expression for the standard observer gain $L^{\star}$, which minimizes the accumulated estimation variance. This gain serves as the optimal observer gain for OD-LQR, analogous to the optimal filter gain in the LQG setting. Unlike observer gains determined via pole assignment, which lacks transient performance guarantee, our theoretical analysis and numerical results demonstrate that $L^{\star}$ ensures control optimality under the standard state-feedback LQR gain $K^{\star}$ \[Theorem 1\].

Using policy gradient expressions, we analyze the optimization landscape of OD-LQR. Our results demonstrate that while the standard LQR gain $K^{\star}$ is commonly used in observer-based designs, it is generally only suboptimal in achieving the minimal quadratic performance when combined with the standard observer gain $L^{\star}$ in the OD-LQR problem. It becomes optimal when the initial cross-correlation between observation error and state observation vanishes \[Proposition 2\].

We derive the set of stationary points of the OD-LQR problem by solving the first-order optimality conditions with the coupled gradients. We show that the solution set satisfies a pair of discrete-time Sylvester equations with symmetric structure. Interestingly, it is shown that when the aforementioned cross-correlation vanishes, the set collapses into the standard controller-observer pair $(L^{\star},K^{\star})$ (see \[Theorem 2\] and \[Proposition 3\]).

To the best of our knowledge, this work represents the first systematic investigation into the optimality of observer-based dynamic LQR. Our findings offer new theoretical insights for designing policy gradient methods for OD-LQR problems, where the stationary point does not necessarily adhere to the separation principle when optimizing the objective function.

The rest of the work is organized as follows. Section II presents the formulation of OD-LQR problems. Section III presents our main results on policy gradients and stationary points. Numerical experiments are shown in Section IV and Section V concludes this work.

Notations. For $X \in {\mathbb{R}}^{n \times n}$, we use $\rho{(X)}$ to denote its spectral radius. The notations ${\mathbb{S}}_{+}^{n}$ and $X \succeq 0$ (respectively, ${\mathbb{S}}_{+ +}^{n}$ and $X \succ 0$) denotes the set of symmetric $n \times n$ positive semi-definite (respectively, positive definite) matrices. We employ the superscript $\star$ to denote the standard optimal controller $K^{\star}$ in LQR and the standard observer $L^{\star}$ that minimizes the trace of the accumulated state estimation variance, and use $\ddagger$ to denote the stationary points $(K^{\ddagger},L^{\ddagger})$ of OD-LQR problems.

## Problem Statement

### II-A Linear Quadratic Control

Consider a discrete-time linear time-invariant (LTI) system

where $x_{t} \in {\mathbb{R}}^{n}$, $u_{t} \in {\mathbb{R}}^{m}$, and $y_{t} \in {\mathbb{R}}^{d}$ denote the states, control inputs, and observation outputs separately, and $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$, $C \in {\mathbb{R}}^{d \times n}$ are known dynamics. The linear quadratic control aims to find control input $u_{t}$ to minimize the cumulative quadratic utilities:

The initial state distribution for $x_{0}$ is assumed to satisfy that ${{\mathbb{E}}_{x_{0}}{\lbrack{x_{0}x_{0}^{\mathsf{T}}}\rbrack}} \succ 0$, a covariance condition commonly adopted in data-driven control that parallels the persistent excitation requirement. For the above system and problem, we make the following assumptions:

### Assumption 1

$Q \in {\mathbb{S}}_{+}^{n}$, $R \in {\mathbb{S}}_{+ +}^{m}$, $(A,B)$ is controllable, and $(C,A)$ and $(Q^{\frac{1}{2}},A)$ are observable. We maintain generality by considering $C$ to have rows of full rank.

When $C$ coincides with the identity matrix $I_{n}$, the optimal controller takes the static form $u_{t} = {Kx_{t}}$, where $K$ can be derived from the associated Riccati equation. Under 1, observer-based dynamic controllers with stabilization guarantees enjoy computational tractability by the separation principle, which will be presented in Section II-B.

### Remark 1

While a continuous-time variant could be conceptualized, extending it to policy optimization would exacerbate the curse of dimensionality due to function approximation in continuous state-spaces. In contrast, our discrete-time formulation provides exact analytical gradients to circumvent this issue. Furthermore, the mathematical structure changes fundamentally. The continuous-time optimality conditions would manifest as coupled algebraic Riccati equations rather than the symmetric Sylvester equations derived in this work.

### II-B Observer Design

Consider the standard observer-based dynamic controller

with $\mathcal{A}_{K,L}:={A - {BK} - {LC}}$, where $\xi_{t} \in {\mathbb{R}}^{n}$ is the state observation and also the internal state of dynamic controller, $K \in {\mathbb{R}}^{m \times n}$ is the undetermined controller gain, and $L \in {\mathbb{R}}^{n \times d}$ is the observer gain to be solved.

According to the separation principle, the controller is stabilizing if and only if $K$ and $L$ are stabilizing‌ gains. We define the stabilizing set of $K$ and $L$ as

A widely-used selection is to choose $K$ as the standard state-feedback LQR gain $K^{\star}$ and find a stabilizing observer gain using pole assignment method such that $A - {LC}$ converges faster than $A - {BK}$. Although we can obtain a stabilizing observer gain, its optimality with respect to the accumulated quadratic utilities has not been fully considered. Section II-C will analyze the quadratic cost from the perspective of the Lyapunov equation of the augmented system.

### II-C Cost Function in the OD-LQR Problem

The closed-loop dynamics of the LTI system under the dynamic controller is

For the convenience of subsequent analysis, a linear transformation $T$ is performed on the augmented state $\begin{bmatrix}
\end{bmatrix}^{\mathsf{T}}$, resulting in the transformed augmented system state as follows

whose initial distribution is denoted as $\mathcal{B}$. Therefore, the dynamics of the augmented system is expressed as

where $x_{t} - \xi_{t}$ is the observation error. We further denote

then the close-loop system is denoted as

where ${\hat{\mathcal{A}}}_{K,L}:={{\overline{A} - {\hat{B}K\overline{F}}} + {{\hat{F}}^{\mathsf{T}}L\hat{C}}}$, $\overline{F}:=\begin{bmatrix}
\end{bmatrix}$ and $\hat{F}:=\begin{bmatrix}

To link our formulation with the general framework of policy optimization, we first define the value function at time $t$ for the augmented state ${\overline{z}}_{t}$ under fixed gains $(K,L)$ as:

where $S_{t}$ is time-dependent. According to the principle of dynamic programming, the Bellman equation is

As the system evolves and approaches the steady state under stabilizing gains $(K,L)$, the value function becomes time-invariant. This implies the convergence of the value matrix:

Therefore, the quadratic cost functional is formulated as

where $S_{K,L} \in {\mathbb{S}}_{+}^{2n}$ satisfies a Lyapunov equation (8a), as shown in Lemma 1. Let the cumulative state correlation driven by a stabilizing gain $K \in {\mathbb{K}}$ be formally defined as

For each $K \in {\mathbb{K}}$ and $L \in {\mathbb{L}}$, there is an associated $S_{K,L}$ and $\Omega_{K,L}$. These matrices provide a convenient way to express the OD-LQR cost function, as summarized in Lemma 1.

### Lemma 1

\[6, Lemma 1\] For any stabilizing controller $K \in {\mathbb{K}}$ and observer $L \in {\mathbb{L}}$, the OD-LQR cost function is

where $S_{K,L}$ and $\Omega_{K,L}$ constitute the unique positive semi-definite solutions to specified Lyapunov equations

$S_{K,L}$ ${= {\hat{Q} + {{\hat{\mathcal{A}}}_{K,L}^{\mathsf{T}}S_{K,L}{\hat{\mathcal{A}}}_{K,L}}}},$ (8a)
$\Omega_{K,L}$ ${= {Y + {{\hat{\mathcal{A}}}_{K,L}\Omega_{K,L}{\hat{\mathcal{A}}}_{K,L}^{\mathsf{T}}}}},$ (8b)

where $Y:={{\mathbb{E}}_{{\overline{z}}_{0} \sim \mathcal{B}}{\lbrack{{\overline{z}}_{0}{\overline{z}}_{0}^{\mathsf{T}}}\rbrack}}$ is the initial state correlation, and

To facilitate subsequent analysis involving the inversion of positive definite matrices, some requirements are given:

### Assumption 2

The initial correlation $Y$ is independent of the controller and observer gains, and is strictly positive definite.

The above assumptions apply in the sequel. Different from OD-LQR, LQG minimizes a limiting average cost, yields a correlation representing the steady-state covariance, which inherently depends on controller and observer gains. Based on the derived cost function, we formulate the OD-LQR problem:

### Problem 1 (Optimization for OD-LQR)

Suppose ${\overline{z}}_{0}$ follows $\mathcal{B}$. The optimal OD-LQR control is formulated as:

where the cost function $J{(K,L)}$ is calculated , and stabilizing sets $\mathbb{K}$ and $\mathbb{L}$ are defined .

The following gives the connectivity of stabilizing sets.

### Lemma 2 (Domain Connectivity)

The sets of stabilizing controller gain $\mathbb{K}$ and observer gain $\mathbb{L}$ are path-connected.

In this work, the closed-form gradient expressions for $J{(K,L)}$ will be established to characterize the optimization geometry of 1. ‣ II-C Cost Function in the OD-LQR Problem ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"). Prior to delving into theoretical analysis, Section II-D presents the block-wise Lyapunov equations and summarizes the associated Lyapunov stability theorems.

### II-D Block-wise Lyapunov Equations

The block-structured Lyapunov equations in (8a) and (8b) serve as foundational analytical tools in this work, where $S_{K,L}$ can be divided into the following blocks:

For notational conciseness, subscripts $K$ and $L$ in the submatrices of $S_{K,L}$ and $\Omega_{K,L}$ will be omitted when $K$ and $L$ dependencies are clear in the context. From (8a), one has

S_{11} & {{= {Q + {K^{\mathsf{T}}RK} + {\left( {A - {BK}} \right)^{\mathsf{T}}S_{11}\left( {A - {BK}} \right)}}},}
S_{12} & {= {{- {K^{\mathsf{T}}RK}} + {\left( {A - {BK}} \right)^{\mathsf{T}}S_{11}BK}}} \\
& {{+ {\left( {A - {BK}} \right)^{\mathsf{T}}S_{12}\left( {A - {LC}} \right)}},}
S_{22} & {= {{K^{\mathsf{T}}RK} + {K^{\mathsf{T}}B^{\mathsf{T}}S_{11}BK} + {K^{\mathsf{T}}B^{\mathsf{T}}S_{12}\left( {A - {LC}} \right)}}} \\
& {{{+ {\left( {A - {LC}} \right)^{\mathsf{T}}S_{12}^{\mathsf{T}}BK}} + {\left( {A - {LC}} \right)^{\mathsf{T}}S_{22}\left( {A - {LC}} \right)}}.}

where $Y_{22}$ denotes the initial correlation of observation error, and $Y_{12}^{\mathsf{T}}$ indicates the initial cross-correlation between observation error and system state. From (8b), we get

\Omega_{11} & {= {Y_{11} + {\left( {A - {BK}} \right)\Omega_{11}\left( {A - {BK}} \right)^{\mathsf{T}}}}} \\
& {+ {\left( {A - {BK}} \right)\Omega_{12}K^{\mathsf{T}}B^{\mathsf{T}}}} \\
& {{{+ {BK\Omega_{12}^{\mathsf{T}}\left( {A - {BK}} \right)^{\mathsf{T}}}} + {BK\Omega_{22}K^{\mathsf{T}}B^{\mathsf{T}}}},}
\Omega_{12} & {= {Y_{12} + {\left( {A - {BK}} \right)\Omega_{12}\left( {A - {LC}} \right)^{\mathsf{T}}}}} \\
& {{+ {BK\Omega_{22}\left( {A - {LC}} \right)^{\mathsf{T}}}},}
\Omega_{22} & {{= {Y_{22} + {\left( {A - {LC}} \right)\Omega_{22}\left( {A - {LC}} \right)^{\mathsf{T}}}}}.}

Lyapunov stability theorems will be employed as analytical fundamentals. Essential propositions are compiled as follows:

### Lemma 3 (Lyapunov Stability Theorems )

If ${\rho{(A)}} < 1$ and $Q \in {\mathbb{S}}_{+}^{n}$, the Lyapunov equation $P = {Q + {A^{\mathsf{T}}PA}}$ has a unique solution $P \in {\mathbb{S}}_{+}^{n}$.

Let $Q \in {\mathbb{S}}_{+ +}^{n}$. ${\rho{(A)}} < 1$ if and only if there exists a unique $P \in {\mathbb{S}}_{+ +}^{n}$ such that $P = {Q + {A^{\mathsf{T}}PA}}$.

## Gradients and Stationary Points

This section first establishes the closed-form gradients of the OD-LQR cost with respect to feedback controller gain $K$ and state observer gain $L$. Then, we investigate the stationary point where the gradients vanish and establish its relationship between the standard LQR controller and standard observer. Finally, we derive the stationary point of the OD-LQR problem through the Sylvester equation and explore the specific conditions under which the stationary point collapses into the standard controller-observer pair.

### III-A The Gradient of the OD-LQR Cost

The gradient of OD-LQR problem is the basis for analyzing stationary points. Lemma 4. ‣ III-A The Gradient of the OD-LQR Cost ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") develops analytical expressions for the gradients of the OD-LQR cost function with respect to the controller and observer gains.

### Lemma 4 (Policy Gradient)

Given any stabilizing controller gain $K \in {\mathbb{K}}$ and observer gain $L \in {\mathbb{L}}$, the gradients are

### Proof

The proof methodology parallels the state-feedback LQR framework \[8, Lemma 1\]. According to the specified Lyapunov equation (8a), the cost function of ${\overline{z}}_{0}$ is

Taking the gradient of $V_{K,L}{({\overline{z}}_{0})}$ with respect to $K$, one has

where the last equation follows by recursion and the fact that ${\overline{z}}_{t + 1} = {{\hat{\mathcal{A}}}_{K,L}{\overline{z}}_{t}} = {{({{\overline{A} - {\hat{B}K\overline{F}}} + {{\hat{F}}^{\mathsf{T}}L\hat{C}}})}{\overline{z}}_{t}}$.

By calculating the stochastic average of gradient expressions across the initial distribution $\mathcal{B}$, we have (13. ‣ III-A The Gradient of the OD-LQR Cost ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")). ∎

The obtained gradient expression is related to the positive semi-definite solutions $S_{K,L}$ and $\Omega_{K,L}$ to the Lyapunov equations. Section III-B will utilize $S_{K,L}$ and $\Omega_{K,L}$ to represent the standard LQR controller and standard observer minimizing the accumulated estimation variance, respectively. Before that, we will present the results about gradient dominance.

### Lemma 5 (Gradient Dominance)

Assuming that the closed-loop matrix ${\hat{\mathcal{A}}}_{K,L}$ admits a uniform spectral norm, i.e., ${\|{\hat{\mathcal{A}}}_{K,L}\|}_{2} \leq \gamma < 1$, there exist local attraction radii $r_{K} > 0$ and $r_{L} > 0$, such that for all controller gain $K$ and observer gain $L$ satisfying ${\|{\DeltaK}\|}_{F} \leq r_{K}$ and ${\|{\DeltaL}\|}_{F} \leq r_{L}$, the cost difference is upper bounded by

where the coefficients associated with the controller gain $K$ and the observer gain $L$ exhibit strictly decoupled structures.

### Proof

See Proof of Lemma 5 for the proof. ∎

### III-B Standard LQR Controller and Standard Observer

According to the classical control theory, the standard optimal state-feedback controller gain for the linear system under the quadratic cost is

where ${\hat{S}}^{\star}$ is the unique positive definite solution to

Note that the above equation is equivalent to

which is similar to the block-wise Lyapunov equation (10a).

If $(K,\mathcal{A}_{K,L})$ is observable, then the dynamic controller is referred as observable. The set of observable controllers under the standard LQR controller gain $K^{\star}$ is denoted as

The following result on the unique positive definite solution of the Lyapunov equation directly follows from Lemma 3. ‣ II-D Block-wise Lyapunov Equations ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control").

### Lemma 6

If $L \in {{\mathbb{L}} \cap {\mathbb{L}}_{o}}$ and ${\rho\left( \mathcal{A}_{K^{\star},L} \right)} < 1$, the solution $S_{K^{\star},L}$ to (8a) is unique and positive definite. Specifically, the blocks of the solution $S_{K^{\star},L}$ satisfy $S_{11}^{\star} = {\hat{S}}^{\star}$ and $S_{12}^{\star} = 0$.

### Proof

Consider the block-wise Lyapunov equation (10a) with fixed dynamics system, where $S_{11}$ only depends on $K$. In particular, for the standard LQR controller $K^{\star}$, the closed-loop system $A - {BK^{\star}}$ is stable. According to Lemma 3. ‣ II-D Block-wise Lyapunov Equations ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")(a), the solution to (10a) with $K^{\star}$, denoted as $S_{11}^{\star}$, is unique. Since the block-wise Lyapunov equation (10a) shares the same structure as the Lyapunov equation, we have $S_{11}^{\star} = {\hat{S}}^{\star}$.

Substituting the standard LQR controller gain $K^{\star}$ into the block-wise Lyapunov equation (10b) yields

By adapting the analysis framework of the unique solution of the Lyapunov equation in \[3, Theorem 8.2.2\], and noting that ${\rho{({A - {BK^{\star}}})}} < 1$ and ${\rho{({A - {LC}})}} < 1$ imply that the product of any eigenvalue pair is strictly less than one, the above Sylvester equation has a unique solution, namely $S_{12}^{\star} = 0$. ∎

Next, the observer gain $L^{\star}$ that minimizes the accumulated estimation variance is introduced. Define the estimation variance at $t$ under observer $L$ as $E_{t}:={{\mathbb{E}}_{{\overline{z}}_{0} \sim \mathcal{B}}{\lbrack{{({x_{t} - \xi_{t}})}{({x_{t} - \xi_{t}})}^{\mathsf{T}}}\rbrack}}$. It is not hard to find that $E_{0} = Y_{22}$. Subtracting , we can derive that

From, we define the accumulated state estimation variance under a stabilizing observer $L \in {\mathbb{L}}$ as ${\hat{\Omega}}_{L}:={\sum_{t = 0}^{\infty}E_{t}}$. Therefore, ${\hat{\Omega}}_{L}$ satisfies the following Lyapunov equation

which is exactly the block-wise Lyapunov equation (12c). Thus, for any stabilizing observer $L \in {\mathbb{L}}$, we have $\Omega_{22} = {\hat{\Omega}}_{L}$. 2. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") further gives the definition of the standard observer.

### Problem 2 (Standard Observer)

A standard observer of system is defined as the one that minimizes the trace of the accumulated state estimation variance ${\hat{\Omega}}_{L}$, whose gain $L^{\star}$ should be the optimal solution to

The cost function ${Tr}{({\hat{\Omega}}_{L})}$ denotes the sum of estimation variance, which is analogous to LQR by viewing the estimation error dynamics with $L$ as the state-feedback gain. Moreover, the constraint acts as an evaluation equation for the cost, which compresses the infinite-horizon summation into a self-consistent equation. The following proposition provides the formulation to calculate the standard observer $L^{\star}$, which follows the solution to the Riccati equation \[6, Prop. 3\].

### Proposition 1 (Standard Observer Gain)

The standard observer gain is in the form of

with ${\hat{\Omega}}_{L^{\star}}$ being the unique positive definite solution to

### III-C Structure of the Stationary Point

This section will further investigate the stationary point at which the gradients vanish. We will first reveal the relationship between the stationary point, the standard LQR controller $K^{\star}$, and the standard observer $L^{\star}$. Then, we will derive the expression the stationary point and discuss the special case of the derived stationary point collapsing into the standard pair. Theorem 1 establishes the observer achieving the optimal cost function under the standard LQR controller.

### Theorem 1

Given the standard LQR controller gain $K^{\star}$, the standard observer $L^{\star}$ defined in (21. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")) is a stationary point of $J{(K^{\star},L)}$. If $L^{\star} \in {\mathbb{L}}_{o}$, $L^{\star}$ is the unique observable stationary point. Otherwise, no observable stationary point exists.

### Proof

Applying the partitions defined in and, the policy gradient ${\nabla_{L}J}{(K,L)}$ in (13. ‣ III-A The Gradient of the OD-LQR Cost ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")) can be expanded as

Substituting the standard LQR controller $K^{\star}$ derives that

Note that $E_{0} = Y_{22}$, and the Lyapunov equations (12c) and have the same expression. By Lemma 3. ‣ II-D Block-wise Lyapunov Equations ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")(b), we have $\Omega_{22} = {\hat{\Omega}}_{L} \in {\mathbb{S}}_{+ +}^{n}$ since $E_{0} \in {\mathbb{S}}_{+ +}^{n}$. It directly follows that

This completes the proof of the first claim.

By Lemma 6, $S_{K^{\star},L} \in {\mathbb{S}}_{+ +}^{2n}$ for any $L \in {\mathbb{L}}_{o}$, which directly leads to $S_{22}^{\star} \in {\mathbb{S}}_{+ +}^{n}$. Since $\Omega_{22} \in {\mathbb{S}}_{+ +}^{n}$ and $C$ has rows of full rank, we have ${C\Omega_{22}C^{\mathsf{T}}} \in {\mathbb{S}}_{+ +}^{n}$. Therefore, by combining with (22. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")), $L^{\star}$ is the unique observable stationary point. ∎

The key to the proof is that when the controller adopts the standard LQR controller $K^{\star}$, the block matrix $S_{12}^{\star} = 0$, *i.e.*, the objective function is independent of the cross term between the state $x_{t}$ and the state estimation error $x_{t} - \xi_{t}$. In contrast, the accumulated state correlation matrix $\Omega_{K,L}$ lacks such good properties, rendering it challenging to derive that the derivative of the cost function about the controller gain vanishes, as shown in Proposition 2.

### Proposition 2

When ${K^{\star}{({\Omega_{22} - \Omega_{12}^{\mathsf{T}}})}} \neq 0$ and the observation error correlation $Y_{22}$ is not equal to the cross-correlation $Y_{12}^{\mathsf{T}}$ with system state, $K^{\star}$ defined in and $L^{\star}$ defined in (21. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")) cannot constitute the stationary point of 1. ‣ II-C Cost Function in the OD-LQR Problem ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control").

### Proof

We will show that if ${{{\nabla_{K}J}{(K,L^{\star})}}|}_{K = K^{\star}} = 0$, then ${K^{\star}{({\Omega_{22} - \Omega_{12}^{\mathsf{T}}})}} = 0$ or ${Y_{22} - Y_{12}^{\mathsf{T}}} = 0$. Similar to, the policy gradient ${\nabla_{K}J}{(K,L)}$ in (13. ‣ III-A The Gradient of the OD-LQR Cost ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")) can be expanded as

where $\Sigma_{22}:={{\mathbb{E}}_{{\overline{z}}_{0} \sim \mathcal{B}}{\lbrack{\sum_{t = 0}^{\infty}{\xi_{t}\xi_{t}^{\mathsf{T}}}}\rbrack}} = {{\Omega_{11} - \Omega_{12} - \Omega_{12}^{\mathsf{T}}} + \Omega_{22}}$ denotes the accumulated correlation of the internal state.

Note that we have $K^{\star} = {{({R + {B^{\mathsf{T}}{\hat{S}}^{\star}B}})}^{- 1}B^{\mathsf{T}}{\hat{S}}^{\star}A}$ and $S_{11}^{\star} = {\hat{S}}^{\star}$. Substituting and (21. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")) into yields

Subtracting the transpose of (12b) from (12c), and applying the standard LQR controller and observer (21. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")), one has

Since ${R + {B^{\mathsf{T}}{\hat{S}}^{\star}B}} \succ 0$, if ${{{\nabla_{K}J}{(K,L^{\star})}}|}_{K = K^{\star}} = 0$, then ${K^{\star}{({\Omega_{22} - \Omega_{12}^{\mathsf{T}}})}} = 0$ or ${Y_{22} - Y_{12}^{\mathsf{T}}} = 0$, which completes the proof. It is also clear that $K^{\star}$ is generally suboptimal in terms of achieving the minimal cost under the standard observer $L^{\star}$ for general initial state correlation matrix $Y$. ∎

The above proposition excludes the possibility of the standard LQR controller $K^{\star}$ and observer $L^{\star}$ forming the stationary point of 1. ‣ II-C Cost Function in the OD-LQR Problem ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") unless ${K^{\star}{({\Omega_{22} - \Omega_{12}^{\mathsf{T}}})}} = 0$ or

that is, the initial cross-correlation between observation error $x_{0} - \xi_{0}$ and state observation $\xi_{0}$ exactly vanishes. Subsequent numerical experiments in Section IV will present that the stationary point obtained through numerical methods are generally independent of the standard LQR controller $K^{\star}$ and the standard observer $L^{\star}$. The following theorem will combine the policy gradient expressions in Lemma 4. ‣ III-A The Gradient of the OD-LQR Cost ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") and derive the conditions that the stationary point satisfies.

### Theorem 2

Suppose that $B$ has columns of full rank. The stationary point of $J{(K^{\ddagger},L^{\ddagger})}$ in 1. ‣ II-C Cost Function in the OD-LQR Problem ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") satisfies the following discrete-time Sylvester equations:

### Proof

Letting the gradients and vanish, we have

$- {R_{K}^{- 1}B^{\mathsf{T}}S_{12}L^{\ddagger}C{({\Omega_{12}^{\mathsf{T}} - \Omega_{22}})}\Sigma_{22}^{- 1}}$
${= {K^{\circ} - {R_{K}^{- 1}B^{\mathsf{T}}S_{12}L^{\ddagger}C{({\Omega_{12}^{\mathsf{T}} - \Omega_{22}})}\Sigma_{22}^{- 1}}}},$ (28a)
$L^{\ddagger}$ $= {{A\Omega_{22}C^{\mathsf{T}}{({C\Omega_{22}C^{\mathsf{T}}})}^{- 1}} + {S_{22}^{- 1}S_{12}^{\mathsf{T}}A\Omega_{12}C^{\mathsf{T}}{({C\Omega_{22}C^{\mathsf{T}}})}^{- 1}}}$
$- {S_{22}^{- 1}S_{12}^{\mathsf{T}}BK^{\ddagger}{({\Omega_{12} - \Omega_{22}})}C^{\mathsf{T}}{({C\Omega_{22}C^{\mathsf{T}}})}^{- 1}}$
${= {L^{\circ} - {S_{22}^{- 1}S_{12}^{\mathsf{T}}BK^{\ddagger}{({\Omega_{12} - \Omega_{22}})}C^{\mathsf{T}}{({C\Omega_{22}C^{\mathsf{T}}})}^{- 1}}}}.$ (28b)

Combining the above equations yields

which completes the proof. ∎

The derived discrete-time Sylvester equations can be solved by utilizing the dlyap instruction in MATLAB. The Sylvester equation (27a) about the controller $K^{\ddagger}$ has a unique solution if and only if ${\lambda_{i}\mu_{j}} \neq 1$ for all $i = {1,\cdots,m}$ and $j = {1,\cdots,n}$, where $\lambda_{1},\cdots,\lambda_{m}$ are the eigenvalues of $R_{K}^{- 1}M$, and $\mu_{1},\cdots,\mu_{n}$ are the eigenvalues of $N\Sigma_{22}^{- 1}$, and the same applies to the Sylvester equation (27b) about the observer $L^{\ddagger}$.

Unlike the independent assignment of the poles of feedback controller and state observer, the controller $K^{\ddagger}$ and observer $L^{\ddagger}$ depend on each other and jointly affect the objective function. Although the derived Sylvester equations are coupled, they have good symmetry. By utilizing the influence of the standard controller-observer pair $(K^{\star},L^{\star})$ on matrices $S_{12}$ and $\Omega_{12}^{\mathsf{T}} - \Omega_{22}$, the following Proposition will further investigate the relationship between the stationary point $(K^{\ddagger},L^{\ddagger})$ and the standard controller-observer pair $(K^{\star},L^{\star})$.

### Proposition 3

Given the standard observer $L^{\star}$ or the standard LQR controller $K^{\star}$ with the special initial state correlation satisfying ${Y_{22} - Y_{12}^{\mathsf{T}}} = 0$, the derived stationary point $(K^{\ddagger},L^{\ddagger})$ will degrade into the ordinary pair $(K^{\star},L^{\star})$.

### Proof

Considering the special initial correlation ${Y_{22} - Y_{12}^{\mathsf{T}}} = 0$, one has ${\Omega_{22} - \Omega_{12}^{\mathsf{T}}} = 0$. Therefore, $N = 0$, $G_{K} = K^{\circ}$, $V = 0$, $G_{L} = L^{\circ}$, and the Sylvester equations can be simplified to

Since $S_{11}$ only depends on $K^{\ddagger}$, $K^{\ddagger} = K^{\star}$. According to Lemma 6, $S_{12} = 0$, and $L^{\ddagger} = {A\Omega_{22}C^{\mathsf{T}}{({C\Omega_{22}C^{\mathsf{T}}})}^{- 1}}$. Since $\Omega_{22}$ only depends on $L^{\ddagger}$, we find that $L^{\ddagger} = L^{\star}$ holds exactly.

Given the standard LQR controller $K^{\star}$, according to Lemma 6, $S_{12} = 0$. Thus, $M = 0$, $G_{K} = K^{\circ}$, $U = 0$, $G_{L} = L^{\circ}$, and the Sylvester equations can be simplified to

Since $\Omega_{22}$ only depends on $L^{\ddagger}$, $L^{\ddagger} = L^{\star}$. Similarly, considering the special initial correlation ${Y_{22} - Y_{12}^{\mathsf{T}}} = 0$, one has ${\Omega_{22} - \Omega_{12}^{\mathsf{T}}} = 0$ and $K^{\ddagger} = {R_{K}^{- 1}B^{\mathsf{T}}S_{11}A}$. Since $S_{11}$ only depends on $K^{\ddagger}$, we find that $K^{\ddagger} = K^{\star}$ holds exactly. ∎

### Remark 2

The condition $Y_{22} = Y_{12}^{\mathsf{T}}$ implies $\Omega_{22} = \Omega_{12}^{\mathsf{T}}$ for the derived stationary point, which reduces to the standard pair and can be designed separately. This statistical orthogonality eliminates the influence of initial correlation on the optimal gains and recovers the certainty equivalence property.

## Experiment

In this section, we will compare the costs and gradients of the standard LQR controller-observer pair and the stationary point of OD-LQR obtained through numerical methods.

### IV-A Internally Unstable Linear System

Take the discrete version of the Doyle's LQG example

which is derived from a physical double-integrator model under a specific coordinate transformation. The selected plant is internally unstable. Experiment results for stable systems are provided in the open-source code.^11^1The code is available at Let $Q = {0.25I_{2}}$, $R = 0.2$. The standard LQR controller $K^{\star} = \begin{bmatrix}
\end{bmatrix}$ can be directly obtained by solving the discrete-time algebraic Riccati equation. Rather, the standard observer minimizing the accumulated estimation variance is determined by the initial estimation variance $E_{0}$. The following will explore the results of general and special initial state correlations separately:

1\) General Initial State Correlation $Y_{g}$: The standard observer $L^{\star} = \begin{bmatrix}
\end{bmatrix}^{\mathsf{T}}$ can be solved through the algebraic Riccati equation (22. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")). The cost function of $L^{\star}$ under the standard LQR controller $K^{\star}$ is shown by the red dot in Fig. 1(a) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"), and the white space denotes unstable ${\hat{\mathcal{A}}}_{K,L}$, where the Lyapunov equations are unsolvable and the cost value is undefined. The unique minimum obtained by numerical search indicates that the standard observer $L^{\star}$ achieves optimality given the standard LQR controller $K^{\star}$. The norm of the gradient of cost function with respect to $L$ depicted in Fig. 1(b) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") shows that $L^{\star}$ is a stationary point of $J{(K^{\star},L)}$.

The landscape of the cost function of controller $K$ under the standard observer $L^{\star}$ is shown in Fig. 1(c) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"), where the cost value of the minimum point is smaller than that of the standard LQR controller $K^{\star}$. Besides, the gradient of cost function for the minimum point vanishes, as shown in Fig. 1(d) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"). By employing the dlyap instruction, the stationary point $K^{\ddagger} = \begin{bmatrix}
\end{bmatrix}$ and $L^{\ddagger} = \begin{bmatrix}
\end{bmatrix}^{\mathsf{T}}$ derived in Theorem 2, whose cost value is 102.2875, can be obtained numerically. Therefore, the experimental results indicate that the standard controller-observer pair $(K^{\star},L^{\star})$ is generally different from the stationary point of the OD-LQR problem, and the standard LQR controller $K^{\star}$ is generally suboptimal when paired with the standard observer $L^{\star}$.

(a) Cost function under K⋆

(b) Norm of grad w.r.t L under K⋆

(c) Cost function under L⋆

(d) Norm of grad w.r.t K under L⋆

Figure 1: Results of general initial state correlation

2\) Special Initial State Correlation $Y_{s}$: Since $Y_{22}$ is the same as the previous case, the standard observer $L^{\star}$ is also the same. The cost values of various observers under $K^{\star}$ are depicted in Fig. 2(a) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"). It can be found that the standard observer $L^{\star}$ achieves the minimum cost value when paired with the standard LQR controller $K^{\star}$. Similarly, the gradient norm of the cost function for diverse observers shown in Fig. 2(b) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") indicates that $L^{\star}$ is a stationary point of $J{(K^{\star},L)}$.

The cost function of different controllers operating with the standard observer $L^{\star}$ is illustrated in Fig. 2(c) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"). Different from the previous case, the minimal cost value identified through numerical grid search coincides exactly with the cost value of the standard LQR controller $K^{\star}$. Besides, as shown in Fig. 2(d) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"), the gradient of cost function for the standard LQR controller $K^{\star}$ vanishes. Therefore, for the special initial correlation ${Y_{22} - Y_{12}^{\mathsf{T}}} = 0$, the standard controller-observer pair $(K^{\star},L^{\star})$ is a stationary point, which shows control optimality.

(a) Cost function under K⋆

(b) Norm of grad w.r.t L under K⋆

(c) Cost function under L⋆

(d) Norm of grad w.r.t K under L⋆

Figure 2: Results of special initial state correlation

### IV-B Unstable System with 2D Controller and 2D Observer

Consider the system with complex controller and observer:

For $Y_{g}$ and $Y_{s}$, we separately solved the standard controller-observer pair $(K^{\star},L^{\star})$ and identified the stationary point $(K^{\ddagger},L^{\ddagger})$ of OD-LQR. The results in Table I indicate that, for the general initial state correlation $Y_{g}$, the stationary point $(K^{\ddagger},L^{\ddagger})$ is different from $(K^{\star},L^{\star})$, and achieves a slightly lower cost value compared with the standard LQR; while for the special initial state correlation $Y_{s}$ with $Y_{22} = Y_{12}^{\mathsf{T}}$, the cost values are consistent. The results confirm that the theory remain valid for the higher-dimensional system.

TABLE I: Comparison of cost values

## Conclusion

In this work, we have explored the optimality of observer-controller pair on the cost function for OD-LQR problems. Based on the derived gradient expressions, we have demonstrated that the standard observer gain minimizing the accumulated estimation variance ensures optimality under the standard LQR controller. However, the standard LQR controller usually fails to achieve the optimal performance under the standard observer, unless the initial state correlations have a special structure. Moreover, we have characterized the stationary point of OD-LQR by Sylvester equations and proved that it reduces to the standard pair under the special initial state correlation, thereby recovering the separation principle. Our examples provide empirical support for the proposed theoretical results. Beyond providing practical guidance for separation-based controller designs, the derived Sylvester equations open a distinct pathway for data-driven methods in dynamic control, shifting the paradigm away from traditional Bellman equations.
