## Introduction

Gradient-based optimization algorithms are a cornerstone of machine learning's success, as they efficiently navigate high-dimensional variable spaces to identify suitable extrema for objective function optimization. For instance, gradient descent and adaptive moment estimation (Adam) \[(https://arxiv.org/html/2507.02131v1#bib.bib30)\] are among the most widely used first-order gradient-based optimizers in deep learning. Consequently, the convergence analysis of gradient descent algorithms is crucial for understanding and improving their performance. While such analyses typically assume exact gradient information, in practice, gradient computations are often subject to perturbations. These perturbations can arise from round-off errors in arithmetic operations, noisy measurements, inaccurate gradient formulas, or approximations in solving auxiliary problems required for gradient computation (see \[(https://arxiv.org/html/2507.02131v1#bib.bib48), Chapter 4\] and \[(https://arxiv.org/html/2507.02131v1#bib.bib5), p. 38\] for details). Under such conditions, gradient descent algorithms may exhibit oscillatory behavior near the optimum or, in severe cases, diverge to infinity \[(https://arxiv.org/html/2507.02131v1#bib.bib48), (https://arxiv.org/html/2507.02131v1#bib.bib5)\]. Therefore, beyond ensuring convergence in noise-free scenarios, a robust optimization algorithm should degrade gracefully in the presence of perturbations. To this end, both the convergence property and robustness of gradient descent algorithms should be jointly considered in their analysis and design.

A solution to better understanding optimization is to consider gradient-based algorithms as dynamical systems. This perspective enables the application of tools and concepts from control theory, such as Lyapunov stability, to analyze the behavior of optimization algorithms \[(https://arxiv.org/html/2507.02131v1#bib.bib61), (https://arxiv.org/html/2507.02131v1#bib.bib20), (https://arxiv.org/html/2507.02131v1#bib.bib41), (https://arxiv.org/html/2507.02131v1#bib.bib27)\]. However, Lyapunov stability primarily examines a system's behavior in the absence of external inputs, making it less suitable for analyzing the convergence and robustness of gradient-based methods subject to external perturbations. Input-to-state stability (ISS) generalizes the Lyapunov stability by linking the system's state to the magnitude of external inputs, offering a more comprehensive criterion for analyzing the effect of external perturbations on gradient-based algorithms \[(https://arxiv.org/html/2507.02131v1#bib.bib53), (https://arxiv.org/html/2507.02131v1#bib.bib55), (https://arxiv.org/html/2507.02131v1#bib.bib56), (https://arxiv.org/html/2507.02131v1#bib.bib12)\]. An ISS estimate can reveal not only the asymptotic stability of gradient descent algorithms under noise-free conditions, but also the ultimate region they settle into when subject to perturbations. These capabilities make ISS a valuable concept for both convergence and robustness analysis of gradient-based methods. For example, in \[(https://arxiv.org/html/2507.02131v1#bib.bib11)\], it is established that the saddle point dynamics of a convex--concave function is ISS with respect to additive noise. In \[(https://arxiv.org/html/2507.02131v1#bib.bib13)\], ISS was applied to analyze the robustness of a bilevel optimization algorithm concerning errors arising from incomplete computation in the inner loop. Similarly, ISS has been employed for robustness analysis of extremum-seeking methods, as demonstrated in \[(https://arxiv.org/html/2507.02131v1#bib.bib49)\] and \[(https://arxiv.org/html/2507.02131v1#bib.bib57)\]. Moreover, the work in \[(https://arxiv.org/html/2507.02131v1#bib.bib8)\] leveraged ISS to address the output regulation problem for tracking a gradient flow in systems subject to disturbances at the plant level.

In this paper, we aim to establish a connection between the ISS of gradient descent algorithms and the *Polyak-Łojasiewicz (PL)* type condition \[(https://arxiv.org/html/2507.02131v1#bib.bib47), (https://arxiv.org/html/2507.02131v1#bib.bib37), (https://arxiv.org/html/2507.02131v1#bib.bib29)\]. The PL condition has been shown to be a sufficient condition for the linear convergence rate of gradient descent, even without assuming the convexity of the objective function. It requires that the square of the gradient norm of the objective function grows proportionally to the deviation of the function value from its optimum. In detail, for a continuously differentiable objective function $\mathcal{J}{(z)}$ defined on a domain $\mathcal{Z}$ with an optimum $z^{\ast}$, the PL condition can be expressed as ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel}^{2} \geq {c{({{\mathcal{J}{(z)}} - {\mathcal{J}{(z^{\ast})}}})}}$, where $c > 0$ is a constant. However, the linearity imposed by the conventional PL condition restricts its applicability to a broader range of problems, such as the optimization of LQR costs discussed at the second part of the paper, where globally establishing such linearity is infeasible. This observation naturally leads to the question: can the linear PL condition be generalized to a nonlinear form, thereby extending its applicability to a wider variety of problems? If so, what types of nonlinear PL-type conditions are most suitable for guaranteeing both convergence and robustness in gradient descent algorithms?

A promising direction involves replacing the constant $c$ with a function $\alpha$ that belongs to Class $\mathcal{K}$, which simply requires $\alpha$ to be strictly increasing and to vanish at zero. Concretely, the conventional PL condition can be generalized to ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel}^{2} \geq {\alpha{({{\mathcal{J}{(z)}} - {\mathcal{J}{(z^{\ast})}}})}}$, where $\alpha$ is a $\mathcal{K}$-function. Any PL condition characterized by such a $\mathcal{K}$-function is termed a "$\mathcal{K}$-PL" condition. For example, ${\alpha{(r)}} = \frac{r}{1 + r}$ could be chosen, which is a $\mathcal{K}$-function and saturates as $r\rightarrow\infty$. If the objective function satisfies the $\mathcal{K}$-PL condition, then the gradient descent algorithm is *small-disturbance ISS* \[(https://arxiv.org/html/2507.02131v1#bib.bib44), (https://arxiv.org/html/2507.02131v1#bib.bib12)\]. More precisely, we show for any objective function that is coercive (i.e., its value tends to infinity as the decision variable approaches the boundary of the admissible set $\mathcal{Z}$), has an $L$-Lipschitz continuous gradient, and satisfies the $\mathcal{K}$-PL condition that, with a step size $0 < \eta \leq {1/L}$, the corresponding gradient descent algorithm is small-disturbance ISS. In other words, the trajectories of the gradient descent will eventually settle into a small neighborhood of the optimal solution for a sufficiently small perturbation, with the size of the neighborhood scaling (nonlinearly) according to the magnitude of the perturbation. If the $\mathcal{K}$-PL condition is further strengthened to a $\mathcal{K}_{\infty}$-PL condition---requiring ${\alpha{(r)}}\rightarrow\infty$ as $r\rightarrow\infty$---the gradient descent algorithm is ISS \[(https://arxiv.org/html/2507.02131v1#bib.bib56)\]. If the $\mathcal{K}$-PL condition is relaxed to a $\mathcal{P}\mathcal{D}$-PL condition, which requires $\alpha$ to be positive definite, the gradient descent algorithm is integral ISS, which is equivalent to global asymptotic stability for discrete-time dynamical systems \[(https://arxiv.org/html/2507.02131v1#bib.bib3)\]. Meanwhile, the conventional (linear) PL condition implies that the gradient descent algorithm is exponentially ISS. It should be noted that the robustness of gradient descent algorithms is typically analyzed under the assumption of convexity \[(https://arxiv.org/html/2507.02131v1#bib.bib48), (https://arxiv.org/html/2507.02131v1#bib.bib52), (https://arxiv.org/html/2507.02131v1#bib.bib15), (https://arxiv.org/html/2507.02131v1#bib.bib33), (https://arxiv.org/html/2507.02131v1#bib.bib14), (https://arxiv.org/html/2507.02131v1#bib.bib4), (https://arxiv.org/html/2507.02131v1#bib.bib61), (https://arxiv.org/html/2507.02131v1#bib.bib39)\] or by assuming that the perturbations converge to zero \[(https://arxiv.org/html/2507.02131v1#bib.bib7)\]. In contrast, the generalized $\mathcal{K}$-PL condition offers an alternative framework for robustness analysis when these convexity or convergent-perturbation assumptions do not hold.

A direct application of the newly developed $\mathcal{K}$-PL condition lies in the robustness analysis of reinforcement learning (RL) algorithms for the linear quadratic regulator (LQR). Policy optimization (PO) stands out as an effective approach for developing RL algorithms \[(https://arxiv.org/html/2507.02131v1#bib.bib58), Chapter 13\], as it parametrizes the policy with universal approximators and updates its parameters directly via gradient descent. Examples of PO-based methods include REINFORCE \[(https://arxiv.org/html/2507.02131v1#bib.bib60)\], actor-critic algorithm \[(https://arxiv.org/html/2507.02131v1#bib.bib32)\], trust region policy optimization (TRPO) \[(https://arxiv.org/html/2507.02131v1#bib.bib50)\], proximal policy optimization (PPO) \[(https://arxiv.org/html/2507.02131v1#bib.bib51)\], and deterministic policy gradient (DPG) \[(https://arxiv.org/html/2507.02131v1#bib.bib36)\]. The LQR, first introduced by Kalman \[(https://arxiv.org/html/2507.02131v1#bib.bib28)\], is a theoretically elegant control method that has seen widespread use in various engineering applications. In LQR, the objective function is defined as a cumulative quadratic function of the state and control input, while the controller itself is a linear function of the state. Because both the gradient and the optimum of the LQR problem can be explicitly computed when the system matrices are known, the performance of a PO algorithm can be analyzed by comparing its solutions with the optimal solution. Consequently, LQR has long served as a benchmark problem for PO in control theory \[(https://arxiv.org/html/2507.02131v1#bib.bib34), (https://arxiv.org/html/2507.02131v1#bib.bib38)\], and it has recently attracted renewed interest due to advancements in RL \[(https://arxiv.org/html/2507.02131v1#bib.bib16), (https://arxiv.org/html/2507.02131v1#bib.bib40), (https://arxiv.org/html/2507.02131v1#bib.bib21)\]. Typically, PO algorithms are implemented in a model-free setting, where the system matrices are unknown and the gradient must be estimated by a data-driven method. For instance, the finite-difference method is used in \[(https://arxiv.org/html/2507.02131v1#bib.bib16), (https://arxiv.org/html/2507.02131v1#bib.bib40), (https://arxiv.org/html/2507.02131v1#bib.bib35)\] to approximate the gradient, and the Gauss-Newton gradient descent direction can be computed via adaptive dynamic programming \[(https://arxiv.org/html/2507.02131v1#bib.bib6), (https://arxiv.org/html/2507.02131v1#bib.bib22)\]. In a data-driven control framework, however, gradient estimation errors are unavoidable due to noisy measurements and limited data samples. Hence, beyond analyzing the convergence of PO algorithms in noise-free scenarios, robust performance against estimation errors becomes pivotal---forming the foundation for a deeper understanding of RL. In the second part of this paper, we utilize the coercivity of the LQR cost, the Lipschitz continuity of its gradient, and its satisfaction of the $\mathcal{K}$-PL condition \[(https://arxiv.org/html/2507.02131v1#bib.bib12)\]. Building on our results from the first part of the paper, we demonstrate that the standard gradient descent algorithm for LQR is small-disturbance ISS under these properties. Furthermore, we establish that both natural gradient descent and Gauss-Newton gradient descent algorithms for LQR also exhibit small-disturbance ISS.

While the conceptual foundations of small-disturbance ISS for discrete-time dynamical systems stem from the continuous-time framework \[(https://arxiv.org/html/2507.02131v1#bib.bib12)\], its Lyapunov characterization cannot be directly demonstrated by simply discretizing the arguments used in the continuous case. Given that gradient descent algorithms inherently operate in discrete time, it is both necessary and appropriate to present these results with comprehensive and rigorous proofs. Moreover, to guarantee the small-disturbance ISS of gradient descent algorithms---viewed as forward Euler discretizations of the gradient flow---the step size for discretization must be appropriately determined based on the Lipschitz continuity of the gradient. In the case of standard gradient descent algorithms for the LQR problem, small-disturbance ISS is ensured by further proving the Lipschitz continuity of the gradient. For natural gradient descent and Gauss-Newton gradient descent algorithms, the step sizes are determined by directly differencing the two Lyapunov functions corresponding to consecutive updates, thereby ensuring small-disturbance ISS.

In summary, the contributions of this paper are three-fold. First, we propose a Lyapunov-like necessary and sufficient condition for small-disturbance ISS in discrete-time dynamical systems. Second, we demonstrate that, under the assumptions of coercivity, the $\mathcal{K}$-PL condition, and $L$-Lipschitz continuity of the objective function and its gradient, the gradient descent algorithm with a step size $0 < \eta \leq \frac{1}{L}$ is small-disturbance ISS with respect to perturbations. Finally, by analyzing the properties of the LQR cost, we show that the standard policy gradient algorithm for LQR is small-disturbance ISS. Additionally, both the natural gradient descent and Gauss-Newton gradient descent algorithms are proven to exhibit small-disturbance ISS.

The remainder of the paper is organized as follows: Section 2 introduces the necessary notations and foundational facts. In Section 3, we provide the definition and Lyapunov-like condition for small-disturbance ISS. Section 4 establishes that the perturbed gradient descent algorithm is small-disturbance ISS. Section 5 demonstrates, through an analysis of the LQR cost, that the standard gradient descent, natural gradient descent, and Gauss-Newton gradient descent algorithms for LQR are all small-disturbance ISS. Finally, the paper concludes in Section 6.

## Notations and Facts

In this article, we denote by $\mathbb{R}$ (${\mathbb{R}}_{+}$) the set of (nonnegative) real numbers, ${\mathbb{Z}}_{+}$ the set of nonnegative integers, and ${\mathbb{S}}^{n}$ (${\mathbb{S}}_{+}^{n}/{\mathbb{S}}_{+ +}^{n}$) the set of $n$-dimensional real symmetric (positive semidefinite/definite) matrices. For a real symmetric matrix, $\lambda_{\min}( \cdot )$ and $\lambda_{\max}( \cdot )$ denote the minimum and maximum eigenvalues, respectively. ${Tr}( \cdot )$ is the trace of a square matrix. The Euclidean norm of a vector or spectral norm of a matrix is denoted by $\parallel \cdot \parallel$, while ${\parallel \cdot \parallel}_{F}$ denotes the Frobenius norm of a matrix.

Let $\ell_{\infty}^{n}$ ($\ell_{\infty}^{m \times n}$) denote the set of bounded functions $w:{{\mathbb{Z}}_{+}\rightarrow{\mathbb{R}}^{n}}$ ($K:{{\mathbb{Z}}_{+}\rightarrow{\mathbb{R}}^{m \times n}}$), with the $\ell_{\infty}$-norm given by ${\parallel w\parallel}_{\infty} = {\sup_{k \in {\mathbb{Z}}_{+}}{\parallel{w{(k)}}\parallel}}$ (${\parallel K\parallel}_{\infty} = {\sup_{k \in {\mathbb{Z}}_{+}}{\parallel{K{(k)}}\parallel}_{F}}$). The truncation of $w \in \ell_{\infty}^{n}$ at step $k$ is denoted by $w_{\lbrack k\rbrack}$, defined as

We use $I_{n}$ to denote the $n$-dimensional identity matrix and $Id$ for the identity function. For any ${K_{1},K_{2}} \in {\mathbb{R}}^{m \times n}$ and $Y \in {\mathbb{S}}_{+ +}^{n}$, we define the inner product as ${\langle K_{1},K_{2}\rangle}_{Y} = {{Tr}\left( {K_{1}YK_{2}^{\top}} \right)}$. For simplicity, we write ${\langle K_{1},K_{2}\rangle} = {\langle K_{1},K_{2}\rangle}_{I_{n}}$. Note that for any $K \in {\mathbb{R}}^{m \times n}$, ${\parallel K\parallel}_{F}^{2} = {\langle K,K\rangle}$. Finally, for any $A \in {\mathbb{S}}^{n}$ and $B \in {\mathbb{S}}^{n}$, $A \succ B$ indicates that ${A - B} \in {\mathbb{S}}_{+ +}^{n}$, and $A \succeq B$ indicates that ${A - B} \in {\mathbb{S}}_{+}^{n}$.

The concepts of comparison functions \[(https://arxiv.org/html/2507.02131v1#bib.bib19)\], which are essential for stability analysis, are introduced here. A function $\alpha:{{\mathbb{R}}_{+}\rightarrow{\mathbb{R}}_{+}}$ is defined as a $\mathcal{K}$-function if it is continuous, strictly increasing, and equals zero at the origin. For any $d > 0$, a function $\alpha:{{\lbrack 0,d)}\rightarrow{\mathbb{R}}_{+}}$ is a $\mathcal{K}_{\lbrack 0,d)}$-function if it is continuous, strictly increasing, and vanishes at zero. A function $\alpha:{{\mathbb{R}}_{+}\rightarrow{\mathbb{R}}_{+}}$ is a $\mathcal{K}_{\infty}$-function if it meets the criteria of a $\mathcal{K}$-function and additionally satisfies ${\alpha{(r)}}\rightarrow\infty$ as $r\rightarrow\infty$. A function $\beta:{{{\mathbb{R}}_{+} \times {\mathbb{R}}_{+}}\rightarrow{\mathbb{R}}_{+}}$ is called a $\mathcal{K}\mathcal{L}$-function if, for each fixed $t \geq 0$, $\beta{( \cdot,t)}$ is a $\mathcal{K}$-function, and for each fixed $r \geq 0$, $\beta{(r, \cdot )}$ is decreasing and approaches zero as $t\rightarrow\infty$.

Several established facts are introduced next to support the development of the main results in this paper.

### Lemma 1 (Weak triangle inequality \[[24](https://arxiv.org/html/2507.02131v1#bib.bib24)\])

For any $\mathcal{K}$-function $\alpha$, any $\mathcal{K}_{\infty}$-function $\rho$, and any ${a,b} \in {\mathbb{R}}_{+}$, it holds that

### Lemma 2 (Cyclic property of trace \[[46](https://arxiv.org/html/2507.02131v1#bib.bib46)\] )

For any ${X,Y,Z} \in {\mathbb{R}}^{n \times n}$, ${{Tr}\left( {XYZ} \right)} = {{Tr}\left( {ZXY} \right)} = {{Tr}\left( {YZX} \right)}$.

### Lemma 3 (Trace inequality \[[59](https://arxiv.org/html/2507.02131v1#bib.bib59)\])

For any $S \in {\mathbb{S}}^{n}$ and $P \in {\mathbb{S}}_{+ +}^{n}$, it holds that

### Lemma 4 (Cauchy-Schwarz inequality)

For any ${K_{1},K_{2}} \in {\mathbb{R}}^{m \times n}$, $R \in {\mathbb{S}}_{+ +}^{m}$, and $Y \in {\mathbb{S}}_{+ +}^{n}$, it holds that

The expression ${\langle K_{1},{RK_{2}}\rangle}_{Y}$ defines a valid inner product with respect to $K_{1}$ and $K_{2}$, from which the Cauchy--Schwarz inequality follows directly.

### Lemma 5 (Lemma 2.4 in \[[12](https://arxiv.org/html/2507.02131v1#bib.bib12)\])

The map ${{h{(v)}} = {\frac{1}{1 + {\parallel v\parallel}}v}}:{{\mathbb{R}}^{m}\rightarrow\left. \{{w \in {\mathbb{R}}^{m}} \middle| {{\parallel w\parallel} < 1}\} \right.}$, with ${h^{- 1}{(w)}} = {\frac{1}{1 - {\parallel w\parallel}}w}$, is a homeomorphism.

### Lemma 6 (Proposition 2.6 in \[[56](https://arxiv.org/html/2507.02131v1#bib.bib56)\])

Suppose ${\omega_{1},\omega_{2}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ are continuous, positive definite with respect to $\chi^{\ast}$, and radially unbounded. Then, there exist $\mathcal{K}_{\infty}$-functions $\rho_{1}$ and $\rho_{2}$ such that

### Lemma 7 (Theorem 18 in \[[54](https://arxiv.org/html/2507.02131v1#bib.bib54)\])

If $A \in {\mathbb{R}}^{n \times n}$ is Hurwitz, then the Lyapunov equation

has a unique solution for any $Q \in {\mathbb{R}}^{n \times n}$, and the solution can be expressed as

The following two corollaries are direct consequences of Lemma (https://arxiv.org/html/2507.02131v1#Thmthm7 "Lemma 7 (Theorem 18 in ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") and the cyclic property of trace in Lemma (https://arxiv.org/html/2507.02131v1#Thmthm2 "Lemma 2 (Cyclic property of trace ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable").

### Corollary 8

Suppose that $A \in {\mathbb{R}}^{n \times n}$ is Hurwitz, ${M,N} \in {\mathbb{S}}^{n}$, and ${P,Y} \in {\mathbb{S}}^{n}$ are the solutions of

Then, ${{Tr}\left( {MY} \right)} = {{Tr}\left( {NP} \right)}$.

### Corollary 9

Suppose that $A \in {\mathbb{R}}^{n \times n}$ is Hurwitz and $Q_{1} \succeq Q_{2}$. Then, $P_{1} \succeq P_{2}$ where

## Small-Disturbance Input-to-State Stability

In this section, we investigate the dependence of state trajectories on the magnitude of the disturbances for the discrete-time nonlinear system:

where ${\chi{(k)}} \in \mathcal{S}$ denotes the state evolving in an open subset $\mathcal{S} \subset {\mathbb{R}}^{n}$ which is homeomorphic to ${\mathbb{R}}^{n}$, $w \in \ell_{\infty}^{m}$ denotes the disturbance, and $f:{{\mathcal{S} \times {\mathbb{R}}^{m}}\rightarrow\mathcal{S}}$ is a continuous function. Assume that $\chi^{\ast} \in \mathcal{S}$ is the equilibrium of the unforced system, that is $\chi^{\ast} = {f{(\chi^{\ast},0)}}$. Denote by $\chi{( \cdot,\xi,w)}$ the trajectory of system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) with the initial state ${\chi{}} = \xi$ and disturbance $w \in \ell_{\infty}^{m}$.

Since system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is defined in an open subset $\mathcal{S}$, instead of ${\mathbb{R}}^{n}$, a size function is introduced to assist in stability analysis and serves as a barrier function preventing escape from $\mathcal{S}$.

### Definition 10 (\[[56](https://arxiv.org/html/2507.02131v1#bib.bib56)\])

A function $\mathcal{V}:{\mathcal{S}\rightarrow{\mathbb{R}}_{+}}$ is a size function for $(\mathcal{S},\chi^{\ast})$ if $\mathcal{V}$ is

positive definite with respect to $\chi^{\ast}$, i.e. ${\mathcal{V}{(\chi^{\ast})}} = 0$ and ${\mathcal{V}{(\chi)}} > 0$ for all $\chi \neq \chi^{\ast}$, $\chi \in \mathcal{S}$;

coercive, i.e. for any sequence ${\{\chi_{k}\}}_{k = 0}^{\infty}$, $\chi_{k}\rightarrow{\partial\mathcal{S}}$ or ${\parallel\chi_{k}\parallel}\rightarrow\infty$, it holds that ${\mathcal{V}{(\chi_{k})}}\rightarrow\infty$, as $k\rightarrow\infty$.

For $\mathcal{S} = {\mathbb{R}}^{n}$, ${\mathcal{V}{(\xi)}} = {\parallel{\xi - \chi^{\ast}}\parallel}$ is a natural choice of a size function. By resorting to size functions, we first introduce the concepts of small-disturbance ISS and small-disturbance ISS-Lyapunov function.

### Definition 11 (\[[45](https://arxiv.org/html/2507.02131v1#bib.bib45), [12](https://arxiv.org/html/2507.02131v1#bib.bib12)\])

The nonlinear system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance input-to-state stable (ISS) if there exist a size function $\mathcal{V}$, a constant $d > 0$ (possibly $\infty$), a $\mathcal{K}\mathcal{L}$-function $\beta$, and a $\mathcal{K}_{\lbrack 0,d)}$-function $\gamma$, such that for all inputs $w$ bounded by $d$ (i.e. ${\parallel w\parallel}_{\infty} < d$), and all initial states ${\chi{}} \in \mathcal{S}$, $\chi{(k)}$ remains in $\mathcal{S}$ and satisfies

By causality, the same definition would result for every $k \in {{\mathbb{Z}}_{+} \smallsetminus {\{ 0\}}}$ if ${\parallel w\parallel}_{\infty}$ was replaced by ${\parallel w_{\lbrack{k - 1}\rbrack}\parallel}_{\infty}$ in ((https://arxiv.org/html/2507.02131v1#S3.E4 "In Definition 11 (). ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), where $w_{\lbrack{k - 1}\rbrack}$ is the truncation of $w$ at $k - 1$. Additionally, the classical ISS definition can be recovered by setting $d = \infty$ and ${\mathcal{V}{({\chi{(k)}})}} = {\parallel{\chi{(k)}}\parallel}$. Thus, small-disturbance ISS serves as an extension of the classical ISS \[(https://arxiv.org/html/2507.02131v1#bib.bib53), (https://arxiv.org/html/2507.02131v1#bib.bib25)\].

### Definition 12

A function $\mathcal{V}:{\mathcal{S}\rightarrow{\mathbb{R}}}$ is a small-disturbance ISS-Lyapunov function for system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) if

$\mathcal{V}$ is a size function for $(\mathcal{S},\chi^{\ast})$;

there exist a $\mathcal{K}$-function $\alpha_{1}$ and a $\mathcal{K}_{\infty}$-function $\alpha_{2}$ such that

for any $\xi \in \mathcal{S}$ and $\mu \in {\mathbb{R}}^{m}$ so that ${\parallel\mu\parallel} \leq {\alpha_{1}{({\mathcal{V}{(\xi)}})}}$.

### Remark 13

An equivalent property holds if the function $\alpha_{2}$ in ((https://arxiv.org/html/2507.02131v1#S3.E5 "In item 2 ‣ Definition 12. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is only required to be continuous and positive definite \[(https://arxiv.org/html/2507.02131v1#bib.bib25), (https://arxiv.org/html/2507.02131v1#bib.bib26)\].

The following remark provides a "dissipation" type of characterization for the small-disturbance ISS property.

### Remark 14

A size function $\mathcal{V}$ for $(\mathcal{S},\chi^{\ast})$ is a small-disturbance ISS-Lyapunov function for system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) if and only if there exist a $\mathcal{K}_{\infty}$-function $\alpha_{2}$, some $d > 0$ (possibly $\infty$), and a $\mathcal{K}_{\lbrack 0,d)}$-function $\alpha_{3}$ such that

for all $\mu \in {\mathbb{R}}^{m}$ bounded by $d$, i.e., ${\parallel\mu\parallel} < d$.

Without loss of generality, assume that ${\alpha_{3}{(r)}}\rightarrow\infty$ as $r\rightarrow d$ (add $\frac{r}{d - r}$ to it if it is not). Clearly, ((https://arxiv.org/html/2507.02131v1#S3.E6 "In Remark 14. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) implies ((https://arxiv.org/html/2507.02131v1#S3.E5 "In item 2 ‣ Definition 12. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). Suppose now that Property 2 in Definition (https://arxiv.org/html/2507.02131v1# "Definition 12. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") holds with some $\alpha_{1} \in \mathcal{K}$ and $\alpha_{2} \in \mathcal{K}_{\infty}$. Let $d = {\sup_{r \in {\mathbb{R}}_{+}}{\alpha_{1}{(r)}}}$ (possibly $\infty$). For any $r \in {\lbrack 0,d)}$, define ${\alpha_{3}{(r)}} = {\max{\{{{{{\mathcal{V}{({f{(\xi,\mu)}})}} - {\mathcal{V}{(\xi)}}} + \left. {\alpha_{2}{({\mathcal{V}{(\xi)}})}} \middle| {\parallel\mu\parallel} \right.} \leq r},{{\alpha_{1}{({\mathcal{V}{(\xi)}})}} \leq r}\}}}$. Then, $\alpha_{3}$ is continuous, non-decreasing, and zero at zero. In addition, we can assume that $\alpha_{3}$ is a $\mathcal{K}_{\lbrack 0,d)}$-function (add $\frac{r}{d - r}$ to it if it is not). When ${\parallel\mu\parallel} \leq {\alpha_{1}{({\mathcal{V}{(\xi)}})}}$, ${{\mathcal{V}{({f{(\xi,\mu)}})}} - {\mathcal{V}{(\xi)}}} \leq {- {\alpha_{2}{({\mathcal{V}{(\xi)}})}}}$; when ${\parallel\mu\parallel} \geq {\alpha_{1}{({\mathcal{V}{(\xi)}})}}$, ${{\mathcal{V}{({f{(\xi,\mu)}})}} - {\mathcal{V}{(\xi)}}} \leq {{- {\alpha_{2}{({\mathcal{V}{(\xi)}})}}} + {\alpha_{3}{({\parallel\mu\parallel})}}}$. Hence, ((https://arxiv.org/html/2507.02131v1#S3.E6 "In Remark 14. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) holds.

As in classic Lyapunov stability theory, we can show that small-disturbance ISS is equivalent to the existence of a small-disturbance ISS-Lyapunov function.

### Theorem 15

System ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS if and only if it admits a small-disturbance ISS-Lyapunov function.

Sufficiency: The proof for the ISS property in \[(https://arxiv.org/html/2507.02131v1#bib.bib25)\] is adapted here. We denote by ${\chi{(k)}} = {\chi{(k,\xi,w)}}$ the state trajectory of ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) for fixed initial state $\xi \in \mathcal{S}$ and input $w \in \ell_{\infty}^{m}$. For the input $w$ with ${\parallel w\parallel}_{\infty} < d$ and $r \in {\lbrack 0,d)}$, where $d = {\sup_{r \in {\mathbb{R}}_{+}}{\alpha_{1}{(r)}}}$, define ${{\hat{\alpha}}_{4}{(r)}} = {\max{\{{\left. {\mathcal{V}{({f{(\xi,\mu)}})}} \middle| {\parallel\mu\parallel} \right. \leq r},{{\alpha_{1}{({\mathcal{V}{(\xi)}})}} \leq r}\}}}$ and ${\alpha_{4}{(r)}} = {\max{\{{{\hat{\alpha}}_{4}{(r)}},{\alpha_{1}^{- 1}{(r)}}\}}}$. Then, $\alpha_{4}$ is continuous, non-decreasing, zero at zero, and can be assumed as a $\mathcal{K}_{\lbrack 0,d)}$-function (add $\frac{r}{d - r}$ if it is not). Let $\mathcal{S}_{w} = \left. \{{\xi \in \mathcal{S}} \middle| {{\mathcal{V}{(\xi)}} \leq {\alpha_{4}{({\parallel w\parallel}_{\infty})}}}\} \right.$. We first show that $\mathcal{S}_{w}$ is forward invariant.\
Claim: If ${\chi{(k_{0})}} \in \mathcal{S}_{w}$ for some $k_{0} \in {\mathbb{Z}}_{+}$, then ${\chi{(k)}} \in \mathcal{S}_{w}$ for all $k \geq k_{0}$.\
Proof of the claim: Suppose that ${\chi{(k_{0})}} \in \mathcal{S}_{w}$. When ${\alpha_{1}^{- 1}{({\parallel w\parallel}_{\infty})}} < {\mathcal{V}{({\chi{(k_{0})}})}} \leq {\alpha_{4}{({\parallel w\parallel}_{\infty})}}$, it follows from ((https://arxiv.org/html/2507.02131v1#S3.E5 "In item 2 ‣ Definition 12. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) that ${\mathcal{V}{({\chi{({k_{0} + 1})}})}} \leq {\mathcal{V}{({\chi{(k_{0})}})}} \leq {\alpha_{4}{({\parallel w\parallel}_{\infty})}}$. When $0 \leq {\mathcal{V}{({\chi{(k_{0})}})}} \leq {\alpha_{1}^{- 1}{({\parallel w\parallel}_{\infty})}}$, by the definition of ${\hat{\alpha}}_{4}{({\parallel w\parallel}_{\infty})}$, ${\mathcal{V}{({\chi{({k_{0} + 1})}})}} \leq {{\hat{\alpha}}_{4}{({\parallel w\parallel}_{\infty})}} \leq {\alpha_{4}{({\parallel w\parallel}_{\infty})}}$. Induction can be used to show that ${\mathcal{V}{({\chi{({k_{0} + j})}})}} \leq {\alpha_{4}{({\parallel w\parallel}_{\infty})}}$ for all $j \in {\mathbb{Z}}_{+}$.

We now let $k_{1} = {\min{\{{k \in \left. {\mathbb{Z}}_{+} \middle| {\chi{(k)}} \right. \in \mathcal{S}_{w}}\}}} \leq \infty$. Then, if follows from the above claim that

For $k < k_{1}$, ${\mathcal{V}{({\chi{(k)}})}} > {\alpha_{4}{({\parallel w\parallel}_{\infty})}} \geq {\alpha_{1}^{- 1}{({\parallel w\parallel}_{\infty})}}$, and it follows from ((https://arxiv.org/html/2507.02131v1#S3.E5 "In item 2 ‣ Definition 12. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) that

By the comparison lemma \[(https://arxiv.org/html/2507.02131v1#bib.bib25), Lemma 4.3\], there exists a $\mathcal{K}\mathcal{L}$-function $\beta$ such that

Hence, we can conclude from ((https://arxiv.org/html/2507.02131v1#S3.E7 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and ((https://arxiv.org/html/2507.02131v1#S3.E9 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) that system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS with $\gamma = \alpha_{4}$.

Necessity: The case when $\mathcal{S} = {\mathbb{R}}^{n}$ is proved first. For any bounded inputs $w$ with ${\parallel w\parallel}_{\infty} < d$, let ${v{(k)}} = {\frac{d}{d - {\parallel{w{(k)}}\parallel}}w{(k)}}$. By inverting the function (see Lemma (https://arxiv.org/html/2507.02131v1#Thmthm5 "Lemma 5 (Lemma 2.4 in ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), we can obtain that ${w{(k)}} = {\frac{d}{d + {\parallel{v{(k)}}\parallel}}v{(k)}}$ and ${\parallel{w{(k)}}\parallel} = {\gamma_{1}{({\parallel{v{(k)}}\parallel})}}$, where ${\gamma_{1}{(r)}} = \frac{dr}{d + r}$ is a $\mathcal{K}$-function with the range $\lbrack 0,d)$. Consider $v{(k)}$ as the input of system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), we have that

Since system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS, by ((https://arxiv.org/html/2507.02131v1#S3.E4 "In Definition 11 (). ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), it holds that

for all $k \in {\mathbb{Z}}_{+}$. Since $\mathcal{V}{(\xi)}$ and $\parallel{\xi - \chi^{\ast}}\parallel$ are size functions for $({\mathbb{R}}^{n},\chi^{\ast})$, from Lemma (https://arxiv.org/html/2507.02131v1#Thmthm6 "Lemma 6 (Proposition 2.6 in ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), there exist ${\rho_{1},\rho_{2}} \in \mathcal{K}_{\infty}$, such that

The fact that ${\gamma \circ \gamma_{1}} \in \mathcal{K}$, and plugging ((https://arxiv.org/html/2507.02131v1#S3.E12 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) into ((https://arxiv.org/html/2507.02131v1#S3.E11 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and considering Lemma (https://arxiv.org/html/2507.02131v1#Thmthm1 "Lemma 1 (Weak triangle inequality ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), implies that the system ((https://arxiv.org/html/2507.02131v1#S3.E10 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is ISS. Consequently, there exists an ISS-Lyapunov function $\mathcal{V}_{1}$ \[(https://arxiv.org/html/2507.02131v1#bib.bib25), Theorem 1\], such that

for all ${\xi \in {\mathbb{R}}^{n}},{\nu \in {\mathbb{R}}^{m}}$, where ${\rho_{i},\gamma_{2}} \in {\mathcal{K}_{\infty}{({i = {3,4,5}})}}$. This further implies that, if ${\parallel\nu\parallel} \leq {{{{\gamma_{2}^{- 1} \circ \frac{1}{2}}\rho_{5}} \circ \rho_{4}^{- 1}}{({\mathcal{V}{(\xi)}})}}$, ${{\mathcal{V}_{1}{({f_{1}{(\xi,\nu)}})}} - {\mathcal{V}_{1}{(\xi)}}} \leq {- {{{\frac{1}{2}\rho_{5}} \circ \rho_{4}^{- 1}}{({\mathcal{V}_{1}{(\xi)}})}}}$. Consequently, if $\mu = {\frac{d}{d + {\parallel\nu\parallel}}\nu}$ and ${\parallel\mu\parallel} \leq {{{{\gamma_{1} \circ \gamma_{2}^{- 1} \circ \frac{1}{2}}\rho_{5}} \circ \rho_{4}^{- 1}}{({\mathcal{V}_{1}{(\xi)}})}}$, ${{\mathcal{V}_{1}{({f{(\xi,\mu)}})}} - {\mathcal{V}_{1}{(\xi)}}} \leq {- {{{\frac{1}{2}\rho_{5}} \circ \rho_{4}^{- 1}}{({\mathcal{V}_{1}{(\xi)}})}}}$. Since ${{\gamma_{1} \circ \gamma_{2}^{- 1} \circ \frac{1}{2}}\rho_{5}} \circ \rho_{4}^{- 1}$ is a $\mathcal{K}$-function with the range $\lbrack 0,d)$, we conclude that the $\mathcal{V}_{1}$ is a small-disturbance ISS-Lyapunov function for system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")).

Next consider the case where $\mathcal{S}$ is an open subset of ${\mathbb{R}}^{n}$ which is homeomorphic to ${\mathbb{R}}^{n}$. Let $\varphi$ denote the homeomorphism from $\mathcal{S}$ to ${\mathbb{R}}^{n}$. For ${\chi{(k)}} \in \mathcal{S}$, let ${\zeta{(k)}} = {\varphi{({\chi{(k)}})}}$ and $\zeta^{\ast} = {\varphi{(\chi^{\ast})}}$. It follows from ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) that

Since system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS over $\mathcal{S} \times {\mathbb{R}}^{m}$, it holds that

for all $k \in {\mathbb{Z}}_{+}$ and all $w \in \ell_{\infty}^{m}$ bounded by $d$. Since the compactness of $\left. \{{\xi \in \mathcal{S}} \middle| {{\mathcal{V}{(\xi)}} \leq c}\} \right.$ implies the compactness of $\left. \{{\zeta \in {\mathbb{R}}^{n}} \middle| {{{\mathcal{V} \circ \varphi^{- 1}}{(\zeta)}} \leq c}\} \right.$, $\mathcal{V} \circ \varphi^{- 1}$ is a proper/coercive function over ${\mathbb{R}}^{n}$. Hence, system ((https://arxiv.org/html/2507.02131v1#S3.E15 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS over ${\mathbb{R}}^{n} \times {\mathbb{R}}^{m}$. According the results for the case of $\mathcal{S} = {\mathbb{R}}^{n}$, there exists a small-disturbance ISS function $\mathcal{V}_{2}$ for system ((https://arxiv.org/html/2507.02131v1#S3.E15 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). It can be easily checked that ${\mathcal{V}_{2} \circ \varphi}:{\mathcal{S}\rightarrow{\mathbb{R}}_{+}}$ is a size function for system ((https://arxiv.org/html/2507.02131v1#S3.E3 "In 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). In conclusion, the necessity holds.

In the above analysis, it is required that $\mathcal{S}$ be homeomorphic to ${\mathbb{R}}^{n}$, which can often be verified directly from the context of the problem---for example, in the LQR problem, where the set of stabilizing gains is homeomorphic to a Euclidean space. If this condition cannot be verified directly, the arguments in \[(https://arxiv.org/html/2507.02131v1#bib.bib62), Theorem 2.2\] can be followed to establish that $\mathcal{S}$ is homeomorphic to ${\mathbb{R}}^{n}$, provided that the function $f{( \cdot,0)}$ is additionally assumed to be a diffeomorphism.

### Remark 16

If $f{( \cdot,0)}$ is a diffeomorphism and the domain of asymptotic stability of $\chi^{\ast}$ is $\mathcal{S}$, then $\mathcal{S}$ is diffeomorphic to ${\mathbb{R}}^{n}$.

## Robustness Analysis of Perturbed Gradient Descent

This section applies the concept of small-disturbance ISS to analyze the gradient descent algorithm for solving the constrained nonlinear program:

where $\mathcal{Z}$ is an admissible set, defined as an open subset of ${\mathbb{R}}^{n}$ that is homeomorphic to ${\mathbb{R}}^{n}$, and $\mathcal{J}:{\mathcal{Z}\rightarrow{\mathbb{R}}}$ is an objective function with a unique global minimizer $z^{\ast}$.

### Definition 17

A continuously differentiable function $\mathcal{J}:{\mathcal{Z}\rightarrow{\mathbb{R}}}$ is a proper objective function if

${\mathcal{J}{(z)}} - {\mathcal{J}{(z^{\ast})}}$ is a size function for $(\mathcal{Z},z^{\ast})$;

${\nabla\mathcal{J}}{(z)}$ is Lipschitz continuous over the sublevel set ${\mathcal{Z}{(h)}} = \left. \{{z \in \mathcal{Z}} \middle| {{\mathcal{J}{(z)}} \leq h}\} \right.$, that is

for all ${z_{1},z_{2}} \in {\mathcal{Z}{(h)}}$.

there exists a $\mathcal{K}$-function $\alpha_{5}$, such that ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel} \geq {\alpha_{5}{({{\mathcal{J}{(z)}} - {\mathcal{J}{(z^{\ast})}}})}}$ ($\mathcal{K}$-PL estimate).

The perturbed gradient descent method for ((https://arxiv.org/html/2507.02131v1#S4.E17 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is

where ${\eta{(k)}} > 0$ is a step size, and $e \in \ell_{\infty}^{n}$ denotes the perturbation to the gradient algorithm. The perturbation $e{(k)}$ may arise from inaccurate gradient estimation in data-driven optimization, rounding errors in numerical computation, or even malicious attacks on the gradient descent algorithm.

### Theorem 18

If $\mathcal{J}$ is a proper objective function and the step size satisfies $0 < {\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$, then system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS.

The derivative of $\kappa{(k,s)}$ is written as

where the second line is from Cauchy-Schwarz inequality and Young's inequality, and the last line is a direct consequence of the $\mathcal{K}$-PL property.

When ${\parallel{e{(k)}}\parallel} \leq {\frac{1}{2}\alpha_{5}{({{\mathcal{J}{({z{(k)}})}} - {\mathcal{J}{(z^{\ast})}}})}}$, we first show that ${z{({k + 1})}} \in {\mathcal{Z}{({\mathcal{J}{({z{(k)}})}})}}$. It follows from ((https://arxiv.org/html/2507.02131v1#S4.E21 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) that

Hence, ${\kappa{(k,s)}} < {\kappa{(k,0)}} = {\mathcal{J}{({z{(k)}})}}$ for some small $s > 0$. Since $\mathcal{J}$ is coercive, the sublevel set $\mathcal{Z}{(\mathcal{J}{(z{(k)})}}$ is compact \[(https://arxiv.org/html/2507.02131v1#bib.bib56), Lemma 2.4\]. As a result, ${z{(k)}} - {s{({{{\nabla\mathcal{J}}{({z{(k)}})}} + {e{(k)}}})}}$ can reach the boundary of $\mathcal{Z}{({\mathcal{J}{({z{(k)}})}})}$ for some ${\overline{s}{(k)}} > 0$. Denote $\overline{s}{(k)}$ as the point at which the boundary is first reached, i.e. ${\kappa{(k,{\overline{s}{(k)}})}} = {\mathcal{J}{({z{(k)}})}}$, and ${{z{(k)}} - {s{({{{\nabla\mathcal{J}}{({z{(k)}})}} + {e{(k)}}})}}} \in {\mathcal{Z}{({\mathcal{J}{({z{(k)}})}})}}$ for all $0 \leq s \leq {\overline{s}{(k)}}$. Since $\kappa{(k,s)}$ is $L_{1}{({\mathcal{J}{({z{(k)}})}})}$-smooth over $s \in {\lbrack 0,{\overline{s}{(k)}}\rbrack}$ with ${L_{1}{({\mathcal{J}{({z{(k)}})}})}} = {{\parallel{{{\nabla\mathcal{J}}{({z{(k)}})}} + {e{(k)}}}\parallel}^{2}L{({\mathcal{J}{({z{(k)}})}})}}$, according to \[(https://arxiv.org/html/2507.02131v1#bib.bib42), Lemma 1.2.3\], it holds that

where the second line is from ((https://arxiv.org/html/2507.02131v1#S4.E21 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). Suppose that ${\overline{s}{(k)}} < \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$, which implies

Using Cauchy-Schwarz inequality, Young's inequality, and the $\mathcal{K}$-PL condition,

Since ${\kappa{(k,{\overline{s}{(k)}})}} < {\mathcal{J}{({z{(k)}})}}$ contradicts ${\kappa{(k,{\overline{s}{(k)}})}} = {\mathcal{J}{({z{(k)}})}}$, it follows that ${\overline{s}{(k)}} \geq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$. Note that ${z{(k)}} - {s{({{{\nabla\mathcal{J}}{({z{(k)}})}} + {e{(k)}}})}}$ reaches the boundary of $\mathcal{Z}{({\mathcal{J}{({z{(k)}})}})}$ for the first time when $s = {\overline{s}{(k)}}$. Hence, ${\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}} \leq {\overline{s}{(k)}}$ leads to ${z{({k + 1})}} \in {\mathcal{Z}{({\mathcal{J}{({z{(k)}})}})}}$.

Next, we show that ${\mathcal{J}{({z{(k)}})}} - {\mathcal{J}{(z^{\ast})}}$ is a small-disturbance ISS-Lyapunov function for system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). Note that

Since ${{z{(k)}},{z{({k + 1})}}} \in {\mathcal{Z}{({\mathcal{J}{({z{(k)}})}})}}$ when ${\parallel{e{(k)}}\parallel} \leq {\frac{1}{2}\alpha_{5}{({{\mathcal{J}{({z{(k)}})}} - {\mathcal{J}{(z^{\ast})}}})}}$, by ((https://arxiv.org/html/2507.02131v1#S4.E23 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and ((https://arxiv.org/html/2507.02131v1#S4.E25 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), it holds that

According to Theorem (https://arxiv.org/html/2507.02131v1# "Theorem 15. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), we conclude that system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS.

In conclusion, Theorem (https://arxiv.org/html/2507.02131v1# "Theorem 18. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") indicates that despite the presence of perturbation $e$ with a bounded magnitude ${\parallel e\parallel}_{\infty} < {\frac{1}{2}{\sup_{r \in {\mathbb{R}}_{+}}{\alpha_{5}{(r)}}}}$, the gradient descent algorithm can still converge to a neighborhood of the optimum $z^{\ast}$, specifically$\left. \{{z \in \mathcal{Z}} \middle| {{{\mathcal{J}{(z)}} - {\mathcal{J}{(z^{\ast})}}} \leq {\alpha_{5}^{- 1}{({2{\parallel e\parallel}_{\infty}})}}}\} \right.$.

Corollary (https://arxiv.org/html/2507.02131v1# "Corollary 19. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") indicates that if the $\mathcal{K}$-PL estimate in Definition (https://arxiv.org/html/2507.02131v1# "Definition 17. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") is strengthened to a $\mathcal{K}_{\infty}$-function, then the system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is ISS \[(https://arxiv.org/html/2507.02131v1#bib.bib25)\], which is a stronger property than small-disturbance ISS.

### Corollary 19

If the $\mathcal{K}$-PL estimate $\alpha_{5}$ in Definition (https://arxiv.org/html/2507.02131v1# "Definition 17. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") is strengthened to a $\mathcal{K}_{\infty}$-function, and the step size satisfies $0 < {\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$, then system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is ISS.

By following the same reasoning as in the proof of Theorem (https://arxiv.org/html/2507.02131v1# "Theorem 18. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), if ${\parallel{e{(k)}}\parallel} \leq {\frac{1}{2}\alpha_{5}{({{\mathcal{J}{({z{(k)}})}} - {\mathcal{J}{(z^{\ast})}}})}}$, then

Since $\alpha_{5}$ is a $\mathcal{K}_{\infty}$-function, it follows from \[(https://arxiv.org/html/2507.02131v1#bib.bib24), Lemma 3.5\] that the system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is ISS.

Additionally, the following corollary states that, if the $\mathcal{K}$-PL estimate $\alpha_{5}$ in Definition (https://arxiv.org/html/2507.02131v1# "Definition 17. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") is relaxed to a positive definite function, then the system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is integral ISS, which is equivalent to global asymptotic stability for discrete-time dynamical systems \[(https://arxiv.org/html/2507.02131v1#bib.bib3)\].

### Corollary 20

If the $\mathcal{K}$-PL estimate $\alpha_{5}$ in Definition (https://arxiv.org/html/2507.02131v1# "Definition 17. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") is relaxed to a positive definite function, and the step size satisfies $0 < {\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$, then system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is integral ISS.

In the absence of noise, the gradient system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) satisfies the inequality:

This implies that the gradient system is globally asymptotically stable. Moreover, by the main result of \[(https://arxiv.org/html/2507.02131v1#bib.bib3)\], it is also integral ISS.

### Remark 21

The gradient dominance condition proposed in Definition (https://arxiv.org/html/2507.02131v1# "Definition 17. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), i.e. the $\mathcal{K}$-PL condition, can be viewed as a nonlinear generalization of the well-known PL condition. If the classical PL condition holds \[(https://arxiv.org/html/2507.02131v1#bib.bib47), (https://arxiv.org/html/2507.02131v1#bib.bib37)\], meaning ${\alpha_{5}{(r)}} = {c\sqrt{r}}$ for all $r \geq 0$ and some $c > 0$, the perturbed gradient descent algorithm in ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is exponentially ISS.

We present several examples of objective functions for which the robustness of the associated gradient descent algorithms is analyzed using the proposed framework.

### Example 22

Consider the optimization problem ${{\min_{z \in {(1,\infty)}}\mathcal{J}}{(z)}} = \frac{{({z - z^{\ast}})}^{2}}{2{({z - 1})}}$ where $z^{\ast} = {1 + \sqrt{2}}$ and ${\mathcal{J}{(z^{\ast})}} = 0$. It can be verified that

The function $\mathcal{J}{(z)}$ is a size function and ${\nabla\mathcal{J}}{(z)}$ is Lipschitz continuous over any sublevel sets. Consequently, if the step size satisfies $0 < {\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$, then the perturbed gradient descent algorithm in ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS.

### Example 23

Consider the optimization problem ${{\min_{z \in {\mathbb{R}}}\mathcal{J}}{(z)}} = {\frac{1}{4}z^{4}}$ with the optimal solution $z^{\ast} = 0$ and ${\mathcal{J}{(z^{\ast})}} = 0$. The function is not strongly convex since its second derivative ${{\nabla^{2}\mathcal{J}}{(z)}} = 0$ at $z = 0$. Furthermore, since ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel}^{2} = {o{({\mathcal{J}{(z)}})}}$ as $z\rightarrow 0$, there does not exist a constant $c > 0$ such that ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel}^{2} \geq {c\mathcal{J}{(z)}}$, which implies that the classical PL condition does not hold. Since ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel} = {({4\mathcal{J}{(z)}})}^{3/4}$, it follows from Corollary (https://arxiv.org/html/2507.02131v1# "Corollary 19. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") that the perturbed gradient descent in ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is ISS if the step size satisfies $0 < {\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$.

### Example 24

Consider the optimization problem ${{\min_{z \in {\mathbb{R}}}\mathcal{J}}{(z)}} = {\log{({z^{2} + 1})}}$, which has a minimum at $z^{\ast} = 0$. The gradient is given by ${{\nabla\mathcal{J}}{(z)}} = \frac{2z}{z^{2} + 1}$. Since ${\lim_{z\rightarrow\infty}{\parallel{{\nabla\mathcal{J}}{(z)}}\parallel}} = 0$ while ${\lim_{z\rightarrow\infty}{\mathcal{J}{(z)}}} = \infty$, we can only identify a positive definite function $\alpha_{5}$ such that ${\parallel{{\nabla\mathcal{J}}{(z)}}\parallel} \geq {\alpha_{5}{({\mathcal{J}{(z)}})}}$. Therefore, by Corollary (https://arxiv.org/html/2507.02131v1# "Corollary 20. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), the gradient system ((https://arxiv.org/html/2507.02131v1#S4.E19 "In 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is integral ISS provided that the step size satisfies $0 < {\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({z{(k)}})}})}}$.

## Application to LQR Problem

In this section, we utilize the tool of small-disturbance ISS to analyze the robustness of the gradient descent algorithms in solving the LQR problem. Some preliminaries on the LQR are introduced in the next subsection.

### Preliminaries of LQR

A linear time-invariant (LTI) system can be represented by

where ${x{(t)}} \in {\mathbb{R}}^{n}$ denotes the state with the initial state $x_{0}$; ${u{(t)}} \in {\mathbb{R}}^{m}$ denotes the control input; $A \in {\mathbb{R}}^{n \times n}$ and $B^{n \times m}$ are constant matrices. The LQR problem aims to find a state-feedback controller by minimizing the cumulative quadratic cost

with ${Q,R} \in {\mathbb{S}}_{+ +}^{n}$. Suppose that $(A,B)$ is stabilizable, according to \[(https://arxiv.org/html/2507.02131v1#bib.bib54), Section 8.4\], the optimal controller is expressed as

where $P^{\ast} \in {\mathbb{S}}_{+ +}^{n}$ is the solution of the algebraic Riccati equation (ARE)

The optimal controller $K^{\ast}$, as indicated in \[(https://arxiv.org/html/2507.02131v1#bib.bib12)\], can be found by directly solving the optimization problem

where $\mathcal{G} = \left. \{{K \in {\mathbb{R}}^{m \times n}} \middle| {A - {BK\text{~is Hurwitz}}}\} \right.$ is the admissible set containing all the stabilizing gains, and $P_{K} \in {\mathbb{S}}_{+ +}^{n}$ is the solution of the Lyapunov equation

Since $\mathcal{G}$ is diffeomorphic to an open convex subset of ${\mathbb{R}}^{m \times n}$ \[(https://arxiv.org/html/2507.02131v1#bib.bib9), Lemma 3.2\], and every open convex subset of ${\mathbb{R}}^{m \times n}$ is homeomorphic to ${\mathbb{R}}^{m \times n}$ itself \[(https://arxiv.org/html/2507.02131v1#bib.bib17)\], it follows that $\mathcal{G}$ is homeomorphic to ${\mathbb{R}}^{m \times n}$.

We next derive the gradient of $\mathcal{J}_{2}{(K)}$. For any $K \in \mathcal{G}$, the increment of ((https://arxiv.org/html/2507.02131v1#S5.E35 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is

It follows from Corollary (https://arxiv.org/html/2507.02131v1#Thmthm8 "Corollary 8. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") that

where $Y_{K} \in {\mathbb{S}}_{+ +}^{n}$ is the solution of

Hence, for any $K \in \mathcal{G}$, the gradient of $\mathcal{J}_{2}{(K)}$ can be computed by

Throughout this article, define $Y^{\ast} \in {\mathbb{S}}_{+ +}^{\ast}$ as the solution of ((https://arxiv.org/html/2507.02131v1#S5.E38 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) with $K$ replaced by $K^{\ast}$. In addition, using corollary (https://arxiv.org/html/2507.02131v1#Thmthm8 "Corollary 8. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") and Lemma (https://arxiv.org/html/2507.02131v1#Thmthm3 "Lemma 3 (Trace inequality ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), it holds that

The following lemma presents a lower bound of $Y_{K}$.

### Lemma 25 (Lemma 5.2 in \[[12](https://arxiv.org/html/2507.02131v1#bib.bib12)\])

For any $K \in \mathcal{G}$, it holds that

The following lemma shows that $\parallel K\parallel$ can be bounded by $\mathcal{J}_{2}{(K)}$.

### Lemma 26

For any $K \in \mathcal{G}$, $\parallel K\parallel$ is bounded by

It follows from ((https://arxiv.org/html/2507.02131v1#S5.E40 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and Lemmas (https://arxiv.org/html/2507.02131v1#Thmthm3 "Lemma 3 (Trace inequality ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") and (https://arxiv.org/html/2507.02131v1# "Lemma 25 (Lemma 5.2 in ). ‣ 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") that

By viewing ((https://arxiv.org/html/2507.02131v1#S5.E42 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) as a quadratic inequality of $\parallel K\parallel$, and bounding the largest root of $\parallel K\parallel$, we obtain

The proof is thus completed. The following lemma shows that the gradient ${\nabla\mathcal{J}_{2}}{(K)}$ is Lipschitz continuous over the sublevel set ${\mathcal{G}{(h)}} = \left. \{{K \in \mathcal{G}} \middle| {{\mathcal{J}_{2}{(K)}} \leq h}\} \right.$.

### Lemma 27

The gradient ${\nabla\mathcal{J}_{2}}{(K)}$ is $L{(h)}$-Lipschitz continuous over the sublevel set ${\mathcal{G}{(h)}} = \left. \{{K \in \mathcal{G}} \middle| {{\mathcal{J}_{2}{(K)}} \leq h}\} \right.$, with

To avoid using tensor notations, define ${\nabla^{2}\mathcal{J}_{2}}{(K)}{\lbrack{dK}\rbrack}$ as the action of the Hessian ${\nabla^{2}\mathcal{J}_{2}}{(K)}$ on ${dK} \in {\mathbb{R}}^{m \times n}$. A direct consequence of ((https://arxiv.org/html/2507.02131v1#S5.E39 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is that

where ${dP_{K}} \in {\mathbb{R}}^{n \times n}$ is defined in ((https://arxiv.org/html/2507.02131v1#S5.E36 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and ${dY_{K}} \in {\mathbb{R}}^{n \times n}$ can be obtained from the increment of ((https://arxiv.org/html/2507.02131v1#S5.E38 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), that is

We next aim to develop the bounds of $dP_{K}$ and $dY_{K}$. By the definition of spectral norm, therelation

can be obtained. Applying Corollary (https://arxiv.org/html/2507.02131v1#Thmthm9 "Corollary 9. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") to ((https://arxiv.org/html/2507.02131v1#S5.E36 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and ((https://arxiv.org/html/2507.02131v1#S5.E46 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) results in

which, in turn, implies that

Similarly, applying Corollary (https://arxiv.org/html/2507.02131v1#Thmthm9 "Corollary 9. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") to ((https://arxiv.org/html/2507.02131v1#S5.E45 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), and considering

Now, we are ready to prove the statement. Taking the norm of ((https://arxiv.org/html/2507.02131v1#S5.E44 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and plugging in ((https://arxiv.org/html/2507.02131v1#S5.E40 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), ((https://arxiv.org/html/2507.02131v1#S5.E48 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), and ((https://arxiv.org/html/2507.02131v1#S5.E50 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) results in

By Lemma (https://arxiv.org/html/2507.02131v1# "Lemma 26. ‣ 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), it follows that

Plugging ((https://arxiv.org/html/2507.02131v1#S5.E52 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) into ([5.1](https://arxiv.org/html/2507.02131v1#S5. "5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) yields

Hence, the proof is completed by \[(https://arxiv.org/html/2507.02131v1#bib.bib42), Lemma 1.2.2\].

### Small-Disturbance ISS of Standard Gradient Descent

This subsection applies the concept of small-disturbance ISS to analyze the robustness of the standard gradient descent method for the LQR problem,

where ${P{(k)}} = P_{K{(k)}}$, ${Y{(k)}} = Y_{K{(k)}}$, and $W \in \ell_{\infty}^{m \times n}$ is the perturbation to the gradient descent algorithm. The perturbation $W$ can represent gradient estimation errors in the context of data-driven control. When the system matrices are unknown, gradient estimation can be achieved through the finite-difference method \[(https://arxiv.org/html/2507.02131v1#bib.bib16)\] or approximate dynamic programming \[(https://arxiv.org/html/2507.02131v1#bib.bib23)\], both of which introduce errors due to measurement noise, system process noise, and even potential malicious attacks on the algorithm. The following lemma is introduced to ensure that $\mathcal{J}_{2}{(K)}$ satisfy the $\mathcal{K}$-PL condition in Definition (https://arxiv.org/html/2507.02131v1# "Definition 17. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), which is critical to the robustness analysis.

### Lemma 28 (Lemma 5.7 in \[[12](https://arxiv.org/html/2507.02131v1#bib.bib12)\])

The objective function $\mathcal{J}_{2}{(K)}$ satisfies the $\mathcal{K}$-PL condition, that is

### Remark 29

The classical PL condition requires ${\parallel{{\nabla\mathcal{J}_{2}}{(K)}}\parallel}^{2} \geq {c{({{\mathcal{J}_{2}{(K)}} - {\mathcal{J}_{2}{(K^{\ast})}}})}}$, which holds only over a compact sublevel set ${\mathcal{G}{(h)}} = \left. \{{K \in \mathcal{G}} \middle| {{\mathcal{J}_{2}{(K)}} \leq h}\} \right.$ due to the limitations of its linear form \[(https://arxiv.org/html/2507.02131v1#bib.bib10), (https://arxiv.org/html/2507.02131v1#bib.bib40)\]. In this article, by generalizing the classical PL condition to nonlinear form, we can obtain a global estimate of the gradient dominance condition.

With the established Lipschitz continuity and the $\mathcal{K}$-PL condition for the objective function $\mathcal{J}_{2}{(K)}$, we are now prepared to present the main result on the robustness of the gradient descent algorithm in ((https://arxiv.org/html/2507.02131v1#S5.E54 "In 5.2 Small-Disturbance ISS of Standard Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")).

### Theorem 30

If $0 < {\eta{(k)}} \leq \frac{1}{L{({\mathcal{J}{({K{(k)}})}})}}$, where $L{(h)}$ is defined in Lemma (https://arxiv.org/html/2507.02131v1# "Lemma 27. ‣ 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), the standard gradient descent algorithm in ((https://arxiv.org/html/2507.02131v1#S5.E54 "In 5.2 Small-Disturbance ISS of Standard Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS with respect to $W$.

Our task is simply to prove that the properties in Definition (https://arxiv.org/html/2507.02131v1# "Definition 17. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") are satisfied by the objective function $\mathcal{J}_{2}{(K)}$. The coercivity of $\mathcal{J}_{2}{(K)}$ is demonstrated in \[(https://arxiv.org/html/2507.02131v1#bib.bib10), Lemma 3.3\]. The $L{(h)}$-Lipschitz continuity and the $\mathcal{K}$-PL condition are established in Lemmas (https://arxiv.org/html/2507.02131v1# "Lemma 27. ‣ 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") and (https://arxiv.org/html/2507.02131v1# "Lemma 28 (Lemma 5.7 in ). ‣ 5.2 Small-Disturbance ISS of Standard Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), respectively. Consequently, by Theorem (https://arxiv.org/html/2507.02131v1# "Theorem 18. ‣ 4 Robustness Analysis of Perturbed Gradient Descent ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), the gradient descent algorithm in ((https://arxiv.org/html/2507.02131v1#S5.E54 "In 5.2 Small-Disturbance ISS of Standard Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS.

### Small-Disturbance ISS of Natural Gradient Descent

This subsection analyzes the robustness of the natural gradient descent algorithm, developed by leveraging the Riemannian geometry of the objective function $\mathcal{J}_{2}{(K)}$. By subtracting ((https://arxiv.org/html/2507.02131v1#S5.E33 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) from ((https://arxiv.org/html/2507.02131v1#S5.E35 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and completing the squares, the Lyapunov equation

can be obtained. Applying Corollary (https://arxiv.org/html/2507.02131v1#Thmthm8 "Corollary 8. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") to ((https://arxiv.org/html/2507.02131v1#S5.E56 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), the LQR cost can be expressed as a quadratic function over the Riemannian metric $(\mathcal{G},{\langle \cdot, \cdot \rangle}_{Y_{K}})$, that is,

The standard gradient descent in ((https://arxiv.org/html/2507.02131v1#S5.E54 "In 5.2 Small-Disturbance ISS of Standard Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) follows the steepest descent direction under the standard Euclidean metric $(\mathcal{G},{\langle \cdot, \cdot \rangle}_{I_{n}})$. However, this ad hoc choice of metric may not be appropriate. As seen in the expression for ${\nabla\mathcal{J}_{2}}{(K)}$ in ((https://arxiv.org/html/2507.02131v1#S5.E39 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), the magnitude of the gradient depends on $Y_{K}$, which can diverge as $K\rightarrow{\partial\mathcal{G}}$ but vanishes as ${\parallel K\parallel}_{F}\rightarrow\infty$ (see Example (https://arxiv.org/html/2507.02131v1# "Example 31. ‣ 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). The non-isotropic property induced by the improper choice of the Euclidean metric may degrade the convergence rate. As pointed out by Amari \[(https://arxiv.org/html/2507.02131v1#bib.bib1), (https://arxiv.org/html/2507.02131v1#bib.bib2)\], the choice of a metric should be based on the manifold that the optimization parameters lie in. Over the Riemannian manifold $(\mathcal{G},{\langle \cdot, \cdot \rangle}_{Y_{K}})$ and according to \[(https://arxiv.org/html/2507.02131v1#bib.bib2), (https://arxiv.org/html/2507.02131v1#bib.bib12)\], the steepest-descent direction can be derived as

In practice, the accurate gradient is not accessible and should be estimated through sampling and experiments. The perturbed natural gradient descent algorithm is

where ${P{(k)}} = P_{K{(k)}}$, $W \in \ell_{\infty}^{m \times n}$ denotes the perturbation and ${\eta{(k)}} > 0$ is the step size to be determined later.

The following example illustrates the advantage of natural gradient descent over standard gradient descent in terms of convergence rate.

### Example 31

Consider an LTI system with $A = 0$ and $B = Q = R = 1$, the admissible set of stabilizing gains is $\mathcal{G} = {(0,\infty)}$, with $Y_{K} = \frac{1}{2K}$ and cost function ${\mathcal{J}_{2}{(K)}} = P_{K} = \frac{K^{2} + 1}{2K}$. The standard gradient is ${{\nabla\mathcal{J}_{2}}{(K)}} = \frac{K^{2} - 1}{2K^{2}}$, while the natural gradient is ${{grad}\left( {\mathcal{J}_{2}{(K)}} \right)} = \frac{K^{2} - 1}{K}$. The optimal solution is $K^{\ast} = 1$ with the corresponding optimal cost ${\mathcal{J}_{2}{(K^{\ast})}} = 1$.

As $K\rightarrow\infty$, the standard gradient ${\nabla\mathcal{J}_{2}}{(K)}$ saturates, while the natural gradient ${grad}\left( {\mathcal{J}_{2}{(K)}} \right)$ remains unbounded. This distinction allows the natural gradient to achieve faster convergence, particularly when $K$ is far from the optimum. Under standard gradient descent with the update rule

it can be shown that

where ${m_{1}{(K,\eta)}} = \frac{{({{2K} - \eta})}{({K + 1})}^{2}}{{{4K^{4}} - {2\eta K^{3}}} + {2\eta K}}$. In comparison, under natural gradient descent with the update rule

it can be verified that

where ${m_{2}{(K,\eta)}} = \frac{{({1 - \eta})}{({K + 1})}^{2}}{{{({1 - \eta})}K^{2}} + \eta}$. Since ${\lim_{K\rightarrow\infty}{m_{1}{(K,\eta)}}} = 0$ while ${\lim_{K\rightarrow\infty}{m_{2}{(K,\eta)}}} = 1$, the convergence rate of natural gradient descent is faster than that of standard gradient descent when $K$ is far from the optimum.

The following two lemmas are introduced to assist in the development of the small-disturbance ISS property of natural gradient descent.

### Lemma 32

For any $K \in \mathcal{G}$, the relation

holds. Note that $K_{+} = {R^{- 1}B^{\top}P_{K}}$.

Subtracting ((https://arxiv.org/html/2507.02131v1#S5.E33 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) from ((https://arxiv.org/html/2507.02131v1#S5.E35 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and completing the squares yield

Completing the squares again gives that

By plugging ((https://arxiv.org/html/2507.02131v1#S5.E60 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) into ((https://arxiv.org/html/2507.02131v1#S5.E59 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) results in

Since $A - {BK^{\ast}}$ is Hurwitz, according to Corollary (https://arxiv.org/html/2507.02131v1#Thmthm8 "Corollary 8. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), it holds that

which completes the proof.

### Lemma 33

For any $K \in \mathcal{G}$, it holds that

where ${c{(K)}} = {1 + {{\parallel Y^{\ast}\parallel}{\parallel{BR^{- 1}B^{\top}}\parallel}{Tr}\left( P_{K} \right)}}$.

It follows from ((https://arxiv.org/html/2507.02131v1#S5.E59 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and Corollary (https://arxiv.org/html/2507.02131v1#Thmthm8 "Corollary 8. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") that

where the last inequality follows from the trace inequality in Lemma (https://arxiv.org/html/2507.02131v1#Thmthm3 "Lemma 3 (Trace inequality ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable").

We are ready to state the main results on robustness analysis of the natural gradient descent algorithm in the presence of perturbations. The core idea is to demonstrate that the expression

serves as a small-disturbance ISS-Lyapunov function.

### Theorem 34

If $0 < {\eta{(k)}} \leq {\min\left\{ \frac{1}{2{\parallel R\parallel}},\frac{1}{6{\parallel R\parallel}c{({K{(k)}})}} \right\}}$, the natural gradient descent algorithm in ((https://arxiv.org/html/2507.02131v1#S5.E57 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS with respect to $W$.

The difference of $\mathcal{V}_{3}{(K)}$ along the trajectories of ((https://arxiv.org/html/2507.02131v1#S5.E57 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is

Lemma (https://arxiv.org/html/2507.02131v1# "Lemma 32. ‣ 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), the trace inequality in Lemma (https://arxiv.org/html/2507.02131v1#Thmthm3 "Lemma 3 (Trace inequality ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), the Cauchy-Schwarz inequality in Lemma (https://arxiv.org/html/2507.02131v1#Thmthm4 "Lemma 4 (Cauchy-Schwarz inequality). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), and Young's inequality imply that

Considering Lemma (https://arxiv.org/html/2507.02131v1# "Lemma 33. ‣ 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") and applying the trace inequality in Lemma (https://arxiv.org/html/2507.02131v1#Thmthm3 "Lemma 3 (Trace inequality ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") again give that

Hence, when ${\eta{(k)}} \leq \frac{1}{6{\parallel R\parallel}c{({K{(k)}})}}$, it holds that

We next derive the difference of ${\mathcal{V}_{4}{(K)}} = {{\mathcal{J}_{2}{(K)}} - {\mathcal{J}_{2}{(K^{\ast})}}}$ along the trajectories of ((https://arxiv.org/html/2507.02131v1#S5.E57 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). At the $({k + 1})$^th^ iteration, $P{({k + 1})}$ is the solution of the Lyapunov equation

The Lyapunov equation at the $k$^th^ iteration can be rewritten as

Subtracting ([5.3](https://arxiv.org/html/2507.02131v1#S5. "5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) from ((https://arxiv.org/html/2507.02131v1#S5.E70 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and considering ((https://arxiv.org/html/2507.02131v1#S5.E57 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) give that

If ${\eta{(k)}} \leq \frac{1}{2{\parallel R\parallel}}$, ${{4\eta{(k)}^{2}R} - {4\eta{(k)}I_{m}}} \preceq {{4\eta{(k)}^{2}{\parallel R\parallel}I_{m}} - {4\eta{(k)}I_{m}}} \preceq {- {2\eta{(k)}I_{m}}}$. By Lemma (https://arxiv.org/html/2507.02131v1#Thmthm3 "Lemma 3 (Trace inequality ). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable") and Corollary (https://arxiv.org/html/2507.02131v1#Thmthm8 "Corollary 8. ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), it holds that

where Lemma (https://arxiv.org/html/2507.02131v1#Thmthm4 "Lemma 4 (Cauchy-Schwarz inequality). ‣ 2 Notations and Facts ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), Young's inequality, and ((https://arxiv.org/html/2507.02131v1#S5.E40 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) are applied to derive the last inequality.

We are now prepared to demonstrate that the function

is indeed a small-disturbance ISS-Lyapunov function for the system in ((https://arxiv.org/html/2507.02131v1#S5.E57 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). Without losing generality, assuming that ${\lambda_{\min}(R)} \leq 1$. By combining ([5.3](https://arxiv.org/html/2507.02131v1#S5. "5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and ([5.3](https://arxiv.org/html/2507.02131v1#S5. "5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")), it follows that

where $c_{1} = {\frac{{3\lambda_{\min}(R)} + {2{\parallel R\parallel}}}{2{\parallel R\parallel}\lambda_{\min}(R)}{\parallel Y^{\ast}\parallel}}$ and $c_{2} = \frac{3}{2\lambda_{\min}(Q)}$. Since ${\eta{(k)}} \leq \frac{1}{2{\parallel R\parallel}}$ and ${\mathcal{J}_{2}{({K{({k + 1})}})}} = {{\mathcal{V}_{3}{({K{({k + 1})}})}} + {\mathcal{J}_{2}{(K^{\ast})}}} \leq {{\mathcal{V}_{5}{({K{({k + 1})}})}} + {\mathcal{J}_{2}{(K^{\ast})}}}$, it readily follows from ([5.3](https://arxiv.org/html/2507.02131v1#S5. "5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) that

In summary, if ${\parallel W{(k)}\parallel}_{F}^{2} \leq \sigma{(\mathcal{V}_{5}{(K{(k)})})})$, where ${\sigma{(r)}} = {\min{({\sigma_{1}{(r)}},{\sigma_{2}{(r)}})}}$, ${{\mathcal{V}_{5}{({K{({k + 1})}})}} - {\mathcal{V}_{5}{({K{(k)}})}}} \leq {- {\frac{\eta{(k)}\lambda_{\min}(R)}{4}\mathcal{V}_{5}{({K{(k)}})}}}$. Since $\sigma$ is a $\mathcal{K}$-function, according to Theorem (https://arxiv.org/html/2507.02131v1# "Theorem 15. ‣ 3 Small-Disturbance Input-to-State Stability ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable"), the system ((https://arxiv.org/html/2507.02131v1#S5.E57 "In 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS.

### Small-Disturbance ISS of the Gauss-Newton Method

This subsection analyzes the robustness of Gauss-Newton method for solving the policy optimization problem of the LQR presented in ((https://arxiv.org/html/2507.02131v1#S5.E34 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")). The action of the Hessian on ${dK} \in {\mathbb{R}}^{m \times n}$ can be reformulated based on ((https://arxiv.org/html/2507.02131v1#S5.E44 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) as

When $K = K^{\ast}$, we have ${{RK^{\ast}} - {B^{\top}P^{\ast}}} = 0$, and it follows from ((https://arxiv.org/html/2507.02131v1#S5.E36 "In 5.1 Preliminaries of LQR ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) that ${dP_{K}} = 0$ for all ${dK} \in {\mathbb{R}}^{m \times n}$. Therefore, in the vicinity of $K^{\ast}$, the last two terms in ((https://arxiv.org/html/2507.02131v1#S5.E81 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) become negligible, allowing us to approximate the Hessian as

This approximation of the Hessian is derived based on arguments similar to those used in the Gauss-Newton method \[(https://arxiv.org/html/2507.02131v1#bib.bib43), Section 10.3\]. Hence, the update direction of Gauss-Newton method is $- {({K - {R^{- 1}B^{\top}P_{K}}})}$, which is obtained by solving $dK$ from

Under the perturbation, the Gauss-Newton algorithm is

### Remark 35

The Gauss-Newton method in ((https://arxiv.org/html/2507.02131v1#S5.E84 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is derived based on the policy optimization of the LQR cost $\mathcal{J}_{2}{(K)}$. The update in ((https://arxiv.org/html/2507.02131v1#S5.E84 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) can also be interpreted as an application of the classical Newton's method to solve the nonlinear algebraic Riccati equation (ARE) \[(https://arxiv.org/html/2507.02131v1#bib.bib31), (https://arxiv.org/html/2507.02131v1#bib.bib18)\]:

Indeed, the action of the gradient of the Riccati operator $\mathcal{R}{(X)}$ on ${dX} \in {\mathbb{S}}^{n}$ is given by

According to Newton's method, at the $({k + 1})$^th^ iteration, $X{({k + 1})}$ is updated as

where $N{(k)}$, the Newton's updated direction, is the solution of ${{\nabla\mathcal{R}}{({X{(k)}})}{\lbrack{N{(k)}}\rbrack}} = {- {\mathcal{R}{({X{(k)}})}}}$, that is

Let us define ${\overline{K}{(k)}} = {R^{- 1}B^{\top}X{(k)}}$ and ${\overline{P}{(k)}} = {{N{(k)}} + {X{(k)}}}$. With these definitions, ((https://arxiv.org/html/2507.02131v1#S5.E88 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) can be reformulated as

In addition, considering ((https://arxiv.org/html/2507.02131v1#S5.E87 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) and the relation ${N{(k)}} = {{\overline{P}{(k)}} - {X{(k)}}}$, the recursive formula of $\overline{K}{(k)}$ becomes

Hence, ((https://arxiv.org/html/2507.02131v1#S5.E90 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is equivalent to ((https://arxiv.org/html/2507.02131v1#S5.E84 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) without perturbation, which implies that the Gauss-Newton method in ((https://arxiv.org/html/2507.02131v1#S5.E84 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) coincides with Newton's method in ((https://arxiv.org/html/2507.02131v1#S5.E87 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) for solving the ARE. This interpretation establishes a connection between the Gauss-Newton method for policy optimization and the classical Newton's method for solving the ARE. The following theorem shows the small-disturbance ISS property of the Gauss-Newton method in ((https://arxiv.org/html/2507.02131v1#S5.E84 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")).

### Theorem 36

If $0 < {\eta{(k)}} \leq {\min\left\{ 1,\frac{1}{4c{({K{(k)}})}} \right\}}$, the Gauss-Newton method in ((https://arxiv.org/html/2507.02131v1#S5.E84 "In 5.4 Small-Disturbance ISS of the Gauss-Newton Method ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable")) is small-disturbance ISS with respect to $W$.

It can be shown that ${\mathcal{V}_{6}{(K)}} = {{\mathcal{V}_{4}{(K)}} + {\frac{1}{2}{\langle{K - K^{\ast}},{R{({K - K^{\ast}})}}\rangle}_{Y^{\ast}}}}$ is a small-disturbance ISS-Lyapunov function by following the proof of Theorem (https://arxiv.org/html/2507.02131v1# "Theorem 34. ‣ 5.3 Small-Disturbance ISS of Natural Gradient Descent ‣ 5 Application to LQR Problem ‣ Perturbed Gradient Descent Algorithms are Small-Disturbance Input-to-State Stable").

## Conclusions

This article introduces the concept of small-disturbance ISS as a unified framework for analyzing the robustness of gradient descent algorithms. Small-disturbance ISS provided a systematic approach to quantify the transient behavior, convergence speed, and robustness of gradient descent algorithms under perturbations. By generalizing the classical linear PL condition to a nonlinear version, referred to as the $\mathcal{K}$-PL condition, we show that gradient descent algorithms are small-disturbance ISS, provided the objective function satisfies the $\mathcal{K}$-PL condition. As a direct application to LQR, we demonstrate that three popular policy gradient algorithms in RL--standard policy gradient, natural policy gradient, and Gauss-Newton method--are all small-disturbance ISS.
