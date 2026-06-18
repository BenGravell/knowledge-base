<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Rectified Flow: A Marginal Preserving Approach to Optimal Transport

Topics include Regression, Optimal transport, Flow, Ordinary differential equation, Convex function.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a flow-based approach to the optimal transport (OT) problem between two continuous distributions pi_0, pi_1 on R^(d), of minimizing a transport cost E[c(X_1-X_0)] in the set of couplings (X_0, X_1) whose marginal distributions on X_0, X_1 equals pi_0, pi_1, respectively, where c is a cost function. Our method iteratively constructs a sequence of neural ordinary differentiable equations (ODE), each learned by solving a simple unconstrained regression problem, which monotonically reduce the transport cost while automatically preserving the marginal constraints. This yields a monotonic interior approach that traverses inside the set of valid couplings to decrease the transport cost, which distinguishes itself from most existing approaches that enforce the coupling constraints from the outside. The main idea of the method draws from rectified flow, a recent approach that simultaneously decreases the whole family of transport costs induced by convex functions c (and is hence multi-objective in nature), but is not tailored to minimize a specific transport cost.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our method is a single-object variant of rectified flow that guarantees to solve the OT problem for a fixed, user-specified convex cost function c.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

wherewe seek tofind (the law of) an optimal coupling $(X_{0},X_{1})$ of $\pi_{0}$ and $\pi_{1}$, for which marginal laws of $X_{0},X_{1}$ equal $\pi_{0},\pi_{1}$, respectively, to minimize ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$, called the $c$-transport cost,fora cost function $c$.Theories, algorithms, and applications of optimal transport have attracted a vast literature; see, for example, the monographs of for overviews. Notably, OT has been growing into a popular and powerful technique in machine learning,for key tasks such as learning generative models, transfer learning, and approximate inference \e.g.,.The OT problem should be treated differently depending on whether $\pi_{0},\pi_{1}$ are discrete or continuous measures.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we focus on the continuous case when $\pi_{0},\pi_{1}$ are high dimensional absolutely continuous measures on ${\mathbb{R}}^{d}$ that are observed through empirical observations, a setting called data-driven OT.A well known result in OT \e.g., shows that,if $\pi_{0}$ is continuous, the optimization in can be restricted to the set of deterministic couplings satisfying $X_{1} = {T{(X_{0})}}$ for some continuous transport mapping $T:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$,which is oftenapproximated in practice with deep neural networks \e.g.,.However, continuous OT remains highly challenging computationally.One major difficultyis to handle the coupling constraints of ${{Law}{(X_{0})}} = \pi_{0}$ and ${{Law}{(X_{1})}} =

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

\pi_{1}$,which are infinite dimensional when $\pi_{0}$ and $\pi_{1}$ are continuous.As a result, can not be solved as a "clean" unconstrained optimization problem.There are essentially two types of approaches to solving in the literature.One uses Lagrange duality to turn into a certain minimax game, and the other one approximatesthe constraint with an integral (often entropic-like) penalty function.However, the minimax approaches suffer from convergence and instability issues andare difficult to solve in practice,while the regularization approach can not effectively enforce the infinite-dimensional coupling constraints.

<!-- chunk {"id": "body-0007", "role": "body", "section": "This work", "weight": 1.0} -->

We present a different approach tocontinuous OTthat re-frames intoa sequence of simple unconstrained nonlinear least squares optimization problems,whichmonotonically reduce the transport cost of a couplingwhile automatically preserving the marginal constraints.Different from theminimax and regularization approaches that enforce the constraints from outside,our method is an *interior* approachwhich starts from a valid coupling (typically the naive independent coupling), and traverses inside the constraint set to decrease the transport cost.Such an interior approach is non-trivial and has not been realized before, because there exists no obvious unconstrained parameterization of the set of couplings of $\pi_{0}$ and $\pi_{1}$. Our method is made possible by leveraging*rectified flow*,a recent approach to constructing (non-optimal) transport maps for generative modeling and domain transfer.What makes rectified flow specialis that it provides a simple procedurethat turns a given coupling into a new one thatobeys the same marginal laws, while yielding no worse transport cost w.r.t.

<!-- chunk {"id": "body-0008", "role": "body", "section": "This work", "weight": 1.0} -->

*all* convex functions $c$ simultaneously.Despite this attractive property,as pointed out,rectified flow can not be used to optimize any fixed cost $c$,as it is essentially a special *multi-objective* optimization procedure that targets no specific cost.Our method is a variant of rectified flow that targets a user-specified cost function $c$ and hence yields a new approach to the OT problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Rectified flow", "weight": 1.0} -->

We provide a high-level overview ofthe rectified flow of and the main results of this work.For

<!-- chunk {"id": "body-0010", "role": "body", "section": "Rectified flow", "weight": 1.0} -->

and $X_{t}$ is the linear interpolation between $X_{0}$ and $X_{1}$.Eq isa least squares regression problem of predicting the line direction of $({X_{1} - X_{0}})$ from every space-time point $(X_{t},t)$ on the linear interpolation path, yielding a solution of

<!-- chunk {"id": "body-0011", "role": "body", "section": "Rectified flow", "weight": 1.0} -->

which isthe average of direction $({X_{1} - X_{0}})$ for all lines that pass point $X_{t} = z$ at time $t$.The (conditional) expectations ${\mathbb{E}}{\lbrack \cdot \rbrack}$ above are w.r.t.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Rectified flow", "weight": 1.0} -->

In practice,the expectation ${\mathbb{E}}{\lbrack \cdot \rbrack}$ is approximated by empirical observations of $(X_{0},X_{1})$, and$v$ is approximated by a parametric family, such as deep neural networks.In this case, the optimization in Eq can be solved conveniently with off-the-shelf stochastic optimizers such as stochastic gradient descent (SGD),without resorting to minimax algorithms or expensive inner loops.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Rectified flow", "weight": 1.0} -->

The initialization can be taken to bethe independent coupling ${(Z_{0}^{0},Z_{1}^{0})} \sim {\pi_{0} \times \pi_{1}}$,or any other couplings that can be constructed from marginal (unpaired) observations of $\pi_{0}$ and $\pi_{1}$.In practice,each step of $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ is empirically approximated by first drawing samples of $(Z_{0}^{k},Z_{1}^{k})$ from the ODE with drift $v^{k}$, and then constructing the next flow $v^{k + 1}$ from the optimization.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Rectified flow", "weight": 1.0} -->

Although this process accumulates errors,it was shown that one or two iterations are sufficient for practical applications.Note that the $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ procedure is "cost-agnostic"in that it does not dependent on any specific cost $c$.Although the recursive$\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ update is monotonically non-increasing on the transport cost for all convex $c$, it does not necessarily converge to the optimal coupling for any pre-specified $c$,as the update would stop whenever two cost functions are conflicting with each other.In,a coupling $(X_{0},X_{1})$ is called *straight* if it is a fixed point of

<!-- chunk {"id": "body-0015", "role": "body", "section": "Rectified flow", "weight": 1.0} -->

a convex $c$ must be straight, but the opposite is not true in general.One exception is the one dimension case ($d = 1$), for which all convex functions $c$ (whose $c$-optimal coupling exists) share a common optimal coupling that is also straight.But this does not hold when $d \geq 2$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "$c$-Rectified flow", "weight": 1.0} -->

In this work,we modify the $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ procedure so that it can be used tosolve given a user-specified cost function $c$.We show that this can be done easily by properly restricting the optimization domain of $v$ and modifying the loss functionin.The case of quadratic loss ${c{(x)}} = {\frac{1}{2}\left.

<!-- chunk {"id": "body-0017", "role": "body", "section": "$c$-Rectified flow", "weight": 1.0} -->

\parallel x\parallel \right.^{2}}$is particularly simple,for which we simplyneed to restrict the $v$to be a gradient field $v_{t} = {\nabla f_{t}}$ in the optimization of.For

<!-- chunk {"id": "body-0018", "role": "body", "section": "Outline", "weight": 1.0} -->

The rest of the work is organized as follows. Section 2introduces the background of optimal transport. Section 3reviews rectified flow of from an optimization-based view.Section 4 characterizesthe if and only if conditionfor two differentiable stochastic processes to have equal marginal laws.Section 5 introduces the main $c$-rectified flow method and establishes its theoretical properties.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Static formulations", "weight": 1.0} -->

The optimal transport problem wasfirst formulated byGaspard Monge in 1781 when he studiedthe problem of how toredistribute mass, e.g., a pile of soil, with minimal effort.Monge's problem can be formulated as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Static formulations", "weight": 1.0} -->

where we minimize the $c$-transport costin the set of deterministic couplings $(X_{0},X_{1})$ that satisfy $X_{1} = {T{(X_{0})}}$ for a transport mapping $T:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$.The Monge--Kantorovich (MK) problem in is the relaxationof to the set of all (deterministic and stochastic) couplings of $\pi_{0}$ and $\pi_{1}$.The two problems are equivalent when the optimum of is achieved by adeterministic coupling, which is guaranteed if $\pi_{0}$ is an absolutely continuous measure on ${\mathbb{R}}^{d}$.A key feature of the MK problem is that it isa linear programming w.r.t.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Static formulations", "weight": 1.0} -->

As the left side of only depends on $(X_{0},X_{1})$ and the right side only on $(\mu,\nu)$, one can show that $(X_{0},X_{1})$ is $c$-optimal and $(\mu,\nu)$ solves iff${{\mu{(X_{0})}} + {\nu{(X_{1})}}} = {c{({X_{1} - X_{0}})}}$holds with probability one, which provides a basic optimality criterion. Many existingOT algorithms are developed by exploiting the primal dual relation of and(see e.g., ), but have the drawback of yielding minimax problems that are challenging to solve in practice. If $c$ is strictly convex,the optimal transport map of is unique (almost surely) and yields a form of

<!-- chunk {"id": "body-0022", "role": "body", "section": "Dynamic formulations", "weight": 1.0} -->

Both the MK and Monge problems can be equivalently framed in dynamic waysas finding continuous-time processes that transfer $\pi_{0}$ to $\pi_{1}$.Let $\{ x_{t}:{t \in {\lbrack 0,1\rbrack}}\}$ be a smooth path connecting $x_{0}$ and $x_{1}$, whose time derivative is denoted as ${\overset{˙}{x}}_{t}$.For

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dynamic formulations", "weight": 1.0} -->

where the infimum is attained when $x_{t}$ is the linear interpolation (geodesic) path: $x_{t} = {{tx_{1}} + {{({1 - t})}x_{0}}}$.Hence, the MK optimal transport problem is equivalent to

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dynamic formulations", "weight": 1.0} -->

where we optimize in the set of time-differentiable stochastic processes${\mathbf{X}} = {\{ X_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$.The optimum of is attained by $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$ when$(X_{0},X_{1})$ is a $c$-optimal coupling of, which is known as the *displacement interpolation*.We call the objective function in the path-wise $c$-transport cost.The Monge problem can also be framed in a dynamic way.Assume the transport map $T$ can be induced by an ODE model${dX_{t}} = {v_{t}{(X_{t})}dt}$ such that $X_{1} = {T{(X_{0})}}$. Then the Monge problem is equivalent to

<!-- chunk {"id": "body-0025", "role": "body", "section": "Dynamic formulations", "weight": 1.0} -->

which is equivalent to restricting $\mathbf{X}$ in to the set of processes that can be induced by ODEs.Assume that $X_{t}$ following ${dX_{t}} = {v_{t}{(X_{t})}dt}$ yields a density function $\varrho_{t}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dynamic formulations", "weight": 1.0} -->

where ${{d\pi_{i}}/d}x$ denotes the density function of $\pi_{i}$.The key idea of and is torestrict the optimization of to the set of deterministic processed induced by ODEs, which significantly reduces the search space.Intuitively,Jensen's inequality ${{\mathbb{E}}{\lbrack{c{(Z)}}\rbrack}} \geq {c{({{\mathbb{E}}{\lbrack Z\rbrack}})}}$ shows that we should be able to reduce the expected cost of a stochastic processby "marginalizing" out the randomness.In fact,we will show that, for a differentiable stochastic process $\mathbf{X}$, its ($c$-)rectified flow yields no largerpath-wise $c$-transport cost in than $\mathbf{X}$ (see Lemma 3.3 and Theorem 5.3 ‣ 5.1 𝑐-Rectified Flow of Time-Differentiable Processes 𝑿 ‣ 5 𝑐-Rectified Flow

<!-- chunk {"id": "body-0027", "role": "body", "section": "Dynamic formulations", "weight": 1.0} -->

‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")).However, all the dynamic formulations above are still highly challenging to solve in practice.We will show that $c$-rectified flow can be viewed as a special coordinate descent like approachto solving (Section 5.4).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

We introduce rectified flow of from an optimization-based perspective:we show that rectified flow can be viewed as the solutionof a special constrained dynamic optimization problem,which allows us to gain more understanding of rectified flow and motivates the development of $c$-rectified flow.Following,for a time-differentiable stochastic process ${\mathbf{X}} = {\{ X_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$, its expected velocity field $v^{\mathbf{X}}$ is defined as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

where the optimization is on the set of all measurable velocity fields $v:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$.The

<!-- chunk {"id": "body-0030", "role": "body", "section": "Rectified Flow: An Optimization-Based View", "weight": 1.0} -->

Moreover, the rectified flow of a coupling $(X_{0},X_{1})$is defined as the rectified flow of $\mathbf{X}$ when $\mathbf{X}$ is the linear interpolation of $(X_{0},X_{1})$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "A optimization view of rectified flow", "weight": 1.0} -->

We show thatthe rectified flow $\mathbf{Z}$ of $\mathbf{X}$achieves the minimum of the path-wise $c$-transport cost in the set of time-differentiable stochastic processes whose expected velocity field equals $v^{\mathbf{X}}$.This explains that the property of non-increasing convex transport costs of rectified flow/coupling.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Straight couplings", "weight": 1.0} -->

Obtaining straight couplingsis useful for learning fast ODE modelsbecause the trajectories of the associated rectified flow $\mathbf{Z}$ are straight lines and hence can be calculated in closed form without iterative numerical solvers. See for more discussion. Moreover, showed thatrectifiable $c$-optimal couplings must be straight.In the one dimensional case ($d = 1$),the straight coupling, if it exists, is unique and attains the minimum of ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$ for all convex functions for which $c$-optimal coupling exists.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Straight couplings", "weight": 1.0} -->

For higher dimensions ($d \geq 2$), however,straight couplings are not unique, and the specific straight couplingobtained at the convergence of the recursive $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ update (i.e. ${(Z_{0}^{k + 1},Z_{1}^{k + 1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(Z_{0}^{k},Z_{1}^{k})})}}$) is implicitly determined by the initial coupling $(Z_{0}^{0},Z_{1}^{0})$,and is not expected to be optimal w.r.t.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Straight couplings", "weight": 1.0} -->

any pre-fixed $c$.The following counter example shows a somewhat stronger negative result:there exist straight couplingsthat are not optimal w.r.t. all second order differentiable convex functions with invertible Hessian matrices.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 3.5", "weight": 1.0} -->

\parallel x\parallel \right.^{p}$ with $p > 0$,the $c$-optimal mapping is the trivial identity coupling $(X_{0},X_{0})$ with $X_{0} \sim \pi_{0}$.However,consider the coupling $(X_{0},{AX_{0}})$,where $A$ is anon-identity and non-reflecting rotation matrix (namely ${A^{\top}A} = I$, ${\det{(A)}} = 1$, $A \neq I$ and $A$ does not have $\lambda = {- 1}$ as an eigenvalue).Then $(X_{0},{AX_{0}})$ is a straight coupling of $\pi_{0}$ and $\pi_{1}$,but it is not $c$-optimal for allsecond order differentiable convex function $c$ whose Hessian matrix is invertible everywhere.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 3.5", "weight": 1.0} -->

See Appendix for the proof.It is the rotation transformthat makes $(X_{0},{AX_{0}})$ sub-optimal,which is removed in the proposed $c$-rectified flow in Section 5 via a Helmholtz like decomposition.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

The marginal preserving property of rectified flow is due to the property of $v^{\mathbf{Z}} = v^{\mathbf{X}}$ by construction.However, we show in this section that$v^{\mathbf{X}} = v^{\mathbf{Z}}$ is only a sufficient condition:two differentiable processes $\mathbf{X}$ and $\mathbf{Z}$can have the same marginal lawseven if $r ≔ {v^{\mathbf{X}} - v^{\mathbf{Z}}} \neq 0$.This is because $r$, as illustrated in Example 3.5,can be a rotation-only vector field (in a generalized sense shown below)that introduces rotation components into the dynamics without modifying the marginal distributions.Therefore, the constraint of $v^{\mathbf{Y}} = v^{\mathbf{X}}$ inthe optimization problem may be too restrictive.A natural relaxation of would be

<!-- chunk {"id": "body-0038", "role": "body", "section": "Differentiable Processes with Equivalent Marginal Laws", "weight": 1.0} -->

which yields a dynamic OT problem with a continuum ofmarginal constraints.In Section 5, we show thatthe solution of yields our $c$-rectified flow thatsolve the OT problemat the fixed point.Solving allows us to remove the rotational components of $v^{\mathbf{X}}$, which is whatwhat renders rectified flow non-optimal.In this section,we first characterize the necessary and sufficient conditionfor having equivalent marginal laws.

<!-- chunk {"id": "body-0039", "role": "body", "section": "$c$-Rectified Flow", "weight": 1.0} -->

We introduce $c$-rectified flow,a $c$-dependent variant of rectified flow that guarantees tominimize the $c$-transport costwhen applied recursively.

<!-- chunk {"id": "body-0040", "role": "body", "section": "$c$-Rectified Flow", "weight": 1.0} -->

This section is organized as follows:Section 5.1defines and discusses the $c$-rectified flow of a differentiable stochastic process $\mathbf{X}$, which we show yields the solution of theinfinite-marginal OT problem.Section 5.2 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")considers the $c$-rectified flow of a coupling $(X_{0},X_{1})$, which we show is non-increasing on the $c$-transport cost.Section 5.3proves that the fixed points of $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$ are $c$-optimal.Section 5.4interprets $c$-rectified flowas an alternating direction descent methodfor the dynamic OT problem,and a majorize-minimization (MM) algorithm for the static OT problem.Section 5.5 discussesa key lemma

<!-- chunk {"id": "body-0041", "role": "body", "section": "$c$-Rectified Flow", "weight": 1.0} -->

relating $c$-optimal couplings and its associated displacement interpolation with Hamilton-Jacobi equation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "$c$-Rectified Flow of Time-Differentiable Processes $\\mathbf{X}$", "weight": 1.0} -->

Note that we have ${\mathsf{m}_{c}(x;y)} \geq 0$ for ${\forall x},y$ following the definition of the conjugate $c^{\ast}$ (or the Fenchel-Young inequality).Losses of form $\mathsf{m}_{c}(x;y)$is equivalent to the so called *matching loss*proposed forlearning generalized linear models. Compared with the original rectified flow,the difference of $c$-rectified flow is i) restricting the velocity field to a form of $g_{t} = {{\nabla c^{\ast}} \circ {\nabla f_{t}}}$, and ii) replacing the quadratic objective function to the matching loss.These two changes combined yield a Helmholtz like decomposition of $v^{\mathbf{X}}$ as we show below, allowing us to remove the "rotation-only" component of $v^{\mathbf{X}}$ and obtain $c$-optimal couplings at fixed points.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Bregman divergence, Helmholtz decomposition, marginal preserving", "weight": 1.0} -->

We can equivalently write using Bergman divergence associated with $c$, that is,

<!-- chunk {"id": "body-0044", "role": "body", "section": "Bregman divergence, Helmholtz decomposition, marginal preserving", "weight": 1.0} -->

Moreover,the generalized Pythagorean theorem of Bregman divergence (e.g., ) gives

<!-- chunk {"id": "body-0045", "role": "body", "section": "Bregman divergence, Helmholtz decomposition, marginal preserving", "weight": 1.0} -->

which can be viewed as projecting the expected velocity $v_{t}^{\mathbf{X}}$ to the set of functions of form $g_{t} = {{\nabla c^{\ast}} \circ {\nabla f_{t}}}$,w.r.t. the Bregman divergence.This

<!-- chunk {"id": "body-0046", "role": "body", "section": "$c$-Rectified flow solves Problem", "weight": 1.0} -->

We are ready to show that the $c$-rectified flow solves the optimization problem.Further, forms a dual problem of.

<!-- chunk {"id": "body-0047", "role": "body", "section": "$c$-Rectified Flow of Coupling $(X_{0},X_{1})$", "weight": 1.0} -->

Similar to the case of rectified flow,the $c$-rectified flow/coupling of a coupling $(X_{0},X_{1})$is defined as the $c$-rectified flow/coupling of its linear interpolation process.In the following, we show that the $c$-rectified coupling of a coupling yields no larger$c$-transport cost.

<!-- chunk {"id": "body-0048", "role": "body", "section": "$c$-Rectified Flow as Optimization Algorithms", "weight": 1.0} -->

In this section, we draw more understanding on how iterative $c$-rectified flowing solves the static and dynamic OT problems. We first show that $c$-rectified flow can be viewed as an alternative direction descent on the dynamic OT problem, and then that $c$-rectified coupling as a majorize-minimization (MM) algorithm on the statistic OT problem.The results in this section are framed in terms of a general path-wise loss function $F_{c}{({\mathbf{Y}})}$,and hence provide a useful starting point for deriving $c$-rectified flow like approaches tomore general optimization problems with coupling constraints.

<!-- chunk {"id": "body-0049", "role": "body", "section": "$c$-Rectified flow as alternative direction descent on", "weight": 1.0} -->

Here in (29 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")),we minimize $F_{c}{({\mathbf{Y}})}$in the set of processes whose start-end pair $(Y_{0},Y_{1})$ equals the coupling $(Z_{0}^{k},Z_{1}^{k})$ from ${\mathbf{Z}}^{k}$,which simply yields the linear interpolation $X_{t}^{k} = {{tZ_{1}^{k}} + {{({1 - t})}Z_{0}^{k}}}$ by Jensen's inequality.In (30 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")), we minimize $F_{c}{({\mathbf{Y}})}$ given the

<!-- chunk {"id": "body-0050", "role": "body", "section": "$c$-Rectified flow as alternative direction descent on", "weight": 1.0} -->

path-wise marginal constraint of ${{Law}{(Y_{t})}} = {{Law}{(X_{t}^{k})}}$ for all time $t \in {\lbrack 0,1\rbrack}$, which yields the $c$-rectified flow following Theorem 5.3 ‣ 5.1 𝑐-Rectified Flow of Time-Differentiable Processes 𝑿 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport").Note that the updates in both (29 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")) and (30 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport"))keep the start-end marginal laws ${Law}{(Y_{0})}$ and ${Law}{(Y_{1})}$ unchanged, and hencethe algorithm stays inside the feasible set

<!-- chunk {"id": "body-0051", "role": "body", "section": "$c$-Rectified flow as alternative direction descent on", "weight": 1.0} -->

$\{{\mathbf{Y}}:{{{{Law}{(Y_{0})}} = \pi_{0}},{{{Law}{(Y_{1})}} = \pi_{1}}}\}$in once it is initialized to be so.The updates in (29 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport"))-(30 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")) highlight a key difference between our method and the Benamou-Brenier approach -:the key idea of Benamou-Brenier is to restrict the optimization domain to the set of deterministic, ODE-induced processes (a.k.a.

<!-- chunk {"id": "body-0052", "role": "body", "section": "$c$-Rectified flow as alternative direction descent on", "weight": 1.0} -->

flows),but our updates alternate between thedeterministic$c$-rectified flow ${\mathbf{Z}}^{k}$ and the linear interpolation process ${\mathbf{X}}^{k}$, which is *not* deterministic or ODE-inducableunless the fixed point is achieved.

<!-- chunk {"id": "body-0053", "role": "body", "section": "$c$-Rectified flow as an MM algorithm", "weight": 1.0} -->

The majorize-minimization (MM) algorithm is a general optimization recipe thatworks by finding a surrogate function that *majorizes* the objective function.Let $F{(X)}$ be the objective concave function to be minimize. An MM algorithm consists of iterative update of form $X^{k + 1} \in {{{\arg\min}_{Y}F^{+}}{(\left. Y \middle| X^{k} \right.)}}$,where $F^{+}$ is a majorization function of $F$ that satsifies

<!-- chunk {"id": "body-0054", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

The proof of Theorem 5.6 relies on akey lemma shows that if the trajectories of an ODE of form ${dX_{t}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(X_{t})}})}dt}$ are geodesic in that $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$,then the induced coupling $(X_{0},X_{1})$ is an $c$-optimal coupling of its marginals.The proof of this lemma relies onHamilton-Jacobi (HJ) equation, which providesa characterization of $f$for an ODE ${dX_{t}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(X_{t})}})}dt}$ whose trajectories are geodesic.The connection between HJ equation and optimal transport has been a

<!-- chunk {"id": "body-0055", "role": "body", "section": "Hamilton-Jacobi Equation and Optimal Transport", "weight": 1.0} -->

classic result andcan be found, for example,.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Connection to Benamou-Brenier Formula", "weight": 1.0} -->

The results in Lemma 5.9can also formally derived from Benamou-Brenier problem,as shown in the seminal work of.By

<!-- chunk {"id": "body-0057", "role": "body", "section": "Connection to Benamou-Brenier Formula", "weight": 1.0} -->

where we assume that $\lambda_{t}v_{r}\rho_{t}$ decays to zero sufficiently fast at infinity.We have

<!-- chunk {"id": "body-0058", "role": "body", "section": "Connection to Benamou-Brenier Formula", "weight": 1.0} -->

At the saddle points,the functional derivations of $\mathcal{L}$ equal zero, yielding

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion and Open Questions", "weight": 1.5} -->

For machine learning (ML) tasks such as generative models and domain transfer, the transport cost is not necessarily the direct object of interest.In these cases,as suggested, rectified flow might be preferred because it is simpler and does not require to specify a particular cost $c$.Question: for such ML tasks, when would it be preferred to use OT with a specific $c$, and how to choose $c$ optimally?

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion and Open Questions", "weight": 1.5} -->

In practice, recursively applying the ($c$-)rectification accumulates errorsbecause the training optimization for the drift field and the simulation of the ODEcan not be conducted perfectly.Howto avoid the error accumulationat each step?Assume ${\{ x_{1,i}\}}_{i} \sim \pi_{1}$, and ${\{ z_{0,i}^{k},z_{1,i}^{k}\}}_{i}$ is obtained by solving the ODE of the $k$-th $c$-rectified flow starting from $z_{0,i}^{k} \sim \pi_{0}$.As we increase $k$, ${\{ z_{0,i}^{k}\}}_{i}$ may yield increasingly bad approximation of $\pi_{1}$ due to the error accumulation.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion and Open Questions", "weight": 1.5} -->

With or without the adjustment step,build a complete theoretical analysis on the statistical error of the method.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion and Open Questions", "weight": 1.5} -->

In what precise sense is rectified flow solving a multi-objective variant of optimal transport?
