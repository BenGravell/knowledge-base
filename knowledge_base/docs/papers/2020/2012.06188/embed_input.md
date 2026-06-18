<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Recent Theoretical Advances in Non-Convex Optimization

Topics include Convex optimization, Neural networks, Optimization, Stationary point, Optimization problem, Convex function.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motivated by recent increased interest in optimization algorithms for non-convex optimization in application to training deep neural networks and other optimization problems in data analysis, we give an overview of recent theoretical results on global performance guarantees of optimization algorithms for non-convex optimization. We start with classical arguments showing that general non-convex problems could not be solved efficiently in a reasonable time. Then we give a list of problems that can be solved efficiently to find the global minimizer by exploiting the structure of the problem as much as it is possible. Another way to deal with non-convexity is to relax the goal from finding the global minimum to finding a stationary point or a local minimum. For this setting, we first present known results for the convergence rates of deterministic first-order methods, which are then followed by a general theoretical analysis of optimal stochastic and randomized gradient schemes, and an overview of the stochastic first-order methods. After that, we discuss quite general classes of non-convex problems, such as minimization of alpha-weakly-quasi-convex functions and functions that satisfy Polyak-Lojasiewicz condition, which still allow obtaining theoretical convergence guarantees of first-order methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Then we consider higher-order and zeroth-order/derivative-free methods and their convergence rates for non-convex optimization problems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this survey, we consider non-convex optimization problems in different settings, including stochastic optimization. We are mainly motivated by an increased interest in such problems in connection to applications in machine learning and data analysis, and our main focus is on the methods which possess theoretical guarantees for their global convergence rate or complexity. As we explain first by providing classical examples murty1987some; nesterov2018lectures, there is no hope to have any theoretical guarantees for finding a global minimizer in a general non-convex optimization problem in a reasonable time. Despite the quite good practical performance of classical general-purpose methods such as L-BFGS nocedal2006numerical; floudas2008encyclopedia, and proven local superlinear convergence, their global complexity is not well understood.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the last 20 years, theoretical analysis of the global convergence rate or global complexity guarantees has become de facto a standard in the area of numerical optimization. Since the convexity of the problem allows for such an analysis, many global complexity and convergence results have been obtained in convex optimization ben-tal2001lectures; bubeck2015convex; nesterov2018lectures; lan2020first; dvurechensky2020advances; dvurechensky2021first-order. Recent advances in machine learning, which were made possible by the application of neural networks, had lead to the optimization community changing focus to non-convex optimization and, especially to stochastic non-convex optimization. In this non-exhaustive survey, we attempt to highlight existing results on global performance guarantees of large-scale non-convex optimization methods. The large dimension of the decision variable in such problems motivates the use of first-order methods, which possess a cheap iteration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the large amount of data motivates to use randomized methods such as stochastic gradient descent, which does not require to look through the whole dataset to make one step of the optimization procedure, thus making the iteration even cheaper.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since, in general, non-convex optimization problems cannot be made efficiently solved, we consider several ways to relax this challenging goal. The first relaxation consists of finding problems with hidden convexity or in a convex reformulation of the problem. This requires exploitation of the problem structure as much as it is possible, which limits the generality of the approach, yet leading to a possibility to find a global solution. Another way is to change the goal from finding the global solution to finding a stationary point or a local extremum. In this case, it is possible to obtain polynomial dependence of the complexity of first-order methods on the dimension of the problem and desired accuracy. We consider this approach in the setting of deterministic and stochastic optimization. The third way is to define a class of non-convex problems, which is, on the one hand, quite general, and on the other hand, allows to obtain a global performance guarantees of an algorithm. We consider a class of problems with objective satisfying Polyak--Łojasiewicz condition, which leads to global linear convergence rate, and the class of problems with $\alpha$-weakly-quasi-convex objective, which leads to global sublinear convergence rate.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the above two approaches, we first focus on first-order methods. Then, motivated by several settings in machine learning such as reinforcement learning, black-box adversarial attacks on neural networks, as well as simulation optimization, in which the gradient of the objective is not available, we consider zeroth-order or derivative-free methods and their convergence rates for non-convex optimization problems. By no means we claim that our survey contains all the important results in this area since the literature is huge and we could miss some recent results. We would like to list here some other books polyak1987introduction; conn2009introduction; lan2020first; GasnikovBook and surveys jain2017non-convex; curtis2017optimization; wright2018optimization; chen2018harnessing; chi2018nonconvex; sun2019optimization; zhang2020from related to our paper^11^1See also this webpage with the list of references being updated

<!-- chunk {"id": "body-0009", "role": "body", "section": "Global Optimization is NP-hard", "weight": 1.0} -->

Following murty1987some, we consider an example which illustrates that the problem of finding the exact global solution of a non-convex problem is NP-hard. To that end, we consider the minimization problem

<!-- chunk {"id": "body-0010", "role": "body", "section": "Global Optimization is NP-hard", "weight": 1.0} -->

where $x_{i}$ is the $i$-th component of the vector $x$. Let $A = {I - {\frac{1}{n}\mathbf{1}\mathbf{1}^{\top}}}$, where $I$ is the identity matrix of size $n$ and $\mathbf{1}$ is a vector of $n$ ones, and let ${\lbrack x\rbrack}^{2}$ denote a vector with components ${\lbrack x\rbrack}_{i}^{2} = x_{i}^{2}$. In this notation, the objective takes the form

<!-- chunk {"id": "body-0011", "role": "body", "section": "Global Optimization is NP-hard", "weight": 1.0} -->

Since $A$ is a positive semidefinite matrix, ${f{(x)}} \geqslant 0$. One may also note that 0 is an eigenvalue of $A$ with multiplicity $1$ and that $\mathbf{1}$ is the corresponding eigenvector. With this in mind, it is not difficult to see that ${f{(x)}} = 0$ if and only if $x$ satisfies

<!-- chunk {"id": "body-0012", "role": "body", "section": "Global Optimization is NP-hard", "weight": 1.0} -->

The problem of checking whether this equation has a solution is a form of the subset sum problem, which is known to be NP-complete. Since this problem has a solution if and only if the global minimum in the original optimization problem is exactly zero, this implies that the problem of finding even the value of a global minimum for a non-convex objective is NP-hard.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Lower Complexity Bound for Global Optimization", "weight": 1.0} -->

Following nesterov2018lectures, we now derive a lower bound for the complexity of finding an approximate global minimum of a possibly non-convex objective. Consider the problem

<!-- chunk {"id": "body-0014", "role": "body", "section": "Lower Complexity Bound for Global Optimization", "weight": 1.0} -->

where $f$ is possibly non-convex and Lipschitz-continuous function, i.e., for some $M > 0$ and for all ${x,y} \in \lbrack 0,1\rbrack^{n}$

<!-- chunk {"id": "body-0015", "role": "body", "section": "Lower Complexity Bound for Global Optimization", "weight": 1.0} -->

Such constant exists for all continuous functions $f{(x)}$ on ${\lbrack 0,1\rbrack}^{n}$, so this assumption is not restrictive. Let us set the desired accuracy in terms of the objective as $\varepsilon$, i.e., our goal is to find a point $\hat{x}$ such that ${{f{(\hat{x})}} - f^{\ast}} \leqslant \varepsilon$, where $f^{\ast}$ is the global minimum of $f$ on $\lbrack 0,1\rbrack^{n}$. For simplicity, we assume $\varepsilon$ to be equal to $1/N$ for some $N \in {\mathbb{N}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Lower Complexity Bound for Global Optimization", "weight": 1.0} -->

Consider a family of continuous non-convex objectives $f_{k}{(x)}$, $k = {1,\ldots,N^{n}}$, constructed as follows: we divide the hypercube ${\lbrack 0,1\rbrack}^{n}$ into ${({{MN}/2})}^{n}$ non-intersecting hypercubes $C_{k}$ with side length $2/\left( {NM} \right)$ and set

<!-- chunk {"id": "body-0017", "role": "body", "section": "Lower Complexity Bound for Global Optimization", "weight": 1.0} -->

where $\partial C_{k}$ is the boundary of $C_{k}$ and $\text{dist}_{\infty}{(x,{\partial C_{k}})}$ is the distance between $x$ and $\partial C_{k}$ in the $\parallel \cdot \parallel_{\infty}$-norm. Each $f_{k}$ has a minimum value of exactly $- \varepsilon$ attained at the center of $C_{k}$, and the Lipschitz constant of $f_{k}$ is equal to $M$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Lower Complexity Bound for Global Optimization", "weight": 1.0} -->

Any minimization method generating its trajectory based on the values of $f{(x)}$ and its derivatives at the points of the trajectory would need to sample a point from each $C_{k}$ to find an approximate minimum of each $f_{k}{(x)}$. This gives us a lower bound on the number of iterations required: ${{\Omega{({({MN})}^{n})}} = {\Omega{({M^{n}\varepsilon^{- n}})}}}.$ And this bound is attained by the algorithm which simply samples the objective values at the vertices of a uniform grid and returns the point with the smallest value. This demonstrates that it is practically impossible to solve a high-dimensional non-convex minimization problem with any reasonable accuracy unless some additional assumptions are introduced.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Lower Complexity Bound for Global Optimization", "weight": 1.0} -->

A similar complexity bound is proved in nesterov2012make for finding a point $\hat{x}$ such that ${\|{{\nabla f}{(\hat{x})}}\|}_{\infty} \leqslant \varepsilon$ and ${\|\hat{x}\|}_{\infty} \leqslant R$. More precisely, for non-convex functions with Lipschitz continuous Hessian, such that there exists at least one point $x^{\ast}$ with ${{\nabla f}{(x^{\ast})}} = 0$ and ${\| x^{\ast}\|}_{\infty} \leqslant R$, the lower complexity bound is $\Omega\left( \left( {{MR^{2}}/\varepsilon} \right)^{n/2} \right)$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Examples of Non-Convex Problems", "weight": 1.0} -->

In this subsection, we make a non-extensive overview of non-convex problem formulations and applications where they arise, with a focus on tractable problems.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Examples of Non-Convex Problems", "weight": 1.0} -->

problems with hidden convexity or analytic solutions;

<!-- chunk {"id": "body-0022", "role": "body", "section": "Examples of Non-Convex Problems", "weight": 1.0} -->

problems with provable global solution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Examples of Non-Convex Problems", "weight": 1.0} -->

Let us consider formulations of a few concrete problems in each of these classes.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

Firstly, it is worth noting a broad class of classical non-convex problems that include linear-fractional programs, geometric programs, problems with two quadratic functions, handling convex equality constraints, convexifying constraint sets. Many such problems are equivalent to convex problems via a simple transformation such as convex relaxation and duality boyd2004convex.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

Next, a wide range of tasks in machine learning and statistics is reduced to eigenproblems. Among these problems are the following principal component analysis, classical multidimensional scaling, and other generalized eigenvalue problems charisopoulos2020entrywise.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

In the context of non-convex optimization problems, one cannot but mention the class of combinatorial optimization problems as graph problems. Basically, most of these problems are NP-complete, but despite this, there are effective approaches and ways to solve them. Let us consider a closer look at the MAX-CUT problem. This is a bright example of convex reformulations. In some problems, the goal is to find a point with a value as small as possible (or as large as possible in the context of maximization problems), but whether this point is close to the global minimum is not that important. In this case, we can try to approximate the problem with a simpler one and show that the exact solution to the approximate problem corresponds to a good solution of the original problem. We will first illustrate this idea on the MAX-CUT problem

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

where $A = \left\| A_{ij} \right\|_{{{i,j} = 1},1}^{n,n}$ ($A = A^{T})$. This is a discrete optimization problem. If we are interested only in the value of the functional and not in the cut itself, we can approximate this problem with a computationally tractable one. Let us introduce matrix

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

A simple observation: if $\varsigma$ is a random vector uniformly distributed on the Hamming cube $\left\{ {- 1},1 \right\}^{n}$, then

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

In fact, we can do better due to the construction of Goemans and Williamson goemans1995improved

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

This is an SDP problem. Let $\Sigma$ be the solution of this SDP problem and let

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

where $\alpha_{GW} \approx 0.878567$, and this constant is unimprovable provided that $\text{P} \neq \text{NP}$ and the Unique games conjecture is true khot2007optimal.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

Further, we would like to highlight the following subclasses of non-convex problems: non-convex proximal operators (Hard-thresholding blumensath2009iterative, Potts minimization kiefer2020iterative ), discrete problems (Binary graph segmentation, Discrete Potts minimization, Nearly optimal $K$-means), infinite-dimensional problems (Smoothing splines, Locally adaptive regression splines, Reproducing kernel Hilbert spaces) and statistical problems.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

Another important practical example we would like to mention in this part is Blind Deconvolution. Convolutional models arise in a wide range of problems in image processing and computer vision. The most basic convolutional data model -- blind deconvolution aims to recover a convolution kernel $a_{0} \in {\mathbb{R}}^{k}$ and signal $x_{0} \in {\mathbb{R}}^{m}$ from their convolution

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

where $y \in {\mathbb{R}}^{m}$ and $\circledast$ is some kind of convolution. This problem is ill-posed in general --- there are infinitely many $(a_{0},x_{0})$ that convolve to produce $y$. To overcome this issue, some low dimensional priors about $a_{0}$ and $x_{0}$ are necessary. As a result, it is essential to use additional constraints and regularization terms. Different priors produce different non-convex optimization problems: Sparse Blind Deconvolution qu2019nonconvex, Multi-channel Sparse Blind Deconvolution shi2020manifold, Subspace blind deconvolution li2016identifiability, Convolutional dictionary learning papyan2017convolutional.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

The seen data in many settings in science and engineering are admixtures of several latent sources. Given the observations, we would normally wish to infer the latent sources as well as the admixture distribution. The non-negative matrix factorization (NMF) ge2015intersecting mathematical framework offers a natural mathematical framework for modeling numerous mixing problems. In NMF, each row of observation matrix $M \in {\mathbb{R}}^{n \times m}$ corresponds to a data-point in ${\mathbb{R}}^{m}$. Next, the following assumptions are used: 1) there are $r$ latent sources, encoded by the unobserved matrix $W \in {\mathbb{R}}^{r \times m}$, and 2) each observed data-point can be rewritten as a linear combination of the $r$ sources, the weights of combination are defined via matrix $A \in {\mathbb{R}}^{n \times r}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

The goal is to find such representation of matrix $M$ that $M = {AW}$ with the entries of $M$, $A$ and $W$ being non-negative. The number $r$ is called the inner-dimension of the factorization, and the smallest possible $r$ is the nonnegative rank of $M$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

Finally, in the part devoted to problems with Hidden Convexity or Analytical Solution we would like deal with Compressed Sensing and L1-optimization. A vector is said to be $s$-sparse if it has at most $s$ non-zero elements. Consider solving ${Ax} = b$ for $x$ where $A$ is an $n \times d$ matrix with $n < d$. The set of solutions to ${Ax} = b$ is a subspace. However, if we restrict ourselves to $s$-sparse solutions, under certain conditions on $A$ there is a unique sparse solution blum2016foundations. For instance, suppose that there were two $s$-sparse solutions $x_{1}$ and $x_{2}$. Then $x_{1} - x_{2}$ would be a $2s$-sparse solution to the homogeneous system ${Ax} = 0$, which would imply that some $2s$ columns of $A$ are linearly dependent. Unless $A$ has $2$s linearly dependent columns, there can only be one $s$-sparse solution.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

There are many areas in which the problem is to find the unique sparse solution to a linear system. One is in plant breeding blum2016foundations. Assume we are given a number of apple trees and the strength of some desirable feature of each tree. If we wish to determine which genes are responsible for the feature, we may formulate a system of linear equations ${Ax} = b$ in which each row of the matrix $A$ corresponds to a tree and each column corresponds to a position on the genome. The vector $b$ corresponds to the strength of the desired feature in each tree. The solution $x$ tells us the positions on the genome corresponding to the genes that account for the feature.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

The problem of finding a sparse solution can be stated as the optimization problem

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

where ${\| x\|}_{0}$ is the number of non-zero coordinates of $x$. This is an NP-hard problem, but it may sometimes be replaced by the convex problem

<!-- chunk {"id": "body-0041", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

What are the sufficient conditions for

<!-- chunk {"id": "body-0042", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

A matrix $A$ is said to satisfy the $s$-restricted isometry property if for any $s$-sparse $x$ there exists $\delta_{s}$ such that

<!-- chunk {"id": "body-0043", "role": "body", "section": "Problems with Hidden Convexity or Analytic Solutions", "weight": 1.0} -->

The following theorems give sufficient conditions for the equivalence mentioned above to hold blum2016foundations; candes2005decoding.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

In this section, we would like to give examples of non-convex optimization problems for which there are methods with proven convergence results. We start with the Phase retrieval problem. The phase retrieval problem has been a topic of study from at least the early 1980s. It is the recovery of a function given the magnitude of its Fourier transform. This problem could be found in various engineering and scientific applications such as optical imaging, electron microscopy, and crystallography, etc. shechtman2015phase. We recover a $d$-dimensional signal vector $x^{\ast} \in {\mathbb{C}}^{d}$ from its phaseless measurements

<!-- chunk {"id": "body-0045", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

with $a_{k}$ denoting the measurement vectors. As a result, the phase-retrieval problem can be formulated as the following least squares problem or empirical risk minimization

<!-- chunk {"id": "body-0046", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

This problem is well-motivated by practical concerns, but unfortunately, this is a non-convex problem, and it is not clear how to find a global minimum even if one exists. In recent literature, there are various approaches to handle this problem wu2020hadamard; tan2019online; chen2019gradient, also, algorithms with the provable convergence results were presented in the following papers candes2015phase; yang2019misspecified.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

In the context of non-convex optimization problems with proven convergence result, one cannot but mention Low-Rank Matrix Completion. There are related problems: matrix completion and matrix sensing bhojanapalli2016dropping, which are present in big data problems with incompleteness and other machine learning problems. We would like to draw attention to the exact low-rank matrix completion. Given a matrix $Y \in {\mathbb{R}}^{n \times n}$, partially observed, over a set of indices $\Omega \subseteq {\{ 1,\ldots,n\}}^{2}$. Consider the problem of finding the lowest-rank matrix matching $X$ on the observed set

<!-- chunk {"id": "body-0048", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

This is a non-convex problem having a natural convex relaxation

<!-- chunk {"id": "body-0049", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

In the paper jain2013low the first results of global optimality of alternating minimization were obtained for matrix completion and the related problem of matrix sensing. Proofs of (nearly) linear convergence of gradient descent for Phase retrieval, Matrix completion, Blind deconvolution can be found in the article ma2018implicit. Under some assumptions, it can be shown that the solution to the convex problem is exactly equal to the solution to the non-convex problem, with high probability over the sampling model candes2010power; candes2009exact. So, this problem can also be attributed to statistical problems with hidden convexity. Moreover, we we emphasise another relevant problem called Low-Rank Matrix Recovery. This problem is also known to be non-convex but under some assumptions has no spurious local minima (see zhang2021sharp; zhang2021general and references therein).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

Deep Learning. In the era of AI, training of the deep neural networks Goodfellow-et-al-2016 is one of the most popular optimization problems with enormous amount of applications, e.g., kniaz2021adversarial; rezanov2021deep; khritankov2021hidden; kuderov2021planning; surazhevsky2021noise-assisted; ilyuhin2020recognition; demin2021necessary; gorodetskiy2020delta; skrynnik2021forgetful; paparoditis2020wire. The simplest example of such problem sun2019optimization is training fully connected neural network for supervised learning problem

<!-- chunk {"id": "body-0051", "role": "body", "section": "Problems with Convergence Results", "weight": 1.0} -->

In general, training neural networks is NP-complete problem blum1989training. Deep neural networks have bad local minima both for non-smooth activation functions swirszcz2016local; safran2018spurious and smooth ones liang2018understanding; yun2018small as well as flat saddles vidal2017mathematics. Nevertheless, there exist positive results about training neural networks. First of all, under different assumptions it was shown that all local minima are global for 1-layer neural networks soltanolkotabi2018theoretical; haeffele2017global; feizi2017porcupine. Next, one can show that GD/SGD converge under some assumptions to global minimum for linear networks arora2018convergence; ji2019gradient; shin2019effects and sufficiently wide over-parameterized networks allen2019convergence. The detailed summary of recent advances in optimization for deep learning can be found in sun2019optimization.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Geometry of non-convex optimization problems", "weight": 1.0} -->

In one of the latest survey zhang2020symmetry, the authors to distinguish a class of tractable non-convex problems, which have certain properties of symmetry. They highlight non-convex optimization problems with rotational symmetry and discrete symmetry. Problems with rotational symmetry include the previously described phase retrieval and related problems in low-rank matrix factorization and recovery. It turns out that the blind deconvolution and tensor decomposition problems have discrete symmetry.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Deterministic First-Order Methods", "weight": 1.0} -->

In this section we focus on the following optimization problem

<!-- chunk {"id": "body-0054", "role": "body", "section": "Deterministic First-Order Methods", "weight": 1.0} -->

where $Q$ is a simple, closed, convex, set, and $f$ is continuously differentiable function. The simplest method for this kind of problems is projected gradient descent, which can be motivated by a simple continuous-time dynamics. For simplicity we start with the unconstrained case with $Q = {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

In the case $Q = {\mathbb{R}}^{n}$, the trajectory of the continuous-time gradient method is the solution to the differential equation $\overset{˙}{x} = {- {{\nabla f}\left( {x{(t)}} \right)}}$. It is easy to see that ${W(x)} = {f\left( {x{(t)}} \right)}$ is a Lyapunov function for this dynamical system. Indeed,

<!-- chunk {"id": "body-0056", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

This implies the convergence of the continuous-time gradient descent method to a stationary point.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

The classic gradient descent method is then the Euler discretization of the above dynamics and has the form polyak1987introduction

<!-- chunk {"id": "body-0058", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

where $h_{k} \geq 0$ is the stepsize of the method. One of the main assumptions in this setting is that the function $f$ is $L$-smooth, or, which is the same, its gradient is Lipschitz-continuous, i.e., for some starting point $x^{0}$,

<!-- chunk {"id": "body-0059", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

This proves that the complexity of finding an approximate stationary point, i.e. a point $\hat{x}$ such that ${\|{{\nabla f}{(\hat{x})}}\|}_{2} \leqslant \varepsilon$ is $O\left( \frac{L\left( {{f\left( x_{0} \right)} - f_{\ast}} \right)}{\varepsilon^{2}} \right)$. This iteration complexity of finding an $\varepsilon$-stationary point $N \sim \varepsilon^{- 2}$ is unimprovable in terms of its dependence on $\varepsilon$ and $L$ for an arbitrary first-order method applied to minimization of an $L$-smooth objective.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

On the one hand this bound is much better than the exponential in the dimension bound for finding the global minimum, which was derived in Subsection 2.2. On the other hand we can guarantee only an approximate stationary point, which could be a saddle-point or even a maximum. This can be illustrated by the example of minimization of the following objective nesterov2018lectures

<!-- chunk {"id": "body-0061", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

If we set $x^{0} = ^{T}$, then $x^{k}$ converges to $^{T}$ as $k\rightarrow\infty$, which is a saddle-point. The good news here is that gradient descent can be perturbed by adding some noise in the iterates in such a way that it converged to a local minimum for almost all initial points and escapes saddle-points jin2017how.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

It is important to note that, under additional smoothness assumptions that higher-order derivatives of the objective are Lipschitz continuous, i.e.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Unconstrained Minimization", "weight": 1.0} -->

carmon2019lowerI; carmon2019lowerII obtain several lower complexity bounds for finding an approximate stationary point. If this inequality holds for $p \in {\{ 1,2\}}$, the lower bound becomes $\varepsilon^{- \frac{12}{7}}$, and the additional assumption that the same holds for $p = 3$ gives the lower bound to $\varepsilon^{- \frac{8}{5}}$. Surprisingly, Lipschitz continuity of derivatives of order 4 and higher gives the same lower complexity bound.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Incorporating Simple Constraints", "weight": 1.0} -->

It is possible to generalize gradient method for the setting of composite optimization with simple convex constraints, i.e. for the problem

<!-- chunk {"id": "body-0065", "role": "body", "section": "Incorporating Simple Constraints", "weight": 1.0} -->

where $Q$ is a closed convex set, $\psi{(x)}$ is a simple convex function, e.g. ${\| x\|}_{1}$, and $f$ is $L$-smooth function. The standard approach for such problems uses prox-function $d{(x)}$ which is continuously differentiable and strongly convex on $Q$, i.e. ${{d{(y)}} - {d{(x)}} - {\langle{{\nabla d}{(x)}},{y - x}\rangle}} \geq {\frac{1}{2}{\|{y - x}\|}^{2}}$ for any ${x,y} \in Q$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Incorporating Simple Constraints", "weight": 1.0} -->

We define also the corresponding Bregman divergence ${V{\lbrack z\rbrack}{(x)}} = {{d{(x)}} - {d{(z)}} - {\langle{d^{\prime}{(z)}},{x - z}\rangle}}$, ${x,z} \in Q$. Then the step of the gradient method from a point $x$ with stepsize $h$ is generalized nesterov2018lectures; ghadimi2016mini-batch to

<!-- chunk {"id": "body-0067", "role": "body", "section": "Incorporating Simple Constraints", "weight": 1.0} -->

if $h = {1/L}$. Here $F_{\ast}$ is a lower bound for $F{(x)}$. In the described above simple situation this bound coincides with the bound. The authors of dang2015stochastic prove that if ${\|{g_{Q}{(x)}}\|} \leqslant \varepsilon$, then $x^{+}$ is an approximately stationary point of the problem. More precisely, there exist $p \in {\partial{\psi{(x^{+})}}}$ such that

<!-- chunk {"id": "body-0068", "role": "body", "section": "Incorporating Simple Constraints", "weight": 1.0} -->

where $\mathcal{N}_{Q}{(x^{+})}$ is the normal cone of $Q$ at the point $x^{+}$, ${B{(r)}} = {\{{v \in {\mathbb{R}}^{n}}:{{\| v\|}_{\ast} \leqslant r}\}}$ -- ball in the dual space defined by the conjugate norm, and it is assumed that $d$ is $L{(d)}$-smooth. Note that there is no contradiction with the exponential lower bound given in the end of Subsection 2.2 since non-necessarily the obtained point $x^{+}$ has small norm of the gradient.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Incorporating Simple Constraints", "weight": 1.0} -->

This approach was further generalized in bogolubsky2016learning; dvurechensky2017gradient; gasnikov2018power for the case of optimization with inexact oracle for the function $f$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

The considered above dynamical system $\overset{˙}{x} = {- {{\nabla f}\left( {x{(t)}} \right)}}$ does not have any mechanical intuition behind it. In polyak1964some the author proposed to consider the following dynamics

<!-- chunk {"id": "body-0071", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

One of the ways to discretize it gives the so called heavy-ball method

<!-- chunk {"id": "body-0072", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

where $h > 0$ is the stepsize and $\beta > 0$ is the momentum parameter. Due to the momentum term $\beta\left( {x^{k} - x^{k - 1}} \right)$ the method avoids zigzagging for ill-conditioned problems, which leads to significant efficiency in practice, especially in training neural networks. Despite practical efficiency, the theoretical guarantee for this method is no better than for the gradient method. In particular, griewank1981generalized considers the dynamical system

<!-- chunk {"id": "body-0073", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

where ${\mu(t)} \sim \left( {{f\left( {x(t)} \right)} - c} \right)$, $c$ is an upper bound on the global minimum of $f{(x)}$, and ${p(t)} = {F\left( {{\nabla f}\left( {x(t)} \right)} \right)}$. With a special choice of $F( \cdot )$, they show that $x(t)$ converges to a local minimizer $x^{loc}$ such that ${f\left( x^{loc} \right)} \leqslant c$ as $t\rightarrow{+ \infty}$. In diakonikolas2019generalized it is shown that for a discretization of a further generalization of the heavy-ball method one may guarantee

<!-- chunk {"id": "body-0074", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

which coincides with the bound for the gradient method.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

A different type of momentum was proposed in nesterov1983method for convex optimization, which led to the Nesterov's accelerated gradient method

<!-- chunk {"id": "body-0076", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

The difference with the heavy-ball method is that the gradient is calculated in the extrapolated point. This idea has been very fruitful and allowed to obtain many accelerated algorithms for convex optimization. A variant of this method with a special choice of the stepsize $h$ and momentum term $\beta_{k}$ was shown in ghadimi2016accelerated to have the same convergence rate as the gradient method. This was further extended in ghadimi2019generalized for the case of objective with Hölder-continuous gradients to obtain a bound $\frac{L_{\nu}^{\frac{1}{\nu}}{({{F{(x^{0})}} - F_{\ast}})}}{\varepsilon^{\frac{1 + {3\nu}}{2\nu}}}$ to find $\left\| {g_{Q}{(x^{k})}} \right\| \leqslant \varepsilon$ in the general setting of composite optimization problem with simple constraints.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

Importantly, this method is universal and uniform, which means that it has best possible convergence rates for convex and non-convex problems without knowing whether the problem is convex or not and without knowing its smoothness parameters such as Hölder exponent and Hölder constant.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

It is possible to combine this idea with the idea of line-search, i.e. minimization in the direction of the step. The papers guminov2019accelerated; nesterov2020primal-dual propose a modification of the accelerated gradient method which is listed as Algorithm 1. Instead of explicitly defining the stepsize $h$ and the momentum term $\beta$, this method uses full one-dimensional relaxation and local information. This makes this method parameter-free and uniform for convex and non-convex smooth optimization by providing optimal complexity bound for the convex and non-convex case. At the same time, inexact line-search is possible and its sufficient accuracy for achieving the desired accuracy is estimated. This method shares some similarities with nonlinear conjugate gradient methods which were analyzed in nemirovski1982orth.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

Algorithm 1 Accelerated Gradient Method with Small-Dimensional Relaxation (AGMsDR)

<!-- chunk {"id": "body-0080", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

The above idea was further extended in guminov2021combination where an accelerated alternating minimization method was proposed and analyzed for convex and non-convex problems. The main assumption is that the set of coordinates is divided into $\overline{n}$ disjoint subsets (blocks) $I_{p}$, $p \in {\{ 1,\ldots,\overline{n}\}}$ and minimization in each block when the other variables are freezed can be made explicitly. The resulting accelerated alternating minimization algorithm is listed as Algorithm 2. This method is also parameter-free and uniform for convex and non-convex smooth optimization with optimal complexity bound for the convex and non-convex case.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

Algorithm 2 Accelerated Alternating Minimization (AAM)

<!-- chunk {"id": "body-0082", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

The sequence $y^{k}$ of this algorithm satisfies

<!-- chunk {"id": "body-0083", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

i.e. there is an additional multiplier $M$ -- number of blocks.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

where $x^{\ast}$ is the closest to $x^{0}$ global minimizer.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Incorporating Momentum for Acceleration", "weight": 1.0} -->

By exploiting the idea of Nesterov's acceleration and combining it with the notion of negative curvature, the authors of carmon2017convex manage to accelerate first-order methods for non-convex optimization under additional assumptions that second and third derivatives are Lipschitz continuous. More precisely, if $L$-smooth function has also Lipschitz continuous Hessian, they obtain complexity $O\left( {\varepsilon^{- {7/4}}{\log{({1/\varepsilon})}}} \right)$ to find a point $\hat{x}$ such that ${\|{{\nabla f}{(\hat{x})}}\|}_{2} \leqslant \varepsilon$. Assuming additionally that the third derivative is Lipschitz, this bound is improved to $O\left( {\varepsilon^{- {5/3}}{\log{({1/\varepsilon})}}} \right)$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Stochastic First-Order Methods", "weight": 1.0} -->

where function $f$ is a general non-convex $L$-smooth function with the uniform lower bound $f_{\ast}$, i.e., it is differentiable and

<!-- chunk {"id": "body-0087", "role": "body", "section": "Stochastic First-Order Methods", "weight": 1.0} -->

We are interested in two particular cases: expectation minimization

<!-- chunk {"id": "body-0088", "role": "body", "section": "Stochastic First-Order Methods", "weight": 1.0} -->

Such problems usually arise in applications of (deep) machine learning Goodfellow-et-al-2016; sun2019optimization and mathematical statistics spokoiny2012parametric, and typically they are solved via stochastic first-order methods.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Stochastic First-Order Methods", "weight": 1.0} -->

In general, the best one can expect to achieve is an approximate stationary point vavasis1993black; arjevani2019lower. To be specific, for this class of problems stochastic first-order methods in the worst case can only find such point $\hat{x}$ that

<!-- chunk {"id": "body-0090", "role": "body", "section": "Stochastic First-Order Methods", "weight": 1.0} -->

Below we summarize recent results about finding $\varepsilon$-stationary point using stochastic first-order methods. We start with presenting the general and unified approach to analyze optimal deterministic and stochastic first-order methods for objectives of types and in the general settings. After that, we consider $3$ big classes of stochastic first-order methods with convergence guarantees: SGD and its variants, variance reduced methods, and adaptive stochastic methods.

<!-- chunk {"id": "body-0091", "role": "body", "section": "General View on Optimal Deterministic and Stochastic First-Order Methods for Non-Convex Optimization", "weight": 1.0} -->

Assume that at each point $x$, we have access to the estimator $g{(x)}$ of the gradient ${\nabla f}{(x)}$. For now, it is not important to specify what properties $g{(x)}$ satisfies. In these settings one can use Algorithm 3 in order to find $\varepsilon$-stationary point.

<!-- chunk {"id": "body-0092", "role": "body", "section": "General View on Optimal Deterministic and Stochastic First-Order Methods for Non-Convex Optimization", "weight": 1.0} -->

0: learning rates {hk}k ≥ 0 satisfying $h_{k} \leq \frac{1}{2L}$, starting point x0 ∈ ℝn, stopping criterion C
Algorithm 3 General scheme of the optimal first-order method for non-convex optimization

<!-- chunk {"id": "body-0093", "role": "body", "section": "General View on Optimal Deterministic and Stochastic First-Order Methods for Non-Convex Optimization", "weight": 1.0} -->

Below we derive preliminary inequalities playing the central role in the analysis of optimal (stochastic) first-order algorithms. From $L$-smoothness of $f$ we have

<!-- chunk {"id": "body-0094", "role": "body", "section": "General View on Optimal Deterministic and Stochastic First-Order Methods for Non-Convex Optimization", "weight": 1.0} -->

Now it is crucial to specify what we need to assume about $g{(x)}$. We emphasize that all $3$ cases considered below are based on the tight bounds for ${\|{{{\nabla f}{(x^{k})}} - g^{k}}\|}_{2}^{2}$ or its expectation.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Deterministic Case", "weight": 1.0} -->

In this case we assume that for all $x \in {\mathbb{R}}^{n}$ we have an access to such $g{(x)}$ that

<!-- chunk {"id": "body-0096", "role": "body", "section": "Deterministic Case", "weight": 1.0} -->

Next, we derive an upper bound for such $N$ that Algorithm 3 stops after $N$ iterations. Assume that, after $N$ iterations the method has not stopped. Then for all $k = {0,1,\ldots,T}$ we have

<!-- chunk {"id": "body-0097", "role": "body", "section": "Deterministic Case", "weight": 1.0} -->

Therefore, the methods stops after

<!-- chunk {"id": "body-0098", "role": "body", "section": "Deterministic Case", "weight": 1.0} -->

iterations. This bound is optimal up to constant factors carmon2019lowerI.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Stochastic Case: Uniformly Bounded Variance", "weight": 1.0} -->

In this case, we assume that for all $x \in {\mathbb{R}}^{n}$ we have

<!-- chunk {"id": "body-0100", "role": "body", "section": "Stochastic Case: Uniformly Bounded Variance", "weight": 1.0} -->

For example, this situation appears when

<!-- chunk {"id": "body-0101", "role": "body", "section": "Stochastic Case: Uniformly Bounded Variance", "weight": 1.0} -->

where $\xi$ is a random variable with distribution $\mathcal{D}$ and $g{(x)}$ is formed as

<!-- chunk {"id": "body-0102", "role": "body", "section": "Stochastic Case: Uniformly Bounded Variance", "weight": 1.0} -->

Then, taking conditional expectation ${\mathbb{E}}\left\lbrack \cdot \mid x^{k} \right\rbrack$ from the both sides of we derive

<!-- chunk {"id": "body-0103", "role": "body", "section": "Stochastic Case: Uniformly Bounded Variance", "weight": 1.0} -->

Finally, we choose the output of the method ${\hat{x}}^{N}$ uniformly at random from $x^{0},x^{1},\ldots,x^{N - 1}$ which implies

<!-- chunk {"id": "body-0104", "role": "body", "section": "Stochastic Case: Uniformly Bounded Variance", "weight": 1.0} -->

This bound is optimal up to constant factors for the case when the variance is uniformly upper bounded arjevani2019lower.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

In this case we assume that the objective function has a finite sum structure with $L$-smooth summands. In fact, this smoothness constant $L$ can be significantly larger than the smoothness constant of $f$. It is essential for providing a fair comparison of different complexity results. It is possible to improve the dependence on $L$ in the final complexity bounds li2020page using average smoothness assumption, but for simplicity we consider the case when all summands are $L$-smooth. Moreover, we assume that there exists constant $\sigma^{2}$ (possibly infinite) such that for $\xi$ taken uniformly at random from $\{ 1,\ldots,m\}$ and for all $x \in {\mathbb{R}}^{n}$

<!-- chunk {"id": "body-0106", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

Here, at iteration $k$ random index $\xi_{k}$ is sampled uniformly at random from $\{ 1,\ldots,m\}$ if $k$ is not divisible by $q$ and random indices $\xi_{k,1},\ldots,\xi_{k,r}$ are i.i.d. samples from uniform distribution on $\{ 1,\ldots,m\}$ if $q = r$ and $r$ divides $k$. As the result, we obtain the variant of SPIDER fang2018spider. We notice that for $k = {{aq} + p}$, $p \in {\{ 0,1,\ldots,{q - 1}\}}$ iteration $k$ requires $2$ calculations of ${\nabla f_{\xi}}{(x)}$ when $p \neq 0$ and $q$ calculations of ${\nabla f_{\xi}}{(x)}$ when $p = 0$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

This implies that $q$ iterations of the method requires only $3q$ calculations of ${\nabla f_{\xi}}{(x)}$, so, if $k \geq q$, then the number of stochastic first-order oracle coincides with the number of iterations up to a constant factor $3$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

Below we present a simplified approach to analyze SPIDER. As before, our goal is to show that ${\mathbb{E}}\left\lbrack {\|{g^{k} - {{\nabla f}{(x^{k})}}}\|}_{2}^{2} \right\rbrack$ can be upper-bounded by either something small or something that can be controlled by other terms. First of all, if $k = {aq}$, then

<!-- chunk {"id": "body-0109", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

Next, using the choice of the stepsize $h = {1/\left( {10L\sqrt{q}} \right)}$ we obtain

<!-- chunk {"id": "body-0110", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

Finally, we put all the inequalities together.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

We notice that this inequality holds for all integers $a \geq 0$ and $p \in {\{ 0,\ldots,{q - 1}\}}$. Summing up these inequalities for $p = {0,\ldots,P}$ and taking $a = A$ where $N = {{Aq} + P}$, $P \in {\{ 0,\ldots,{q - 1}\}}$ we get

<!-- chunk {"id": "body-0112", "role": "body", "section": "Stochastic Case: Finite Sum Minimization", "weight": 1.0} -->

calculations of ${\nabla f_{\xi}}{(x)}$ which is optimal up to constant factors fang2018spider.

<!-- chunk {"id": "body-0113", "role": "body", "section": "SGD and Its Variants", "weight": 1.0} -->

As it was shown in the previous section, SGD

<!-- chunk {"id": "body-0114", "role": "body", "section": "SGD and Its Variants", "weight": 1.0} -->

in the settings of Section 4.1 requires $O\left( \frac{L{(f{(x^{0})} - f_{\ast}}}{\epsilon^{2}} \right)$ iterations with batch size $r = {\Theta\left( {\max\left\{ 1,\frac{\sigma^{2}}{\epsilon^{2}} \right\}} \right)}$ to find an $\epsilon$-stationary point in expectation. The total number of stochastic first-order oracle calls equals

<!-- chunk {"id": "body-0115", "role": "body", "section": "SGD and Its Variants", "weight": 1.0} -->

We emphasize that we use large batch size for the sake of simplicity and unification of the results in 3 different cases. In fact, it is possible to obtain the bound using smaller stepsizes and constant batch sizes of the order $O{}$ ghadimi2013stochastic.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Assumptions on the Stochastic Gradient", "weight": 1.0} -->

In addition to assumption, which is quite restrictive, there exist several other assumptions on the stochastic gradient studied in the literature. Recently in khaled2020better it was proposed a simple and unified way to cover the most popular ones.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

The second moment of stochastic gradients satisfies

<!-- chunk {"id": "body-0118", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

This assumption generalizes the notion of expected smoothness introduced and adjusted for convex problems in gower2019sgd. Moreover, the following assumptions are stronger than Assumption 4.1 ‣ Assumptions on the Stochastic Gradient ‣ 4.2 SGD and Its Variants ‣ 4 Stochastic First-Order Methods ‣ Recent Theoretical Advances in Non-Convex Optimization") or can be seen as special cases of Assumption 4.1 ‣ Assumptions on the Stochastic Gradient ‣ 4.2 SGD and Its Variants ‣ 4 Stochastic First-Order Methods ‣ Recent Theoretical Advances in Non-Convex Optimization") (see more details and formal proofs in khaled2020better ).

<!-- chunk {"id": "body-0119", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Uniformly upper-bounded variance (UV) assumption. Indeed, if $A = 0$, $B = 1$ and $C = \sigma^{2}$, then using variance decomposition inequality (32 ‣ Assumptions on the Stochastic Gradient ‣ 4.2

<!-- chunk {"id": "body-0120", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Expected strong growth condition (E-SG). When $A = C = 0$ and $B = \alpha \geq 1$ inequality (32 ‣ Assumptions on the Stochastic Gradient ‣ 4.2

<!-- chunk {"id": "body-0121", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Maximal strong growth condition (M-SG) tseng1998incremental; schmidt2013fast states that there exists such $\alpha > 0$ that

<!-- chunk {"id": "body-0122", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

This condition implies E-SG while known convergence results in expectation under M-SG assumption have no advantage in comparison with their counterparts under E-SG.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Relaxed growth condition (RG) bottou2018optimization can be seen as another special case of Assumption 4.1 ‣ Assumptions on the Stochastic Gradient ‣ 4.2

<!-- chunk {"id": "body-0124", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

However, there exist simple problems of type + that fit the settings we are interested in but do not satisfy (see Proposition 1 from khaled2020better ).

<!-- chunk {"id": "body-0125", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Gradient confusion condition (GC) sankararaman2019impact was developed for the finite-sum case. In particular, it states that there exists such $\eta > 0$ that for all ${{i,j} = 1},{\ldots,m}$ and for all $x \in {\mathbb{R}}^{n}$

<!-- chunk {"id": "body-0126", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

One can show (see Theorem 1, khaled2020better ) that inequality implies with $\alpha = m$ and $\beta = {\eta{({m - 1})}}$, and, as a consequence, it is a special case of Assumption 4.1 ‣ Assumptions on the Stochastic Gradient ‣ 4.2 SGD and Its Variants ‣ 4 Stochastic First-Order Methods ‣ Recent Theoretical Advances in Non-Convex Optimization") with $A = 0$, $B = m$, and $C = {\eta{({m - 1})}}$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Sure-smoothness condition (SS) lei2019stochastic is defined for the case when the objective is represented as an expectation and ${g{(x)}} = {{\nabla f}{(x,\xi)}}$ where $\xi$ is sampled independently at each iteration of SGD. That is, sure-smoothness condition means that^44^4In the original paper lei2019stochastic, authors considered more general situation when stochastic realizations $f{(x,\xi)}$ have Hölder-continuous gradients. for all ${x,y} \in {\mathbb{R}}^{n}$

<!-- chunk {"id": "body-0128", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Applying classical corollaries of $L$-smoothness one can derive inequality (32 ‣ Assumptions on the Stochastic Gradient ‣ 4.2 SGD and Its Variants ‣ 4 Stochastic First-Order Methods ‣ Recent Theoretical Advances in Non-Convex Optimization")) with $A = {2L}$, $B = 0$, and $C = {2Lf_{\ast}}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Next, Assumption 4.1 ‣ Assumptions on the Stochastic Gradient ‣ 4.2 SGD and Its Variants ‣ 4 Stochastic First-Order Methods ‣ Recent Theoretical Advances in Non-Convex Optimization") covers arbitrary sampling setup and distributed setup with quantization^55^5This technique is applied in distributed optimization to reduce the overall communication cost (e.g., see alistarh2017qsgd; beznosikov2020biased; pmlr-v139-gorbunov21a ). However, methods for distributed optimization are out of scope of our survey.. For simplicity, we mention only sampling with replacement as a special case of arbitrary sampling (see more examples in khaled2020better ). In particular, consider the finite-sum optimization problem + and assume that $f_{i}$ is $L_{i}$-smooth and bounded from below by $f_{i, \ast}$ for all $i = {1,\ldots,m}$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

Finally, under Assumption 4.1 ‣ Assumptions on the Stochastic Gradient ‣ 4.2 SGD and Its Variants ‣ 4 Stochastic First-Order Methods ‣ Recent Theoretical Advances in Non-Convex Optimization") Khaled and Richtárik khaled2020better derived the following complexity bound: if $h = {\min\left\{ \frac{1}{\sqrt{LAN}},\frac{1}{LB},\frac{\varepsilon}{2LC} \right\}}$, then inequality

<!-- chunk {"id": "body-0131", "role": "body", "section": "Assumption 4.1 (Expected Smoothness; Assumption 2 from khaled2020better )", "weight": 1.0} -->

iterations of SGD. It is worth to mention that this bound gives the sharpest rates for all known special cases. We summarize some of them in Table 1. We notice that is weaker than, but it is easy to obtain the same bound guaranteeing instead of based on the analysis given in khaled2020better.

<!-- chunk {"id": "body-0132", "role": "body", "section": "The Choice of the Stepsize", "weight": 1.0} -->

In practice, instead of using the constant stepsize for SGD it is popular to periodically decrease the stepsize by some factor bottou2010large; krizhevsky2009learning; he2016deep even for non-convex problems. For strongly convex problems such a choice is natural: it is well-known gorbunov2020unified that if the stepsize equals $h$ and strong convexity parameter equals $\mu$, then SGD converges with linear rate $\overset{\sim}{O}{({({h\mu})}^{- 1})}$ to the neighborhood of the solution with size proportional to $h$. Surprisingly, SGD enjoys similar behaviour even for non-convex problems which was recently shown in shi2020learning.

<!-- chunk {"id": "body-0133", "role": "body", "section": "The Choice of the Stepsize", "weight": 1.0} -->

In the neural networks training, "warmup" goyal2017accurate; gotmare2018closer and cyclical stepsize smith2017cyclical; loshchilov2016sgdr schedules are also very popular and useful. The first one refers to the strategy when, during several epochs of training, tiny stepsizes are used, and then they are increased. This technique was successfully applied for several deep learning problems like ResNet he2016deep, large-batch training of Imagenet goyal2017accurate and natural language problems vaswani2017attention; devlin2018bert.

<!-- chunk {"id": "body-0134", "role": "body", "section": "The Choice of the Stepsize", "weight": 1.0} -->

Cyclical stepsize schedule means that the stepsize is changing between some lower and upper bounds. There are different modification of this technique including gradual decrease and increase during one epoch smith2017cyclical and gradual decrease of the stepsize followed by the sudden increase loshchilov2016sgdr. However, the theoretical understanding of the success of "warmup" and cyclical schedules is very limited.

<!-- chunk {"id": "body-0135", "role": "body", "section": "The Choice of the Stepsize", "weight": 1.0} -->

We also discuss different stepsize policies including adaptive ones (Section 4.4), Armijo line-search under expected strong growth assumption and stochastic Polyak stepsizes under relaxed growth assumption (Section 4.2) in the following subsections.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Over-Parameterized Models", "weight": 1.0} -->

In Section 2.3, we mentioned that over-parameterization livni2014computational; neyshabur2017exploring; zhang2016understanding; nguyen2018loss; li2018over; allen2019convergence; allen2019on, meaning that the last layer has more neurons than the number of samples in the training set, is a good property for neural networks from the optimization and generalization ma2018power; allen2019learning; allen2019can point perspectives, but not a panacea: over-parameterized neural networks have no spurious valleys, but still can have bad local minima ding2019spurious.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Over-Parameterized Models", "weight": 1.0} -->

In the papers, focusing mostly on the optimization aspects of over-parameterized models, it was shown that SGD converges with the same (up to the difference in the smoothness constants) rate as GD in terms of the iteration complexity in convex and strongly convex cases vaswani2018fast; vaswani2019painless; loizou2020stochastic under interpolation condition: for the finite-sum optimization problem + there exists such point $x^{\ast} \in {\mathbb{R}}^{n}$ that

<!-- chunk {"id": "body-0138", "role": "body", "section": "Over-Parameterized Models", "weight": 1.0} -->

Furthermore, in this setting SGD converges with Armijo line-search vaswani2019painless, with stochastic Polyak stepsizes loizou2020stochastic, and, if additionally expected strong growth condition holds, SGD can be accelerated vaswani2018fast and the accelerated version converges as good as Nesterov's method nesterov1983method in terms of iteration complexity up to expected strong growth multiplicative factor $\alpha$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Over-Parameterized Models", "weight": 1.0} -->

In the general non-convex case, the following results exist.\
Constant stepsizes. In vaswani2018fast, it was shown that SGD with constant stepsize $h = {1/{\alphaL}}$ finds $\varepsilon$-stationary point under expected strong growth condition with the rate $O\left( {{\alphaL\left( {{f\left( x^{0} \right)} - f_{\ast}} \right)}/\varepsilon^{2}} \right)$ matching the iteration complexity of GD up to the factor $\alpha$.\
Armijo line-search. The idea that under interpolation condition/expected strong growth condition SGD and GD have similar properties was then strengthen in vaswani2019painless, where authors showed that SGD with Armijo line-search converges in these settings. In particular, the authors of vaswani2019painless considered such stepsizes $h_{k}$ that

<!-- chunk {"id": "body-0140", "role": "body", "section": "Over-Parameterized Models", "weight": 1.0} -->

$L_{\max}$ is the maximal smoothness constant of summands $f_{i}$, and $f$ is the smoothness constant of $f$.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Over-Parameterized Models", "weight": 1.0} -->

Authors of vaswani2019painless also considered the version with samples used for backtracking independent from those used for determining the stochastic gradient, and the version with non-increasing stepsizes under additional assumption that the iterates lie in some ball with radius $D$. The rates are $O\left( {{{\max\left\{ L_{\max},{\alphaL} \right\}}\left( {{f\left( x^{0} \right)} - f_{\ast}} \right)}/\varepsilon^{2}} \right)$ and $O\left( {{{\max\left\{ L_{\max},{\alphaL} \right\}}LD^{2}}/\varepsilon^{2}} \right)$ respectively, and both complexity bounds hold with $c = {1/2}$ and $h_{\max} = {1/\left( {\alphaL} \right)}$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Over-Parameterized Models", "weight": 1.0} -->

Finally, in the numerical experiments from vaswani2019painless the authors observed that the method's performance is robust to the choic of $c$ and $h_{\max}$.\
Stochastic Polyak stepsizes.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Proximal Variants", "weight": 1.0} -->

In the previous subsections, all complexity results rely on the smoothness of the objective function. The natural question arises: is it possible to generalize these results to the non-smooth case? In the recent work kornowski2021oracle, the authors give a negative answer to this question for generally non-smooth non-convex functions, i.e., one cannot find efficiently via first-order methods near $\varepsilon$-stationary points.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Proximal Variants", "weight": 1.0} -->

where the function $f$ is $L$-smooth, but, possibly, non-convex, while $R{(x)}$, i.e., composite term/regularizer, is a proper closed convex function which can be non-smooth. Moreover, function $R{(x)}$ is often chosen in such a way that the proximal operator

<!-- chunk {"id": "body-0145", "role": "body", "section": "Proximal Variants", "weight": 1.0} -->

can be easily computed, and to make the solution of the problem satisfy certain properties, e.g., sparsity; see candes2008enhancing; combettes2011proximal; bach2012optimization for the detailed discussion and examples of regularizers.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Proximal Variants", "weight": 1.0} -->

Moreover, to measure the progress of the method the generalized projected stochastic gradient is used: ${\overset{\sim}{g}}^{k} = {\left( {x^{k} - x^{k + 1}} \right)/h_{k}}$. When the regularizer $R{(x)}$ is a constant ${\overset{\sim}{g}}^{k} = g^{k}$. For proximal stochastic methods we say that the iterate $x^{k}$ is $\varepsilon$-stationary point if

<!-- chunk {"id": "body-0147", "role": "body", "section": "Proximal Variants", "weight": 1.0} -->

In ghadimi2016mini-batch, it was shown that prox-SGD under uniformly upper-bounded variance assumption converges with the rate given. However, the analysis from ghadimi2016mini-batch works only in the large-batch setting, i.e., when batch sizes are of the order $O{(\varepsilon^{- 2})}$. For a long time, there was no analysis establishing the same bound without using $O{(\varepsilon^{- 2})}$ batches, and the problem was recently resolved in davis2019stochastic.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Momentum-SGD", "weight": 1.0} -->

As we already mentioned, SGD is optimal among stochastic first-order methods for finding $\varepsilon$-stationary points under uniformly bounded variance assumption arjevani2019lower. However, it does not imply that there is no sense in using different methods for such problems. In practice, different additional tricks are applied to improve the convergence of SGD, and, perhaps, the most popular one is momentum polyak1964some.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Momentum-SGD", "weight": 1.0} -->

Momentum-SGD/Heavy Ball SGD can be written in different forms. Usually it is written as

<!-- chunk {"id": "body-0150", "role": "body", "section": "Momentum-SGD", "weight": 1.0} -->

where parameter $\beta_{k} \in {\lbrack 0,1)}$ is called momentum parameter. In the convex and strongly convex cases this method has some advantages in comparison to SGD like better last-iterate convergence guarantees tao2018primal; taylor2019stochastic; sebbouh2020convergence, but does not have an accelerated rate kidambi2018insufficiency. In the non-convex case, Momentum-SGD has the same complexity guarantee as SGD under uniformly bounded variance assumption yan2018unified; defazio2020understanding. However, in practice, Momentum-SGD often works much better than SGD especially on computer vision problems sutskever2013importance, and also navigates ravines and escapes saddle points better than SGD.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Momentum-SGD", "weight": 1.0} -->

Among other works on Momentum-SGD we emphasize the recent paper defazio2020understanding establishing the tight convergence rates for Momentum-SGD in Stochastic Primal Averaging tao2018primal form via Lyapunov functions analysis. In particular, defazio2020understanding justifies (theoretically and/or empirically) the following important insights about the behavior of Momentum-SGD: (i) Momentum-SGD is provably better than SGD during the early stage of the convergence, (ii) it is better to gradually reduce momentum parameter $\beta_{k}$ rather than the stepsize $h_{k}$, and (iii) gradual changes of the parameters of Momentum-SGD are preferable than sudden changes.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Random Reshuffling", "weight": 1.0} -->

Before this subsection, we always assumed that stochastic gradients are sampled independently from previous iterations. However, in the context of finite sum optimization +, the different sampling strategy called Random Reshuffling (or SGD with Without Replacement sampling) is often used: at each epoch (pass through the dataset) random permutation $\{ i_{1},i_{2},\ldots,i_{m}\}$ of the set $\{ 1,2,\ldots,m\}$ is generated defining the order of gradients computations (see Algorithm 4). This strategy implies that stochastic gradient in RR is biased.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Random Reshuffling", "weight": 1.0} -->

0: learning rates {hs, k}s, k ≥ 0, starting point x0 ∈ ℝn, batch size r ≥ 1, number of epochs S
Generate random permutation {is, 1, …, is, m} of the set {1, …, m}
Compute $g_{s}^{k} = {\frac{1}{r_{s}^{k}}{\sum\limits_{j = 1}^{r_{s}^{k}}{{\nabla f_{i_{s,{{kr} + j}}}}{(x_{s}^{k})}}}}$
xsk + 1 = xsk − hs, k gsk
Algorithm 4 Random Reshuffling (RR)

<!-- chunk {"id": "body-0154", "role": "body", "section": "Random Reshuffling", "weight": 1.0} -->

While the superiority of RR to SGD was empirically discovered a long time ago bottou2009curiously; bottou2012stochastic, the theoretical justification of this phenomenon was developed only recently haochen2018random; rajput2020closing; nguyen2020unified; mishchenko2020random. In particular, authors of nguyen2020unified proved that RR under uniformly bounded gradients assumption,

<!-- chunk {"id": "body-0155", "role": "body", "section": "Random Reshuffling", "weight": 1.0} -->

finds $\varepsilon$-stationary point with the rate $O\left( {L_{\max}m{({{f{(x^{0})}} - f_{\ast}})}\left( {\varepsilon^{- 2} + {G\varepsilon^{- 3}}} \right)} \right)$, where $L_{\max}$ is the maximal smoothness constant of summands $f_{1},\ldots,f_{m}$. Then, in mishchenko2020random this result was generalized and tightened: under the assumption

<!-- chunk {"id": "body-0156", "role": "body", "section": "Random Reshuffling", "weight": 1.0} -->

which is a special case of (32 ‣ Assumptions on the Stochastic Gradient ‣ 4.2

<!-- chunk {"id": "body-0157", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

In this section, we discuss variance reduction for non-convex optimization -- a special technique aimed at improving the convergence speed of SGD for finite-sum optimization problems +. The typical behaviour of SGD with constant stepsize $h$ and batch size $r < m$ is as following: during the first iterations the method converges rapidly to some neighbourhood of the solution or local minimum and then it starts to oscillate in this neighbourhood. Such oscillations of SGD are common even for strongly convex problems meaning that it is not a drawback of the problem. The size of the oscillation region is proportional to ${h\sigma^{2}}/r$ and this fact hints two simple and famous remedies: decreasing (gradually or suddenly) or small stepsizes and large enough batch sizes. However, the first option can make the convergence too slow and the second option dramatically increases the iteration cost.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

To remove these drawbacks one can apply variance-reduced methods like SAG schmidt2017minimizing, SAGA defazio2014SAGA, SVRG johnson2013accelerating, Finito defazio2014finito, MISO mairal2015incremental. In particular, all of the mentioned methods have $O\left( {\left( {m + {L/\mu}} \right){\ln\frac{1}{\varepsilon}}} \right)$ convergence rate in the $\mu$-strongly convex case. What is more, they use constant stepsize and at each iteration (besides each $m$-th iteration or besides the first one) they require one computation of the stochastic gradient with batch size $r = 1$ in the strongly convex case.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

Among variance-reduced methods SAGA and SVRG are the most popular ones (see Algorithm 5 and 6).

<!-- chunk {"id": "body-0160", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

0: learning rate h &gt; 0, epoch length T, starting point x0 ∈ ℝn, batch size r ≥ 1
Uniformly randomly pick set Ik from {1, …, m} (with replacement) such that |Ik| = r
$g^{k} = {{\frac{1}{r}{\sum\limits_{i \in I_{k}}\left( {{{\nabla f_{i}}{(x_{s}^{k})}} - {{\nabla f_{i}}{(\phi_{s})}}} \right)}} + {{\nabla f}{(\phi_{s})}}}$
Algorithm 6 SVRG johnson2013accelerating; reddi2016proximal

<!-- chunk {"id": "body-0161", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

In previous subsections, we already mentioned that to find $\varepsilon$-stationary GD and SGD require^66^6For simplicity we neglect all parameters except $m$ and $\varepsilon$, see the details in Table 2 $O\left( {m\varepsilon^{- 2}} \right)$ and $O{(\varepsilon^{- 4})}$ calculations of the gradients of the summands respectively. Despite the fact that SAGA and SVRG were initially analysed only in strongly convex cases, now their convergence in non-convex case is also well-known due to reddi2016proximal; reddi2016stochastic. Unfortunately, when $r = 1$ both SAGA and SVRG guarantee only $O{({m\varepsilon^{- 2}})}$ convergence rate as simple GD.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

However, if $r = m^{2/3}$, then SAGA and SVRG converges with the rate $O{({m^{2/3}\varepsilon^{- 2}})}$ which has $m^{1/3}$ times better dependence on $m$ than the complexity bound for GD.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

However, the lower bound is $\Omega\left( {\sqrt{m}\varepsilon^{- 2}} \right)$ fang2018spider; li2020page and there exist optimal algorithms. Essentially, these methods are variations of SARAH nguyen2017stochastic. However, in the original paper on SARAH for non-convex problems authors did not prove complexity bounds for the finite-sum optimization problems. After that, in fang2018spider authors proposed the first lower bounds in the small data regime $m = {O{({L^{2}{({{f{(x^{0})}} - f^{\ast}})}\varepsilon^{- 4}})}}$ together with the first optimal method called SPIDER. Despite the theoretical optimality of the method, it requires very small stepsize (proportional to $\varepsilon^{- 1}$) that leads to the poor behaviour in practice. Moreover, the original proof of the convergence rate for SPIDER is technically tough and, because of it, it is hard to generalize the method for the composite optimization problems.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

In recent works wang2018spiderboost; wang2019spiderboost, much simpler optimal method called SpiderBoost was proposed (see Algorithm 7). Moreover, this method works with big constant stepsizes (of order $L^{- 1}$), can be easily generalized for the composite optimization problems, and works well with heavy-ball momentum.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

0: learning rate h &gt; 0, epoch length T, starting point x0 ∈ ℝn, batch size r ≥ 1, number of iterations K
Uniformly randomly pick set Ik from {1, …, m} (with replacement) such that |Ik| = r
Compute $g^{k} = {{\frac{1}{r}{\sum\limits_{i \in I_{k}}\left( {{{\nabla f_{i}}{(x^{k})}} - {{\nabla f_{i}}{(x^{k - 1})}}} \right)}} + g^{k - 1}}$
Pick ξ uniformly at random from {0, …, K − 1}
Algorithm 7 SpiderBoost wang2018spiderboost; wang2019spiderboost

<!-- chunk {"id": "body-0166", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

Next, in li2020page, the same lower bound $\Omega\left( {\sqrt{m}\varepsilon^{- 2}} \right)$ was derived without any assumptions on $m$. Furthermore, authors of li2020page proposed a new optimal method called PAGE (see Algorithm 8) which is a variant of SPIDER with random length of the inner loop making the method easier to analyze.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

However, in deep neural networks training, variance-reduced methods work typically worse than SGD or SGD with momentum defazio2019ineffectiveness. This happens often due to the bad behaviour of variance-reduced methods with several widespread in deep learning tricks like batch normalization, data augmentation and dropout (see the details in defazio2019ineffectiveness ). Moreover, if the model is over-parameterized or, in particular, expected strong growth condition or its relaxed version with small noise level hold, SGD is as fast as GD in terms of iteration complexity, meaning that variance reduction is superfluous. That is, variance reduction trick is often not needed or gives worse rates than the rate of SGD for over-parameterized models from theoretical and practical perspectives. Nevertheless, when the problem is not over-parameterized, it makes sense to use variance-reduced methods.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

We summarize the discussed above complexity bounds in Table 2.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

We also want to mention some papers not presented in Table 2 but being highly relevant. In li2020unified, there was developed the generalization of the approach from khaled2020better providing a unified analysis of different variants of SGD, non-optimal variance-reduced methods like SAGA or L-SVRG hofmann2015variance; kovalev2020don, and some distributed methods with quantization alistarh2017qsgd including DIANA-type variance reduction mishchenko2019distributed; horvath2019stochastic for non-convex optimization. Next, for the online case + with smooth stochastic trajectories the optimal rate $O{(\varepsilon^{- 3})}$ was shown for STOchastic Recursive Momentum (STORM) method cutkosky2019momentum, which does not require periodical large-batch stochastic gradient computations and is more robust to the parameters selection, and for its proximal variant xu2020momentum. These results shade a light on the role of momentum in the stochastic first-order methods.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Variance-reduced Methods", "weight": 1.0} -->

Finally, it is optimal to generalize SPIDER and get similar rates for composition optimization problems zhang2020stochastic; chen2020momentum.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Convex and Weakly Convex Sums of Non-Convex Functions", "weight": 1.0} -->

There are also several results devoted to the case when the objective function $f$ from is (strongly) convex or almost convex, while the summands $f_{i}$ are smooth, but can be non-convex. In particular, zhou2019lower establishes the lower bounds for the cases when (i) $f$ is $\mu$-strongly convex with $\mu \geq 0$, (ii) $f$ is $\alpha$-weakly convex

<!-- chunk {"id": "body-0172", "role": "body", "section": "Convex and Weakly Convex Sums of Non-Convex Functions", "weight": 1.0} -->

and (iii) $f_{i}$ are $\alpha$-weakly convex. Due to the additional assumptions on the structure of non-convexity in the problem the proposed lower bounds are tighter in these situations than the lower bound from fang2018spider; li2020page. The lower bounds for the case (i) were further tightened in xie2019general. Moreover, there exist optimal and almost optimal methods for each case, see Table 3 for the details.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Convex and Weakly Convex Sums of Non-Convex Functions", "weight": 1.0} -->

f is cvx. and L-smooth, {fi} are average L-smooth
$m + {m^{3/4}\sqrt{\frac{LR_{0}^{2}}{\varepsilon}}}$, zhou2019lower
$m + {m^{3/4}\sqrt{\frac{LR_{0}^{2}}{\varepsilon}}}$, Dual-Free SDCA shalev2016sdca, KatyushaX allen2018katyusha

<!-- chunk {"id": "body-0174", "role": "body", "section": "Adaptive Methods", "weight": 1.0} -->

One of the most significant issues of the methods described above is that they require tuning of the stepsize and other parameters (e.g., batch size) when used in practice. It is often challenging and takes a lot of time, especially for training deep neural networks. That is why, in the recent few years, adaptive methods gained a lot of attention. Below we discuss the most popular ones -- AdaGrad and Adam -- as well as their variants. In fact, all of these methods depend on some parameters, but these algorithms are much more robust than other variants of SGD or variance-reduced methods. Therefore, they are often called adaptive. One can find PyTorch implementation of many popular adaptive first-order methods together with with visualization of their convergence on Rosenbrock and Rastrigin functions in pytorchOpt.

<!-- chunk {"id": "body-0175", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

AdaGrad. As we mentioned above, SGD requires the tuning of the stepsize.

<!-- chunk {"id": "body-0176", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

where the subscript $i$ denotes the $i$-th component of the vector, $G_{i}^{k} = {\sum_{t = 0}^{k}{(g_{i}^{t})}^{2}}$, and $\delta$ is some small positive number preventing from the division by zero and typically taken of the order $10^{- 8}$. AdaGrad can be considered as a special case of SGD with different per-coordinate stepsizes.

<!-- chunk {"id": "body-0177", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

The main advantage of AdaGrad is in its robustness to the choice of $h$: in practice, it often works well with the default value $h = 10^{- 2}$. Moreover, AdaGrad was shown to work well with sparse data duchi2013estimation. However, in the dense settings AdaGrad stepsizes rapidly decrease which leads to the slow convergence of the method wilson2017marginal.

<!-- chunk {"id": "body-0178", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

Adam. To resolve this issue of AdaGrad one can use exponential moving averages instead of sums $G_{i}^{k}$ leading to the method called RMSprop tieleman2012lecture. Then, based on RMSprop authors of kingma2014adam proposed one the most popular methods in deep learning -- Adam^77^7To distinguish exponents from superindexes we use braces $( \cdot )$ for exponents.:

<!-- chunk {"id": "body-0179", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

$\delta$ is some small positive number preventing from the division by zero and typically taken of the order $10^{- 8}$. Default values $\beta_{1} = 0.9$ and $\beta_{2} = 0.999$ from the original paper kingma2014adam often make Adam work well in practice. Adam was initially analyzed in the online convex case, but then authors of reddi2019convergence found out the flaw in the proof for Adam and proposed a convergent variant of Adam called AMSGrad.

<!-- chunk {"id": "body-0180", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

Convergence Guarantees. While the superiority of AdaGrad and Adam in comparison to SGD was noticed in many application duchi2013estimation; lacroix2018canonical; Goodfellow-et-al-2016, the best-known complexity bounds for AdaGrad, Adam, and their modifications are the same or even worse than ones for SGD chen2018convergence; zhou2018convergence; zaheer2018adaptive; ward2019adagrad; defossez2020convergence. Furthermore, these complexity results in non-convex case under more restrictive assumption, e.g., uniformly bounded second moment of the stochastic gradient, than their counterparts for SGD. Among other works providing complexity results for Adam and AdaGrad in the non-convex case we emphasize defossez2020convergence because of the generality and the simplicity of the proofs. Moreover, the unified analysis of proximal variants of AdaGrad and Adam was proposed in yun2020general. Furthermore, we emphasize the recent work shi2020rmsprop where authors analyse RMSprop without assuming uniform boundedness of the gradients.

<!-- chunk {"id": "body-0181", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

Next, in zhang2019adam the theoretical and empirical study why Adam sometimes behaves significantly better than SGD was conducted. The authors of zhang2019adam empirically discovered that Adam performs better than SGD when stochastic gradients are heavy-tailed and the reason is that Adam does an "adaptive gradient clipping" goodfellow2016deep; gorbunov2020stochastic; mikolov2012statistical; pascanu2013difficulty; usmanova2017master; gorbunov2021near-optimal. In the same work zhang2019adam authors showed that in such situations SGD can fail to converge while clipped-SGD (with general and coordinate-wise clipping operators) provably converges to $\epsilon$-stationary point. Moreover, in zhang2019gradient it was shown that Gradient Descent with clipping converges even under weaker assumption than $L$-smoothness in the non-convex case with the rate $\sim \epsilon^{- 2}$ while Gradient Descent in the same settings can converge arbitrary slower.

<!-- chunk {"id": "body-0182", "role": "body", "section": "AdaGrad and Adam", "weight": 1.0} -->

Then, the bound from zhang2019gradient was improved in zhang2020improved. Finally, it is known goodfellow2016deep that clipped-SGD works better than SGD in the vicinity of extremely steep cliffs. A very similar approach based on the normalization of Gradient Descent was also studied in hazan2015beyond; levy2016power.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Adaptive SGD", "weight": 1.0} -->

The approach described in Section 4.1 for general stochastic optimization problem with the objective given as was recently extended in dvinskikh2020line-search to obtain adaptive methods with Armijo-type line-search for stochastic non-convex optimization. To do that they consider Algorithm 3 with the mini-batch stochastic gradient and mini-batch size $r = {\max{\{ 1,{{8\sigma_{0}^{2}}/\varepsilon^{2}}\}}}$, where $\sigma_{0} \geqslant \sigma$. In each iteration $k$ of Algorithm 3 the stepsize is taken as $h_{k} = {1/L_{k}}:={1/\left( {2^{i_{k} - 1}L_{k - 1}} \right)}$ by increasing $i_{k} \geqslant 0$ until the inequality

<!-- chunk {"id": "body-0184", "role": "body", "section": "Adaptive SGD", "weight": 1.0} -->

is satisfied. This inequality is an inexact upper quadratic bound which follows for sufficiently large $L_{k}$ from the $L$-smoothness and bounded variance. Thus, $L_{k}$ plays the role of a guess of the Lipschitz constant $L$ locally between the points $x^{k}$ and $x^{k + 1}$. The authors of dvinskikh2020line-search propose also methods for convex problems based on the same idea with the difference that in the convex case the mini-batch size $r$ depends on the iteration counter $k$. Careful choice of this dependence allows to simultaneously adaptively choose both the stepsize $h_{k}$ and the mini-batch size $r_{k}$. These methods have the same, up to logarithmic factors, iteration complexity and total number of stochastic oracle calls as their non-adaptive counterparts.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Adaptive SGD", "weight": 1.0} -->

In particular, for the non-convex case the iteration complexity to obtain $\varepsilon$-stationary point is $\overset{\sim}{O}\left( {{L\left( {{f\left( x^{0} \right)} - f_{\ast}} \right)}/\varepsilon^{2}} \right)$ and the oracle complexity is $\overset{\sim}{O}\left( {L\left( {{f{(x^{0})}} - f_{\ast}} \right){\max\left\{ {1/\varepsilon^{2}},{\sigma^{2}/\varepsilon^{4}} \right\}}} \right)$. Moreover, empirically, the methods designed for convex problems turned out to be more efficient on non-convex problems than the method designed for non-convex problems.

<!-- chunk {"id": "body-0186", "role": "body", "section": "First-Order Methods under Additional Assumptions", "weight": 1.0} -->

In the previous parts of the paper, we focused on general non-convex problems. In this section, we consider two subclasses of non-convex objective functions which satisfy assumptions weaker than convexity and, at the same time, strong enough to obtain good global convergence rates of optimization algorithms. For simplicity, we consider an unconstrained optimization problem with $Q = {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

A function $f{(x)}$ is said to satisfy the Polyak--Łojasiewicz (PŁ) condition polyak1963gradient; lojasiewicz1963topological (or to be gradient dominated) if for all $x \in {\mathbb{R}}^{n}$

<!-- chunk {"id": "body-0188", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

This condition implies that any stationary point of $f{(x)}$ is a global minimum, although it is not necessarily unique. In particular, this property holds for strongly convex functions. It was first shown in polyak1963gradient that if the objective is also $L$-smooth, then gradient descent linearly converges to a global minimum, i.e.,

<!-- chunk {"id": "body-0189", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

The Polyak--Łojasiewicz condition is naturally satisfied for the problems of solving nonlinear systems of equalities ${g{(x)}} = 0$, where $g{(x)}$ is a vector-valued function. This problem can be equivalently reformulated as

<!-- chunk {"id": "body-0190", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

where $J_{g}{(x)}$ is the Jacobian matrix of $g{(x)}$, one can show that

<!-- chunk {"id": "body-0191", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

which is exactly the Polyak--Łojasiewicz condition since ${g{(x^{\ast})}} = 0$. An extensive survey of first-order optimization methods under this condition, as well as its relationship with other classes of functions, can be found in karimi2016linear. An interesting example of the emergence of PŁ condition in Linear Feedback Control theory was recently described in fatkhullin2020optimizing and in over-parameterized deep learning in belkin2021fit.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

Next, consider the convergence of gradient descent under the PŁ condition in terms of relative accuracy $\overset{\sim}{\nabla}f{(x)}$

<!-- chunk {"id": "body-0193", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

where $\alpha \in {\lbrack 0,1)}$. Let the stepsize $h$ in gradient descent

<!-- chunk {"id": "body-0194", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

Combining this with the Lipschitz condition, we obtain

<!-- chunk {"id": "body-0195", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

As a result, we achieve a linear convergence rate for the gradient descent under the PŁ condition.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

In general case the main ingredient that guaranties global linear convergence under PŁ condition is an estimate like

<!-- chunk {"id": "body-0197", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

where $\theta{(N)}$ -- some decreasing function, i.e.. We assume that there exists such $N{(\mu)}$, that ${\theta\left( {N{(\mu)}} \right)} \leq \mu$, i.e. for ${N{(\mu)}} = {{2L}/\mu}$. In this case from PŁ condition

<!-- chunk {"id": "body-0198", "role": "body", "section": "Polyak--Łojasiewicz Condition", "weight": 1.0} -->

By applying restarts we obtain oracle complexity $\overset{\sim}{O}\left( {N{(\mu)}} \right)$.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Stochastic First-Order Methods under Polyak--Łojasiewicz Condition", "weight": 1.0} -->

The majority of the methods described in Section 4 are analyzed under PŁ condition as well. That is, one can find the state-of-the-art results for different variants of SGD and non-accelerated variance reduced methods like SVRG and SAGA in li2020unified, accelerated variance reduced methods like PAGE in li2020page, the tightest known analysis of Random Reshuffling under PŁ condition in ahn2020sgd, and the convergence results for SGD in the over-parameterized case with constant, Armijo-type, and stochastic Polyak's stepsizes in vaswani2018fast, vaswani2019painless, and loizou2020stochastic respectively. The summary of known complexity results for the stochastic methods under PŁ condition is given in Table 4. We emphasize that the analysis from gower2020sgd is derived under so-called expected residual (ER) assumption on the stochastic gradient $g{(x)}$: there exists such constant $\rho > 0$ that

<!-- chunk {"id": "body-0200", "role": "body", "section": "Stochastic First-Order Methods under Polyak--Łojasiewicz Condition", "weight": 1.0} -->

Rather simple introduction (close to the state of the art results) for SGD with bias under PŁ condition can be find in ajalloeian2020analysis.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Star-convexity and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

A function $f{(x)}$ is called star-convex if for some global minimizer $x^{\ast}$ and for all $\lambda \in {\lbrack 0,1\rbrack}$ and $x \in {\mathbb{R}}^{n}$

<!-- chunk {"id": "body-0202", "role": "body", "section": "Star-convexity and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

While any interval connecting two points on the graph of a convex function lies not lower than the graph, for a star-convex functions this is assumed only for intervals connecting some fixed global minimizer and any other point on the graph. This condition is considerably weaker than convexity, even for functions of one variable. For example, the function ${|x|}{({1 - e^{- {|x|}}})}$ is a non-convex star-convex function. The authors of lee2016optimizing analyze a cutting plane method for minimization of this class of functions and obtain a polylogarithmic in $\varepsilon$ and polynomial in $n$ complexity bound using only function evaluations. The authors of guminov2019accelerated; nesterov2020primal-dual prove that the same Algorithm 1 possesses the following convergence rate for star-convex $L$-smooth functions

<!-- chunk {"id": "body-0203", "role": "body", "section": "Star-convexity and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

A more general class of functions is the class of $\alpha$-weakly-quasi-convex functions satisfying

<!-- chunk {"id": "body-0204", "role": "body", "section": "Star-convexity and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

for some $\alpha \in {(0,1\rbrack}$ and some global minimizer $x^{\ast}$. Continuously differentiable 1-weakly-quasi-convex functions are exactly the star-convex functions. The authors of guminov2017accelerated propose an algorithm with iteration complexity $O{({\alpha^{- 1}L^{1/2}R\varepsilon^{- {1/2}}})}$, where $R$ is an upper bound on the initial distance to the point $x^{\ast}$. A slightly worse bound $O{({\alpha^{- {3/2}}L^{1/2}R\varepsilon^{- {1/2}}})}$ is obtained in nesterov2020primal-dual by restarting Algorithm 1. Both approaches require a line search for which the complexity also needs to be estimated.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Star-convexity and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

The authors of hinder2020near analyze this complexity and propose an algorithm with $O{({\alpha^{- 1}L^{1/2}R\varepsilon^{- {1/2}}})}$ iteration complexity and the same up to a logarithmic factor in $\alpha^{- 1}\varepsilon^{- 1}$ number of function and gradient evaluations. Moreover, they provide a similar lower complexity bound, thus proving that their method is optimal. Further, they also consider a class of $(\alpha,\mu)$-strongly quasi-convex functions satisfying

<!-- chunk {"id": "body-0206", "role": "body", "section": "Star-convexity and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

and provide an algorithm which has iteration complexity

<!-- chunk {"id": "body-0207", "role": "body", "section": "Star-convexity and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

and requires up to a logarithmic factor the same number function and gradient evaluations. Similar optimal complexity bounds for accelerated gradient method for $\alpha$-weakly-quasi-convex functions and $(\alpha,\mu)$-strongly quasi-convex functions were obtained in bu2020note by extending the estimating sequence technique.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Stochastic Methods and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

The most general analysis of SGD under $\alpha$-weak-quasi-convexity is provided in gower2020sgd. As it was mentioned earlier, authors of gower2020sgd consider finite-sum optimization problems^88^8In fact, most of the results from gower2020sgd do not rely on the finite-sum structure of $f$. + and derive complexity bounds for SGD under expected residual assumption on the stochastic gradient for the $\alpha$-weak-quasi-convex function and functions satisfying PŁ condition.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Stochastic Methods and $\\alpha$-weak-quasi-convexity", "weight": 1.0} -->

where $\sigma_{\ast}^{2} = {{\mathbb{E}}{\lbrack{\|{g{(x^{\ast})}}\|}_{2}^{2}\rbrack}}$ is the variance of the stochastic gradient at the solution. Note, that when interpolation condition holds this bounds reduces to $O\left( {{\left( {\rho + L} \right)R_{0}^{2}}/\left( {\alpha^{2}\varepsilon} \right)} \right)$. Moreover, under interpolation condition the authors of gower2020sgd also derived that the generalized version of stochastic Polyak stepsize for stochastically reformulated problem + converges with the rate

<!-- chunk {"id": "body-0210", "role": "body", "section": "Further Generalizations", "weight": 1.0} -->

A more wide class of functions that covers the class of $\alpha$-weakly-quasi-convex functions referred to as approximately homogeneous functions satisfying the condition

<!-- chunk {"id": "body-0211", "role": "body", "section": "Further Generalizations", "weight": 1.0} -->

where $\partial{f{(x)}}$ is a subgradient of $f{(x)}$ and $N,M$ are some constants. This class of functions was first defined in shor1967generalized and discussed in polyak1987introduction.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Further Generalizations", "weight": 1.0} -->

In general, if there exist good lower and upper convex models for non-convex target function, one can derive that complexity of such problem is similar to convex ones rather than non-convex (see bazarova2020linearly and references therein).

<!-- chunk {"id": "body-0213", "role": "body", "section": "Second-Order Methods", "weight": 1.0} -->

Another branch of optimization incremental methods for solving are methods that use the second-order information about the function. This information is very helpful to escape saddle-points by using a negative curvature. Next we define an $(\varepsilon,\delta)$-second-order stationary point $x^{\ast}$ if

<!-- chunk {"id": "body-0214", "role": "body", "section": "Second-Order Methods", "weight": 1.0} -->

Next in this section we suppose that $f{(x)}$ has $L_{2}$-Lipschitz second-order derivative. The basic method for this class of problems is a Cubic Regularization method (CR) nesterov2006cubic.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Second-Order Methods", "weight": 1.0} -->

where $H \geq 0$. It globally converges to the minimum for convex functions and converges to a $(\varepsilon,\delta)$-second-order stationary point for non-convex function within $O{(\varepsilon^{- {3/2}})}$ number of iterations. Note, that the subproblem is also non-convex but in nesterov2006cubic authors proposed a method to solve this problem as a convex problem via special choose of $H$ and line-search for a dual problem. A related line of work considers trust region methods conn2000trust; cartis2011adaptive; cartis2011adaptive2; cartis2017improved; cartis2019universal, where a classical Newton step is calculated on a Euclidean ball of a carefully chosen radius. Both cubic regularized Newton methods and trust region methods can be extended to work for constrained problems with linear and conic constraints haeser2019optimality; dvurechensky2019generalized; dvurechensky2021hessian.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Second-Order Methods", "weight": 1.0} -->

In general, all these algorithms work well for the problems in moderate dimensions. Unfortunately, for many large-scale Machine Learning problems it is hard to calculate the full Hessian and the inverse such a large matrix. Recent work has therefore explored the use of Hessian-vector products ${{\nabla^{2}f}{(x)}} \cdot s$, which can be computed as efficiently as gradients in many cases including neural networks by using autogradient technique. By this Hessian-vector product we can efficiently find $x_{\text{Cubic}}^{k + 1}$ by variants of gradient descent carmon2016gradient. Several algorithms incorporating Hessian-vector products allen2018make; allen2018natasha have been shown to achieve faster convergence rates than gradient descent in the non-stochastic setting. However, in the stochastic setting where we only have access to stochastic Hessian-vector products, significantly less progress has been made.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Second-Order Methods", "weight": 1.0} -->

One of the improvement of this method was done in wang2020cubic. The authors introduce a momentum step and obtain faster convergence rate. This technique is widely used to speed up the first order methods and also can speed up the second order method.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Second-Order Methods", "weight": 1.0} -->

Also, second-order methods that have access to the Hessian of $f$ can exploit negative curvature to more effectively escape saddles and arrive at local minima. To show this concept we introduce one of such methods wright2018optimization. There are two types of steps: gradient steps and a step in a negative curvature for the Hessian. So

<!-- chunk {"id": "body-0219", "role": "body", "section": "Second-Order Methods", "weight": 1.0} -->

There are different policies to $\alpha_{k}$ and gradient steps. The main idea here is to use the first-order methods as a cheap main method and switch to expensive second-order methods when we reach local stationary point and want to escape it to find a better local minimum. Methods with this idea are still developing. In ge2015escaping; jin2017how it was proved that gradient methods with additive noise are able to escape from nondegenerate saddle points and find approximate local minima. These ideas lead to the state of art first-order methods to find local minima with Hessian-vector product carmon2018accelerated; royer2018complexity; allen2018natasha; xu2018first; allen2018neon2; jin2018accelerated; fang2018spider; nguyen2017sarah. In recent works fang2019sharp; jin2019nonconvex; roy2020escaping it was proved that stochastic gradient descent can escape from saddle point and converges to approximate local minima.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

Now we move to stochastic version of problem. Firstly, we speak about online version, where we minimize expectation of some stochastic function. In the work tripuraneni2018stochastic authors propose a stochastic optimization method that utilizes stochastic gradients and Hessian-vector products to find an $(\varepsilon,\delta)$-second-order stationary point using only $O{(\varepsilon^{- 3.5})}$ oracle evaluations. This rate improves upon the $O{(\varepsilon^{- 4})}$ rate of stochastic gradient descent, and matches the best-known result for finding local minima without the need for any delicate acceleration or variance reduction techniques.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

This is a stochastic cubic regularization algorithm in Algorithm 10. To obtain stochastic gradients and Hessians, we can sample independent batches of $S_{1}$and $S_{2}$ in each iteration, but they can also be connected so that $S_{2} \subseteq S_{1}$. The average gradient is denoted by

<!-- chunk {"id": "body-0222", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

This subproblem should be solved by special gradient-based subroutine. It is written in details in tripuraneni2018stochastic. Since only the gradient is used to solve the subproblem, we need to compute only a Hessian-vector product $B^{k}{\lbrack s\rbrack}$ but not a full Hessian $B^{k}$. If our function can be represented by a computational tree, then we can use autogradient techniques and compute Hessian-vector products as fast as we compute gradients up to a small constant.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

How many Hessians should we take? By concentration inequalities it is possible to show that we need

<!-- chunk {"id": "body-0224", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

So in total, the method converges with $O\left( \varepsilon^{- {3/2}} \right)$ iterations and $O\left( \varepsilon^{- {5/2}} \right)$ Hessian calculations of the function.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

In paper arjevani2020second this approach is improved by using special variance reduction technique. Authors get method that needs only $O{(\varepsilon^{- 3})}$ gradients and Hessian-vector products for finding second-order stationary point. Also, in this article authors prove lower bounds for higher-order stochastic problems.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

What is the main advantage of such methods? We calculate fewer Hessians than in the full CR version and also do it in parallel if we have many cores for computing. The simplicity of the algorithms, both at fast rates and when escaping from saddle-points, leads us to very good optimization methods for non-convex stochastic problems.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

Next we go to offline version that works with sum of functions.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

where $f_{i}{(x)}$ has Lipschitz continuous Hessian. In this regime we have $m$ functions and hence classic CR needs to compute $O{({m\varepsilon^{- {3/2}}})}$ Hessians. To reduce it in papers kohler2017sub; xu2020newton authors used subsampled gradient and subsampled Hessian, which achieve $\overset{\sim}{O}{({{m\varepsilon^{- {3/2}}} \land \varepsilon^{- {7/2}}})}$ gradient complexity and $\overset{\sim}{O}{({{m\varepsilon^{- {3/2}}} \land \varepsilon^{- {5/2}}})}$ Hessian complexity similarly to the previous section. Next appears many articles with different stochastic variance-reduced cubic(SVRC) methods.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

To collect this results in one place we add a table (see Table 5) with the convergence rates, where ${a \land b} = {\min{\{ a,b\}}}$.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Stochastic Second-Order Methods", "weight": 1.0} -->

As a result, we have a method that not only works efficiently with the big sum by utilizing stochastic nature, but also employs Hessian information to escape saddles more effectively and arrive at to better local minimum. This statement is supported by the experiments described in xu2020second; osawa2018second; martens2010deep; park2020combining. The authors of these papers experiment with various second-order methods and show how they compete with first-order methods without any second-order information in practice. These papers' main conclusions are that second-order methods find deeper local minima and avoid saddle-points. They are more robust when hyperparameters are used. Subsampling speeds up computations and allows for the parallelization of such methods. As a result, second-order methods may be competitive with first-order methods in practice.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

Next, we present high-order or tensor methods for finding local minima of a highly smooth and non-convex objective function. High-order derivatives better describe functions and enable you to use curvature to improve convergence.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

First, we lay out some standard assumptions about the smoothness of the function $f$. In the following, we will denote the directional derivative of the function $f$ at $x$ along the directions ${h^{j} \in {\mathbb{R}}^{n}},{j = {1,\ldots,p}}$ as

<!-- chunk {"id": "body-0233", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

The functions $f_{i}$ for each $p = {0,\ldots,3}$ has $L_{p}$-Lipschitz-continuous derivatives,

<!-- chunk {"id": "body-0234", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

From this inequality we get next tensor method for $p = 3$,

<!-- chunk {"id": "body-0235", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

In papers birgin2017worst; carmon2019lowerI; carmon2019lowerII it was proved that tensor $p$-order method with Taylor approximation is optimal, match lower bounds, and converges with the rate $O{(\varepsilon^{- {{({p + 1})}/p}})}$ for non-convex problems, hence for the third-order methods we get the rate $O{(\varepsilon^{- {4/3}})}$ instead of $O{(\varepsilon^{- {3/2}})}$ for the second-order methods. So, we get that third-order methods are faster than second-order methods in terms of iterations.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

Another crucial motivation is that the second-order method could get stuck at the so-called degenerate saddle point, where the Hessian matrix has nonnegative eigenvalues with some eigenvalues equal to 0 anandkumar2016efficient.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

In paper zhu2020adaptive it is shown how gradient descent and cubic regularization method stuck in such points for even small problems, like ${f{(x,y)}} = {x^{3} - {3xy^{2}}}$ in degenerate saddle point $$. So, we should use third-order information to escape them.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

This lead us to the third-order critical point. We define next critically measures

<!-- chunk {"id": "body-0239", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

Third-order method converges to a $(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})$-third-order critical point with the rate $O\left( {\max\left( \varepsilon_{1}^{- {4/3}},\varepsilon_{2}^{- 2},\varepsilon_{3}^{- 4} \right)} \right)$.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

But the calculation of the third-order derivative would be very computationally expensive. This problem leads us to stochastic tensor methods. The main idea of the stochastic method that by different concentration inequalities we can compute much fewer Hessians and third-order derivatives for sum type problems, than gradients. Correct proportions is written. For example, if we have $200000$ functions in sum, we may compute full gradient, only $10000$ Hessians and $100$ third-order derivatives and get the same speed as for full Hessian and full third-order derivatives.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

In paper by lucchi2019stochastic introduce such method that work with batch tensors and converges as fast as for full-batch methods. The optimization algorithm we consider is detailed in Algorithm 11. This algorithm uses sub-sampled derivatives instead of exact quantities and its implementation relies on tensor-vector products only. The proposed approach is shown to find an $(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3})$-third-order critical point in at most $O\left( {\max\left( \varepsilon_{1}^{- {4/3}},\varepsilon_{2}^{- 2},\varepsilon_{3}^{- 4} \right)} \right)$ iterations, thereby matching the rate of deterministic approaches.

<!-- chunk {"id": "body-0242", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

It is worth mentioning that the implementation of the algorithm does not require the computation of the Hessian or the third-order tensor, both of which would demand significant computational resources, but rather directly computes Tensor-vector products with a complexity of order $O{(n)}$.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

We will make use of the following condition in order to reach an $\varepsilon$-critical point (where $\varepsilon = \varepsilon_{1}$).

<!-- chunk {"id": "body-0244", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

In practice, we can choose the size of the sample sets $S^{g},S^{b}$ and $S^{t}$ as follows

<!-- chunk {"id": "body-0245", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

where $\overset{\sim}{O}$ hides poly-logarithmic factors and a polynomial dependency to $n$. We can see that due to the stochastic nature of the data and tensor concentration inequalities, we can use far fewer computations while still achieving the same convergence speed as a full-batch method.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

1: Input: Starting point x0 ∈ ℝn (e.g x0 = 0) 0 &lt; γ1 &lt; 1 &lt; γ2 &lt; γ3, 1 &gt; η2 &gt; η1 &gt; 0, and H0 &gt; 0, Hm i n &gt; 0
2: for k = 0, 1, …, until convergence do
3: Sample gradient gk, Hessian Bk and Tk such that Eq., Eq. &amp; Eq. hold.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

Algorithm 11 Stochastic Tensor Method (STM)

<!-- chunk {"id": "body-0248", "role": "body", "section": "Tensor Methods", "weight": 1.0} -->

As shown in emmenegger2021oracle, the lower bounds for sum type problem are still rather far from upper bound even for the second-order methods. Hence, further research in this area may lead to new methods for sum-type problems by using variance reduction techniques. Another branch of possible research is a combination of tensor methods with first or second-order methods.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

Gradient free or zeroth-order optimization methods, which use only function values, are becoming increasingly important in machine learning problems, especially in reinforcement learning malik2020derivativefree, black-box adversarial attacks on deep neural networks papernot2017practical and other problems with structure making gradients difficult or infeasible to obtain.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

While there is a class of methods that does not have any connection to the gradient, for example, random search algorithms Schumer1968 (which are one of the first methods of zeroth-order optimization, beside grid search), the Nelder--Mead algorithm nelder1965simplex, the model-based methods (see Chapters 2-6 and 10-11 in conn2009introduction ) or the recent stochastic three points (STP) method bergou2019stochastic and its momentum variant STMP gorbunov2020smtp most zeroth-order optimization methods use gradient estimations, such as ${g{(x)}} = {\sum_{i = 1}^{n}{\left\lbrack {\left( {{f\left( {x + {\mue_{i}}} \right)} - {f(x)}} \right)/\mu} \right\rbracke_{i}}}$ (where $e_{i}$ are columns of $n \times n$ identity matrix $I_{n}$, $i \in

<!-- chunk {"id": "body-0251", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

{\{ 1,\ldots,n\}}$), then for good enough functions ($f \in C_{L}^{1,1}$ i.e. continuously differentiable with Lipschitz-continuous gradient) it can be shown, for example, that ${\|{{g{(x)}} - {{\nabla f}{(x)}}}\|}_{2} \leqslant {\muL\sqrt{n}}$.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

One then can consider some first-order optimization scheme, replace actual gradients with their estimations, and use bounds like this to return to gradients from estimations in proofs, obtaining the results for the zeroth-order case relatively easy.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

While such deterministic zeroth-order schemes (like the $GD$ with gradient estimation of the same form as above) often suffer from the problem dimensionality because of the number of oracle calls needed to reconstruct the gradient ($n$ for the estimation mentioned above, see also berahas2020theoretical for other examples), in a randomized approach one can use two- or one- point schemes of gradient approximation which makes every iteration simpler, sometimes leading to better results in terms of oracle calls liu2018zerothorder. Another benefit of the stochastic approach is that such methods often have good theoretical properties, for example, the Gaussian smoothing approach nesterov2017random that gives a smoothed version of the initial function, for which the convergence of stochastic zeroth-order algorithm can be easily proved, which can be later used to show the convergence of the algorithm for the initial function. And there are setups (for example online learning bubeck2011introduction ) where one is limited to use only several (or even one) oracle queries thus being unable to construct the full gradient approximation, so the stochastic approach becomes the only option.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

We begin with the formalization of these zeroth-order randomized schemes - we have a problem with the form

<!-- chunk {"id": "body-0255", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

then stochastic zeroth-order methods generate $\{ x^{k}\}$ s.t.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Zeroth-Order Methods", "weight": 1.0} -->

In the subsections, we will discuss the characteristics of several zeroth-order gradient estimations and then the zeroth-order methods for sum-minimization type problems in a non-convex setup. Other information on gradient-free optimization (such as structured objectives) can be found in the recent survey Larson_2019.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

Let us start with the methods following the standard zeroth-order scheme of using gradient approximation to benefit from the analysis of first-order methods. In this section all methods have a form similar to the classic gradient descent

<!-- chunk {"id": "body-0258", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

with only difference that instead of the true gradient we use the gradient approximation $g{(x,u)}$. One way to build such gradient approximations is to use random directions to compute finite differences in the form

<!-- chunk {"id": "body-0259", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

It makes sense to use centrally symmetric distributions for $u^{k}$, for example uniformly distributed over the unit Euclidean sphere $S^{n - 1} = {\{{x \in {\mathbb{R}}^{n}}:{{\| x\|}_{2} = 1}\}}$ (see flaxman2005online; gorbunov2018accelerated; dvurechensky2021accelerated ), or $u^{k} \sim {\mathcal{N}{(0,I_{n})}}$ --- so-called Gaussian smoothing introduced in nesterov2017random. In this article, the authors proved Gaussian approximation

<!-- chunk {"id": "body-0260", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

they show only that this process converges to the stationary point of $f_{\mu}{(x)}$ -- consider $Q$ with ${\text{diam}{(Q)}} \leqslant R$, then it can be shown that we need to make

<!-- chunk {"id": "body-0261", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

with functional gap ${|{{f_{\mu}{(x)}} - {f{(x)}}}|} = {O\left( {\varepsilon/\left\lbrack n^{{({1 + \nu})}/2} \right\rbrack} \right)}$. For the case of $\nu = 1$ (i.e. $f \in C_{L_{1}}^{1,1}$) these results can be improved to $N = {O\left( {n/\varepsilon^{2}} \right)}$ ($n$ times better) achieving the same rate of convergence as in previous paper nesterov2017random.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

Such noisy setup is also interesting because it can be shown Risteski2016AlgorithmsAM, that for a non-convex function $\hat{f}{(x)}$ s.t. ${|{{\hat{f}{(x)}} - {f{(x)}}}|} \leqslant \varepsilon_{f}$, where initial $f$ is convex and $1$-Lipschitz and $\varepsilon_{f} \sim {\max\left\{ {\varepsilon^{2}/\sqrt{n}},{\varepsilon/n} \right\}}$ there exists an algorithm which finds a point $\overset{\sim}{x}$ s.t.

<!-- chunk {"id": "body-0263", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

This Gaussian smoothing technique was later used in works ghadimi2013stochastic (RSGF) and ghadimi2016mini-batch (RSPGF) to obtain complexity guarantees for stochastic zeroth-order optimization. In the first one (ghadimi2013stochastic ), the unconstrained problem $Q = {\mathbb{R}}^{n}$ is considered, where $\hat{f} = {F{(x,\xi)}}$ s.t. ${{\mathbb{E}}_{\xi}{\lbrack{F{(x,\xi)}}\rbrack}} = {f{(x)}}$ and $F{( \cdot,\xi)}$ has a Lipschitz-continuous gradient with constant $L_{1}$, $\xi$ is a random variable whose distribution $P$ is supported on $\Xi_{k} \subseteq R^{n}$. The procedure has a form similar to the one proposed in nesterov2017random

<!-- chunk {"id": "body-0264", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

The method then chooses the $x^{k}$ from generated ${\{ x^{k}\}}_{k = 1}^{N}$ as $k = R$ where $R$ is some random variable with a probability mass function $P_{R}$ supported on $\{ 1,\ldots,N\}$. The main goal to introduce this random iteration count $R$ is to derive new complexity results for non-convex stochastic optimization case.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

they obtain (ghadimi2013stochastic \[Theorem 3.2\])

<!-- chunk {"id": "body-0266", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

where the expectation is taken with respect to $R$, $\{\xi^{k}\}$. After choosing specific constant stepsizes $h_{k} = {{1/\left\lbrack \sqrt{n + 4} \right\rbrack} \cdot {\min\left\{ {1/\left\lbrack {4L\sqrt{n + 4}} \right\rbrack},{\overset{\sim}{D}/\left\lbrack {\sigma\sqrt{N}} \right\rbrack} \right\}}}$ (note that this makes $P_{R}$ uniform on $\{ 1,\ldots,N\}$) they get (ghadimi2013stochastic \[Corollary 3.3\])

<!-- chunk {"id": "body-0267", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

where $\overset{\sim}{D} > 0$ is our estimation of $D_{f}$ (for example some upper bound). It can be shown that to ensure ${{\mathbb{P}}{\{{{\|{{\nabla f}{(x^{R})}}\|}_{2}^{2} \leqslant \varepsilon}\}}} \geqslant {1 - \Lambda}$ (so-called $(\varepsilon,\Lambda)$-solution) the total number of calls to the oracle $\hat{f}$ can be bounded as

<!-- chunk {"id": "body-0268", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

Another method that is considered in ghadimi2013stochastic is a two-phase method (2-RSGF), which uses the first one (RSGF) $S = {\log\left( {2/\Lambda} \right)}$ times as a subroutine producing a list of candidates ${\{{\overline{x}}^{k}\}}_{k = 1}^{S}$ and then the output point ${\overline{x}}^{\ast}$ is chosen in such a way that

<!-- chunk {"id": "body-0269", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

then it can be shown (ghadimi2013stochastic \[Theorem 3.4\]) that $(\varepsilon,\Lambda)$-solution will be achieved after taking

<!-- chunk {"id": "body-0270", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

calls to the $\hat{f}$ which is better than the previous one in terms of $\Lambda$.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

A more general problem ${{\min_{x \in Q \subseteq {\mathbb{R}}^{n}}\Psi}{(x)}} = {{f{(x)}} + {h{(x)}}}$, where $f \in C_{L}^{1,1}$ and $h{(x)}$ is a simple convex and possibly non-smooth function is considered in ghadimi2016mini-batch. They use a mini-batched version of gradient estimation from the previous paper ghadimi2013stochastic and generalized projection obtaining (ghadimi2016mini-batch \[Theorem 4, Corollaries 6-7\]) similar bounds for the gradient norm.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

In Sener2020Learning, the authors use symmetric gradient estimations based on uniform distribution over the sphere to build a less dimension depending method.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

which is much better than the previous one (because $d \ll n$). However, this is impractical due to the fact that it requires the knowledge of $\theta^{\ast}$. Authors mix two previous estimations and estimate $\theta$ and $\psi$ on every step, obtaining the method that (Sener2020Learning \[Theorem 1\]) after $N$ steps ensures

<!-- chunk {"id": "body-0274", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

which is better than the initial bound for $d \leqslant n^{1/2}$.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

While such gradient estimates based on random directions are common it can be shown that in terms of the number of samples required to the approximate gradient to ensure norm condition (or at least ensure it with some probability) random directions based methods lose to standard finite differences berahas2020theoretical; berahas2019global; berahas2019linear.

<!-- chunk {"id": "body-0276", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

The main idea in berahas2020theoretical is to compare the number of calls r (essentially a batch size) to the oracle $\hat{f}{(x)}$ that will be enough to ensure norm condition

<!-- chunk {"id": "body-0277", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

for zeroth-order gradient estimation $g{(x)}$. This condition simplifies the transition from gradient estimations to gradient when proving the convergence of algorithms. One of its implications is that $g{(x)}$ is a descent direction for the function $\phi$. In berahas2019global the line-search method that uses such gradient approximations, ensuring the norm condition, is shown to converge.

<!-- chunk {"id": "body-0278", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

They consider several methods of gradient estimation, deterministic (Forward and Central Finite Differences ($FFD$ and $CFD$) and Linear Interpolation ($LI$) as generalization) and stochastic (Gaussian Smoothed Gradients ($GSG$ and its centered version $cGSG$) and Sphere Smoothed Gradients ($BSG$ and $cBSG$)), for the latter authors obtain the number of calls needed to ensure the norm condition with probability $1 - \delta$.

<!-- chunk {"id": "body-0279", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

Let us take a look at two of these methods: $FFD$ and $GSG$. For the first one, the gradient estimation takes the form

<!-- chunk {"id": "body-0280", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

where $e_{i}$ are the columns of $I_{n}$. It can be shown that for such $g{(x)}$ the following holds

<!-- chunk {"id": "body-0281", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

If there was no noise ($\varepsilon_{f} = 0$) we could make this approximation as close to the gradient as we want, so we would be able to ensure the norm condition in $n$ calls to the $\hat{f}$. This is also true for a small enough noise (for example even from this inequality we can take $\varepsilon_{f} = {{L\mu^{2}}/4}$ obtaining ${\|{{g{(x)}} - {{\nabla f}{(x)}}}\|}_{2} \leqslant {\muL\sqrt{n}}$). Authors provide such noise bound in form of lower bound on ${\|{{\nabla f}{(x)}}\|}_{2}$ for which the norm condition can still be ensured

<!-- chunk {"id": "body-0282", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

For the $GSG$ they consider the mini-batched version of Gaussian smoothing from nesterov2017random

<!-- chunk {"id": "body-0283", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

and prove that the norm condition will be ensured with probability $1 - \delta$ after

<!-- chunk {"id": "body-0284", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

calls, which is while linear on $n$ is still worse than the plain $n$ in $FFD$, because of $\delta$, and additional constants. However, this is a sufficient number of calls, not a necessary, so authors derive the lower bound for $r$ (berahas2020theoretical \[Section 2.3.1\])

<!-- chunk {"id": "body-0285", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

necessary to have probability ${{\mathbb{P}}{({{\|{{g{(x)}} - {{\nabla f}{(x)}}}\|}_{2} \leqslant {\theta{\|{{\nabla f}{(x)}}\|}_{2}}})}} > {1 - \delta}$. In their numerical experiments they show that to ensure the norm condition with $\theta < {1/2}$ with probability of at least $1/2$ more than $n$ oracle calls are needed, so this lower bound is weak.

<!-- chunk {"id": "body-0286", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

The sufficient lower bound can be improved using smoothing on a sphere for which they obtain $\Omega\left( {{n/\theta^{2}} \cdot {\log\left\lbrack {\left( {n + 1} \right)/\delta} \right\rbrack}} \right)$, yet it is still worse than deterministic variants, and in practice its behavior is very similar to the Gaussian directions based approach.

<!-- chunk {"id": "body-0287", "role": "body", "section": "Random Directions Gradient Estimations", "weight": 1.0} -->

There are also results for the case of ${f{(x)}} \in C_{M}^{2,2}$ (centered versions of the estimations), they can be found in Table 6.

<!-- chunk {"id": "body-0288", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

One special case of the ${\min f}{(x)}$ problem is the finite sum minimization which was considered in previous sections for the first-order methods. These problems in zeroth-order setup arise in reinforcement learning fazel2019global (there as a minimization of a long-term cost which is essentially a sum of functions) and non-stationary online optimization problems zhang2020boosting.

<!-- chunk {"id": "body-0289", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

Let us start with the ZO-SVRG from liu2018zerothorder -- a zeroth-order version of SVRG from johnson2013accelerating.

<!-- chunk {"id": "body-0290", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

There a non-convex finite-sum problem of the form

<!-- chunk {"id": "body-0291", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

and consider several different gradient estimates: two based on random directions on a unit sphere (in notation of berahas2019global these are $BSG$ with $N = 1$ and $N = q$ (see Table 6), called RandGradEst and Avg-RandGradEst respectively), and one deterministic coordinate estimation (variant of $CFD$ from Table 6 with possibly different $\mu_{j}$ for each direction $e_{j}$ called CoordGradEst)

<!-- chunk {"id": "body-0292", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

0: stepsizes {hsk}, epoch length T, starting point x0 ∈ ℝn, batch size r ≥ 1, smoothing parameter μ &gt; 0, number of iterations N = S ⋅ T
Uniformly randomly pick set Ik from {1, …, m} such that |Ik| = r
$g^{k} = {{\frac{1}{r}{\sum\limits_{i \in I_{k}}\left( {{\hat{\nabla}f_{i}{(x_{s}^{k})}} - {\hat{\nabla}f_{i}{(\phi_{s})}}} \right)}} + {\hat{\nabla}f{(\phi_{s})}}}$
xsk + 1 = xsk − hsk gk
Pick ξ uniformly at random from {0, …, N − 1}
Algorithm 12 ZO-SVRG liu2018zerothorder

<!-- chunk {"id": "body-0293", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

For a mini-batch $I \subseteq {\{ 1,\ldots,m\}}$ of size $r$, authors denote

<!-- chunk {"id": "body-0294", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

and the algorithm is the same as for SVRG (Algorithm 6), with the only difference that instead of true gradients update

<!-- chunk {"id": "body-0295", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

This estimation $\hat{\nabla}f{(x_{s}^{0})}$ is no longer unbiased for zeroth-order gradient estimations, and that is the main problem for the convergence analysis of this method. They show that under assumptions mentioned above ZO-SVRG algorithm after $N = {S \cdot T}$ (there $S$ is a number of epochs) steps ensures that

<!-- chunk {"id": "body-0296", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

there $n$ is a dimension, $r = {|I|}$ -- batch size, $q$ is the number of directions used to estimate gradient via Avg-RandGradEst, $\overline{x}$ is uniformly chosen from ${\{ x_{s}^{k}\}}_{{s,k} = 0}^{{S - 1},{T - 1}}$, $N = {S \cdot T}$ is a total number of steps and

<!-- chunk {"id": "body-0297", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

Basically, that means that CoordGradEst, the deterministic policy of gradient estimations, achieves the convergence rates of the original SVRG. In their tests, however, in terms of training loss versus function queries ZO-SVRG (the variant without mini-batching and with random directions on the sphere) beats ZO-SVRG-Ave (based on Avg-RandGradEst) and ZO-SVRG-Coord (based on CoordGradEst).

<!-- chunk {"id": "body-0298", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

0: n0 ∈ [1, n1/2/6], Lipschitz constant L, epoch length T, starting point x0 ∈ ℝn, outer batch size r1 ≥ 1, inner batch size r2 ≥ 1, number of iterations N = S ⋅ T Uniformly randomly pick set Ik from {1, …, m} (with replacement) such that |Ik| = r1 Compute $g^{k} = {\sum\limits_{j = 1}^{n}{\left( {\frac{1}{r_{1}}{\sum\limits_{i \in I_{k}}\frac{\lbrack{{f_{i}{({x^{k} + {\mue_{j}}})}} - {f_{i}{(x^{k})}}}\rbrack}{\mu}}} \right)e_{j}}}$ Create set of pairs Ik = {(i,ui)} where i uniformly randomly picked from {1, …, m} (with replacement) and independent ui ∼ 𝒩

<!-- chunk {"id": "body-0299", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

Another discussed above algorithm that can be used in the zeroth-order finite-sum minimization setting is SPIDER fang2018spider. The zeroth-order variant (Algorithm 13) of the algorithm blends stochastic and deterministic gradient estimations, using mini-batched $FFD$ (Table 6) every $p$ steps to reconstruct $v^{k}$, which is later updated by mini-batched $GSG$.

<!-- chunk {"id": "body-0300", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

The $h_{k} = {\min\left( {\varepsilon/\left\lbrack {Ln_{0}\left\| v^{k} \right\|_{2}} \right\rbrack},{1/\left\lbrack {2Ln_{0}} \right\rbrack} \right)}$ is a stepsize policy from Normalized Gradient Descent (NGD, nesterov2004introduction ), where the stepsize is inverse-proportional to the norm of the gradient.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

Authors show, that after $N = {O\left( {1/\varepsilon^{2}} \right)}$ iterations and $O\left( {n{\min\left( {m^{1/2}/\varepsilon^{2}},{1/\varepsilon^{3}} \right)}} \right)$ (there $n$ is a dimension and $m$ is a number of functions) IZO calls (i.e. calls of the oracle that returns the value of $f_{i}{(x)}$ given $x$ and $i$) this algorithm ensures

<!-- chunk {"id": "body-0302", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

where $\overline{x}$ is uniformly chosen from ${\{ x^{k}\}}_{k = 0}^{N - 1}$. This result is better than what follows directly from nesterov2017random, at least by the factor of $m^{1/2}$ (the direct application of the results from nesterov2017random requires $m$ calls on every step, and gives ${{\mathbb{E}}{\lbrack{\|{{\nabla f}{(\overline{x})}}\|}_{2}\rbrack}} \leqslant \varepsilon$ in $O\left( {n/\varepsilon^{2}} \right)$ steps so the number of IZO calls would be $O\left( {{nm}/\varepsilon^{2}} \right)$).

<!-- chunk {"id": "body-0303", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

The results of two previously discussed papers liu2018zerothorder; fang2018spider were improved in the recent work ji2019improved. Authors show that ZO-SVRG-Coord actually has a better convergence rate (ji2019improved \[Theorem 2\]) of ${{\mathbb{E}}\left\lbrack {\|{{\nabla f}{(\overline{x})}}\|}_{2}^{2} \right\rbrack} = {O\left( {1/N} \right)}$ ($n$ times better than the previous analysis).

<!-- chunk {"id": "body-0304", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

At first they consider an intermediate variant of ZO-SVRG-Coord and ZO-SVRG-Ave called ZO-SVRG-Coord-Rand, that uses $CFD$ and $BSG$ (Table 6) for $\hat{\nabla}f{(\phi_{s})}$ and ${\hat{\nabla}f_{i}{(x_{s}^{k})}} - {\hat{\nabla}f_{i}{(\phi_{s})}}$ parts of

<!-- chunk {"id": "body-0305", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

(from Algorithm 12) respectively, while variants in liu2018zerothorder used only one type of gradient estimation at once. Then authors proof (ji2019improved \[Corollary 1\]) the convergence rate ${{\mathbb{E}}\left\lbrack {\|{{\nabla f}{(\overline{x})}}\|}_{2}^{2} \right\rbrack} = {O\left( {1/N} \right)}$ and show (ji2019improved \[Lemmas 1-2\]) that although the replacement of $BSG$ with $CFD$ requires $n$ more oracle calls it achieves more accurate gradient estimation so the convergence rate stays the same for the ZO-SVRG-Coord.

<!-- chunk {"id": "body-0306", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

Another part of this work is devoted to SPIDER. Authors construct a new algorithm (called ZO-SPIDER-Coord) in a way similar to the previous one -- they use $CFD$ instead of $GSG$ in Algorithm 13 and show that it has the same rate of convergence, but with bigger stepsize $h_{k} = {1/\left\lbrack {4L} \right\rbrack}$ (that doesn't depend on $\varepsilon$), which is better in practice.

<!-- chunk {"id": "body-0307", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

One particular case of finite-sum minimization is considered in zhang2020boosting. In this paper, authors consider non-stationary online optimization problems, when the objective function being queried is time-varying, so one is limited to the use of one-point estimators.

<!-- chunk {"id": "body-0308", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

Such estimators can be constructed easily in the stochastic zeroth-order case. For example we can consider $GSG$ (Table 6) with $N = 1$ then

<!-- chunk {"id": "body-0309", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

so we can chose ${g{(x)}}:={\left\lbrack {{f\left( {x + {\muu}} \right)}/\mu} \right\rbracku}$ and obtain a reasonable one-point estimation. The problem is that the variance of such estimations explodes as $\mu\rightarrow 0$ (see berahas2019global ).

<!-- chunk {"id": "body-0310", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

In this work, authors consider the residual feedback estimator

<!-- chunk {"id": "body-0311", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

(there $\nabla f_{\mu,k}$ is a gradient of smoothed $f_{k}$). They consider the online bandit problem with regret function

<!-- chunk {"id": "body-0312", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

and if additionally $f \in C_{L_{1}}^{1,1}$ (zhang2020boosting \[Theorem 4.3\])

<!-- chunk {"id": "body-0313", "role": "body", "section": "Variance-Reduced Zeroth-Order Methods", "weight": 1.0} -->

In their numerical experiments, authors compare conventional one-point and two-point approaches with one-point residual feedback. Even though the latter works worse than the two-point variant, it has lower variance and achieves better results than the conventional one-point feedback, and can be used in practice, in contrast to two-point feedback.

<!-- chunk {"id": "body-0314", "role": "body", "section": "Globalization Techniques", "weight": 1.0} -->

In the previous sections we mainly considered guarantees for the methods to converge to a stationary point or local extremum. Global performance guarantees are available only for some subclasses of non-convex minimization problems. Despite that there are several practical techniques for convergence globalization for the local methods, which we briefly describe next, following zhigljavsky2007stochastic.

<!-- chunk {"id": "body-0315", "role": "body", "section": "Multistart Technique", "weight": 1.0} -->

The first approach involves using an algorithm which converges to a local minimum and running it multiple times from different starting points. This may result in the algorithm for finding multiple local minima of the objective, some of which might in fact be global solutions.

<!-- chunk {"id": "body-0316", "role": "body", "section": "Multistart Technique", "weight": 1.0} -->

To be more concrete, we consider the problem

<!-- chunk {"id": "body-0317", "role": "body", "section": "Multistart Technique", "weight": 1.0} -->

Let the initial points be sampled from the uniform distribution on ${\lbrack 0,1\rbrack}^{n}$. If the Lebesgue measure of the attraction basin (the set of points, initialized at which the local algorithm converges to the global minimum) of the global minimum is $\mu > 0$, then the expected number of points required to find the global minimum is $m = {\overset{\sim}{O}\left( {1/\mu} \right)}$. If the attraction basin is a ball of radius $r$, then $\mu \sim r^{n}$. Hence, it is reasonable to expect that the number of initial points required depends on $n$ exponentially. For that reason, this approach to global optimization becomes impractical as $n$ grows.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Multistart Technique", "weight": 1.0} -->

The effectiveness of this approach also depends on the chosen initial points. The quality of a family of initial points $\left\{ x^{0,i} \right\}_{i = 1}^{m}$ can be characterized by the quantity

<!-- chunk {"id": "body-0319", "role": "body", "section": "Multidimensional Bisection", "weight": 1.0} -->

The main shortcoming of the approach described above is that the family $\left\{ x^{0,k} \right\}_{k = 1}^{m}$ is constructed without taking into account any properties of $f(x)$. Assume now that, for all ${x,y} \in {\lbrack 0,1\rbrack}^{n}$ $\left., \middle| f(y) - f(x) \middle| \leqslant M\parallel y - x\parallel \right.$. Then, for any $y$, the function ${f{(y)}} - {M{\|{x - y}\|}}$ is a minorant of $f{(x)}$.

<!-- chunk {"id": "body-0320", "role": "body", "section": "Multidimensional Bisection", "weight": 1.0} -->

In the one-dimensional case, each minorant is just a piecewise linear function, and its minimum is easy to compute explicitly. In higher-dimensions, this idea is more difficult to implement, and the resulting algorithms also tend to become slower as $n$ increases. This method also requires an estimate of the Lipschitz constant and is sensitive to the accuracy of this estimate.

<!-- chunk {"id": "body-0321", "role": "body", "section": "Langevin Dynamics", "weight": 1.0} -->

The last but not least approach which we consider in this section is inspired by the Langevin dynamics, which is defined by the stochastic differential equation

<!-- chunk {"id": "body-0322", "role": "body", "section": "Langevin Dynamics", "weight": 1.0} -->

where $W{(t)}$ is a Wiener process (also known as Brownian motion) and $T$ is the temperature parameter. It has been shown that the distribution of $x(t)$ converges to a distribution with density

<!-- chunk {"id": "body-0323", "role": "body", "section": "Langevin Dynamics", "weight": 1.0} -->

as $t\rightarrow\infty$, and as $T\rightarrow{0 +}$ this distribution concentrates around the global minima. To apply this in practice, the continuous dynamics has to be discretized.

<!-- chunk {"id": "body-0324", "role": "body", "section": "Langevin Dynamics", "weight": 1.0} -->

where $h > 0$ is the stepsize and $\epsilon_{k}$ is standard gaussian random variable. Non-asymptotic results demonstrating the convergence of this method to an approximate global minimum were presented in the work xu2018global. In this paper, the temperature parameter $T$ was assumed to be constant. However, other strategies are sometimes used in practice, for example,

<!-- chunk {"id": "body-0325", "role": "body", "section": "Langevin Dynamics", "weight": 1.0} -->

which ensures $T_{k}\rightarrow{0 +}$ as $k\rightarrow\infty$.
