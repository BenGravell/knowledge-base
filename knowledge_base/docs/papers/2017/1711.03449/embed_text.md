## Introduction

Maneuvering autonomous systems in an environment with obstacles is a challenging problem that arises in a number of practical applications including robotic manipulators and trajectory planning for autonomous systems such as self-driving cars and quadcopters. In almost all of those applications, a fundamental feature is the system's ability to avoid collision with obstacles which are, for example, humans operating in the same area, other autonomous systems, or static objects such as walls.

Optimization-based trajectory planning algorithms such as Model Predictive Control (MPC) have received significant attention recently, ranging from (unmanned) aircraft to robots to autonomous cars. This can be attributed to the increase in computational resources, the availability of robust numerical algorithms for solving optimization problems, as well as MPC's ability to systematically encode system dynamics and constraints inside its formulation.

One fundamental challenge in optimization-based trajectory planning is the appropriate formulation of collision avoidance constraints, which are known to be non-convex and computationally difficult to handle in general. While a number of formulations have been proposed in the literature for dealing with collision avoidance constraints, they are typically limited by one of the following features: $(i)$ The collision avoidance constraints are approximated through linear constraint, and it is difficult to establish the approximation error; $({ii})$ Existing formulations focus on point-mass controlled objects, and are not applicable to full-dimensional objects; $({iii})$ When the obstacles are polyhedral, then the collision avoidance constraints are often reformulated using integer variables. While this reformulation is attractive for linear systems with convex constraints since in this case a mixed-integer convex optimization problem can be solved, integer variables should generally be avoided when dealing with nonlinear systems when designing real-time controllers for robotic systems.

In this paper, we focus on a *controlled object* that moves in a general $n$-dimensional space while avoiding obstacles, and propose a novel approach for modeling obstacle avoidance constraints that overcomes the aforementioned limitations. Specifically, the contributions of this paper can be summarized as follows:

We show that if the controlled object and the obstacles are described by convex sets such as polytopes or ellipsoids (or can be decomposed into a finite union of such convex sets), then the collision avoidance constraints can be exactly and non-conservatively reformulated as a set of smooth non-convex constraints. This is achieved by appropriately reformulating the *distance*-function between two convex sets using strong duality of convex optimization.

We provide a second formulation for collision avoidance based on the notion of *signed distance*, which characterizes not only the distance between two objects but also their penetration. This reformulation allows us to compute "least-intrusive" trajectories in case collisions cannot be avoided.

We demonstrate the efficacy of the proposed obstacle avoidance reformulations on a quadcopter trajectory planning problem and autonomous parking application, where the controlled vehicles must navigate in tight environments. We show that both the distance reformulation and the signed distance reformulation enable real-time path planning and find trajectories even in challenging circumstances.

Furthermore, since both our formulations allow the incorporation of system dynamics and input constraints, the generated trajectories are *kinodynamically feasible*, and hence can be tracked by simple low-level controllers.

This paper is organized as follows: Section 2 introduces the problem setup. Section 3 presents the collision avoidance and minimum-penetration formulations for the case when the controlled object is a point mass. These results are then extended to full-dimensional controlled objects in Section 4. Numerical experiments demonstrating the efficacy of the proposed method are given in Sections 5 and 6, and conclusions are drawn in Section 7. The Appendix contains auxiliary results needed to prove the main results of the paper. The source code of a quadcopter navigation example and autonomous parking example described in Sections 5 and 6 is provided at [https://github.com/XiaojingGeorgeZhang/OBCA](https://github.com/XiaojingGeorgeZhang/OBCA).

### Related Work

A large body of work exists on the topic of obstacle avoidance. In this paper, we do not review, or compare, optimization-based collision avoidance methods with alternative approaches such as those based on dynamic programming, reachability analysis, graph search, (random) sampling, or interpolating curves. Indeed, collision avoidance problems are known to be NP-hard in general, and all practical methods constitute some sort of "heuristics", whose performance depends on the specific problem and configuration at hand. In the following, we briefly review optimization-based approaches, and refer the interested reader to for a comprehensive review on existing trajectory planning and obstacle avoidance algorithms.

The basic idea in optimization-based methods is to express the collision avoidance problem as an optimal control problem, and then solve it using numerical optimization techniques. One way of dealing with obstacle avoidance is to use unconstrained optimization, in which case the objective function is augmented with "artificial potential fields" that represent the obstacles. More recently, methods based on constrained optimization has attracted attention in the control community, due to its ability to explicitly formulate collision avoidance through constraints. Broadly speaking, constrained optimization-based collision-avoidance algorithms can be divided into two cases based on the modeling of the controlled object: point-mass models and full-dimensional objects. Due to its conceptual simplicity, the vast majority of literature focuses on collision avoidance for point-mass models, and consider the shape of the controlled object by inflating the obstacles. The obstacles are generally assumed to be either polytopes or ellipsoids. For polyhedral obstacles, disjunctive programming can be used to ensure collision avoidance, which is often reformulated as a mixed-integer optimization problem. In case of ellipsoidal obstacles, the collision avoidance constraints can be formulated as a smooth non-convex constraint, and the resulting optimization problem can be solved using generic non-linear programming solvers.

The case of full-dimensional controlled objects has, to be best of the authors' knowledge, not been widely studied in the context of optimization-based methods, with the exception of. In, the authors model the controlled object through its vertices and, under the assumption that all involved object are rectangles, ensure collision avoidance by keeping all vertices of the controlled object outside the obstacle. A more general way of handling collision avoidance for full-dimensional controlled object has been proposed in using the notion of signed distance, where the authors also propose a sequential linearization technique to deal with the non-convexity of the signed distance function.

The approach most closely related to our formulation is probably the work of, where the authors propose a smooth reformulation of the collision avoidance constraint for point-mass controlled objects and polyhedral obstacles. However, our approach differs from as $(i)$ our approach generalizes to full-dimensional controlled objects, and $({ii})$ we are, based on the notion of penetration, also able to compute least-intrusive trajectories in case collisions cannot be avoided.

### Notation

Given a proper cone $\mathcal{K} \subset {\mathbb{R}}^{l}$ and two vectors ${a,b} \in {\mathbb{R}}^{l}$, then $a \preceq_{\mathcal{K}}b$ is equivalent to ${({b - a})} \in \mathcal{K}$. If $\mathcal{K} = {\mathbb{R}}_{+}^{l}$ is the standard cone, then $\preceq_{{\mathbb{R}}_{+}^{l}}$ is equivalent to the standard (element-wise) inequality $\leq$. Moreover, $\parallel \cdot \parallel_{\ast}$ is the dual norm of $\parallel \cdot \parallel$, and $\mathcal{K}^{\ast} \subset {\mathbb{R}}^{l}$ is the dual cone of $\mathcal{K}$. The "space" occupied by the controlled object (e.g., a drone, vehicle, or robot in general) is denoted as ${\mathbb{E}} \subset {\mathbb{R}}^{n}$; similarly, the space occupied by the obstacles is denoted as ${\mathbb{O}} \subset {\mathbb{R}}^{n}$.

## Problem Description

### Dynamics, Objective and Constraints

We assume that the dynamics of the controlled object takes the form

where $x_{k} \in {\mathbb{R}}^{n_{x}}$ is the state of the controlled object at time step $k$ given an initial state $x_{0} = x_{S}$, $u_{k} \in {\mathbb{R}}^{n_{u}}$ is the control input, and $f:{{{\mathbb{R}}^{n_{x}} \times {\mathbb{R}}^{n_{u}}}\rightarrow{\mathbb{R}}^{n_{x}}}$ describes the dynamics of the system. In most cases, the state $x_{k}$ contains information such as the position $p_{k} \in {\mathbb{R}}^{n}$ and angles $\theta_{k} \in {\mathbb{R}}^{n}$ of the controlled object, as well the velocities ${\overset{˙}{p}}_{k}$ and angular rates ${\overset{˙}{\theta}}_{k}$. In this paper, we assume that no disturbance is present, and that the system is subject to input and state constraints of the form

where $h:{{{\mathbb{R}}^{n_{x}} \times {\mathbb{R}}^{n_{u}}}\rightarrow{\mathbb{R}}^{n_{h}}}$, $n_{h}$ is the number of constraints, and the inequality in is interpreted element-wise. Our goal is to find a control sequence, over a horizon $N$, which allows the controlled object to navigate from the initial state $x_{S}$ to its final state $x_{F} \in {\mathbb{R}}^{n_{x}}$, while optimizing some objective function $J = {\sum_{k = 0}^{N}{\ell{(x_{k},u_{k})}}}$, where $\ell:{{{\mathbb{R}}^{n_{x}} \times {\mathbb{R}}^{n_{u}}}\rightarrow{\mathbb{R}}}$ is a stage cost, and avoiding $M \geq 1$ obstacles ${{\mathbb{O}}^{},{\mathbb{O}}^{},\ldots,{\mathbb{O}}^{(M)}} \subset {\mathbb{R}}^{n}$. Throughout this paper, we assume that the functions $f{( \cdot, \cdot )}$, $h{( \cdot, \cdot )}$ and $\ell{( \cdot, \cdot )}$ are smooth. Smoothness is assumed for simplicity, although all forthcoming statements apply equally to cases when those functions are twice continuously differentiable.

### Obstacle and Controlled Object Modeling

Given the state $x_{k}$, we denote by ${{\mathbb{E}}{(x_{k})}} \subset {\mathbb{R}}^{n}$ the "space" occupied by the controlled object at time $k$, which we assume is a subset of ${\mathbb{R}}^{n}$. The collision avoidance constraint at time $k$ is now given by^11^1In this paper, we only consider collision avoidance constraints that are associated with the position and geometric shape of the controlled object, which are typically defined by its position $p_{k}$ and angles $\theta_{k}$. This is not a restriction of the theory as the forthcoming approaches can be easily generalized to collision avoidance involving other states, but done to simplify exposition of the material.

Constraint is non-differentiable in general, e.g., when the obstacles are polytopic. In this paper, we will remodel in such a way that both continuity and differentiability are preserved. To this end, we assume that the obstacles ${\mathbb{O}}^{(m)}$ are convex compact sets with non-empty relative interior^22^2Non-convex obstacles can often be approximated/decomposed as the union of convex obstacles, and can be represented as

where $A^{(m)} \in {\mathbb{R}}^{l \times n}$, $b^{(m)} \in {\mathbb{R}}^{l}$, and $\mathcal{K} \subset {\mathbb{R}}^{l}$ is a closed convex pointed cone with non-empty interior. Representation is entirely generic since any compact convex set admits a conic representation of the form \[40, p.15\]. In particular, polyhedral obstacles can be represented as by choosing $\mathcal{K} = {\mathbb{R}}_{+}^{l}$; in this case $\preceq_{\mathcal{K}}$ corresponds to the well-known element-wise inequality $\leq$. Likewise, ellipsoidal obstacles can be represented by letting $\mathcal{K}$ be the second-order cone, see for details. To simplify the upcoming exposition, the same cone $\mathcal{K}$ is assumed for all obstacles; the extension to obstacle-specific cones $\mathcal{K}^{(m)}$ is straight-forward.

In this paper, we will consider controlled objects ${\mathbb{E}}{(x_{k})}$ that are modeled as *point-masses* as well as *full-dimensional* objects. In the former case, ${\mathbb{E}}{(x_{k})}$ simply extracts the position $p_{k}$ from the state $x_{k}$, i.e.,

### Optimal Control Problem with Collision Avoidance

By combining --, the constrained finite-horizon optimal control problem with collision avoidance constraint is given by

where ${\mathbb{E}}{(x_{k})}$ is either given by (5a) (point-mass model) or (5b) (full-dimensional set), $\mathbf{x}:={\lbrack x_{0},x_{1},\ldots,x_{N + 1}\rbrack}$ is the collection of all states, and $\mathbf{u}:={\lbrack u_{0},u_{1},\ldots,u_{N}\rbrack}$ is the collection of all inputs. A key difficulty in solving problem, even for linear systems with convex objective function and convex state/input constraints, is the presence of the collision-avoidance constraints ${{{\mathbb{E}}{(x_{k})}} \cap {\mathbb{O}}^{(m)}} = \varnothing$, which in general are non-convex and non-differentiable. In the following, we present two novel approaches for modeling collision avoidance constraints that preserve continuity and differentiability, and are amendable for use with existing off-the-shelf gradient- and Hessian-based optimization algorithms.

### Collision Avoidance

A popular way of formulating collision avoidance is based on the notion of *signed distance*

where $\text{dist}{( \cdot, \cdot )}$ and $\text{pen}{( \cdot, \cdot )}$ are the distance and penetration function, and are defined as

$\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}$ ${:={\min\limits_{t}{\{{{\| t\|}:{{\left( {{{\mathbb{E}}{(x)}} + t} \right) \cap {\mathbb{O}}} \neq \varnothing}}\}}}},$ (8a)
$\text{pen}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}$ ${:={\min\limits_{t}{\{{{\| t\|}:{{\left( {{{\mathbb{E}}{(x)}} + t} \right) \cap {\mathbb{O}}} = \varnothing}}\}}}}.$ (8b)

Roughly speaking, the signed distance is positive if ${\mathbb{E}}{(x)}$ and $\mathbb{O}$ do not intersect, and negative if they overlap. Therefore, collision avoidance can be ensured by requiring ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > 0$. Unfortunately, directly enforcing ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > 0$ inside the optimization problem is generally difficult since it is non-convex and non-differentiable in general. Furthermore, for optimization algorithms to be numerically efficient, they require an explicit representation of the functions they are dealing with, in this case $\text{sd}{( \cdot, \cdot )}$. This, however, is difficult to obtain in practice since $\text{sd}{( \cdot, \cdot )}$ itself is the solution of the optimization problems (8a) and (8b). As a result, existing algorithms approximate through local linearization, for which it is difficult to establish bounds on approximation errors.

In the following, we propose two reformulation techniques for obstacles avoidance that overcome the issues of non-differentiability and that do not require an explicit representation of the signed distance. We begin with point-mass models in Section 3, and treat the general case of full-dimensional controlled objects in Section 4.

## Collision Avoidance for Point-Mass Models

In this section, we first present a smooth reformulation of when ${{\mathbb{E}}{(x_{k})}} = p_{k}$ in Section 3.1, and then extend the approach in Section 3.2 to generate minimum-penetration trajectories in case collisions cannot be avoided. To simplify notation, the time indices $k$ are omitted in the remainder of this section.

### Collision-Free Trajectory Generation

### Proposition 1

Assume that the obstacle $\mathbb{O}$ and the controlled object are given as in and (5a), respectively, and let $\mathsf{d}_{\text{min}} \geq 0$ be a desired safety margin between the controlled object and the obstacle. Then we have:

### Proof

It follows from and (8a) that ${\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {\min_{t}{\{{{\| t\|}:{{A{({{{\mathbb{E}}{(x)}} + t})}} \preceq_{\mathcal{K}}b}}\}}}$. Following \[41, p.401\], its dual problem is given by $\max_{\lambda}\left\{ {{{({{A{\mathbb{E}}{(x)}} - b})}^{\top}\lambda}:{{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1},{\lambda \succeq_{\mathcal{K}^{\ast}}0}}} \right\}$, where $\parallel \cdot \parallel_{\ast}$ is the dual norm associated to $\parallel \cdot \parallel$ and $\mathcal{K}^{\ast}$ is the dual cone of $\mathcal{K}$. Since $\mathbb{O}$ is assumed to have non-empty relative interior, strong duality holds, and ${\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {\max_{\lambda}\left\{ {{{({{A{\mathbb{E}}{(x)}} - b})}^{\top}\lambda}:{{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1},{\lambda \succeq_{\mathcal{K}^{\ast}}0}}} \right\}}$. Hence, for any non-negative scalar $\mathsf{d}_{\text{min}}$, ${\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > \mathsf{d}_{\text{min}}$ is satisfied if, and only if, there exists ${\lambda \succeq_{\mathcal{K}^{\ast}}0}:{{{{({{A{\mathbb{E}}{(x)}} - b})}^{\top}\lambda} > \mathsf{d}_{\text{min}}},{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1}}$. The desired result follows from identity (5a). ∎

Intuitively speaking, any variable $\lambda$ satisfying the right-hand-side of is a certificate verifying the condition ${\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > \mathsf{d}_{\text{min}}$. Since ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} = \varnothing$ is equivalent to ${\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > 0$, the optimal control problem for the point-mass model (5a) is given by

where $p_{k}$ is the position of the controlled object at time $k$, $\lambda_{k}^{(m)}$ is the dual variable associated with obstacle ${\mathbb{O}}^{(m)}$ at time step $k$, and the optimization is performed over the states $\mathbf{x}$, the inputs $\mathbf{u}$ and the dual variables ${\mathbf{λ}} = {\lbrack\lambda_{0}^{},\ldots,\lambda_{0}^{(m)},\lambda_{1}^{},\ldots,\lambda_{N}^{(m)}\rbrack}$. We emphasize that is an *exact* reformulation of and that the optimal trajectory $\mathbf{x}^{\ast} = {\lbrack x_{0}^{\ast},x_{1}^{\ast},\ldots,x_{N}^{\ast}\rbrack}$ obtained by solving is *kinodynamically feasible*.

### Remark 1

Without further assumptions on the norm $\parallel \cdot \parallel$ and the cone $\mathcal{K}$, the last two constraints in are not guaranteed to be smooth, a property that many general-purpose non-linear optimization algorithms require^33^3Strictly speaking, these solvers often require the cost function and constraints to be twice continuously differentiable only. Smoothness is assumed in this paper for the sake of simplicity.. Fortunately, it turns out that these constraints are smooth for the practically relevant cases of $\parallel \cdot \parallel$ being the Euclidean distance and $\mathcal{K}$ either the standard cone or the second-order cone, which allows us to model polyhedral and ellipsoidal obstacles. In these cases, and under the assumption that the functions $f{( \cdot, \cdot )}$, $h{( \cdot, \cdot )}$ and $\ell{( \cdot, \cdot )}$ are smooth, is a smooth nonlinear optimization problem that is amendable to general-purpose non-linear optimization algorithms such as IPOPT. Without going into details, we point out that smoothness is retained when $\parallel \cdot \parallel = \parallel \cdot \parallel_{p}$ is a general $p$-norm, with $p \in {(1,\infty)}$, and $\mathcal{K}$ is the cartesian product of $p$-order cones $\mathcal{K}_{p}:={\{{(s,z)}:{{\| z\|}_{p} \leq s}\}}$, with $p \in {(1,\infty)}$. In this case, the dual norm is given by $\parallel \cdot \parallel_{\ast} = \parallel \cdot \parallel_{q}$ and the dual cone is ${(\mathcal{K}_{p})}^{\ast} = \mathcal{K}_{q}$, where $q$ satisfies ${{1/p} + {1/q}} = 1$, see for details on dual norms and dual cones.

While reformulation can be used for obstacle avoidance, it is limited to finding collision-free trajectories. Indeed, in case collisions cannot be avoided, the above formulation is not able to find "least-intrusive" trajectories by softening the constraints. Intuitively speaking, this is because is based on the notion of distance, and the distance between two overlapping objects (as is in the case of collision), is always zero, regardless of the penetration. From a practical point of view, this implies that slack variables cannot be included in the constraints of, because the optimal control problem is not able to distinguish between "severe" and "less severe" colliding trajectories. Furthermore, in practice, it is often desirable to soften constraints and include slack variables to ensure feasibility of the (non-convex) optimization problem, since (local) infeasibilities in non-convex optimization problem are known to cause numerical difficulties. In the following, we show how the above limitations can be overcome by considering the notion of penetration and softening the collision avoidance constraints.

### Minimum-Penetration Trajectory Generation

In this section, we consider the design of *minimum-penetration* trajectories for cases when collision cannot be avoided and the goal is to find a "least-intrusive" trajectory. Following the literature, we measure "intrusion" in terms of *penetration* as defined in (8b).

### Proposition 2

Assume that the obstacle $\mathbb{O}$ and controlled object are given as in and (5a), respectively, and let $\mathsf{p}_{\text{max}} \geq 0$ be a desired maximum penetration of the controlled object and the obstacle. Then we have:

### Proof

The proof, along with auxiliary lemmas, is given in the Appendix. ∎

Proposition 2 resembles Proposition 1 with the difference that the convex inequality constraint ${\|{A^{\top}\lambda}\|}_{\ast} \leq 1$ is replaced with the non-convex equality constraint ${\|{A^{\top}\lambda}\|}_{\ast} = 1$. In the following, we will see that Propositions 1 and 2 can be combined to represent the *signed distance* as defined in.

### Theorem 1

Assume that the obstacle $\mathbb{O}$ and the controlled object are given as in and (5a), respectively. Then, for any $\mathsf{d} \in {\mathbb{R}}$, we have:

### Proof

By definition, ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}}$ if ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} = \varnothing$, and ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {- {\text{pen}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}}}$ if ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} \neq \varnothing$. Let ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} \neq \varnothing$, in which case follows directly from. If ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} = \varnothing$, then we have from that ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > \mathsf{d}$ is equivalent to ${{\exists\lambda} \succeq_{\mathcal{K}^{\ast}}0}:{{{{({{Ap} - b})}^{\top}\lambda} > \mathsf{d}},{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1}}$. Due to homogeneity with respect to $\lambda$, if the previous condition is satisfied, then there always exists a (scaled) dual multiplier $\lambda^{\prime} \succeq_{\mathcal{K}^{\ast}}0$ such that ${{{({{Ap} - b})}^{\top}\lambda^{\prime}} > \mathsf{d}},{{\|{A^{\top}\lambda^{\prime}}\|}_{\ast} = 1}$. This concludes the proof. ∎

Reformulation is similar to reformulation, with the difference that holds for all $\mathsf{d} \in {\mathbb{R}}$, while only holds for $\mathsf{d} \geq 0$. The "price" we pay for this generalization is that the convex constraint ${\|{A^{\top}\lambda}\|}_{\ast} \leq 1$ is turned into the non-convex equality constraint ${\|{A^{\top}\lambda}\|}_{\ast} = 1$ which, as we will see later on, generally results in longer computation times. Nevertheless, Theorem 1 allows us to compute trajectories of least penetration whenever collision cannot be avoided by solving the following soft-constrained *minimum-penetration* problem:

where $p_{k}$ is the position of the controlled object at time $k$, $s_{k}^{(m)} \in {\mathbb{R}}_{+}$ is the slack variable associated to the object ${\mathbb{O}}^{(m)}$ at time step $k$, and $\kappa \geq 0$ is a weight factor that keeps the slack variable as close to zero as possible. Without going into details, we point out that the weight $\kappa$ should be chosen "big enough" such that the slack variables only become active when the original problem is infeasible, i.e., when obstacle avoidance is not possible. Notice that a positive slack variable implies a colliding trajectory, where the penetration depth is given by $s_{k}^{(m)}$. We close this section by pointing out that if, a priori, it is known that a collision-free trajectory can be generated, then formulation should be given preference over formulation because the former has fewer decision variables, and because the constraint ${\|{{}_{}^{(m)}\lambda_{k}^{(m)}}\|}_{\ast} \leq 1$ is convex, which generally leads to improved solution times. Smoothness of is ensured if $\parallel \cdot \parallel$ is the Euclidean distance, and $\mathcal{K}$ is either the standard cone or the second-order cone, see Remark 1 for details.

## Collision Avoidance for Full-Dimension Controlled Objects

The previous section provided a framework for computing collision-free and minimum-penetration trajectories for controlled objects that are described by point-mass models. While such models can be used to generate trajectories for "ball-shaped" controlled objects, done by setting the minimum distance $d_{\min}$ equal to the radius of the controlled object (see Section 5 for such an example), it can be restrictive in other cases. For example, modeling a car in a parking lot as a Euclidean ball can be very conservative, and prevent the car from finding a parking spot. To alleviate this issue, we show in this section how the results of Section 3 can be extended to full-dimensional controlled objects.

### Collision-Free Trajectory Generation

Similar to Section 3, we begin by first reformulating the distance function, which will allow us to generate collision-free trajectories:

### Proposition 3

Assume that the controlled object and the obstacle are given as in (5b) and, respectively, and let $\mathsf{d}_{\text{min}} \geq 0$ be a desired safety margin. Then we have:

### Proof

Recall that ${\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {\min_{e,o}{\{{{\|{e - o}\|}:{{{Ao} \preceq_{\mathcal{K}}b},{e \in {{\mathbb{E}}{(x)}}}}}\}}} = {\min_{e^{\prime},o}{\{{{\|{{{R{(x)}e^{\prime}} + {t{(x)}}} - o}\|}:{{{Ao} \preceq_{\mathcal{K}}b},{{Ge^{\prime}} \preceq_{\overline{\mathcal{K}}}g}}}\}}}$, where the last equality follows from (5b). The dual of this minimization problem is given by $\max_{\lambda,\mu}{\{{{{- {g^{\top}\mu}} + {{({{At{(x)}} - b})}^{\top}\lambda}}:{{{{G^{\top}\mu} + {R{(x)}^{\top}A^{\top}\lambda}} = 0},{{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1},{{\lambda \succeq_{\mathcal{K}^{\ast}}0},{\mu \succeq_{{\overline{\mathcal{K}}}^{\star}}0}}}}}\}}$, see e.g., \[41, Section 8.2\] for the derivation, where $\parallel \cdot \parallel_{\ast}$ is the dual norm, and $\mathcal{K}^{\ast}$ and ${\overline{\mathcal{K}}}^{\star}$ are the dual cones of $\mathcal{K}$ and $\overline{\mathcal{K}}$, respectively. Since $\mathbb{O}$ and $\mathbb{B}$ are assumed to have non-empty relative interior, strong duality holds, and ${{\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > \mathsf{d}_{\min}}\Leftrightarrow{{\max_{\lambda,\mu}{\{{{{- {g^{\top}\mu}} + {{({{At{(x)}} - b})}^{\top}\lambda}}:{{{{G^{\top}\mu} + {R{(x)}^{\top}A^{\top}\lambda}} = 0},{{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1},{{\lambda \succeq_{\mathcal{K}^{\ast}}0},{\mu \succeq_{{\overline{\mathcal{K}}}^{\star}}0}}}}}\}}} > \mathsf{d}_{\min}}\Leftrightarrow{{{\exists\lambda} \succeq_{\mathcal{K}^{\ast}}0},{\mu \succeq_{{\overline{\mathcal{K}}}^{\ast}}0}}:{{{{- {g^{\top}\mu}} + {{({{At{(x)}} - b})}^{\top}\lambda}} > \mathsf{d}_{\min}},{{{{G^{\top}\mu} + {R{(x)}^{\top}A^{\top}\lambda}} = 0},{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1}}}$. ∎

Compared to Proposition 1, we see that full-dimensional controlled objects require the introduction of the additional dual variables $\mu^{(m)}$, one for each obstacle ${\mathbb{O}}^{(m)}$. By setting $\mathsf{d}_{\text{min}} = 0$, we obtain now the following reformulation of for full-dimensional objects:

where $\lambda_{k}^{(m)}$ and $\mu_{k}^{(m)}$ are the dual variables associated with the obstacle ${\mathbb{O}}^{(m)}$ at step $k$, $\mathbf{λ}$ and $\mathbf{μ}$ are the collection of all $\lambda_{k}^{(m)}$ and $\mu_{k}^{(m)}$, respectively, and the optimization is performed over $(\mathbf{x},\mathbf{u},{\mathbf{λ}},{\mathbf{μ}})$. Notice that is an *exact* reformulation of. Smoothness of is ensured if $\parallel \cdot \parallel$ is the Euclidean distance, and $\mathcal{K}$ and $\overline{\mathcal{K}}$ are either the standard cone or the second-order cone, see also Remark 1 for details.

Similar to the point-mass case in Section 3.1, the optimal control problem is able to generate collision-free trajectories, but unable to find "least-intrusive" trajectories in case collision-free trajectories do not exist. This limitation is addressed next.

### Minimum-Penetration Trajectory Generation

We overcome the above limitation by considering again the notion of penetration. We begin with the following result:

### Proposition 4

Assume that the obstacles and controlled object are given as in and (5b), respectively, and let $\mathsf{p}_{\text{max}} \geq 0$ be a maximal penetration depth. Then we have:

### Proof

It follows from that ${\text{pen}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {\text{pen}{(0,{{\mathbb{O}} - {{\mathbb{E}}{(x)}}})}}$, where ${{\mathbb{O}} - {{\mathbb{E}}{(x)}}}:={\{{o - e}:{{o \in {\mathbb{O}}},{e \in {{\mathbb{E}}{(x)}}}}\}}$ is the Minkowski difference. Furthermore, we have from the proof of Proposition 2 that ${\text{pen}{(0,{{\mathbb{O}} - {{\mathbb{E}}{(x)}}})}} = {\inf_{\{ z:{{\| z\|}_{\ast} = 1}\}}{\{{\max_{y \in {{\mathbb{O}} - {{\mathbb{E}}{(x)}}}}{\{{y^{\top}z}\}}}\}}}$. Using strong duality of convex optimization, we can dualize the inner maximization problem as ${\max_{{o \in {\mathbb{O}}},{e \in {{\mathbb{E}}{(x)}}}}{\{{z^{\top}{({o - e})}}\}}} = {\max_{{o \in {\mathbb{O}}},{e^{\prime} \in {\mathbb{B}}}}{\{{z^{\top}{({o - {R{(x)}e^{\prime}} - {t{(x)}}})}}\}}} = {\min_{\lambda,\mu}{\{{{{{{b^{\top}\lambda} + {g^{\top}\mu}} - {z^{\top}t{(x)}}}:{{{A^{\top}\lambda} = z},{{G^{\top}\mu} = {- {R^{\top}z}}}}}:{{\lambda \succeq_{K^{\ast}}0},{\mu \succeq_{{\overline{\mathcal{K}}}^{\ast}}0}}}\}}}$. Hence, ${\text{pen}{(0,{{\mathbb{O}} - {{\mathbb{E}}{(x)}}})}} = {\inf_{z,\lambda,\mu}{\{{{{b^{\top}\lambda} + {g^{\top}\mu}} - {z^{\top}t{(x)}}}:{{{A^{\top}\lambda} = z},{{{G^{\top}\mu} = {- {R^{\top}z}}},{{\| z\|}_{\ast} = 1}}}\}}}$. Eliminating the $z$-variable using the first equality constraint and following the steps of the proof of Proposition 2 gives the desired result. ∎

The following theorem shows that Propositions 3 and 4 can be combined to represent the *signed distance* function.

### Theorem 2

Assume that the obstacles and controlled object are given as in and (5b), respectively. Then, for any $\mathsf{d} \in {\mathbb{R}}$, we have:

### Proof

By definition, ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {\text{dist}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}}$ if ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} = \varnothing$, and ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} = {- {\text{pen}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}}}$ if ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} \neq \varnothing$. Consider now ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} \neq \varnothing$, in which case follows directly from. Assume now that ${{{\mathbb{E}}{(x)}} \cap {\mathbb{O}}} = \varnothing$; then we have from that ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > \mathsf{d}$ is equivalent to ${{{\exists\lambda} \succeq_{\mathcal{K}^{\ast}}0},{\mu \succeq_{{\overline{\mathcal{K}}}^{\ast}}0}}:{{{{- {g^{\top}\mu}} + {{({{At{(x)}} - b})}^{\top}\lambda}} > \mathsf{d}},{{{{G^{\top}\mu} + {R{(x)}^{\top}A^{\top}\lambda}} = 0},{{\|{A^{\top}\lambda}\|}_{\ast} \leq 1}}}$. Due to homogeneity with respect to $\lambda$ and $\mu$, if the previous condition is satisfied, then there also exists a $\lambda^{\prime} \succeq_{\mathcal{K}^{\ast}}0$ and $\mu^{\prime} \succeq_{{\overline{K}}^{\ast}}0$ such that ${{{- {g^{\top}\mu}} + {{({{At{(x)}} - b})}^{\top}\lambda}} > \mathsf{d}},{{{{G^{\top}\mu} + {R{(x)}^{\top}A^{\top}\lambda}} = 0},{{\|{A^{\top}\lambda}\|}_{\ast} = 1}}$. This concludes the proof. ∎

Theorem 2 allows us to formulate the following soft-constrained *minimum-penetration* optimal control problem

where $s_{k}^{(m)} \in {\mathbb{R}}_{+}$ is the slack variable associated to obstacle ${\mathbb{O}}^{(m)}$ at time step $k$, and $\kappa \geq 0$ is a weight factor that keeps the slack variable as small as possible. Smoothness of is ensured if $\parallel \cdot \parallel$ is the Euclidean distance, and $\mathcal{K}$ and $\overline{\mathcal{K}}$ are either the standard cone or the second-order cone, see Remark 1 for details.

In the following sections, we illustrate our obstacle avoidance formulation on two applications: a quadcopter path planning problem where the point-mass formulation is used (Section 5), and an automated parking problem, where the full-dimensional obstacle avoidance problem formulation is used (Section 6).

## Example 1: Quadcopter Path Planning

In this section, we illustrate reformulations and on a quadcopter navigation problem, where the quadcopter must find a path from one end of the room to the other end, while avoiding a low-hanging wall and passing through a small window hole, see Fig. 1.

Figure 1: Setup of quadcopter example together with a (locally optimal) point-to-point trajectory. The start position is behind the blue wall at X = 1, and the end position in front of red wall at X = 9. The quadcopter needs to fly below the blue wall and pass through a window in the red wall, see https://youtu.be/7WLNJhaHcoQ for an animation. The black circles illustrate the safety distance dmin = 0.25 m which models the shape of the quadcopter.

### Environment and Obstacle Modeling

The size of the room is $10.5 \times 10.5 \times 5.5$ m, and we see from Fig. 1 that the direct path between the start and end position is blocked by two obstacles. The first obstacle, a low-hanging wall, blocks the entire upper part of the room, and can only be passed from below. The second obstacle, another wall, blocks the entire room, but has a small window through which the quadcopter must pass to reach its target position. We approximate the shape of the quadcopter by a (Euclidean) sphere of radius 0.25 m. In the framework of and, the shape of the quadcopter can be taken into account by requiring a safety distance of $\mathsf{d}_{\text{min}} = 0.25$ m.

The first wall, which can only be passed from below, is placed at $X$ = 2 m, and the passage below is 0.85 m high. The second wall is placed at $X$ = 7 m, and the window (size $1 \times 1$m) is placed in the middle of the second wall at a height of $Z = 2.5$ m. Finally the depth of both walls is 0.5 m. This obstacle formation can be formally formulated using five axis-aligned rectangles, where the first obstacle is represented by one such rectangle and the window can be modeled as the union of four rectangles, see Fig. 1. The collision avoidance constraints with respect to the four outer walls of the room are achieved by appropriately upper- and lower-bounding the ${(X,Y,Z)} -$coordinates of the quadcopter.

### Quadcopter Model

We consider the standard quadcopter model as used in, which is derived by finding the equation of motion of the center of gravity (CoG) and summarized next. In this model, $X,Y,Z$ denote the position of the CoG in the world frame, and we use the $Z$-$X$-$Y$ Euler angles do describe the rotation of the quadcopter, where $\phi$ is the pitch angle, $\theta$ is the roll angle, and $\psi$ is the yaw angle. The rotation matrix that translates from the world to the body frame, which is defined with respect to the CoG, is hence given by

where $s_{\phi}:={\sin{(\phi)}}$ and $c_{\phi}:={\cos{(\phi)}}$. The accelerations of the CoG can be derived by considering the sum of the forces produced by the four rotors $F_{i}$ which point in positive z-direction in the body frame, and the gravity force which acts on the negative z-direction in the world frame, resulting in the following equation of motion,

\end{bmatrix}} = {\begin{bmatrix}
\end{bmatrix} + {R_{WB}\begin{bmatrix}
where $m$ is the mass of the quadcopter and $\overset{¨}{X}$, $\overset{¨}{Y}$ and $\overset{¨}{Z}$ are the second time derivatives of $X$, $Y$ and $Z$, respectively. The attitude dynamics of the quadcopter is derived in the body rates $p$, $q$, and $r$ which are related to the Euler angles through the following rotation matrix,

\end{bmatrix} = {\begin{bmatrix}
{s_{\theta}t_{\phi}} & 1 & {- {c_{\theta}t_{\phi}}} \\
{- {s_{\theta}/c_{\phi}}} & 0 & {c_{\theta}/c_{\phi}}
\end{bmatrix}\begin{bmatrix}
The body rates are given by the following equation of motion, which is driven by the four rotor forces $F_{i}$, as well as the corresponding moments $M_{i}$ and has the following form,

\end{bmatrix}} = {\begin{bmatrix}
\end{bmatrix} - {{\begin{bmatrix}
\end{bmatrix} \times I}\begin{bmatrix}
where $I$ is the inertia matrix which in our case is diagonal and $L$ is the distance from the CoG to the rotor. The rotor forces and moments depend quadratically on the motor speed $\omega_{i}$, which are the control inputs and are defined as follows,

where, $k_{F}$ and $k_{M}$ are constants depending on the rotor blades. Hence, the state of the quadcopter is $x = {\lbrack X,Y,Z,\phi,\theta,\psi,\overset{˙}{X},\overset{˙}{Y},\overset{˙}{Z},p,q,r\rbrack}$ and the inputs are the four rotor speeds $u = {\lbrack\omega_{1},\omega_{2},\omega_{3},\omega_{4}\rbrack}$.

The parameters of the model, as well as the bounds on the inputs, are taken from, which corresponds to a quadcopter which weighs 0.5 kg and has a diameter of half a meter. Bounds on the angles, velocities and body rates are considered, and the dynamics can be brought into the form using a (forward) Euler discretization, such that $x_{k + 1} = {x_{k} + {T_{\text{opt}}\overset{\sim}{f}{(x_{k},u_{k})}}}$, where $T_{\text{opt}}$ is the sampling time, and $\overset{\sim}{f}{( \cdot, \cdot )}$ is the continuous-time dynamics that can be obtained from (19a)--(19d).

### Cost function

Our control objective is to navigate the quadcopter as fast as possible, while avoiding excessive control inputs. We combine these competing goals as a weighted sum of the form $J = {{q\tau_{F}} + {\sum_{k = 0}^{N - 1}{u_{k}^{T}Ru_{k}}}}$, where $\tau_{F}$ is the final time and $R = R^{\top} \succeq 0$, and $q \geq 0$ are weighting factors. Motivated by, we do not directly minimize $\tau_{F}$; instead, observing that $\tau_{F} = {NT_{\text{opt}}}$, we will treat the discretization time $T_{\text{opt}}$ as a decision variable. This allows the use of the slightly modified cost function

which will be used in the numerical simulations later on.

Treating $T_{\text{opt}}$ as an optimization variable has the additional benefit that the duration of the maneuver does not need to be fixed a priori, allowing us to avoid feasibility issues caused by a too short maneuver lengths. We point out that having $T_{\text{opt}}$ as a decision variable comes at the cost of introducing an additional decision variable $T_{\text{opt}}$, which renders the dynamics "more non-linear", which can be seen when looking at the Euler discretization in the previous section.

### Choice of Initial Guess

Recall that and are non-convex optimization problems, and hence computationally challenging to solve in general. In practice, one has to content oneself with a locally optimal solution that, for instance, satisfied the Karush-Kuhn-Tucker (KKT) conditions, since most numerical solvers operate locally. Furthermore, it is well-known that the solution quality critically depends on the initial guess ("warm starting point") that is provided to the solvers, and that different initial guesses can lead to different (local) optima. Unfortunately, computing a good initial guess is often difficult and highly problem dependent; ideally, the initial guess should be obstacle-free and approximately satisfy the system dynamics.

For the quadcopter example, we have observed that the well-known A^⋆^ algorithm is able to provide good initial guesses. A^⋆^ is a graph search algorithm that is able to find obstacle-free paths by gridding the position space. It is similar to Dijkstra's algorithm, but uses a so-called heuristic function to perform a "best-first" search, see for details. In our quadcopter example, we use the A^⋆^ algorithm to find an obstacle-free path in the position space, which we use to initialize the states that correspond to the quadcopter's position. The remaining states are initialized with zero, while inputs are initialized with the steady state input that keeps the quadcopter in a hoovering position. The dual variables $\lambda_{k}^{(m)}$ are initialized with 0.05, and the discretization time $T_{\text{opt}}$ with 0.25. Fig. 2 depicts the initial guess used to generate the trajectory shown in Fig. 1. Notice that, due to gridding, the path in Fig. 2 exhibits a zigzag pattern.

Figure 2: A sample warm start trajectory, obtained from the A⋆ algorithm, is shown. Notice that this trajectory avoids obstacles but does not satisfy the dynamic constraints of the quadcopter, which will be “corrected” by solving and. The black tube is the safety distance dmin which is used to represent the shape of the quadcopter.

### Simulation Results

To verify the performance and robustness of our approach, we considered 36 path planning scenarios, each starting and ending in a hovering position. The starting point is always located at ${(X,Y,Z)} = {}$ m, and the finishing point is always located behind the wall with the window at $X = 9$ m, but with varying $Y$ and $Z$ coordinates. The final positions are generated by gridding the $(Y,Z)$ space with nine points in the $Y$ direction and four points in the $Z$ direction as shown in Fig. 3. We tested both the distance formulation as well as the signed distance formulation. The horizon $N$ equals the number of steps performed by the $A^{\star}$ algorithm, and takes values between 100 and 129 for the given setup and a grid size of 0.1 m. The sampling time $T_{\text{opt}}$ is restricted to lie between $0.125$ s and $0.375$ s. The optimization problems are implemented with the modeling toolbox JuMP in the programming language Julia, and solved using the general purpose nonlinear solver IPOPT. The problems are solved on a 2013 MacBook Pro with an i7 processor clocked at 2.6 GHz.

Table 1 lists the minimum, maximum and average computation time of the A^⋆^ algorithm, and the time required to solve problems and. Fig. 3 reports the solution time as a function of the finishing position, where a circle indicates that IPOPT has successfully found a solution. We see from Fig. 3 that both the distance and signed distance formulation are able to compute all paths successfully. Interestingly, however, the computation time pattern of these two approaches are not correlated; in other words, a "difficult" scenario for the distance formulation might be "easy" for the signed distance formulation, and vice versa. In practice, this implies that to obtain feasible trajectories as fast as possible, the navigation problem should be solved with both obstacle avoidance formulations, and the first solution should be taken. In our setup, such an approach would result in a worst case computation time of 28.9 s, as opposed to 48.0 s and 59.1 s if the distance and signed distance reformulation are considered individually.

We close this section by pointing out that, with a maximum computation time of 2.8 s, the time for A^⋆^ to find an initial guess is considerably lower than that for solving the optimization problems, see Table 1. This is not surprising since A^⋆^ only plans a path in the $(X,Y,Z)$-space and ignores the system dynamics which leads to zigzag behavior, see Fig. 2. A dynamically feasible path is only obtained after solving the optimal control problems and which, by explicitly taking into account system dynamics, smoothen and locally optimize the path provided by the A^⋆^ algorithm.

Figure 3: Solution time for quadcopter trajectory planning with distance formulation (top) and signed-distance formulation (right).

signed distance formulation

Table 1: Computation time of A⋆, distance formulation and signed distance formulation.

## Example 2: Autonomous Parking

As a second application for our collision avoidance formulation, we consider the autonomous parking problem for self-driving cars. In contrast to the quadcopter case, modeling a car as a point-mass and then approximating its shape with a ball can be very conservative and prevent the car from finding a feasible parking trajectory, especially when the environment is tight. In this section, we model the car as a rectangle, and then employ the full-dimensional formulation described in Section 4. We show that our modelling framework allows us to find obstacle-free parking trajectories even in tight environments. Two scenarios are considered: reverse parking (Fig. 4) and parallel parking (Fig. 5).

Figure 4: Reverse parking maneuver. The controlled vehicle is shown in green at every time step. Vehicle starts on the left facing to the right, and ends facing upwards, see https://youtu.be/V7IUPW2qDFc for an animation.

Figure 5: Parallel parking maneuver. The controlled vehicle is shown in green at every time step. Vehicle starts facing to the right, and ends facing to the right, see https://youtu.be/FST7li4M6lU for an animation.

### Environment and Obstacle Modeling

For the reverse parking scenario, the parking spot is assumed 2.6 m wide and 5.2 m long. The width of the road, where the car can maneuver in, is 6 m, see Fig. 4 for an illustration. For the parallel parking scenario, the parking spot is 2.5 m deep and 6 m long, and the space to maneuver is 6 m wide (Fig. 5). Note that the obstacles in the reverse parking scenario can be described by three axis aligned rectangles, while the obstacles in the parallel parking scenario can be described by four axis aligned rectangles. In both cases, the controlled vehicle is modeled as a rectangle of size $4.7 \times 2$ m, whose orientation is determined by the car's yaw angle.

### System Dynamics and Cost Function

The car is described by the classical kinematic bicycle model, which is well-suited for velocities used in typical parking scenarios. The states $(X,Y)$ correspond to the center of the rear axes, while $\varphi$ is the yaw angle with respect to the X-axis, and $v$ is the velocity with respect to the rear axes. The inputs are the steering angle $\delta$ and the acceleration $a$. Hence, the continuous-time dynamics of the car is given by

where $L = 2.7$ m is the wheel base of the car. The steering angle is limited between $\pm 0.6$ rad (approximately 34 deg), with rate constraints $\overset{˙}{\delta} \in {\lbrack{- 0.6},0.6\rbrack}$ rad/s; acceleration is limited to be between $\pm 1$ m/s^2^. We limit the car's velocity to lie between $- 1$ and $2$ m/s. Similar as in the quadcopter case, the continuous-time dynamics are discretized using a forward Euler scheme. Finally, the same cost function as in the quadcopter is used, i.e., a weighted sum between the discretization-time and control effort is considered.

### Initial Guess

Similar to the previous example, the solution quality of the non-convex optimization problems heavily depends on the initial guess provided to the numerical solvers. Unfortunately, it turns out that the A^⋆^ algorithm used in the quadcopter example generally provides a poor warm start as it is unable to take into account the vehicle's non-holonomic dynamics^44^4Roughly speaking, A^⋆^ will return trajectories that would require the vehicle to move sideways. Simulations indicate that the numerical solvers are typically not able to "correct" such a behavior and unable to recover a feasible solution when initialized with A^⋆^.. To address this issue, we resort to a modified version of A^⋆^, called Hybrid A^⋆^. The main idea behind Hybrid A^⋆^ is to use a simplified vehicle model with states $(X,Y,\varphi)$, and a finite number of steering inputs to generate a coarse parking trajectory. Like A^⋆^, Hybrid A^⋆^ grids the state space and performs a tree search, where the nodes are expanded using the simplified vehicle model. We refer the interested reader to for details on Hybrid A^⋆^. Fig. 6 and Fig. 7 depict two trajectories obtained from the Hybrid A^⋆^ algorithm. Notice that, due to discretization of state and input, the paths generated by Hybrid A^⋆^ seems more "bang-bang" and less "smooth" than those shown in Fig. 4 and Fig. 3.

Figure 6: Initial guess provided by Hybrid A⋆ for reverse parking.

Figure 7: Initial guess provided by Hybrid A⋆ for parallel parking.

### Simulation Results

To evaluate the performance of formulations and, we study the reverse and parallel trajectory planning problem. For both cases, we consider different starting positions but one fixed end position at $X = 0$ m, and investigate the computation time of each method. The starting positions are generated by gridding the maneuvering space within $X \in {\lbrack{- 10},10\rbrack}$ m and $Y \in {\lbrack 6.5,9.5\rbrack}$ m, with 21 grid points in the $X$ direction and 4 grid points in $Y$ direction, see Fig. 8. The orientation for all the starting points is $\varphi = 0$, resulting in a total of 84 starting points. The horizon length $N$ is given by the Hybrid A^⋆^ algorithm. The optimization problems are again implemented with the modeling toolbox JuMP in the programming Julia, and IPOPT is used as the numerical solver. The problems are solved on a 2013 MacBook Pro with a i7 processor clocked at 2.6 GHz. A Julia-based example code can be found at [https://github.com/XiaojingGeorgeZhang/OBCA](https://github.com/XiaojingGeorgeZhang/OBCA).

We begin by considering the reverse parking case, where one specific maneuver is illustrated in Fig. 4. The computation times for the distance and the signed distance formulation are listed in Table 2 (upper half) and shown in Fig. 8, for all 84 initial conditions. Table 2 indicates that the distance formulation is generally faster than the signed-distance formulation, with a mean computation time of 0.60 s compared to 1.03 s. This is not surprising since the signed distance formulation has more decision variables due to the presence of the slack variables $s_{k}^{(m)}$, see. Furthermore, we see from Fig. 8 that both approaches are able to find feasible parking trajectories, for all 84 considered initial conditions. Interestingly, we see that there are no obvious relations between starting positions and solution times.

Figure 8: Solution time for reverse parking with distance formulation (top) and signed-distance formulation (bottom).

The computation times of the parallel parking case is shown in Fig. 9 and Table 2 (lower half). Similar as in the reverse parking case, we see that both approaches have a 100% success rate, and that, again due to the presence of the slack variables, the signed distance formulation requires longer computation time (1.67 s on average) than the distance formulation (0.87 s on average). Compared to reverse parking we see that parallel parking is computationally more demanding. We believe that this is due to the fact that the paths in parallel parking are generally longer than in reverse parking, since the car first needs to drive to the right before it can back into the parking lot, see also Fig. 5.

warm start (Hybrid A⋆)

signed distance formulation

warm start (Hybrid A⋆)

signed distance reformulation

Table 2: Computation time of Hybrid A⋆, distance formulation and signed distance formulation.

Figure 9: Solution time for parallel parking with distance formulation (top) and signed-distance formulation (bottom).

We close this section with the following two remarks: First, we point out that, while the paths generated by the Hybrid A^⋆^ are collision-free and kinodynamically feasible, they are challenging to track with low-level path following controllers because they do not incorporate information on the velocity and do not take into account the rate constraints in both steering and acceleration, allowing the car to take "aggressive" maneuveures. As demonstrated in, this leads, in general, to significantly longer maneuvering times. Second, we notice from Table 2 that the computation time of Hybrid A^⋆^ is comparable to those of (signed) distance. Furthermore, the maximum overall computation time of Hybrid A^⋆^ and signed distance reformulation is 7.7 s (reserve parking), and 9.2 s (parallel parking). This implies that, when initialized with Hybrid A^⋆^, the proposed collision avoidance framework enables real-time autonomous parking in tight environments.

## Conclusion

In this paper, we presented smooth reformulations for collision avoidance constraints for problems where the controlled object and the obstacle can be represented as the finite union of convex sets. We have shown that non-differentiable polytopic obstacle constraints can be dealt with via dualization techniques to preserve differentiability, allowing the use of gradient- and Hessian-based optimization methods. The presented reformulation techniques are exact and non-conservative, and apply equally to point-mass and full-dimensional controlled vehicles. Furthermore, in case collision-free trajectories cannot be generated, our framework allows us to find least-intrusive trajectories, measured in terms of penetration.

Our numerical studies, performed on a quadcopter trajectory planning and autonomous car parking example, indicate that, when appropriately initialized, the proposed framework is robust, real-time feasible, and able to generate dynamically feasible trajectories. Furthermore, we have seen that the initialization method is problem-dependent, and should be chosen depending on the system at hand. Current research focuses on appropriately warm starting the discretization time $T_{\text{opt}}$, as well as on methods for further speeding up computation times.
