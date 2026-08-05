<!-- arxiv-full-text:v1 {"arxiv_id": "2004.09875", "source": "ar5iv"} -->

## Introduction

The linear quadratic regulator (LQR) problem is formulated as an optimization problem of minimizing a quadratic integral cost with respect to control function. It has been extensively analyzed in the last century since the seminal works of Kalman in 1960. The main result claims that for an infinite-horizon LTI system the optimal control can be expressed as linear static state feedback. The optimal gain can be found by solving the algebraic matrix Riccati equation (ARE). The results became classical and were immediately included in textbooks on control. New approaches to the problem were based on the techniques of semidefinite programming --- reduction to convex optimization with Linear Matrix Inequalities (LMIs) as constraints. Linear static feedback is a very natural and simple form of control for engineers, thus there were many attempts to extend the technique for other control problems.

The nearest relative of LQR is output feedback --- the same LTI system with quadratic performance in the case when full state is not measured but some output (a linear function of the state) is available. The attempts to apply static output feedback (SOF) met numerous difficulties. The problem was first addressed by Levine and Athans, but it was discovered that such stabilizing control may be lacking and there are no simple optimality certificates if it does exist. Serious theoretical efforts were directed on the formulation of existence conditions, see, but the problem remains open. If a system is stabilizable via a static output controller, there are just necessary conditions for optimality; moreover, these conditions are formulated as a system of nonlinear matrix equations. Thus the design of optimal SOF implies application of numerical methods. The first one was proposed , but it requires to solve nonlinear matrix equations on each iteration. The method suggested by Anderson and Moore is based on the solution of linear matrix equations only, but its properties were not obvious. Some results on the convergence of both methods can be found . Since then, numerous iterative schemes have been proposed, see and references therein. However rigorous validation is lacking for many of them, while some others include hard nonlinear problems to be solved at each iteration. To sum up, optimization of SOF remains a challenging problem.

A promising tool for solving both state and output feedback control is the direct gradient method. Matrix gain $K$ for state ${u{(t)}} = {Kx{(t)}}$ or output ${u{(t)}} = {Ky{(t)}}$ control is considered as variable for optimization of the objective function which is expressed as $f{(K)}$. This function is well-defined for the set of stabilizing controllers $\mathcal{S}$ (otherwise the quadratic integral performance index is not defined). The set $\mathcal{S}$ is open and the minimum of $f{(K)}$ is achieved at the interior point. Thus a simple gradient method for unconstrained minimization of $f{(K)}$ can be applied provided that the initial stabilizing controller $K_{0}$ is known. Gradient ${\nabla f}{(K)}$ for state feedback case has been found in the pioneering paper of Kalman, for output feedback it was obtained by Levine and Athans. Its calculation is computationally inexpensive --- it requires the solution of two Lyapunov equations. Such approach looks very attractive, but there are some obstacles. For state feedback the set $\mathcal{S}$ is connected but (in general) nonconvex, thus $f{(K)}$ can be nonconvex as well. A more sophisticated situation is met for output control. The set $\mathcal{S}$ can be disconnected while saddle points or local minima can exist in a connected component. These difficulties explain why in many papers gradient method was applied without rigorous validation, as a purely heuristic algorithm. Luckily it worked successively in many applications.

Recently there was a breakthrough in this field. First there appeared papers devoted to discrete-time version of state-feedback LQR. $f{(K)}$, despite being non-convex is shown to satisfy the so-called Lezanski-Polyak-Lojasiewicz (LPL) condition. This condition was proposed in the works back in the 1960s and still remains a powerful tool in non-convex optimization. Based on the LPL condition it was possible to prove global convergence of the gradient method to optimal controller. Important works overcome the nonconvexity obstacle for classical continuous-time LQR. It was proved that the LPL condition holds for this case and the gradient method converges. This line of research is continued .

The situation is more complicated for output control. As we mentioned above, the domain $\mathcal{S}$ can be nonconnected, and values of local minima at different connected components are different. Moreover, several local minima points can exist in a single component. Thus it is hard to expect something better than convergence to a stationary point.

Contributions of the paper As we have mentioned, direct optimization methods for feedback control is a highly intensive direction of recent research. If compared with known results the main contributions of the presented paper can be formulated as follows. a\. Most of the results on the convergence of the gradient method for state feedback were known for discrete-time case. We focus on the continuous-time case and prove convergence of the method to the single minimizer with a linear rate. Similar results have been obtained in but the technique of the proof there is completely different. In the problem was converted into convex optimization by the change of variables. However such transformation is possible for state control only, while we use the technique which fits for both state and output cases. b\. Novel results on convergence (and rate of convergence) to stationary points are obtained for output feedback. They are based on the proved $L$-smoothness of the objective function. It is worth mentioning that a similar analysis can be applied to the wider class of problems which is called in parametric LQR. It includes such important problems as low-order control, PID control, decentralized control. c\. The particular properties of the feedback optimization allow to design new versions of minimization methods --- such as novel step-size rule for gradient and conjugate gradient methods or global convergence of the reduced gradient method. These algorithms can be extended to a general optimization setup, see Section 6.

Organization of the paper In Section 2 we formulate the LQR as a matrix optimization problem with nonlinear equality constraints. Then it is reduced to matrix unconstrained minimization with objective $f{(K)}$ and its domain $\mathcal{S}$. Section 3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") discusses the properties of this function defined on a generally non-convex set. The most important are $L$-smoothness property; for state feedback case LPL condition holds. In Section 4 the gradient flow on this set is showed to be exponentially stable and the discrete gradient method with special step-size rule is introduced. The convergence guarantees are presented. Section 5 illustrates the numerical experiments for the proposed method. In Section 6 we address the links between the proposed method and general optimization problems such as unconstrained smooth minimization and optimization with equality-type constraints. Finally, in Section 7 we discuss directions for future research. The proofs of the results are relegated to Appendix.

## Problem Statement

We use standard notation: $\parallel \cdot \parallel -$ spectral norm of a matrix; $\parallel \cdot \parallel_{F} -$ its Frobenius norm; ${\mathbb{S}}_{n} -$ the set of symmetric matrices; $I$ is the identity matrix; $A \succ B$ ($A \succeq B$) means that the matrix $A - B$ is positive (semi-)definite; the eigenvalues $\lambda_{i}{(A)}$ of a matrix $A \in {\mathbb{R}}^{n \times n}$ are indexed in an increasing order with respect to their real parts, i.e., ${{\Re\left({\lambda_{1}{(A)}} \right)} \leq \ldots \leq {\Re\left({\lambda_{n}{(A)}} \right)}}.$ Consider linear time-invariant system with state $x$ and output $y$ and matrices $A \in {\mathbb{R}}^{n \times n}$, ${B \in {\mathbb{R}}^{n \times m}},$ $C \in {\mathbb{R}}^{r \times n}$. The infinite-horizon LQR performance criterion is given by where the expectation is taken over the distribution of an initial condition $x{}$ with zero mean and covariance matrix $\Sigma$, and the quadratic cost is parameterized by ${0 \prec Q \in {\mathbb{S}}_{n}},$ and ${0 \prec R \in {\mathbb{S}}_{m}}.$ The static feedback control is ${u{(t)}} = {- {Ky{(t)}}}$, where gain $K \in {\mathbb{R}}^{m \times r}$ is a constant matrix. Then the closed loop system is given by and objective function becomes We use notation $f{(K)}$ to underline that the performance index depends on gain only; all other ingredients of system description are known. Thus our optimization problem is here $\mathcal{S}$ is the set of stabilizing feedback gains, Indeed, $f{(K)}$ is defined for stabilizing controllers $K \in \mathcal{S}$ only.

The problem of existence of stable output feedback is hard, see e.g.. However we are not interested in this, our main assumption is that a stabilizing controller exists and is available: For instance if $A$ is Hurwitz then we can take $K_{0} = 0$. This controller will be taken as the initial approximation for iterative methods. Thus our goal is to improve the performance of the known regulator. Denote $\mathcal{S}_{0}$ the sublevel set We suppose the following Assumptions hold: Notice that there are no assumtions on controllability/observability, existence of $K_{0} \in \mathcal{S}$ suffices. Also we assume $B \neq 0$, otherwise the problem is trivial. Condition $Q \succ 0$ sometimes can be relaxed to $Q \succeq 0$, but we do not focus on this.

We distinguish two main versions of the problem: 1\. SLQR - state LQR - if $C = I$, that is the state $x{(t)}$ is available as control input. If it is needed to specify the performance index $f{(K)}$ for this case, we denote it as $f_{S}{(K)}$.

2\. OLQR - output LQR - if $C \neq I$, when output $y{(t)}$ is the only information available. We use notation $f_{O}{(K)}$ to specify this case, while $f{(K)}$ is used in general situation.

Let us formulate the problem as matrix constrained optimization one. To avoid calculation of integrals Bellman lemma is instrumental.

### Lemma 2.1

Given ${W \succ 0},$ and a Hurwitz matrix $A$. Then on the solution of the LTI system where $X$ is the solution of the Lyapunov matrix equation Applying this result we rewrite 5 in the final form

### Problem 2.2

This is an optimization problem with matrix variables $K,X$ and nonlinear equality-type constraint. For $K \in \mathcal{S}$ the solution $X \succ 0$ of this equation exists (Lyapunov theorem), we denote it as $X{(K)}$. Thus the problem is rewritten in the form with ${f{(K)}} = {{Tr}\left( {X{(K)}\Sigma} \right)}$.

In the next section we analyse the properties of the function $f{(K)}$, its domain $\mathcal{S}$ and sublevel set $\mathcal{S}_{0}$.

## Properties of $f{(K)}$

### Examples

We start with few simple examples to exhibit the variety of situations.

### Example 3.1

Let us consider 1D example with parameters ${A = 0 \in {\mathbb{R}}},{Q = R = {2B} = 1 \in {\mathbb{R}}},{K = k \in {\mathbb{R}}}$. The function can be written explicitly.

Here $\mathcal{S} = {\mathbb{R}}_{+}$ is convex and unbounded, $\mathcal{S}_{0}$ is bounded, $f{(K)}$ is convex and unbounded on $\mathcal{S}$ ).

Figure 1: f (K) for 1D example

### Example 3.2

Let ${n = 2},{m = 2}$, set $A,B$ and $C$ to be identity matrices. Then We see that $\mathcal{S}$ is not convex. This can be verified if one takes a cut ${x = k_{11} = k_{12}},{y = k_{22} = k_{21}}$). Moreover the boundary of $\mathcal{S}$ is non-smooth.

### Example 3.3

For ${n = 3},{m = 1}$ consider the matrices ${A = \begin{pmatrix} \end{pmatrix}},{B = \begin{pmatrix} \end{pmatrix}}$ and $C = I$. Then Again $\mathcal{S}$ is not convex with non-smooth boundary. For instance, the cut ${x = k_{1}},{y = k_{2} = k_{3}}$) is not convex.

Figure 2: Nonconvex cut of 𝒮 for m = n = 2 Figure 3: Nonconvex cut of 𝒮 for m = 1, n = 3 Previous examples related to SLQR (state feedback). Now we proceed to OLQR (output feedback).

### Example 3.4

Consider an example with a scalar control and ${Q = I_{3}},{R = 1}$, ${A = \begin{pmatrix} \end{pmatrix}},$ $B = \begin{pmatrix} \end{pmatrix}$ and $C = \begin{pmatrix} If $\alpha = {- 1}$ this set is non-connected, it has two connectivity components. The function is illustrated on Fig. 5 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."). It has a single minima at each of the components. If $\alpha = {- 1.4}$ this set is connected, it is a ray $k > {- 0.2}$. The function is illustrated on Fig. 5 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."). It has two local minima located in the same connected component.

Figure 4: fO (K) for scalar output control with local minima in two disconnected set.

Figure 5: fO (K) for scalar output control with local minima in the same connected component.

### Example 3.5

is connected with two local minima and a saddle point $K = {(1.95,0.38)}$ for $\alpha = 1.2$ ). If $\alpha$ is set to $0.9$ there are two connectivity components with a single local minimum in each component ).

Figure 6: Two local minima of fO (K) Figure 7: Two connectivity components of 𝒮 We conclude that domain $\mathcal{S}$ of $f{(K)}$ can be nonconvex with non-smooth boundary even for SLQR, and disconnected for OLQR. Function $f{(K)}$ can be unbounded on its domain but it looks smooth. We shall validate these properties below.

### Connectednes of $\mathcal{S}$, $\mathcal{S}_{0}$

It was known that $\mathcal{S}$ in state feedback case is connected, and the same is true for $\mathcal{S}_{0}$.

### Lemma 3.6

Let $C = I$. The sets $\mathcal{S},\mathcal{S}_{0}$ are connected for every $K_{0} \in \mathcal{S}$.

### Proof 3.7

For $C = I$ equation becomes ${{{({A - {BK}})}^{\top}X} + {X{({A - {BK}})}} + {K^{\top}RK} + Q} = 0$. It is proved in that equality here can be replaced with inequality and after change of variables $P = X^{- 1}$ definition of stabilizing controllers becomes The inequality for $P$ can be rewritten as block LMI and defines a convex set. Its image given by the continuous map $K = {R^{- 1}B^{T}P^{- 1}}$ is connected. Similarly the set $\mathcal{S}_{0}$ is defined by the same map for the same set of $P$ with extra constraint ${TrP^{- 1}\Sigma} \leq {f{(K_{0})}}$ which is convex (again it can be written as LMI in $P$), this implies connectedness of $\mathcal{S}_{0}$.

We provided the proof to demonstrate well known technique of variable change which allows to transform the original problem to a convex one. This line of research was developed in to validate the gradient method. Unfortunately this trick does not work for output feedback --- there exist no convex reparametrization in this case.

As we have seen in Examples, the set $\mathcal{S}$ can be non-connected. Upper estimates for the number $N$ of connected elements for particular cases may be found . For instance, if $m = r = 1$ (single-input single-output system) then $N \leq {n + 1}$. For more general problems with additional condition $K \in {L,L}$ being a linear subspace in the set of matrices (so-called decentralised control) the number of components can grow exponentially, see, where numerous examples can be found.

### $f{(K)}$ is coercive and $\mathcal{S}_{0}$ is bounded

The Examples exhibit that function $f{(K)}$ is unbounded on its domain. Below we analyse its behavior in more details.

### Definition 3.8

A continuous function $f:{K\mapsto{f{(K)}} \in {\mathbb{R}}}$ defined on the set $\mathcal{S}$ is called coercive if for any sequence $\left\{ K_{j} \right\}_{j = 1}^{\infty} \subseteq \mathcal{S}$

### Lemma 3.9

The function ${f{(K)}} = {{Tr}\left({X{(K)}\Sigma} \right)}$ is coercive and the following estimates hold The proof of the Lemma and further results can be found in Appendices B and C. From estimate (9 is coercive and 𝒮₀ is bounded ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")) we immediately get

### Corollary 3.10

For any $K_{0} \in \mathcal{S}$ the set $\mathcal{S}_{0}$ is bounded.

On the other hand a minimum point of $f{(K)}$ on $\mathcal{S}_{0}$ exists (continuous function on a compact set) but $\mathcal{S}_{0}$ has no common points with boundary of $\mathcal{S}$ due to (8 is coercive and 𝒮₀ is bounded ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")). Hence

### Corollary 3.11

There exists a minimum point $K_{\ast} \in \mathcal{S}$.

This reasoning can be seen as an alternative proof of lemma 2.1 .

### Gradient of $f{(K)}$

Differentiability of $f{(K)}$ is a well known fact, proved in the pioneering papers by Kalman for SLQR and by Levine and Athans for OLQR. We provide it for completeness.

### Lemma 3.12

For all $K \in \mathcal{S}$, the gradient of is where $Y$ is the solution to the Lyapunov matrix equation

### Proof 3.13

Consider the increment of the Lyapunov equation Eq. 7 Denote $M:={{RKC} - {B^{\top}X}}$ then where $Y$ is the solution to Eq. 11 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.").

The necessary condition for the minimizer of $f{(K)}$ is ${{\nabla f}{(K_{\ast})}} = 0$ (because $K_{\ast}$ exists and belongs to the open set $\mathcal{S}$). This condition implies the set of three nonlinear matrix equations for $K_{\ast}$: ${{\nabla f}{(K_{\ast})}} = 0$, (11 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")),. In general they can not be solved explicitly and numerical methods are required.

However there is the famous case of state feedback control $C = I$ when explicit form of the solution (going back to Kalman) can be obtained. Then by setting the gradient calculated in Lemma 3.12 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") to zero and noting that ${Y_{\ast} \succ 0},{C = I}$ we get Further, substituting the control matrix in Eq. 7 by the expression for $K_{\ast}$ we obtain the well known Riccati equation for $X_{\ast}$ Of course this is not completely explicit solution because Riccati equation should be solved numerically, but the methods for this purpose are well developed.

### Second derivative of $f{(K)}$

The performance index $f{(K)}$ is twice differentiable. To avoid tensors, we restrict analysis with the action of the Hessian $\nabla^{2}f{(K)})\lbrack E,E\rbrack$ on a matrix $E \in {\mathbb{R}}^{m \times n}$. It is given by the expression where $X':={X'{(K)}{\lbrack E\rbrack}}$ and $Y':={Y'{(K)}{\lbrack E\rbrack}}$ are the solutions to equations which can be equivalently rewritten as Then applying Lemma A.1 and substituting $X'$ for $Y'$ in the last term of Eq. 12 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") we obtain

### Lemma 3.14

For all $K \in \mathcal{S}$, the gradient of $f{(\cdot)}$ is differentiable and the action of the Hessian of $f{(\cdot)}$ on any $E \in {\mathbb{R}}^{m \times n}$ satisfies As Examples show, $f{(K)}$ is in general nonconvex. However for state feedback case we can guarantee local strong convexity in the neighborhood of the minimum point $K_{\ast}$.

### Corollary 3.15

$f_{S}{( \cdot )}$ is strongly convex in the neighborhood of $K_{\ast}$.

### Proof 3.16

Note that when $K = K_{\ast}$ the second term in Eq. 13 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") turns to zero. If we recall that ${R,Y} \succ 0$ it is straightforward to show that Then the Hessian is positive definite at $K_{\ast}$ and there is a neighbourhood of $K_{\ast}$ where the function $f_{S}{(\cdot)}$ is strongly convex.

The upper bound for the second derivative is available.

### Lemma 3.17

On the set $\mathcal{S}$ the action of the Hessian ${\nabla^{2}f}{(K)}$ on a matrix ${E \in {\mathbb{R}}^{m \times n}},{{\| E\|}_{F} = 1}$ can be bounded as where $X'$ and $Y$ are solutions to the Lyapunov matrix equations

### Proof 3.18

It follows from Eq. 13 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") that Now we estimate both terms in this expression separately assuming ${\| E\|}_{F} = 1$: By Cauchy - Schwarz inequality It suffices to bound ${\|{BECY}\|}_{F}$ when ${\| E\|}_{F} = 1$

### $f{(K)}$ is L-smooth on $\mathcal{S}_{0}$

A function is called L-smooth, if its gradient satisfies Lipschitz condition with constant $L$. Function $f{(K)}$ fails to be L-smooth on $\mathcal{S}$, however it has this property on sublevel set $\mathcal{S}_{0}$.

### Theorem 3.19

On the set $\mathcal{S}_{0}$ the function $f{(K)}$ is $L$-smooth with constant where $\xi = {\frac{\sqrt{n}f{(K_{0})}}{\lambda_{1}{(\Sigma)}}\left({\frac{f{(K_{0})}{\| B\|}}{\lambda_{1}{(\Sigma)}\lambda_{1}{(Q)}} + \sqrt{\left(\frac{f{(K_{0})}{\| B\|}}{\lambda_{1}{(\Sigma)}\lambda_{1}{(Q)}} \right)^{2} + {\lambda_{n}{(R)}}}} \right)}$.

For the proof see Appendix B.

### Corollary 3.20

The following inequality holds for $K \in \mathcal{S}_{0}$: where $L$ is given in (15 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")).

Indeed for twice differentiable functions Lipschitz constant $L$ for gradients equals to the upper bound for the norm of second derivatives.

As we have seen for the examples, the boundary of $\mathcal{S}$ can be non-smooth, while level sets of $f{(K)}$ are smooth due to $L$-smoothness property of $f{(K)}$.

### Gradient domination property

As we have seen, $f{(K)}$ can be noncovex even for state feedback case (SLQR). However there is a useful property which replaces convexity in validation of minimization methods. This property is referred to in the optimization literature as gradient domination or Ležanski-Polyak-Lojasiewicz (LPL) condition.

### Theorem 3.21

The function $f_{S}{(K)}$ defined in Eq. 6 satisfies the LPL condition on the set $\mathcal{S}_{0}$ Constant $\mu$ in the LPL condition depends on $K_{0}$ and tends to zero when $f_{S}{(K)}$ tends to infinity. The condition is false for the entire set $\mathcal{S}$, as can be seen from Example 3.1 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."). The condition cannot be applied for output feedback - for instance, in Example 3.4 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") there are two disconnected components with different values of minima. Moreover in Example 3.5 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") there are two local minima in the connected domain.

## Methods

Now we proceed to versions of gradient method for minimization of $f{(K)}$. This is not a standard task, because function $f{(K)}$ is defined not on the entire space of matrices, it is unbounded on its domain and can be nonconvex. However the properties of the function obtained in Section 3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") allow to get convergence results. In all cases, the gradient methods behave monotonically. For SLQR global convergence to the single minimum point with linear rate can be validated. For OLQR global convergence to a stationary point holds. In all versions of the method, the known stabilizing controller $K_{0}$ serves as the initial point.

### Continuous Method

First we consider the gradient flow defined by the system of ordinary differential equations

### Theorem 4.1

The solution of the above system $K_{t} = {K{(t)}} \in \mathcal{S}_{0}$ exists for all $t \geq 0$, $f{(K_{t})}$ is monotone decreasing and If $C = I$ then $K_{t}$ converges to the global minimum point $K_{\ast}$ exponentially: where $\mu$ and $L$ are determined in Theorems 3.21 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") and 3.19 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.").

The main idea of the proof is the equality ${\frac{d}{dt}f{(K)}} = {- {\|{{\nabla f}{(K)}}\|}^{2}}$, the details are in Appendix D.

### Discrete Method

Consider the gradient method in general form The properties obtained in Theorems 3.21 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") and 3.19 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") allow to establish convergence guaranties for the above method.

### Theorem 4.2

For arbitrary $0 < \gamma_{j} \leq \frac{2}{L}$ method generates nonincreasing sequence $f{(K_{j})}$: Moreover if ${0 < \varepsilon_{1} \leq \gamma_{j} \leq {\frac{2}{L} - \varepsilon_{2}}},{\varepsilon_{2} > 0}$ then and for $C = I$ the method converges to the global minimum $K_{\ast}$ with a linear rate The simplest choice is $\gamma_{j} = {1/L}$, then in the last inequality constants $c,q$ can be written explicitly. The proof in Appendix D is mainly the replica of the standard ones; however the non-trivial part is the proof that all iterations remain in $\mathcal{S}_{0}$.

### Algorithm

The method above is just a "conceptual" one, we do not know constant $L$ and it is hard to estimate it. Thus an implementable version of the algorithm is needed. It can be constructed as follows. Inequality provides the opportunity to apply Armijo-like rule: step-size $\gamma$ satisfies this rule if for some $0 < \alpha < 1$. We can achieve this inequality by subsequent reduction of the initial guess for $\gamma$ due to. This initial guess can be taken as follows. Consider a univariate function One iteration of Newton method for minimization of $\varphi{(t)}$ starting from $t_{0} = 0$ implies Calculating derivatives we get But expressions for these quantities were obtained in Section 3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") (see Eqs. 10 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") and 13 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")). Notice that $t_{1} \geq {1/L}$ due to (16 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")), thus such step-size is bounded below. Taking $\gamma_{j} = {\min{\{ t_{1},T_{1}\}}}$ with some $T_{1} > 0$ (such upper bound is needed to restrict the step-size) for $K = K_{j}$ in gradient method we arrive to the basic algorithm below.

9: ${t\leftarrow{\min{\{ T_{1},\frac{{\|{{\nabla f}{(K)}}\|}_{F}^{2}}{{\nabla^{2}f}{(K)}{\lbrack{{\nabla f}{(K)}},{{\nabla f}{(K)}}\rbrack}}\}}}},{K_{prev}\leftarrow K}$. 13: repeat the gradient step. Algorithm 1 Gradient method

### Theorem 4.3

For Algorithm 1 the number of step reductions is bounded uniformly for all iterations and convergence results of Theorem 4.2 hold true.

The proof follows the same lines as for Theorem 4.2 and is given in the Appendix.

There are different ways to choose constants $T_{1},\alpha$ in the Algorithm. We do not discuss them here, because there are various implementations of the Algorithm and they deserve a separate consideration.

It is also possible to consider a different approach for a stepsize choice. For instance, it can be chosen in such a way that guaranties that a new iterate remains stabilizing. Then there is no need to check if $K \in \mathcal{S}$ on every iteration. Consider the Lyapunov equation Denote $K_{t} = {K - {t{\nabla f}{(K)}}}$ and $G = {{{({B{\nabla f}{(K)}C})}Y} + {Y{({B{\nabla f}{(K)}C})}^{\top}}}$.

The function ${V{(x)}} = {x^{\top}Y^{- 1}x}$ remains the quadratic Lyapunov function for a new $A_{K_{t}}$ when ${I - {tG}} \succ 0$. If ${\lambda_{max}{(G)}} \leq 0$, then ${K_{t} \in \mathcal{S}},{{\forall t} > 0}$. Otherwise, $K_{t} \in \mathcal{S}$ if $0 < t < \frac{1}{\lambda_{max}{(G)}}$.

## Simulation

We have started with the comparison of various versions of the step-size choice of gradient descent method for low-dimensional tests, such as Examples 3.1 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), 3.2 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), 3.3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), 3.4 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), and 3.5 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."). In all cases, Algorithm 1 was superior and converged to global or local minimizers with high accuracy in 10--20 iterations.

For medium-size simulation we generated matrices with dimensions ${n = 100},{m = 10}$ for SLQR problem: where $ones{(n,m)}$ is a $n \times m$ matrix with all entries equal to one and $rand{(n,m)}$ is a $n \times m$ matrix with every entry generated from the uniform distribution between $0$ and $1$. We choose the initial stabilizing controller as $K_{0} = 0$. It is indeed stabilizing because $A$ is Hurwitz. We find optimal gain $K_{\ast}$ by solving ARE, thus we could compare the accuracy of the obtained solutions. Then we apply three different versions of the first order methods to solve this problem. The first one is the simplest version of the gradient method Eq. 22 with constant step-size $\gamma_{j} = \gamma$ tuned at initial iterations to guarantee monotonicity of $f{(K_{j})}$, it is denoted as $GD_r$. The second is our basic Algorithm 1 $({GDN})$. The last one is the conjugate gradient method described below by update rules in Eq. 31 $({CGN})$. The convergence of the methods is illustrated in Fig. 8. Of course, the simplest form of gradient method $GD_r$ is very slow, because step-size should be strongly enlarged after initial iterations. Our basic algorithm $({GDN})$ converges satisfactory; it is worth mentioning that the number of step reductions or truncations is minimal (approximately 10 for 100 iterations), thus step-size rule Eq. 26 works with minor corrections at all stages of iteration process. Finally, the proposed version of the conjugate gradient method strongly accelerates convergence.

Of course these calculations are preliminary, much more should be done to develop reliable and efficient gradient-based algorithms for state feedback which can win in competition with classical algorithms based on Riccati-equation techniques. The behavior of the method for output feedback also requires detailed investigations.

Figure 8: Three first-order methods for n = 100, m = 10

## Links with general optimization problems

The results obtained above for the particular feedback minimization problem can provide some surplus profit for the analysis of several abstract formulations for unconstrained and constrained optimization. We consider three such "side effects".

### Step-size choice for gradient descent

The step-size rule proposed in Eq. 26 is also valid for a general setup of smooth unconstrained optimization problem The gradient method becomes and it is promising whenever the problem structure allows an efficient computation of the quadratic form in the denominator. It is particularly attractive in practice, because it does not require the knowledge of constants $L$ and $\mu$ and uses a second order information at a minor cost. For quadratic functions ${f{(x)}} = {({Hx},x)}$ the method coincides with the steepest descent. For nonquadratic functions its rigorous validation is possible for strongly convex case.

### Theorem 6.1

Let $f{(\cdot)}$ be twice differentiable $\mu$-strongly convex function in ${\mathbb{R}}^{n}$, ${\nabla f}{(\cdot)}$ and ${\nabla^{2}f}{(\cdot)}$ Lipschitz continuous with constants $L$ and $M$ respectively. Then if the initial condition $x_{0}$ satisfies then the method Eq. 27 converges to the global minimizer $x_{\ast}$ with a linear rate: The damped version of ($\gamma_{j}$ replaced with ${{\sigma\gamma_{j}},\sigma} \leq \frac{\mu}{L}$) converges for an arbitrary $x_{0}$: The proofs are deferred to Appendix D.

Similar step-size rule can be applied for the solution of constrained minimization problem ${\min_{Q}f}{(x)}$ via gradient projection method.

### New version of the conjugate gradient method

Similar approach can be exploited for the conjugate gradient method for unconstrained minimization of $f{(x)}$ in ${\mathbb{R}}^{n}$. The standard version of the method requires 1D minimization for finding step-size $\alpha_{j}$, but it can be replaced as follows: There are various formulae for $\beta_{j}$, see e.g., we provided above just the simplest one. Probably, convergence results for can be obtained.

### Reduced gradient method

Gradient method for feedback minimization can be considered in general setup of abstract optimization problem with equality-type constraints here ${{x \in {\mathbb{R}}^{n}},{{y \in {\mathbb{R}}^{m}},{{g{(x)}} \in {\mathbb{R}}^{n}}}}.$ Suppose that the solution $x{(y)}$ of the equality ${g{(x,y)}} = 0$ for fixed $y \in \mathcal{S}$ can be found either explicitly or with minor computational efforts. Define ${F{(y)}}:={f{({x{(y)}},y)}}$. Thus problem is converted to unconstrained optimization Gradient of $F{(y)}$ can be written with no problems and gradient method with $y_{0} \in \mathcal{S}$ becomes so-called reduced gradient method: The method has been proposed by Ph.Wolfe and implemented in numerous algorithms, see e.g.. The standard assumption was $\mathcal{S} = {\mathbb{R}}^{n}$. However the method for nonlinear equalty constraints had just local theoretical validation (see e.g. Theorem 8, Chapter 8.2 in), while the main interest is its global convergence. In the setup of the present paper $x$ corresponds to $Y$, $y$ to $K$. The main tool for proving convergence in general case is to obtain the conditions which are the analogs of our results on $L$-smoothness and LPL-condition (Theorems 3.19 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") and 3.21 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")). If such results hold, the proof is a replica of our considerations.

## Conclusion

The results can be extended in several directions. First, more efficient computational schemes are of interest. Gradient method is the simplest method for unconstrained smooth optimization. Accelerated algorithms - such as conjugate gradient, heavy ball, Nesterov acceleration - are developed for strongly convex functions. But we have proved (Corollary 3.15 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")) that $f_{S}{(K)}$ is strongly convex in the neighborhood of the optimal solution $K_{\ast}$. Thus such methods are applicable to accelerate local convergence. Second, more research should be devoted to output minimization. For instance, how common is the effect of multiple minima in one connectivity component )? Does the method converge to a local minima only or it can be a saddle point? Third, there is highly important research direction which unites the problems of control, optimization and machine learning and uses such approaches as policy optimization, reinforcement learning, adaptive control, see the survey. The gradient method can be easily extended to decentralised control (this additional condition $K \in {L,L}$ being a linear subspace in the space of matrices), see e.g. and to other parametric LQR problems. However its validation remains open question.
