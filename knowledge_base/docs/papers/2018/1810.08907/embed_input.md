<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Understanding the Acceleration Phenomenon via High-Resolution Differential Equations

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Gradient-based optimization algorithms can be studied from the perspective of limiting ordinary differential equations (ODEs). Motivated by the fact that existing ODEs do not distinguish between two fundamentally different algorithms - Nesterov's accelerated gradient method for strongly convex functions (NAG-SC) and Polyak's heavy-ball method - we study an alternative limiting process that yields high-resolution ODEs. We show that these ODEs permit a general Lyapunov function framework for the analysis of convergence in both continuous and discrete time. We also show that these ODEs are more accurate surrogates for the underlying algorithms; in particular, they not only distinguish between NAG-SC and Polyak's heavy-ball method, but they allow the identification of a term that we refer to as "gradient correction" that is present in NAG-SC but not in the heavy-ball method and is responsible for the qualitative difference in convergence of the two methods. We also use the high-resolution ODE framework to study Nesterov's accelerated gradient method for (non-strongly) convex functions, uncovering a hitherto unknown result - that NAG-C minimizes the squared gradient norm at an inverse cubic rate.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, by modifying the high-resolution ODE of NAG-C, we obtain a family of new optimization methods that are shown to maintain the accelerated convergence rates of NAG-C for smooth convex functions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Machine learning has become one of the major application areas for optimization algorithms during the past decade. While there have been many kinds of applications, to a wide variety of problems, the most prominent applications have involved large-scale problems in which the objective function is the sum over terms associated with individual data, such that stochastic gradients can be computed cheaply, while gradients are much more expensive and the computation (and/or storage) of Hessians is often infeasible. In this setting, simple first-order gradient descent algorithms have become dominant, and the effort to make these algorithms applicable to a broad range of machine learning problems has triggered a flurry of new research in optimization, both methodological and theoretical.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will be considering unconstrained minimization problems, where $f$ is a smooth convex function. Perhaps the simplest first-order method for solving this problem is gradient descent. Taking a fixed step size $s$, gradient descent is implemented as the recursive rule given an initial point $x_{0}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As has been known at least since the advent of conjugate gradient algorithms, improvements to gradient descent can be obtained within a first-order framework by using the history of past gradients. Modern research on such extended first-order methods arguably dates to Polyak, whose *heavy-ball method* incorporates a momentum term into the gradient step. This approach allows past gradients to influence the current step, while avoiding the complexities of conjugate gradients and permitting a stronger theoretical analysis. Explicitly, starting from an initial point ${x_{0},x_{1}} \in {\mathbb{R}}^{n}$, the heavy-ball method updates the iterates according to where $\alpha > 0$ is the momentum coefficient. While the heavy-ball method provably attains a faster rate of *local* convergence than gradient descent near a minimum of $f$, it does not come with *global* guarantees.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, demonstrate that even for strongly convex functions the method can fail to converge for some choices of the step size.^11^1 considers $s = {4/{({\sqrt{L} + \sqrt{\mu}})}^{2}}$ and $\alpha = {({1 - \sqrt{\mus}})}^{2}$. This momentum coefficient is basically the same as the choice $\alpha = \frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$ (adopted starting from Section 1.1) if $s$ is small.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The next major development in first-order methodology was due to Nesterov, who discovered a class of *accelerated gradient methods* that have a faster global convergence rate than gradient descent. For a $\mu$-strongly convex objective $f$ with $L$-Lipschitz gradients, Nesterov's accelerated gradient method (NAG-SC) involves the following pair of update equations: given an initial point $x_{0} = y_{0} \in {\mathbb{R}}^{n}$. Equivalently, NAG-SC can be written in a single-variable form that is similar to the heavy-ball method: starting from $x_{0}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Like the heavy-ball method, NAG-SC blends gradient and momentum contributions into its update direction, but defines a specific momentum coefficient $\frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$. Nesterov also developed the *estimate sequence technique* to prove that NAG-SC achieves an accelerated linear convergence rate: if the step size satisfies $0 < s \leq {1/L}$. Moreover, for a (weakly) convex objective $f$ with $L$-Lipschitz gradients, Nesterov defined a related accelerated gradient method (NAG-C), that takes the following form: with $x_{0} = y_{0} \in {\mathbb{R}}^{n}$. The choice of momentum coefficient $\frac{k}{k + 3}$, which tends to one, is fundamental to the estimate-sequence-based argument used by Nesterov to establish the following inverse quadratic convergence rate: for any step size $s \leq {1/L}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under an oracle model of optimization complexity, the convergence rates achieved by NAG-SC and NAG-C are optimal for smooth strongly convex functions and smooth convex functions, respectively.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Gradient Correction: Small but Essential", "weight": 1.0} -->

Throughout the present paper, we let $\alpha = \frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$ to define a specific implementation of the heavy-ball method in (1.2). This choice of the momentum coefficient and the second initial point renders the heavy-ball method and NAG-SC identical except for the last (small) term in (1.4). Despite their close resemblance, however, the two methods are in fact fundamentally different, with contrasting convergence results (see, for example, ). Notably, the former algorithm in general only achieves *local* acceleration, while the latter achieves acceleration method for all initial values of the iterate. As a numerical illustration, Figure 1 presents the trajectories that arise from the two methods when minimizing an ill-conditioned convex quadratic function.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gradient Correction: Small but Essential", "weight": 1.0} -->

We see that the heavy-ball method exhibits pronounced oscillations throughout the iterations, whereas NAG-SC is monotone in the function value once the iteration counter exceeds $50$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Gradient Correction: Small but Essential", "weight": 1.0} -->

This term corrects the update direction in NAG-SC by contrasting the gradients at consecutive iterates. Although an essential ingredient in NAG-SC, the effect of the gradient correction is unclear from the vantage point of the estimate-sequence technique used in Nesterov's proof. Accordingly, while the estimate-sequence technique delivers a proof of acceleration for NAG-SC, it does not explain why the absence of the gradient correction prevents the heavy-ball method from achieving acceleration for strongly convex functions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Gradient Correction: Small but Essential", "weight": 1.0} -->

A recent line of research has taken a different point of view on the theoretical analysis of acceleration, formulating the problem in continuous time and obtaining algorithms via discretization ). This can be done by taking continuous-time limits of existing algorithms to obtain ordinary differential equations (ODEs) that can be analyzed using the rich toolbox associated with ODEs, including Lyapunov functions^33^3One can think of the Lyapunov function as a generalization of the idea of the energy of a system. Then the method studies stability by looking at the rate of change of this measure of energy.. For instance, shows that with initial conditions ${X{}} = x_{0}$ and ${\overset{˙}{X}{}} = 0$, is the exact limit of NAG-C (1.5) by taking the step size $s\rightarrow 0$. Alternatively, the starting point may be a Lagrangian or Hamiltonian framework. In either case, the continuous-time perspective not only provides analytical power and intuition, but it also provides design tools for new accelerated algorithms.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gradient Correction: Small but Essential", "weight": 1.0} -->

Unfortunately, existing continuous-time formulations of acceleration stop short of differentiating between the heavy-ball method and NAG-SC. In particular, these two methods have the same limiting ODE (see, for example,): and, as a consequence, this ODE does not provide any insight into the stronger convergence results for NAG-SC as compared to the heavy-ball method. As will be shown in Section 2, this is because the gradient correction ${\frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}s\left({{{\nabla f}{(x_{k})}} - {{\nabla f}{(x_{k - 1})}}} \right)} = {O{(s^{1.5})}}$ is an order-of-magnitude smaller than the other terms in (1.4) if $s = {o{}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Gradient Correction: Small but Essential", "weight": 1.0} -->

Consequently, the gradient correction is not reflected in the low-resolution ODE (1.9) associated with NAG-SC, which is derived by simply taking $s\rightarrow 0$ in both (1.2) and (1.4).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Just as there is not a singled preferred way to discretize a differential equation, there is not a single preferred way to take a continuous-time limit of a difference equation. Inspired by dimensional-analysis strategies widely used in fluid mechanics in which physical phenomena are investigated at multiple scales via the inclusion of various orders of perturbations, we propose to incorporate $O{(\sqrt{s})}$ terms into the limiting process for obtaining an ODE, including the (Hessian-driven) gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in (1.7). This will yield *high-resolution ODEs* that differentiate between the NAG methods and the heavy-ball method.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

We list the high-resolution ODEs that we derive in the paper here^44^4We note that the form of the initial conditions is fixed for each ODE throughout the paper. For example, while $x_{0}$ is arbitrary, $X{}$ and $\overset{˙}{X}{}$ must always be equal to $x_{0}$ and $- {{2\sqrt{s}f{(x_{0})}}/{({1 + \sqrt{\mus}})}}$ respectively in the high-resolution ODE of the heavy-ball method.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

The high-resolution ODE for NAG-C (1.5): High-resolution ODEs are more accurate continuous-time counterparts for the corresponding discrete algorithms than low-resolution ODEs, thus allowing for a better characterization of the accelerated methods. This is illustrated in Figure 2, which presents trajectories and convergence of the discrete methods, and the low- and high-resolution ODEs. For both NAGs, the high-resolution ODEs are in much better agreement with the discrete methods than the low-resolution ODEs^55^5Note that for the heavy-ball method, the trajectories of the high-resolution ODE and the low-resolution ODE are almost identical.. Moreover, for NAG-SC, its high-resolution ODE captures the non-oscillation pattern while the low-resolution ODE does not.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

The three new ODEs include $O{(\sqrt{s})}$ terms that are not present in the corresponding low-resolution ODEs (compare, for example, (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) and (1.8)). Note also that if we let $s\rightarrow 0$, each high-resolution ODE reduces to its low-resolution counterpart. Thus, the difference between the heavy-ball method and NAG-SC is reflected only in their high-resolution ODEs: the gradient correction (1.7) of NAG-SC is preserved only in its high-resolution ODE in the form $\sqrt{s}{\nabla^{2}f}{({X{(t)}})}\overset{˙}{X}{(t)}$. This term, which we refer to as the (Hessian-driven) gradient correction, is connected with the discrete gradient correction by the approximate identity: for small $s$, with the identification $t = {k\sqrt{s}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

The gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in NAG-C arises in the same fashion^66^6Henceforth, the dependence of $X$ on $t$ is suppressed when clear from the context.. Interestingly, although both NAGs are first-order methods, their gradient corrections brings in second-order information from the objective function.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Despite being small, the gradient correction has a fundamental effect on the behavior of both NAGs, and this effect is revealed by inspection of the high-resolution ODEs. We provide two illustrations of this.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Effect of the gradient correction in acceleration. Viewing the coefficient of $\overset{˙}{X}$ as a damping ratio, the ratio ${2\sqrt{\mu}} + {\sqrt{s}{\nabla^{2}f}{(X)}}$ of $\overset{˙}{X}$ in the high-resolution ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-SC is adaptive to the position $X$, in contrast to the fixed damping ratio $2\sqrt{\mu}$ in the ODE (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) for the heavy-ball method.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

To appreciate the effect of this adaptivity, imagine that the velocity $\overset{˙}{X}$ is highly correlated with an eigenvector of ${\nabla^{2}f}{(X)}$ with a large eigenvalue, such that the large friction ${({{2\sqrt{\mu}} + {\sqrt{s}{\nabla^{2}f}{(X)}}})}\overset{˙}{X}$ effectively "decelerates" along the trajectory of the ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-SC. This feature of NAG-SC is appealing as taking a cautious step in the presence of high curvature generally helps avoid oscillations. Figure 1 and the left plot of Figure 2 confirm the superiority of NAG-SC over the heavy-ball method in this respect.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

If we can translate this argument to the discrete case we can understand why NAG-SC achieves acceleration globally for strongly convex functions but the heavy-ball method does not. We will be able to make this translation by leveraging the high-resolution ODEs to construct discrete-time Lyapunov functions that allow maximal step sizes to be characterized for the NAG-SC and the heavy-ball method. The detailed analyses is given in Section 3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Effect of gradient correction in gradient norm minimization. We will also show how to exploit the high-resolution ODE of NAG-C to construct a continuous-time Lyapunov function to analyze convergence in the setting of a smooth convex objective with $L$-Lipschitz gradients. Interestingly, the time derivative of the Lyapunov function is not only negative, but it is smaller than $- {O{({\sqrt{s}t^{2}{\|{{\nabla f}{(X)}}\|}^{2}})}}$. This bound arises from the gradient correction and, indeed, it cannot be obtained from the Lyapunov function studied in the low-resolution case. This finer characterization in the high-resolution case allows us to establish a new phenomenon: That is, we discover that NAG-C achieves an inverse *cubic* rate for minimizing the squared gradient norm.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

By comparison, from (1.6) and the $L$-Lipschitz continuity of $\nabla f$ we can only show that $\left\| {{\nabla f}{(x_{k})}} \right\|^{2} \leq {O\left({L^{2}/k^{2}} \right)}$. See Section 4 for further elaboration on this cubic rate for NAG-C.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

As we will see, the high-resolution ODEs are based on a phase-space representation that provides a systematic framework for translating from continuous-time Lyapunov functions to discrete-time Lyapunov functions. In sharp contrast, the process for obtaining a discrete-time Lyapunov function for low-resolution ODEs presented relies on "algebraic tricks" (see, for example, Theorem 6 of ). On a related note, a Hessian-driven damping term also appears in ODEs for modeling Newton's method.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Organization and Notation", "weight": 1.0} -->

The remainder of the paper is organized as follows. In Section 2, we briefly introduce our high-resolution ODE-based analysis framework. This framework is used in Section 3 to study the heavy-ball method and NAG-SC for smooth strongly convex functions. In Section 4, we turn our focus to NAG-C for a general smooth convex objective. In Section 5 we derive some extensions of NAG-C. We conclude the paper in Section 6 with a list of future research directions. Most technical proofs are deferred to the Appendix.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The High-Resolution ODE Framework", "weight": 1.0} -->

This section introduces a high-resolution ODE framework for analyzing gradient-based methods, with NAG-SC being a guiding example. Given a (discrete) optimization algorithm, the first step in this framework is to derive a high-resolution ODE using dimensional analysis, the next step is to construct a continuous-time Lyapunov function to analyze properties of the ODE, the third step is to derive a discrete-time Lyapunov function from its continuous counterpart and the last step is to translate properties of the ODE into that of the original algorithm. The overall framework is illustrated in Figure 3.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Step 1: Deriving High-Resolution ODEs", "weight": 1.0} -->

Our analysis is inspired by dimensional analysis, a strategy widely used in physics to construct a series of differential equations that involve increasingly high-order terms corresponding to small perturbations. In more detail, taking a small $s$, one first derives a differential equation that consists only of $O{}$ terms, then derives a differential equation consisting of both $O{}$ and $O{(\sqrt{s})}$, and next, one proceeds to obtain a differential equation consisting of ${O{}},{O{(\sqrt{s})}}$ and $O{(s)}$ terms. High-order terms in powers of $\sqrt{s}$ are introduced sequentially until the main characteristics of the original algorithms have been extracted from the resulting approximating differential equation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Step 1: Deriving High-Resolution ODEs", "weight": 1.0} -->

Thus, we aim to understand Nesterov acceleration by incorporating $O{(\sqrt{s})}$ terms into the ODE, including the (Hessian-driven) gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ which results from the (discrete) gradient correction (1.7) in the single-variable form (1.4) of NAG-SC. We also show (see Appendix A.1 for the detailed derivation) that this $O{(\sqrt{s})}$ term appears in the high-resolution ODE of NAG-C, but is not found in the high-resolution ODE of the heavy-ball method.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Step 1: Deriving High-Resolution ODEs", "weight": 1.0} -->

As shown below, each ODE admits a unique global solution under mild conditions on the objective, and this holds for an arbitrary step size $s > 0$. The solution is accurate in approximating its associated optimization method if $s$ is small. To state the result, we use $C^{2}{(I;{\mathbb{R}}^{n})}$ to denote the class of twice-continuously-differentiable maps from $I$ to ${\mathbb{R}}^{n}$ for $I = {\lbrack 0,\infty)}$ (the heavy-ball method and NAG-SC) and $I = {\lbrack{1.5\sqrt{s}},\infty)}$ (NAG-C).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Step 2: Analyzing ODEs Using Lyapunov Functions", "weight": 1.0} -->

With these high-resolution ODEs in place, the next step is to construct Lyapunov functions for analyzing the dynamics of the corresponding ODEs, as is done in previous work. For NAG-SC, we consider the Lyapunov function The first and second terms ${({1 + \sqrt{\mus}})}\left({{f{(X)}} - {f{(x^{\star})}}} \right)$ and $\frac{1}{4}{\|\overset{˙}{X}\|}^{2}$ can be regarded, respectively, as the potential energy and kinetic energy, and the last term is a mix.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Step 2: Analyzing ODEs Using Lyapunov Functions", "weight": 1.0} -->

The differentiability of $\mathcal{E}{(t)}$ will allow us to investigate properties of the ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) in a principled manner. For example, we will show that $\mathcal{E}{(t)}$ decreases exponentially along the trajectories of (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")), recovering the accelerated linear convergence rate of NAG-SC. Furthermore, a comparison between the Lyapunov function of NAG-SC and that of the heavy-ball method will explain why the gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ yields acceleration in the former case. This is discussed in Section 3.1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Step 3: Constructing Discrete Lyapunov Functions", "weight": 1.0} -->

Our framework make it possible to translate continuous Lyapunov functions into discrete Lyapunov functions via a phase-space representation (see, for example,). We illustrate the procedure in the case of NAG-SC. The first step is formulate explicit position and velocity updates: where the velocity variable $v_{k}$ is defined as: The initial velocity is $v_{0} = {- {\frac{2\sqrt{s}}{1 + \sqrt{\mus}}{\nabla f}{(x_{0})}}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Step 3: Constructing Discrete Lyapunov Functions", "weight": 1.0} -->

Interestingly, this phase-space representation has the flavor of symplectic discretization, in the sense that the update for $x_{k} - x_{k - 1}$ is explicit (it only depends on the last iterate $v_{k - 1}$) while the update for $v_{k} - v_{k - 1}$ is implicit (it depends on the current iterates $x_{k}$ and $v_{k}$)^88^8Although this suggestion is a heuristic one, it is also possible to rigorously derive a symplectic integrator of the high-resolution ODE of NAG-SC; this integrator has the form: ${x_{k} - x_{k - 1}} = {\sqrt{s}v_{k - 1}}$ ${{v_{k} - v_{k - 1}} = {{- {2\sqrt{\mus}v_{k}}} -

<!-- chunk {"id": "body-0038", "role": "body", "section": "Step 4: Analyzing Algorithms Using Discrete Lyapunov Functions", "weight": 1.0} -->

The last step is to map properties of high-resolution ODEs to corresponding properties of optimization methods. This step closely mimics Step 2 except that now the object is a discrete algorithm and the tool is a discrete Lyapunov function such as (2.6). Given that Step 2 has been performed, this translation is conceptually straightforward, albeit often calculation-intensive. For example, using the discrete Lyapunov function (2.6), we will recover the optimal linear rate of NAG-SC and gain insights into the fundamental effect of the gradient correction in accelerating NAG-SC. In addition, NAG-C is shown to minimize the squared gradient norm at an inverse cubic rate by a simple analysis of the decreasing rate of its discrete Lyapunov function.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Gradient Correction for Acceleration", "weight": 1.0} -->

In this section, we use our high-resolution ODE framework to analyze NAG-SC and the heavy-ball method. Section 3.1 focuses on the ODEs with an objective function $f \in {\mathcal{S}_{\mu,L}^{2}{({\mathbb{R}}^{n})}}$, and in Section 3.2 we extend the results to the discrete case for $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$. Finally, in Section 3.3 we offer a comparative study of NAG-SC and the heavy-ball method from a finite-difference viewpoint.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Gradient Correction for Acceleration", "weight": 1.0} -->

Throughout this section, the strategy is to analyze the two methods in parallel, thereby highlighting the differences between the two methods. In particular, the comparison will demonstrate the vital role of the gradient correction, namely ${\frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}} \cdot s}\left( {{{\nabla f}{(x_{k})}} - {{\nabla f}{(x_{k - 1})}}} \right)$ in the discrete case and $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in the ODE case, in making NAG-SC an accelerated method.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The ODE Case", "weight": 1.0} -->

The following theorem characterizes the convergence rate of the high-resolution ODE corresponding to NAG-SC.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

The only inequality in (3.4) is due to the term $\frac{\sqrt{s}}{2}{({\left\| {{\nabla f}{(X)}} \right\|^{2} + {{\overset{˙}{X}}^{\top}{\nabla^{2}f}{(X)}\overset{˙}{X}}})}$, which is discussed right after the statement of Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). This term results from the gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in the NAG-SC ODE. For comparison, this term does not appear in Lemma 3.2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") in the case of the heavy-ball method as its ODE does not include the gradient correction and, accordingly, its Lyapunov function (3.3) is free of the $\sqrt{s}{\nabla f}{(X)}$ term.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Discrete Case", "weight": 1.0} -->

This section carries over the results in Section 3.1 to the two discrete algorithms, namely NAG-SC and the heavy-ball method. Here we consider an objective $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$ since second-order differentiability of $f$ is not required in the two discrete methods. Recall that both methods start with an arbitrary $x_{0}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Stability Perspective on Acceleration", "weight": 1.0} -->

As shown in Section 3.2, the gradient correction is the fundamental cause of the difference in convergence rates between the heavy-ball method and NAG-SC. This section aims to further elucidate this distinction from the viewpoint of numerical stability. A numerical scheme is said to be stable if, roughly speaking, this scheme does not magnify errors in the input data. Accordingly, we address the question of what values of the step size $s$ are allowed for solving the high-resolution ODEs (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) and (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) in a stable fashion. While various discretization schemes on low-resolution ODEs have been explored, we limit our attention to the forward Euler scheme to simplify the discussion (see for an exposition on discretization schemes).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical Stability Perspective on Acceleration", "weight": 1.0} -->

For the heavy-ball method, the forward Euler scheme applied to (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) is Using the approximation ${{\nabla f}{({{X{({t - \sqrt{s}})}} + \epsilon})}} \approx {{{\nabla f}{({X{({t - \sqrt{s}})}})}} + {{\nabla^{2}f}{({X{({t - \sqrt{s}})}})}\epsilon}}$ for a small perturbation $\epsilon$, we get the characteristic equation of (3.17): where $\mathbf{I}$ denotes the $n \times n$ identity matrix. The numerical stability of (3.17) requires the roots of the characteristic equation to be no larger than one in absolute value.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Stability Perspective on Acceleration", "weight": 1.0} -->

Therefore, a necessary condition for the stability is that^1010^10The notation $A \preceq B$ indicates that $B - A$ is positive semidefinite for symmetric matrices $A$ and $B$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Stability Perspective on Acceleration", "weight": 1.0} -->

By the $L$-smoothness of $f$, the largest singular value of ${\nabla^{2}f}{({X{({t - \sqrt{s}})}})}$ can be as large as $L$. Therefore, (3.18) is guaranteed in the worst case analysis only if which shows that the step size must obey Next, we turn to the high-resolution ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-SC, for which the forward Euler scheme reads Its characteristic equation is which, as earlier, suggests that the numerical stability condition of (3.20) is This inequality is ensured by setting the step size As constraints on the step sizes, both (3.19) and (3.21) are in agreement with the discussion in Section 3.2, albeit from a different perspective.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical Stability Perspective on Acceleration", "weight": 1.0} -->

In short, a comparison between (3.17) and (3.20) reveals that the Hessian $\sqrt{s}{\nabla^{2}f}{({X{({t - \sqrt{s}})}})}$ makes the forward Euler scheme for the NAG-SC ODE numerically stable with a larger step size, namely $s = {O{({1/L})}}$. This is yet another reflection of the vital importance of the gradient correction in yielding acceleration for NAG-SC.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Gradient Correction for Gradient Norm Minimization", "weight": 1.0} -->

In this section, we extend the use of the high-resolution ODE framework to NAG-C (1.5) in the setting of minimizing an $L$-smooth convex function $f$. The main result is an improved rate of NAG-SC for minimizing the squared gradient norm. Indeed, we show that NAG-C achieves the $O{({L^{2}/k^{3}})}$ rate of convergence for minimizing ${\|{{\nabla f}{(x_{k})}}\|}^{2}$. To the best of our knowledge, this is the sharpest known bound for this problem using NAG-C without any modification. Moreover, we will show that the gradient correction in NAG-C is responsible for this rate and, as it is therefore unsurprising that this inverse cubic rate was not perceived within the low-resolution ODE frameworks such as that of.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Gradient Correction for Gradient Norm Minimization", "weight": 1.0} -->

In Section 4.3, we propose a new accelerated method with the same rate $O{({L^{2}/k^{3}})}$ and briefly discuss the benefit of the phase-space representation in simplifying technical proofs.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The ODE Case", "weight": 1.0} -->

We begin by studying the high-resolution ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) corresponding to NAG-C with an objective $f \in {\mathcal{F}_{L}^{2}{({\mathbb{R}}^{n})}}$ and an arbitrary step size $s > 0$. For convenience, let $t_{0} = {1.5\sqrt{s}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "The Discrete Case", "weight": 1.0} -->

We now turn to the discrete NAG-C (1.5) for minimizing an objective $f \in {\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}}$. Recall that this algorithm starts from any $x_{0}$ and $y_{0} = x_{0}$. The discrete counterpart of Theorem 5 is as follows.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Modified NAG-C without a Phase-Space Representation", "weight": 1.0} -->

This section proposes a new accelerated method that also achieves the $O{({L^{2}/k^{3}})}$ rate for minimizing the squared gradient norm. This method takes the following form: starting with $x_{0}$ and $y_{0} = x_{0}$. As shown by the following theorem, this new method has the same convergence rates as NAG-C.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Extensions", "weight": 1.0} -->

Motivated by the high-resolution ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-C, this section considers a family of generalized high-resolution ODEs that take the form for $t \geq {{\alpha\sqrt{s}}/2}$, with initial conditions ${X{({{\alpha\sqrt{s}}/2})}} = x_{0}$ and ${\overset{˙}{X}{({{\alpha\sqrt{s}}/2})}} = {- {\sqrt{s}{\nabla f}{(x_{0})}}}$. As demonstrated, the low-resolution counterpart (that is, set $s = 0$) of (5.1) achieves acceleration if and only if $\alpha \geq 3$. Accordingly, we focus on the case where the friction parameter $\alpha \geq 3$ and the gradient correction parameter $\beta > 0$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Extensions", "weight": 1.0} -->

An investigation of the case of $\alpha < 3$ is left for future work.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Extensions", "weight": 1.0} -->

By discretizing the ODE (5.1), we obtain a family of new accelerated methods for minimizing smooth convex functions: starting with $x_{0} = y_{0}$. The second line of the iteration is equivalent to In Section 5.1, we study the convergence rates of this family of generalized NAC-C algorithms along the lines of Section 4. To further our understanding of (5.2), Section 5.2 shows that this method in the super-critical regime (that is, $\alpha > 3$) converges to the optimum actually faster than $O{({1/{({sk^{2}})}})}$. As earlier, the proofs of all the results follow the high-resolution ODE framework introduced in Section 2. Proofs are deferred to Appendix D. Finally, we note that Section 6 briefly sketches the extensions along this direction for NAG-SC.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Convergence Rates", "weight": 1.0} -->

The theorem below characterizes the convergence rates of the generalized NAG-C (5.2).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Faster Convergence in Super-Critical Regime", "weight": 1.0} -->

We turn to the case in which $\alpha > 3$, where we show that the generalized NAG-C in this regime attains a faster rate for minimizing the function value. The following proposition provides a technical inequality that motivates the derivation of the improved rate.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we have proposed high-resolution ODEs for modeling three first-order optimization methods---the heavy-ball method, NAG-SC, and NAG-C. These new ODEs are more faithful surrogates for the corresponding discrete optimization methods than existing ODEs in the literature, thus serving as a more effective tool for understanding, analyzing, and generalizing first-order methods. Using this tool, we identified a term that we refer to as "gradient correction" in NAG-SC and in its high-resolution ODE, and we demonstrate its critical effect in making NAG-SC an accelerated method, as compared to the heavy-ball method. We also showed via the high-resolution ODE of NAG-C that this method minimizes the squared norm of the gradient at a faster rate than expected for smooth convex functions, and again the gradient correction is the key to this rate. Finally, the analysis of this tool suggested a new family of accelerated methods with the same optimal convergence rates as NAG-C.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion", "weight": 1.5} -->

The aforementioned results are obtained using the high-resolution ODEs in conjunction with a new framework for translating findings concerning the amenable ODEs into those of the less "user-friendly" discrete methods. This framework encodes an optimization property under investigation to a continuous-time Lyapunov function for an ODE and a discrete-time Lyapunov function for the discrete method. As an appealing feature of this framework, the transformation from the continuous Lyapunov function to its discrete version is through a phase-space representation. This representation links continuous objects such as position and velocity variables to their discrete counterparts in a faithful manner, permitting a transparent analysis of the three discrete methods that we studied.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion", "weight": 1.5} -->

There are a number of avenues open for future research using the high-resolution ODE framework. First, the discussion of Section 5 can carry over to the heavy-ball method and NAG-SC, which correspond to the high-resolution ODE with $\beta = 0$ and $\beta = 1$, respectively. This ODE with a general $0 < \beta < 1$ corresponds to a new algorithm that can be thought of as an interpolation between the two methods. It is of interest to investigate the convergence properties of this class of algorithms. Second, we recognize that new optimization algorithms are obtained in by using different discretization schemes on low-resolution ODE. Hence, a direction of interest is to apply the techniques therein to our high-resolution ODEs and to explore possible appealing properties of the new methods. Third, the technique of dimensional analysis, which we have used to derive high-resolution ODEs, can be further used to incorporate even higher-order powers of $\sqrt{s}$ into the ODEs. This might lead to further fine-grained findings concerning the discrete methods.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion", "weight": 1.5} -->

More broadly, we wish to remark on possible extensions of the high-resolution ODE framework beyond smooth convex optimization in the Euclidean setting. In the non-Euclidean case, it would be interesting to derive a high-resolution ODE for mirror descent. This framework might also admit extensions to non-smooth optimization and stochastic optimization, where the ODEs are replaced, respectively, by differential inclusions \[ORX^+^16, \] and stochastic differential equations \[ HMC^+^18, \]. Finally, recognizing that the high-resolution ODEs are well-defined for non-convex functions, we believe that this framework will provide more accurate characterization of local behaviors of first-order algorithms near saddle points \[JGN^+^17, DJL^+^17, \]. On a related note, given the centrality of the problem of finding an approximate stationary point in the non-convex setting, it is worth using the high-resolution ODE framework to explore possible applications of the faster rate for minimizing the squared gradient norm that we have uncovered.
