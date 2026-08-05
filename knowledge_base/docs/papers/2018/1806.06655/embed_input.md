<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond Convexity - Contraction and Global Convergence of Gradient Descent

Topics include Convex optimization, Gradient descent, Natural gradients, Online algorithms, Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers the analysis of continuous time gradient-based optimization algorithms through the lens of nonlinear contraction theory. It demonstrates that in the case of a time-invariant objective, most elementary results on gradient descent based on convexity can be replaced by much more general results based on contraction. In particular, gradient descent converges to a unique equilibrium if its dynamics are contracting in any metric, with convexity of the cost corresponding to the special case of contraction in the identity metric. More broadly, contraction analysis provides new insights for the case of geodesically-convex optimization, wherein non-convex problems in Euclidean space can be transformed to convex ones posed over a Riemannian manifold. In this case, natural gradient descent converges to a unique equilibrium if it is contracting in any metric, with geodesic convexity of the cost corresponding to contraction in the natural metric. New results using semi-contraction provide additional insights into the topology of the set of optimizers in the case when multiple optima exist. Furthermore, they show how semi-contraction may be combined with specific additional information to reach broad conclusions about a dynamical system. The contraction perspective also easily extends to time-varying optimization settings and allows one to recursively build large optimization structures out of simpler elements.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensions to natural primal-dual optimization and game-theoretic contexts further illustrate the potential reach of these new perspectives.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% Additional Equal Contribution Note% Also use this double-dagger symbol for special authorship notes, such as senior authorship.%\ddag These authors also contributed equally to this work.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% Current address notes%\textcurrency Current Address: Dept/Program/Center, Institution Name, City, State, Country % change symbol to "\textcurrency a" if more than one current address note% \textcurrency b Insert second current address% \textcurrency c Insert third current address% Deceased author note% Group/Consortium Author Note%\textpilcrow Membership list can be found in the Acknowledgments section.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% Use the asterisk to denote corresponding authorship and provide email address in note below.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% Please keep the abstract below 300 words This paper considers the analysis of continuous time gradient-based optimization algorithms through the lens of nonlinear contraction theory. It demonstrates that in the case of a time-invariant objective, most elementary results on gradient descent based on convexity can be replaced by much more general results based on contraction. In particular, gradient descent converges to a unique equilibrium if its dynamics are contracting in any metric, with convexity of the cost corresponding to the special case of contraction in the identity metric. More broadly, contraction analysis provides new insights for the case of geodesically-convex optimization, wherein non-convex problems in Euclidean space can be transformed to convex ones posed over a Riemannian manifold. In this case, natural gradient descent converges to a unique equilibrium if it is contracting in any metric, with geodesic convexity of the cost corresponding to contraction in the natural metric. New results using semi-contraction provide additional insights into the topology of the set of optimizers in the case when multiple optima exist. Furthermore, they show how semi-contraction may be combined with specific additional information to reach broad conclusions about a dynamical system.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The contraction perspective also easily extends to time-varying optimization settings and allows one to recursively build large optimization structures out of simpler elements. Extensions to natural primal-dual optimization and game-theoretic contexts further illustrate the potential reach of these new perspectives.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This paper considers the analysis of continuous-time gradient-based optimization through the lens of nonlinear contraction theory. It is motivated, in part, by recent observations in machine learning that arise in the application of gradient descent (or its stochastic counterpart) for the training of over-parameterized networks. Modern networks often possess many more parameters than training examples and can fit the labels perfectly, resulting in submanifold valleys of the parameter space with equal cost. Moreover, recent results suggest that highly-redundant networks experience few to no local optima that are not global optima. These observations may be surprising in light of the fact that the loss landscapes for these problems are rarely convex.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Although convex problems admit provable globally optimal solutions, other broader classes of functions share this same property. For example, Invex functions guarantee that any local optimum is a global optimum, although the utility of invexity conditions remains a point of contention. Functions satisfying the Polyak-Lojasiewicz (PL) inequality give rise to exponentially convergent gradient descent to a provably optimal solution. While the PL condition is, in general, difficult to verify without an a-priori known globally optimal solution, the existence of zero-loss solutions in over-parameterized learning makes it tractable in important special cases. Geodesic convexity generalizes convexity to a Riemannian setting, with applicability to optimization on manifolds, as well as to conventional Euclidean settings where $\mathbb{R}^n$ is endowed with a manifold structure through the definition of a metric. Here, we consider another class of conditions for the convergence of gradient and natural gradient descent to a globally optimal point. We do so through adopting the perspective of nonlinear contraction theory and analyzing gradient descent in continuous time.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Contraction theory~ allows the stability of nonlinear non-autonomous systems to be characterized through linear time-varying dynamics describing the propagation of infinitesimally small displacements along the systems' flow. The existence of a Riemannian metric that contracts these virtual displacements (i.e., elements in the tangent space) is necessary and sufficient for exponential convergence of any pair of trajectories. Contraction naturally yields methods for constructing stable systems of systems, including synchronization phenomena and consensus as well as other key building blocks that allow the construction of large contracting systems out of simpler elements. These properties provide opportunities to construct larger optimization structures from simpler elements (e.g., in distributed or competitive optimization settings).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The contribution of this paper is to apply these contraction tools for the analysis of gradient and natural gradient optimization. We consider optimization problems posed over $\Rn$ wherein no explicit manifold structure necessarily exists a-priori. Instead, we consider the analysis of optimization following endowing these problems with additional structure (a Riemannian metric), analyzing their convergence, and considering the use of contraction tools to build larger optimization structures out of smaller ones. Analysis proceeds in continuous time. While this approach is limited, in part, by the fact that computational optimization algorithms require a discrete implementation, a continuous perspective has yielded insight on important phenomena such as in the analysis~, discrete implementations, and extensions of Nesterov's accelerated gradient descent method. It has also enabled analysis of primal-dual algorithms~, where an absolute time reference is obtained by introducing additional fast dynamics or delays using a singular perturbation framework. Recent results provide principled tools to derive discrete-time implementations that preserve specific continuous-time convergence rates.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The paper is organized as follows. Section~sec:Convex provides our main results, detailing the applicability of contraction theory to analyze gradient descent in continuous time. We show that convex functions represent the special case of contraction in the identity metric. The flexibility afforded by state-dependent contraction metrics, however, enables significant extra freedom for guaranteeing that all local optima are globally optimal. We then consider the extensions of these results to natural gradient descent, where geodesic convexity of a function corresponds to contraction of its natural gradient system in the natural metric. In both cases, results highlight the topology of the set of optimizers in the case of semi-contraction, which would have most direct applicability to over-parameterized networks. New results also show how semi-contraction may be combined with specific additional information to reach broad conclusions about a dynamical system. Section~GPD_opt details extensions of these results to the case of primal-dual type dynamics that appear in mixed convex/concave saddle systems, and shows how a broad class of natural adaptive control laws can be interpreted as a primal-dual system. Section sec:application discusses the special case of g-convex functions and associated combination properties for interfacing with other models.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Section sec:Conclusions provides an outlook on potential future advances that may stem from these connections.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Contraction Analysis of Gradient Systems} \label{sec:Convex} We first recall basic definitions and facts on convex optimization and show how a contraction analysis of gradient-based optimization considerably generalizes the class of functions that admit a unique global optimum. Following this presentation, results are generalized to the case of geodesically-convex optimization, which is particularly suited to analysis via contraction tools.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Throughout this analysis, given a differentiable function $\h:\R^n \rightarrow \R^m$, we denote the Jacobian of $\h(\x)$ by \Jac{\h}{\x} = \begin{bmatrix} \Jac{\h}{x_1} & \cdots & \Jac{\h}{x_n} \end{bmatrix} \in \R^{m\times n} In the special case of a scalar-valued function $f:\R^n\rightarrow \R $ we denote the gradient of $f(\x)$ by \grad{f}{}(\x) = \left[\Jac{f}{\x} \right]\T \in \R^n and its Hessian by $\nabla^2f(\x)$. Unless otherwise stated, we assume all functions are sufficiently smooth such that derivatives of the necessary order exist and are continuous.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Before we embark on this discussion, let us note that of course, as illustrated, e.g., in~ and in the following example, continuous-time analysis tools in general may be used to conceptually illuminate the mechanisms involved in discrete-time algorithms. As this paper will show, contraction tools give particularly simple insights into important classes of optimization problems, such as, e.g., geodesically-convex optimization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The Polyak-Lojasiewicz (PL) inequality is one of the most general sufficient conditions for discrete-time gradient descent to exhibit linear convergence rates without strong convexity of the A function is said to satisfy the PL inequality if it has a (typically unknown) global minimum value $f^*$ and there exists a constant $\mu>0$ such that Consider gradient descent on the cost function $f(\x)$ from a continuous-time point of view, Using $ \ V= f(\x) - f^* \ $ as a Lyapunov-like function, and then requiring that $V$ converges exponentially with rate $\mu$, The inequality above is exactly the PL condition. Thus, we see that the PL condition is nothing but the condition for exponential convergence of the residual cost $ \ V= f(\x) - f^* \ $.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Similarly, imposing $\ \dot{V} \le - \mu \sqrt{V}\ $, corresponding to finite-time convergence (in time less than $\ 2 \sqrt{V}/\mu \ $), would require a modified PL-like condition \forall \x, \ \ \ \ \ \ \ \| \nabla f(\x) \|^2 \ \ge \ \mu \ \sqrt{ f(\x) - f^*} while imposing $\ \dot{V} \le - \mu V^2\ $ would require \forall \x, \ \ \ \ \ \ \ \| \nabla f(\x) \|\ \ge \ \sqrt{\mu} \ (f(\x) - f^*) By comparison, the results pursued via contraction analysis in this paper will ensure exponential convergence of any pair of trajectories for gradient descent, but likewise will ensure convergence of those solutions to a global optimum.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Relationships Between Convexity and Contraction} \label{sec:contractAndGradient} \begin{definition}[Strong Convexity] \label{def:strongConv} A twice differentiable function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is $\alpha$-strongly convex with $\alpha>0$ if its Hessian matrix $\nabla^2{f}{}{}(\x)$ satisfies the matrix inequality \nabla^2{f}(\x) \succeq \alpha\, \mathbf{I} \quad \quad \forall \x \in \mathbb{R}^n As its name suggests, a function that is strongly convex is convex in the usual sense, while the converse is not always true.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Paper Body", "weight": 1.0} -->

From a dynamic systems perspective, strong convexity provides exponential convergence of gradient flows: \begin{proposition}[Exponential Convergence of Gradient Systems for Strongly Convex Functions] \label{prop:euc_grad_desc} \ If a twice differentiable function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is $\alpha$-strongly convex, then its gradient system \label{eq:grad_descent} converges to the unique global minimum of $f$ exponentially with rate $\alpha$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Toward proving this proposition, we will consider stability analysis through the application of nonlinear contraction theory.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[Contraction Metric~] \label{def:contraction} A system $\dot{\x} = \h(\x,t)$ is said to be contracting at rate $\alpha>0$ with respect to a symmetric positive definite metric $\M: \Rn \rightarrow \R^{n\times n}$, if for all $t \in \R$ and all $\x \in \Rn $, \dot{\M} + \A\T\, \M + \M\, \A \preceq -2 \alpha \M \label{eq:contraction_condition} where $\A(\x,t) = \Jac{\h}{\x}$ is the system Jacobian and $\dot{\M}= \sum_i \left(\partial \M / \partial x_i \right) h_i(\x,t)$. The system is said to be semi-contracting with respect to $\M$ when eq:contraction_condition holds with $\alpha=0$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Given an $\alpha$-contracting system and an arbitrary pair of initial conditions $\x_1$ and $\x_2$, the solutions $\x_1(t)$ and $\x_2(t)$ converge to one another exponentially \begin{equation}\label{d_M} d_{\mathcal{M}}(\x_1(t), \x_2(t)) \ \le \ {\rm e}^{-\alpha t} \ d_{\mathcal{M}}(\x_1, \x_2) \ \where $d_{\mathcal{M}}(\cdot,\cdot)$ denotes the geodesic distance on the Riemannian manifold $\mathcal{M} = (\Rn, \M)$. This property can be shown by considering the evolution of differential displacements $\delta \x$, which describe the evolution of nearby trajectories and coincide with the notion of virtual displacements in Lagrangian mechanics.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Paper Body", "weight": 1.0} -->

More precisely, letting $\x(t;\x_0, t_0)$ denote the solution of $\dot{\x} = \h(\x,t)$ from initial condition $\x(t_0) = \x_0$, differential displacements evolve according to \delta \x(t) = \frac{ \partial \x(t; \x_0, t_0) }{\partial \x_0} \ \delta \x(t_0) Property~d_M follows from the evolution of the squared length of these differential displacements~, which verifies \begin{equation}\label{ddt_z^2} \dd{}{t} (\delta \x\T \M \delta \x) \le - 2 \alpha (\delta \x\T \M \delta \x) Furthermore, if a system is $\alpha$-contracting in a metric $\M$ that satisfies $\M(\x)\succeq \beta \mathbf{I}$ uniformly for some constant $\beta>0$, then any two solutions verify \|

<!-- chunk {"id": "body-0026", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\x_1(t) - \x_2(t) \| \ \le \ \frac{1}{\sqrt{\beta}} \ {\rm e}^{-\alpha t} d_{\mathcal{M}}(\x_1, \x_2) Consider an $\alpha$-strongly convex function $f$ and its associated gradient descent system~eq:grad_descent.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since $f$ is strongly convex, it has a unique global minimum $\x^*$, which is a equilibrium point of eq:grad_descent. It can be verified that the gradient descent dynamics of $f$ are contracting in the identity metric $\M = {\bf I}$ with rate $\alpha$. Since geodesic distances are just Euclidean distances in this metric,~d_M immediately implies that thus proving Proposition~prop:euc_grad_desc.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Paper Body", "weight": 1.0} -->

From this example, it is clear that strongly convex functions are a special case of ones whose gradient systems are contracting. The following proposition shows that one does not lose the convergence properties to a global optimum on this more general class of functions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition}[Exponential Convergence of Contracting Gradient Systems] \label{prop:contracting_grad_desc} Consider again gradient descent as in equation eq:grad_descent. The system converges exponentially to a unique global minimum if it is contracting in \emph{some} metric.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof} Because eq:grad_descent is autonomous and contracting, it converges exponentially to a unique equilibrium $\x^\star$. Furthermore, this equilibrium must be a global minimum since $f$ can only decrease along trajectories, with $\ \dot{f} = - \grad{f}{}(\x)\T \ \grad{f}{}(\x) \ < \ 0\ $ for The above result, which emphasizes contraction rather than convexity as a sufficient condition to converge to a global minimum, can be extended to the semi-contracting case as follows.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition}[Asymptotic Convergence of Semi-Contracting Gradient Systems] \label{prop:SemiGrad} Consider a twice differentiable function $f: \mathbb{R}^n \rightarrow \mathbb{R}$, a symmetric positive definite metric $\M: \mathbb{R}^n \rightarrow \mathbb{R}^{n \times n}$, and the associated gradient system \dot{\x} = -\grad{f}{}(\x) \label{eq:grad_auton} Assume that dynamics eq:grad_auton is semi-contracting in \emph{some} metric, and furthermore that one trajectory of the system is known to be bounded.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then, (a) $f$ has at least one stationary point, (b) any local minimum of $f$ is a global minimum, (c) all global minima of $f$ are path-connected, and (d) all trajectories asymptotically converge (a) By assumption, there exists some initial condition $\x_0$ such that $\x(t; \x_0)$ remains bounded. This, in turn, implies that the $\omega$-limit set $\omega[\x(t;\x_0)]$ is non-empty, compact, forward invariant, and that d(\x(t;\x_0), \omega[\x(t;\x_0)]) \rightarrow 0 ~{\rm \ as~ \ }t\rightarrow + \infty Let $\x^*$ denote an element of $\omega[\x(t;\x_0)]$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since eq:grad_auton is a gradient system, Theorem 15.0.3 of guarantees that $\x^*$ must be an equilibrium point of eq:grad_auton. This proves that $f$ has at least one stationary point.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let us now show that $\omega[\x(t;\x_0)]$ consists only of the single point $\x^*$, by contradiction. Let $\x_1^*$ and $\x_2^*$ be distinct elements in $\omega[\x(t;\x_0)]$. Further let $\epsilon = d_\M(\x_1^*, \x_2^*)$ the geodesic distance between $\x_1^*$ and $\x_2^*$. Then, the geodesic balls $\mathcal{B}_1: = \mathcal{B}_{\M}(\x_1^*,\frac{\epsilon}{3})$ and $\mathcal{B}_{\M}(\x_2^*,\frac{\epsilon}{3})$ are disjoint. Further, since the system is semi-contracting these geodesic balls are forward invariant.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Yet, since $\x_1^*$ a limit point, $\x(t;\x_0)$ arrives within $\mathcal{B}_1$ at some point, and never leaves. Likewise, since $\x_2^*$ is a limit point, $\x(t;\x_0)$ arrives within $\mathcal{B}_2$ at some point, and never leaves. Thus, we have a contradiction, and the limit set must consist of a single point.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Paper Body", "weight": 1.0} -->

(b) and (c): Consider now two equilibrium points of eq:grad_auton, $\x_1^*$ and $\x_2^*$, and a smooth path $\bgamma(s)$ such that $\bgamma = \x^*_1$ and $\bgamma = \x^*_2$. Since the gradient dynamics are semi-contracting, for each $s$ the solution $\x(t;\bgamma(s))$ remains bounded. Thus, by the same reasoning as above, each $\x(t;\bgamma(s))$ converges to some equilibrium $\x^*(s)$ as $t\rightarrow + \infty$. Since $\nabla f(\x^*(s)) =0$ for each $s$, and $\x^*(s)$ smoothly connects $\x^*_1$ and $\x_2^*$, it follows that $f(\x_1^*) = f(\x_2^*)$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Paper Body", "weight": 1.0} -->

That is, all solutions converge to the same value for $f$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Paper Body", "weight": 1.0} -->

(d): That all solutions of eq:grad_descent asymptotically converge to a global minimum of $f$ follows from that fact that $f$ decreases along all solutions, and all solutions converge to the same value for $f$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{remark} In the case that a contraction metric needs to be found numerically, note that the conditions eq:contraction_condition for certifying contraction or semi-contraction are convex criteria. Thus, in many instances, the process of finding a metric numerically to verify contraction may be accomplished via convex optimization approaches, such as those based on sums-of-squares programming~.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Relationship Between Geodesic Convexity and Contraction} Geodesic convexity generalizes conventional notions of convexity to the case where the domain of a function is equipped with a Riemannian metric. A special case occurs in geometric programming (GP)~. In GP, a non-convex problem over positive variables $\{x_i\}_{i=1}^N$ can be transformed into a convex problem by a change of variables $y_i = {\rm log}(x_i)$. Alternately GP can be formulated over the positive reals viewed as a Riemannian manifold by measuring differential length elements $ds$ in a relative sense ds^2 = \sum_{i=1}^N \left(\frac{dx_i}{x_i} \right)^2 = \sum_{i=1}^N dy_i^2 Geodesically-convex optimization generalizes this transformation strategy to a broader class of problems~. However, beyond special cases (see, e.g.,), generative procedures remain lacking to formulate g-convex optimization problems or recognize g-convexity.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To introduce g-convexity more formally, consider a function $f:\mathbb{R}^n \rightarrow \mathbb{R}$ and a positive definite metric $\M:\Rn \rightarrow \R^{n\times n}$. We note that geodesic convexity of $f$ is not an intrinsic property of the function itself, but rather is a property of $f$ defined on the Riemannian manifold $(\Rn, \M)$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[g-Strong Convexity] A twice differentiable function $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is said to be geodesically $\alpha$-strongly convex (with $\alpha>0$) in a symmetric positive definite metric $\M$ if its Riemannian Hessian matrix $\H(\x)$ satisfies: \H(\x) \succeq \alpha\, \M(\x)\quad \quad \forall \x \in \mathbb{R}^n The elements of the Riemannian Hessian are given as where $\pdd{f}{i}{j} = \frac{\partial^2 f}{\partial x_i \partial x_j}$ provide the elements of the conventional (Euclidean) Hessian and $\Gamma_{ij}^k$ denotes the Christoffel symbols of the second kind \Gamma_{ij}^m = \frac{1}{2} \sum_{k=1}^n \left[M^{mk}

<!-- chunk {"id": "body-0043", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The Riemannian Hessian generalizes the notion of the Hessian from a Euclidean context and captures the curvature of $f$ along geodesics. Likewise, the natural gradient generalizes the notion of a Euclidean gradient to the Riemannian context in the following sense.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{definition}[Natural Gradient] Consider $\Rn$ equipped with a Riemannian metric $\M$. The {\em natural} gradient of a differentiable function $f: \Rn \rightarrow \R$ is the direction of steepest ascent on the manifold and is given in coordinates by $ \ \M(\x)^{-1} \grad{f}{}(\x) \ $.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Paper Body", "weight": 1.0} -->

When $\M(\x)$ is the Hessian of some twice differentiable strictly convex scalar function $\psi(\x)$, natural gradient descent coincides with the continuous-time limit of mirror descent~ with potential $\psi(\x)$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{remark} From a differential geometric viewpoint, the first covariant derivative of $f$ is a covector field given in coordinates by $\grad{f}{}(\x)$, while the natural gradient is a vector field given in coordinates by $\M(\x)^{-1} \grad{f}{}(\x)$ ~. In a Euclidean context, where $\M(\x)$ is identity, this distinction between covariant (covector) and contravariant (vector) representations of the gradient is immaterial.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Similarly, the Riemannian Hessian $\vec{H}$ represents in coordinates the second covariant derivative of $f$.%, a tensor field.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Paper Body", "weight": 1.0} -->

When $\M$ is the identity metric, geodesic $\alpha$-strong convexity naturally coincides with the definition of $\alpha$-strong convexity in Definition~def:strongConv. The natural gradient can be used to directly mirror Proposition~prop:euc_grad_desc within the Riemannian context.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{theorem}[Equivalence between g-Strong Convexity and Contraction of Natural Gradient] \label{th_main} Consider a twice differentiable function $f: \mathbb{R}^n\times \mathbb{R} \rightarrow \mathbb{R}$, a symmetric positive definite metric $\M: \mathbb{R}^n \rightarrow \mathbb{R}^{n \times n}$, and the natural gradient system \dot{\x} = \h(\x,t) = -\M(\x)^{-1}\, \grad{f(\x,t)}{\x} \label{eq:NatGrad} Then, $f$ is $\alpha$-strongly g-convex in the metric $\M$ for each $t$ if and only if eq:NatGrad is contracting with rate $\alpha$ in the metric $\M$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Paper Body", "weight": 1.0} -->

More specifically, the Riemannian Hessian verifies \vec{H} = -\frac{1}{2}\left(\M \A + \A\T \M + \dot{\M} \right) Appendix 1 provides a self-contained proof using conventional tensor analysis methods~, whose relationship with contraction conditions have been noted previously. The same relationships drive coordinate-free versions of the result in~.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{remark} Theorem~th_main can also be viewed as a special case of contraction analysis for complex Hamilton-Jacobi dynamics~. A reorganization of eq:NatGrad as may be recognized as the generalized momentum being the negative covariant gradient within a Hamiltonian mechanics context. %This interpretation is consistent with $\H(\x)$ being the second covariant derivative of $f$~.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Paper Body", "weight": 1.0} -->

While Theorem th_main applies to $\alpha$-strong convexity, the link between the Riemannian Hessian and the contraction condition~eq:contraction_condition also provides immediate equivalence between g-convexity of a function and semi-contraction of its natural gradient dynamics.%, and between strict contraction and strict g-convexity. %As expected, a Equation eq:H provides an alternate way to compute the geodesic Hessian $\H$, and, as expected, leaves it invariant when the metric $\M$ is scaled by a strictly positive constant. Because of the structure of the natural gradient dynamics, scaling $\M$ is akin to scaling time and implies inversely scaling the contraction rate $\alpha$, consistently with~eq:Hessian.\\By contrast, note that given a \emph{fixed} dynamics $\h$, the contraction metric analyzing it can always be arbitrarily scaled while leaving the contraction rate unchanged.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Similar to in Section~sec:contractAndGradient where convexity corresponded to contraction of gradient in the identity metric, we likewise see that Thm.~th_main imposes g-convexity via a particular choice of contraction metric for the natural gradient dynamics. Mirroring Prop.~prop:contracting_grad_desc, removing this restriction on the contraction metric leads to significant additional flexibility for guaranteeing convergence to a globally optimal point.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition}[Exponential Convergence of Contracting Natural Gradient Systems] \label{prop:contracting_Natgrad_desc} Consider again natural gradient descent as in equation eq:NatGrad. The system converges exponentially to a unique global minimum if it is contracting in \emph{some} metric.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The proof follows immediately from the same logic as the proof of Proposition~prop:contracting_grad_desc.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{rem:robust} Note that contraction also provides robustness. Consider perturbed dynamics $\dot{\x} = \h(\x,t) + \bd(t)$ with $\sqrt{ \bd(t)\T \M(\x) \bd(t) } < R$ uniformly. If the dynamics are contracting with rate $\lambda$, then all trajectories contract to a geodesic ball of radius $R/\lambda$. This observation implies favorable properties for algorithms where an exact gradient may be difficult or intractable to compute, with approximation methods used in their place.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{theorem}[Semi-Contraction for Natural Gradient] \label{thm:natGradNonStrict} Consider a twice differentiable function $f: \mathbb{R}^n \rightarrow \mathbb{R}$, a symmetric positive definite metric $\M: \mathbb{R}^n \rightarrow \mathbb{R}^{n \times n}$, and the associated natural gradient system \dot{\x} = - \M(\x)^{-1} \grad{f}{}(\x) \label{eq:nat_grad_auton} Assume that dynamics eq:nat_grad_auton is semi-contracting in \emph{some} metric, and furthermore that one trajectory of the system is known to be bounded.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then, (a) $f$ has at least one stationary point, (b) any local minimum of $f$ is a global minimum, (c) all global minima of $f$ are path-connected, and (d) all trajectories asymptotically converge The proof follows the exact same line of logic as the proof to Prop.~prop:SemiGrad. The result of Theorem 15.0.3 of, which guarantees that any $\omega$-limit point of gradient descent eq:grad_auton is an equilibrium point, generalizes immediately to the case of natural gradient descent eq:nat_grad_auton.%\pmw{Must just note that the result from Wiggins Chapter 15 generalizes immediately the the case of natural gradient.} \label{rem:bad_saddles} The topology of global optimizers satisfying this semi-contraction condition is the same as those observed when training over-parameterized networks~. However, empirical loss functions in these networks often also experience multiple saddle points.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The attractor sets associated with strict saddles have measure zero under discrete gradient descent with sufficiently small stepsize (i.e., with adequately close approximation to the continuous time case), while the dimensionality of the attractor sets can be further reduced via smoothed versions of the gradient.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Paper Body", "weight": 1.0} -->

While the presence of strict saddles precludes the ability of a gradient system to be globally semi-contracting, any of the results given here can be generalized to forward invariant contraction or semi-contraction regions~. In principle, saddles could then be treated by excluding their measure zero attractor sets from suitably chosen contraction or semi-contraction regions.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The topology of equilibria in semi-contracting gradient systems immediately implies the following result.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{corollary}\label{think_locally} Consider an autonomous, semi-contracting natural gradient system. If the linearization at some equilibrium point is strictly stable, then all system trajectories tend to this global minimizer.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Paper Body", "weight": 1.0} -->

More generally, if some equilibrium is locally asymptotically stable, all trajectories tend to this global minimizer.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proof} We prove the second part, the first then follows directly from Lyapunov's linearization method. Existence of an equilibrium implies existence of a bounded trajectory. Furthermore, by definition, there exists a ball around the equilibrium point $\x^\star$ such that all trajectories initiated in that ball tend to $\x^\star$. If there was another equilibrium, the path connecting it to $\x^\star$ would intersect that ball, which is a contradiction since the path is itself composed of equilibria via Thm.~thm:natGradNonStrict.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{rem:JacobianOfSemi} Strict stability of a natural gradient system at an equilibrium point can of course be established simply by ensuring that all eigenvalues of its Jacobian at this point are strictly in the left-half complex plane. This condition is equivalent to requiring that the Hessian of the objective function is positive definite at $\x^\star$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that this condition is equivalent to the geodesic Hessian at $\x^\star$ being positive definite in any metric, as the Euclidean Hessian is numerically equal to the geodesic Hessian in any metric in this case, due to all terms multiplying the Christoffel symbols in eq:riemhessian being zero.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{corollary} Consider an autonomous semi-contracting natural gradient system, and assume that the system has more than one equilibrium. Then, at any equilibrium, both the Jacobian matrix of the dynamics and the Hessian of the objective have at least one zero eigenvalue.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider an equilibrium $\x^\star$, and an equilibrium path connecting it to some other equilibrium. The unit tangent vector at $\x^\star$ along this path is an eigenvector of the Jacobian with eigenvalue zero. Given the algebraic relation between the Jacobian and the objective Hessian pointed out in Remark~rem:JacobianOfSemi, this shows in turn that the objective Hessian has a zero eigenvalue.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Let us illustrate Theorem~th_main using the classical nonconvex Rosenbrock function: This function has a unique global optimum at $\x^*=\T$, which is located along a long, shallow, parabolic-shaped valley. %As a result, it exhibits poor scaling and is frequently used as a test problem for optimization.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider the Rosenbrock function eq:rosenbrock and the metric \end{bmatrix} %\ {\color{red} \ge \... \ }\ > \ {\bf 0} The metric $\M(\x)$ satisfies ${\rm tr}(\M(\x))= 400 x_1^2 + 101>0$ and ${\rm det}(\M(\x)) = 100>0$, and thus $\M(\x)\succ0$. Note that $\M(\x)$ is not the Hessian of $f(\x)$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The natural gradient dynamics follows \dot{\x} = \h(\x)= - \M(\x)^{-1} \grad{f}{}(\x) = -2 \begin{bmatrix} x_1 -1 \\ x_1^2 - 2 x_1 + x_2 \end{bmatrix} It can be verified algebraically that \M \left(\Jac{\h}{\x} \right) + \left(\Jac{\h}{\x}\right)\T \M + \dot{\M} = -4 \M which shows that natural gradient descent is contracting with rate $\alpha=2$. This implies that the natural gradient dynamics satisfy where $\x^* = \T$. Equivalently, the Rosenbrock function is geodesically $\alpha$-strongly convex with $\alpha = 2$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The Rosenbrock metric $\M(\x)$ can be viewed as following from a differential change of variables \delt{z} = \boldsymbol{\Theta}(\x) \delt{x} = \begin{bmatrix} 20 x_1 & -10 \\ 1 & 0 \end{bmatrix} \delt{x} where $\M=\boldsymbol{\Theta}\T\boldsymbol{\Theta}$ yields $\ \delt{x}\T\M\delt{x} = \delt{z}\T \delt{z}$. This differential change of variables is integrable, so that g-convexity of the Rosenbrock can be shown using the explicit nonlinear coordinate change $z_1 = 10 x^2_1 - 10 x_2$ and $z_2 = x_1-1$ that provides $f = z_1^2 + z_2^2$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{example} \label{psi} Mirror descent provides another example of a metric corresponding to an explicit state transformation, with Newton's method as a special case.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider a twice differentiable scalar objective function $f(\x)$, and a smooth strictly convex scalar function $\psi(\x)$. Denoting by $\H_f(\x) = \nabla^2 f(\x)$ and $\H_\psi = \nabla^2 \psi$ the Hessians of these functions, continuous-time mirror descent of $f(\x)$ under potential $\psi(\x)$ corresponds to natural gradient in the Hessian metric $\H_\psi$ \dot{\x} = - \H_\psi^{-1} \nabla f(\x) Consider the explicit change of variables $\z = \nabla \psi(\x)$, which can be written in differential form as $\ \delta \z = \H_\psi \delta \x$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The dynamics eq:mirror_in_x can be viewed in the mirror space as \begin{equation}\nonumber \dot{\z} = \H_\psi \, \dot{\x} = - \nabla f(\x) \begin{equation}\nonumber Letting $\M(\x) = \H_\psi^2$, this yields \begin{equation}\nonumber \dd{}{t} \left[\delta \x^T \M(\x) \delta \x \right] = \dd{}{t} \left[\delta \z^T \delta \z \right] = - \delta \x\T \left[\H_f \H_\psi + \H_\psi \H_f \right] \delta \x\T Thus, continuous mirror descent eq:mirror_in_x is contracting with rate $\lambda > 0$ in the metric $\M(\x) = \H_\psi^2$ if \H_f \H_\psi + \H_\psi \H_f \succeq 2 \lambda

<!-- chunk {"id": "body-0076", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\H_\psi^2 In the particular case when $f$ is $\alpha$-strongly convex and the potential function is chosen as $\psi(\x) = f(\x)$, equation eq:mirror_in_x simply corresponds to Newton's method, and eq:contractionConditionMirror verifies that Newton's method is contracting with rate 1 in the squared Hessian metric $\M(\x) = \H_f^2(\x)$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that the well-known result that the transformation $\z = \grad{\phi}{}(\x)$ is one-to-one (given the strict convexity of $\psi$) can also be shown by constructing, for a given $\z$, the system \dot{\x} + \grad{\psi}{}(\x) = \z \label{eq:InvertGrandientViaDynamics} which is autonomous and contracting in the identity metric and thus must reach a unique equilibrium point.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The following proposition provides further insight into the case when the contraction metric is related to an explicit change of variables more generally.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition}[Relationship between gradient and natural gradient under a diffeomorphic change of variables]\label{change_variable} Consider a diffeomorphic change of variables $\z = \g(\x)$, and the associated metric $\M(\x) =\boldsymbol{\Theta}(\x)\T \boldsymbol{\Theta}(\x)$, with $\boldsymbol{\Theta}(\x) = \jac{\g}{\x}$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\right]\T \\label{prop:curvature} Consider a metric $\M(\x)$ and suppose there exists a diffeomorphic change of variables $\z = \g(\x)$ such that $\M(\x) =\boldsymbol{\Theta}(\x)\T \boldsymbol{\Theta}(\x)$, with $\boldsymbol{\Theta}(\x) = \jac{\g}{\x}$. Then, the associated Riemannian curvature tensor with components $R_{ik\ell m}$ must be identically zero.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that since $\delta \z = \boldsymbol{\Theta}(\x) \delta \x$, it follows that $\delta \z\T \delta \z = \delta \x\T \M(\x) \delta \x$ and thus the Riemannian metric tensor expressed in the $\z$ coordinates is the identity. Since the components of the Riemannian metric tensor are constant in these transformed coordinates, it follows that the components of the Riemannian curvature tensor are identically zero. Transformation laws for tensors ensure that the components of the curvature tensor remain zero under arbitrary coordinate change, thus $R_{ik\ell m}=0$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The general freedom to consider differential changes of coordinates $\delta \z = \boldsymbol{\Theta}(\x) \delta \x$ where $\boldsymbol{\Theta}$ is non-integrable provides additional flexibility and generality to both contraction analysis and g-convexity, as illustrated by the following examples.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider the non-convex function which has a global minimum at $\x=\mathbf{0}$. Contours of the function are shown in Fig.~fig:DescentContracting. Gradient descent \dot{\x} = - \nabla f(\x) = -2 \begin{bmatrix} x_1 (1+x_2^2) \\ x_2 (1+x_1^2) \end{bmatrix} can be shown to be contracting at rate $\lambda=2$ in the metric \M(\x) = \begin{bmatrix} 2+x_1^2 & \ -x_1 x_2 \\ -x_1 x_2 & \ 2+x_2^2 \end{bmatrix} Fig.~fig:DescentContracting shows two solutions and plots their geodesic distance. The decay is, as expected, at a rate faster than the exponentially decreasing upper bound as derived from d_M.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The curvature tensor for this metric has some non-zero components, From Proposition prop:curvature, this shows that this metric cannot be derived from an explicit change of coordinates.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\includegraphics[width=\columnwidth]{SimResults-crop1.pdf} \caption{Contracting gradient descent corresponding to Example ex:DescentContracting.} \label{fig:DescentContracting} Consider the function and natural gradient descent with a given natural metric $ \boldsymbol{\Theta}(\z)\T \boldsymbol{\Theta}(\z)$, where \boldsymbol{\Theta}(\z) = \begin{bmatrix} 1 & 0 \\This natural gradient dynamics is verified semi-contracting in the metric \M(\z) = \boldsymbol{\Theta}(\z)\T \begin{bmatrix} 1 + z_2^2 - 2 z_1^3 z_2 + z_1^6 & 0 \\0 & 1 + z_1^2 \end{bmatrix} \boldsymbol{\Theta}(z) Similar to Example~ex:DescentContracting, this metric has non-zero Riemannian curvature, and thus cannot be derived from a change of coordinates.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Figure~fig:SemiDescent shows the contours of $f$ and two solutions of natural gradient descent. Figure fig:SemiDescentFunction shows that the the geodesic distance between these two solutions is non-increasing. Since the system is only semi-contracting, the distance between solutions does not tend toward zero. It can be verified that $f$ is a sum of squares and thus $f(\z)\ge0$, and that $f(\z)=0$ when $z_2 = z_1^3-z_1$. Both initial conditions asymptotically lead to this path connected set of global optima.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\includegraphics[width=\columnwidth]{SimResults-crop2.pdf} \caption{Semi-Contracting Natural Gradient Descent for Example~ex:semiDescent. } \label{fig:SemiDescent} \includegraphics[width=\columnwidth]{SemiFunc-crop.pdf} \caption{Semi-Contracting Natural Gradient Descent for Example~ex:semiDescent. } \label{fig:SemiDescentFunction} Geodesically-convex optimization can also be used to carry out manifold-constrained optimization in an unconstrained fashion via recasting problems over a Riemannian manifold directly. Taking an intrinsic view of the manifold, coordinate free results are available, however, for the purposes of computation, we assume a global coordinate chart here.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider for instance optimization over the set $\mathbb{S}^n_+$ of $n\times n$ positive definite matrices, and specifically the problem of finding the Karcher mean of $m$ matrices $\A_i \in \mathbb{S}^n_+$, which minimizes the objective function f(\X) = \frac{1}{2}\sum_{i=1}^m\| {\rm log}(\A_i^{-1}\,\X) \|_F^2 where $\|\A\|_F=\sqrt{{\rm tr}(\A\T \A)}$ denotes the Frobenius norm of a matrix $ \A$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The function $f(\X)$ is $m$-strongly convex~ on $\mathbb{S}^n_+ \ $in the metric that measures symmetric differential displacements as ds^2 = {\rm tr}\left(\left(\delta \X \ \X^{-1} \right)^2 \right) \label{eq:PSD_Riem} Naturally, the requirement that $\delta \X$ be symmetric makes it an element of the tangent space to the manifold of symmetric positive definite matrices.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This metric generalizes the GP case eq:GP_Gconvex, and coincides with the second-order terms in the Taylor series of the log barrier $-{\rm logdet}(\X)$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The gradient of $f(\X)$ can be written \grad{f}{}(\X) = \sum_{i=1}^m {\rm log}(\A_i^{-1}\,\X)\, \X^{-1} and accordingly the natural gradient can be shown to satisfy \sum_{i=1}^m \ \X \, {\rm log}(\A_i^{-1}\,\X) = \X \, \grad{f}{}(\X) \, \X From Theorem th_main, any trajectory with arbitrary initial condition $\X \in \mathbb{S}^n_+$ will remain within $\mathbb{S}^n_+$ under the natural gradient descent dynamics \dot{\X} = - \sum_{i=1}^m \ \X \, {\rm log}(\A_i^{-1}\,\X) since (intuitively) the Riemannian metric eq:PSD_Riem makes any element on the boundary of the positive definite cone an infinite

<!-- chunk {"id": "body-0092", "role": "body", "section": "Paper Body", "weight": 1.0} -->

distance away from any one in the interior, and contraction of the natural gradient dynamics ensures that geodesic distances decrease exponentially.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Paper Body", "weight": 1.0} -->

An approximation to the Riemannian distance of two positive definite (PD) matrices on the PD cone is given by the Bregman LogDet divergence on $\mathbb{S}_+^n$ The metric is convex in its first argument, and can be shown to be geodesically convex in the second. We illustrate the connection with contraction to show this property.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that so that the natural gradient descent dynamics are simply \dot{\X} = - \X \left[\grad{d(\A||\X)}{\X} \right] \X = -\X + \A with differential dynamics \delta \dot{\X} = - \delta \X where the differential displacement $\delta \X$ must be symmetric.%{\color{blue} Comment about $\delta \X$ being symmetric, so that tangent space is not an issue.} Considering the rate of change in length of these differential displacements and defining the differential change of variables $\delta \Z = \X^{-\frac{1}{2}}\, \delta \X \, \X^{-\frac{1}{2}}$, one has $\tr{ \delta \Z^2} = {\rm tr}\left((\X^{-1} \, \delta \X)^2 \right) $ and for all $\delta \Z\ne \mathbf{0}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Hence, considering only the second argument to LogDet divergence, its Riemannian Hessian is positive definite, thus proving g-convexity via Thm.~th_main.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Non-autonomous Systems and Virtual Systems} In our optimization context, the fact that contraction analysis is directly applicable to non-autonomous systems can be exploited in a variety of ways. As we shall detail later, a key aspect is that it allows feedback combinations or hierarchies of contracting modules to be exploited to address more elaborate optimization problems or architectures. Also, it makes the construction of \emph{virtual} systems~ possible to potentially extend results beyond natural-gradient descent.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{remark} The natural gradient $\ \M^{-1}(\x)\ \grad{f}{\x}(\x,t)$ represents the direction of steepest ascent on the manifold at any given time. With this in mind, Remark~rem:robust on robustness enables convergence analysis for natural gradient descent within time-varying optimization contexts~. Let $\x^*(t)$ denote the optimum of a time-varying $\alpha$-strongly g-convex function. If $\sqrt{\dot{\x}^*(t)\T \M(\x) \dot{\x}^*(t)}<R$, then the natural gradient will track $\dot{\x}^*(t)$ with accuracy $R/\alpha$ after exponential transient.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider a contracting natural gradient system of the form eq:NatGrad. In the autonomous case, equations governing the differential displacement follow \begin{equation}\label{delta_x} \dd{}{t} \ \delta \x \ = \ \Jac{\h}{\x} \ \delta \x which has a similar structure to the time evolution of $\h(\x)$ \begin{equation}\label{ddt_h} \dd{}{t} \ \h(\x) \ = \ \left(\grad{ \h}{}(\x) \right) \ \h(\x) Thus, for natural gradient descent of an $\alpha$-strong g-convex function $f(\x)$, the same algebra leading to~ddt_z^2 also gives so that the Krasovskii-like function can be viewed as an exponentially converging Lyapunov function, with global minimum $V=0$ at the unique minimum of $f(\x)$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Of course, delta_x remains valid for \emph{non-autonomous} systems as well, while~ddt_h does not.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% \subsection{Virtual Systems} The use of virtual contracting systems~ allows guaranteed exponential convergence to a unique minimum to be extended to classes of dynamics which are not pure natural gradient. For instance, it is common in optimization to adjust the learning rate as the descent progresses. Consider a natural gradient descent with the function $f(\x)$ $\alpha$-strongly g-convex in metric $\M(\x)$, and define the new system where the smooth scalar function $p(\x,t)$ modulates the learning rate~ and is uniformly positive definite, \[\exists \ p_{min} > 0, \ \forall t \ge 0, \ \forall \x, \ \ \ \Let us show that this system tends exponentially to the minimum $\x^*$ of $f(\x)$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider the auxiliary, \emph{virtual} system, For this system, $p(\x(t),t)$ is an external, uniformly positive definite function of time, and thus so that the contraction of~eq:NatGrad with rate $\alpha$ implies the contraction of~virtual_p(x,t) with rate $ \ \alpha p_{min} \ $. Since both $\x(t)$ and $\x^*$ are particular solutions of~virtual_p(x,t), this implies in turn that $\x(t)$ tends to $\x^*$ with rate $ \ \alpha p_{min} \ $.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Paper Body", "weight": 1.0} -->

%to the same global optimizer.%Thus, virtual_p(x,t) is contracting with metric $\M(\y)$, and furthermore both $\x(t)$ and the minimum of $f$ are particular solutions of its dynamics. This implies that $\x(t)$ tends exponentially to the unique minimum of $f$, with rate $\ p_{min} \alpha$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note that since we only assumed that $p(\x,t)$ is uniformly positive definite, in general the actual system~p(x,t) is not contracting with respect to the metric $\M(\x)$. %The approach extends immediately to the primal-dual context of Section~GPD_opt.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The learning rate may also be selected to improve the numerical properties of the algorithm in a discrete time implementation. For example, $p(\x,t)$ could vary as the inverse of the condition number of $\nabla^2 f(\x)$ to improve numeric conditioning without impact on stability guarantees.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Corollary~think_locally above points to a more general class of results where contraction or semi-contraction properties are combined with other information, such as a stable local linearization or a decreasing cost, to provide global results.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Contraction is attractive}%From local to global As we now show, Corollary~think_locally extends more generally to autonomous semi-contracting systems. An instance of this result in the case of an identity metric was derived in~.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition} \label{7} Consider an autonomous system semi-contracting in a bounded metric $\M(\x)$, {\bf 0} \prec \bl^2 \I \preceq \M(\x) \preceq \bu^2 \I \quad \quad \forall \x If a system equilibrium is locally asymptotically stable, then it is globally asymptotically stable. In particular, if the system linearization at some equilibrium point is strictly stable, then all system trajectories tend to this equilibrium.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The result is a particular case of Theorem~3, to be \begin{theorem}\label{3} Consider a non-autonomous system, semi-contracting in a bounded metric $\M(\x)$, {\bf 0} \prec \bl^2 \I \preceq \M(\x) \preceq \bu^2 \I \quad \quad \forall \x Assume that a \emph{specific} trajectory $\x^\star(t)$ is locally attractive. Then all trajectories tend asymptotically to $\x^\star(t)$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In particular, if contraction holds (possibly in a different bounded metric) along a specific trajectory $\x^\star(t)$, and within a tube of constant size around it, then all trajectories tend asymptotically to $\x^\star(t)$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The first part generalizes the equilibrium argument from to arbitrary trajectories and arbitrary metrics. Assume that $\x^*(t)$ is locally attractive, by which we mean there exists some $\epsilon>0$ such that, for any initial time $t_0$ and initial condition $\x_0 \in \B_{ \mathbf{I}}(\x^*(t_0), \epsilon) $, one has $\x(t_0+T; \x_0, t_0) \rightarrow \x^*(t_0+T)$ as $T\rightarrow +\infty$. Without loss of generality, we assume $t_0= 0$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider some generic initial condition $\x_0$ with $\dI(\x_0, \x^*) > \epsilon$. We will argue that there is always a finite time window over which the geodesic distance from $\x(t;\x_0)$ to $\x^*(t)$ decreases by a fixed finite increment.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider a geodesic connecting $\x_0$ and $\x^*$ and denote by $\xl$ the unique point on this geodesic that is a geodesic distance $\bl \epsilon$ away from $\x^*$. Due to the uniform positive definiteness of $\M$, this condition implies that $\xl \in \B_{\mathbf{I}}(\x^*,\epsilon)$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Because of the local attractivity of $\x^*(t)$, there exists a time $t_1>0$ such that which further implies that In addition, since the system is semi-contracting, we have and so by the triangle inequality &\phantom{=}~~~~~~~~~~~ - d_\M(\x^*, \xl) + \bl \frac{\epsilon}{2} \\This implies that so long as $\dI(\x_0, \x^*) > \epsilon$, the trajectory from $\x_0$ will eventually decrease its geodesic distance by a fixed finite increment. Since this process can be repeated, it follows that there must exist some time $T$ such that $\x(T; \x_0) \in \B_{\mathbf{I}}(\x^*(T),\epsilon)$.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Paper Body", "weight": 1.0} -->

To complete the second part of the proof we proceed to show that if contraction eq:contraction_condition holds within a tube of constant size around trajectory $\x^*(t)$, for some bounded metric $(\beta_0^\star)^2 \I \preceq \M^\star(\x) \preceq (\beta_1^\star)^2 \mathbf{I} \ $ and some rate $\alpha^\star>0$, then that trajectory is locally attractive. By condition eq:contraction_condition holding within a tube we mean that there exists some $\epsilon >0$ such that eq:contraction_condition holds for any time $t$ and any $\x \in \B_\I(\x^*(t),\epsilon)$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Paper Body", "weight": 1.0} -->

From boundedness of the metric, we have \beta_0^\star \, d_{\I}(\x^*(t), \x) \le d_{\M^\star}(\x^*(t), \x) so that any initial condition $\x_0$ satisfying necessarily starts within this tube. Further, since eq:contraction_condition holds within the tube, it follows that the geodesic ball of radius $\epsilon \beta_0^\star$ around $\x^\star(t)$ is forward invariant. Since this ball is contained within a contraction region, this implies that for any $\x_0 \in \B_\M(\x^\star, \beta_0^\star \epsilon)$ which proves local asymptotic stability of $\x^\star(t)$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% Contraction implies that:% \begin{align}\nonumber% \dd{}{t} \left[\delta \x\T \M^\star(\x) \delta \x \right] &= \delta \x\T \left[\M^\star \A + \A \T \M^\star + \dot{\M}^\star \right] \delta \x\\% &\le -2 \alpha \ \delta \x\T \M^\star(\x) \delta \x \nonumber% for any differential displacement $\delta \x$ along the trajectory. [FALSE: Boundedness of $\x^*(t)$ implies that the negative definite matrix% $\M^\star \A + \A\T \M^\star + \dot{\M}^\star$% is uniformly bounded away from 0, and remains so within some $\epsilon>0$ neighborhood of the trajectory $\x^\star(t)$.]

<!-- chunk {"id": "body-0117", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The condition regarding contraction within a tube of fixed size is included to avoid pathological cases where the region of contraction shrinks to zero as $t\rightarrow +\infty$. For example, the system $\dot{x} = -x + t x^3$ is contracting with rate $1$ at the origin for all time, yet the origin is not locally asymptotically stable.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Intuitively, the result can be understood by analogy with a shrinking rope. Consider a path of initial conditions connecting $\x^\star$ to any $\x_0$. As this path flows forward in time, at $t=0$, only a portion of this path of states is within the basin of attraction for $\x^\star(t)$. Viewing this path as a rope, the semi-contraction property ensures that no part of the rope can increase in length as it flows forward through the dynamics. Yet, due to local attractivity at one end of the rope, a portion of it is guaranteed to have shrinking length, pulling the rest of the rope toward the the region of attraction.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Numerical tools for determining contraction metrics are based on the fact that contraction conditions eq:contraction_condition are convex in the metric {\em for a fixed contraction rate}. In practice, these methods often involve an outer search procedure for the contraction rate (e.g., via a binary search). In this sense, the use of semi-contraction is desirable as it does not require this additional search.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Paper Body", "weight": 1.0} -->

These results have analogs in the context of controller design using control contraction metrics (CCMs)~. In this setting, one can impose a semi-contracting closed-loop metric everywhere, except in a tube along a desired trajectory where a strict contraction condition would be required, possibly in a different metric. Since the existence of an exponential (resp. semi) CCM implies that the closed-loop plant can be rendered contracting (resp. semi-contracting), Theorem~3 would then imply asymptotic stabilizability of the desired trajectory.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This extension likewise has analogs for manifold convergence results and convergence to a limit cycle by transverse contraction~, both of which are special cases of CCM results applied to suitably constructed virtual control systems~. In either case, a semi-contracting CCM everywhere can be combined with a contracting CCM condition on the manifold (or limit cycle) and within a neighborhood of it to assert asymptotic stability of the manifold (or limit cycle). In the limit cycle case for autonomous systems, the contracting CCM condition needs only be enforced on the limit cycle itself, as its satisfaction within some neighborhood is then guaranteed by compactness. Likewise, for convergence to a compact manifold (e.g., an eggshell) in an autonomous system, the contracting CCM condition needs only be considered on the manifold itself.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsubsection{Contraction as minimization} Similarly, Proposition prop:contracting_grad_desc may be viewed as a particular instance of the following results, which use contraction properties to minimize a cost or Lyapunov-like function.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition}[Exponential Cost Minimization]\label{8} Consider an autonomous contracting system eq:autonomousSystem, and a scalar cost function $V(\x)$ such that $\dot{V}(\x) \le 0 $ for all $\x$. Then all trajectories tend exponentially to a global minimum of $V$. \begin{proof} Because the system is contracting and autonomous, it tends exponentially to a unique equilibrium $\x^\star$. Consider now an arbitrary $\x$, and the system trajectory initialized at $\x$. Since the cost $V$ can only decrease along the trajectory, this implies that $V(\x^\star) \le V(\x)$, for all $\x$.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{proposition}\label{9} Consider an autonomous semi-contracting system eq:autonomousSystem in a bounded metric $\M(\x)$, and a scalar cost function $V(\x)$ such that $\dot{V}(\x) \le 0 $ for all $\x$. Assume that one system equilibrium $\x^\star$ is locally attractive (e.g., that linearization at $\x^\star$ is strictly stable). Then this equilibrium is unique, it is a global minimum of $V$, and all trajectories converge to it asymptotically.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Applying Proposition~7 shows that all trajectories asymptotically tend to $\x^\star$, which also implies that the equilibrium is unique. By the same reasoning as in Proposition~8, since $V$ can only decrease, $V(\x^\star)$ must be a global minimum.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{remark}\label{16} These results extend readily to the case where a system is semi-contracting within some forward invariant region, as opposed to globally. These generalizations may have applicability e.g., to the continuous-time limit of trained neural networks~, wherein semi-contraction regions represent basins of attraction that are free of saddles. Metrics may become singular as they approach the boundary of these open sets, allowing the semi-contraction region to cover the entire basin.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proposition~9 can be stated more generally as follows.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{theorem}[Asymptotic Cost Minimization]\label{10} Consider an autonomous semi-contracting system in a bounded metric $\M(\x)$, and a scalar cost function $V(\x)$ such that $\dot{V}(\x) \le 0 $ for all $\x$. Assume that one trajectory is known to be bounded. Let $\script{I}$ be a forward invariant set where $\dot{V}=0$, and assume that the contraction condition eq:contraction_condition holds on $\script{I}$ for some (possibly different) metric.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then $\script{I}$ is path connected, all system trajectories converge to a unique equilibrium $\x^\star \in \script{I}$, and $V$ is globally Let us first show that $\script{I}$ is path connected, by contradiction. Assume $\script{I}$ is not path connected, then it can be decomposed into two disjoints subsets, $\script{I}_1$ and $\script{I}_2$. Because $\script{I}$ is invariant and the subsets are disjoint, each of the subsets must be invariant. Strict contraction on $\script{I}_1$ and $\script{I}_2$ then implies that each subset contains at least one locally stable equilibrium point (note that each of the subsets may themselves be disconnected and thus may contain more than one stable equilibrium point). The existence of two equilibrium points contradicts Proposition~9, and thus $\script{I}$ is path connected.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Next, on the connected invariant set $\script{I}$, contraction implies that the geodesic distance between any two points shrinks exponentially. By the same reasoning as in Proposition~8, this in turn implies convergence to a global minimum of $V$.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Paper Body", "weight": 1.0} -->

%In this proof, the contraction condition on the invariant set is used only to ensure that some geodesic distance between any two points in the set shrinks exponentially. Depending on the specific dynamics, this latter condition may be derived directly using weaker assumptions. Note that for a system where a scalar cost $V$ satisfies $\dot{V}\le 0$, radial unboundedness of $V$ is a sufficient condition for all trajectories to be bounded, ensuring the existence of a bounded trajectory as necessary in Thm.~10.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In the case of mechanical systems, $V$ may often be chosen as the total energy of the system, so that Proposition~8 implies exponential convergence of the total energy, and, in turn, that potential energy is exponentially minimized. Similarly, Theorem~10 implies that potential energy is asymptotically minimized.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Contraction criteria can also be expressed in non-Euclidean norms and their associated matrix measures (, section 3.7.ii). The results above extend immediately to these representations.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Primal-Dual Optimization}\label{GPD_opt} Primal-Dual algorithms are widely used in optimization to determine saddle points and also appear naturally in constrained optimization~, where Lagrange parameters play the role of dual variables. When a function is strictly convex in a subset of its variables, and strictly concave in the remaining, gradient descent/ascent dynamics converge to a unique saddle equilibrium~. Within the context of constrained optimization, these dynamics are known as the primal-dual dynamics. Such dynamics play an important role e.g., in machine learning, for instance in adversarial training~, in the information theory~ of deep networks, in reinforcement learning~ and actor-critic methods, and in support vector machine representations~. More generally, they are central to a large class of practical min-max problems, such as problems in physics involving nonlinear electrical networks modeled in terms of Brayton-Moser mixed potentials~.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider a scalar function $\script{L}({\bf x},{\bf \llambda}, t)$, possibly time-dependent, and metrics $\M_\x(\x)$ and $\M_{\llambda}(\llambda)$.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider the natural primal-dual dynamics, which \begin{subequations} \label{eq:PD} \begin{align} \label{eq:primal} {\bf M_\x}({\bf x})\ \dot{\bf x} \ &= -\nabla_{\bf x} \script{L}(\x,\llambda,t) \\{\bf M_\llambda}({\bf \llambda})\ \dot{\llambda} \ &= \ \nabla_{\llambda} \script{L}(\x,\llambda,t) \label{eq:dual} In contrast to Remark rem:bad_saddles, wherein spurious saddle equilibrium points presented an obstacle to global contraction, here the target equilibrium points of these dynamics are, by construction, chosen to be the saddle points of the function $\script{L}$.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Using the metrics ${\bf M_x}({\bf x})$ and ${\bf M_\llambda}({\llambda})$ extends the standard case, where they would be replaced by constant, symmetric positive definite matrices. The practical relevance of this extension is illustrated by the following example in the case of natural adaptive control.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% {\color{red} Explain it is a different case than avoiding% saddle points. Here the target equilibrium points are actually chosen to be the saddle points of some function.}%The extension of analysis for primal-dual optimization in the case of natural gradient ascent/descent is illustrated by the following practical example.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Primal Dual Dynamics in Natural Adaptive Control} This section illustrates the presence of natural primal-dual dynamics embedded in the application of natural adaptive control laws. Consider a system given by \label{eq:sys_for_adaptive} with configuration $\x\in \R^N$, control $\u \in \R^N$, and unknown parameters $\a \in \Acal \subset \R^p$. The regressor $\Y \in \R^{N \times p}$ and symmetric matrix $\J \in \R^{N\times N}$ may depend nonlinearly on the state and its derivatives. We assume that the matrix $\J$ remains positive definite for all $\a \in \Acal$ and that it is linear in $\a$.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Paper Body", "weight": 1.0} -->

As a result, there exists a regressor function $\W$ such that and a regressor function $\Q$ such that for any $\s\in\R^N$ -\frac{1}{2} \dot{\J} \s = \Q(\x, \ldots, \x^{(n-1)}, \s)\, \a Consider a desired trajectory $\x_d(t)$ and the associated sliding variable \s = \left(\dd{}{t} + \lambda\right)^{n-1} \xt = \x^{(n-1)} -\x_r^{(n-1)} where $\xt = \x - \x_d$.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Paper Body", "weight": 1.0} -->

With this sliding variable, we define a reference $\x_r^{(n-1)}$ for the order $n-1$ derivative of the state.% with a corresponding reference $\x_r^{(n)}$ for the $n$-th derivative%It is noted that due to the form of eq:sliding, $\x_r^{(n)}$ can be computed from knowledge of the desired trajectory $\x_d(t)$ and its derivatives up to order $n$, as well as $\x$ and its derivatives up to order $n-1$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Choosing the control law where $\x_r^{(n)} = \dd{}{t} \x_r^{(n-1)}$ provides the closed-loop dynamics \J \dot{\s} + \K \s %= \Jt\x_r^{(n)}+ \Y \at - \frac{1}{2}\Jdh \s Inspired by the elegant modification of the Slotine and Li adaptive robot controller introduced by Lee et al.~, we consider the Lyapunov-like function where $d_f(\a || \ah)$ denotes the Bregman divergence of a function $f$ assumed convex on $\Acal$ and given by Note that the LogDet divergence from eq:breg follows this form for $f(\X) = - \logdet{\X}$.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Here, we consider the case when $\Acal$ is open and $f$ is chosen as a convex barrier function on $\Acal$, such that the Hessian metric $\H = \nabla^2 f(\x)$ endows $\Acal$ with a barrier Hessian manifold structure.%For example, if $\A$ is open $f$ may be chosen as any convex barrier function on $\A$. Note that if $f$ is a second-order function $\frac{1}{2}\a^T \P \a$, the Bregman divergence is simply $\frac{1}{2}\at\T \P \at$, with $\H^{-1}$ equal to the constant matrix $\bf{P}^{-1}$ similar to the standard adaptive algorithm.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A quick calculation shows that the derivative of the Bregman divergence is simply $\dot{\ah}\T \H \ \at \ $, % with $\H = \nabla^2 f(\ah)$ the \emph{Hessian} of the convex function $f$.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Paper Body", "weight": 1.0} -->

so that the adaptation law \label{eq:ahat_dot}%the Lyapunov-like function has rate of change:% Overall, this update law provides the closed-loop dynamics% \dot{\s} &= - \J^{-1} \left(\K \s - \W(\ah - \a) - \Q\ah \right) \\% \dot{\ah} &= \H^{-1} \left (-\W\T \s - \Q\T \s \right) \noindent Considering a virtual system with $\W$ and $\Q$ as externally provided functions of time, the dynamics eq:sdot and eq:ahat_dot are equivalent to natural primal-dual over the function in the decoupled metric $\M_\s = \J$ and $\M_{\ah} = \H(\ah)$. Overall, this construction enables the results in natural adaptive robot control~ to be extended to the broader class eq:sys_for_adaptive.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Paper Body", "weight": 1.0} -->

%We note that when $f$ is chosen as a barrier function over $\A$, the Hessian of the barrier function naturally defines a Riemannian geometry on $\A$~.% \subsection{Bregman Extension} Note that a similar construction could be applied to provide natural adaptation within recent applications of nonlinear adaptive control based on control contraction metrics. %While employs an upper bound on the Riemannian energy in its Lyapunov analysis, its treatment of the parameter error takes a conventional Euclidean gradient descent approach.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The inclusion of a natural adaptive law akin to and here presents opportunity to unify the analysis of tracking error and parameter error through a fully geometric treatment.%\pmw{Probably too long.}% Consider the Lyapunov-like function% That is, use the Bregman divergence in place of the usual quadratic parameter error in the Lyapunov-like function.%A quick calculation shows that the derivative of the Bregman divergence is simply $\dot{\ah}\T \H \ \at $, with $\H = \nabla^2 f(\ah)$ the \emph{Hessian} of the convex function $f$.%So that, in effect, the gain matrix $\bP$ in the adaptation laws based on the usual quadratic term is replaced by the state-dependent Hessian $\H $ of the convex function $f$, yielding a natural gradient-like adaptation law.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Natural Primal Dual} Continuous-time convex primal-dual optimization is analyzed from a nonlinear contraction perspective in~, building on a earlier result of~. As we now show, Theorem~th_main yields a natural extension to geodesic primal-dual optimization, where convexity in terms of primal and dual variables is replaced by g-convexity, thus broadening the above results to state-dependent metrics.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Paper Body", "weight": 1.0} -->

% Consider a scalar cost function $\script{L}({\bf x},{\bf \llambda}, t)$,% possibly time-dependent, with $\script{L}$ g-strongly convex over $\x$ and g-strongly concave over $\llambda$ in metrics% $\M_\x(\x)$ and $\M_{\llambda}(\llambda)$ respectively.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider the geodesic primal-dual dynamics, which% \begin{subequations} \label{eq:PD}% \begin{align} \label{eq:primal}% {\bf M_\x}({\bf x})\ \dot{\bf x} \ &= -\nabla_{\bf x} \script{L} \\% {\bf M_\llambda}({\bf \llambda})\ \dot{\llambda} \ &= \ \nabla_{\llambda} \script{L} \label{eq:dual}% Using the metrics ${\bf M_x}({\bf x})$ and ${\bf M_\llambda}({\llambda})$ extends the standard case, where they would be replaced by constant, symmetric positive definite matrices.%{\color{red} Requirements of g-strong convexity in $\x$ and g-strong concavity in $\llambda$.}% Consider the Primal-Dual dynamics

<!-- chunk {"id": "body-0151", "role": "body", "section": "Paper Body", "weight": 1.0} -->

eq:PD and suppose that eq:primal is contracting in $\x$ for each fixed $\llambda$ under a metric $\M_\x(\x)$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Suppose also that eq:dual is contracting in $\llambda$ for each fixed $\x$ under a metric $\M_\llambda(\lambda)$. Then, the primal-dual dynamics eq:primal are globally contracting in%A special case of the previous result occurs when $\script{L}$ is g-convex in $\x$ and g-concave in $\llambda$.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{theorem}\label{th_PD} Consider a scalar function $\script{L}({\bf x},{\bf \llambda}, t)$, with $\script{L}$ g-strongly convex over $\x$ and g-strongly concave over $\llambda$ in metrics $\M_\x(\x)$ and $\M_{\llambda}(\llambda)$ respectively.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Then, the geodesic primal-dual dynamics~eq:PD is globally contracting, in metric \begin{equation}\label{GPD} {\bf M}({\bf x},{\bf \llambda}) = \begin{bmatrix} \begin{proof} \ Letting $\z = [{\x}\T, {\llambda}{}\T]\T$ and $\dot{\z} = \f(\z,t)$ denote the overall system dynamics, the system's Jacobian can be written \begin{equation} \label{eq:PD_Jacobian} {\M_\llambda}^{-1} \ \hess{\L}{\llambda}{\x} & \jac{}{\llambda} (\M_\llambda^{-1} \grad{\L}{\llambda}) \noindent so that, using Theorem~th_main, \begin{equation}\nonumber {\bf M} {\bf A} + \

<!-- chunk {"id": "body-0155", "role": "body", "section": "Paper Body", "weight": 1.0} -->

{\bf A}\T {\bf M} \ + \ \dot{\bf M } \ = \ -2 \ \begin{bmatrix} \end{equation} \end{proof} Consider the primal dual dynamics eq:PD for a scalar cost function $\script{L}({\bf x},{\bf \llambda})$, with $\script{L}$ g-strongly convex over $\x$ and g-concave (not necessarily strongly so) over $\llambda$ in metrics $\M_\x(\x)$ and $\M_{\llambda}(\llambda)$ respectively.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Suppose also that one solution of eq:PD is known to be bounded. Then, for any initial condition, the geodesic primal-dual dynamics~eq:PD converge to an equilibrium $\x^*$, $\llambda^*$. Moreover, $\x^*$ is independent of initial conditions.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The proof is given as a corollary to Theorem thm:semi_nash in the next section.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The above proposition highlights that contraction of the PD dynamics (e.g., as developed in ) is not necessary to guarantee convergence to a unique primal solution. Note however, that the above results only guarantee asymptotic convergence toward the unique primal equilibrium, as opposed to exponential convergence when contraction can be shown for the PD dynamics as a whole.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Paper Body", "weight": 1.0} -->

This proposition is reminiscent of results in adaptive control wherein the error dynamics of a certainty-equivalent controller may be asymptotically stable despite the fact that an associated adaptation law may not converge to the actual unknown parameters~, with adaptation occurring on a "need-to-know" basis in that sense. Conceptually, this principle can apply to more general contexts involving concurrent control and learning, when effective control is the main goal (e.g., in reinforcement learning).

<!-- chunk {"id": "body-0160", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\begin{remark} Note that this analogy between adaptive control and primal-dual optimization also enables recent results in distributed adaptive control to be applied in a distributed primal-dual setting. These results also include straightforward strategies for stably handling communication delays (e.g., using a wave variable formulation ) which would find additional motivation in distributed primal-dual optimization applications.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section{Applying Contraction Tools to G-Convex Optimization} \label{sec:application} Theorem th_main immediately implies that existing combination properties from contraction analysis can be directly applied in the context of g-convex optimization. While these properties derive from simple matrix algebra and in principle could be proven directly from the definition of geodesic convexity, as we will see most rely for their practical relevance on the flexibility%of using non-autonomous systems afforded by the contraction analysis point of view.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Sum of g-convex} If two functions $f_1(\x,t)$ and $f_2(\x,t)$ are g-convex in the same metric for each $t$, then their sum $f_1(\x,t) + f_2(\x,t)$ is g-convex in the same metric. %This simple result has important implications for distributed optimization.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{example:Parallel_Geo_Desc} Consider a function $f_1(\x_1,\y_1,t)$ g-convex for each $t$ in a block diagonal metric ${\rm BlkDiag}(\M_{x_1}(\x_1),\M_y(\y_1))$ and a function $f_2(\x_2,\y_2,t)$ g-convex for each $t$ in a block diagonal metric ${\rm BlkDiag}(\M_{x_2}(\x_2), \M_y(\y_2))$. Then, the function: is g-convex in metric ${\rm BlkDiag}(\M_{x_1},\M_{x_2},\M_y)$ for each $t$.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Skew-Symmetric Feedback Coupling} Assume that a scalar function $f_1(\x_1,\x_2)$ is $\alpha_1$-strongly g-convex in $\x_1$ in a metric $\M_1(\x_1)$ for each fixed $\x_2$, and similarly that a scalar function $f_2(\x_1,\x_2)$ is $\alpha_2$-strongly g-convex in a metric $\M_2(\x_2)$ for each fixed $\x_1$.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Paper Body", "weight": 1.0} -->

If $f_1$ and $f_2$ satisfy the scaled skew-symmetry property \label{eq:skew_property} where $k$ is some strictly positive constant, then the natural gradient dynamics \label{eq:Nash_dyn} \dot{\x}_2 &= - \M_2(\x_2)^{-1} \ \grad{f_2(\x_1,\x_2)}{\x_2} \nonumber is contracting with rate $ \ \min(\alpha_1, \alpha_2) $ in metric $\M(\x_1,\x_2) = {\rm BlkDiag}(\M_1(\x_1), k \M_2(\x_2))$.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since the {\em overall} system is both contracting and autonomous, it tends to a unique equilibrium~ $(\x_1^*, \x_2^*)$ which satisfies the Nash-like conditions Note that the result can be broadened to cases where the scaled skew-symmetry property is not exactly satisfied, by using the small-gain extension in~. Taking again the machine learning context as a potential example, such two-player game dynamics can occur in certain types of adversarial training.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The result extends to a game with an arbitrary number of players. Consider $n$ functions $\{f_i(\x_1,\ldots,\x_n)\}_{i=1}^n$ such that each $f_i$ is $\alpha_i$-strongly g-convex over $\x_i$ in a metric $\M_i(\x_i)$. If the functions satisfy the skew-symmetry conditions for each $j>i$, then the suitable generalizations of eq:Nash_dyn result in a coupled system that is contracting with rate ${\rm min}(\alpha_1, \ldots, \alpha_n)$ in the metric The overall system converges to a unique Nash-like equilibrium satisfying and a similar relation for each other player.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Likewise, the result can be extended to the case when the natural gradient dynamics for each individual player may only be semi-contracting.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{thm:semi_nash} Consider the two player case eq:Nash_dyn, wherein (a) $f_1$ is $\alpha_1$-strongly g-convex with $\alpha_1>0$ in a uniformly positive definite metric $\M_1(\x_1)$ for each $\x_2$ (b) the Riemannian Hessian $\H_2(\x_1,\x_2)$ of $f_2(\x_1,\x_2)$ in $\x_2$ is only positive {\em semi}-definite for each $\x_1$ in a uniformly positive definite metric $\M_2(\x_2)$ and (c) the skew-symmetry property eq:skew_property holds. Assume that one trajectory of eq:Nash_dyn is known to be bounded. Then, every trajectory of eq:Nash_dyn converges to a Nash equilibrium $\x_1^*$, $\x_2^*$.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Moreover, $\x_1^*$ does not depend on initial conditions (i.e., every Nash has the same strategy for player 1).

<!-- chunk {"id": "body-0171", "role": "body", "section": "Paper Body", "weight": 1.0} -->

It can be shown that virtual displacements evolve such that \dd{}{t} &\left(\delta \x_1\T \M_1(\x_1)\delta \x_1 + k \delta \x_2\T \M_2(\x_2) \delta \x_2 \right) \\which implies, by Barbalat's lemma, \delta \x_1 \rightarrow 0 \quad {\rm and}\quad \H_2(\x_1,\x_2) \delta \x_2 \ \rightarrow \ 0 Via the same argument as follows from ddt_h, it follows that $\grad{f_1}{\x_1}(\x_1(t), \x_2(t)) \rightarrow 0$ as $t\rightarrow \infty$. So, for each initial condition, $\x_1(t)$ must converge to some equilibrium $\x_1^*$ of the $\x_1$ dynamics.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Furthermore, since any $ \delta \x_1 \rightarrow 0 $,% eq:Nash_dyn is contracting in $\x_1$, $\x_1^*$ must be {\em unique} and independent of initial conditions. Let us now turn to the behavior of the $\x_2$ dynamics. Given an arbitrary initial condition $(\x_{1,0}$, $\x_{2,0})$ for eq:Nash_dyn, let $L^+$ denote its $\omega$-limit set. Any point in $(\x_1,\x_2) \in L^+$ must satisfy $\x_1 = \x_1^*$. Since the dynamics are autonomous, $L^+$ is composed of trajectories of the system Moreover, $L^+$ must be closed and bounded.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since eq:x2_dyn is a natural gradient system of a g-convex function, Thm.~thm:natGradNonStrict ensures that any trajectory of eq:x2_dyn must converge to an equilibrium point that is a global minimizer for $f_2(\x_1^*, \x_2)$. Considering any initial condition of eq:x2_dyn that begins in $L^+$, we denote $(\x_1^*, \x_2^*) \in L^+$ as the resulting equilibrium point. However, since eq:Nash_dyn is semi-contracting, any geodesic ball around $(\x_1^*, \x_2^*)$ is forward invariant for eq:Nash_dyn, which implies that $L^+ = \{ (\x_1^*,\x_2^*) \}$. Thus, $\x_2(t)\rightarrow \x_2^*$ as $t\rightarrow \infty$.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Note again that, while $\x_2^*$ depends on initial conditions, $\x_1^*$ does not.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Consider any two equilibrium points $(\x_1^*, \x_{21}^*)$ and $(\x_1^*, \x_{22}^*)$ for a system that satisfies the condition of Theorem~thm:semi_nash. Then, the geodesic between these points is comprised of extremal Nash equilibrium points, all of which have the same cost.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Further, if one equilibrium of eq:x2_dyn is locally asymptotically stable, then it is necessarily globally attractive, and thus all trajectories of eq:x2_dyn converge to this unique equilibrium $(\x_1^*, \x_2^*)$ regardless of initial conditions. Proof of the first part follows immediately from applying Corollary 3.1 of to the function $f_2(\x_1^*, \x_2)$. Proof of the second part follows immediately from the application of Corollary think_locally herein.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Proposition eq:semi_PD is true. Consider Thm.~thm:semi_nash with $f_1 = \script{L}(\x,\llambda)$ and $f_2 = - \script{L}(\x,\llambda)$.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\subsection{Hierarchical Natural Gradient} Consider a function $f_1(\x_1)$ $\alpha_1$-strongly g-convex in a metric $\M_1(\x_1)$, and a function $f_2(\x_1,\x_2)$ $\alpha_2$-strongly g-convex in a metric $\M_2(\x_2)$ for each given $\x_1$. Then, the hierarchical natural gradient dynamics is contracting with rate $ \ \min(\alpha_1, \alpha_2) \ $ in metric $\M(\x_1,\x_2) = {\rm BlkDiag}(\M_1(\x_1), \M_2(\x_2))$, under the mild assumption that the coupling Jacobian is bounded~.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Since the {\em overall} system is both contracting and autonomous, it tends to a unique equilibrium~ at rate $\min(\alpha_1, \alpha_2)$, and thus to the unique solution of By recursion, this structure can be chained an arbitrary number of times, or applied to any cascade or directed acyclic graph of natural gradient dynamics. Such hierarchical optimization may play a role, for instance, in backpropagation of natural gradients in machine learning, with all descents occurring concurrently rather than in sequence.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In large-scale optimization settings such as those appearing commonly in machine learning, natural gradient with a fully-dense metric can become intractable. In specific cases, such as natural gradient descent based on Fisher information~, computationally effective approximations have been derived~. In addition, the combination of simple (e.g., diagonal) metrics through hierarchical structures lends an opportunity to recover significant complexity at broad scale $-$ see, e.g., the hierarchical combination of scalar metrics to learn hierarchical representations of symbolic data. Such simpler metrics are also well motivated in the context of positive or monotone systems. In special cases of a dense Hessian metric $\M(\x) = \nabla^2 \psi(\x)$ from a potential $\psi(\x)$, note that continuous mirror descent (see also Proposition~change_variable and Example~psi) provides an alternate method to compute continuous natural gradient.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Paper Body", "weight": 1.0} -->

These methods can avoid the need to invert the metric in cases where there is an explicit inverse exists for the change of variables $\z = \nabla \psi(\x)$, or when eq:InvertGrandientViaDynamics can be run at a fast time scale to invert the gradient map through dynamics.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\label{sec:Conclusions} Overall, this paper has demonstrated that nonlinear contraction analysis provides a general perspective for analyzing and certifying the global convergence properties of gradient-based optimization algorithms. The common case of strong convexity corresponds to the special case of contracting gradient descent in the identity metric, while our analysis admits global convergence results in the significantly broader case of state-dependent metrics. This result has clear links to the case of geodesically-convex optimization wherein natural gradient descent converges to a unique equilibrium if it is contracting in any metric, broadening from the special case of g-convexity corresponding to contraction in the natural metric. Our analysis of semi-contraction of gradient systems, and the resulting smoothly connected sets of global optima may shed additional light on applications in learning with over parameterized networks where the set of optimizers is recognized to take the form of a low-dimensional manifold. Results on natural primal dual and the convergence to Nash equilibria showcase the broad reach of these fundamental results, where they may serve as the basis for the generation of larger scale distributed optimization algorithms in future work.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A framework we call Contraction + shows how contraction or semi-contraction properties can be combined with specific but coarse information on a system, such as the local stability of a particular equilibrium or the weak decreasing of a cost or a Lyapunov-like function, to conclude on global convergence or minimization.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Paper Body", "weight": 1.0} -->

A natural next step for the application of contraction in optimization is to design geodesic quorum sensing ~ algorithms for synchronization, as well as other consensus mechanisms considering time-delays~, which may serve as the basis for distributed and large-scale optimization techniques on Riemannian manifolds. Other future applications will consider stochastic gradient descent in the Riemannian setting~ with quorum sensing extensions (as, e.g., in~). Such advances could have direct applications, e.g., in the context of machine learning, among others.%\\%\thisTime{Gauss Liouville} \noindent {\bf Acknowledgements} \ \ We thank Nicholas Boffi for stimulating discussions. This research was supported in part by grant 1809314 from the National Science Foundation.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\section*{Supporting Information} \paragraph*{Proof of Theorem 1} \renewcommand*{\theproposition}{A.\arabic{proposition}} \newcommand*{\thepropositiondis}{A.\arabic{proposition}} \renewcommand*{\theremark}{A.\arabic{remark}} \newcommand*{\theremarkdis}{A.\arabic{remark}} \newcommand{\nablaM}{\overset{\scriptscriptstyle \M}{\nabla}{}} We precede the proof of Theorem 1 with a more general result that links contraction with the notion of taking covariant derivatives.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Paper Body", "weight": 1.0} -->

If we view $\h(\x,t):\R^n \times \R \rightarrow \R^n$ as providing the components of a vector field, then its covariant derivative (w.r.t.~the Riemannian connection $\nablaM{}$) along the $i$-th coordinate vector field has components: \Big[\nablaM{}_{\partial_i} \h \Big]_j = \pd{}{i}{h_j} + \Gamma_{ki}^j h_k where $\Gamma_{ij}^k$ denotes the Christoffel symbol of the second kind \Gamma_{ij}^m = \frac{1}{2} M^{mk} \left(\pd{M_{ik}}{\xsubj} + \pd{M_{jk}}{\xsubi} - \pd{M_{ij}}{\xsubk} \right) and the usual Einstein summation convention is applied (implying, e.g., a sum over

<!-- chunk {"id": "body-0187", "role": "body", "section": "Paper Body", "weight": 1.0} -->

By contrast, if we view a function $\g(\x,t):\R^n \times \R \rightarrow \R^n$ as giving the components of a co-vector field (i.e., a covariant vector field) we have: \Big[\nablaM{}^*_{\partial_i} \g \Big]_j = \pd{}{i}{g_j} - \Gamma_{ij}^k g_k where the $^*$ on $\nablaM{}^*$ denotes that we are considering $\g$ as giving the components of a co-vector field.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Paper Body", "weight": 1.0} -->

In either case, we can collect these derivatives along each coordinate vector field into Jacobian-like matrices denoted: \nablaM\, \h = \begin{bmatrix}\nablaM_{\partial_1}\h & \cdots & \nablaM_{\partial_n} \h \end{bmatrix} ~~~~~~~~~ \nablaM^* \, \g = \begin{bmatrix}\nablaM^*_{\partial_1}\g & \cdots & \nablaM^*_{\partial_n} \g \end{bmatrix} We are now prepared to state the main Proposition involved in proving Theorem 1.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Following the setup for the previous proposition, the covariant derivatives can also be shown to satisfy: \M \left[\nablaM \h \right] = \nablaM^* \g which immediately gives: \M \left(\Jac{\h}{\x} \right) + \left(\Jac{\h}{\x} \right)\T \M + \dot{\M} = \M \left[\nablaM \h \right] + \left[\nablaM \h \right]^T \M \label{eq:covariant_contraction} \newcommand{\Ttheta}{\boldsymbol{\Theta}} \newcommand{\Tthetadot}{\dot{\Ttheta}} We consider the metric factored as $\M = \Ttheta\T \Ttheta$ with the generalized Jacobian defined according to \mathbf{F} = \Ttheta \frac{\partial \h}{\partial \x} \Ttheta^{-1} +

<!-- chunk {"id": "body-0190", "role": "body", "section": "Paper Body", "weight": 1.0} -->

\Tthetadot \Ttheta^{-1} where we associate $\delta \z = \Theta \delta \x$ as a differential change of coordinates.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Paper Body", "weight": 1.0} -->

The generalized Jacobian satisfies that, along the flow of the system, local perturbations evolve according to $\frac{\rm d}{{\rm d} t}\delta \z = \mathbf{F} \delta \z$.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Paper Body", "weight": 1.0} -->

Considering a similarity transform on $\mathbf{F}$ \Ttheta^{-1} \, \mathbf{F} \, \Ttheta = \frac{\partial \h}{\partial \x} + \Ttheta^{-1} \Tthetadot we see that the right-hand side takes a similar structural form to the covariant derivative eq:covariant, as noted originally. Indeed, defining some new connection coefficients: \tilde{\Gamma}^{i}_{jk} = \left[\Ttheta^{-1} \frac{\partial \Ttheta}{\partial x_j} \right]_{ik} determines an affine connection with covariant derivatives uniquely specified according to \tilde{\nabla}_{\partial_i} \mathbf{e}_j = \tilde{\Gamma}^{k}_{ij} \mathbf{e}_k where $\mathbf{e}_j$ gives the $j$-th unit vector.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Paper Body", "weight": 1.0} -->

(Note this equation uses the symbols to sum over vectors, as opposed to components of vectors as previously.) While this new connection can be shown to be metric compatible (as defined in), it is not in general equal to the one provided by the Riemannian connection $\nablaM$ with the corresponding symbols~$\Gamma^{i}_{jk}$ via eq:christoffel. Any differences do not affect the final contraction analysis in the sense that relationship eq:covariant_contraction still holds when the Riemannian connection $\nablaM$ is replaced with any metric-compatible connection. However, eq:co_vs_contra and therefore eq:covar_result does not hold in general.% It can be shown (how?) that this generalized Jacobian is related to the above covariant derivatives via the similarity transform:% \mathbf{F} = \Ttheta \left[\nablaM \h \right] \Ttheta^{-1}% That is, $\mathbf{F}$ is just a change of basis on the conventional covariant derivative.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Paper Body", "weight": 1.0} -->

We are now ready to prove Theorem 1 from the main text. \begin{proof}[Proof of Theorem 1] Recall that $\alpha$-strong geodesic convexity of $f(\x,t)$ in the metric $ \M(\x)$ (for each $t$) is equivalent to the Riemannian Hessian of $f$, denoted $\H(\x,t)$, satisfying: \H(\x,t) \succeq \alpha \M(\x) \quad \forall \x In coordinates, entries of $\H$ are given by H_{ij} = \pdd{f}{\xsubi}{\xsubj} - \Gamma_{ij}^k \left(\pd{f}{\xsub{k}} \right) which we see is directly related to taking the covariant derivative of the co-vector field with components $\partial_k f$.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Paper Body", "weight": 1.0} -->

More specifically, defining $\g(\x,t) = -\nabla f(\x,t)$ we have: Via Proposition~prop:appendix, we thus have $\mathbf{Q} = \M \left(\Jac{\h}{\x} \right) + \left(\Jac{\h}{\x} \right)\T \M + \dot{\M} = -2 \mathbf{H}$ such that contraction of the natural gradient dynamics eq:NatGrad with rate $\alpha$ under the inequality is equivalent to requiring $\H \succeq \alpha \M$.
