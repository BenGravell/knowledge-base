## Introduction

Policy optimization is the problem of designing a control policy that minimizes a prescribed performance objective. In reinforcement learning (RL), the problem is typically formulated as a search over a parameterized policy class \[sutton2002reinforcement\]. *Model-based* RL methods use a model of the dynamics to guide policy updates, improving sample efficiency \[atkeson1997comparison\].

A growing line of work studies policy optimization problems where the policy is a model predictive controller (MPC) \[amos2018differentiable, gros2019data, agrawal2020learning, drgovna2022differentiable, zuliani2023bp, zuliani2024closed\]. MPC-based policies generate predictions of future state trajectories using a system model and naturally incorporate constraints into their decision-making process, offering stronger safety guarantees and greater interpretability compared to model-free approaches.

Existing MPC-based policy optimization schemes typically assume that the dynamics model is exact, and convergence results rely on this assumption \[zuliani2023bp\]; obtaining convergence guarantees when the model is inaccurate remains an open problem. In this paper, we propose a novel policy optimization algorithm with convergence guarantees inspired by \[he2024gray\] blending model-based gradient information with zeroth-order updates that is robust to inexact models. A key feature of our method is that it can smoothly trade off between model-based and zeroth-order components, putting more weight on the model whenever it is trusted and relying more on model-free information otherwise. To handle the nonsmoothness of MPC policies, we leverage the tools of \[bolte2021conservative\]. We valide our approach on a 12-dimensional nonlinear quadcopter.

Related work: Zeroth-order optimization addresses the problem of minimizing an objective function when first-order information is unavailable. The foundations of the approach used in this paper trace back to the seminal work of \[flaxman2004online\], which introduced a smoothing-based approximation technique enabling gradient-free optimization for possibly nonsmooth functions. Subsequent research extended these ideas to convex settings: see \[duchi2012randomized\] and \[nesterov2017random\] for one-point gradient estimators, or \[shamir2017optimal\] for a two-point estimator. More recently, \[lin2022gradient\] generalized the two-point approach to nonconvex problems, demonstrating its effectiveness beyond the convex regime. Closest to our work is \[he2024gray\], which combines a one-point zeroth-order estimator with model-based gradient information to improve convergence speed, a direction we further build upon in this paper.

Notation: $\mathcal{X}^{n}$ denotes the $n$-fold Cartesian product of the set $\mathcal{X}$. Given a path-differentiable function $g$ of two arguments $x$ and $y$, $\mathcal{J}_{g,x}$ and $\mathcal{J}_{g,y}$ denote the projection of the conservative Jacobian $\mathcal{J}_{g}$ onto the $x$ and $y$ entries. $\mathbb{B}$ and $\mathbb{S}$ are the unit ball and sphere in the Euclidean norm. $U{({\mathbb{B}})}$ and $U{({\mathbb{S}})}$ denote uniform distributions over $\mathbb{B}$ and $\mathbb{S}$. $\mathcal{N}_{\mathcal{X}}$ is the tangent cone of the set $\mathcal{X}$ in the sense of Clarke. $\operatorname{dist}\limits_{p}{(a,B)}$ is the distance between point $a$ and set $B$ in the $p$-norm.

## Preliminaries

For completeness, we briefly review the notions of definability and conservative Jacobians in Sections 2.1 and 2.2, respectively. In Appendix A, we further detail under which assumptions the solution map of an MPC problem admits a conservative Jacobian, and summarize an efficient algorithm to compute it. In Section 2.3 we summarize various notions of critical points in nonsmooth analysis, used throughout the paper.

### Functions Definable in an o-minimal Geometry

### Definition 2.1 (Definitions 1.4 and 1.5, \[coste1999introduction\])

A collection $\mathcal{O} = {(\mathcal{O}_{n})}_{n \in {\mathbb{N}}}$, where $\mathcal{O}_{n} \subset 2^{{\mathbb{R}}^{\ltimes}}$ for each $n \in {\mathbb{N}}$, is an o-minimal structure on $({\mathbb{R}}, +, \cdot )$ if: 1) all semialgebraic subsets of ${\mathbb{R}}^{\ltimes}$ belong to $\mathcal{O}_{n}$; 2) $\mathcal{O}_{1}$ is the set of all finite unions of points and intervals; 3) $\mathcal{O}_{n}$ is a boolean subalgebra of $2^{{\mathbb{R}}^{\ltimes}}$; 4) ${A \times B} \in \mathcal{O}_{n + m}$ for all ${A,B} \in {\mathcal{O}_{n} \times \mathcal{O}_{m}}$; 5) the set $\{{v \in {\mathbb{R}}^{\ltimes}}:{{(\succapprox,\precapprox)} \in {{\mathbb{A}}\text{~for some~}\precapprox} \in {\mathbb{R}}}\}$, for any $A \in \mathcal{O}_{n + 1}$, belongs to $\mathcal{O}_{n}$. A subset of ${\mathbb{R}}^{\ltimes}$ which belongs to $\mathcal{O}$ is said to be definable.

A function $\varphi:{{\mathbb{R}}^{\ltimes}\rightarrow{\mathbb{R}}^{\mid}}$ is definable if its graph $\{{(x,v)}:{v = {\varphi{(x)}}}\}$ is definable. Definable functions are ubiquitous in control and optimization, containing, for example, all semialgebraic and globally subanalytic functions. Moreover, they are stable under most common operations, such as composition, differentiation, and affine transformations.

### Conservative Jacobians

The notion of Conservative Jacobians, introduced in \[bolte2021conservative\], extends the concept of derivatives to locally Lipschitz, almost everywhere differentiable functions.

### Definition 2.2 (\[bolte2021conservative\])

The map $\mathcal{J}_{\phi}:{{\mathbb{R}}^{\ltimes}\rightrightarrows{\mathbb{R}}^{\gtrdot \times \ltimes}}$ is a conservative Jacobian of the locally Lipschitz function $\phi:{{\mathbb{R}}^{\ltimes}\rightarrow{\mathbb{R}}^{\gtrdot}}$ if it is nonempty-valued, outer semicontinuous, locally bounded, and for all absolutely continuous curves $x:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{\ltimes}}$ and almost all $t \in {\lbrack 0,1\rbrack}$

Excluding a set of measure zero, $\mathcal{J}_{\phi}$ coincides almost everywhere with the gradient $\nabla\phi$. Unlike other nonsmooth Jacobians, such as Clarke Jacobians, conservative Jacobians obey the chain rule of differentiation and a nonsmooth version of the implicit function theorem \[bolte2021nonsmooth\], making them particularly suitable for the sensitivity analysis of solution maps of optimization problems, which are typically nonsmooth functions implicitly defined by optimality conditions.

A function admitting a conservative Jacobian is called *path-differentiable*. As demonstrated in Lemma 3, \[bolte2021nonsmooth\], locally Lipschitz definable functions are always path-differentiable.

### Stationary points in nonsmooth optimization

The *Clarke Jacobian* of a locally Lipschitz function $f:{{\mathbb{R}}^{\ltimes}\rightarrow{\mathbb{R}}}$ is the outer-semicontinuous map

where $D_{f} \subset {\mathbb{R}}^{\ltimes}$ is the full-measure set on which $f$ is differentiable, and $\operatorname{co}$ denotes the convex hull. There is a close connection between Clarke and conservative Jacobians \[bolte2021conservative\]

If $x$ is a local minimizer of $f$, then $0 \in {\partial_{c}{f{(x)}}}$ (and similarly $0 \in {{\operatorname{co}\mathcal{J}_{f}}{(x)}}$). Hence, in nonsmooth optimization, one typically searches for *Clarke stationary points*, that is, points $x$ with $0 \in {\partial_{c}{f{(x)}}}$. In our setting, however, identifying Clarke stationary points is infeasible due to the lack of exact knowledge of the true system dynamics. A weaker notion of stationarity is that of a *Goldstein $\delta$-critical point*, defined as any $x$ such that $0 \in {\partial_{\delta}{f{(x)}}}$, where

is the Goldstein $\delta$-subdifferential of $f$. As shown in \[zhang2020complexity\], ${\lim_{\delta \downarrow 0}{\partial_{\delta}{f{(x)}}}} = {\partial_{c}{f{(x)}}}$, making Goldstein $\delta$-stationarity a meaningful optimality condition for nonsmooth problems.

For constrained problems, such as minimizing $f{(x)}$ subject to ${h{(x)}} = 0$, $x \in \mathcal{X}$, we consider a generalized stationarity concept adapted from \[grimmer2025goldstein\]. A point $x$ is said to satisfy the *Goldstein Fritz-John $\delta$-critical condition* if there exist multipliers ${\lambda_{0},\lambda_{1}} \geq 0$ such that

This condition parallels the classical Fritz-John optimality conditions, with the gradients replaced by Goldstein $\delta$-subdifferentials. If $\lambda_{0} > 0$, the point is called a *Goldstein KKT $\delta$-critical point*.

## Problem Formulation

Consider an unknown system evolving over $t \in {\mathbb{Z}}_{\lbrack\nvdash,{\mathbb{T}}\rbrack}$ from an initial condition $x_{0} \in {\mathbb{R}}^{\ltimes_{\curvearrowleft}}$

$u_{t}$ ${= {\operatorname{MPC}{(x_{t},\theta)}}},$ (2b)

where $\theta \in \Theta$ is a tunable parameter that determines the behavior of the policy and $\Theta \subset {\mathbb{R}}^{\ltimes_{\theta}}$ is a parameter set. Despite not knowing the dynamics in (2a) exactly, we assume existence of a model $g:{{{\mathbb{R}}^{\ltimes_{\curvearrowleft}} \times {\mathbb{R}}^{\ltimes_{\approxeq}}}\rightarrow{\mathbb{R}}^{\ltimes_{\curvearrowleft}}}$ such that ${g{(x,u)}} \approx {f{(x,u)}}$ for all $x$ and $u$. We consider the constraints

where $\mathcal{X} \subseteq {\mathbb{R}}^{\ltimes_{\curvearrowleft}}$ and $\mathcal{U} \subseteq {\mathbb{R}}^{\ltimes_{\approxeq}}$ are known convex sets. The input $u_{t} = {\operatorname{MPC}{(x_{t},\theta)}}$ depends on the state $x_{t}$ (last constraint in (2b)) and the parameters $\theta$. It is computed by solving the problem

where $\ell_{\theta}$ and $\ell_{N,\theta}$ are parameterized cost functions, and applying $u_{t} = u_{0|t}$. Throughout, we assume that is a quadratic program (QP) meeting the conditions of Theorem A.2. ‣ Appendix A Differentiating Solutions of Optimization Problems ‣ Policy Optimization for Unknown Systems using Differentiable Model Predictive Control") in Appendix A. If $g$ is a nonlinear function, one can use the linearization techniques in \[zuliani2023bp, Section VI-A\] to obtain an MPC that can be expressed as a quadratic program.

Our emphasis is on QP-based MPC policies, which often deliver strong performance even on nonlinear control problems. Nonetheless, the framework can easily be extended to fully nonlinear policies using the differentiation methods in \[zuliani2025differentiable\]. Similarly, this method can accommodate nonconvex upper-level constraints in as long as the MPC satisfies Assumption 1. Note additionally that while in this work we restrict $\theta$ to parameters appearing in the cost of (2b), extending it to also affect the constraints or dynamics of the MPC is straightforward.

Out goal is to obtain an MPC design $\theta^{\ast}$ that minimizes a known objective function $C{(x,u)}$, where $x = {(x_{0},\ldots,x_{T})}$ and $u = {(u_{0},\ldots,u_{T - 1})}$, tipically with $T \gg N$, are the closed-loop trajectories obtained by combining (2a) and (2b), while satisfying for all $t$.

Since $f$ is unknown, problem cannot be solved directly.

## Model-based Gradient Estimation

### Solving the problem when dynamics are known

Even with perfect model knowledge, is difficult to solve due to the nonsmooth constraints imposed by the MPC function. In \[zuliani2023bp\] we introduced a gradient-based method specifically designed for such problems, which solves an unconstrained reformulation of. To cast as an unconstrained problem, let $x:{\Theta\rightarrow{\mathbb{R}}^{{\mathbb{T}}\ltimes_{\curvearrowleft}}}$ and $u:{\Theta\rightarrow{\mathbb{R}}^{{({{\mathbb{T}} - \nVdash})}\ltimes_{\approxeq}}}$ be the closed-loop trajectories obtained by combining (2b) and (2a) over the entire horizon $t \in {\mathbb{Z}}_{\lbrack\nvdash,{\mathbb{T}}\rbrack}$. Then becomes

Since enforces ${u_{t}{(\theta)}} \in \mathcal{U}$ for all $t \in {\mathbb{Z}}_{\lbrack\nvdash,{{\mathbb{T}} - \nVdash}\rbrack}$, the input constraints in can be dropped. The state constraints can be enforced through a continuous penalty function ${P{(\theta)}} = {\overline{P}{({x{(\theta)}})}}$ satisfying ${P{(\theta)}} = 0$ whenever ${x{(\theta)}} \in \mathcal{X}^{T}$ and ${P{(\theta)}} > 0$ otherwise

Under appropriate assumptions, which we detail in Section 6.1, $\mathcal{C}$ is path-differentiable and the update law $\theta_{k + 1} = {\Pi_{\Theta}{\lbrack{\theta_{k} - {\alpha_{k}d_{k}}}\rbrack}}$, where $d_{k} \in {\mathcal{J}_{\mathcal{C}}{(\theta_{k})}}$, and $\Pi_{\Theta}:{{\mathbb{R}}^{\ltimes_{\theta}}\rightarrow\Theta}$ is the projector onto the set $\Theta$, converges to a minimizer of.

### Imperfect Gradient Information using an Inexact Model

Since (2a) is unknown, the exact Jacobian $\mathcal{J}_{\mathcal{C}}$ cannot be computed, and the exact update cannot be applied directly. Instead, we approximate $\mathcal{J}_{\mathcal{C}}$ using the available model $g$ of the true dynamics $f$. First, we recursively build approximations $J_{x}{(\theta)}$ and $J_{u}{(\theta)}$ of $\mathcal{J}_{x}{(\theta)}$ and $\mathcal{J}_{u}{(\theta)}$ via

$J_{u_{t}}{(\theta)}$ ${= {{J_{\operatorname{MPC},x}{(x_{t},\theta)}J_{x_{t}}{(\theta)}} + {J_{\operatorname{MPC},\theta}{(x_{t},\theta)}}}},$ (8b)
where $x_{t} = {x_{t}{(\theta)}}$, $u_{t} = {u_{t}{(\theta)}}$, and $J_{g}{(x,u)}$ and $J_{\text{MPC}}{(x,\theta)}$ are elements of the conservative Jacobians $\mathcal{J}_{g}{(x,u)}$ and $\mathcal{J}_{\text{MPC}}{(x,\theta)}$, respectively. We then combine $J_{x}{(\theta)}$ and $J_{u}{(\theta)}$ to obtain an estimate $J_{\mathcal{C}}{(\theta)}$ of $\mathcal{J}_{\mathcal{C}}{(\theta)}$ using the chain rule

${{J_{\mathcal{C}}{(\theta)}} = {{J_{C,x}{(x,u)}J_{x}{(\theta)}} + {J_{C,u}{(x,u)}J_{u}{(\theta)}}}},$ (8c)

where ${\mathcal{C}{(\theta)}} = {C{({x{(\theta)}},{u{(\theta)}})}}$, and ${J_{C}{(x,u)}} \in {\mathcal{J}_{C}{(x,u)}}$. Replacing $\mathcal{J}_{\mathcal{C}}{(\theta)}$ with $J_{\mathcal{C}}{(\theta)}$ yields the implementable update $\theta_{k + 1} = {\Pi_{\Theta}{\lbrack{\theta_{k} - {\alpha_{k}J_{\mathcal{C}}{(\theta_{k})}}}\rbrack}}$.

## Model-free Gradient Estimation

The update of Section 4.2 is appealing because it only relies on the approximate model. However, without further assumptions on the model accuracy, it is impossible to derive convergence guarantees. To address this issue, we construct gradient-like directions purely from data, for which convergence can be established under mild conditions.

For any $\delta > 0$, consider the *randomized smoothing approximation* ${\mathcal{C}^{\delta}{(\theta)}}:{\Theta_{\delta}\rightarrow{\mathbb{R}}}$ of $\mathcal{C}$

where $\Theta_{\delta}:={\Theta + {\delta{\mathbb{B}}}}$. $\mathcal{C}^{\delta}$ is a smooth approximation of $\mathcal{C}$: as long as $\mathcal{C}$ is Lipschitz with constant $L_{\mathcal{C}}$, $\mathcal{C}^{\delta}$ is continuously differentiable and Lipschitz with constant $L_{\mathcal{C}^{\delta}} = {c\sqrt{n_{\theta}}\delta^{- 1}L_{\mathcal{C}}}$ for some $c > 0$ \[lin2022gradient, Proposition 2.3\]. Working with $\mathcal{C}^{\delta}$ instead of $\mathcal{C}$ has two key benefits: (i) the Lipschitz continuity of $\mathcal{C}$ implies smoothness of $\mathcal{C}^{\delta}$, and (ii) one can estimate $\nabla\mathcal{C}^{\delta}$ solely using function evaluations. For this, we use the following one-point estimator

where $v_{k}$ is sampled i.i.d. from $U{({\mathbb{S}})}$ for each $k \in {\mathbb{N}}$. We have the following.

### Lemma 5.1

For any $\theta \in \Theta$, ${{\mathbb{E}}_{\succapprox}{\lbrack{{\mathbb{J}}_{{\mathbb{C}}^{\delta}}{(\theta,\succapprox)}}\rbrack}} = {{\nabla{\mathbb{C}}^{\delta}}{(\theta)}}$.

### Proof 5.2

By Lemma 1 in \[flaxman2004online\], it holds that ${{\mathbb{E}}_{\succapprox}{\lbrack{{\mathbb{C}}{({\theta + {\delta\succapprox}})}\succapprox}\rbrack}} = {{\delta/\ltimes_{\theta}}{\nabla{\mathbb{C}}^{\delta}}{(\theta)}}$. Since $v$ is zero-mean, we immediately have ${{\mathbb{E}}_{\succapprox}{\lbrack{{({{{\mathbb{C}}{({\theta + {\delta\succapprox}})}} - {{\mathbb{C}}{(\theta)}}})}\succapprox}\rbrack}} = {{\mathbb{E}}_{\succapprox}{\lbrack{{\mathbb{C}}{({\theta + {\delta\succapprox}})}\succapprox}\rbrack}} = {{\delta/\ltimes_{\theta}}{\nabla{\mathbb{C}}^{\delta}}{(\theta)}}$.

Lemma 5.1 shows that the zeroth-order estimator provides an unbiased estimate of $\nabla\mathcal{C}^{\delta}$. To relate this to the original nonsmooth objective, we recall the following result from \[lin2022gradient\].

### Lemma 5.3

Suppose $\mathcal{C}$ is $L_{\mathcal{C}}$-Lipschitz in $\Theta$. Then ${{\nabla\mathcal{C}^{\delta}}{(\theta)}} \in {\partial_{\delta}{\mathcal{C}{(\theta)}}}$ for any $\theta \in \Theta$.

This means that estimating $\nabla\mathcal{C}^{\delta}$ yields an element of the Goldstein $\delta$-subdifferential of the true objective $\mathcal{C}$, thus providing a second implementable update law $\theta_{k + 1} = {\Pi_{\Theta}{\lbrack{\theta_{k} - {\alpha_{k}J_{\mathcal{C}^{\delta}}{(\theta_{k},v_{k})}}}\rbrack}}$.

## Proposed Algorithm

Our algorithm combines the model-based update of Section 4.2 with the model-free update of Section 5, following the *gray-box* scheme of \[he2024gray\]. At iteration $k$, we update $\theta^{k}$ as follows

where ${\{\alpha_{k}\}}_{k \in {\mathbb{N}}} \subset {\mathbb{R}}_{> \nvdash}$ is a sequence of vanishing stepsizes, and ${\{\eta_{k}\}}_{k \in {\mathbb{N}}} \subset {\lbrack 0,1\rbrack}$ weights the relative contribution of the two update directions. Choosing $\eta_{k} \approx 1$ prioritizes the model-based direction $J_{\mathcal{C}}{(\theta_{k})}$, whereas $\eta_{k} \approx 0$ makes the update closer to zeroth order via $J_{\mathcal{C}^{\delta}}{(\theta_{k},v_{k})}$. Generally, selecting $\eta_{k}$ is a design choice that should reflect the trustworthiness of the model. We showcase how the converge speed is affected by different choices of $\eta_{k}$ in simulation in Section 7.

### Convergence to a Goldstein \\texorpdfstring$\delta$delta-Critical Point

Our convergence analysis builds on Lemma 5.1 and standard results on stochastic projected gradient methods for nonsmooth, nonconvex objectives \[davis2020stochastic\]. We first impose regularity assumptions ensuring that the closed-loop map and the objective are locally Lipschitz and definable.

### Assumption 1

The true dynamics $f$, the model $g$, the cost function $C$, the penalty $P$, and the MPC function $\operatorname{MPC}:{{{\mathbb{R}}^{\ltimes_{\curvearrowleft}} \times \Theta}\rightarrow{\mathbb{R}}^{\ltimes_{\approxeq}}}$ are locally Lipschitz and definable in an o-minimal structure.

Under Assumption 1, the closed-loop trajectories $x{(\theta)}$ and $u{(\theta)}$ are locally Lipschitz and definable in $\theta$, allowing the definition of conservative Jacobians. Assumption 1 is not restrictive, as definable functions cover almost all functions of interest in control and optimization, and the MPC function satisfies Assumption 1 under the mild conditions laid out in Appendix A. To ensure feasibility of the MPC, one can resort to the technique in \[zuliani2023bp, Section VI-D\].

Our last technical requirement simplifies the analysis by ensuring boundedness of the gradients.

### Assumption 2

The set $\Theta$ is convex, compact and definable in an o-minimal structure.

To ensure convergence, we require the following conditions on $\alpha_{k}$ and $\eta_{k}$

${\alpha_{k} > 0},$ ${{{\sum_{k \in {\mathbb{N}}}\alpha_{k}} = {+ \infty}},{{\sum_{k \in {\mathbb{N}}}\alpha_{k}^{2}} < {+ \infty}}},$ (11a)
${\eta_{k} \in {\lbrack 0,1\rbrack}},$ ${{\sum_{k \in {\mathbb{N}}}{\eta_{k}\alpha_{k}}} < {+ \infty}}.$ (11b)

These conditions hold, for example, if $\alpha_{k} = {1/{({k + 1})}^{\gamma}}$ and $\eta_{k} = {1/{({k + 1})}^{\beta - \gamma}}$, with $\gamma \in {(0.5,1\rbrack}$ and $\beta > 1$. This allows for a wide range of possible stepsizes and, crucially, for different decrease rates for $\eta_{k}$. This last feature, in particular, allows us to accomodate situations where the model $J_{\mathcal{C}}$ is deemed trustworthy, and thus $\eta_{k}$ should have larger values, but also situations where $J_{\mathcal{C}}$ is less trusted and the zeroth-order estimation is preferred. Observe that $\eta_{k} \downarrow 0$, meaning that eventually the information obtained using the model is discarded and the algorithm relies solely on data.

### Theorem 6.1

Under Assumptions 1, and 2, if $\alpha_{k}$ and $\eta_{k}$ satisfy, then $\theta_{k}$ as obtained through converges to a Goldstein Fritz-John $\delta$-critical point of the problem

The proof of Theorem 6.1 requires several preliminary results. First, we prove that under Assumption 1 the approximation $\mathcal{C}^{\delta}$ of $\mathcal{C}$ retains definability and Lipschitz continuity.

### Lemma 6.2

Under Assumptions 1 and 2, $\mathcal{C}^{\delta}$ is Lipschitz continuous and definable.

### Proof 6.3

Under Assumptions 1 and 2, the functions $x{(\theta)}$ and $u{(\theta)}$ are definable and locally Lipschitz since both these properties are preserved by composition \[coste1999introduction, Exercise 1.11\]. Next, the function $y\mapsto{\max{\{ y_{1},y_{2}\}}}$ is the pointwise maximum of two linear functions, and it is therefore locally Lipschitz and definable (it is, in fact, semialgebraic). This proves that $\mathcal{C}$ is locally Lipschitz and definable. Since integration (and therefore expectation) preserves definability \[speissegger1999pfaffian\], $\mathcal{C}^{\delta}$ is definable for every $\delta > 0$. Moreover, since $\mathcal{C}$ is locally Lipschitz and therefore Lipschitz if restricted to $\Theta$, by \[lin2022gradient, Proposition 2.3\], $\mathcal{C}^{\delta}$ is Lipschitz for any $\delta > 0$.

Next, we show that the zeroth-order update dominates the model-based one for all $k$ large enough.

### Lemma 6.4

Under Assumptions 1 and 2, if $\alpha_{k}$ and $\eta_{k}$ satisfy, then ${\sum_{k \in {\mathbb{N}}}{\alpha_{k}\eta_{k}{\|{J_{\mathcal{C}}{(\theta_{k})}}\|}}} < {+ \infty}$.

### Proof 6.5

Since ${\sum_{k \in {\mathbb{N}}}{\alpha_{k}\eta_{k}}} < {+ \infty}$ by (11b), it suffices to prove that $\|{J_{\mathcal{C}}{(\theta_{k})}}\|$ is bounded for all $\theta_{k}$. To prove this, observe that ${\|{x{(\theta)}}\|} \leq C_{x}$ and ${\|{u{(\theta)}}\|} \leq C_{u}$ for all $\theta \in \Theta$ for some (unknown) ${C_{x},C_{u}} < {+ \infty}$ since both $x{(\theta)}$ and $u{(\theta)}$ are locally Lipschitz and $\Theta$ is compact by Assumption 2. Since $J_{g}$ in is an element of the conservative Jacobian of the locally Lipschitz definable function $g$, its value is almost surely equal to $\nabla g$, and it is therefore almost surely bounded above by the Lipschitz constant of $g$ on $\Theta$. The same goes for $J_{\operatorname{MPC}}$. Since $J_{x}$ and $J_{u}$ are constructed through the recursion involving bounded quantities, and the horizon $T$ of the problem is finite, $J_{x_{t}}$ and $J_{u_{t}}$ are bounded for all $t$, and therefore so are $J_{x}$ and $J_{u}$. Finally, since $C$ is Lipschitz on the set ${{C_{x}{\mathbb{B}}} \times {\mathbb{C}}_{\approxeq}}{\mathbb{B}}$, $J_{\mathcal{C}}$ is bounded. This completes the proof.

Our final technical result is about proving the finiteness of the variance of $J_{\mathcal{C}^{\delta}}$ for each $k$.

### Lemma 6.6

Under Assumptions 1 and 2, we have for all $k \in {\mathbb{N}}$ that

### Proof 6.7

The first equation is trivial since ${{\mathbb{E}}{\lbrack{{\mathbb{J}}_{{\mathbb{C}}^{\delta}}{(\theta_{\daleth},\succapprox_{\daleth})}}\rbrack}} = {{\nabla{\mathbb{C}}^{\delta}}{(\theta_{\daleth})}}$ by Lemma 5.1. Next, we have

Since $v_{k} \sim {U{({\mathbb{S}})}}$, the term on the right is always finite for finite $\theta_{k}$. Combining this with the continuity of $\|{{\nabla\mathcal{C}^{\delta}}{( \cdot )}}\|$, we conclude the existence of a function $p:{\Theta\rightarrow{\mathbb{R}}_{> \nvdash}}$ bounded on bounded sets such that ${\mathbb{E}}_{\succapprox_{\daleth}}{\lbrack \parallel {\mathbb{J}}_{{\mathbb{C}}^{\delta}}{(\theta_{\daleth})} - \nabla{\mathbb{C}}^{\delta}{(\theta_{\daleth})} \parallel^{\nvDash}\rbrack} \leq \mid {(\theta_{\daleth})}$, concluding the proof.

Proof of Theorem 6.1. We follow Section A in \[davis2020stochastic\]. Note that since $\mathcal{C}^{\delta}$ is continuously differentiable, we can take its gradient $\nabla\mathcal{C}^{\delta}$ as a conservative field. First, observe that

where ${\alpha_{k}\xi_{k}} = {{\Pi_{\Theta}{\lbrack{\theta_{k} - {\alpha_{k}{({1 - \eta_{k}})}J_{\mathcal{C}^{\delta}}{(\theta_{k},v_{k})}} - {\alpha_{k}\eta_{k}J_{\mathcal{C}}{(\theta_{k})}}}\rbrack}} - {\Pi_{\Theta}{\lbrack{\theta_{k} - {\alpha_{k}{\nabla\mathcal{C}^{\delta}}{(\theta_{k})}}}\rbrack}}}$. By leveraging the convexity of $\Theta$ and the triangle inequality, we have

Since $\mathcal{C}^{\delta}$ is Lipschitz and definable by Lemma 6.2, and both $\theta_{k} \in \Theta$ and $v_{k} \in {\mathbb{S}}$ take on finite values, there exists a constant $C_{J} > 0$ such that ${{\|{J_{\mathcal{C}}{(\theta_{k})}}\|} + {\|{J_{\mathcal{C}^{\delta}}{(\theta_{k},v_{k})}}\|}} \leq C_{J}$ for all $k \in {\mathbb{N}}$, which combined with (11b) gives ${\sum_{k \in {\mathbb{N}}}{\alpha_{k}\eta_{k}{\lbrack{{\|{J_{\mathcal{C}}{(\theta_{k})}}\|} + {\|{J_{\mathcal{C}^{\delta}}{(\theta_{k},v_{k})}}\|}}\rbrack}}} < {+ \infty}$. Next, leveraging Lemma 6.4, (11a), and the compactness of $\Theta$, we conclude that ${\sum_{k \in {\mathbb{N}}}{\alpha_{k}{\|{{J_{\mathcal{C}^{\delta}}{(\theta_{k})}} - {{\nabla\mathcal{C}^{\delta}}{(\theta_{k})}}}\|}}} < {+ \infty}$ by \[davis2020stochastic, Lemma 4.1\], as the summability condition coincides with Assumption A.4 in \[davis2020stochastic\]. This proves that ${\sum_{k \in {\mathbb{N}}}{\alpha_{k}\xi_{k}}} < {+ \infty}$. Next, letting ${G_{k}{(\theta)}} = {{- {{\nabla\mathcal{C}^{\delta}}{(\theta_{k})}}} - {\alpha_{k}^{- 1}{\lbrack{\theta - {\alpha_{k}{\nabla\mathcal{C}^{\delta}}{(\theta)}} - {\Pi_{\Theta}{\lbrack{\theta - {\alpha_{k}{\nabla\mathcal{C}^{\delta}}{(\theta)}}}\rbrack}}}\rbrack}}}$, the update in can be written as

The final argument of this proof relies on \[davis2020stochastic, Theorem 3.2\], which we will invoke to prove convergence to a critical point of. To utilize \[davis2020stochastic, Theorem 3.2\] we require all items in \[davis2020stochastic, Assumption A\] to hold true. First, observe that items 1-4 hold thanks to Assumption 2 and ${\sum_{k \in {\mathbb{N}}}{\alpha_{k}\xi_{k}}} < {+ \infty}$. It only remains to show that item 5 holds, that is, that given any unbounded subset $\mathcal{K}$ of $\mathbb{N}$ for which $\theta_{j}\rightarrow\overline{\theta}$, $j \in \mathcal{K}$, we have ${\operatorname{dist}{({{1/k}{\sum_{j = 0}^{k}g_{j}}},{G{(\overline{\theta})}})}}\rightarrow 0$, where ${G{(\overline{\theta})}} = {{- {{\nabla\mathcal{C}^{\delta}}{(\overline{\theta})}}} - {\mathcal{N}_{\Theta}{(\overline{\theta})}}}$ and ${\mathcal{C}^{\delta}{(\theta)}} = {{\mathbb{E}}_{\succapprox}{\lbrack{{\mathbb{C}}{({\theta + {\delta\succapprox}})}}\rbrack}}$. Since $G{(\overline{\theta})}$ is a convex set, we have

meaning that it suffices to show that ${\operatorname{dist}{(g_{j},{G{(\overline{\theta})}})}}\rightarrow 0$ as $j\rightarrow\infty$, $j \in \mathcal{K}$. Since for each $j$ we have ${\Pi_{\Theta}{\lbrack{\theta_{j} - {\alpha_{j}{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}}}\rbrack}} \in {\theta_{j} - {\alpha_{j}{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}} - {\mathcal{N}_{\Theta}{({\Pi_{\Theta}{\lbrack{\theta_{j} - {\alpha_{j}{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}}}\rbrack}})}}}$, we have by definition that $g_{j} = {{- {{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}}} - {\alpha_{j}^{- 1}z_{j}}}$, for some $z_{j} \in {\mathcal{N}_{\Theta}{({\Pi_{\Theta}{\lbrack{\theta_{j} - {\alpha_{j}{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}}}\rbrack}})}}$, and therefore ${g_{j} - {G{(\overline{\theta})}}} = {{{- {{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}}} - {\alpha_{j}^{- 1}z_{j}}} + {{\nabla\mathcal{C}^{\delta}}{(\overline{\theta})}} + {\mathcal{N}_{\Theta}{(\overline{\theta})}}}$. Due to the outer semicontinuity of the normal cone $\mathcal{N}_{\Theta}$ of a convex set $\Theta$, and that $\theta_{j + 1} = {\Pi_{\Theta}{\lbrack{\theta_{j} - {\alpha_{j}{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}}}\rbrack}}\rightarrow\overline{\theta}$, we have that in the limit ${\alpha_{j}^{- 1}z_{j}} \in {\mathcal{N}_{\Theta}{(\overline{\theta})}}$. Moreover, by continuity of $\nabla\mathcal{C}^{\delta}$, ${{\nabla\mathcal{C}^{\delta}}{(\theta_{j})}}\rightarrow{{\nabla\mathcal{C}^{\delta}}{(\overline{\theta})}}$. This proves that all items in \[davis2020stochastic, Assumption A\] are satisfied. Since \[davis2020stochastic, Assumption B\] is also satisfied thanks to Lemma 6.2 and \[davis2020stochastic, Theorem 5.8\], we conclude that converges to a point satisfying $0 \in {{{\nabla\mathcal{C}^{\delta}}{(\overline{\theta})}} + {\mathcal{N}_{\Theta}{(\overline{\theta})}}}$. By Lemma 5.3, this means that $0 \in {{\partial_{\delta}{\lbrack{{C{(\overline{\theta})}} + {P{(\overline{\theta})}}}\rbrack}} + {\mathcal{N}_{\Theta}{(\overline{\theta})}}}$. Since ${\bigcup_{\vartheta \in {\delta{\mathbb{B}}}}{\lbrack{{\partial_{c}{C{({\theta + \vartheta})}}} + {\partial_{c}{P{({\theta + \vartheta})}}}}\rbrack}} \subseteq {{\bigcup_{\vartheta \in {\delta{\mathbb{B}}}}{\lbrack{\partial_{c}{C{({\theta + \vartheta})}}}\rbrack}} + {\bigcup_{\vartheta \in {\delta{\mathbb{B}}}}{\lbrack{\partial_{c}{P{({\theta + \vartheta})}}}\rbrack}}}$, and this inclusion is preserved if we consider the convex hull of both sets, we have that ${\partial_{\delta}{\lbrack{{C{(\overline{\theta})}} + {P{(\overline{\theta})}}}\rbrack}} \subseteq {{\partial_{\delta}{C{(\overline{\theta})}}} + {\partial_{\delta}{P{(\overline{\theta})}}}}$, and therefore there exist ${\lambda_{0},\lambda_{1}} \geq 0$ with ${\lambda_{0} + \lambda_{1}} = 1$ such that

proving that the algorithm converges to a Goldstein Fritz-John $\delta$-critical point of. $\blacksquare$\

Under stronger assumptions on the constraint ${P{(\theta)}} = 0$ (for example the constraint qualification given in \[grimmer2025goldstein\]), one can additionally prove that any feasible solution $\overline{\theta}$ satisfies with $\lambda_{0} > 0$, that is, that $\overline{\theta}$ is a KKT point of.

## Simulation Results

We evaluate our approach on the 12-dimensional quadcopter model from \[abdulkareem2022modeling\] whose state vector comprises the position $(p_{x},p_{y},p_{z})$, velocity $(v_{x},v_{y},v_{z})$, Euler angles $(\phi,\vartheta,\psi)$, and angular velocity $(p,q,r)$ in the body frame.^11^1The code will be made available at The control inputs are the rotation speeds $\omega_{i}$ of the four rotors. The system is subject to the constraints $\omega_{i} \in {\lbrack 0,630\rbrack}$, ${v_{x},v_{y},v_{z}} \in {\lbrack{- 2},2\rbrack}$, $\phi,\vartheta$, $\psi \in {\lbrack{- {\pi/4}},{\pi/4}\rbrack}$, and ${p,q,r} \in {\lbrack{- {\pi/8}},{\pi/8}\rbrack}$. We implement with $N = 12$ and

where $x_{\text{ref}} = {({- 6},{- 3.5},0,\mathbf{0}_{9})}$ and $u_{\text{ref}}$ is the input required to maintain the drone at a hovering state. The parameter $\theta = {(p_{Q},p_{R},p_{P})}$ defines the stage cost matrices $Q = {{\operatorname{diag}{(p_{Q}^{2})}} + {10^{- 6}I}}$ and $R = {{\operatorname{diag}{(p_{R}^{2})}} + {10^{- 6}I}}$, as well as the terminal cost $P = {{LL^{\top}} + {10^{- 6}I}}$, where $L$ is a lower-triangular matrix containing the entries of $p_{P}$. To handle constraint violations, we relax the state constraints using slack variables, which are penalized using both a quadratic and a linear penalty (scaled by a factor of $25$). We model the system as linear choosing ${g{(x,u)}} = {{Ax} + {Bu}}$, where the matrices $A$ and $B$ are identified via least-squares regression on 100 closed-loop trajectories collected near the target point under a stabilizing MPC controller. In practice, if such a controller is not available, these trajectories could instead be generated by a human pilot. The upper-level cost is

where $T = 200$, $\mathcal{Q} = {\operatorname{diag}{(\mathbf{1}_{6},{0.1 \cdot \mathbf{1}_{6}})}}$, $\mathcal{R} = {0.01 \cdot I}$, and $\mathcal{P} = {\operatorname{diag}{(\mathbf{1}_{6},{10^{3} \cdot \mathbf{1}_{3}},\mathbf{1}_{3})}}$ is used to impose the terminal orientation of the drone. The penalty term is ${P{(\theta)}} = {300{\operatorname{dist}\limits_{1}{({x{(\theta)}},\mathcal{X}^{T + 1})}}}$.

We choose $\delta = 10^{- 4}$, $\alpha_{k} = {{{5 \cdot 10^{- 5}}{\log k}} + {2/{({k + 1})}^{0.75}}}$ and $\eta_{k} = {1/{({k + 1})}^{\gamma}}$, with $\gamma \in {\{ 0.25,0.5,0.75\}}$, and train for $200$ iterations starting with $Q = \mathcal{Q}$, $R = \mathcal{R}$, and $P$ obtained by solving the DARE with the identified dynamics and cost given by $\mathcal{Q}$ and $\mathcal{R}$. To isolate the contribution of each optimization component, we additionally train using the same stepsizes and initial conditions with $\eta_{k} = 1$ and $\eta_{k} = 0$. The behavior of the tracking cost and the constraint violation across iterations can be seen in Figure 1. The proposed approach demonstrates the most efficient convergence, whereas the purely model-based method exhibits rapid improvement during the initial iterations but later becomes unstable and fails to converge. The purely zeroth-order method, on the other hand, achieves consistent progress, but at a significantly slower rate. The proposed hybrid strategy benefits from fast initial transients, enabled by the model, and improved long-term convergence, supported by zeroth-order correction. Notably, smaller values of $\gamma$, corresponding to greater reliance on the model, lead to faster initial convergence, but also to more pronounced instability.

Figure 1: Tracking cost and constraint violation across iterations.

To further assess policy quality, we compare the trajectory generated by the trained controller with that obtained from tuning using the exact nonlinear model. As shown in Figure 2, the two trajectories exhibit strong qualitative agreement across all states. Quantitatively, the trained controller achieves a final cost of $1111.71$, compared to $1103.04$ for the controller optimized with perfect model knowledge. This corresponds to less than $1\%$ suboptimality, indicating that the learned parameters are nearly optimal despite using an approximate model and noisy gradients.

Figure 2: Comparison of position (left) and attitude (right) trajectories obtained with the trained controller (solid) and the controller tuned using the exact model (dash-dotted).

## Conclusions and Future Work

We introduced a policy optimization framework for MPC policies that combines model-based gradient information with zeroth-order achieving fast learning transients while guaranteeing convergence to a critical point even under imperfect models. This approach is well-suited to settings where accurate modeling is difficult, offering robustness without sacrificing efficiency. We demonstrated the effectiveness of our algorithm on a nonlinear quadcopter task, showing that it achieves near-optimal performance while outperforming purely model-based and model-free baselines. Future work will focus on strenghtening the safety guarantees of the approach.
