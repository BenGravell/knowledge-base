<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Suboptimal Coverings for Continuous Spaces of Control Tasks

Topics include Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose the α-suboptimal covering number to characterize multi-task control problems where the set of dynamical systems and/or cost functions is infinite, analogous to the cardinality of finite task sets. This notion may help quantify the function class expressiveness needed to represent a good multi-task policy, which is important for learning-based control methods that use parameterized function approximation. We study suboptimal covering numbers for linear dynamical systems with quadratic cost (LQR problems) and construct a class of multi-task LQR problems amenable to analysis. For the scalar case, we show logarithmic dependence on the "breadth" of the space. For the matrix case, we present experiments 1) measuring the efficiency of a particular constructive cover, and 2) visualizing the behavior of two candidate systems for the lower bound.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

An advanced control system such as a mobile robot may be required to perform many different tasks. If the task set is finite, like selecting between "map an environment" and "deliver a package", then its size is naturally quantified by the number of tasks. If the task set is infinite, like delivering packages with arbitrary mass and inertial properties, then its size is not so easily quantified. Even if the task space is equipped with a metric or measure, these structures may be only weakly linked to the diversity of behavior required for good performance on all tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our interest in this issue is motivated by multi-task paradigms in learning-based control, where the policy is selected from a parameterized family of functions that map state and task parameters directly to actions. As the task space expands from a singleton set, we expect to need a more expressive class of functions to represent a good multi-task policy. In this work, we propose the *$\alpha$-suboptimal covering number* to capture this idea. For a task space $\Phi$ and a suboptimality ratio $\alpha > 1$, we define $N_{\alpha}{(\Phi)}$ as the size of the smallest set of single-task policies $\mathcal{C}$ such that for every $\phi \in \Phi$, at least one $\pi \in \mathcal{C}$ has a cost ratio no greater than $\alpha$ relative to the optimal policy for $\phi$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the policies in $\mathcal{C}$ are parameterized functions, then $\mathcal{C}$ provides an upper bound on the number of parameters needed to represent an $\alpha$-suboptimal multi-task policy. In switching-based adaptive control, where $\phi$ is unknown, a smaller $\mathcal{C}$ implies a faster convergence time.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To study suboptimal covering numbers in a concrete setting, we consider linear dynamical systems with quadratic cost functions, or LQR problems. LQR problems are a common setting to analyze learning algorithms because detailed properties are known. This has led to new inquiries into their fundamental properties. We construct a family of well-behaved multi-task LQR problems where $\Phi$ is controlled by a "breadth" parameter $\theta \in {\lbrack 1,\infty)}$, and for which $N_{\alpha}{(\Phi_{\theta})}$ is finite and increasing in $\theta$. For the special case of a scalar LQR problem, we derive matching logarithmic upper and lower bounds on $N_{\alpha}{(\Phi_{\theta})}$ as a function of $\theta$. As an effort towards analogous bounds for the matrix case, we present empirical results intended to shed light on the problem structure. For the upper bound, we analyze properties of a logical extension of our scalar cover.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For the lower bound, we visualize suboptimal neighborhoods for two choices of "extremal" systems and find surprising topological behavior for one choice.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is an initial step towards a comprehensive theory. In addition to a more complete picture of deterministic LQR systems, ideas of $\alpha$-suboptimal coverings could be applied to a wide range of multi-task problems. We also hope they will lead to insights about function class expressiveness in learning-based multi-task control.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem setting", "weight": 1.0} -->

In this section, we first define suboptimal covering numbers with respect to an abstract multi-task control problem independent of distinctions such as continuous vs. discrete time and stochastic vs. deterministic. We then instantiate these notions for a particular class of LQR problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Standard LQR problem", "weight": 1.0} -->

A continuous-time, deterministic, infinite-horizon, time-invariant LQR problem with full-state feedback is defined by state space $\mathcal{X} = {\mathbb{R}}^{n}$, action space $\mathcal{U} = {\mathbb{R}}^{m}$, linear dynamics ${\overset{˙}{x} = {{Ax} + {Bu}}},$ where ${A \in {\mathbb{R}}^{n \times n}},{B \in {\mathbb{R}}^{n \times m}}$, and quadratic cost where $Q \succeq \mathbf{0}$ and $R \succ \mathbf{0}$ are cost matrices of appropriate dimensions and $\mathcal{N}{(\mathbf{0},I)}$ is the unit Gaussian distribution.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Standard LQR problem", "weight": 1.0} -->

For the purposes of this paper, the pair $(A,B)$ is *controllable* if ${J{(\pi)}} < \infty$ for some policy $\pi$. If $(A,B)$ is controllable, then the optimal policy is the linear $u = {K^{\star}x}$, where $K^{\star} \in {\mathbb{R}}^{m \times n}$ can be computed by finding the unique maximal positive semidefinite solution $P$ of the algebraic Riccati equation ${{{{A^{\top}P} + {PA}} - {PBR^{- 1}B^{\top}P}} + Q} = \mathbf{0}$ (henceforth called the *maximal solution*) and letting $K^{\star} = {- {R^{- 1}B^{\top}P}}$. Additionally, ${J{(K^{\star})}} = {{Tr}\lbrack P\rbrack}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Multi-dynamics LQR", "weight": 1.0} -->

A fully general formulation of multi-task LQR would allow variations in each of $(A,B,Q,R)$, but this creates redundancy. Any LQR problem where $Q \succ 0$ is equivalent via change of coordinates to another LQR problem where $Q = I$ and $R = I$. To reduce redundancy, we consider only *multi-dynamics* LQR problems where $Q = I_{n \times n}$ and $R = I_{m \times m}$ in this work. The reference policy class is linear: $\Pi_{ref} = {\mathbb{R}}^{m \times n}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Multi-dynamics LQR", "weight": 1.0} -->

A multi-dynamics LQR problem can be defined by $\Phi = {\mathbf{A} \times \mathbf{B}}$ for some sets $\mathbf{A} \subseteq {\mathbb{R}}^{n \times n}$ and $\mathbf{B} \subseteq {\mathbb{R}}^{n \times m}$, but it is not obvious how to design $\mathbf{A}$ and $\mathbf{B}$. To support an asymptotic analysis of $N_{\alpha}{(\Phi)}$, the task space $\Phi$ should have a real-valued "breadth" parameter $\theta$ that sweeps from a single task to sets with arbitrarily large, but finite, covering numbers. Matrix norm balls are a popular representation of dynamics uncertainty in the robust control literature, but they can easily contain uncontrollable pairs, and removing the uncontrollable pairs can lead to an infinite covering number.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Multi-dynamics LQR", "weight": 1.0} -->

For example, in the scalar problem ${\mathbf{A} = {\{ a\}}},{\mathbf{B} = {{\lbrack{- \theta},0)} \cup {(0,\theta\rbrack}}}$, where $a > 0$, it can be shown that no $\alpha$-suboptimal cover is finite.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Multi-dynamics LQR", "weight": 1.0} -->

These properties are worrying, but the example $\mathbf{B}$ is pathological. The zero crossing is analogous to reversing the direction of force applied by an actuator in a physical system. A more relevant multi-dynamics problem is variations in mass or actuator strength, whose signs are fixed. We formalize this idea with the following definition.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Decomposed dynamics form", "weight": 1.0} -->

The continuity of the LQR cost with respect to $B$ and the compactness of $\Phi$ for any $\theta$ imply that $N_{\alpha}{(\Phi_{\theta})}$ is always finite. Variations in $A$ are redundant in the scalar case where we focus our theoretical work in this paper. The definition can be extended to include them in future work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linearized quadrotor example", "weight": 1.0} -->

As an example of a realistic DDF problem, we consider the quadrotor helicopter illustrated in Figure 1. Near the hover state, its full nonlinear dynamics are well approximated by a linearization. The state is given by ${x = {(\mathbf{x},\mathbf{v},\mathbf{r},{\mathbf{ω}})}},$ where $\mathbf{x} \in {\mathbb{R}}^{3}$ is position, $\mathbf{v} \in {\mathbb{R}}^{3}$ is linear velocity, $\mathbf{r} \in {\mathbb{R}}^{3}$ is attitude Euler angles, and ${\mathbf{ω}} \in {\mathbb{R}}^{3}$ is angular velocity. The inputs $u \in {\mathbb{R}}_{\geq 0}^{4}$ are the squared angular velocities of the propellers.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Linearized quadrotor example", "weight": 1.0} -->

Many factors influence the response to inputs, including geometry, mass, moments of inertia, motor properties, and propeller aerodynamics. These can be combined and partially nondimensionalized into four control authority parameters to form $\phi \in \Phi$. The hover state occurs at ${x = \mathbf{0}},{u \propto \mathbf{1}}$, where the constant input counteracts gravity. The linearized dynamics are given by where $g$ is the gravitational constant and ${\hat{e}}_{z} = {\lbrack 0\ 0\ 1\rbrack}^{\top}$. The parameters $(\sigma_{z},\sigma_{\phi},\sigma_{\theta},\sigma_{\psi})$ denote the thrust, roll, pitch, and yaw authority constants respectively. Since we use the convention $\sigma \in {\lbrack\frac{1}{\theta},1\rbrack}$, the maximum value of each constant can be varied by scaling the columns of $U$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Theoretical results", "weight": 1.0} -->

In this section we show logarithmic upper and lower bounds on the growth of $N_{\alpha}{(\Phi_{\theta})}$ in $\theta$ for scalar DDF problems. We present several intermediate results in matrix form because they are needed for our empirical results later. We begin with a key lemma in the framework of *guaranteed cost control* (GCC) from Petersen and McFarlane, simplified for our use case.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Scalar upper bound", "weight": 1.0} -->

We are now ready to bound the covering number for scalar systems. The first lemma bounding $J_{a,b}^{\star}$ will be useful for the lower bound also. We then construct a cover inductively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Scalar lower bound", "weight": 1.0} -->

For the matching lower bound, we begin by deriving a simplified overestimate of $\mathcal{N}_{\alpha}{(k)}$. We then show that the true $\mathcal{N}_{\alpha}{(k)}$ is still a closed interval moving monotonically with $k$. Finally, we argue that the gaps between consecutive elements of a cover grow at most geometrically, while the range of $k$ values in a cover must grow linearly with $\theta$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remarks", "weight": 1.0} -->

For the upper bound, it may be possible to compute or bound $\beta$ in the scalar case as a function of $a$ and $\alpha$, but the analogous result will likely be much more complicated in the matrix case. thm:covering-scalar imposes a lower bound on $\alpha$ greater than $1$. We believe this is a mild condition in practice: if the application demands a suboptimality ratio very close to 1, then the size of the suboptimal cover is likely to become impractical for storage. However, further theoretical results building upon suboptimal coverings may require eliminating the bound.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Empirical results", "weight": 1.0} -->

For matrix DDF problems, we present empirical results as a first step towards covering number bounds. We begin by testing a cover construction. If the construction fails to achieve a conjectured upper bound in a numerical experiment, then either the conjecture is false, or the construction is not efficient. A natural idea is to extend the geometrically spaced sequence of $b$ values from \\lemmareflem:scalar-cost-ub to multiple dimensions. We now make this notion, illustrated in Figure 2, precise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Empirical upper bound on $N_{\\alpha}{(\\Phi)}$", "weight": 1.0} -->

In this experiment, we construct an $\alpha$-suboptimal cover $\mathcal{C}$ using geometric grids, such that each $K \in \mathcal{C}$ is $\alpha$-suboptimal for a full grid cell. For each cell $\mathbf{\Sigma}{(j)}$, we attempt GCC synthesis. If it succeeds, we check if ${\mathbf{\Sigma}{(j)}} \subseteq {\mathcal{N}_{\alpha}{({K{(j)}})}}$. If not, we increment the grid pitch $k$ and try again. Termination is guaranteed by continuity. We show results for the linearized quadrotor with $\alpha = 2$ in Figure 2. The data follow roughly logarithmic growth, as indicated by the linear least-squares best-fit curve in black. Small values of $\theta$ are excluded from the fit (indicated by grey points), as we do not expect the asymptotic growth pattern to appear yet.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Empirical upper bound on $N_{\\alpha}{(\\Phi)}$", "weight": 1.0} -->

These results do not rule out the $\log{(\theta)}^{d}$ growth suggested by the geometric grid construction. Testing larger values of $\theta$ is computationally difficult because the number of grid cells becomes huge and the GCC Riccati equation becomes numerically unstable for very small $\Sigma$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Efficiency of geometric grid partition", "weight": 1.0} -->

Given an $\alpha$-suboptimal geometric grid cover, we examine a measurable quantity that may reflect the "efficiency" of the cover. Intuitively, in a good cover we expect the suboptimality ratio of each controller $K{(j)}$ relative to its grid cell $\mathbf{\Sigma}{(j)}$ to be close to $\alpha$. If it close to $\alpha$ for some cells but significantly less than $\alpha$ for others, then the grid pitch around the latter cells is finer than necessary. We visualize results for this computation on the linearized quadrotor with ${\theta = 10},{k = 4}$ in Figure 2 --- only the corners of the $4 \times 4 \times 4 \times 4$ grid are shown. The suboptimality ratio is close to $\alpha = 2$ for cells with low control authority (near $\Sigma = {\frac{1}{\theta}I}$), but drops to around $1.4$ for cells with high control authority (near $\Sigma = I$).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Efficiency of geometric grid partition", "weight": 1.0} -->

The difference suggests that the geometric grid cover could be more efficient in the high-authority regime.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Efficiency of GCC synthesis", "weight": 1.0} -->

One possible source of conservativeness is that \\lemmareflem:petersen-gcc applies to the affine image of a $m \times n$-dimensional matrix norm ball, but we only require guaranteed cost on a $d$-dimensional affine subspace of diagonal matrices. In other words, we ask GCC synthesis to ensure $\alpha$-suboptimality on systems that are not actually part of $\Phi$. If this is negatively affecting the result, then we should observe that the worst-case cost of $K{(j)}$ on $\mathbf{\Sigma}{(j)}$ is less than the trace of the solution $P$ for the GCC Riccati equation. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")). The worst-case cost always occurs at the minimal $\Sigma \in {\mathbf{\Sigma}{(j)}}$ by \\lemmareflem:lancaster-ARE-domination; we evaluate it.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Efficiency of GCC synthesis", "weight": 1.0} -->

For the quadrotor, a mismatch sometimes occurs for smaller values of $\theta$, but it does not occur for the large values of $\theta$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Suboptimal neighborhood visualizations", "weight": 1.0} -->

We now present intuition-building experiments towards a covering number lower bound for matrix DDF problems. A lower bound requires a class of DDF problem that can be instantiated for any dimensionality $d$. Two choices come to mind: *minimum coupling*, where $A = I$, and *maximum coupling*, where $A = {\frac{1}{n}\mathbf{1}}$. Note that for minimum coupling, an $\alpha$-suboptimal policy is not necessarily $\alpha$-suboptimal on each scalar subsystem---if it were, the lower bound $\log{(\theta)}^{d}$ would trivially follow from the results in Section 3. $\overset{A{= I}}{\overbrace{}}\mspace{51mu}\overset{A{= {\frac{1}{n}\mathbf{1}}}}{\overbrace{}}$ Figure 3: α-suboptimal neighborhoods for geometric grid partition in 2D system.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Suboptimal neighborhood visualizations", "weight": 1.0} -->

Left: minimum coupling; A = I. Right: maximum coupling; $A = {\frac{1}{n}\mathbf{1}}$. Columns: varying suboptimality threshold α. All axes are logarithmic. Colors have no meaning. Discussion in Section 4.1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Suboptimal neighborhood visualizations", "weight": 1.0} -->

We show approximate suboptimal neighborhoods for a two-dimensional system in Figure 3. We select a geometric grid of $\Sigma$ values (indicated by the circular markers) and synthesize their LQR-optimal controllers. Then, we evaluate the suboptimality ratio of each controller on a finer grid of $\Sigma$ values to get approximate neighborhoods, indicated by the semi-transparent regions. We repeat this experiment with three values of $\alpha$ for both choices of $A$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Suboptimal neighborhood visualizations", "weight": 1.0} -->

Interestingly, the neighborhoods for $A = I$ are not always connected. In the plot for $\alpha = 1.05$ (far left), the neighborhood for the minimal $\Sigma$ has another component that overlaps other neighborhoods to its top and right. If we increase to $\alpha = 1.1$, the components join into an "L"-shaped region. In contrast, the neighborhoods for $A = {\frac{1}{n}\mathbf{1}}$ seem more well-behaved. For both choices of $A$, the neighborhoods are of comparable size.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Suboptimal neighborhood visualizations", "weight": 1.0} -->

To verify that this behavior is not an artifact of the two-dimensional case only, we repeat the experiment in three dimensions. Figure 4 shows neighborhoods of one controller $K = K_{{({2/\theta})}I}^{\star}$ for $\alpha$ ranging from $1.04$ to $1.2$. As $\alpha$ grows, $\mathcal{N}_{\alpha}{(K)}$ shows similar topological phases as the $2$D case. In the simply-connected phase (large $\alpha$), the neighborhood appears to include any $\Sigma$ where at least one $\sigma_{i}$ is sufficiently small. If this property holds in higher dimensions, then it would be possible to construct a cover using only controllers of uniform gain in all dimensions for large $\alpha$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

In this paper, we introduced and motivated the $\alpha$-suboptimal covering number to quantify infinite task spaces for multi-task control problems. We defined a particular class of multi-task linear-quadratic regulator problems amenable to analysis of the $\alpha$-suboptimal covering number, and showed logarithmic dependency on the problem "breadth" parameter $\theta$ in the scalar case. Towards analogous results for the matrix case, we presented empirical studies intended to shed light on possible proof techniques. For the upper bound, we considered a natural covering construction that would preserve logarithmic dependence on $\theta$ but give exponential dependence on dimensionality. Experiments did not rule out its validity. For the lower bound, we visualized suboptimal neighborhoods for two possible system classes and observed interesting topological behavior for the minimal-coupling class.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

After extending our current results to the matrix case, in future work the analysis can be applied to other classes of multi-task LQR problems including variations in $A,Q,R$, discrete time, and stochastic dynamics. It will be interesting to see if there are major differences between LQR variants. We also hope that suboptimal covers and covering numbers will be a useful tool for analyzing how the size of the task space affects the required expressiveness of function classes used in practice as multi-task policies, such as neural networks.
