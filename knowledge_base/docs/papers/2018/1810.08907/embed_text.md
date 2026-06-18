## Introduction

Machine learning has become one of the major application areas for optimization algorithms during the past decade. While there have been many kinds of applications, to a wide variety of problems, the most prominent applications have involved large-scale problems in which the objective function is the sum over terms associated with individual data, such that stochastic gradients can be computed cheaply, while gradients are much more expensive and the computation (and/or storage) of Hessians is often infeasible. In this setting, simple first-order gradient descent algorithms have become dominant, and the effort to make these algorithms applicable to a broad range of machine learning problems has triggered a flurry of new research in optimization, both methodological and theoretical.

We will be considering unconstrained minimization problems,

where $f$ is a smooth convex function. Perhaps the simplest first-order method for solving this problem is gradient descent. Taking a fixed step size $s$, gradient descent is implemented as the recursive rule

given an initial point $x_{0}$.

As has been known at least since the advent of conjugate gradient algorithms, improvements to gradient descent can be obtained within a first-order framework by using the history of past gradients. Modern research on such extended first-order methods arguably dates to Polyak \[, \], whose *heavy-ball method* incorporates a momentum term into the gradient step. This approach allows past gradients to influence the current step, while avoiding the complexities of conjugate gradients and permitting a stronger theoretical analysis. Explicitly, starting from an initial point ${x_{0},x_{1}} \in {\mathbb{R}}^{n}$, the heavy-ball method updates the iterates according to

where $\alpha > 0$ is the momentum coefficient. While the heavy-ball method provably attains a faster rate of *local* convergence than gradient descent near a minimum of $f$, it does not come with *global* guarantees. Indeed, \[\] demonstrate that even for strongly convex functions the method can fail to converge for some choices of the step size.^11^1\[\] considers $s = {4/{({\sqrt{L} + \sqrt{\mu}})}^{2}}$ and $\alpha = {({1 - \sqrt{\mus}})}^{2}$. This momentum coefficient is basically the same as the choice $\alpha = \frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$ (adopted starting from Section 1.1) if $s$ is small.

The next major development in first-order methodology was due to Nesterov, who discovered a class of *accelerated gradient methods* that have a faster global convergence rate than gradient descent \[, \]. For a $\mu$-strongly convex objective $f$ with $L$-Lipschitz gradients, Nesterov's accelerated gradient method (NAG-SC) involves the following pair of update equations:

given an initial point $x_{0} = y_{0} \in {\mathbb{R}}^{n}$. Equivalently, NAG-SC can be written in a single-variable form that is similar to the heavy-ball method:

starting from $x_{0}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$. Like the heavy-ball method, NAG-SC blends gradient and momentum contributions into its update direction, but defines a specific momentum coefficient $\frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$. Nesterov also developed the *estimate sequence technique* to prove that NAG-SC achieves an accelerated linear convergence rate:

if the step size satisfies $0 < s \leq {1/L}$. Moreover, for a (weakly) convex objective $f$ with $L$-Lipschitz gradients, Nesterov defined a related accelerated gradient method (NAG-C), that takes the following form:

with $x_{0} = y_{0} \in {\mathbb{R}}^{n}$. The choice of momentum coefficient $\frac{k}{k + 3}$, which tends to one, is fundamental to the estimate-sequence-based argument used by Nesterov to establish the following inverse quadratic convergence rate:

for any step size $s \leq {1/L}$. Under an oracle model of optimization complexity, the convergence rates achieved by NAG-SC and NAG-C are optimal for smooth strongly convex functions and smooth convex functions, respectively \[\].

### Gradient Correction: Small but Essential

Throughout the present paper, we let $\alpha = \frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$ to define a specific implementation of the heavy-ball method in (1.2). This choice of the momentum coefficient and the second initial point renders the heavy-ball method and NAG-SC identical except for the last (small) term in (1.4). Despite their close resemblance, however, the two methods are in fact fundamentally different, with contrasting convergence results (see, for example, \[\]). Notably, the former algorithm in general only achieves *local* acceleration, while the latter achieves acceleration method for all initial values of the iterate \[\]. As a numerical illustration, Figure 1 presents the trajectories that arise from the two methods when minimizing an ill-conditioned convex quadratic function. We see that the heavy-ball method exhibits pronounced oscillations throughout the iterations, whereas NAG-SC is monotone in the function value once the iteration counter exceeds $50$.

This striking difference between the two methods can only be attributed to the last term in (1.4):

which we refer to henceforth as the gradient correction^22^2The gradient correction for NAG-C is ${\frac{k}{k + 3} \cdot s}{({{{\nabla f}{(x_{k})}} - {{\nabla f}{(x_{k - 1})}}})}$, as seen from the single-variable form of NAG-C: $x_{k + 1} = {{x_{k} + {\frac{k}{k + 3}{({x_{k} - x_{k - 1}})}}} - {s{\nabla f}{(x_{k})}} - {{\frac{k}{k + 3} \cdot s}{({{{\nabla f}{(x_{k})}} - {{\nabla f}{(x_{k - 1})}}})}}}$.. This term corrects the update direction in NAG-SC by contrasting the gradients at consecutive iterates. Although an essential ingredient in NAG-SC, the effect of the gradient correction is unclear from the vantage point of the estimate-sequence technique used in Nesterov's proof. Accordingly, while the estimate-sequence technique delivers a proof of acceleration for NAG-SC, it does not explain why the absence of the gradient correction prevents the heavy-ball method from achieving acceleration for strongly convex functions.

Figure 1: A numerical comparison between NAG-SC and heavy-ball method. The objective function (ill-conditioned μ/L ≪ 1) is f (x1,x2) = 5 × 10−3 x12 + x22, with the initial iterate.

A recent line of research has taken a different point of view on the theoretical analysis of acceleration, formulating the problem in continuous time and obtaining algorithms via discretization \[ \]). This can be done by taking continuous-time limits of existing algorithms to obtain ordinary differential equations (ODEs) that can be analyzed using the rich toolbox associated with ODEs, including Lyapunov functions^33^3One can think of the Lyapunov function as a generalization of the idea of the energy of a system. Then the method studies stability by looking at the rate of change of this measure of energy.. For instance, \[\] shows that

with initial conditions ${X{}} = x_{0}$ and ${\overset{˙}{X}{}} = 0$, is the exact limit of NAG-C (1.5) by taking the step size $s\rightarrow 0$. Alternatively, the starting point may be a Lagrangian or Hamiltonian framework \[\]. In either case, the continuous-time perspective not only provides analytical power and intuition, but it also provides design tools for new accelerated algorithms.

Unfortunately, existing continuous-time formulations of acceleration stop short of differentiating between the heavy-ball method and NAG-SC. In particular, these two methods have the same limiting ODE (see, for example, \[\]):

and, as a consequence, this ODE does not provide any insight into the stronger convergence results for NAG-SC as compared to the heavy-ball method. As will be shown in Section 2, this is because the gradient correction ${\frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}s\left( {{{\nabla f}{(x_{k})}} - {{\nabla f}{(x_{k - 1})}}} \right)} = {O{(s^{1.5})}}$ is an order-of-magnitude smaller than the other terms in (1.4) if $s = {o{}}$. Consequently, the gradient correction is not reflected in the low-resolution ODE (1.9) associated with NAG-SC, which is derived by simply taking $s\rightarrow 0$ in both (1.2) and (1.4).

### Overview of Contributions

Just as there is not a singled preferred way to discretize a differential equation, there is not a single preferred way to take a continuous-time limit of a difference equation. Inspired by dimensional-analysis strategies widely used in fluid mechanics in which physical phenomena are investigated at multiple scales via the inclusion of various orders of perturbations \[\], we propose to incorporate $O{(\sqrt{s})}$ terms into the limiting process for obtaining an ODE, including the (Hessian-driven) gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in (1.7). This will yield *high-resolution ODEs* that differentiate between the NAG methods and the heavy-ball method.

We list the high-resolution ODEs that we derive in the paper here^44^4We note that the form of the initial conditions is fixed for each ODE throughout the paper. For example, while $x_{0}$ is arbitrary, $X{}$ and $\overset{˙}{X}{}$ must always be equal to $x_{0}$ and $- {{2\sqrt{s}f{(x_{0})}}/{({1 + \sqrt{\mus}})}}$ respectively in the high-resolution ODE of the heavy-ball method. This is in accordance with the choice of $\alpha = \frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$.:

The high-resolution ODE for the heavy-ball method (1.2):

with ${X{}} = x_{0}$ and ${\overset{˙}{X}{}} = {- \frac{2\sqrt{s}{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$.

The high-resolution ODE for NAG-SC (1.3):

with ${X{}} = x_{0}$ and ${\overset{˙}{X}{}} = {- \frac{2\sqrt{s}{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$.

The high-resolution ODE for NAG-C (1.5):

High-resolution ODEs are more accurate continuous-time counterparts for the corresponding discrete algorithms than low-resolution ODEs, thus allowing for a better characterization of the accelerated methods. This is illustrated in Figure 2, which presents trajectories and convergence of the discrete methods, and the low- and high-resolution ODEs. For both NAGs, the high-resolution ODEs are in much better agreement with the discrete methods than the low-resolution ODEs^55^5Note that for the heavy-ball method, the trajectories of the high-resolution ODE and the low-resolution ODE are almost identical.. Moreover, for NAG-SC, its high-resolution ODE captures the non-oscillation pattern while the low-resolution ODE does not.

Figure 2: Top left and bottom left: trajectories and errors of NAG-SC and the heavy-ball method for minimizing f (x1,x2) = 5 × 10−3 x12 + x22, from the initial value, the same setting as Figure 1. Top right and bottom right: trajectories and errors of NAG-C for minimizing f (x1,x2) = 2 × 10−2 x12 + 5 × 10−3 x22, from the initial value. For the two bottom plots, we use the identification $t = {k\sqrt{s}}$ between time and iterations for the x-axis.

The three new ODEs include $O{(\sqrt{s})}$ terms that are not present in the corresponding low-resolution ODEs (compare, for example, (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) and (1.8)). Note also that if we let $s\rightarrow 0$, each high-resolution ODE reduces to its low-resolution counterpart. Thus, the difference between the heavy-ball method and NAG-SC is reflected only in their high-resolution ODEs: the gradient correction (1.7) of NAG-SC is preserved only in its high-resolution ODE in the form $\sqrt{s}{\nabla^{2}f}{({X{(t)}})}\overset{˙}{X}{(t)}$. This term, which we refer to as the (Hessian-driven) gradient correction, is connected with the discrete gradient correction by the approximate identity:

for small $s$, with the identification $t = {k\sqrt{s}}$. The gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in NAG-C arises in the same fashion^66^6Henceforth, the dependence of $X$ on $t$ is suppressed when clear from the context.. Interestingly, although both NAGs are first-order methods, their gradient corrections brings in second-order information from the objective function.

Despite being small, the gradient correction has a fundamental effect on the behavior of both NAGs, and this effect is revealed by inspection of the high-resolution ODEs. We provide two illustrations of this.

Effect of the gradient correction in acceleration. Viewing the coefficient of $\overset{˙}{X}$ as a damping ratio, the ratio ${2\sqrt{\mu}} + {\sqrt{s}{\nabla^{2}f}{(X)}}$ of $\overset{˙}{X}$ in the high-resolution ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-SC is adaptive to the position $X$, in contrast to the fixed damping ratio $2\sqrt{\mu}$ in the ODE (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) for the heavy-ball method. To appreciate the effect of this adaptivity, imagine that the velocity $\overset{˙}{X}$ is highly correlated with an eigenvector of ${\nabla^{2}f}{(X)}$ with a large eigenvalue, such that the large friction ${({{2\sqrt{\mu}} + {\sqrt{s}{\nabla^{2}f}{(X)}}})}\overset{˙}{X}$ effectively "decelerates" along the trajectory of the ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-SC. This feature of NAG-SC is appealing as taking a cautious step in the presence of high curvature generally helps avoid oscillations. Figure 1 and the left plot of Figure 2 confirm the superiority of NAG-SC over the heavy-ball method in this respect.

If we can translate this argument to the discrete case we can understand why NAG-SC achieves acceleration globally for strongly convex functions but the heavy-ball method does not. We will be able to make this translation by leveraging the high-resolution ODEs to construct discrete-time Lyapunov functions that allow maximal step sizes to be characterized for the NAG-SC and the heavy-ball method. The detailed analyses is given in Section 3.

Effect of gradient correction in gradient norm minimization. We will also show how to exploit the high-resolution ODE of NAG-C to construct a continuous-time Lyapunov function to analyze convergence in the setting of a smooth convex objective with $L$-Lipschitz gradients. Interestingly, the time derivative of the Lyapunov function is not only negative, but it is smaller than $- {O{({\sqrt{s}t^{2}{\|{{\nabla f}{(X)}}\|}^{2}})}}$. This bound arises from the gradient correction and, indeed, it cannot be obtained from the Lyapunov function studied in the low-resolution case by \[\]. This finer characterization in the high-resolution case allows us to establish a new phenomenon:

That is, we discover that NAG-C achieves an inverse *cubic* rate for minimizing the squared gradient norm. By comparison, from (1.6) and the $L$-Lipschitz continuity of $\nabla f$ we can only show that $\left\| {{\nabla f}{(x_{k})}} \right\|^{2} \leq {O\left( {L^{2}/k^{2}} \right)}$. See Section 4 for further elaboration on this cubic rate for NAG-C.

As we will see, the high-resolution ODEs are based on a phase-space representation that provides a systematic framework for translating from continuous-time Lyapunov functions to discrete-time Lyapunov functions. In sharp contrast, the process for obtaining a discrete-time Lyapunov function for low-resolution ODEs presented by \[\] relies on "algebraic tricks" (see, for example, Theorem 6 of \[\]). On a related note, a Hessian-driven damping term also appears in ODEs for modeling Newton's method \[ \].

### Related Work

There is a long history of using ODEs to analyze optimization methods \[ \]. Recently, the work of \[, \] has sparked a renewed interest in leveraging continuous dynamical systems to understand and design first-order methods and to provide more intuitive proofs for the discrete methods. Below is a rather incomplete review of recent work that uses continuous-time dynamical systems to study accelerated methods.

In the work of \[ \], Lagrangian and Hamiltonian frameworks are used to generate a large class of continuous-time ODEs for a unified treatment of accelerated gradient-based methods. Indeed, \[\] extend NAG-C to non-Euclidean settings, mirror descent and accelerated higher-order gradient methods, all from a single "Bregman Lagrangian." In \[\], the connection between ODEs and discrete algorithms is further strengthened by establishing an equivalence between the estimate sequence technique and Lyapunov function techniques, allowing for a principled analysis of the discretization of continuous-time ODEs. Recent papers have considered symplectic \[\] and Runge--Kutta \[\] schemes for discretization of the low-resolution ODEs.

An ODE-based analysis of mirror descent has been pursued in another line of work by \[ \], delivering new connections between acceleration and constrained optimization, averaging and stochastic mirror descent.

In addition to the perspective of continuous-time dynamical systems, there has also been work on the acceleration from a control-theoretic point of view \[ \] and from a geometric point of view \[, \]. See also \[ \] for a number of other recent contributions to the study of the acceleration phenomenon.

### Organization and Notation

The remainder of the paper is organized as follows. In Section 2, we briefly introduce our high-resolution ODE-based analysis framework. This framework is used in Section 3 to study the heavy-ball method and NAG-SC for smooth strongly convex functions. In Section 4, we turn our focus to NAG-C for a general smooth convex objective. In Section 5 we derive some extensions of NAG-C. We conclude the paper in Section 6 with a list of future research directions. Most technical proofs are deferred to the Appendix.

We mostly follow the notation of \[\], with slight modifications tailored to the present paper. Let $\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}$ be the class of $L$-smooth convex functions defined on ${\mathbb{R}}^{n}$; that is, $f \in \mathcal{F}_{L}^{1}$ if ${f{(y)}} \geq {{f{(x)}} + \left\langle {{\nabla f}{(x)}},{y - x} \right\rangle}$ for all ${x,y} \in {\mathbb{R}}^{n}$ and its gradient is $L$-Lipschitz continuous in the sense that

where $\parallel \cdot \parallel$ denotes the standard Euclidean norm and $L > 0$ is the Lipschitz constant. (Note that this implies that $\nabla f$ is also $L^{\prime}$-Lipschitz for any $L^{\prime} \geq L$.) The function class $\mathcal{F}_{L}^{2}{({\mathbb{R}}^{n})}$ is the subclass of $\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}$ such that each $f$ has a Lipschitz-continuous Hessian. For $p = {1,2}$, let $\mathcal{S}_{\mu,L}^{p}{({\mathbb{R}}^{n})}$ denote the subclass of $\mathcal{F}_{L}^{p}{({\mathbb{R}}^{n})}$ such that each member $f$ is $\mu$-strongly convex for some $0 < \mu \leq L$. That is, $f \in {\mathcal{S}_{\mu,L}^{p}{({\mathbb{R}}^{n})}}$ if $f \in {\mathcal{F}_{L}^{p}{({\mathbb{R}}^{n})}}$ and

for all ${x,y} \in {\mathbb{R}}^{n}$. Note that this is equivalent to the convexity of ${f{(x)}} - {\frac{\mu}{2}{\|{x - x^{\star}}\|}^{2}}$, where $x^{\star}$ denotes a minimizer of the objective $f$.

## The High-Resolution ODE Framework

This section introduces a high-resolution ODE framework for analyzing gradient-based methods, with NAG-SC being a guiding example. Given a (discrete) optimization algorithm, the first step in this framework is to derive a high-resolution ODE using dimensional analysis, the next step is to construct a continuous-time Lyapunov function to analyze properties of the ODE, the third step is to derive a discrete-time Lyapunov function from its continuous counterpart and the last step is to translate properties of the ODE into that of the original algorithm. The overall framework is illustrated in Figure 3.

Figure 3: An illustration of our high-resolution ODE framework. The three solid straight lines represent Steps 1, 2 and 3, and the two curved lines denote Step 4. The dashed line is used to emphasize that it is difficult, if not impractical, to construct discrete Lyapunov functions directly from the algorithms.

### Step 1: Deriving High-Resolution ODEs

Our focus is on the single-variable form (1.4) of NAG-SC. For any nonnegative integer $k$, let $t_{k} = {k\sqrt{s}}$ and assume $x_{k} = {X{(t_{k})}}$ for some sufficiently smooth curve $X{(t)}$. Performing a Taylor expansion in powers of $\sqrt{s}$, we get

We now use a Taylor expansion for the gradient correction, which gives

Multiplying both sides of (1.4) by $\frac{1 + \sqrt{\mus}}{1 - \sqrt{\mus}} \cdot \frac{1}{s}$ and rearranging the equality, we can rewrite NAG-SC as

Next, plugging (2.1) and (2.2) into (2.3), we have^77^7Note that we use the approximation $\frac{{x_{k + 1} + x_{k - 1}} - {2x_{k}}}{s} = {{\overset{¨}{X}{(t_{k})}} + {O{(s)}}}$, whereas \[\] relies on the low-accuracy Taylor expansion $\frac{{x_{k + 1} + x_{k - 1}} - {2x_{k}}}{s} = {{\overset{¨}{X}{(t_{k})}} + {o{}}}$ in the derivation of the low-resolution ODE of NAG-C. We illustrate this derivation of the three low-resolution ODEs in Appendix A.2; they can be compared to the high-resolution ODEs that we derive here.

which can be rewritten as

Multiplying both sides of the last display by $1 - \sqrt{\mus}$, we obtain the following high-resolution ODE of NAG-SC:

where we ignore any $O{(s)}$ terms but retain the $O{(\sqrt{s})}$ terms (note that ${{({1 - \sqrt{\mus}})}\sqrt{s}} = {\sqrt{s} + {O{(s)}}}$).

Our analysis is inspired by dimensional analysis \[\], a strategy widely used in physics to construct a series of differential equations that involve increasingly high-order terms corresponding to small perturbations. In more detail, taking a small $s$, one first derives a differential equation that consists only of $O{}$ terms, then derives a differential equation consisting of both $O{}$ and $O{(\sqrt{s})}$, and next, one proceeds to obtain a differential equation consisting of ${O{}},{O{(\sqrt{s})}}$ and $O{(s)}$ terms. High-order terms in powers of $\sqrt{s}$ are introduced sequentially until the main characteristics of the original algorithms have been extracted from the resulting approximating differential equation. Thus, we aim to understand Nesterov acceleration by incorporating $O{(\sqrt{s})}$ terms into the ODE, including the (Hessian-driven) gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ which results from the (discrete) gradient correction (1.7) in the single-variable form (1.4) of NAG-SC. We also show (see Appendix A.1 for the detailed derivation) that this $O{(\sqrt{s})}$ term appears in the high-resolution ODE of NAG-C, but is not found in the high-resolution ODE of the heavy-ball method.

As shown below, each ODE admits a unique global solution under mild conditions on the objective, and this holds for an arbitrary step size $s > 0$. The solution is accurate in approximating its associated optimization method if $s$ is small. To state the result, we use $C^{2}{(I;{\mathbb{R}}^{n})}$ to denote the class of twice-continuously-differentiable maps from $I$ to ${\mathbb{R}}^{n}$ for $I = {\lbrack 0,\infty)}$ (the heavy-ball method and NAG-SC) and $I = {\lbrack{1.5\sqrt{s}},\infty)}$ (NAG-C).

### Proposition 2.1

For any $f \in {\mathcal{S}_{\mu}^{2}{({\mathbb{R}}^{n})}}:={\cup_{L \geq \mu}{\mathcal{S}_{\mu,L}^{2}{({\mathbb{R}}^{n})}}}$, each of the ODEs (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) and (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) with the specified initial conditions has a unique global solution $X \in {C^{2}{({\lbrack 0,\infty)};{\mathbb{R}}^{n})}}$. Moreover, the two methods converge to their high-resolution ODEs, respectively, in the sense that

for any fixed $T > 0$.

In fact, Proposititon 2.1 holds for $T = \infty$ because both the discrete iterates and the ODE trajectories converge to the unique minimizer when the objective is stongly convex.

### Proposition 2.2

For any $f \in {\mathcal{F}^{2}{({\mathbb{R}}^{n})}}:={\cup_{L > 0}{\mathcal{F}_{L}^{2}{({\mathbb{R}}^{n})}}}$, the ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) with the specified initial conditions has a unique global solution $X \in {C^{2}{({\lbrack{1.5\sqrt{s}},\infty)};{\mathbb{R}}^{n})}}$. Moreover, NAG-C converges to its high-resolution ODE in the sense that

for any fixed $T > 0$.

The proofs of these propositions are given in Appendix A.3.1 and Appendix A.3.2.

### Step 2: Analyzing ODEs Using Lyapunov Functions

With these high-resolution ODEs in place, the next step is to construct Lyapunov functions for analyzing the dynamics of the corresponding ODEs, as is done in previous work \[ \]. For NAG-SC, we consider the Lyapunov function

The first and second terms ${({1 + \sqrt{\mus}})}\left( {{f{(X)}} - {f{(x^{\star})}}} \right)$ and $\frac{1}{4}{\|\overset{˙}{X}\|}^{2}$ can be regarded, respectively, as the potential energy and kinetic energy, and the last term is a mix. For the mixed term, it is interesting to note that the time derivative of $\overset{˙}{X} + {2\sqrt{\mu}{({X - x^{\star}})}} + {\sqrt{s}{\nabla f}{(X)}}$ equals $- {{({1 + \sqrt{\mus}})}{\nabla f}{(X)}}$.

The differentiability of $\mathcal{E}{(t)}$ will allow us to investigate properties of the ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) in a principled manner. For example, we will show that $\mathcal{E}{(t)}$ decreases exponentially along the trajectories of (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")), recovering the accelerated linear convergence rate of NAG-SC. Furthermore, a comparison between the Lyapunov function of NAG-SC and that of the heavy-ball method will explain why the gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ yields acceleration in the former case. This is discussed in Section 3.1.

### Step 3: Constructing Discrete Lyapunov Functions

Our framework make it possible to translate continuous Lyapunov functions into discrete Lyapunov functions via a phase-space representation (see, for example, \[\]). We illustrate the procedure in the case of NAG-SC. The first step is formulate explicit position and velocity updates:

where the velocity variable $v_{k}$ is defined as:

The initial velocity is $v_{0} = {- {\frac{2\sqrt{s}}{1 + \sqrt{\mus}}{\nabla f}{(x_{0})}}}$. Interestingly, this phase-space representation has the flavor of symplectic discretization, in the sense that the update for $x_{k} - x_{k - 1}$ is explicit (it only depends on the last iterate $v_{k - 1}$) while the update for $v_{k} - v_{k - 1}$ is implicit (it depends on the current iterates $x_{k}$ and $v_{k}$)^88^8Although this suggestion is a heuristic one, it is also possible to rigorously derive a symplectic integrator of the high-resolution ODE of NAG-SC; this integrator has the form: ${x_{k} - x_{k - 1}} = {\sqrt{s}v_{k - 1}}$ ${{v_{k} - v_{k - 1}} = {{- {2\sqrt{\mus}v_{k}}} - {s{\nabla^{2}f}{(x_{k})}v_{k}} - {{({1 + \sqrt{\mus}})}\sqrt{s}{\nabla f}{(x_{k})}}}}.$.

The representation (2.5) suggests translating the continuous-time Lyapunov function (2.4) into a discrete-time Lyapunov function of the following form:

by replacing continuous terms (e.g., $\overset{˙}{X}$) by their discrete counterparts (e.g., $v_{k}$). Akin to the continuous (2.4), here $\mathbf{I}$, $\mathbf{I}\mathbf{I}$, and $\mathbf{I}\mathbf{I}\mathbf{I}$ correspond to potential energy, kinetic energy, and mixed energy, respectively, from a mechanical perspective. To better appreciate this translation, note that the factor $\frac{1 + \sqrt{\mus}}{1 - \sqrt{\mus}}$ in $\mathbf{I}$ results from the term $\frac{1 + \sqrt{\mus}}{1 - \sqrt{\mus}}\sqrt{s}{\nabla f}{(x_{k})}$ in (2.5). Likewise, $\frac{2\sqrt{\mu}}{1 - \sqrt{\mus}}$ in $\mathbf{I}\mathbf{I}\mathbf{I}$ is from the term $\frac{2\sqrt{\mus}}{1 - \sqrt{\mus}}v_{k}$ in (2.5). The need for the final (small) negative term is technical; we discuss it in Section 3.2.

### Step 4: Analyzing Algorithms Using Discrete Lyapunov Functions

The last step is to map properties of high-resolution ODEs to corresponding properties of optimization methods. This step closely mimics Step 2 except that now the object is a discrete algorithm and the tool is a discrete Lyapunov function such as (2.6). Given that Step 2 has been performed, this translation is conceptually straightforward, albeit often calculation-intensive. For example, using the discrete Lyapunov function (2.6), we will recover the optimal linear rate of NAG-SC and gain insights into the fundamental effect of the gradient correction in accelerating NAG-SC. In addition, NAG-C is shown to minimize the squared gradient norm at an inverse cubic rate by a simple analysis of the decreasing rate of its discrete Lyapunov function.

## Gradient Correction for Acceleration

In this section, we use our high-resolution ODE framework to analyze NAG-SC and the heavy-ball method. Section 3.1 focuses on the ODEs with an objective function $f \in {\mathcal{S}_{\mu,L}^{2}{({\mathbb{R}}^{n})}}$, and in Section 3.2 we extend the results to the discrete case for $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$. Finally, in Section 3.3 we offer a comparative study of NAG-SC and the heavy-ball method from a finite-difference viewpoint.

Throughout this section, the strategy is to analyze the two methods in parallel, thereby highlighting the differences between the two methods. In particular, the comparison will demonstrate the vital role of the gradient correction, namely ${\frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}} \cdot s}\left( {{{\nabla f}{(x_{k})}} - {{\nabla f}{(x_{k - 1})}}} \right)$ in the discrete case and $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in the ODE case, in making NAG-SC an accelerated method.

### The ODE Case

The following theorem characterizes the convergence rate of the high-resolution ODE corresponding to NAG-SC.

### Theorem 1 (Convergence of NAG-SC ODE)

Let $f \in {\mathcal{S}_{\mu,L}^{2}{({\mathbb{R}}^{n})}}$. For any step size $0 < s \leq {1/L}$, the solution $X = {X{(t)}}$ of the high-resolution ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) satisfies

The theorem states that the functional value $f{(X)}$ tends to the minimum $f{(x^{\star})}$ at a linear rate. By setting $s = {1/L}$, we obtain ${{f{(X)}} - {f{(x^{\star})}}} \leq {2L\left\| {x_{0} - x^{\star}} \right\|^{2}e^{- \frac{\sqrt{\mu}t}{4}}}$.

The proof of Theorem 1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") is based on analyzing the Lyapunov function $\mathcal{E}{(t)}$ for the high-resolution ODE of NAG-SC. Recall that $\mathcal{E}{(t)}$ defined in (2.4) is

The next lemma states the key property we need from this Lyapunov function

### Lemma 3.1 (Lyapunov function for NAG-SC ODE)

Let $f \in {\mathcal{S}_{\mu,L}^{2}{({\mathbb{R}}^{n})}}$. For any step size $s > 0$, and with $X = {X{(t)}}$ being the solution to the high-resolution ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")), the Lyapunov function (2.4) satisfies

The proof of this theorem relies on Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") through the inequality ${\overset{˙}{\mathcal{E}}{(t)}} \leq {- {\frac{\sqrt{\mu}}{4}\mathcal{E}{(t)}}}$. The term ${\frac{\sqrt{s}}{2}{({\left\| {{\nabla f}{(X)}} \right\|^{2} + {{\overset{˙}{X}}^{\top}{\nabla^{2}f}{(X)}\overset{˙}{X}}})}} \geq 0$ plays no role at the moment, but Section 3.2 will shed light on its profound effect in the discretization of the high-resolution ODE of NAG-SC.

### Proof of Theorem 1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")

Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") implies ${\overset{˙}{\mathcal{E}}{(t)}} \leq {- {\frac{\sqrt{\mu}}{4}\mathcal{E}{(t)}}}$, which amounts to

By integrating out $t$, we get

Recognizing the initial conditions ${X{}} = x_{0}$ and ${\overset{˙}{X}{}} = {- \frac{2\sqrt{s}{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$, we write (3.2) as

Since $f \in \mathcal{S}_{\mu,L}^{2}$, we have that ${\|{{\nabla f}{(x_{0})}}\|} \leq {L{\|{x_{0} - x^{\star}}\|}}$ and ${{f{(x_{0})}} - {f{(x^{\star})}}} \leq {{L{\|{x_{0} - x^{\star}}\|}^{2}}/2}$. Together with the Cauchy--Schwarz inequality, the two inequalities yield

which is valid for all $s > 0$. To simplify the coefficient of $\left\| {x_{0} - x^{\star}} \right\|^{2}e^{- \frac{\sqrt{\mu}t}{4}}$, note that $L$ can be replaced by $1/s$ in the analysis since $s \leq {1/L}$. It follows that

Furthermore, a bit of analysis reveals that

since ${\mus} \leq {\mu/L} \leq 1$, and this step completes the proof of Theorem 1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). ∎

We now consider the heavy-ball method (1.2). Recall that the momentum coefficient $\alpha$ is set to $\frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$. The following theorem characterizes the rate of convergence of this method.

### Theorem 2 (Convergence of heavy-ball ODE)

Let $f \in {\mathcal{S}_{\mu,L}^{2}{({\mathbb{R}}^{n})}}$. For any step size $0 < s \leq {1/L}$, the solution $X = {X{(t)}}$ of the high-resolution ODE (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) satisfies

As in the case of NAG-SC, the proof of Theorem 2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") is based on a Lyapunov function:

which is the same as the Lyapunov function (2.4) for NAG-SC except for the lack of the $\sqrt{s}{\nabla f}{(X)}$ term. In particular, (2.4) and (3.3) are identical if $s = 0$. The following lemma considers the decay rate of (3.3).

### Lemma 3.2 (Lyapunov function for the heavy-ball ODE)

Let $f \in {\mathcal{S}_{\mu,L}^{2}{({\mathbb{R}}^{n})}}$. For any step size $s > 0$, the Lyapunov function (3.3) for the high-resolution ODE (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) satisfies

The proof of Theorem 2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") follows the same strategy as the proof of Theorem 1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). In brief, Lemma 3.2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") gives ${\mathcal{E}{(t)}} \leq {e^{- {{\sqrt{\mu}t}/4}}\mathcal{E}{}}$ by integrating over the time parameter $t$. Recognizing the initial conditions

in the high-resolution ODE of the heavy-ball method and using the $L$-smoothness of $\nabla f$, Lemma 3.2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") yields

if the step size $s \leq {1/L}$. Finally, since $0 < {\mus} \leq {\mu/L} \leq 1$, the coefficient satisfies

The proofs of Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") and Lemma 3.2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") share similar ideas. In view of this, we present only the proof of the former here, deferring the proof of Lemma 3.2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") to Appendix B.1.

### Proof of Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")

Along trajectories of (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) the Lyapunov function (2.4) satisfies

Furthermore, $\left\langle {{\nabla f}{(X)}},{X - x^{\star}} \right\rangle$ is greater than or equal to both ${{f{(X)}} - {f{(x^{\star})}}} + {\frac{\mu}{2}{\|{X - x^{\star}}\|}^{2}}$ and $\mu{\|{X - x^{\star}}\|}^{2}$ due to the $\mu$-strong convexity of $f$. This yields

which together with (3.4) suggests that the time derivative of this Lyapunov function can be bounded as

Next, the Cauchy--Schwarz inequality yields

from which it follows that

Combining (3.5) and (3.6) completes the proof of the theorem.

### Remark 3.3

The only inequality in (3.4) is due to the term $\frac{\sqrt{s}}{2}{({\left\| {{\nabla f}{(X)}} \right\|^{2} + {{\overset{˙}{X}}^{\top}{\nabla^{2}f}{(X)}\overset{˙}{X}}})}$, which is discussed right after the statement of Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). This term results from the gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in the NAG-SC ODE. For comparison, this term does not appear in Lemma 3.2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") in the case of the heavy-ball method as its ODE does not include the gradient correction and, accordingly, its Lyapunov function (3.3) is free of the $\sqrt{s}{\nabla f}{(X)}$ term.

### The Discrete Case

This section carries over the results in Section 3.1 to the two discrete algorithms, namely NAG-SC and the heavy-ball method. Here we consider an objective $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$ since second-order differentiability of $f$ is not required in the two discrete methods. Recall that both methods start with an arbitrary $x_{0}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$.

### Theorem 3 (Convergence of NAG-SC)

Let $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$. If the step size is set to $s = {1/{({4L})}}$, the iterates ${\{ x_{k}\}}_{k = 0}^{\infty}$ generated by NAG-SC (1.3) satisfy

for all $k \geq 0$.

In brief, the theorem states that ${\log{({{f{(x_{k})}} - {f{(x^{\star})}}})}} \leq {- {O{({k\sqrt{\mu/L}})}}}$, which matches the optimal rate for minimizing smooth strongly convex functions using only first-order information \[\]. More precisely, \[\] shows that ${{f{(x_{k})}} - {f{(x^{\star})}}} = {O{({({1 - \sqrt{\mu/L}})}^{k})}}$ by taking $s = {1/L}$ in NAG-SC. Although this optimal rate of NAG-SC is well known in the litetature, this is the first Lyapunov-function-based proof of this result.

As indicated in Section 2, the proof of Theorem 3. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") rests on the discrete Lyapunov function (2.6):

Recall that this functional is derived by writing NAG-SC in the phase-space representation (2.5). Analogous to Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"), the following lemma gives an upper bound on the difference ${\mathcal{E}{({k + 1})}} - {\mathcal{E}{(k)}}$.

### Lemma 3.4 (Lyapunov function for NAG-SC)

Let $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$. Taking any step size $0 < s \leq {1/{({4L})}}$, the discrete Lyapunov function (2.6) with ${\{ x_{k}\}}_{k = 0}^{\infty}$ generated by NAG-SC satisfies

The form of the inequality ensured by Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") is consistent with that of Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). Alternatively, it can be written as ${\mathcal{E}{({k + 1})}} \leq {\frac{1}{1 + \frac{\sqrt{\mus}}{6}}\mathcal{E}{(k)}}$. With Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") in place, we give the proof of Theorem 3. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations").

### Proof of Theorem 3. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")

To see this, first note that

Combining these two inequalities, we get

Next, we inductively apply Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"), yielding

Recognizing the initial velocity $v_{0} = {- \frac{2\sqrt{s}{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$ in NAG-SC, one can show that

Taking $s = {1/{({4L})}}$ in (3.9), it follows from (3.7) and (3.8) that

Here the constant factor $C_{\mu/L}$ is a short-hand for

which is less than five by making use of the fact that ${\mu/L} \leq 1$. This completes the proof.

We now turn to the heavy-ball method (1.2). Recall that $\alpha = \frac{1 - \sqrt{\mus}}{1 + \sqrt{\mus}}$ and $x_{1} = {x_{0} - \frac{2s{\nabla f}{(x_{0})}}{1 + \sqrt{\mus}}}$.

### Theorem 4 (Convergence of heavy-ball method)

Let $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$. If the step size is set to $s = {\mu/{({16L^{2}})}}$, the iterates ${\{ x_{k}\}}_{k = 0}^{\infty}$ generated by the heavy-ball method satisfy

for all $k \geq 0$.

The heavy-ball method minimizes the objective at the rate ${\log{({{f{(x_{k})}} - {f{(x^{\star})}}})}} \leq {- {O{({{k\mu}/L})}}}$, as opposed to the optimal rate $- {O{({k\sqrt{\mu/L}})}}$ obtained by NAG-SC. Thus, the acceleration phenomenon is not observed in the heavy-ball method for minimizing functions in the class $\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}$. This difference is, on the surface, attributed to the much smaller step size $s = {\mu/{({16L^{2}})}}$ in Theorem 4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") than the ($s = {1/{({4L})}}$) in Theorem 3. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). Further discussion of this difference is given after Lemma 3.5. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") and in Section 3.3.

In addition to allowing us to complete the proof of Theorem 4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"), Lemma 3.5. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") will shed light on why the heavy-ball method needs a more conservative step size. To state this lemma, we consider the discrete Lyapunov function defined as

which is derived by discretizing the continuous Lyapunov function (3.3) using the phase-space representation of the heavy-ball method:

### Lemma 3.5 (Lyapunov function for the heavy-ball method)

Let $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$. For any step size $s > 0$, the discrete Lyapunov function (3.10) with ${\{ x_{k}\}}_{k = 0}^{\infty}$ generated by the heavy-ball method satisfies

The proof of Lemma 3.5. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") can be found in Appendix B.3. To apply this lemma to prove Theorem 4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"), we need to ensure

A sufficient and necessary condition for (3.13) is

This is because $\left\| {{\nabla f}{(x_{k + 1})}} \right\|^{2} \leq {2L\left( {{f{(x_{k + 1})}} - {f{(x^{\star})}}} \right)}$, which can be further reduced to an equality (for example, ${f{(x)}} = {\frac{L}{2}{\| x\|}^{2}}$). Thus, the step size $s$ must obey

In particular, the choice of $s = \frac{\mu}{16L^{2}}$ fulfills (3.14) and, as a consequence, Lemma 3.5. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") implies

The remainder of the proof of Theorem 4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") is similar to that of Theorem 3. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") and is therefore omitted. As an aside, \[\] uses $s = {4/{({\sqrt{L} + \sqrt{\mu}})}^{2}}$ for local accelerated convergence of the heavy-ball method. This choice of step size is larger than our step size $s = \frac{\mu}{16L^{2}}$, which yields a non-accelerated but global convergence rate.

The term $\frac{s}{2}\left( \frac{1 + \sqrt{\mus}}{1 - \sqrt{\mus}} \right)^{2}\left\| {{\nabla f}{(x_{k + 1})}} \right\|^{2}$ in (3.12. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) that arises from finite differencing of (3.10) is a (small) term of order $O{(s)}$ and, as a consequence, this term is not reflected in Lemma 3.2. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). In relating to the case of NAG-SC, one would be tempted to ask why this term does not appear in Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). In fact, a similar term can be found in ${\mathcal{E}{({k + 1})}} - {\mathcal{E}{(k)}}$ by taking a closer look at the proof of Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). However, this term is canceled out by the discrete version of the quadratic term $\frac{\sqrt{s}}{2}{({\left\| {{\nabla f}{(X)}} \right\|^{2} + {{\overset{˙}{X}}^{\top}{\nabla^{2}f}{(X)}\overset{˙}{X}}})}$ in Lemma 3.1. ‣ 3.1 The ODE Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") and is, therefore, not present in the statement of Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations"). Note that this quadratic term results from the gradient correction (see Remark 3.3). In light of the above, the gradient correction is the key ingredient that allows for a larger step size in NAG-SC, which is necessary for achieving acceleration.

For completeness, we finish Section 3.2 by proving Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations").

### Proof of Lemma 3.4. ‣ 3.2 The Discrete Case ‣ 3 Gradient Correction for Acceleration ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")

Using the Cauchy--Schwarz inequality, we have^99^9See the definition of $\mathbf{I}\mathbf{I}\mathbf{I}$ in (2.6).

which, together with the inequality

for $f \in {\mathcal{S}_{\mu,L}^{1}{({\mathbb{R}}^{n})}}$, shows that the Lyapunov function (2.6) satisfies

Next, as shown in Appendix B.2, the inequality

holds for $s \leq {1/{({2L})}}$. Comparing the coefficients of the same terms in (3.15) for $\mathcal{E}{({k + 1})}$ and (3.16), we conclude that the first difference of the discrete Lyapunov function (2.6) must satisfy

### Numerical Stability Perspective on Acceleration

As shown in Section 3.2, the gradient correction is the fundamental cause of the difference in convergence rates between the heavy-ball method and NAG-SC. This section aims to further elucidate this distinction from the viewpoint of numerical stability. A numerical scheme is said to be stable if, roughly speaking, this scheme does not magnify errors in the input data. Accordingly, we address the question of what values of the step size $s$ are allowed for solving the high-resolution ODEs (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) and (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) in a stable fashion. While various discretization schemes on low-resolution ODEs have been explored in \[ \], we limit our attention to the forward Euler scheme to simplify the discussion (see \[\] for an exposition on discretization schemes).

For the heavy-ball method, the forward Euler scheme applied to (1.10 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) is

Using the approximation ${{\nabla f}{({{X{({t - \sqrt{s}})}} + \epsilon})}} \approx {{{\nabla f}{({X{({t - \sqrt{s}})}})}} + {{\nabla^{2}f}{({X{({t - \sqrt{s}})}})}\epsilon}}$ for a small perturbation $\epsilon$, we get the characteristic equation of (3.17):

where $\mathbf{I}$ denotes the $n \times n$ identity matrix. The numerical stability of (3.17) requires the roots of the characteristic equation to be no larger than one in absolute value. Therefore, a necessary condition for the stability is that^1010^10The notation $A \preceq B$ indicates that $B - A$ is positive semidefinite for symmetric matrices $A$ and $B$.

By the $L$-smoothness of $f$, the largest singular value of ${\nabla^{2}f}{({X{({t - \sqrt{s}})}})}$ can be as large as $L$. Therefore, (3.18) is guaranteed in the worst case analysis only if

which shows that the step size must obey

Next, we turn to the high-resolution ODE (1.11 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-SC, for which the forward Euler scheme reads

Its characteristic equation is

which, as earlier, suggests that the numerical stability condition of (3.20) is

This inequality is ensured by setting the step size

As constraints on the step sizes, both (3.19) and (3.21) are in agreement with the discussion in Section 3.2, albeit from a different perspective. In short, a comparison between (3.17) and (3.20) reveals that the Hessian $\sqrt{s}{\nabla^{2}f}{({X{({t - \sqrt{s}})}})}$ makes the forward Euler scheme for the NAG-SC ODE numerically stable with a larger step size, namely $s = {O{({1/L})}}$. This is yet another reflection of the vital importance of the gradient correction in yielding acceleration for NAG-SC.

## Gradient Correction for Gradient Norm Minimization

In this section, we extend the use of the high-resolution ODE framework to NAG-C (1.5) in the setting of minimizing an $L$-smooth convex function $f$. The main result is an improved rate of NAG-SC for minimizing the squared gradient norm. Indeed, we show that NAG-C achieves the $O{({L^{2}/k^{3}})}$ rate of convergence for minimizing ${\|{{\nabla f}{(x_{k})}}\|}^{2}$. To the best of our knowledge, this is the sharpest known bound for this problem using NAG-C without any modification. Moreover, we will show that the gradient correction in NAG-C is responsible for this rate and, as it is therefore unsurprising that this inverse cubic rate was not perceived within the low-resolution ODE frameworks such as that of \[\]. In Section 4.3, we propose a new accelerated method with the same rate $O{({L^{2}/k^{3}})}$ and briefly discuss the benefit of the phase-space representation in simplifying technical proofs.

### The ODE Case

We begin by studying the high-resolution ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) corresponding to NAG-C with an objective $f \in {\mathcal{F}_{L}^{2}{({\mathbb{R}}^{n})}}$ and an arbitrary step size $s > 0$. For convenience, let $t_{0} = {1.5\sqrt{s}}$.

### Theorem 5

Assume $f \in {\mathcal{F}_{L}^{2}{({\mathbb{R}}^{n})}}$ and let $X = {X{(t)}}$ be the solution to the ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")). The squared gradient norm satisfies

By taking the step size $s = {1/L}$, this theorem shows that

where the infimum operator is necessary as the squared gradient norm is generally not decreasing in $t$. In contrast, directly combining the convergence rate of the function value (see Corollary 4.2) and inequality ${\|{{\nabla f}{(X)}}\|}^{2} \leq {2L{({{f{(X)}} - {f{(x^{\star})}}})}}$ only gives a $O{({L/t^{2}})}$ rate for squared gradient norm minimization.

The proof of the theorem is based on the continuous Lyapunov function

which reduces to the continuous Lyapunov function in \[\] when setting $s = 0$.

### Lemma 4.1

Let $f \in {\mathcal{F}_{L}^{2}{({\mathbb{R}}^{n})}}$. The Lyapunov function defined in (4.1) with $X = {X{(t)}}$ being the solution to the ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) satisfies

for all $t \geq t_{0}$.

The decreasing rate of $\mathcal{E}{(t)}$ as specified in the lemma is sufficient for the proof of Theorem 5. First, note that Lemma 4.1 readily gives

where the last step is due to the fact ${\mathcal{E}{(t)}} \geq 0$. Thus, it follows that

Recognizing the initial conditions of the ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")), we get

which together with (4.3) gives

This bound reduces to the one claimed by Theorem 5 by only keeping the first term ${\sqrt{s}{({t^{3} - t_{0}^{3}})}}/3$ in the denominator.

The gradient correction $\sqrt{s}{\nabla^{2}f}{(X)}\overset{˙}{X}$ in the high-resolution ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) plays a pivotal role in Lemma 4.1 and is, thus, key to Theorem 5. As will be seen in the proof of the lemma, the factor $\left\| {{\nabla f}{(X)}} \right\|^{2}$ in (4.2) results from the term $t\sqrt{s}{\nabla f}{(X)}$ in the Lyapunov function (4.1), which arises from the gradient correction in the ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")). In light of this, the low-resolution ODE (1.8) of NAG-C cannot yield a result similar to Lemma 4.1 and; furthermore, we conjecture that the $O{({\sqrt{L}/t^{3}})}$ rate does applies to this ODE. Section 4.2 will discuss this point further in the discrete case.

In passing, it is worth pointing out that the analysis above applies to the case of $s = 0$. In this case, we have $t_{0} = 0$, and (4.4) turns out to be

This result is similar to that of the low-resolution ODE in \[\]^1111^11To see this, recall that \[\] shows that ${{f{({X{(t)}})}} - {f{(x^{\star})}}} \leq \frac{2{\|{x_{0} - x^{\star}}\|}^{2}}{t^{2}}$, where $X = {X{(t)}}$ is the solution to (4.4) with $s = 0$. Using the $L$-smoothness of $f$, we get ${\|{{\nabla f}{({X{(t)}})}}\|}^{2} \leq {2L{({{f{({X{(t)}})}} - {f{(x^{\star})}}})}} \leq \frac{4L{\|{x_{0} - x^{\star}}\|}^{2}}{t^{2}}$..

This section is concluded with the proof of Lemma 4.1.

### Proof of Lemma 4.1

The time derivative of the Lyapunov function (4.1) obeys

Making use of the basic inequality ${f{(x^{\star})}} \geq {{f{(X)}} + \left\langle {{\nabla f}{(X)}},{x^{\star} - X} \right\rangle + {\frac{1}{2L}\left\| {{\nabla f}{(X)}} \right\|^{2}}}$ for $L$-smooth $f$, the expression of $\frac{d\mathcal{E}}{dt}$ above satisfies

Note that Lemma 4.1 shows $\mathcal{E}{(t)}$ is a decreasing function, from which we get

by recognizing the initial conditions of the high-resolution ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")). This gives the following corollary.

### Corollary 4.2

Under the same assumptions as in Theorem 5, for any $t > t_{0}$, we have

### The Discrete Case

We now turn to the discrete NAG-C (1.5) for minimizing an objective $f \in {\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}}$. Recall that this algorithm starts from any $x_{0}$ and $y_{0} = x_{0}$. The discrete counterpart of Theorem 5 is as follows.

### Theorem 6

Let $f \in {\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}}$. For any step size $0 < s \leq {1/{({3L})}}$, the iterates $\left\{ x_{k} \right\}_{k = 0}^{\infty}$ generated by NAG-C obey

for all $k \geq 0$. In additional, we have

for all $k \geq 0$.

Taking $s = {1/{({3L})}}$, Theorem 6 shows that NAG-C minimizes the squared gradient norm at the rate $O{({L^{2}/k^{3}})}$. This theoretical prediction is in agreement with two numerical examples illustrated in Figure 4. To our knowledge, the bound $O{({L^{2}/k^{3}})}$ is sharper than any existing bounds in the literature for NAG-C for squared gradient norm minimization. In fact, the convergence result ${{f{(x_{k})}} - {f{(x^{\star})}}} = {O{({L/k^{2}})}}$ for NAG-C and the $L$-smoothness of the objective immediately give ${\|{{\nabla f}{(x_{k})}}\|}^{2} \leq {O{({L^{2}/k^{2}})}}$. This well-known but loose bound can be improved by using a recent result from \[\], which shows that a slightly modified version NAG-C satisfies ${{f{(x_{k})}} - {f{(x^{\star})}}} = {o{({L/k^{2}})}}$ (see Section 5.2 for more discussion of this improved rate). This reveals

which, however, remains looser than that of Theorem 6. In addition, the rate $o{({L^{2}/k^{2}})}$ is not valid for $k \leq {n/2}$ and, as such, the bound $o{({L^{2}/k^{2}})}$ on the squared gradient norm is dimension-dependent \[\]. For completeness, the rate $O{({L^{2}/k^{3}})}$ can be achieved by introducing an additional sequence of iterates and a more aggressive step size policy in a variant of NAG-C \[\]. In stark contrast, our result shows that no adjustments are needed for NAG-C to yield an accelerated convergence rate for minimizing the gradient norm.

Figure 4: Scaled squared gradient norm s2 (k+1)3 min0 ≤ i ≤ k∥∇f (xi)∥2 of NAG-C. In both plots, the scaled squared gradient norm stays bounded as k → ∞. Left: ${f{(x)}} = {{\frac{1}{2}\left\langle {Ax},x \right\rangle} + \left\langle b,x \right\rangle}$, where A = T′ T is a 500 × 500 positive semidefinite matrix and b is 1 × 500. All entries of b, T ∈ ℝ500 × 500 are i.i.d. uniform random variables on, and ∥ ⋅ ∥2 denotes the matrix spectral norm. Right: ${f{(x)}} = {\rho{\log\left\{ {\sum\limits_{i = 1}^{200}{\exp\left\lbrack {\left( {\left\langle a_{i},x \right\rangle - b_{i}} \right)/\rho} \right\rbrack}} \right\}}}$, where A = [a1, …, a200]′ is a 200 × 50 matrix and b is a 200 × 1 column vector. All entries of A and b are i.i.d.-sampled from 𝒩 and ρ = 20.

An $\Omega{({L^{2}/k^{4}})}$ lower bound has been established by \[\] as the optimal convergence rate for minimizing ${\|{\nabla f}\|}^{2}$ with access to only first-order information. (For completeness, Appendix C.3 presents an exposition of this fundamental barrier.) In the same paper, a regularization technique is used in conjunction with NAG-SC to obtain a matching upper bound (up to a logarithmic factor). This method, however, takes as input the distance between the initial point and the minimizer, which is not practical in general \[\].

Returning to Theorem 6, we present a proof of this theorem using a Lyapunov function argument. By way of comparison, we remark that Nesterov's estimate sequence technique is unlikely to be useful for characterizing the convergence of the gradient norm as this technique is essentially based on local quadratic approximations. The phase-space representation of NAG-C (1.5) takes the following form:

for any initial position $x_{0}$ and the initial velocity $v_{0} = {- {\sqrt{s}{\nabla f}{(x_{0})}}}$. This representation allows us to discretize the continuous Lyapunov function (4.1) into

The following lemma characterizes the dynamics of this Lyapunov function.

### Lemma 4.3

Under the assumptions of Theorem 6, we have

for all $k \geq 0$.

Next, we provide the proof of Theorem 6.

### Proof of Theorem 6

We start with the fact that

for $k \geq 2$. To show this, note that it suffices to guarantee

which is self-evident since $s \leq {1/{({3L})}}$ by assumption.

Next, by a telescoping-sum argument, Lemma 4.3 leads to the following inequalities for $k \geq 4$:

where the second inequality is due to (4.7). To further simplify the bound, observe that

for $k \geq 4$. Plugging this inequality into (4.9) yields

It is shown in Appendix C.1 that

for $s \leq {1/{({3L})}}$. As a consequence of this, (4.10) gives

For completeness, Appendix C.1 proves, via a brute-force calculation, that $\left\| {{\nabla f}{(x_{0})}} \right\|^{2},\left\| {{\nabla f}{(x_{1})}} \right\|^{2},\left\| {{\nabla f}{(x_{2})}} \right\|^{2}$, and $\left\| {{\nabla f}{(x_{3})}} \right\|^{2}$ are all bounded above by the right-hand side of (4.11). This completes the proof of the first inequality claimed by Theorem 6.

For the second claim in Theorem 6, the definition of the Lyapunov function and its decreasing property ensured by (4.7) implies

for all $k \geq 2$. Appendix C.1 establishes that ${f{(x_{0})}} - {f{(x^{\star})}}$ and ${f{(x_{1})}} - {f{(x^{\star})}}$ are bounded by the right-hand side of (4.12). This completes the proof.

Now, we prove Lemma 4.3.

### Proof of Lemma 4.3

The difference of the Lyapunov function (4.6) satisfies

where the last two equalities are due to

which follows from the phase-space representation (4.5). Rearranging the identity for ${\mathcal{E}{({k + 1})}} - {\mathcal{E}{(k)}}$, we get

The next step is to recognize that the convexity and the $L$-smoothness of $f$ gives

Plugging these two inequalities into (4.14), we have

where the second inequality uses the fact that $\left\langle {{\nabla f}{(x_{k + 1})}},{x_{k + 1} - x^{\star}} \right\rangle \geq 0$.

To further bound ${\mathcal{E}{({k + 1})}} - {\mathcal{E}{(k)}}$, making use of (4.13) with $k + 1$ in place of $k$, we get

This completes the proof.

In passing, we remark that the gradient correction sheds light on the superiority of the high-resolution ODE over its low-resolution counterpart, just as in Section 3. Indeed, the absence of the gradient correction in the low-resolution ODE leads to the lack of the term ${({k + 1})}s{\nabla f}{(x_{k})}$ in the Lyapunov function (see Section 4 of \[\]), as opposed to the high-resolution Lyapunov function (4.6). Accordingly, it is unlikely to carry over the bound ${{\mathcal{E}{({k + 1})}} - {\mathcal{E}{(k)}}} \leq {- {O{({s^{2}k^{2}{\|{{\nabla f}{(x_{k + 1})}}\|}^{2}})}}}$ of Lemma 4.3 to the low-resolution case and, consequently, the low-resolution ODE approach pioneered by \[\] is insufficient to obtain the $O{({L^{2}/k^{3}})}$ rate for squared gradient norm minimization.

### Modified NAG-C without a Phase-Space Representation

This section proposes a new accelerated method that also achieves the $O{({L^{2}/k^{3}})}$ rate for minimizing the squared gradient norm. This method takes the following form:

starting with $x_{0}$ and $y_{0} = x_{0}$. As shown by the following theorem, this new method has the same convergence rates as NAG-C.

### Theorem 7

Let $f \in {\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}}$. Taking any step size $0 < s \leq {1/L}$, the iterates ${\{{(x_{k},y_{k})}\}}_{k = 0}^{\infty}$ generated by the modified NAG-C (4.15) satisfy

for all $k \geq 0$.

We refer readers to Appendix C.2 for the proof of Theorem 7, which is, as earlier, based on a Lyapunov function. However, since both $f{(x_{k})}$ and $f{(y_{k})}$ appear in the iteration, (4.15) does not admit a phase-space representation. As a consequence, the construction of the Lyapunov function is complex; we arrived at it via trial and error. Our initial aim was to seek possible improved rates of the original NAG-C without using the phase-space representation, but the enormous challenges arising in this process motivated us to modify NAG-C to the current (4.15), and to adopt the phase-space representation. Employing the phase-space representation yields a simple proof of the $O{({L^{2}/k^{3}})}$ rate for the original NAG-C and this technique turned out to be useful for other accelerated methods.

## Extensions

Motivated by the high-resolution ODE (1.12 ‣ 1.2 Overview of Contributions ‣ 1 Introduction ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations")) of NAG-C, this section considers a family of generalized high-resolution ODEs that take the form

for $t \geq {{\alpha\sqrt{s}}/2}$, with initial conditions ${X{({{\alpha\sqrt{s}}/2})}} = x_{0}$ and ${\overset{˙}{X}{({{\alpha\sqrt{s}}/2})}} = {- {\sqrt{s}{\nabla f}{(x_{0})}}}$. As demonstrated in \[ \], the low-resolution counterpart (that is, set $s = 0$) of (5.1) achieves acceleration if and only if $\alpha \geq 3$. Accordingly, we focus on the case where the friction parameter $\alpha \geq 3$ and the gradient correction parameter $\beta > 0$. An investigation of the case of $\alpha < 3$ is left for future work.

By discretizing the ODE (5.1), we obtain a family of new accelerated methods for minimizing smooth convex functions:

starting with $x_{0} = y_{0}$. The second line of the iteration is equivalent to

In Section 5.1, we study the convergence rates of this family of generalized NAC-C algorithms along the lines of Section 4. To further our understanding of (5.2), Section 5.2 shows that this method in the super-critical regime (that is, $\alpha > 3$) converges to the optimum actually faster than $O{({1/{({sk^{2}})}})}$. As earlier, the proofs of all the results follow the high-resolution ODE framework introduced in Section 2. Proofs are deferred to Appendix D. Finally, we note that Section 6 briefly sketches the extensions along this direction for NAG-SC.

### Convergence Rates

The theorem below characterizes the convergence rates of the generalized NAG-C (5.2).

### Theorem 8

Let ${f \in {\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}}},{\alpha \geq 3}$, and $\beta > \frac{1}{2}$. There exists $c_{\alpha,\beta} > 0$ such that, taking any step size $0 < s \leq {c_{\alpha,\beta}/L}$, the iterates ${\{ x_{k}\}}_{k = 0}^{\infty}$ generated by the generalized NAG-C (5.2) obey

for all $k \geq 0$. In addition, we have

for all $k \geq 0$. The constants $c_{\alpha,\beta}$ and $C_{\alpha,\beta}$ only depend on $\alpha$ and $\beta$.

The proof of Theorem 8 is given in Appendix D.1 for $\alpha = 3$ and Appendix D.2 for $\alpha > 3$. This theorem shows that the generalized NAG-C achieves the same rates as the original NAG-C in both squared gradient norm and function value minimization. The constraint $\beta > \frac{1}{2}$ reveals that further leveraging of the gradient correction does not hurt acceleration, but perhaps not the other way around (note that NAG-C in its original form corresponds to $\beta = 1$). It is an open question whether this constraint is a technical artifact or is fundamental to acceleration.

### Faster Convergence in Super-Critical Regime

We turn to the case in which $\alpha > 3$, where we show that the generalized NAG-C in this regime attains a faster rate for minimizing the function value. The following proposition provides a technical inequality that motivates the derivation of the improved rate.

### Proposition 5.1

Let ${f \in {\mathcal{F}_{L}^{1}{({\mathbb{R}}^{n})}}},{\alpha > 3}$, and $\beta > \frac{1}{2}$. There exists $c_{\alpha,\beta}^{\prime} > 0$ such that, taking any step size $0 < s \leq {c_{\alpha,\beta}^{\prime}/L}$, the iterates ${\{ x_{k}\}}_{k = 0}^{\infty}$ generated by the generalized NAG-C (5.2) obey

where the constants $c_{\alpha,\beta}^{\prime}$ and $C_{\alpha,\beta}^{\prime}$ only depend on $\alpha$ and $\beta$.

In relating to Theorem 8, one can show that Proposition 5.1 in fact implies (5.3) in Theorem 8. To see this, note that for $k \geq 1$, one has

where the second inequality follows from Proposition 5.1.

Proposition 5.1 can be thought of as a generalization of Theorem 6 of \[\]. In particular, this result implies an intriguing and important message. To see this, first note that, by taking $s = {O{({1/L})}}$, Proposition 5.1 gives

which would not be valid if ${{f{(x_{k})}} - {f{(x^{\star})}}} \geq {{cL\left\| {x_{0} - x^{\star}} \right\|^{2}}/k^{2}}$ for a constant $c > 0$. Thus, it is tempting to suggest that there might exist a faster convergence rate in the sense that

This faster rate is indeed achievable as we show next, though there are examples where (5.4) and ${{f{(x_{k})}} - {f{(x^{\star})}}} = {O{({{L\left\| {x_{0} - x^{\star}} \right\|^{2}}/k^{2}})}}$ are both satisfied but (5.5) does not hold (a counterexample is given in Appendx D.3).

### Theorem 9

Under the same assumptions as in Proposition 5.1, taking the step size $s = {c_{\alpha,\beta}^{\prime}/L}$, the iterates ${\{ x_{k}\}}_{k = 0}^{\infty}$ generated by the generalized NAG-C (5.2) starting from any $x_{0} \neq x^{\star}$ satisfy

Figure 5: Scaled error s (k+1)2 (f (xk)−f (x⋆)) of the generalized NAG-C (5.2) with various (α,β). The setting is the same as the left plot of Figure 4, with the objective ${f{(x)}} = {{\frac{1}{2}\left\langle {Ax},x \right\rangle} + \left\langle b,x \right\rangle}$. The step size is s = 10−1 ∥A∥2−1. The left shows the short-time behaviors of the methods, while the right focuses on the long-time behaviors. The scaled error curves with the same β are very close to each other in the short-time regime, but in the long-time regime, the scaled error curves with the same α almost overlap. The four scaled error curves slowly tend to zero.

Figure 6: Scaled error s (k+1)2 (f (xk)−f (x⋆)) of the generalized NAG-C (5.2) with various (α,β). The setting is the same as the right plot of Figure 4, with the objective ${f{(x)}} = {\rho{\log\left\{ {\sum\limits_{i = 1}^{200}{\exp\left\lbrack {\left( {\left\langle a_{i},x \right\rangle - b_{i}} \right)/\rho} \right\rbrack}} \right\}}}$. The step size is s = 0.1. This set of simulation studies implies that the convergence in Theorem 9 is slow for some problems.

Figures 5 and 6 present several numerical studies concerning the prediction of Theorem 9. For a fixed dimension $n$, the convergence in Theorem 9 is uniform over functions in $\mathcal{F}^{1} = {\cup_{L > 0}\mathcal{F}_{L}^{1}}$ and, consequently, is independent of the Lipschitz constant $L$ and the initial point $x_{0}$. In addition to following the high-resolution ODE framework, the proof of this theorem reposes on the finiteness of the series in Proposition 5.1. See Appendix D.2 and Appendix D.4 and 𝑜⁢(𝐿/𝑘²) ‣ Appendix D Technical Details in Section 5 ‣ Understanding the Acceleration Phenomenon via High-Resolution Differential Equations") for the full proofs of the proposition and the theorem, respectively.

In the literature, \[ \] use low-resolution ODEs to establish the faster rate $o{({1/k^{2}})}$ for the generalized NAG-C (5.2) in the special case of $\beta = 1$. In contrast, our proof of Theorem 9 is more general and applies to a broader class of methods.

In passing, we make the observation that Proposition 5.1 reveals that

which would not hold if ${\min_{0 \leq i \leq k}{\|{{\nabla f}{(x_{i})}}\|}^{2}} \geq {{c{\|{x_{0} - x^{\star}}\|}^{2}}/{({s^{2}k^{3}})}}$ for all $k$ and a constant $c > 0$. In view of the above, it might be true that the rate of the generalized NAG-C for minimizing the squared gradient norm can be improved to

We leave the confirmation or disconfirmation of this asymptotic result for future research.

## Discussion

In this paper, we have proposed high-resolution ODEs for modeling three first-order optimization methods---the heavy-ball method, NAG-SC, and NAG-C. These new ODEs are more faithful surrogates for the corresponding discrete optimization methods than existing ODEs in the literature, thus serving as a more effective tool for understanding, analyzing, and generalizing first-order methods. Using this tool, we identified a term that we refer to as "gradient correction" in NAG-SC and in its high-resolution ODE, and we demonstrate its critical effect in making NAG-SC an accelerated method, as compared to the heavy-ball method. We also showed via the high-resolution ODE of NAG-C that this method minimizes the squared norm of the gradient at a faster rate than expected for smooth convex functions, and again the gradient correction is the key to this rate. Finally, the analysis of this tool suggested a new family of accelerated methods with the same optimal convergence rates as NAG-C.

The aforementioned results are obtained using the high-resolution ODEs in conjunction with a new framework for translating findings concerning the amenable ODEs into those of the less "user-friendly" discrete methods. This framework encodes an optimization property under investigation to a continuous-time Lyapunov function for an ODE and a discrete-time Lyapunov function for the discrete method. As an appealing feature of this framework, the transformation from the continuous Lyapunov function to its discrete version is through a phase-space representation. This representation links continuous objects such as position and velocity variables to their discrete counterparts in a faithful manner, permitting a transparent analysis of the three discrete methods that we studied.

There are a number of avenues open for future research using the high-resolution ODE framework. First, the discussion of Section 5 can carry over to the heavy-ball method and NAG-SC, which correspond to the high-resolution ODE

with $\beta = 0$ and $\beta = 1$, respectively. This ODE with a general $0 < \beta < 1$ corresponds to a new algorithm that can be thought of as an interpolation between the two methods. It is of interest to investigate the convergence properties of this class of algorithms. Second, we recognize that new optimization algorithms are obtained in \[, \] by using different discretization schemes on low-resolution ODE. Hence, a direction of interest is to apply the techniques therein to our high-resolution ODEs and to explore possible appealing properties of the new methods. Third, the technique of dimensional analysis, which we have used to derive high-resolution ODEs, can be further used to incorporate even higher-order powers of $\sqrt{s}$ into the ODEs. This might lead to further fine-grained findings concerning the discrete methods.

More broadly, we wish to remark on possible extensions of the high-resolution ODE framework beyond smooth convex optimization in the Euclidean setting. In the non-Euclidean case, it would be interesting to derive a high-resolution ODE for mirror descent \[, \]. This framework might also admit extensions to non-smooth optimization and stochastic optimization, where the ODEs are replaced, respectively, by differential inclusions \[ORX^+^16, \] and stochastic differential equations \[ HMC^+^18, \]. Finally, recognizing that the high-resolution ODEs are well-defined for non-convex functions, we believe that this framework will provide more accurate characterization of local behaviors of first-order algorithms near saddle points \[JGN^+^17, DJL^+^17, \]. On a related note, given the centrality of the problem of finding an approximate stationary point in the non-convex setting \[ \], it is worth using the high-resolution ODE framework to explore possible applications of the faster rate for minimizing the squared gradient norm that we have uncovered.
