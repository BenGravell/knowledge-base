<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Coordinate Descent Algorithms

Topics include Attention mechanisms, Optimization, Learning, Coordinate descent.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Coordinate descent algorithms solve optimization problems by successively performing approximate minimization along coordinate directions or coordinate hyperplanes. They have been used in applications for many years, and their popularity continues to grow because of their usefulness in data analysis, machine learning, and other areas of current interest. This paper describes the fundamentals of the coordinate descent approach, together with variants and extensions and their convergence properties, mostly with reference to convex objectives. We pay particular attention to a certain problem structure that arises frequently in machine learning applications, showing that efficient implementations of accelerated coordinate descent algorithms are possible for problems of this type. We also present some parallel variants and discuss their convergence properties under several models of parallel execution.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Coordinate descent (CD) algorithms for optimization have a history that dates to the foundation of the discipline. They are iterative methods in which each iterate is obtained by fixing most components of the variable vector $x$ at their values from the current iteration, and approximately minimizing the objective with respect to the remaining components. Each such subproblem is a lower-dimensional (even scalar) minimization problem, and thus can typically be solved more easily than the full problem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

CD methods are the archetype of an almost universal approach to algorithmic optimization: solving an optimization problem by solving a sequence of simpler optimization problems. The obviousness of the CD approach and its acceptable performance in many situations probably account for its long-standing appeal among practitioners. Paradoxically, the apparent lack of sophistication may also account for its unpopularity as a subject for investigation by optimization researchers, who have usually been quick to suggest alternative approaches in any given situation. There are some very notable exceptions. The 1970 text of Ortega and Rheinboldt ( Section 14.6) included a comprehensive discussion of "univariate relaxation," and such optimization specialists as Luo and Tseng Tseng, and Bertsekas and Tsitsiklis made important contributions to understanding the convergence properties of these methods in the 1980s and 1990s.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The situation has changed in recent years. Various applications (including several in computational statistics and machine learning) have yielded problems for which CD approaches are competitive in performance with more reputable alternatives. The properties of these problems (for example, the low cost of calculating one component of the gradient, and the need for solutions of only modest accuracy) lend themselves well to efficient implementations of CD, and CD methods can be adapted well to handle such special features of these applications as nonsmooth regularization terms and a small number of equality constraints. At the same time, there have been improvements in the algorithms themselves and in our understanding of them. Besides their extension to handle the features just mentioned, new variants that make use of randomization and acceleration have been introduced. Parallel implementations that lend themselves well to modern computer architectures have been implemented and analyzed. Perhaps most surprisingly, these developments are relevant even to the most fundamental problem in numerical computation: solving the linear equations ${Aw} = b$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the remainder of this section, we state the problem types for which CD methods have been developed, and sketch the most fundamental versions of CD. Section 2 surveys applications both historical and modern. Section 3 sketches the types of algorithms that have been implemented and analyzed, and presents several representative convergence results. Section 4 focuses on parallel CD methods, describing the behavior of these methods under synchronous and asynchronous models of computation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach throughout is to describe the CD methods in their simplest forms, to illustrate the fundamentals of the applications, implementations, and analysis. We focus almost exclusively on methods that adjust just one coordinate on each iteration. Most applications use block coordinate descent methods, which adjust groups of blocks of indices at each iteration, thus searching along a coordinate hyperplane rather than a single coordinate direction. Most derivation and analysis of single-coordinate descent methods can be extended without great difficulty to the block-CD setting; the concepts do not change fundamentally. We mention too that much effort has been devoted to developing more general forms of CD algorithms and analysis, involving weighted norms and other features, that allow more flexible implementation and allow the proof of stronger and more general (though usually not qualitatively different) convergence results.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Formulations", "weight": 1.0} -->

The problem considered in most of this paper is the following unconstrained minimization problem: where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is continuous. Different variants of CD make further assumptions about $f$. Sometimes it is assumed to be smooth and convex, sometimes smooth and possibly nonconvex, and sometimes smooth but with a restricted domain. (We will make such assumptions clear in each discussion of algorithmic variants and convergence results.)

<!-- chunk {"id": "body-0009", "role": "body", "section": "Formulations", "weight": 1.0} -->

Motivated by recent popular applications, it is common to consider the following structured formulation: where $f$ is smooth, $\Omega$ is a regularization function that may be nonsmooth and extended-valued, and $\lambda > 0$ is a regularization parameter. $\Omega$ is often convex and usually assumed to be separable or block-separable. When separable, $\Omega$ has the form where $\Omega_{i}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ for all $i$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Formulations", "weight": 1.0} -->

Block separability means that the $n \times n$ identity matrix can be partitioned into column submatrices $U_{i}$, $i = {1,2,\ldots,N}$ such that Block-separable examples include group-sparse regularizers in which ${\Omega_{i}{(z_{i})}}:={\| z_{i}\|}_{2}$. Formulations of the type, with separable or block-separable regularizers, arise in such applications as compressed sensing, statistical variable selection, and model selection.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Formulations", "weight": 1.0} -->

The class of problems known as empirical risk minimization (ERM) gives rise to a formulation that is particularly amenable to coordinate descent; see. These problems have the form for vectors $c_{i} \in {\mathbb{R}}^{d}$, $i = {1,2,\ldots,n}$ and convex functions $\phi_{i}$, $i = {1,2,\ldots,n}$ and $g$. We can express linear least-squares, logistic regression, support vector machines, and other problems in this framework. Recalling the following definition of the conjugate $t^{\ast}$ of a convex function $t$: we can write the Fenchel dual (Section 31) of as follows: where $C$ is the $d \times n$ matrix whose columns are $c_{i}$, $i = {1,2,\ldots,n}$. The dual formulation is has special appeal as a target for coordinate descent, because of separability of the summation term.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Formulations", "weight": 1.0} -->

One interesting case is the system of linear equations which we assume to be a feasible system. The least-norm solution is found by solving whose Lagrangian dual is (We recover the primal solution from by setting $w = {A^{T}x}$.) We can see that is a special case of the Fenchel dual obtained from if we set where $I_{\{ b_{i}\}}$ denotes the indicator function for $b_{i}$, which is zero at $b_{i}$ and infinite elsewhere. (Its conjugate is ${I_{\{ b_{i}\}}^{\ast}{(s_{i})}} = {b_{i}s_{i}}$.) The primal problem can be restated correspondingly as where $A_{i}$ denotes the $i$th row of the matrix $A$, which has the form.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Outline of Coordinate Descent Algorithms", "weight": 1.0} -->

The basic coordinate descent framework for continuously differentiable minimization is shown in Algorithm 1. Each step consists of evaluation of a single component $i_{k}$ of the gradient $\nabla f$ at the current point, followed by adjustment of the $i_{k}$ component of $x$, in the opposite direction to this gradient component. (Here and throughout, we use ${\lbrack{{\nabla f}{(x)}}\rbrack}_{i}$ to denote the $i$th component of the gradient ${\nabla f}{(x)}$.) There is much scope for variation within this framework. The components can be selected in a cyclic fashion, in which $i_{0} = 1$ and They can be required to satisfy an "essentially cyclic" condition, in which for some $T \geq n$, each component is modified at least once in every stretch of $T$ iterations, that is, Alternatively, they can be selected randomly at each iteration (though not necessarily with equal probability).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Outline of Coordinate Descent Algorithms", "weight": 1.0} -->

Turning to steplength $\alpha_{k}$: we may perform exact minimization along the $i_{k}$ component, or choose a value of $\alpha_{k}$ that satisfies traditional line-search conditions (such as sufficient decrease), or make a predefined "short-step" choice of $\alpha_{k}$ based on prior knowledge of the properties of $f$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Outline of Coordinate Descent Algorithms", "weight": 1.0} -->

Set k ← 0 and choose x0 ∈ ℝn; xk + 1 ← xk − αk [∇f (xk)]ik eik for some αk > 0; until termination test satisfied; Algorithm 1 Coordinate Descent for The CD framework for the separable regularized problem, is shown in Algorithm 2. At iteration $k$, a scalar subproblem is formed by making a linear approximation to $f$ along the $i_{k}$ coordinate direction at the current iterate $x^{k}$, adding a quadratic damping term weighted by $1/\alpha_{k}$ (where $\alpha_{k}$ plays the role of a steplength), and treating the relevant regularization term $\Omega_{i}$ explicitly.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline of Coordinate Descent Algorithms", "weight": 1.0} -->

Note that when the regularizer $\Omega_{i}$ is not present, the step is identical to the one taken in Algorithm 1. For some interesting choices of $\Omega_{i}$ (for example $\Omega_{i}{(\cdot)} = | \cdot |$), it is possible to write down a closed-form solution of the subproblem; no explicit search is needed. The operation of solving such subproblems is often referred to as a "shrink operation," which we denote by $S_{\beta}$ and define as follows: By stating the subproblem in Algorithm 2 equivalently as we can express the CD update as $z_{i_{k}}^{k}\leftarrow{S_{\lambda\alpha_{k}}{({x_{i_{k}}^{k} - {\alpha_{k}{\lbrack{{\nabla f}{(x^{k})}}\rbrack}_{i_{k}}}})}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Outline of Coordinate Descent Algorithms", "weight": 1.0} -->

Set k ← 0 and choose x0 ∈ ℝn; $z_{i_{k}}^{k}\leftarrow\arg\min_{\chi}{(\chi - x_{i_{k}}^{k})}^{T}{\lbrack\nabla f{(x^{k})}\rbrack}_{i_{k}} + \frac{1}{2\alpha_{k}} \parallel \chi - x_{i_{k}}^{k} \parallel_{2}^{2} + \lambda\Omega_{i}{(\chi)}$ for some αk > 0; xk + 1 ← xk + (zikk − xikk) eik; until termination test satisfied; Algorithm 2 Coordinate Descent, Algorithms 1 and 2 can be extended to block-CD algorithms in a straightforward way, by updating a block of coordinates (denoted by the column submatrix $U_{i_{k}}$ of the identity matrix) rather than a single coordinate.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Outline of Coordinate Descent Algorithms", "weight": 1.0} -->

In Algorithm 2, it is assumed that the choice of block is consistent with the block-separable structure of the regularization function $\Omega$, that is, $U_{i_{k}}$ is a concatenation of several of the submatrices $U_{i}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Application to Linear Equations", "weight": 1.0} -->

For the formulation that arises from the linear system ${Aw} = b$, let us assume that the rows of $A$ are normalized, that is, Applying Algorithm 1 to with $\alpha_{k} \equiv 1$, each step has the form If we maintain and update the estimate $w^{k}$ of the solution to the primal problem after each update of $x^{k}$, according to $w^{k} = {A^{T}x^{k}}$, we obtain which is the update formula for the Kaczmarz algorithm kaczmarz37. Following this update, we have using that so that the $i_{k}$ equation in the system ${Aw} = b$ is now satisfied. This method if sometimes known as the "method of successive projections" because it projects onto the feasible hyperplane for a single constraint at every iteration.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Relationship to Other Methods", "weight": 1.0} -->

Stochastic gradient (SG) methods, also undergoing a revival of interest because of their usefulness in data analysis and machine learning applications, minimize a smooth function $f$ by taking a (negative) step along an estimate $g^{k}$ of the gradient ${\nabla f}{(x^{k})}$ at iteration $k$. It is often assumed that $g^{k}$ is an unbiased estimate of ${\nabla f}{(x^{k})}$, that is, ${{\nabla f}{(x^{k})}} = {E{(g^{k})}}$, where the expectation is taken over whatever random variables were used in obtaining $g^{k}$ from the current iterate $x^{k}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Relationship to Other Methods", "weight": 1.0} -->

Randomized CD algorithms can be viewed as a special case of SG methods, in which $g^{k} = {n{\lbrack{{\nabla f}{(x^{k})}}\rbrack}_{i_{k}}e_{i_{k}}}$, where $i_{k}$ is chosen uniformly at random from $\{ 1,2,\ldots,n\}$. Here, $i_{k}$ is the random variable, and we have certifying unbiasedness. However, CD algorithms have the advantage over general SG methods that descent in $f$ can be guaranteed at every iteration. Moreover, the variance of the gradient estimate $g^{k}$ shrinks to zero as the iterates converge to a solution $x^{\ast}$, since every component of ${\nabla f}{(x^{\ast})}$ is zero. By contrast, in general SG methods, the gradient estimates $g^{k}$ may be nonzero even when $x^{k}$ is a solution.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Relationship to Other Methods", "weight": 1.0} -->

The relationship between CD and SG methods can also be discerned from the Fenchel dual pair and. SG methods are quite popular for solving formulation, where the estimate $g^{k}$ is obtained by taking a single term $i_{k}$ from the summation and using ${\nabla\phi_{i_{k}}}{({c_{i_{k}}^{T}w})}c_{i_{k}}$ as the estimate of the gradient of the full summation. This approach corresponds to applying CD to the dual, where the component $i_{k}$ of $x$ is selected for updating at iteration $k$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Relationship to Other Methods", "weight": 1.0} -->

This relationship is typified by the Kaczmarz algorithm for ${Aw} = b$, which can be derived either as CD applied to the dual formulation or as SG applied to the sum-of-squares problem CD is related in an obvious way to the Gauss-Seidel method for $n \times n$ systems of linear equations, which adjusts the $i_{k}$ variable to ensure satisfaction of the $i_{k}$ equation, at iteration $k$. (Successive over-relaxation (SOR) modifies this approach by scaling each Gauss-Seidel step by a factor $({1 + \omega})$ for some constan $\omega \in {\lbrack 0,1)}$, chosen so as to improve the convergence rate.) Standard Gauss-Seidel and SOR use the cyclic choice of coordinates, whereas a random choice of $i_{k}$ would correspond to "randomized" versions of these methods.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Relationship to Other Methods", "weight": 1.0} -->

To make the connections more explicit: The Gauss-Seidel method applied to the normal equations for --- that is, ${A^{T}Aw} = {A^{T}b}$ --- is equivalent to applying Algorithm 1 to the least-squares problem, when the steplength $\alpha_{k}$ is chosen to minimize the objective exactly along the given coordinate direction. SOR also corresponds to Algorithm 1, with $\alpha_{k}$ chosen to be a factor $({1 + \omega})$ times the exact minimum. These equivalences allow the results of Section 3 to be used to derive convergence rates for Gauss-Seidel applied to the normal equations, including linear convergence when $A^{T}A$ is nonsingular. Note that these results do not require feasibility of the original equations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Applications", "weight": 1.0} -->

We mention here several applications of CD methods to practical problems, some dating back decades and others relatively new. Our list is necessarily incomplete, but it attests to the popularity of CD in a wide variety of application communities.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Applications", "weight": 1.0} -->

Bouman and Sauer discuss an application to positron emission tomography (PET) in which the objective has the form where $f$ is smooth and convex and $\Omega$ is a sum of terms of the form ${|{x_{j} - x_{l}}|}^{q}$ for some pairs of components $(j,l)$ of $x$ and some $q \in {\lbrack 1,2\rbrack}$. Ye et al. Ye:99 apply a similar method to a different objective arising from optical diffusion tomography.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Applications", "weight": 1.0} -->

Liu, Paratucco, and Zhang Liu:2009:BCD:1553374.1553458 describe a block CD approach for linear least squares plus a regularization function consisting of a sum of $\ell_{\infty}$ norms of subvectors of $x$. The technique is applied to semantic basis discovery, which learns from data how to identify and classify the functional MRI response of a person's brain when they hear certain English words.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Applications", "weight": 1.0} -->

Canutescu and Dunbrack describe a cyclic coordinate descent method for determining protein structure, adjusting the dihedral angles in a protein chain so that the atom at the end of the chain comes close to a specified position in space.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Applications", "weight": 1.0} -->

Florian and Chen recover origin-destination matrices from observed traffic flows by alternately solving a bilevel optimization problem over two blocks of variables: the origin-destination demands and the proportion of each origin-destination flow assigned to each arc in the network.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Applications", "weight": 1.0} -->

Breheny and Huang discuss coordinate descent for linear and logistic regression with nonconvex separable regularization terms, reporting results for genetic association and gene expression studies. The SparseNet algorithm applied to problems with these same nonconvex separable regularizers uses warm-started cyclic coordinate descent as an inner loop to solve a sequence of problems in which the regularization parameter $\lambda$ in and the parameters defining concavity of the regularization functions are varied.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Applications", "weight": 1.0} -->

Friedman, Hastie, and Tibshirani propose a block CD algorithm for estimating a sparse inverse covariance matrix, given a sample covariance matrix $S$ and taking the variable in their formulation to be a modification $W$ of $S$, such that $W^{- 1}$ is sparse. The resulting "graphical lasso" algorithm cycles through the rows/columns of $W$ (in the style of block CD), solving a standard lasso problem to calculate each update. The same authors apply CD to generalized linear models such as linear least squares and logistic regression, with convex regularization terms. Their framework include such formulations as lasso, graphical lasso, elastic net, and the Dantzig selector, and is implemented in the package glmnet.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Applications", "weight": 1.0} -->

Chang, Hsieh, and Lin use cyclic and stochastic CD to solve a squared-loss formulation of the support vector machine (SVM) problem in machine learning, that is, where ${(x_{i},y_{i})} \in {{\mathbb{R}}^{N} \times {\{ 0,1\}}}$ are feature vector / label pairs and $\lambda$ is a regularization parameter. This problem is an important instance of the ERM form. In the best known early application of coordinate descent to SVM, Platt deals with a hinge-loss formulation of SVM, which is identical to except that the square on each term of the summation is omitted. The dual of this problem has bounds on its variables along with a single linear constraint. Platt's procedure SMO (for "sequential minimal optimization"), applied to the dual, changes two variables at a time, with the variable pair chosen according to a "greedy" criterion and the search direction chosen to maintain feasibility of the linear constraint.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Applications", "weight": 1.0} -->

Sardy, Bruce, and Tseng consider the basis-pursuit formulation of wavelet denoising: This formulation is equivalent to the well known lasso of Tibshirani and has become famous because of its applicability to sparse recovery and compressed sensing. Although this formulation fits the ERM framework and could thus be dualized before applying CD, the approach of applies block CD directly to the primal formulation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Applications", "weight": 1.0} -->

Applications of block CD approaches to transceiver design for cellular networks and to tensor factorization are discussed in Razaviyayn ( Section 8).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Applications", "weight": 1.0} -->

Finally, we mention several popular problem classes and algorithms that can be interpreted as CD algorithms, but for which such an interpretation may not be particularly helpful in understanding the performance of the algorithm. First, we consider low-rank matrix completion problems in which we are presented with limited information about a rectangular matrix $M \in {\mathbb{R}}^{m \times n}$ and seek matrices $U \in {\mathbb{R}}^{n \times r}$ and $V \in {\mathbb{R}}^{m \times r}$ (with $r$ small) such that $UV^{T}$ is consistent with the observations of $M$. When the observations satisfy a restricted isometry property (an assumption commonly made in compressed sensing; see ( Definition 3.1) for a definition that applies to matrix completion), the block CD approach of Jain, Netrapalli, and Sanghavi ( Algorithm 1) converges to a solution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Applications", "weight": 1.0} -->

This approach defines the objective to be the least-squares fit between the observations and their predicted values according to the product $UV^{T}$ --- a function that is nonconvex with respect to $(U,V)$ --- and minimizes alternately over $U$ and $V$, respectively. Standard analysis of CD for nonconvex functions would yield at best stationarity of accumulation points, but much stronger results are attained in because of special assumptions that are made on the problem in this paper.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Applications", "weight": 1.0} -->

Second, we consider the "alternating-direction method of multipliers" (ADMM) which has gained great currency in the past few years because of its usefulness in solving regularized problems in statistics and machine learning, and in designing parallel algorithms. Each major iteration of ADMM consists of an (approximate) minimization of the augmented Lagrangian function for a constrained optimization problem over each block of primal variables in turn, followed by an update to the Lagrange multiplier estimates. It might seem appealing to do multiple cycles of updating the primal variable blocks, in the manner of cyclic block CD, thus finding a better approximation to the solution of each subproblem over all primal variables and moving the method closer to the standard augmented Lagrangian approach. Eckstein and Yao show, however, that this "approximate augmented Lagrangian" approach has a fundamentally different theoretical interpretation from ADMM, and a computational comparison between the two approaches ( Section 5) appears to show an advantage for ADMM.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Coordinate Descent: Algorithms, Convergence, Implementations", "weight": 1.0} -->

We now describe the most important variants of coordinate descent and present their convergence properties, including the proofs of some fundamental results. We also discuss the implementation of accelerated CD methods for problems of the form and for the Kaczmarz algorithm for ${Aw} = b$. As mentioned in the introduction, we deal with the most elementary framework possible, to expose the essential properties of the methods.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Powell's Example", "weight": 1.0} -->

We start with a simple but intriguing example due to Powell (formula) of a function in ${\mathbb{R}}^{3}$ for which cyclic CD fails to converge to a stationary point. The nonconvex, continuously differentiable function $f:{{\mathbb{R}}^{3}\rightarrow{\mathbb{R}}}$ is defined as follows: It has minimizers at the corners ${}^{T}$ and ${({- 1},{- 1},{- 1})}^{T}$ of the unit cube, but coordinate descent with exact minimization, started near (but just outside of) one of the other vertices of the cube cycles around the neighborhoods of six points that are close to the six non-optimal vertices. Powell shows that the cyclic nonconvergence behavior is rather special and is destroyed by small perturbations on this particular example, and we can note that a randomized coordinate descent method applied to this example would be expected to converge to the vicinity of a solution within a few steps.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Powell's Example", "weight": 1.0} -->

Still, this example and others in make it clear that we cannot expect a general convergence result for nonconvex functions, of the type that are available for full-gradient descent. Results are available for the nonconvex case under certain additional assumptions that still admit interesting applications. Bertsekas (Proposition 2.7.1) describes convergence of a cyclic approach applied to nonconvex problems, under the assumption that the minimizer along any coordinate direction from any point $x$ is unique. More recent work; focuses on CD with two blocks of variables, applied to functions that satisfy the so-called Kurdyka-Łojasiewicz (KL) property, such as semi-algebraic functions. Convergence of subsequences or the full sequence $\{ x^{k}\}$ to stationary points can be proved in this setting.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumptions and Notation", "weight": 1.0} -->

For most of this section, we focus on the unconstrained problem, where the objective $f$ is convex and Lipschitz continuously differentiable. In some places, we assume strong convexity with respect to the Euclidean norm, that is, existence of a modulus of convexity $\sigma > 0$ such that (Henceforth, we use $\parallel \cdot \parallel$ to denote the Euclidean norm $\parallel \cdot \parallel_{2}$, unless otherwise specified.) We define Lipschitz constants that are tied to the component directions, and are key to the algorithms and their analysis. The first set of such constants are the component Lipschitz constants, which are positive quantities $L_{i}$ such that for all $x \in {\mathbb{R}}^{n}$ and all $t \in {\mathbb{R}}$ we have We define the coordinate Lipschitz constant $L_{\text{max}}$ to be such that The standard Lipschitz constant $L$ is such that for all $x$ and $d$ of interest.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumptions and Notation", "weight": 1.0} -->

By referring to relationships between norm and trace of a symmetric matrix, we can assume that $1 \leq {L/L_{\text{max}}} \leq n$. (The upper bound is achieved when ${f{(x)}} = {e{({e^{T}x})}}$, for $e = {(1,1,\ldots,1)}^{T}$.) We also define the restricted Lipschitz constant $L_{\text{res}}$ such that the following property is true for all $x \in {\mathbb{R}}^{n}$, all $t \in {\mathbb{R}}$, and all $i = {1,2,\ldots,n}$: Clearly, $L_{\text{res}} \leq L$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumptions and Notation", "weight": 1.0} -->

The ratio is important in our analysis of asynchronous parallel algorithms in Section 4. In the case of $f$ convex and twice continuously differentiable, we have by positive semidefiniteness of the ${\nabla^{2}f}{(x)}$ at all $x$ that from which we can deduce that However, we can derive stronger bounds on $\Lambda$ for functions $f$ in which the coupling between components of $x$ is weak. In the extreme case in which $f$ is separable, we have $\Lambda = 1$. The coordinate Lipschitz constant corresponds $L_{\text{max}}$ to the maximal absolute value of the diagonal elements of the Hessian ${\nabla^{2}f}{(x)}$, while the restricted Lipschitz constant $L_{\text{res}}$ is related to the maximal column norm of the Hessian. Therefore, if the Hessian is positive semidefinite and diagonally dominant, the ratio $\Lambda$ is at most $2$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumptions and Notation", "weight": 1.0} -->

The following assumption is useful in the remainder of the paper.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The function $f$ in is convex and uniformly Lipschitz continuously differentiable, and attains its minimum value $f^{\ast}$ on a set $\mathcal{S}$. There is a finite $R_{0}$ such that the level set for $f$ defined by $x^{0}$ is bounded, that is,

<!-- chunk {"id": "body-0046", "role": "body", "section": "Randomized Algorithms", "weight": 1.0} -->

In randomized CD algorithms, the update component $i_{k}$ is chosen randomly at each iteration. In Algorithm 3 we consider the simplest variant in which each $i_{k}$ is selected from $\{ 1,2,\ldots,n\}$ with equal probability, independently of the selections made at previous iterations. (We can think of this scheme as "sampling with replacement" from the set $\{ 1,2,\ldots,n\}$.)

<!-- chunk {"id": "body-0047", "role": "body", "section": "Randomized Algorithms", "weight": 1.0} -->

Choose index ik with uniform probability from {1, 2, …, n}, independently of choices at prior iterations; Set xk + 1 ← xk − αk [∇f (xk)]ik eik for some αk > 0; until termination test satisfied; Algorithm 3 Randomized Coordinate Descent for We denote expectation with respect to a single random index $i_{k}$ by $E_{i_{k}}{(\cdot)}$, while $E{(\cdot)}$ denotes expectation with respect to all random variables $i_{0},i_{1},i_{2},\ldots$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Randomized Algorithms", "weight": 1.0} -->

We prove a convergence result for the randomized algorithm, for the simple steplength choice $\alpha_{k} \equiv {1/L_{\text{max}}}$. (The proof is a simplified version of the analysis in Nesterov ( Section 2). A result similar to is proved by Shalev-Schwartz and Tewari for certain types of $\ell_{1}$-regularized problems.)

<!-- chunk {"id": "body-0049", "role": "body", "section": "Randomized Kaczmarz Algorithm", "weight": 1.0} -->

It is worth proving an expected linear convergence result for the Kaczmarz iteration for linear equations ${Aw} = b$ as a separate, more elementary analysis. In one sense, the result is a special case of Theorem 3.1 since, as we showed above, the iteration is obtained by applying Algorithm 3 to the dual formulation. In another sense, the result is stronger, since we obtain a linear rate of convergence without requiring strong convexity of the objective, that is, the system ${Aw} = b$ is allowed to have multiple solutions.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Randomized Kaczmarz Algorithm", "weight": 1.0} -->

We denote by $\lambda_{\min,{nz}}$ the minimum nonzero eigenvalue of $AA^{T}$ and let $P{(\cdot)}$ denote projection onto the solution set of ${Aw} = b$. We have where we have used normalization of the rows and the fact that ${A_{i_{k}}P{(x^{k})}} = b_{i_{k}}$. By taking expectations of both sides with respect to $i_{k}$, we have By taking expectations of both sides with respect to all random variables $i_{0},i_{1},\ldots$, and proceeding recursively, we obtain (This analysis is slightly generalized from Strohmer and Vershynin to allow for nonunique solutions of ${Aw} = b$; see also.)

<!-- chunk {"id": "body-0051", "role": "body", "section": "Accelerated Randomized Algorithms", "weight": 1.0} -->

The accelerated randomized algorithm, specified here as Algorithm 4, was proposed by Nesterov. It assumes that an estimate is available of modulus of strong convexity $\sigma \geq 0$, as well as estimates of the component-wise Lipschitz constants $L_{i}$. (The algorithm remains valid if we simply use $L_{\text{max}}$ in place of $L_{i_{k}}$ for all $k$.)

<!-- chunk {"id": "body-0052", "role": "body", "section": "Accelerated Randomized Algorithms", "weight": 1.0} -->

Choose γk to be the larger root of $${{\gamma_{k}^{2} - \frac{\gamma_{k}}{n}} = {\left({1 - \frac{\gamma_{k}\sigma}{n}} \right)\gamma_{k - 1}^{2}}}.$$ $${{\alpha_{k}\leftarrow\frac{n - {\gamma_{k}\sigma}}{\gamma_{k}{({n^{2} - \sigma})}}},{\beta_{k}\leftarrow{1 - \frac{\gamma_{k}\sigma}{n}}}};$$ Choose index ik ∈ {1, 2, …, n} with uniform probability and set dk = [∇f (yk)]ik eik; until termination test satisfied; Algorithm 4 Accelerated Randomized Coordinate Descent for The approach is a close relative of the accelerated (full-)gradient methods that have become extremely popular in recent years.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Accelerated Randomized Algorithms", "weight": 1.0} -->

These methods have their origin in a 1983 paper of Nesterov and owe much of their recent popularity to a recent incarnation known as FISTA and an exposition in Nesterov's 2004 monograph, as well as ease of implementation and good practical experience. In their use of momentum in the choice of step --- the search direction combines new gradient information with the previous search direction --- these methods are also related to such other classical techniques as the heavy-ball method (see) and conjugate gradient methods.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Accelerated Randomized Algorithms", "weight": 1.0} -->

Nesterov ( Theorem 6) proves the following convergence result for Algorithm 4.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

1}\leftarrow{{{\beta_{k}{\overset{\sim}{v}}^{k}} + {{({1 - \beta^{k}})}{\overset{\sim}{y}}^{k}}} - {\gamma_{k}{\overset{\sim}{d}}^{k}}}$; until termination test satisfied; Algorithm 5 Accelerated Randomized Kaczmarz, One fact detracts from the appeal of accelerated CD methods over standard methods: the higher cost of each iteration of Algorithm 4. Both standard and accelerated variants require calculation of one element of the gradient, but Algorithm 3 requires an update of just a single component of $x$, whereas Algorithm 4 also requires manipulation of the generally dense vectors $y$ and $v$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

Moreover, the gradient is evaluated at $x^{k}$ in Algorithm 3, where the argument changes by only one component from the prior iteration, a fact that can be exploited in several contexts. In Algorithm 4, the argument $y^{k}$ for the gradient changes more extensively from one iteration to the next, making it less obvious whether such economies are available. However, by using a change of variables due to Lee and Sidford, it is possible to implement the accelerated randomized CD approach efficiently for problems with certain structure, including the linear system ${Aw} = b$ and certain problems of the form.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

We explain the Lee-Sidford technique in the context of the Kaczmarz algorithm, assuming normalization of the rows of $A$. As we explained, the Kaczmarz algorithm is obtained by applying CD to the dual formulation with variables $x$, but operating in the space of "primal" variables $w$ using the transformation $w = {A^{T}x}$. If we apply the transformations ${\overset{\sim}{v}}^{k} = {A^{T}v^{k}}$ and ${\overset{\sim}{y}}^{k} = {A^{T}y^{k}}$ to the other vectors in Algorithm 4, and use the fact of normalization (and hence ${({AA^{T}})}_{ii} = 1$ for all $i = {1,2,\ldots,m}$) to note that $L_{i} \equiv 1$, we obtain Algorithm 5.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

When the matrix $A$ is dense, there is only a small factor of difference between the per-iteration workload of the standard Kaczmarz algorithm and its accelerated variant, Algorithm 5. Both require $O{({m + n})}$ operations per iteration. However, when $A$ is sparse, the computational difference between the two algorithms becomes substantial. At iteration $k$, the standard Kaczmarz algorithm requires computation proportion to a small multiple of the number of nonzeros in row $A_{i_{k}}$ (which we denote by $|A_{i_{k}}|$). Meanwhile, iteration $k$ of Algorithm 5 requires manipulation of the dense vectors ${\overset{\sim}{v}}^{k}$ and ${\overset{\sim}{y}}^{k}$ --- both $O{(n)}$ processes --- and the benefits of sparsity are lost.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

This apparent defect was partly remedied in by "caching" the updates to these vectors, resulting in a number of cycles within which updates gradually "fill." The more effective approach of performs a change of variables from ${\overset{\sim}{v}}^{k}$ and ${\overset{\sim}{y}}^{k}$ to two other vectors ${\hat{v}}^{k}$ and ${\hat{y}}^{k}$ that can be updated in $O{({|A_{i_{k}}|})}$ operations.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

To describe this representation, we start by noting that if we substitute for $w^{k}$ and $w^{k + 1}$ in the formulas of Algorithm 5, we obtain the updates to ${\overset{\sim}{v}}^{k}$ and ${\overset{\sim}{y}}^{k}$ in the following form: Note that $R_{k}$ is a $2 \times 2$ matrix while $S_{k}$ is an $n \times 2$ matrix with nonzeros only in those rows for which $A_{i_{k}}^{T}$ has a nonzero entry. We define a change of variables based on another $2 \times 2$ matrix $B_{k}$, as follows: where we initialize with $B_{0} = I$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

By substituting this representation into, we obtain so we can maintain validity of the representation at iteration $k + 1$ by setting The computations in can be performed in $O{({|A_{i_{k}}|})}$ operations, and can replace the relatively expensive computations of ${\overset{\sim}{y}}^{k}$ and ${\overset{\sim}{v}}^{k + 1}$ in Algorithm 5. The only other operation of note in this algorithm --- computation of ${A_{i_{k}}{\overset{\sim}{y}}^{k}} - b_{i_{k}}$ --- can also be performed in $O{({|A_{i_{k}}|})}$ operations using the $({\hat{v}}^{k},{\hat{y}}^{k})$ representation, by noting from that This efficient implementation can be extended to the dual empirical risk minimization problem for certain choices of regularization function

<!-- chunk {"id": "body-0062", "role": "body", "section": "Efficient Implementation of the Accelerated Algorithm", "weight": 1.0} -->

As pointed out, the key requirement for the efficient scheme is that the gradient term ${\lbrack{{\nabla f}{(y^{k})}}\rbrack}_{i_{k}}$ can be evaluated efficiently after an update to the two vectors in the alternative representation of $y^{k}$, and to the two coefficients in this representation. Another variant of this implementation technique appears in (Section 5).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Cyclic Variants", "weight": 1.0} -->

We have the following result from for the cyclic variant of Algorithm 1.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Extension to Separable Regularized Case", "weight": 1.0} -->

In this section we consider the separable regularized formulation, where $f$ is smooth and strongly convex, and each $\Omega_{i}$, $i = {1,2,\ldots,n}$ is convex. We prove a result similar to the second part of Theorem 3.1 for a randomized version of Algorithm 2. The proof is a simplified version of the analysis. It makes use of the following assumption.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The function $f$ in is uniformly Lipschitz continuously differentiable and strongly convex with modulus $\sigma > 0$ (see ). The functions $\Omega_{i}$, $i = {1,2,\ldots,n}$ are convex. The function $h$ in attains its minimum value $h^{\ast}$ at a unique point $x^{\ast}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Our result uses the coordinate Lipschitz constant $L_{\text{max}}$ for $f$, as defined. Note that the modulus of convexity $\sigma$ for $f$ is also the modulus of convexity for $h$. By elementary results for convex functions, we have

<!-- chunk {"id": "body-0067", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

A full computational comparison between variants of CD (and between CD and other methods) is beyond the scope of this paper. Nevertheless it is worth asking whether various aspects of the convergence analysis presented above --- in particular, the distinction between CD variants --- can be observed in practice. To this end, we used these methods to minimize a convex quadratic ${f{(x)}} = {{({1/2})}x^{T}Qx}$ (with $Q$ symmetric and positive semidefinite) for which $x^{\ast} = 0$ and $f^{\ast} = 0$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

We constructed $Q$ by choosing an integer $r$ from $1,2,\ldots,n$ and parameters $\eta \in {\lbrack 0,1\rbrack}$ and $\zeta > 0$, and defining where $V \in {\mathbb{R}}^{n \times r}$ is a random matrix with $r \leq n$ orthogonal columns, $\Sigma$ is an $r \times r$ positive diagonal matrix whose diagonal elements were chosen from a log-uniform distribution to have a specified condition number (with maximum diagonal of $1$), and $\mathbf{1}$ is the vector ${(1,1,\ldots,1)}^{T}$. For convenience, we normalized $Q$ so that its maximum diagonal --- and thus $L_{\text{max}}$ --- is $1$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

By choosing $\eta$ and $\zeta$ appropriately, we can obtain a range of values for the quantities described in Subsection 3.2, which enter along with the smallest singular value into the convergence expression. For example, by setting $\zeta = 0$ and $\eta = 0$ we obtain a randomly oriented matrix, possibly singular, with a specified range of nonzero eigenvalues. Nonzero values of $\eta$ and $\zeta$ induce different types of orientation bias. In particular, we see that $\Lambda$ increases toward its upper bound of $\sqrt{n}$ as $\zeta$ increases away from zero.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

IID: Randomized CD using sampling with replacement: Algorithm 3.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

EPOCHS: The "sampling without replacement" variant of Algorithm 3, described following the proof of Theorem 3.1.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

For each variant, we tried both a fixed steplength $\alpha_{k} \equiv {1/L_{\text{max}}}$ and the optimal steplength $\alpha_{k} = {1/Q_{i_{k},i_{k}}}$. Thus, there were a total of six algorithmic variants tested.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

The starting point $x^{0}$ was chosen randomly, with all components from the unit normal distribution $N{}$. The algorithms were terminated when the objective was reduced by a factor of $10^{- 6}$ over its initial value $f{(x^{0})}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Computational Notes", "weight": 1.0} -->

The speed of convergence varied widely according to the problem construction parameters $\eta$, $\lambda$, and $\text{cond}{(\Sigma)}$, but we can make some general observations. First, on problems that are not well conditioned, the function values $f{(x^{k})}$ decreased rapidly at first, then settled into a linear rate of decrease. This linear rate held even for problems in which $Q$ was singular --- a significant improvement over the sublinear rates predicted by the theory. Second, the EPOCHS variant of randomized CD tended to converge faster than the IID version, though rarely more than twice as fast. Third, the use of the optimal step was usually better than the fixed step (with sometimes up to six times fewer iterations), but this was by no means always the case. Fourth, while there were extensive regimes of parameter values in which all six variants performed similarly, there were numerous "stressed" settings in which the CYCLIC variants are much slower than the randomized variants, by factors of $10$ or more.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Parallel CD Algorithms", "weight": 1.0} -->

CD methods lend themselves to different kinds of parallel implementation. Even basic algorithm frameworks such as Algorithm 1 may be amenable to application-specific parallelism, when the computations involved in evaluating a single element of the gradient vector are substantial enough to be spread out across cores of a multicore computer. We concern ourselves here with more generic forms of parallelism, which involve multiple instances of the basic CD algorithm, running in parallel on multiple processors.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Parallel CD Algorithms", "weight": 1.0} -->

We can distinguish different types of parallel CD algorithms. Synchronous algorithms are those that partition the computation into pieces that can be executed in parallel on multiple processors (or cores of a multicore machine), but that synchronize frequently across all processors, to ensure consistency of the information available to all processors at certain points in time. For example, each processor could update a subset of components of $x$ in parallel (with the subsets being disjoint), and the synchronization step could ensure that the results of all updates are shared across all processors before further computation occurs. The synchronization step often detracts from the performance of algorithms, not only because some processors may be forced to idle while others complete their work, but also because the overheads associated with (hardware and software) locking of memory accesses can be high. Thus, asynchronous methods, which weaken or eliminate the requirement of consistent information across processors, are preferred in practice. Analysis of such methods is more difficult, but results have been obtained that accord with practical experience of such methods. Indeed, it can be verified that in certain regimes, linear speedup can be expected across a modest number of processors.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Synchronous Parallelism", "weight": 1.0} -->

We mention several synchronous parallel variants of CD that appear in the recent literature. We note that in the some of these papers, the computational results were obtained by implementing the methods in an asynchronous fashion, disregarding the synchronization step required by the analysis.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Synchronous Parallelism", "weight": 1.0} -->

Bradley at al. consider a bound-constrained problem that is a reformulation of the problem with specific choices of $f$ and with ${\Omega{(x)}} = {\| x\|}_{1}$. Their algorithm performs short-step updates of individual components of $x$ in parallel on $P$ processors, with synchronization after each round of parallel updating. This scheme essentially updates a randomly-chosen block of $P$ variables at each cycle. By modifying the analysis of, they show that the $1/k$ sublinear convergence rate bound is not affected provided that $P$ is no larger than $n/L$, where $L$ is the Lipschitz constant.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Synchronous Parallelism", "weight": 1.0} -->

Jaggi et al. perform a synchronized CD method on the dual ERM model for the case of ${g{(w)}} = {g^{\ast}{(w)}} = {{({1/2})}{\| w\|}^{2}}$, partitioning components of the dual variable $x$ between cores and sharing a copy of the vector $Ax$ across cores, updating this vector at each synchronization point. The approach can be thought of as a nonlinear block Gauss-Jacobi method (by contrast with the coordinate Gauss-Seidel approaches discussed in Section 3).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Synchronous Parallelism", "weight": 1.0} -->

Richtarik and Takac describe a method for the separably regularized formulation, in which a subset of indices $S_{k} \subset {\{ 1,2,\ldots,n\}}$ is updated according to the formula in Algorithm 2. The work of updating the components in $S_{k}$ is divided between processors; essentially, a synchronization step takes place at each iteration. This scheme is enhanced with an acceleration step; the extra computations associated with the acceleration step too are parallelized, using ideas. In the scheme of Marecek, Richtarik, and Takac, the variable vector $x$ is partitioned into subvectors, and each processor is assigned the responsibility for updating one of these subvectors. On each processor, the updating scheme described in is applied, providing a second level of parallelism. Synchronization takes place at each outer iteration. Details of the information-sharing between processors required for accurate computation of gradients in different applications are described in ( Section 6).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

In asynchronous variants of CD, the variable vector $x$ is assumed to be accessible to each processor, available for reading and updating. (For example, $x$ could be stored in the shared-memory space of a multicore computer, where each core is viewed as a processor.) Each processor runs its own CD process, shown here as Algorithm 6, without any attempt to coordinate or synchronize with other processors. Each iteration on each processor chooses an index $i$, loads the components of $x$ that are needed to compute the gradient component ${\lbrack{{\nabla f}{(x)}}\rbrack}_{i}$, then updates the $i$th component $x_{i}$. Note that this evaluation may need only a small subset of the components of $x$; this is the case when the Hessian $\nabla^{2}f$ is structurally sparse, for example.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

On some multicore architectures (for example, the Intel Xeon), the update of $x_{i}$ can be performed as a unitary operation; no software or hardware locking is required to block access of other cores to the location $x_{i}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

Evaluate [∇f (x)]i, reading components of x from shared memory as necessary; Update xi ← xi − α [∇f (x)]i for some α > 0; Algorithm 6 Coordinate Descent for (running on each Processor) We can take a global view of the entire parallel process, consisting of multiple processors each executing Algorithm 6, by defining a global counter $k$ that is incremented whenever any processor updates an element of $x$: see Algorithm 7. Note that the only difference with the basic framework of Algorithm 1 is in the argument of the gradient component: In Algorithm 1 this is the latest iterate $x^{k}$ whereas in Algorithm 7 it is a vector ${\hat{x}}^{k}$ that is generally made up of components of vectors from previous iterations $x^{j}$, $j = {0,1,\ldots,k}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

The reason for this discrepancy is that between the time at which a processor reads the vector $x$ from shared storage in order to calculate ${\lbrack{{\nabla f}{(x)}}\rbrack}_{i}$, and the time at which it updates component $i$, other processors have generally made changes to $x$. In consequence, each update step is using slightly stale information about $x$. To prove convergence results, we need to make assumptions on how much "staleness" can be tolerated, and to modify the convergence analysis quite substantially. Indeed, proofs of convergence even for the most basic asynchronous algorithms are quite technical.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

Set k ← 0 and choose x0 ∈ ℝn; xk + 1 ← xk − αk [∇f (x̂k)]ik eik for some αk > 0; until termination test satisfied; Algorithm 7 Asynchronous Coordinate Descent for Asynchronous CD algorithms are distinguished from each other mostly by the assumptions they make on the the choice of update components $i_{k}$ and on the "ages" of the components of ${\hat{x}}^{k}$, that is, the iterations at which each component of this vector was last updated.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

In the terminology of Bertsekas and Tsitsiklis, the algorithm is totally asynchronous if each index $i \in {\{ 1,2,\ldots,n\}}$ of $x$ is updated at infinitely many iterations; and if $\nu_{j}^{k}$ denotes the iteration at which component $j$ of the vector ${\hat{x}}^{k}$ was last updated, then $\nu_{j}^{k}\rightarrow\infty$ as $k\rightarrow\infty$ for all $j = {1,2,\ldots,n}$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

In other words, each component of $x$ is updated infinitely often, and all components used in successive evaluation vectors ${\hat{x}}^{k}$ are also updated infinitely often.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Asynchronous Parallelism", "weight": 1.0} -->

The following convergence result for totally asynchronous variants of Algorithm 7 is due to Bertsekas and Tsitsiklis; see in particular ( Sections 6.1, 6.2, and 6.3.3).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have surveyed the state of the art in convergence of coordinate descent methods, with a focus on the most elementary settings and the most fundamental algorithms. The recent literature contains many extensions, enhancements, and elaborations; we refer interested readers to the bibliography of this paper, and note that new works are appearing at a rapid pace.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Coordinate descent method have become an important tool in the optimization toolbox that is used to solve problems that arise in machine learning and data analysis, particularly in "big data" settings. We expect to see further developments and extensions, further customization of the approach to specific problem structures, further adaptation to various computer platforms, and novel combinations with other optimization tools to produce effective "solutions" for key application areas.
