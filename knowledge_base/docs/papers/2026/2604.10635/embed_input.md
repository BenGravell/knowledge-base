<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control

Topics include Policy gradients, Reinforcement learning, Optimization, Control, Learning, Linear quadratic regulator, Linear quadratic Gaussian.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Understanding the optimization landscape of linear quadratic regulation (LQR) problems is fundamental to the design of efficient reinforcement learning solutions. Recent work has made significant progress in characterizing the landscape of static output-feedback control and linear quadratic Gaussian (LQG) control. For LQG, much of the analysis leverages the separation principle, which allows the controller and estimator to be designed independently. However, this simplification breaks down when the gradients with respect to the estimator and controller parameters are inherently coupled, leading to a more intricate analysis. This paper investigates the optimization landscape of observer-based dynamic output-feedback control of LQR problems. We derive the optimal observer-controller pair in settings where transient quadratic performance cannot be neglected. Our analysis reveals that, in general, the combination of the standard LQR controller and the observer that minimizes the trace of the accumulated estimation error covariance does not correspond to a stationary point of the overall closed-loop performance objective. Moreover, we derive a pair of discrete-time Sylvester equations with symmetric structure, both involving the same set of matrix elements, that characterize the stationary point of the observer-based dynamic LQR problem.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These equations offer analytical insight into the structure of the optimality conditions and provide a foundation for developing numerical policy gradient methods aimed at learning complex controllers that rely on reconstructed state information.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The linear quadratic regulation (LQR) problem serves as a fundamental research topic within the realm of control theory, whose optimal controller has a static state-feedback form. During the past few years, theoretical analysis work targeting the LQR control has made substantial progress, laying the foundation for policy structures \[20 control")\], convergence guarantees, efficiency improvements, and sample complexity. However, due to the practical challenges of obtaining full state information, output-feedback control warrants further investigation as a more realistic and significant controller design approach.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some recent works have studied the optimization landscape of static output-feedback control. The necessary and sufficient conditions for the stability of static output-feedback (SOF) controllers are derived by bridging the error between state-feedback gain and output-feedback gain. On the other hand, further research has delved into the optimization landscape of dynamic output-feedback linear quadratic regulation (dLQR). proved the observable stationary point of dLQR is unique. proposed an alternative policy parameterization using the past input-output trajectory of finite length as feedback and established a global convergence guarantee. Robustness constraints have been incorporated in the design of dynamical controllers, where the feasible set of stabilizing controllers is proved to have at most two connected components. The global optimality of the standard $H_{\infty}$ robust control with non-degenerated stabilizing dynamical structures is further considered, which reveals that all Clarke stationary points are globally optimal despite the non-smoothness of $H_{\infty}$ cost function.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For stochastic dynamics, the linear quadratic Gaussian (LQG) problem is analyzed from the perspectives of the connectivity of stabilizing controllers and the structure of stationary points \[20 control")\]. For unknown systems, model-free learning methods have been designed for dLQR with convergence and optimality analysis.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although static output-feedback LQR offers greater design flexibility, observer-based output-feedback can achieve performance closer to that of full state-feedback control by leveraging reconstructed state information. This advantage stems from the separation principle, which enables independent pole placement for state observers and feedback controllers. Given that pole locations dominate the convergence rate of estimation error and the performance deviation from the state-feedback control, such structural decoupling has important theoretical significance. However, for policy gradient method of solving LQG, it has been demonstrated in LQG problems that the gradients of the objective function with respect to the controller and observer are not separable. Based on the derived gradients, policy gradient methods demonstrate efficacy in optimizing the controller-observer pair for observer-based dynamic LQR (OD-LQR) problems through dynamical system augmentation. However, the analysis there overlooks the transient performance and hence cannot guarantee the optimality. Moreover, existing works only focus on developing numerical solutions. They lack rigorous analysis of both the optimality conditions and the effect of the transient quadratic performance on the optimization landscape.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we investigate the stationary point of dynamic output-feedback LQR control with a state observer, providing novel insights into the optimality conditions of observer-based LQR. Our main theoretical results are summarized as follows: We derive an analytical expression for the standard observer gain $L^{\star}$, which minimizes the accumulated estimation variance. This gain serves as the optimal observer gain for OD-LQR, analogous to the optimal filter gain in the LQG setting. Unlike observer gains determined via pole assignment, which lacks transient performance guarantee, our theoretical analysis and numerical results demonstrate that $L^{\star}$ ensures control optimality under the standard state-feedback LQR gain $K^{\star}$ \[Theorem 1\].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using policy gradient expressions, we analyze the optimization landscape of OD-LQR. Our results demonstrate that while the standard LQR gain $K^{\star}$ is commonly used in observer-based designs, it is generally only suboptimal in achieving the minimal quadratic performance when combined with the standard observer gain $L^{\star}$ in the OD-LQR problem. It becomes optimal when the initial cross-correlation between observation error and state observation vanishes \[Proposition 2\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive the set of stationary points of the OD-LQR problem by solving the first-order optimality conditions with the coupled gradients. We show that the solution set satisfies a pair of discrete-time Sylvester equations with symmetric structure. Interestingly, it is shown that when the aforementioned cross-correlation vanishes, the set collapses into the standard controller-observer pair $(L^{\star},K^{\star})$ (see \[Theorem 2\] and \[Proposition 3\]).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, this work represents the first systematic investigation into the optimality of observer-based dynamic LQR. Our findings offer new theoretical insights for designing policy gradient methods for OD-LQR problems, where the stationary point does not necessarily adhere to the separation principle when optimizing the objective function.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the work is organized as follows. Section II presents the formulation of OD-LQR problems. Section III presents our main results on policy gradients and stationary points. Numerical experiments are shown in Section IV and Section V concludes this work.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations. For $X\in\mathbb{R}^{n\times n}$, we use $\rho(X)$ to denote its spectral radius. The notations $\mathbb{S}^{n}_{+}$ and $X\succeq 0$ (respectively, $\mathbb{S}^{n}_{++}$ and $X\succ 0$) denotes the set of symmetric $n\times n$ positive semi-definite (respectively, positive definite) matrices. We employ the superscript $\star$ to denote the standard optimal controller $K^{\star}$ in LQR and the standard observer $L^{\star}$ that minimizes the trace of the accumulated state estimation variance, and use $\ddagger$ to denote the stationary points $(K^{\ddagger},L^{\ddagger})$ of OD-LQR problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Linear Quadratic Control", "weight": 1.0} -->

Consider a discrete-time linear time-invariant (LTI) system where $x_{t}\in\mathbb{R}^{n}$, $u_{t}\in\mathbb{R}^{m}$, and $y_{t}\in\mathbb{R}^{d}$ denote the states, control inputs, and observation outputs separately, and $A\in\mathbb{R}^{n\times n}$, $B\in\mathbb{R}^{n\times m}$, $C\in\mathbb{R}^{d\times n}$ are known dynamics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Linear Quadratic Control", "weight": 1.0} -->

The linear quadratic control aims to find control input $u_{t}$ to minimize the cumulative quadratic utilities: The initial state distribution for $x_{0}$ is assumed to satisfy that $\mathbb{E}_{x_{0}}[x_{0}x_{0}^{{{\mathsf{T}}}}]\succ 0$, a covariance condition commonly adopted in data-driven control that parallels the persistent excitation requirement.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$Q\in\mathbb{S}_{+}^{n}$, $R\in\mathbb{S}_{++}^{m}$, $(A,B)$ is controllable, and $(C,A)$ and $(Q^{\frac{1}{2}},A)$ are observable. We maintain generality by considering $C$ to have rows of full rank.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

When $C$ coincides with the identity matrix $I_{n}$, the optimal controller takes the static form $u_{t}=Kx_{t}$, where $K$ can be derived from the associated Riccati equation. Under 1, observer-based dynamic controllers with stabilization guarantees enjoy computational tractability by the separation principle, which will be presented in Section II-B.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1", "weight": 1.0} -->

While a continuous-time variant could be conceptualized, extending it to policy optimization would exacerbate the curse of dimensionality due to function approximation in continuous state-spaces. In contrast, our discrete-time formulation provides exact analytical gradients to circumvent this issue. Furthermore, the mathematical structure changes fundamentally. The continuous-time optimality conditions would manifest as coupled algebraic Riccati equations rather than the symmetric Sylvester equations derived in this work.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Observer Design", "weight": 1.0} -->

Consider the standard observer-based dynamic controller | | $\displaystyle\xi_{t+1}$ | $\displaystyle=\mathcal{A}_{K,L}\xi_{t}+Ly_{t},$ | | \(3\) | with $\mathcal{A}_{K,L}:=A-BK-LC$, where $\xi_{t}\in\mathbb{R}^{n}$ is the state observation and also the internal state of dynamic controller, $K\in\mathbb{R}^{m\times n}$ is the undetermined controller gain, and $L\in\mathbb{R}^{n\times d}$ is the observer gain to be solved.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Observer Design", "weight": 1.0} -->

According to the separation principle, the controller is stabilizing if and only if $K$ and $L$ are stabilizing‌ gains. We define the stabilizing set of $K$ and $L$ as | | $\displaystyle\mathbb{K}:$ | $\displaystyle=\{K\in\mathbb{R}^{m\times n}:\rho(A-BK)<1\},$ | | \(4\) | | | $\displaystyle\mathbb{L}:$ | $\displaystyle=\{L\in\mathbb{R}^{n\times d}:\rho(A-LC)<1\}.$ | | | A widely-used selection is to choose $K$ as the standard state-feedback LQR gain $K^{\star}$ and find a stabilizing observer gain using pole assignment method such that $A-LC$ converges faster than $A-BK$. Although we can obtain a stabilizing observer gain, its optimality with respect to the accumulated quadratic utilities has not been fully considered.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Observer Design", "weight": 1.0} -->

Section II-C will analyze the quadratic cost from the perspective of the Lyapunov equation of the augmented system.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Cost Function in the OD-LQR Problem", "weight": 1.0} -->

The closed-loop dynamics of the LTI system under the dynamic controller is For the convenience of subsequent analysis, a linear transformation $T$ is performed on the augmented state $\begin{bmatrix}x^{{{\mathsf{T}}}}_{t}&\xi^{{{\mathsf{T}}}}_{t}\end{bmatrix}^{{{\mathsf{T}}}}$, resulting in the transformed augmented system state as follows whose initial distribution is denoted as $\mathcal{B}$. Therefore, the dynamics of the augmented system is expressed as where $x_{t}-\xi_{t}$ is the observation error.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Cost Function in the OD-LQR Problem", "weight": 1.0} -->

To link our formulation with the general framework of policy optimization, we first define the value function at time $t$ for the augmented state $\bar{z}_{t}$ under fixed gains $(K,L)$ as: where $S_{t}$ is time-dependent. According to the principle of dynamic programming, the Bellman equation is As the system evolves and approaches the steady state under stabilizing gains $(K,L)$, the value function becomes time-invariant. This implies the convergence of the value matrix: Therefore, the quadratic cost functional is formulated as where $S_{K,L}\in\mathbb{S}_{+}^{2n}$ satisfies a Lyapunov equation (8a), as shown in Lemma 1. Let the cumulative state correlation driven by a stabilizing gain $K\in\mathbb{K}$ be formally defined as For each $K\in\mathbb{K}$ and $L\in\mathbb{L}$, there is an associated $S_{K,L}$ and $\Omega_{K,L}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Cost Function in the OD-LQR Problem", "weight": 1.0} -->

These matrices provide a convenient way to express the OD-LQR cost function, as summarized in Lemma 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The initial correlation $Y$ is independent of the controller and observer gains, and is strictly positive definite.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The above assumptions apply in the sequel. Different from OD-LQR, LQG minimizes a limiting average cost, yields a correlation representing the steady-state covariance, which inherently depends on controller and observer gains.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 1 (Optimization for OD-LQR)", "weight": 1.0} -->

Suppose $\bar{z}_{0}$ follows $\mathcal{B}$. The optimal OD-LQR control is formulated as: where the cost function $J(K,L)$ is calculated, and stabilizing sets $\mathbb{K}$ and $\mathbb{L}$ are defined.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 1 (Optimization for OD-LQR)", "weight": 1.0} -->

The following gives the connectivity of stabilizing sets.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-D Block-wise Lyapunov Equations", "weight": 1.0} -->

The block-structured Lyapunov equations in (8a) and (8b) serve as foundational analytical tools in this work, where $S_{K,L}$ can be divided into the following blocks: For notational conciseness, subscripts $K$ and $L$ in the submatrices of $S_{K,L}$ and $\Omega_{K,L}$ will be omitted when $K$ and $L$ dependencies are clear in the context. From (8a), one has where $Y_{22}$ denotes the initial correlation of observation error, and $Y_{12}^{{{\mathsf{T}}}}$ indicates the initial cross-correlation between observation error and system state. From (8b), we get Lyapunov stability theorems will be employed as analytical fundamentals.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Gradients and Stationary Points", "weight": 1.0} -->

This section first establishes the closed-form gradients of the OD-LQR cost with respect to feedback controller gain $K$ and state observer gain $L$. Then, we investigate the stationary point where the gradients vanish and establish its relationship between the standard LQR controller and standard observer. Finally, we derive the stationary point of the OD-LQR problem through the Sylvester equation and explore the specific conditions under which the stationary point collapses into the standard controller-observer pair.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A The Gradient of the OD-LQR Cost", "weight": 1.0} -->

The gradient of OD-LQR problem is the basis for analyzing stationary points. Lemma 4. ‣ III-A The Gradient of the OD-LQR Cost ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") develops analytical expressions for the gradients of the OD-LQR cost function with respect to the controller and observer gains.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Standard LQR Controller and Standard Observer", "weight": 1.0} -->

According to the classical control theory, the standard optimal state-feedback controller gain for the linear system under the quadratic cost is where $\hat{S}^{\star}$ is the unique positive definite solution to Note that the above equation is equivalent to which is similar to the block-wise Lyapunov equation (10a).

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Standard LQR Controller and Standard Observer", "weight": 1.0} -->

If $(K,\mathcal{A}_{K,L})$ is observable, then the dynamic controller is referred as observable. The set of observable controllers under the standard LQR controller gain $K^{\star}$ is denoted as The following result on the unique positive definite solution of the Lyapunov equation directly follows from Lemma 3. ‣ II-D Block-wise Lyapunov Equations ‣ II Problem Statement ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control").

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem 2 (Standard Observer)", "weight": 1.0} -->

A standard observer of system is defined as the one that minimizes the trace of the accumulated state estimation variance $\hat{\Omega}_{L}$, whose gain $L^{\star}$ should be the optimal solution to | | $\displaystyle\min_{L\in\mathbb{L}}$ | $\displaystyle{\rm Tr}(\hat{\Omega}_{L})$ | | \(20\) | | | subject to | $\displaystyle~eq.accumulated_estimation_lyapu.$ | | | The cost function ${\rm Tr}(\hat{\Omega}_{L})$ denotes the sum of estimation variance, which is analogous to LQR by viewing the estimation error dynamics with $L$ as the state-feedback gain. Moreover, the constraint acts as an evaluation equation for the cost, which compresses the infinite-horizon summation into a self-consistent equation. The following proposition provides the formulation to calculate the standard observer $L^{\star}$, which follows the solution to the Riccati equation \[6, Prop. 3\].

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-C Structure of the Stationary Point", "weight": 1.0} -->

This section will further investigate the stationary point at which the gradients vanish. We will first reveal the relationship between the stationary point, the standard LQR controller $K^{\star}$, and the standard observer $L^{\star}$. Then, we will derive the expression the stationary point and discuss the special case of the derived stationary point collapsing into the standard pair. Theorem 1 establishes the observer achieving the optimal cost function under the standard LQR controller.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The condition $Y_{22}=Y_{12}^{{{\mathsf{T}}}}$ implies $\Omega_{22}=\Omega_{12}^{{{\mathsf{T}}}}$ for the derived stationary point, which reduces to the standard pair and can be designed separately. This statistical orthogonality eliminates the influence of initial correlation on the optimal gains and recovers the certainty equivalence property.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiment", "weight": 1.0} -->

In this section, we will compare the costs and gradients of the standard LQR controller-observer pair and the stationary point of OD-LQR obtained through numerical methods.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

Take the discrete version of the Doyle's LQG example which is derived from a physical double-integrator model under a specific coordinate transformation. The selected plant is internally unstable. Experiment results for stable systems are provided in the open-source code.^11^1The code is available at Let $Q=0.25I_{2}$, $R=0.2$. The standard LQR controller $K^{\star}=\begin{bmatrix}4.8768&4.3773\end{bmatrix}$ can be directly obtained by solving the discrete-time algebraic Riccati equation. Rather, the standard observer minimizing the accumulated estimation variance is determined by the initial estimation variance $E_{0}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

The following will explore the results of general and special initial state correlations separately: 1\) General Initial State Correlation $Y_{g}$: The standard observer $L^{\star}=\begin{bmatrix}-0.5667&1.8333\end{bmatrix}^{{{\mathsf{T}}}}$ can be solved through the algebraic Riccati equation (22. ‣ III-B Standard LQR Controller and Standard Observer ‣ III Gradients and Stationary Points ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control")). The cost function of $L^{\star}$ under the standard LQR controller $K^{\star}$ is shown by the red dot in Fig. 1(a) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"), and the white space denotes unstable $\hat{\mathcal{A}}_{K,L}$, where the Lyapunov equations are unsolvable and the cost value is undefined.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

The unique minimum obtained by numerical search indicates that the standard observer $L^{\star}$ achieves optimality given the standard LQR controller $K^{\star}$. The norm of the gradient of cost function with respect to $L$ depicted in Fig. 1(b) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") shows that $L^{\star}$ is a stationary point of $J(K^{\star},L)$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

The landscape of the cost function of controller $K$ under the standard observer $L^{\star}$ is shown in Fig. 1(c) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"), where the cost value of the minimum point is smaller than that of the standard LQR controller $K^{\star}$. Besides, the gradient of cost function for the minimum point vanishes, as shown in Fig. 1(d) ‣ Figure 1 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control").

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

By employing the dlyap instruction, the stationary point $K^{\ddagger}=\begin{bmatrix}4.2598&3.9482\end{bmatrix}$ and $L^{\ddagger}=\begin{bmatrix}-2.5604&4.0196\end{bmatrix}^{{{\mathsf{T}}}}$ derived in Theorem 2, whose cost value is 102.2875, can be obtained numerically. Therefore, the experimental results indicate that the standard controller-observer pair $(K^{\star},L^{\star})$ is generally different from the stationary point of the OD-LQR problem, and the standard LQR controller $K^{\star}$ is generally suboptimal when paired with the standard observer $L^{\star}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

(a) Cost function under K⋆ (b) Norm of grad w.r.t L under K⋆ (c) Cost function under L⋆ (d) Norm of grad w.r.t K under L⋆ Figure 1: Results of general initial state correlation 2\) Special Initial State Correlation $Y_{s}$: Since $Y_{22}$ is the same as the previous case, the standard observer $L^{\star}$ is also the same. The cost values of various observers under $K^{\star}$ are depicted in Fig. 2(a) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"). It can be found that the standard observer $L^{\star}$ achieves the minimum cost value when paired with the standard LQR controller $K^{\star}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

Similarly, the gradient norm of the cost function for diverse observers shown in Fig. 2(b) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control") indicates that $L^{\star}$ is a stationary point of $J(K^{\star},L)$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

The cost function of different controllers operating with the standard observer $L^{\star}$ is illustrated in Fig. 2(c) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"). Different from the previous case, the minimal cost value identified through numerical grid search coincides exactly with the cost value of the standard LQR controller $K^{\star}$. Besides, as shown in Fig. 2(d) ‣ Figure 2 ‣ IV-A Internally Unstable Linear System ‣ IV Experiment ‣ On the Optimization Landscape of Observer-based Dynamic Linear Quadratic Control"), the gradient of cost function for the standard LQR controller $K^{\star}$ vanishes. Therefore, for the special initial correlation $Y_{22}-Y_{12}^{{{\mathsf{T}}}}=0$, the standard controller-observer pair $(K^{\star},L^{\star})$ is a stationary point, which shows control optimality.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Internally Unstable Linear System", "weight": 1.0} -->

(a) Cost function under K⋆ (b) Norm of grad w.r.t L under K⋆ (c) Cost function under L⋆ (d) Norm of grad w.r.t K under L⋆ Figure 2: Results of special initial state correlation

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Unstable System with 2D Controller and 2D Observer", "weight": 1.0} -->

Consider the system with complex controller and observer: For $Y_{g}$ and $Y_{s}$, we separately solved the standard controller-observer pair $(K^{\star},L^{\star})$ and identified the stationary point $(K^{\ddagger},L^{\ddagger})$ of OD-LQR. The results in Table I indicate that, for the general initial state correlation $Y_{g}$, the stationary point $(K^{\ddagger},L^{\ddagger})$ is different from $(K^{\star},L^{\star})$, and achieves a slightly lower cost value compared with the standard LQR; while for the special initial state correlation $Y_{s}$ with $Y_{22}=Y_{12}^{{{\mathsf{T}}}}$, the cost values are consistent. The results confirm that the theory remain valid for the higher-dimensional system.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have explored the optimality of observer-controller pair on the cost function for OD-LQR problems. Based on the derived gradient expressions, we have demonstrated that the standard observer gain minimizing the accumulated estimation variance ensures optimality under the standard LQR controller. However, the standard LQR controller usually fails to achieve the optimal performance under the standard observer, unless the initial state correlations have a special structure. Moreover, we have characterized the stationary point of OD-LQR by Sylvester equations and proved that it reduces to the standard pair under the special initial state correlation, thereby recovering the separation principle. Our examples provide empirical support for the proposed theoretical results. Beyond providing practical guidance for separation-based controller designs, the derived Sylvester equations open a distinct pathway for data-driven methods in dynamic control, shifting the paradigm away from traditional Bellman equations.
