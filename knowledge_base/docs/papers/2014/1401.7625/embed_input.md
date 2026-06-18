<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RES: Regularized Stochastic BFGS Algorithm

Topics include Convex optimization, Gradient descent, Stochastic gradients, Optimization, RES, Stochastic BFGS, BFGS, Stochastic gradient descent.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

RES, a regularized stochastic version of the Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton method is proposed to solve convex optimization problems with stochastic objectives. The use of stochastic gradient descent algorithms is widespread, but the number of iterations required to approximate optimal arguments can be prohibitive in high dimensional problems. Application of second order methods, on the other hand, is impracticable because computation of objective function Hessian inverses incurs excessive computational cost. BFGS modifies gradient descent by introducing a Hessian approximation matrix computed from finite gradient differences. RES utilizes stochastic gradients in lieu of deterministic gradients for both, the determination of descent directions and the approximation of the objective function's curvature. Since stochastic gradients can be computed at manageable computational cost RES is realizable and retains the convergence rate advantages of its deterministic counterparts. Convergence results show that lower and upper bounds on the Hessian egeinvalues of the sample functions are sufficient to guarantee convergence to optimal arguments. Numerical experiments showcase reductions in convergence time relative to stochastic gradient descent algorithms and non-regularized stochastic versions of BFGS.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An application of RES to the implementation of support vector machines is developed.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic optimization algorithms are used to solve the problem of optimizing an objective function over a set of feasible values in situations where the objective function is defined as an expectation over a set of random functions. In particular, consider an optimization variable $\mathbf{w} \in {\mathbb{R}}^{n}$ and a random variable ${\mathbf{θ}} \in \Theta \subseteq {\mathbb{R}}^{p}$ that determines the choice of a function ${f{(\mathbf{w},{\mathbf{θ}})}}:{{\mathbb{R}}^{n \times p}\rightarrow{\mathbb{R}}}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The stochastic optimization problems considered in this paper entail determination of the argument $\mathbf{w}^{\ast}$ that minimizes the expected value ${F{(\mathbf{w})}}:={{\mathbb{E}}_{\mathbf{θ}}{\lbrack{f{(\mathbf{w},{\mathbf{θ}})}}\rbrack}}$,

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We refer to $f{(\mathbf{w},{\mathbf{θ}})}$ as the random or instantaneous functions and to ${F{(\mathbf{w})}}:={{\mathbb{E}}_{\mathbf{θ}}{\lbrack{f{(\mathbf{w},{\mathbf{θ}})}}\rbrack}}$ as the average function. Problems having the form in are common in machine learning as well as in optimal resource allocation in wireless systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the objective function of is convex, descent algorithms can be used for its minimization. However, conventional descent methods require exact determination of the gradient of the objective function ${{\nabla_{\mathbf{w}}F}{(\mathbf{w})}} = {{\mathbb{E}}_{\mathbf{θ}}{\lbrack{{\nabla_{\mathbf{w}}f}{(\mathbf{w},{\mathbf{θ}})}}\rbrack}}$, which is intractable in general. Stochastic gradient descent (SGD) methods overcome this issue by using unbiased gradient estimates based on small subsamples of data and are the workhorse methodology used to solve large-scale stochastic optimization problems. Practical appeal of SGD remains limited, however, because they need large number of iterations to converge. This problem is most acute when the variable dimension $n$ is large as the condition number tends to increase with $n$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Developing stochastic Newton algorithms, on the other hand, is of little use because unbiased estimates of Newton steps are not easy to compute.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recourse to quasi-Newton methods then arises as a natural alternative. Indeed, quasi-Newton methods achieve superlinear convergence rates in deterministic settings while relying on gradients to compute curvature estimates. Since unbiased gradient estimates are computable at manageable cost, stochastic generalizations of quasi-Newton methods are not difficult to devise. Numerical tests of these methods on simple quadratic objectives suggest that stochastic quasi-Newton methods retain the convergence rate advantages of their deterministic counterparts. The success of these preliminary experiments notwithstanding, stochastic quasi-Newton methods are prone to yield near singular curvature estimates that may result in erratic behavior (see Section V-A).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we introduce a stochastic regularized version of the Broyden-Fletcher-Goldfarb-Shanno (BFGS) quasi-Newton method to solve problems with the generic structure. The proposed regularization avoids the near-singularity problems of more straightforward extensions and yields an algorithm with provable convergence guarantees when the functions $f{(\mathbf{w},{\mathbf{θ}})}$ are strongly convex.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We begin the paper with a brief discussion of SGD (Section II) and deterministic BFGS (Section II-A). The fundamental idea of BFGS is to continuously satisfy a secant condition that captures information on the curvature of the function being minimized while staying close to previous curvature estimates. To regularize deterministic BFGS we retain the secant condition but modify the proximity condition so that eigenvalues of the Hessian approximation matrix stay above a given threshold (Section II-A). This regularized version is leveraged to introduce the regularized stochastic BFGS algorithm (Section II-B). Regularized stochastic BFGS differs from standard BFGS in the use of a regularization to make a bound on the largest eigenvalue of the Hessian inverse approximation matrix and on the use of stochastic gradients in lieu of deterministic gradients for both, the determination of descent directions and the approximation of the objective function's curvature.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We abbreviate regularized stochastic BFGS as RES^11^1The letters "R and "E" appear in "regularized" as well as in the names of Broyden, Fletcher, and Daniel Goldfarb; "S" is for "stochastic" and Shanno..

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convergence properties of RES are then analyzed (Section III). We prove that lower and upper bounds on the Hessians of the sample functions $f{(\mathbf{w},{\mathbf{θ}})}$ are sufficient to guarantee convergence to the optimal argument $\mathbf{w}^{\ast}$ with probability 1 over realizations of the sample functions (Theorem 1). We complement this result with a characterization of the convergence rate which is shown to be at least linear in expectation (Theorem 2). Linear expected convergence rates are typical of stochastic optimization algorithms and, in that sense, no better than SGD. Advantages of RES relative to SGD are nevertheless significant, as we establish in numerical results for the minimization of a family of quadratic objective functions of varying dimensionality and condition number (Section IV). As we vary the condition number we observe that for well conditioned objectives RES and SGD exhibit comparable performance, whereas for ill conditioned functions RES outperforms SGD by an order of magnitude (Section IV-A). As we vary problem dimension we observe that SGD becomes unworkable for large dimensional problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

RES however, exhibits manageable degradation as the number of iterations required for convergence doubles when the problem dimension increases by a factor of ten (Section IV-C).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

An important example of a class of problems having the form in are support vector machines (SVMs) that reduce binary classification to the determination of a hyperplane that separates points in a given training set; see, e.g.,. We adapt RES for SVM problems (Section V) and show the improvement relative to SGD in convergence time, stability, and classification accuracy through numerical analysis (SectionV-A). We also compare RES to standard (non-regularized) stochastic BFGS. The regularization in RES is fundamental in guaranteeing convergence as standard (non-regularized) stochastic BFGS is observed to routinely fail in the computation of a separating hyperplane.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Algorithm definition", "weight": 1.0} -->

We can find the optimal argument $\mathbf{w}^{\ast}$ in with a gradient descent algorithm where gradients of $F{(\mathbf{w})}$ are given by

<!-- chunk {"id": "body-0017", "role": "body", "section": "Algorithm definition", "weight": 1.0} -->

When the number of functions $f{(\mathbf{w},{\mathbf{θ}})}$ is large, as is the case in most problems of practical interest, exact evaluation of the gradient $\mathbf{s}{(\mathbf{w})}$ is impractical. This motivates the use of stochastic gradients in lieu of actual gradients. More precisely, consider a given set of $L$ realizations $\overset{\sim}{\mathbf{θ}} = {\lbrack{\mathbf{θ}}_{1};\ldots;{\mathbf{θ}}_{L}\rbrack}$ and define the stochastic gradient of $F{(\mathbf{w})}$ at $\mathbf{w}$ given samples $\overset{\sim}{\mathbf{θ}}$ as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithm definition", "weight": 1.0} -->

Introducing now a time index $t$, an initial iterate $\mathbf{w}_{0}$, and a step size sequence $\epsilon_{t}$, a stochastic gradient descent algorithm is defined by the iteration

<!-- chunk {"id": "body-0019", "role": "body", "section": "Algorithm definition", "weight": 1.0} -->

To implement we compute stochastic gradients $\hat{\mathbf{s}}{(\mathbf{w}_{t},{\overset{\sim}{\mathbf{θ}}}_{t})}$ using. In turn, this requires determination of the gradients of the random functions $f{(\mathbf{w},{\mathbf{θ}}_{tl})}$ for each ${\mathbf{θ}}_{tl}$ component of ${\overset{\sim}{\mathbf{θ}}}_{t}$ and their corresponding average. The computational cost is manageable for small values of $L$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm definition", "weight": 1.0} -->

The stochastic gradient $\hat{\mathbf{s}}{(\mathbf{w},\overset{\sim}{\mathbf{θ}})}$ in is an unbiased estimate of the (average) gradient $\mathbf{s}{(\mathbf{w})}$ in in the sense that ${{\mathbb{E}}_{\overset{\sim}{\mathbf{θ}}}{\lbrack{\hat{\mathbf{s}}{(\mathbf{w},\overset{\sim}{\mathbf{θ}})}}\rbrack}} = {\mathbf{s}{(\mathbf{w})}}$. Thus, the iteration in is such that, on average, iterates descend along a negative gradient direction. This intuitive observation can be formalized into a proof of convergence when the step size sequence is selected as nonsummable but square summable, i.e.,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm definition", "weight": 1.0} -->

A customary step size choice for which holds is to make $\epsilon_{t} = {{\epsilon_{0}T_{0}}/{({T_{0} + t})}}$, for given parameters $\epsilon_{0}$ and $T_{0}$ that control the initial step size and its speed of decrease, respectively. Convergence notwithstanding, the number of iterations required to approximate $\mathbf{w}^{\ast}$ is very large in problems that don't have small condition numbers. This motivates the alternative methods we discuss in subsequent sections.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

To speed up convergence of resort to second order methods is of little use because evaluating Hessians of the objective function is computationally intensive. A better suited methodology is the use of quasi-Newton methods whereby gradient descent directions are premultiplied by a matrix $\mathbf{B}_{t}^{- 1}$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

The idea is to select positive definite matrices $\mathbf{B}_{t} \succ 0$ close to the Hessian of the objective function ${\mathbf{H}{(\mathbf{w}_{t})}}:={{\nabla^{2}F}{(\mathbf{w}_{t})}}$. Various methods are known to select matrices $\mathbf{B}_{t}$, including those by Broyden e.g. Davidon, Feletcher, and Powell (DFP); and Broyden, Fletcher, Goldfarb, and Shanno (BFGS) e.g.,. We work here with the matrices $\mathbf{B}_{t}$ used in BFGS since they have been observed to work best in practice.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

In BFGS -- and all other quasi-Newton methods for that matter -- the function's curvature is approximated by a finite difference. Specifically, define the variable and gradient variations at time $t$ as

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

respectively, and select the matrix $\mathbf{B}_{t + 1}$ to be used in the next time step so that it satisfies the secant condition ${\mathbf{B}_{t + 1}\mathbf{v}_{t}} = \mathbf{r}_{t}$. The rationale for this selection is that the Hessian $\mathbf{H}{(\mathbf{w}_{t})}$ satisfies this condition for $\mathbf{w}_{t + 1}$ tending to $\mathbf{w}_{t}$. Notice however that the secant condition ${\mathbf{B}_{t + 1}\mathbf{v}_{t}} = \mathbf{r}_{t}$ is not enough to completely specify $\mathbf{B}_{t + 1}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

To resolve this indeterminacy, matrices $\mathbf{B}_{t + 1}$ in BFGS are also required to be as close as possible to $\mathbf{B}_{t}$ in terms of the Gaussian differential entropy,

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

The constraint $\mathbf{Z} \succeq \mathbf{0}$ in (II-A) restricts the feasible space to positive semidefinite matrices whereas the constraint ${\mathbf{Z}\mathbf{v}}_{t} = \mathbf{r}_{t}$ requires $\mathbf{Z}$ to satisfy the secant condition.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

The solution $\mathbf{B}_{t + 1}$ of the semidefinite program in (II-A) is therefore closest to $\mathbf{B}_{t}$ in the sense of minimizing the Gaussian differential entropy among all positive semidefinite matrices that satisfy the secant condition ${\mathbf{Z}\mathbf{v}}_{t} = \mathbf{r}_{t}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

Strongly convex functions are such that the inner product of the gradient and variable variations is positive, i.e., ${\mathbf{v}_{t}^{T}\mathbf{r}_{t}} > 0$. In that case the matrix $\mathbf{B}_{t + 1}$ in (II-A) is explicitly given by the update -- see, e.g., and the proof of Lemma 1 --,

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

In principle, the solution to (II-A) could be positive semidefinite but not positive definite, i.e., we can have $\mathbf{B}_{t + 1} \succeq \mathbf{0}$ but $\mathbf{B}_{t + 1} \nsucc \mathbf{0}$. However, through direct operation in it is not difficult to conclude that $\mathbf{B}_{t + 1}$ stays positive definite if the matrix $\mathbf{B}_{t}$ is positive definite. Thus, initializing the curvature estimate with a positive definite matrix $\mathbf{B}_{0} \succ \mathbf{0}$ guarantees $\mathbf{B}_{t} \succ \mathbf{0}$ for all subsequent times $t$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

Still, it is possible for the smallest eigenvalue of $\mathbf{B}_{t}$ to become arbitrarily close to zero which means that the largest eigenvalue of $\mathbf{B}_{t}^{- 1}$ can become arbitrarily large. This has been proven not to be an issue in BFGS implementations but is a more significant challenge in the stochastic version proposed here.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

To avoid this problem we introduce a regularization of (II-A) to enforce the eigenvalues of $\mathbf{B}_{t + 1}$ to exceed a positive constant $\delta$. Specifically, we redefine $\mathbf{B}_{t + 1}$ as the solution of the semidefinite program,

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-A Regularized BFGS", "weight": 1.0} -->

The curvature approximation matrix $\mathbf{B}_{t + 1}$ defined in (II-A) still satisfies the secant condition ${\mathbf{B}_{t + 1}\mathbf{v}_{t}} = \mathbf{r}_{t}$ but has a different proximity requirement since instead of comparing $\mathbf{B}_{t}$ and $\mathbf{Z}$ we compare $\mathbf{B}_{t}$ and $\mathbf{Z} - {\delta\mathbf{I}}$. While (II-A) does not ensure that all eigenvalues of $\mathbf{B}_{t + 1}$ exceed $\delta$ we can show that this will be the case under two minimally restrictive assumptions. We do so in the following proposition where we also give an explicit solution for (II-A) analogous to the expression in that solves the non regularized problem in (II-A).

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

As can be seen from the regularized BFGS curvature estimate $\mathbf{B}_{t + 1}$ is obtained as a function of previous estimates $\mathbf{B}_{t}$, iterates $\mathbf{w}_{t}$ and $\mathbf{w}_{t + 1}$, and corresponding gradients $\mathbf{s}{(\mathbf{w}_{t})}$ and $\mathbf{s}{(\mathbf{w}_{t + 1})}$. We can then think of a method in which gradients $\mathbf{s}{(\mathbf{w}_{t})}$ are replaced by stochastic gradients $\hat{\mathbf{s}}{(\mathbf{w}_{t},{\overset{\sim}{\mathbf{θ}}}_{t})}$ in both, the curvature approximation update in and the descent iteration.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

where we added the identity bias term $\Gamma\mathbf{I}$ for a given positive constant $\Gamma > 0$. Relative to SGD as defined, RES as defined by differs in the use of the matrix ${\hat{\mathbf{B}}}_{t}^{- 1} + {\Gamma\mathbf{I}}$ to account for the curvature of $F{(\mathbf{w})}$. Relative to (regularized or non regularized) BFGS as defined in RES differs in the use of stochastic gradients $\hat{\mathbf{s}}{(\mathbf{w}_{t},{\overset{\sim}{\mathbf{θ}}}_{t})}$ instead of actual gradients and in the use of the curvature approximation ${\hat{\mathbf{B}}}_{t}^{- 1} + {\Gamma\mathbf{I}}$ in lieu of $\mathbf{B}_{t}^{- 1}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

Observe that in we add a bias $\Gamma\mathbf{I}$ to the curvature approximation ${\hat{\mathbf{B}}}_{t}^{- 1}$. This is necessary to ensure convergence by hedging against random variations in ${\hat{\mathbf{B}}}_{t}^{- 1}$ as we discuss in Section III.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

and redefine ${\overset{\sim}{\mathbf{r}}}_{t}$ so that it stands for the modified stochastic gradient variation

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

8: Compute modified stochastic gradient variation [cf. ]

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

Algorithm 1 RES: Regularized Stochastic BFGS

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

The resulting RES algorithm is summarized in Algorithm 1. The two core steps in each iteration are the descent in Step 4 and the update of the Hessian approximation ${\hat{\mathbf{B}}}_{t}$ in Step 8. Step 2 comprises the observation of $L$ samples that are required to compute the stochastic gradients in steps 3 and 5. The stochastic gradient $\hat{\mathbf{s}}{(\mathbf{w}_{t},{\overset{\sim}{\mathbf{θ}}}_{t})}$ in Step 3 is used in the descent iteration in Step 4. The stochastic gradient of Step 3 along with the stochastic gradient $\hat{\mathbf{s}}{(\mathbf{w}_{t + 1},{\overset{\sim}{\mathbf{θ}}}_{t})}$ of Step 5 are used to compute the variations in steps 6 and 7 that permit carrying out the update of the Hessian approximation ${\hat{\mathbf{B}}}_{t}$

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-B RES: Regularized Stochastic BFGS", "weight": 1.0} -->

in Step 8. Iterations are initialized at arbitrary variable $\mathbf{w}_{0}$ and positive definite matrix ${\hat{\mathbf{B}}}_{0}$ with the smallest eigenvalue larger than $\delta$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Convergence", "weight": 1.0} -->

For the subsequent analysis it is convenient to define the instantaneous objective function associated with samples $\overset{\sim}{\mathbf{θ}} = {\lbrack{\mathbf{θ}}_{1},\ldots,{\mathbf{θ}}_{L}\rbrack}$ as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Convergence", "weight": 1.0} -->

Our goal here is to show that as time progresses the sequence of variable iterates $\mathbf{w}_{t}$ approaches the optimal argument $\mathbf{w}^{\ast}$. In proving this result we make the following assumptions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The second moment of the norm of the stochastic gradient is bounded for all $\mathbf{w}$. i.e., there exists a constant $S^{2}$ such that for all variables $\mathbf{w}$ it holds

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The regularization constant $\delta$ is smaller than the smallest Hessian eigenvalue $\overset{\sim}{m}$, i.e., $\delta < \overset{\sim}{m}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

As a consequence of Assumption 1 similar eigenvalue bounds hold for the (average) function $F{(\mathbf{w})}$. Indeed, it follows from the linearity of the expectation operator and the expression in that the Hessian is ${{\nabla_{\mathbf{w}}^{2}F}{(\mathbf{w})}} = {\mathbf{H}{(\mathbf{w})}} = {{\mathbb{E}}_{\mathbf{θ}}{\lbrack{\hat{\mathbf{H}}{(\mathbf{w},\overset{\sim}{\mathbf{θ}})}}\rbrack}}$. Combining this observation with the bounds in it follows that there are constants $m \geq \overset{\sim}{m}$ and $M \leq \overset{\sim}{M}$ such that

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The bounds in are customary in convergence proofs of descent methods. For the results here the stronger condition spelled in Assumption 1 is needed. The restriction imposed by Assumption 2 is typical of stochastic descent algorithms, its intent being to limit the random variation of stochastic gradients. Assumption 3 is necessary to guarantee that the inner product ${{\overset{\sim}{\mathbf{r}}}_{t}^{T}\mathbf{v}_{t}} = {{({\mathbf{r}_{t} - {\delta\mathbf{v}_{t}}})}^{T}\mathbf{v}_{t}} > 0$ \cf. Proposition is positive as we show in the following lemma.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-A Rate of Convergence", "weight": 1.0} -->

We complement the convergence result in Theorem 1 with a characterization of the expected convergence rate that we introduce in the following theorem.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical analysis", "weight": 1.0} -->

We compare convergence times of RES and SGD in problems with small and large condition numbers. We use a stochastic quadratic objective function as a test case. In particular, consider a positive definite diagonal matrix $\mathbf{A} \in {\mathbb{S}}_{n}^{+ +}$, a vector $\mathbf{b} \in {\mathbb{R}}^{n}$, a random vector ${\mathbf{θ}} \in {\mathbb{R}}^{n}$, and diagonal matrix $\text{diag}{({\mathbf{θ}})}$ defined by $\mathbf{θ}$. The function $F{(\mathbf{w})}$ in is defined as

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical analysis", "weight": 1.0} -->

In (IV), the random vector $\mathbf{θ}$ is chosen uniformly at random from the $n$ dimensional box $\Theta = {\lbrack{- \theta_{0}},\theta_{0}\rbrack}^{n}$ for some given constant $\theta_{0} < 1$. The linear term $\mathbf{b}^{T}\mathbf{w}$ is added so that the instantaneous functions $f{(\mathbf{w},\theta)}$ have different minima which are (almost surely) different from the minimum of the average function $F{(\mathbf{w})}$. The quadratic term is chosen so that the condition number of $F{(\mathbf{w})}$ is the condition number of $\mathbf{A}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical analysis", "weight": 1.0} -->

Indeed, just observe that since ${{\mathbb{E}}_{\theta}{\lbrack{\mathbf{θ}}\rbrack}} = \mathbf{0}$, the average function in (IV) can be written as ${F{(\mathbf{w})}} = {{{({1/2})}\mathbf{w}^{T}{\mathbf{A}\mathbf{w}}} + {\mathbf{b}^{T}\mathbf{w}}}$. The parameter $\theta_{0}$ controls the variability of the instantaneous functions $f{(\mathbf{w},\theta)}$. For small $\theta_{0} \approx 0$ instantaneous functions are close to each other and to the average function. For large $\theta_{0} \approx 1$ instantaneous functions vary over a large range.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical analysis", "weight": 1.0} -->

Further note that we can write the optimum argument as $\mathbf{w}^{\ast} = {\mathbf{A}^{- 1}\mathbf{b}}$ for comparison against iterates $\mathbf{w}_{t}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical analysis", "weight": 1.0} -->

For a given $\rho$ we study the convergence metric

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical analysis", "weight": 1.0} -->

which represents the time needed to achieve a given relative distance to optimality ${{\|{\mathbf{w}_{t} - \mathbf{w}^{\ast}}\|}/{\|\mathbf{w}^{\ast}\|}} \leq \rho$ as measured in terms of the number $Lt$ of stochastic functions that are processed to achieve such accuracy.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-A Effect of problem's condition number", "weight": 1.0} -->

To study the effect of the problem's condition number we generate instances of (IV) by choosing $\mathbf{b}$ uniformly at random from the box ${\lbrack 0,1\rbrack}^{n}$ and the matrix $\mathbf{A}$ as diagonal with elements $a_{ii}$ uniformly drawn from the discrete set $\{ 1,10^{- 1},\ldots,10^{- \xi}\}$. This choice of $\mathbf{A}$ yields problems with condition number $10^{\xi}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A Effect of problem's condition number", "weight": 1.0} -->

Representative runs of RES and SGD for $n = 50$, $\theta_{0} = 0.5$, and $\xi = 2$ are shown in Fig. 1. For the RES run the stochastic gradients $\hat{\mathbf{s}}{(\mathbf{w},\overset{\sim}{\mathbf{θ}})}$ in are computed as an average of $L = 5$ realizations, the regularization parameter in (II-A) is set to $\delta = 10^{- 3}$, and the minimum progress parameter in to $\Gamma = 10^{- 4}$. For SGD we use $L = 1$. In both cases the step size sequence is of the form $\epsilon_{t} = {{\epsilon_{0}T_{0}}/{({T_{0} + t})}}$ with $\epsilon_{0} = 10^{- 1}$ and $T_{0} = 10^{3}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-A Effect of problem's condition number", "weight": 1.0} -->

Since we are using different value of $L$ for SGD and RES we plot the relative distance to optimality ${\|{\mathbf{w}_{t} - \mathbf{w}^{\ast}}\|}/{\|\mathbf{w}^{\ast}\|}$ against the number $Lt$ of functions processed up until iteration $t$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A Effect of problem's condition number", "weight": 1.0} -->

Conversely, upon processing ${Lt} = {1,200}$ random functions -- which corresponds to $t = 240$ iterations -- RES achieves accuracy ${{\|{\mathbf{w}_{t} - \mathbf{w}^{\ast}}\|}/{\|\mathbf{w}^{\ast}\|}} = {6.6 \times 10^{- 3}}$. This relative performance difference can be made arbitrarily large by modifying the condition number of $\mathbf{A}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Effect of problem's condition number", "weight": 1.0} -->

A more comprehensive analysis of the relative advantages of RES appears in figs. 2 and 3. We keep the same parameters used to generate Fig. 1 except that we use $\xi = 0$ for Fig. 2 and $\xi = 2$ for Fig. 3. This yields a family of well-condition functions with condition number $10^{\xi} = 1$ and a family of ill-conditioned functions with condition number $10^{\xi} = 10^{2}$. In both figures we consider $\rho = 10^{- 2}$ and study the convergence times $\tau$ and $\tau^{\prime}$ of RES and SGD, respectively \cf. ([53)\]. Resulting empirical distributions of $\tau$ and $\tau^{\prime}$ across $J = {1,000}$ instances of the functions $F{(\mathbf{w})}$ in (IV) are reported in figs. 2 and 3 for the well conditioned and ill conditioned families, respectively.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-A Effect of problem's condition number", "weight": 1.0} -->

For the well conditioned family RES reduces the number of functions processed from an average of ${\overline{\tau}}^{\prime} = 601$ in the case of SGD to an average of $\overline{\tau} = 144$. This nondramatic improvement becomes more significant for the ill conditioned family where the reduction is from an average of ${\overline{\tau}}^{\prime} = {7.2 \times 10^{3}}$ for SGD to an average of $\overline{\tau} = {3.2 \times 10^{2}}$ for RES. The spread in convergence times is also smaller for RES.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B Choice of stochastic gradient average", "weight": 1.0} -->

To study the effect of the choice of $L$ on RES we consider problems as in (IV) with matrices $\mathbf{A}$ and vectors $\mathbf{b}$ generated as in Section IV-A. We consider problems with $n = 50$, $\theta_{0} = 0.5$, and $\xi = 2$; set the RES parameters to $\delta = 10^{- 3}$ and $\Gamma = 10^{- 4}$; and the step size sequence to $\epsilon_{t} = {{\epsilon_{0}T_{0}}/{({T_{0} + t})}}$ with $\epsilon_{0} = 10^{- 1}$ and $T_{0} = 10^{3}$. We then consider different choices of $L$ and for each specific value generate $J = {1,000}$ problem instances.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-B Choice of stochastic gradient average", "weight": 1.0} -->

For each run we record the total number $\tau_{L}$ of sample functions that need to be processed to achieve relative distance to optimality ${{\|{\mathbf{w}_{t} - \mathbf{w}^{\ast}}\|}/{\|\mathbf{w}^{\ast}\|}} \leq 10^{- 2}$ \cf. ([53)\]. If $\tau > 10^{4}$ we report $\tau = 10^{4}$ and interpret this outcome as a convergence failure. The resulting estimates of the probability distributions of the times $\tau_{L}$ are reported in Fig. 4 for $L = 1$, $L = 2$, $L = 5$, $L = 10$, and $L = 20$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-B Choice of stochastic gradient average", "weight": 1.0} -->

The trends in convergence times $\tau$ apparent in Fig. 4 are: (i) As we increase $L$ the variance of convergence times decreases. (ii) The average convergence time decreases as we go from small to moderate values of $L$ and starts increasing as we go from moderate to large values of $L$. Indeed, the empirical standard deviations of convergence times decrease monotonically from $\sigma_{\tau_{1}} = {2.8 \times 10^{3}}$ to $\sigma_{\tau_{2}} = {2.6 \times 10^{2}}$, $\sigma_{\tau_{5}} = 31.7$, $\sigma_{\tau_{10}} = 28.8$, and $\sigma_{\tau_{20}} = 22.7$, when $L$ increases from $L = 1$ to $L = 2$, $L = 5$, $L = 10$, and $L = 20$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-B Choice of stochastic gradient average", "weight": 1.0} -->

This behavior is expected since increasing $L$ results in curvature estimates ${\hat{\mathbf{B}}}_{t}$ closer to the Hessian $\mathbf{H}{(\mathbf{w}_{t})}$ thereby yielding better convergence times. As we keep increasing $L$, there is no payoff in terms of better curvature estimates and we just pay a penalty in terms of more function evaluations for an equally good ${\hat{\mathbf{B}}}_{t}$ matrix. This can be corroborated by observing that the convergence times $\tau_{5}$ are about half those of $\tau_{10}$ which in turn are about half those of $\tau_{20}$. This means that the actual convergence times $\tau/L$ have similar distributions for $L = 5$, $L = 10$, and $L = 20$. The empirical distributions in Fig. 4 show that moderate values of $L$ suffice to provide workable curvature approximations. This justifies the use $L = 5$ in sections IV-A and IV-C

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-C Effect of problem's dimension", "weight": 1.0} -->

To evaluate performance for problems of different dimensions we consider functions of the form in (IV) with $\mathbf{b}$ uniformly chosen from the box ${\lbrack 0,1\rbrack}^{n}$ and diagonal matrix $\mathbf{A}$ as in Section IV-A. However, we select the elements $a_{ii}$ as uniformly drawn from the interval $\lbrack 0,1\rbrack$. This results in problems with more moderate condition numbers and allows for a comparative study of performance degradations of RES and SGD as the problem dimension $n$ grows.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-C Effect of problem's dimension", "weight": 1.0} -->

The variability parameter for the random vector $\mathbf{θ}$ is set to $\theta_{0} = 0.5$. The RES parameters are $L = 5$, $\delta = 10^{- 3}$, and $\Gamma = 10^{- 4}$. For SGD we use $L = 1$. In both methods the step size sequence is $\epsilon_{t} = {{\epsilon_{0}T_{0}}/{({T_{0} + t})}}$ with $\epsilon_{0} = 10^{- 1}$ and $T_{0} = 10^{3}$. For a problem of dimension $n$ we study convergence times $\tau_{n}$ and $\tau_{n}^{\prime}$ of RES and SGD as defined in with $\rho = 1$. For each value of $n$ considered we determine empirical distributions of $\tau_{n}$ and $\tau_{n}^{\prime}$ across $J = {1,000}$ problem instances.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-C Effect of problem's dimension", "weight": 1.0} -->

If $\tau > {5 \times 10^{5}}$ we report $\tau = {5 \times 10^{5}}$ and interpret this outcome as a convergence failure. The resulting histograms are shown in Fig. 5 for $n = 5$, $n = 10$, $n = 20$, and $n = 50$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-C Effect of problem's dimension", "weight": 1.0} -->

For problems of small dimension having $n = 5$ the average performances of RES and SGD are comparable, with SGD performing slightly better. E.g., the medians of these times are ${\text{median}{(\tau_{5})}} = 400$ and ${\text{median}{(\tau_{5}^{\prime})}} = 265$, respectively. A more significant difference is that times $\tau_{5}$ of RES are more concentrated than times $\tau_{5}^{\prime}$ of SGD. The latter exhibits large convergence times $\tau_{5}^{\prime} > 10^{3}$ with probability $0.06$ and fails to converge altogether in a few rare instances -- we have $\tau_{5}^{\prime} = {5 \times 10^{5}}$ in 1 out of 1,000 realizations. In the case of RES all realizations of $\tau_{5}$ are in the interval $70 \leq \tau_{5} \leq 1095$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-C Effect of problem's dimension", "weight": 1.0} -->

For large dimensional problems having $n = 50$ SGD becomes unworkable. It fails to achieve convergence in $5 \times 10^{5}$ iterations with probability $0.07$ and exceeds $10^{4}$ iterations with probability $0.45$. For RES we fail to achieve convergence in $5 \times 10^{5}$ iterations with probability $3 \times 10^{- 3}$ and achieve convergence in less than $10^{4}$ iterations in all other cases. Further observe that RES degrades smoothly as $n$ increases. The median number of gradient evaluations needed to achieve convergence increases by a factor of ${{{\text{median}{(\tau_{50}^{\prime})}}/\text{median}}{(\tau_{5}^{\prime})}} = 29.9$ as we increase $n$ by a factor of $10$. The spread in convergence times remains stable as $n$ grows.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Support vector machines", "weight": 1.0} -->

A particular case of is the implementation of a support vector machine (SVM). Given a training set with points whose class is known the goal of a SVM is to find a hyperplane that best separates the training set. To be specific let $\mathcal{S} = {\{{(\mathbf{x}_{i},y_{i})}\}}_{i = 1}^{N}$ be a training set containing $N$ pairs of the form $(\mathbf{x}_{i},y_{i})$, where $\mathbf{x}_{i} \in {\mathbb{R}}^{n}$ is a feature vector and $y_{i} \in {\{{- 1},1\}}$ is the corresponding vector's class.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Support vector machines", "weight": 1.0} -->

The goal is to find a hyperplane supported by a vector $\mathbf{w} \in {\mathbb{R}}^{n}$ which separates the training set so that ${\mathbf{w}^{T}\mathbf{x}_{i}} > 0$ for all points with $y_{i} = 1$ and ${\mathbf{w}^{T}\mathbf{x}_{i}} < 0$ for all points with $y_{i} = {- 1}$. This vector may not exist if the data is not perfectly separable, or, if the data is separable there may be more than one separating vector. We can deal with both situations with the introduction of a loss function $l{({(\mathbf{x},y)};\mathbf{w})}$ defining some measure of distance between the point $\mathbf{x}_{i}$ and the hyperplane supported by $\mathbf{w}$. We then select the hyperplane supporting vector as

<!-- chunk {"id": "body-0072", "role": "body", "section": "Support vector machines", "weight": 1.0} -->

it follows that we can rewrite the objective function in as

<!-- chunk {"id": "body-0073", "role": "body", "section": "Support vector machines", "weight": 1.0} -->

since each of the functions $f{(\mathbf{w},{\mathbf{θ}})}$ is drawn with probability $1/N$ according to the definition of $m_{\mathbf{θ}}{({\mathbf{θ}})}$. Substituting into yields a problem with the general form of with random functions $f{(\mathbf{w},{\mathbf{θ}})}$ explicitly given.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Support vector machines", "weight": 1.0} -->

These training points are selected uniformly at random from the training set $\mathcal{S}$. We also need to particularize steps 3 and 5 to evaluate the stochastic gradient of the specific instantaneous function. E.g., Step 3 takes the form

<!-- chunk {"id": "body-0075", "role": "body", "section": "Support vector machines", "weight": 1.0} -->

The specific form of Step 5 is obtained by replacing $\mathbf{w}_{t + 1}$ for $\mathbf{w}_{t}$ in (V). We analyze the behavior of Algorithm in the implementation of a SVM in the following section.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

Likewise, each of the $n$ components of each of the feature vectors $\mathbf{x}_{i} \in {\mathbb{R}}^{n}$ is chosen uniformly at random from the interval $\lbrack{- 0.2},0.8\rbrack$ for the class $y_{i} = 1$. The overlap in the range of the feature vectors is such that the classification accuracy expected from a clairvoyant classifier that knows the statistic model of the data set is less than $100\%$. Exact values can be computed from the Irwin-Hall distribution. For $n = 4$ this amounts to $98\%$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

In all of our numerical experiments the parameter $\lambda$ in is set to $\lambda = 10^{- 3}$. Recall that since the Hessian eigenvalues of ${f{(\mathbf{w},{\mathbf{θ}})}}:={{{\lambda{\|\mathbf{w}\|}^{2}}/2} + {l{({(\mathbf{x}_{i},y_{i})};\mathbf{w})}}}$ are, at least, equal to $\lambda$ this implies that the eigenvalue lower bound $\overset{\sim}{m}$ is such that $\overset{\sim}{m} \geq \lambda = 10^{- 3}$. We therefore set the RES regularization parameter to $\delta = \lambda = 10^{- 3}$. Further set the minimum progress parameter in to $\Gamma = 10^{- 4}$ and the sample size for computation of stochastic gradients to $L = 5$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

The stepsizes are of the form $\epsilon_{t} = {{\epsilon_{0}T_{0}}/{({T_{0} + t})}}$ with $\epsilon_{0} = {3 \times 10^{- 2}}$ and $T_{0} = 10^{3}$. We compare the behavior of SGD and RES for a small dimensional problem with $n = 4$ and a large dimensional problem with $n = 40$. For SGD the sample size in is $L = 1$ and we use the same stepsize sequence used for RES.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

An illustration of the relative performances of SGD and RES for $n = 4$ is presented in Fig. 6. The value of the objective function $F{(\mathbf{w}_{t})}$ is represented with respect to the number of feature vectors processed, which is given by the product $Lt$ between the iteration index and the sample size used to compute stochastic gradients. This is done because the sample sizes in RES ($L = 5$) and SGD ($L = 1$) are different. The curvature correction of RES results in significant reductions in convergence time. E.g., RES achieves an objective value of ${F{(\mathbf{w}_{t})}} = {6.5 \times 10^{- 2}}$ upon processing of ${Lt} = 315$ feature vectors. To achieve the same objective value ${F{(\mathbf{w}_{t})}} = {6.5 \times 10^{- 2}}$ SGD processes $1.74 \times 10^{3}$ feature vectors.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

The performance difference between the two methods is larger for feature vectors of larger dimension $n$. The plot of the value of the objective function $F{(\mathbf{w}_{t})}$ with respect to the number of feature vectors processed $Lt$ is shown in Fig. 7 for $n = 40$. The convergence time of RES increases but is still acceptable. For SGD the algorithm becomes unworkable. After processing $3.5 \times 10^{3}$ RES reduces the objective value to ${F{(\mathbf{w}_{t})}} = {5.55 \times 10^{- 4}}$ while SGD has barely made progress at ${F{(\mathbf{w}_{t})}} = {1.80 \times 10^{- 2}}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

Differences in convergence times translate into differences in classification accuracy when we process all $N$ vectors in the training set. This is shown for dimension $n = 4$ and training set size $N = {2.5 \times 10^{3}}$ in Fig. 8. To build Fig. 8 we process $N = {2.5 \times 10^{3}}$ feature vectors with RES and SGD with the same parameters used in Fig. 6. We then use these vectors to classify $10^{4}$ observations in the test set and record the percentage of samples that are correctly classified. The process is repeated $10^{3}$ times to estimate the probability distribution of the correct classification percentage represented by the histograms shown. The dominance of RES with respect to SGD is almost uniform. The vector $\mathbf{w}_{t}$ computed by SGD classifies correctly at most $65\%$ of the of the feature vectors in the test set. The vector $\mathbf{w}_{t}$ computed by RES exceeds this accuracy with probability $0.98$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

Perhaps more relevant, the classifier computed by RES achieves a mean classification accuracy of $82.2\%$ which is not far from the clairvoyant classification accuracy of $98\%$. Although performance is markedly better in general, RES fails to compute a working classifier with probability $0.02$. We omit comparison of classification accuracy for $n = 40$ due to space considerations. As suggested by Fig. 7 the differences are more significant than for the case $n = 4$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

We also investigate the difference between regularized and non-regularized versions of stochastic BFGS for feature vectors of dimension $n = 10$. Observe that non-regularized stochastic BFGS corresponds to making $\delta = 0$ and $\Gamma = 0$ in Algorithm 1. To illustrate the advantage of the regularization induced by the proximity requirement in (II-A), as opposed to the non regularized proximity requirement in (II-A), we keep a constant stepsize $\epsilon_{t} = 10^{- 1}$. The corresponding evolutions of the objective function values $F{(\mathbf{w}_{t})}$ with respect to the number of feature vectors processed $Lt$ are shown in Fig. 9 along with the values associated with stochastic gradient descent. As we reach convergence the likelihood of having small eigenvalues appearing in ${\hat{\mathbf{B}}}_{t}$ becomes significant. In regularized stochastic BFGS (RES) this results in recurrent jumps away from the optimal classifier $\mathbf{w}^{\ast}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-A Numerical Analysis", "weight": 1.0} -->

However, the regularization term limits the size of the jumps and further permits the algorithm to consistently recover a reasonable curvature estimate. In Fig. 9 we process $10^{4}$ feature vectors and observe many occurrences of small eigenvalues. However, the algorithm always recovers and heads back to a good approximation of $\mathbf{w}^{\ast}$. In the absence of regularization small eigenvalues in ${\hat{\mathbf{B}}}_{t}$ result in larger jumps away from $\mathbf{w}^{\ast}$. This not only sets back the algorithm by a much larger amount than in the regularized case but also results in a catastrophic deterioration of the curvature approximation matrix ${\hat{\mathbf{B}}}_{t}$. In Fig. 9 we observe recovery after the first two occurrences of small eigenvalues but eventually there is a catastrophic deviation after which non-regularized stochastic BFSG behaves not better than SGD.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Convex optimization problems with stochastic objectives were considered. RES, a stochastic implementation of a regularized version of the Broyden-Fletcher-Goldfarb-Shanno quasi-Newton method was introduced to find corresponding optimal arguments. Almost sure convergence was established under the assumption that sample functions have well behaved Hessians. A linear convergence rate in expectation was further proven. Numerical results showed that RES affords important reductions in terms of convergence time relative to stochastic gradient descent. These reductions are of particular significance for problems with large condition numbers or large dimensionality since RES exhibits remarkable stability in terms of the total number of iterations required to achieve target accuracies. An application of RES to support vector machines was also developed. In this particular case the advantages of RES manifest in improvements of classification accuracies for training sets of fixed cardinality. Future research directions include the development of limited memory versions as well as distributed versions where the function to be minimized is spread over agents of a network.
