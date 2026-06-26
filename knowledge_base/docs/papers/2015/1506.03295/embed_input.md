<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Computational Complexity versus Statistical Performance on Sparse Recovery Problems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that several classical quantities controlling compressed sensing performance directly match classical parameters controlling algorithmic complexity. We first describe linearly convergent restart schemes on first-order methods solving a broad range of compressed sensing problems, where sharpness at the optimum controls convergence speed. We show that for sparse recovery problems, this sharpness can be written as a condition number, given by the ratio between true signal sparsity and the largest signal size that can be recovered by the observation matrix. In a similar vein, Renegar's condition number is a data-driven complexity measure for convex programs, generalizing classical condition numbers for linear systems. We show that for a broad class of compressed sensing problems, the worst case value of this algorithmic complexity measure taken over all signals matches the restricted singular value of the observation matrix which controls robust recovery performance. Overall, this means in both cases that, in compressed sensing problems, a single parameter directly controls both computational complexity and recovery performance. Numerical experiments illustrate these points using several classical algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sparse recovery problems have received a lot of attention from various perspectives. On one side, an extensive literature explores the limits of recovery performance. On the other side, a long list of algorithms now solve these problems very efficiently. Early, it was noticed empirically by e.g. Donoho and Tsaig, that recovery problems which are easier to solve from a statistical point of view (i.e., where more samples are available), are also easier to solve numerically. Here, we show that these two aspects are indeed intimately related.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recovery problems consist in retrieving a signal $x^{\ast}$, lying in some Euclidean space $E$, given linear observations. If the signal is "sparse", namely if it can be efficiently compressed, a common approach is to minimize the corresponding sparsity inducing norm $\parallel \cdot \parallel$ (e.g. the $\ell_{1}$ norm in classical sparse recovery). The exact sparse recovery problem then reads in the variable $x \in E$, where $A$ is a linear operator on $E$ and $b = {A{(x^{\ast})}}$ is the vector of observations. If the observations are affected by noise a robust version of this problem is written as in the variable $x \in E$, where $\parallel \cdot \parallel_{2}$ is the Euclidean norm and $\epsilon > 0$ is a tolerance to noise. In penalized form, this is in the variable $x \in E$ where $\lambda > 0$ is a penalization parameter.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This last problem is known as the LASSO \Tibshirani, in the $\ell_{1}$ case.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

When $x^{\ast}$ has no more than $s$ non zero values, Donoho and Tanner and Candès and Tao have shown that, for certain linear operators $A$, $O{({s{\log p}})}$ observations suffice for stable recovery of $x^{\ast}$ by solving the exact formulation using the $\ell_{1}$ norm (a linear program), where $p$ is the dimension of the space $E$. These results have then been generalized to many other recovery problems with various assumptions on signal structure (e.g., where $x$ is a block-sparse vector, a low-rank matrix, etc.) and corresponding convex relaxations were developed in those cases (see e.g. Chandrasekaran et al. and references therein). Recovery performance is often measured in terms of the number of samples required to guarantee exact or robust recovery given a level of noise.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the computational side, many algorithms were developed to solve these problems at scale. Besides specialized methods such as LARS \Efron et al. FISTA \Beck and Teboulle, and NESTA \Becker, Bobin and Candès solvers use accelerated gradient methods to solve robust recovery problems, with efficient and flexible implementations covering a wide range of compressed sensing instances developed by e.g. Becker, Candès and Grant. Recently, linear convergence results have been obtained for the LASSO \Agarwal et al., [2011; Yen et al., 2014; Zhou et al., 2015\] using variants of the classical strong convexity assumption, while \Zhou and So, studied error bounds for a much broader class of structured optimization problems including sparse recovery and matrix completion. Some restart schemes have also been developed in e.g. \O'Donoghue and Candes, [2015; Su et al., 2014; Giselsson and Boyd, 2014\] while Fercoq and Qu showed that generic restart schemes can offer linear convergence given a rough estimate of the behavior of the function around its minimizers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As mentioned above, Donoho and Tsaig was one of the first reference to connect statistical and computational performance in this case, showing empirically that recovery problems which are easier to solve from a statistical point of view (i.e., where more samples are available), are also easier to solve numerically (using homotopy methods). More recently, Chandrasekaran and Jordan; Amelunxen et al. studied computational and statistical tradeoffs for increasingly tight convex relaxations of shrinkage estimators. They show that recovery performance is directly linked to the Gaussian squared-complexity of the tangent cone with respect to the constraint set and study the complexity of several convex relaxations. In \Chandrasekaran and Jordan, [2013; Amelunxen et al., 2014\] however, the structure of the convex relaxation is varying and affecting both complexity and recovery performance, while in \Donoho and Tsaig, and in what follows, the structure of the relaxation is fixed, but the data (i.e. the observation matrix $A$) varies.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, as a first step, we study the exact recovery case and show that the null space property introduced by Cohen et al. can be seen as a measure of sharpness on the optimum of the sparse recovery problem. On one hand this allows us to develop linearly convergent restart schemes whose rate depends on this sharpness. On the other hand we recall how the null space property is linked to the recovery threshold of the sensing operator $A$ for random designs, thus producing a clear link between statistical and computational performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then analyze the underlying conic geometry of recovery problems. Robust recovery performance is controlled by a minimal conically restricted singular value. We recall Renegar's condition number and show how it affects the computational complexity of optimality certificates for exact recovery and the linear convergence rate of restart schemes. By observing that the minimal conically restricted singular value matches the worst case value of Renegar's condition number on sparse signals, we provide further evidence that a single quantity controls both computational and statistical aspects of recovery problems. Numerical experiments illustrate its impact on various classical algorithms for sparse recovery.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first two sections focus on the $\ell_{1}$ case for simplicity. We generalize our results to non-overlapping group norms and the nuclear norm in a third section.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Notations", "weight": 1.0} -->

For a given integer $p \geq 1$, $⟦1,p⟧$ denotes the set of integers between $1$ and $p$. For a given subset $S \subset {⟦1,p⟧}$, we denote $S^{c} = {{⟦1,p⟧} \smallsetminus S}$ its complementary and $\operatorname{\mathbf{C}\mathbf{a}\mathbf{r}\mathbf{d}}{(S)}$ its cardinality.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Notations", "weight": 1.0} -->

For a given linear operator or matrix $A$, we denote ${Null}{(A)}$ its null space, ${Im}{(A)}$ its range, and ${\| X\|}_{2}$ its operator norm with respect to the Euclidean norm (for matrices this is the spectral norm). The identity operator is denoted $\mathbf{I}$. In a linear topological space $E$ we denote $\operatorname{\mathbf{i}\mathbf{n}\mathbf{t}}{(F)}$ the interior of $F \subset E$. Finally for a given real $a$, we denote $\lceil a\rceil$ the smallest integer larger than or equal to $a$ and $\lfloor a\rfloor$ the largest integer smaller than or equal to $a$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sharpness, Restart and Sparse Recovery Performance", "weight": 1.0} -->

In this section and the following one, we discuss sparse recovery problems using the $\ell_{1}$ norm. Given a matrix $A \in {\mathbb{R}}^{n \times p}$ and observations $b = {Ax^{\ast}}$ on a signal $x^{\ast} \in {\mathbb{R}}^{p}$, recovery is performed by solving the $\ell_{1}$ minimization program in the variable $x \in {\mathbb{R}}^{p}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sharpness, Restart and Sparse Recovery Performance", "weight": 1.0} -->

In what follows, we show that the Null Space Property condition (recalled below) can be seen as measure of sharpness for $\ell_{1}$-recovery of a sparse signal $x^{\ast}$, with for any $x \neq x^{\ast}$ such that ${Ax} = b$, and some $0 \leq \gamma < 1$. This first ensures that $x^{\ast}$ is the unique minimizer of problem ($\ell_{1}$ recovery) but also has important computational implications. It allows us to produce linear convergent restart schemes whose rates depend on sharpness. By connecting null space property to recovery threshold for random observation matrices, we thus get a direct link between computational and statistical aspects of sparse recovery problems.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Null space property & sharpness for exact recovery", "weight": 1.0} -->

Although the definition of null space property appeared in earlier work \Donoho and Huo, [2001; Feuer and Nemirovski, 2003\] the terminology of restricted null space is due to Cohen et al.. The following definition differs slightly from the original one in order to relate it to intrinsic geometric properties of the problem in Section 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Restarting first-order methods", "weight": 1.0} -->

In this section, we seek to solve the recovery problem ($\ell_{1}$ recovery) and exploit the sharpness bound (Sharp). The NESTA algorithm \Becker, Bobin and Candès, uses the smoothing argument of Nesterov to solve ($\ell_{1}$ recovery). In practice, this means using the optimal algorithm of Nesterov to minimize for some $\epsilon > 0$, which approximates the $\ell_{1}$ norm uniformly up to $\epsilon/2$. This is the classical Huber function, which has a Lipschitz continuous gradient with constant equal to $p/\epsilon$. Overall given an accuracy $\epsilon$ and a starting point $x_{0}$ this method outputs after $t$ iterations a point $x = {\mathcal{A}{(x_{0},\epsilon,t)}}$ such that for any $\hat{x}$ solution of problem ($\ell_{1}$ recovery).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Restarting first-order methods", "weight": 1.0} -->

Now if the sharpness bound is satisfied, restarting this method, as described in the (Restart) scheme presented below, accelerates its convergence.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Restarting first-order methods", "weight": 1.0} -->

Initial point y0 ∈ ℝp, initial gap ϵ0 ≥ ∥y0∥1 − ∥x̂∥1, decreasing factor ρ, restart clock t A point ŷ = yK approximately solving (ℓ1 recovery). Algorithm 1 Restart Scheme (Restart)

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal restart scheme", "weight": 1.0} -->

We begin by analyzing an optimal restart scheme assuming the sharpness constant is known. We use a non-integer clock to highlight its dependency to the sharpness. Naturally clock and number of restarts must be integer but this does not affect much bounds as detailed in Appendix A. The next proposition shows that algorithm $\mathcal{A}$ needs a constant number of iterations to decrease the gap by a constant factor, which means restart leads to linear convergence.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Practical restart scheme", "weight": 1.0} -->

Several parameters are needed to run the optimal scheme above. The optimal decreasing factor is independent of the data. The initial gap $\epsilon_{0}$ can be taken as ${\| y_{0}\|}_{1}$ for ${Ay_{0}} = b$. The sharpness constant $\gamma$ is for its part mostly unknown such that we cannot choose the number $t^{\ast}$ of inner iterations a priori. However, given a budget of iterations $N$ (the total number of iterations in the optimization algorithm, across restarts), a log scale grid search can be performed on the optimal restart clock to get nearly optimal rates as detailed in the following corollary (contrary to the general results in \Roulet and d'Aspremont the sharpness exponent $\nu$ in is equal to one here, simplifying the parameter search).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Recovery threshold", "weight": 1.0} -->

If (NSP) is satisfied at a given order $s$ it holds also for any $s' \leq s$. However, the constant, and therefore the speed of convergence, may change. Here we show that this constant actually depends on the ratio between the maximal order at which $A$ satisfies (NSP) and the sparsity of the signal that we seek to recover.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Recovery threshold", "weight": 1.0} -->

To this end, we give a more concrete geometric meaning to the constant $\alpha$ in (NSP), connecting it with the diameter of a section of the $\ell_{1}$ ball by the null space of the matrix $A$ (see e.g. Kashin and Temlyakov for more details).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Renegar's condition number and restricted singular values", "weight": 1.0} -->

We first gave concrete evidence of the link between optimization complexity and recovery performance for the exact recovery problem by highlighting sharpness properties of the objective around the true signal, given by the null space condition. We now take a step back and consider results on the underlying conic geometry of recovery problems that also control both computational and statistical aspects.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Renegar's condition number and restricted singular values", "weight": 1.0} -->

On the statistical side, minimal conically restricted singular values are known to control recovery performance in robust recovery problems. On the computational side, Renegar's condition number, a well known computational complexity measure for conic convex programs, controls the cost of obtaining optimality certificates for exact recovery and the sharpness of exact recovery problems (hence computational complexity of the (Restart) scheme presented in the previous section). Numerical experiments will then illustrate its relevance to control numerous other classical algorithms. By observing that minimal conically restricted singular values match the worst case of Renegar's condition number on sparse signals, our analysis shows once more that one single geometrical quantity controls both statistical robustness and computational complexity of recovery problems.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conic linear systems", "weight": 1.0} -->

Conic linear systems arise naturally from optimality conditions of the exact recovery problem. To see this, define the tangent cone at point $x$ with respect to the $\ell_{1}$ norm, that is, the set of descent directions for $\parallel \cdot \parallel_{1}$ at $x$, as As shown for example by \Chandrasekaran et al., [2012, Prop 2.1\] a point $x$ is then the unique optimum of the exact recovery problem ($\ell_{1}$ recovery) if and only if ${{{Null}{(A)}} \cap {\mathcal{T}{(x)}}} = {\{ 0\}}$, that is, there is no point satisfying the linear constraints that has lower $\ell_{1}$ norm than $x$. Correct recovery of an original signal $x^{\ast}$ is therefore certified by the infeasibility of a conic linear system of the form where $C$ is a closed cone and $A$ a given matrix.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conic linear systems", "weight": 1.0} -->

For both computational and statistical aspects we will be interested in the distance to feasibility. On the computational side this will give a distance to ill-posedness that plays the role of a condition number. On the statistical side it will measure the amount of perturbation that the recovery can handle.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Recovery performance of robust recovery", "weight": 1.0} -->

Several quantities control the stability of sparse recovery in a noisy setting, with e.g. \Candes et al., using restricted isometry constants, and \Kashin and Temlyakov, [2007; Juditsky and Nemirovski, 2011\] using diameters with respect to various norms. In this vein, the previous section showed that recovery of a signal $x^{\ast}$ is ensured by infeasiblity of the conic linear system (P~A,$\mathcal{T}{(x^{\ast})}$~), i.e. positiveness of the minimal conically restricted singular value $\sigma_{\mathcal{T}{(x^{\ast})}}{(A)}$. We now show how this quantity also controls recovery performance in the presence of noise.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Recovery performance of robust recovery", "weight": 1.0} -->

In that case, the robust recovery problem attempts to retrieve an original signal $x^{\ast}$ by solving in the variable $x \in {\mathbb{R}}^{p}$, with the same design matrix $A \in {\mathbb{R}}^{n \times p}$, where $b \in {\mathbb{R}}^{n}$ are given observations perturbed by noise of level $\delta > 0$. The following classical result then bounds reconstruction error in terms of $\sigma_{\mathcal{T}{(x^{\ast})}}{(A)}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Computational complexity of recovery problems", "weight": 1.0} -->

Computational complexity for convex optimization problems is often described in terms of polynomial functions of problem size. This produces a clear link between problem structure and computational complexity but fails to account for the nature of the data. If we use linear systems as a basic example, unstructured linear systems of dimension $n$ can be solved with complexity $O{(n^{3})}$ regardless of the matrix values, but iterative solvers will converge much faster on systems that are better conditioned. The seminal work of Renegar \[1995b, 2001\] extends this notion of conditioning to optimization problems, producing data-driven bounds on the complexity of solving conic programs, and showing that the number of outer iterations of interior point algorithms increases as the distance to ill-posedness decreases.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Renegar's condition number", "weight": 1.0} -->

Renegar's condition number \Renegar, [1995b, a; Peña, 2000\] provides a data-driven measure of the complexity of certifying infeasibility of a conic linear system of the form presented in (P~A,C~) (the larger the condition number, the harder the problem). It is rooted in the sensible idea that certifying infeasibility is easier if the problem is far from being feasible. It is defined as the scale invariant reciprocal of the distance to feasibility $\sigma_{C}{(A)}$, defined in (37. ‣ 2.1. Conic linear systems ‣ 2. Renegar’s condition number and restricted singular values ‣ Computational Complexity versus Statistical Performance on Sparse Recovery Problems")), of problem (P~A,C~), i.e.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Renegar's condition number", "weight": 1.0} -->

Notice that, if $C$ were the whole space ${\mathbb{R}}^{p}$, and if $A^{T}A$ were full-rank (never the case if $n < p$), then $\sigma_{C}{(A)}$ would be the smallest singular value of $A$. As a result, $\mathcal{R}_{C}{(A)}$ would reduce to the classical condition number of $A$ (and to $\infty$ when $A^{T}A$ is rank-deficient). Renegar's condition number is necessarily smaller (better) than the latter, as it further incorporates the notion that $A$ need only be well conditioned along those directions that matter with respect to $C$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Complexity of certifying optimality", "weight": 1.0} -->

In a first step, we study the complexity of the oracle certifying optimality of a candidate solution $x$ to ($\ell_{1}$ recovery) as a proxy for the problem of computing an optimal solution to this problem. As mentioned in Section 2.1, optimality of a point $x$ is equivalent to infeasibility of where the tangent cone $\mathcal{T}{(x)}$ is defined. By a theorem of alternative, infeasibility of (P~A,$\mathcal{T}(x)$~) is equivalent to feasibility of the dual problem where $\mathcal{T}{(x)}^{\circ}$ is the polar cone of $\mathcal{T}{(x)}$. Therefore, to certify infeasibility of (P~A,$\mathcal{T}(x)$~) it is sufficient to exhibit a solution for the dual problem (D~A,$\mathcal{T}(x)$~).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Complexity of certifying optimality", "weight": 1.0} -->

Several references have connected Renegar's condition number and the complexity of solving such conic linear systems using various algorithms \Renegar, [1995b; Freund and Vera, 1999a; Epelman and Freund, 2000; Renegar, 2001; Vera et al., 2007; Belloni et al., 2009\]. In particular, Vera et al. linked it to the complexity of solving the primal dual pair (P~A,$\mathcal{T}(x)$~)--(D~A,$\mathcal{T}(x)$~) using a barrier method. They show that the number of outer barrier method iterations grows as where $\rho$ is the barrier parameter, while the conditioning (hence the complexity) of the linear systems arising at each interior point iteration is controlled by $\mathcal{R}_{\mathcal{T}{(x)}}{(A)}^{2}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Complexity of certifying optimality", "weight": 1.0} -->

This link was also tested empirically on linear programs using the NETLIB library of problems by Ordóñez and Freund, where computing times and number of iterations were regressed against estimates of the condition number computed using the approximations for Renegar's condition number detailed by Freund and Vera.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Complexity of certifying optimality", "weight": 1.0} -->

Studying the complexity of computing an optimality certificate gives insights on the performance of oracle based optimization techniques such as the ellipsoid method. We now show how Renegar's condition also controls the number steps in the (Restart) scheme presented in Section 1.2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Complexity of restart scheme with Renegar's condition number", "weight": 1.0} -->

Convergence of the (Restart) scheme presented in Section 1.2 is controlled by the sharpness of the problem deduced from (NSP). We now observe that sharpness is controlled by the worst case Renegar condition number for the optimality certificates (P~A,$\mathcal{T}(x)$~) on all $s$-sparse signals, defined as Connecting Lemmas 2.3, 2.5 and Proposition 1.4 we get the following corollary.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Computational complexity for inexact recovery", "weight": 1.0} -->

When the primal problem (P~A,$\mathcal{T}(x)$~) is feasible, so that ${\sigma_{\mathcal{T}{(x)}}{(A)}} = 0$, Renegar's condition number as defined here is infinite. While this correctly captures the fact that, in that regime, statistical recovery does not hold, it does not properly capture the fact that, when (P~A,$\mathcal{T}(x)$~) is "comfortably" feasible, certifying so is easy, and algorithms terminate quickly (although they return a useless estimator). From both a statistical and a computational point of view, the truly delicate cases correspond to problem instances for which both (P~A,$\mathcal{T}(x)$~) and (D~A,$\mathcal{T}(x)$~) are only barely feasible or infeasible.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Computational complexity for inexact recovery", "weight": 1.0} -->

This is illustrated in simple numerical example by \Boyd and Vandenberghe, [2004, §11.4.3\] and in our numerical experiments, corresponding to the peaks in the CPU time plots of the right column in Figure 4: problems where sparse recovery barely holds/fails are relatively harder. For simplicity, we only focused here on distance to feasibility for problem (P~A,$\mathcal{T}(x)$~). However, it is possible to symmetrize the condition numbers used here as described by \Amelunxen and Lotz, [2014, §1.3\], where a symmetric version of the condition number is defined as where $\sigma_{\mathcal{T}{(x)}}^{P}{(A)}$ and $\sigma_{\mathcal{T}{(x)}}^{D}{(A)}$ denote the distance to feasibility of respectively (P~A,$\mathcal{T}(x)$~) and (D~A,$\mathcal{T}(x)$~).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Computational complexity for inexact recovery", "weight": 1.0} -->

This quantity peaks for programs that are nearly feasible/infeasible.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Computational complexity for inexact recovery", "weight": 1.0} -->

As we noticed in Section 1.2, a Łojasiewicz inequality for the ($\ell_{1}$ recovery) problem is sufficient to ensure linear convergence of the restart scheme. Connecting the symmetrized Renegar condition number to the Łojasiewicz inequality constant $\gamma$ may then produce complexity bounds for the restart scheme beyond the recovery case. Łojasievicz inequalities for convex programs have indeed proven their relevance. They were used by Fercoq and Qu; Roulet and d'Aspremont to accelerate classical methods, in particular on the LASSO problem. Lower computational bounds for the computational complexity of accelerated methods on convex optimization problems satisfying sharpness assumptions were also studied by \Nemirovskii and Nesterov, [1985, Page 6\]. Although the Łojasievicz inequality is proven to be satisfied by a broad class of functions \Bolte et al. quantifying its parameters is still a challenging problem that would enable better parameter choices for appropriate algorithms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Other algorithms", "weight": 1.0} -->

The restart scheme presented in Section 1.2 is of course not the only one to solve problem ($\ell_{1}$ recovery) in practice and it has not been analyzed in the noisy case. However, we will observe in the numerical experiments of Section 4 that the condition number is correlated with the empirical performance of efficient recovery algorithms such as LARS \Efron et al., and Homotopy \Donoho and Tsaig, [2008; Asif and Romberg, 2014\]. On paper, the computational complexities of ($\ell_{1}$ recovery) and (Robust $\ell_{1}$ recovery) are very similar (in fact, infeasible start primal-dual algorithms designed for solving ($\ell_{1}$ recovery) actually solve problem (Robust $\ell_{1}$ recovery) with $\delta$ small). However in our experiments, we did observe sometimes significant differences in behavior between the noisy and noiseless case.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Generalization to Common Sparsity Inducing Norms", "weight": 1.0} -->

In this section we generalize previous results to sparse recovery problems in (non-overlapping) group norms or nuclear norm. Group norms arise in contexts such as genomics to enforce the selection of groups of genes (e.g., Obozinski et al. and references therein.) The nuclear norm is used for low-rank estimation (e.g., Recht et al. and references therein.) We use the framework of decomposable norms introduced by Negahban et al. which applies to these norms. This allows us to generalize the null space property and to derive corresponding sharpness bounds for the exact recovery problem in a broader framework. We then again relate recovery performance and computational complexity of these recovery problems.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Decomposable norms", "weight": 1.0} -->

Sparsity inducing norms have been explored from various perspectives. Here, we use the framework of decomposable norms by Negahban et al. to generalize our results from $\ell_{1}$ norms to non-overlapping group norms and nuclear norms in a concise form. We then discuss the key geometrical properties of these norms and potential characterization of their conic nature.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Decomposable norms", "weight": 1.0} -->

We first recall the definition of decomposable norms by Negahban et al. in terms of projectors.

<!-- chunk {"id": "body-0046", "role": "body", "section": "$\\ell_{1}$ norm", "weight": 1.0} -->

In the the $\ell_{1}$ norm case, $E = {\mathbb{R}}^{p}$ and $\mathcal{P}$ is the set of projectors on coordinate subspaces of ${\mathbb{R}}^{p}$, that is, $\mathcal{P}$ contains all projectors which zero out all coordinates of a vector except for a subset of them, which are left unaffected. The maps $\overline{P}$ are the complementary projectors: $\overline{P} = {\mathbf{I} - P}$. Property (ii) ‣ Definition 3.1. ‣ 3.1. Decomposable norms ‣ 3. Generalization to Common Sparsity Inducing Norms ‣ Computational Complexity versus Statistical Performance on Sparse Recovery Problems") is the classical decomposability of the $\ell_{1}$ norm.

<!-- chunk {"id": "body-0047", "role": "body", "section": "$\\ell_{1}$ norm", "weight": 1.0} -->

Naturally, the complexity level corresponds to the number of coordinates preserved by $P$, i.e., ${\nu{(P)}} = {\operatorname{\mathbf{R}\mathbf{a}\mathbf{n}\mathbf{k}}{(P)}}$. These definitions recover the usual notion of sparsity.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Group norms", "weight": 1.0} -->

Given a partition $G$ of $⟦1,p⟧$ in (non-overlapping) groups $g \subset {⟦1,p⟧}$, the group norm is defined for $x \in {\mathbb{R}}^{p}$ as where ${\| x_{g}\|}_{r}$ is the $\ell_{r}$-norm of the projection of $x$ onto the coordinates defined by $g$. The cases $r = {2,\infty}$ correspond respectively to $\ell_{1}/\ell_{2}$ and $\ell_{1}/\ell_{\infty}$ block norms. Here, $E = {\mathbb{R}}^{p}$ and the family $\mathcal{P}$ is composed of orthogonal projectors onto coordinates defined by (disjoint) unions of groups $g$, and $\overline{P} = {\mathbf{I} - P}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Group norms", "weight": 1.0} -->

Formally, to each $P$ we associate $F \subset G$ such that for any $x \in E$, ${({Px})}_{g} = x_{g}$ if $g \in F$ and ${({Px})}_{g} = 0$ otherwise. Decomposability (ii) ‣ Definition 3.1. ‣ 3.1. Decomposable norms ‣ 3. Generalization to Common Sparsity Inducing Norms ‣ Computational Complexity versus Statistical Performance on Sparse Recovery Problems") then clearly holds. To each group $g$ we associate a weight $\eta_{g}$ and for a projector $P \in \mathcal{P}$ with associated $F \subset G$, ${\eta{(P)}} = {\sum_{g \in F}\eta_{g}}$. A classical choice of weights is $\eta_{g} = 1$ for all $g \in G$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Nuclear norm", "weight": 1.0} -->

The nuclear norm is defined for matrices $X \in {\mathbb{R}}^{p \times q}$ with singular values $\sigma_{i}{(X)}$ as Here $E = {\mathbb{R}}^{p \times q}$ and its associated family of projectors contains $P$ such that where $P_{left} \in {\mathbb{R}}^{p \times p}$ and $P_{right} \in {\mathbb{R}}^{q \times q}$ are orthogonal projectors.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Nuclear norm", "weight": 1.0} -->

Their weights are defined as ${\eta{(P)}} = {\max\left({\operatorname{\mathbf{R}\mathbf{a}\mathbf{n}\mathbf{k}}{(P_{left})}},{\operatorname{\mathbf{R}\mathbf{a}\mathbf{n}\mathbf{k}}{(P_{right})}} \right)}$ defining therefore $s$-sparse matrices as matrices of rank at most $s$. As $P$ and $\overline{P}$ project on orthogonal row and column spaces, condition (ii) ‣ Definition 3.1. ‣ 3.1. Decomposable norms ‣ 3. Generalization to Common Sparsity Inducing Norms ‣ Computational Complexity versus Statistical Performance on Sparse Recovery Problems") holds.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Nuclear norm", "weight": 1.0} -->

Decomposable norms offer a unified nomenclature for the study of sparsity inducing norms. However, they appear to be essentially restricted to the three examples presented above. Moreover, it is not clear if their definition is sufficient to characterize the conic nature of these norms, in particular in the nuclear norm case that will require additional linear algebra results. In comparison, the framework proposed by Juditsky et al. can encompass *non-latent* overlapping groups. For future use, we simplify the third property of their definition \Juditsky et al., [2014, Section 2.1\] in Appendix B. It is not clear how this view can be used for latent overlapping group norms presented by Obozinski et al. applied in biology. Moreover the sufficient conditions that Juditsky et al. present are sufficient but not necessary in the nuclear norm case. Better characterizing the key geometrical properties of these norms is therefore a challenging research direction.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sharpness and generalized null space property", "weight": 1.0} -->

From now, we assume that we are given an ambient Euclidean space $E$ with one of the three decomposable norms $\parallel. \parallel$ presented in previous section, i.e. $\ell_{1}$, group or nuclear norm, and the associated family of orthogonal projectors $\mathcal{P}$ as introduced in Definition 3.1. We study the sparse recovery problem in the variable $x \in E$, where $A$ is a linear operator onto ${\mathbb{R}}^{n}$ and the observations $b \in {\mathbb{R}}^{n}$ are taken from an original point $x^{\ast}$ such that $b = {A{(x^{\ast})}}$. We begin by generalizing the null space property in this setting.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Robust recovery performance and computational complexity", "weight": 1.0} -->

In this section, for a Euclidean space $E$ and $x \in E$ we denote ${\| x\|}_{2}$ the $\ell_{2}$ norm of its coefficients, if $E$ is a matrix space ${\| x\|}_{2}$ is then the Frobenius norm of $x$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Generalized cone restricted singular value", "weight": 1.0} -->

We begin by addressing the recovery performance of robust sparse recovery problems that reads in the variable $x \in E$, with the same linear operator $A$, where the observations $b \in {\mathbb{R}}^{n}$ are affected by noise of level $\delta > 0$. For a linear operator $A$ from $E$ to ${\mathbb{R}}^{n}$, we denote its operator norm with respect to $\parallel \cdot \parallel$, ${\| A\|}_{2} = {\sup_{{x \in E}:{{\| x\|}_{2} \leq 1}}{\|{A{(x)}}\|}_{2}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Generalized cone restricted singular value", "weight": 1.0} -->

The results of Section 2.2 transpose directly to the general case by replacing $\parallel \cdot \parallel_{1}$ by $\parallel \cdot \parallel$. Precisely, assuming that $b = {{Ax^{\ast}} + w}$ where ${\| w\|}_{2} \leq {\delta{\| A\|}_{2}}$, an optimal solution $\hat{x}$ of problem (Robust sparse recovery) satisfies the error bound where the tangent cone is defined as and robust recovery of $s$-sparse signals is therefore controlled by The key point is then to characterize the tangent cones of $s$-sparse signals. First, this will allow statistical estimations of $\mu_{s}{(A)}$. Second, it will enable us to estimate the constant (GNSP), hence sharpness of the exact recovery problem and computational complexity of associated restart schemes. This is the aim of the following lemma.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Renegar's condition number", "weight": 1.0} -->

On the computational side, denote $\mathcal{R}_{\mathcal{T}{(x)}}{(A)}$ the Renegar condition number of the conic linear system and the worst-case Renegar condition number on $s$-sparse signals First, Renegar's condition number plays the same role as before in computing optimality certificates for the exact recovery problems. Then, combining Lemma 3.5 and Proposition 3.3 shows that the sharpness bound for exact recovery reads This sharpness will then control linearly convergent restart schemes for the exact recovery problem.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Renegar's condition number", "weight": 1.0} -->

Overall then, as established earlier in this paper, a single geometric quantity---namely, the minimal cone restricted singular value---appears to control both computational and statistical aspects. We now illustrate this statement on numerical experiments.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

In this section, we first test the empirical performance of restart schemes and its link with recovery performance. We then perform similar experiments on Renegar's condition number.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Sharpness & restart for exact recovery", "weight": 1.0} -->

We test the (Restart) scheme on $\ell_{1}$-recovery problems with random design matrices. Throughout the experiments, we use the NESTA code described in \Becker, Bobin and Candès, as the subroutine in the restart strategy. We generate a random design matrix $A \in {\mathbb{R}}^{n \times p}$ with i.i.d. Gaussian coefficients. We then normalize $A$ so that ${AA^{T}} = \mathbf{I}$ (to fit NESTA's format) and generate observations $b = {Ax^{\ast}}$ where $x^{\ast} \in {\mathbb{R}}^{p}$ is an $s$-sparse vector whose nonzero coefficients are all ones.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Restart scheme performance", "weight": 1.0} -->

First we compare in Figure 1 the practical scheme presented in Section 1.2.2 with a plain implementation of NESTA without restart or continuation steps. Dimensions of the problem are $p = 300$, $n = 200$ and $s = 10$. Starting from $x_{0} = {A^{T}b}$, we use $\epsilon_{0} = {\| x_{0}\|}_{1}$ as a first initial guess on the gap and perform a grid search of step size $h = 4$ for a budget of $N = 500$ iterations. The first and last schemes of the grid search were not run as they are unlikely to produce a nearly optimal restart scheme. The grid search can be parallelized and the best scheme found is plotted with a solid red line. The dashed red line represents the convergence rate accounting for the cost of the grid search. For the plain implementation of NESTA, we used different target precisions. These control indeed the smoothness of the surrogate function $f_{\epsilon}$ which itself controls the step size of Nesterov's algorithm. Therefore a high precision slows down the algorithm.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Restart scheme performance", "weight": 1.0} -->

However for low precision NESTA can be faster but will not approximate well the original signal. Also, the theoretical bound might be very pessimistic, as the surrogate function $f_{\epsilon}$ may approximate the $\ell_{1}$ norm for the points of interest at a much better accuracy than $\epsilon$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Restart scheme performance", "weight": 1.0} -->

\psfrag{fmu}[b][t]{f(xt) − f*}\psfrag{k}[t][b]{Inner iterations}\includegraphics[width=216.81pt]{figures/VRResVsNest.eps} Figure 1. Best restarted NESTA (solid red line) and overall cost of the practical restart schemes (dashed red line) versus plain NESTA implementation with low accuracy ϵ = 10−1 (dotted black line) and higher accuracy ϵ = 10−3 (dash-dotted black line) for a budget of 500 iterations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Restart scheme performance", "weight": 1.0} -->

Overall, we observe a clear linear convergence of the restart scheme that outperforms the plain implementation. This was already observed by Becker, Bobin and Candès who developed their continuation steps against which we compare in Figure 2. We used default options for NESTA, namely 5 continuation steps with a stopping criterion based on the relative objective change in the surrogate function (specifically, the algorithm stops when these changes are lower than the target accuracy, set to $10^{- 6}$). We compare continuations steps and best restart found by grid search for different dimensions of the problem, we fix $p = 300$, $s = 10$ and vary the number of samples $n = {\{ 120,200\}}$. Continuation steps converge faster with better conditioned problems, i.e., more samples. Overall the heuristic of continuation steps offer similar or better linear convergence than the restart scheme found by grid-search. Notice that a lot of parameters are involved for both algorithms, in particular the target precision may play an important role, so that more extensive experiments may be needed to refine these statements.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Restart scheme performance", "weight": 1.0} -->

Our goal here is to provide a simple but strong baseline with theoretical guarantees for recovery. Improving on it, as Fercoq and Qu did for LASSO, is an appealing research direction. Sharpness may be used for example to refine the heuristic strategy of the continuations steps.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Restart scheme performance", "weight": 1.0} -->

\psfrag{fmu}[b][t]{f(xt) − f*}\psfrag{k}[t][b]{Inner iterations}\includegraphics[width=195.12767pt]{figures/VRResVsNESTA_n120.eps} \psfrag{fmu}[b][t]{f(xt) − f*}\psfrag{k}[t][b]{Inner iterations}\includegraphics[width=195.12767pt]{figures/VRResVsNESTA_n200.eps} Figure 2. Best restarted NESTA (solid red line) and overall cost of the practical restart schemes (dashed red line) versus NESTA with 5 continuation steps (dotted blue line) for a budget of 500 iterations. Crosses represent the restart occurrences. Left: n = 120. Right: n = 200.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Convergence rate and oversampling ratio", "weight": 1.0} -->

We now illustrate the theoretical results of Section 1.3 by running the practical scheme presented in Section 1.2.2 for increasing values of the oversampling ratio $\tau = {n/s}$. In Figure 3, we plot the best scheme found by the grid search, that approximates the optimal scheme, for a budget of $N = 500$ iterations. We use a non-logarithmic grid to find the best restart scheme. Other algorithmic parameters remain unchanged: $x_{0} = {A^{T}b}$ and $\epsilon_{0} = {\| x_{0}\|}_{1}$. We fix the dimension $p = 1000$ and either make $n$ vary for a fixed sparsity $s = 17$ or make $s$ vary for a fixed number of samples $n = 200$. These values ensure that we stay in the recovery regime as analyzed in \Juditsky and Nemirovski,. In both cases we do observe an improved convergence for increasing oversampling ratio $\tau$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Convergence rate and oversampling ratio", "weight": 1.0} -->

\psfrag{fmu}[b][t]{f(xk) − f(x*)}\psfrag{k}[t][b]{Inner iterations}\psfrag{tau}{τ}\includegraphics[width=195.12767pt]{figures/VRItersVsSig_n.eps} \psfrag{fmu}[b][t]{f(xk) − f(x*)}\psfrag{k}[t][b]{Inner iterations}\psfrag{tau}{τ}\includegraphics[width=195.12767pt]{figures/VRItersVsSig_s.eps} Figure 3. Best restart scheme found by grid search for increasing values of the oversampling ratio τ = n/s with p = 1000. Left: sparsity s = 17 fixed. Right: number of samples n = 200 fixed.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Renegar's condition number and compressed sensing performance", "weight": 1.0} -->

Our theoretical results showed that Renegar's condition number measures the complexity for the exact recovery problem. However it does not a priori control convergence of the robust recovery problems defined in the introduction. This numerical section aims therefore at analyzing the relevance of this condition number for general recovery problems in the $\ell_{1}$ case, assuming that their complexity corresponds roughly to that of checking optimality of a given point at each iteration, as mentioned in Section 2.3. We first describe how we approximate the value of $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$ as defined in for a given original signal $x^{\ast}$ and matrix $A \in {\mathbb{R}}^{n \times p}$. We then detail numerical experiments on synthetic data sets.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Computing $\\mathcal{R}_{\\mathcal{T}{(x^{\\ast})}}{(A)}$", "weight": 1.0} -->

The condition number $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$ appears here in upper bounds on computational complexities and statistical performances. In order to test numerically whether this quantity truly explains those features (as opposed to merely appearing in a wildly pessimistic bound), we explicitly compute it in numerical experiments.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Computing $\\mathcal{R}_{\\mathcal{T}{(x^{\\ast})}}{(A)}$", "weight": 1.0} -->

To compute $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$, we propose a heuristic which computes $\sigma_{\mathcal{T}{(x^{\ast})}}{(A)}$ in (37. ‣ 2.1. Conic linear systems ‣ 2. Renegar’s condition number and restricted singular values ‣ Computational Complexity versus Statistical Performance on Sparse Recovery Problems")) and, the value of a nonconvex minimization problem over the cone of descent directions $\mathcal{T}{(x^{\ast})}$. The closure of the latter is the polar of the cone generated by the subdifferential to the $\ell_{1}$-norm ball at $x^{\ast}$ \Chandrasekaran et al., [2012, §2.3\].

<!-- chunk {"id": "body-0072", "role": "body", "section": "Computing $\\mathcal{R}_{\\mathcal{T}{(x^{\\ast})}}{(A)}$", "weight": 1.0} -->

Let $S \subset {⟦1,p⟧}$ denote the support of $x^{\ast}$ and $s = {\operatorname{\mathbf{C}\mathbf{a}\mathbf{r}\mathbf{d}}{(S)}}$. Then, with $u = {{sign}{(x^{\ast})}}$, Thus, $\sigma_{\mathcal{T}{(x^{\ast})}}{(A)}$ is the square root of Let $\lambda$ denote the largest eigenvalue of $A^{T}A$. If it were not for the cone constraint, solutions of this problem would be the dominant eigenvectors of ${\lambda\mathbf{I}} - {A^{T}A}$, which suggests a *projected power method* \Deshpande et al., as follows.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Computing $\\mathcal{R}_{\\mathcal{T}{(x^{\\ast})}}{(A)}$", "weight": 1.0} -->

Given an initial guess $z_{0} \in {\mathbb{R}}^{p}$, ${\| z_{0}\|}_{2} = 1$, iterate where we used the orthogonal projector to $\mathcal{T}{(x^{\ast})}$, This convex, linearly constrained quadratic program is easily solved with CVX \Grant et al.,. As can be seen from KKT conditions, this iteration is a generalized power iteration \Luss and Teboulle, [2013; Journée et al., 2008\] From the latter, it follows that ${\|{Az_{k}}\|}_{2}$ decreases monotonically with $k$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Computing $\\mathcal{R}_{\\mathcal{T}{(x^{\\ast})}}{(A)}$", "weight": 1.0} -->

Thus, the sequence ${\|{Az_{k}}\|}_{2}$ converges, but it may do so slowly, and the value it converges to may depend on the initial iterate $z_{0}$. On both accounts, it helps greatly to choose $z_{0}$ well. To obtain one, we modify (95}⁢(𝐴) ‣ 4.2. Renegar’s condition number and compressed sensing performance ‣ 4. Numerical Results ‣ Computational Complexity versus Statistical Performance on Sparse Recovery Problems")) by smoothly penalizing the inequality constraint in the cost function, which results in a smooth optimization problem on the $\ell_{2}$ sphere.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Computing $\\mathcal{R}_{\\mathcal{T}{(x^{\\ast})}}{(A)}$", "weight": 1.0} -->

Specifically, for small ${\varepsilon_{1},\varepsilon_{2}} > 0$, we use smooth proxies ${h{(x)}} = {\sqrt{x^{2} + \varepsilon_{1}^{2}} - \varepsilon_{1}} \approx {|x|}$ and ${q{(x)}} = {\varepsilon_{2}{\log{({1 + {\exp{({x/\varepsilon_{2}})}}})}}} \approx {\max{(0,x)}}$. Then, with $\gamma > 0$ as Lagrange multiplier, we consider We solve the latter locally with Manopt \Boumal et al. itself with a uniformly random initial guess on the sphere, to obtain $z_{0}$. Then, we iterate the projected power method.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Computing $\\mathcal{R}_{\\mathcal{T}{(x^{\\ast})}}{(A)}$", "weight": 1.0} -->

The value ${\|{Az}\|}_{2}$ is an upper bound on $\sigma_{\mathcal{T}{(x^{\ast})}}{(A)}$, so that we obtain a lower bound on $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$. Empirically, this procedure, which is random only through the initial guess on the sphere, consistently returns the same value, up to five digits of accuracy, which suggests the proposed heuristic computes a good approximation of the condition number. Similarly positive results have been reported on other cones by Deshpande et al., where the special structure of the cone even made it possible to certify that this procedure indeed attains a global optimum in proposed experiments. Similarly, a generalized power method was recently shown to converge to global optimizers for the phase synchronization problem (in a certain noise regime) \Boumal, [2016; Zhong and Boumal, 2017\]. This gives us confidence in the estimates produced here.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Sparse recovery performance", "weight": 1.0} -->

We conduct numerical experiments in the $\ell_{1}$ case to illustrate the connection between the condition number $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$, the computational complexity of solving ($\ell_{1}$ recovery), and the statistical efficiency of the estimator (Robust $\ell_{1}$ recovery). Importantly, throughout the experiments, the classical condition number of $A$ will remain essentially constant, so that the main variations cannot be attributed to the latter.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Sparse recovery performance", "weight": 1.0} -->

We follow a standard setup, similar to some of the experiments by Donoho and Tsaig. Fixing the ambient dimension $p = 300$ and sparsity $s = {\| x^{\ast}\|}_{0} = 15$, we let the number of linear measurements $n$ vary from 1 to 150. For each value of $n$, we generate a random signal $x^{\ast} \in {\mathbb{R}}^{p}$ (uniformly random support, i.i.d. Gaussian entries, unit $\ell_{2}$-norm) and a random sensing matrix $A \in {\mathbb{R}}^{n \times p}$ with i.i.d. standard Gaussian entries. Furthermore, for a fixed value $\delta = 10^{- 2}$, we generate a random noise vector $w \in {\mathbb{R}}^{n}$ with i.i.d.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Sparse recovery performance", "weight": 1.0} -->

For each triplet $(A,x^{\ast},b)$, we first solve the noisy problem (Robust $\ell_{1}$ recovery) with the L1-Homotopy algorithm ($\tau = 10^{- 7}$) \Asif and Romberg and report the estimation error ${\|{\hat{x} - x^{\ast}}\|}_{2}$. Then, we solve the noiseless problem with L1-Homotopy and the TFOCS routine for basis pursuit ($\mu = 1$) \Becker, Candès and Grant,. Exact recovery is declared when the error is less than $10^{- 5}$, and we report the empirical probability of exact recovery, together with the number of iterations required by each of the solvers. The number of iterations of LARS \Efron et al., is also reported, for comparison.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Sparse recovery performance", "weight": 1.0} -->

For L1-Homotopy, we report the computation time, normalized by the computation time required for one least-squares solve in $A$, as in \Donoho and Tsaig, [2008, Fig. 3\], which accounts for the growth in $n$. Finally, we compute the classical condition number of $A$, $\kappa{(A)}$, as well as (a lower bound on) the cone-restricted condition number $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$, as per the previous section. As it is the computational bottleneck of the experiment, it is only computed for 20 of the 100 repetitions.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Sparse recovery performance", "weight": 1.0} -->

The results of Figure 4 show that the cone-restricted condition number explains both the computational complexity of ($\ell_{1}$ recovery) and the statistical complexity of (Robust $\ell_{1}$ recovery): fewer samples mean bad conditioning which in turn implies high computational complexity. We caution that our estimate of $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$ is only a lower bound. Indeed, for small $n$, the third plot on the left shows that, even in the absence of noise, recovery of $x^{\ast}$ is not achieved by (Robust $\ell_{1}$ recovery). Lemma 2.3 then requires $\mathcal{R}_{\mathcal{T}{(x^{\ast})}}{(A)}$ to be infinite.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Sparse recovery performance", "weight": 1.0} -->

But the computational complexity of solving ($\ell_{1}$ recovery) is visibly favorable for small $n$, where far from the phase transition, problem (P~A,$\mathcal{T}(x)$~) is far from infeasibility, which is just as easy to verify as it is to certify that (P~A,$\mathcal{T}(x)$~) is infeasible when $n$ is comfortably larger than needed. This phenomenon is best explained using a symmetric version of the condition number \Amelunxen and Lotz, (omitted here to simplify computations).

<!-- chunk {"id": "body-0083", "role": "body", "section": "Sparse recovery performance", "weight": 1.0} -->

We also solved problem ($\ell_{1}$ recovery) with interior point methods (IPM) via CVX. The number of iterations appeared mostly constant throughout the experiments, suggesting that the practical implementation of such solvers renders their complexity mostly data agnostic in the present setting. Likewise, the computation time required by L1-Homotopy on the noisy problem (Robust $\ell_{1}$ recovery), normalized by the time of a least-squares solve, is mostly constant (at about 150). This hints that the link between computational complexity of ($\ell_{1}$ recovery) and (Robust $\ell_{1}$ recovery) remains to be fully explained.
