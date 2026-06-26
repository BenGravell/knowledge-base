<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions

Topics include Optimization, C2M, TM, Convex function.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider iterative gradient-based optimization algorithms applied to functions that are smooth and strongly convex. The fastest globally convergent algorithm for this class of functions is the Triple Momentum (TM) method. We show that if the objective function is also twice continuously differentiable, a new, faster algorithm emerges, which we call C2-Momentum (C2M). We prove that C2M is globally convergent and that its worst-case convergence rate is strictly faster than that of TM, with no additional computational cost. We validate our theoretical findings with numerical examples, demonstrating that C2M outperforms TM when the objective function is twice continuously differentiable.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We consider the well-studied optimization problem where $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is continuously differentiable. A popular approach to solving, particularly when the dimension $d$ is large, is to use iterative gradient-based methods, such as Gradient Descent (GD) and its accelerated variants.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A central question in the study of iterative methods is that of *worst-case convergence rate* over a class of functions $\mathcal{F}$. In this letter, we consider the *root-convergence factor* (also known as geometric convergence rate), denoted $\rho \in {}$, a notion we make precise in Section 2.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

$\rho$ is a *lower bound* for $\mathcal{F}$ if for any algorithm, there exists $f \in \mathcal{F}$ and an algorithm initialization such that the algorithm converges no faster than $\rho$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

$\rho$ is an *upper bound* for $\mathcal{F}$ if there exists an algorithm such that for all $f \in \mathcal{F}$ and algorithm initializations, the algorithm converges at least as fast as $\rho$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

If $\mathcal{F}$ has matching lower and upper bounds, this $\rho$ and the corresponding algorithm that achieves it are said to be *minimax optimal* for $\mathcal{F}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

Generally, adding more structure to a function class, such as convexity or Lipschitz properties, makes the minimax rate faster because iterative algorithms can exploit the additional structure to converge more rapidly. We now provide a brief survey of different function classes and their minimax rates. The relationship between these classes is illustrated in the Venn diagram of Fig. 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

The class $\mathcal{F}_{m,L}$ consists of continuously differentiable functions with sector-bounded gradients. Specifically, there exists $x_{\star} \in {\mathbb{R}}^{d}$ (the optimal point) and constants $0 < m \leq L$ such that ${\left( {{L{({x - x_{\star}})}} - {{\nabla f}{(x)}}} \right)^{\mathsf{T}}\left( {{{\nabla f}{(x)}} - {m{({x - x_{\star}})}}} \right)} \geq 0$ for all $x \in {\mathbb{R}}^{d}$. Functions in this class may be nonconvex but nevertheless have a unique local (and global) minimizer.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

The class $\mathcal{S}_{m,L}^{1}$ consists of functions that have Lipschitz gradient with Lipschitz constant $L$ and are strongly convex with parameter $m$. The superscript "1" indicates that $f \in C^{1}$, which follows from Lipschitz gradients. One can show that $\mathcal{S}_{m,L}^{1} \subset \mathcal{F}_{m,L}$. The minimax rate for $\mathcal{S}_{m,L}^{1}$ is $\rho = {1 - \frac{1}{\sqrt{\kappa}}}$, and was recently proved in using an exact characterization of $\mathcal{S}_{m,L}^{1}$ via interpolation conditions and the Performance Estimation paradigm. The same lower bound was obtained in a parallel line of work by viewing algorithms as discrete-time Lur'e systems and applying integral quadratic constraints (IQCs) or dissipativity theory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

Specifically, the set $\mathcal{S}_{m,L}^{1}$ was over-approximated using Zames--Falb IQCs, leading to an upper bound that turned out to be exact. The minimax rate for $\mathcal{S}_{m,L}^{1}$ is achieved by the Triple Momentum (TM) Method and the Information Theoretic Exact Method (ITEM).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

There are several minimax optimal methods for $\mathcal{Q}_{m,L}$, the simplest of which is Polyak's Heavy Ball (HB) method \[12, §3.2.1\]. Polyak used Lyapunov's indirect method to show that HB converges *locally* for any $f \in \mathcal{S}_{m,L}^{1}$ provided that $f$ is twice continuously differentiable ($f \in C^{2}$) in a neighborhood of the optimal point. In other words, HB converges on $\mathcal{S}_{m,L}^{1}$ when initialized sufficiently close to the optimal point and enjoys the same fast rate as for $\mathcal{Q}_{m,L}$! If incorrectly initialized, HB need not converge at all on $\mathcal{S}_{m,L}^{1}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

The aforementioned minimax optimal algorithms are described in Section 2.1 and summarized in Table 1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

Polyak's observation raises an interesting possibility, which forms the starting point for the present work. If we consider the function class $\mathcal{S}_{m,L}^{2}\operatorname{:-}{\mathcal{S}_{m,L}^{1} \cap C^{2}}$, then by Lyapunov's indirect method, any globally convergent method will converge at its *local rate*, which may be faster than the minimax rate of $\mathcal{S}_{m,L}^{1}$. This function class satisfies $\mathcal{Q}_{m,L} \subset \mathcal{S}_{m,L}^{2} \subset \mathcal{S}_{m,L}^{1}$ and may be characterized succinctly as functions whose Hessians satisfy ${mI_{d}} \preceq {{\nabla^{2}f}{(x)}} \preceq {LI_{d}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

Functions of interest in this category include regularized logistic loss, exponential family negative log-likelihoods with bounded natural parameters, and Moreau envelope smoothing of any $f \in \mathcal{S}_{m,L}^{1}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

Our main result is a new algorithm, $C^{2}$-Momentum (C2M). We show that C2M achieves an upper bound of $\max\left\{ \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1},\rho_{\text{C2M}} \right\}$ on $\mathcal{S}_{m,L}^{2}$, where $\rho_{\text{C2M}} < {1 - \sqrt{\frac{2}{\kappa}}}$. This corresponds to an iteration complexity that is faster than the minimax rate of $\mathcal{S}_{m,L}^{1}$ by a factor of $\sqrt{2}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

Notable related works are the recent papers, which use the same idea of optimizing the local convergence rate while enforcing global convergence. Specifically, these works develop re-tunings of HB and TM that converge globally on $\mathcal{F}_{m,L}$ but have optimized local rates because they also assume $f \in C^{2}$ locally near the optimal point.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Upper bounds", "weight": 1.0} -->

The rest of this letter is organized as follows. In Section 2 we describe C2M, in Section 3 we prove convergence results, in Section 4 we present some numerical results, and in Section 5 we discuss implications and future directions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "MAIN RESULT", "weight": 1.0} -->

In this section, we describe our proposed algorithm, state its main convergence result, and use root locus arguments to provide intuition behind the algorithm parameters.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm Form", "weight": 1.0} -->

We consider iterative first-order algorithms parameterized by ${\alpha,\beta,\eta} \in {\mathbb{R}}$ of the form for $k \geq 0$ with initial conditions ${x_{0},x_{- 1}} \in {\mathbb{R}}^{d}$. We can interpret such an algorithm as a linear time-invariant (LTI) system $G$ in feedback with the gradient $\nabla f$, where the transfer function^11^1As a slight abuse of notation, we use the same symbol to refer to both an LTI system and its transfer function. from the gradient $u_{k}$ to the point $y_{k}$ at which the gradient is evaluated is A minimal state-space realization of the reduced system $g$ is Despite its simplicity, the form can represent *all* algorithms referenced in Section 1 when $\alpha,\beta,\eta$ are suitably chosen (GD, HB, TM, ITEM, GHB, GAG). Table 1 shows parameters for the minimax methods discussed in Section 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main Result", "weight": 1.0} -->

To describe our main result, we first define the root-convergence factor of an algorithm, which is a way to characterize its rate of convergence; see \[15, §9.2\].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Root Locus Interpretation", "weight": 1.0} -->

Before rigorously analyzing the convergence of C2M, we first provide intuition behind the C2M parameters (5 ‣ 2.2 𝐶²-Momentum ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions")) using a root locus argument.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Root Locus Interpretation", "weight": 1.0} -->

Consider the general algorithm applied to a function $f \in \mathcal{Q}_{m,L} \subset \mathcal{S}_{m,L}^{2}$ with Hessian $Q$. By diagonalizing the Hessian, the iterates separate into $d$ decoupled systems, each in (positive) feedback with an eigenvalue $q_{i}$ of $Q$. Since the objective function is $L$-smooth, $m$-strongly convex, and twice continuously differentiable, its Hessian has eigenvalues in the interval $\lbrack m,L\rbrack$. Therefore, we can study worst-case local convergence by analyzing the eigenvalues of $A + {qBC}$ for $q \in {\lbrack m,L\rbrack}$. These closed-loop eigenvalues are solutions of the root locus $0 = {1 - {qg{(z)}}}$ for $q \in {\lbrack m,L\rbrack}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Root Locus Interpretation", "weight": 1.0} -->

The parameters of C2M are the solutions to the following conditions: The root locus passes through $z = {- \rho}$ when $q = L$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Root Locus Interpretation", "weight": 1.0} -->

The root locus has a double root at $z = \rho$ when $q = m$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Root Locus Interpretation", "weight": 1.0} -->

The visual reasoning for these two conditions is illustrated in Fig. 2, which shows the root locus of $1 - {qg{(z)}}$ as $q$ varies. As $q\rightarrow 0$, the roots are the poles of $g{(z)}$, which are $\beta$ and $1$. These roots meet at $z = \rho$, circle around the zero at $z = \frac{\eta}{1 + \eta}$, then break in on the negative real axis, with one root converging to the zero and the other going to $- \infty$ along the real axis. By enforcing the above two conditions, the root locus remains entirely inside the $\rho$-circle for all $q \in {\lbrack m,L\rbrack}$. In terms of the transfer function, these conditions are that where the last two equations are for the double root.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Root Locus Interpretation", "weight": 1.0} -->

Straightforward calculations show that the parameters (5 ‣ 2.2 𝐶²-Momentum ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions")) for C2M are the unique solution to the equations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "CONVERGENCE ANALYSIS", "weight": 1.0} -->

We now prove the main convergence result for C2M from 1 ‣ 2.3 Main Result ‣ 2 MAIN RESULT ‣ The Fastest Known First-Order Method for Minimizing Twice Continuously Differentiable Smooth Strongly Convex Functions"). Our proof consists of two steps. First, we show that the algorithm is globally asymptotically stable, meaning that the iterates converge to the minimizer of $f$ for all initial conditions. Once we have global convergence, we then show that the worst-case root-convergence factor is $\rho$ by analyzing the linearization of the algorithm about its equilibrium.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Global Stability via Frequency-Domain Analysis", "weight": 1.0} -->

To verify global asymptotic stability, we use integral quadratic constraints (IQCs). In discrete time, these are defined as follows (see ), where $\ell_{2}^{n}$ denotes the space of square-summable sequences on ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Local Convergence", "weight": 1.0} -->

While the root locus interpretation provides intuition behind the local convergence of C2M, we now use Lyapunov's indirect method along with the Jury criterion to systematically prove local convergence; see for similar analyses in other settings. We begin by characterizing the worst-case root convergence factor in terms of the system matrices.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Iteration Complexity", "weight": 1.0} -->

It is common in optimization to characterize algorithm convergence using *iteration complexity* \[11, §1.1.2\]. Iteration complexity is an expression for how the worst-case number of iterations $N$ required to reach a specified error $\varepsilon$ scales as a function of problem parameters such as $\kappa$, expressed asymptotically as $\varepsilon\rightarrow 0$ and $\kappa\rightarrow\infty$. If the convergence rate is $\rho$ as defined in 2, then $\left\| {x_{k} - x_{\star}} \right\| \leq {c{(k)}\rho^{k}}$, where $c{(k)}$ grows sub-exponentially in $k$. We seek the smallest $N$ such that ${c{(N)}\rho^{N}} \leq \varepsilon$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Iteration Complexity", "weight": 1.0} -->

Rearranging, we obtain ${{{\log c}{(N)}} + {N{\log\rho}}} \leq {\log\varepsilon}$. Since $c{(N)}$ is sub-exponential, it is dominated by the linear term in $N$ as $\varepsilon\rightarrow 0$ (and therefore $N\rightarrow\infty$), so we neglect it. We are left with $N \geq {\frac{- 1}{\log\rho}{\log\frac{1}{\varepsilon}}}$. Next, we expand $\frac{- 1}{\log\rho}$ as a function of $\kappa\rightarrow\infty$, keeping only the most significant term.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Iteration Complexity", "weight": 1.0} -->

For C2M, we do not have a nice expression for $\rho_{\text{C2M}}$, but we can nevertheless find an asymptotic analytic expansion for it about $\kappa\rightarrow\infty$, which leads to the bounds Therefore, $c = \sqrt{2}$ and $N_{\text{C2M}} \gtrsim {\frac{\sqrt{\kappa}}{\sqrt{2}}{\log\frac{1}{\varepsilon}}}$. In other words, C2M is faster than TM by a factor of $\sqrt{2}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Iteration Complexity", "weight": 1.0} -->

In contrast, GD has iteration complexity $N_{\text{GD}} \gtrsim {\frac{\kappa}{2}{\log\frac{1}{\varepsilon}}}$. In the optimization literature, methods with the $\sqrt{\kappa}$ factor instead of merely $\kappa$ are called *accelerated methods*. We can visualize iteration complexity by plotting $\frac{- 1}{\log\rho}$ versus $\kappa$ on a log-log scale (we omit the $\log\frac{1}{\varepsilon}$ factor); see Fig. 3. We also included a plot for GD (see Table 1).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Iteration Complexity", "weight": 1.0} -->

We see in Fig. 3 that non-accelerated methods (GD, GAG) have an asymptotic slope of $1$ whereas accelerated methods (C2M, TM) have an asymptotic slope of $\frac{1}{2}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "NUMERICAL VALIDATION", "weight": 1.0} -->

We simulate our proposed algorithm C2M along with several other first-order methods on a function chosen to showcase worst-case behavior. We used the function \[8, §IV\] where $g{(w)}$ is $\frac{1}{2}w^{2}e^{- {r/w}}$ if $w > 0$ and zero if $w \leq 0$. When $r > 0$ and $0 < m \leq L$ and $\left\| \begin{bmatrix} \end{bmatrix} \right\| = 1$, such functions satisfy $f \in \mathcal{S}_{m,L}^{2}$. We chose the parameters $L = 1$, $m = 10^{- 3}$, $r = 10^{- 3}$, $p = 2$, $a_{1} = {}$, $a_{2} = {(0,0.002)}$, and $b_{1} = b_{2} = 100$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "NUMERICAL VALIDATION", "weight": 1.0} -->

In Fig. 4, we plot error as a function of iteration. The function $f$ elicits worst-case behavior from GD, HB, and TM. In other words, GD and TM converge at their respective minimax rates for $\mathcal{F}_{m,L}$ and $\mathcal{S}_{m,L}^{1}$. Since $f \notin \mathcal{Q}_{m,L}$, HB is only locally convergent. In our simulation, we see that HB does not converge; however, if we were to initialize HB sufficiently close to $x_{\star}$, then it would converge at least as fast as the minimax rate for $\mathcal{Q}_{m,L}$. Our proposed C2M exploits additional smoothness in the objective to converge globally at a rate that is always faster than the minimax $\mathcal{S}_{m,L}^{1}$ rate.

<!-- chunk {"id": "body-0038", "role": "body", "section": "NUMERICAL VALIDATION", "weight": 1.0} -->

Likewise, GAG, which is globally convergent on $\mathcal{F}_{m,L}$, is slightly faster than GD, which is minimax-optimal on $\mathcal{F}_{m,L}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

The proposed C2M algorithm is the first method, to the best of the authors' knowledge, that is designed specifically for the function class $\mathcal{S}_{m,L}^{2}$. The minimax rate for this function class, however, is not known, in contrast to the function classes $\mathcal{S}_{m,L}^{1}$ and $\mathcal{Q}_{m,L}$. Finding this minimax rate or even lower bounds are interesting open problems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

The parameters of C2M are related to two other algorithms from the literature. As we have already seen, C2M reduces to HB when $\rho = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$. Moreover, the general C2M parameters are identical (after appropriate transformations) to those of GAG \[14, Cor. 1.1\]. This makes sense, since the work also considers the family of algorithms and is optimizing for local convergence. The two cases differ, however, in the choice of $\rho$, since GAG is optimized over the function class $\mathcal{F}_{m,L}$ defined in Section 1 rather than $\mathcal{S}_{m,L}^{2}$.
