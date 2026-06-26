<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LQR through the Lens of First Order Methods: Discrete-time Case

Topics include Gradient descent, Natural gradients, Lyapunov methods, First-order methods, Discrete-time, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the Linear-Quadratic-Regulator (LQR) problem in terms of optimizing a real-valued matrix function over the set of feedback gains. Such a setup facilitates examining the implications of a natural initial-state independent formulation of LQR in designing first order algorithms. It is shown that this cost function is smooth and coercive, and provide an alternate means of noting its gradient dominated property. In the process, we provide a number of analytic observations on the LQR cost when directly analyzed in terms of the feedback gain. We then examine three types of well-posed flows for LQR: gradient flow, natural gradient flow and the quasi-Newton flow. The coercive property suggests that these flows admit unique solutions while gradient dominated property indicates that the corresponding Lyapunov functionals decay at an exponential rate; we also prove that these flows are exponentially stable in the sense of Lyapunov. We then discuss the forward Euler discretization of these flows, realized as gradient descent, natural gradient descent and the quasi-Newton iteration. We present stepsize criteria for gradient descent and natural gradient descent, guaranteeing that both algorithms converge linearly to the global optima.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An optimal stepsize for the quasi-Newton iteration is also proposed, guaranteeing a Q-quadratic convergence rate - and in the meantime - recovering the Hewer algorithm.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linear-quadratic-regulator (LQR) has been one of the cornerstones of control theory since Kalman's original work in the 1960s. LQR is formulated around an optimization problem for determining a sequence of (control) inputs to a linear system in order to minimize a given (integral) quadratic cost over an infinite horizon.^11^1We shall not delve into the finite-horizon LQR in this paper. From the theoretical point of view, a fundamental property of LQR synthesis is that the resulting optimal input is in the form of a state feedback; as such, it can be represented as a constant feedback gain on the state of the system. The state feedback gain that "solves" the infinite-horizon LQR problem, in turn, can be obtained by solving the algebraic Riccati equation (ARE). That is, in the traditional approach to LQR design, the state feedback gain is revealed after obtaining the "certificate" or "cost-to-go" for the underlying optimal control problem.^22^2The analogy here would be solving the dual, followed by the recovery of the primal solution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Historically, a large number of works have studied the solution of ARE, including approaches based on iterative algorithms, algebraic solution methods, and semidefinite programming.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although the cost function plays a fundamental role in the LQR problem, it is generally not "recommended" to directly compute the optimal gain (policy) using this cost function without solving the associated Riccati equation. This approach, in the meantime, is in sharp contrast to how one would typically go about minimizing a cost function over the variable of interest in introductory optimization, say, through gradient descent.^33^3This is essentially due to the dynamic nature of the constraint set. With recent advances in sophisticated statistical and optimization methods, there has been a surge of interest in constructing optimal control strategies directly, viewing control synthesis through the lens of first order methods.^44^4One might as well extrapolate that these methods provide a streamline recipe for learning optimal feedback gains in real-time. Adopting such a point of view has been partially inspired by the application of learning algorithms, such as Reinforcement Learning (RL), where using principles of Dynamic Programming (DP), one can devise real-time model-free methods for both continuous-time and discrete-time LQR. Learning (over time) also has a spatial counterpart, realized in terms of control of distributed systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Such systems have become increasingly important in recent years; as such, it is desired to design feedback mechanisms that conform to a given sparsity pattern mirroring the underlying interaction topology amongst the various subsystems. That is, each "node" in the network forms its control action by employing local information collected from its neighbors; the corresponding zero pattern in the feedback gain mirrors this locality in the information exchange. Such design problems have gained a lot of attention in the system and control community over the past two decades. However, there remains a host of issues in further understanding such class of problems. For example, in the case of structured synthesis, even the existence of an optimal structured LQR gain is nontrivial to assert. A rather brief sampling of related works on the structured synthesis problem is as follows.^55^5With apologies for not going over a large body of work in this area. In, a combined primal-dual method with a penalty function is employed to obtain a feedback controller with the desired zero pattern. The work proposes a relaxed mixed-integer semidefinite-programming in which the graph topology is enforced through the integer constraints. Directly related to the present work is, where the authors propose a projected gradient descent algorithm for structured synthesis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, inspired by the work, we examine first order methods for solving the centralized and distributed LQR problem. In this direction, we first "tweak" the LQR problem formulation, motivated by the well-known fact that the state-feedback law is independent of the initial state of the system. In order to eliminate the dependence on this initial state, we adopt a cost function that sums the traditional LQR cost over a set of linearly independent initial states. This cost function can then be viewed as a well-defined matrix function over stabilizing feedback gains. We argue that this formulation (see §3.2 for details) is necessary for the adoption of first order methods for LQR-type problems. More importantly, in this setting, we show that the cost is smooth, coercive and gradient dominated over its effective domain.^66^6The property was first observed; in this paper, we provide an alternate proof of this fact. We then proceed to show that the LQR cost over the set of stabilizing state feedback gains does attain a minimum, by showing that all its sub-level sets are compact.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Subsequently, using the topological and metrical properties of the set of (static) stabilizing feedback gains, one can conclude that the proposed optimization formulation of LQR synthesis does attain its global minimum. This cost function also gives rise to three types of well-posed flows over the set of stabilizing controllers, namely, gradient flow, natural gradient flow and the quasi-Newton flow. In this direction, we prove that the Lyapunov functionals for these flows decay at an exponential rate and the corresponding trajectories are exponentially stable in the sense of Lyapunov.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then proceed to discuss the forward Euler discretization of these flows, realized as gradient descent, natural gradient descent and the quasi-Newton iteration (hence, the state feedback gain can be updated iteratively). The problem of solving the LQR using direct gain (policy) update has been addressed, where it is shown that first-order gradient descent in fact converges to the optimal feedback gain.^77^7To be more precise, the work establishes the convergence of cost function; as such, the convergence of iterates, i.e., feedback gains, is not shown explicitly. This setup was also considered, without a convergence analysis. In, the gradient dominated property, is used to guarantee the global convergence of gradient descent and natural gradient descent. The discretization scheme obtained in the present work is consistent with the setup adopted, but in some ways, approaches the problem more directly and indeed, provides a practical choice of stepsize for gradient descent and improves the choice of stepsize for natural gradient descent and quasi-Newton iteraton.^88^8Our approach primary aims to mold the LQR synthesis problem in the spirit of.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that the stepsizes in the gradient descent natural gradient descent can be obtained via the Lyapunov equations in two consecutive updates; the coerciveness of the cost function on the other hand, ensures that the updated feedback gains remain stabilizing. As such, both the function values and feedback gains converge linearly to the corresponding global minimum. In view of these observations, one can then state that the proposed iterations generate a sequence of stabilizing feedback gains that converge linearly to the optimal LQR gain. Particularly in the case of natural gradient descent we obtain a sequence of value matrices that is monotonically decreasing on the positive semidefinite cone.^99^9The terminology "natural gradient descent" (flow) is reserved for a particular choice of Riemannian metric; see §5 for details. Convergence rate of the quasi-Newton iteration is also analyzed,^1010^10The quasi-Newton iteration is consistent with Hewer's algorithm, essentially a Newton's iteration. However, traditionally, the emphasis has been placed on the convergence of the value matrices, rather than direct policy update.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a more transparent motivation as to why the proposed algorithm is a "quasi-Newton" iteration over direct policy space. proving that the corresponding iterates and function values converge quadratically to the global optima.^1111^11The algorithm is referred to as "Gauss-Newton" in and the convergence was only shown to be linear rather than $Q$-quadratic.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work also considers the extension of the proposed synthesis framework to the problem of designing feedback gains with an arbitrary sparsity pattern. This setup is inspired by the scheme adopted. In this direction, we propose a formalism to set up the problem where projected gradient descent has a simple realization. In the case of structured synthesis, the LQR cost function is no longer "gradient dominated" and the choice of stepsize can not be generalized from the unstructured case. On the other hand, the proposed stepsize choice in assumes a rather involved analytical form and convergence analysis to first-order stationary point is not straightforward.^1212^12The stepsize sequence described in is asymptotically vanishing. As such, the convergence is only guaranteed if the sequence is square summable but not absolutely summable. However, these conditions were not verified. Furthermore it has been stated that the proposed algorithm will converge to a local minimum. This is not necessary valid as gradient descent for nonconvex objectives can in principle only converge to a first-order stationary point. One might invoke an "escaping saddle" type argument here but this requires more work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we adapt the machinery developed for the unstructured LQR for the structured synthesis: we first define the initial state independent LQR formulation and then show that the cost function can be equivalently defined as the unstructured LQR cost function restricted to the linear space defined by the information-exchange graph; as such, the cost function is smooth in the subspace topology and has a coercive property. Using this setup, we can obtain the gradient and Hessian of the cost function, leading to a natural choice of stepsize by bounding the Hessian over the initial sublevel set. We show this stepsize will guarantee a nonasymptotic sublinear convergence rate to the first-order stationary point.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is as follows. The LQR problem statement and related definitions are provided in §3. The averaged LQR cost over a set of linearly independent initial states is also defined in §3. §3.4 introduces the analytical properties of the LQR cost function.. Subsequently, gradient flow, natural (Riemannian) gradient flow and quasi-Newton flow are introduced in §4, §5 and §6, respectively. Discrete realizations of these flows, namely, gradient descent, natural gradient descent and quasi-Newton iterations are addressed in §4.1, §5.1 and §6.1. §7 introduces the formalism for setting up a first order approach for structured LQR synthesis, supplemented with the stepsize selection analysis and sublinear convergence to the first-order stationary point. §8 presents simulation results to illustrate the theoretical contributions of the paper; in §9, we provide a few concluding remarks.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Setup and its Analytic Properties", "weight": 1.0} -->

In this section, we provide an overview of LQR, and in particular its modified initial state independent version, as well as a few analytic observations that are of independent interest. Although the reader might know of the extensive LQR literature, we note that some of these observations have only become necessary when the LQR optimization is viewed directly on the set of stabilizing feedback gains.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Discrete-time LQR", "weight": 1.0} -->

In the standard setup of LQR, we consider a (discrete-time) linear time invariant model of the form, where $A \in {{\mathbb{M}}_{n \times n}{({\mathbb{R}})}}$ and $B \in {{\mathbb{M}}_{n \times m}{({\mathbb{R}})}}$. The LQR problem is the optimization problem of devising a linear feedback gain $K \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$ for which $u_{k} = {- {Kx_{k}}}$, minimizing,^1414^14The condition that $u_{k}$ has the form $- {Kx_{k}}$ is not set a priori in the LQR formulation; this feedback form is typically shown via the adoption of a dynamic programming step.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Discrete-time LQR", "weight": 1.0} -->

where $x_{0}$ is the initial condition, and the quadratic cost is parameterized by ${0 \preceq Q \in {\mathbb{S}}_{n}},$ and $0 \prec R \in {\mathbb{S}}_{m}$. LQR is traditionally solved via dynamic programming or calculus of variations, leading to the celebrated Algebraic Riccati Equation (ARE).^1515^15For the dynamic programming case, one starts with the finite horizon case, apply the optimality principle, and then identify a solution concept for the infinite horizon case using a limit argument; calculus of variations provide another approach for deriving necessary conditions for LQ-type problems.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Cost function for direct policy update", "weight": 1.0} -->

In order to update the feedback gain (policy) directly, it will be conceptually appealing to consider the cost as a matrix function over the set of feedback gains. With this aim in mind, we may define $J_{x_{0}}:{{{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}\rightarrow{\mathbb{R}}}$ as, for some fixed initial condition $x_{0} \in {\mathbb{R}}^{n}$. Our first task in this direct optimization setup is to determine the domain over which the function is well-defined.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Cost function for direct policy update", "weight": 1.0} -->

In the meantime, for a non-stabilizing $K$, i.e., ${\rho{({A - {BK}})}} \geq 1$, when the system matrix $A - {BK}$ has both stable and unstable modes, if $x_{0}$ is chosen to be in the span of eigenspace corresponding to stable modes, ${J_{x_{0}}{(K)}} < \infty$. That is, $\{{K:{\rho{({A - {BK}})}} < 1}\}$ is a proper subset of $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Cost function for direct policy update", "weight": 1.0} -->

Indeed, $\{{K:{\rho{({A - {BK}})}} < 1}\}$ is the interior of $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{(J_{x_{0}})}$. Before proving this, we show that the set of feedback gains for which a fixed vector $x$ is not orthogonal to any eigenvector of the closed-loop system is dense.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Initial condition independent formulation of LQR", "weight": 1.0} -->

This can be achieved by choosing a set of linearly independent vectors ${\{ x_{0}^{1},\ldots,x_{0}^{n}\}} \subseteq {\mathbb{R}}^{n}$ and defining,^1717^17Of course, one may choose the standard basis $\{ e_{1},\ldots,e_{n}\}$, where $e_{i}$ is the vector with zero entries except a "1" at the $i$th entry; the choice of an arbitrary basis simply retains flexibility.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Initial condition independent formulation of LQR", "weight": 1.0} -->

As such, the function $f$ would be infinite if $K$ is not stabilizing (see Lemma 3.7 for details).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

The initial independent formulation is rather natural for general optimal control problems. In such problems, it is often desired to constrain the control synthesis to stabilizing feedback gains. For a learning algorithm that is built around a descent direction, such a formulation allows for an automatic enforcement of this stabilizing feature.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

We shall now see that $f$ enjoys several favorable properties, e.g., $f$ is differentiable over its effective domain and $f$ diverges to infinity when $K$ tends to the boundary of this domain, i.e., $f$ is coercive.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

This is due to the fact that matrix $X$ only makes (mathematical) sense if $K$ is stabilizing, but $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}{({J_{x_{0}^{j}}{(K)}})}$ contains non-stabilizing feedback gains; see 3.2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Alternatively, we could let $x_{0} \sim \mathcal{D}$, where $\mathcal{D}$ denotes some probability distribution, and let As long as the samples span the whole space with probability $1$, the function enjoys same properties as we have defined above. This is indeed the formulation adopted, without discussing its implications on differentiablility and coerciveness of $$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Analytical Properties of the LQR cost function", "weight": 1.0} -->

In this section, we investigate the properties of the LQR cost. We will observe that, $f$ is a real analytic function over its domain. $f$ is coercive and has compact sublevel sets.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Analytical Properties of the LQR cost function", "weight": 1.0} -->

To simplify the notation, in the rest of this paper, we shall denote^1818^18On some occations, we use subscript $M_{K}$ to emphasize the dependence on feedback gain $K$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Analytical Properties of the LQR cost function", "weight": 1.0} -->

Let us recall some of the topological properties of the set of Schur stabilizing feedback gains $\mathcal{S}$; the proofs can be found.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 3.11", "weight": 1.0} -->

We note that at $K_{\ast}$, for every $E \in {{\mathbb{M}}_{m \times n}{({\mathbb{R}})}}$, the action of Hessian is positive: namely, ${\nabla^{2}f}{(K)}$ is positive definite. This validates that $K_{\ast}$ is a local minimizer--and thus--the global minimizer, as $K_{\ast}$ is the unique stationary point.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 3.11", "weight": 1.0} -->

We now observe that the LQR cost is a *gradient dominated* function.^2828^28This property is also referred as Polyak-Łojasiewicz condition, as a special case of what had been proposed. The proof of this property in (Corollary 5) is based on a careful comparison of the cost difference in each time step between the optimal policy and a specified policy. Here, we provide an alternate proof of this important property. This alternate approach is more control-theoretic in the sense that it is mainly concerned with the properties of the Lyapunov equation. Moreover, this approach allows determining an upper bound on the gradient dominance coefficient--that in turn--facilitates estimating the iteration compexity of the gradient descent algorithm to reach an $\varepsilon$-precision solution for LQR.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gradient Flow on $\\mathcal{S}$", "weight": 1.0} -->

In this section, we show that the LQR cost function gives rise to a well-posed gradient flow, Let us first observe that admits a unique solution for all time $t$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discretization of Gradient Flow", "weight": 1.0} -->

In this section, we examine the discretization of the gradient flow. As we have observed in Lemma 4.3 and Theorem 4.2, both the energy functional and the trajectory of this flow converge exponentially to their respective global minimum. Ideally, a gradient descent algorithm converges linearly for the function values as well as the iterates. In this direction, the forward Euler discretization of the gradient flow yields, where $\eta_{j}$ is a nonnegative stepsize to be determined. The stepsize (or learning rate) should reflect two principles during the iterative process: stay stabilizing and sufficiently decrease the function value. In following, we shall see that the gradient dominated property leads to a stepsize that results in a sufficient decrease in the function values while the coerciveness guarantees that the acquired feedback gain is stabilizing.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discretization of Gradient Flow", "weight": 1.0} -->

To begin, we observe that if $K_{j + 1} = {K_{j} - {\eta_{j}{\nabla f}{(K_{j})}}}$, provided that $K_{j}$ and $K_{j + 1}$ are both stabilizing, the difference of the value matrix $X_{j + 1} - X_{j}$ can be characterized as follows.^3030^30This relationship is used.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

In our simulations, the linear rate is much better than what is estimated by the above result.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

It is now straightforward to bound the number of iterations needed to reach $\varepsilon$-precision in terms of problem data.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 4.9", "weight": 1.0} -->

We shall point out this complexity bound is very conservative as in determining stepsize, several crude bounds were used. Empirically, we observe that the actual convergence rate is faster than the one given here.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Natural Gradient Flow on $\\mathcal{S}$", "weight": 1.0} -->

If we inspect the proof of gradient dominated property (Lemma 3.12) and the Lyapunov stability of the gradient system (Theorem 4.2), the positive definite matrix $Y$ does not affect the qualitative nature of these properties. Nevertheless, the matrix $Y$ introduces a constant factor in the corresponding upper bounds. In this section, we consider a family of gradient systems of the form, where $\gamma > 0$ is (real) scalar.^3636^36When $\gamma = 1$, this flow can be viewed as the continuous limit of the natural gradient descent as discussed. As discussed subsequently, such parameterized gradient system can achieve better convergence rate for different values of $\gamma$. Viewing such a gradient flow in the context of a flow on a Riemannian manifold is particularly pertinent.^3737^37We will see that in our case, it is better to choose $\gamma$ other than $\gamma = 1$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 5.5", "weight": 1.0} -->

Over the Riemannian manifold, the Lyapunov functional converges exponentially to the origin via the natural gradient flow, which leads to an exponentially stable trajectory.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 5.7", "weight": 1.0} -->

We note that the convergence rate of trajectory $K_{t}$ is dependent on $\lambda_{1}{(Y)}$ and $\lambda_{n}{(Y)}$. For example, when $\gamma = 1$ and $\mathbf{\Sigma} = {2I}$, then the natural gradient flow converges faster than the gradient flow since ${\lambda_{1}{(Y)}} > 1$. On the other hand, if $\gamma = 1$ and ${\lambda_{1}{(Y)}} < 1$, then gradient flow converges faster than natural gradient flow.^3939^39This can be done by an $\mathbf{\Sigma}$ that has a spectrum bounded by $1$. Simulation results in §8 show that this parameterized gradient flow offers a significant computational advantage for LQR.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 5.7", "weight": 1.0} -->

We remark that in the particular case of $\gamma = 1$, the natural gradient flow has a favorable property with respect to the induced flow on the value matrix $X_{t}$. Consider again the flow, inducing the flow over the "value" matrix $X_{t} ≔ {X{(K_{t})}}$ given,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discretization of Natural Gradient Flow", "weight": 1.0} -->

In this section, we delve into the discretization of natural gradient flow; we shall only consider the case when $\gamma = 1$.^4040^40Other choices can be analyzed in a similar manner. Specifically, we consider the gradient flow, The forward Euler discretization yields, where $\eta_{j}$ is the stepsize to be determined. In discretizing gradient flow, our guideline is to choose a stepsize such that the function value is sufficiently decreased while keeping iterates stabilizing. However, in natural gradient flow with $\gamma = 1$, we observe that by Lemma 5.8: if we follow the natural gradient flow, the value matrix is monotonic with respect to the semidefinite cone. This essentially means that taking a sufficiently small stepsize in the direction of the natural gradient would guarantee a decrease in the value of the Lyapunov matrix solution $X_{t + \delta} \preceq X_{\delta}$. The reader is also referred to (Lemma 15) where a similar stepsize for the natural gradient update has been derived).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 5.11", "weight": 1.0} -->

We note that the discretization of natural gradient flow can perform better than gradient descent. One can monitor the one step progression $r_{j} - r_{j + 1}$ to confirm such a behavior. This is different from the continuous flows as if ${\lambda_{1}{(Y)}} > 1$, then gradient flow performs better than natural gradient flow.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quasi-Newton Flow on $\\mathcal{S}$", "weight": 1.0} -->

In this section, we motivate a quasi-Newton flow over the set of stabilizing feedback gains (policy) $\mathcal{S}$.^4141^41The justification for calling this evolution a quasi-Newton flow becomes apparent subseqeuntly. As observed previously, the Hessian of the LQR cost $f{(K)}$ is not positive definite everywhere. As such, there is no well-defined notion of (global) Newton iteration over policy space. However, examining Lemmas 4.4 and 5.9 allows us to derive a local second-order approximation of the LQR cost under the Riemannian metric $Y$. With is metric, recall that the gradient of $f$ is, We now provide the second-order approximation of the cost function.^4242^42Lemma 6.1 can be considered as a slight extension of Lemma $6$. However, the emphasis in was on the asymptotic behavior of the first-order approximation; this setup was subsequently utilized for a different purpose.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Quasi-Newton Flow on $\\mathcal{S}$", "weight": 1.0} -->

For our purpose, it is important to prove that for the second-order approximation, the remainder of the approximation is $O{({\|{\DeltaK}\|}^{2})}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discretization of Quasi-Newton Flow", "weight": 1.0} -->

The quasi-Newton flow over $\mathcal{S}$ has interesting consequences in terms of its discretization: the forward Euler leads to the iterative procedure with stepsize $\eta_{j}$ to be determined; we shall show that with constant stepsize $\eta = \frac{1}{2}$, both the function value and the iterates will converge quadratically to the optima.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 6.2", "weight": 1.0} -->

The update is consistent with the Gauss-Newton updates proposed. We have chosen to refer to this update as quasi-Newton in this paper as it is obtained by minimizing a local second-order approximation of the LQR cost at each iteration.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 6.2", "weight": 1.0} -->

We first observe that if $\eta \leq 1$, the corresponding sequence of value matrices $\{ X_{j}\}$ is monotonically decreasing over the positive semidefinite cone.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 6.4", "weight": 1.0} -->

With the optimal choice of stepsize as $\eta = {1/2}$, the quasi-Newton over $K$ coincides with the Hewer' algorithm, obtained by considering the Newton iteration over the ARE. We have thus provided an alternative point view of this algorithm: the algorithm can be obtained directly over the policy space even without the ARE.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Structured LQR Synthesis", "weight": 1.0} -->

In this section, we consider the problem of designing the feedback gain $K$ over a subspace. In particular, we are primary interested in feedback gains with a desired sparsity pattern. This is a natural formulation of distributed networked systems on an information-exchange graph $\mathcal{G} = {(V,E)}$. In such a setting, structured feedback gains reflecting the underlying interaction network are of particular interest. If the state of only a subset of agents is accessible for control implementation, the feedback gain must have a zero pattern that is compatible with this accessibility requirement, i.e., $K_{ij} = 0$ if ${(i,j)} \notin {E{(\mathcal{G})}}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Structured LQR Synthesis", "weight": 1.0} -->

In this section, we are interested in optimizing the LQR cost over the set, where $\mathcal{U}$ is a linear subspace defined by the graph structure, i.e., In light of the central theme of this work, projected gradient descent (PGD) is a natural choice for determining the feedback gain in the set $\mathcal{K}$, optimizing $f$ over $\mathcal{U}$. Such an approach leads to the iteration of the form, where $\eta$ is the stepsize; the choice of this stepsize will be discussed in §7.1. One may note that the geometry of $\mathcal{K}$ can be rather involved. Indeed, this set could have exponentially many path connected components (see). In the meantime, a favorable structure for $A$ and the graph $\mathcal{G}$ would guarantee that $\mathcal{K}$ has only one connected component. This point will not be further discussed in this paper.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Structured LQR Synthesis", "weight": 1.0} -->

Herein, we further examine how to update the feedback gain in the path connected component of $\mathcal{K}$, once the algorithm has been initialized in this component.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Structured LQR Synthesis", "weight": 1.0} -->

Even this more modest objective however faces some issues as $\mathcal{K}$ has an intricate geometry and one has to address how to efficiently project onto it. In the sequel, we shall show that the seemingly relaxed update rule, is equivalent to, where $P_{\mathcal{U}}$ denotes the orthogonal projection onto $\mathcal{U}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Convergence of Projected Gradient Descent", "weight": 1.0} -->

As we have argued, the projected gradient descent scheme is equivalent to gradient descent on $g$.^4545^45One should note that the analysis in § 4.1 can not be adopted for the projected case. In the analysis of one step progression of gradient descent, the crucial fact is that the difference between $f{(K_{j})}$ and $f{(K_{j + 1})}$ is bounded in terms of product of positive semidefinite matrices.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Convergence of Projected Gradient Descent", "weight": 1.0} -->

In fact, $\mathcal{V}$ could be negative definite or indefinite in general. Conceptually, the stepsize can be determined as follows: if $K_{0} \in \mathcal{K}$, then the sublevel set $S_{g{(K_{0})}} = {\{{K \in \mathcal{S}:{g{(K)}} \leq {g{(K_{0})}}}\}}$ is compact.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Convergence of Projected Gradient Descent", "weight": 1.0} -->

As $\|{{\nabla^{2}g}{(K)}}\|$ is continuous, there is a scalar $L > 0$ such that ${\max_{K \in S_{g{(K_{0})}}}{\|{{\nabla^{2}g}{(K)}}\|}} = L$, i.e., the gradient mapping ${\nabla g}{(K)}$ is Lipschitz continuous with rank $L$ on $S_{g{(K_{0})}}$. We may have chosen a constant stepsize $1/L$ if $g$ was a convex function. However, nonconvexity of $g$ and $\mathcal{K}$ introduce additional complications for determining the constant stepsize. In fact, we need to first address whether the sequence ${\{ K_{j}\}}_{j = 0}^{\infty}$ generated by is guaranteed to stay in $\mathcal{K}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Convergence of Projected Gradient Descent", "weight": 1.0} -->

As in the convergence analysis of $L$-smooth convex functions, at iterate $K_{j}$, a quadratic function majorizing $g{(K)}$ is formulated; in this case, minimizing the quadratic majorizing function will lead to the global minimum. In our case, the quadratic majorant, only majorizes $g{(K)}$ over the sublevel set $S_{g{(K_{0})}}$. Since $\mathcal{K}$ is not convex, it is not straightforward that, is still stabilizing. But the coerciveness of $g$ remedies this complication.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Choosing the stepsize for projected gradient descent", "weight": 1.0} -->

As we have pointed out, choosing an appropriate stepsize is equivalent to estimating the operator norm of the Hessian ${\nabla^{2}g}{(K)}$ over the sublevel set $S_{g{(K_{0})}}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 7.10", "weight": 1.0} -->

We shall point out that as the projected gradient descent algorithm proceeds the function values $g{(K)}$ decrease. Hence, we can re-estimate the bounds in the above propositions at each iteration. For example, at iteration $K_{j}$, the Lipschtiz constant $L_{K_{j}}$ of ${\nabla g}{(K)}$ over the sublevel set $S_{g{(K_{j})}}$ can be estimated and we may as well use a stepsize $1/L_{K_{j}}$ by Lemma 7.4. The benefit is that this stepsize is certainly larger than $1/L_{f{(K_{0})}}$. In this case, we shall have an increasing sequence of stepsizes ${\{{1/L_{j}}\}}_{j = 0}^{\infty}$ that is bounded from above.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 7.10", "weight": 1.0} -->

The stepsize rule devised here certainly works for unstructured case (i.e., gradient descent). However, this stepsize is typically smaller than the one we work out in Lemma 4.5. The reason is that here all the terms must be bounded over the whole sublevel set while in Lemma 4.5 we carefully compare one step progression of gradient descent.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In this section, we provide a representative set of examples to demonstrate the results reported in this paper.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We first demonstrate the exponential stability of the proposed continuous flows. The system is of form with parameters $(A,B)$, $A \in {\mathbb{R}}^{100 \times 100}$ and $B = I$, guaranteeing the controllability of the system. The entries of $A$ are sampled from a standard normal distribution $\mathcal{N}{}$. We also scale $A$ when necessary to make it stable such that the initial feedback gain can be set as $K_{0} = 0$. The cost matrices $Q,R$ are taken to be identity with appropriate dimensions. For the natural gradient, we simulate the flow with two different Riemannian metrics, one induced by $Y$ and the other by $Y^{2}$. Figure 3 demonstrates the exponential stability of the corresponding trajectories and Figure 3 depicts the exponential stability of the Lyapunov functionals for all flows when $\mathbf{\Sigma} = {0.5I}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The results are consistent with the observations discussed in §4, §5, and §6. In particular, since ${\lambda_{1}{(Y)}} < 1$, the natural gradient flow converges faster than the gradient flow, and amongst the natural gradient flows, the one with the metric induced by $Y^{2}$ outperforms the one with metric $Y$. Figures 5 and 5 show the convergence results with the same LQR parameters $(A,B,Q,R)$, but the initial state matrix has chosen to be $\mathbf{\Sigma} = {2I}$. These two figures underscore the observations in Remark 5.7: gradient flow outperforms natural gradient flows when ${\lambda_{1}{(Y)}} > 1$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Next we examine the discrete realizations of these flows, namely, gradient descent, natural gradient descent and the quasi-Newton iteration (with the same setup for system parameters). With the adaptive stepsize proposed in Theorem 4.6, Figure 7 demonstrates that the sequence of feedback gains generated by gradient descent is stabilizing and converges to the global optimal feedback gain. Moreover, Figure 7 shows that the cost function $f{(K)}$ converges to $f{(K_{\ast})}$ at a linear rate.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

The paper considers LQR through the lens of first order methods--an LQR calculus--where control synthesis is viewed directly in terms of optimizing an objective function over the set of stabilizing feedback gains. Using this narrative, we proceed to examine gradient descent and its various extensions for solving the LQR problem. The LQR objective is constructed over a set of linearly independent initial states to eliminate the dependency of the optimal policy on the initial state and encode closed loop stability. It is shown that the corresponding cost function is smooth, coercive and gradient dominated (this latter fact was previously reported in the literature; we provide an alternate approach for its proof). We next discussed three types of well-posed flows over the set of stabilizing controllers: gradient flow, natural gradient flow and the quasi-Newton flow. We subsequently examine the discretization of these flows, and show that their realizations using the forward Euler method, i.e., gradient descent, natural gradient flow and quasi-Newton iterations, lead to algorithms with linear convergence rate and quadratic convergence rate. Finally, we consider projected gradient descent for solving structured LQR.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this direction, we provided a stepsize rule which leads to the sublinear convergence to the first-order stationary point.
