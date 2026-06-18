<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Differential Equation for Modeling Nesterov's Accelerated Gradient Method: Theory and Insights

Topics include Nesterov acceleration, Ordinary differential equation, Differential equation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We derive a second-order ordinary differential equation (ODE) which is the limit of Nesterov's accelerated gradient method. This ODE exhibits approximate equivalence to Nesterov's scheme and thus can serve as a tool for analysis. We show that the continuous time ODE allows for a better understanding of Nesterov's scheme. As a byproduct, we obtain a family of schemes with similar convergence rates. The ODE interpretation also suggests restarting Nesterov's scheme leading to an algorithm, which can be rigorously proven to converge at a linear rate whenever the objective is strongly convex.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many fields of machine learning, minimizing a convex function is at the core of efficient model estimation. In the simplest and most standard form, we are interested in solving

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $f$ is a convex function, smooth or non-smooth, and $x \in {\mathbb{R}}^{n}$ is the variable. Since Newton, numerous algorithms and methods have been proposed to solve the minimization problem, notably gradient and subgradient descent, Newton's methods, trust region methods, conjugate gradient methods, and interior point methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

First-order methods have regained popularity as data sets and problems are ever increasing in size and, consequently, there has been much research on the theory and practice of accelerated first-order schemes. Perhaps the earliest first-order method for minimizing a convex function $f$ is the gradient method, which dates back to Euler and Lagrange. Thirty years ago, however, in a seminal paper Nesterov proposed an accelerated gradient method, which may take the following form: starting with $x_{0}$ and $y_{0} = x_{0}$, inductively define

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For any fixed step size $s \leq {1/L}$, where $L$ is the Lipschitz constant of $\nabla f$, this scheme exhibits the convergence rate

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Above, $x^{\star}$ is any minimizer of $f$ and $f^{\star} = {f{(x^{\star})}}$. It is well-known that this rate is optimal among all methods having only information about the gradient of $f$ at consecutive iterates. This is in contrast to vanilla gradient descent methods, which have the same computational complexity but can only achieve a rate of $O{({1/k})}$. This improvement relies on the introduction of the momentum term $x_{k} - x_{k - 1}$ as well as the particularly tuned coefficient ${{({k - 1})}/{({k + 2})}} \approx {1 - {3/k}}$. Since the introduction of Nesterov's scheme, there has been much work on the development of first-order accelerated methods, see Nesterov for theoretical developments, and Tseng for a unified analysis of these ideas. Notable applications can be found in sparse linear regression, compressed sensing and, deep and recurrent neural networks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In a different direction, there is a long history relating ordinary differential equation (ODEs) to optimization, see Helmke and Moore, Schropp and Singer, and Fiori for example. The connection between ODEs and numerical optimization is often established via taking step sizes to be very small so that the trajectory or solution path converges to a curve modeled by an ODE. The conciseness and well-established theory of ODEs provide deeper insights into optimization, which has led to many interesting findings. Notable examples include linear regression via solving differential equations induced by linearized Bregman iteration algorithm, a continuous-time Nesterov-like algorithm in the context of control design, and modeling design iterative optimization algorithms as nonlinear dynamical systems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we derive a second-order ODE which is the exact limit of Nesterov's scheme by taking small step sizes; to the best of our knowledge, this work is the first to use ODEs to model Nesterov's scheme or its variants in this limit. One surprising fact in connection with this subject is that a first-order scheme is modeled by a second-order ODE.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

for $t > 0$, with initial conditions ${{X{}} = x_{0}},{{\overset{˙}{X}{}} = 0}$; here, $x_{0}$ is the starting point in Nesterov's scheme, $\overset{˙}{X} \equiv {{{dX}/d}t}$ denotes the time derivative or velocity and similarly $\overset{¨}{X} \equiv {{{d^{2}X}/d}t^{2}}$ denotes the acceleration. The time parameter in this ODE is related to the step size in via $t \approx {k\sqrt{s}}$. Expectedly, it also enjoys inverse quadratic convergence rate as its discrete analog,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Approximate equivalence between Nesterov's scheme and the ODE is established later in various perspectives, rigorous and intuitive. In the main body of this paper, examples and case studies are provided to demonstrate that the homogeneous and conceptually simpler ODE can serve as a tool for understanding, analyzing and generalizing Nesterov's scheme.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the following, two insights of Nesterov's scheme are highlighted, the first one on oscillations in the trajectories of this scheme, and the second on the peculiar constant 3 appearing in the ODE.

<!-- chunk {"id": "body-0013", "role": "body", "section": "From Overdamping to Underdamping", "weight": 1.0} -->

In general, Nesterov's scheme is not monotone in the objective function value due to the introduction of the momentum term. Oscillations or overshoots along the trajectory of iterates approaching the minimizer are often observed when running Nesterov's scheme. Figure 1 presents typical phenomena of this kind, where a two-dimensional convex function is minimized by Nesterov's scheme. Viewing the ODE as a damping system, we obtain interpretations as follows.

<!-- chunk {"id": "body-0014", "role": "body", "section": "From Overdamping to Underdamping", "weight": 1.0} -->

Small $t$. In the beginning, the damping ratio $3/t$ is large. This leads the ODE to be an overdamped system, returning to the equilibrium without oscillating;\
Large $t$. As $t$ increases, the ODE with a small $3/t$ behaves like an underdamped system, oscillating with the amplitude gradually decreasing to zero.

<!-- chunk {"id": "body-0015", "role": "body", "section": "From Overdamping to Underdamping", "weight": 1.0} -->

As depicted in Figure 1(a), in the beginning the ODE curve moves smoothly towards the origin, the minimizer $x^{\star}$. The second interpretation "Large $t$'' provides partial explanation for the oscillations observed in Nesterov's scheme at later stage. Although our analysis extends farther, it is similar in spirit to that carried in O'Donoghue and Candès. In particular, the zoomed Figure 1(b) presents some butterfly-like oscillations for both the scheme and ODE. There, we see that the trajectory constantly moves away from the origin and returns back later. Each overshoot in Figure 1(b) causes a bump in the function values, as shown in Figure 1(c). We observe also from Figure 1(c) that the periodicity captured by the bumps are very close to that of the ODE solution. In passing, it is worth mentioning that the solution to the ODE in this case can be expressed via Bessel functions, hence enabling quantitative characterizations of these overshoots and bumps, which are given in full detail in Section 3.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Phase Transition", "weight": 1.0} -->

The constant 3, derived from ${({k + 2})} - {({k - 1})}$, is not haphazard. In fact, it is the smallest constant that guarantees $O{({1/t^{2}})}$ convergence rate. Specifically, parameterized by a constant $r$, the generalized ODE

<!-- chunk {"id": "body-0017", "role": "body", "section": "Phase Transition", "weight": 1.0} -->

can be translated into a generalized Nesterov's scheme that is the same as the original except for ${({k - 1})}/{({k + 2})}$ being replaced by ${({k - 1})}/{({{k + r} - 1})}$. Surprisingly, for both generalized ODEs and schemes, the inverse quadratic convergence is guaranteed if and only if $r \geq 3$. This phase transition suggests there might be deep causes for acceleration among first-order methods. In particular, for $r \geq 3$, the worst case constant in this inverse quadratic convergence rate is minimized at $r = 3$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Outline and Notation", "weight": 1.0} -->

The rest of the paper is organized as follows. In Section 2, the ODE is rigorously derived from Nesterov's scheme, and a generalization to composite optimization, where $f$ may be non-smooth, is also obtained. Connections between the ODE and the scheme, in terms of trajectory behaviors and convergence rates, are summarized in Section 3. In Section 4, we discuss the effect of replacing the constant $3$ in by an arbitrary constant on the convergence rate. A new restarting scheme is suggested in Section 5, with linear convergence rate established and empirically observed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Outline and Notation", "weight": 1.0} -->

Some standard notations used throughout the paper are collected here. We denote by $\mathcal{F}_{L}$ the class of convex functions $f$ with $L$--Lipschitz continuous gradients defined on ${\mathbb{R}}^{n}$, i.e., $f$ is convex, continuously differentiable, and satisfies

<!-- chunk {"id": "body-0020", "role": "body", "section": "Derivation", "weight": 1.0} -->

First, we sketch an informal derivation of the ODE. Assume $f \in \mathcal{F}_{L}$ for $L > 0$. Combining the two equations of and applying a rescaling gives

<!-- chunk {"id": "body-0021", "role": "body", "section": "Derivation", "weight": 1.0} -->

By comparing the coefficients of $\sqrt{s}$, we obtain

<!-- chunk {"id": "body-0022", "role": "body", "section": "Derivation", "weight": 1.0} -->

The first initial condition is ${X{}} = x_{0}$. Taking $k = 1$ in yields

<!-- chunk {"id": "body-0023", "role": "body", "section": "Derivation", "weight": 1.0} -->

Hence, the second initial condition is simply ${\overset{˙}{X}{}} = 0$ (vanishing initial velocity).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Derivation", "weight": 1.0} -->

Classical results in ODE theory do not directly imply the existence or uniqueness of the solution to this ODE because the coefficient $3/t$ is singular at $t = 0$. In addition, $\nabla f$ is typically not analytic at $x_{0}$, which leads to the inapplicability of the power series method for studying singular ODEs. Nevertheless, the ODE is well posed: the strategy we employ for showing this constructs a series of ODEs approximating, and then chooses a convergent subsequence by some compactness arguments such as the Arzelá-Ascoli theorem.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simple Properties", "weight": 1.0} -->

We collect some elementary properties that are helpful in understanding the ODE.\
Time Invariance. If we adopt a linear time transformation, $\overset{\sim}{t} = {ct}$ for some $c > 0$, by the chain rule it follows that

<!-- chunk {"id": "body-0026", "role": "body", "section": "Simple Properties", "weight": 1.0} -->

This yields the ODE parameterized by $\overset{\sim}{t}$,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Simple Properties", "weight": 1.0} -->

Also note that minimizing $f/c^{2}$ is equivalent to minimizing $f$. Hence, the ODE is invariant under the time change. In fact, it is easy to see that time invariance holds if and only if the coefficient of $\overset{˙}{X}$ has the form $C/t$ for some constant $C$.\
Rotational Invariance. Nesterov's scheme and other gradient-based schemes are invariant under rotations. As expected, the ODE is also invariant under orthogonal transformation. To see this, let $Y = {QX}$ for some orthogonal matrix $Q$. This leads to ${\overset{˙}{Y} = {Q\overset{˙}{X}}},{\overset{¨}{Y} = {Q\overset{¨}{X}}}$ and ${\nabla_{Y}f} = {Q{\nabla_{X}f}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simple Properties", "weight": 1.0} -->

Hence, denoting by $Q^{T}$ the transpose of $Q$, the ODE in the new coordinate system reads ${{Q^{T}\overset{¨}{Y}} + {\frac{3}{t}Q^{T}\overset{˙}{Y}} + {Q^{T}{\nabla_{Y}f}}} = 0$, which is of the same form as once multiplying $Q$ on both sides.\
Initial Asymptotic. Assume sufficient smoothness of $X$ such that $\lim_{t\rightarrow 0}{\overset{¨}{X}{(t)}}$ exists.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simple Properties", "weight": 1.0} -->

This asymptotic expansion is consistent with the empirical observation that Nesterov's scheme moves slowly in the beginning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "ODE for Composite Optimization", "weight": 1.0} -->

It is interesting and important to generalize the ODE to minimizing $f$ in the composite form ${f{(x)}} = {{g{(x)}} + {h{(x)}}}$, where the smooth part $g \in \mathcal{F}_{L}$ and the non-smooth part $h:{{\mathbb{R}}^{n}\rightarrow{({- \infty},\infty\rbrack}}$ is a structured general convex function. Both Nesterov and Beck and Teboulle obtain $O{({1/k^{2}})}$ convergence rate by employing the proximal structure of $h$. In analogy to the smooth case, an ODE for composite $f$ is derived in the appendix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Connections and Interpretations", "weight": 1.0} -->

In this section, we explore the approximate equivalence between the ODE and Nesterov's scheme, and provide evidence that the ODE can serve as an amenable tool for interpreting and analyzing Nesterov's scheme. The first subsection exhibits inverse quadratic convergence rate for the ODE solution, the next two address the oscillation phenomenon discussed in Section 1.1, and the last subsection is devoted to comparing Nesterov's scheme with gradient descent from a numerical perspective.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Analogous Convergence Rate", "weight": 1.0} -->

The original result from Nesterov states that, for any $f \in \mathcal{F}_{L}$, the sequence $\{ x_{k}\}$ given by with step size $s \leq {1/L}$ satisfies

<!-- chunk {"id": "body-0033", "role": "body", "section": "Analogous Convergence Rate", "weight": 1.0} -->

Our next result indicates that the trajectory of closely resembles the sequence $\{ x_{k}\}$ in terms of the convergence rate to a minimizer $x^{\star}$. Compared with the discrete case, this proof is shorter and simpler.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

For quadratic $f$, the ODE admits a solution in closed form. This closed form solution turns out to be very useful in understanding the issues raised in the introduction.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

Let ${f{(x)}} = {{\frac{1}{2}{\langle x,{Ax}\rangle}} + {\langle b,x\rangle}}$, where $A \in {\mathbb{R}}^{n \times n}$ is a positive semidefinite matrix and $b$ is in the column space of $A$ because otherwise this function can attain $- \infty$. Then a simple translation in $x$ can absorb the linear term $\langle b,x\rangle$ into the quadratic term. Since both the ODE and the scheme move within the affine space perpendicular to the kernel of $A$, without loss of generality, we assume that $A$ is positive definite, admitting a spectral decomposition $A = {Q^{T}\LambdaQ}$, where $\Lambda$ is a diagonal matrix formed by the eigenvalues.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

Replacing $x$ with $Qx$, we assume $f = {\frac{1}{2}{\langle x,{\Lambdax}\rangle}}$ from now. Now, the ODE for this function admits a simple decomposition of form

<!-- chunk {"id": "body-0037", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

This is Bessel's differential equation of order one. Since $Y_{i}$ vanishes at $u = 0$, we see that $Y_{i}$ is a constant multiple of $J_{1}$, the Bessel function of the first kind of order one.^22^2Up to a constant multiplier, $J_{1}$ is the unique solution to the Bessel's differential equation ${{u^{2}{\overset{¨}{J}}_{1}} + {u{\overset{˙}{J}}_{1}} + {{({u^{2} - 1})}J_{1}}} = 0$ that is finite at the origin.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

In the analytic expansion of $J_{1}$, $m!!$ denotes the double factorial defined as ${m!!} = {m \times {({m - 2})} \times \cdots \times 2}$ for even $m$, or ${m!!} = {m \times {({m - 2})} \times \cdots \times 1}$ for odd $m$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

which gives the asymptotic expansion

<!-- chunk {"id": "body-0040", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

This asymptotic expansion yields (note that $f^{\star} = 0$)

<!-- chunk {"id": "body-0041", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

In view of, Nesterov's scheme might possibly exhibit $O{({1/k^{3}})}$ convergence rate for strongly convex functions. This convergence rate is consistent with the second inequality in Theorem 6. In Section 4.3, we prove the $O{({1/t^{3}})}$ rate for a generalized version of. However, rules out the possibility of a higher order convergence rate.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

Recall that the function considered in Figure 1 is ${f{(x)}} = {{0.02x_{1}^{2}} + {0.005x_{2}^{2}}}$, starting from $x_{0} = {}$. As the step size $s$ becomes smaller, the trajectory of Nesterov's scheme converges to the solid curve represented via the Bessel function. While approaching the minimizer $x^{\star}$, each trajectory displays the oscillation pattern, as well-captured by the zoomed Figure 1(b). This prevents Nesterov's scheme from achieving better convergence rate. The representation offers excellent explanation as follows. Denote by $T_{1},T_{2}$, respectively, the approximate periodicities of the first component $|X_{1}|$ in absolute value and the second $|X_{2}|$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Quadratic $f$ and Bessel Functions", "weight": 1.0} -->

A careful look at Figure 1(c) reveals that within each major bump, roughly, there are ${{10\pi}/T_{1}} = 2$ minor peaks.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Fluctuations of Strongly Convex $f$", "weight": 1.0} -->

The analysis carried out in the previous subsection only applies to convex quadratic functions. In this subsection, we extend the discussion to one-dimensional strongly convex functions. The Sturm-Picone theory is extensively used all along the analysis.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Fluctuations of Strongly Convex $f$", "weight": 1.0} -->

Let $f \in {\mathcal{S}_{\mu,L}{({\mathbb{R}})}}$. Without loss of generality, assume $f$ attains minimum at $x^{\star} = 0$. Then, by definition $\mu \leq {{f^{\prime}{(x)}}/x} \leq L$ for any $x \neq 0$. Denoting by $X$ the solution to the ODE, we consider the self-adjoint equation,

<!-- chunk {"id": "body-0046", "role": "body", "section": "Fluctuations of Strongly Convex $f$", "weight": 1.0} -->

which, apparently, admits a solution ${Y{(t)}} = {X{(t)}}$. To apply the Sturm-Picone comparison theorem, consider

<!-- chunk {"id": "body-0047", "role": "body", "section": "Fluctuations of Strongly Convex $f$", "weight": 1.0} -->

To obtain a similar result in the opposite direction, consider

<!-- chunk {"id": "body-0048", "role": "body", "section": "Fluctuations of Strongly Convex $f$", "weight": 1.0} -->

Applying the Sturm-Picone comparison theorem to and, we ensure that between any two consecutive positive roots of $X$, there is at least one ${\overset{\sim}{t}}_{i}/\sqrt{L}$. Now, we summarize our findings in the following. Roughly speaking, this result concludes that the oscillation frequency of the ODE solution is between $O{(\sqrt{\mu})}$ and $O{(\sqrt{L})}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

The ansatz $t \approx {k\sqrt{s}}$ in relating the ODE and Nesterov's scheme is formally confirmed in Theorem 2. Consequently, for any constant $t_{c} > 0$, this implies that $x_{k}$ does not change much for a range of step sizes $s$ if $k \approx {t_{c}/\sqrt{s}}$. To empirically support this claim, we present an example in Figure 3(a), where the scheme minimizes ${f{(x)}} = {{{\|{y - {Ax}}\|}^{2}/2} + {\| x\|}_{1}}$ with $y = {}$ and ${{A{(:,1)}} = {}},{{A{(:,2)}} = {}}$ starting from $x_{0} = {}$ (here $A{(:,j)}$ is the $j$th column of $A$).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

From this figure, we are delight to observe that $x_{k}$ with the same $t_{c}$ are very close to each other.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

This interesting square-root scaling has the potential to shed light on the superiority of Nesterov's scheme over gradient descent. Roughly speaking, each iteration in Nesterov's scheme amounts to traveling $\sqrt{s}$ in time along the integral curve of, whereas it is known that the simple gradient descent $x_{k + 1} = {x_{k} - {s{\nabla f}{(x_{k})}}}$ moves $s$ along the integral curve of ${\overset{˙}{X} + {{\nabla f}{(X)}}} = 0$. We expect that for small $s$ Nesterov's scheme moves more in each iteration since $\sqrt{s}$ is much larger than $s$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

Figure 3(b) illustrates and supports this claim, where the function minimized is $f = {{|x_{1}|}^{3} + {5{|x_{2}|}^{3}} + {0.001{({x_{1} + x_{2}})}^{2}}}$ with step size $s = 0.05$ (The coordinates are appropriately rotated to allow $x_{0}$ and $x^{\star}$ lie on the same horizontal line). The circles are the iterates for $k = {1,10,20,30,45,60,90,120,150,190,250,300}$. For Nesterov's scheme, the seventh circle has already passed $t = 15$, while for gradient descent the last point has merely arrived at $t = 15$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

(b) Race between Nesterov’s and gradient.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

A second look at Figure 3(b) suggests that Nesterov's scheme allows a large deviation from its limit curve, as compared with gradient descent. This raises the question of the stable step size allowed for numerically solving the ODE in the presence of accumulated errors. The finite difference approximation by the forward Euler method is

<!-- chunk {"id": "body-0055", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

Assuming $f$ is sufficiently smooth, we have ${{\nabla f}{({x + {\deltax}})}} \approx {{{\nabla f}{(x)}} + {{\nabla^{2}f}{(x)}\deltax}}$ for small perturbations $\deltax$, where ${\nabla^{2}f}{(x)}$ is the Hessian of $f$ evaluated at $x$. Identifying $k = {{t/\Delta}t}$, the characteristic equation of this finite difference scheme is approximately

<!-- chunk {"id": "body-0056", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

The numerical stability of with respect to accumulated errors is equivalent to this: all the roots of lie in the unit circle. When ${\nabla^{2}f} \preceq {LI_{n}}$ (i.e. ${LI_{n}} - {\nabla^{2}f}$ is positive semidefinite), if ${\Deltat}/t$ small and ${\Deltat} < {2/\sqrt{L}}$, we see that all the roots of lie in the unit circle. On the other hand, if ${\Deltat} > {2/\sqrt{L}}$, can possibly have a root $\lambda$ outside the unit circle, causing numerical instability. Under our identification $s = {\Deltat^{2}}$, a step size of $s = {1/L}$ in Nesterov's scheme is approximately equivalent to a step size of ${\Deltat} = {1/\sqrt{L}}$ in the forward Euler method, which is stable for numerically integrating.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Nesterov's Scheme Compared with Gradient Descent", "weight": 1.0} -->

Thus, to guarantee ${- I_{n}} \preceq {1 - {\Deltat{\nabla^{2}f}}} \preceq I_{n}$ in worst case analysis, one can only choose ${\Deltat} \leq {2/L}$ for a fixed step size, which is much smaller than the step size $2/\sqrt{L}$ for when $\nabla f$ is very variable, i.e., $L$ is large.

<!-- chunk {"id": "body-0058", "role": "body", "section": "The Magic Constant 3", "weight": 1.0} -->

Recall that the constant 3 appearing in the coefficient of $\overset{˙}{X}$ in originates from ${{({k + 2})} - {({k - 1})}} = 3$. This number leads to the momentum coefficient in taking the form ${{({k - 1})}/{({k + 2})}} = {{1 - {3/k}} + {O{({1/k^{2}})}}}$. In this section, we demonstrate that 3 can be replaced by any larger number, while maintaining the $O{({1/k^{2}})}$ convergence rate.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Magic Constant 3", "weight": 1.0} -->

with initial conditions ${{X{}} = x_{0}},{{\overset{˙}{X}{}} = 0}$. The proof of Theorem 1, which seamlessly applies here, guarantees the existence and uniqueness of the solution $X$ to this ODE.

<!-- chunk {"id": "body-0060", "role": "body", "section": "The Magic Constant 3", "weight": 1.0} -->

Interpreting the damping ratio $r/t$ as a measure of friction^33^3In physics and engineering, damping may be modeled as a force proportional to velocity but opposite in direction, i.e. resisting motion; for instance, this force may be used as an approximation to the friction caused by drag. In our model, this force would be proportional to $- {\frac{r}{t}\overset{˙}{X}}$ where $\overset{˙}{X}$ is velocity and $\frac{r}{t}$ is the damping coefficient. in the damping system, our results say that more friction does not end the $O{({1/t^{2}})}$ and $O{({1/k^{2}})}$ convergence rate. On the other hand, in the lower friction setting, where $r$ is smaller than 3, we can no longer expect inverse quadratic convergence rate, unless some additional structures of $f$ are imposed. We believe that this striking phase transition at 3 deserves more attention as an interesting research challenge.

<!-- chunk {"id": "body-0061", "role": "body", "section": "High Friction", "weight": 1.0} -->

Here, we study the convergence rate of with $r > 3$ and $f \in \mathcal{F}_{\infty}$. Compared, this new ODE as a damping suffers from higher friction. Following the strategy adopted in the proof of Theorem 3, we consider a new energy functional defined as

<!-- chunk {"id": "body-0062", "role": "body", "section": "High Friction", "weight": 1.0} -->

By studying the derivative of this functional, we get the following result.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Low Friction", "weight": 1.0} -->

Now we turn to the case $r < 3$. Then, unfortunately, the energy functional approach for proving Theorem 5 is no longer valid, since the left-hand side of is positive in general. In fact, there are counterexamples that fail the desired $O{({1/t^{2}})}$ or $O{({1/k^{2}})}$ convergence rate. We present such examples in continuous time. Equally, these examples would also violate the $O{({1/k^{2}})}$ convergence rate in the discrete schemes, and we forego the details.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Low Friction", "weight": 1.0} -->

where the exponent $r$ is tight. This rules out the possibility of inverse quadratic convergence of the generalized ODE and scheme for all $f \in \mathcal{F}_{L}$ if $r < 2$. An example with $r = 1$ is plotted in Figure 2.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Low Friction", "weight": 1.0} -->

Next, we consider the case $2 \leq r < 3$ and let ${f{(x)}} = {|x|}$ (this also applies to multivariate $f = {\| x\|}$).^44^4This function does not have a Lipschitz continuous gradient. However, a similar pattern as in Figure 2 can be also observed if we smooth $|x|$ at an arbitrarily small vicinity of 0. Starting from $x_{0} > 0$, we get ${X{(t)}} = {x_{0} - \frac{t^{2}}{2{({1 + r})}}}$ for $t \leq \sqrt{2{({1 + r})}x_{0}}$. Requiring continuity of $X$ and $\overset{˙}{X}$ at the change point 0, we get

<!-- chunk {"id": "body-0066", "role": "body", "section": "Low Friction", "weight": 1.0} -->

For illustration, Figure 4 plots $t^{2}{({{f{({X{(t)}})}} - f^{\star}})}$ and $sk^{2}{({{f{(x_{k})}} - f^{\star}})}$ with $r = {2,2.5}$, and $r = 4$ for comparison^55^5For Figures 4(d), 4(e) and 4(f), if running generalized Nesterov's schemes with too many iterations (e.g. $10^{5}$), the deviations from the ODE will grow. Taking a sufficiently small $s$ can solve this issue.. It is clearly that inverse quadratic convergence does not hold for $r = {2,2.5}$, that is, does not hold for $r < 3$. Interestingly, in Figures 4(a) and 4(d), the scaled errors at peaks grow linearly, whereas for $r = 2.5$, the growth rate, though positive as well, seems sublinear.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Low Friction", "weight": 1.0} -->

However, if $f$ possesses some additional property, inverse quadratic convergence is still guaranteed, as stated below. In that theorem, $f$ is assumed to be a continuously differentiable convex function.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Strongly Convex $f$", "weight": 1.0} -->

Strong convexity is a desirable property for optimization. Making use of this property carefully suggests a generalized Nesterov's scheme that achieves optimal linear convergence. In that case, even vanilla gradient descent has a linear convergence rate. Unfortunately, the example given in the previous subsection simply rules out such possibility for and its generalizations. However, from a different perspective, this example suggests that $O{(t^{- r})}$ convergence rate can be expected. In the next theorem, we prove a slightly weaker statement of this kind, that is, a provable $O{(t^{- \frac{2r}{3}})}$ convergence rate is established for strongly convex functions. Bridging this gap may require new tools and more careful analysis.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

We study six synthetic examples to compare with the step sizes are fixed to be $1/L$, as illustrated in Figure 5. The error rates exhibits similar patterns for all $r$, namely, decreasing while suffering from local bumps. A smaller $r$ introduces less friction, thus allowing $x_{k}$ moves towards $x^{\star}$ faster in the beginning. However, when sufficiently close to $x^{\star}$, more friction is preferred in order to reduce overshoot. This point of view explains what we observe in these examples. That is, across these six examples, with a smaller $r$ performs slightly better in the beginning, but a larger $r$ has advantage when $k$ is large. It is an interesting question how to choose a good $r$ for different problems in practice.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Lasso with square design. Minimize ${f{(x)}} = {{\frac{1}{2}{\|{{Ax} - b}\|}^{2}} + {\lambda{\| x\|}_{1}}}$, where $A$ a $500 \times 500$ random matrix with i.i.d. standard Gaussian entries, $b$ generated independently has i.i.d. $\mathcal{N}{}$ entries, and the penalty $\lambda = 4$. The plot is Figure 5(b).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Nonnegative least squares (NLS) with fat design. Minimize ${f{(x)}} = {\|{{Ax} - b}\|}^{2}$ subject to $x \succeq 0$, with the same design $A$ and $b$ as in Figure 5(a). The plot is Figure 5(c).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Nonnegative least squares with sparse design. Minimize ${f{(x)}} = {\|{{Ax} - b}\|}^{2}$ subject to $x \succeq 0$, in which $A$ is a $1000 \times 10000$ sparse matrix with nonzero probability $10\%$ for each entry and $b$ is given as $b = {{Ax^{0}} + {\mathcal{N}{(0,I_{1000})}}}$. The nonzero entries of $A$ are independently Gaussian distributed before column normalization, and $x^{0}$ has 100 nonzero entries that are all equal to 4. The plot is Figure 5(d).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Restarting", "weight": 1.0} -->

The example discussed in Section 4.2 demonstrates that Nesterov's scheme and its generalizations are not capable of fully exploiting strong convexity. That is, this example suggests evidence that $O{({{1/{\mathtt{p}\mathtt{o}\mathtt{l}\mathtt{y}}}{(k)}})}$ is the best rate achievable under strong convexity. In contrast, the vanilla gradient method achieves linear convergence $O{({({1 - {\mu/L}})}^{k})}$. This drawback results from too much momentum introduced when the objective function is strongly convex. The derivative of a strongly convex function is generally more reliable than that of non-strongly convex functions. In the language of ODEs, at later stage a too small $3/t$ in leads to a lack of friction, resulting in unnecessary overshoot along the trajectory.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Restarting", "weight": 1.0} -->

Incorporating the optimal momentum coefficient $\frac{\sqrt{L} - \sqrt{\mu}}{\sqrt{L} + \sqrt{\mu}}$ (This is less than ${({k - 1})}/{({k + 2})}$ when $k$ is large), Nesterov's scheme has convergence rate of $O{({({1 - \sqrt{\mu/L}})}^{k})}$, which, however, requires knowledge of the condition number $\mu/L$. While it is relatively easy to bound the Lipschitz constant $L$ by the use of backtracking, estimating the strong convexity parameter $\mu$, if not impossible, is very challenging.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Restarting", "weight": 1.0} -->

Among many approaches to gain acceleration via adaptively estimating $\mu/L$, O'Donoghue and Candès proposes a procedure termed as gradient restarting for Nesterov's scheme in which is restarted with $x_{0} = y_{0}:=x_{k}$ whenever ${f{(x_{k + 1})}} > {f{(x_{k})}}$. In the language of ODEs, this restarting essentially keeps $\langle{\nabla f},\overset{˙}{X}\rangle$ negative, and resets $3/t$ each time to prevent this coefficient from steadily decreasing along the trajectory. Although it has been empirically observed that this method significantly boosts convergence, there is no general theory characterizing the convergence rate.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Restarting", "weight": 1.0} -->

In this section, we propose a new restarting scheme we call the speed restarting scheme. The underlying motivation is to maintain a relatively high velocity $\overset{˙}{X}$ along the trajectory, similar in spirit to the gradient restarting. Specifically, our main result, Theorem 10, ensures linear convergence of the continuous version of the speed restarting. More generally, our contribution here is merely to provide a framework for analyzing restarting schemes rather than competing with other schemes; it is beyond the scope of this paper to get optimal constants in these results. Throughout this section, we assume $f \in \mathcal{S}_{\mu,L}$ for some $0 < \mu \leq L$. Recall that function $f \in \mathcal{S}_{\mu,L}$ if $f \in \mathcal{F}_{L}$ and ${f{(x)}} - {{\mu{\| x\|}^{2}}/2}$ is convex.

<!-- chunk {"id": "body-0077", "role": "body", "section": "New Restarting Scheme", "weight": 1.0} -->

We first define the speed restarting time. For the ODE, we call

<!-- chunk {"id": "body-0078", "role": "body", "section": "New Restarting Scheme", "weight": 1.0} -->

the speed restarting time. In words, $T$ is the first time the velocity $\|\overset{˙}{X}\|$ decreases. Back to the discrete scheme, it is the first time when we observe ${\|{x_{k + 1} - x_{k}}\|} < {\|{x_{k} - x_{k - 1}}\|}$. This definition itself does not directly imply that $0 < T < \infty$, which is proven later in Lemmas 13 and 25. Indeed, $f{({X{(t)}})}$ is a decreasing function before time $T$; for $t \leq T$,

<!-- chunk {"id": "body-0079", "role": "body", "section": "New Restarting Scheme", "weight": 1.0} -->

The speed restarted ODE is thus

<!-- chunk {"id": "body-0080", "role": "body", "section": "New Restarting Scheme", "weight": 1.0} -->

where $t_{sr}$ is set to zero whenever ${\langle\overset{˙}{X},\overset{¨}{X}\rangle} = 0$ and between two consecutive restarts, $t_{sr}$ grows just as $t$. That is, $t_{sr} = {t - \tau}$, where $\tau$ is the latest restart time. In particular, $t_{sr} = 0$ at $t = 0$. Letting $X^{sr}$ be the solution to, we have the following observations.

<!-- chunk {"id": "body-0081", "role": "body", "section": "New Restarting Scheme", "weight": 1.0} -->

The theorem below guarantees linear convergence of $X^{sr}$. This is a new result in the literature. The proof of Theorem 10 is based on Lemmas 12 and 13, where the first guarantees the rate ${f{(X^{sr})}} - f^{\star}$ decays by a constant factor for each restarting, and the second confirms that restartings are adequate. In these lemmas we all make a convention that the uninteresting case $x_{0} = x^{\star}$ is excluded.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Below we present a discrete analog to the restarted scheme. There, $k_{\min}$ is introduced to avoid having consecutive restarts that are too close. To compare the performance of the restarted scheme with the original, we conduct four simulation studies, including both smooth and non-smooth objective functions. Note that the computational costs of the restarted and non-restarted schemes are the same.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Algorithm 1 Speed Restarting Nesterov’s Scheme

<!-- chunk {"id": "body-0084", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Quadratic. ${f{(x)}} = {{\frac{1}{2}x^{T}Ax} + {b^{T}x}}$ is a strongly convex function, in which $A$ is a $500 \times 500$ random positive definite matrix and $b$ a random vector. The eigenvalues of $A$ are between $0.001$ and $1$. The vector $b$ is generated as i.i.d. Gaussian random variables with mean 0 and variance 25.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

where ${n = 50},{{m = 200},{\rho = 20}}$. The matrix $A = {(a_{ij})}$ is a random matrix with i.i.d. standard Gaussian entries, and $b = {(b_{i})}$ has i.i.d. Gaussian entries with mean $0$ and variance $2$. This function is not strongly convex.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Matrix completion. ${f{(X)}} = {{\frac{1}{2}{\|{X_{obs} - M_{obs}}\|}_{F}^{2}} + {\lambda{\| X\|}_{\ast}}}$, in which the ground truth $M$ is a rank-5 random matrix of size $300 \times 300$. The regularization parameter is set to $\lambda = 0.05$. The 5 singular values of $M$ are $1,\ldots,5$. The observed set is independently sampled among the $300 \times 300$ entries so that 10% of the entries are actually observed.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

Lasso in $\ell_{1}$--constrained form with large sparse design. ${{f{(x)}} = {\frac{1}{2}{\|{{Ax} - b}\|}^{2}}}\quad{{\text{s.t.}{\| x\|}_{1}} \leq \delta}$, where $A$ is a $5000 \times 50000$ random sparse matrix with nonzero probability $0.5\%$ for each entry and $b$ is generated as $b = {{Ax^{0}} + z}$. The nonzero entries of $A$ independently follow the Gaussian distribution with mean 0 and variance $0.04$. The signal $x^{0}$ is a vector with 250 nonzeros and $z$ is i.i.d. standard Gaussian noise. The parameter $\delta$ is set to ${\| x^{0}\|}_{1}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

In these examples, $k_{\min}$ is set to be 10 and the step sizes are fixed to be $1/L$. If the objective is in composite form, the Lipschitz bound applies to the smooth part. Figure 6 presents the performance of the speed restarting scheme, the gradient restarting scheme, the original Nesterov's scheme and the proximal gradient method. The objective functions include strongly convex, non-strongly convex and non-smooth functions, violating the assumptions in Theorem 10. Among all the examples, it is interesting to note that both speed restarting scheme empirically exhibit linear convergence by significantly reducing bumps in the objective values. This leaves us an open problem of whether there exists provable linear convergence rate for the gradient restarting scheme as in Theorem 10. It is also worth pointing out that compared with gradient restarting, the speed restarting scheme empirically exhibits more stable linear convergence rate.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion", "weight": 1.5} -->

This paper introduces a second-order ODE and accompanying tools for characterizing Nesterov's accelerated gradient method. This ODE is applied to study variants of Nesterov's scheme and is capable of interpreting some empirically observed phenomena, such as oscillations along the trajectories. Our approach suggests a large family of generalized Nesterov's schemes that are all guaranteed to converge at the rate $O{({1/k^{2}})}$, and a restarting scheme provably achieving a linear convergence rate whenever $f$ is strongly convex.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we often utilize ideas from continuous-time ODEs, and then apply these ideas to discrete schemes. The translation, however, involves parameter tuning and tedious calculations. This is the reason why a general theory mapping properties of ODEs into corresponding properties for discrete updates would be a welcome advance. Indeed, this would allow researchers to only study the simpler and more user-friendly ODEs.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Discussion", "weight": 1.5} -->

As evidenced by many examples, the viewpoint of regarding the ODE as a surrogate for Nesterov's scheme would allow a new perspective for studying accelerated methods in optimization. The discrete scheme and the ODE are closely connected by the exact mapping between the coefficients of momentum (e.g. ${({k - 1})}/{({k + 2})}$) and velocity (e.g. $3/t$). The derivations of generalized Nesterov's schemes and the speed restarting scheme are both motivated by trying a different velocity coefficient, in which the surprising phase transition at 3 is observed. Clearly, such alternatives are endless, and we expect this will lead to findings of many discrete accelerated schemes. In a different direction, a better understanding of the trajectory of the ODEs, such as curvature, has the potential to be helpful in deriving appropriate stopping criteria for termination, and choosing step size by backtracking.
