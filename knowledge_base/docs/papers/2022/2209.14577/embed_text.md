## Introduction

The Monge--Kantorovich (MK) optimal transport (OT) problem concerns finding an optimal coupling between two distributions $\pi_{0},\pi_{1}$:

wherewe seek tofind (the law of) an optimal coupling $(X_{0},X_{1})$ of $\pi_{0}$ and $\pi_{1}$, for which marginal laws of $X_{0},X_{1}$ equal $\pi_{0},\pi_{1}$, respectively, to minimize ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$, called the $c$-transport cost,fora cost function $c$.Theories, algorithms, and applications of optimal transport have attracted a vast literature; see, for example, the monographs of for overviews. Notably, OT has been growing into a popular and powerful technique in machine learning,for key tasks such as learning generative models, transfer learning, and approximate inference \e.g.,.The OT problem should be treated differently depending on whether $\pi_{0},\pi_{1}$ are discrete or continuous measures. In this work, we focus on the continuous case when $\pi_{0},\pi_{1}$ are high dimensional absolutely continuous measures on ${\mathbb{R}}^{d}$ that are observed through empirical observations, a setting called data-driven OT in.A well known result in OT \e.g., shows that,if $\pi_{0}$ is continuous, the optimization in can be restricted to the set of deterministic couplings satisfying $X_{1} = {T{(X_{0})}}$ for some continuous transport mapping $T:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$,which is oftenapproximated in practice with deep neural networks \e.g.,.However, continuous OT remains highly challenging computationally.One major difficultyis to handle the coupling constraints of ${{Law}{(X_{0})}} = \pi_{0}$ and ${{Law}{(X_{1})}} = \pi_{1}$,which are infinite dimensional when $\pi_{0}$ and $\pi_{1}$ are continuous.As a result, can not be solved as a "clean" unconstrained optimization problem.There are essentially two types of approaches to solving in the literature.One uses Lagrange duality to turn into a certain minimax game, and the other one approximatesthe constraint with an integral (often entropic-like) penalty function.However, the minimax approaches suffer from convergence and instability issues andare difficult to solve in practice,while the regularization approach can not effectively enforce the infinite-dimensional coupling constraints.

### This work

We present a different approach tocontinuous OTthat re-frames intoa sequence of simple unconstrained nonlinear least squares optimization problems,whichmonotonically reduce the transport cost of a couplingwhile automatically preserving the marginal constraints.Different from theminimax and regularization approaches that enforce the constraints from outside,our method is an *interior* approachwhich starts from a valid coupling (typically the naive independent coupling), and traverses inside the constraint set to decrease the transport cost.Such an interior approach is non-trivial and has not been realized before, because there exists no obvious unconstrained parameterization of the set of couplings of $\pi_{0}$ and $\pi_{1}$. Our method is made possible by leveraging*rectified flow*,a recent approach to constructing (non-optimal) transport maps for generative modeling and domain transfer.What makes rectified flow specialis that it provides a simple procedurethat turns a given coupling into a new one thatobeys the same marginal laws, while yielding no worse transport cost w.r.t. *all* convex functions $c$ simultaneously.Despite this attractive property,as pointed out in,rectified flow can not be used to optimize any fixed cost $c$,as it is essentially a special *multi-objective* optimization procedure that targets no specific cost.Our method is a variant of rectified flow that targets a user-specified cost function $c$ and hence yields a new approach to the OT problem.

### Rectified flow

We provide a high-level overview ofthe rectified flow of and the main results of this work.For a given coupling $(X_{0},X_{1})$ of $\pi_{0}$ and $\pi_{1}$,the *rectified flow*induced by $(X_{0},X_{1})$is the time-differentiable process ${\mathbf{Z}} = {\{ Z_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$ over an artificial notion of time $t \in {\lbrack 0,1\rbrack}$,that solves the following ordinary differential equation (ODE):

where $v^{X}:{{{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}}\rightarrow{\mathbb{R}}^{d}}$is a time-dependent velocity field defined as the solution of

and $X_{t}$ is the linear interpolation between $X_{0}$ and $X_{1}$.Eq isa least squares regression problem of predicting the line direction of $({X_{1} - X_{0}})$ from every space-time point $(X_{t},t)$ on the linear interpolation path, yielding a solution of

which isthe average of direction $({X_{1} - X_{0}})$ for all lines that pass point $X_{t} = z$ at time $t$.The (conditional) expectations ${\mathbb{E}}{\lbrack \cdot \rbrack}$ above are w.r.t. the randomness of $(X_{0},X_{1})$.We assume that the solution of exists and is unique,and hence$v_{t}^{X}{(z)}$ is assumed to exist at least on the trajectories of the ODE.The start-end pair $(Z_{0},Z_{1})$ induced by $\mathbf{Z}$ is called the *rectified coupling* of $(X_{0},X_{1})$,and we denote it by ${(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$. In practice,the expectation ${\mathbb{E}}{\lbrack \cdot \rbrack}$ is approximated by empirical observations of $(X_{0},X_{1})$, and$v$ is approximated by a parametric family, such as deep neural networks.In this case, the optimization in Eq can be solved conveniently with off-the-shelf stochastic optimizers such as stochastic gradient descent (SGD),without resorting to minimax algorithms or expensive inner loops. This makes rectified flow attractive for deep learning applications as these considered in.The importance of ${(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$ is justifiedby two key properties:1) *$(Z_{0},Z_{1})$ shares the same marginal laws as $(X_{0},X_{1})$ and is hence a valid coupling of $\pi_{0}$ and $\pi_{1}$;* 2) *$(Z_{0},Z_{1})$ yields no larger convex transport costs than $(X_{0},X_{1})$,that is, ${{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} \leq {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}$,for *every* convex function $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$.*Hence, it is natural to recursively apply the $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ mapping, that is,${(Z_{0}^{k + 1},Z_{1}^{k + 1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(Z_{0}^{k},Z_{1}^{k})})}}$ starting from ${(Z_{0}^{0},Z_{1}^{0})} = {(X_{0},X_{1})}$,yielding a sequence ofcouplingsthat is monotonicallynon-increasing in terms of all convex transport costs. The initialization can be taken to bethe independent coupling ${(Z_{0}^{0},Z_{1}^{0})} \sim {\pi_{0} \times \pi_{1}}$,or any other couplings that can be constructed from marginal (unpaired) observations of $\pi_{0}$ and $\pi_{1}$.In practice,each step of $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ is empirically approximated by first drawing samples of $(Z_{0}^{k},Z_{1}^{k})$ from the ODE with drift $v^{k}$, and then constructing the next flow $v^{k + 1}$ from the optimization in. Although this process accumulates errors,it was shown that one or two iterations are sufficient for practical applications.Note that the $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ procedure is "cost-agnostic"in that it does not dependent on any specific cost $c$.Although the recursive$\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ update is monotonically non-increasing on the transport cost for all convex $c$, it does not necessarily converge to the optimal coupling for any pre-specified $c$,as the update would stop whenever two cost functions are conflicting with each other.In,a coupling $(X_{0},X_{1})$ is called *straight* if it is a fixed point of $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$, that is, ${(X_{0},X_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$.It was shown that rectifiable couplings that are optimal w.r.t. a convex $c$ must be straight, but the opposite is not true in general.One exception is the one dimension case ($d = 1$), for which all convex functions $c$ (whose $c$-optimal coupling exists) share a common optimal coupling that is also straight.But this does not hold when $d \geq 2$.

### $c$-Rectified flow

In this work,we modify the $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ procedure so that it can be used tosolve given a user-specified cost function $c$.We show that this can be done easily by properly restricting the optimization domain of $v$ and modifying the loss functionin.The case of quadratic loss ${c{(x)}} = {\frac{1}{2}\left. \parallel x\parallel \right.^{2}}$is particularly simple,for which we simplyneed to restrict the $v$to be a gradient field $v_{t} = {\nabla f_{t}}$ in the optimization of.For more general convex $c$,we need to restrict $v$ to have a form of ${v_{t}{(x)}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(x)}})}}$, with $f$ minimizing the following loss function:

where $c^{\ast}$ denotes the conjugate function of $c$.Obviously when ${c{(x)}} = {\frac{1}{2}\left. \parallel x\parallel \right.^{2}}$, reduces to with $v = {\nabla f}$.The loss function in is closely related to *Bregman divergence* \e.g., and the so-called *matching loss* \e.g.,.We call ${\mathbf{Z}} = {\{ Z_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$ that follows ${dZ_{t}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(Z_{t})}})}dt}$ with $Z_{0} = X_{0}$ and $f$ solving the $c$-rectified flow of $(X_{0},X_{1})$, and the corresponding $(Z_{0},Z_{1})$ the $c$-rectified coupling of $(X_{0},X_{1})$, denoted as ${(Z_{0},Z_{1})} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$.Similar to the original rectified coupling,the $c$-rectified coupling $(Z_{0},Z_{1})$ also share the same marginal laws as $(X_{0},X_{1})$ and hence is a coupling of $\pi_{0}$ and $\pi_{1}$.In addition, $(Z_{0},Z_{1})$ yields no larger transport cost than $(X_{0},X_{1})$ w.r.t. $c$,that is, ${{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} \leq {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}$. But this only holds for the specific $c$ that is used to define the flow, rather than all convex functions like $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$.More importantly,recursively performing $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$allows us to find $c$-optimal couplings that solve the OT problem.Under mild conditions, we have

where $\ell_{X,c}^{\ast}$ denotes the minimum value of the loss function in,which provides a criterion of $c$-optimality of a given coupling without solving the OT problem. Moreover,when following the recursive update ${(Z_{0}^{k + 1},Z_{1}^{k + 1})} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(Z_{0}^{k},Z_{1}^{k})})}}$,the $\ell_{Z^{k},c}^{\ast}$ is guaranteed to decay to zero with ${\min_{k \leq K}\ell_{Z^{k},c}^{\ast}} = {O\left( {1/K} \right)}$.

### Notation

Let $C^{1}{({\mathbb{R}}^{d})}$ be the set of continuously differentiable functions $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, and $C_{c}^{1}{({\mathbb{R}}^{d})}$ the functions in $C^{1}{({\mathbb{R}}^{d})}$ whose support is compact.For a time-dependent velocity field $v:{{{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}}\rightarrow{\mathbb{R}}}$,we write ${v_{t}{( \cdot )}} = {v{(x,t)}}$ anduse ${{\overset{˙}{v}}_{t}{(x)}} ≔ {\partial{v{(x,t)}}}$ and ${{\nabla v_{t}}{(x)}} ≔ {\partial_{x}{v{(x,t)}}}$ to denote the partial derivative w.r.t. time $t$ and variable $x$, respectively.We denote by $C^{2,1}{({{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}})}$the set of functions $f:{{{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}}\rightarrow{\mathbb{R}}}$ that are second-order continuously differentiable w.r.t. $x$ and first-order continuously differentiable w.r.t. $t$.In this work,an ordinary differential equation(ODE) ${dz_{t}} = {v_{t}{(z_{t})}dt}$ should be interpolated as an integral equation $z_{t} = {z_{0} + {\int_{0}^{t}{v_{t}{(z_{t})}{dt}}}}$.For $x \in {\mathbb{R}}^{d}$, $\left. \parallel x\parallel \right.$ denotes the Euclidean norm. We always write $c^{\ast}$ as the convex conjugate of $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, that is, ${c^{\ast}{(x)}} = {\sup_{y \in {\mathbb{R}}^{d}}{\{{{x^{\top}y} - {c{(y)}}}\}}}$.Random variables are capitalized (e.g., $X,Y,Z$) to distinguish them with deterministic values (e.g, $x,y,z$).Recall that an ${\mathbb{R}}^{d}$-valued random variable$X = {X{(\omega)}}$ is a measurable function $X:{\Omega\rightarrow{\mathbb{R}}^{d}}$, where $\Omega$ is an underlying sample space equipped with a $\sigma$-algebra $\mathcal{F}$ and a probability measure $\mathbb{P}$.The triplet $(\Omega,\mathcal{F},{\mathbb{P}})$ form the underlying probability space, which is omitted in writing in the most places.We use ${Law}{(X)}$ to denote the probability law of $X$, which is the probability measure $\mathbb{L}$ that satisfies ${{\mathbb{L}}{(B)}} = {{\mathbb{P}}{({\{\omega:{{X{(\omega)}} \in B}\}})}}$ for all measurable sets on ${\mathbb{R}}^{d}$.For a functional $F{(X)}$ of a random variable $X$,the optimization problem ${\min_{X}F}{(X)}$ technically means tofind a measurable function $X{(\omega)}$ to minimize $F$, even though we omit the underlying sample space $\Omega$. When $F{(X)}$ depends on $X$ only through ${Law}{(X)}$, the optimization problem is equivalent to finding the optimal ${Law}{(X)}$.

### Outline

The rest of the work is organized as follows. Section 2introduces the background of optimal transport. Section 3reviews rectified flow of from an optimization-based view.Section 4 characterizesthe if and only if conditionfor two differentiable stochastic processes to have equal marginal laws.Section 5 introduces the main $c$-rectified flow method and establishes its theoretical properties.

## Background of Optimal Transport

This section introduces the background of optimal transport (OT),including both the static and dynamic formulations.Of special importance is the dynamic formulation,which is closely related to the rectified flow approach.The readers can find systematic introductions to OT ina collection of excellent textbooks.

### Static formulations

The optimal transport problem wasfirst formulated byGaspard Monge in 1781 when he studiedthe problem of how toredistribute mass, e.g., a pile of soil, with minimal effort.Monge's problem can be formulated as

where we minimize the $c$-transport costin the set of deterministic couplings $(X_{0},X_{1})$ that satisfy $X_{1} = {T{(X_{0})}}$ for a transport mapping $T:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$.The Monge--Kantorovich (MK) problem in is the relaxationof to the set of all (deterministic and stochastic) couplings of $\pi_{0}$ and $\pi_{1}$.The two problems are equivalent when the optimum of is achieved by adeterministic coupling, which is guaranteed if $\pi_{0}$ is an absolutely continuous measure on ${\mathbb{R}}^{d}$.A key feature of the MK problem is that it isa linear programming w.r.t. the law of the coupling $(X_{0},X_{1})$, and yields a dual problem of form:

where we write ${\pi_{1}{(\mu)}} ≔ {\int{\mu{(x)}{d\pi_{1}}{(x)}}}$, and $\mu,\nu$ are optimized in all functions from ${\mathbb{R}}^{d}$ to $\mathbb{R}$.For any coupling $(X_{0},X_{1})$ of $\pi_{0}$ and $\pi_{1}$, and $(\mu,\nu)$ satisfying the constraint in, it is easy to see that

As the left side of only depends on $(X_{0},X_{1})$ and the right side only on $(\mu,\nu)$, one can show that $(X_{0},X_{1})$ is $c$-optimal and $(\mu,\nu)$ solves iff${{\mu{(X_{0})}} + {\nu{(X_{1})}}} = {c{({X_{1} - X_{0}})}}$holds with probability one, which provides a basic optimality criterion. Many existingOT algorithms are developed by exploiting the primal dual relation of and(see e.g., ), but have the drawback of yielding minimax problems that are challenging to solve in practice. If $c$ is strictly convex,the optimal transport map of is unique (almost surely) and yields a form of

where $c^{\ast}$ is the convex conjugate function of $c$, and $\nu$ is an optimal solution of, which is $c$-convex in that ${\nu{(x)}} = {\sup_{y}\left\{ {{- {c{({y - x})}}} + {\mu{(y)}}} \right\}}$ with $\mu$ the associated solution.In the canonical case of quadratic cost ${c{(x)}} = {\frac{1}{2}\left. \parallel x\parallel \right.^{2}}$, we can write ${T{(x)}} = {{\nabla\phi}{(x)}}$, where ${\phi{(x)}} ≔ {{\frac{1}{2}\left. \parallel x\parallel \right.^{2}} + {\nu{(x)}}}$ is a convex function.

### Dynamic formulations

Both the MK and Monge problems can be equivalently framed in dynamic waysas finding continuous-time processes that transfer $\pi_{0}$ to $\pi_{1}$.Let $\{ x_{t}:{t \in {\lbrack 0,1\rbrack}}\}$ be a smooth path connecting $x_{0}$ and $x_{1}$, whose time derivative is denoted as ${\overset{˙}{x}}_{t}$.For convex $c$, by Jensen's inequality, we can represent the cost $c{({x_{1} - x_{0}})}$ in an integral form:

where the infimum is attained when $x_{t}$ is the linear interpolation (geodesic) path: $x_{t} = {{tx_{1}} + {{({1 - t})}x_{0}}}$.Hence, the MK optimal transport problem is equivalent to

where we optimize in the set of time-differentiable stochastic processes${\mathbf{X}} = {\{ X_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$.The optimum of is attained by $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$ when$(X_{0},X_{1})$ is a $c$-optimal coupling of, which is known as the *displacement interpolation*.We call the objective function in the path-wise $c$-transport cost.The Monge problem can also be framed in a dynamic way.Assume the transport map $T$ can be induced by an ODE model${dX_{t}} = {v_{t}{(X_{t})}dt}$ such that $X_{1} = {T{(X_{0})}}$. Then the Monge problem is equivalent to

which is equivalent to restricting $\mathbf{X}$ in to the set of processes that can be induced by ODEs.Assume that $X_{t}$ following ${dX_{t}} = {v_{t}{(X_{t})}dt}$ yields a density function $\varrho_{t}$. Thenit is well known that $\varrho_{t}$ satisfies the continuity equation:

Hence, we can rewrite into an optimization problem on $(v,\varrho)$, yielding the celebrated *Benamou-Brenier formula*:

where ${{d\pi_{i}}/d}x$ denotes the density function of $\pi_{i}$.The key idea of and is torestrict the optimization of to the set of deterministic processed induced by ODEs, which significantly reduces the search space.Intuitively,Jensen's inequality ${{\mathbb{E}}{\lbrack{c{(Z)}}\rbrack}} \geq {c{({{\mathbb{E}}{\lbrack Z\rbrack}})}}$ shows that we should be able to reduce the expected cost of a stochastic processby "marginalizing" out the randomness.In fact,we will show that, for a differentiable stochastic process $\mathbf{X}$, its ($c$-)rectified flow yields no largerpath-wise $c$-transport cost in than $\mathbf{X}$ (see Lemma 3.3 and Theorem 5.3 ‣ 5.1 𝑐-Rectified Flow of Time-Differentiable Processes 𝑿 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")).However, all the dynamic formulations above are still highly challenging to solve in practice.We will show that $c$-rectified flow can be viewed as a special coordinate descent like approachto solving (Section 5.4).

## Rectified Flow: An Optimization-Based View

We introduce rectified flow of from an optimization-based perspective:we show that rectified flow can be viewed as the solutionof a special constrained dynamic optimization problem,which allows us to gain more understanding of rectified flow and motivates the development of $c$-rectified flow.Following,for a time-differentiable stochastic process ${\mathbf{X}} = {\{ X_{t}:{t \in {\lbrack 0,1\rbrack}}\}}$, its expected velocity field $v^{\mathbf{X}}$ is defined as

where ${\overset{˙}{X}}_{t}$ denotes the time derivative of $X_{t}$.Obviously, $v^{\mathbf{X}}$ is the solution of

where the optimization is on the set of all measurable velocity fields $v:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$.The importance of $v^{\mathbf{X}}$ lies on the fact that it characterizes the time-evolution of the marginal laws $\rho_{t} ≔ {{Law}{(X_{t})}}$ of $\mathbf{X}$, through the continuity equation in the distributional sense:

Precisely, Equation should be interpreted by its weak and integral form:

where ${\rho_{t}{(h)}} ≔ {\int{h{(x)}{d\rho_{t}}{(x)}}}$ and $C_{c}^{1}{({\mathbb{R}}^{d})}$ denotes the set of continuously differentiable functions on ${\mathbb{R}}^{d}$ with compact support.Hence,if the solution of Eq - is unique, thenthe marginal laws ${\{{{Law}{(X_{t})}}\}}_{t}$ of $\mathbf{X}$ are uniquely determined by $v^{\mathbf{X}}$ and the initial ${Law}{(X_{0})}$.We define the rectified flow of $\mathbf{X}$,denoted by ${\mathbf{Z}} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{({\mathbf{X}})}}$,as the ODE driven by $v^{\mathbf{X}}$:

Moreover, the rectified flow of a coupling $(X_{0},X_{1})$is defined as the rectified flow of $\mathbf{X}$ when $\mathbf{X}$ is the linear interpolation of $(X_{0},X_{1})$.

### Definition 3.1

A stochastic process $\mathbf{X}$ is called rectifiable if $v^{\mathbf{X}}$ exists and is locally bounded,and Equation has an unique solution.A coupling $(X_{0},X_{1})$ is called rectifiable if its linear interpolation process $\mathbf{X}$, following $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$, is rectifiable.In this case, we call $\mathbf{Z} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{(\mathbf{X})}}$ the rectified flow of $(X_{0},X_{1})$, and write it (with an abuse of notation) as $\mathbf{Z} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{({(X_{0},X_{1})})}}$.The corresponding$(Z_{0},Z_{1})$ is called the rectified coupling of $(X_{0},X_{1})$, denoted as ${(Z_{0},Z_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$.

By the definition in,we have $v^{\mathbf{Z}} = v^{\mathbf{X}}$,and hence the marginal laws ${Law}{(Z_{t})}$ of $\mathbf{Z}$ are governed by the same continuity equation -, which is a well known fact. As shown in, Equation has an unique solution iff Equation has an unique solution,which implies that $\mathbf{Z}$ and $\mathbf{X}$ share the same marginal laws.We also assumed that the solution of is unique;if not, results in the paper hold for all solutions of.

### Theorem 3.2 (Theorem 3.3 of \[15\])

Assume that $\mathbf{X}$ is rectifiable. We have

Hence,rectified flowturns a rectifiable stochastic process into a flow while preserving the marginal laws.

### A optimization view of rectified flow

We show thatthe rectified flow $\mathbf{Z}$ of $\mathbf{X}$achieves the minimum of the path-wise $c$-transport cost in the set of time-differentiable stochastic processes whose expected velocity field equals $v^{\mathbf{X}}$.This explains that the property of non-increasing convex transport costs of rectified flow/coupling.

### Lemma 3.3

The rectified flow $\mathbf{Z} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{(\mathbf{X}_{t})}}$ in attains the minimum of

which holds for *any* convex functions $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$.

### Proof

For any stochastic process $\mathbf{Y}$ with ${v_{t}^{\mathbf{X}}{(z)}} = {v_{t}^{\mathbf{Y}}{(z)}} = {{\mathbb{E}}{\lbrack{\left. {\overset{˙}{Y}}_{t} \middle| Y_{t} \right. = z}\rbrack}}$, we have

Lemma 3.3 suggests that the rectified flow decreases the path-wise $c$-transport cost: ${F_{c}{({\mathbf{Z}})}} \leq {F_{c}{({\mathbf{X}})}}$, for all convex $c$.Note that ${{\mathbb{E}}\left\lbrack {c{({Z_{1} - Z_{0}})}} \right\rbrack} \leq {F_{c}{({\mathbf{Z}})}}$ by Jensen's inequality,and ${{\mathbb{E}}\left\lbrack {c{({X_{1} - X_{0}})}} \right\rbrack} = {F_{c}{({\mathbf{X}})}}$if $\mathbf{X}$ is the linear interpolation of $(X_{0},X_{1})$. Hence, in this case, we have

which yields a proof of Theorem 3.2 of that the rectified coupling $(Z_{0},Z_{1})$ yields no larger convex transport costs than $(X_{0},X_{1})$.

### A primal-dual relation

Let us generalize the least squares loss $L_{\mathbf{X}}{(v)}$ in to aa Bregman divergence based loss:

where $\mathsf{b}_{c}{( \cdot; \cdot )}$ is the Bregman divergence w.r.t. $c$. The least squares loss $L_{\mathbf{X}}$ is recovered with ${c{(x)}} = {\frac{1}{2}\left. \parallel x\parallel \right.^{2}}$.Rectified flow can be alternatively implemented by minimizing ${\overset{\sim}{L}}_{{\mathbf{X}},c}$ with a differentiable strictly convex $c$,as in this case the minimum of ${\overset{\sim}{L}}_{{\mathbf{X}},c}$ is also attended by ${v^{\mathbf{X}}{(z)}} = {{\mathbb{E}}{\lbrack{\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right. = z}\rbrack}}$.The $c$-rectified flowis obtained if we minimize ${\overset{\sim}{L}}_{{\mathbf{X}},c}$ with $v$ restricted to be a form of $v = {{\nabla c^{\ast}} \circ {\nabla f_{t}}}$.See more in Section 5.In the following, we show thatthe optimization in can be viewed as the dual problem.

### Theorem 3.4

For any differentiable convex function $c$,and rectifiable process $\mathbf{X}$, we have

andthe optima above are achieved when $v = v^{\mathbf{X}}$ and $\mathbf{Y} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{(\mathbf{X})}}$.

### Proof

Let${{var}_{c}{(\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right.)}} ≔ {{\mathbb{E}}{\lbrack{{c{({\overset{˙}{X}}_{t})}} - \left. {c{({{\mathbb{E}}{\lbrack\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right.\rbrack}})}} \middle| X_{t} \right.}\rbrack}}$.For any $v$, we have

The inequality is tight when $v = v^{\mathbf{X}}$, which attains the minimum of ${\overset{\sim}{L}}_{{\mathbf{X}},c}$.Write ${R_{{\mathbf{X}},c}{({\mathbf{Y}})}} = {{F_{c}{({\mathbf{X}})}} - {F_{c}{({\mathbf{Y}})}}}$.We know that ${\mathbf{Z}} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({\mathbf{X}})}}$ attains the maximum of $R_{{\mathbf{X}},c}{({\mathbf{Y}})}$ subject to $v^{\mathbf{Y}} = v^{\mathbf{X}}$ by Lemma 3.3. In addition,

This concludes the proof. ∎

### Straight couplings

The ${\overset{\sim}{\ell}}_{{\mathbf{X}},c}^{\ast} = {\int_{0}^{1}{{var}_{c}{(\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right.)}{dt}}}$ aboveprovides a measure of how much the different paths of $\mathbf{X}$ intersect with each other.If $c$ is strictly convex and${\overset{\sim}{\ell}}_{{\mathbf{X}},c}^{\ast} = 0$, we have ${\overset{˙}{X}}_{t} = {{\mathbb{E}}{\lbrack\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right.\rbrack}}$ almost surely,meaning that there exist no two paths that go across a point along two different directions.In this case, $\mathbf{X}$ is afixed point of ${\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{( \cdot )}$, that is, ${\mathbf{X}} = {\mathbf{Z}} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({\mathbf{X}})}}$,because we have${dX_{t}} = {{\overset{˙}{X}}_{t}dt} = {{\mathbb{E}}{\lbrack\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right.\rbrack}dt} = {v^{\mathbf{X}}{(X_{t})}dt}$, which is the same Equation that defines $\mathbf{Z}$.Similarly, if $\mathbf{X}$ is the linear interpolation of the coupling $(X_{0},X_{1})$, then${\overset{\sim}{\ell}}_{{\mathbf{X}},c}^{\ast} = 0$ with strictly convex $c$ if and only if $(X_{0},X_{1})$ is a fixed point of the $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ mapping, that is, ${(X_{0},X_{1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$,following.Such couplings are called *straight*, or *fully rectified* in. Obtaining straight couplingsis useful for learning fast ODE modelsbecause the trajectories of the associated rectified flow $\mathbf{Z}$ are straight lines and hence can be calculated in closed form without iterative numerical solvers. See for more discussion. Moreover, showed thatrectifiable $c$-optimal couplings must be straight.In the one dimensional case ($d = 1$),the straight coupling, if it exists, is unique and attains the minimum of ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$ for all convex functions for which $c$-optimal coupling exists. For higher dimensions ($d \geq 2$), however,straight couplings are not unique, and the specific straight couplingobtained at the convergence of the recursive $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ update (i.e. ${(Z_{0}^{k + 1},Z_{1}^{k + 1})} = {{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(Z_{0}^{k},Z_{1}^{k})})}}$) is implicitly determined by the initial coupling $(Z_{0}^{0},Z_{1}^{0})$,and is not expected to be optimal w.r.t. any pre-fixed $c$.The following counter example shows a somewhat stronger negative result:there exist straight couplingsthat are not optimal w.r.t. all second order differentiable convex functions with invertible Hessian matrices.

### Example 3.5

Take $\pi_{0} = \pi_{1} = {\mathcal{N}{(0,I)}}$.Hence, for ${c{(x)}} = \left. \parallel x\parallel \right.^{p}$ with $p > 0$,the $c$-optimal mapping is the trivial identity coupling $(X_{0},X_{0})$ with $X_{0} \sim \pi_{0}$.However,consider the coupling $(X_{0},{AX_{0}})$,where $A$ is anon-identity and non-reflecting rotation matrix (namely ${A^{\top}A} = I$, ${\det{(A)}} = 1$, $A \neq I$ and $A$ does not have $\lambda = {- 1}$ as an eigenvalue).Then $(X_{0},{AX_{0}})$ is a straight coupling of $\pi_{0}$ and $\pi_{1}$,but it is not $c$-optimal for allsecond order differentiable convex function $c$ whose Hessian matrix is invertible everywhere. See Appendix for the proof.It is the rotation transformthat makes $(X_{0},{AX_{0}})$ sub-optimal,which is removed in the proposed $c$-rectified flow in Section 5 via a Helmholtz like decomposition.

## Differentiable Processes with Equivalent Marginal Laws

The marginal preserving property of rectified flow is due to the property of $v^{\mathbf{Z}} = v^{\mathbf{X}}$ by construction.However, we show in this section that$v^{\mathbf{X}} = v^{\mathbf{Z}}$ is only a sufficient condition:two differentiable processes $\mathbf{X}$ and $\mathbf{Z}$can have the same marginal lawseven if $r ≔ {v^{\mathbf{X}} - v^{\mathbf{Z}}} \neq 0$.This is because $r$, as illustrated in Example 3.5,can be a rotation-only vector field (in a generalized sense shown below)that introduces rotation components into the dynamics without modifying the marginal distributions.Therefore, the constraint of $v^{\mathbf{Y}} = v^{\mathbf{X}}$ inthe optimization problem may be too restrictive.A natural relaxation of would be

which yields a dynamic OT problem with a continuum ofmarginal constraints.In Section 5, we show thatthe solution of yields our $c$-rectified flow thatsolve the OT problemat the fixed point.Solving allows us to remove the rotational components of $v^{\mathbf{X}}$, which is whatwhat renders rectified flow non-optimal.In this section,we first characterize the necessary and sufficient conditionfor having equivalent marginal laws.

### Definition 4.1

A time-dependent vector field $r:{{{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}}\rightarrow{\mathbb{R}}^{d}}$ is said to be $\mathbf{X}$-marginal-preserving if

Equation is equivalent to sayingthat ${{\mathbb{E}}{\lbrack{{\nabla h}{(X_{t})}^{\top}r_{t}{(X_{t})}}\rbrack}} = 0$ holds almost surely assuming that $t$ is a random variable following $\text{Uniform}{({\lbrack 0,1\rbrack})}$ (i.e., $t$-almost surely).Let $\rho_{t} = {{Law}{(X_{t})}}$ and it yields a density function $\varrho_{t}$. Using integration by parts, we have

which gives ${\nabla \cdot {({r_{t}\varrho_{t}})}} = 0$. This says that $r_{t}\varrho_{t}$ is a rotation-only (or divergence-free) vector field in the classical sense.

### Lemma 4.2

Let $\mathbf{X}$ and $\mathbf{Y}$be two stochastic processes withthe same initial distributions ${{Law}{(X_{0})}} = {{Law}{(Y_{0})}}$.Assume that $\mathbf{X}$ is rectifiable, and ${v_{t}^{\mathbf{Y}}{(z)}}:={{\mathbb{E}}{\lbrack{\left. {\overset{˙}{Y}}_{t} \middle| Y_{t} \right. = z}\rbrack}}$ exists and is locally bounded. Then $\mathbf{X}$ and $\mathbf{Y}$ share the same marginal laws at all time, that is, ${{Law}{(X_{t})}} = {{Law}{(Y_{t})}}$, ${{\forall t} \in {\lbrack 0,1\rbrack}},$if and only if $v^{\mathbf{X}} - v^{\mathbf{Y}}$ is $\mathbf{Y}$-marginal-preserving.

### Proof

Taking any $h$ in $C_{c}^{1}{({\mathbb{R}}^{d})}$, we have for $t \in {\lbrack 0,1\rbrack}$

This suggests that the marginal law $\rho_{t} ≔ {{Law}{(X_{t})}}$ satisfies

where we define${\rho_{t}{(h)}} = {\int{h{(x)}{d\rho_{t}}{(x)}}}$.Equation is formally written as the continuity equation:

Similarly, ${\overset{\sim}{\rho}}_{t} ≔ {{Law}{(Y_{t})}}$ satisfies

If $v_{t}^{\mathbf{X}} - v_{t}^{\mathbf{Y}}$ is ${Law}{(Y_{t})}$-preserving for ${\forall t} \in {\lbrack 0,1\rbrack}$, we have

which suggests that ${\overset{\sim}{\rho}}_{t} ≔ {{Law}{(Y_{t})}}$solves the same continuity equation, starting from the same initialization as ${{Law}{(X_{0})}} = {{Law}{(Y_{0})}}$.Hence, we have $\rho_{t} = {\overset{\sim}{\rho}}_{t}$ if the solution of is unique,which is equivalent to the uniqueness of the solution of ${dZ_{t}} = {v_{t}^{\mathbf{X}}{(Z_{t})}}$ in following Corollary 1.3 of.On the other hand, if $\rho_{t} = {{Law}{(X_{t})}} = {{Law}{(Y_{t})}} = {\overset{\sim}{\rho}}_{t}$,following and, we have for any $h \in {C_{c}^{1}{({\mathbb{R}}^{d})}}$,

which is the definition of$\mathbf{Y}$-marginal-preserving following.∎

## $c$-Rectified Flow

We introduce $c$-rectified flow,a $c$-dependent variant of rectified flow that guarantees tominimize the $c$-transport costwhen applied recursively. This section is organized as follows:Section 5.1defines and discusses the $c$-rectified flow of a differentiable stochastic process $\mathbf{X}$, which we show yields the solution of theinfinite-marginal OT problem.Section 5.2 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")considers the $c$-rectified flow of a coupling $(X_{0},X_{1})$, which we show is non-increasing on the $c$-transport cost.Section 5.3proves that the fixed points of $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$ are $c$-optimal.Section 5.4interprets $c$-rectified flowas an alternating direction descent methodfor the dynamic OT problem,and a majorize-minimization (MM) algorithm for the static OT problem.Section 5.5 discussesa key lemma relating $c$-optimal couplings and its associated displacement interpolation with Hamilton-Jacobi equation.

### $c$-Rectified Flow of Time-Differentiable Processes $\mathbf{X}$

For a convex cost function $c:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ anda time-differentiable process $\mathbf{X}$,the $c$-rectified flow of $\mathbf{X}$,denoted as ${\mathbf{Z}} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{({\mathbf{X}})}}$, is defined as the solution of

where ${c^{\ast}{(x)}} ≔ {\sup_{y}{\{{{x^{\top}y} - {c{(y)}}}\}}}$ is the convex conjugate of $c$, and$f^{{\mathbf{X}},c}:{{{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}}\rightarrow{\mathbb{R}}}$ is the optimal solution of

where $\mathsf{m}_{c}:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{d}}\rightarrow{\lbrack 0,{+ \infty})}}$ is a loss function defined as

Note that we have ${\mathsf{m}_{c}(x;y)} \geq 0$ for ${\forall x},y$ following the definition of the conjugate $c^{\ast}$ (or the Fenchel-Young inequality).Losses of form $\mathsf{m}_{c}(x;y)$is equivalent to the so called *matching loss*proposed forlearning generalized linear models. Compared with the original rectified flow,the difference of $c$-rectified flow is i) restricting the velocity field to a form of $g_{t} = {{\nabla c^{\ast}} \circ {\nabla f_{t}}}$, and ii) replacing the quadratic objective function to the matching loss.These two changes combined yield a Helmholtz like decomposition of $v^{\mathbf{X}}$ as we show below, allowing us to remove the "rotation-only" component of $v^{\mathbf{X}}$ and obtain $c$-optimal couplings at fixed points.

### Bregman divergence, Helmholtz decomposition, marginal preserving

We can equivalently write using Bergman divergence associated with $c$, that is,

Then it is easy to see that ${\mathsf{m}_{c}(x;y)} = {\mathsf{b}_{c}\left( x;{{\nabla c^{\ast}}{(y)}} \right)}$, by using the fact that ${{\nabla c}{({{\nabla c^{\ast}}{(y)}})}} = y$ and ${c^{\ast}{(y)}} = {{y^{\top}{\nabla c^{\ast}}{(y)}} - {c{({{\nabla c^{\ast}}{(y)}})}}}$.Hence, $\mathsf{m}_{c}$ and $\mathsf{b}_{c}$ are equivalent up to the monotonic transform $\nabla c^{\ast}$ on $y$.The minimum ${\mathsf{b}_{c}(x;y)} = 0$ is achieved when $y = x$,while ${\mathsf{m}_{c}(x;y)} = 0$ is achieved when ${{\nabla c^{\ast}}{(y)}} = x$.Therefore, is equivalent to

Moreover,the generalized Pythagorean theorem of Bregman divergence (e.g., ) gives

Because ${v^{\mathbf{X}}{(X_{t})}} = {{\mathbb{E}}\left\lbrack {\overset{˙}{X}}_{t} \middle| X_{t} \right\rbrack}$ and the last term of is independent with $g_{t}$,we can further reframeinto

which can be viewed as projecting the expected velocity $v_{t}^{\mathbf{X}}$ to the set of functions of form $g_{t} = {{\nabla c^{\ast}} \circ {\nabla f_{t}}}$,w.r.t. the Bregman divergence.This yields an orthogonal decomposition of $v_{t}^{\mathbf{X}}$:

where $r_{t}^{{\mathbf{X}},c} = {v_{t}^{{\mathbf{X}},c} - {{\nabla c^{\ast}} \circ {\nabla f_{t}^{{\mathbf{X}},c}}}}$ is the residual term.The key result below shows that $r^{{\mathbf{X}},c}$ is $\mathbf{X}$-marginal-preserving, which ensures thatthe $c$-rectified flow preserves the marginals of $\mathbf{X}$.

### Definition 5.1

We say that $\mathbf{X}$ is $c$-rectifiable if $v^{\mathbf{X}}$ exists,the minimum of exists and is attained by a locally bounded function $f^{\mathbf{X},c}$,and the solution of Equation exists and is unique.

### Theorem 5.2

Assume that $\mathbf{X}$ is $c$-rectifiable,and $c^{\ast} ≔ {\sup_{y}{\{{{x^{\top}y} - {c{(y)}}}\}}}$ and $c^{\ast} \in {C^{1}{({\mathbb{R}}^{d})}}$. We havei) $v^{\mathbf{X}} - g^{\mathbf{X},c}$ is $\mathbf{X}$-marginal-preserving.ii) $\mathbf{Z} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{(\mathbf{X})}}$ preserves the marginal laws of $\mathbf{X}$, that is,${{Law}{(Z_{t})}} = {{Law}{(X_{t})}}$, ${\forall t} \in {\lbrack 0,1\rbrack}$.

### Proof

i)By ${v_{t}^{\mathbf{X}}{(z)}} = {{\mathbb{E}}{\lbrack{\left. {\overset{˙}{X}}_{t} \middle| X_{t} \right. = z}\rbrack}}$, the loss function in is equivalent to

By Euler-Lagrange equation, we have

Taking $g_{s} = h$ if $s < t$ and $g_{s} = 0$ if $s > t$ yields that ${r^{{\mathbf{X}},c}{(x)}} = {{{\nabla c^{\ast}}{({{\nabla f_{s}^{{\mathbf{X}},c}}{(X_{s})}})}} - {v^{\mathbf{X}}{(X_{s})}}}$ is $\mathbf{X}$-marginal-preserving following.ii) Note that $\mathbf{Z}$ is rectifiable if $\mathbf{X}$ is $c$-rectifiable. Applying Lemma 4.2yields the result. ∎

For the quadratic cost ${c{(x)}} = {c^{\ast}{(x)}} = {\frac{1}{2}\left. \parallel x\parallel \right.^{2}}$, the $\nabla c^{\ast}$ is the identity mapping, and reduces to the Helmholtz decomposition,which represents a velocity field into the sum of a gradient field and a divergence-free field. Hence, yields a generalization of Helmholtz decomposition, in which a monotonic transform $\nabla c^{\ast}$ is applied on the gradient field component.We call a*Bregman Helmholtz decomposition*.

### Remark: score matching

In some special cases, $v^{\mathbf{X}}$ may already be a gradient field,and hence the rectified flow and $c$-rectified flow coincide for ${c{(x)}} = {\frac{1}{2}\left. \parallel x\parallel \right.^{2}}$. One example of this is when $X_{t} = {{\alpha_{t}X_{1}} + {\beta_{t}\xi}}$for some time-differentiable functions $\alpha_{t}$ and $\beta_{t}$, and $\xi \sim {\mathcal{N}{(0,I)}}$, satisfying ${\alpha_{1} = 1},{\beta_{1} = 0}$, and $X_{0} = {{\alpha_{0}X_{1}} + {\beta_{0}\xi}}$. In this case, one can show that

where $\varrho_{t}$ is the density function of $X_{t}$ with${\varrho_{t}{(z)}} \propto {\int{\phi\left( \frac{z - {\alpha_{t}x_{1}}}{\beta_{t}} \right){d\pi_{1}}{(x_{1})}}}$ and ${\phi{(z)}} = {\exp{({- {\left. \parallel z\parallel \right.^{2}/2}})}}$, and$\eta_{t} = {\beta_{t}^{2}{({{{\overset{˙}{\alpha}}_{t}/\alpha_{t}} - {{\overset{˙}{\beta}}_{t}/\beta_{t}}})}}$ and $\zeta_{t} = {{\overset{˙}{\alpha}}_{t}/\alpha_{t}}$.This case covers the probability flow ODEs and denoising diffusion implicit models (DDIM) with different choices of $\alpha_{t}$ and $\beta_{t}$ as suggested in.When $\zeta_{t} = 0$,as the case of,$v_{t}^{\mathbf{X}}$ is proportional to ${{\nabla\log}\rho_{t}},$ the *score function* of $\varrho_{t}$,and the least squares loss $L_{\mathbf{X}}{(v)}$ in reduces to a time-integrated*score matching* loss.However,$v_{t}^{\mathbf{X}}$ is generally not a score function or gradient function, especially in complicate cases when the coupling $(X_{0},X_{1})$ is induced from the previous rectified flow aswe iteratively apply the rectification procedure.In these cases, it is necessary to impose the gradient form as we do in $c$-rectified flow.

### $c$-Rectified flow solves Problem (17)

We are ready to show that the $c$-rectified flow solves the optimization problem in.Further, forms a dual problem of.

### Theorem 5.3

Under the conditions in Theorem 5.2, we havei) $\mathbf{Z} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{(\mathbf{X})}}$ attains the minimum of.ii) Problem and has a strong duality:

As the optima above are achieved by $f^{\mathbf{X},c}$ and $\mathbf{Z}$, we have${{L_{\mathbf{X},c}{(f^{\mathbf{X},c})}} = {{F_{c}{(\mathbf{X})}} - {F_{c}{(\mathbf{Z})}}}}.$

### Proof

Write ${R_{{\mathbf{X}},c}{({\mathbf{Y}})}} = {{F_{c}{({\mathbf{X}})}} - {F_{c}{({\mathbf{Y}})}}}$.First, we show that ${L_{{\mathbf{X}},c}{(f)}} \geq {R_{{\mathbf{X}},c}{({\mathbf{Y}})}}$ forany $f$ and $\mathbf{Y}$ that satisfies ${{Law}{(Y_{t})}} = {{Law}{(X_{t})}}$, $\forall t$:

Moreover, if we take${\mathbf{Y}} = {\mathbf{Z}}$ and $f = f^{{\mathbf{X}},c}$,then the inequality in $\overset{}{\leq}$ is tight because ${\overset{˙}{Z}}_{t} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(Y_{t})}})}}$ holds $t$-almost surely.Therefore, ${R_{{\mathbf{X}},c}{({\mathbf{Z}})}} = {L_{{\mathbf{X}},c}{(f^{{\mathbf{X}},c})}} \geq {R^{{\mathbf{X}},c}{(Y)}}$, which suggests that $\mathbf{Z}$ attains the maximum of $R_{{\mathbf{X}},c}$ (under the marginal constraints) and the strong duality holds.∎

### $c$-Rectified Flow of Coupling $(X_{0},X_{1})$

Similar to the case of rectified flow,the $c$-rectified flow/coupling of a coupling $(X_{0},X_{1})$is defined as the $c$-rectified flow/coupling of its linear interpolation process.In the following, we show that the $c$-rectified coupling of a coupling yields no larger$c$-transport cost.

### Definition 5.4

Let $\mathbf{X}$ be the linear interpolation ofcoupling $(X_{0},X_{1})$ in that ${X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}},{{\forall t} \in {\lbrack 0,1\rbrack}}$. We say that $(X_{0},X_{1})$ is $c$-rectifiable if $\mathbf{X}$ is $c$-rectifiable, and call $\mathbf{Z} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{(\mathbf{X})}}$ the $c$-rectified flow of $(X_{0},X_{1})$.We call the induced $(Z_{0},Z_{1})$ the $c$-rectified coupling of $(X_{0},X_{1})$, denoted as ${(Z_{0},Z_{1})} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$.

Note that the$c$-transport cost ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}$ is related tothe path-wise $c$-transport cost $F_{c}{({\mathbf{X}})}$ via

where $S_{c}{({\mathbf{X}})}$ is a non-negative measurement of how close $\mathbf{X}$ is to be geodesic:We have ${S_{c}{({\mathbf{X}})}} \geq 0$following Jensen's inequality ${\int_{0}^{1}{c{({\overset{˙}{X}}_{t})}{dt}}} \geq {c{({\int_{0}^{1}{{\overset{˙}{X}}_{t}{dt}}})}} = {c{({X_{1} - X_{0}})}}$, and ${S_{c}{({\mathbf{X}})}} = 0$ if $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$.Hence, when $\mathbf{X}$ is the linear interpolation of $(X_{0},X_{1})$, we have from Theorem 5.3 ‣ 5.1 𝑐-Rectified Flow of Time-Differentiable Processes 𝑿 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport") that

which establishes that $(Z_{0},Z_{1})$ yields no larger transport cost than $(X_{0},X_{1})$.

### Theorem 5.5

Assume that $c$ is convex with conjugate $c^{\ast} \in {C^{1}{({\mathbb{R}}^{d})}}$, and the conditions in Definition 5.4 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport") holds. Then Equation (28 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")) holdsand ${{{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}} \leq {{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}}}.$

Compared with the regular $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ mapping,the key difference here is thatthe monotonicity of $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$ only holds for the specific $c$ that it employees, rather than all convex cost functions. More importantly,as we show below,recursively applying $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$yields optimal couplings w.r.t. $c$,a key property that the regular rectified flow misses.

### Fixed Points of$c$-$\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ are$c$-Optimal

We show three key results regarding the optimality of fixed points of the $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$ mapping:1) A coupling $(X_{0},X_{1})$ is afixed point of$c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$, that is, ${(X_{0},X_{1})} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$, if and only if it is $c$-optimal;2) Define $\ell_{X,c}^{\ast} = {\inf_{f}{L_{{\mathbf{X}},c}{(f)}}}$ where $\mathbf{X}$ is the linear interpolation of $(X_{0},X_{1})$.Then $\ell_{X,c}^{\ast}$ yields an indication of $c$-optimality of $(X_{0},X_{1})$, that is, $L_{X,c}^{\ast} = 0$, iff $(X_{0},X_{1})$ is $c$-optimal.3) The minimum $\ell_{X,c}^{\ast}$ in the first $k$ iterations of $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$ steps decreaseswith an $O{({1/k})}$ rate.

### Theorem 5.6

Assume that $c$ is convex with conjugate $c^{\ast}$, and ${c,c^{\ast}} \in {C^{1}{({\mathbb{R}}^{d})}}$ and $\mathbf{X}$ is the linear interpolation process of $(X_{0},X_{1})$.Assume that $(X_{0},X_{1})$ is a $c$-rectifiable coupling,and $f^{\mathbf{X},c} \in {C^{2,1}{({{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}})}}$.Then the following statements are equivalent:i) $(X_{0},X_{1})$ is a fixed point of $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$, that is, ${(X_{0},X_{1})} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{(X_{0},X_{1})}}$.ii) $\ell_{X,c}^{\ast} ≔ {\inf_{f}{L_{\mathbf{X},c}{(f)}}} = {L_{\mathbf{X},c}{(f^{\mathbf{X},c})}} = 0$, for $L_{\mathbf{X},c}$ in.iii) $(X_{0},X_{1})$ is a $c$-optimal coupling.

### Proof

i\) $\rightarrow$ ii).If ${(Z_{0},Z_{1})} = {(X_{0},X_{1})}$, we have ${S_{c}{({\mathbf{Z}})}} = 0$ and ${L_{{\mathbf{X}},c}{(f^{{\mathbf{X}},c})}} = 0$ following (28 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")).iii) $\rightarrow$ ii).If $(X_{0},X_{1})$ is $c$-optimal, we have ${{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}} \leq {{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}}$, which again implies that ${L_{{\mathbf{X}},c}{(f^{{\mathbf{X}},c})}} = 0$ following (28 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")).ii) $\rightarrow$ i)Note that

Therefore, ${L_{{\mathbf{X}},c}{(f^{{\mathbf{X}},c})}} = 0$implies that${\overset{˙}{X}}_{t} = {g_{t}^{{\mathbf{X}},c}{(X_{t})}}$$t$-almost surely. Because $Z_{t}$ satisfies the same equation, whose solution is assumed to be unique, we have ${\mathbf{Z}} = {\mathbf{X}}$ and hence ${(Z_{0},Z_{1})} = {(X_{0},X_{1})}$.ii) $\rightarrow$ iii)Because $\mathbf{X}$ is the linear interpolation, we have $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$, and it simultaneously satisfies the ODE ${dX_{t}} = {g_{t}^{{\mathbf{X}},c}{(X_{t})}dt}$.Using Lemma 5.9 shows that $(X_{0},X_{1})$ is $c$-optimal.∎

Knowing that $L_{{\mathbf{X}},c}{(f^{{\mathbf{X}},c})}$ is an indication of $c$-optimality, we show below that it is guaranteed to converge to zero with recursive $\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}$ updates.

### Corollary 5.7

Let $\mathbf{Z}^{k}$ be the $k$-th $c$-rectified flow of $(X_{0},X_{1})$, satisfying $\mathbf{Z}^{k + 1} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{({(Z_{0}^{k},Z_{1}^{k})})}}$ and ${(Z_{0}^{0},Z_{1}^{0})} = {(X_{0},X_{1})}$.Assume each $(Z_{0}^{k},Z_{1}^{k})$ is $c$-rectifiable for $k = {0,\ldots,K}$. Then

Therefore, if ${{\mathbb{E}}{\lbrack{c{({X_{1} - X_{0}})}}\rbrack}} < {+ \infty}$,we have ${{{\min_{k \leq K}L_{\mathbf{Z}^{k},c}}{(f^{\mathbf{Z}^{k},c})}} + {S_{c}{(\mathbf{Z}^{k + 1})}}} = {O\left( {1/K} \right)}$.

### Proof

Applying (28 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")) to $(Z_{0}^{k},Z_{1}^{k})$ and $(Z_{0}^{k + 1},Z_{1}^{k + 1})$ yields

Summing it over $k = {0,\ldots,K}$,

### $c$-Rectified Flow as Optimization Algorithms

In this section, we draw more understanding on how iterative $c$-rectified flowing solves the static and dynamic OT problems. We first show that $c$-rectified flow can be viewed as an alternative direction descent on the dynamic OT problem, and then that $c$-rectified coupling as a majorize-minimization (MM) algorithm on the statistic OT problem.The results in this section are framed in terms of a general path-wise loss function $F_{c}{({\mathbf{Y}})}$,and hence provide a useful starting point for deriving $c$-rectified flow like approaches tomore general optimization problems with coupling constraints.

### $c$-Rectified flow as alternative direction descent on (8)

The mapping ${\mathbf{Z}}^{k + 1} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{({\mathbf{Z}}^{k})}}$ can beinterpreted as an alternative direction descent procedure for the dynamic OT problem:

Here in (29 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")),we minimize $F_{c}{({\mathbf{Y}})}$in the set of processes whose start-end pair $(Y_{0},Y_{1})$ equals the coupling $(Z_{0}^{k},Z_{1}^{k})$ from ${\mathbf{Z}}^{k}$,which simply yields the linear interpolation $X_{t}^{k} = {{tZ_{1}^{k}} + {{({1 - t})}Z_{0}^{k}}}$ by Jensen's inequality.In (30 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")), we minimize $F_{c}{({\mathbf{Y}})}$ given the path-wise marginal constraint of ${{Law}{(Y_{t})}} = {{Law}{(X_{t}^{k})}}$ for all time $t \in {\lbrack 0,1\rbrack}$, which yields the $c$-rectified flow following Theorem 5.3 ‣ 5.1 𝑐-Rectified Flow of Time-Differentiable Processes 𝑿 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport").Note that the updates in both (29 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")) and (30 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport"))keep the start-end marginal laws ${Law}{(Y_{0})}$ and ${Law}{(Y_{1})}$ unchanged, and hencethe algorithm stays inside the feasible set $\{{\mathbf{Y}}:{{{{Law}{(Y_{0})}} = \pi_{0}},{{{Law}{(Y_{1})}} = \pi_{1}}}\}$in once it is initialized to be so.The updates in (29 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport"))-(30 ‣ 5.4 𝑐-Rectified Flow as Optimization Algorithms ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport")) highlight a key difference between our method and the Benamou-Brenier approach -:the key idea of Benamou-Brenier is to restrict the optimization domain to the set of deterministic, ODE-induced processes (a.k.a. flows),but our updates alternate between thedeterministic$c$-rectified flow ${\mathbf{Z}}^{k}$ and the linear interpolation process ${\mathbf{X}}^{k}$, which is *not* deterministic or ODE-inducableunless the fixed point is achieved.

### $c$-Rectified flow as an MM algorithm

The majorize-minimization (MM) algorithm is a general optimization recipe thatworks by finding a surrogate function that *majorizes* the objective function.Let $F{(X)}$ be the objective concave function to be minimize. An MM algorithm consists of iterative update of form $X^{k + 1} \in {{{\arg\min}_{Y}F^{+}}{(\left. Y \middle| X^{k} \right.)}}$,where $F^{+}$ is a majorization function of $F$ that satsifies

In this case,the MM update guarantees that $F{(X^{k})}$ is monotonically non-increasing:

One can also view MM as conducting coordinate descent on $(X,Y)$ for solving ${\min_{X,Y}F^{+}}{(\left. Y \middle| X \right.)}$.In the following, we show that ${(Z_{0}^{k + 1},Z_{1}^{k + 1})} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(Z_{0}^{k},Z_{1}^{k})})}}$can be interpreted as an MM algorithm for the static OT problem for minimizing ${\mathbb{E}}{\lbrack{c{({X_{1} - X_{1}})}}\rbrack}$ in the set of couplings of $\pi_{0}$ and $\pi_{1}$. The majorization function corresponding to $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$ can be shown to be

where $F_{c}^{+}{(\left. {(Y_{0},Y_{1})} \middle| {(X_{0},X_{1})} \right.)}$ denotes the minimum value of $F_{c}{(\overset{\sim}{\mathbf{Y}})}$for $\overset{\sim}{\mathbf{Y}}$ whose start-end points equal $(Y_{0},Y_{1})$,and yields the same marginal laws as that of the linear interpolation process of $(X_{0},X_{1})$.

### Proposition 5.8

i)$F_{c}^{+}$yields a majorization function of the $c$-transport cost ${\mathbb{E}}{\lbrack{c{({Y_{1} - Y_{0}})}}\rbrack}$ in the sense that

and the minimum is attained by ${(X_{0},X_{1})} = {(Y_{0},Y_{1})}$,where $\Pi_{0,1}$ denotes the set of couplings of $\pi_{0}$ and $\pi_{1}$.ii) $c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}$ yields the MM update related $F^{+}$ in that

### Proof

i\) For any coupling $(X_{0},X_{1})$ and $(Y_{0},Y_{1})$, we have

where the inequality holds because remove the constraint ${\mathbf{Y}} \in \mathcal{M}_{X}$. In addition, it is obvious that the inequality above becomes equality when ${(X_{0},X_{1})} = {(Y_{0},Y_{1})}$.ii) Note that

whose minimum of the right side is attained by ${\mathbf{Y}} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{f}\mathtt{l}\mathtt{o}\mathtt{w}}{({(X_{0},X_{1})})}}$ following Theorem 5.3 ‣ 5.1 𝑐-Rectified Flow of Time-Differentiable Processes 𝑿 ‣ 5 𝑐-Rectified Flow ‣ \Name Flow: A Marginal Preserving Approach to Optimal Transport"). Hence, the minimum of the left side is attained by ${(Y_{0},Y_{1})} = {c\text{-}{\mathtt{R}\mathtt{e}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{f}\mathtt{y}}{({(X_{0},X_{1})})}}$.∎

### Hamilton-Jacobi Equation and Optimal Transport

The proof of Theorem 5.6 relies on akey lemma shows that if the trajectories of an ODE of form ${dX_{t}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(X_{t})}})}dt}$ are geodesic in that $X_{t} = {{tX_{1}} + {{({1 - t})}X_{0}}}$,then the induced coupling $(X_{0},X_{1})$ is an $c$-optimal coupling of its marginals.The proof of this lemma relies onHamilton-Jacobi (HJ) equation, which providesa characterization of $f$for an ODE ${dX_{t}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(X_{t})}})}dt}$ whose trajectories are geodesic.The connection between HJ equation and optimal transport has been a classic result andcan be found in, for example,.

### Lemma 5.9

Let ${v_{t}{(x)}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(x)}})}}$ where $c^{\ast} \in {C^{1}{({\mathbb{R}}^{d})}}$is a convex function $c$, and $f \in {C^{2,1}{({{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}})}}$ and $\nabla c^{\ast}$ is an injective mapping. Assume all trajectories of ${dx_{t}} = {v_{t}{(x_{t})}dt}$ are geodesic paths in that $x_{t} = {{tx_{1}} + {{({1 - t})}x_{0}}}$. Then we have:i) There exists ${\overset{\sim}{f}}_{t}$ such that ${\nabla{\overset{\sim}{f}}_{t}} = {\nabla f_{t}}$ (and hence we can replace $f$ with $\overset{\sim}{f}$ in the assumption),such that the following Hamilton--Jacobi (HJ) equation holds

where the minimum is attained if $\{ y_{t}\}$ follows the ODE ${dy_{t}} = {v_{t}{(y_{t})}dt}$.iii)Assume a coupling $(X_{0},X_{1})$of $\pi_{0},\pi_{1}$satisfies ${dX_{t}} = {v_{t}{(X_{t})}dt}$.Then $(X_{0},X_{1})$ is a $c$-optimal coupling.

### Proof

i)Starting from any point $x_{t} = x \in {\mathbb{R}}^{d}$ at time $t$,because the trajectories of ${dx_{t}} = {v_{t}{(x_{t})}dt}$ are geodesic,we have ${\overset{˙}{x}}_{t} = {v_{t}{(x_{t})}} = {const}$ following the trajectory. Because ${v_{t}{(x)}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(x)}})}}$ and$\nabla c^{\ast}$ is injective, we have ${{\nabla f_{t}}{(x_{t})}} = {const}$ as well. Hence, we have

On the other hand, define ${h_{t}{(x)}} = {{\partial_{t}{f_{t}{(x)}}} + {c^{\ast}{({{\nabla f_{t}}{(x)}})}}}$. Then we have

This suggests that ${{\nabla_{x}h_{t}}{(x)}} = 0$ everywhere and hence$h_{t}{(x)}$ does not depend on $x$.Define ${{\overset{\sim}{f}}_{t}{(x)}} = {{f_{t}{(x)}} - {\int_{0}^{t}{h_{t}{(x_{0})}{dt}}}}$, where $x_{0}$ is any fixed point in ${\mathbb{R}}^{d}$.Then

ii)Take any $y_{0},y_{1}$ in ${\mathbb{R}}^{d}$,let $y_{t} = {{ty_{1}} + {{({1 - t})}y_{0}}}$ be their linear interpolation. We have

The equality in$\overset{}{\leq}$ is attained if $y_{t}$ follows the geodesic ODE ${dy_{t}} = {v_{t}{(y_{t})}dt}$ as we have ${y_{1} - y_{0}} = {{\nabla c^{\ast}}{({{\nabla f_{t}}{(y_{t})}})}}$, $\forall t$ in this case.A similar derivation holds for $f_{t}$.iii) Note that i) gives that ${c{({y_{1} - y_{0}})}} \geq {{f_{1}{(y_{1})}} - {f_{0}{(y_{0})}}}$.For any coupling $(Y_{0},Y_{1})$ of $\pi_{0},\pi_{1}$, we have

Hence, $(X_{0},X_{1})$ is a $c$-optimal coupling.∎

### Connection to Benamou-Brenier Formula

The results in Lemma 5.9can also formally derived from Benamou-Brenier problem,as shown in the seminal work of.By introducing a Lagrangian multiplier $\lambda:{{{\mathbb{R}}^{d} \times {\lbrack 0,1\rbrack}}\rightarrow{\mathbb{R}}}$ for the constraint of ${{\overset{˙}{\varrho}}_{t} + {\nabla \cdot {({v_{t}\varrho_{t}})}}} = 0$, the problem in can be framed into a minimax problem:

where $\mathcal{L}{(v,\varrho,\lambda)}$ is the Lagrangian function, and$\Gamma_{0,1}$ denotes the set of density functions ${\{\varrho_{t}\}}_{t}$ satisfying ${\varrho_{0} = {{{d\pi_{0}}/d}x}},{\varrho_{1} = {{{d\pi_{1}}/d}x}}$.Note that the following integration by parts formulas:

where we assume that $\lambda_{t}v_{r}\rho_{t}$ decays to zero sufficiently fast at infinity.We have

At the saddle points,the functional derivations of $\mathcal{L}$ equal zero, yielding

Assume $\varrho_{t}$ is positive everywhere and note that ${{\nabla c^{\ast}}{({{\nabla c}{(x)}})}} = x$, we have $v_{t} = {{\nabla c^{\ast}}{({\nabla\lambda_{t}})}}$,and hence ${{\nabla{\lambda_{t}^{\top}v_{t}}} - {c{(v_{t})}}} = {c^{\ast}{({\nabla\lambda_{t}})}}$.Plugging it back to $\frac{\delta\mathcal{L}}{\delta\rho_{t}} = 0$ yields that ${{\overset{˙}{\lambda}}_{t} + {c^{\ast}{({\nabla\lambda_{t}})}}} = 0$.Overall, the (formal) KKT condition of is

This matches the result in Lemma 5.9 with $\lambda_{t} = {\overset{\sim}{f}}_{t}$.

## Discussion and Open Questions

Corollary 5.7 only bounds the surrogate measure $\ell_{Z^{k},c}^{\ast}$. Can we directly bound the optimality gap on the $c$-transport cost$e_{k}^{\ast} = {{{\mathbb{E}}{\lbrack{c{({Z_{1}^{k} - Z_{0}^{k}})}}\rbrack}} - {\inf_{(Z_{0},Z_{1})}{{\mathbb{E}}{\lbrack{c{({Z_{1} - Z_{0}})}}\rbrack}}}}$?Can we find a certain type of strong convexity like condition, under which $e_{k}^{\ast}$ decays exponentially with $k$?

For machine learning (ML) tasks such as generative models and domain transfer, the transport cost is not necessarily the direct object of interest.In these cases,as suggested in, rectified flow might be preferred because it is simpler and does not require to specify a particular cost $c$.Question: for such ML tasks, when would it be preferred to use OT with a specific $c$, and how to choose $c$ optimally?

In practice, recursively applying the ($c$-)rectification accumulates errorsbecause the training optimization for the drift field and the simulation of the ODEcan not be conducted perfectly.Howto avoid the error accumulationat each step?Assume ${\{ x_{1,i}\}}_{i} \sim \pi_{1}$, and ${\{ z_{0,i}^{k},z_{1,i}^{k}\}}_{i}$ is obtained by solving the ODE of the $k$-th $c$-rectified flow starting from $z_{0,i}^{k} \sim \pi_{0}$.As we increase $k$, ${\{ z_{0,i}^{k}\}}_{i}$ may yield increasingly bad approximation of $\pi_{1}$ due to the error accumulation. One way to fix this is to adjust $\{ z_{1,i}^{k}\}$ to make it closer to ${\{ x_{1,i}^{k}\}}_{i}$ at each step. This can be done by reweighting/transporting ${\{ z_{1,i}^{k}\}}_{i}$ towards ${\{ x_{1,i}^{k}\}}_{i}$ by minimizing certain discrepancy measure,or replacing each $z_{1,i}^{k}$ with $x_{\sigma{(i)}}^{k}$ where $\sigma$ is a permutation that yields a one-to-one matching between $\{ z_{1}^{(i)}\}$ and ${\{ x_{1}^{(i)}\}}_{i}$.The key and challenging part is to do the adjustment in a good and fast way, ideally with a (near) linear time complexity.

With or without the adjustment step,build a complete theoretical analysis on the statistical error of the method.

In what precise sense is rectified flow solving a multi-objective variant of optimal transport?
