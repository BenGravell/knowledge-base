<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dissipativity Theory for Nesterov's Accelerated Method

Topics include Semidefinite programming, Lyapunov methods, Control, Lyapunov functions, Ordinary differential equation, Differential equation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we adapt the control theoretic concept of dissipativity theory to provide a natural understanding of Nesterov's accelerated method. Our theory ties rigorous convergence rate analysis to the physically intuitive notion of energy dissipation. Moreover, dissipativity allows one to efficiently construct Lyapunov functions (either numerically or analytically) by solving a small semidefinite program. Using novel supply rate functions, we show how to recover known rate bounds for Nesterov's method and we generalize the approach to certify both linear and sublinear rates in a variety of settings. Finally, we link the continuous-time version of dissipativity to recent works on algorithm analysis that use discretizations of ordinary differential equations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nesterov's accelerated method has garnered interest in the machine learning community because of its fast global convergence rate guarantees. The original convergence rate proofs of Nesterov's accelerated method are derived using the method of estimate sequences, which has proven difficult to interpret. This observation motivated a sequence of recent works on new analysis and interpretations of Nesterov's accelerated method.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many of these recent papers rely on Lyapunov-based stability arguments. Lyapunov theory is an analogue to the principle of minimum energy and brings a physical intuition to convergence behaviors. When applying such proof techniques, one must construct a Lyapunov function, which is a nonnegative function of the algorithm's state (an "internal energy") that decreases along all admissible trajectories. Once a Lyapunov function is found, one can relate the rate of decrease of this internal energy to the rate of convergence of the algorithm. The main challenge in applying Lyapunov's method is finding a suitable Lyapunov function.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are two main approaches for Lyapunov function constructions. The first approach adopts the integral quadratic constraint (IQC) framework from control theory and formulates a linear matrix equality (LMI) whose feasibility implies the linear convergence of the algorithm. Despite the generality of the IQC approach and the small size of the associated LMI, one must typically resort to numerical simulations to solve the LMI. The second approach seeks an ordinary differential equation (ODE) that can be appropriately discretized to yield the algorithm of interest. One can then gain intuition about the trajectories of the algorithm by examining trajectories of the continuous-time ODE. The work of Wilson et al. also establishes a general equivalence between Lyapunov functions and estimate sequence proofs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we bridge the IQC approach and the discretization approach by using dissipativity theory. The term "dissipativity" is borrowed from the notion of energy dissipation in physics and the theory provides a general approach for the intuitive understanding and construction of Lyapunov functions. Dissipativity for quadratic Lyapunov functions in particular has seen widespread use in controls. In the sequel, we tailor dissipativity theory to the automated construction of Lyapunov functions, which are not necessarily quadratic, for the analysis of optimization algorithms. Our dissipation inequality leads to an LMI condition that is simpler than the one in Lessard et al. and hence more amenable to being solved analytically. When specialized to Nesterov's accelerated method, our LMI recovers the Lyapunov function proposed in Wilson et al.. Finally, we extend our LMI-based approach to the sublinear convergence analysis of Nesterov's accelerated method in both discrete and continuous time domains. This complements the original LMI-based approach in Lessard et al., which mainly handles linear convergence rate analyses.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

An LMI-based approach for sublinear rate analysis similar to ours was independently and simultaneously proposed by Fazlyab et al.. While this work and the present work both draw connections to the continuous-time results mentioned above, different algorithms and function classes are emphasized. For example, Fazlyab et al. develops LMIs for gradient descent and proximal/projection-based variants with convex/quasi-convex objective functions. In contrast, the present work develops LMIs tailored to the analysis of discrete-time accelerated methods and Nesterov's method in particular.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Classical Dissipativity Theory", "weight": 1.0} -->

Consider a linear dynamical system governed by the state-space model

<!-- chunk {"id": "body-0009", "role": "body", "section": "Classical Dissipativity Theory", "weight": 1.0} -->

Here, $\xi_{k} \in {\mathbb{R}}^{n_{\xi}}$ is the state, $w_{k} \in {\mathbb{R}}^{n_{w}}$ is the input, $A \in {\mathbb{R}}^{n_{\xi} \times n_{\xi}}$ is the state transition matrix, and $B \in {\mathbb{R}}^{n_{\xi} \times n_{w}}$ is the input matrix. The input $w_{k}$ can be physically interpreted as a driving force. Classical dissipativity theory describes how the internal energy stored in the state $\xi_{k}$ evolves with time $k$ as one applies the input $w_{k}$ to drive the system. A key concept in dissipativity theory is the supply rate, which characterizes the energy change in $\xi_{k}$ due to the driving force $w_{k}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Classical Dissipativity Theory", "weight": 1.0} -->

The supply rate is a function $S:{{{\mathbb{R}}^{n_{\xi}} \times {\mathbb{R}}^{n_{w}}}\rightarrow{\mathbb{R}}}$ that maps any state/input pair $(\xi,w)$ to a scalar measuring the amount of energy delivered from $w$ to state $\xi$. Now we introduce the notion of dissipativity.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Example: Dissipativity for Gradient Descent", "weight": 1.0} -->

There is an intrinsic connection between dissipativity theory and the IQC approach. The IQC analysis of the gradient descent method in Lessard et al. may be reframed using dissipativity theory. Then, the pointwise IQC amounts to using a quadratic supply rate $S$ with $S \leq 0$. Specifically, assume $f$ is $L$-smooth and $m$-strongly convex, and consider the gradient descent method

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example: Dissipativity for Gradient Descent", "weight": 1.0} -->

By co-coercivity, we have ${S{(\xi_{k},w_{k})}} \leq 0$ for all $k$. This just restates Lessard et al.. Then, we can directly apply Theorem 2 to construct the dissipation inequality. We can parameterize $P = {p \otimes I_{p}}$ and define the storage function as ${V{(\xi_{k})}} = {p{\parallel\xi_{k}\parallel}^{2}} = {p{\parallel{x_{k} - x_{\star}}\parallel}^{2}}$. The LMI becomes

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example: Dissipativity for Gradient Descent", "weight": 1.0} -->

The LMI is simple and can be analytically solved to recover the existing rate results for the gradient descent method. For example, we can choose $(\alpha,\rho,p)$ to be $(\frac{1}{L},{1 - \frac{m}{L}},L^{2})$ or $(\frac{2}{L + m},\frac{L - m}{L + m},\frac{1}{2}{(L + m)}^{2}$) to immediately recover the standard rate results in Polyak.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example: Dissipativity for Gradient Descent", "weight": 1.0} -->

Based on the example above, it is evident that choosing a proper supply rate is critical for the construction of a Lyapunov function. The supply rate turns out to be inadequate for the analysis of Nesterov's accelerated method. For Nesterov's accelerated method, the dependence between the internal energy and the driving force is more complicated due to the presence of momentum terms. We will next develop a new supply rate that captures this complicated dependence. We will also make use of this new supply rate to recover the standard linear rate results for Nesterov's accelerated method.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Dissipativity for Nesterov's Method", "weight": 1.0} -->

Nesterov's accelerated method can improve the convergence rate since the input $w_{k}$ depends on both $x_{k}$ and $x_{k - 1}$, and drives the state in a specific direction, i.e. along ${{({1 + \beta})}x_{k}} - {\betax_{k - 1}}$. This leads to a supply rate that extracts energy out of the system significantly faster than with gradient descent. This is formally stated in the next lemma.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dissipativity Theory for More General Methods", "weight": 1.0} -->

We demonstrate the generality of the dissipativity theory on a more general variant of Nesterov's method. Consider a modified accelerated method

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 6", "weight": 1.0} -->

It is noted in Lessard et al. that searching over combinations of multiple IQCs may yield improved rate bounds. The same is true of supply rates. For example, we could include ${\lambda_{1},\lambda_{2}} \geq 0$ as decision variables and search for a dissipation inequality with supply rate ${\lambda_{1}S_{1}} + {\lambda_{2}S_{2}}$ where e.g. $S_{1}$ is and $S_{2}$ is.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dissipativity for Sublinear Rates", "weight": 1.0} -->

The LMI approach in is tailored for the analysis of linear convergence rates for algorithms that are time-invariant (the $A$ and $B$ matrices in do not change with $k$). We now show that dissipativity theory can be used to analyze the sublinear rates $O{({1/k})}$ and $O{({1/k^{2}})}$ via slight modifications of the dissipation inequality.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Dissipativity for $O{({1/k})}$ rates", "weight": 1.0} -->

The $O{({1/k})}$ modification, which we present first, is very similar to the linear rate result.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Dissipativity for $O{({1/k^{2}})}$ rates", "weight": 1.0} -->

Certifying a $O{({1/k})}$ rate for the gradient method required solving a single LMI (25 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")). However, this is not the case for the $O{({1/k^{2}})}$ rate analysis of Nesterov's accelerated method. Nesterov's algorithm has parameters that depend on $k$ so the analysis is more involved. We will begin with the general case and then specialize to Nesterov's algorithm. Consider the dynamical system

<!-- chunk {"id": "body-0021", "role": "body", "section": "Dissipativity for $O{({1/k^{2}})}$ rates", "weight": 1.0} -->

The state matrix $A_{k}$ and input matrix $B_{k}$ change with the time step $k$, and hence (26 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) is referred to as a "linear time-varying" (LTV) system. The analysis of LTV systems typically requires a time-dependent supply rate such as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Dissipativity for $O{({1/k^{2}})}$ rates", "weight": 1.0} -->

for all $k$, then we have ${{V_{k + 1}{(\xi_{k + 1})}} - {V_{k}{(\xi_{k})}}} \leq {S_{k}{(\xi_{k},w_{k})}}$ with the time-dependent storage function defined as ${V_{k}{(\xi_{k})}}{: =}{\xi_{k}^{\mathsf{T}}P_{k}\xi_{k}}$. This is a standard approach for dissipation inequality constructions of LTV systems and can be proved using the same proof technique in Theorem 2. Note that we need (28 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) to simultaneously hold for all $k$. This leads to an infinite number of LMIs in general.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Dissipativity for $O{({1/k^{2}})}$ rates", "weight": 1.0} -->

Now we consider Nesterov's accelerated method for a convex $L$-smooth objective function $f$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Dissipativity for $O{({1/k^{2}})}$ rates", "weight": 1.0} -->

It is known that (29 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) achieves a rate of $O{({1/k^{2}})}$ when $\alpha_{k}{: =}{1/L}$ and $\beta_{k}$ is defined recursively as follows.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Dissipativity for $O{({1/k^{2}})}$ rates", "weight": 1.0} -->

The sequence $\{\zeta_{k}\}$ satisfies ${\zeta_{k}^{2} - \zeta_{k}} = \zeta_{k - 1}^{2}$. We now present a dissipativity theory for the sublinear rate analysis of Nesterov's accelerated method. Rewrite (29 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Dissipativity for $O{({1/k^{2}})}$ rates", "weight": 1.0} -->

Hence, Nesterov's accelerated method (29 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) is in the form of (26 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) with $\xi_{k}{: =}\begin{bmatrix}
{({x_{k} - x_{\star}})}^{\mathsf{T}} & {({x_{k - 1} - x_{\star}})}^{\mathsf{T}}
\end{bmatrix}^{\mathsf{T}}$. The $O{({1/k^{2}})}$ rate analysis of Nesterov's method (29 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) requires the following time-dependent supply rate.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 10", "weight": 1.0} -->

Theorem 9 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method") is quite general. The infinite family of LMIs (34 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) can also be applied for linear rate analysis and collapses down to the single LMI in that case. To apply (34 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) to linear rate analysis, one needs to slightly modify (31 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method"))--(32 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) such that the strong convexity parameter $m$ is incorporated into the formulas of $M_{k},N_{k}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 10", "weight": 1.0} -->

By setting $\mu_{k}{: =}\rho^{- {2k}}$ and $P_{k}{: =}{\rho^{- {2k}}P}$, then the LMI (34 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) is the same for all $k$ and we recover. This illustrates how the infinite number of LMIs (34 rates ‣ 4 Dissipativity for Sublinear Rates ‣ Dissipativity Theory for Nesterov’s Accelerated Method")) can collapse to a single LMI under special circumstances.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Continuous-time Dissipation Inequality", "weight": 1.0} -->

Finally, we briefly discuss dissipativity theory for the continuous-time ODEs used in optimization research. Note that dissipativity theory was first introduced in Willems in the context of continuous-time systems. We denote continuous-time variables in upper case. Consider a continuous-time state-space model

<!-- chunk {"id": "body-0030", "role": "body", "section": "Continuous-time Dissipation Inequality", "weight": 1.0} -->

where $\Lambda{(t)}$ is the state, $W{(t)}$ is the input, and $\overset{˙}{\Lambda}{(t)}$ denotes the time derivative of $\Lambda{(t)}$. In continuous-time, the supply rate is a function $S:{{{\mathbb{R}}^{n_{\Lambda}} \times {\mathbb{R}}^{n_{W}} \times {\mathbb{R}}_{+}}\rightarrow{\mathbb{R}}}$ that assigns a scalar to each possible state and input pair. Here, we allow $S$ to also depend on time $t \in {\mathbb{R}}_{+}$. To simplify our exposition, we will omit the explicit time dependence $(t)$ from our notation.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 13", "weight": 1.0} -->

As in the discrete-time case, the infinite family of LMIs can also be reduced to a single LMI for the linear rate analysis of continuous-time ODEs. For further discussion on the topic of continuous-time exponential dissipation inequalities, see Hu & Seiler.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we developed new notions of dissipativity theory for understanding of Nesterov's accelerated method. Our approach enjoys advantages of both the IQC framework and the discretization approach in the sense that our proposed LMI condition is simple enough for analytical rate analysis of Nesterov's method and can also be easily generalized to more complicated algorithms. Our approach also gives an intuitive interpretation of the convergence behavior of Nesterov's method using an energy dissipation perspective.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

One potential application of our dissipativity theory is for the design of accelerated methods that are robust to gradient noise. This is similar to the algorithm design work in Lessard et al.. However, compared with the IQC approach in Lessard et al., our dissipativity theory leads to smaller LMIs. This can be beneficial since smaller LMIs are generally easier to solve analytically. In addition, the IQC approach in Lessard et al. is only applicable to strongly-convex objective functions while our dissipativity theory may facilitate the design of robust algorithm for weakly-convex objective functions. The dissipativity framework may also lead to the design of adaptive or time-varying algorithms.
