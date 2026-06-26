<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Perturbed Gradient Descent Algorithms Are Small-Disturbance Input-to-State Stable

Topics include Gradient descent, Policy gradients, Lyapunov methods, Stability analysis, Robustness, Online algorithms, ISS, PL.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This article investigates the robustness of gradient descent algorithms under perturbations. The concept of small-disturbance input-to-state stability (ISS) for discrete-time nonlinear dynamical systems is introduced, along with its Lyapunov characterization. The conventional linear Polyak-Lojasiewicz (PL) condition is then extended to a nonlinear version, and it is shown that the gradient descent algorithm is small-disturbance ISS provided the objective function satisfies the generalized nonlinear PL condition. This small-disturbance ISS property guarantees that the gradient descent algorithm converges to a small neighborhood of the optimum under sufficiently small perturbations. As a direct application of the developed framework, we demonstrate that the LQR cost satisfies the generalized nonlinear PL condition, thereby establishing that the policy gradient algorithm for LQR is small-disturbance ISS. Additionally, other popular policy gradient algorithms, including natural policy gradient and Gauss-Newton method, are also proven to be small-disturbance ISS.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient-based optimization algorithms are a cornerstone of machine learning's success, as they efficiently navigate high-dimensional variable spaces to identify suitable extrema for objective function optimization. For instance, gradient descent and adaptive moment estimation (Adam) are among the most widely used first-order gradient-based optimizers in deep learning. Consequently, the convergence analysis of gradient descent algorithms is crucial for understanding and improving their performance. While such analyses typically assume exact gradient information, in practice, gradient computations are often subject to perturbations. These perturbations can arise from round-off errors in arithmetic operations, noisy measurements, inaccurate gradient formulas, or approximations in solving auxiliary problems required for gradient computation (see \[48, Chapter 4\] and \[5, p. 38\] for details). Under such conditions, gradient descent algorithms may exhibit oscillatory behavior near the optimum or, in severe cases, diverge to infinity. Therefore, beyond ensuring convergence in noise-free scenarios, a robust optimization algorithm should degrade gracefully in the presence of perturbations. To this end, both the convergence property and robustness of gradient descent algorithms should be jointly considered in their analysis and design.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A solution to better understanding optimization is to consider gradient-based algorithms as dynamical systems. This perspective enables the application of tools and concepts from control theory, such as Lyapunov stability, to analyze the behavior of optimization algorithms. However, Lyapunov stability primarily examines a system's behavior in the absence of external inputs, making it less suitable for analyzing the convergence and robustness of gradient-based methods subject to external perturbations. Input-to-state stability (ISS) generalizes the Lyapunov stability by linking the system's state to the magnitude of external inputs, offering a more comprehensive criterion for analyzing the effect of external perturbations on gradient-based algorithms. An ISS estimate can reveal not only the asymptotic stability of gradient descent algorithms under noise-free conditions, but also the ultimate region they settle into when subject to perturbations. These capabilities make ISS a valuable concept for both convergence and robustness analysis of gradient-based methods. For example it is established that the saddle point dynamics of a convex--concave function is ISS with respect to additive noise.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In, ISS was applied to analyze the robustness of a bilevel optimization algorithm concerning errors arising from incomplete computation in the inner loop. Similarly, ISS has been employed for robustness analysis of extremum-seeking methods, as demonstrated in and. Moreover, the work in leveraged ISS to address the output regulation problem for tracking a gradient flow in systems subject to disturbances at the plant level.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we aim to establish a connection between the ISS of gradient descent algorithms and the *Polyak-Łojasiewicz (PL)* type condition. The PL condition has been shown to be a sufficient condition for the linear convergence rate of gradient descent, even without assuming the convexity of the objective function. It requires that the square of the gradient norm of the objective function grows proportionally to the deviation of the function value from its optimum. In detail, for a continuously differentiable objective function $\mathcal{J}{(z)}$ defined on a domain $\mathcal{Z}$ with an optimum $z^{\ast}$, the PL condition can be expressed as ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel}^{2} \geq {c{({{\mathcal{J}{(z)}} - {\mathcal{J}{(z^{\ast})}}})}}$, where $c > 0$ is a constant.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the linearity imposed by the conventional PL condition restricts its applicability to a broader range of problems, such as the optimization of LQR costs discussed at the second part of the paper, where globally establishing such linearity is infeasible. This observation naturally leads to the question: can the linear PL condition be generalized to a nonlinear form, thereby extending its applicability to a wider variety of problems? If so, what types of nonlinear PL-type conditions are most suitable for guaranteeing both convergence and robustness in gradient descent algorithms?

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising direction involves replacing the constant $c$ with a function $\alpha$ that belongs to Class $\mathcal{K}$, which simply requires $\alpha$ to be strictly increasing and to vanish at zero. Concretely, the conventional PL condition can be generalized to ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel}^{2} \geq {\alpha{({{\mathcal{J}{(z)}} - {\mathcal{J}{(z^{\ast})}}})}}$, where $\alpha$ is a $\mathcal{K}$-function. Any PL condition characterized by such a $\mathcal{K}$-function is termed a "$\mathcal{K}$-PL" condition. For example, ${\alpha{(r)}} = \frac{r}{1 + r}$ could be chosen, which is a $\mathcal{K}$-function and saturates as $r\rightarrow\infty$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the objective function satisfies the $\mathcal{K}$-PL condition, then the gradient descent algorithm is *small-disturbance ISS*. More precisely, we show for any objective function that is coercive (i.e., its value tends to infinity as the decision variable approaches the boundary of the admissible set $\mathcal{Z}$), has an $L$-Lipschitz continuous gradient, and satisfies the $\mathcal{K}$-PL condition that, with a step size $0 < \eta \leq {1/L}$, the corresponding gradient descent algorithm is small-disturbance ISS. In other words, the trajectories of the gradient descent will eventually settle into a small neighborhood of the optimal solution for a sufficiently small perturbation, with the size of the neighborhood scaling (nonlinearly) according to the magnitude of the perturbation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the $\mathcal{K}$-PL condition is further strengthened to a $\mathcal{K}_{\infty}$-PL condition---requiring ${\alpha{(r)}}\rightarrow\infty$ as $r\rightarrow\infty$---the gradient descent algorithm is ISS. If the $\mathcal{K}$-PL condition is relaxed to a $\mathcal{P}\mathcal{D}$-PL condition, which requires $\alpha$ to be positive definite, the gradient descent algorithm is integral ISS, which is equivalent to global asymptotic stability for discrete-time dynamical systems. Meanwhile, the conventional (linear) PL condition implies that the gradient descent algorithm is exponentially ISS. It should be noted that the robustness of gradient descent algorithms is typically analyzed under the assumption of convexity or by assuming that the perturbations converge to zero. In contrast, the generalized $\mathcal{K}$-PL condition offers an alternative framework for robustness analysis when these convexity or convergent-perturbation assumptions do not hold.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A direct application of the newly developed $\mathcal{K}$-PL condition lies in the robustness analysis of reinforcement learning (RL) algorithms for the linear quadratic regulator (LQR). Policy optimization (PO) stands out as an effective approach for developing RL algorithms \[58, Chapter 13\], as it parametrizes the policy with universal approximators and updates its parameters directly via gradient descent. Examples of PO-based methods include REINFORCE, actor-critic algorithm, trust region policy optimization (TRPO), proximal policy optimization (PPO), and deterministic policy gradient (DPG). The LQR, first introduced by Kalman, is a theoretically elegant control method that has seen widespread use in various engineering applications. In LQR, the objective function is defined as a cumulative quadratic function of the state and control input, while the controller itself is a linear function of the state. Because both the gradient and the optimum of the LQR problem can be explicitly computed when the system matrices are known, the performance of a PO algorithm can be analyzed by comparing its solutions with the optimal solution.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consequently, LQR has long served as a benchmark problem for PO in control theory, and it has recently attracted renewed interest due to advancements in RL. Typically, PO algorithms are implemented in a model-free setting, where the system matrices are unknown and the gradient must be estimated by a data-driven method. For instance, the finite-difference method is used in to approximate the gradient, and the Gauss-Newton gradient descent direction can be computed via adaptive dynamic programming. In a data-driven control framework, however, gradient estimation errors are unavoidable due to noisy measurements and limited data samples. Hence, beyond analyzing the convergence of PO algorithms in noise-free scenarios, robust performance against estimation errors becomes pivotal---forming the foundation for a deeper understanding of RL. In the second part of this paper, we utilize the coercivity of the LQR cost, the Lipschitz continuity of its gradient, and its satisfaction of the $\mathcal{K}$-PL condition. Building on our results from the first part of the paper, we demonstrate that the standard gradient descent algorithm for LQR is small-disturbance ISS under these properties.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we establish that both natural gradient descent and Gauss-Newton gradient descent algorithms for LQR also exhibit small-disturbance ISS.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the conceptual foundations of small-disturbance ISS for discrete-time dynamical systems stem from the continuous-time framework, its Lyapunov characterization cannot be directly demonstrated by simply discretizing the arguments used in the continuous case. Given that gradient descent algorithms inherently operate in discrete time, it is both necessary and appropriate to present these results with comprehensive and rigorous proofs. Moreover, to guarantee the small-disturbance ISS of gradient descent algorithms---viewed as forward Euler discretizations of the gradient flow---the step size for discretization must be appropriately determined based on the Lipschitz continuity of the gradient. In the case of standard gradient descent algorithms for the LQR problem, small-disturbance ISS is ensured by further proving the Lipschitz continuity of the gradient. For natural gradient descent and Gauss-Newton gradient descent algorithms, the step sizes are determined by directly differencing the two Lyapunov functions corresponding to consecutive updates, thereby ensuring small-disturbance ISS.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, the contributions of this paper are three-fold. First, we propose a Lyapunov-like necessary and sufficient condition for small-disturbance ISS in discrete-time dynamical systems. Second, we demonstrate that, under the assumptions of coercivity, the $\mathcal{K}$-PL condition, and $L$-Lipschitz continuity of the objective function and its gradient, the gradient descent algorithm with a step size $0 < \eta \leq \frac{1}{L}$ is small-disturbance ISS with respect to perturbations. Finally, by analyzing the properties of the LQR cost, we show that the standard policy gradient algorithm for LQR is small-disturbance ISS. Additionally, both the natural gradient descent and Gauss-Newton gradient descent algorithms are proven to exhibit small-disturbance ISS.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows: Section 2 introduces the necessary notations and foundational facts. In Section 3, we provide the definition and Lyapunov-like condition for small-disturbance ISS. Section 4 establishes that the perturbed gradient descent algorithm is small-disturbance ISS. Section 5 demonstrates, through an analysis of the LQR cost, that the standard gradient descent, natural gradient descent, and Gauss-Newton gradient descent algorithms for LQR are all small-disturbance ISS. Finally, the paper concludes in Section 6.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Notations and Facts", "weight": 1.0} -->

In this article, we denote by $\mathbb{R}$ (${\mathbb{R}}_{+}$) the set of (nonnegative) real numbers, ${\mathbb{Z}}_{+}$ the set of nonnegative integers, and ${\mathbb{S}}^{n}$ (${\mathbb{S}}_{+}^{n}/{\mathbb{S}}_{+ +}^{n}$) the set of $n$-dimensional real symmetric (positive semidefinite/definite) matrices. For a real symmetric matrix, $\lambda_{\min}( \cdot )$ and $\lambda_{\max}( \cdot )$ denote the minimum and maximum eigenvalues, respectively. ${Tr}( \cdot )$ is the trace of a square matrix. The Euclidean norm of a vector or spectral norm of a matrix is denoted by $\parallel \cdot \parallel$, while ${\parallel \cdot \parallel}_{F}$ denotes the Frobenius norm of a matrix.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Notations and Facts", "weight": 1.0} -->

The concepts of comparison functions, which are essential for stability analysis, are introduced here. A function $\alpha:{{\mathbb{R}}_{+}\rightarrow{\mathbb{R}}_{+}}$ is defined as a $\mathcal{K}$-function if it is continuous, strictly increasing, and equals zero at the origin. For any $d > 0$, a function $\alpha:{{\lbrack 0,d)}\rightarrow{\mathbb{R}}_{+}}$ is a $\mathcal{K}_{\lbrack 0,d)}$-function if it is continuous, strictly increasing, and vanishes at zero.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Notations and Facts", "weight": 1.0} -->

Several established facts are introduced next to support the development of the main results in this paper.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Small-Disturbance Input-to-State Stability", "weight": 1.0} -->

In this section, we investigate the dependence of state trajectories on the magnitude of the disturbances for the discrete-time nonlinear system: where ${\chi{(k)}} \in \mathcal{S}$ denotes the state evolving in an open subset $\mathcal{S} \subset {\mathbb{R}}^{n}$ which is homeomorphic to ${\mathbb{R}}^{n}$, $w \in \ell_{\infty}^{m}$ denotes the disturbance, and $f:{{\mathcal{S} \times {\mathbb{R}}^{m}}\rightarrow\mathcal{S}}$ is a continuous function. Assume that $\chi^{\ast} \in \mathcal{S}$ is the equilibrium of the unforced system, that is $\chi^{\ast} = {f{(\chi^{\ast},0)}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Small-Disturbance Input-to-State Stability", "weight": 1.0} -->

Denote by $\chi{(\cdot,\xi,w)}$ the trajectory of system with the initial state ${\chi{}} = \xi$ and disturbance $w \in \ell_{\infty}^{m}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Small-Disturbance Input-to-State Stability", "weight": 1.0} -->

Since system is defined in an open subset $\mathcal{S}$, instead of ${\mathbb{R}}^{n}$, a size function is introduced to assist in stability analysis and serves as a barrier function preventing escape from $\mathcal{S}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 13", "weight": 1.0} -->

An equivalent property holds if the function $\alpha_{2}$ in is only required to be continuous and positive definite.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 13", "weight": 1.0} -->

The following remark provides a "dissipation" type of characterization for the small-disturbance ISS property.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 14", "weight": 1.0} -->

A size function $\mathcal{V}$ for $(\mathcal{S},\chi^{\ast})$ is a small-disturbance ISS-Lyapunov function for system if and only if there exist a $\mathcal{K}_{\infty}$-function $\alpha_{2}$, some $d > 0$ (possibly $\infty$), and a $\mathcal{K}_{\lbrack 0,d)}$-function $\alpha_{3}$ such that for all $\mu \in {\mathbb{R}}^{m}$ bounded by $d$, i.e., ${\parallel\mu\parallel} < d$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 14", "weight": 1.0} -->

As in classic Lyapunov stability theory, we can show that small-disturbance ISS is equivalent to the existence of a small-disturbance ISS-Lyapunov function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 16", "weight": 1.0} -->

If $f{( \cdot,0)}$ is a diffeomorphism and the domain of asymptotic stability of $\chi^{\ast}$ is $\mathcal{S}$, then $\mathcal{S}$ is diffeomorphic to ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robustness Analysis of Perturbed Gradient Descent", "weight": 1.0} -->

This section applies the concept of small-disturbance ISS to analyze the gradient descent algorithm for solving the constrained nonlinear program: where $\mathcal{Z}$ is an admissible set, defined as an open subset of ${\mathbb{R}}^{n}$ that is homeomorphic to ${\mathbb{R}}^{n}$, and $\mathcal{J}:{\mathcal{Z}\rightarrow{\mathbb{R}}}$ is an objective function with a unique global minimizer $z^{\ast}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 21", "weight": 1.0} -->

The gradient dominance condition proposed in Definition 17, i.e. the $\mathcal{K}$-PL condition, can be viewed as a nonlinear generalization of the well-known PL condition. If the classical PL condition holds, meaning ${\alpha_{5}{(r)}} = {c\sqrt{r}}$ for all $r \geq 0$ and some $c > 0$, the perturbed gradient descent algorithm in is exponentially ISS.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 21", "weight": 1.0} -->

We present several examples of objective functions for which the robustness of the associated gradient descent algorithms is analyzed using the proposed framework.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Application to LQR Problem", "weight": 1.0} -->

In this section, we utilize the tool of small-disturbance ISS to analyze the robustness of the gradient descent algorithms in solving the LQR problem. Some preliminaries on the LQR are introduced in the next subsection.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Small-Disturbance ISS of Standard Gradient Descent", "weight": 1.0} -->

This subsection applies the concept of small-disturbance ISS to analyze the robustness of the standard gradient descent method for the LQR problem, where ${P{(k)}} = P_{K{(k)}}$, ${Y{(k)}} = Y_{K{(k)}}$, and $W \in \ell_{\infty}^{m \times n}$ is the perturbation to the gradient descent algorithm. The perturbation $W$ can represent gradient estimation errors in the context of data-driven control. When the system matrices are unknown, gradient estimation can be achieved through the finite-difference method or approximate dynamic programming, both of which introduce errors due to measurement noise, system process noise, and even potential malicious attacks on the algorithm. The following lemma is introduced to ensure that $\mathcal{J}_{2}{(K)}$ satisfy the $\mathcal{K}$-PL condition in Definition 17, which is critical to the robustness analysis.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 29", "weight": 1.0} -->

The classical PL condition requires ${\parallel{{\nabla\mathcal{J}_{2}}{(K)}}\parallel}^{2} \geq {c{({{\mathcal{J}_{2}{(K)}} - {\mathcal{J}_{2}{(K^{\ast})}}})}}$, which holds only over a compact sublevel set ${\mathcal{G}{(h)}} = \left. \{{K \in \mathcal{G}} \middle| {{\mathcal{J}_{2}{(K)}} \leq h}\} \right.$ due to the limitations of its linear form. In this article, by generalizing the classical PL condition to nonlinear form, we can obtain a global estimate of the gradient dominance condition.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 29", "weight": 1.0} -->

With the established Lipschitz continuity and the $\mathcal{K}$-PL condition for the objective function $\mathcal{J}_{2}{(K)}$, we are now prepared to present the main result on the robustness of the gradient descent algorithm.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Small-Disturbance ISS of Natural Gradient Descent", "weight": 1.0} -->

This subsection analyzes the robustness of the natural gradient descent algorithm, developed by leveraging the Riemannian geometry of the objective function $\mathcal{J}_{2}{(K)}$. By subtracting from and completing the squares, the Lyapunov equation | | & {{+ {{({K - K^{\ast}})}^{\top}R{({K - K^{\ast}})}}} = 0} | | | can be obtained. Applying Corollary 8 to, the LQR cost can be expressed as a quadratic function over the Riemannian metric $(\mathcal{G},{\langle \cdot, \cdot \rangle}_{Y_{K}})$, that is, The standard gradient descent in follows the steepest descent direction under the standard Euclidean metric $(\mathcal{G},{\langle \cdot, \cdot \rangle}_{I_{n}})$. However, this ad hoc choice of metric may not be appropriate.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Small-Disturbance ISS of Natural Gradient Descent", "weight": 1.0} -->

As seen in the expression for ${\nabla\mathcal{J}_{2}}{(K)}$, the magnitude of the gradient depends on $Y_{K}$, which can diverge as $K\rightarrow{\partial\mathcal{G}}$ but vanishes as ${\parallel K\parallel}_{F}\rightarrow\infty$ (see Example 31). The non-isotropic property induced by the improper choice of the Euclidean metric may degrade the convergence rate. As pointed out by Amari, the choice of a metric should be based on the manifold that the optimization parameters lie. Over the Riemannian manifold $(\mathcal{G},{\langle \cdot, \cdot \rangle}_{Y_{K}})$ and according to, the steepest-descent direction can be derived as In practice, the accurate gradient is not accessible and should be estimated through sampling and experiments.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Small-Disturbance ISS of Natural Gradient Descent", "weight": 1.0} -->

The perturbed natural gradient descent algorithm is where ${P{(k)}} = P_{K{(k)}}$, $W \in \ell_{\infty}^{m \times n}$ denotes the perturbation and ${\eta{(k)}} > 0$ is the step size to be determined later.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Small-Disturbance ISS of Natural Gradient Descent", "weight": 1.0} -->

The following example illustrates the advantage of natural gradient descent over standard gradient descent in terms of convergence rate.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 31", "weight": 1.0} -->

As $K\rightarrow\infty$, the standard gradient ${\nabla\mathcal{J}_{2}}{(K)}$ saturates, while the natural gradient ${grad}\left({\mathcal{J}_{2}{(K)}} \right)$ remains unbounded. This distinction allows the natural gradient to achieve faster convergence, particularly when $K$ is far from the optimum. Under standard gradient descent with the update rule it can be shown that where ${m_{1}{(K,\eta)}} = \frac{{({{2K} - \eta})}{({K + 1})}^{2}}{{{4K^{4}} - {2\eta K^{3}}} + {2\eta K}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 31", "weight": 1.0} -->

In comparison, under natural gradient descent with the update rule it can be verified that where ${m_{2}{(K,\eta)}} = \frac{{({1 - \eta})}{({K + 1})}^{2}}{{{({1 - \eta})}K^{2}} + \eta}$. Since ${\lim_{K\rightarrow\infty}{m_{1}{(K,\eta)}}} = 0$ while ${\lim_{K\rightarrow\infty}{m_{2}{(K,\eta)}}} = 1$, the convergence rate of natural gradient descent is faster than that of standard gradient descent when $K$ is far from the optimum.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 31", "weight": 1.0} -->

The following two lemmas are introduced to assist in the development of the small-disturbance ISS property of natural gradient descent.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Small-Disturbance ISS of the Gauss-Newton Method", "weight": 1.0} -->

Therefore, in the vicinity of $K^{\ast}$, the last two terms in become negligible, allowing us to approximate the Hessian as This approximation of the Hessian is derived based on arguments similar to those used in the Gauss-Newton method \[43, Section 10.3\]. Hence, the update direction of Gauss-Newton method is $- {({K - {R^{- 1}B^{\top}P_{K}}})}$, which is obtained by solving $dK$ from Under the perturbation, the Gauss-Newton algorithm is

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 35", "weight": 1.0} -->

The Gauss-Newton method in is derived based on the policy optimization of the LQR cost $\mathcal{J}_{2}{(K)}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 35", "weight": 1.0} -->

The update in can also be interpreted as an application of the classical Newton's method to solve the nonlinear algebraic Riccati equation (ARE): Indeed, the action of the gradient of the Riccati operator $\mathcal{R}{(X)}$ on ${dX} \in {\mathbb{S}}^{n}$ is given by | | {{\nabla\mathcal{R}}{(X)}{\lbrack{dX}\rbrack}} & {= {{({A - {BR^{- 1}B^{\top}X}})}^{\top}dX}} \\ | | | According to Newton's method, at the $({k + 1})$^th^ iteration, $X{({k + 1})}$ is updated as where $N{(k)}$, the Newton's updated direction, is the solution of

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 35", "weight": 1.0} -->

With these definitions, can be reformulated as | | & {{{({A - {B\overline{K}{(k)}}})}^{\top}\overline{P}{(k)}} + {\overline{P}{(k)}{({A - {B\overline{K}{(k)}}})}}} \\ | | | | | & {{{{+ Q} + {\overline{K}{(k)}^{\top}R\overline{K}{(k)}}} = 0}.} | | | In addition, considering and the relation ${N{(k)}} = {{\overline{P}{(k)}} - {X{(k)}}}$, the recursive formula of $\overline{K}{(k)}$ becomes Hence, is equivalent to without perturbation, which implies that the Gauss-Newton method in coincides with Newton's method in for solving the ARE.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 35", "weight": 1.0} -->

This interpretation establishes a connection between the Gauss-Newton method for policy optimization and the classical Newton's method for solving the ARE. The following theorem shows the small-disturbance ISS property of the Gauss-Newton method.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This article introduces the concept of small-disturbance ISS as a unified framework for analyzing the robustness of gradient descent algorithms. Small-disturbance ISS provided a systematic approach to quantify the transient behavior, convergence speed, and robustness of gradient descent algorithms under perturbations. By generalizing the classical linear PL condition to a nonlinear version, referred to as the $\mathcal{K}$-PL condition, we show that gradient descent algorithms are small-disturbance ISS, provided the objective function satisfies the $\mathcal{K}$-PL condition. As a direct application to LQR, we demonstrate that three popular policy gradient algorithms in RL--standard policy gradient, natural policy gradient, and Gauss-Newton method--are all small-disturbance ISS.
