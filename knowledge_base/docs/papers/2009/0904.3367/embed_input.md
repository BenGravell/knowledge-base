<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

NESTA: A Fast and Accurate First-order Method for Sparse Recovery

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Accurate signal recovery or image reconstruction from indirect and possibly undersampled data is a topic of considerable interest; for example, the literature in the recent field of compressed sensing is already quite immense. Inspired by recent breakthroughs in the development of novel first-order methods in convex optimization, most notably Nesterov's smoothing technique, this paper introduces a fast and accurate algorithm for solving common recovery problems in signal processing. In the spirit of Nesterov's work, one of the key ideas of this algorithm is a subtle averaging of sequences of iterates, which has been shown to improve the convergence properties of standard gradient-descent algorithms. This paper demonstrates that this approach is ideally suited for solving large-scale compressed sensing reconstruction problems as 1) it is computationally efficient, 2) it is accurate and returns solutions with several correct digits, 3) it is flexible and amenable to many kinds of reconstruction problems, and 4) it is robust in the sense that its excellent performance across a wide range of problems does not depend on the fine tuning of several parameters. Comprehensive numerical experiments on realistic signals exhibiting a large dynamic range show that this algorithm compares favorably with recently proposed state-of-the-art methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We also apply the algorithm to solve other problems for which there are fewer alternatives, such as total-variation minimization, and convex programs seeking to minimize the l1 norm of Wx under constraints, in which W is not diagonal.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Compressed sensing (CS) is a novel sampling theory, which is based on the revelation that one can exploit sparsity or compressibility when acquiring signals of general interest. In a nutshell, compressed sensing designs nonadaptive sampling techniques that condense the information in a compressible signal into a small amount of data. There are some indications that because of the significant reduction in the number of measurements needed to recover a signal accurately, engineers are changing the way they think about signal acquisition in areas ranging from analog-to-digital conversion, digital optics, magnetic resonance imaging, seismics and astronomy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this field, a signal $x^{0} \in {\mathbb{R}}^{n}$ is acquired by collecting data of the form where $x^{0}$ is the signal of interest (or its coefficient sequence in a representation where it is assumed to be fairly sparse), $A$ is a known $m \times n$ "sampling" matrix, and $z$ is a noise term. In compressed sensing and elsewhere, a standard approach attempts to reconstruct $x^{0}$ by solving where $\epsilon^{2}$ is an estimated upper bound on the noise power. The choice of the regularizing function $f$ depends on prior assumptions about the signal $x^{0}$ of interest: if $x^{0}$ is (approximately) sparse, an appropriate convex function is the $\ell_{1}$ norm (as advocated by the CS theory); if $x^{0}$ is a piecewise constant object, the total-variation norm provides accurate recovery results, and so.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Solving large-scale problems such as (think of $x^{0}$ as having millions of entries as in mega-pixel images) is challenging. Although one cannot review the vast literature on this subject, the majority of the algorithms that have been proposed are unable to solve these problems accurately with low computational complexity. On the one hand, standard second-order methods such as interior-point methods are accurate but problematic for they need to solve large systems of linear equations to compute the Newton steps. On the other hand, inspired by iterative thresholding ideas, we have now available a great number of first-order methods, see and the many earlier references therein, which may be faster but not necessarily accurate. Indeed, these methods are shown to converge slowly, and typically need a very large number of iterations when high accuracy is required.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We would like to pause on the demand for high accuracy since this is the main motivation of the present paper. While in some applications, one may be content with one or two digits of accuracy, there are situations in which this is simply unacceptable. Imagine that the matrix $A$ models a device giving information about the signal $x^{0}$, such as an analog-to-digital converter, for example. Here, the ability to detect and recover low-power signals that are barely above the noise floor, and possibly further obscured by large interferers, is critical to many applications. In mathematical terms, one could have a superposition of high power signals corresponding to components $x^{0}{\lbrack i\rbrack}$ of $x^{0}$ with magnitude of order 1, and low power signals with amplitudes as far as 100 dB down, corresponding to components with magnitude about $10^{- 5}$. In this regime of high-dynamic range, very high accuracy is required. In the example above, one would need at least five digits of precision as otherwise, the low power signals would go undetected.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another motivation is solving accurately when the signal $x^{0}$ is not exactly sparse, but rather approximately sparse, as in the case of real-world compressible signals. Since exactly sparse signals are rarely found in applications---while compressible signals are ubiquitous---it is important to have an accurate first-order method to handle realistic signals.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

A few years ago, Nesterov published a seminal paper which couples smoothing techniques (see and the references therein) with an improved gradient method to derive first-order methods which achieve a convergence rate he had proved to be optimal two decades earlier. As a consequence of this breakthrough, a few recent works have followed up with improved techniques for some very special problems in signal or image processing, see for example, or for minimizing composite functions such as $\ell_{1}$-regularized least-squares problems. In truth, these novel algorithms demonstrate great promise; they are fast, accurate and robust in the sense that their performance does not depend on the fine tuning of various controlling parameters.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper also builds upon Nesterov's work by extending some of his works discussed just above, and proposes an algorithm---or, better said, a class of algorithms---for solving recovery problems from incomplete measurements. We refer to this algorithm as NESTA---a shorthand for Nesterov's algorithm---to acknowledge the fact that it is based on his method. The main purpose and the contribution of this paper consist in showing that NESTA obeys the following desirable properties.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

Speed: NESTA is an iterative algorithm where each iteration is decomposed into three steps, each involving only a few matrix-vector operations when $A^{\ast}A$ is an orthogonal projector and, more generally, when the eigenvalues of $A^{\ast}A$ are well clustered. This, together with the accelerated convergence rate of Nesterov's algorithm, makes NESTA a method of choice for solving large-scale problems. Furthermore, NESTA's convergence is mainly driven by a single smoothing parameter $\mu$ introduced in Section 2. One can use continuation techniques to dynamically update this parameter to substantially accelerate this algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

Accuracy: NESTA depends on a few parameters that can be set in a very natural fashion. In fact, there is a trivial relationship between the value of these parameters and the desired accuracy. Furthermore, our numerical experiments demonstrate that NESTA can find the first 4 or 5 significant digits of the optimal solution to, where $f{(x)}$ is the $\ell_{1}$ norm or the total-variation norm of $x$, in a few hundred iterations. This makes NESTA amenable to solve recovery problems involving signals of very large sizes that also exhibit a great dynamic range.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

Flexibility: NESTA can be adapted to solve many problems beyond $\ell_{1}$ minimization with the same efficiency, such as total-variation (TV) minimization problems. In this paper, we will also discuss applications in which $f$ in is given by ${f{(x)}} = {\|{Wx}\|}_{\ell_{1}}$, where one may think of $W$ as a short-time Fourier transform also known as the Gabor transform, a curvelet transform, an undecimated wavelet transform and so, or a combination of these, or a general arbitrary dictionary of waveforms (note that this class of recovery problems also include weighted $\ell_{1}$ methods ). This is particularly interesting because recent work suggests the potential advantage of this analysis-based approach over the classical basis pursuit in solving important inverse problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

A consequence of these properties is that NESTA, and more generally Nesterov's method, may be of interest to researchers working in the broad area of signal recovery from indirect and/or undersampled data.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

Another contribution of this paper is that it also features a fairly wide range of numerical experiments comparing various methods against problems involving realistic and challenging data. By challenging, we mean problems of very large scale where the unknown solution exhibits a large dynamic range; that is, problems for which classical second-order methods are too slow, and for which standard first-order methods do not provide sufficient accuracy. More specifically, Section 5 presents a comprehensive series of numerical experiments which illustrate the behavior of several state-of-the-art methods including interior point methods, projected gradient techniques, fixed point continuation and iterative thresholding algorithms. It is important to consider that most of these methods have been perfected after several years of research, and did not exist two years ago. For example, the Fixed Point Continuation method with Active Set, which represents a notable improvement over existing ideas, was released while we were working on this paper.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Organization of the paper and notations", "weight": 1.0} -->

As emphasized earlier, NESTA is based on Nesterov's ideas and Section 2 gives a brief but essential description of Nesterov's algorithmic framework. The proposed algorithm is introduced in Section 3. Inspired by continuation-like schemes, an accelerated version of NESTA is described in Section 3.6. We report on extensive and comparative numerical experiments in Section 5. Section 6 covers extensions of NESTA to minimize the $\ell_{1}$ norm of $Wx$ under data constraints (Section 6.1), and includes realistic simulations in the field of radar pulse detection and estimation. Section 6.3 extends NESTA to solve total-variation problems and presents numerical experiments which also demonstrate its remarkable efficiency there as well. Finally, we conclude with Section 7 discussing further extensions, which would address an even wider range of linear inverse problems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Organization of the paper and notations", "weight": 1.0} -->

Notations. Before we begin, it is best to provide a brief summary of the notations used throughout the paper. As usual, vectors are written in small letters and matrices in capital letters. The $i$th entry of a vector $x$ is denoted $x{\lbrack i\rbrack}$ and the $(i,j)$th entry of the matrix $A$ is $A{\lbrack i,j\rbrack}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Organization of the paper and notations", "weight": 1.0} -->

It is convenient to introduce some common optimization problems that will be discussed throughout. Solving sparse reconstruction problems can be approached via several different equivalent formulations. In this paper, we particularly emphasize the quadratically constrained $\ell_{1}$-minimization problem where $\epsilon$ quantifies the uncertainty about the measurements $b$ as in the situation where the measurements are noisy. This formulation is often preferred because a reasonable estimate of $\epsilon$ may be known. A second frequently discussed approach considers solving this problem in Lagrangian form, i.e. and is also known as the basis pursuit denoising problem (BPDN). This problem is popular in signal and image processing because of its loose interpretation as a maximum a posteriori estimate in a Bayesian setting. In statistics, the same problem is more well-known as the lasso Standard optimization theory asserts that these three problems are of course equivalent provided that $\epsilon,\lambda,\tau$ obey some special relationships. With the exception of the case where the matrix $A$ is orthogonal, this functional dependence is hard to compute.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Organization of the paper and notations", "weight": 1.0} -->

Because it is usually more natural to determine an appropriate $\epsilon$ rather than an appropriate $\lambda$ or $\tau$, the fact that NESTA solves ($\text{BP}_{\epsilon}$) is a significant advantage. Further, note that theoretical equivalence of course does not mean that all three problems are just as easy (or just as hard) to solve. For instance, the constrained problem ($\text{BP}_{\epsilon}$) is harder to solve than ($\text{QP}_{\lambda}$), as discussed in Section 5.2. Therefore, the fact that NESTA turns out to be competitive with algorithms that only solve ($\text{QP}_{\lambda}$) is quite remarkable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Minimizing smooth convex functions", "weight": 1.0} -->

In, Nesterov introduces a subtle algorithm to minimize any smooth convex function $f$ on the convex set $\mathcal{Q}_{p}$, We will refer to $\mathcal{Q}_{p}$ as the primal feasible set. The function $f$ is assumed to be differentiable and its gradient ${\nabla f}{(x)}$ is Lipschitz and obeys in short, $L$ is an upper bound on the Lipschitz constant. With these assumptions, Nesterov's algorithm minimizes $f$ over $\mathcal{Q}_{p}$ by iteratively estimating three sequences $\{ x_{k}\}$, $\{ y_{k}\}$ and $\{ z_{k}\}$ while smoothing the feasible set $\mathcal{Q}_{p}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Minimizing smooth convex functions", "weight": 1.0} -->

The algorithm depends on two scalar sequences $\{\alpha_{k}\}$ and $\{\tau_{k}\}$ discussed below, and takes the following form: At step $k$, $y_{k}$ is the current guess of the optimal solution. If we only performed the second step of the algorithm with $y_{k - 1}$ instead of $x_{k}$, we would obtain a standard first-order technique with convergence rate $\mathcal{O}{({1/k})}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Minimizing smooth convex functions", "weight": 1.0} -->

The novelty is that the sequence $z_{k}$ "keeps in mind" the previous iterations since Step 3 involves a weighted sum of already computed gradients. Another aspect of this step is that---borrowing ideas from smoothing techniques in optimization ---it makes use of a prox-function $p_{p}{(x)}$ for the primal feasible set $Q_{p}$. This function is strongly convex with parameter $\sigma_{p}$; assuming that $p_{p}{(x)}$ vanishes at the prox-center $x_{p}^{c} = {\text{argmin}_{x}{p_{p}{(x)}}}$, this gives The prox-function is usually chosen so that $x_{p}^{c} \in \mathcal{Q}_{p}$, thus discouraging $z_{k}$ from moving too far away from the center $x_{p}^{c}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Minimizing smooth convex functions", "weight": 1.0} -->

The point $x_{k}$, at which the gradient of $f$ is evaluated, is a weighted average between $z_{k}$ and $y_{k}$. In truth, this is motivated by a theoretical analysis, which shows that if $\alpha_{k} = {{1/2}{({k + 1})}}$ and $\tau_{k} = {2/{({k + 3})}}$, then the algorithm converges to with the convergence rate This decay is far better than what is achievable via standard gradient-based optimization techniques since we have an approximation scaling like $L/k^{2}$ instead of $L/k$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Minimizing nonsmooth convex functions", "weight": 1.0} -->

In an innovative paper, Nesterov recently extended this framework to deal with nonsmooth convex functions. Assume that $f$ can be written as where $x \in {\mathbb{R}}^{n}$, $u \in {\mathbb{R}}^{p}$ and $W \in {\mathbb{R}}^{p \times n}$. We will refer to $\mathcal{Q}_{d}$ as the dual feasible set, and suppose it is convex.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Minimizing nonsmooth convex functions", "weight": 1.0} -->

This assumption holds for all of the problems of interest in this paper---we will see in Section 3 that this holds for ${\| x\|}_{\ell_{1}}$, ${\|{Wx}\|}_{\ell_{1}}$, the total-variation norm and, in general, for any induced norm---yet it provides enough information beyond the black-box model to allow cleverly-designed methods with a convergence rate scaling like $\mathcal{O}{({1/k^{2}})}$ rather than $\mathcal{O}{({1/\sqrt{k}})}$, in the number of steps $k$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Minimizing nonsmooth convex functions", "weight": 1.0} -->

With this formulation, the minimization can be recast as the following saddle point problem: The point is that $f$ is convex but generally nonsmooth. In, Nesterov proposed substituting $f$ by the smooth approximation where $p_{d}{(u)}$ is a prox-function for $\mathcal{Q}_{d}$; that is, $p_{d}{(u)}$ is continuous and strongly convex on $\mathcal{Q}_{d}$, with convexity parameter $\sigma_{d}$ (we shall assume that $p_{d}$ vanishes at some point in $\mathcal{Q}_{d}$). Nesterov proved that $f_{\mu}$ is continuously differentiable, and that its gradient obeys where $u_{\mu}{(x)}$ is the optimal solution of. Furthermore, $\nabla f_{\mu}$ is shown to be Lipschitz with constant ($\| W\|$ is the operator norm of $W$).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Minimizing nonsmooth convex functions", "weight": 1.0} -->

Nesterov's algorithm can then be applied to $f_{\mu}{(x)}$ as proposed. For a fixed $\mu$, the algorithm converges in $\mathcal{O}{({1/k^{2}})}$ iterations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Minimizing nonsmooth convex functions", "weight": 1.0} -->

If we describe convergence in terms of the number of iterations needed to reach an $\varepsilon$ solution (that is, the number of steps is taken to produce an $x$ obeying ${|{{f_{\mu}{(x)}} - {\min f_{\mu}}}|} < \varepsilon$), then because $\mu$ is approximately proportional to the accuracy of the approximation, and because $L_{\mu}$ is proportional to ${1/\mu} \approx {1/\varepsilon}$, the rate of convergence is ${\mathcal{O}{(\sqrt{L_{\mu}/\varepsilon})}} \approx {\mathcal{O}{({1/\varepsilon})}}$, a significant improvement over the sub-gradient method which has rate $\mathcal{O}{({1/\varepsilon^{2}})}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Extension to Compressed Sensing", "weight": 1.0} -->

We now extend Nesterov's algorithm to solve compressed sensing recovery problems, and refer to this extension as NESTA. For now, we shall be concerned with solving the quadratically constrained $\ell_{1}$ minimization problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "NESTA", "weight": 1.0} -->

In this section, we assume that $A^{\ast}A$ is an orthogonal projector, i.e. the rows of $A$ are orthonormal. This is often the case in compressed sensing applications where it is common to take $A$ as a submatrix of a unitary transformation which admits a fast algorithm for matrix-vector products; special instances include the discrete Fourier transform, the discrete cosine transform, the Hadamard transform, the noiselet transform, and so. Basically, collecting incomplete structured orthogonal measurements is the prime method for efficient data acquisition in compressed sensing.

<!-- chunk {"id": "body-0031", "role": "body", "section": "NESTA", "weight": 1.0} -->

Recall that the $\ell_{1}$ norm is of the form where the dual feasible set is the $\ell_{\infty}$ ball Therefore, a natural smooth approximation to the $\ell_{1}$ norm is where $p_{d}{(u)}$ is our dual prox-function. For $p_{d}{(u)}$, we would like a strongly convex function, which is known analytically and takes its minimum value (equal to zero) at some $u_{d}^{c} \in \mathcal{Q}_{d}$. It is also usual to have $p_{d}{(u)}$ separable. Taking these criteria into account, a convenient choice is ${p_{d}{(u)}} = {\frac{1}{2}{\| u\|}_{\ell_{2}}^{2}}$ whose strong convexity parameter $\sigma_{d}$ is equal to $1$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "NESTA", "weight": 1.0} -->

With this prox-function, $f_{\mu}$ is the well-known Huber function and $\nabla f_{\mu}$ is Lipschitz with constant $1/\mu$.^11^1In the case of total-variation minimization in which ${f{(x)}} = {\| x\|}_{TV}$, $f_{\mu}$ is not a known function. In particular, ${\nabla f_{\mu}}{(x)}$ is given by Following Nesterov, we need to solve the smooth constrained problem where $\mathcal{Q}_{p} = \left\{ x:{{\|{b - {Ax}}\|}_{\ell_{2}} \leq \epsilon} \right\}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "NESTA", "weight": 1.0} -->

Once the gradient of $f_{\mu}$ at $x_{k}$ is computed, Step $2$ and Step $3$ of NESTA consist in updating two auxiliary iterates, namely, $y_{k}$ and $z_{k}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Updating $y_{k}$", "weight": 1.0} -->

To compute $y_{k}$, we need to solve where $x_{k}$ is given. The Lagrangian for this problem is of course and at the primal-dual solution $(y_{k},\lambda_{\epsilon})$, the Karush-Kuhn-Tucker (KKT) conditions read From the stationarity condition, $y_{k}$ is the solution to the linear system As discussed earlier, our assumption is that $A^{\ast}A$ is an orthogonal projector so that In this case, computing $y_{k}$ is cheap since no matrix inversion is required---only a few matrix-vector products are necessary. Moreover, from the KKT conditions, the value of the optimal Lagrange multiplier is obtained explicitly, and equals Observe that this can be computed beforehand since it only depends on $x_{k}$ and ${\nabla f_{\mu}}{(x_{k})}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Updating $z_{k}$", "weight": 1.0} -->

To compute $z_{k}$, we need to solve where $p_{p}{(x)}$ is the primal prox-function. The point $z_{k}$ differs from $y_{k}$ since it is computed from a weighted cumulative gradient $\sum_{i \leq k}{\alpha_{i}{\nabla f_{\mu}}{(x_{i})}}$, making it less prone to zig-zagging, which typically occurs when we have highly elliptical level sets. This step keeps a memory from the previous steps and forces $z_{k}$ to stay near the prox-center.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Updating $z_{k}$", "weight": 1.0} -->

A good primal prox-function is a smooth and strongly convex function that is likely to have some positive effect near the solution. In the setting of, a suitable smoothing prox-function may be for some $x_{0} \in {\mathbb{R}}^{n}$, e.g. an initial guess of the solution. Other choices of primal feasible set $\mathcal{Q}_{p}$ may lead to other choices of prox-functions. For instance, when $\mathcal{Q}_{p}$ is the standard simplex, choosing an entropy distance for $p_{p}{(x)}$ is smarter and more efficient, see. In this paper, the primal feasible set is quadratic, which makes the Euclidean distance a reasonable choice. What is more important, however, is that this choice allows very efficient computations of $y_{k}$ and $z_{k}$ while other choices may considerably slow down each Nesterov iteration.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Updating $z_{k}$", "weight": 1.0} -->

Finally, notice that the bound on the error at iteration $k$ in is proportional to $p_{p}{(x^{\star})}$; choosing $x_{0}$ wisely (a good first guess) can make $p_{p}{(x^{\star})}$ small. When nothing is known about the solution, a natural choice may be $x_{0} = {A^{\ast}b}$; this idea will be developed in Section 3.6.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Updating $z_{k}$", "weight": 1.0} -->

With, the strong convexity parameter of $p_{p}{(x)}$ is equal to $1$, and to compute $z_{k}$ we need to solve for some value of $\lambda$. Just as before, the solution is given by with a value of the Lagrange multiplier equal to In practice, the instances ${\{{{\nabla f_{\mu}}{(x_{i})}}\}}_{i \leq k}$ have not to be stored; one just has to store the cumulative gradient $\sum_{i \leq k}{\alpha_{i}{\nabla f_{\mu}}{(x_{i})}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

The computational complexity of each of NESTA's step is clear. In large-scale problems, most of the work is in the application of $A$ and $A^{\ast}$. Put $\mathcal{C}_{A}$ for the complexity of applying $A$ or $A^{\ast}$. The first step, namely, computing $\nabla f_{\mu}$, only requires vector operations whose complexity is $\mathcal{O}{(n)}$. Step $2$ and $3$ require the application of $A$ or $A^{\ast}$ three times each (we only need to compute $A^{\ast}b$ once). Hence, the total complexity of a single NESTA iteration is ${6\mathcal{C}_{A}} + {\mathcal{O}{(n)}}$ where $\mathcal{C}_{A}$ is dominant.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

The calculation above are in some sense overly pessimistic. In compressed sensing applications, it is common to choose $A$ as a submatrix of a unitary transformation $U$, which admits a fast algorithm for matrix-vector products. In the sequel, it might be useful to think of $A$ as a subsampled DFT. In this case, letting $R$ be the $m \times n$ matrix extracting the observed measurements, we have $A = {RU}$. The trick then is to compute in the $U$-domain directly. Making the change of variables $x\leftarrow{Ux}$, our problem is where ${\hat{f}}_{\mu} = {f_{\mu} \circ U^{\ast}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

Put $\mathcal{C}_{U}$ for the complexity of applying $U$ and $U^{\ast}$. The complexity of Step $1$ is now $2\mathcal{C}_{U}$, so that this simple change of variables reduces the cost of each NESTA iteration to ${2\mathcal{C}_{U}} + {\mathcal{O}{(n)}}$. For example, in the case of a subsampled DFT (or something similar), the cost of each iteration is essentially that of two FFTs. Hence, each iteration is extremely fast.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

NESTA involves the selection of a single smoothing parameter $\mu$ and of a suitable stopping criterion. For the latter, our experience indicates that a robust and fairly natural stopping criterion is to terminate the algorithm when the relative variation of $f_{\mu}$ is small. Define $\Deltaf_{\mu}$ as Then convergence is claimed when for some $\delta > 0$. In our experiments, $\delta \in {\{ 10^{- 5},10^{- 6},10^{- 7},10^{- 8}\}}$ depending upon the desired accuracy.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Parameter selection", "weight": 1.0} -->

The choice of $\mu$ is based on a trade-off between the accuracy of the smoothed approximation $f_{\mu}$ (basically, ${\lim_{\mu\rightarrow 0}{f_{\mu}{(x)}}} = {\| x\|}_{\ell_{1}}$) and the speed of convergence (the convergence rate is proportional to $\mu$). With noiseless data, $\mu$ is directly linked to the desired accuracy. To illustrate this, we have observed in that when the true signal $x^{0}$ is exactly sparse and is actually the minimum solution under the equality constraints ${Ax^{0}} = b$, the $\ell_{\infty}$ error on the nonzero entries is on the order of $\mu$. The link between $\mu$ and accuracy will be further discussed in Section 4.3.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

Inspired by homotopy techniques which find the solution to the lasso problem for values of $\tau$ ranging in an interval $\lbrack 0,\tau_{\max}\rbrack$, introduces a fixed point continuation technique which solves $\ell_{1}$-penalized least-square problems for values of $\lambda$ obeying $0 < \lambda < {\|{A^{\ast}b}\|}_{\ell_{\infty}}$. The continuation solution approximately follows the path of solutions to the problem $(\text{QP}_{\lambda})$ and, hence, the solutions to and may be found by solving a sequence a $\ell_{1}$ penalized least-squares problems.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

The point of this is that it has been noticed (see ) that solving (resp. the lasso ) is faster when $\lambda$ is large (resp. $\tau$ is low). This observation greatly motivates the use of continuation for solving for a fixed $\lambda_{f}$. The idea is simple: propose a sequence of problems with decreasing values of the parameter $\lambda$, $\lambda_{0} > \cdots > \lambda_{f}$, and use the intermediate solution as a warm start for the next problem. This technique has been used with some success. Continuation has been shown to be a very successful tool to increase the speed of convergence, in particular when dealing with large-scale problems and high dynamic range signals.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

Likewise, our proposed algorithm can greatly benefit from a continuation approach. Recall that to compute $y_{k}$, we need to solve for some vector $c$. Thus with $\mathcal{P}_{\mathcal{Q}_{p}}$ the projector onto $\mathcal{Q}_{p}$, $y_{k} = {\mathcal{P}_{\mathcal{Q}_{p}}{({x_{k} - {L_{\mu}^{- 1}c}})}}$. Now two observations are in order.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

Computing $y_{k}$ is similar to a projected gradient step as the Lipschitz constant $L_{\mu}^{- 1}$ plays the role of the step size. Since $L_{\mu}$ is proportional to $\mu^{- 1}$, the larger $\mu$, the larger the step-size, and the faster the convergence. This also applies to the sequence $\{ z_{k}\}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

For a fixed value of $\mu$, the convergence rate of the algorithm obeys where $x_{\mu}^{\star}$ is the optimal solution to $\min f_{\mu}$ over $\mathcal{Q}_{p}$. On the one hand, the convergence rate is proportional to $\mu^{- 1}$, so a large value of $\mu$ is beneficial. On the other hand, choosing a good guess $x_{0}$ close to $x_{\mu}^{\star}$ provides a low value of ${p_{p}{(x_{\mu}^{\star})}} = {\frac{1}{2}{\|{x_{\mu}^{\star} - x_{0}}\|}_{\ell_{2}}^{2}}$, also improving the rate of convergence. Warm-starting with $x_{0}$ from a previous solve not only changes the starting point of the algorithm, but it beneficially changes $p_{p}$ as well.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

These two observations motivate the following continuation-like algorithm: This algorithm iteratively finds the solutions to a succession of problems with decreasing smoothing parameters $\mu_{0} > \cdots > \mu_{f} = {\gamma^{T}\mu_{0}}$ producing a sequence of---hopefully--- finer estimates of $x_{\mu_{f}}^{\star}$; these intermediate solutions are cheap to compute and provide a string of convenient first guess for the next problem. In practice, they are solved with less accuracy, making them even cheaper to compute.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

The value of $\mu_{f}$ is based on a desired accuracy as explained in Section 3.5. As for an initial value $\mu_{0}$, makes clear that the smoothing parameter plays a role similar to a threshold. A first choice may then be $\mu_{0} = {0.9{\|{A^{\ast}b}\|}_{\ell_{\infty}}}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

We illustrate the good behavior of the continuation-inspired algorithm by applying NESTA with continuation to solve a sparse reconstruction problem from partial frequency data. In this series of experiments, we assess the performance of NESTA while the dynamic range of the signals to be recovered increases.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

The signals $x$ are $s$-sparse signals---that is, have exactly $s$ nonzero components---of size $n = 4096$ and $s = {m/40}$. Put $\Lambda$ for the indices of the nonzero entries of $x$; the amplitude of each nonzero entry is distributed uniformly on a logarithmic scale with a fixed dynamic range. Specifically, each nonzero entry is generated as follows: where ${\eta_{1}{\lbrack i\rbrack}} = {\pm 1}$ with probability $1/2$ (a random sign) and $\eta_{2}{\lbrack i\rbrack}$ is uniformly distributed in $\lbrack 0,1\rbrack$. The parameter $\alpha$ quantifies the dynamic range. Unless specified otherwise, a dynamic range of $d$ dB means that $\alpha = {d/20}$ (since for large signals $\alpha$ is approximately the logarithm base 10 of the ratio between the largest and the lowest magnitudes).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

For instance, 80 dB signals are generated according to with $\alpha = 4$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

The measurements $Ax$ consist of $m = {n/8}$ random discrete cosine measurements so that $A^{\ast}A$ is diagonalized by the DCT. Finally, $b$ is obtained by adding a white Gaussian noise term with standard deviation $\sigma = 0.1$. The initial value of the smoothing parameter is $\mu_{0} = {\|{A^{\ast}b}\|}_{\ell_{\infty}}$ and the terminal value is $\mu_{f} = {2\sigma}$. The algorithm terminates when the relative variation of $f_{\mu}$ is lower than $\delta = 10^{- 5}$. NESTA with continuation is applied to 10 random trials for varying number of continuation steps $T$ and various values of the dynamic range. Figure 1 graphs the value of $f_{\mu_{f}}$ while applying NESTA with and without continuation as a function of the iteration count. The number of continuation steps is set to $T = 4$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

One can observe that computing the solution to $\min f_{\mu_{f}}$ (solid line) takes a while when computed with the final value $\mu_{f}$; notice that NESTA seems to be slow at the beginning (number of iterations lower than 15). In the meantime NESTA with continuation rapidly estimates a sequence of coarse intermediate solutions that converges to the solution to $\min f_{\mu_{f}}$ In this case, continuation clearly enhances the global speed of convergence with a factor $10$. Figure 2 provides deeper insights into the behavior of continuation with NESTA and shows the number of iterations required to reach convergence for varying values of the continuation steps $T$ for different values of the dynamic range.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

When the ratio $\mu_{0}/\mu_{f}$ is low or when the required accuracy is low, continuation is not as beneficial: intermediate continuation steps require a number of iterations which may not speed up overall convergence. The stepsize which is about $L_{\mu_{f}}^{- 1}$ works well in this regime. When the dynamic range increases and we require more accuracy, however, the ratio $\mu_{0}/\mu_{f}$ is large, since $\mu_{0} = {\|{A^{\ast}b}\|}_{\ell_{\infty}}} \approx {\| x\|}_{\ell_{\infty}} \gg \sigma$, and continuation provides considerable improvements. In this case, the step size $L_{\mu_{f}}^{- 1}$ is too conservative and it takes a while to find the large entries of $x$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

Empirically, when the dynamic range is $100$ dB, continuation improves the speed of convergence by a factor of $8$. As this factor is likely to increase exponentially with the dynamic range (when expressed in dB), NESTA with continuation seems to be a better candidate for solving sparse reconstruction problems with high accuracy.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Accelerating NESTA with continuation", "weight": 1.0} -->

Interestingly, the behavior of NESTA with continuation seems to be quite stable: increasing the number of continuation steps does not increase dramatically the number of iterations. In practice, although the ideal $T$ is certainly signal dependent, we have observed that choosing $T \in {\{ 4,5,6\}}$ leads to reasonable results.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Some theoretical considerations", "weight": 1.0} -->

The convergence of NESTA with and without continuation is straightforward. The following theorem states that each continuation step with $\mu = \mu^{(t)}$ converges to $x_{\mu}^{\star}$. Global convergence is proved by applying this theorem to $t = T$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Accurate Optimization", "weight": 1.0} -->

A significant fraction of the numerical part of this paper focuses on comparing different sparse recovery algorithms in terms of speed and accuracy. In this section, we first demonstrate that NESTA can easily recover the exact solution to $(\text{BP}_{\epsilon})$ with a precision of 5 to 6 digits. Speaking of precision, we shall essentially use two criteria to evaluate accuracy.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Accurate Optimization", "weight": 1.0} -->

The first is the (relative) error on the objective functional where $x^{\star}$ is the optimal solution to $(\text{BP}_{\epsilon})$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Accurate Optimization", "weight": 1.0} -->

The second is the accuracy of the optimal solution itself and is measured via which gives a precise value of the accuracy per entry.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Is NESTA accurate?", "weight": 1.0} -->

For general problem instances, the exact solution to $(\text{BP}_{\epsilon})$ (or equivalently $(\text{QP}_{\lambda})$) cannot be computed analytically. Under some conditions, however, a simple formula is available when the optimal solution has exactly the same support and the same sign as the unknown (sparse) $x^{0}$ (recall the model $b = {{Ax^{0}} + z}$). Denote by $I$ the support of $x^{0}$, $I:={\{ i:{{|{x^{0}{\lbrack i\rbrack}}|} > 0}\}}$. Then if $x^{0}$ is sufficiently sparse and if the nonzero entries of $x^{0}$ are sufficiently large, the solution $x^{\star}$ to $(\text{QP}_{\lambda})$ is given by see for example.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Is NESTA accurate?", "weight": 1.0} -->

In this expression, $x{\lbrack I\rbrack}$ is the vector with indices in $I$ and $A{\lbrack I\rbrack}$ is the submatrix with columns indices in $I$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Is NESTA accurate?", "weight": 1.0} -->

To evaluate NESTA's accuracy, we set $n = {262,144}$, $m = {n/8}$, and $s = {m/100}$ (this is the number of nonzero coordinates of $x_{0}$). The absolute values of the nonzero entries of $x_{0}$ are distributed between $1$ and $10^{5}$ so that we have about $100$ dB of dynamic range. The measurements $Ax^{0}$ are discrete cosine coefficients selected uniformly at random. We add Gaussian white noise with standard deviation $\sigma = 0.01$. We then compute the solution, and make sure it obeys the KKT optimality conditions for $(\text{QP}_{\lambda})$ so that the optimal solution is known.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Is NESTA accurate?", "weight": 1.0} -->

Rel. error ℓ1-norm Table 1: Assessing FISTA’s and NESTA’s accuracy when the optimal solution is known. The relative error on the optimal value is given by and the ℓ∞ error on the optimal solution. 𝒩A is the number of calls to A or A* to compute the solution.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Is NESTA accurate?", "weight": 1.0} -->

We run NESTA with continuation with the value of $\epsilon:={\|{b - {Ax^{\star}}}\|}$. We use $\mu = 0.02$, $\delta = 10^{- 7}$ and the number of continuation steps is set to $5$. Table 1 reports on numerical results. First, the value of the objective functional is accurate up to $4$ digits. Second, the computed solution is very accurate since we observe an $\ell_{\infty}$ error of $0.08$. Now recall that the nonzero components of $x^{\star}$ vary from about $1$ to $10^{5}$ so that we have high accuracy over a huge dynamic range. This can also be gleaned from Figure 4 which plots NESTA's solution versus the optimal solution, and confirms the excellent precision of our algorithm.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Setting up a reference algorithm for accuracy tests", "weight": 1.0} -->

In general situations, a formula for the optimal solution is of course unavailable, and evaluating the accuracy of solutions requires defining a method of reference. In this paper, we will use FISTA as such a reference since it is an efficient algorithm that also turns out to be extremely easy to use; in particular, no parameter has to be tweaked, except for the standard stopping criterion (maximum number of iterations and tolerance on the relative variation of the objective function).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Setting up a reference algorithm for accuracy tests", "weight": 1.0} -->

We run FISTA with $20,000$ iterations on the same problem as above, and report its accuracy in Table 1. The $\ell_{1}$-norm is exact up to $4$ digits. Furthermore, Figure 4 shows the entries of FISTA's solution versus those of the optimal solution, and one observes a very good fit (near perfect when the magnitude of a component of $x^{\star}$ is higher than $3$). The $\ell_{\infty}$ error between FISTA's solution and the optimal solution $x^{\star}$ is equal to $0.31$; that is, the entries are exact up to $\pm 0.31$. Because this occurs over an enormous dynamic range, we conclude that FISTA also gives very accurate solutions provided that sufficiently many iterations are taken.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Setting up a reference algorithm for accuracy tests", "weight": 1.0} -->

We have observed that running FISTA with a high number of iterations---typically greater than $20,000$---provides accurate solutions to $(\text{QP}_{\lambda})$, and this is why we will use it as our method of reference in the forthcoming comparisons from this section and the next.

<!-- chunk {"id": "body-0071", "role": "body", "section": "The smoothing parameter $\\mu$ and NESTA's accuracy", "weight": 1.0} -->

By definition, $\mu$ fixes the accuracy of the approximation $f_{\mu}$ to the $\ell_{1}$ norm and, therefore, NESTA's accuracy directly depends on this parameter. We now propose to assess the accuracy of NESTA for different values of $\mu$. The problem sizes are as before, namely, $n = {262,144}$ and $m = {n/8}$, except that now the unknown $x^{0}$ is far less sparse with $s = {m/5}$. The standard deviation of the additive Gaussian white noise is also higher, and we set $\sigma = 0.1$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The smoothing parameter $\\mu$ and NESTA's accuracy", "weight": 1.0} -->

Because of the larger value of $s$ and $\sigma$, it is no longer possible to have an analytic solution. Instead, we use FISTA to compute a reference solution $x_{F}$, using $20,000$ iterations and with $\lambda = 0.0685$, which gives ${\|{b - {Ax_{F}}}\|}_{\ell_{2}}^{2} \simeq {{({m + {2\sqrt{2m}}})}\sigma^{2}}$. To be sure that FISTA's solution is very close to the optimal solution, we check that the KKT stationarity condition is nearly verified. If $I_{\star}$ is the support of the optimal solution $x^{\star}$, this condition reads Now define $I$ to be the support of $x_{F}$. Then, here, $x_{F}$ obeys This shows that $x_{F}$ is extremely close to the optimal solution.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The smoothing parameter $\\mu$ and NESTA's accuracy", "weight": 1.0} -->

NESTA is run with $T = 5$ continuation steps for three different values of $\mu \in {\{ 0.2,0.02,0.002\}}$ (the tolerance $\delta$ is set to $10^{- 6}$, $10^{- 7}$ and $10^{- 8}$ respectively). Figure 5 plots the solutions given by NESTA versus the "optimal solution" $x_{F}$. Clearly, when $\mu$ decreases, the accuracy of NESTA increases just as expected. More precisely, notice in Table 2 that for this particular experiment, decreasing $\mu$ by a factor of $10$ gives about $1$ additional digit of accuracy on the optimal value.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The smoothing parameter $\\mu$ and NESTA's accuracy", "weight": 1.0} -->

Rel. error ℓ1-norm Table 2: NESTA’s accuracy. The errors and number of function calls 𝒩A have the same meaning as in Table 1.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The smoothing parameter $\\mu$ and NESTA's accuracy", "weight": 1.0} -->

According to this table, $\mu = 0.02$ seems a reasonable choice to guarantee an accurate solution since one has between $4$ and $5$ digits of accuracy on the optimal value, and since the $\ell_{\infty}$ error is lower than $1$. Observe that this value separates the nonzero entries from the noise floor (when $\sigma = 0.01$). In the extensive numerical experiments of Section 5, we shall set $\mu = 0.02$ and $\delta = 10^{- 7}$ as default values.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Numerical comparisons", "weight": 1.0} -->

This section presents numerical experiments comparing several state-of-the-art optimization techniques designed to solve or. To be as fair as possible, we propose comparisons with methods for which software is publicly available online. To the best of our knowledge, such extensive comparisons are currently unavailable. Moreover, whereas publications sometimes test algorithms on relatively easy and academic problems, we will subject optimization methods to hard but realistic $\ell_{1}$ reconstruction problems.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Numerical comparisons", "weight": 1.0} -->

In our view, a challenging problem involves some or all of the characteristics below.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Numerical comparisons", "weight": 1.0} -->

High dynamic range. As mentioned earlier, most optimization techniques are able to find (more or less rapidly) the most significant entries (those with a large amplitude) of the signal $x$. Recovering the entries of $x$ that have low magnitudes accurately is more challenging.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Numerical comparisons", "weight": 1.0} -->

Approximate sparsity. Realistic signals are seldom exactly sparse and, therefore, coping with approximately sparse signals is of paramount importance. In signal or image processing for example, wavelet coefficients of natural images contain lots of low level entries that are worth retrieving.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Numerical comparisons", "weight": 1.0} -->

Large scale. Some standard optimization techniques, such as interior point methods, are known to provide accurate solutions. However, these techniques are not applicable to large-scale problems due to the large cost of solving linear systems. Further, many existing software packages fail to take advantage of fast-algorithms for applying $A$. We will focus on large-scale problems in which the number of unknowns $n$ is over a quarter of a million, i.e. $n = {262,144}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "State-of-the-art methods", "weight": 1.0} -->

Most of the algorithms discussed in this section are considered to be state-of-art in the sense that they are the most competitive among sparse reconstruction algorithms. To repeat ourselves, many of these methods have been improved after several years of research, and many did not exist two years ago. For instance, was submitted for publication less than three months before we put the final touches on this paper. Finally, our focus is on rapid algorithms so that we are interested in methods which can take advantage of fast algorithms for applying $A$ to a vector. This is why we have not tested other good methods such as, for example.

<!-- chunk {"id": "body-0082", "role": "body", "section": "NESTA", "weight": 1.0} -->

Below, we applied NESTA with the following default parameters (recall that $x_{0}$ is the initial guess). The maximal number of iterations is set to $\mathcal{I}_{\max} = {10,000}$; if convergence is not reached after $\mathcal{I}_{\max}$ iterations, we record that the algorithm did not convergence (DNC). Because NESTA requires 2 calls to either $A$ or $A^{\ast}$ per iteration, this is equivalent to declaring DNC after $\mathcal{N}_{A} = {20,000}$ iterations where $\mathcal{N}_{A}$ refers to the total number of calls to $A$ or $A^{\ast}$; hence, for the other methods, we declare DNC when $\mathcal{N}_{A} > {20,000}$. When continuation is used, extra parameters are set up as follows: and for $t = {1,\ldots,T}$, Numerical results are reported and discussed in Section 5.4.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Gradient Projections for Sparse Reconstruction (GPSR)", "weight": 1.0} -->

GPSR has been introduced in to solve the standard $\ell_{1}$ minimization problem in Lagrangian form ($\text{QP}_{\lambda}$). GPSR is based on the well-known projected gradient step technique, for some projector $\mathcal{P}_{\mathcal{Q}}$ onto a convex set $\mathcal{Q}$; this set contains the variable of interest $v$. In this equation, $F$ is the function to be minimized. In GPSR, the problem is recast such that the variable $v = {\lbrack v_{1},v_{2}\rbrack}$ has positive entries and $x = {v_{1} - v_{2}}$ (a standard change of variables in linear programming methods).

<!-- chunk {"id": "body-0084", "role": "body", "section": "Gradient Projections for Sparse Reconstruction (GPSR)", "weight": 1.0} -->

The function $F$ is then where $\underset{¯}{1}$ is the vector of ones, and $v$ belongs to the nonnegative orthant, ${v{\lbrack i\rbrack}} \geq 0$ for all $i$. The projection onto $\mathcal{Q}$ is then trivial. Different techniques for choosing the step-size $\alpha_{k}$ (backtracking, Barzilai-Borwein, and so on) are discussed. The code is available at In the forthcoming experiments, the parameters are set to their default values.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Gradient Projections for Sparse Reconstruction (GPSR)", "weight": 1.0} -->

GPSR also implements continuation, and we test this version as well. All parameters were set to defaults except, per the recommendation of one of the GPSR authors to increase performance, the number of continuation steps was set to 40, the ToleranceA variable was set to $10^{- 3}$, and the MiniterA variable was set to $1$. In addition, the code itself was tweaked a bit; in particular, the stopping criteria for continuation steps (other than the final step) was changed. Future releases of GPSR will probably contain a similarly updated continuation stopping criteria.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Sparse reconstruction by separable approximation (SpaRSA)", "weight": 1.0} -->

SpaRSA is an algorithm to minimize composite functions ${\phi{(x)}} = {{f{(x)}} + {\lambdac{(x)}}}$ composed of a smooth term $f$ and a separable non-smooth term $c$, e.g. ($\text{QP}_{\lambda}$). At every step, a subproblem of the form with optimization variable $x$ must be solved; this is the same as computing the proximity operator corresponding to $c$. For ($\text{QP}_{\lambda}$), the solution is given by shrinkage. In this sense, SpaRSA is an iterative shrinkage/thresholding (IST) algorithm, much like FISTA (though without the accelerated convergence) and FPC. Also like FPC, continuation is used to speed convergence, and like FPC-BB, a Barzilai-Borwein heuristic is used for the step size $\alpha$ (instead of using a pessimistic bound like the Lipschitz constant).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Sparse reconstruction by separable approximation (SpaRSA)", "weight": 1.0} -->

With this choice, SpaRSA is not guaranteed to be monotone, which can be remedied by implementing an appropriate safeguard, although this is not done in practice because there is little experimental advantage to doing so. Code for SpaRSA may be obtained at Parameters were set to default except the number of continuation steps was set to 40 and the MiniterA variable was set to 1 (instead of the default 5), as per the recommendations of one of the SpaRSA authors---again, as to increase performance.

<!-- chunk {"id": "body-0088", "role": "body", "section": "$\\ell_{1}$ regularized least squares (l1_ls)", "weight": 1.0} -->

This method solves the standard unconstrained $\ell_{1}$ minimization problem, and is an interior point method (with log-barrier) using preconditioned conjugate gradient (PCG) to accelerate convergence and stabilize the algorithm. The preconditioner used in the PCG step is a linear combination of the diagonal approximation of the Hessian of the quadratic term and of the Hessian of the log-barrier term. l1_ls is shown to be faster than usual interior point methods; nevertheless, each step requires solving a linear system of the form ${H\Deltax} = g$. Even if PCG makes the method more reliable, l1_ls is still problematic for large-scale problems. In the next comparisons, we provide some typical values of its computational complexity compared to the other methods. The code is available at

<!-- chunk {"id": "body-0089", "role": "body", "section": "Spectral projected gradient (SPGL1)", "weight": 1.0} -->

In 2008, van den Berg et al. adapted the spectral projection gradient algorithm introduced in to solve the LASSO ($\text{LS}_{\tau}$). Interestingly, they introduced a clever root finding procedure such that solving a few instances of $(\text{LS}_{\tau})$ for different values of $\tau$ enables them to equivalently solve ($\text{BP}_{\epsilon}$). Furthermore, if the algorithm detects a nearly-sparse solution, it defines an active set and solves an equation like on this active set. In the next experiments, the parameters are set to their default values. The code is available at

<!-- chunk {"id": "body-0090", "role": "body", "section": "Fixed Point Continuation method (FPC)", "weight": 1.0} -->

The Fixed Point Continuation method is a recent first-order algorithm for solving $(\text{QP}_{\lambda})$ and simple generalizations of $(\text{QP}_{\lambda})$ ​. The main idea is based on a fixed point equation, $x = {F{(x)}}$, which holds at the solution (derived from the subgradient optimality condition). For appropriate parameters, $F$ is a contraction, and thus the algorithm $x_{k + 1} = {F{(x_{k})}}$ converges. The operator $F$ comes from forward-backward splitting, and consists of a soft-thresholding/shrinkage step and a gradient step. The main computational burden is one application of $A$ and $A^{\ast}$ at every step. The papers prove $q$-linear convergence, and finite-convergence of some of the components of $x$ for $s$-sparse signals.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Fixed Point Continuation method (FPC)", "weight": 1.0} -->

The parameter $\lambda$ in $(\text{QP}_{\lambda})$ determines the amount of shrinkage and, therefore, the speed of convergence; thus in practice, $\lambda$ is decreased in a continuation scheme. Code for FPC is available at Also available is a state-of-the-art version of FPC from 2008 that uses Barzilai-Borwein steps to accelerate performance. In the numerical tests, the Barzilai-Borwein version (referred to as FPC-BB) significantly outperforms standard FPC. All parameters were set to default values.

<!-- chunk {"id": "body-0092", "role": "body", "section": "FPC Active Set (FPC-AS)", "weight": 1.0} -->

In 2009, inspired by both first-order algorithms, such as FPC, and greedy algorithms, Wen et al. extend FPC into the two-part algorithm FPC Active Set to solve $(\text{QP}_{\lambda})$ ​​. In the first stage, FPC-AS calls an improved version of FPC that allows the step-size to be updated dynamically, using a non-monotone exact line search to ensure $r$-linear convergence, and a Barzilai-Borwein heuristic. After a given stopping criterion, the current value, $x_{k}$, is hard-thresholded to determine an active set.

<!-- chunk {"id": "body-0093", "role": "body", "section": "FPC Active Set (FPC-AS)", "weight": 1.0} -->

On the active set, ${\| x\|}_{\ell_{1}}$ is replaced by $c^{\ast}x$, where $c = {\text{sgn}{(x_{k})}}$, with the constraints that ${{{x{\lbrack i\rbrack}} \cdot c}{\lbrack i\rbrack}} > 0$ for all the indices $i$ belonging to the active set. The objective is now smooth, and solvers, like conjugate gradients (CG) or quasi-Newton methods (e.g. L-BFGS or L-BFGS-B), can solve for $x$ on the active set; this the same as solving. This two-step process is then repeated for a smaller value of $\lambda$ in a continuation scheme.

<!-- chunk {"id": "body-0094", "role": "body", "section": "FPC Active Set (FPC-AS)", "weight": 1.0} -->

We tested FPC-AS using both L-BFGS (the default) and CG (which we refer to as FPC-AS-CG) to solve the subproblem; both of these solvers do not actually enforce the ${{{x{\lbrack i\rbrack}} \cdot c}{\lbrack i\rbrack}} > 0$ constraint on the active set. Code for FPC-AS is available at For $s$-sparse signals, all parameters were set to defaults except for the stopping criteria (as discussed in Section 5.3). For approximately sparse signals, FPC-AS performed poorly ($> {10,000}$ iterations) with the default parameters. By changing a parameter that controls the estimated number of nonzeros from $m/2$ (default) to $n$, the performance improved dramatically, and this is the performance reported in the tables. The maximum number of subspace iterations was also changed from the default to 10, as recommended in the help file.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Bregman", "weight": 1.0} -->

The Bregman Iterative algorithm, motivated by the Bregman distance, has been shown to be surprisingly simple. The first iteration solves $(\text{QP}_{\lambda})$ for a specified value of $\lambda$; subsequent iterations solve $(\text{QP}_{\lambda})$ for the same value of $\lambda$, with an updated observation vector $b$. Typically, only a few outer iterations are needed (e.g. 4), but each iteration requires a solve of ($\text{QP}_{\lambda}$), which is costly. The original Bregman algorithm calls FPC to solve these subproblems; we test Bregman using FPC and the Barzilai-Borwein version of FPC as subproblem solvers.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Bregman", "weight": 1.0} -->

A version of the Bregman algorithm, known as the Linearized Bregman algorithm, takes only one step of the inner iteration per outer iteration; consequently, many outer iterations are taken, in contrast to the regular Bregman algorithm. It can be shown that linearized Bregman is equivalent to gradient ascent on the dual problem. Linearized Bregman was not included in the tests because no standardized public code is available. Code for the regular Bregman algorithm may be obtained at There are quite a few parameters, since there are parameters for the outer iterations and for the inner (FPC) iterations; for all experiments, parameters were set to defaults. In particular, we noted that using the default stopping criteria for the inner solve, which limited FPC to $1,000$ iterations, led to significantly better results than allowing the subproblem to run to $10,000$ iterations.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Fast Iterative Soft-Thresholding Algorithm (FISTA)", "weight": 1.0} -->

FISTA is based upon Nesterov's work but departs from NESTA in two important ways: 1) FISTA solves the sparse unconstrained reconstruction problem ($\text{QP}_{\lambda}$); 2) FISTA is a proximal subgradient algorithm, which only uses two sequences of iterates. In some sense, FISTA is a simplified version of the algorithm previously introduced by Nesterov to minimize composite functions. The theoretical rate of convergence of FISTA is similar to NESTA's, and has been shown to decay as $\mathcal{O}{({1/k^{2}})}$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Fast Iterative Soft-Thresholding Algorithm (FISTA)", "weight": 1.0} -->

For each test, FISTA is run twice: it is first run until the relative variation in the function value is less than $10^{- 14}$, with no limit on function calls, and this solution is used as the reference solution. It is then run a second time using either Criteria 1 or Criteria 2 as the stopping condition, and these are the results reported in the tables.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Constrained versus unconstrained minimization", "weight": 1.0} -->

We would like to briefly highlight the fact that these algorithms are not solving the same problem. NESTA and SPGL1 solve the constrained problem ($\text{BP}_{\epsilon}$), while all other methods tested solve the unconstrained problem ($\text{QP}_{\lambda}$).

<!-- chunk {"id": "body-0100", "role": "body", "section": "Constrained versus unconstrained minimization", "weight": 1.0} -->

As the first chapter of any optimization book will emphasize, solving an unconstrained problem is in general much easier than a constrained problem.^22^2The constrained problem ($\text{BP}_{\epsilon}$) is equivalent to that of minimizing ${\| x\|}_{\ell_{1}} + {\chi_{\mathcal{Q}_{p}}{(x)}}$ where $\mathcal{Q}_{p}$ is the feasible set $\{ x:{{\|{{Ax} - b}\|}_{\ell_{2}} \leq \epsilon}\}$, and ${\chi_{\mathcal{Q}_{p}}{(x)}} = 0$ if $x \in \mathcal{Q}_{p}$ and $+ \infty$ otherwise. Hence, the unconstrained problem has a discontinuous objective functional.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Constrained versus unconstrained minimization", "weight": 1.0} -->

For example, it may be hard to even find a feasible point for ($\text{BP}_{\epsilon}$), since the pseudo-inverse of $A$, when $A$ is not a projection, may be difficult to compute. It is possible to solve a sequence of unconstrained ($\text{QP}_{\lambda_{j}}$) problems for various $\lambda_{j}$ to approximately find a value of the dual variable $\lambda$ that leads to equivalence with ($\text{BP}_{\epsilon}$), but even if this procedure is integrated with the continuation procedure, it will require several, if not dozens, of solves of $(\text{QP}_{\lambda})$ (and this will in general only lead to an approximate solution to ($\text{BP}_{\epsilon}$)). The Newton-based root finding method of SPGL1 relies on solving a sequence of constrained problems ($\text{LS}_{\tau}$); basically, the dual solution to a constrained problem gives useful information.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Constrained versus unconstrained minimization", "weight": 1.0} -->

Thus, we emphasize that SPGL1 and NESTA are actually more general than the other algorithms (and as Section 6 shows, NESTA is even more general because it handles a wide variety of constrained problems); this is especially important because from a practical viewpoint, it may be easier to estimate an appropriate $\epsilon$ than an appropriate value of $\lambda$. Furthermore, as will be shown in Section 5.4, SPGL1 and NESTA with continuation are also the most robust methods for arbitrary signals (i.e. they perform well even when the signal is not exactly sparse, and even when it has high dynamic range). Combining these two facts, we feel that these two algorithms are extremely useful for real-world applications.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Experimental protocol", "weight": 1.0} -->

In these experiments, we compare NESTA with other efficient methods. There are two main difficulties with comparisons which might explain why broad comparisons have not been offered before. The first problem is that some algorithms, such as NESTA, solve ($\text{BP}_{\epsilon}$), whereas other algorithms solve ($\text{QP}_{\lambda}$). Given $\epsilon$, it is difficult to compute $\lambda{(\epsilon)}$ that gives an equivalence between the problems; in theory, the KKT conditions give $\lambda$, but we have observed in practice that because we have an approximate solution (albeit a very accurate one), computing $\lambda$ in this fashion is not stable.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Experimental protocol", "weight": 1.0} -->

Instead, we note that given $\lambda$ and a solution $x_{\lambda}$ to ($\text{QP}_{\lambda}$), it is easy to compute a very accurate $\epsilon{(\lambda)}$ since $\epsilon = {\|{{Ax_{\lambda}} - b}\|}_{\ell_{2}}$. Hence, we use a two-step procedure. In the first step, we choose a value of $\epsilon_{0} = {\sqrt{m + {2\sqrt{2m}}}\sigma}$ based on the noise level $\sigma$ (since a value of $\lambda$ that corresponds to $\sigma$ is less clear), and use SPGL1 to solve ($\text{BP}_{\epsilon}$). From the SPGL1 dual solution, we have an estimate of $\lambda = {\lambda{(\epsilon_{0})}}$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Experimental protocol", "weight": 1.0} -->

As noted above, this equivalence may not be very accurate, so the second step is to compute $\epsilon_{1} = {\epsilon{(\lambda)}}$ via FISTA, using a very high accuracy of $\delta = 10^{- 14}$. The pair $(\lambda,\epsilon_{1})$ now leads to nearly equivalent solutions of ($\text{QP}_{\lambda}$) and ($\text{BP}_{\epsilon}$). The solution from FISTA will also be used to judge the accuracy of the other algorithms.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Experimental protocol", "weight": 1.0} -->

The other main difficulty in comparisons is a fair stopping criterion. Each algorithm has its own stopping criterion (or may offer a choice of stopping criteria), and these are not directly comparable. To overcome this difficulty, we have modified the codes of the algorithms to allow for two new stopping criterion that we feel are the only fair choices. The short story is that we use NESTA to compute a solution $x_{N}$ and then ask the other algorithms to compute a solution that is at least as accurate.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Experimental protocol", "weight": 1.0} -->

Specifically, given NESTA's solution $x_{N}$ (using continuation), the other algorithms terminate at iteration $k$ when the solution ${\hat{x}}_{k}$ satisfies We run tests with both stopping criteria to reduce any potential bias from the fact that some algorithms solve ($\text{QP}_{\lambda}$), for which Crit. 2 is the most natural, while others solve ($\text{BP}_{\epsilon}$), for which Crit. 1 is the most natural. In practice, the results when applying Crit. 1 or Crit. 2 are not significantly different.

<!-- chunk {"id": "body-0108", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

This first series of experiments tests all the algorithms discussed above in the case where the unknown signal is $s$-sparse with $s = {m/5}$, $m = {n/8}$, and $n = {262,144}$. This situation is close to the limit of perfect recovery from noiseless data. The $s$ nonzero entries of the signals $x^{0}$ are generated as described. Reconstruction is performed with several values of the dynamic range $d = {20,40,60,80,100}$ in dB. The measurement operator is a randomly subsampled discrete cosine transform, as in Section 4.1 (with a different random set of measurements chosen for each trial). The noise level is set to $\sigma = 0.1$. The results are reported in Tables 3 (Crit. 1) and 4 (Crit.

<!-- chunk {"id": "body-0109", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

2); each cell in these table contains the mean value of $\mathcal{N}_{A}$ (the number of calls of $A$ or $A^{\ast}$) over $10$ random trials, and, in smaller font, the minimum and maximum value of $\mathcal{N}_{A}$ over the $10$ trials. When convergence is not reached after $\mathcal{N}_{A} = {20,000}$, we report DNC (did not converge). As expected, the number of calls needed to reach convergence varies a lot from an algorithm to another.

<!-- chunk {"id": "body-0110", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

The careful reader will notice that Tables 3 and 4 do not feature the results provided by l1_ls; indeed, while it seems faster than other interior point methods, it is still far from being comparable to the other algorithms reviewed here. In these experiments l1_ls typically needed $1500$ calls to $A$ or $A^{\ast}$ for reconstructing a $20$ dB signal with $s = {m/100}$ nonzero entries. For solving the same problem with a dynamic range of $100$ dB, it took $5$ hours to converge on a dual core MacPro G5 clocked at 2.7GHz.

<!-- chunk {"id": "body-0111", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

GPSR performs well in the case of low-dynamic range signals; its performance, however, decreases dramatically as the dynamic range increases; Table 4 shows that it does not converge for 80 and 100 dB signals. GPSR with continuation does worse on the low dynamic range signals (which is not surprising). It does much better than the regular GPSR version on the high dynamic range signals, though it is slower than NESTA with continuation by more than a factor of 10. SpaRSA performs well at low dynamic range, comparable to NESTA, and begins to outperform GSPR with continuation as the dynamic range increases, although it begins to underperform NESTA with continuation in this regime. SpaRSA takes over twice as many function calls on the 100 dB signal as on the 20 dB signal.

<!-- chunk {"id": "body-0112", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

SPGL1 shows good performance with very sparse signals and low dynamic range. Although it has fewer iteration counts than NESTA, the performance decreases much more quickly than for NESTA as the dynamic range increases; SPGL1 requires about 9$\times$ more calls to $A$ at 100 dB than at 20 dB, whereas NESTA with continuation requires only about 1.5$\times$ more calls. FISTA is almost as fast as SPGL1 on the low dynamic range signal, but degrades very quickly as the dynamic range increases, taking about 200$\times$ more iterations at 100 dB than at 20 dB. One large contributing factor to this poor performance at high dynamic range is the lack of a continuation scheme.

<!-- chunk {"id": "body-0113", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

FPC performs well at low dynamic range, but is very slow on 100 dB signals. The Barzilai-Borwein version was consistently faster than the regular version, but also degrades much faster than NESTA with continuation as the dynamic range increases. Both FPC Active Set and the Bregman algorithm perform well at all dynamic ranges, but again, degrade faster than NESTA with continuation as the dynamic range increases. There is a slight difference between the two FPC Active set versions (using L-BFGS or CG), but the dependence on the dynamic range is roughly similar.

<!-- chunk {"id": "body-0114", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

The performances of NESTA with continuation are reasonable when the dynamic range is low. When the dynamic range increases, continuation helps by dividing the number of calls up to a factor about $20$, as in the 100 dB case. In these experiments, the tolerance $\delta$ is consistently equal to $10^{- 7}$; while this choice is reasonable when the dynamic range is high, it seems too conservative in the low dynamic range case. Setting a lower value of $\delta$ should improve NESTA's performance in this regime. In other words, NESTA with continuation might be tweaked to run faster on the low dynamic range signals. However, this is not in the spirit of this paper and this is why we have not researched further refinements.

<!-- chunk {"id": "body-0115", "role": "body", "section": "The case of exactly sparse signals", "weight": 1.0} -->

In summary, for exactly sparse signals exhibiting a significant dynamic range, 1) the performance of NESTA with continuation---but otherwise applied out-of-the-box---is comparable to that of state-of-the-art algorithms, and 2) most state-of-the-art algorithms are efficient on these types of signals.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

We now turn our attention to approximately sparse signals. Such signals are generated via a permutation of the Haar wavelet coefficients of a $512 \times 512$ natural image. The data $b$ are ${m = {n/8} = 32},768$ discrete cosine measurements selected at random. White Gaussian noise with standard deviation $\sigma = 0.1$ is then added. Each test is repeated 5 times, using a different random permutation every time (as well as a new instance of the noise vector). Unlike in the exactly sparse case, the wavelet coefficients of natural images mostly contain mid-range and low level coefficients (see Figure 6) which are challenging to recover.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

The results are reported in Tables 5 (Crit. 1) and 6 (Crit. 2); the results from applying the two stopping criteria are nearly identical. In these series of experiments, the performance of SPGL1 is quite good but seems to vary a lot from one trial to another (Table 6). Notice that the concept of an active-set is ill defined in the approximately sparse case; as a consequence, the active set version of FPC is not much of an improvement over the regular FPC version. FPC is very fast for $s$-sparse signals but lacks the robustness to deal with less ideal situations in which the unknown is only approximately sparse.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

FISTA and SpaRSA converge for these tests, but are not competitive with the best methods. It is reasonable to assume that FISTA would also improve if implemented with continuation. SpaRSA already uses continuation but does not match its excellent performance on exactly sparse signals.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

Bregman, SPGL1, and NESTA with continuation all have excellent performances (continuation really helps NESTA) in this series of experiments. NESTA with continuation seems very robust when high accuracy is required. The main distinguishing feature of NESTA is that it is less sensitive to dynamic range; this means that as the dynamic range increases, or as the noise level $\sigma$ decreases, NESTA becomes very competitive. For example, when the same test was repeated with more noise ($\sigma = 1$), all the algorithms converged faster. In moving from $\sigma = 1$ to $\sigma = 0.1$, SPGL1 required $90\%$ more iterations and Bregman required $20\%$ more iterations, while NESTA with continuation required only $5\%$ more iterations.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

One conclusion from these tests is that SPGL1, Bregman and NESTA (with continuation) are the only methods dealing with approximately sparse signals effectively. The other methods, most of which did very well on exactly sparse signals, take over $10,000$ function calls or even do not converge in $20,000$ function calls; by comparison, SPGL1, Bregman and NESTA with continuation converge in about $2,000$ function calls. It is also worth noting that Bregman is only as good as the subproblem solver; though not reported here, using the regular FPC (instead of FPC-BB) with Bregman leads to much worse performance.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

The algorithms which did converge all achieved a mean relative $\ell_{1}$ error (using and the high accuracy FISTA solution as the reference) less than $2 \cdot 10^{- 4}$ and sometimes as low as $10^{- 5}$, except SPGL1, which had a mean relative error of $1.1 \cdot 10^{- 3}$. Of the algorithms that did not converge in $20,000$ function calls, FPC and FPC-BB had a mean $\ell_{1}$ relative error about $5 \cdot 10^{- 3}$, GPSR with continuation had errors about $5 \cdot 10^{- 2}$, and the rest had errors greater than $10^{- 1}$.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

FPC Active Set FPC Active Set (CG) Table 5: Recovery results of an approximately sparse signal with Crit. 1 as a stopping rule.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Approximately sparse signals", "weight": 1.0} -->

FPC Active Set FPC Active Set (CG) Table 6: Recovery results of an approximately sparse signal with Crit. 2 as a stopping rule.

<!-- chunk {"id": "body-0124", "role": "body", "section": "An all-purpose algorithm", "weight": 1.0} -->

A distinguishing feature is that NESTA is able to cope with a wide range of standard regularizing functions. In this section, we present two examples: nonstandard $\ell_{1}$ minimization and total-variation minimization.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Nonstandard sparse reconstruction: $\\ell_{1}$ analysis", "weight": 1.0} -->

Suppose we have a signal $x \in {\mathbb{R}}^{n}$, which is assumed to be approximately sparse in a transformed domain such as the wavelet, the curvelet or the time-frequency domains. Let $W$ be the corresponding synthesis operator whose columns are the waveforms we use to synthesize the signal $x = {W\alpha}$ (real-world signals do not admit an exactly sparse expansion); e.g. the columns may be wavelets, curvelets and so, or both. We will refer to $W^{\ast}$ as the analysis operator. As before, we have (possibly noisy) measurements $b = {{Ax^{0}} + z}$. The synthesis approach attempts reconstruction by solving while the analysis approach solves the related problem If $W$ is orthonormal, the two problems are equivalent, but in general, these give distinct solutions and current theory explaining the differences is still in its infancy. The article suggests that synthesis may be overly sensitive, and argues with geometric heuristics and numerical simulations that analysis is sometimes preferable.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Nonstandard sparse reconstruction: $\\ell_{1}$ analysis", "weight": 1.0} -->

Solving $\ell_{1}$-analysis problems with NESTA is straightforward as only Step $1$ needs to be adapted. We have and the gradient at $x$ is equal to Steps $2$ and $3$ remain unchanged. The computational complexity of the algorithm is then increased by an extra term, namely $2\mathcal{C}_{W}$ where $\mathcal{C}_{W}$ is the cost of applying $W$ or $W^{\ast}$ to a vector. In practical situations, there is often a fast algorithm for applying $W$ and $W^{\ast}$, e.g. a fast wavelet transform, a fast curvelet transform, a fast short-time Fourier transform and so, which makes this a low-cost extra step^33^3The ability to solve the analysis problem also means that NESTA can easily solve reweighted $\ell_{1}$ problems with no change to the code..

<!-- chunk {"id": "body-0127", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

Because NESTA is one of very few algorithms that can solve both the analysis and synthesis problems efficiently, we tested the performance of both analysis and synthesis on a simulated real-world signal from the field of radar detection. The test input is a superposition of three signals. The first signal, which is intended to make recovery more difficult for any smaller signals, is a plain sinusoid with amplitude of 1000 and frequency near 835 MHz.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

A second signal, similar to a Doppler pulse radar, is at a carrier frequency of 2.33 GHz with maximum amplitude of 10, a pulse width of 1 $\mus$ and a pulse repetition interval of 10 $\mu$s; the pulse envelope is trapezoidal, with a 10 ns rise time and 40 ns fall time. This signal is more than 40 dB lower than the pure sinusoid, since the maximum amplitude is 100$\times$ smaller, and since the radar is nonzero only 10% of the time. The Doppler pulse was chosen to be roughly similar to a realistic weather Doppler radar. In practice, these systems operate at 5 cm or 10 cm wavelengths (i.e. 6 or 3 GHz) and send out short trapezoidal pulses to measure the radial velocity of water droplets in the atmosphere using the Doppler effect.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

The third signal, which is the signal of interest, is a frequency-hopping radar pulse with maximum amplitude of 1 (so about 20 dB beneath the Doppler signal, and more than 60 dB below the sinusoid). For each instance of the pulse, the frequency is chosen uniformly at random from the range 200 MHz to 2.4 GHz. The pulse duration is 2 $\mus$ and the pulse repetition interval is 22 $\mus$, which means that some, but not all, pulses overlap with the Doppler radar pulses. The rise time and fall time of the pulse envelope are comparable to the Doppler pulse. Frequency-hopping signals may arise in applications because they can be more robust to interference and because they can be harder to intercept. When the carrier frequencies are not known to the listener, the receiver must be designed to cover the entire range of possible frequencies (2.2 GHz in our case). While some current analog-to-digital converters (ADC) may be capable of operating at 2.2 GHz, they do so at the expense of low precision.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

Hence this situation may be particularly amenable to a compressed sensing setup by using several slower (but accurate) ADC to cover a large bandwidth.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

We consider the exact signal to be the result of an infinite-precision ADC operating at 5 GHz, which corresponds to the Nyquist rate for signals with 2.5 GHz of bandwidth. Measurements are taken using an orthogonal Hadamard transform with randomly permuted columns, and these measurements were subsequently sub-sampled by randomly choosing $m = n}$ rows of the transform (so that we undersample Nyquist by $10/3$). Samples are recorded for $T = {209.7\mu}$s, which corresponds to $n = 2^{20}$. White noise was added to the measurements to make a 60 dB signal-to-noise ratio (SNR) (note that the effective SNR for the frequency-hopping pulse is much lower). The frequencies of the sinusoid and the Doppler radar were chosen such that they were not integer multiples of the lowest recoverable frequency $f_{min} = {1/{({2T})}}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

For reconstruction, the signal is analyzed with a tight frame of Gabor atoms that is approximately 5.5$\times$ overcomplete. The particular parameters of the frame are chosen to give reasonable reconstruction, but were not tweaked excessively. It is likely that differences in performance between analysis and synthesis are heavily dependent on the particular dictionary.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

To analyze performance, we restrict our attention to the frequency domain in order to simplify comparisons. The top plot in Figure 7 shows the frequency components of the original, noiseless signal. The frequency hopping pulse barely shows up since the amplitude is 1000$\times$ smaller than the sinusoid and since each frequency only occurs for 1 $\mu$s (of 210 $\mu$s total).

<!-- chunk {"id": "body-0134", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

The bottom plots in Figure 7 show the spectrum of the recovered signal using analysis and synthesis, respectively. For this test, analysis does a better job at finding the frequencies belonging to the small pulse, while synthesis does a better job recreating the large pulse and the pure tone. The two reconstructions used slightly different values of $\mu$ to account for the redundancy in the size of the dictionary; otherwise, algorithm parameters were the same. In the analysis problem, NESTA took 231 calls to the analysis/synthesis operator (and 231 calls to the Hadamard transform); for synthesis, NESTA took 1378 calls to the analysis/synthesis operator (and 1378 to the Hadamard transform). With NESTA, synthesis is more computationally expensive than analysis since no change of variables trick can be done; in the synthesis case, $W$ and $W^{\ast}$ are used in Step $2$ and $3$ while in the analysis case, the same operators are used once in Step $1$ (this is accomplished by the previously mentioned change-of-variables for partial orthogonal measurements).

<!-- chunk {"id": "body-0135", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

As emphasized, when $W$ is overcomplete, the solution computed by solving the analysis problems is likely to be denser than in the synthesis case. In plain English, the analysis solution may seem "noisier" than the synthesis solution. But the compactness of the solution of the synthesis problem may also be its weakness: an error on one entry of $\alpha$ may lead to a solution that differs a lot. This may explain why the frequency-hopping radar pulse is harder to recover with the synthesis prior.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Numerical results for nonstandard $\\ell_{1}$ minimization", "weight": 1.0} -->

Because all other known first-order methods solve only the synthesis problem, NESTA may prove to be extremely useful for real-world applications. Indeed, this simple test suggests that analysis may sometimes be much preferable to synthesis, and given a signal with $2^{20}$ samples (too large for interior point methods), we know of no other algorithm that can return the same results.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Total-variation minimization", "weight": 1.0} -->

Nesterov's framework also makes total-variation minimization possible. The TV norm of a 2D digital object $x{\lbrack i,j\rbrack}$ is given by where $D_{1}$ and $D_{2}$ are the horizontal and vertical differences Now the TV norm can be expressed as follows: where $u = {\lbrack u_{1},u_{2}\rbrack}^{\ast} \in \mathcal{Q}_{d}$ if and only for each $(i,j)$, ${{u_{1}^{2}{\lbrack i,j\rbrack}} + {u_{2}^{2}{\lbrack i,j\rbrack}}} \leq 1$, and $D = {\lbrack D_{1},D_{2}\rbrack}^{\ast}$.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Total-variation minimization", "weight": 1.0} -->

The key feature of Nesterov's work is to smooth a well-structured nonsmooth function as follows (notice in the similarity between the TV norm and the $\ell_{1}$ norm): Choosing ${p_{d}{(u)}} = {\frac{1}{2}{\| u\|}_{\ell_{2}}^{2}}$ provides a reasonable prox-function that eases the computation of $\nabla f_{\mu}$. Just as before, changing the regularizing function only modifies Step $1$ of NESTA. Here, where $u_{\mu}{(x)}$ is of the form ${\lbrack u_{1},u_{2}\rbrack}^{\ast}$ and for each $a \in {\{ 1,2\}}$, The application of $D$ and $D^{\ast}$ leads to a negligible computational cost (sparse matrix-vector multiplications).

<!-- chunk {"id": "body-0139", "role": "body", "section": "Numerical results for TV minimization", "weight": 1.0} -->

We are interested in solving To be sure, a number of efficient TV-minimization algorithms have been proposed to solve in the special case $A = I$ (denoising problem), see. In comparison, only a few methods have been proposed to solve the more general problem even when $A$ is a projector. Known methods include interior point methods ($\ell_{1}$-magic), proximal-subgradient methods, Split-Bregman, and the very recently introduced RecPF^44^4available, which operates in the special case of partial Fourier measurements. Roughly, proximal gradient methods approach the solution to by iteratively updating the current estimate $x_{k}$ as follows: where $\text{Prox}_{{TV},\gamma}$ is the proximity operator of TV, see and references therein, Evaluating the proximity operator at $z$ is equivalent to solving a TV denoising problem. In, the authors advocate the use of a side algorithm (for instance Chambolle's algorithm) to evaluate the proximity operator. There are a few issues with this approach.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Numerical results for TV minimization", "weight": 1.0} -->

The first is that side algorithms depend on various parameters, and it is unclear how one should select them in a robust fashion. The second is that these algorithms are computationally demanding which makes them hard to apply to large-scale problems.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Numerical results for TV minimization", "weight": 1.0} -->

To be as fair as possible, we decided to compare NESTA with algorithms for which a code has been publicly released; this is the case for the newest in the family, namely, RecPF (as $\ell_{1}$-magic is based on an interior point method, it is hardly applicable to this large-scale problem). Hence, we propose comparing NESTA for TV minimization with RecPF.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Numerical results for TV minimization", "weight": 1.0} -->

Evaluations are made by comparing the performances of NESTA (with continuation) and RecPF on a set of images composed of random squares. As in Section 5, the dynamic range of the signals (amplitude of the squares) varies in a range from $20$ to $40$ dB. The size of each image $x$ is $1024 \times 1024$; one of these images is displayed in the top panel of Figure 8. The data $b$ are partial Fourier measurements as; the number of measurements $m = {n/10}$. White Gaussian noise of standard deviation $\sigma = 0.1$ is added. The parameters of NESTA are set up as follows: and the initial value of $\mu$ is The maximal number of iterations is set to $\mathcal{I}_{\max} = {4,000}$. As it turns out, TV minimization from partial Fourier measurements is of significant interest in the field of Magnetic Resonance Imaging.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Numerical results for TV minimization", "weight": 1.0} -->

As discussed above, RecPF has been designed to solve TV minimization reconstruction problems from partial Fourier measurements. We set the parameters of RecPF to their default values except for the parameter tol_rel_inn that is set to $10^{- 5}$. This choice makes sure that this converges to a solution close enough to NESTA's output. Figure 8 shows the the solution computed by RecPF (bottom left) and NESTA (bottom right).

<!-- chunk {"id": "body-0144", "role": "body", "section": "Numerical results for TV minimization", "weight": 1.0} -->

The curves in Figure 9 show the number of calls to $A$ or $A^{\ast}$; mid-points are averages over $5$ random trials, with error bars indicating the minimum and maximum number of calls. Here, RecPF is stopped when where $x_{N}$ is the solution computed via NESTA. As before continuation is very efficient when the dynamic range is high (typically higher than $40$ dB). An interesting feature is that the numbers of calls are very similar over all five trials. When the dynamic range increases, the computational costs of both NESTA and RecPF naturally increase. Note that in the $60$ and $80$ dB experiments, RecPF did not converge to the solution and this is the reason why the number of calls saturates. While both methods have a similar computational cost in the low-dynamic range regime, NESTA has a clear advantage in the higher-dynamic range regime. Moreover, the number of iterations needed to reach convergence with NESTA with continuation is fairly low---300-400 calls to $A$ and $A^{\ast}$---and so this algorithm is well suited to large scale problems.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we have proposed an algorithm for general sparse recovery problems, which is based on Nesterov's method. This algorithm is accurate and competitive with state-of-the-art alternatives. In fact, in applications of greatest interest such as the recovery of approximately sparse signals, it outperforms most of the existing methods we have used in our comparisons and is comparable to the best. Further, what is interesting here, is that we have not attempted to optimize the algorithm in any way. For instance, we have not optimized the parameters $\{\alpha_{k}\}$ and $\{\tau_{k}\}$, or the number of continuation steps as a function of the desired accuracy $\delta$, and so it is expected that finer tuning would speed up the algorithm. Another advantage is that NESTA is extremely flexible in the sense that minor adaptations lead to efficient algorithms for a host of optimization problems that are crucial in the field of signal/image processing.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Extensions", "weight": 1.0} -->

This paper focused on the situation in which $A^{\ast}A$ is a projector (the rows of $A$ are orthonormal). This stems from the facts that 1) the most computationally friendly compressed sensing are of this form, and 2) it allows fast computations of the two sequence of iterates $\{ y_{k}\}$ and $\{ z_{k}\}$. It is important, however, to extend NESTA as to be able to cope with a wider range of problem in which $A^{\ast}A$ is not a projection (or not diagonal).

<!-- chunk {"id": "body-0147", "role": "body", "section": "Extensions", "weight": 1.0} -->

In order to do this, observe that in Steps $2$ and $3$, we need to solve problems of the form for some $q$, and we have seen that the solution is given by $y_{k} = {\mathcal{P}_{\mathcal{Q}_{p}}{(q)}}$, where $\mathcal{P}_{\mathcal{Q}_{p}}$ is the projector onto $\mathcal{Q}_{p}:={\{ x:{{\|{{Ax} - b}\|}_{\ell_{2}} \leq \epsilon}\}}$. The solution is given by for some $\lambda \geq 0$. When the eigenvalues of $A^{\ast}A$ are well clustered, the right-hand side of can be computed very efficiently via a few conjugate gradients (CG) steps.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Extensions", "weight": 1.0} -->

Note that this is of direct interest in compressed sensing applications in which $A$ is a random matrix since in all the cases we are familiar, the eigenvalues of $A^{\ast}A$ are tightly clustered. Hence, NESTA may be extended to general problems while retaining its efficiency, with the proviso that a good rule for selecting $\lambda$ in is available; i.e. such that ${\|{{Ay_{k}} - b}\|}_{\ell_{2}} = \epsilon$ unless $q \in \mathcal{Q}_{p}$. Of course, one can always eliminate the problem of finding such a $\lambda$ by solving the unconstrained problem $(\text{QP}_{\lambda})$ instead of $(\text{BP}_{\epsilon})$. In this case, each NESTA iteration is actually very cheap, no matter how $A$ looks like.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Extensions", "weight": 1.0} -->

Finally, we also observe that Nesterov's framework is likely to provide efficient algorithms for related problems, which do not have the special $\ell_{1} + \ell_{2}^{2}$ structure. One example might be the Dantzig selector, which is a convenient and flexible estimator for recovering sparse signals from noisy data: This is of course equivalent to the unconstrained problem for some value of $\lambda$. Clearly, one could apply Nesterov's smoothing techniques to smooth both terms in the objective functional together with Nesterov's accelerated gradient techniques, and derive a novel and efficient algorithm for computing the solution to the Dantzig selector. This is an example among many others. Another might be the minimization of a sum of two norms, e.g. an $\ell_{1}$ and a TV norm, under data constraints.
