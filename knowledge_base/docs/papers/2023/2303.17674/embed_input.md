<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convex Hulls of Reachable Sets

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the convex hulls of reachable sets of nonlinear systems with bounded disturbances and uncertain initial conditions. Reachable sets play a critical role in control, but remain notoriously challenging to compute, and existing over-approximation tools tend to be conservative or computationally expensive. In this work, we characterize the convex hulls of reachable sets as the convex hulls of solutions of an ordinary differential equation with initial conditions on the sphere. This finite-dimensional characterization unlocks an efficient sampling-based estimation algorithm to accurately over-approximate reachable sets. We also study the structure of the boundary of the reachable convex hulls and derive error bounds for the estimation algorithm. We give applications to neural feedback loop analysis and robust MPC.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Forward reachability analysis plays a critical role in control theory and robust controller design. Generally, it entails characterizing all states that a system can reach at any time in the future. As such, reachability analysis allows certifying the performance of feedback loops under disturbances and designing controllers with robustness properties. In robust model predictive control (MPC) for instance, it is used to construct tubes around nominal state trajectories to ensure that constraints are satisfied in the presence of external disturbances.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we study the following reachability analysis problem. Let $n\in\mathbb{N}$ be the state dimension, $f:\mathbb{R}\times\mathbb{R}^{n}\to\mathbb{R}^{n}$ and $g:\mathbb{R}\times\mathbb{R}^{n}\to\mathbb{R}^{n\times n}$ be functions for the dynamics, and $\mathcal{W},\mathcal{X}_{0}\subset\mathbb{R}^{n}$ be bounded sets of disturbances and initial conditions. Given a time $T>0$ and an initial state $x^{0}\in\mathcal{X}_{0}$, we consider systems defined by the ordinary differential equation (ODE) where the disturbances $w:[0,T]\to\mathcal{W}$ are assumed to be integrable ($w\in L^{\infty}([0,T],\mathcal{W})$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under standard smoothness assumptions (see Assumptions LABEL:assumption:f-LABEL:assumption:W), the ODE has a unique solution, denoted by $x_{(w,x^{0})}(\cdot)$. For any time $t\in[0,T]$, we define the reachable set that characterizes all states that are reachable at time $t$ for some disturbance $w$ and initial state $x^{0}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reachability analysis of nonlinear dynamical systems is challenging. Indeed computing the reachable sets seemingly requires evaluating an infinite number of state trajectories for all possible disturbances and initial conditions.^11^1Each reachable set $\mathcal{X}_{t}$ is the image of an infinite-dimensional set. Indeed, by defining the maps $g_{t}(w,x^{0})=x_{(w,x^{0})}(t)\in\mathbb{R}^{n}$, each reachable set is expressed as $\mathcal{X}_{t}=g_{t}(L^{\infty}([0,T],\mathcal{W})\times\mathcal{X}_{0})$. Due to the complexity of the problem, many existing tools seek convex over-approximations of reachable sets. Yet, current methods tend to be conservative or computationally expensive, see Sections 2 and 11. This motivates the study of properties of convex hulls of reachable sets that can simplify their estimation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contribution is a new characterization of the convex hulls of reachable sets of dynamical systems of the form, under smoothness assumptions of $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ (see Assumptions LABEL:assumption:f-LABEL:assumption:X0). Specifically, denoting by $\textrm{H}(A)$ the convex hull of a set $A\subset\mathbb{R}^{n}$, we show that where $F(d^{0},t)$ is the solution to an ODE with initial conditions $d^{0}$ on the sphere $\mathcal{S}^{n-1}\subset\mathbb{R}^{n}$, see Theorem LABEL:thm:hull_F and $\textbf{ODE}_{d^{0}}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, the convex hulls of the reachable sets can now be computed as the convex hulls of solutions of an ODE for different initial conditions $d^{0}\in\mathcal{S}^{n-1}$. Equation represents a significantly simpler (finite-dimensional) characterization of the convex hulls.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This result unlocks an approach (Algorithm LABEL:alg:1) to efficiently estimate the convex hulls $\textrm{H}(\mathcal{X}_{t})$ by integrating an ODE from a sample of initial conditions. This approach allows efficiently tackling challenging problems such as analyzing the robustness of neural network controllers (see Section 11). This characterization also informs the design of a robust MPC controller (see Algorithm LABEL:alg:mpc) that we demonstrate on a robust spacecraft control task.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work extends preliminary results in \[LewBonalliEtAl2023\]: considering time-varying disturbance-affine dynamics, accounting for uncertain initial conditions, studying the boundary of the convex hulls of reachable sets to obtain tighter error bounds (Section 6, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")), analyzing problems with rectangular uncertainty sets (Section 8), and with disturbances that only affect a subset of directions of the statespace (Section 10 ‣ Convex Hulls of Reachable Sets")), providing additional numerical results (Section 11), The main characterization (see Theorem LABEL:thm:hull_F and $\textbf{ODE}_{d^{0}}$) also does not rely on the projection step from \[LewBonalliEtAl2023\] anymore, simplifying the evaluation of solutions to $\textbf{ODE}_{d^{0}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Outline", "weight": 1.0} -->

In Section 2, we review prior work. In Section 3, we introduce notations and preliminary results. In Sections 4 ‣ Convex Hulls of Reachable Sets")-5, we state and derive our characterization result of the reachable convex hulls $\textrm{H}(\mathcal{X}_{t})$ and propose an estimation algorithm (Algorithm LABEL:alg:1). In Sections 6, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")-7, we study the boundary of $\textrm{H}(\mathcal{X}_{t})$ and derive error bounds for Algorithm LABEL:alg:1. We study problems with rectangular uncertainty sets and disturbances that only affect a subset of the statespace in Sections 8-9 and 10 ‣ Convex Hulls of Reachable Sets"), respectively. We provide numerical results in Section 11 and conclude in Section 12. The appendix contains additional details about theoretical and numerical results.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Numerical methods", "weight": 1.0} -->

The forward reachable sets of nonlinear systems are generally difficult to characterize. For this reason, many existing approaches seek convex over-approximations of the reachable sets, e.g., represented as hyper-rectangles \[Meyer2021\], ellipsoids \[Kurzhanski2000\], zonotopes \[Althoff2008\], or ellipsotopes \[Kousik2023\], see \[Althoff2021\] for a recent survey that also reviews non-convex approximations. Existing over-approximation methods include techniques based on conservative linearization \[Althoff2008\], differential inequalities \[Ramdani2009, Scott2013\], and Taylor models \[Berz1998, Chen2013\]. In particular, systems with mixed-monotone \[meyer2019hscc, Coogan2015, Abate2022\] or contracting \[Maidens2015, Fan2017, SinghMajumdarEtAl2017\] dynamics have been extensively studied, as these properties simplify the computation of accurate over-approximations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Numerical methods", "weight": 1.0} -->

To tackle smooth systems, a standard approach consists of linearizing the dynamics and bounding the Taylor remainder using smoothness properties of the dynamics \[Althoff2008, koller2018, Yu2013, Leeman2023, Althoff2021\]. This method has been widely used in robust MPC but is known to be conservative \[LewPavone2020\], see also Section 11.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Numerical methods", "weight": 1.0} -->

Methods that estimate the reachable sets from a sample of state trajectories \[Huang2012, Donz2007\] have recently found significant interest \[ThorpeL4DC2021, LewPavone2020, LewJansonEtAl2022\]. However, the sample complexity of these methods increases with the number of uncertain variables. For systems with disturbances as, the number of uncertain variables (and thus the approximation error) increases as the discretization is refined. Thus, naive sampling-based methods are not well-suited for reachability of systems with continuous-time disturbances, see also Section 11 for comparisons.

<!-- chunk {"id": "body-0015", "role": "body", "section": "On geometry and optimal control", "weight": 1.0} -->

The deep connection between geometry, reachability analysis, and optimal control is well-known \[Agrachev2004, BonnardChyba2003, Trelat2012\]. It was previously used in \[Krener1989, Schttler2012\] to characterize the true reachable sets of dynamical systems of dimensions $n\leq 4$ with scalar control inputs (control inputs in \[Krener1989\] take the role of disturbances in ). Our results also leverage geometric arguments and the Pontryagin Maximum Principle (PMP), but apply to a different class of dynamical systems with arbitrary state dimensionality $n$ and the same number of disturbances and states. With an appropriate relaxation scheme inspired from \[Silva2010\], these results can be approximately generalized to problems with a smaller number of disturbances than states, see Section 10 ‣ Convex Hulls of Reachable Sets").

<!-- chunk {"id": "body-0016", "role": "body", "section": "On geometry and optimal control", "weight": 1.0} -->

Importantly, by studying the convex hulls of the reachable sets, our results apply to arbitrarily-large times $T$ and sets $(\mathcal{X}_{0},\mathcal{W})$, and thus do not rely on a small-time assumption as in \[Krener1989\] or on a set $\mathcal{X}_{0}$ small-enough as in \[Reiig2007\]. In contrast, \[Krener1989\] and \[Reiig2007\] study the structure of the true reachable sets that may self-intersect for times $T$ too large, see Example LABEL:example:selfintersect.

<!-- chunk {"id": "body-0017", "role": "body", "section": "On geometry and optimal control", "weight": 1.0} -->

Our derivations start with the idea of searching for boundary states that are the furthest in different directions (see $\textbf{OCP}_{d}$). This approach is standard in the setting with linear dynamics where reachable sets are convex \[Pecsvaradi1971, Schttler2012\],\[Kurzhanski2014, Chap.1.4\]. However, in the nonlinear case, reachable sets may be non-convex, and finding the extremal disturbance trajectories that generate boundary states requires solving optimal control problems (OCPs) or their corresponding boundary-value problems (BVPs) stemming from the PMP (see $\textbf{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")). Such approaches were explored in \[Gornov2015\] and \[Baier2009\], but remain computationally challenging.

<!-- chunk {"id": "body-0018", "role": "body", "section": "On geometry and optimal control", "weight": 1.0} -->

Our results show that under the right set of assumptions (see Assumptions LABEL:assumption:f-LABEL:assumption:X0), solving OCPs is not necessary and extremal trajectories take a simple form. The key is the additional idea of sampling initial values of the adjoint vector. Studying the convex hulls of reachable sets unlocks arguments from convex geometry that allow proving the exactness of the approach.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convex geometry", "weight": 1.0} -->

A point in a set $A$ is said to be an extreme point if it is the endpoint of every segment in $A$ that contains it \[Grothendieck1973\]. We denote by $\textrm{H}(A)$ the convex hull of $A\subset\mathbb{R}^{n}$ and by $\text{Ext}(A)$ the set of extreme points of a compact set $A\subset\mathbb{R}^{n}$. The next result is standard.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Differential geometry", "weight": 1.0} -->

Let $\mathcal{M}\subseteq\mathbb{R}^{n}$ be a $k$-dimensional submanifold. Equipped with the induced metric from the ambient Euclidean norm $\|\cdot\|$, $\mathcal{M}$ is a Riemannian submanifold. For any $x\in\mathcal{M}$, $T_{x}\mathcal{M}$ and $N_{x}\mathcal{M}$ denote the tangent and normal spaces of $\mathcal{M}$\[Lee2012\], respectively, which we view as linear subspaces of $\mathbb{R}^{n}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Ovaloids and Gauss maps", "weight": 1.0} -->

An $(n-1)$-dimensional submanifold $\mathcal{M}\subset\mathbb{R}^{n}$ is called a hypersurface. Let $\mathcal{C}\subset\mathbb{R}^{n}$ be such that $\mathcal{M}=\partial\mathcal{C}$ is a hypersurface. The Gauss map of $\mathcal{M}$ is the map $n^{\mathcal{M}}:\mathcal{M}\to\mathcal{S}^{n-1}$ defined such that $n^{\mathcal{M}}(x)$ is the unit-norm outward-pointing normal vector of $\mathcal{M}$ at $x\in\mathcal{M}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Ovaloids and Gauss maps", "weight": 1.0} -->

For any $x\in\mathcal{M}$, the shape operator (or Weingarten map) is the linear map $S_{x}:T_{x}\mathcal{M}\to T_{x}\mathcal{M}$ defined by $S_{x}(v)=\nabla n(x)v$. The $(n-1)$ eigenvalues of the shape operator are called the principal curvatures of $\mathcal{M}$. $\mathcal{M}$ is said to be an ovaloid (or of strictly positive curvature), if all the principal curvatures of $\mathcal{M}$ are strictly positive.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Ovaloids and Gauss maps", "weight": 1.0} -->

If $\mathcal{M}$ is an ovaloid, then the Gauss map $n^{\mathcal{M}}:\mathcal{M}\to\mathcal{S}^{n-1}$ is a diffeomorphism \[Rauch1974\], $\mathcal{M}$ is the boundary of a bounded strictly convex set $\mathcal{C}$ such that $\partial\mathcal{C}=\mathcal{M}$ \[Rauch1974\], and for any $x\in\mathcal{M}$,

<!-- chunk {"id": "body-0024", "role": "body", "section": "The structure of $\\textrm{H}(\\mathcal{X}_{t})$", "weight": 1.0} -->

Our results rely on the following four assumptions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The structure of $\\textrm{H}(\\mathcal{X}_{t})$", "weight": 1.0} -->

Assumption LABEL:assumption:f is a standard smoothness assumption \[Lorenz2005, Cannarsa2006\] guaranteeing the existence and uniqueness of solutions to the ODE in and $\textbf{ODE}_{d^{0}}$. By multiplying $f$ and $g$ with a smooth cutoff function whose arbitrarily large support contains states of interest, the Lipschitzianity assumptions are always satisfied if $f,g\in C^{2}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The structure of $\\textrm{H}(\\mathcal{X}_{t})$", "weight": 1.0} -->

Assumption LABEL:assumption:g does not hold for problems with fewer disturbances than states. It is relaxed in Section 10 ‣ Convex Hulls of Reachable Sets").

<!-- chunk {"id": "body-0027", "role": "body", "section": "The structure of $\\textrm{H}(\\mathcal{X}_{t})$", "weight": 1.0} -->

Assumption LABEL:assumption:W and A4b hold in particular if $\mathcal{W}$ and $\mathcal{X}_{0}$ are spheres or ellipsoids, which are commonly used in applications. These assumptions imply that $\mathcal{W}$ and $\mathcal{X}_{0}$ are strictly convex. They are relaxed in Section 8.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The structure of $\\textrm{H}(\\mathcal{X}_{t})$", "weight": 1.0} -->

Assuming that $\mathcal{W}$ is convex is standard to prove that the reachable sets are compact.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Searching for extreme points of $\\textrm{H}(\\mathcal{X}_{T})$", "weight": 1.0} -->

Assume that $\mathcal{X}_{0}=\{x^{0}\}$. Let $d\in\mathcal{S}^{n-1}$ be a search direction and define the optimal control problem (OCP) $\textbf{OCP}_{d}$ is well-posed under Assumptions LABEL:assumption:f and LABEL:assumption:W, i.e., it admits at least one solution $w_{d}\in L^{\infty}([0,T],\mathcal{W})$ (see, e.g., \[Trelat2023, Theorem 9\], and note that $w(\cdot)=0$ is feasible). Intuitively, solving $\textbf{OCP}_{d}$ gives a reachable state $x_{d}(T)\in\mathcal{X}_{T}$ that is the furthest in the direction $d$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Reformulating $\\textbf{OCP}_{d}$ using the PMP to reduce the search of solutions from $L^{\\infty}([0,T],\\mathcal{W})$ to $\\mathbb{R}^{n}$", "weight": 1.0} -->

The Pontryagin Maximum Principle (PMP) \[Pontryagin1987, Agrachev2004, Trelat2012\] gives necessary conditions of optimality for $\textbf{OCP}_{d}$. As the Hamiltonian of $\textbf{OCP}_{d}$ is given by $H(t,x,w,p)=p^{\top}(f(t,x)+g(t,x)w))$, for any locally-optimal solution $(x_{d},w_{d})$ of $\textbf{OCP}_{d}$, there exists an absolutely-continuous function $p_{d}:[0,T]\to\mathbb{R}^{n}$, called the adjoint vector, such that for almost every $t\in[0,T]$, A tuple $(x_{d},p_{d},w_{d})$ satisfying the above equations is called (Pontryagin) extremal for $\textbf{OCP}_{d}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reformulating $\\textbf{OCP}_{d}$ using the PMP to reduce the search of solutions from $L^{\\infty}([0,T],\\mathcal{W})$ to $\\mathbb{R}^{n}$", "weight": 1.0} -->

These equations indicate that the adjoint vector is non-zero at all times.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Reformulating $\\textbf{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets\") with knowledge of $\\frac{p_{d}}{\\|p_{d}\\|}$", "weight": 1.0} -->

$\textbf{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") and (16 to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) indicate that extremal state trajectories $x_{d}$ follow dynamics that only depend on $\frac{p_{d}}{\|p_{d}\|}$. The next result shows that extremal trajectories are independent of the norm of $p_{d}$. Thus, it suffices to search over $\mathcal{S}^{n-1}$ to retrieve extremal trajectories $x_{d}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Concluding the proof of Theorem LABEL:thm:hull_F", "weight": 1.0} -->

Lemma 5.2/‖𝑝⁢‖). ‣ 5.3 Reformulating "BVP"_𝑑 with knowledge of 𝑝_𝑑⁢/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") yields the following key result.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion and insights", "weight": 1.5} -->

In Table 1, we summarize the different problems used to derive $\textbf{ODE}_{d^{0}}$ and ultimately prove Theorem LABEL:thm:hull_F.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion and insights", "weight": 1.5} -->

At first sight, $\textbf{OCP}_{d}$ and $\textbf{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") suggest using Algorithm LABEL:alg:2 to reconstruct the convex hull of the reachable set $\textrm{H}(\mathcal{X}_{T})$ (similar ideas are investigated in \[Gornov2015\] and in \[Baier2009\]). However, this procedure can be computationally expensive. Also, $\textbf{OCP}_{d}$ is generally non-convex, so Algorithm LABEL:alg:2 could be prone to local minima and under-estimating the reachable sets. Thus, Algorithm LABEL:alg:2 may be unsuitable for applications that require efficient reachable set over-approximations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion and insights", "weight": 1.5} -->

Carrying on the analysis using samples of $p_{d}\in\mathcal{S}^{n-1}$ and observing that the norm of $p_{d}(t)$ does not play a role in the problem (Section 5.3/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets")) is key to our result.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Discussion and insights", "weight": 1.5} -->

Lemma 5.2/‖𝑝⁢‖). ‣ 5.3 Reformulating "BVP"_𝑑 with knowledge of 𝑝_𝑑⁢/‖𝑝_𝑑⁢‖ ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") implies that extremal trajectories are completely specified by the initial value of the adjoint vector $p_{d}\in\mathcal{S}^{n-1}$. Thus, given $p_{d}=d^{0}$, we can integrate $\textbf{ODE}_{d^{0}}$ to obtain the corresponding reachable extremal states $x_{d}(t)$, independently of the search direction $d$ (as $d$ is implicitly encoded in $p_{d}$). This observation is the key insight behind Algorithm LABEL:alg:1, that consists of integrating $\textbf{ODE}_{d^{0}}$ for different values of $d^{0}\in\mathcal{S}^{n-1}$ to recover the convex hulls of the reachable sets.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Discussion and insights", "weight": 1.5} -->

To gain further intuition with the linear case, see Appendix.1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The boundary structure of $\\textrm{H}(\\mathcal{X}_{t})$, geometric estimation, and error bounds", "weight": 1.0} -->

How accurate are the estimates returned by Algorithm LABEL:alg:1, which approximates the reachable convex hulls $\textrm{H}(\mathcal{X}_{t})$ with the convex hulls of a finite number of state trajectories? First, we show that the boundaries of the convex hulls of reachable sets are smooth submanifolds under Assumptions LABEL:assumption:f-LABEL:assumption:X0 (Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")). This smooth boundary structure implies tight error bounds for convex-hull sampling-based estimators (Theorem LABEL:thm:error_bound). Indeed, error bounds of sample-based approximations typically rely on smoothness properties of the functions of interest and on sufficient coverage of the samples, as shown below.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 6.8 (Proving Theorem LABEL:thm:error_bound)", "weight": 1.0} -->

The proof of Theorem LABEL:thm:error_bound relies on Theorem LABEL:thm:hull_F. It takes inspiration from \[LewBonalliJansonPavone2023, Theorem 1.1\], but requires new analysis due to several difficulties. First, the map $F(\cdot,t)$ is not a diffeomorphism onto its image: $\mathcal{S}^{n-1}$ is an $(n-1)$-dimensional submanifold of $\mathbb{R}^{n}$, but the set $F(\mathcal{S}^{n-1},t)$ may self-intersect and is thus not a submanifold of $\mathbb{R}^{n}$, see Example LABEL:example:selfintersect.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 6.8 (Proving Theorem LABEL:thm:error_bound)", "weight": 1.0} -->

$F$ is neither a submersion: $\textrm{d}F(d^{0},t):T_{d^{0}}\mathcal{S}^{n-1}\to T_{F(d^{0},t)}\mathbb{R}^{n}$ cannot be surjective since $\mathcal{S}^{n-1}$ is only $(n-1)$-dimensional. To prove Theorem LABEL:thm:error_bound, we exploit properties of solutions to $\textbf{ODE}_{d^{0}}$ and of $F$. Theorem LABEL:thm:error_bound relies on Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"), whose proof relies on the PMP and the structure of extremal trajectories from the PMP coupled with properties of convex sets.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

First, we prove that $\partial\textrm{H}(\mathcal{X}_{t})$ is a submanifold of $\mathbb{R}^{n}$ of dimension $(n-1)$ (Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")). The analysis leverages Theorem LABEL:thm:hull_F and properties of convex sets.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

Proof of Lemma 6.7} is smooth). ‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"): $\textrm{H}(\mathcal{X}_{t})$ is convex, compact (Lemma 3 ‣ 4 The structure of "H"⁢(𝒳_𝑡) ‣ Convex Hulls of Reachable Sets")), and has interior points ($\textrm{Int}(\mathcal{X}_{t})\neq\emptyset$ since the reachable state $x_{w}(t)$ associated to the disturbance $w(\cdot)=0$ is clearly in $\textrm{Int}(\mathcal{X}_{t})$).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

Thus, by \[Schneider2014, Theorem 2.2.4\], it suffices to prove that there is a unique support hyperplane to $\textrm{H}(\mathcal{X}_{t})$ at any boundary point $x\in\partial\textrm{H}(\mathcal{X}_{t})$. In the following, as in the proof of Lemma 5.4, we prove the result for $t=T$ without loss of generality.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

By contradiction (see Figure 4), assume that there is a different support hyperplane for $\textrm{H}(\mathcal{X}_{T})$ at $x=x_{w}(T)$ parameterized by $\tilde{d}\in\mathcal{S}^{n-1}$ with $\tilde{d}\neq d$. Then, since $\tilde{d}^{\top}x\geq\tilde{d}^{\top}y$ for all $y\in\mathcal{X}_{T}$, from the previous reasoning, the same trajectory $(x_{w},w)$ also solves $\textbf{OCP}_{\tilde{d}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

Thus, $w$ satisfies $w(T)=(n^{\partial\mathcal{W}})^{-1}(g(T,x)^{\top}\tilde{d}/\|g(T,x)^{\top}\tilde{d}\|)$. This is a contradiction, since $g(T,x)$ is invertible by Assumption LABEL:assumption:g, $n^{\partial\mathcal{W}}$ is a diffeomorphism by Assumption LABEL:assumption:W, and $\tilde{d}\neq d$. Thus, $x$ has a unique support hyperplane.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

Second, we consider boundary points that are not in $F(\mathcal{S}^{n-1},T)$. Let $x\in\partial\textrm{H}(\mathcal{X}_{T})\setminus F(\mathcal{S}^{n-1},T)$. As $\text{Ext}(\textrm{H}(F(\mathcal{S}^{n-1},T)))\subseteq F(\mathcal{S}^{n-1},T)$ (Lemma 2) and $\textrm{H}(\mathcal{X}_{T})=\textrm{H}(F(\mathcal{S}^{n-1},T))$ (Theorem LABEL:thm:hull_F), $x$ is not an extreme point.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

Since $x\in\partial\textrm{H}(\mathcal{X}_{T})$, there is a support hyperplane $H=\{y\in\mathbb{R}^{n}:d^{\top}(y-x)=0\}$ at $x$ parameterized by some $d\in\mathcal{S}^{n-1}$ such that $d^{\top}x\geq d^{\top}y$ for all $y\in\textrm{H}(\mathcal{X}_{T})$. Thus, from which one can show that $d^{\top}x=d^{\top}x_{1}=d^{\top}x_{2}$. Thus, $H$ is a support hyperplane at $x_{2}$. Since $x_{2}$ has a unique support hyperplane as shown previously, we conclude that $H$ is the unique support hyperplane at $x$. This concludes the proof of Lemma 6.7} is smooth).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Proofs of Theorem LABEL:thm:error_bound and Lemma 6.7} is smooth). ‣ 6 The boundary structure of \"H\"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets\")", "weight": 1.0} -->

‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets"). $\blacksquare$ The proof of Theorem LABEL:thm:error_bound relies on the fact that $F$ maps tangent spaces of $\mathcal{S}^{n-1}$ to tangent spaces of $\partial\textrm{H}(\mathcal{X}_{t})$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Approximate characterization for rectangular uncertainty sets $\\mathcal{W}$ and $\\mathcal{X}_{0}$", "weight": 1.0} -->

In the next three sections, we relax Assumptions LABEL:assumption:g-LABEL:assumption:X0. First, we relax Assumptions LABEL:assumption:W and [(A4b)](2303.17674v5/assumption:X0), which state that $\partial\mathcal{W}$ and $\partial\mathcal{X}_{0}$ are ovaloids. These assumptions prevent using rectangular uncertainties, as defined below.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Approximate characterization for rectangular uncertainty sets $\\mathcal{W}$ and $\\mathcal{X}_{0}$", "weight": 1.0} -->

We propose an approximation scheme for problems with hyper-rectangular sets $(\mathcal{W},\mathcal{X}_{0})$ satisfying Assumptions LABEL:assumption:W_box and LABEL:assumption:X0_box. Given a relaxation parameter $\lambda>1$, we use smooth inner- and outer-approximations of $(\mathcal{W},\mathcal{X}_{0})$, defined in as $\lambda$-norm ellipsoids. The approximation scheme is shown in Figure 5 and has three key properties.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Approximate characterization for rectangular uncertainty sets $\\mathcal{W}$ and $\\mathcal{X}_{0}$", "weight": 1.0} -->

The approximations of $(\mathcal{W},\mathcal{X}_{0})$ satisfy Assumptions LABEL:assumption:W and LABEL:assumption:X0, so the convex hulls of their associated reachable sets are characterized by Theorem LABEL:thm:hull_F.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Approximate characterization for rectangular uncertainty sets $\\mathcal{W}$ and $\\mathcal{X}_{0}$", "weight": 1.0} -->

The approximations either inner- or outer-bound $(\mathcal{W},\mathcal{X}_{0})$, so their reachable sets either inner- and outer-approximate the true reachable sets $\mathcal{X}_{t}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Approximate characterization for rectangular uncertainty sets $\\mathcal{W}$ and $\\mathcal{X}_{0}$", "weight": 1.0} -->

By choosing $\lambda$ large-enough, the approximations can be made arbitrarily close to $(\mathcal{W},\mathcal{X}_{0})$, so the resulting approximate reachable sets can be made arbitrarily close to the true reachable sets $\mathcal{X}_{t}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Approximate characterization for rectangular uncertainty sets $\\mathcal{W}$ and $\\mathcal{X}_{0}$", "weight": 1.0} -->

Combining these properties, we obtain arbitrarily-close inner- and outer-approximations of the convex hulls of the reachable sets $\mathcal{X}_{t}$ of dynamical systems with $(\mathcal{W},\mathcal{X}_{0})$ satisfying Assumptions LABEL:assumption:W_box and LABEL:assumption:X0_box. This characterization is given in Theorem LABEL:thm:hull_F:rect_lambda and is proved in Section 9. Below, we state this result and necessary definitions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Approximate characterization for non-invertible $g(t,x)$", "weight": 1.0} -->

Assumption LABEL:assumption:g states that $g(t,x)$ is invertible, so Theorem LABEL:thm:hull_F does not directly apply to problems that have more states than disturbances. To relax this assumption, given two integers $m<n$, we consider the system where $x\in\mathcal{X}_{0}$ with $\mathcal{X}_{0}\subset\mathbb{R}^{n}$ satisfying Assumption LABEL:assumption:X0, $w\in L^{\infty}([0,T],\mathcal{W})$ with $\mathcal{W}\subset\mathbb{R}^{m}$ satisfying Assumption LABEL:assumption:W, $f$ satisfies Assumption LABEL:assumption:f, and $g(t,x)=(g_{1},\dots,g_{m})(t,x)\in\mathbb{R}^{n\times m}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Approximate characterization for non-invertible $g(t,x)$", "weight": 1.0} -->

The reachable sets of (10 ‣ Convex Hulls of Reachable Sets")) are defined as in and are denoted by $\mathcal{X}_{t}$. We relax the invertibility assumption on $g$ (Assumption LABEL:assumption:g) as follows.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Approximate characterization for non-invertible $g(t,x)$", "weight": 1.0} -->

Assumption LABEL:assumption:g:full_rank is standard and holds in many practical applications. By appropriately completing the range of $g$, we approximate the system (10 ‣ Convex Hulls of Reachable Sets")) with a system that has similar reachable sets and satisfies Assumption LABEL:assumption:f-LABEL:assumption:X0. First, we rely on the choice of a particular set $\widehat{\mathcal{W}}\subset\mathbb{R}^{n}$. Below, $\pi(w_{1},\dots,w_{m},w_{m+1},\dots,w_{n})=(w_{1},\dots,w_{m})$ denotes the projection map.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Approximate characterization for non-invertible $g(t,x)$", "weight": 1.0} -->

For $g(t,x)$ that is constant and satisfies Assumption LABEL:assumption:g:full_rank, choosing the maps $(g_{m+1},\dots,g_{n})$ with constant values sampled at random on the sphere $\mathcal{S}^{n-1}$ (from a uniform distribution) suffices to satisfy Assumption LABEL:assumption:g_bar_epsilon. We refer to \[Silva2010\] for insightful discussion related to this assumption and to Section 11.1 for an example.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Approximate characterization for non-invertible $g(t,x)$", "weight": 1.0} -->

Third, we define the extended system where $x\in\mathcal{X}_{0}$ and $\widehat{w}\in L^{\infty}([0,T],\widehat{\mathcal{W}})$, with associated reachable sets denoted by $\widehat{\mathcal{X}}_{t}^{\epsilon}$. The system (54 ‣ Convex Hulls of Reachable Sets")) satisfies the assumptions of Theorem LABEL:thm:hull_F. This suggests defining the following augmented ODE: As stated below, solutions to $\textbf{ODE}_{d^{0}}^{\epsilon}$ characterize the convex hulls of the reachable sets $\mathcal{X}_{t}$ of the system (10 ‣ Convex Hulls of Reachable Sets")) arbitrarily well by selecting $\epsilon$ small-enough.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 10.12 (Error bounds and stable integration)", "weight": 1.0} -->

Error bounds for obtaining convex hull approximations of the reachable sets of system (10 ‣ Convex Hulls of Reachable Sets")) with Algorithm LABEL:alg:1 can be derived by combining (29, geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets")) and (57 ‣ Convex Hulls of Reachable Sets")).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Results and applications", "weight": 1.0} -->

We evaluate Algorithm LABEL:alg:1 on three nonlinear systems, and use its reachable set estimates to design a robust model predictive controller (Algorithm LABEL:alg:mpc). Computation times are measured on a laptop with an 1.10GHz Intel Core i7-10710U CPU. Code to reproduce results is available.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Validating the relaxation schemes on Dubins car", "weight": 1.0} -->

We consider two different choices of $g$ and $\mathcal{W}$ that violate Assumption LABEL:assumption:W ($\partial\mathcal{W}$ is an ovaloid in $\mathbb{R}^{n}$) and Assumption LABEL:assumption:g ($g(t,x)$ is invertible), which allows us to validate the relaxation schemes in Section 8 and 10 ‣ Convex Hulls of Reachable Sets").

<!-- chunk {"id": "body-0064", "role": "body", "section": "Rectangular disturbances set", "weight": 1.0} -->

As Assumption LABEL:assumption:W does not hold, we use the relaxation scheme in Section 8. We apply Algorithm LABEL:alg:1 to $\mathchoice{\hbox to0.0pt{\raisebox{0.98221pt}{\scalebox{1.0}[-1.0]{\hbox{\set@color$\displaystyle\widehat{\hphantom{\textbf{ODE}_{d^{0}}^{\lambda}}}$}}}\hss}{\textbf{ODE}_{d^{0}}^{\lambda}}}{\hbox

<!-- chunk {"id": "body-0065", "role": "body", "section": "Rectangular disturbances set", "weight": 1.0} -->

Theorem LABEL:thm:hull_F:rect_lambda ensures that these approximations inner- and outer-approximate the true convex hulls of the reachable sets, and that these approximations converge as the relaxation parameter $\lambda$ increases. Indeed, the results in Figure 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") (left) show that the approximations converge as $\lambda$ increases.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Non-invertible $g(t,x)$", "weight": 1.0} -->

Let $G^{\top}={\footnotesize\begin{bmatrix}1&0&0\\0&0&1\end{bmatrix}}$ and $\mathcal{W}=B(0,10^{-2})\subset\mathbb{R}^{2}$. As Assumption LABEL:assumption:g does not hold, we use the relaxation scheme in Section 10 ‣ Convex Hulls of Reachable Sets"). We apply Algorithm LABEL:alg:1 to $\textbf{ODE}_{d^{0}}^{\epsilon}$ using the approximation of $\mathcal{W}$ in Example LABEL:example:gauss_maps:not_full_rank and $g_{3}(t,x)=$. Since Assumptions LABEL:assumption:Wbar:smooth_fulldim and LABEL:assumption:g_bar_epsilon are satisfied, Theorem LABEL:thm:hull_F:not_full_rank guarantees that the approximations get closer to the true convex hulls of the reachable sets as the relaxation parameter $\epsilon$ decreases.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Non-invertible $g(t,x)$", "weight": 1.0} -->

Indeed, the results in Figure 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") (right) show that the approximations converge as $\epsilon$ decreases.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Neural feedback loop analysis", "weight": 1.0} -->

Consider the system $\dot{x}(t)=Ax(t)+B\pi(x(t))+w(t)$, where $\pi$ is a neural network and $n=2$. The dynamics parameters $(A,B,\pi)$ are as in \[LewBonalliEtAl2023\] and \[Everett21_journal, Sec. VIII.A-C\]. The sets of initial conditions and disturbances $\mathcal{X}_{0}$ and $\mathcal{W}$ are ellipsoidal sets, see Appendix A.4 for details.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Validating Theorem LABEL:thm:hull_F", "weight": 1.0} -->

We run Algorithm LABEL:alg:1 with $M=10^{3}$ samples of $d^{0}$ evenly covering the circle $\mathcal{S}^{n-1}$. Then, we uniformly sample $10^{5}$ disturbances $w(t)\in\mathcal{W}$ at each timestep and evaluate the corresponding trajectories. We verify that all resulting trajectories are within the convex hulls computed by Algorithm LABEL:alg:1, which empirically validates Theorem LABEL:thm:hull_F. Thus, using Algorithm LABEL:alg:1, it suffices to sample initial directions $d^{0}\in\mathcal{S}^{n-1}$ to reconstruct the convex hulls of the reachable sets.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Comparisons", "weight": 1.0} -->

We consider a first baseline that randomly samples disturbances $w(t)\in\mathcal{W}$ at each timestep and returns the convex hulls of closed-loop trajectories (RandUP \[LewJansonEtAl2022\]). As ground truth, we use Algorithm LABEL:alg:1 with a very large number of samples ($10^{4}$), which is justified by Theorem LABEL:thm:hull_F. We report results in Figures 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") and 9. Algorithm LABEL:alg:1 returns estimates that are orders of magnitude more accurate than the baseline's estimates. Given a desired accuracy, Algorithm LABEL:alg:1 is thus orders of magnitude faster than the baseline.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Comparisons", "weight": 1.0} -->

This difference is a direct consequence of Theorem LABEL:thm:hull_F: only initial directions $d^{0}$ on the sphere $\mathcal{S}^{n-1}$ need to be sampled using Algorithm LABEL:alg:1. In contrast, the baseline requires sampling a much larger number of variables that increases with the number of prediction timesteps, resulting in significantly worse sample complexity (see \[LewJansonEtAl2022, LewBonalliJansonPavone2023\] for error bounds) and trajectories that are far from the reachable set boundaries. Recall that Algorithm LABEL:alg:1 returns under-approximations of the convex hulls of the reachable sets, since any extremal trajectory $x_{d^{0}}$ solving $\textbf{ODE}_{d^{0}}$ is contained in the true reachable sets. These simulations show that naive Monte-Carlo estimates poorly approximate the convex hulls of the reachable sets for this problem.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Comparisons", "weight": 1.0} -->

In Figure 8 ‣ 11.1 Validating the relaxation schemes on Dubins car ‣ 11 Results and applications ‣ Convex Hulls of Reachable Sets") and 9, we also report the over-approximations from a formal method (ReachLP \[Everett21_journal\]) that significantly over-estimate the true reachable sets and is unable to capture the closed-loop stability of the system. In contrast, Algorithm LABEL:alg:1 returns accurate approximations using a small number of samples. Other reachability methods may return more accurate approximations for this type of problems \[ManzanasLopez2023\], albeit potentially at the expense of additional computation time.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Robust MPC for attitude control of a spacecraft", "weight": 1.0} -->

We design an attitude controller for a spacecraft with state $x=(q,\omega)\in\mathbb{R}^{7}$, control $u\in\mathbb{R}^{3}$, and dynamics with $x=x^{0}=(q^{0},\omega^{0})$, $w(t)\in\mathcal{W}=B(0,10^{-2})$, inertia matrix $J=\textrm{diag}$, and matrices $(\Omega,S)(\omega)$ defined in \[Leeman2023, LewBonalliEtAl2023\].

<!-- chunk {"id": "body-0074", "role": "body", "section": "Robust MPC for attitude control of a spacecraft", "weight": 1.0} -->

We constrain $\omega(t)$ and $u(t)$ as We consider feedback controls parameterized as $u(t)=\bar{u}(t)+K\omega(t)$, where $\bar{u}\in L^{\infty}([0,T],\mathbb{R}^{3})$ is an open-loop control and $K=-\textrm{diag}$ is a feedback gain. To enforce, we define the reachable set for any $\bar{u}\in L^{\infty}([0,T],\mathbb{R}^{3})$ and $t\in[0,T]$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Robust MPC for attitude control of a spacecraft", "weight": 1.0} -->

The convex hulls of the reachable sets $\textrm{H}(\mathcal{R}_{t}(\bar{u}))$ can be estimated using Algorithm LABEL:alg:1, where $\textbf{ODE}_{d^{0}}$ is defined using (61b) with $u(t)=\bar{u}(t)+K\omega(t)$ and $\mathcal{X}_{0}=\{x^{0}\}$ is a singleton. Thus, given $M$ samples $d^{i}\in\mathcal{S}^{n-1}$ and $\epsilon_{t}>0$ large-enough, the constraints can be approximated by for all $j=1,2,3$, $i=1,\dots,M$, $t\in[0,T]$. The conservatism of follows from the convexity of and Corollary 6.6.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Robust MPC for attitude control of a spacecraft", "weight": 1.0} -->

‣ 6 The boundary structure of "H"⁢(𝒳_𝑡), geometric estimation, and error bounds ‣ Convex Hulls of Reachable Sets") or Theorem LABEL:thm:error_bound, see \[LewBonalliJansonPavone2023, Corollary 5.5\]. Given a reference $x_{\text{r}}=(1,0,\dots,0)$ and $(Q,R)=(10I_{7},I_{3})$, we define the robust control problem [$\textbf{OCP}(x^{0})$]: By recursively solving $\textbf{OCP}(x^{0})$ and applying the computed control inputs, we obtain the receding horizon robust MPC controller in Algorithm LABEL:alg:mpc. We use $M=50$ samples of $d^{0}$ and the error bounds $\epsilon_{t}$ in Theorem LABEL:thm:error_bound.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Robust MPC for attitude control of a spacecraft", "weight": 1.0} -->

We solve $\textbf{OCP}(x^{0})$ using a standard direct method based on sequential convex programming (SCP). We refer to Appendix A.5 and the open-source code for further details.

<!-- chunk {"id": "body-0078", "role": "body", "section": "MPC results", "weight": 1.0} -->

We evaluate the controller in $100$ experiments with uniformly-sampled disturbances and initial states. Results in Figure 10 show that despite disturbances, the system converges to the reference and the constraints are always satisfied. The optimization problem is always feasible in these experiments. We observe that the error bounds from Theorem LABEL:thm:error_bound introduce reasonable conservatism. By increasing the sample size $M$, this conservatism can be made arbitrarily small.

<!-- chunk {"id": "body-0079", "role": "body", "section": "MPC results", "weight": 1.0} -->

As is common in MPC, in Algorithm LABEL:alg:mpc, we warm-start the optimization using the previously computed solution and only perform a single SCP iteration per timestep, yielding a replanning rate with MPC of approximately $20$Hz with our Python implementation. We report solver statistics and computation times from a zero-initial guess in the appendix in Figures 13 and 13. We observe that a few SCP iterations suffice to reach accurate solutions. Computation time roughly scales linearly with the sample size (most computation time is spent evaluating ) and could be reduced via parallelization on a GPU.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Comparisons with other reachability methods", "weight": 1.0} -->

We compare the reachable set convex hull estimates from Algorithm LABEL:alg:1 with those from two other standard methods. The first baseline is a sampling-based method (RandUP \[LewPavone2020\]) that estimates the convex hulls $\textrm{H}(\mathcal{X}_{t})$ with the convex hulls of trajectories from with samples of $w(k\Delta t)$. The second standard baseline propagates uncertainty from the disturbances using a linear model of and bounds the approximation error using the Lipschitz constant of the Jacobian $\nabla_{x}\bar{f}(x,u)$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Comparisons with other reachability methods", "weight": 1.0} -->

Given a control trajectory $\bar{u}$ solving $\textbf{OCP}(x^{0})$, we present reachable set estimates in Figure 11. First, the Lipschitz-based and the naive sampling-based baselines are the fastest (with runtimes at $35\mu\textit{s}$ and $150\mu\textit{s}$, respectively), followed by Algorithm LABEL:alg:1 ($350\mu\textit{s}$). However, the over-approximations of the reachable sets from the Lipschitz-based method are significantly more conservative than those from Algorithm LABEL:alg:1. A controller using the reachable set estimates from this baseline would deem $\bar{u}$ to potentially violate constraints and would thus be more conservative than the proposed robust MPC approach. Also, the naive sampling-based baseline significantly under-estimates the true convex hulls.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Comparisons with other reachability methods", "weight": 1.0} -->

One can show that this baseline performs worse as the discretization is refined, see also Section 11.2. In contrast, Algorithm LABEL:alg:1 is derived in continuous time so its sample complexity is independent of the discretization of the dynamics. Since Algorithm LABEL:alg:1 only samples on the $(n-1)$-dimensional sphere $\mathcal{S}^{n-1}$, it is more efficient and its precision only depends on the accuracy of the discretization of $\textbf{ODE}_{d^{0}}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We showed that estimating the convex hulls of reachable sets of nonlinear systems with disturbances and uncertain initial conditions is equivalent to studying the solutions of an ODE with initial conditions on the sphere. This result is a significantly simpler finite-dimensional characterization of the convex hulls of reachable sets that could inform the design of efficient reachability analysis algorithms for nonlinear systems.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Algorithm LABEL:alg:1 has two main limitations. First, the accuracy of sampling-based techniques decreases as the number of uncertain variables increases. Thanks to our characterization result, the sample space is only of dimension $(n-1)$ as opposed to an infinite-dimensional space of disturbances. However, obtaining provably-accurate approximations for high-dimensional systems in reasonable computation time remains difficult. This limitation is unfortunately shared by other reachability analysis algorithms for nonlinear systems. It would be interesting to develop methods to bias sampling to get accurate approximations with fewer samples, e.g., using adversarial sampling \[LewPavone2020\], or use additional properties of the dynamics to design a method that out-performs sampling-based-only algorithms. Second, convex hull approximations of non-convex reachable sets may be conservative for some systems. Given additional computation time, this limitation could be addressed by splitting the sample space $\mathcal{S}^{n-1}$ into distinct regions, running Algorithm LABEL:alg:1 on each region, and approximating the reachable sets with the non-convex union of the outputs.
