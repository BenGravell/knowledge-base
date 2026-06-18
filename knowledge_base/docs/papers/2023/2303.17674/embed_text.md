## Introduction

Forward reachability analysis plays a critical role in control theory and robust controller design. Generally, it entails characterizing all states that a system can reach at any time in the future. As such, reachability analysis allows certifying the performance of feedback loops under disturbances and designing controllers with robustness properties. In robust model predictive control (MPC) for instance, it is used to construct tubes around nominal state trajectories to ensure that constraints are satisfied in the presence of external disturbances.

In this work, we study the following reachability analysis problem. Let $n \in {\mathbb{N}}$ be the state dimension, $f:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n}}$ and $g:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n \times n}}$ be functions for the dynamics, and ${\mathcal{W},\mathcal{X}_{0}} \subset {\mathbb{R}}^{n}$ be bounded sets of disturbances and initial conditions. Given a time $T > 0$ and an initial state $x^{0} \in \mathcal{X}_{0}$, we consider systems defined by the ordinary differential equation (ODE)

where the disturbances $w:{{\lbrack 0,T\rbrack}\rightarrow\mathcal{W}}$ are assumed to be integrable ($w \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}$. Under standard smoothness assumptions (see Assumptions LABEL:assumption:f-LABEL:assumption:W), the ODE has a unique solution, denoted by $x_{(w,x^{0})}{( \cdot )}$. For any time $t \in {\lbrack 0,T\rbrack}$, we define the reachable set

that characterizes all states that are reachable at time $t$ for some disturbance $w$ and initial state $x^{0}$.

Figure 1: The convex hulls H (𝒳t) of the reachable sets 𝒳t can be computed by (a) integrating an augmented ODE (ODEd0) for different directions d0 on the sphere 𝒮n − 1, and (b) taking the convex hulls of the resulting extremal state trajectories xd0.

Reachability analysis of nonlinear dynamical systems is challenging. Indeed, from, computing the reachable sets seemingly requires evaluating an infinite number of state trajectories for all possible disturbances and initial conditions.^11^1Each reachable set $\mathcal{X}_{t}$ is the image of an infinite-dimensional set. Indeed, by defining the maps ${g_{t}{(w,x^{0})}} = {x_{(w,x^{0})}{(t)}} \in {\mathbb{R}}^{n}$, each reachable set is expressed as $\mathcal{X}_{t} = {g_{t}{({{L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}} \times \mathcal{X}_{0}})}}$. Due to the complexity of the problem, many existing tools seek convex over-approximations of reachable sets. Yet, current methods tend to be conservative or computationally expensive, see Sections 2 and 11. This motivates the study of properties of convex hulls of reachable sets that can simplify their estimation.

Our main contribution is a new characterization of the convex hulls of reachable sets of dynamical systems of the form, under smoothness assumptions of $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ (see Assumptions LABEL:assumption:f-LABEL:assumption:X0). Specifically, denoting by $\text{H}{(A)}$ the convex hull of a set $A \subset {\mathbb{R}}^{n}$, we show that

where $F{(d^{0},t)}$ is the solution to an ODE with initial conditions $d^{0}$ on the sphere $\mathcal{S}^{n - 1} \subset {\mathbb{R}}^{n}$, see Theorem LABEL:thm:hull_F and $\text{ODE}_{d^{0}}$. Thus, the convex hulls of the reachable sets can now be computed as the convex hulls of solutions of an ODE for different initial conditions $d^{0} \in \mathcal{S}^{n - 1}$. Equation represents a significantly simpler (finite-dimensional) characterization of the convex hulls.

This result unlocks an approach (Algorithm LABEL:alg:1) to efficiently estimate the convex hulls $\text{H}{(\mathcal{X}_{t})}$ by integrating an ODE from a sample of initial conditions. This approach allows efficiently tackling challenging problems such as analyzing the robustness of neural network controllers (see Section 11). This characterization also informs the design of a robust MPC controller (see Algorithm LABEL:alg:mpc) that we demonstrate on a robust spacecraft control task.

This work extends preliminary results in \[LewBonalliEtAl2023\] by:

considering time-varying disturbance-affine dynamics,

accounting for uncertain initial conditions,

studying the boundary of the convex hulls of reachable sets to obtain tighter error bounds (Section 6, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")),

analyzing problems with rectangular uncertainty sets (Section 8), and with disturbances that only affect a subset of directions of the statespace (Section 10 ‣ Convex Hulls of Reachable Sets")),

providing additional numerical results (Section 11),

The main characterization (see Theorem LABEL:thm:hull_F and $\text{ODE}_{d^{0}}$) also does not rely on the projection step from \[LewBonalliEtAl2023\] anymore, simplifying the evaluation of solutions to $\text{ODE}_{d^{0}}$.

### Outline

In Section 2, we review prior work. In Section 3, we introduce notations and preliminary results. In Sections 4 ‣ Convex Hulls of Reachable Sets")-5, we state and derive our characterization result of the reachable convex hulls $\text{H}{(\mathcal{X}_{t})}$ and propose an estimation algorithm (Algorithm LABEL:alg:1). In Sections 6, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")-7, we study the boundary of $\text{H}{(\mathcal{X}_{t})}$ and derive error bounds for Algorithm LABEL:alg:1. We study problems with rectangular uncertainty sets and disturbances that only affect a subset of the statespace in Sections 8-9 and 10 ‣ Convex Hulls of Reachable Sets"), respectively. We provide numerical results in Section 11 and conclude in Section 12. The appendix contains additional details about theoretical and numerical results.

## Related work

### Numerical methods

The forward reachable sets of nonlinear systems are generally difficult to characterize. For this reason, many existing approaches seek convex over-approximations of the reachable sets, e.g., represented as hyper-rectangles \[Meyer2021\], ellipsoids \[Kurzhanski2000\], zonotopes \[Althoff2008\], or ellipsotopes \[Kousik2023\], see \[Althoff2021\] for a recent survey that also reviews non-convex approximations. Existing over-approximation methods include techniques based on conservative linearization \[Althoff2008\], differential inequalities \[Ramdani2009, Scott2013\], and Taylor models \[Berz1998, Chen2013\]. In particular, systems with mixed-monotone \[meyer2019hscc, Coogan2015, Abate2022\] or contracting \[Maidens2015, Fan2017, SinghMajumdarEtAl2017\] dynamics have been extensively studied, as these properties simplify the computation of accurate over-approximations. To tackle smooth systems, a standard approach consists of linearizing the dynamics and bounding the Taylor remainder using smoothness properties of the dynamics \[Althoff2008, koller2018, Yu2013, Leeman2023, Althoff2021\]. This method has been widely used in robust MPC but is known to be conservative \[LewPavone2020\], see also Section 11.

Methods that estimate the reachable sets from a sample of state trajectories \[Huang2012, Donz2007\] have recently found significant interest \[ThorpeL4DC2021, LewPavone2020, LewJansonEtAl2022\]. However, the sample complexity of these methods increases with the number of uncertain variables. For systems with disturbances as in, the number of uncertain variables (and thus the approximation error) increases as the discretization is refined. Thus, naive sampling-based methods are not well-suited for reachability of systems with continuous-time disturbances, see also Section 11 for comparisons.

### On geometry and optimal control

The deep connection between geometry, reachability analysis, and optimal control is well-known \[Agrachev2004, BonnardChyba2003, Trelat2012\]. It was previously used in \[Krener1989, Schttler2012\] to characterize the true reachable sets of dynamical systems of dimensions $n \leq 4$ with scalar control inputs (control inputs in \[Krener1989\] take the role of disturbances in ). Our results also leverage geometric arguments and the Pontryagin Maximum Principle (PMP), but apply to a different class of dynamical systems with arbitrary state dimensionality $n$ and the same number of disturbances and states. With an appropriate relaxation scheme inspired from \[Silva2010\], these results can be approximately generalized to problems with a smaller number of disturbances than states, see Section 10 ‣ Convex Hulls of Reachable Sets"). Importantly, by studying the convex hulls of the reachable sets, our results apply to arbitrarily-large times $T$ and sets $(\mathcal{X}_{0},\mathcal{W})$, and thus do not rely on a small-time assumption as in \[Krener1989\] or on a set $\mathcal{X}_{0}$ small-enough as in \[Reiig2007\]. In contrast, \[Krener1989\] and \[Reiig2007\] study the structure of the true reachable sets that may self-intersect for times $T$ too large, see Example LABEL:example:selfintersect.

Our derivations start with the idea of searching for boundary states that are the furthest in different directions (see $\text{OCP}_{d}$). This approach is standard in the setting with linear dynamics where reachable sets are convex \[Pecsvaradi1971, Schttler2012\],\[Kurzhanski2014, Chap.1.4\]. However, in the nonlinear case, reachable sets may be non-convex, and finding the extremal disturbance trajectories that generate boundary states requires solving optimal control problems (OCPs) or their corresponding boundary-value problems (BVPs) stemming from the PMP (see $\text{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")). Such approaches were explored in \[Gornov2015\] and \[Baier2009\], but remain computationally challenging. Our results show that under the right set of assumptions (see Assumptions LABEL:assumption:f-LABEL:assumption:X0), solving OCPs is not necessary and extremal trajectories take a simple form. The key is the additional idea of sampling initial values of the adjoint vector. Studying the convex hulls of reachable sets unlocks arguments from convex geometry that allow proving the exactness of the approach.

## Notations and preliminary results

### Notations

Let ${{a,b} \in {\mathbb{R}}^{n}},{\lambda \in {\mathbb{R}}}$. We denote by ${a^{\top}b} = {\sum_{i = 1}^{n}{a_{i}b_{i}}}$ the Euclidean inner product, by ${\| a\|} = {({\sum_{i = 1}^{n}a_{i}^{2}})}^{1/2}$ the Euclidean norm, by ${\| a\|}_{\lambda} = {({\sum_{i = 1}^{n}{|a_{i}|}^{\lambda}})}^{1/\lambda}$ the $\lambda$-norm with $\lambda \geq 1$, by ${a \odot b} = {({a_{1}b_{1}},\ldots,{a_{n}b_{n}})}$ the elementwise product, $a^{\lambda} = {(a_{1}^{\lambda},\ldots,a_{n}^{\lambda})}$, by ${|a|} = {({|a_{1}|},\ldots,{|a_{n}|})}$ the absolute value, by $I_{n}$ the identity matrix of size $n$, by ${B{(x,r)}} = {\{{y \in {\mathbb{R}}^{n}}:{{\|{y - x}\|}^{2} \leq r^{2}}\}}$ the closed ball of center $x$ and radius $r \geq 0$, and by $\mathcal{S}^{n - 1} = {\{{x \in {\mathbb{R}}^{n}}:{{\| x\|}^{2} = 1}\}}$ the unit sphere. Given ${A,B} \subset {\mathbb{R}}^{n}$, we denote by $\text{Int}{(A)}$, $\overline{A}$, ${\partial A} = {\overline{A} \smallsetminus {\text{Int}{(A)}}}$, and $A^{\mathsf{c}} = {{\mathbb{R}}^{n} \smallsetminus A}$ the interior, closure, boundary, and complement of $A$, by ${d_{A}{(x)}} = {\inf_{a \in A}{\|{x - a}\|}}$ the distance from $x$ to $A$, and by

the Hausdorff distance between compact sets $A$ and $B$.

### Convex geometry

A point in a set $A$ is said to be an extreme point if it is the endpoint of every segment in $A$ that contains it \[Grothendieck1973\]. We denote by $\text{H}{(A)}$ the convex hull of $A \subset {\mathbb{R}}^{n}$ and by $\text{Ext}{(A)}$ the set of extreme points of a compact set $A \subset {\mathbb{R}}^{n}$. The next result is standard.

### Lemma 1 (Support hyperplane)

Let $C \subset {\mathbb{R}}^{n}$ be a closed and convex set and $x \in {\partial C}$. Then, there exists a support hyperplane $\{{y \in {\mathbb{R}}^{n}}:{{d^{\top}{({y - x})}} = 0}\}$ defined by some $d \in \mathcal{S}^{n - 1}$ such that ${d^{\top}x} \geq {d^{\top}y}$ for all $y \in C$.

The next result follows from the Krein-Milman theorem \[Grothendieck1973\] and is also well-known, see \[LewBonalliEtAl2023, Lemmas 6 and 7\].

### Lemma 2

Let $A \subset {\mathbb{R}}^{n}$ be a compact set. Then, ${\text{Ext}{({\text{H}{(A)}})}} \subseteq A$ and ${\text{H}{(A)}} = {\text{H}{({\partial A})}} = {\text{H}{({{\partial{\text{H}{(A)}}} \cap A})}}$.

### Differential geometry

Let $\mathcal{M} \subseteq {\mathbb{R}}^{n}$ be a $k$-dimensional submanifold. Equipped with the induced metric from the ambient Euclidean norm $\parallel \cdot \parallel$, $\mathcal{M}$ is a Riemannian submanifold. For any $x \in \mathcal{M}$, $T_{x}\mathcal{M}$ and $N_{x}\mathcal{M}$ denote the tangent and normal spaces of $\mathcal{M}$\[Lee2012\], respectively, which we view as linear subspaces of ${\mathbb{R}}^{n}$.

Given a map $F:{{\mathbb{R}}^{m}\rightarrow{\mathbb{R}}^{n}}$ and ${x,v,w} \in {\mathbb{R}}^{n}$, $\text{d}F_{x}$ denotes the first-order differential of $F$ at $x$, with ${\text{d}F_{x}{(v)}} = {\sum_{i = 1}^{m}{\frac{\partial F}{\partial x_{i}}{(x)}v_{i}}}$. A differentiable map $F$ is a submersion if ${\text{d}F_{x}}:{{T_{x}{\mathbb{R}}^{m}}\rightarrow{T_{F{(x)}}{\mathbb{R}}^{n}}}$ is surjective for all $x \in {\mathbb{R}}^{m}$, and $F$ is a diffeomorphism if it is a bijection and its inverse is differentiable. For any ${(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$, ${{\nabla f}{(t,x)}} \in {\mathbb{R}}^{n \times n}$ denotes the Jacobian matrix of $f{(t, \cdot )}$ at $x$ in Euclidean coordinates, and ${{\nabla g}{(t,x)}} \in {\mathbb{R}}^{n \times n \times n}$ is the $3$-tensor with entries ${\lbrack{{\nabla g}{(t,x)}}\rbrack}_{ijk} = {({\partial{{g_{ij}{(t,x)}}/{\partial x_{k}}}})}$. We define ${{\nabla g}{(t,x)}v} \in {\mathbb{R}}^{n \times n}$ with ${\lbrack{{\nabla g}{(t,x)}v}\rbrack}_{ik} = {\sum_{j}{{\lbrack{{\nabla g}{(t,x)}}\rbrack}_{ijk}v_{j}}}$ for any $v \in {\mathbb{R}}^{m}$.

Figure 2: Gauss map nℳ: ℳ → 𝒮n − 1 of an ovaloid ℳ = ∂𝒞.

### Ovaloids and Gauss maps

An $({n - 1})$-dimensional submanifold $\mathcal{M} \subset {\mathbb{R}}^{n}$ is called a hypersurface. Let $\mathcal{C} \subset {\mathbb{R}}^{n}$ be such that $\mathcal{M} = {\partial\mathcal{C}}$ is a hypersurface. The Gauss map of $\mathcal{M}$ is the map $n^{\mathcal{M}}:{\mathcal{M}\rightarrow\mathcal{S}^{n - 1}}$ defined such that $n^{\mathcal{M}}{(x)}$ is the unit-norm outward-pointing normal vector of $\mathcal{M}$ at $x \in \mathcal{M}$. For any $x \in \mathcal{M}$, the shape operator (or Weingarten map) is the linear map $S_{x}:{{T_{x}\mathcal{M}}\rightarrow{T_{x}\mathcal{M}}}$ defined by ${S_{x}{(v)}} = {{\nabla n}{(x)}v}$. The $({n - 1})$ eigenvalues of the shape operator are called the principal curvatures of $\mathcal{M}$. $\mathcal{M}$ is said to be an ovaloid (or of strictly positive curvature), if all the principal curvatures of $\mathcal{M}$ are strictly positive. If $\mathcal{M}$ is an ovaloid, then the Gauss map $n^{\mathcal{M}}:{\mathcal{M}\rightarrow\mathcal{S}^{n - 1}}$ is a diffeomorphism \[Rauch1974\], $\mathcal{M}$ is the boundary of a bounded strictly convex set $\mathcal{C}$ such that ${\partial\mathcal{C}} = \mathcal{M}$ \[Rauch1974\], and for any $x \in \mathcal{M}$,

## The structure of $\text{H}\hspace{0pt}{(\mathcal{X}_{t})}$

Our results rely on the following four assumptions.

Assumption LABEL:assumption:f is a standard smoothness assumption \[Lorenz2005, Cannarsa2006\] guaranteeing the existence and uniqueness of solutions to the ODE in and $\text{ODE}_{d^{0}}$. By multiplying $f$ and $g$ with a smooth cutoff function whose arbitrarily large support contains states of interest, the Lipschitzianity assumptions are always satisfied if ${f,g} \in C^{2}$.

Assumption LABEL:assumption:g does not hold for problems with fewer disturbances than states. It is relaxed in Section 10 ‣ Convex Hulls of Reachable Sets").

Assumption LABEL:assumption:W and A4b hold in particular if $\mathcal{W}$ and $\mathcal{X}_{0}$ are spheres or ellipsoids, which are commonly used in applications. These assumptions imply that $\mathcal{W}$ and $\mathcal{X}_{0}$ are strictly convex. They are relaxed in Section 8.

Assuming that $\mathcal{W}$ is convex is standard to prove that the reachable sets are compact.

### Lemma 3 ($\mathcal{X}_{t}$ is compact)

Assume that $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ satisfy Assumptions LABEL:assumption:f, LABEL:assumption:W, and LABEL:assumption:X0. Then, for any $t \in {\lbrack 0,T\rbrack}$, the reachable set $\mathcal{X}_{t} = {\text{(}\text{)}}$ is compact.

Lemma 3 ‣ 4 The structure of "H"⁢(𝒳_𝑡) ‣ Convex Hulls of Reachable Sets") is standard, see e.g. \[Trelat2023\] (from Grönwall's inequality, state trajectories are uniformly bounded thanks to Assumptions LABEL:assumption:f, LABEL:assumption:W, and LABEL:assumption:X0, so Lemma 3 ‣ 4 The structure of "H"⁢(𝒳_𝑡) ‣ Convex Hulls of Reachable Sets") follows from \[Trelat2023, Theorem 7\] with minor adaptations).

Thanks to Assumptions LABEL:assumption:W and A4b, the Gauss maps

of $\partial\mathcal{W}$ and $\partial\mathcal{X}_{0}$ are diffeomorphisms, see Section 3. Recall that $n^{\partial\mathcal{C}}{(x)}$ is the unit outward-pointing normal vector of $\partial\mathcal{C}$ at $x \in {\partial\mathcal{C}}$ for $\mathcal{C} = \mathcal{W}$ and $\mathcal{C} = \mathcal{X}_{0}$, such that for any $w \in {\partial\mathcal{W}}$ and $v \in \mathcal{W}$,

and similarly for $\mathcal{X}_{0}$. If $\mathcal{W} = {B{(0,r)}}$ is a ball, then ${n^{\partial\mathcal{W}}{(w)}} = \frac{w}{\| w\|}$ and ${{(n^{\partial\mathcal{W}})}^{- 1}{(d)}} = {rd}$, see Example LABEL:example:gauss_maps.

Next, we state our main characterization result. Given any direction $d^{0} \in \mathcal{S}^{n - 1}$, we define the augmented ODE

which has a unique solution ${(x,p)}_{d^{0}} \in {C{({\lbrack 0,T\rbrack},{\mathbb{R}}^{2n})}}$ thanks to Assumptions LABEL:assumption:f-LABEL:assumption:X0, from standard results on solutions of ODEs \[Lee2012\]. Note that $g{(t,{x{(t)}})}^{\top}p{(t)}$ is always non-zero under Assumptions LABEL:assumption:f-LABEL:assumption:X0 (see Lemma 4 ‣ 5.2 Reformulating "OCP"_𝑑 using the PMP to reduce the search of solutions from 𝐿^∞⁢([0,𝑇],𝒲) to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")), so (11 ‣ Convex Hulls of Reachable Sets")) is well-defined. The next result characterizes the convex hulls of the reachable sets $\text{H}{(\mathcal{X}_{t})}$ as the convex hull of solutions to $\text{ODE}_{d^{0}}$ for all $d^{0} \in \mathcal{S}^{n - 1}$.

Theorem LABEL:thm:hull_F states that integrating $\text{ODE}_{d^{0}}$ for all values of $d^{0} \in \mathcal{S}^{n - 1}$ (i.e., evaluating ${x_{d^{0}}{(t)}} = {F{(d^{0},t)}}$ for different directions $d^{0}$) is sufficient to recover the convex hulls of the reachable sets $\text{H}{(\mathcal{X}_{t})}$. This characterization significantly simplifies the reachability analysis problem, which is now finite-dimensional and amounts to integrating an ODE from different initial conditions.

### Corollary 1 (Reachable tube)

Assume that $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ satisfy Assumptions LABEL:assumption:f-LABEL:assumption:X0 and define $F = {\text{(}\text{)}}$ as in Theorem LABEL:thm:hull_F. Then, for all $t \in {\lbrack 0,T\rbrack}$,

where ${F{(d^{0},{\lbrack 0,T\rbrack})}_{t}} = {F{(d^{0},t)}}$.

Corollary 1 ‣ 4 The structure of "H"⁢(𝒳_𝑡) ‣ Convex Hulls of Reachable Sets") directly follows from Theorem LABEL:thm:hull_F. This result states that to recover the reachable convex hull $\text{H}{(\mathcal{X}_{t})}$ at any time $t$, it suffices to integrate $\text{ODE}_{d^{0}}$ over $\lbrack 0,T\rbrack$ only once for each initial direction $d^{0} \in \mathcal{S}^{n - 1}$. This result implies that all the information required to compute the entire convex reachable tube $\bigcup_{t \in {\lbrack 0,T\rbrack}}{\text{H}{(\mathcal{X}_{t})}}$ (e.g., to enforce constraints at all times for robust MPC, see Section 11.3) is available after evaluating $\text{H}{(\mathcal{X}_{T})}$.

Theorem LABEL:thm:hull_F and Corollary 1 ‣ 4 The structure of "H"⁢(𝒳_𝑡) ‣ Convex Hulls of Reachable Sets") justify using Algorithm LABEL:alg:1 to reconstruct the convex hulls $\text{H}{(\mathcal{X}_{t})}$. Error bounds for the approximation are derived in Section 6, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets").

## Proof of Theorem LABEL:thm:hull_F

We prove Theorem LABEL:thm:hull_F using convex geometry and optimal control. We first prove Theorem LABEL:thm:hull_F assuming that $\mathcal{X}_{0} = {\{ x^{0}\}}$ (i.e., that Assumption LABEL:assumption:X0 holds with A4a) by searching for trajectories with endpoints $x{(T)}$ on the boundary of the reachable set $\mathcal{X}_{t}$. We then characterize the structure of such trajectories using the Pontryagin Maximum Principle (PMP) and conclude with an argument using convex geometry. Finally, we prove the case where $\partial\mathcal{X}_{0}$ is an ovaloid (i.e., Assumption LABEL:assumption:X0 holds with A4b). We discuss these results in Section 5.5.

### Searching for extreme points of $\text{H}\hspace{0pt}{(\mathcal{X}_{T})}$

Assume that $\mathcal{X}_{0} = {\{ x^{0}\}}$. Let $d \in \mathcal{S}^{n - 1}$ be a search direction and define the optimal control problem (OCP)

$\text{OCP}_{d}$ is well-posed under Assumptions LABEL:assumption:f and LABEL:assumption:W, i.e., it admits at least one solution $w_{d} \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}$ (see, e.g., \[Trelat2023, Theorem 9\], and note that ${w{( \cdot )}} = 0$ is feasible). Intuitively, solving $\text{OCP}_{d}$ gives a reachable state ${x_{d}{(T)}} \in \mathcal{X}_{T}$ that is the furthest in the direction $d$.

### Reformulating $\text{OCP}_{d}$ using the PMP to reduce the search of solutions from $L^{\infty}\hspace{0pt}{({\lbrack 0,T\rbrack},\mathcal{W})}$ to ${\mathbb{R}}^{n}$

The Pontryagin Maximum Principle (PMP) \[Pontryagin1987, Agrachev2004, Trelat2012\] gives necessary conditions of optimality for $\text{OCP}_{d}$. As the Hamiltonian of $\text{OCP}_{d}$ is given by $H{(t,x,w,p)} = p^{\top}{(f{(t,x)} + g{(t,x)}w)})$, for any locally-optimal solution $(x_{d},w_{d})$ of $\text{OCP}_{d}$, there exists an absolutely-continuous function $p_{d}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{n}}$, called the adjoint vector, such that for almost every $t \in {\lbrack 0,T\rbrack}$,

${\overset{˙}{p}}_{d}{(t)}$ $= {- {\left( \begin{array}{cl} (15a)
\end{array} \right)^{\top}p_{d}{(t)}}}$
$w_{d}{(t)}$ $= {\underset{v \in \mathcal{W}}{\arg\max}{p_{d}{(t)}^{\top}g{(t,{x_{d}{(t)}})}v}}$ (15c)

A tuple $(x_{d},p_{d},w_{d})$ satisfying the above equations is called (Pontryagin) extremal for $\text{OCP}_{d}$. These equations indicate that the adjoint vector is non-zero at all times.

### Lemma 4 (No singular arcs)

Assume that $(f,g,\mathcal{W})$ satisfy Assumptions LABEL:assumption:f-LABEL:assumption:W. Let $(x_{d},p_{d},w_{d})$ be an extremal for $\text{OCP}_{d}$ with $d \in \mathcal{S}^{n - 1}$. Then, ${p_{d}{(t)}} \neq 0$ and ${p_{d}{(t)}^{\top}g{(t,{x_{d}{(t)}})}} \neq 0$ for every $t \in {\lbrack 0,T\rbrack}$.

### Proof 5.1

By contradiction, ${p_{d}{(t)}} = 0$ for some $t \in {\lbrack 0,T\rbrack}$. Then, $0$ is the unique solution to the ODE ${\overset{˙}{p}{(s)}} = {\text{(}\text{)}}$ for $s \in {\lbrack t,T\rbrack}$ with ${p{(t)}} = 0$. Thus, we obtain ${d{\overset{\text{(}\text{)}}{=}{p_{d}{(T)}}}} = 0$, which is a contradiction. The result ${p_{d}{(t)}^{\top}g{(t,{x_{d}{(t)}})}} \neq 0$ for $t \in {\lbrack 0,T\rbrack}$ follows from ${p_{d}{(t)}} \neq 0$ for $t \in {\lbrack 0,T\rbrack}$ and Assumption LABEL:assumption:g.

Thanks to Lemma 4 ‣ 5.2 Reformulating "OCP"_𝑑 using the PMP to reduce the search of solutions from 𝐿^∞⁢([0,𝑇],𝒲) to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") and Assumption LABEL:assumption:W, the maximality condition (15c to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) can be simplified. First, since ${p_{d}{(t)}^{\top}g{(t,{x_{d}{(t)}})}} \neq 0$ for all $t \in {\lbrack 0,T\rbrack}$ thanks to Lemma 4 ‣ 5.2 Reformulating "OCP"_𝑑 using the PMP to reduce the search of solutions from 𝐿^∞⁢([0,𝑇],𝒲) to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets"), (15c to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) is well-defined. Second, since $\mathcal{W}$ is convex and $v\mapsto{p_{d}{(t)}^{\top}g{(t,{x_{d}{(t)}})}v}$ is linear, searching for disturbances in $\partial\mathcal{W}$ suffices. Then,

where $n^{\partial\mathcal{W}}:{{\partial\mathcal{W}}\rightarrow\mathcal{S}^{n - 1}}$ is the Gauss map in (8 ‣ Convex Hulls of Reachable Sets")), which is a diffeomorphism since $\partial\mathcal{W}$ is an ovaloid \[Rauch1974\] by Assumption LABEL:assumption:W. The last equality in (16 to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) follows from (9 ‣ Convex Hulls of Reachable Sets")) (note that ${\text{(}\text{)}} = 0$ if and only if $v = {w{(t)}}$, due to the strict convexity of $\partial\mathcal{W}$). Thus, by combining (15 to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) and (16 to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")), we obtain that candidate optimal solutions of $\text{OCP}_{d}$ must solve the boundary-value problem (BVP)

With $\text{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets"), we reduced the search of solutions to $\text{OCP}_{d}$ from $w \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}$ to ${p_{d}{}} \in {\mathbb{R}}^{n}$.

### Reformulating $\text{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") with knowledge of $\frac{p_{d}\hspace{0pt}{(0)}}{\|{p_{d}\hspace{0pt}{(0)}}\|}$

$\text{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") and (16 to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) indicate that extremal state trajectories $x_{d}$ follow dynamics that only depend on $\frac{p_{d}}{\| p_{d}\|}$. The next result shows that extremal trajectories are independent of the norm of $p_{d}{}$. Thus, it suffices to search over $\mathcal{S}^{n - 1}$ to retrieve extremal trajectories $x_{d}$.

### Lemma 5.2 (Extremals of OCP are identified by $\frac{p\hspace{0pt}{(0)}}{\|{p\hspace{0pt}{(0)}}\|}$)

Assume that $(f,g,\mathcal{W})$ satisfy Assumptions LABEL:assumption:f-LABEL:assumption:W. Let $d \in \mathcal{S}^{n - 1}$ and $(x_{d},p_{d},w_{d})$ be an extremal for $\text{OCP}_{d}$. Then, there exist a direction $d^{0} \in \mathcal{S}^{n - 1}$ and an adjoint trajectory $\overset{\sim}{p}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{n}}$ with ${\overset{\sim}{p}{}} = d^{0}$ such that $(x_{d},\overset{\sim}{p},w_{d})$ solves $\text{ODE}_{d^{0}}$ with $\mathcal{X}_{0} = {\{ x^{0}\}}$.

### Proof 5.3

First, for all $t \in {\lbrack 0,T\rbrack}$, we define

which is well-defined for all $t \in {\lbrack 0,T\rbrack}$ thanks to Lemma 4 ‣ 5.2 Reformulating "OCP"_𝑑 using the PMP to reduce the search of solutions from 𝐿^∞⁢([0,𝑇],𝒲) to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") and such that ${q_{d}{}} = \frac{p_{d}{}}{\|{p_{d}{}}\|} \in \mathcal{S}^{n - 1}$. We define

and write ${(x_{t},p_{t},w_{t},q_{t})} = {({x_{d}{(t)}},{p_{d}{(t)}},{w_{d}{(t)}},{q_{d}{(t)}})}$ for conciseness. As $(x,p,w)$ is an extremal for $\text{OCP}_{d}$,

${w_{t}{\overset{\text{(}\text{)}}{=}{\left( n^{\partial\mathcal{W}} \right)^{- 1}\left( \frac{q_{t}^{\top}g{(t,x_{t})}}{\|{q_{t}^{\top}g{(t,x_{t})}}\|} \right)}}},$ (20a)
${{{\overset{˙}{x}}_{t}{\overset{\text{(}\text{)}}{=}{f{(t,x_{t})}}}} + {g{(t,x_{t})}w_{t}}},$ (20b)
${\overset{\text{(}\text{)}}{=} - {\left( {I_{n} - {q_{t}q_{t}^{\top}}} \right){({{{\nabla f}{(t,x_{t})}} + {{\nabla g}{(t,x_{t})}w_{t}}})}^{\top}q_{t}}},$ (20c)
${q_{0}{\overset{\text{(}\text{)}}{=}d^{0}}}.$ (20d)

Next, let $(\overset{\sim}{x},\overset{\sim}{p},\overset{\sim}{w})$ be the solution to $\text{ODE}_{d^{0}}$ and define $\overset{\sim}{q} = \frac{\overset{\sim}{p}}{\|\overset{\sim}{p}\|}$. We claim that ${(\overset{\sim}{x},\overset{\sim}{w})} = {(x,w)}$. Indeed,

${{\overset{\sim}{w}}_{t} = {\left( n^{\partial\mathcal{W}} \right)^{- 1}\left( \frac{{\overset{\sim}{q}}_{t}^{\top}g{(t,{\overset{\sim}{x}}_{t})}}{\|{{\overset{\sim}{q}}_{t}^{\top}g{(t,{\overset{\sim}{x}}_{t})}}\|} \right)}},$ (21a)
${{\overset{˙}{\overset{\sim}{x}}}_{t} = {{f{(t,{\overset{\sim}{x}}_{t})}} + {g{(t,{\overset{\sim}{x}}_{t})}{\overset{\sim}{w}}_{t}}}},$ (21b)
${{\overset{˙}{\overset{\sim}{q}}}_{t} = {- {{({I_{n} - {{\overset{\sim}{q}}_{t}{\overset{\sim}{q}}_{t}^{\top}}})}{({{{\nabla f}{(t,{\overset{\sim}{x}}_{t})}} + {{\nabla g}{(t,{\overset{\sim}{x}}_{t})}{\overset{\sim}{w}}_{t}}})}^{\top}{\overset{\sim}{q}}_{t}}}},$ (21c)

By uniqueness of solutions to ODEs, from (20/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) and (21/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")), we conclude that ${(\overset{\sim}{x},\overset{\sim}{q},\overset{\sim}{w})} = {(x,q,w)}$, and in particular that ${(\overset{\sim}{x},\overset{\sim}{w})} = {(x,w)}$. The conclusion follows.

### Concluding the proof of Theorem LABEL:thm:hull_F

Lemma 5.2/‖𝑝⁢‖). ‣ 5.3 Reformulating "BVP"_𝑑 with knowledge of 𝑝_𝑑⁢/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") yields the following key result.

### Lemma 5.4

Assume that $f$, $g$, and $\mathcal{W}$ satisfy Assumptions LABEL:assumption:f-LABEL:assumption:W, $\mathcal{X}_{0}$ satisfies Assumption LABEL:assumption:X0 with A4a ($\mathcal{X}_{0} = {\{ x^{0}\}}$ is a singleton), and define $F = {\text{(}\text{)}}$ as in Theorem LABEL:thm:hull_F. Then, for all $t \in {\lbrack 0,T\rbrack}$, $F{( \cdot,t)}$ is smooth and

### Proof 5.5

Without loss of generality, we prove the result for $t = T$. The proof can be extended to $t \in {\lbrack 0,T)}$ by defining $\text{OCP}_{d}$ ^t^ to maximize $d^{\top}x{(t)}$, which results in the same expressions for ODE and $F$.

First, $F{( \cdot,T)}$ is smooth since it is the solution to an ODE with smooth coefficients.

Second, ${F{(\mathcal{S}^{n - 1},T)}} \subseteq \mathcal{X}_{T}$ by definition. To show the other inclusion, let $y \in {{\partial{\text{H}{(\mathcal{X}_{T})}}} \cap \mathcal{X}_{T}}$. Since $y \in \mathcal{X}_{T}$, there exists some $w \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}$ such that $y = {x_{w}{(T)}}$ where $x_{w}$ solves the ODE in. Then, since ${x_{w}{(T)}} = y \in {\partial{\text{H}{(\mathcal{X}_{T})}}}$, by the convexity of $\text{H}{(\mathcal{X}_{T})}$ and Lemma 1 ‣ 3.0.2 Convex geometry ‣ 3 Notations and preliminary results ‣ Convex Hulls of Reachable Sets"), $x_{w}{(T)}$ maximizes the function $\overset{\sim}{w}\mapsto{d^{\top}x_{\overset{\sim}{w}}{(T)}}$ over $\overset{\sim}{w} \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}$ for some $d \in \mathcal{S}^{n - 1}$, i.e., $(x_{w},w)$ solves $\text{OCP}_{d}$. Thus, by Lemma 5.2/‖𝑝⁢‖). ‣ 5.3 Reformulating "BVP"_𝑑 with knowledge of 𝑝_𝑑⁢/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets"), $x_{w}$ solves $\text{ODE}_{d^{0}}$ for some $d^{0} \in \mathcal{S}^{n - 1}$. We obtain $y = {x_{w}{(T)}} = {F{(d^{0},T)}} \in {F{(\mathcal{S}^{n - 1},T)}}$.

Theorem LABEL:thm:hull_F (for the case where $\mathcal{X}_{0} = {\{ x^{0}\}}$) almost immediately follows from Lemmas 2 and 5.4. To prove the case where $\partial\mathcal{X}_{0}$ is an ovaloid, we define a dynamical system with the same reachable sets but with a fixed initial state and conclude with the previous result.

Proof of Theorem LABEL:thm:hull_F if $\mathcal{X}_{0} = {\{ x^{0}\}}$ (Assumption LABEL:assumption:X0 holds with A4a): For any $t \in {\lbrack 0,T\rbrack}$, ${\text{H}{(\mathcal{X}_{t})}} = {\text{H}{({F{(\mathcal{S}^{n - 1},t)}})}}$ follows from taking the convex hull on both sides of and using ${\text{H}\left( {{\partial{\text{H}{(\mathcal{X}_{t})}}} \cap \mathcal{X}_{t}} \right)} = {\text{H}{(\mathcal{X}_{t})}}$ (Lemma 2) since $\mathcal{X}_{t}$ is compact (Lemma 3 ‣ 4 The structure of "H"⁢(𝒳_𝑡) ‣ Convex Hulls of Reachable Sets")). $\blacksquare$

Proof of Theorem LABEL:thm:hull_F if $\partial\mathcal{X}_{0}$ is an ovaloid (Assumption LABEL:assumption:X0 holds with A4b): We define the new ODE

where $w \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}$ and $v \in {L^{\infty}{({\lbrack{- 1},0\rbrack},\mathcal{X}_{0})}}$. Under Assumptions LABEL:assumption:f-LABEL:assumption:X0, this ODE has a unique solution, denoted by ${\overset{\sim}{x}}_{(w,v)}{( \cdot )}$. We define the reachable sets ${\overset{\sim}{\mathcal{X}}}_{t} = \left\{ {{\overset{\sim}{x}}_{(w,v)}{(t)}}:{{w \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}},{v \in {L^{\infty}{({\lbrack{- 1},0\rbrack},\mathcal{X}_{0})}}}} \right\}$ for $t \in {\lbrack{- 1},T\rbrack}$. By definition, ${\overset{\sim}{\mathcal{X}}}_{0} = \mathcal{X}_{0}$ and

Table 1: Problems used to prove Theorem LABEL:thm:hull_F.

Given any $d^{0} \in \mathcal{S}^{n - 1}$, we define the ODE

which has a unique solution ${(\overset{\sim}{x},\overset{\sim}{p})}_{d^{0}} \in {C{({\lbrack{- 1},T\rbrack},{\mathbb{R}}^{2n})}}$ thanks to Assumptions LABEL:assumption:f-LABEL:assumption:X0, and the map

Theorem LABEL:thm:hull_F (with fixed initial condition ${\overset{\sim}{x}{({- 1})}} = \, 0$) gives

Next, from ${\overset{\sim}{\text{ODE}}}_{d^{0}}$, ${\overset{\sim}{p}{(t)}} = d^{0}$ for all $t \in {\lbrack{- 1},0\rbrack}$, so ${\overset{\sim}{v}{(t)}} = {{(n^{\partial\mathcal{X}_{0}})}^{- 1}{(d^{0})}}$ for all $t \in {\lbrack{- 1},0\rbrack}$, and

Thus, ${\overset{\sim}{\text{ODE}}}_{d^{0}}$ restricted to $t \in {\lbrack 0,T\rbrack}$ from is exactly $\text{ODE}_{d^{0}}$, which concludes the proof of Theorem LABEL:thm:hull_F. $\blacksquare$

### Discussion and insights

In Table 1, we summarize the different problems used to derive $\text{ODE}_{d^{0}}$ and ultimately prove Theorem LABEL:thm:hull_F.

At first sight, $\text{OCP}_{d}$ and $\text{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") suggest using Algorithm LABEL:alg:2 to reconstruct the convex hull of the reachable set $\text{H}{(\mathcal{X}_{T})}$ (similar ideas are investigated in \[Gornov2015\] and in \[Baier2009\]). However, this procedure can be computationally expensive. Also, $\text{OCP}_{d}$ is generally non-convex, so Algorithm LABEL:alg:2 could be prone to local minima and under-estimating the reachable sets. Thus, Algorithm LABEL:alg:2 may be unsuitable for applications that require efficient reachable set over-approximations. Carrying on the analysis using samples of ${p_{d}{}} \in \mathcal{S}^{n - 1}$ and observing that the norm of $p_{d}{(t)}$ does not play a role in the problem (Section 5.3/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) is key to our result.

Lemma 5.2/‖𝑝⁢‖). ‣ 5.3 Reformulating "BVP"_𝑑 with knowledge of 𝑝_𝑑⁢/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") implies that extremal trajectories are completely specified by the initial value of the adjoint vector ${p_{d}{}} \in \mathcal{S}^{n - 1}$. Thus, given ${p_{d}{}} = d^{0}$, we can integrate $\text{ODE}_{d^{0}}$ to obtain the corresponding reachable extremal states $x_{d}{(t)}$, independently of the search direction $d$ (as $d$ is implicitly encoded in $p_{d}{}$). This observation is the key insight behind Algorithm LABEL:alg:1, that consists of integrating $\text{ODE}_{d^{0}}$ for different values of $d^{0} \in \mathcal{S}^{n - 1}$ to recover the convex hulls of the reachable sets. To gain further intuition with the linear case, see Appendix.1.

## The boundary structure of $\text{H}\hspace{0pt}{(\mathcal{X}_{t})}$, geometric estimation, and error bounds

How accurate are the estimates returned by Algorithm LABEL:alg:1, which approximates the reachable convex hulls $\text{H}{(\mathcal{X}_{t})}$ with the convex hulls of a finite number of state trajectories? First, we show that the boundaries of the convex hulls of reachable sets are smooth submanifolds under Assumptions LABEL:assumption:f-LABEL:assumption:X0 (Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")). This smooth boundary structure implies tight error bounds for convex-hull sampling-based estimators (Theorem LABEL:thm:error_bound). Indeed, error bounds of sample-based approximations typically rely on smoothness properties of the functions of interest and on sufficient coverage of the samples, as shown below.

### Corollary 6.6 (Naive error bound)

Assume that $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ satisfy Assumptions LABEL:assumption:f-LABEL:assumption:X0. Let $\delta > 0$, $Z_{\delta} \subset \mathcal{S}^{n - 1}$ be a $\delta$-cover of $\mathcal{S}^{n - 1}$ (i.e., $\mathcal{S}^{n - 1} \subset {Z_{\delta} + {B{(0,\delta)}}}$), and define $F = {\text{(}\text{)}}$. Then

where ${\overline{L}}_{t}$ denotes the Lipschitz constant^22^2$F{( \cdot,t)}$ is Lipschitz since it is differentiable and $\mathcal{S}^{n - 1}$ is compact. of $F{( \cdot,t)}$.

Corollary 6.6. ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets") follows from Theorem LABEL:thm:hull_F using a standard covering argument, see \[LewBonalliJansonPavone2023, Lemma 4.2\]. It implies that given a sufficiently-dense sample $Z_{\delta} = {\{ d^{i}\}}_{i = 1}^{M}$ that $\delta$-covers $\mathcal{S}^{n - 1}$, padding the set estimates from Algorithm LABEL:alg:1 by $\epsilon_{t} = {{\overline{L}}_{t}\delta}$ suffices to obtain over-approximations of the reachable sets $\mathcal{X}_{t}$. However, Corollary 6.6. ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets") does not fully exploit the smoothness of the sets of interest.

### Lemma 6.7 ($\partial{\text{H}\hspace{0pt}{(\mathcal{X}_{t})}}$ is smooth)

Assume that $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ satisfy Assumptions LABEL:assumption:f-LABEL:assumption:X0. Then, $\partial{\text{H}{(\mathcal{X}_{t})}}$ is an $({n - 1})$-dimensional submanifold of ${\mathbb{R}}^{n}$ for any $t > 0$.

The proof of Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets") uses the structure of extremal trajectories and is in Section 7.^33^3A version of Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets") quantifying the smoothness of the boundary $\partial{\text{H}{(\mathcal{X}_{t})}}$ can be derived by combining the interior smoothness properties of reachable sets in \[Lorenz2005, Cannarsa2006\] and of convex hulls in \[LewBonalliJansonPavone2023\]. Thanks to the smoothness of the dynamics, of the input set $\mathcal{S}^{n - 1}$ for the map $F$, and of the reachable convex hull boundary $\partial{\text{H}{(\mathcal{X}_{t})}}$ (see \[LewBonalliJansonPavone2023\] for a quantitative definition of smoothness of sets), Algorithm LABEL:alg:1 admits the following error bounds.

The error bound in (29, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")) is quadratic in $\delta$. It is thus tighter than the naive error bound in Corollary 6.6. ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets") for smaller values of $\delta$ (i.e., for sufficiently-many samples of $d^{0}$ so that $\delta \leq {{({2{\overline{L}}_{t}})}/{({{\overline{L}}_{t} + {\overline{H}}_{t}})}}$).

According to Theorem LABEL:thm:error_bound, the sample complexity of Algorithm LABEL:alg:1 is exponential in the dimension of the sample space $\mathcal{S}^{n - 1}$, as the minimum number of samples to $\delta$-cover a compact set scales exponentially with the dimension of the set \[wainwright_2019, Eq.(5.9)\], so the performance of Algorithm LABEL:alg:1 may degrade as the state dimension $n$ increases. This limitation is shared by other algorithms and is known as the curse of dimensionality. Nevertheless, thanks to Theorem LABEL:thm:hull_F, the sample space is only of dimension $({n - 1})$ as opposed to an infinite-dimensional space of disturbances, so we expect better performance than if naively sampling disturbances, see Section 11.

### Remark 6.8 (Proving Theorem LABEL:thm:error_bound)

The proof of Theorem LABEL:thm:error_bound relies on Theorem LABEL:thm:hull_F. It takes inspiration from \[LewBonalliJansonPavone2023, Theorem 1.1\], but requires new analysis due to several difficulties. First, the map $F{( \cdot,t)}$ is not a diffeomorphism onto its image: $\mathcal{S}^{n - 1}$ is an $({n - 1})$-dimensional submanifold of ${\mathbb{R}}^{n}$, but the set $F{(\mathcal{S}^{n - 1},t)}$ may self-intersect and is thus not a submanifold of ${\mathbb{R}}^{n}$, see Example LABEL:example:selfintersect. $F$ is neither a submersion: ${\text{d}F{(d^{0},t)}}:{{T_{d^{0}}\mathcal{S}^{n - 1}}\rightarrow{T_{F{(d^{0},t)}}{\mathbb{R}}^{n}}}$ cannot be surjective since $\mathcal{S}^{n - 1}$ is only $({n - 1})$-dimensional. To prove Theorem LABEL:thm:error_bound, we exploit properties of solutions to $\text{ODE}_{d^{0}}$ and of $F$. Theorem LABEL:thm:error_bound relies on Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"), whose proof relies on the PMP and the structure of extremal trajectories from the PMP coupled with properties of convex sets.

## Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")

First, we prove that $\partial{\text{H}{(\mathcal{X}_{t})}}$ is a submanifold of ${\mathbb{R}}^{n}$ of dimension $({n - 1})$ (Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")). The analysis leverages Theorem LABEL:thm:hull_F and properties of convex sets.

Proof of Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"): $\text{H}{(\mathcal{X}_{t})}$ is convex, compact (Lemma 3 ‣ 4 The structure of "H"⁢(𝒳_𝑡) ‣ Convex Hulls of Reachable Sets")), and has interior points (${\text{Int}{(\mathcal{X}_{t})}} \neq \varnothing$ since the reachable state $x_{w}{(t)}$ associated to the disturbance ${w{( \cdot )}} = 0$ is clearly in $\text{Int}{(\mathcal{X}_{t})}$). Thus, by \[Schneider2014, Theorem 2.2.4\], it suffices to prove that there is a unique support hyperplane to $\text{H}{(\mathcal{X}_{t})}$ at any boundary point $x \in {\partial{\text{H}{(\mathcal{X}_{t})}}}$. In the following, as in the proof of Lemma 5.4, we prove the result for $t = T$ without loss of generality.

First, let $x \in {{\partial{\text{H}{(\mathcal{X}_{T})}}} \cap {F{(\mathcal{S}^{n - 1},T)}}}$. As $x \in {\partial{\text{H}{(\mathcal{X}_{T})}}}$, by Lemma 1 ‣ 3.0.2 Convex geometry ‣ 3 Notations and preliminary results ‣ Convex Hulls of Reachable Sets"), there exists a support hyperplane $\{{y \in {\mathbb{R}}^{n}}:{{d^{\top}{({y - x})}} = 0}\}$ for $\text{H}{(\mathcal{X}_{T})}$ at $x$ parameterized by some $d \in \mathcal{S}^{n - 1}$ such that ${d^{\top}x} \geq {d^{\top}y}$ for all $y \in {\text{H}{(\mathcal{X}_{T})}}$. In particular, since $\mathcal{X}_{T} \subseteq {\text{H}{(\mathcal{X}_{T})}}$,

As $x \in {F{(\mathcal{S}^{n - 1},T)}}$, there exists some $d^{0} \in \mathcal{S}^{n - 1}$ and $(x_{w},p_{w},w)$ that solve $\text{ODE}_{d^{0}}$ with $x = {x_{w}{(T)}}$. Then, by, ${d^{\top}x} = {d^{\top}x_{w}{(T)}} \geq {d^{\top}y}$ for all $y \in \mathcal{X}_{T}$, so $(x_{w},w)$ solves $\text{OCP}_{d}$. Define ${q_{w}{(t)}} = {{p_{w}{(t)}}/{\|{p_{w}{(t)}}\|}}$ as in (18/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")). Then, ${q_{w}{(T)}} = d$ by (15b to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")), so ${w{(T)}} = {{(n^{\partial\mathcal{W}})}^{- 1}{({{g{(T,x)}^{\top}d}/{\|{g{(T,x)}^{\top}d}\|}})}}$.

Figure 4: Two support hyperplanes at x = xw (T).

By contradiction (see Figure 4), assume that there is a different support hyperplane for $\text{H}{(\mathcal{X}_{T})}$ at $x = {x_{w}{(T)}}$ parameterized by $\overset{\sim}{d} \in \mathcal{S}^{n - 1}$ with $\overset{\sim}{d} \neq d$. Then, since ${{\overset{\sim}{d}}^{\top}x} \geq {{\overset{\sim}{d}}^{\top}y}$ for all $y \in \mathcal{X}_{T}$, from the previous reasoning, the same trajectory $(x_{w},w)$ also solves $\text{OCP}_{\overset{\sim}{d}}$. Thus, $w$ satisfies ${w{(T)}} = {{(n^{\partial\mathcal{W}})}^{- 1}{({{g{(T,x)}^{\top}\overset{\sim}{d}}/{\|{g{(T,x)}^{\top}\overset{\sim}{d}}\|}})}}$. This is a contradiction, since $g{(T,x)}$ is invertible by Assumption LABEL:assumption:g, $n^{\partial\mathcal{W}}$ is a diffeomorphism by Assumption LABEL:assumption:W, and $\overset{\sim}{d} \neq d$. Thus, $x$ has a unique support hyperplane.

Second, we consider boundary points that are not in $F{(\mathcal{S}^{n - 1},T)}$. Let $x \in {{\partial{\text{H}{(\mathcal{X}_{T})}}} \smallsetminus {F{(\mathcal{S}^{n - 1},T)}}}$. As ${\text{Ext}{({\text{H}{({F{(\mathcal{S}^{n - 1},T)}})}})}} \subseteq {F{(\mathcal{S}^{n - 1},T)}}$ (Lemma 2) and ${\text{H}{(\mathcal{X}_{T})}} = {\text{H}{({F{(\mathcal{S}^{n - 1},T)}})}}$ (Theorem LABEL:thm:hull_F), $x$ is not an extreme point. Thus, $x$ can be written as $x = {{\alphax_{1}} + {{({1 - \alpha})}x_{2}}}$ for some $\alpha \in {}$, $x_{1} \in {\text{H}{(\mathcal{X}_{T})}}$, and $x_{2} \in {{\partial{\text{H}{(\mathcal{X}_{T})}}} \cap {F{(\mathcal{S}^{n - 1},T)}}}$ (see the proof of Lemma 2 and note that ${\text{H}{(\mathcal{X}_{T})}} = {\text{H}{({{\partial{\text{H}{(\mathcal{X}_{T})}}} \cap {F{(\mathcal{S}^{n - 1},T)}}})}}$ by Theorem LABEL:thm:hull_F and Lemma 2). Since $x \in {\partial{\text{H}{(\mathcal{X}_{T})}}}$, there is a support hyperplane $H = {\{{y \in {\mathbb{R}}^{n}}:{{d^{\top}{({y - x})}} = 0}\}}$ at $x$ parameterized by some $d \in \mathcal{S}^{n - 1}$ such that ${d^{\top}x} \geq {d^{\top}y}$ for all $y \in {\text{H}{(\mathcal{X}_{T})}}$. Thus,

from which one can show that ${d^{\top}x} = {d^{\top}x_{1}} = {d^{\top}x_{2}}$. Thus, $H$ is a support hyperplane at $x_{2}$. Since $x_{2}$ has a unique support hyperplane as shown previously, we conclude that $H$ is the unique support hyperplane at $x$. This concludes the proof of Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"). $\blacksquare$

The proof of Theorem LABEL:thm:error_bound relies on the fact that $F$ maps tangent spaces of $\mathcal{S}^{n - 1}$ to tangent spaces of $\partial{\text{H}{(\mathcal{X}_{t})}}$.

### Lemma 7.9 (Tangent vectors map to tangent vectors)

Assume that $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ satisfy Assumptions LABEL:assumption:f-LABEL:assumption:X0. Let $t \in {(0,T\rbrack}$, and define ${F^{t}{( \cdot )}} = {F{( \cdot,t)}}$. Then,

for all $x \in {{\partial{\text{H}{(\mathcal{X}_{t})}}} \cap {F{(\mathcal{S}^{n - 1},t)}}}$, where $x = {F{(d^{0},t)}}$ and $d^{0} \in \mathcal{S}^{n - 1}$.

### Proof 7.10

By Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"), each tangent space $T_{x}{\partial{\text{H}{(\mathcal{X}_{t})}}}$ is well-defined and of dimension $({n - 1})$. Next, let $t \in {(0,T\rbrack}$ and $x \in {{\partial{\text{H}{(\mathcal{X}_{t})}}} \cap {F{(\mathcal{S}^{n - 1},t)}}}$ be such that $x = {F{(d^{0},t)}}$ for some $d^{0} \in \mathcal{S}^{n - 1}$.

By contradiction, let $v \in {T_{d^{0}}\mathcal{S}^{n - 1}}$ be a tangent vector such that ${\text{d}F_{d^{0}}^{t}{(v)}} \notin {T_{x}{\partial{\text{H}{(\mathcal{X}_{t})}}}}$. Then, there exists a smooth curve $\gamma:{{({- \epsilon},\epsilon)}\rightarrow\mathcal{S}^{n - 1}}$ such that ${\gamma{}} = d^{0}$ and ${\gamma^{\prime}{}} = v$. Define the smooth curve $\alpha:{{({- \epsilon},\epsilon)}\rightarrow{\mathbb{R}}^{n}}$ by ${\alpha{(r)}} = {F^{t}{({\gamma{(r)}})}}$ and note that ${\alpha{(r)}} \in \mathcal{X}_{t}$ for all $r \in {({- \epsilon},\epsilon)}$ by Theorem LABEL:thm:hull_F. Since ${\alpha^{\prime}{}} = {\text{d}F_{d^{0}}^{t}{(v)}} \notin {T_{x}{\partial{\text{H}{(\mathcal{X}_{t})}}}}$, by \[LewBonalliJansonPavone2023, Lemma 4.6\], there exists some $s \in {({- \epsilon},\epsilon)}$ such that ${\alpha{(s)}} \notin {\text{H}{(\mathcal{X}_{t})}}$. This is a contradiction, since ${\alpha{(s)}} \in \mathcal{X}_{t} \subseteq {\text{H}{(\mathcal{X}_{t})}}$.

Finally, Theorem LABEL:thm:error_bound follows from combining Lemmas 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")-7.9. ‣ 7 Proofs of Theorem and Lemma 6.7 ‣ Convex Hulls of Reachable Sets") and recent geometric results in \[LewBonalliJansonPavone2023\].

Proof of Theorem LABEL:thm:error_bound: First, each tangent space $T_{x}{\partial{\text{H}{(\mathcal{X}_{t})}}}$ at $x \in {\partial{\text{H}{(\mathcal{X}_{t})}}}$ is well-defined by Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"). Then, for all $x \in {{\partial{\text{H}{(\mathcal{X}_{t})}}} \cap {F{(\mathcal{S}^{n - 1},t)}}}$ and ${d^{0},z} \in \mathcal{S}^{n - 1}$ with $x = {F{(d^{0},t)}}$,

by \[LewBonalliJansonPavone2023, Lemma 4.4\] and due to Lemma 7.9. ‣ 7 Proofs of Theorem and Lemma 6.7 ‣ Convex Hulls of Reachable Sets") (the proof of \[LewBonalliJansonPavone2023, Lemma 4.4\] applies to our setting by replacing the use of\[LewBonalliJansonPavone2023, Lemma 4.7\] with Lemma 7.9. ‣ 7 Proofs of Theorem and Lemma 6.7 ‣ Convex Hulls of Reachable Sets")). Moreover, applying \[LewBonalliJansonPavone2023, Lemma 4.3\] gives

The conclusion follows from and. $\blacksquare$

## Approximate characterization for rectangular uncertainty sets $\mathcal{W}$ and $\mathcal{X}_{0}$

In the next three sections, we relax Assumptions LABEL:assumption:g-LABEL:assumption:X0. First, we relax Assumptions LABEL:assumption:W and [(A4b)](2303.17674v5/assumption:X0), which state that $\partial\mathcal{W}$ and $\partial\mathcal{X}_{0}$ are ovaloids. These assumptions prevent using rectangular uncertainties, as defined below.

We propose an approximation scheme for problems with hyper-rectangular sets $(\mathcal{W},\mathcal{X}_{0})$ satisfying Assumptions LABEL:assumption:W_box and LABEL:assumption:X0_box. Given a relaxation parameter $\lambda > 1$, we use smooth inner- and outer-approximations of $(\mathcal{W},\mathcal{X}_{0})$, defined in as $\lambda$-norm ellipsoids. The approximation scheme is shown in Figure 5 and has three key properties.

The approximations of $(\mathcal{W},\mathcal{X}_{0})$ satisfy Assumptions LABEL:assumption:W and LABEL:assumption:X0, so the convex hulls of their associated reachable sets are characterized by Theorem LABEL:thm:hull_F.

The approximations either inner- or outer-bound $(\mathcal{W},\mathcal{X}_{0})$, so their reachable sets either inner- and outer-approximate the true reachable sets $\mathcal{X}_{t}$.

By choosing $\lambda$ large-enough, the approximations can be made arbitrarily close to $(\mathcal{W},\mathcal{X}_{0})$, so the resulting approximate reachable sets can be made arbitrarily close to the true reachable sets $\mathcal{X}_{t}$.

Combining these properties, we obtain arbitrarily-close inner- and outer-approximations of the convex hulls of the reachable sets $\mathcal{X}_{t}$ of dynamical systems with $(\mathcal{W},\mathcal{X}_{0})$ satisfying Assumptions LABEL:assumption:W_box and LABEL:assumption:X0_box. This characterization is given in Theorem LABEL:thm:hull_F:rect_lambda and is proved in Section 9. Below, we state this result and necessary definitions.

Given a relaxation parameter $\lambda > 1$, we define the maps ${\left( {n_{\lambda}^{\partial\mathcal{W}}} \right)^{- 1},\left( {n_{\lambda}^{\partial\mathcal{X}_{0}}} \right)^{- 1}}:{\mathcal{S}^{n - 1}\rightarrow{\mathbb{R}}^{n}}$ by

$\left( {\hat{}n_{\lambda}^{\partial\mathcal{W}}} \right)^{- 1}{(d)}$ ${= \frac{{d \odot {|d|}^{\frac{2 - \lambda}{\lambda - 1}} \odot \delta}{\overline{w}}^{\frac{\lambda}{\lambda - 1}}}{\left\| {|{{d \odot \delta}\overline{w}}|}^{\frac{1}{\lambda - 1}} \right\|_{\lambda}}},$ (34a)
$\left( {\hat{}n_{\lambda}^{\partial\mathcal{X}_{0}}} \right)^{- 1}{(d)}$ ${= {{\overline{x}}_{0} + \frac{{d \odot {|d|}^{\frac{2 - \lambda}{\lambda - 1}} \odot \delta}{\overline{x}}_{0}^{\frac{\lambda}{\lambda - 1}}}{\left\| {|{{d \odot \delta}{\overline{x}}_{0}}|}^{\frac{1}{\lambda - 1}} \right\|_{\lambda}}}},$ (34b)

for any $d \in \mathcal{S}^{n - 1}$, the under-approximation ODE

the maps ${\left( \hat{n_{\lambda}^{\partial\mathcal{W}}} \right)^{- 1},\left( \hat{n_{\lambda}^{\partial\mathcal{X}_{0}}} \right)^{- 1}}:{\mathcal{S}^{n - 1}\rightarrow{\mathbb{R}}^{n}}$ by

$\left( \hat{n_{\lambda}^{\partial\mathcal{W}}} \right)^{- 1}{(d)}$ ${= {n^{\frac{1}{\lambda}}\frac{{d \odot {|d|}^{\frac{2 - \lambda}{\lambda - 1}} \odot \delta}{\overline{w}}^{\frac{\lambda}{\lambda - 1}}}{\left\| {|{{d \odot \delta}\overline{w}}|}^{\frac{1}{\lambda - 1}} \right\|_{\lambda}}}},$ (35a)
$\left( \hat{n_{\lambda}^{\partial\mathcal{X}_{0}}} \right)^{- 1}{(d)}$ ${= {{\overline{x}}_{0} + {n^{\frac{1}{\lambda}}\frac{{d \odot {|d|}^{\frac{2 - \lambda}{\lambda - 1}} \odot \delta}{\overline{x}}_{0}^{\frac{\lambda}{\lambda - 1}}}{\left\| {|{{d \odot \delta}{\overline{x}}_{0}}|}^{\frac{1}{\lambda - 1}} \right\|_{\lambda}}}}},$ (35b)

for any $d \in \mathcal{S}^{n - 1}$, and the over-approximation ODE

The result below approximately characterizes the convex hulls of reachable sets of systems with rectangular sets $\mathcal{W}$ and $\mathcal{X}_{0}$. Importantly, the proposed approximations always inner- and outer-bound the true convex hulls and converge as the relaxation parameter $\lambda$ increases.

## Proof of Theorem LABEL:thm:hull_F:rect_lambda

First, we describe the smooth set approximation used in Theorem LABEL:thm:hull_F:rect_lambda. Given $\overline{x} \in {\mathbb{R}}^{n}$ and ${\delta\overline{x}} \in {\mathbb{R}}^{n}$ with ${\delta{\overline{x}}_{i}} > 0$ for all $i = {1,\ldots,n}$, we define the hyper-rectangular set

with the continuous function $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ defined as

For any $\lambda > 1$, we define the function $h_{\lambda}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ as

and, as shown in Figure 5, the associated sets

$\hat{}C_{\lambda}$ ${= {\{{x \in {\mathbb{R}}^{n}}:{{h_{\lambda}{(x)}} \leq 1}\}}},$ (43a)
$\hat{C_{\lambda}}$ ${= {\{{x \in {\mathbb{R}}^{n}}:{{h_{\lambda}{(x)}} \leq n^{\frac{2}{\lambda}}}\}}}.$ (43b)

We define the map $n^{\partial C_{\lambda}}:{{({{\mathbb{R}}^{n} \smallsetminus {\{ 0\}}})}\rightarrow\mathcal{S}^{n - 1}}$ by

and the maps ${{(n^{\partial{C_{\lambda}}})}^{- 1},{(n^{\partial\hat{C_{\lambda}}})}^{- 1}}:{\mathcal{S}^{n - 1}\rightarrow{\mathbb{R}}^{n}}$ by

$\left( n^{\partial{\hat{}C_{\lambda}}} \right)^{- 1}{(d)}$ ${= {\overline{x} + \frac{{d \odot {|d|}^{\frac{2 - \lambda}{\lambda - 1}} \odot \delta}{\overline{x}}^{\frac{\lambda}{\lambda - 1}}}{\left\| {|{{d \odot \delta}\overline{x}}|}^{\frac{1}{\lambda - 1}} \right\|_{\lambda}}}},$ (45a)
$\left( n^{\partial\hat{C_{\lambda}}} \right)^{- 1}{(d)}$ ${= {\overline{x} + {n^{\frac{1}{\lambda}}\frac{{d \odot {|d|}^{\frac{2 - \lambda}{\lambda - 1}} \odot \delta}{\overline{x}}^{\frac{\lambda}{\lambda - 1}}}{\left\| {|{{d \odot \delta}\overline{x}}|}^{\frac{1}{\lambda - 1}} \right\|_{\lambda}}}}}.$ (45b)

Figure 5: Smooth under- and over-approximations of a rectangular set C for different relaxation parameters λ. As λ increases, the approximations converge to the set C.

### Lemma 9.11 (The sets $({\hspace{0pt}C_{\lambda}},\hat{C_{\lambda}})$ approximate $C$)

Let $\lambda > 1$ and define the sets $(C,{C_{\lambda}},\hat{C_{\lambda}})$ as in -(43b).

The sets $(C,{C_{\lambda}},\hat{C_{\lambda}})$ are convex, compact and

The sets $({C_{\lambda}},\hat{C_{\lambda}})$ approximate $C$ arbitrarily well by increasing $\lambda$:

${{d_{H}{({\hat{}C_{\lambda}},C)}}\rightarrow{0\text{~as~}\lambda}\rightarrow\infty},$ (47a)
${{d_{H}{(\hat{C_{\lambda}},C)}}\rightarrow{0\text{~as~}\lambda}\rightarrow\infty}.$ (47b)

The boundaries $({\partial{C_{\lambda}}},{\partial\hat{C_{\lambda}}})$ are ovaloids. Their Gauss maps are given by ${n^{\partial{C_{\lambda}}}{(x)}} = {n^{\partial C_{\lambda}}{(x)}}$ and ${n^{\partial\hat{C_{\lambda}}}{(x)}} = {n^{\partial C_{\lambda}}{(x)}}$, where the map $n^{\partial C_{\lambda}}$ is defined in. Their inverse Gauss maps ${(n^{\partial{C_{\lambda}}})}^{- 1}$ and ${(n^{\partial\hat{C_{\lambda}}})}^{- 1}$ are given by (45a) and (45b).

The proof of Lemma 9.11̂) approximate 𝐶). ‣ 9 Proof of Theorem ‣ Convex Hulls of Reachable Sets") is provided in Appendix A.2. With this result, we prove Theorem LABEL:thm:hull_F:rect_lambda.

Proof of Theorem LABEL:thm:hull_F:rect_lambda: First, we define the sets

$\hat{}\mathcal{W}^{\lambda}$ ${= {\{{w \in {\mathbb{R}}^{n}}:{{h_{\lambda}^{\mathcal{W}}{(w)}} \leq 1}\}}},$ (48a)
$\hat{}\mathcal{X}_{0}^{\lambda}$ ${= {\{{x \in {\mathbb{R}}^{n}}:{{h_{\lambda}^{\mathcal{X}}{(x)}} \leq 1}\}}},$ (48b)
$\hat{\mathcal{W}^{\lambda}}$ ${= {\{{w \in {\mathbb{R}}^{n}}:{{h_{\lambda}^{\mathcal{W}}{(w)}} \leq n^{\frac{2}{\lambda}}}\}}},$ (48c)
$\hat{\mathcal{X}_{0}^{\lambda}}$ ${= {\{{x \in {\mathbb{R}}^{n}}:{{h_{\lambda}^{\mathcal{X}}{(x)}} \leq n^{\frac{2}{\lambda}}}\}}},$ (48d)

where ${h_{\lambda}^{\mathcal{W}}{(w)}} = {\|{{w \odot \delta}{\overline{w}}^{- 1}}\|}_{\lambda}^{2}$ and ${h_{\lambda}^{\mathcal{X}}{(x)}} = {\|{{{({x - {\overline{x}}_{0}})} \odot \delta}{\overline{x}}_{0}^{- 1}}\|}_{\lambda}^{2}$ as in. By Lemma 9.11̂) approximate 𝐶). ‣ 9 Proof of Theorem ‣ Convex Hulls of Reachable Sets"), $({\mathcal{W}^{\lambda}},\hat{\mathcal{W}^{\lambda}})$ satisfy Assumption LABEL:assumption:W, $({\mathcal{X}_{0}^{\lambda}},\hat{\mathcal{X}_{0}^{\lambda}})$ satisfy Assumption LABEL:assumption:X0,

${{{\hat{}\mathcal{W}^{\lambda}} \subseteq \mathcal{W} \subseteq \hat{\mathcal{W}^{\lambda}}},{{\hat{}\mathcal{X}_{0}^{\lambda}} \subseteq \mathcal{X}_{0} \subseteq \hat{\mathcal{X}_{0}^{\lambda}}}},$ (49a)
${{\lim\limits_{\lambda\rightarrow 0}{d_{H}{({\hat{}\mathcal{W}^{\lambda}},\mathcal{W})}}} = {\lim\limits_{\lambda\rightarrow 0}{d_{H}{(\hat{\mathcal{W}^{\lambda}},\mathcal{W})}}} = 0},$ (49b)
${{\lim\limits_{\lambda\rightarrow 0}{d_{H}{({\hat{}\mathcal{X}_{0}^{\lambda}},\mathcal{X}_{0})}}} = {\lim\limits_{\lambda\rightarrow 0}{d_{H}{(\hat{\mathcal{X}_{0}^{\lambda}},\mathcal{X}_{0})}}} = 0},$ (49c)

and the inverse Gauss maps of $({\mathcal{W}^{\lambda}},{\mathcal{X}_{0}^{\lambda}},\hat{\mathcal{W}^{\lambda}},\hat{\mathcal{X}_{0}^{\lambda}})$ are given by ((34a), (34b), (35a), (35b)).

Second, we define the reachable sets

By definition and thanks to (49a), for all $t \in {\lbrack 0,T\rbrack}$,

By Theorem LABEL:thm:hull_F, for all $t \in {\lbrack 0,T\rbrack}$,

$\text{H}\left( {\hat{}\mathcal{X}_{t}^{\lambda}} \right)$ ${= {\text{H}\left( {\hat{}F_{\lambda}{(\mathcal{S}^{n - 1},t)}} \right)}},$ (51a)
$\text{H}\left( \hat{\mathcal{X}_{t}^{\lambda}} \right)$ ${= {\text{H}\left( {\hat{F_{\lambda}}{(\mathcal{S}^{n - 1},t)}} \right)}}.$ (51b)

Combining, (51a), and (51b) gives. Combining (49b), (49c) and a standard continuity result (see Lemma A.20. ‣ A.3 Small differences in dynamics, initial conditions, and disturbances imply small reachable set errors ‣ Appendix A Additional results and proofs ‣ Convex Hulls of Reachable Sets") in the appendix) gives (39a) and (39b). a $\blacksquare$

## Approximate characterization for non-invertible $g\hspace{0pt}{(t,x)}$

Assumption LABEL:assumption:g states that $g{(t,x)}$ is invertible, so Theorem LABEL:thm:hull_F does not directly apply to problems that have more states than disturbances. To relax this assumption, given two integers $m < n$, we consider the system

where ${x{}} \in \mathcal{X}_{0}$ with $\mathcal{X}_{0} \subset {\mathbb{R}}^{n}$ satisfying Assumption LABEL:assumption:X0, $w \in {L^{\infty}{({\lbrack 0,T\rbrack},\mathcal{W})}}$ with $\mathcal{W} \subset {\mathbb{R}}^{m}$ satisfying Assumption LABEL:assumption:W, $f$ satisfies Assumption LABEL:assumption:f, and ${g{(t,x)}} = {{(g_{1},\ldots,g_{m})}{(t,x)}} \in {\mathbb{R}}^{n \times m}$. The reachable sets of (10 ‣ Convex Hulls of Reachable Sets")) are defined as in and are denoted by $\mathcal{X}_{t}$. We relax the invertibility assumption on $g$ (Assumption LABEL:assumption:g) as follows.

Assumption LABEL:assumption:g:full_rank is standard and holds in many practical applications. By appropriately completing the range of $g$, we approximate the system (10 ‣ Convex Hulls of Reachable Sets")) with a system that has similar reachable sets and satisfies Assumption LABEL:assumption:f-LABEL:assumption:X0. First, we rely on the choice of a particular set $\hat{\mathcal{W}} \subset {\mathbb{R}}^{n}$. Below, ${\pi{(w_{1},\ldots,w_{m},w_{m + 1},\ldots,w_{n})}} = {(w_{1},\ldots,w_{m})}$ denotes the projection map.

Figure 6: Smooth approximation $\hat{\mathcal{W}}$ satisfying Assumption LABEL:assumption:Wbar:smooth_fulldim.

Second, we define ${\hat{g}}_{\epsilon}:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n \times n}}$ by

where $\epsilon > 0$ and the functions $g_{i}:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n}}$ with $i = {{m + 1},\ldots,n}$ are chosen as follows.

For $g{(t,x)}$ that is constant and satisfies Assumption LABEL:assumption:g:full_rank, choosing the maps $(g_{m + 1},\ldots,g_{n})$ with constant values sampled at random on the sphere $\mathcal{S}^{n - 1}$ (from a uniform distribution) suffices to satisfy Assumption LABEL:assumption:g_bar_epsilon. We refer to \[Silva2010\] for insightful discussion related to this assumption and to Section 11.1 for an example.

Third, we define the extended system

where ${x{}} \in \mathcal{X}_{0}$ and $\hat{w} \in {L^{\infty}{({\lbrack 0,T\rbrack},\hat{\mathcal{W}})}}$, with associated reachable sets denoted by ${\hat{\mathcal{X}}}_{t}^{\epsilon}$. The system (54 ‣ Convex Hulls of Reachable Sets")) satisfies the assumptions of Theorem LABEL:thm:hull_F. This suggests defining the following augmented ODE:

As stated below, solutions to $\text{ODE}_{d^{0}}^{\epsilon}$ characterize the convex hulls of the reachable sets $\mathcal{X}_{t}$ of the system (10 ‣ Convex Hulls of Reachable Sets")) arbitrarily well by selecting $\epsilon$ small-enough.

### Remark 10.12 (Error bounds and stable integration)

Error bounds for obtaining convex hull approximations of the reachable sets of system (10 ‣ Convex Hulls of Reachable Sets")) with Algorithm LABEL:alg:1 can be derived by combining (29, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")) and (57 ‣ Convex Hulls of Reachable Sets")).

The disturbances $\hat{w}{(t)}$ may become discontinuous as $\epsilon\rightarrow 0$, see \[Silva2010\]. Thus, a stable integration scheme should be used to integrate $\text{ODE}_{d^{0}}^{\epsilon}$ for small values of $\epsilon$, and similarly for ${\text{ODE}}_{d^{0}}^{\lambda}$ and $\hat{\text{ODE}_{d^{0}}^{\lambda}}$ for large values of $\lambda$.

### Proof 10.13

First, we define the intermediate system

with reachable sets ${\hat{\mathcal{X}}}_{t}$, where ${x{}} \in \mathcal{X}_{0}$, $\hat{w} \in {L^{\infty}{({\lbrack 0,T\rbrack},\hat{\mathcal{W}})}}$, and the map $\hat{g}:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n \times n}}$ is defined by ${\hat{g}{(t,x)}} = {\lbrack{g_{1}{(t,x)}},\ldots,{g_{m}{(t,x)}},0,\ldots,0\rbrack}$.

Since for any ${\hat{w}{(t)}} \in \hat{\mathcal{W}}$, we have ${\hat{g}{(t,{x{(t)}})}\hat{w}{(t)}} = {\sum_{i = 1}^{m}{g_{i}{(t,{x{(t)}})}{\hat{w}}_{i}{(t)}}}$ and ${{({\hat{w}}_{1},\ldots,{\hat{w}}_{m})}{(t)}} \in \mathcal{W}$, the reachable sets ${\hat{\mathcal{X}}}_{t}$ of system (58 ‣ Convex Hulls of Reachable Sets")) satisfy^55^5Note that Theorem LABEL:thm:hull_F does not give information about ${\hat{\mathcal{X}}}_{t}$, since $\hat{g}{(t,x)}$ is not invertible.

Second, given any ${w{(t)}} = {{(w_{1},\ldots,w_{m})}{(t)}} \in \mathcal{W}$, the extended disturbance ${\hat{w}{(t)}} = {{(w_{1},\ldots,w_{m},0,\ldots,0)}{(t)}}$ satisfies ${\hat{w}{(t)}} \in \hat{\mathcal{W}}$ and ${\hat{g}{(t,x)}\hat{w}{(t)}} = {{\hat{g}}_{\epsilon}{(t,x)}\hat{w}{(t)}}$. Thus, the reachable sets ${\hat{\mathcal{X}}}_{t}^{\epsilon}$ of the system (54 ‣ Convex Hulls of Reachable Sets")) satisfy

Applying Theorem LABEL:thm:hull_F to the system (54 ‣ Convex Hulls of Reachable Sets")) gives ${\text{H}{({\hat{\mathcal{X}}}_{t}^{\epsilon})}} = {\text{H}\left( {F_{\epsilon}{(\mathcal{S}^{n - 1},t)}} \right)}$. Combining this last result with (59 ‣ Convex Hulls of Reachable Sets")) and (60 ‣ Convex Hulls of Reachable Sets")) gives (56 ‣ Convex Hulls of Reachable Sets")).

To show (57 ‣ Convex Hulls of Reachable Sets")), note ${\|{\hat{g} - {\hat{g}}_{\epsilon}}\|}_{\infty} \leq \epsilon$, so ${d_{H}{({\hat{\mathcal{X}}}_{t},{\hat{\mathcal{X}}}_{t}^{\epsilon})}} \leq {C_{T}^{\hat{\mathcal{W}}}\epsilon}$ by a standard continuity result (Lemma A.20. ‣ A.3 Small differences in dynamics, initial conditions, and disturbances imply small reachable set errors ‣ Appendix A Additional results and proofs ‣ Convex Hulls of Reachable Sets") in the appendix). Thus, ${d_{H}{({\text{H}{({\hat{\mathcal{X}}}_{t})}},{\text{H}{({\hat{\mathcal{X}}}_{t}^{\epsilon})}})}} \leq {C_{T}^{\hat{\mathcal{W}}}\epsilon}$, so (57 ‣ Convex Hulls of Reachable Sets")) follows from (59 ‣ Convex Hulls of Reachable Sets")) and ${\text{H}{({\hat{\mathcal{X}}}_{t}^{\epsilon})}} = {\text{H}\left( {F_{\epsilon}{(\mathcal{S}^{n - 1},t)}} \right)}$.

## Results and applications

We evaluate Algorithm LABEL:alg:1 on three nonlinear systems, and use its reachable set estimates to design a robust model predictive controller (Algorithm LABEL:alg:mpc). Computation times are measured on a laptop with an 1.10GHz Intel Core i7-10710U CPU. Code to reproduce results is available at [https://github.com/StanfordASL/chreach](https://github.com/StanfordASL/chreach).

### Validating the relaxation schemes on Dubins car

Consider the dynamical system with state ${x{(t)}} = {{(p_{1},p_{2},\theta)}{(t)}} \in {\mathbb{R}}^{3}$ evolving according to the ODE $\overset{˙}{x}{(t)} = {(v\cos{(\theta{(t)})},v\sin\theta{(t)})},\omega) + Gw(t)$ with $t \in {\lbrack 0,6\rbrack}$, $v = \omega = 0.5$, $G \in {\mathbb{R}}^{3 \times m}$ a (constant) matrix, and ${x{}} \in \mathcal{X}_{0} = {\mathcal{E}{(0,{{10^{- 3} \cdot \text{diag}}{({\lbrack 1,1,10^{- 1}\rbrack})}})}}$. We consider two different choices of $g$ and $\mathcal{W}$ that violate Assumption LABEL:assumption:W ($\partial\mathcal{W}$ is an ovaloid in ${\mathbb{R}}^{n}$) and Assumption LABEL:assumption:g ($g{(t,x)}$ is invertible), which allows us to validate the relaxation schemes in Section 8 and 10 ‣ Convex Hulls of Reachable Sets").

### Rectangular disturbances set

Let $G = I_{3}$ and $\mathcal{W} \subset {\mathbb{R}}^{3}$ be the rectangular set in Assumption LABEL:assumption:W_box with ${\delta\overline{w}} = {10^{- 2}{}}$. As Assumption LABEL:assumption:W does not hold, we use the relaxation scheme in Section 8. We apply Algorithm LABEL:alg:1 to ${\text{ODE}}_{d^{0}}^{\lambda}$ and $\hat{\text{ODE}_{d^{0}}^{\lambda}}$ for different values of the relaxation parameter $\lambda$. Theorem LABEL:thm:hull_F:rect_lambda ensures that these approximations inner- and outer-approximate the true convex hulls of the reachable sets, and that these approximations converge as the relaxation parameter $\lambda$ increases. Indeed, the results in Figure 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") (left) show that the approximations converge as $\lambda$ increases.

### Non-invertible $g\hspace{0pt}{(t,x)}$

Let $G^{\top} = \begin{bmatrix}
\end{bmatrix}$ and $\mathcal{W} = {B{(0,10^{- 2})}} \subset {\mathbb{R}}^{2}$. As Assumption LABEL:assumption:g does not hold, we use the relaxation scheme in Section 10 ‣ Convex Hulls of Reachable Sets"). We apply Algorithm LABEL:alg:1 to $\text{ODE}_{d^{0}}^{\epsilon}$ using the approximation of $\mathcal{W}$ in Example LABEL:example:gauss_maps:not_full_rank and ${g_{3}{(t,x)}} = {}$. Since Assumptions LABEL:assumption:Wbar:smooth_fulldim and LABEL:assumption:g_bar_epsilon are satisfied, Theorem LABEL:thm:hull_F:not_full_rank guarantees that the approximations get closer to the true convex hulls of the reachable sets as the relaxation parameter $\epsilon$ decreases. Indeed, the results in Figure 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") (right) show that the approximations converge as $\epsilon$ decreases.

Figure 7: Output of Algorithm LABEL:alg:1 on Dubins car dynamics (Section 11.1) for different relaxation parameters. Left (rectangular disturbance set): inner- (dashed lines) and outer- (full lines) approximations using relaxation scheme in Theorem LABEL:thm:hull_F:rect_lambda. Right (non-invertible g (t,x)): outer-approximations using relaxation scheme in Theorem LABEL:thm:hull_F:not_full_rank.

Figure 8: Neural feedback loop analysis. Estimates of the reachable set convex hulls estimates (M = 103) and Monte-Carlo samples (in gray).

### Neural feedback loop analysis

Figure 9: Neural feedback loop analysis. Estimation error dH(H(𝒳T), H({xi}i = 1M) vs sample size and computation time.

Consider the system ${\overset{˙}{x}{(t)}} = {{Ax{(t)}} + {B\pi{({x{(t)}})}} + {w{(t)}}}$, where $\pi$ is a neural network and $n = 2$. The dynamics parameters $(A,B,\pi)$ are as in \[LewBonalliEtAl2023\] and \[Everett21_journal, Sec. VIII.A-C\]. The sets of initial conditions and disturbances $\mathcal{X}_{0}$ and $\mathcal{W}$ are ellipsoidal sets, see Appendix A.4 for details.

### Validating Theorem LABEL:thm:hull_F

We run Algorithm LABEL:alg:1 with $M = 10^{3}$ samples of $d^{0}$ evenly covering the circle $\mathcal{S}^{n - 1}$. Then, we uniformly sample $10^{5}$ disturbances ${w{(t)}} \in \mathcal{W}$ at each timestep and evaluate the corresponding trajectories. We verify that all resulting trajectories are within the convex hulls computed by Algorithm LABEL:alg:1, which empirically validates Theorem LABEL:thm:hull_F. Thus, using Algorithm LABEL:alg:1, it suffices to sample initial directions $d^{0} \in \mathcal{S}^{n - 1}$ to reconstruct the convex hulls of the reachable sets.

### Comparisons

We consider a first baseline that randomly samples disturbances ${w{(t)}} \in \mathcal{W}$ at each timestep and returns the convex hulls of closed-loop trajectories (RandUP \[LewJansonEtAl2022\]). As ground truth, we use Algorithm LABEL:alg:1 with a very large number of samples ($10^{4}$), which is justified by Theorem LABEL:thm:hull_F. We report results in Figures 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") and 9. Algorithm LABEL:alg:1 returns estimates that are orders of magnitude more accurate than the baseline's estimates. Given a desired accuracy, Algorithm LABEL:alg:1 is thus orders of magnitude faster than the baseline. This difference is a direct consequence of Theorem LABEL:thm:hull_F: only initial directions $d^{0}$ on the sphere $\mathcal{S}^{n - 1}$ need to be sampled using Algorithm LABEL:alg:1. In contrast, the baseline requires sampling a much larger number of variables that increases with the number of prediction timesteps, resulting in significantly worse sample complexity (see \[LewJansonEtAl2022, LewBonalliJansonPavone2023\] for error bounds) and trajectories that are far from the reachable set boundaries. Recall that Algorithm LABEL:alg:1 returns under-approximations of the convex hulls of the reachable sets, since any extremal trajectory $x_{d^{0}}$ solving $\text{ODE}_{d^{0}}$ is contained in the true reachable sets. These simulations show that naive Monte-Carlo estimates poorly approximate the convex hulls of the reachable sets for this problem.

In Figure 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") and 9, we also report the over-approximations from a formal method (ReachLP \[Everett21_journal\]) that significantly over-estimate the true reachable sets and is unable to capture the closed-loop stability of the system. In contrast, Algorithm LABEL:alg:1 returns accurate approximations using a small number of samples. Other reachability methods may return more accurate approximations for this type of problems \[ManzanasLopez2023\], albeit potentially at the expense of additional computation time.

### Robust MPC for attitude control of a spacecraft

We design an attitude controller for a spacecraft with state $x = {(q,\omega)} \in {\mathbb{R}}^{7}$, control $u \in {\mathbb{R}}^{3}$, and dynamics

$\overset{˙}{q}{(t)}$ ${= {\Omega{({\omega{(t)}})}q{(t)}}},$ (61a)

with ${x{}} = x^{0} = {(q^{0},\omega^{0})}$, ${w{(t)}} \in \mathcal{W} = {B{(0,10^{- 2})}}$, inertia matrix $J = {\text{diag}{}}$, and matrices ${(\Omega,S)}{(\omega)}$ defined in \[Leeman2023, LewBonalliEtAl2023\]. We constrain $\omega{(t)}$ and $u{(t)}$ as

We consider feedback controls parameterized as ${u{(t)}} = {{\overline{u}{(t)}} + {K\omega{(t)}}}$, where $\overline{u} \in {L^{\infty}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{3})}}$ is an open-loop control and $K = {- {\text{diag}{}}}$ is a feedback gain. To enforce, we define the reachable set

for any $\overline{u} \in {L^{\infty}{({\lbrack 0,T\rbrack},{\mathbb{R}}^{3})}}$ and $t \in {\lbrack 0,T\rbrack}$. The convex hulls of the reachable sets $\text{H}{({\mathcal{R}_{t}{(\overline{u})}})}$ can be estimated using Algorithm LABEL:alg:1, where $\text{ODE}_{d^{0}}$ is defined using (61b) with ${u{(t)}} = {{\overline{u}{(t)}} + {K\omega{(t)}}}$ and $\mathcal{X}_{0} = {\{ x^{0}\}}$ is a singleton. Thus, given $M$ samples $d^{i} \in \mathcal{S}^{n - 1}$ and $\epsilon_{t} > 0$ large-enough, the constraints can be approximated by

$${{{- 0.1} + \epsilon_{t}} \leq {\omega^{i}{(\overline{u},t)}_{j}} \leq {0.1 - \epsilon_{t}}},$$ (64a)
$${{{- 0.1} + \epsilon_{t}} \leq {({{\overline{u}{(t)}} + {K\omega^{i}{(\overline{u},t)}}})}_{j} \leq {0.1 - \epsilon_{t}}},$$ (64b)

for all $j = {1,2,3}$, $i = {1,\ldots,M}$, $t \in {\lbrack 0,T\rbrack}$. The conservatism of follows from the convexity of and Corollary 6.6. ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets") or Theorem LABEL:thm:error_bound, see \[LewBonalliJansonPavone2023, Corollary 5.5\]. Given a reference $x_{\text{r}} = {(1,0,\ldots,0)}$ and ${(Q,R)} = {({10I_{7}},I_{3})}$, we define the robust control problem [$\text{OCP}{(x^{0})}$]:

By recursively solving $\text{OCP}{(x^{0})}$ and applying the computed control inputs, we obtain the receding horizon robust MPC controller in Algorithm LABEL:alg:mpc. We use $M = 50$ samples of $d^{0}$ and the error bounds $\epsilon_{t}$ in Theorem LABEL:thm:error_bound. We solve $\text{OCP}{(x^{0})}$ using a standard direct method based on sequential convex programming (SCP). We refer to Appendix A.5 and the open-source code for further details.

### MPC results

We evaluate the controller in $100$ experiments with uniformly-sampled disturbances and initial states. Results in Figure 10 show that despite disturbances, the system converges to the reference and the constraints are always satisfied. The optimization problem is always feasible in these experiments. We observe that the error bounds from Theorem LABEL:thm:error_bound introduce reasonable conservatism. By increasing the sample size $M$, this conservatism can be made arbitrarily small.

Figure 10: 100 closed-loop trajectories using robust MPC (Algorithm LABEL:alg:mpc) to stabilize the attitude of the spacecraft from different initial conditions under external disturbances.

As is common in MPC, in Algorithm LABEL:alg:mpc, we warm-start the optimization using the previously computed solution and only perform a single SCP iteration per timestep, yielding a replanning rate with MPC of approximately $20$Hz with our Python implementation. We report solver statistics and computation times from a zero-initial guess in the appendix in Figures 13 and 13. We observe that a few SCP iterations suffice to reach accurate solutions. Computation time roughly scales linearly with the sample size (most computation time is spent evaluating ) and could be reduced via parallelization on a GPU.

### Comparisons with other reachability methods

We compare the reachable set convex hull estimates from Algorithm LABEL:alg:1 with those from two other standard methods. The first baseline is a sampling-based method (RandUP \[LewPavone2020\]) that estimates the convex hulls $\text{H}{(\mathcal{X}_{t})}$ with the convex hulls of trajectories from with samples of $w{({k\Deltat})}$. The second standard baseline propagates uncertainty from the disturbances using a linear model of and bounds the approximation error using the Lipschitz constant of the Jacobian ${\nabla_{x}\overline{f}}{(x,u)}$.

Given a control trajectory $\overline{u}$ solving $\text{OCP}{(x^{0})}$, we present reachable set estimates in Figure 11. First, the Lipschitz-based and the naive sampling-based baselines are the fastest (with runtimes at $35\mu\text{s}$ and $150\mu\text{s}$, respectively), followed by Algorithm LABEL:alg:1 ($350\mu\text{s}$). However, the over-approximations of the reachable sets from the Lipschitz-based method are significantly more conservative than those from Algorithm LABEL:alg:1. A controller using the reachable set estimates from this baseline would deem $\overline{u}$ to potentially violate constraints and would thus be more conservative than the proposed robust MPC approach. Also, the naive sampling-based baseline significantly under-estimates the true convex hulls. One can show that this baseline performs worse as the discretization is refined, see also Section 11.2. In contrast, Algorithm LABEL:alg:1 is derived in continuous time so its sample complexity is independent of the discretization of the dynamics. Since Algorithm LABEL:alg:1 only samples on the $({n - 1})$-dimensional sphere $\mathcal{S}^{n - 1}$, it is more efficient and its precision only depends on the accuracy of the discretization of $\text{ODE}_{d^{0}}$.

Figure 11: Reachability comparison: convex hull reachable sets estimates computed with Algorithm LABEL:alg:1 and with two baselines.

## Conclusion

We showed that estimating the convex hulls of reachable sets of nonlinear systems with disturbances and uncertain initial conditions is equivalent to studying the solutions of an ODE with initial conditions on the sphere. This result is a significantly simpler finite-dimensional characterization of the convex hulls of reachable sets that could inform the design of efficient reachability analysis algorithms for nonlinear systems.

Algorithm LABEL:alg:1 has two main limitations. First, the accuracy of sampling-based techniques decreases as the number of uncertain variables increases. Thanks to our characterization result, the sample space is only of dimension $({n - 1})$ as opposed to an infinite-dimensional space of disturbances. However, obtaining provably-accurate approximations for high-dimensional systems in reasonable computation time remains difficult. This limitation is unfortunately shared by other reachability analysis algorithms for nonlinear systems. It would be interesting to develop methods to bias sampling to get accurate approximations with fewer samples, e.g., using adversarial sampling \[LewPavone2020\], or use additional properties of the dynamics to design a method that out-performs sampling-based-only algorithms. Second, convex hull approximations of non-convex reachable sets may be conservative for some systems. Given additional computation time, this limitation could be addressed by splitting the sample space $\mathcal{S}^{n - 1}$ into distinct regions, running Algorithm LABEL:alg:1 on each region, and approximating the reachable sets with the non-convex union of the outputs.
