Research centre Saclay--Île-de-France

### Contents

1. 0.1 Eigendecomposition of a Positive Definite Matrix
2. 0.2 The Multivariate Normal Distribution
3. 0.3 Randomized Black Box Optimization
4. 0.4 Hessian and Covariance Matrices
3. 1 Basic Equation: Sampling
4. 2 Selection and Recombination: Moving the Mean
5. 3 Adapting the Covariance Matrix
1. 3.1 Estimating the Covariance Matrix From Scratch
2. 3.3.2 Cumulation: Utilizing the Evolution Path
4. 3.4 Combining Rank-$\mu$-Update and Cumulation
8. A Algorithm Summary: The CMA-ES
1. B.1 Multivariate normal distribution
2. B.2 Strategy internal numerical effort
5. B.5 Boundaries and Constraints
10. C MATLAB Source Code
11. D Reformulation of Learning Parameter $c_{cov}$

## Nomenclature

We adopt the usual vector notation, where bold letters, $\mathbf{v}$, are column vectors, capital bold letters, $\mathbf{A}$, are matrices, and a transpose is denoted by ${\mathbf{v}}^{\mathsf{T}}$. A list of used abbreviations and symbols is given in alphabetical order.

### Abbreviations

: CMA Covariance Matrix Adaptation

: EMNA Estimation of Multivariate Normal Algorithm

: $({\mu/\mu_{\{ I,W\}}},\lambda)$-ES, Evolution Strategy with $\mu$ parents, with recombination of all $\mu$ parents, either Intermediate or Weighted, and $\lambda$ offspring.

: RHS Right Hand Side.

### Greek symbols

: $\lambda \geq 2$, population size, sample size, number of offspring, see.

: $\mu \leq \lambda$ parent number, number of (positively) selected search points in the population, number of strictly positive recombination weights, see.

: $\mu_{eff} = \left( {\sum_{i = 1}^{\mu}w_{i}^{2}} \right)^{- 1}$, the variance effective selection mass for the mean, see.

: ${\sum w_{j}} = {\sum_{i = 1}^{\lambda}w_{i}}$, sum of all weights, note that $w_{i} \leq 0$ for $i > \mu$, see also and (55-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")).

: ${\sum{|w_{i}|}^{+}} = {\sum_{i = 1}^{\mu}w_{i}} = 1$, sum of all positive weights.

: ${\sum{|w_{i}|}^{-}} = {- {({{\sum w_{j}} - {\sum{|w_{i}|}^{+}}})}} = {- {\sum_{i = {\mu + 1}}^{\lambda}w_{i}}} \geq 0$, minus the sum of all negative weights.

: $\sigma^{(g)} \in {\mathbb{R}}_{> 0}$, step-size.

### Latin symbols

: ${\mathbf{B}} \in {\mathbb{R}}^{n}$, an orthogonal matrix. Columns of $\mathbf{B}$ are eigenvectors of $\mathbf{C}$ with unit length and correspond to the diagonal elements of $\mathbf{D}$.

: ${\mathbf{C}}^{(g)} \in {\mathbb{R}}^{n \times n}$, covariance matrix at generation $g$.

: $c_{ii}$, diagonal elements of $\mathbf{C}$.

: $c_{1} \leq {1 - c_{\mu}}$, learning rate for the rank-one update of the covariance matrix update, see and (47-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")), and Table 1-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial").

: $c_{\mu} \leq {1 - c_{1}}$, learning rate for the rank-$\mu$ update of the covariance matrix update, see (3.2) and (47-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")), and Table 1-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial").

: $c_{\sigma} < 1$, decay rate for the cumulation path for the step-size control, see and (43-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")), and Table 1-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial").

: $c_{c} \leq 1$, decay rate for cumulation path for the rank-one update of the covariance matrix, see and (45-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")), and Table 1-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial").

: $c_{m} = 1$, learning rate for the mean.

: ${\mathbf{D}} \in {\mathbb{R}}^{n}$, a diagonal matrix. The diagonal elements of $\mathbf{D}$ are square roots of eigenvalues of $\mathbf{C}$ and correspond to the respective columns of $\mathbf{B}$.

: $d_{i} > 0$, diagonal elements of diagonal matrix $\mathbf{D}$, $d_{i}^{2}$ are eigenvalues of $\mathbf{C}$.

: $d_{\sigma} \approx 1$, damping parameter for step-size update, see and (44-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")).

: $\mathsf{E}$ Expectation value

: $f:{{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}},{{\mathbf{x}}\mapsto{f{({\mathbf{x}})}}}}$, objective function (fitness function) to be minimized.

: $f_{sphere}:{{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}},{{\mathbf{x}}\mapsto{\|{\mathbf{x}}\|}^{2} = {{\mathbf{x}}^{\mathsf{T}}{\mathbf{x}}} = {\sum_{i = 1}^{n}x_{i}^{2}}}}$.

: $g \in {\mathbb{N}}_{0}$, generation counter, iteration number.

: $\mathbf{I} \in {\mathbb{R}}^{n \times n}$, Identity matrix, unity matrix.

: ${\mathbf{m}}^{(g)} \in {\mathbb{R}}^{n}$, mean value of the search distribution at generation $g$.

: $n \in {\mathbb{N}}$, search space dimension, see $f$.

: $\mathcal{N}(\mathbf{0},\mathbf{I})$, multivariate normal distribution with zero mean and unity covariance matrix. A vector distributed according to $\mathcal{N}(\mathbf{0},\mathbf{I})$ has independent, $$-normally distributed components.

: ${\mathcal{N}({\mathbf{m}},{\mathbf{C}})} \sim {{\mathbf{m}} + {\mathcal{N}(\mathbf{0},{\mathbf{C}})}}$, multivariate normal distribution with mean ${\mathbf{m}} \in {\mathbb{R}}^{n}$ and covariance matrix ${\mathbf{C}} \in {\mathbb{R}}^{n \times n}$. The matrix $\mathbf{C}$ is symmetric and positive definite.

: ${\mathbb{R}}_{> 0}$, strictly positive real numbers.

: ${\mathbf{p}} \in {\mathbb{R}}^{n}$, evolution path, a sequence of successive (normalized) steps, the strategy takes over a number of generations.

: $w_{i}$, where $i = {1,\ldots,\lambda}$, recombination weights, see and (3.2) and (49-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial"))--(55-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")).

: ${\mathbf{x}}_{k}^{({g + 1})} \in {\mathbb{R}}^{n}$, $k$-th offspring/individual from generation $g + 1$. We also refer to ${\mathbf{x}}^{({g + 1})}$, as search point, or object parameters/variables, commonly used synonyms are candidate solution, or design variables.

: ${\mathbf{x}}_{i:\lambda}^{({g + 1})}$, $i$-th best individual out of ${\mathbf{x}}_{1}^{({g + 1})},\ldots,{\mathbf{x}}_{\lambda}^{({g + 1})}$, see. The index $i:\lambda$ denotes the index of the $i$-th ranked individual and ${f{({\mathbf{x}}_{1:\lambda}^{({g + 1})})}} \leq {f{({\mathbf{x}}_{2:\lambda}^{({g + 1})})}} \leq \cdots \leq {f{({\mathbf{x}}_{\lambda:\lambda}^{({g + 1})})}}$, where $f$ is the objective function to be minimized.

: ${\mathbf{y}}_{k}^{({g + 1})} = {{({{\mathbf{x}}_{k}^{({g + 1})} - {\mathbf{m}}^{(g)}})}/\sigma^{(g)}}$ corresponding to ${\mathbf{x}}_{k} = {{\mathbf{m}} + {\sigma{\mathbf{y}}_{k}}}$.

## Preliminaries

This tutorial introduces the CMA Evolution Strategy (ES), where CMA stands for Covariance Matrix Adaptation.^11^1Parts of this material have also been presented in and, in the context of *Estimation of Distribution Algorithms* and *Adaptive Encoding*, respectively. An introduction deriving CMA-ES from the information-geometric concept of a natural gradient can be found in. The CMA-ES is a stochastic, or *randomized*, method for real-parameter (continuous domain) optimization of non-linear, non-convex functions (see also Section 0.3 below).^22^2While CMA variants for *multi-objective* optimization and *elitistic* variants have been proposed, this tutorial is solely dedicated to single objective optimization and non-elitistic truncation selection, also referred to as comma-selection. We try to motivate and derive the algorithm from intuitive concepts and from requirements of non-linear, non-convex search in continuous domain. For a concise algorithm description see Appendix A-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial"). A respective Matlab source code is given in Appendix C.

Before we start to introduce the algorithm in Sect. 1, a few required fundamentals are summed up.

### Eigendecomposition of a Positive Definite Matrix

A symmetric, positive definite matrix, ${\mathbf{C}} \in {\mathbb{R}}^{n \times n}$, is characterized in that for all ${\mathbf{x}} \in {{\mathbb{R}}^{n}\backslash{\{\mathbf{0}\}}}$ holds ${{\mathbf{x}}^{\mathsf{T}}{{\mathbf{C}}{\mathbf{x}}}} > 0$. The matrix $\mathbf{C}$ has an orthonormal basis of eigenvectors, ${\mathbf{B}} = {\lbrack{\mathbf{b}}_{1},\ldots,{\mathbf{b}}_{n}\rbrack}$, with corresponding eigenvalues, ${d_{1}^{2},\ldots,d_{n}^{2}} > 0$.

> That means for each ${\mathbf{b}}_{i}$ holds
> $${{{\mathbf{C}}{\mathbf{b}}}_{i} = {d_{i}^{2}{\mathbf{b}}_{i}}}.$$ \(1\)
> The important message from is that *eigenvectors are not rotated* by $\mathbf{C}$. This feature uniquely distinguishes eigenvectors. Because we assume the orthogonal eigenvectors to be of unit length, ${{\mathbf{b}}_{i}^{\mathsf{T}}{\mathbf{b}}_{j}} = \delta_{ij} = \left\{ \begin{array}{ll}
> \end{array} \right.$, and ${{\mathbf{B}}^{\mathsf{T}}{\mathbf{B}}} = \mathbf{I}$ (obviously this means ${\mathbf{B}}^{- 1} = {\mathbf{B}}^{\mathsf{T}}$, and it follows ${{\mathbf{B}}{\mathbf{B}}}^{\mathsf{T}} = \mathbf{I}$). An basis of eigenvectors is practical, because for any ${\mathbf{v}} \in {\mathbb{R}}^{n}$ we can find coefficients $\alpha_{i}$, such that ${\mathbf{v}} = \left. \sum{}_{i}{\alpha_{i}{\mathbf{b}}_{i}} \right.$, and then we have ${{\mathbf{C}}{\mathbf{v}}} = \left. \sum{}_{i}{d_{i}^{2}\alpha_{i}{\mathbf{b}}_{i}} \right.$.

The eigendecomposition of $\mathbf{C}$ obeys

: $\mathbf{B}$ is an orthogonal matrix, ${{\mathbf{B}}^{\mathsf{T}}{\mathbf{B}}} = {{\mathbf{B}}{\mathbf{B}}}^{\mathsf{T}} = \mathbf{I}$. Columns of $\mathbf{B}$ form an orthonormal basis of eigenvectors.

: ${\mathbf{D}}^{2} = {{\mathbf{D}}{\mathbf{D}}} = {{diag}{(d_{1},\ldots,d_{n})}^{2}} = {{diag}{(d_{1}^{2},\ldots,d_{n}^{2})}}$ is a diagonal matrix with eigenvalues of $\mathbf{C}$ as diagonal elements.

: ${\mathbf{D}} = {{diag}{(d_{1},\ldots,d_{n})}}$ is a diagonal matrix with square roots of eigenvalues of $\mathbf{C}$ as diagonal elements.

The matrix decomposition is unique, apart from signs of columns of $\mathbf{B}$ and permutations of columns in $\mathbf{B}$ and ${\mathbf{D}}^{2}$ respectively, given all eigenvalues are different.^33^3Given $m$ eigenvalues are equal, any orthonormal basis of their $m$-dimensional subspace can be used as column vectors. For $m > 1$ there are infinitely many such bases.

Given the eigendecomposition, the inverse ${\mathbf{C}}^{- 1}$ can be computed via

From we naturally define the square root of $\mathbf{C}$ as

### The Multivariate Normal Distribution

A multivariate normal distribution, $\mathcal{N}({\mathbf{m}},{\mathbf{C}})$, has a unimodal, "bell-shaped" density, where the top of the bell (the modal value) corresponds to the distribution mean, $\mathbf{m}$. The distribution $\mathcal{N}({\mathbf{m}},{\mathbf{C}})$ is uniquely determined by its mean ${\mathbf{m}} \in {\mathbb{R}}^{n}$ and its symmetric and positive definite covariance matrix ${\mathbf{C}} \in {\mathbb{R}}^{n \times n}$. Covariance (positive definite) matrices have an appealing geometrical interpretation: they can be uniquely identified with the (hyper-)ellipsoid $\left. \{{{\mathbf{x}} \in {\mathbb{R}}^{n}} \middle| {{{\mathbf{x}}^{\mathsf{T}}{\mathbf{C}}^{- 1}{\mathbf{x}}} = 1}\} \right.$, as shown in Fig. 1.

Figure 1: Ellipsoids depicting one-σ lines of equal density of six different normal distributions, where σ ∈ ℝ &gt; 0, D is a diagonal matrix, and C is a positive definite full covariance matrix. Thin lines depict possible objective function contour lines

The ellipsoid is a surface of equal density of the distribution. The principal axes of the ellipsoid correspond to the eigenvectors of $\mathbf{C}$, the squared axes lengths correspond to the eigenvalues. The eigendecomposition is denoted by ${\mathbf{C}} = {{\mathbf{B}}({\mathbf{D}})^{2}{\mathbf{B}}^{\mathsf{T}}}$ (see Sect. 0.1). If ${\mathbf{D}} = {\sigma\mathbf{I}}$, where $\sigma \in {\mathbb{R}}_{> 0}$ and $\mathbf{I}$ denotes the identity matrix, ${\mathbf{C}} = {\sigma^{2}\mathbf{I}}$ and the ellipsoid is isotropic (Fig. 1, left). If ${\mathbf{B}} = \mathbf{I}$, then ${\mathbf{C}} = {\mathbf{D}}^{2}$ is a diagonal matrix and the ellipsoid is axis parallel oriented (middle). In the coordinate system given by the columns of $\mathbf{B}$, the distribution $\mathcal{N}(\mathbf{0},{\mathbf{C}})$ is always uncorrelated.

The normal distribution $\mathcal{N}({\mathbf{m}},{\mathbf{C}})$ can be written in different ways.

where "$\sim$" denotes equality in distribution, and ${\mathbf{C}}^{\frac{1}{2}} = {{\mathbf{B}}{\mathbf{D}}{\mathbf{B}}}^{\mathsf{T}}$. The last row can be well interpreted, from right to left

$\mathcal{N}(\mathbf{0},\mathbf{I})$

: produces an spherical (isotropic) distribution as in Fig. 1, left.

: scales the spherical distribution within the coordinate axes as in Fig. 1, middle. ${{\mathbf{D}}\mathcal{N}(\mathbf{0},\mathbf{I})} \sim {\mathcal{N}\left( \mathbf{0},{\mathbf{D}}^{2} \right)}$ has $n$ independent components. The matrix $\mathbf{D}$ can be interpreted as (individual) step-size matrix and its diagonal entries are the standard deviations of the components.

: defines a new orientation for the ellipsoid, where the new principal axes of the ellipsoid correspond to the columns of $\mathbf{B}$. Note that $\mathbf{B}$ has $\frac{n^{2} - n}{2}$ degrees of freedom.

Equation is useful to compute $\mathcal{N}({\mathbf{m}},{\mathbf{C}})$ distributed vectors, because $\mathcal{N}(\mathbf{0},\mathbf{I})$ is a vector of independent $$-normally distributed numbers that can easily be realized on a computer.

### Randomized Black Box Optimization

We consider the black box search scenario, where we want to *minimize an objective function* (or *cost* function or *fitness* function)

The objective is to find one or more search points (candidate solutions), ${\mathbf{x}} \in {\mathbb{R}}^{n}$, with a function value, $f{({\mathbf{x}})}$, as small as possible. We do not state the objective of searching for a global optimum, as this is often neither feasible nor relevant in practice. *Black box* optimization refers to the situation, where function values of evaluated search points are the only accessible information on $f$.^44^4Knowledge about the underlying optimization problem might well enter the composition of $f$ and the chosen problem *encoding*. The search points to be evaluated can be freely chosen. We define the search costs as the number of executed function evaluations, in other words the amount of information we needed to acquire from $f$^55^5Also $f$ is sometimes denoted as *cost function*, but it should not to be confused with the *search costs*.. Any performance measure must consider the search costs *together* with the achieved objective function value.^66^6A performance measure can be obtained from a number of trials as, for example, the mean number of function evaluations to reach a given function value, or the median best function value obtained after a given number of function evaluations.

A randomized black box search algorithm is outlined in Fig. 2.

Figure 2: Randomized black box search. f: ℝn → ℝ is the objective function

In the CMA Evolution Strategy the search distribution, $P$, is a multivariate normal distribution. Given all variances and covariances, the normal distribution has the largest entropy of all distributions in ${\mathbb{R}}^{n}$. Furthermore, coordinate directions are not distinguished in any way. Both makes the normal distribution a particularly attractive candidate for randomized search.

Randomized search algorithms are regarded to be robust in a rugged search landscape, which can comprise discontinuities, (sharp) ridges, or local optima. The covariance matrix adaptation (CMA) in particular is designed to tackle, additionally, ill-conditioned and non-separable^77^7An $n$-dimensional *separable* problem can be solved by solving $n$ $1$-dimensional problems separately, which is a far easier task. problems.

### Hessian and Covariance Matrices

We consider the convex-quadratic objective function $f_{\mathbf{H}}:{{\mathbf{x}}\mapsto{\frac{1}{2}{\mathbf{x}}^{\mathsf{T}}{{\mathbf{H}}{\mathbf{x}}}}}$, where the Hessian matrix ${\mathbf{H}} \in {\mathbb{R}}^{n \times n}$ is a positive definite matrix. Given a search distribution $\mathcal{N}({\mathbf{m}},{\mathbf{C}})$, there is a close relation between $\mathbf{H}$ and $\mathbf{C}$: Setting ${\mathbf{C}} = {\mathbf{H}}^{- 1}$ on $f_{\mathbf{H}}$ is equivalent to optimizing the isotropic function ${f_{sphere}{({\mathbf{x}})}} = {\frac{1}{2}{\mathbf{x}}^{\mathsf{T}}{\mathbf{x}}} = {\frac{1}{2}{\sum_{i}x_{i}^{2}}}$ (where ${\mathbf{H}} = \mathbf{I}$) with ${\mathbf{C}} = \mathbf{I}$.^88^8Also the initial mean value $\mathbf{m}$ has to be transformed accordingly. That is, on convex-quadratic objective functions, setting the covariance matrix of the search distribution to the inverse Hessian matrix is equivalent to rescaling the ellipsoid function into a spherical one. Consequently, we assume that the optimal covariance matrix equals to the inverse Hessian matrix, up to a constant factor.^99^9Even though there is good intuition and strong empirical evidence for this statement, a rigorous proof is missing. Furthermore, choosing a covariance matrix or choosing a respective affine linear transformation of the search space (i.e. of $\mathbf{x}$) is equivalent, because for any full rank $n \times n$-matrix $\mathbf{A}$ we find a positive definite Hessian such that ${\frac{1}{2}{({{\mathbf{A}}{\mathbf{x}}})}^{\mathsf{T}}{{\mathbf{A}}{\mathbf{x}}}} = {\frac{1}{2}{\mathbf{x}}^{\mathsf{T}}{\mathbf{A}}^{\mathsf{T}}{{\mathbf{A}}{\mathbf{x}}}} = {\frac{1}{2}{\mathbf{x}}^{\mathsf{T}}{{\mathbf{H}}{\mathbf{x}}}}$.

The final objective of covariance matrix adaptation is to closely *approximate the contour lines of the objective function $f$*. On convex-quadratic functions this amounts to approximating the inverse Hessian matrix, similar to a quasi-Newton method.

In Fig. 1 the solid-line distribution in the right figure follows the objective function contours most suitably, and it is easy to foresee that it will aid to approach the optimum the most.

The condition number of a positive definite matrix $\mathbf{A}$ is defined via the Euclidean norm: ${{\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{d}}{({\mathbf{A}})}}\overset{def}{=}{{\|{\mathbf{A}}\|} \times {\|{\mathbf{A}}^{- 1}\|}}$, where ${\|{\mathbf{A}}\|} = {\sup_{{\|{\mathbf{x}}\|} = 1}{\|{{\mathbf{A}}{\mathbf{x}}}\|}}$. For a positive definite (Hessian or covariance) matrix $\mathbf{A}$ holds ${\|{\mathbf{A}}\|} = \lambda_{\max}$ and ${{\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{d}}{({\mathbf{A}})}} = \frac{\lambda_{\max}}{\lambda_{\min}} \geq 1$, where $\lambda_{\max}$ and $\lambda_{\min}$ are the largest and smallest eigenvalue of $\mathbf{A}$.

## Basic Equation: Sampling

In the CMA Evolution Strategy, a population of new search points (individuals, offspring) is generated by sampling a multivariate normal distribution.^1010^10Recall that, given all (co-)variances, the normal distribution has the largest entropy of all distributions in ${\mathbb{R}}^{n}$. The basic equation for sampling the search points, for generation number $g = {0,1,2,\ldots}$, reads^1111^11Framed equations belong to the final algorithm of a CMA Evolution Strategy.

: $\sim$ denotes the same distribution on the left and right side.

: $\mathcal{N}{(\mathbf{0},{\mathbf{C}}^{(g)})}$ is a multivariate normal distribution with zero mean and covariance matrix ${\mathbf{C}}^{(g)}$, see Sect. 0.2. It holds ${{\mathbf{m}}^{(g)} + {\sigma^{(g)}\mathcal{N}{(\mathbf{0},{\mathbf{C}}^{(g)})}}} \sim {\mathcal{N}\left( {\mathbf{m}}^{(g)},{{(\sigma^{(g)})}^{2}{\mathbf{C}}^{(g)}} \right)}$.

: ${\mathbf{x}}_{k}^{({g + 1})} \in {\mathbb{R}}^{n}$, $k$-th offspring (individual, search point) from generation $g + 1$.

: ${\mathbf{m}}^{(g)} \in {\mathbb{R}}^{n}$, mean value of the search distribution at generation $g$.

: $\sigma^{(g)} \in {\mathbb{R}}_{> 0}$, "overall" standard deviation, step-size, at generation $g$.

: ${\mathbf{C}}^{(g)} \in {\mathbb{R}}^{n \times n}$, covariance matrix at generation $g$. Up to the scalar factor ${}_{}^{(g)}$, ${\mathbf{C}}^{(g)}$ is the covariance matrix of the search distribution.

: $\lambda \geq 2$, population size, sample size, number of offspring.

To define the complete iteration step, the remaining question is, how to calculate ${\mathbf{m}}^{({g + 1})}$, ${\mathbf{C}}^{({g + 1})}$, and $\sigma^{({g + 1})}$ for the next generation $g + 1$. The next three sections will answer these questions, respectively. An algorithm summary with all parameter settings and matlab source code are given in Appendix A-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial") and C, respectively.

## Selection and Recombination: Moving the Mean

The new mean ${\mathbf{m}}^{({g + 1})}$ of the search distribution is a *weighted average of $\mu$ selected points* from the sample ${\mathbf{x}}_{1}^{({g + 1})},\ldots,{\mathbf{x}}_{\lambda}^{({g + 1})}$:

: $\mu \leq \lambda$ is the parent population size, i.e. the number of selected points.

: $w_{i = {1\ldots\mu}} \in {\mathbb{R}}_{> 0}$, positive weight coefficients for recombination. For $w_{i = {1\ldots\mu}} = {1/\mu}$, Equation calculates the mean value of $\mu$ selected points.

: ${\mathbf{x}}_{i:\lambda}^{({g + 1})}$, $i$-th best individual out of ${\mathbf{x}}_{1}^{({g + 1})},\ldots,{\mathbf{x}}_{\lambda}^{({g + 1})}$ from. The index $i:\lambda$ denotes the index of the $i$-th ranked individual and ${f{({\mathbf{x}}_{1:\lambda}^{({g + 1})})}} \leq {f{({\mathbf{x}}_{2:\lambda}^{({g + 1})})}} \leq \cdots \leq {f{({\mathbf{x}}_{\lambda:\lambda}^{({g + 1})})}}$, where $f$ is the objective function to be minimized.

Equation implements *truncation selection* by choosing $\mu < \lambda$ out of $\lambda$ offspring points. Assigning *different* weights $w_{i}$ should also be interpreted as a selection mechanism. Equation implements *weighted intermediate recombination* by taking $\mu > 1$ individuals into account for a weighted average.

The measure^1212^12Later, the vector $\mathbf{w}$ will have $\lambda \geq \mu$ elements. Here, for computing the norm, we assume that any additional $\lambda - \mu$ elements are zero.

will be repeatedly used in the following and can be paraphrased as *effective sample size* of the selected samples or *variance effective selection mass*. From the definition of $w_{i}$ in we derive $1 \leq \mu_{eff} \leq \mu$, and $\mu_{eff} = \mu$ for equal recombination weights, i.e. $w_{i} = {1/\mu}$ for all $i = {1\ldots\mu}$.

> The notion of $\mu_{eff}$ with different recombination weights generalizes the notion of $\mu$ with equal recombination weights in several aspects. The number $\mu$ (with equal recombination weights) is the amount of information used, expressed as number of independent sources. Taking the weighted average of *independent* samples reduces the original variance by a factor of $\mu$ for equal weights and by a factor of $\mu_{eff}$ for any weights, hence $\mu_{eff}$ can be considered as the amount of used information. To keep the variance unchanged, the average must be multiplied by $\sqrt{\mu_{eff}}$. However, the optimal step-size (given $\mu < n$) is proportional to $\mu$ for equal weights and proportional to $1.25\mu_{eff}$ for optimal recombination weights, respectively, see also Section 4.

Usually, $\mu_{eff} \approx {\lambda/4}$ indicates a reasonable setting of $w_{i}$. A simple and reasonable setting is $w_{i} \propto {{\mu - i} + 1}$, and $\mu \approx {\lambda/2}$, where $\mu_{eff} \approx {{3\lambda}/8}$.

The final equation rewrites as an *update* of $\mathbf{m}$,

: $c_{m}$ is a learning rate, usually set to $1$.^1313^13In the literature the notation $\kappa = {1/c_{m}}$ is also common and $\kappa$ is used as multiplier in instead of in.

Equation generalizes. If ${c_{m}{\sum_{i = 1}^{\mu}w_{i}}} = 1$, as it is the case with the default parameter setting (compare Table 1-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial") in Appendix A-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")), $- {\mathbf{m}}^{(g)}$ cancels out ${\mathbf{m}}^{(g)}$, and Equations and are identical.

> Choosing $c_{m} < 1$ can be advantageous on noisy functions. With optimal step-size we have roughly $\sigma \propto \left. 1/c_{m} \right.$, hence the "test steps" in are in effect increased whereas the update step in remains unchanged. However, too large test steps negatively impact the performance because the ranking indices $i:\lambda$ are determined too far away from the (current) region of relevance. Arbitrary small test steps (when $c_{m}\rightarrow\infty$) work generally well, within the limits of numerical precision, on unimodal and noisefree functions.

## Adapting the Covariance Matrix

In this section, the update of the covariance matrix, $\mathbf{C}$, is derived. We will start out estimating the covariance matrix from a single population of one generation (Sect. 3.1). For small populations this estimation is unreliable and an adaptation procedure has to be invented (rank-$\mu$-update, Sect. 3.2). In the limit case only a single point can be used to update (adapt) the covariance matrix at each generation (rank-one-update, Sect. 3.3). This adaptation can be enhanced by exploiting dependencies between successive steps applying cumulation (Sect. 3.3.2). Finally we combine the rank-$\mu$ and rank-one updating methods (Sect. 3.4).

### Estimating the Covariance Matrix From Scratch

For the moment we assume that the population contains enough information to reliably estimate a covariance matrix from the population.^1414^14To re-estimate the covariance matrix, $\mathbf{C}$, from a $\mathcal{N}(\mathbf{0},\mathbf{I})$ distributed sample such that ${{\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{d}}{({\mathbf{C}})}} < 10$ a sample size $\lambda \geq {4n}$ is needed, as can be observed in numerical experiments. For the sake of convenience we assume $\sigma^{(g)} = 1$ (see ) in this section. For $\sigma^{(g)} \neq 1$ the formulae hold except for a constant factor.

We can (re-)estimate the original covariance matrix ${\mathbf{C}}^{(g)}$ using the sampled population from, ${\mathbf{x}}_{1}^{({g + 1})}\ldots{\mathbf{x}}_{\lambda}^{({g + 1})}$, via the empirical covariance matrix

The empirical covariance matrix ${\mathbf{C}}_{emp}^{({g + 1})}$ is an unbiased estimator of ${\mathbf{C}}^{(g)}$: assuming the ${{\mathbf{x}}_{i}^{({g + 1})},i} = {1\ldots\lambda}$, to be random variables (rather than a realized sample), we have that ${\mathsf{E}\left\lbrack {\mathbf{C}}_{emp}^{({g + 1})} \middle| {\mathbf{C}}^{(g)} \right\rbrack} = {\mathbf{C}}^{(g)}$. Consider now a slightly different approach to get an estimator for ${\mathbf{C}}^{(g)}$.

Also the matrix ${\mathbf{C}}_{\lambda}^{({g + 1})}$ is an unbiased estimator of ${\mathbf{C}}^{(g)}$. The remarkable difference between and is the reference mean value. For ${\mathbf{C}}_{emp}^{({g + 1})}$ it is the mean of the *actually realized* sample. For ${\mathbf{C}}_{\lambda}^{({g + 1})}$ it is the *true* mean value, ${\mathbf{m}}^{(g)}$, of the sampled distribution (see ). Therefore, the estimators ${\mathbf{C}}_{emp}^{({g + 1})}$ and ${\mathbf{C}}_{\lambda}^{({g + 1})}$ can be interpreted differently: while ${\mathbf{C}}_{emp}^{({g + 1})}$ estimates the distribution variance *within the sampled points*, ${\mathbf{C}}_{\lambda}^{({g + 1})}$ estimates variances of sampled *steps*, ${\mathbf{x}}_{i}^{({g + 1})} - {\mathbf{m}}^{(g)}$.

> A minor difference between and is the different normalizations $\frac{1}{\lambda - 1}$ versus $\frac{1}{\lambda}$, necessary to get an unbiased estimator in both cases. In one degree of freedom is already taken by the inner summand. In order to get a *maximum likelihood* estimator, in both cases $\frac{1}{\lambda}$ must be used.

Equation re-estimates *the original* covariance matrix. To "estimate" a "better" covariance matrix, the same, *weighted selection* mechanism as in is used.

The matrix ${\mathbf{C}}_{\mu}^{({g + 1})}$is an estimator for the distribution of *selected steps*, just as ${\mathbf{C}}_{\lambda}^{({g + 1})}$ is an estimator of the original distribution of steps before selection. Sampling from ${\mathbf{C}}_{\mu}^{({g + 1})}$ tends to reproduce selected, i.e. *successful* steps, giving a justification for what a "better" covariance matrix means.

> Following, we compare with the Estimation of Multivariate Normal Algorithm EMNA~global~. The covariance matrix in EMNA~global~ reads, similar to,
> $${{\mathbf{C}}_{{EMNA}_{global}}^{({g + 1})} = {\frac{1}{\mu}{\sum\limits_{i = 1}^{\mu}{\left( {{\mathbf{x}}_{i:\lambda}^{({g + 1})} - {\mathbf{m}}^{({g + 1})}} \right)\left( {{\mathbf{x}}_{i:\lambda}^{({g + 1})} - {\mathbf{m}}^{({g + 1})}} \right)^{\mathsf{T}}}}}},$$ \(13\)
> where ${\mathbf{m}}^{({g + 1})} = {\frac{1}{\mu}{\sum_{i = 1}^{\mu}{\mathbf{x}}_{i:\lambda}^{({g + 1})}}}$. Similarly, applying the so-called Cross-Entropy method to continuous domain optimization yields the covariance matrix $\frac{\mu}{\mu - 1}{\mathbf{C}}_{{EMNA}_{global}}^{({g + 1})}$, i.e. the *unbiased* empirical covariance matrix of the $\mu$ best points. In both cases the subtle, but most important difference to is, again, the choice of the reference mean value.^1515^15Taking a weighted sum, $\sum_{i = 1}^{\mu}{w_{i}\ldots}$, instead of the mean, $\frac{1}{\mu}{\sum_{i = 1}^{\mu}\ldots}$, is an appealing, but less important, difference. Equation estimates the variance *within* the selected population while estimates selected steps. Equation reveals always smaller variances than, because its reference mean value is the minimizer for the variances. Moreover, in most conceivable selection situations decreases the variances compared to ${\mathbf{C}}^{(g)}$.
> Figure 3: Estimation of the covariance matrix on ${f_{linear}{({\mathbf{x}})}} = {- {\sum_{i = 1}^{2}x_{i}}}$ to be minimized. Contour lines (dotted) indicate that the strategy should move toward the upper right corner. Above: estimation of Cμ(g+1) according to, where wi = 1/μ. Below: estimation of CEMNAg l o b a l(g+1) according to. Left: sample of λ = 150 𝒩 (0,I) distributed points. Middle: the μ = 50 selected points (dots) determining the entries for the estimation equation (solid straight lines). Right: search distribution of the next generation (solid ellipsoids). Given wi = 1/μ, estimation via Cμ(g+1) increases the expected variance in gradient direction for all μ &lt; λ/2, while estimation via CEMNAg l o b a l(g+1) decreases this variance for any μ &lt; λ geometrically fast
> Figure 3 demonstrates the estimation results on *a linear* objective function for $\lambda = 150$, $\mu = 50$, and $w_{i} = \left. 1/\mu \right.$. Equation geometrically increases the expected variance in direction of the gradient (where the selection takes place, here the diagonal), given ordinary settings for parent number $\mu$ and recombination weights $w_{1},\ldots,w_{\mu}$. Equation always decreases the variance in gradient direction geometrically fast! Therefore, is highly susceptible to premature convergence, in particular with small parent populations, where the population cannot be expected to bracket the optimum at any time. However, for large values of $\mu$ in large populations with large initial variances, the impact of the different reference mean value can become marginal.

In order to ensure with and, that ${\mathbf{C}}_{\mu}^{({g + 1})}$ is a *reliable* estimator, the variance effective selection mass $\mu_{eff}$ (cf. ) must be large enough: getting condition numbers (cf. Sect. 0.4) smaller than ten for ${\mathbf{C}}_{\mu}^{(g)}$ on ${f_{sphere}{({\mathbf{x}})}} = {\sum_{i = 1}^{n}x_{i}^{2}}$, requires $\mu_{eff} \approx {10n}$. The next step is to circumvent this restriction on $\mu_{eff}$.

### Rank-$\mu$-Update

To achieve *fast* search (opposite to *more robust* or *more global* search), e.g. competitive performance on $f_{sphere}:{{\mathbf{x}}\mapsto{\sum x_{i}^{2}}}$, the population size $\lambda$ must be small. Because typically (and ideally) $\mu_{eff} \approx {\lambda/4}$ also $\mu_{eff}$ must be small and we may assume, e.g., $\mu_{eff} \leq {1 + {\ln n}}$. Then, it is not possible to get a *reliable* estimator for a good covariance matrix from. As a remedy, information from previous generations is used additionally. For example, after a sufficient number of generations, the mean of the estimated covariance matrices from all generations,

becomes a reliable estimator for the selected steps. To make ${\mathbf{C}}_{\mu}^{(g)}$ from different generations comparable, the different $\sigma^{(i)}$ are incorporated. (Assuming $\sigma^{(i)} = 1$, resembles the covariance matrix from the Estimation of Multivariate Normal Algorithm EMNA~i~.)

In, all generation steps have the same weight. To assign recent generations a higher weight, exponential smoothing is introduced. Choosing ${\mathbf{C}}^{} = \mathbf{I}$ to be the unity matrix and a learning rate $0 < c_{\mu} \leq 1$, then ${\mathbf{C}}^{({g + 1})}$ reads

: $c_{\mu} \leq 1$ learning rate for updating the covariance matrix. For $c_{\mu} = 1$, no prior information is retained and ${\mathbf{C}}^{({g + 1})} = {\frac{1}{{}_{}^{(g)}}{\mathbf{C}}_{\mu}^{({g + 1})}}$. For $c_{\mu} = 0$, no learning takes place and ${\mathbf{C}}^{({g + 1})} = {\mathbf{C}}^{}$. Here, $c_{\mu} \approx {\min{(1,{\mu_{eff}/n^{2}})}}$ is a reasonably choice.

: $w_{1\ldots\mu} \in {\mathbb{R}}$ such that $w_{1} \geq \cdots \geq w_{\mu} > 0$ and ${\sum_{i}w_{i}} = 1$.

: ${\mathbf{y}}_{i:\lambda}^{({g + 1})} = {{({{\mathbf{x}}_{i:\lambda}^{({g + 1})} - {\mathbf{m}}^{(g)}})}/\sigma^{(g)}}$.

: ${\mathbf{z}}_{i:\lambda}^{({g + 1})} = {{}_{}^{(g)}{\mathbf{y}}_{i:\lambda}^{({g + 1})}}$ is the mutation vector expressed in the unique coordinate system where the sampling is isotropic and the respective coordinate system transformation does not rotate the original principal axes of the distribution.

This covariance matrix update is called rank-$\mu$-update, because the sum of outer products in is of rank $\min{(\mu,n)}$ with probability one (given $\mu$ non-zero weights). This sum can even consist of a single term, if $\mu = 1$.

Finally, we generalize to $\lambda$ weight values which need neither sum to $1$, nor be non-negative anymore,

: $w_{1\ldots\lambda} \in {\mathbb{R}}$ such that $w_{1} \geq \cdots \geq w_{\mu} > 0 \geq w_{\mu + 1} \geq w_{\lambda}$, and usually ${\sum_{i = 1}^{\mu}w_{i}} = 1$ and ${\sum_{i = 1}^{\lambda}w_{i}} \approx 0$.

: ${\sum w_{i}} = {\sum_{i = 1}^{\lambda}w_{i}}$

The second line of (3.2) expresses the update in the natural coordinate system, an idea already considered in. The identity covariance matrix is updated and a coordinate system transformation is applied afterwards by multiplication with ${}_{}^{(g)}$ on both sides. Equation (3.2) uses $\lambda$ weights, $w_{i}$, of which about half are negative. If the weights are chosen such that ${\sum w_{i}} = 0$, the decay on ${\mathbf{C}}^{(g)}$ disappears and changes are only made along axes in which samples are realized.

> Negative values for the recombination weights in the covariance matrix update have been introduced in the seminal paper of Jastrebski and Arnold as *active* covariance matrix adaptation. Non-equal negative weight values have been used in together with a rather involved mechanism to make up for different vector lengths. The default recombination weights as defined in Table 1-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial") in Appendix A-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial") are somewhere in between these two proposals, but closer to. Slightly deviating from (3.2) later on, vector lengths associated with negative weights will be rescaled to a (direction dependent) constant, see (46-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")) and (47-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")) in Appendix A-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial"). This allows to *guaranty* positive definiteness of ${\mathbf{C}}^{({g + 1})}$. Conveniently, it also alleviates a selection error which usually makes directions associated with longer vectors worse.

The number $1/c_{\mu}$ is the backward time horizon that contributes roughly $63\%$ of the overall information.

> Because (3.2) expands to the weighted sum
> the backward time horizon, $\Deltag$, where about $63\%$ of the overall weight is summed up, is defined by
> $${{c_{\mu}{\sum\limits_{i = {{g + 1} - {\Deltag}}}^{g}\left( {1 - c_{\mu}} \right)^{g - i}}} \approx 0.63 \approx {1 - \frac{1}{e}}}.$$ \(18\)
> Resolving the sum yields
> $${\left( {1 - c_{\mu}} \right)^{\Deltag} \approx \frac{1}{e}},$$ \(19\)
> and resolving for $\Deltag$, using the Taylor approximation for $\ln$, yields
> $${{\Deltag} \approx \frac{1}{c_{\mu}}}.$$ \(20\)
> That is, approximately $37\%$ of the information in ${\mathbf{C}}^{({g + 1})}$ is older than $\left. 1/c_{\mu} \right.$ generations, and, according to, the original weight is reduced by a factor of $0.37$ after approximately $\left. 1/c_{\mu} \right.$ generations.^1616^16This can be shown more easily, because ${(1 - c_{\mu})}^{g} = \exp\ln{(1 - c_{\mu})}^{g} = \exp{(g\ln{(1 - c_{\mu})})} \approx \exp{( - gc_{\mu})}$ for small $c_{\mu}$, and for $g \approx {1/c_{\mu}}$ we get immediately ${({1 - c_{\mu}})}^{g} \approx {\exp{({- 1})}}$.

The choice of $c_{\mu}$ is crucial. Small values lead to slow learning, too large values lead to a failure, because the covariance matrix degenerates. Fortunately, a good setting seems to be largely independent of the function to be optimized.^1717^17We use the sphere model ${f_{sphere}{({\mathbf{x}})}} = {\sum_{i}x_{i}^{2}}$ to empirically find a good setting for the parameter $c_{\mu}$, dependent on $n$ and $\mu_{eff}$. The found setting was applicable to any non-noisy objective function we tried so far. A first order approximation for a good choice is $c_{\mu} \approx {\mu_{eff}/n^{2}}$. Therefore, the characteristic time horizon for (3.2) is roughly $n^{2}/\mu_{eff}$.

Experiments suggest that $c_{\mu} \approx {\mu_{eff}/n^{2}}$ is a rather conservative setting for large values of $n$, whereas $\mu_{eff}/n^{1.5}$ appears to be slightly beyond the limit of stability. The best, yet robust choice of the exponent remains to be an open question.

Even for the learning rate $c_{\mu} = 1$, adapting the covariance matrix cannot be accomplished within one generation. The effect of the original sample distribution does not vanish until a sufficient number of generations. Assuming fixed search costs (number of function evaluations), a small population size $\lambda$ allows a larger number of generations and therefore usually leads to a faster adaptation of the covariance matrix.

### Rank-One-Update

In Section 3.1 we started by estimating the complete covariance matrix from scratch, using all selected steps from a *single generation*. We now take an opposite viewpoint. We repeatedly update the covariance matrix in the generation sequence using a *single selected step* only. First, this perspective will give another justification of the adaptation rule (3.2). Second, we will introduce the so-called evolution path that is finally used for a rank-one update of the covariance matrix.

### Different Viewpoint

We consider a specific method to produce $n$-dimensional normal distributions with zero mean. Let the vectors ${{\mathbf{y}}_{1},\ldots,{\mathbf{y}}_{g_{0}}} \in {\mathbb{R}}^{n}$, $g_{0} \geq n$, span ${\mathbb{R}}^{n}$ and let $\mathcal{N}$ denote independent $$-normally distributed random numbers, then

is a normally distributed random vector with zero mean and covariance matrix $\sum_{i = 1}^{g_{0}}{{\mathbf{y}}_{i}{\mathbf{y}}_{i}^{\mathsf{T}}}$. The random vector is generated by adding "line-distributions" $\mathcal{N}{\mathbf{y}}_{i}$. The singular distribution ${\mathcal{N}{\mathbf{y}}_{i}} \sim {\mathcal{N}{(\mathbf{0},{{\mathbf{y}}_{i}{\mathbf{y}}_{i}^{\mathsf{T}}})}}$ generates the vector ${\mathbf{y}}_{i}$ with maximum likelihood considering all normal distributions with zero mean.

> The line distribution that generates a vector $\mathbf{y}$ with the maximum likelihood must "live" on a line that includes $\mathbf{y}$, and therefore the distribution must obey ${\mathcal{N}\sigma{\mathbf{y}}} \sim {\mathcal{N}\left( 0,{\sigma^{2}{{\mathbf{y}}{\mathbf{y}}}^{\mathsf{T}}} \right)}$. Any other line distribution with zero mean cannot generate $\mathbf{y}$ at all. Choosing $\sigma$ reduces to choosing the maximum likelihood of $\left\| {\mathbf{y}} \right\|$ for the one-dimensional gaussian $\mathcal{N}\left( 0,{\sigma^{2}\left\| {\mathbf{y}} \right\|^{2}} \right)$, which is $\sigma = 1$.
> The covariance matrix ${{\mathbf{y}}{\mathbf{y}}}^{\mathsf{T}}$ has rank one, its only eigenvectors are $\left\{ {\alpha{\mathbf{y}}} \middle| {\alpha \in {\mathbb{R}}_{\smallsetminus 0}} \right\}$ with eigenvalue $\left\| {\mathbf{y}} \right\|^{2}$. Using equation, any normal distribution can be realized if ${\mathbf{y}}_{i}$ are chosen appropriately. For example, resembles with ${\mathbf{m}} = \mathbf{0}$, using the orthogonal eigenvectors ${\mathbf{y}}_{i} = {d_{ii}{\mathbf{b}}_{i}}$, for $i = {1,\ldots,n}$, where ${\mathbf{b}}_{i}$ are the columns of $\mathbf{B}$. In general, the vectors ${\mathbf{y}}_{i}$ need not to be eigenvectors of the covariance matrix, and they usually are not.

Considering and a slight simplification of (3.2), we try to gain insight into the adaptation rule for the covariance matrix. Let the sum in (3.2) consist of a single summand only (e.g. $\mu = 1$), and let ${\mathbf{y}}_{g + 1} = \frac{{\mathbf{x}}_{1:\lambda}^{({g + 1})} - {\mathbf{m}}^{(g)}}{\sigma^{(g)}}$. Then, the rank-one update for the covariance matrix reads

The right summand is of rank one and adds the maximum likelihood term for ${\mathbf{y}}_{g + 1}$ into the covariance matrix ${\mathbf{C}}^{(g)}$. Therefore the probability to generate ${\mathbf{y}}_{g + 1}$ in the next generation increases.

An example of the first two iteration steps of is shown in Figure 4.

Figure 4: Change of the distribution according to the covariance matrix update. Left: vectors e1 and e2, and C = I = e1 e1T + e2 e2T. Middle: vectors 0.91 e1, 0.91 e2, and 0.41 y1 (the coefficients deduce from c1 = 0.17), and C = (1−c1) I + c1 y1 y1T, where ${\mathbf{y}}_{1} = \binom{- 0.59}{- 2.2}$. The distribution ellipsoid is elongated into the direction of y1, and therefore increases the likelihood of y1. Right: C = (1−c1) C + c1 y2 y2T, where ${\mathbf{y}}_{2} = \binom{0.97}{1.5}$.

The distribution $\mathcal{N}{(\mathbf{0},{\mathbf{C}}^{})}$ tends to reproduce ${\mathbf{y}}_{1}$ with a larger probability than the initial distribution $\mathcal{N}{(\mathbf{0},\mathbf{I})}$; the distribution $\mathcal{N}{(\mathbf{0},{\mathbf{C}}^{})}$ tends to reproduce ${\mathbf{y}}_{2}$ with a larger probability than $\mathcal{N}{(\mathbf{0},{\mathbf{C}}^{})}$, and so forth. When ${\mathbf{y}}_{1},\ldots,{\mathbf{y}}_{g}$ denote the formerly selected, favorable steps, $\mathcal{N}{(\mathbf{0},{\mathbf{C}}^{(g)})}$ tends to reproduce these steps. The process leads to an alignment of the search distribution $\mathcal{N}{(\mathbf{0},{\mathbf{C}}^{(g)})}$ to the distribution of the selected steps. If both distributions become alike, as under random selection, in expectation no further change of the covariance matrix takes place.

### Cumulation: Utilizing the Evolution Path

We have used the selected steps, ${\mathbf{y}}_{i:\lambda}^{({g + 1})} = {{({{\mathbf{x}}_{i:\lambda}^{({g + 1})} - {\mathbf{m}}^{(g)}})}/\sigma^{(g)}}$, to update the covariance matrix in (3.2) and. Because ${{\mathbf{y}}{\mathbf{y}}}^{\mathsf{T}} = {- {{\mathbf{y}}{({- {\mathbf{y}}})}^{\mathsf{T}}}}$, *the sign of the steps is irrelevant* for the update of the covariance matrix --- that is, the sign information is lost when calculating ${\mathbf{C}}^{({g + 1})}$. To reintroduce the sign information, a so-called *evolution path* is constructed.

We call a sequence of successive steps, the strategy takes over a number of generations, an evolution path. An evolution path can be expressed by a sum of consecutive steps. This summation is referred to as *cumulation*. To construct an evolution path, the step-size $\sigma$ is disregarded. For example, an evolution path of three steps of the distribution mean $\mathbf{m}$ can be constructed by the sum

In practice, to construct the evolution path, ${\mathbf{p}}_{c} \in {\mathbb{R}}^{n}$, we use exponential smoothing as in (3.2), and start with ${\mathbf{p}}_{c}^{} = \mathbf{0}$.^1818^18In the final algorithm is still slightly modified, compare (45-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")).

: ${\mathbf{p}}_{c}^{(g)} \in {\mathbb{R}}^{n}$, evolution path at generation $g$.

: $c_{c} \leq 1$. Again, $1/c_{c}$ is the backward time horizon of the evolution path ${\mathbf{p}}_{c}$ that contains roughly $63\%$ of the overall weight (compare derivation of ). A time horizon between $\sqrt{n}$ and $n$ is effective.

The factor $\sqrt{c_{c}{({2 - c_{c}})}\mu_{eff}}$ is a normalization constant for ${\mathbf{p}}_{c}$. For $c_{c} = 1$ and $\mu_{eff} = 1$, the factor reduces to one, and ${\mathbf{p}}_{c}^{({g + 1})} = {{({{\mathbf{x}}_{1:\lambda}^{({g + 1})} - {\mathbf{m}}^{(g)}})}/\sigma^{(g)}}$.

> The factor $\sqrt{c_{c}\left( {2 - c_{c}} \right)\mu_{eff}}$ is chosen, such that
> $${\mathbf{p}}_{c}^{({g + 1})} \sim {\mathcal{N}(\mathbf{0},{\mathbf{C}})}$$ \(25\)
> $${\mathbf{p}}_{c}^{(g)} \sim \frac{{\mathbf{x}}_{i:\lambda}^{({g + 1})} - {\mathbf{m}}^{(g)}}{\sigma^{(g)}} \sim {\mathcal{N}(\mathbf{0},{\mathbf{C}}){\text{for all~}{i = {1,\ldots,\mu}}\text{~.}}}$$ \(26\)
> To derive from and remark that
> $${{\left( {1 - c_{c}} \right)^{2} + {\sqrt{c_{c}\left( {2 - c_{c}} \right)}}^{2}} = {1\text{and}{\sum\limits_{i = 1}^{\mu}{w_{i}\mathcal{N}_{i}(\mathbf{0},{\mathbf{C}})}}} \sim {\frac{1}{\sqrt{\mu_{eff}}}\mathcal{N}(\mathbf{0},{\mathbf{C}})}}.$$ \(27\)

The (rank-one) update of the covariance matrix ${\mathbf{C}}^{(g)}$ via the evolution path ${\mathbf{p}}_{c}^{({g + 1})}$ reads

An empirically validated choice for the learning rate in is $c_{1} \approx {2/n^{2}}$. For $c_{c} = 1$ and $\mu = 1$, Equations and (3.2) are identical.

Using the evolution path for the update of $\mathbf{C}$ is a significant improvement of (3.2) for small $\mu_{eff}$, because correlations between consecutive steps are heavily exploited. The leading signs of steps, and the dependencies between consecutive steps play a significant role for the resulting evolution path ${\mathbf{p}}_{c}^{({g + 1})}$.

> We consider the two most extreme situations, fully correlated steps and entirely anti-correlated steps. The summation in reads for positive correlations ∑\_i=0\^$g$(1-$c_{c}$)\^i →1$c_{c}$ (for $g\rightarrow\infty$), and for negative correlations
> $\sum\limits_{i = 0}^{g}{\left( {- 1} \right)^{i}\left( {1 - c_{c}} \right)^{i}}$ $=$ ${\sum\limits_{i = 0}^{\lfloor{g/2}\rfloor}\left( {1 - c_{c}} \right)^{2i}} - {\sum\limits_{i = 0}^{{({g - 1})}/2}\left( {1 - c_{c}} \right)^{{2i} + 1}}$
> $=$ ${\sum\limits_{i = 0}^{\lfloor{g/2}\rfloor}\left( {1 - c_{c}} \right)^{2i}} - {\left( {1 - c_{c}}) \right.{\sum\limits_{i = 0}^{{({g - 1})}/2}\left( {1 - c_{c}} \right)^{2i}}}$
> $=$ ${c_{c}{\sum\limits_{i = 0}^{\lfloor{g/2}\rfloor}\left( \left( {1 - c_{c}} \right)^{2} \right)^{i}}} + {\left( {1 - c_{c}} \right)^{g}\left( {\left( {g + 1} \right)\operatorname{mod}2} \right)}$
> $\rightarrow$ ${\frac{c_{c}}{1 - \left( {1 - c_{c}} \right)^{2}} = {\frac{1}{2 - c_{c}}{\text{(for~}{g\rightarrow\infty}\text{)}}}}.$
> Multipling these by $\sqrt{c_{c}\left( {2 - c_{c}} \right)}$, which is applied to each input vector, we find that the length of the evolution path is modulated by the factor of up to
> $\sqrt{\frac{2 - c_{c}}{c_{c}}}$ $\approx \frac{1}{\sqrt{c_{c}}}$ \(29\)
> due to the positive correlations, or its inverse due to negative correlations, respectively \[19, Equations and \].

With $\sqrt{n} \leq {1/c_{c}} \leq {n/2}$ the number of function evaluations needed to adapt a nearly optimal covariance matrix on cigar-like objective functions becomes $\mathcal{O}{(n)}$, despite a learning rate of $c_{1} \approx {2/n^{2}}$. A plausible interpretation of this effect is two-fold. First, the desired axis is represented in the path (much) more accurately than in single steps. Second, the learning rate $c_{1}$ is modulated: the increased length of the evolution path as computed in acts in effect similar to an increased learning rate by a factor of up to $c_{c}^{- {1/2}}$.

As a last step, we combine (3.2) and.

### Combining Rank-$\mu$-Update and Cumulation

The final CMA update of the covariance matrix combines (3.2) and.

: $c_{\mu} \approx {\min{({\mu_{eff}/n^{2}},{1 - c_{1}})}}$.

: ${\mathbf{y}}_{i:\lambda}^{({g + 1})} = {{({{\mathbf{x}}_{i:\lambda}^{({g + 1})} - {\mathbf{m}}^{(g)}})}/\sigma^{(g)}}$.

: ${\sum w_{j}} = {\sum_{i = 1}^{\lambda}w_{i}} \approx {- {c_{1}/c_{\mu}}}$, but see also (55-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")) and(46-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial")) in Appendix A-CMA-ES ‣ The CMA Evolution Strategy: A Tutorial").

Equation reduces to (3.2) for $c_{1} = 0$ and to for $c_{\mu} = 0$. The equation combines the advantages of (3.2) and. On the one hand, the information from the entire population is used efficiently by the so-called rank-$\mu$ update. On the other hand, information of correlations *between* generations is exploited by using the evolution path for the rank-one update. The former is important in large populations, the latter is particularly important in small populations.

## Step-Size Control

The covariance matrix adaptation, discussed in the last section, does not explicitly control the "overall scale" of the distribution, the step-size. The covariance matrix adaptation increases or decreases the scale only *in a single direction* for each selected step---or it decreases the scale by fading out old information by a given, non-adaptive factor. Less informally, we have two specific reasons to introduce a step-size control in addition to the adaptation rule for ${\mathbf{C}}^{(g)}$.

The *optimal* overall step length cannot be well approximated by, in particular if $\mu_{eff}$ is chosen larger than one.

> For example, on ${f_{sphere}({\mathbf{x}})} = {\sum_{i = 1}^{n}x_{i}^{2}}$, given ${\mathbf{C}}^{(g)} = \mathbf{I}$ and $\lambda \leq n$, the optimal step-size $\sigma$ equals approximately $\left. {\mu\sqrt{f_{sphere}({\mathbf{x}})}}/n \right.$ with equal recombination weights and $\left. {1.25\mu_{eff}\sqrt{f_{sphere}({\mathbf{x}})}}/n \right.$ with optimal recombination weights.^1919^19Because recombination then reduces the size of the realized step by a factor of $\sqrt{\mu}$ or $\sqrt{\mu_{eff}}$ (under random selection or in large dimension), the effective optimal steps are proportional to $\sqrt{\mu}$ or $1.25\sqrt{\mu_{eff}}$, respectively. This dependency on $\mu$ or $\mu_{eff}$ can not be realized by (3.2) or.

The largest reliable learning rate for the covariance matrix update in is too slow to achieve competitive change rates for the overall step length.

> To achieve optimal performance on $f_{sphere}$ with an Evolution Strategy with weighted recombination, the overall step length must decrease by a factor of about ${\exp(0.25)} \approx 1.28$ within $n$ function evaluations, as can be derived from progress formulas as in and \[6, p. 229\]. That is, the time horizon for the step length change must be proportional to $n$ or shorter. From the learning rates $c_{1}$ and $c_{\mu}$ in follows that the adaptation is too slow to perform competitive on $f_{sphere}$ whenever $\mu_{eff} \ll n$. This can be validated by simulations even for moderate dimensions, $n \geq 10$, and small $\mu_{eff} \leq {1 + {\ln n}}$.

To control the step-size $\sigma^{(g)}$ we utilize an evolution path, i.e. a sum of successive steps (see also Sect. 3.3.2). The method can be applied independently of the covariance matrix update and is denoted as *cumulative path length control*, cumulative step-size control, or cumulative step length adaptation (CSA). The length of an evolution path is exploited, based on the following reasoning, as depicted in Fig. 5.

Figure 5: Three evolution paths of respectively six steps from different selection situations (idealized). The lengths of the single steps are all comparable. The length of the evolution paths (sum of steps) is remarkably different and is exploited for step-size control

Whenever the evolution path is short, single steps cancel each other out (Fig. 5, left). Loosely speaking, they are anti-correlated. If steps extinguish each other, the step-size should be decreased.

Whenever the evolution path is long, the single steps are pointing to similar directions (Fig. 5, right). Loosely speaking, they are correlated. Because the steps are similar, the same distance can be covered by fewer but longer steps into the same directions. In the limit case, when consecutive steps have identical direction, they can be replaced by any of the enlarged single step. Consequently, the step-size should be increased.

In the desired situation the steps are (approximately) perpendicular in expectation and therefore uncorrelated (Fig. 5, middle).

To decide whether the evolution path is "long" or "short", we compare the length of the path with its expected length under random selection^2020^20Random selection means that the index $i:\lambda$ (compare ) is independent of the value of ${\mathbf{x}}_{i:\lambda}^{({g + 1})}$ for all $i = {1,\ldots,\lambda}$, e.g. $i:{\lambda = i}$., where consecutive steps are independent and therefore uncorrelated (uncorrelated steps are the desired situation). If selection biases the evolution path to be longer then expected, $\sigma$ is increased, and, vice versa, if selection biases the evolution path to be shorter than expected, $\sigma$ is decreased. In the ideal situation, selection does not bias the length of the evolution path and the length equals its expected length under random selection.

In practice, to construct the evolution path, ${\mathbf{p}}_{\sigma}$, the same techniques as in are applied. In contrast to, a *conjugate* evolution path is constructed, because the expected length of the evolution path ${\mathbf{p}}_{c}$ from depends on its direction (compare ). Initialized with ${\mathbf{p}}_{\sigma}^{} = \mathbf{0}$, the conjugate evolution path reads

: ${\mathbf{p}}_{\sigma}^{(g)} \in {\mathbb{R}}^{n}$ is the conjugate evolution path at generation $g$.

: $c_{\sigma} < 1$. Again, $1/c_{\sigma}$ is the backward time horizon of the evolution path (compare ). For small $\mu_{eff}$, a time horizon between $\sqrt{n}$ and $n$ is reasonable.

: $\sqrt{c_{\sigma}{({2 - c_{\sigma}})}\mu_{eff}}$ is a normalization constant, see.

: ${}_{}^{(g)}\overset{def}{=}{{\mathbf{B}}^{(g)}{}_{}^{(g)}{}_{}^{(g)}}$, where ${\mathbf{C}}^{(g)} = {{\mathbf{B}}^{(g)}\left( {\mathbf{D}}^{(g)} \right)^{2}{}_{}^{(g)}}$ is an eigendecomposition of ${\mathbf{C}}^{(g)}$, where ${\mathbf{B}}^{(g)}$ is an orthonormal basis of eigenvectors, and the diagonal elements of the diagonal matrix ${\mathbf{D}}^{(g)}$ are square roots of the corresponding positive eigenvalues (cf. Sect. 0.1).

For ${\mathbf{C}}^{(g)} = \mathbf{I}$, we have ${}_{}^{(g)} = \mathbf{I}$ and replicates. The transformation ${}_{}^{(g)}$ re-scales the step ${\mathbf{m}}^{({g + 1})} - {\mathbf{m}}^{(g)}$ within the coordinate system given by ${\mathbf{B}}^{(g)}$.

> The single factors of the transformation ${}_{}^{(g)} = {{\mathbf{B}}^{(g)}{}_{}^{(g)}{}_{}^{(g)}}$ can be explained as follows (from right to left):
>: ${}_{}^{(g)}$ rotates the space such that the columns of ${\mathbf{B}}^{(g)}$, i.e. the principal axes of the distribution $\mathcal{N}\left( \mathbf{0},{\mathbf{C}}^{(g)} \right)$, rotate into the coordinate axes. Elements of the resulting vector relate to projections onto the corresponding eigenvectors.
>: ${}_{}^{(g)}$ applies a (re-)scaling such that all axes become equally sized.
>: ${\mathbf{B}}^{(g)}$ rotates the result back into the original coordinate system. This last transformation ensures that the principal axes of the distribution are not rotated by the overall transformation and directions of consecutive steps are comparable.

Consequently, the transformation ${}_{}^{(g)}$ makes the expected length of ${\mathbf{p}}_{\sigma}^{({g + 1})}$ independent of its direction, and for any sequence of realized covariance matrices ${\mathbf{C}}_{g = {0,1,2,\ldots}}^{(g)}$ we have under random selection ${\mathbf{p}}_{\sigma}^{({g + 1})} \sim {\mathcal{N}(\mathbf{0},\mathbf{I})}$, given ${\mathbf{p}}_{\sigma}^{} \sim {\mathcal{N}(\mathbf{0},\mathbf{I})}$.

To update $\sigma^{(g)}$, we "compare" $\|{\mathbf{p}}_{\sigma}^{({g + 1})}\|$ with its expected length $\mathsf{E}{\|{\mathcal{N}(\mathbf{0},\mathbf{I})}\|}$, that is

: $d_{\sigma} \approx 1$, damping parameter, scales the change magnitude of $\ln\sigma^{(g)}$. The factor ${c_{\sigma}/d_{\sigma}/\mathsf{E}}{\|{\mathcal{N}(\mathbf{0},\mathbf{I})}\|}$ is based on in-depth investigations of the algorithm.

: ${\mathsf{E}{\|{\mathcal{N}(\mathbf{0},\mathbf{I})}\|}} = {{{\sqrt{2}\Gamma{(\frac{n + 1}{2})}}/\Gamma}{(\frac{n}{2})}} \approx {\sqrt{n} + {\mathcal{O}{({1/n})}}}$, expectation of the Euclidean norm of a $\mathcal{N}(\mathbf{0},\mathbf{I})$ distributed random vector.

For ${\|{\mathbf{p}}_{\sigma}^{({g + 1})}\|} = {\mathsf{E}{\|{\mathcal{N}(\mathbf{0},\mathbf{I})}\|}}$ the second summand in is zero, and $\sigma^{(g)}$ is unchanged, while $\sigma^{(g)}$ is increased for ${\|{\mathbf{p}}_{\sigma}^{({g + 1})}\|} > {\mathsf{E}{\|{\mathcal{N}(\mathbf{0},\mathbf{I})}\|}}$, and $\sigma^{(g)}$ is decreased for ${\|{\mathbf{p}}_{\sigma}^{({g + 1})}\|} < {\mathsf{E}{\|{\mathcal{N}(\mathbf{0},\mathbf{I})}\|}}$.

> Alternatively, we might use the squared norm $\left\| {\mathbf{p}}_{\sigma}^{({g + 1})} \right\|^{2}$ in and compare with its expected value $n$. In this case would read
> $\ln\sigma^{({g + 1})}$ $=$ ${{\ln\sigma^{(g)}} + {\frac{c_{\sigma}}{2d_{\sigma}}\left( {\frac{\left\| {\mathbf{p}}_{\sigma}^{({g + 1})} \right\|^{2}}{n} - 1} \right)}}.$ \(33\)
> This update performs rather similar to, while it presumable leads to faster step-size increments and slower step-size decrements.

The step-size change is unbiased on the log scale, because ${\mathsf{E}\left\lbrack {\ln\sigma^{({g + 1})}} \middle| \sigma^{(g)} \right\rbrack} = {\ln\sigma^{(g)}}$ for ${\mathbf{p}}_{\sigma}^{({g + 1})} \sim {\mathcal{N}(\mathbf{0},\mathbf{I})}$. The role of unbiasedness is discussed in Sect. 5. Equations and cause successive steps of the distribution mean ${\mathbf{m}}^{(g)}$ to be approximately ${}_{}^{(g)}$-conjugate.

> In order to show that successive steps are approximately ${}_{}^{(g)}$-conjugate first we remark that and adapt $\sigma$ such that the length of ${\mathbf{p}}_{\sigma}^{({g + 1})}$ equals approximately $\mathsf{E}\left\| {\mathcal{N}(\mathbf{0},\mathbf{I})} \right\|$. Starting from $\left( {\mathsf{E}\left\| {\mathcal{N}(\mathbf{0},\mathbf{I})} \right\|} \right)^{2} \approx \left\| {\mathbf{p}}_{\sigma}^{({g + 1})} \right\|^{2} = {{}_{}^{\left( {g + 1} \right)}{\mathbf{p}}_{\sigma}^{({g + 1})}} = {{RHS}^{\mathsf{T}}{RHS}}$ of and assuming that the expected squared *length* of ${}_{}^{(g)}\left( {{\mathbf{m}}^{({g + 1})} - {\mathbf{m}}^{(g)}} \right)$ is unchanged by selection (unlike its direction) we get
> $${{\left( {{}_{}^{(g)}{\mathbf{p}}_{\sigma}^{(g)}} \right)^{\mathsf{T}}{}_{}^{(g)}\left( {{\mathbf{m}}^{({g + 1})} - {\mathbf{m}}^{(g)}} \right)} \approx 0}.$$ \(35\)
> Given $\left. 1/\left( {c_{1} + c_{\mu}} \right) \right. \gg 1$ and we assume also ${{}_{}^{\left( {g - 1} \right)}{}_{}^{(g)}\left( {{\mathbf{m}}^{({g + 1})} - {\mathbf{m}}^{(g)}} \right)} \approx 0$ and derive
> $${{\left( {{\mathbf{m}}^{(g)} - {\mathbf{m}}^{({g - 1})}} \right)^{\mathsf{T}}{}_{}^{(g)}\left( {{\mathbf{m}}^{({g + 1})} - {\mathbf{m}}^{(g)}} \right)} \approx 0}.$$ \(36\)
> That is, the steps taken by the distribution mean become approximately ${}_{}^{(g)}$-conjugate.

Because $\sigma^{(g)} > 0$, is equivalent to

The length of the evolution path is an intuitive and empirically well validated goodness measure for the overall step length. For $\mu_{eff} > 1$ it is the best measure to our knowledge.^2121^21Recently, two-point adaptation has shown to achieve similar performance. Nevertheless, it fails to adapt nearly optimal step-sizes on very noisy objective functions.

## Discussion

The CMA-ES is an attractive option for non-linear optimization, if "classical" search methods, e.g. quasi-Newton methods (BFGS) and/or conjugate gradient methods, fail due to a non-convex or rugged search landscape (e.g. sharp bends, discontinuities, outliers, noise, and local optima). Learning the covariance matrix in the CMA-ES is analogous to learning the inverse Hessian matrix in a quasi-Newton method. In the end, any convex-quadratic (ellipsoid) objective function is transformed into the spherical function $f_{sphere}$. This can reduce the number of $f$-evaluations needed to reach a target $f$-value on ill-conditioned and/or non-separable problems by orders of magnitude.

The CMA-ES overcomes typical problems that are often associated with evolutionary algorithms.

Poor performance on badly scaled and/or highly non-separable objective functions. Equation adapts the search distribution to badly scaled and non-separable problems.

The inherent need to use large population sizes. A typical, however intricate to diagnose reason for the failure of population based search algorithms is the degeneration of the population into a subspace.^2222^22The same problem can be observed with the downhill simplex method in dimension, say, larger than ten. This is usually prevented by non-adaptive components in the algorithm and/or by a large population size (considerably larger than the problem dimension). In the CMA-ES, the population size can be freely chosen, because the learning rates $c_{1}$ and $c_{\mu}$ in prevent the degeneration even for small population sizes, e.g. $\lambda = 9$. Small population sizes usually lead to faster convergence, large population sizes help to avoid local optima.

Premature convergence of the population. Step-size control in prevents the population to converge prematurely. It does not prevent the search to end up in a local optimum.

Therefore, the CMA-ES is highly competitive on a considerable number of test functions and was successfully applied to many real world problems.^2323^23The author stopped to maintain the growing list of (at the time 120) published references to applications in 2009.

Finally, we discuss a few basic design principles that were applied in the previous sections.

### Change rates

We refer to a change rate as the expected parameter change *per sampled search point*, given a certain selection situation. To achieve competitive performance on a wide range of objective functions, the possible change rates of the adaptive parameters need to be adjusted carefully. The CMA-ES separately controls change rates for the mean value of the distribution, $\mathbf{m}$, the covariance matrix, $\mathbf{C}$, and the step-size, $\sigma$.

The change rate for the mean value $\mathbf{m}$, relative to the given sample distribution, is determined by $c_{m}$, and by the parent number and the recombination weights. The larger $\mu_{eff}$, the smaller is the possible change rate of $\mathbf{m}$.^2424^24Given $\lambda\gg\not{}n$, then the mean change per generation is roughly proportional to $\sigma/\sqrt{\mu_{eff}}$, while the optimal step-size $\sigma$ is roughly proportional to $\mu_{eff}$. Therefore, the net change *with optimal step-size* is proportional to $\sqrt{\mu_{eff}}$ per generation. Now considering the effect on the resulting convergence rate, a closer approximation of the gradient adds another factor of $\sqrt{\mu_{eff}}$, such that the generational progress rate is proportional to $\mu_{eff}$. Given ${\lambda/\mu_{eff}} \approx 4$, we have the remarkable result that the convergence rate *per $f$-evaluation* is roughly independent of $\lambda$. Similar holds for most evolutionary algorithms.

The change rate of the covariance matrix $\mathbf{C}$ is explicitly controlled by the learning rates $c_{1}$ and $c_{\mu}$ and therefore detached from parent number and population size. The learning rate reflects the model complexity. In evolutionary algorithms, the explicit control of change rates of the covariances, independently of population size and mean change, is a rather unique feature.

The change rate of the step-size $\sigma$ is explicitly controlled by the damping parameter $d_{\sigma}$ and is in particular independent from the change rate of $\mathbf{C}$. The time constant ${1/c_{\sigma}} \leq n$ ensures a sufficiently fast change of the overall step length in particular with small population sizes.

### Invariance

Invariance properties of a search algorithm denote identical behavior on a set, or a class of objective functions. Invariance is an important property of the CMA-ES.^2525^25Special acknowledgments to Iván Santibán̄ez-Koref for pointing this out to me. Translation invariance should be taken for granted in continuous domain optimization. Translation invariance means that the search behavior on the function ${\mathbf{x}}\mapsto{f{({{\mathbf{x}} + {\mathbf{a}}})}}$, ${\mathbf{x}}^{} = {{\mathbf{b}} - {\mathbf{a}}}$, is independent of ${\mathbf{a}} \in {\mathbb{R}}^{n}$. Further invariances, e.g. invariance to certain linear transformations of the search space, are highly desirable: they imply uniform performance on classes of functions^2626^26However, most invariances are linked to a state space transformation. Therefore, uniform performance is only observed *after* the state of the algorithm has been adapted. and therefore allow for generalization of empirical results. In addition to translation invariance, the CMA-ES exhibits the following invariances.

Invariance to order preserving (i.e. strictly monotonic) transformations of the objective function value. The algorithm only depends on *the ranking* of function values.

Invariance to angle preserving (rigid) transformations of the search space (rotation, reflection, and translation) if the initial search point is transformed accordingly.

Scale invariance if the initial scaling, e.g. $\sigma^{}$, and the initial search point, ${\mathbf{m}}^{}$, are chosen accordingly.

Invariance to a scaling of variables (diagonal invariance) if the initial diagonal covariance matrix ${\mathbf{C}}^{}$, and the initial search point, ${\mathbf{m}}^{}$, are chosen accordingly.

Invariance to any invertible linear transformation of the search space, $\mathbf{A}$, if the initial covariance matrix ${\mathbf{C}}^{} = {{\mathbf{A}}^{- 1}\left( {\mathbf{A}}^{- 1} \right)^{\mathsf{T}}}$, and the initial search point, ${\mathbf{m}}^{}$, are transformed accordingly. Together with translation invariance, this can also be referred to as *affine invariance*, i.e. invariance to affine search space transformations.

Invariance should be a fundamental design criterion for any search algorithm. Together with the ability to efficiently adapt the invariance governing parameters, invariance is a key to competitive performance.

### Stationarity or Unbiasedness

An important design criterion for a *randomized* search procedure is *unbiasedness* of variations of object and strategy parameters. Consider random selection, e.g. the objective function ${f{({\mathbf{x}})}} = {\mathtt{r}\mathtt{a}\mathtt{n}\mathtt{d}}$ to be independent of $\mathbf{x}$. Then the population mean is unbiased if its expected value remains unchanged in the next generation, that is ${\mathsf{E}\left\lbrack {\mathbf{m}}^{({g + 1})} \middle| {\mathbf{m}}^{(g)} \right\rbrack} = {\mathbf{m}}^{(g)}$. For the population mean, stationarity under random selection is a rather intuitive concept. In the CMA-ES, stationarity is respected for all parameters that appear in the basic equation. The distribution mean $\mathbf{m}$, the covariance matrix $\mathbf{C}$, and $\ln\sigma$ are unbiased. Unbiasedness of $\ln\sigma$ does not imply that $\sigma$ is unbiased. Under random selection, ${\mathsf{E}\left\lbrack \sigma^{({g + 1})} \middle| \sigma^{(g)} \right\rbrack} > \sigma^{(g)}$, compare.^2727^27Alternatively, if were designed to be unbiased for $\sigma^{({g + 1})}$, this would imply that ${\mathsf{E}\left\lbrack {\ln\sigma^{({g + 1})}} \middle| \sigma^{(g)} \right\rbrack} < {\ln\sigma^{(g)}}$, in our opinion a less desirable alternative.

For distribution variances (or step-sizes) a bias toward increase or decrease entails the risk of divergence or premature convergence, respectively, whenever the selection pressure is low or when no improvements are observed. On noisy problems, a properly controlled bias towards increase can be appropriate. It has the non-negligible disadvantage that the decision for termination becomes more difficult.
