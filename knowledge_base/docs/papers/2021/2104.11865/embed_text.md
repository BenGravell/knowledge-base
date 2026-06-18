## Introduction

An advanced control system such as a mobile robot may be required to perform many different tasks. If the task set is finite, like selecting between "map an environment" and "deliver a package", then its size is naturally quantified by the number of tasks. If the task set is infinite, like delivering packages with arbitrary mass and inertial properties, then its size is not so easily quantified. Even if the task space is equipped with a metric or measure, these structures may be only weakly linked to the diversity of behavior required for good performance on all tasks.

Our interest in this issue is motivated by multi-task paradigms in learning-based control, where the policy is selected from a parameterized family of functions that map state and task parameters directly to actions. As the task space expands from a singleton set, we expect to need a more expressive class of functions to represent a good multi-task policy. In this work, we propose the *$\alpha$-suboptimal covering number* to capture this idea. For a task space $\Phi$ and a suboptimality ratio $\alpha > 1$, we define $N_{\alpha}{(\Phi)}$ as the size of the smallest set of single-task policies $\mathcal{C}$ such that for every $\phi \in \Phi$, at least one $\pi \in \mathcal{C}$ has a cost ratio no greater than $\alpha$ relative to the optimal policy for $\phi$. If the policies in $\mathcal{C}$ are parameterized functions, then $\mathcal{C}$ provides an upper bound on the number of parameters needed to represent an $\alpha$-suboptimal multi-task policy. In switching-based adaptive control, where $\phi$ is unknown, a smaller $\mathcal{C}$ implies a faster convergence time.

To study suboptimal covering numbers in a concrete setting, we consider linear dynamical systems with quadratic cost functions, or LQR problems. LQR problems are a common setting to analyze learning algorithms because detailed properties are known. This has led to new inquiries into their fundamental properties. We construct a family of well-behaved multi-task LQR problems where $\Phi$ is controlled by a "breadth" parameter $\theta \in {\lbrack 1,\infty)}$, and for which $N_{\alpha}{(\Phi_{\theta})}$ is finite and increasing in $\theta$. For the special case of a scalar LQR problem, we derive matching logarithmic upper and lower bounds on $N_{\alpha}{(\Phi_{\theta})}$ as a function of $\theta$. As an effort towards analogous bounds for the matrix case, we present empirical results intended to shed light on the problem structure. For the upper bound, we analyze properties of a logical extension of our scalar cover. For the lower bound, we visualize suboptimal neighborhoods for two choices of "extremal" systems and find surprising topological behavior for one choice.

This paper is an initial step towards a comprehensive theory. In addition to a more complete picture of deterministic LQR systems, ideas of $\alpha$-suboptimal coverings could be applied to a wide range of multi-task problems. We also hope they will lead to insights about function class expressiveness in learning-based multi-task control.

## Problem setting

In this section, we first define suboptimal covering numbers with respect to an abstract multi-task control problem independent of distinctions such as continuous vs. discrete time and stochastic vs. deterministic. We then instantiate these notions for a particular class of LQR problems.

### Notation

The set of all functions $\mathcal{X}\mapsto\mathcal{Y}$ is denoted by $\mathcal{Y}^{\mathcal{X}}$. The relation $A \succeq B$ (resp. $A \succ B$) denotes that $A - B$ is positive semidefinite (resp. definite). Matrices of zeros and ones, with dimension implied by context, are denoted by $\mathbf{0}$ and $\mathbf{1}$. The integers $\{ 1,\ldots,N\}$ are denoted by $\lbrack N\rbrack$.

### Multi-task optimal control

A *multi-task optimal control problem* is defined by an arbitrary state space $\mathcal{X}$, action space $\mathcal{U}$, and task space $\Phi$; a class of reference policies $\Pi_{ref} \subseteq \mathcal{U}^{\mathcal{X}}$, and a strictly positive objective function $J:{{\Phi \times \mathcal{U}^{\mathcal{X}}}\mapsto{\mathbb{R}}_{> 0}}$. The partial application of $J$ for $\phi \in \Phi$ is denoted by $J_{\phi}:{\mathcal{U}^{\mathcal{X}}\mapsto{\mathbb{R}}}$. The optimal reference cost for an task is denoted by $J_{\phi}^{\star} = {{\min_{\pi \in \Pi_{ref}}J_{\phi}}{(\pi)}}$.

### Suboptimal coverings

Consider a multi-task optimal control problem $(\mathcal{X},\mathcal{U},\Phi,\Pi_{ref})$ and a suboptimality ratio $\alpha > 1$. The *$\alpha$-suboptimal neighborhood* of the policy $\pi:{\mathcal{X}\mapsto\mathcal{U}}$ is $\mathcal{N}_{\alpha}{(\pi)} = \left\{ \phi \in \Phi:J_{\phi}{(\pi)}/J_{\phi}^{\star} \leq \alpha \right\}.$ The set $\mathcal{C} \subseteq \mathcal{U}^{\mathcal{X}}$ is an *$\alpha$-suboptimal cover* of $\Phi$ if ${{\bigcup_{\pi \in \mathcal{C}}{\mathcal{N}_{\alpha}{(\pi)}}} = \Phi}.$ The *$\alpha$-suboptimal covering number* of $\Phi$, denoted $N_{\alpha}{(\Phi)}$, is the size of the smallest finite $\alpha$-suboptimal cover of $\Phi$ if one exists, or $\infty$ otherwise.

### Standard LQR problem

A continuous-time, deterministic, infinite-horizon, time-invariant LQR problem with full-state feedback is defined by state space $\mathcal{X} = {\mathbb{R}}^{n}$, action space $\mathcal{U} = {\mathbb{R}}^{m}$, linear dynamics ${\overset{˙}{x} = {{Ax} + {Bu}}},$ where ${A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times m}}$, and quadratic cost

where $Q \succeq \mathbf{0}$ and $R \succ \mathbf{0}$ are cost matrices of appropriate dimensions and $\mathcal{N}{(\mathbf{0},I)}$ is the unit Gaussian distribution. For the purposes of this paper, the pair $(A,B)$ is *controllable* if ${J{(\pi)}} < \infty$ for some policy $\pi$. If $(A,B)$ is controllable, then the optimal policy is the linear $u = {K^{\star}x}$, where $K^{\star} \in {\mathbb{R}}^{m \times n}$ can be computed by finding the unique maximal positive semidefinite solution $P$ of the algebraic Riccati equation ${{{{A^{\top}P} + {PA}} - {PBR^{- 1}B^{\top}P}} + Q} = \mathbf{0}$ (henceforth called the *maximal solution*) and letting $K^{\star} = {- {R^{- 1}B^{\top}P}}$. Additionally, ${J{(K^{\star})}} = {{Tr}\lbrack P\rbrack}$. An arbitrary controller $K \in {\mathbb{R}}^{m \times n}$ is *stabilizing* if ${J{(K)}} < \infty$, in which case $J{(K)}$ satisfies

$W$ can be computed by solving the Lyapunov equation ${{{{({A + {BK}})}^{\top}W} + {W{({A + {BK}})}} + I} = \mathbf{0}}.$

### Multi-dynamics LQR

A fully general formulation of multi-task LQR would allow variations in each of $(A,B,Q,R)$, but this creates redundancy. Any LQR problem where $Q \succ 0$ is equivalent via change of coordinates to another LQR problem where $Q = I$ and $R = I$. To reduce redundancy, we consider only *multi-dynamics* LQR problems where $Q = I_{n \times n}$ and $R = I_{m \times m}$ in this work. The reference policy class is linear: $\Pi_{ref} = {\mathbb{R}}^{m \times n}$.

A multi-dynamics LQR problem can be defined by $\Phi = {\mathbf{A} \times \mathbf{B}}$ for some sets $\mathbf{A} \subseteq {\mathbb{R}}^{n \times n}$ and $\mathbf{B} \subseteq {\mathbb{R}}^{n \times m}$, but it is not obvious how to design $\mathbf{A}$ and $\mathbf{B}$. To support an asymptotic analysis of $N_{\alpha}{(\Phi)}$, the task space $\Phi$ should have a real-valued "breadth" parameter $\theta$ that sweeps from a single task to sets with arbitrarily large, but finite, covering numbers. Matrix norm balls are a popular representation of dynamics uncertainty in the robust control literature, but they can easily contain uncontrollable pairs, and removing the uncontrollable pairs can lead to an infinite covering number. For example, in the scalar problem ${\mathbf{A} = {\{ a\}}},{\mathbf{B} = {{\lbrack{- \theta},0)} \cup {(0,\theta\rbrack}}}$, where $a > 0$, it can be shown that no $\alpha$-suboptimal cover is finite.

These properties are worrying, but the example $\mathbf{B}$ is pathological. The zero crossing is analogous to reversing the direction of force applied by an actuator in a physical system. A more relevant multi-dynamics problem is variations in mass or actuator strength, whose signs are fixed. We formalize this idea with the following definition.

### Decomposed dynamics form

Fix $A \in {\mathbb{R}}^{n \times n}$ and a *breadth* parameter $\theta \geq 1$. Let $\mathbf{B} = {\{{U\SigmaV^{\top}}:{\Sigma \in \mathbf{\Sigma}}\}}$, where $\mathbf{\Sigma} = {\{{{diag}{(\sigma)}}:{\sigma \in {\lbrack\frac{1}{\theta},1\rbrack}^{d}}\}}$. The matrices $U \in {\mathbb{R}}^{n \times d}$ and $V \in {\mathbb{R}}^{m \times d}$ each have rank $d$, where $0 < d \leq {\min{\{ n,m\}}}$. The tuple $(A,U,V,\theta)$ fully defines a *multi-task LQR problem in decomposed dynamics form*, or *DDF problem* for brevity.

The continuity of the LQR cost with respect to $B$ and the compactness of $\Phi$ for any $\theta$ imply that $N_{\alpha}{(\Phi_{\theta})}$ is always finite. Variations in $A$ are redundant in the scalar case where we focus our theoretical work in this paper. The definition can be extended to include them in future work.

### Linearized quadrotor example

As an example of a realistic DDF problem, we consider the quadrotor helicopter illustrated in Figure 1. Near the hover state, its full nonlinear dynamics are well approximated by a linearization. The state is given by ${x = {(\mathbf{x},\mathbf{v},\mathbf{r},{\mathbf{ω}})}},$ where $\mathbf{x} \in {\mathbb{R}}^{3}$ is position, $\mathbf{v} \in {\mathbb{R}}^{3}$ is linear velocity, $\mathbf{r} \in {\mathbb{R}}^{3}$ is attitude Euler angles, and ${\mathbf{ω}} \in {\mathbb{R}}^{3}$ is angular velocity. The inputs $u \in {\mathbb{R}}_{\geq 0}^{4}$ are the squared angular velocities of the propellers.

Many factors influence the response to inputs, including geometry, mass, moments of inertia, motor properties, and propeller aerodynamics. These can be combined and partially nondimensionalized into four control authority parameters to form $\phi \in \Phi$. The hover state occurs at ${x = \mathbf{0}},{u \propto \mathbf{1}}$, where the constant input counteracts gravity. The linearized dynamics are given by

where $g$ is the gravitational constant and ${\hat{e}}_{z} = {\lbrack 0\ 0\ 1\rbrack}^{\top}$. The parameters $(\sigma_{z},\sigma_{\phi},\sigma_{\theta},\sigma_{\psi})$ denote the thrust, roll, pitch, and yaw authority constants respectively. Since we use the convention $\sigma \in {\lbrack\frac{1}{\theta},1\rbrack}$, the maximum value of each constant can be varied by scaling the columns of $U$.

Figure 1: Quadrotor helicopter with position states x, y, z, attitude states ϕ, θ, ψ, and propeller speed inputs u1, u2, u3, u4. The linearized dynamics at hover, subject to variations in mass, geometry, etc., can be expressed in decomposed dynamics form—see Section 2.

## Theoretical results

In this section we show logarithmic upper and lower bounds on the growth of $N_{\alpha}{(\Phi_{\theta})}$ in $\theta$ for scalar DDF problems. We present several intermediate results in matrix form because they are needed for our empirical results later. We begin with a key lemma in the framework of *guaranteed cost control* (GCC) from Petersen and McFarlane, simplified for our use case.

### Lemma 3.1 (GCC synthesis, Petersen and McFarlane (1994))

Given the multi-task LQR problem $\mathbf{A} = {\{ A\}}$, $\mathbf{B} = {\{{{B_{1}\Delta} + B_{2}}:{{\parallel\Delta\parallel} \leq 1}\}}$, where ${B_{1},B_{2}} \in {\mathbb{R}}^{m \times p}$ are arbitrary for arbitrary $p$, and the state cost matrix is $Q \succ \mathbf{0}$, if there exists $\tau > 0$ such that $P \succ \mathbf{0}$ solves the Riccati equation

then the controller $K = {- {\frac{1}{1 + \tau}B_{2}^{\top}P}}$ has cost ${J_{B}{(K)}} \leq {{Tr}\lbrack P\rbrack}$ for all $B \in \mathbf{B}$. Also, ${Tr}\lbrack P\rbrack$ is a convex function of $\tau$.

We use the notation ${P,\tau,K} = {\text{GCC}{(A,B_{1},B_{2},Q)}}$ to indicate that $P,\tau$ solve. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")) and $K$ is the corresponding controller. It is straightforward to show that any DDF problem can be expressed in the form required by \\lemmareflem:petersen-gcc with additional constraints on $\Delta$.

In the original presentation, Petersen and McFarlane treat $B_{1}$ as given, so they accept that. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")) may have no solution (for example, when ${A = {2I}},{{B_{1} = I},{B_{2} = \mathbf{0}}}$). Our application requires constructing values of $B_{1},B_{2}$ that guarantee a solution, motivating the following lemma. We abbreviate the reference text Lancaster and Rodman as.

### Lemma 3.2 (existence of $\alpha$-suboptimal GCC)

For the DDF problem $(A,U,V,\theta)$, if $B \in \mathbf{B}$ and $\alpha > 1$, then there exists $B_{1} \neq \mathbf{0} \in {\mathbb{R}}^{m \times n}$ such that the GCC Riccati equation. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")) with $B_{2} = B$ has a solution $(P,\tau)$ satisfying ${{Tr}\lbrack P\rbrack} \leq {\alphaJ_{B}^{\star}}$.

### Proof 3.3

For this proof, it will be more convenient to write the algebraic Riccati equation as

where $D \succeq \mathbf{0}$. Let $\mathcal{D} = {\{{D \succeq \mathbf{0}}:{{(A,D)}\text{~is controllable}}\}}$. Controllability of $(A,B)$ implies that ${BB^{\top}} \in \mathcal{D}$ (Corollary 4.1.3 ). Let ${Ric}_{+}$ denote the map from $\mathcal{D}$ to the maximal solution of, which is continuous (Theorem 11.2.1 ), and let $\mathcal{D}_{\alpha} = {\{{D \in \mathcal{D}}:{{{Tr}\left\lbrack {{Ric}_{+}{(D)}} \right\rbrack} < {\alphaJ_{B}^{\star}}}\}}$. The set $\mathcal{D}_{\alpha}$ is open in $\mathcal{D}$ by continuity and is nonempty because it contains $BB^{\top}$. Now define ${B_{1}{(\tau)}} = {\tauB}$ for $\tau \in {(0,\frac{1}{2})}$. The equivalent of $D$ in the GCC Riccati equation. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")) becomes

As a positive multiple of $BB^{\top}$, we know ${D{(\tau)}} \in \mathcal{D}$, and because ${\lim_{\tau\rightarrow 0}{D{(\tau)}}} = {BB^{\top}}$, the set of $\tau$ for which ${D{(\tau)}} \in \mathcal{D}_{\alpha}$ is nonempty. Any such $\tau$ and $B_{1}{(\tau)}$ provide a solution.

Finally, the following comparison result will be useful in several places.

### Lemma 3.4 (Lan95, Corollary 9.1.6)

Given two algebraic Riccati equations

with maximal solutions $P$ and $\overset{\sim}{P}$, let $X = \begin{bmatrix}
\end{bmatrix}$ and $\overset{\sim}{X} = \begin{bmatrix}
\overset{\sim}{Q} & {\overset{\sim}{A}}^{\top} \\
\overset{\sim}{A} & {- {\overset{\sim}{B}{\overset{\sim}{B}}^{\top}}}
\end{bmatrix}$. If $X \succeq \overset{\sim}{X}$, then $P \succeq \overset{\sim}{P}$.

### Scalar upper bound

We are now ready to bound the covering number for scalar systems. The first lemma bounding $J_{a,b}^{\star}$ will be useful for the lower bound also. We then construct a cover inductively.

### Lemma 3.5

In a scalar LQR problem, if $a > 0$ and $0 < b \leq 1$, then the optimal scalar LQR cost satisfies the bounds $\left. 2a/b^{2} < J_{a,b}^{\star} < {(2a + 1)}/b^{2}. \right.$

### Proof 3.6

The lower bound is visible from the closed-form solution for the scalar Riccati equation, which is ${J_{a,b}^{\star} = \frac{a + \sqrt{a^{2} + b^{2}}}{b^{2}}}.$ The upper bound is obtained by substituting ${a^{2} + b^{2}} \leq {({a + 1})}^{2}$.

### Lemma 3.7

If ${p,\tau,k} = {\text{GCC}{(a,b_{1},b_{2},q)}}$, then for any $\beta \in {}$, there exists $k^{\prime} \in {\mathbb{R}}$ such that ${p^{\prime},\tau,k^{\prime}} = {\text{GCC}\left( a,{\betab_{1}},{\betab_{2}},{\beta^{- 2}q} \right)}$, where $p^{\prime} = {\beta^{- 2}p}$.

### Proof 3.8

In the scalar system, the GCC matrix Riccati equation. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")) reduces to the quadratic equation

Substituting $p^{\prime} = {\beta^{- 2}p}$ into and multiplying by $\beta^{- 2}$ yields a new instance of with the parameters $b_{1}^{\prime} = {\betab_{1}}$, $b_{2}^{\prime} = {\betab_{2}}$, $q^{\prime} = {\beta^{- 2}q}$, for which $p^{\prime}$ is a solution with $\tau$ unchanged.

### Theorem 3.9

For the scalar DDF problem defined by $\mathbf{A} = {\{ a\}}$, where $a > 0$, and $\mathbf{B} = \left\lbrack \frac{1}{\theta},1 \right\rbrack$, if $\alpha \geq \frac{{2a} + 1}{2a}$, then ${N_{\alpha}{(\mathbf{B})}} = {O{({\log\theta})}}$.

### Proof 3.10

We construct a cover from the upper end of $\mathbf{B}$. By \\lemmareflem:scalar-cost-ub, the condition $\alpha \geq \frac{{2a} + 1}{2a}$ implies that ${J_{b = 1}^{\star} < {\alpha2a} < {\alphaJ_{b = 1}^{\star}}}.$ Therefore, by \\lemmareflem:petersen-gcc,lem:petersen-existence, there exists $\beta \in {}$ and $p,\tau,k$ such that ${p,\tau,k} = {\text{GCC}{(a,{{({1 - \beta})}/2},{{({1 + \beta})}/2},1)}}$ and $p \leq {\alpha2a}$.

Proceeding inductively, suppose that for $N \geq 1$, we have covered $\lbrack\beta^{N},1\rbrack$ by the intervals $\mathbf{B}_{n} = {\lbrack\beta^{n + 1},\beta^{n}\rbrack}$ for $n \in {\{ 0,\ldots,{N - 1}\}}$, and each $\mathbf{B}_{n}$ has a controller $k_{n}$ such that

Then the existence of the desired $\mathbf{B}_{N},k_{N}$ follows immediately from \\lemmareflem:scalar-cover-recursion.

By \\lemmareflem:lancaster-ARE-domination, for each $\mathbf{B}_{n}$ the GCC state cost $q_{n} = \beta^{- {2n}} \geq 1$ is an upper bound on the cost if we replace $q_{n}$ with $1$ to match the DDF problem. Therefore, for each interval $\mathbf{B}_{n}$, for all $b \in \mathbf{B}_{n}$,

where first inequality is due to \\lemmareflem:lancaster-ARE-domination, the second is due to \\lemmareflem:scalar-cost-ub, the third is by construction of $p$, and last is due to the GCC guarantee of $k_{n}$. Hence, $\mathbf{B}_{n} \subseteq {\mathcal{N}_{\alpha}{(k_{n})}}$. We cover the full $\mathbf{B}$ when $\beta^{N} \leq \frac{1}{\theta}$, which is satisfied by $N \geq {- {\log{\theta/{\log\beta}}}}$.

### Scalar lower bound

For the matching lower bound, we begin by deriving a simplified overestimate of $\mathcal{N}_{\alpha}{(k)}$. We then show that the true $\mathcal{N}_{\alpha}{(k)}$ is still a closed interval moving monotonically with $k$. Finally, we argue that the gaps between consecutive elements of a cover grow at most geometrically, while the range of $k$ values in a cover must grow linearly with $\theta$.

### Lemma 3.11

For a scalar DDF problem with ${a \geq 1},{\mathbf{B} = {\lbrack\frac{1}{\theta},1\rbrack}}$, for any $k < 0$, if $\alpha \geq {3/2}$, then ${\mathcal{N}_{\alpha}{(k)}} \subseteq {\frac{1}{|k|}{\lbrack{c_{1} - c_{2}},{c_{1} + c_{2}}\rbrack}}$, where $c_{1}$ and $c_{2}$ are constants depending on $\alpha$ and $a$.

### Proof 3.12

Beginning with the closed-form solution for $J_{b}{(k)}$, which can be derived from, we define

By \\lemmareflem:scalar-cost-ub, we have $\left. J_{b}^{\star} < 3a/b^{2} \triangleq \overline{J_{b}^{\star}} \right.$, so $\left. \overset{\sim}{r} = \underset{¯}{J_{b}}{(k)}/\overline{J_{b}^{\star}} \right.$ is a lower bound on the suboptimality of $k$. Computing $\partial^{2}{\overset{\sim}{r}/{\partial b^{2}}}$ shows that $\overset{\sim}{r}$ is strictly convex in $b$ on the domain ${a + {bk}} < 0$, so the $\alpha$-sublevel set of $\overset{\sim}{r}$ is the closed interval with boundaries where $\overset{\sim}{r} = \alpha$. This equation is quadratic in $b$ with the solutions $b = {- {{a{({{3\alpha} \pm \sqrt{{9\alpha^{2}} - {6\alpha}}})}}/k}}$. The resulting interval contains $\mathcal{N}_{\alpha}{(k)}$.

### Lemma 3.13

For a scalar DDF problem, if $\alpha > 1$ and $k < {- 1}$, then $\mathcal{N}_{\alpha}{(k)}$ is either empty or a closed interval $\lbrack b_{1},b_{2}\rbrack$, with $b_{1}$ and $b_{2}$ positive and nondecreasing in $k$.

### Proof 3.14

The result follows from quasiconvexity of both the suboptimality ratio ${J_{b}{(k)}}/J_{b}^{\star}$ and the cost $J_{b}{(k)}$. Showing these requires some tedious calculations. For details, see Appendix A.

### Theorem 3.15

For a scalar DDF problem with ${a = 1},{\mathbf{B} = {\lbrack\frac{1}{\theta},1\rbrack}}$, if $\alpha \geq \frac{3}{2}$, then ${N_{\alpha}{(\mathbf{B})}} = {\Omega{({\log\theta})}}$.

### Proof 3.16

From the closed-form solution $k_{a,b}^{\star} = {- {{({a + \sqrt{a^{2} + b^{2}}})}/b}}$, we observe that $k_{b}^{\star} < {- 1}$ for all $b \in \mathbf{B}$. This, along with the quasiconvexity of $J_{b}{(k)}$ in $k$, implies that there exists a minimal $\alpha$-suboptimal cover $\mathcal{C}$ for which all $k_{i} < {- 1}$. Suppose $\mathcal{C} = {k_{1},\ldots,k_{N}}$ is such a cover, ordered such that $k_{i} < k_{i + 1}$. Then by \\lemmareflem:subopt-convex, $\mathcal{N}_{\alpha}{(k_{i})}$ and $\mathcal{N}_{\alpha}{(k_{i + 1})}$ must intersect, so their overestimates according to \\lemmareflem:scalar-neighborhood-optimistic certainly intersect, therefore satisfying

By \\lemmareflem:scalar-neighborhood-optimistic, to cover $b = 1$ controller $k_{1}$ must satisfy $k_{1} \geq {- {({c_{1} + c_{2}})}}$, and to cover $b = \frac{1}{\theta}$, controller $k_{N}$ must satisfy $k_{N} \leq {- {\theta{({c_{1} - c_{2}})}}}$. Along with the previous result, this implies

Recalling that $c_{1}$ and $c_{2}$ only depend on $a$ and $\alpha$, the $\Omega{({\log\theta})}$ dependence on $\theta$ is established.

### Remarks

For the upper bound, it may be possible to compute or bound $\beta$ in the scalar case as a function of $a$ and $\alpha$, but the analogous result will likely be much more complicated in the matrix case.

thm:covering-scalar imposes a lower bound on $\alpha$ greater than $1$. We believe this is a mild condition in practice: if the application demands a suboptimality ratio very close to 1, then the size of the suboptimal cover is likely to become impractical for storage. However, further theoretical results building upon suboptimal coverings may require eliminating the bound.

## Empirical results

For matrix DDF problems, we present empirical results as a first step towards covering number bounds. We begin by testing a cover construction. If the construction fails to achieve a conjectured upper bound in a numerical experiment, then either the conjecture is false, or the construction is not efficient. A natural idea is to extend the geometrically spaced sequence of $b$ values from \\lemmareflem:scalar-cost-ub to multiple dimensions. We now make this notion, illustrated in Figure 2, precise.

### Definition 4.1 (Geometric grid partition)

Given a DDF problem with $\mathbf{\Sigma} = {\lbrack\frac{1}{\theta},1\rbrack}^{d}$, and a grid pitch $k \in {\mathbb{N}}_{+}$, select $s_{1},\ldots,s_{k + 1}$ such that $s_{1} = \frac{1}{\theta}$, $s_{k + 1} = 1$, and $\frac{s_{i + 1}}{s_{i}} > 0$ is constant. For each $j \in {\lbrack k\rbrack}^{d}$, define the grid cell ${{\mathbf{\Sigma}{(j)}} = {\prod_{i = 1}^{d}{\lbrack s_{j{(i)}},s_{{j{(i)}} + 1}\rbrack}}},$ where $j{(i)}$ is the $i^{th}$ component of $j$. The cells satisfy ${\mathbf{\Sigma} = {\bigcup_{j \in {\lbrack k\rbrack}^{d}}{\mathbf{\Sigma}{(j)}}}},$ thus forming an partition (up to boundaries) of $\mathbf{\Sigma}$ into $k^{d}$ cells.

Figure 2: Application of geometric grid cover to linearized quadrotor. (a) Illustration of geometric grid partition. (b) Empirical upper bound on covering number. (c) Suboptimality ratios for corner cells in empirical cover. Discussion in Section 4.

### Empirical upper bound on $N_{\alpha}\hspace{0pt}{(\Phi)}$

In this experiment, we construct an $\alpha$-suboptimal cover $\mathcal{C}$ using geometric grids, such that each $K \in \mathcal{C}$ is $\alpha$-suboptimal for a full grid cell. For each cell $\mathbf{\Sigma}{(j)}$, we attempt GCC synthesis. If it succeeds, we check if ${\mathbf{\Sigma}{(j)}} \subseteq {\mathcal{N}_{\alpha}{({K{(j)}})}}$. If not, we increment the grid pitch $k$ and try again. Termination is guaranteed by continuity. We show results for the linearized quadrotor with $\alpha = 2$ in Figure 2. The data follow roughly logarithmic growth, as indicated by the linear least-squares best-fit curve in black. Small values of $\theta$ are excluded from the fit (indicated by grey points), as we do not expect the asymptotic growth pattern to appear yet.

These results do not rule out the $\log{(\theta)}^{d}$ growth suggested by the geometric grid construction. Testing larger values of $\theta$ is computationally difficult because the number of grid cells becomes huge and the GCC Riccati equation becomes numerically unstable for very small $\Sigma$.

### Efficiency of geometric grid partition

Given an $\alpha$-suboptimal geometric grid cover, we examine a measurable quantity that may reflect the "efficiency" of the cover. Intuitively, in a good cover we expect the suboptimality ratio of each controller $K{(j)}$ relative to its grid cell $\mathbf{\Sigma}{(j)}$ to be close to $\alpha$. If it close to $\alpha$ for some cells but significantly less than $\alpha$ for others, then the grid pitch around the latter cells is finer than necessary. We visualize results for this computation on the linearized quadrotor with ${\theta = 10},{k = 4}$ in Figure 2 --- only the corners of the $4 \times 4 \times 4 \times 4$ grid are shown. The suboptimality ratio is close to $\alpha = 2$ for cells with low control authority (near $\Sigma = {\frac{1}{\theta}I}$), but drops to around $1.4$ for cells with high control authority (near $\Sigma = I$). The difference suggests that the geometric grid cover could be more efficient in the high-authority regime.

### Efficiency of GCC synthesis

One possible source of conservativeness is that \\lemmareflem:petersen-gcc applies to the affine image of a $m \times n$-dimensional matrix norm ball, but we only require guaranteed cost on a $d$-dimensional affine subspace of diagonal matrices. In other words, we ask GCC synthesis to ensure $\alpha$-suboptimality on systems that are not actually part of $\Phi$. If this is negatively affecting the result, then we should observe that the worst-case cost of $K{(j)}$ on $\mathbf{\Sigma}{(j)}$ is less than the trace of the solution $P$ for the GCC Riccati equation. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")). The worst-case cost always occurs at the minimal $\Sigma \in {\mathbf{\Sigma}{(j)}}$ by \\lemmareflem:lancaster-ARE-domination; we evaluate it with. For the quadrotor, a mismatch sometimes occurs for smaller values of $\theta$, but it does not occur for the large values of $\theta$.

### Suboptimal neighborhood visualizations

We now present intuition-building experiments towards a covering number lower bound for matrix DDF problems. A lower bound requires a class of DDF problem that can be instantiated for any dimensionality $d$. Two choices come to mind: *minimum coupling*, where $A = I$, and *maximum coupling*, where $A = {\frac{1}{n}\mathbf{1}}$. Note that for minimum coupling, an $\alpha$-suboptimal policy is not necessarily $\alpha$-suboptimal on each scalar subsystem---if it were, the lower bound $\log{(\theta)}^{d}$ would trivially follow from the results in Section 3.

$\overset{A{= I}}{\overbrace{}}\mspace{51mu}\overset{A{= {\frac{1}{n}\mathbf{1}}}}{\overbrace{}}$
Figure 3: α-suboptimal neighborhoods for geometric grid partition in 2D system. Left: minimum coupling; A = I. Right: maximum coupling; $A = {\frac{1}{n}\mathbf{1}}$. Columns: varying suboptimality threshold α. All axes are logarithmic. Colors have no meaning. Discussion in Section 4.1.

We show approximate suboptimal neighborhoods for a two-dimensional system in Figure 3. We select a geometric grid of $\Sigma$ values (indicated by the circular markers) and synthesize their LQR-optimal controllers. Then, we evaluate the suboptimality ratio of each controller on a finer grid of $\Sigma$ values to get approximate neighborhoods, indicated by the semi-transparent regions. We repeat this experiment with three values of $\alpha$ for both choices of $A$.

Interestingly, the neighborhoods for $A = I$ are not always connected. In the plot for $\alpha = 1.05$ (far left), the neighborhood for the minimal $\Sigma$ has another component that overlaps other neighborhoods to its top and right. If we increase to $\alpha = 1.1$, the components join into an "L"-shaped region. In contrast, the neighborhoods for $A = {\frac{1}{n}\mathbf{1}}$ seem more well-behaved. For both choices of $A$, the neighborhoods are of comparable size.

To verify that this behavior is not an artifact of the two-dimensional case only, we repeat the experiment in three dimensions. Figure 4 shows neighborhoods of one controller $K = K_{{({2/\theta})}I}^{\star}$ for $\alpha$ ranging from $1.04$ to $1.2$. As $\alpha$ grows, $\mathcal{N}_{\alpha}{(K)}$ shows similar topological phases as the $2$D case. In the simply-connected phase (large $\alpha$), the neighborhood appears to include any $\Sigma$ where at least one $\sigma_{i}$ is sufficiently small. If this property holds in higher dimensions, then it would be possible to construct a cover using only controllers of uniform gain in all dimensions for large $\alpha$.

Figure 4: α-suboptimal neighborhoods for the three-dimensional decomposed dynamics system with minimal coupling (A = U = V⊤ = I3 × 3) and breadth θ = 100. Neighborhoods shown for α ranging from 1.04 to 1.2 with a fixed controller.

## Related work

Suboptimal coverings are closely related to several topics in control theory. Robust control synthesis under parametric uncertainty can be interpreted as seeking a policy that performs well on all of $\Phi$ without observing the particular $\phi \in \Phi$. Most problem statements in robust synthesis admit problem instances with no solution; the goal is to find a robust policy *if* one exists. Adaptive control is also concerned with sets of control tasks, with the added complication that $\phi$ is not known to the policy. Adaptive policies of the self-tuning type synthesize a single-task policy after estimating $\phi$, but this relies on the assumption that control synthesis can be computed quickly.

Adaptive and gain-scheduled multi-model methods use a precomputed set of policies instead, but researchers have focused more on the switching rule than the policy set. For example, Fu and Barmish; Stilwell and Rugh; Yoon et al. non-constructively assert the existence of a finite cover by continuity and compactness arguments. To address the need for small covers, Anderson et al.; McNichols and Fadali; Tan et al.; Fekri et al.; Du et al. propose constructive algorithms, sometimes with arguments for minimality, but without size bounds on the cover. Jalali and Golmohammad show an upper bound in terms of frequency-domain properties of $\Phi$, as opposed to state-space parameters like mass and geometry. The most closely related work to ours is from Fu, who shows a tight bound of $2^{n}$ for the stability covering number of a relatively broad $\Phi$. This result is complementary to ours: suboptimality is a stronger criterion than stability, but our class of $\Phi$ is more restrictive. We are not aware of prior work that bounds covering numbers in a setup based on local suboptimality, as opposed to a single global performance measure.

Multi-task control is also a popular topic in deep learning research, where it is often motivated by ideas of lifelong skill acquisition in robotics. Domain randomization methods follow the spirit of robust control, but usually optimize for the average case instead of a worst-case guarantee. Many methods where the policy observes $\phi$ use architectural constructs that can only be applied to finite task sets. A common approach for infinite task spaces is to treat $\phi$ as a vector input alongside the system state. Yu et al.; Chen et al. use this approach for dynamics parameters; Schaul et al. use it for navigation goals. There is evidence that policy class influences these methods: in a recent benchmark, the concatenated-input architecture trails the finite-task architecture. Other investigations into the difficulty of learning policies for multi-task control include methods to condition the multi-task optimization landscape or balance disparate cost ranges.

## Conclusion and future work

In this paper, we introduced and motivated the $\alpha$-suboptimal covering number to quantify infinite task spaces for multi-task control problems. We defined a particular class of multi-task linear-quadratic regulator problems amenable to analysis of the $\alpha$-suboptimal covering number, and showed logarithmic dependency on the problem "breadth" parameter $\theta$ in the scalar case. Towards analogous results for the matrix case, we presented empirical studies intended to shed light on possible proof techniques. For the upper bound, we considered a natural covering construction that would preserve logarithmic dependence on $\theta$ but give exponential dependence on dimensionality. Experiments did not rule out its validity. For the lower bound, we visualized suboptimal neighborhoods for two possible system classes and observed interesting topological behavior for the minimal-coupling class.

After extending our current results to the matrix case, in future work the analysis can be applied to other classes of multi-task LQR problems including variations in $A,Q,R$, discrete time, and stochastic dynamics. It will be interesting to see if there are major differences between LQR variants. We also hope that suboptimal covers and covering numbers will be a useful tool for analyzing how the size of the task space affects the required expressiveness of function classes used in practice as multi-task policies, such as neural networks.
