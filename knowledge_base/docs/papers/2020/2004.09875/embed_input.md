<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimizing Static Linear Feedback: Gradient Method

Topics include Optimal control, Optimization, Control, Linear quadratic regulator, Optimization problem, Stationary point, Gradient method, Output feedback.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

The linear quadratic regulator is the fundamental problem of optimal control. The abstract also notes that its state feedback version was set and solved in the early 1960s.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The linear quadratic regulator is the fundamental problem of optimal control. Its state feedback version was set and solved in the early 1960s. However the static output feedback problem has no explicit-form solution. It is suggested to look at both of them from another point of view as matrix optimization problems, where the variable is a feedback matrix gain. The properties of such a function are investigated, it turns out to be smooth, but not convex, with possible non-connected domain. Nevertheless, the gradient method for it with the special step-size choice converges to the optimal solution in the state feedback case and to a stationary point in the output feedback case. The results can be extended for the general framework of unconstrained optimization and for reduced gradient method for minimization with equality-type constraints.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The linear quadratic regulator (LQR) problem is formulated as an optimization problem of minimizing a quadratic integral cost with respect to control function. It has been extensively analyzed in the last century since the seminal works of Kalman in 1960. The main result claims that for an infinite-horizon LTI system the optimal control can be expressed as linear static state feedback. The optimal gain can be found by solving the algebraic matrix Riccati equation (ARE). The results became classical and were immediately included in textbooks on control. New approaches to the problem were based on the techniques of semidefinite programming --- reduction to convex optimization with Linear Matrix Inequalities (LMIs) as constraints. Linear static feedback is a very natural and simple form of control for engineers, thus there were many attempts to extend the technique for other control problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The nearest relative of LQR is output feedback --- the same LTI system with quadratic performance in the case when full state is not measured but some output (a linear function of the state) is available. The attempts to apply static output feedback (SOF) met numerous difficulties. The problem was first addressed by Levine and Athans, but it was discovered that such stabilizing control may be lacking and there are no simple optimality certificates if it does exist. Serious theoretical efforts were directed on the formulation of existence conditions, see, but the problem remains open. If a system is stabilizable via a static output controller, there are just necessary conditions for optimality; moreover, these conditions are formulated as a system of nonlinear matrix equations. Thus the design of optimal SOF implies application of numerical methods. The first one was proposed, but it requires to solve nonlinear matrix equations on each iteration. The method suggested by Anderson and Moore is based on the solution of linear matrix equations only, but its properties were not obvious. Some results on the convergence of both methods can be found. Since then, numerous iterative schemes have been proposed, see and references therein.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However rigorous validation is lacking for many of them, while some others include hard nonlinear problems to be solved at each iteration. To sum up, optimization of SOF remains a challenging problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising tool for solving both state and output feedback control is the direct gradient method. Matrix gain $K$ for state ${u{(t)}} = {Kx{(t)}}$ or output ${u{(t)}} = {Ky{(t)}}$ control is considered as variable for optimization of the objective function which is expressed as $f{(K)}$. This function is well-defined for the set of stabilizing controllers $\mathcal{S}$ (otherwise the quadratic integral performance index is not defined). The set $\mathcal{S}$ is open and the minimum of $f{(K)}$ is achieved at the interior point. Thus a simple gradient method for unconstrained minimization of $f{(K)}$ can be applied

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

provided that the initial stabilizing controller $K_{0}$ is known. Gradient ${\nabla f}{(K)}$ for state feedback case has been found in the pioneering paper of Kalman, for output feedback it was obtained by Levine and Athans. Its calculation is computationally inexpensive --- it requires the solution of two Lyapunov equations. Such approach looks very attractive, but there are some obstacles. For state feedback the set $\mathcal{S}$ is connected but (in general) nonconvex, thus $f{(K)}$ can be nonconvex as well. A more sophisticated situation is met for output control. The set $\mathcal{S}$ can be disconnected while saddle points or local minima can exist in a connected component. These difficulties explain why in many papers gradient method was applied without rigorous validation, as a purely heuristic algorithm. Luckily it worked successively in many applications.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently there was a breakthrough in this field. First there appeared papers devoted to discrete-time version of state-feedback LQR. $f{(K)}$, despite being non-convex is shown to satisfy the so-called Lezanski-Polyak-Lojasiewicz (LPL) condition. This condition was proposed in the works back in the 1960s and still remains a powerful tool in non-convex optimization. Based on the LPL condition it was possible to prove global convergence of the gradient method to optimal controller. Important works overcome the nonconvexity obstacle for classical continuous-time LQR. It was proved that the LPL condition holds for this case and the gradient method converges. This line of research is continued.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The situation is more complicated for output control. As we mentioned above, the domain $\mathcal{S}$ can be nonconnected, and values of local minima at different connected components are different. Moreover, several local minima points can exist in a single component. Thus it is hard to expect something better than convergence to a stationary point.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions of the paper As we have mentioned, direct optimization methods for feedback control is a highly intensive direction of recent research. If compared with known results the main contributions of the presented paper can be formulated as follows.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

a\. Most of the results on the convergence of the gradient method for state feedback were known for discrete-time case. We focus on the continuous-time case and prove convergence of the method to the single minimizer with a linear rate. Similar results have been obtained in but the technique of the proof there is completely different. In the problem was converted into convex optimization by the change of variables. However such transformation is possible for state control only, while we use the technique which fits for both state and output cases.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

b\. Novel results on convergence (and rate of convergence) to stationary points are obtained for output feedback. They are based on the proved $L$-smoothness of the objective function. It is worth mentioning that a similar analysis can be applied to the wider class of problems which is called in parametric LQR. It includes such important problems as low-order control, PID control, decentralized control.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

c\. The particular properties of the feedback optimization allow to design new versions of minimization methods --- such as novel step-size rule for gradient and conjugate gradient methods or global convergence of the reduced gradient method. These algorithms can be extended to a general optimization setup, see Section 6.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Organization of the paper In Section 2 we formulate the LQR as a matrix optimization problem with nonlinear equality constraints. Then it is reduced to matrix unconstrained minimization with objective $f{(K)}$ and its domain $\mathcal{S}$. Section 3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") discusses the properties of this function defined on a generally non-convex set. The most important are $L$-smoothness property; for state feedback case LPL condition holds. In Section 4 the gradient flow on this set is showed to be exponentially stable and the discrete gradient method with special step-size rule is introduced. The convergence guarantees are presented. Section 5 illustrates the numerical experiments for the proposed method. In Section 6 we address the links between the proposed method and general optimization problems such as unconstrained smooth minimization and optimization with equality-type constraints. Finally, in Section 7 we discuss directions for future research. The proofs of the results are relegated to Appendix.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We use standard notation: $\parallel \cdot \parallel -$ spectral norm of a matrix; $\parallel \cdot \parallel_{F} -$ its Frobenius norm; ${\mathbb{S}}_{n} -$ the set of symmetric matrices; $I$ is the identity matrix; $A \succ B$ ($A \succeq B$) means that the matrix $A - B$ is positive (semi-)definite; the eigenvalues $\lambda_{i}{(A)}$ of a matrix $A \in {\mathbb{R}}^{n \times n}$ are indexed in an increasing order with respect to their real parts, i.e., ${{\Re\left( {\lambda_{1}{(A)}} \right)} \leq \ldots \leq {\Re\left( {\lambda_{n}{(A)}} \right)}}.$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

where the expectation is taken over the distribution of an initial condition $x{}$ with zero mean and covariance matrix $\Sigma$, and the quadratic cost is parameterized by ${0 \prec Q \in {\mathbb{S}}_{n}},$ and ${0 \prec R \in {\mathbb{S}}_{m}}.$

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The static feedback control is ${u{(t)}} = {- {Ky{(t)}}}$, where gain $K \in {\mathbb{R}}^{m \times r}$ is a constant matrix. Then the closed loop system is given by

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We use notation $f{(K)}$ to underline that the performance index depends on gain only; all other ingredients of system description are known. Thus our optimization problem is

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

here $\mathcal{S}$ is the set of stabilizing feedback gains,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Indeed, $f{(K)}$ is defined for stabilizing controllers $K \in \mathcal{S}$ only.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The problem of existence of stable output feedback is hard, see e.g..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

For instance if $A$ is Hurwitz then we can take $K_{0} = 0$. This controller will be taken as the initial approximation for iterative methods. Thus our goal is to improve the performance of the known regulator. Denote $\mathcal{S}_{0}$ the sublevel set

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Notice that there are no assumtions on controllability/observability, existence of $K_{0} \in \mathcal{S}$ suffices. Also we assume $B \neq 0$, otherwise the problem is trivial. Condition $Q \succ 0$ sometimes can be relaxed to $Q \succeq 0$, but we do not focus on this.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

1\. SLQR - state LQR - if $C = I$, that is the state $x{(t)}$ is available as control input. If it is needed to specify the performance index $f{(K)}$ for this case, we denote it as $f_{S}{(K)}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

2\. OLQR - output LQR - if $C \neq I$, when output $y{(t)}$ is the only information available. We use notation $f_{O}{(K)}$ to specify this case, while $f{(K)}$ is used in general situation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Let us formulate the problem as matrix constrained optimization one. To avoid calculation of integrals Bellman lemma is instrumental.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 2.2", "weight": 1.0} -->

This is an optimization problem with matrix variables $K,X$ and nonlinear equality-type constraint. For $K \in \mathcal{S}$ the solution $X \succ 0$ of this equation exists (Lyapunov theorem), we denote it as $X{(K)}$. Thus the problem is rewritten in the form with ${f{(K)}} = {{Tr}\left( {X{(K)}\Sigma} \right)}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem 2.2", "weight": 1.0} -->

In the next section we analyse the properties of the function $f{(K)}$, its domain $\mathcal{S}$ and sublevel set $\mathcal{S}_{0}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Examples", "weight": 1.0} -->

We start with few simple examples to exhibit the variety of situations.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

Let ${n = 2},{m = 2}$, set $A,B$ and $C$ to be identity matrices. Then

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

We see that $\mathcal{S}$ is not convex. This can be verified if one takes a cut ${x = k_{11} = k_{12}},{y = k_{22} = k_{21}}$ ). Moreover the boundary of $\mathcal{S}$ is non-smooth.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 3.3", "weight": 1.0} -->

Again $\mathcal{S}$ is not convex with non-smooth boundary. For instance, the cut ${x = k_{1}},{y = k_{2} = k_{3}}$ ) is not convex.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 3.3", "weight": 1.0} -->

Previous examples related to SLQR (state feedback). Now we proceed to OLQR (output feedback).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 3.4", "weight": 1.0} -->

If $\alpha = {- 1}$ this set is non-connected, it has two connectivity components. The function is illustrated on Fig. 5 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."). It has a single minima at each of the components. If $\alpha = {- 1.4}$ this set is connected, it is a ray $k > {- 0.2}$. The function is illustrated on Fig. 5 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."). It has two local minima located in the same connected component.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 3.5", "weight": 1.0} -->

is connected with two local minima and a saddle point $K = {(1.95,0.38)}$ for $\alpha = 1.2$ ). If $\alpha$ is set to $0.9$ there are two connectivity components with a single local minimum in each component ).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 3.5", "weight": 1.0} -->

We conclude that domain $\mathcal{S}$ of $f{(K)}$ can be nonconvex with non-smooth boundary even for SLQR, and disconnected for OLQR. Function $f{(K)}$ can be unbounded on its domain but it looks smooth. We shall validate these properties below.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Connectednes of $\\mathcal{S}$, $\\mathcal{S}_{0}$", "weight": 1.0} -->

It was known that $\mathcal{S}$ in state feedback case is connected, and the same is true for $\mathcal{S}_{0}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "$f{(K)}$ is coercive and $\\mathcal{S}_{0}$ is bounded", "weight": 1.0} -->

The Examples exhibit that function $f{(K)}$ is unbounded on its domain. Below we analyse its behavior in more details.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Gradient of $f{(K)}$", "weight": 1.0} -->

Differentiability of $f{(K)}$ is a well known fact, proved in the pioneering papers by Kalman for SLQR and by Levine and Athans for OLQR. We provide it for completeness.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Second derivative of $f{(K)}$", "weight": 1.0} -->

The performance index $f{(K)}$ is twice differentiable. To avoid tensors, we restrict analysis with the action of the Hessian $\nabla^{2}f{(K)})\lbrack E,E\rbrack$ on a matrix $E \in {\mathbb{R}}^{m \times n}$. It is given by the expression

<!-- chunk {"id": "body-0042", "role": "body", "section": "Second derivative of $f{(K)}$", "weight": 1.0} -->

Then applying Lemma A.1 and substituting $X^{\prime}$ for $Y^{\prime}$ in the last term of Eq. 12 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") we obtain

<!-- chunk {"id": "body-0043", "role": "body", "section": "$f{(K)}$ is L-smooth on $\\mathcal{S}_{0}$", "weight": 1.0} -->

A function is called L-smooth, if its gradient satisfies Lipschitz condition with constant $L$. Function $f{(K)}$ fails to be L-smooth on $\mathcal{S}$, however it has this property on sublevel set $\mathcal{S}_{0}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Gradient domination property", "weight": 1.0} -->

As we have seen, $f{(K)}$ can be noncovex even for state feedback case (SLQR). However there is a useful property which replaces convexity in validation of minimization methods. This property is referred to in the optimization literature as gradient domination or Ležanski-Polyak-Lojasiewicz (LPL) condition.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Methods", "weight": 1.0} -->

Now we proceed to versions of gradient method for minimization of $f{(K)}$. This is not a standard task, because function $f{(K)}$ is defined not on the entire space of matrices, it is unbounded on its domain and can be nonconvex. However the properties of the function obtained in Section 3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") allow to get convergence results. In all cases, the gradient methods behave monotonically. For SLQR global convergence to the single minimum point with linear rate can be validated. For OLQR global convergence to a stationary point holds. In all versions of the method, the known stabilizing controller $K_{0}$ serves as the initial point.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Continuous Method", "weight": 1.0} -->

First we consider the gradient flow defined by the system of ordinary differential equations

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discrete Method", "weight": 1.0} -->

Consider the gradient method in general form

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discrete Method", "weight": 1.0} -->

The properties obtained in Theorems 3.21 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") and 3.19 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") allow to establish convergence guaranties for the above method.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm", "weight": 1.0} -->

The method above is just a "conceptual" one, we do not know constant $L$ and it is hard to estimate it. Thus an implementable version of the algorithm is needed. It can be constructed as follows. Inequality provides the opportunity to apply Armijo-like rule: step-size $\gamma$ satisfies this rule if

<!-- chunk {"id": "body-0050", "role": "body", "section": "Algorithm", "weight": 1.0} -->

for some $0 < \alpha < 1$. We can achieve this inequality by subsequent reduction of the initial guess for $\gamma$ due to. This initial guess can be taken as follows. Consider a univariate function

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithm", "weight": 1.0} -->

One iteration of Newton method for minimization of $\varphi{(t)}$ starting from $t_{0} = 0$ implies

<!-- chunk {"id": "body-0052", "role": "body", "section": "Algorithm", "weight": 1.0} -->

But expressions for these quantities were obtained in Section 3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") (see Eqs. 10 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") and 13 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")). Notice that $t_{1} \geq {1/L}$ due to (16 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithm", "weight": 1.0} -->

\fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")), thus such step-size is bounded below. Taking $\gamma_{j} = {\min{\{ t_{1},T_{1}\}}}$ with some $T_{1} > 0$ (such upper bound is needed to restrict the step-size) for $K = K_{j}$ in gradient method we arrive to the basic algorithm below.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Simulation", "weight": 1.0} -->

We have started with the comparison of various versions of the step-size choice of gradient descent method for low-dimensional tests, such as Examples 3.1 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), 3.2 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), 3.3 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), 3.4 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."), and 3.5 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Simulation", "weight": 1.0} -->

\fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005."). In all cases, Algorithm 1 was superior and converged to global or local minimizers with high accuracy in 10--20 iterations.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulation", "weight": 1.0} -->

where $ones{(n,m)}$ is a $n \times m$ matrix with all entries equal to one and $rand{(n,m)}$ is a $n \times m$ matrix with every entry generated from the uniform distribution between $0$ and $1$. We choose the initial stabilizing controller as $K_{0} = 0$. It is indeed stabilizing because $A$ is Hurwitz. We find optimal gain $K_{\ast}$ by solving ARE, thus we could compare the accuracy of the obtained solutions. Then we apply three different versions of the first order methods to solve this problem. The first one is the simplest version of the gradient method Eq. 22 with constant step-size $\gamma_{j} = \gamma$ tuned at initial iterations to guarantee monotonicity of $f{(K_{j})}$, it is denoted as $GD\_r$. The second is our basic Algorithm 1 $({GDN})$. The last one is the conjugate gradient method described below by update rules in Eq. 31 $({CGN})$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulation", "weight": 1.0} -->

The convergence of the methods is illustrated in Fig. 8. Of course, the simplest form of gradient method $GD\_r$ is very slow, because step-size should be strongly enlarged after initial iterations. Our basic algorithm $({GDN})$ converges satisfactory; it is worth mentioning that the number of step reductions or truncations is minimal (approximately 10 for 100 iterations), thus step-size rule Eq. 26 works with minor corrections at all stages of iteration process. Finally, the proposed version of the conjugate gradient method strongly accelerates convergence.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Simulation", "weight": 1.0} -->

Of course these calculations are preliminary, much more should be done to develop reliable and efficient gradient-based algorithms for state feedback which can win in competition with classical algorithms based on Riccati-equation techniques. The behavior of the method for output feedback also requires detailed investigations.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Links with general optimization problems", "weight": 1.0} -->

The results obtained above for the particular feedback minimization problem can provide some surplus profit for the analysis of several abstract formulations for unconstrained and constrained optimization. We consider three such "side effects".

<!-- chunk {"id": "body-0060", "role": "body", "section": "Step-size choice for gradient descent", "weight": 1.0} -->

The step-size rule proposed in Eq. 26 is also valid for a general setup of smooth unconstrained optimization problem

<!-- chunk {"id": "body-0061", "role": "body", "section": "Step-size choice for gradient descent", "weight": 1.0} -->

and it is promising whenever the problem structure allows an efficient computation of the quadratic form in the denominator. It is particularly attractive in practice, because it does not require the knowledge of constants $L$ and $\mu$ and uses a second order information at a minor cost. For quadratic functions ${f{(x)}} = {({Hx},x)}$ the method coincides with the steepest descent. For nonquadratic functions its rigorous validation is possible for strongly convex case.

<!-- chunk {"id": "body-0062", "role": "body", "section": "New version of the conjugate gradient method", "weight": 1.0} -->

Similar approach can be exploited for the conjugate gradient method for unconstrained minimization of $f{(x)}$ in ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "New version of the conjugate gradient method", "weight": 1.0} -->

There are various formulae for $\beta_{j}$, see e.g., we provided above just the simplest one. Probably, convergence results for can be obtained.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Reduced gradient method", "weight": 1.0} -->

Gradient method for feedback minimization can be considered in general setup of abstract optimization problem with equality-type constraints

<!-- chunk {"id": "body-0065", "role": "body", "section": "Reduced gradient method", "weight": 1.0} -->

Gradient of $F{(y)}$ can be written with no problems

<!-- chunk {"id": "body-0066", "role": "body", "section": "Reduced gradient method", "weight": 1.0} -->

The method has been proposed by Ph.Wolfe and implemented in numerous algorithms, see e.g.. The standard assumption was $\mathcal{S} = {\mathbb{R}}^{n}$. However the method for nonlinear equalty constraints had just local theoretical validation (see e.g. Theorem 8, Chapter 8.2 in ), while the main interest is its global convergence. In the setup of the present paper $x$ corresponds to $Y$, $y$ to $K$. The main tool for proving convergence in general case is to obtain the conditions which are the analogs of our results on $L$-smoothness and LPL-condition (Theorems 3.19 is L-smooth on 𝒮₀ ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.") and 3.21 ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Reduced gradient method", "weight": 1.0} -->

\fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")). If such results hold, the proof is a replica of our considerations.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The results can be extended in several directions. First, more efficient computational schemes are of interest. Gradient method is the simplest method for unconstrained smooth optimization. Accelerated algorithms - such as conjugate gradient, heavy ball, Nesterov acceleration - are developed for strongly convex functions. But we have proved (Corollary 3.15 ‣ 3 Properties of 𝑓⁢(𝐾) ‣ Optimizing Static Linear Feedback: Gradient MethodSubmitted to the editors on April 2020. \fundingThe revised version of this work was funded by Russian Science Foundation under Grant 21-71-30005.")) that $f_{S}{(K)}$ is strongly convex in the neighborhood of the optimal solution $K_{\ast}$. Thus such methods are applicable to accelerate local convergence. Second, more research should be devoted to output minimization. For instance, how common is the effect of multiple minima in one connectivity component )? Does the method converge to a local minima only or it can be a saddle point? Third, there is highly important research direction which unites the problems of control, optimization and machine learning and uses such approaches as policy optimization, reinforcement learning, adaptive control, see the survey.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The gradient method can be easily extended to decentralised control (this additional condition $K \in {L,L}$ being a linear subspace in the space of matrices), see e.g. and to other parametric LQR problems. However its validation remains open question.
