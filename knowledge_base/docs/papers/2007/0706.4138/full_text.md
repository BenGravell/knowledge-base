# Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization

- arXiv ID: [0706.4138](https://arxiv.org/abs/0706.4138)
- HTML source: [ar5iv](https://ar5iv.labs.arxiv.org/html/0706.4138)

Benjamin Recht Center for the Mathematics of Information, California Institute of Technology    Maryam Fazel Control and Dynamical Systems, California Institute of Technology    Pablo A. Parrilo Laboratory for Information and Decision Systems, Massachusetts Institute of Technology

###### Abstract 

The affine rank minimization problem consists of finding a matrix of minimum rank that satisfies a given system of linear equality constraints. Such problems have appeared in the literature of a diverse set of fields including system identification and control, Euclidean embedding, and collaborative filtering. Although specific instances can often be solved with specialized algorithms, the general affine rank minimization problem is NP-hard, because it contains vector cardinality minimization as a special case.

In this paper, we show that if a certain restricted isometry property holds for the linear transformation defining the constraints, the minimum rank solution can be recovered by solving a convex optimization problem, namely the minimization of the nuclear norm over the given affine space. We present several random ensembles of equations where the restricted isometry property holds with overwhelming probability, provided the codimension of the subspace is $\Omega\hspace{0pt}{({r\hspace{0pt}{({m + n})}\hspace{0pt}{\log{m\hspace{0pt}n}}})}$, where $m,n$ are the dimensions of the matrix, and $r$ is its rank.

The techniques used in our analysis have strong parallels in the compressed sensing framework. We discuss how affine rank minimization generalizes this pre-existing concept and outline a dictionary relating concepts from cardinality minimization to those of rank minimization. We also discuss several algorithmic approaches to solving the norm minimization relaxations, and illustrate our results with numerical examples.

Keywords. rank, convex optimization, matrix norms, random matrices, compressed sensing, semidefinite programming.

## 1 Introduction 

Notions such as order, complexity, or dimensionality can often be expressed by means of the rank of an appropriate matrix. For example, a low-rank matrix could correspond to a low-degree statistical model for a random process (e.g., factor analysis), a low-order realization of a linear system \[28\], a low-order controller for a plant \[22\], or a low-dimensional embedding of data in Euclidean space \[34\]. If the set of feasible models or designs is affine in the matrix variable, choosing the simplest model can be cast as an *affine rank minimization problem*,

  -- ------------------------------------------------------------- -- -------
     $$\begin{array}{ll}                                              (1.1)
     \text{minimize} & {{rank}{(X)}} \\                               
     \text{subject to} & {{{\mathcal{A}\hspace{0pt}{(X)}} = b},}      
     \end{array}$$                                                    
  -- ------------------------------------------------------------- -- -------

where $X \in {\mathbb{R}}^{m \times n}$ is the decision variable, and the linear map $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ and vector $b \in {\mathbb{R}}^{p}$ are given. In certain instances with very special structure, the rank minimization problem can be solved by using the singular value decomposition, or can be exactly reduced to the solution of linear systems \[37, 41\]. In general, however, problem (1.1) is a challenging nonconvex optimization problem for which all known finite time algorithms have at least doubly exponential running times in both theory and practice. For the general case, a variety of heuristic algorithms based on local optimization, including alternating projections \[31\] and alternating LMIs \[45\], have been proposed.

A recent heuristic introduced in \[27\] minimizes the *nuclear norm*, or the sum of the singular values of the matrix, over the affine subset. The nuclear norm is a convex function, can be optimized efficiently, and is the best convex approximation of the rank function over the unit ball of matrices with norm less than one. When the matrix variable is symmetric and positive semidefinite, this heuristic is equivalent to the trace heuristic often used by the control community (see, e.g., \[5, 37\]). The nuclear norm heuristic has been observed to produce very low-rank solutions in practice, but a theoretical characterization of when it produces the minimum rank solution has not been previously available. This paper provides the first such mathematical characterization.

Our work is built upon a large body of literature on a related optimization problem. When the matrix variable is constrained to be diagonal, the affine rank minimization problem reduces to finding the *sparsest vector* in an affine subspace. This problem is commonly referred to as *cardinality minimization*, since we seek the vector whose support has the smallest cardinality, and is known to be NP-hard \[39\]. For diagonal matrices, the sum of the singular values is equal to the sum of the absolute values (i.e., the $\ell_{1}$ norm) of the diagonal elements. Minimization of the $\ell_{1}$ norm is a well-known heuristic for the cardinality minimization problem, and stunning results pioneered by Candès and Tao \[10\] and Donoho \[17\] have characterized a vast set of instances for which the $\ell_{1}$ heuristic can be *a priori* guaranteed to yield the optimal solution. These techniques provide the foundations of the recently developed *compressed sensing* or *compressive sampling* frameworks for measurement, coding, and signal estimation. As has been shown by a number of research groups (e.g., \[4, 12, 13, 14\]), the $\ell_{1}$ heuristic for cardinality minimization provably recovers the sparsest solution whenever the sensing matrix has certain "basis incoherence" properties, and in particular, when it is randomly chosen according to certain specific ensembles.

The fact that the $\ell_{1}$ heuristic is a special case of the nuclear norm heuristic suggests that these results from the compressed sensing literature might be extended to provide guarantees about the nuclear norm heuristic for the more general rank minimization problem. In this paper, we show that this is indeed the case, and the parallels are surprisingly strong. Following the program laid out in the work of Candès and Tao, our main contribution is the development of a restricted isometry property (RIP), under which the nuclear norm heuristic can be *guaranteed* to produce the minimum-rank solution. Furthermore, as in the case for the $\ell_{1}$ heuristic, we provide several specific examples of matrix ensembles for which RIP holds with overwhelming probability. Our results considerably extend the compressed sensing machinery in a so far undeveloped direction, by allowing a much more general notion of parsimonious models that rely on low-rank assumptions instead of cardinality restrictions.

To make the parallels as clear as possible, we begin by establishing a dictionary between the matrix rank and nuclear norm minimization problems and the vector sparsity and $\ell_{1}$ norm problems in Section 2. In the process of this discussion, we present a review of many useful properties of the matrices and matrix norms necessary for the main results. We then generalize the notion of Restricted Isometry to matrices in Section 3 and show that when linear mappings are Restricted Isometries, recovering low-rank solutions of underdetermined systems can be achieved by nuclear norm minimization. In Section 4, we present several families of random linear maps that are restricted isometries with overwhelming probability when the dimensions are sufficiently large. In Section 5, we briefly discuss three different algorithms designed for solving the nuclear norm minimization problem and their relative strengths and weaknesses: interior point methods, gradient projection methods, and a low-rank factorization technique. In Section 6, we demonstrate that in practice nuclear-norm minimization recovers the lowest rank solutions of affine sets with even fewer constraints than those guaranteed by our mathematical analysis. Finally, in Section 7, we list a number of possible directions for future research.

### 1.1 When are random constraints interesting for rank minimization? 

As in the case of compressed sensing, the conditions we derive to guarantee properties about the nuclear norm heuristic are deterministic, but they are at least as difficult to check as solving the rank minimization problem itself. We are only able to guarantee that the nuclear norm heuristic recovers the minimum rank solution of ${\mathcal{A}\hspace{0pt}{(X)}} = b$ when $\mathcal{A}$ is sampled from specific ensembles of random maps. The constraints appearing in many of the applications mentioned above, such as low-order control system design, are typically not random at all and have structured demands according to the specifics of the design problem. It thus behooves us to present several examples where random constraints manifest themselves in practical scenarios for which no practical solution procedure is known.

#### Minimum order linear system realization 

Rank minimization forms the basis of many model reduction and low-order system identification problems for linear time-invariant (LTI) systems. The following example illustrates how random constraints might arise in this context. Consider the problem of finding the minimum order discrete-time LTI system that is consistent with a set of time-domain observations. In particular, suppose our observations are the system output sampled at a fixed time $N$, after a random Gaussian input signal is applied from $t = 0$ to $t = N$. Suppose we make such measurements for $p$ different input signals, that is, we observe ${y_{i}\hspace{0pt}{(N)}} = {\sum_{t = 0}^{N}{a_{i}\hspace{0pt}{({N - t})}\hspace{0pt}h\hspace{0pt}{(t)}}}$ for $i = {1,\ldots,p}$, where $a_{i}$, the $i$th input signal, is a zero-mean Gaussian random variable with the same variance for $t = {0,{\ldots\hspace{0pt}N}}$, and $h\hspace{0pt}{(t)}$ denotes the impulse response. We can write this compactly as $y = {A\hspace{0pt}h}$, where $h = {\lbrack{h\hspace{0pt}{(0)}},\ldots,{h\hspace{0pt}{(N)}}\rbrack}^{\prime}$, and $A_{i\hspace{0pt}j} = {a_{i}\hspace{0pt}{({N - j})}}$.

From linear system theory, the order of the minimal realization for such a system is given by the rank of the following Hankel matrix (see, e.g., \[29, 46\])

  -- -------------------------------------------------------------------------------------------------- --
     $${{{hank}{(h)}}:=\begin{bmatrix}                                                                  
     {h\hspace{0pt}{(0)}} & {h\hspace{0pt}{(1)}} & \cdots & {h\hspace{0pt}{(N)}} \\                     
     {h\hspace{0pt}{(1)}} & {h\hspace{0pt}{(2)}} & \cdots & {h\hspace{0pt}{({N + 1})}} \\               
     \vdots & \vdots & & \vdots \\                                                                      
     {h\hspace{0pt}{(N)}} & {h\hspace{0pt}{({N + 1})}} & \cdots & {h\hspace{0pt}{({2\hspace{0pt}N})}}   
     \end{bmatrix}}.$$                                                                                  
  -- -------------------------------------------------------------------------------------------------- --

Therefore the problem can be expressed as

  -- ------------------------------------------------ --
     $$\begin{array}{ll}                              
     \text{minimize} & {{rank}{({{hank}{(h)}})}} \\   
     \text{subject to} & {{A\hspace{0pt}h} = y}       
     \end{array}$$                                    
  -- ------------------------------------------------ --

where the optimization variables are ${h\hspace{0pt}{(0)}},\ldots,{h\hspace{0pt}{({2\hspace{0pt}N})}}$, and the matrix $A$ consists of i.i.d. zero-mean Gaussian entries.

#### Low-Rank Matrix Completion 

In the matrix completion problem where we are given random subset of entries of a matrix, we would like to fill in the missing entries such that the resulting matrix has the lowest possible rank. This problem arises in machine learning scenarios where we are given partially observed examples of a process with a low-rank covariance matrix and would like to estimate the missing data. A typical situation where the hidden matrix is low-rank is when the columns are i.i.d. samples of a random process with low-rank covariance. Such models are ubiquitous in Factor Analysis, Collaborative Filtering, and Latent Semantic Indexing \[42, 47\]. In many of these settings, some prior probability distribution (such as a Bernoulli model or uniform distribution on subsets) is assumed to generate the set of available entries.

Suppose we are presented with a set of triples $({I\hspace{0pt}{(i)}},{J\hspace{0pt}{(i)}},{S\hspace{0pt}{(i)}})$ for $i = {1,\ldots,p}$ and wish to find the matrix with $S\hspace{0pt}{(i)}$ in the entry corresponding to row $I\hspace{0pt}{(i)}$ and column $J\hspace{0pt}{(i)}$ for all $i$. The matrix completion problem seeks to solve

  -- ----------------------------------------------------------------------------------------------------------- --
     $$\begin{aligned}                                                                                           
     \min\limits_{Y} & {{rank}{(Y)}} \\                                                                          
     \text{s.t.} & {{Y_{{I\hspace{0pt}{(i)}},{J\hspace{0pt}{(i)}}} = {S\hspace{0pt}{(i)}}},{i = {1,\ldots,K}}}   
     \end{aligned}$$                                                                                             
  -- ----------------------------------------------------------------------------------------------------------- --

which is a special case of the affine rank minimization problem.

#### Low-dimensional Euclidean embedding problems 

A problem that arises in a variety of fields is the determination of configurations of points in low-dimensional Euclidean spaces, subject to some given distance information. In Multi-Dimensional Scaling (MDS), such problems occur in extracting the underlying geometric structure of distance data. In psychometrics, the information about inter-point distances is usually gathered through a set of experiments where subjects are asked to make quantitative (in metric MDS) or qualitative (in non-metric MDS) comparisons of objects. In computational chemistry, they come up in inferring the three-dimensional structure of a molecule (molecular conformation) from information about interatomic distances \[52\].

A symmetric matrix $D \in \mathcal{S}^{n}$ is called a *Euclidean distance matrix* (EDM) if there exist points $x_{1},\ldots,x_{n}$ in ${\mathbb{R}}^{d}$ such that $D_{i\hspace{0pt}j} = {\|{x_{i} - x_{j}}\|}^{2}$. Let $V:={I_{n} - {\frac{1}{n}\hspace{0pt}\mathbf{1}\mathbf{1}^{T}}}$ be the projection matrix onto the hyperplane $\{{v \in {\mathbb{R}}^{n}}:{{\,\, 1^{T}\hspace{0pt}v} = 0}\}$. A classical result by Schoenberg states that $D$ is a Euclidean distance matrix of $n$ points in ${\mathbb{R}}^{d}$ if and only if $D_{i\hspace{0pt}i} = 0$, the matrix $V\hspace{0pt}D\hspace{0pt}V$ is negative semidefinite, and ${rank}{({V\hspace{0pt}D\hspace{0pt}V})}$ is less than or equal to $d$ \[44\]. If the matrix $D$ is known exactly, the corresponding configuration of points (up to a unitary transform) is obtained by simply taking a matrix square root of $- {\frac{1}{2}\hspace{0pt}V\hspace{0pt}D\hspace{0pt}V}$. However, in many cases, only a random sampling collection of the distances are available. The problem of finding a valid EDM consistent with the known inter-point distances and with the smallest embedding dimension can be expressed as the rank optimization problem

  -- -------------------------------------------------------------------- --
     $$\begin{array}{clc}                                                 
     \text{minimize} & {{rank}{({V\hspace{0pt}D\hspace{0pt}V})}} & \\     
     \text{subject to} & {{V\hspace{0pt}D\hspace{0pt}V} \preceq 0} & \\   
      & {{{\mathcal{A}\hspace{0pt}{(D)}} = b},} &                         
     \end{array}$$                                                        
  -- -------------------------------------------------------------------- --

where $\mathcal{A}:{\mathcal{S}^{n}\rightarrow{\mathbb{R}}^{p}}$ is a random sampling operator as discussed in the matrix completion problem.

This problem involves a Linear Matrix Inequality (LMI) and appears to be more general than the equality constrained rank minimization problem. However, general LMIs can equivalently be expressed as rank constraints on an appropriately defined block matrix. The rank of a block symmetric matrix is equal to the rank of a diagonal block plus the rank of its Schur complement (see, e.g., \[33, §2.2\]). Given a function $f$ that maps matrices into $q \times q$ symmetric matrices, that $f\hspace{0pt}{(X)}$ is positive semidefinite can be equivalently expressed through a rank constraint as

  -- -------------------------------------------------------------------------------------------------------- --
     $${{{f\hspace{0pt}{(X)}} \succeq {0\qquad\Leftrightarrow}}\mspace{39mu}{{{{rank}\left( \begin{bmatrix}   
     I_{q} & B \\                                                                                             
     B^{\prime} & {f\hspace{0pt}{(X)}}                                                                        
     \end{bmatrix} \right)} \leq q},{{\text{~for some~}\hspace{0pt}B} \in {\mathbb{R}}^{q \times q}}}}.$$     
  -- -------------------------------------------------------------------------------------------------------- --

That is, if there exists a matrix $B$ satisfying the inequality above, then ${f\hspace{0pt}{(X)}} = {B^{\prime}\hspace{0pt}B} \succeq 0$. Using this equivalent representation allows us to rewrite (1.1) as an affine rank minimization problem.

#### Image Compression 

A simple and well-known method to compress two-dimensional images can be obtained by using the singular value decomposition (e.g., \[3\]). The basic idea is to associate to the given grayscale image a rectangular matrix $M$, with the entries $M_{i\hspace{0pt}j}$ corresponding to the gray level of the $(i,j)$ pixel. The best rank-$k$ approximation of $M$ is given by

  -- -------------------------------------------------------------------------------------- --
     $${X^{\ast}:={{\arg\min\limits_{{{rank}{(X)}} \leq k}}\hspace{0pt}{\|{M - X}\|}}},$$   
  -- -------------------------------------------------------------------------------------- --

where $|| \cdot ||$ is any unitarily invariant norm. By the classical Eckart-Young-Mirsky theorem (\[20, 38\]), the optimal approximant is given by a truncated singular value decomposition of $M$, i.e., if $M = {U\hspace{0pt}\Sigma\hspace{0pt}V^{T}}$, then $X^{\ast} = {U\hspace{0pt}\Sigma_{k}\hspace{0pt}V^{T}}$, where the first $k$ diagonal entries of $\Sigma_{k}$ are the largest $k$ singular values, and the rest of the entries are zero. If for a given rank $k$, the approximation error $\|{M - X^{\ast}}\|$ is small enough, then the amount of data needed to encode the information about the image is $k\hspace{0pt}{({{m + n} - k})}$ real numbers, which can be much smaller than the $m\hspace{0pt}n$ required to transmit the values of all the entries.

Consider a given image, whose associated matrix $M$ has low-rank, or can be well-approximated by a low-rank matrix. As proposed by Wakin *et al.* \[54\], a single-pixel camera would ideally produce measurements that are random linear combinations of all the pixels of the given image. Under this situation, the image reconstruction problem boils down exactly to affine rank minimization, where the constraints are given by the random linear functionals.

It should be remarked that the simple SVD image compression scheme described has certain deficiencies that more sophisticated techniques do not share (in particular, the lack of invariance of the description length under rotations). Nevertheless, due to its simplicity and relatively good practical performance, this method is particularly popular in introductory treatments and numerical linear algebra textbooks.

## 2 From Compressed Sensing to Rank Minimization 

As discussed above, when the matrix variable is constrained to be diagonal, the affine rank minimization problem (1.1) reduces to the cardinality minimization problem of finding the element in the affine space with the fewest number of nonzero components. In this section we will establish a dictionary between the concepts of rank and cardinality minimization. The main elements of this correspondence are outlined in Table 1. With these elements in place, the existing proofs of sparsity recovery provide a template for the more general case of low-rank recovery.

In establishing our dictionary, we will provide a review of useful facts regarding matrix norms and their characterization as convex optimization problems. We will show how computing both the operator norm and the nuclear norm of a matrix can be cast as semidefinite programming problems. We also establish the suitable optimality conditions for the minimization of the nuclear norm under affine equality constraints, the main convex optimization problem studied in this article. Our discussion of matrix norms will mostly follow the discussion in \[27, 53\] where extensive lists of references are provided.

parsimony concept
cardinality
rank

Hilbert Space norm
Euclidean
Frobenius

sparsity inducing norm
ℓ1
nuclear

dual norm
ℓ∞
operator

norm additivity
disjoint support
orthogonal row and column spaces

convex optimization
linear programming
semidefinite programming

Table 1: A dictionary relating the concepts of cardinality and rank minimization.

#### Matrix vs.  Vector Norms 

The three vector norms that play significant roles in the compressed sensing framework are the $\ell_{1}$, $\ell_{2}$, and $\ell_{\infty}$ norms, denoted by ${\| x\|}_{1}$, $\| x\|$ and ${\| x\|}_{\infty}$ respectively. These norms have natural generalizations to matrices, inheriting many appealing properties from the vector case. In particular, there is a parallel duality structure.

For a rectangular matrix $X \in {\mathbb{R}}^{m \times n}$, $\sigma_{i}\hspace{0pt}{(X)}$ denotes the $i$-th largest singular value of $X$ and is equal to the square-root of the $i$-th largest eigenvalue of $X\hspace{0pt}X^{\prime}$. The rank of $X$ will usually be denoted by $r$, and is equal to the number of nonzero singular values. For matrices $X$ and $Y$ of the same dimensions, we define the inner product in ${\mathbb{R}}^{m \times n}$ as ${\langle X,Y\rangle}:={{Tr}{({X^{\prime}\hspace{0pt}Y})}} = {\sum_{i = 1}^{m}{\sum_{j = 1}^{n}{X_{i\hspace{0pt}j}\hspace{0pt}Y_{i\hspace{0pt}j}}}}$. The norm associated with this inner product is called the Frobenius (or Hilbert-Schmidt) norm $|| \cdot ||_{F}$. The Frobenius norm is also equal to the Euclidean, or $\ell_{2}$, norm of the vector of singular values, i.e.,

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\| X\|}_{F}:=\sqrt{\langle X,X\rangle} = \sqrt{{Tr}{({X^{\prime}\hspace{0pt}X})}} = \left( {\sum\limits_{i = 1}^{m}{\sum\limits_{j = 1}^{n}X_{i\hspace{0pt}j}^{2}}} \right)^{\frac{1}{2}} = \left( {\sum\limits_{i = 1}^{r}\sigma_{i}^{2}} \right)^{\frac{1}{2}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

The operator norm (or induced 2-norm) of a matrix is equal to its largest singular value (i.e., the $\ell_{\infty}$ norm of the singular values):

  -- ------------------------------------------------ --
     $${{\| X\|}:={\sigma_{1}\hspace{0pt}{(X)}}}.$$   
  -- ------------------------------------------------ --

The nuclear norm of a matrix is equal to the sum of its singular values, i.e.,

  -- -------------------------------------------------------------------------------- --
     $${{\| X\|}_{\ast}:={\sum\limits_{i = 1}^{r}{\sigma_{i}\hspace{0pt}{(X)}}}},$$   
  -- -------------------------------------------------------------------------------- --

and is alternatively known by several other names including the Schatten $1$-norm, the Ky Fan $r$-norm, and the trace class norm. Since the singular values are all positive, the nuclear norm is equal to the $\ell_{1}$ norm of the vector of singular values. These three norms are related by the following inequalities which hold for any matrix $X$ of rank at most $r$:

  -- ----------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{\| X\|} \leq {\| X\|}_{F} \leq {\| X\|}_{\ast} \leq {\sqrt{r}\hspace{0pt}{\| X\|}_{F}} \leq {r\hspace{0pt}{\| X\|}}}.$$      (2.1)
  -- ----------------------------------------------------------------------------------------------------------------------------- -- -------

#### Dual norms 

For any given norm $\parallel \cdot \parallel$ in an inner product space, there exists a dual norm $\parallel \cdot \parallel_{d}$ defined as

  -- -------------------------------------------------------------------------------------- -- -------
     $${{\| X\|}_{d}:={\max\limits_{Y}{\{{{\langle X,Y\rangle}:{{\| Y\|} \leq 1}}\}}}}.$$      (2.2)
  -- -------------------------------------------------------------------------------------- -- -------

Furthermore, the norm dual to the norm $|| \cdot ||_{d}$ is again the original norm $|| \cdot ||$.

In the case of vector norms in ${\mathbb{R}}^{n}$, it is well-known that the dual norm of the $\ell_{p}$ norm (with $1 < p < \infty$) is the $\ell_{q}$ norm, where ${\frac{1}{p} + \frac{1}{q}} = 1$. This fact is essentially equivalent to Hölder's inequality. Similarly, the dual norm of the $\ell_{\infty}$ norm of a vector is the $\ell_{1}$ norm. These facts also extend to the matrix norms we have defined. For instance, the dual norm of the Frobenius norm is the Frobenius norm. This can be verified by simple calculus (or Cauchy-Schwarz), since

  -- ------------------------------------------------------------------------------------------------------------- --
     $$\max\limits_{Y}{\{{{{Tr}{({X^{\prime}\hspace{0pt}Y})}}:{{{Tr}{({Y^{\prime}\hspace{0pt}Y})}} \leq 1}}\}}$$   
  -- ------------------------------------------------------------------------------------------------------------- --

is equal to ${\| X\|}_{F}$, with the maximizing $Y$ being equal to $X/{\| X\|}_{F}$. Similarly, as shown below, the dual norm of the operator norm is the nuclear norm. The proof of this fact will also allow us to present variational characterizations of each of these norms as semidefinite programs.

###### Proposition 2.1 

The dual norm of the operator norm $|| \cdot ||$ in ${\mathbb{R}}^{m \times n}$ is the nuclear norm $|| \cdot ||_{\ast}$.

Proof    First consider an $m \times n$ matrix $Z$. The fact that $Z$ has operator norm less than $t$ can be expressed as a linear matrix inequality:

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{{\| Z\|} \leq {t\quad\Leftrightarrow}}\quad{{{{t^{2}\hspace{0pt}I_{m}} - {Z\hspace{0pt}Z^{\prime}}} \succeq {0\quad\Leftrightarrow}}\quad{\begin{bmatrix}      (2.3)
     {t\hspace{0pt}I_{m}} & Z \\                                                                                                                                        
     Z^{\prime} & {t\hspace{0pt}I_{n}}                                                                                                                                  
     \end{bmatrix} \succeq 0}}},$$                                                                                                                                      
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

where the last implication follows from a Schur complement argument. As a consequence, we can give a semidefinite optimization characterization of the operator norm, namely

  -- ---------------------------------------------------------------------------- -- -------
     $${{{\| Z\|} = {{\min\limits_{t}t}\qquad\text{s.t.}}}\quad{\begin{bmatrix}      (2.4)
     {t\hspace{0pt}I_{m}} & Z \\                                                     
     Z^{\prime} & {t\hspace{0pt}I_{n}}                                               
     \end{bmatrix} \succeq 0}}.$$                                                    
  -- ---------------------------------------------------------------------------- -- -------

Now let $X = {U\hspace{0pt}\Sigma\hspace{0pt}V^{\prime}}$ be a singular value decomposition of an $m \times n$ matrix $X$, where $U$ is an $m \times r$ matrix, $V$ is an $n \times r$ matrix, $\Sigma$ is a $r \times r$ diagonal matrix and $r$ is the rank of $X$. Let $Y:={U\hspace{0pt}V^{\prime}}$. Then ${\| Y\|} = 1$ and ${{Tr}{({X\hspace{0pt}Y^{\prime}})}} = {\sum_{i = 1}^{r}{\sigma_{i}\hspace{0pt}{(X)}}} = {\| X\|}_{\ast}$, and hence the dual norm is greater than or equal to the nuclear norm.

To provide an upper bound on the dual norm, we appeal to semidefinite programming duality. From the characterization in (2.3), the optimization problem

  -- ------------------------------------------------------------------- --
     $$\max\limits_{Y}{\{{{\langle X,Y\rangle}:{{\| Y\|} \leq 1}}\}}$$   
  -- ------------------------------------------------------------------- --

is equivalent to the semidefinite program

  -- ---------------------------------------------------------- -- -------
     $$\begin{array}{ll}                                           (2.5)
     \max\limits_{Y} & {{Tr}{({X^{\prime}\hspace{0pt}Y})}} \\      
     \text{s.t.} & {{\begin{bmatrix}                               
     I_{m} & Y \\                                                  
     Y^{\prime} & I_{n}                                            
     \end{bmatrix} \succeq 0}.}                                    
     \end{array}$$                                                 
  -- ---------------------------------------------------------- -- -------

The dual of this SDP (after an inconsequential rescaling) is given by

  -- ------------------------------------------------------------------------------------------------- -- -------
     $$\begin{array}{ll}                                                                                  (2.6)
     \min\limits_{W_{1},W_{2}} & {\frac{1}{2}\hspace{0pt}{({{{Tr}{(W_{1})}} + {{Tr}{(W_{2})}}})}} \\      
     \text{s.t.} & {{\begin{bmatrix}                                                                      
     W_{1} & X \\                                                                                         
     X^{\prime} & W_{2}                                                                                   
     \end{bmatrix} \succeq 0}.}                                                                           
     \end{array}$$                                                                                        
  -- ------------------------------------------------------------------------------------------------- -- -------

Set $W_{1}:={U\hspace{0pt}\Sigma\hspace{0pt}U^{\prime}}$ and $W_{2}:={V\hspace{0pt}\Sigma\hspace{0pt}V^{\prime}}$. Then the triple $(W_{1},W_{2},X)$ is feasible for (2.6) since

  -- ------------------------------------------------------------ --
     $${\begin{bmatrix}                                           
     W_{1} & X \\                                                 
     X^{\prime} & W_{2}                                           
     \end{bmatrix} = {\begin{bmatrix}                             
     U \\                                                         
     V                                                            
     \end{bmatrix}\hspace{0pt}\Sigma\hspace{0pt}\begin{bmatrix}   
     U \\                                                         
     V                                                            
     \end{bmatrix}^{\prime}} \succeq 0}.$$                        
  -- ------------------------------------------------------------ --

Furthermore, we have ${{Tr}{(W_{1})}} = {{Tr}{(W_{2})}} = {{Tr}{(\Sigma)}}$, and thus the objective function satisfies ${{({{{Tr}{(W_{1})}} + {{Tr}{(W_{2})}}})}/2} = {{Tr}\Sigma} = {\| X\|}_{\ast}$. Since any feasible solution of (2.6) provides an upper bound for (2.5), we have that the dual norm is less than or equal to the nuclear norm of $X$, thus proving the proposition.  

Notice that the argument given in the proof above further shows that the nuclear norm ${\| X\|}_{\ast}$ can be computed using either the SDP (2.5) or its dual (2.6), since there is no duality gap between them. Alternatively, this could have also been proven using a Slater-type interior point condition since both (2.5) and (2.6) admit strictly feasible solutions.

#### Convex envelopes of rank and cardinality functions 

Let $\mathcal{C}$ be a given convex set. The *convex envelope* of a (possibly nonconvex) function $f:{\mathcal{C}\rightarrow{\mathbb{R}}}$ is defined as the largest convex function $g$ such that ${g\hspace{0pt}{(x)}} \leq {f\hspace{0pt}{(x)}}$ for all $x \in \mathcal{C}$ (see, e.g., \[32\]). This means that among all convex functions, $g$ is the best pointwise approximation to $f$. In particular, if the optimal $g$ can be conveniently described, it can serve as an approximation to $f$ that can be minimized efficiently.

By the chain of inequalities in (2.1), we have that ${{rank}{(X)}} \geq {{\| X\|}_{\ast}/{\| X\|}}$ for all $X$. For all matrices with ${\| X\|} \leq 1$, we must have that ${{rank}{(X)}} \geq {\| X\|}_{\ast}$, so the nuclear norm is a convex lower bound of the rank function on the unit ball in the operator norm. In fact, it can be shown that this is the tightest convex lower bound.

###### Theorem 2.2 (\[27\]) 

The convex envelope of ${rank}{(X)}$ on the set $\{{X \in {\mathbb{R}}^{m \times n}}:{{\| X\|} \leq 1}\}$ is the nuclear norm ${\| X\|}_{\ast}$.

The proof is given in \[27\] and uses a basic result from convex analysis that establishes that (under some technical conditions) the biconjugate of a function is its convex envelope \[32\].

Theorem 2.2 ‣ Convex envelopes of rank and cardinality functions ‣ 2 From Compressed Sensing to Rank Minimization ‣ Guaranteed Minimum-Rank Solutions of Linear Matrix Equations via Nuclear Norm Minimization") provides the following interpretation of the nuclear norm heuristic for the affine rank minimization problem. Suppose $X_{0}$ is the minimum rank solution of ${\mathcal{A}\hspace{0pt}{(X)}} = b$, and $M = {\| X_{0}\|}$. The convex envelope of the rank on the set $\mathcal{C} = {\{{X \in {\mathbb{R}}^{m \times n}}:{{\| X\|} \leq M}\}}$ is ${\| X\|}_{\ast}/M$. Let $X_{\ast}$ be the minimum nuclear norm solution of ${\mathcal{A}\hspace{0pt}{(X)}} = b$. Then we have

  -- --------------------------------------------------------------------------------- --
     $${{\| X_{\ast}\|}_{\ast}/M} \leq {{rank}{(X_{0})}} \leq {{rank}{(X_{\ast})}}$$   
  -- --------------------------------------------------------------------------------- --

providing an upper and lower bound on the optimal rank when the norm of the optimal solution is known. Furthermore, this is the tightest lower bound among all convex lower bounds of the rank function on the set $\mathcal{C}$.

For vectors, we have a similar inequality. Let ${card}{(x)}$ denote the cardinality function which counts the number of non-zero entries in the vector $x$. Then we have ${{card}{(x)}} \geq {{\| x\|}_{1}/{\| x\|}_{\infty}}$. Not surprisingly, the $\ell_{1}$ norm is also the convex envelope of the cardinality function over the set $\{{x \in {\mathbb{R}}^{n}}:{{\| x\|}_{\infty} \leq 1}\}$. This result can be either proven directly or can be seen as a special case of the above theorem.

#### Additivity of rank and nuclear norm 

A function $f$ mapping a linear space $\mathcal{S}$ to $\mathbb{R}$ is called *subadditive* if ${f\hspace{0pt}{({x + y})}} \leq {{f\hspace{0pt}{(x)}} + {f\hspace{0pt}{(y)}}}$. It is *additive* if ${f\hspace{0pt}{({x + y})}} = {{f\hspace{0pt}{(x)}} + {f\hspace{0pt}{(y)}}}$. In the case of vectors, both the cardinality function and the $\ell_{1}$ norm are subadditive. That is, if $x$ and $y$ are sparse vectors, then it always holds that the number of non-zeros in $x + y$ is less than or equal to the number of non-zeros in $x$ plus the number of non-zeros of $y$; furthermore (by the triangle inequality) ${\|{x + y}\|}_{1} \leq {{\| x\|}_{1} + {\| y\|}_{1}}$. In particular, the cardinality function is additive exactly when the vectors $x$ and $y$ have disjoint support. In this case, the $\ell_{1}$ norm is also additive, in the sense that ${\|{x + y}\|}_{1} = {{\| x\|}_{1} + {\| y\|}_{1}}$.

For matrices, the rank function is subadditive. For the rank to be additive, it is necessary and sufficient that the row and column spaces of the two matrices intersect only at the origin, since in this case they operate in essentially disjoint spaces (see, e.g., \[36\]). As we will show below, a related condition that ensures that the nuclear norm is additive, is that the matrices $A$ and $B$ have row and column spaces that are *orthogonal*. In fact, a compact sufficient condition for the additivity of the nuclear norm will be that ${A\hspace{0pt}B^{\prime}} = 0$ and ${A^{\prime}\hspace{0pt}B} = 0$. This is a stronger requirement than the aforementioned condition for rank additivity, as orthogonal subspaces only intersect at the origin. The disparity arises because the nuclear norm of a linear map depends on the choice of the inner products on the spaces ${\mathbb{R}}^{m}$ and ${\mathbb{R}}^{n}$ on which the matrix acts, whereas the rank is independent of such a choice.

###### Lemma 2.3 

Let $A$ and $B$ be matrices of the same dimensions. If ${A\hspace{0pt}B^{\prime}} = 0$ and ${A^{\prime}\hspace{0pt}B} = 0$ then ${\|{A + B}\|}_{\ast} = {{\| A\|}_{\ast} + {\| B\|}_{\ast}}$.

Proof    Partition the singular value decompositions of $A$ and $B$ to reflect the zero and non-zero singular vectors

  -- ----------------------------------------------------- --
     $${{A = {\begin{bmatrix}                              
     U_{A\hspace{0pt}1} & U_{A\hspace{0pt}2}               
     \end{bmatrix}\hspace{0pt}\begin{bmatrix}              
     \Sigma_{A} & \\                                       
      & 0                                                  
     \end{bmatrix}\hspace{0pt}\begin{bmatrix}              
     V_{A\hspace{0pt}1} & V_{A\hspace{0pt}2}               
     \end{bmatrix}^{\prime}}}\qquad{B = {\begin{bmatrix}   
     U_{B\hspace{0pt}1} & U_{B\hspace{0pt}2}               
     \end{bmatrix}\hspace{0pt}\begin{bmatrix}              
     \Sigma_{B} & \\                                       
      & 0                                                  
     \end{bmatrix}\hspace{0pt}\begin{bmatrix}              
     V_{B\hspace{0pt}1} & V_{B\hspace{0pt}2}               
     \end{bmatrix}^{\prime}}}}.$$                          
  -- ----------------------------------------------------- --

The condition ${A\hspace{0pt}B^{\prime}} = 0$ implies that ${V_{A\hspace{0pt}1}^{\prime}\hspace{0pt}V_{B\hspace{0pt}1}} = 0$, and similarly, ${A^{\prime}\hspace{0pt}B} = 0$ implies that ${U_{A\hspace{0pt}1}^{\prime}\hspace{0pt}U_{B\hspace{0pt}1}} = 0$. Hence, there exist matrices $U_{C}$ and $V_{C}$ such that $\lbrack{U_{A\hspace{0pt}1}\hspace{0pt}U_{B\hspace{0pt}1}\hspace{0pt}U_{C}}\rbrack$ and $\lbrack{V_{A\hspace{0pt}1}\hspace{0pt}V_{B\hspace{0pt}1}\hspace{0pt}V_{C}}\rbrack$ are orthogonal matrices. Thus, the following are valid singular value decompositions for $A$ and $B$:

  -- ----- ------------------------------------------------- --
     $A$   $= {\begin{bmatrix}                               
           U_{A\hspace{0pt}1} & U_{B\hspace{0pt}1} & U_{C}   
           \end{bmatrix}\hspace{0pt}\begin{bmatrix}          
           \Sigma_{A} & & \\                                 
            & 0 & \\                                         
            & & 0                                            
           \end{bmatrix}\hspace{0pt}\begin{bmatrix}          
           V_{A\hspace{0pt}1} & V_{B\hspace{0pt}1} & V_{C}   
           \end{bmatrix}^{\prime}}$                          
     $B$   ${= {\begin{bmatrix}                              
           U_{A\hspace{0pt}1} & U_{B\hspace{0pt}1} & U_{C}   
           \end{bmatrix}\hspace{0pt}\begin{bmatrix}          
           0 & & \\                                          
            & \Sigma_{B} & \\                                
            & & 0                                            
           \end{bmatrix}\hspace{0pt}\begin{bmatrix}          
           V_{A\hspace{0pt}1} & V_{B\hspace{0pt}1} & V_{C}   
           \end{bmatrix}^{\prime}}}.$                        
  -- ----- ------------------------------------------------- --

In particular, we have that

  -- ------------------------------------------ --
     $${{A + B} = {\begin{bmatrix}              
     U_{A\hspace{0pt}1} & U_{B\hspace{0pt}1}    
     \end{bmatrix}\hspace{0pt}\begin{bmatrix}   
     \Sigma_{A} & \\                            
      & \Sigma_{B}                              
     \end{bmatrix}\hspace{0pt}\begin{bmatrix}   
     V_{A\hspace{0pt}1} & V_{B\hspace{0pt}1}    
     \end{bmatrix}^{\prime}}}.$$                
  -- ------------------------------------------ --

This shows that the singular values of $A + B$ are equal to the union (with repetition) of the singular values of $A$ and $B$. Hence, ${\|{A + B}\|}_{\ast} = {{\| A\|}_{\ast} + {\| B\|}_{\ast}}$ as desired.  

###### Corollary 2.4 

Let $A$ and $B$ be matrices of the same dimensions. If the row and column spaces of $A$ and $B$ are orthogonal, then ${\|{A + B}\|}_{\ast} = {{\| A\|}_{\ast} + {\| B\|}_{\ast}}$.

Proof    It suffices to show that if the row and column spaces of $A$ and $B$ are orthogonal, then ${A\hspace{0pt}B^{\prime}} = 0$ and ${A^{\prime}\hspace{0pt}B} = 0$. But this is immediate: if the columns of $A$ are orthogonal to the columns of $B$, we have ${A^{\prime}\hspace{0pt}B} = 0$. Similarly, orthogonal row spaces imply that ${A\hspace{0pt}B^{\prime}} = 0$ as well.  

#### Nuclear norm minimization 

Let us turn now to the study of equality-constrained norm minimization problems where we are searching for a matrix $X \in {\mathbb{R}}^{m \times n}$ of minimum nuclear norm belonging to a given affine subspace. In our applications, the subspace is usually described by linear equations of the form ${\mathcal{A}\hspace{0pt}{(X)}} = b$, where $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ is a linear mapping. This problem admits the primal-dual convex formulation

  -- ------------------- -------------------------------------- ------------------- --------------------------------------------------------- -- -------
     $\min\limits_{X}$   ${\| X\|}_{\ast}$                      $\max\limits_{z}$   $b^{\prime}\hspace{0pt}z$                                    (2.7)
     s.t                 ${\mathcal{A}\hspace{0pt}{(X)}} = b$   s.t.                ${{\|{\mathcal{A}^{\ast}\hspace{0pt}{(z)}}\|} \leq 1},$      
  -- ------------------- -------------------------------------- ------------------- --------------------------------------------------------- -- -------

where $\mathcal{A}^{\ast}:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}^{m \times n}}$ is the adjoint of $\mathcal{A}$. The formulation (2.7) is valid for any norm minimization problem, by replacing the norms appearing above by any dual pair of norms. In particular, if we replace the nuclear norm with the $\ell_{1}$ norm and the operator norm with the $\ell_{\infty}$ norm, we obtain a primal-dual pair of optimization problems, that can be reformulated in terms of linear programming.

Using the SDP characterizations of the nuclear and operator norms given in (2.5)-(2.6) above allows us to rewrite (2.7) as the primal-dual pair of semidefinite programs

  -- -------------------------------- ------- -------------------------------------- -------------- ------------------- -------------------------------------------------------- -- -------
     $\min\limits_{X,W_{1},W_{2}}$            $\frac{1}{2}{({Tr}{(W_{1})} + {Tr}}$   ${(W_{2})})$   $\max\limits_{z}$   $b^{\prime}\hspace{0pt}z$                                   (2.8)
     s.t.                                     $\begin{bmatrix}                       $\succeq 0$    s.t.                ${\begin{bmatrix}                                           
                                              W_{1} & X \\                                                              I_{m} & {\mathcal{A}^{\ast}\hspace{0pt}{(z)}} \\            
                                              X^{\prime} & W_{2}                                                        {\mathcal{A}^{\ast}\hspace{0pt}{(z)}^{\prime}} & I_{n}      
                                              \end{bmatrix}$                                                            \end{bmatrix} \succeq 0}.$                                  
     $\mathcal{A}\hspace{0pt}{(X)}$   $= b$                                                                                                                                         
  -- -------------------------------- ------- -------------------------------------- -------------- ------------------- -------------------------------------------------------- -- -------

#### Optimality conditions 

In order to describe the optimality conditions for the norm minimization problem (2.7), we must first characterize the subdifferential of the nuclear norm. Recall that for a convex function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, the subdifferential of $f$ at $x \in {\mathbb{R}}^{n}$ is the compact convex set

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\partial{f\hspace{0pt}{(x)}}}:={\{{d \in {\mathbb{R}}^{n}}:{{{f\hspace{0pt}{(y)}} \geq {{f\hspace{0pt}{(x)}} + {\langle d,{y - x}\rangle}}}\mspace{21mu}{{\forall y} \in {\mathbb{R}}^{n}}}\}}}.$$   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

Let $X$ be an $m \times n$ matrix with rank $r$ and let $X = {U\hspace{0pt}\Sigma\hspace{0pt}V^{\prime}}$ be a singular value decomposition where $U \in {\mathbb{R}}^{m \times r}$, $V \in {\mathbb{R}}^{n \times r}$ and $\Sigma$ is an $r \times r$ diagonal matrix. The subdifferential of the nuclear norm at $X$ is then given by (see, e.g., \[55\])

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{\partial{\| X\|}_{\ast}} = {\{{{U\hspace{0pt}V^{\prime}} + W}:{{W\hspace{0pt}\text{~and~}\hspace{0pt}X\hspace{0pt}\text{~have orthogonal row and column spaces, and~}\hspace{0pt}{\| W\|}} \leq 1}\}}}.$$      (2.9)
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

For comparison, recall the case of the $\ell_{1}$ norm, where $T$ denotes the support of the $n$-vector $x$, $T^{c}$ is the complement of $T$ in the set $\{ 1,\ldots,n\}$, and

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${{\partial{\| x\|}_{1}} = {\{{d \in {\mathbb{R}}^{n}}:{{d_{i} = {{{sign}{(x)}}\hspace{0pt}\text{~for~}\hspace{0pt}i} \in T},{{|d_{i}|} \leq {1\hspace{0pt}\text{~for~}\hspace{0pt}i} \in T^{c}}}\}}}.$$      (2.10)
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

The similarity between (2.9) and (2.10) is particularly transparent if we recall the *polar decomposition* of a matrix into a product of orthogonal and positive semidefinite matrices (see, e.g., \[33\]). The "angular" component of the matrix $X$ is exactly given by $U\hspace{0pt}V^{\prime}$. Thus, these subgradients always have the form of an "angle" (or sign), plus possibly a contraction in an orthogonal direction if the norm is not differentiable at the current point.

We can now write concise optimality conditions for the optimization problem (2.7). A matrix $X$ is optimal for (2.7) if there exists a vector $z \in {\mathbb{R}}^{p}$ such that

  -- ------------------------------------------------------------------------------------------------------------------- -- --------
     $${{{\mathcal{A}\hspace{0pt}{(X)}} = b},{{\mathcal{A}^{\ast}\hspace{0pt}{(z)}} \in {\partial{\| X\|}_{\ast}}}}.$$      (2.11)
  -- ------------------------------------------------------------------------------------------------------------------- -- --------

The first condition in (2.11) requires feasibility of the linear equations, and the second one guarantees that there is no feasible direction of improvement. Indeed, since $\mathcal{A}^{\ast}\hspace{0pt}{(z)}$ is in the subdifferential at $X$, for any $Y$ in the primal feasible set of (2.7) we have

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\| Y\|}_{\ast} \geq {{\| X\|}_{\ast} + {\langle{\mathcal{A}^{\ast}\hspace{0pt}{(z)}},{Y - X}\rangle}} = {{\| X\|}_{\ast} + {\langle z,{\mathcal{A}\hspace{0pt}{({Y - X})}}\rangle}} = {\| X\|}_{\ast}},$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

where the last step follows from the feasibility of $X$ and $Y$. As we can see, the optimality conditions (2.11) for the nuclear norm minimization problem exactly parallel those of the $\ell_{1}$ optimization case.

These optimality conditions can be used to check and certify whether a given candidate $X$ is indeed the minimum nuclear norm solution. For this, it is sufficient (and necessary) to find a vector $z \in {\mathbb{R}}^{p}$ in the subdifferential of the norm, i.e., such that the left- and right-singular spaces of $\mathcal{A}^{\ast}\hspace{0pt}{(z)}$ are aligned with those of $X$, and is a contraction in the orthogonal complement.

## 3 Restricted Isometry and Recovery of Low-Rank Matrices 

Let us now turn to the central problem analyzed in this paper. Let $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ be a linear map and let $X_{0}$ be a matrix of rank $r$. Set $b:={\mathcal{A}\hspace{0pt}{(X_{0})}}$, and define the convex optimization problem

  -- ----------------------------------------------------------------------------------------------------------------------- -- -------
     $${{X^{\ast}:={{\arg{\min\limits_{X}{\| X\|}_{\ast}}}\qquad\text{s.t.}}}\quad{{\mathcal{A}\hspace{0pt}{(X)}} = b}}.$$      (3.1)
  -- ----------------------------------------------------------------------------------------------------------------------- -- -------

In this section, we will characterize specific cases when we can *a priori* guarantee that $X^{\ast} = X_{0}$. The key conditions will be determined by the values of a sequence of parameters $\delta_{r}$ that quantify the behavior of the linear map $\mathcal{A}$ when restricted to the subvariety of matrices of rank $r$. The following definition is the natural generalization of the Restricted Isometry Property from vectors to matrices.

###### Definition 3.1 

Let $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$ be a linear map. Without loss of generality, assume $m \leq n$. For every integer $r$ with $1 \leq r \leq m$, define the $r$-restricted isometry constant to be the smallest number $\delta_{r}\hspace{0pt}{(\mathcal{A})}$ such that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- -------
     $${{({1 - {\delta_{r}\hspace{0pt}{(\mathcal{A})}}})}\hspace{0pt}{\| X\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(X)}}\|} \leq {{({1 + {\delta_{r}\hspace{0pt}{(\mathcal{A})}}})}\hspace{0pt}{\| X\|}_{F}}$$      (3.2)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- -------

holds for all matrices $X$ of rank at most $r$.

Note that by definition, ${\delta_{r}\hspace{0pt}{(\mathcal{A})}} \leq {\delta_{r^{\prime}}\hspace{0pt}{(\mathcal{A})}}$ for $r \leq r^{\prime}$.

The Restricted Isometry Property for sparse vectors was developed by Candès and Tao in \[14\], and requires (3.2) to hold with the Euclidean norm replacing the Frobenius norm and rank being replaced by cardinality. Since for diagonal matrices, the Frobenius norm is equal to the Euclidean norm of the diagonal, this definition reduces to the original Restricted Isometry Property of \[14\] in the diagonal case.^11^1In \[14\], the authors define the restricted isometry properties with squared norms. We note here that the analysis is identical modulo some algebraic rescaling of constants. We choose to drop the squares as it greatly simplifies the analysis in Section 4.

Unlike the case of "standard" compressed sensing, our RIP condition for low-rank matrices cannot be interpreted as guaranteeing all sub-matrices of the linear transform $\mathcal{A}$ of a certain size are well conditioned. Indeed, the set of matrices $X$ for which (3.2) must hold is *not* a finite union of subspaces, but rather a certain "generalized Stiefel manifold," which is also an algebraic variety (in fact, it is the $r$th-secant variety of the variety of rank-one matrices). Surprisingly, we are still able to derive analogous recovery results for low-rank solutions of equations when $\mathcal{A}$ obeys this RIP condition. Furthermore, we will see in Section 4 that many ensembles of random matrices have the Restricted Isometry Property with $\delta_{r}$ quite small with high probability for reasonable values of $m$,$n$, and $p$.

The following two recovery theorems will characterize the power of the restricted isometry constants. Both theorems are more or less immediate generalizations from the sparse case to the low-rank case and use only minimal properties of the rank of matrices and the nuclear norm. The first theorem generalizes Lemma 1.3 in \[14\] to low-rank recovery.

###### Theorem 3.2 

Suppose that $\delta_{2\hspace{0pt}r} < 1$ for some integer $r \geq 1$. Then $X_{0}$ is the only matrix of rank at most $r$ satisfying ${\mathcal{A}\hspace{0pt}{(X)}} = b$.

Proof    Assume, on the contrary, that there exists a rank $r$ matrix $X$ satisfying ${\mathcal{A}\hspace{0pt}{(X)}} = b$ and $X \neq X_{0}$. Then $Z:={X_{0} - X}$ is a nonzero matrix of rank at most $2\hspace{0pt}r$, and ${\mathcal{A}\hspace{0pt}{(Z)}} = 0$. But then we would have $0 = {\|{\mathcal{A}\hspace{0pt}{(Z)}}\|} \geq {{({1 - \delta_{2\hspace{0pt}r}})}\hspace{0pt}{\| Z\|}_{F}} > 0$ which is a contradiction.  

The proof of the preceding theorem is identical to the argument given by Candès and Tao and is an immediate consequence of our definition of the constant $\delta_{r}$. No adjustment is necessary in the transition from sparse vectors to low-rank matrices. The key property used is the sub-additivity of the rank.

Next, we state a weak $\ell_{1}$-type recovery theorem whose proof mimics the approach in \[12\], but for which a few details need to be adjusted when switching from vectors to matrices.

###### Theorem 3.3 

Suppose that $r \geq 1$ is such that $\delta_{5\hspace{0pt}r} < {1/10}$. Then $X^{\ast} = X_{0}$.

We will need the following technical lemma that shows for any two matrices $A$ and $B$, we can decompose $B$ as the sum of two matrices $B_{1}$ and $B_{2}$ such that ${rank}{(B_{1})}$ is not too large and $B_{2}$ satisfies the conditions of Lemma 2.3. This will be the key decomposition for proving Theorem 3.3.

###### Lemma 3.4 

Let $A$ and $B$ be matrices of the same dimensions. Then there exist matrices $B_{1}$ and $B_{2}$ such that

1.  [1.]

    $B = {B_{1} + B_{2}}$

2.  [2.]

    ${{rank}{(B_{1})}} \leq {2\hspace{0pt}{{rank}{(A)}}}$

3.  [3.]

    ${A\hspace{0pt}B_{2}^{\prime}} = 0$ and ${A^{\prime}\hspace{0pt}B_{2}} = 0$

4.  [4.]

    ${\langle B_{1},B_{2}\rangle} = 0$

Proof    Consider a full singular value decomposition of $A$

  -- ------------------------------------------ --
     $${A = {U\hspace{0pt}\begin{bmatrix}       
     \Sigma & 0 \\                              
     0 & 0                                      
     \end{bmatrix}\hspace{0pt}V^{\prime}}},$$   
  -- ------------------------------------------ --

and let $\hat{B}:={U^{\prime}\hspace{0pt}B\hspace{0pt}V}$. Partition $\hat{B}$ as

  -- ------------------------------------ --
     $${\hat{B} = \begin{bmatrix}         
     {\hat{B}}_{11} & {\hat{B}}_{12} \\   
     {\hat{B}}_{21} & {\hat{B}}_{22}      
     \end{bmatrix}}.$$                    
  -- ------------------------------------ --

Defining now

  -- ----------------------------------------------------------------------------- --
     $${{B_{1}:={U\hspace{0pt}\begin{bmatrix}                                      
     {\hat{B}}_{11} & {\hat{B}}_{12} \\                                            
     {\hat{B}}_{21} & 0                                                            
     \end{bmatrix}\hspace{0pt}V^{\prime}}},{B_{2}:={U\hspace{0pt}\begin{bmatrix}   
     0 & 0 \\                                                                      
     0 & {\hat{B}}_{22}                                                            
     \end{bmatrix}\hspace{0pt}V^{\prime}}}},$$                                     
  -- ----------------------------------------------------------------------------- --

it can be easily verified that $B_{1}$ and $B_{2}$ satisfy the conditions (1)--(4).  

We now proceed to a proof of Theorem 3.3.

Proof   \of Theorem [3.3\] By optimality of $X^{\ast}$, we have ${\| X_{0}\|}_{\ast} \geq {\| X^{\ast}\|}_{\ast}$. Let $R:={X^{\ast} - X_{0}}$. Applying Lemma 3.4 to the matrices $X_{0}$ and $R$, there exist matrices $R_{0}$ and $R_{c}$ such that $R = {R_{0} + R_{c}}$, ${{rank}{(R_{0})}} \leq {2\hspace{0pt}{{rank}{(X_{0})}}}$, and ${X_{0}\hspace{0pt}R_{c}^{\prime}} = 0$ and ${X_{0}^{\prime}\hspace{0pt}R_{c}} = 0$. Then,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $$\begin{array}{r}                                                                                                                                                                          (3.3)
     {{{\| X_{0}\|}_{\ast} \geq {\|{X_{0} + R}\|}_{\ast} \geq {{\|{X_{0} + R_{c}}\|}_{\ast} - {\| R_{0}\|}_{\ast}} = {{{\| X_{0}\|}_{\ast} + {\| R_{c}\|}_{\ast}} - {\| R_{0}\|}_{\ast}}},}      
     \end{array}$$                                                                                                                                                                               
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

where the middle assertion follows from the triangle inequality and the last one from Lemma 2.3. Rearranging terms, we can conclude that

  -- ----------------------------------------------------- -- -------
     $${{\| R_{0}\|}_{\ast} \geq {\| R_{c}\|}_{\ast}}.$$      (3.4)
  -- ----------------------------------------------------- -- -------

Next we partition $R_{c}$ into a sum of matrices $R_{1},R_{2},\ldots$, each of rank at most $3\hspace{0pt}r$. Let $R_{c} = {U\hspace{0pt}{{diag}{(\sigma)}}\hspace{0pt}V^{\prime}}$ be the singular value decomposition of $R_{c}$. For each $i \geq 1$ define the index set $I_{i} = {\{{{3\hspace{0pt}r\hspace{0pt}{({i - 1})}} + 1},\ldots,{3\hspace{0pt}r\hspace{0pt}i}\}}$, and let $R_{i}:={U_{I_{i}}\hspace{0pt}{{diag}{(\sigma_{I_{i}})}}\hspace{0pt}V_{I_{i}}^{\prime}}$ (notice that ${\langle R_{i},R_{j}\rangle} = 0$ if $i \neq j$). By construction, we have

  -- ---------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{\sigma_{k} \leq {\frac{1}{3\hspace{0pt}r}\hspace{0pt}{\sum\limits_{j \in I_{i}}\sigma_{j}}}}\mspace{39mu}{{\forall k} \in I_{i + 1}}},$$      (3.5)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------- -- -------

which implies ${\| R_{i + 1}\|}_{F}^{2} \leq {\frac{1}{3\hspace{0pt}r}\hspace{0pt}{\| R_{i}\|}_{\ast}^{2}}$. We can then compute the following bound

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{\sum\limits_{j \geq 2}{\| R_{j}\|}_{F}} \leq {\frac{1}{\sqrt{3\hspace{0pt}r}}\hspace{0pt}{\sum\limits_{j \geq 1}{\| R_{j}\|}_{\ast}}} = {\frac{1}{\sqrt{3\hspace{0pt}r}}\hspace{0pt}{\| R_{c}\|}_{\ast}} \leq {\frac{1}{\sqrt{3\hspace{0pt}r}}\hspace{0pt}{\| R_{0}\|}_{\ast}} \leq {\frac{\sqrt{2\hspace{0pt}r}}{\sqrt{3\hspace{0pt}r}}\hspace{0pt}{\| R_{0}\|}_{F}}},$$      (3.6)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

where the last inequality follows from (2.1) and the fact that ${{rank}{(R_{0})}} \leq {2\hspace{0pt}r}$. Finally, note that the rank of $R_{0} + R_{1}$ is at most $5\hspace{0pt}r$, so we may put this all together as

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $$\begin{array}{cl}                                                                                                                                                                    (3.7)
     {\|{\mathcal{A}\hspace{0pt}{(R)}}\|} & {\geq {{\|{\mathcal{A}\hspace{0pt}{({R_{0} + R_{1}})}}\|} - {\sum\limits_{j \geq 2}{\|{\mathcal{A}\hspace{0pt}{(R_{j})}}\|}}}} \\               
      & {\geq {{{({1 - \delta_{5\hspace{0pt}r}})}\hspace{0pt}{\|{R_{0} + R_{1}}\|}_{F}} - {{({1 + \delta_{3\hspace{0pt}r}})}\hspace{0pt}{\sum\limits_{j \geq 2}{\| R_{j}\|}_{F}}}}} \\      
      & {\geq {\left( {{({1 - \delta_{5\hspace{0pt}r}})} - {\sqrt{\frac{2}{3}}\hspace{0pt}{({1 + \delta_{3\hspace{0pt}r}})}}} \right)\hspace{0pt}{\| R_{0}\|}_{F}}} \\                      
      & {{\geq {\left( {{({1 - \delta_{5\hspace{0pt}r}})} - {\frac{9}{11}\hspace{0pt}{({1 + \delta_{3\hspace{0pt}r}})}}} \right)\hspace{0pt}{\| R_{0}\|}_{F}}}.}                            
     \end{array}$$                                                                                                                                                                          
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

By assumption ${\mathcal{A}\hspace{0pt}{(R)}} = {\mathcal{A}\hspace{0pt}{({X^{\ast} - X_{0}})}} = 0$, so if the factor on the right-hand side is strictly positive, $R_{0} = 0$, which further implies $R_{c} = 0$ by (3.4), and thus $X^{\ast} = X_{0}$. Simple algebra reveals that the right-hand side is positive when ${{9\hspace{0pt}\delta_{3\hspace{0pt}r}} + {11\hspace{0pt}\delta_{5\hspace{0pt}r}}} < 2$. Since $\delta_{3\hspace{0pt}r} \leq \delta_{5\hspace{0pt}r}$, we immediately have that $X^{\ast} = X_{0}$ if $\delta_{5\hspace{0pt}r} < {1/10}$.  

The rational number ($9/11$) in the proof of the theorem is chosen for notational simplicity and is clearly not optimal. A slightly tighter bound can be achieved working directly with the second to last line in (3.7). The most important point is that our recovery condition on $\delta_{5\hspace{0pt}r}$ is an absolute constant, independent of $m$, $n$, $r$, and $p$.

We have yet to demonstrate any specific linear mappings $\mathcal{A}$ for which $\delta_{r} < 1$. We shall show in the next section that linear transformations sampled from several families of random matrices with appropriately chosen dimensions have this property with overwhelming probability. The analysis is again similar to the compressive sampling literature, but several details specific to the rank recovery problem need to be employed.

## 4 Nearly Isometric Families 

In this section, we will demonstrate that when we sample linear maps from a class of probability distributions obeying certain tail bounds, then they will obey the Restricted Isometry Property (3.2) as $p$, $m$, and $n$ tend to infinity at appropriate rates. The following definition characterizes this family of random linear transformation.

###### Definition 4.1 

Let $\mathcal{A}$ be a random variable that takes values in linear maps from ${\mathbb{R}}^{m \times n}$ to ${\mathbb{R}}^{p}$. We say that $\mathcal{A}$ is *nearly isometrically distributed* if for all $X \in {\mathbb{R}}^{m \times n}$

  -- --------------------------------------------------------------------------------------------------------- -- -------
     $${\mathbf{E}\hspace{0pt}{\lbrack{\|{\mathcal{A}\hspace{0pt}{(X)}}\|}^{2}\rbrack}} = {\| X\|}_{F}^{2}$$      (4.1)
  -- --------------------------------------------------------------------------------------------------------- -- -------

and for all $0 < \epsilon < 1$ we have,

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${\mathbf{P}\hspace{0pt}{({{|{{\|{\mathcal{A}\hspace{0pt}{(X)}}\|}^{2} - {\| X\|}_{F}^{2}}|} \geq {\epsilon\hspace{0pt}{\| X\|}_{F}^{2}}})}} \leq {2\hspace{0pt}{\exp\left( {- {\frac{p}{2}\hspace{0pt}{({{\epsilon^{2}/2} - {\epsilon^{3}/3}})}}} \right)}}$$      (4.2)
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

and for all $t > 0$, we have

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${\mathbf{P}\hspace{0pt}\left( {{\|\mathcal{A}\|} \geq {1 + \sqrt{\frac{m\hspace{0pt}n}{p}} + t}} \right)} \leq {\exp{({- {\gamma\hspace{0pt}p\hspace{0pt}t^{2}}})}}$$      (4.3)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

for some constant $\gamma > 0$.

There are two ingredients for a random linear map to be nearly isometric. First, it must be isometric in expectation. Second, the probability of large distortions of length must be exponentially small. The exponential bound in (4.2) guarantees union bounds will be small even for rather large sets. This concentration is the typical ingredient required to prove the Johnson-Lindenstrauss Lemma (cf \[2, 15\]).

The majority of nearly isometric random maps are described in terms of random matrices. For a linear map $\mathcal{A}:{{\mathbb{R}}^{m \times n}\rightarrow{\mathbb{R}}^{p}}$, we can always write its matrix representation as

  -- ------------------------------------------------------------------------------ -- -------
     $${{\mathcal{A}\hspace{0pt}{(X)}} = {\mathbf{A}\hspace{0pt}{{vec}{(X)}}}},$$      (4.4)
  -- ------------------------------------------------------------------------------ -- -------

where ${vec}{(X)}$ denotes the vector of $X$ with its columns stacked in order on top of one another, and $\mathbf{A}$ is a ${p \times m}\hspace{0pt}n$ matrix. We now give several examples of nearly isometric random variables in this matrix representation. The most well known is the ensemble with independent, identically distributed (i.i.d.) Gaussian entries \[15\]

  -- --------------------------------------------------------------------------- -- -------
     $${A_{i\hspace{0pt}j} \sim {\mathcal{N}\hspace{0pt}{(0,\frac{1}{p})}}}.$$      (4.5)
  -- --------------------------------------------------------------------------- -- -------

We also mention the two following ensembles of matrices, described in \[2\]. One has entries sampled from an i.i.d. symmetric Bernoulli distribution

  -- ---------------------------------------------------------------------------- -- -------
     $${A_{i\hspace{0pt}j} = \begin{cases}                                           (4.6)
     \sqrt{\frac{1}{p}} & {\text{with probability~}\hspace{0pt}\frac{1}{2}} \\       
     {- \sqrt{\frac{1}{p}}} & {\text{with probability~}\hspace{0pt}\frac{1}{2}}      
     \end{cases}},$$                                                                 
  -- ---------------------------------------------------------------------------- -- -------

and the other has zeros in two-thirds of the entries

  -- ---------------------------------------------------------------------------- -- -------
     $${A_{i\hspace{0pt}j} = \begin{cases}                                           (4.7)
     \sqrt{\frac{3}{p}} & {\text{with probability~}\hspace{0pt}\frac{1}{6}} \\       
     0 & {\text{with probability~}\hspace{0pt}\frac{2}{3}} \\                        
     {- \sqrt{\frac{3}{p}}} & {\text{with probability~}\hspace{0pt}\frac{1}{6}}      
     \end{cases}}.$$                                                                 
  -- ---------------------------------------------------------------------------- -- -------

The fact that the top singular value of the matrix $\mathbf{A}$ is concentrated around $1 + \sqrt{D/p}$ for all of these ensembles follows from the work of Yin, Bai, and Krishnaiah, who showed that whenever the entries $A_{i\hspace{0pt}j}$ are i.i.d. with zero mean and finite fourth moment, then the maximum singular value of $\mathbf{A}$ is almost surely $1 + \sqrt{D/p}$ for $D$ sufficiently large \[56\]. El Karoui uses this result to prove the concentration inequality (4.3) for all such distributions \[23\]. The result for Gaussians is rather tight with $\gamma = {1/2}$ (see, e.g., \[16\]).

Finally, note that a random projection also obeys all of the necessary concentration inequalities. Indeed, since the norm of a random projection is exactly $\sqrt{D/p}$, (4.3) holds trivially. The concentration inequality (4.2) is proven in \[15\].

The main result of this section is the following:

###### Theorem 4.2 

Fix $0 < \delta < 1$. If $\mathcal{A}$ is a nearly isometric random variable, then for every $1 \leq r \leq m$, there exist constants ${c_{0},c_{1}} > 0$ depending only on $\delta$ such that, with probability at least $1 - {\exp{({- {c_{1}\hspace{0pt}p}})}}$, ${\delta_{r}\hspace{0pt}{(\mathcal{A})}} \leq \delta$ whenever $p \geq {c_{0}\hspace{0pt}r\hspace{0pt}{({m + n})}\hspace{0pt}{\log{({m\hspace{0pt}n})}}}$.

The proof will make use of standard techniques in concentration of measure. We first extend the concentration results of \[4\] to subspaces of matrices. We will show that the distortion of a subspace by a linear map is robust to perturbations of the subspace. Finally, we will provide an epsilon net over the set of all subspaces and, using a union bound, will show that with overwhelming probability, nearly isometric random variables will obey the Restricted Isometry Property (3.2) as the size of the matrices tend to infinity.

The following lemma characterizes the behavior of a nearly isometric random mapping $\mathcal{A}$ when restricted to an arbitrary subspace of matrices $U$ of dimension $d$.

###### Lemma 4.3 

Let $\mathcal{A}$ be a nearly isometric linear map and let $U$ be an arbitrary subspace of $m \times n$ matrices with $d = {\dim{(U)}} \leq p$. Then for any $0 < \delta < 1$ we have

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{{({1 - \delta})}\hspace{0pt}{\| X\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(X)}}\|} \leq {{({1 + \delta})}\hspace{0pt}{\| X\|}_{F}}}\mspace{39mu}{{\forall X} \in U}$$      (4.8)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

with probability at least

  -- --------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${1 - {2\hspace{0pt}{({12/\delta})}^{d}\hspace{0pt}{\exp\left( {- {\frac{p}{2}\hspace{0pt}{({{\delta^{2}/8} - {\delta^{3}/24}})}}} \right)}}}.$$      (4.9)
  -- --------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

Proof    The proof of this theorem is identical to the argument in \[4\] where the authors restricted their attention to subspaces aligned with the coordinate axes. We will sketch the proof here as the argument is straightforward.

There exists a finite set $\Omega$ of at most ${({12/\delta})}^{d}$ points such that for every $X \in U$ with ${\| X\|}_{F} \leq 1$, there exists a $Q \in \Omega$ such that ${\|{X - Q}\|}_{F} \leq {\delta/4}$. By the standard union bound, the concentration inequality (4.2) holds for all $Q \in \Omega$ with $\epsilon = {\delta/2}$ with probability at least (4.9). If (4.2) holds for all $Q \in \Omega$, then we immediately have that ${{({1 - {\delta/2}})}\hspace{0pt}{\| Q\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(Q)}}\|} \leq {{({1 + {\delta/2}})}\hspace{0pt}{\| Q\|}_{F}}$ for all $Q \in \Omega$ as well.

Let $X$ be in $\{{X \in U}:{{\| X\|}_{F} \leq 1}\}$, and $M$ be the maximum of $\|{\mathcal{A}\hspace{0pt}{(X)}}\|$ on this set. Then there exists a $Q \in \Omega$ such that ${\|{X - Q}\|}_{F} \leq {\delta/4}$. We then have

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\|{\mathcal{A}\hspace{0pt}{(X)}}\|} \leq {{\|{\mathcal{A}\hspace{0pt}{(Q)}}\|} + {\|{\mathcal{A}\hspace{0pt}{({X - Q})}}\|}} \leq {1 + {\delta/2} + {{M\hspace{0pt}\delta}/4}}},$$   
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

and since $M \leq {1 + {\delta/2} + {{M\hspace{0pt}\delta}/4}}$ by definition, we have $M \leq {1 + \delta}$. The lower bound is proven by the following chain of inequalities

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     $${{\|{\mathcal{A}\hspace{0pt}{(X)}}\|} \geq {{\|{\mathcal{A}\hspace{0pt}{(Q)}}\|} - {\|{\mathcal{A}\hspace{0pt}{({X - Q})}}\|}} \geq {1 - {\delta/2} - {{{({1 + \delta})}\hspace{0pt}\delta}/4}} \geq {1 - \delta}}.$$   
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

 

The proof of preceding lemma revealed that the near isometry of a linear map is robust to small perturbations of the matrix on which the map is acting. We will now show that this behavior is robust with respect to small perturbations of the subspace $U$ as well. This perturbation will be measured in the natural distance between two subspaces

  -- ------------------------------------------------------------------------- -- --------
     $${{\rho\hspace{0pt}{(T_{1},T_{2})}}:={\|{P_{T_{1}} - P_{T_{2}}}\|}},$$      (4.10)
  -- ------------------------------------------------------------------------- -- --------

where $T_{1}$ and $T_{2}$ are subspaces and $P_{T_{i}}$ is the orthogonal projection associated with each subspace. This distance measures the operator norm of the difference between the corresponding projections, and is equal to the sine of the largest principal angle between $T_{1}$ and $T_{2}$ \[1\].

The set of all $d$-dimensional subspaces of ${\mathbb{R}}^{D}$ is commonly known as the Grassmannian manifold ${\mathfrak{G}}\hspace{0pt}{(D,d)}$. We will endow it with the metric $\rho\hspace{0pt}{( \cdot , \cdot )}$ given by (4.10), also known as the *projection 2-norm*. In the following lemma we characterize and quantify the change in the isometry constant $\delta$ as one smoothly moves through the Grassmannian.

###### Lemma 4.4 

Let $U_{1}$ and $U_{2}$ be $d$-dimensional subspaces of ${\mathbb{R}}^{D}$. Suppose that for all $X \in U_{1}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------ -- --------
     $${{({1 - \delta})}\hspace{0pt}{\| X\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(X)}}\|} \leq {{({1 + \delta})}\hspace{0pt}{\| X\|}_{F}}$$      (4.11)
  -- ------------------------------------------------------------------------------------------------------------------------------------------ -- --------

for some constant $0 < \delta < 1$. Then for all $Y \in U_{2}$

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------
     $${{({1 - \delta^{\prime}})}\hspace{0pt}{\| Y\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(Y)}}\|} \leq {{({1 + \delta^{\prime}})}\hspace{0pt}{\| Y\|}_{F}}$$      (4.12)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------

with

  -- ----------------------------------------------------------------------------------------------------------- -- --------
     $${\delta^{\prime} = {\delta + {{{({1 + {\|\mathcal{A}\|}})} \cdot \rho}\hspace{0pt}{(U_{1},U_{2})}}}}.$$      (4.13)
  -- ----------------------------------------------------------------------------------------------------------- -- --------

Proof    Consider any $Y \in U_{2}$. Then

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$\begin{array}{cl}                                                                                                                                                                                                    (4.14)
     {\|{\mathcal{A}\hspace{0pt}{(Y)}}\|} & {= \left\| {\mathcal{A}\hspace{0pt}\left( {{P_{U_{1}}\hspace{0pt}{(Y)}} - {{\lbrack{P_{U_{1}} - P_{U_{2}}}\rbrack}\hspace{0pt}{(Y)}}} \right)} \right\|} \\                     
      & {\leq {\left\| {\mathcal{A}\hspace{0pt}{({P_{U_{1}}\hspace{0pt}{(Y)}})}}\| \right. + \left. \|{\mathcal{A}\hspace{0pt}\left( {{\lbrack{P_{U_{1}} - P_{U_{2}}}\rbrack}\hspace{0pt}{(Y)}} \right)} \right\|}} \\      
      & {\leq {{{({1 + \delta})}\hspace{0pt}{\|{P_{U_{1}}\hspace{0pt}{(Y)}}\|}_{F}} + {{\|\mathcal{A}\|}\hspace{0pt}{\|{P_{U_{1}} - P_{U_{2}}}\|}\hspace{0pt}{\| Y\|}_{F}}}} \\                                             
      & {{\leq {\left( {1 + \delta + {{\|\mathcal{A}\|}\hspace{0pt}{\|{P_{U_{1}} - P_{U_{2}}}\|}}} \right)\hspace{0pt}{\| Y\|}_{F}}}.}                                                                                      
     \end{array}$$                                                                                                                                                                                                          
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

Similarly, we have

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$\begin{array}{cl}                                                                                                                                                                                                                                        (4.15)
     {\|{\mathcal{A}\hspace{0pt}{(Y)}}\|} & {\geq {\left\| {\mathcal{A}\hspace{0pt}{({P_{U_{1}}\hspace{0pt}{(Y)}})}}\| \right. - \left. \|{\mathcal{A}\hspace{0pt}\left( {{\lbrack{P_{U_{1}} - P_{U_{2}}}\rbrack}\hspace{0pt}{(Y)}} \right)} \right\|}} \\      
      & {\geq {{{({1 - \delta})}\hspace{0pt}{\|{P_{U_{1}}\hspace{0pt}{(Y)}}\|}_{F}} - {{\|\mathcal{A}\|}\hspace{0pt}{\|{P_{U_{1}} - P_{U_{2}}}\|}\hspace{0pt}{\| Y\|}_{F}}}} \\                                                                                 
      & {\geq {{{({1 - \delta})}\hspace{0pt}{\| Y\|}_{F}} - {{({1 - \delta})}\hspace{0pt}{\|{{({P_{U_{1}} - P_{U_{2}}})}\hspace{0pt}{(Y)}}\|}_{F}} - {{\|\mathcal{A}\|}\hspace{0pt}{\|{P_{U_{1}} - P_{U_{2}}}\|}\hspace{0pt}{\| Y\|}_{F}}}} \\                  
      & {{\geq {\left\lbrack {1 - \delta - {{({{\|\mathcal{A}\|} + 1})}\hspace{0pt}{\|{P_{U_{1}} - P_{U_{2}}}\|}}} \right\rbrack\hspace{0pt}{\| Y\|}_{F}}},}                                                                                                    
     \end{array}$$                                                                                                                                                                                                                                              
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

which completes the proof.  

To apply these concentration results to low-rank matrices, we characterize the set of all matrices of rank at most $r$ as a union of subspaces. Let $V \subset {\mathbb{R}}^{m}$ and $W \subset {\mathbb{R}}^{n}$ be fixed subspaces of dimension $r$. Then the set of all $m \times n$ matrices $X$ whose row space is contained in $W$ and column space is contained in $V$ forms an $r^{2}$-dimensional subspace of matrices of rank less than or equal to $r$. Denote this subspace as ${\Sigma\hspace{0pt}{(V,W)}} \subset {\mathbb{R}}^{m \times n}$. Any matrix of rank less than or equal to $r$ is an element of some $\Sigma\hspace{0pt}{(V,W)}$ for a suitable pair of subspaces, i.e., the set

  -- --------------------------------------------------------------------------------------------------------------------------------------------------- --
     $$\Sigma_{m\hspace{0pt}n\hspace{0pt}r}:={\{\Sigma{(V,W)}\mspace{23mu}:\mspace{23mu} V \in {\mathfrak{G}}{(m,r)},W \in {\mathfrak{G}}{(n,r)}\}}.$$   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------- --

We now characterize how many subspaces are necessary to cover this set to arbitrary resolution. The *covering number* ${\mathfrak{N}}\hspace{0pt}{(\epsilon)}$ of $\Sigma_{m\hspace{0pt}n\hspace{0pt}r}$ at resolution $\epsilon$ is defined to be the smallest number of subspaces $(V_{i},W_{i})$ such that for any pair of subspaces $(V,W)$, there is an $i$ with ${\rho\hspace{0pt}{({\Sigma\hspace{0pt}{(V,W)}},{\Sigma\hspace{0pt}{(V_{i},W_{i})}})}} \leq \epsilon$. That is, the covering number is the smallest cardinality of an $\epsilon$-net. The following Lemma characterizes the cardinality of such a set.

###### Lemma 4.5 

The covering number ${\mathfrak{N}}\hspace{0pt}{(\epsilon)}$ of $\Sigma_{m\hspace{0pt}n\hspace{0pt}r}$ is bounded above by

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------
     $${{\mathfrak{N}}\hspace{0pt}{(\epsilon)}} \leq \left( \frac{2\hspace{0pt}C_{0}}{\epsilon} \right)^{r\hspace{0pt}{({{m + n} - {2\hspace{0pt}r}})}}$$      (4.16)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------

where $C_{0}$ is a constant independent of $\epsilon$, $m$, $n$, and $r$.

Proof    Note that the projection operator onto $\Sigma\hspace{0pt}{(V,W)}$ can be written as $P_{\Sigma\hspace{0pt}{(V,W)}} = {P_{V} \otimes P_{W}}$, so for a pair of subspaces $(V_{1},W_{1})$ and $(V_{2},W_{2})$, we have

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$\begin{array}{cl}                                                                                                                                                                               (4.17)
     {\rho\hspace{0pt}{({\Sigma\hspace{0pt}{(V_{1},W_{1})}},{\Sigma\hspace{0pt}{(V_{2},W_{2})}})}} & {= {\|{P_{\Sigma\hspace{0pt}{(V_{1},W_{1})}} - P_{\Sigma\hspace{0pt}{(V_{2},W_{2})}}}\|}} \\      
      & {= {\|{{P_{V_{1}} \otimes P_{W_{1}}} - {P_{V_{2}} \otimes P_{W_{2}}}}\|}} \\                                                                                                                   
      & {= {\|{{{({P_{V_{1}} - P_{V_{2}}})} \otimes P_{W_{1}}} + {P_{V_{2}} \otimes {({P_{W_{1}} - P_{W_{2}}})}}}\|}} \\                                                                               
      & {\leq {{{\|{P_{V_{1}} - P_{V_{2}}}\|}\hspace{0pt}{\| P_{W_{1}}\|}} + {{\| P_{V_{2}}\|}\hspace{0pt}{\|{P_{W_{1}} - P_{W_{2}}}\|}}}} \\                                                          
      & {{= {{\rho\hspace{0pt}{(V_{1},V_{2})}} + {\rho\hspace{0pt}{(W_{1},W_{2})}}}}.}                                                                                                                 
     \end{array}$$                                                                                                                                                                                     
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

The conditions ${\rho\hspace{0pt}{(V_{1},V_{2})}} \leq \frac{\epsilon}{2}$ and ${\rho\hspace{0pt}{(W_{1},W_{2})}} \leq \frac{\epsilon}{2}$ together imply that ${\rho\hspace{0pt}{({\Sigma\hspace{0pt}{(V_{1},W_{1})}},{\Sigma\hspace{0pt}{(V_{2},W_{2})}})}} \leq {{\rho\hspace{0pt}{(V_{1},V_{2})}} + {\rho\hspace{0pt}{(W_{1},W_{2})}}} \leq \epsilon$. Let $V_{1},\ldots,V_{N_{1}}$ cover the set of $r$-dimensional subspaces of ${\mathbb{R}}^{m}$ to resolution $\epsilon/2$ and $U_{1},\ldots,U_{N_{2}}$ cover the $r$-dimensional subspaces of ${\mathbb{R}}^{n}$ to resolution $\epsilon/2$. Then for any $(V,W)$, there exist $i$ and $j$ such that ${\rho\hspace{0pt}{(V,V_{i})}} \leq {\epsilon/2}$ and ${\rho\hspace{0pt}{(W,W_{j})}} \leq {\epsilon/2}$. Therefore, ${{\mathfrak{N}}\hspace{0pt}{(\epsilon)}} \leq {N_{1}\hspace{0pt}N_{2}}$. By the work of Szarek on $\epsilon$-nets of the Grassmannian (\[49\], \[50, Th. 8\]) there is a universal constant $C_{0}$, independent of $m$, $n$, and $r$, such that

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------
     $${N_{1} \leq {\left( \frac{2\hspace{0pt}C_{0}}{\epsilon} \right)^{r\hspace{0pt}{({m - r})}}\qquad\text{and}}}\qquad{N_{2} \leq \left( \frac{2\hspace{0pt}C_{0}}{\epsilon} \right)^{r\hspace{0pt}{({n - r})}}}$$      (4.18)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------

which completes the proof.  

The exact value of the universal constant $C_{0}$ is not provided by Szarek in \[50\]. It takes the same value for any homogeneous space whose automorphism group is a subgroup of the orthogonal group, and is independent of the dimension of the homogeneous space. Hence, one might expect this constant to be quite large. However, it is known that for the sphere $C_{0} \leq 3$ \[35\], and there is no indication that this constant is not similarly small for the Grassmannian.

We now proceed to the proof of the main result in this section. For this, we use a union bound to combine the probabilistic guarantees of Lemma 4.3 with the estimates of the covering number of $\Sigma\hspace{0pt}{(U,V)}$.

Proof   \of Theorem [4.2\]

Let $\Omega = {\{{(V_{i},W_{i})}\}}$ be a finite set of subspaces that satisfies the conditions of Lemma 4.5 for $\epsilon > 0$, so ${|\Omega|} \leq {{\mathfrak{N}}\hspace{0pt}{(\epsilon)}}$. For each pair $(V_{i},W_{i})$, define the set of matrices

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${\mathcal{B}_{i}:=\left\{ X \middle| {{\exists{{(V,W)}\hspace{0pt}\text{such that}\hspace{0pt}X}} \in {\Sigma\hspace{0pt}{(V,W)}\hspace{0pt}\text{and}\hspace{0pt}\rho\hspace{0pt}{({\Sigma\hspace{0pt}{(V,W)}},{\Sigma\hspace{0pt}{(V_{i},W_{i})}})}} \leq \epsilon} \right\}}.$$      (4.19)
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

Since $\Omega$ is an $\epsilon$-net, we have that the union of all the $\mathcal{B}_{i}$ is equal to $\Sigma_{m\hspace{0pt}n\hspace{0pt}r}$. Therefore, if for all $i$, ${{({1 - \delta})}\hspace{0pt}{\| X\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(X)}}\|} \leq {{({1 + \delta})}\hspace{0pt}{\| X\|}_{F}}$ for all $X \in \mathcal{B}_{i}$, we must have that ${\delta_{r}\hspace{0pt}{(\mathcal{A})}} \leq \delta$ proving that

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$\begin{array}{cl}                                                                                                                                                                                                                                                                                                        (4.20)
     {\mathbf{P}\hspace{0pt}{({{\delta_{r}\hspace{0pt}{(\mathcal{A})}} \leq \delta})}} & {= \mathbf{P}\left\lbrack {(1 - \delta)} \parallel X \parallel_{F} \leq \parallel \mathcal{A}{(X)} \parallel \leq {(1 + \delta)} \parallel X \parallel_{F}\mspace{24mu}\forall X\text{~s.t.~}{rank}{(X)} \leq r \right\rbrack} \\      
      & {\geq \mathbf{P}\left\lbrack \forall i{(1 - \delta)} \parallel X \parallel_{F} \leq \parallel \mathcal{A}{(X)} \parallel \leq {(1 + \delta)} \parallel X \parallel_{F}\mspace{24mu}\forall X \in \mathcal{B}_{i} \right\rbrack}                                                                                         
     \end{array}$$                                                                                                                                                                                                                                                                                                              
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

Now note that if we have ${{({1 + {\|\mathcal{A}\|}})}\hspace{0pt}\epsilon} \leq {\delta/2}$ and, for all $Y \in {\Sigma\hspace{0pt}{(V_{i},W_{i})}}$, ${{({1 - {\delta/2}})}\hspace{0pt}{\| Y\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(Y)}}\|} \leq {{({1 + {\delta/2}})}\hspace{0pt}{\| Y\|}_{F}}$, Lemma 4.3 implies that ${{({1 - \delta})}\hspace{0pt}{\| X\|}_{F}} \leq {\|{\mathcal{A}\hspace{0pt}{(X)}}\|} \leq {{({1 + \delta})}\hspace{0pt}{\| X\|}_{F}}$ for all $X \in \mathcal{B}_{i}$. Therefore, using a union bound, (4.20) is greater than or equal to

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$\begin{array}{cl}                                                                                                                                                                                                                                                                                                                                                                                   (4.21)
     1 & {- {\sum\limits_{i = 1}^{|\Omega|}{\mathbf{P}\hspace{0pt}\left\lbrack {{{\exists Y} \in {{\Sigma\hspace{0pt}{(V_{i},W_{i})}}\quad{{{\|{\mathcal{A}\hspace{0pt}{(Y)}}\|}\hspace{0pt}{<{({1 - \frac{\delta}{2}})}\parallel}\hspace{0pt}Y}\parallel}_{F}\quad\text{or}}}\quad{{\|{\mathcal{A}\hspace{0pt}{(Y)}}\|} > {{({1 + \frac{\delta}{2}})}\hspace{0pt}{\| Y\|}_{F}}}} \right\rbrack}}} \\      
      & {{- {\mathbf{P}\hspace{0pt}\left\lbrack {{\|\mathcal{A}\|} \geq {\frac{\delta}{2\hspace{0pt}\epsilon} - 1}} \right\rbrack}}.}                                                                                                                                                                                                                                                                      
     \end{array}$$                                                                                                                                                                                                                                                                                                                                                                                         
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

We can bound these quantities separately. First we have by Lemmas 4.3 and 4.5

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$\begin{array}{cl}                                                                                                                                                                                                                                                                                                                                                                (4.22)
     {\sum\limits_{i = 1}^{|\Omega|}\mathbf{P}} & \left\lbrack {{{\exists Y} \in {{\Sigma\hspace{0pt}{(V_{i},W_{i})}}\quad{{{\|{\mathcal{A}\hspace{0pt}{(Y)}}\|}\hspace{0pt}{<{({1 - \frac{\delta}{2}})}\parallel}\hspace{0pt}Y}\parallel}_{F}\quad\text{or}}}\quad{{\|{\mathcal{A}\hspace{0pt}{(Y)}}\|} > {{({1 + \frac{\delta}{2}})}\hspace{0pt}{\| Y\|}_{F}}}} \right\rbrack \\      
      & {\leq {2\hspace{0pt}{\mathfrak{N}}\hspace{0pt}{(\epsilon)}\hspace{0pt}\left( \frac{24}{\delta} \right)^{r^{2}}\hspace{0pt}{\exp\left( {- {\frac{p}{2}\hspace{0pt}{({{\delta^{2}/32} - {\delta^{3}/96}})}}} \right)}}} \\                                                                                                                                                        
      & {{\leq {2\hspace{0pt}\left( \frac{2\hspace{0pt}C_{0}}{\epsilon} \right)^{r\hspace{0pt}{({{m + n} - {2\hspace{0pt}r}})}}\hspace{0pt}\left( \frac{24}{\delta} \right)^{r^{2}}\hspace{0pt}{\exp\left( {- {\frac{p}{2}\hspace{0pt}{({{\delta^{2}/32} - {\delta^{3}/96}})}}} \right)}}}.}                                                                                            
     \end{array}$$                                                                                                                                                                                                                                                                                                                                                                      
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

Secondly, since $\mathcal{A}$ is nearly isometric, there exists a constant $\gamma$ such that

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${{\mathbf{P}\hspace{0pt}\left( {{\|\mathcal{A}\|} \geq {1 + \sqrt{\frac{m\hspace{0pt}n}{p}} + t}} \right)} \leq {\exp{({- {\gamma\hspace{0pt}p\hspace{0pt}t^{2}}})}}}.$$      (4.23)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

In particular,

  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${{\mathbf{P}\hspace{0pt}\left( {{\|\mathcal{A}\|} \geq {\frac{\delta}{2\hspace{0pt}\epsilon} - 1}} \right)} \leq {\exp\left( {- {\gamma\hspace{0pt}p\hspace{0pt}\left( {\frac{\delta}{2\hspace{0pt}\epsilon} - \sqrt{\frac{m\hspace{0pt}n}{p}} - 2} \right)^{2}}} \right)}}.$$      (4.24)
  -- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

We now must pick a suitable resolution $\epsilon$ to guarantee that this probability is less than $\exp{({- {c_{1}\hspace{0pt}p}})}$ for a suitably chosen constant $c_{1}$. First note that if we choose $\epsilon < {{({\delta/4})}\hspace{0pt}{({\sqrt{{m\hspace{0pt}n}/p} + 1})}^{- 1}}$,

  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $${{\mathbf{P}\hspace{0pt}\left( {{\|\mathcal{A}\|} \geq {\frac{\delta}{2\hspace{0pt}\epsilon} - 1}} \right)} \leq {\exp{({- {\gamma\hspace{0pt}m\hspace{0pt}n}})}}},$$      (4.25)
  -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

which achieves the desired scaling because ${m\hspace{0pt}n} > p$. With this choice of $\epsilon$, the quantity in Equation (4.22) is less than or equal to

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------
     $$\begin{array}{cl}                                                                                                                                                                                                                                                                                               (4.26)
      & {2\hspace{0pt}\left( \frac{8\hspace{0pt}C_{0}\hspace{0pt}{({\sqrt{{m\hspace{0pt}n}/p} + 1})}}{\delta} \right)^{r\hspace{0pt}{({{m + n} - {2\hspace{0pt}r}})}}\hspace{0pt}{({24/\delta})}^{r^{2}}\hspace{0pt}{\exp\left( {- {\frac{p}{2}\hspace{0pt}{({{\delta^{2}/32} - {\delta^{3}/96}})}}} \right)}} \\      
      & {= \exp\left( - pa{(\delta)} + r{(m + n - 2r)}\log\left( \sqrt{\frac{m\hspace{0pt}n}{p}} + 1 \right) \right.} \\                                                                                                                                                                                               
      & \left. + r{(m + n - 2r)}\log\left( \frac{8\hspace{0pt}C_{0}}{\delta} \right) + r^{2}\log\left( \frac{24}{\delta} \right) \right)                                                                                                                                                                               
     \end{array}$$                                                                                                                                                                                                                                                                                                     
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- --------

where ${a\hspace{0pt}{(\delta)}} = {{\delta^{2}/64} - {\delta^{3}/192}}$. Since ${{m\hspace{0pt}n}/p} < {m\hspace{0pt}n}$ for all $p > 1$, there exists a constant $c_{0}$ independent of $m$,$n$,$p$, and $r$, such that the sum of the last three terms in the exponent are bounded above by ${({{c_{0}/a}\hspace{0pt}{(\delta)}})}\hspace{0pt}r\hspace{0pt}{({m + n})}\hspace{0pt}{\log{({m\hspace{0pt}n})}}$. It follows that there exists a constant $c_{1}$ independent of $m$,$n$,$p$, and $r$ such that $p \geq {c_{0}\hspace{0pt}r\hspace{0pt}{({m + n})}\hspace{0pt}{\log{({m\hspace{0pt}n})}}}$ observations are sufficient to yield an RIP of $\delta$ with probability greater than $1 - e^{- {c_{1}\hspace{0pt}p}}$.  

Heuristically, the scaling $p = {O\hspace{0pt}\left( {r\hspace{0pt}{({m + n})}\hspace{0pt}{\log{({m\hspace{0pt}n})}}} \right)}$ is very reasonable, since a rank $r$ matrix has $r\hspace{0pt}{({{m + n} - r})}$ degrees of freedom. This coarse tail bound only provides asymptotic estimates for recovery, and is quite conservative in practice. As we demonstrate in Section 6, minimum rank solutions can be determined from between $2\hspace{0pt}r\hspace{0pt}{({{m + n} - r})}$ to $4\hspace{0pt}r\hspace{0pt}{({{m + n} - r})}$ observations for many practical problems.

## 5 Algorithms for nuclear norm minimization 

A variety of methods can be developed for the effective minimization of the nuclear norm over an affine subspace of matrices, and we do not have room for a comprehensive treatment here. Instead, we focus on three methods highlighting the trade-offs between computational speed and guarantees on accuracy of the resulting solution. Directly solving the semidefinite characterization of the nuclear norm problem using primal-dual interior point methods is a numerically efficient method for small problems and can be used to yield accuracy up to floating-point precision.

Since interior point methods use second order information, the memory requirements for computing descent directions quickly becomes too large as the problem size increases. Moreover, for larger problem sizes it is preferable to use methods that exploit, at least partially, the structure of the problem. This can be done at several levels, either by taking into account further information that may be available about the linear map $\mathcal{A}$ (e.g., the case of partially observed Fourier measurements) or by formulating algorithms that are specific to the nuclear norm problem. For the latter, we show how to apply subgradient methods to minimize the nuclear norm over an affine set. Such first-order methods cannot yield as high numerical precision as interior point methods, but much larger problems can be solved because no second-order information needs to be stored. For even larger problems, we discuss a low-rank semidefinite programming that explicitly works with a factorization of the decision variable. This method can be applied even when the matrix decision variable cannot fit into memory, but convergence guarantees are much less satisfactory than in the other two cases.

### 5.1 Interior Point Methods for Semidefinite programming 

For small problems where a high-degree of numerical precision is required, interior point methods for semidefinite programming can be directly applied to solve affine nuclear minimization problems. As we have seen in earlier sections, the nuclear norm minimization problem can be directly posed as a semidefinite programming problem via the standard form primal-dual pair (2.8). As written, the primal problem has one ${({n + m})} \times {({n + m})}$ semidefinite constraint and $p$ affine constraints. Conversely, the dual problem has one ${({n + m})} \times {({n + m})}$ semidefinite constraint and $p$ scalar decision variables. Thus, the total number of decision variables (primal and dual) is equal to $\binom{n + m + 1}{2} + p$.

Modern interior point solvers for semidefinite programming generally use primal-dual methods, and compute an update direction for the current solution by solving a suitable Newton system. Depending on the structure of the linear mapping $\mathcal{A}$, this may entail solving a potentially large, dense linear system.

If the matrix dimensions $n$ and $m$ are not too large, then any good interior point SDP solver, such as SeDuMi \[48\] or SDPT3 \[51\], will quickly produce accurate solutions. In fact, as we will see in the next section, problems with $n$ and $m$ around $50$ can be solved to machine precision in minutes on a desktop computer to machine precision. However, solving such a primal-dual pair of programs with traditional interior point methods can prove to be quite challenging when the dimensions of the matrix $X$ are much bigger than $100 \times 100$, since in this case the corresponding Newton systems become quite large. In the absence of any specific additional structure, the memory requirements of such dense systems quickly limit the size of problems that can be solved.

Perhaps the most important drawback of the direct SDP approach is that it completely ignores the possibility of efficiently computing the nuclear norm via a singular value decomposition, instead of the less efficient eigenvalue decomposition of a bigger matrix. The method we discuss next will circumvent this obstacle, by directly working with subgradients of the nuclear norm.

### 5.2 Projected subgradient methods 

The nuclear norm minimization (3.1) is a linearly constrained nondifferentiable convex problem. There are numerous techniques to approach this kind of problems, depending on the specific nature of the constraints (e.g., dense vs. sparse), and the possibility of using first- or second-order information.

In this section we describe a simple, easy to implement, subgradient projection approach to the solution of (3.1). This first-order method will proceed by computing a sequence of feasible points $\{ X_{k}\}$, with iterates satisfying the update rule

  -- ------------------------------------------------------------------------------------------------------------------------ --
     $${{X_{k + 1} = {\Pi\hspace{0pt}{({X_{k} - {s_{k}\hspace{0pt}Y_{k}}})}}},{Y_{k} \in {\partial{\| X_{k}\|}_{\ast}}}},$$   
  -- ------------------------------------------------------------------------------------------------------------------------ --

where $\Pi$ is the orthogonal projection onto the affine subspace defined by the linear constraints ${\mathcal{A}\hspace{0pt}{(X)}} = b$, and $s_{k} > 0$ is a stepsize parameter. In other words, the method updates the current iterate $X_{k}$ by taking a step along the direction of a subgradient at the current point and then projecting back onto the feasible set. Alternatively, since $X_{k}$ is feasible, we can rewrite this as

  -- ------------------------------------------------------------------------------------ --
     $${X_{k + 1} = {X_{k} - {s_{k}\hspace{0pt}\Pi_{\mathcal{A}}\hspace{0pt}Y_{k}}}},$$   
  -- ------------------------------------------------------------------------------------ --

where $\Pi_{\mathcal{A}}$ is the orthogonal projection onto the kernel of $\mathcal{A}$. Since the feasible set is an affine subspace, there are several options for the projection $\Pi_{\mathcal{A}}$. For small problems, one can precompute it using, for example, a QR decomposition of the matrix representation of $\mathcal{A}$ and store it. Alternatively, one can solve a least squares problem at each step by iterative methods such as conjugate gradients.

The subgradient-based method described above is extremely simple to implement, since only a subgradient evaluation is required at every step. The computation of the subgradient can be done using the formula given in (2.9) earlier, thus requiring only a singular value decomposition of the current point $X_{k}$.

A possible alternative here to the use of the SVD for the subgradient computation is to directly focus on the "angular" factor of the polar decomposition of $X_{k}$, using for instance the Newton-like methods developed by Gander in \[30\]. Specifically, for a given matrix $X_{k}$, the Halley-like iteration

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------- --
     $$X\rightarrow{X\hspace{0pt}{({{X^{\prime}\hspace{0pt}X} + {3\hspace{0pt}I}})}\hspace{0pt}{({{3\hspace{0pt}X^{\prime}\hspace{0pt}X} + I})}^{- 1}}$$   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------- --

converges globally and quadratically to the polar factor of $X$, and thus yields an element of the subdifferential of the nuclear norm. This iteration method (suitable scaled) can be faster than a direct SVD computation, particularly if the singular values of the initial matrix are close to 1. This could be appealing since presumably only a very small number of iterations would be needed to update the polar factor of $X_{k}$, although the nonsmoothness of the subdifferential is bound to cause some additional difficulties.

Regarding convergence, for general nonsmooth problems, subgradient methods do not guarantee a decrease of the cost function at every iteration, even for arbitrarily small step sizes (see, e.g., \[7, §6.3.1\]), unless the minimum-norm subgradient is used. Instead, convergence is usually shown through the decrease (for small stepsize) of the distance from the iterates $X_{k}$ to any optimal point. There are several possibilities for the choice of stepsize $s_{k}$. The simplest choice that can guarantee convergence is to use a diminishing stepsize with an infinite travel condition (i.e., such that ${\lim_{k\rightarrow\infty}s_{k}} = 0$ and $\sum_{k > 0}s_{k}$ diverging).

Often times, even the computation of a singular value decomposition or Halley-like iteration can be too computationally expensive. The next section proposes a reduction of the size of the search space to alleviate such demands. We must give up guarantees of convergence for this convenience, but this may be an acceptable trade-off for very large-scale problems.

### 5.3 Low-rank parametrization 

We now turn to a method that works with an explicit low-rank factorization of $X$. This algorithm not only requires less storage capacity and computational overhead than the previous methods, but for many problems does not even require one to be able to store the decision variable $X$ in memory. This is the case, for example, in the matrix completion problem where $\mathcal{A}\hspace{0pt}{(X)}$ is a subset of the entries of $X$.

Given observations of the form ${\mathcal{A}\hspace{0pt}{(X)}} = b$ of an $m \times n$ matrix $X$ of rank $r$, a possible search algorithm to find a suitable $X$ would be to find a factorization $X = {L\hspace{0pt}R^{\prime}}$, where $L$ is an $m \times r$ matrix and $R$ an $n \times r$ matrix, such that the equality constraints are satisfied. Since there are many possible such factorizations, we could search for one where the matrices $L$ and $R$ have Frobenius norm as small as possible, i.e., the solution of the optimization problem

  -- ------------------------------------------------------------------------------------------- -- -------
     $$\begin{aligned}                                                                              (5.1)
     \min\limits_{L,R} & {\frac{1}{2}\hspace{0pt}{({{\| L\|}_{F}^{2} + {\| R\|}_{F}^{2}})}} \\      
     \text{s.t.} & {{{\mathcal{A}\hspace{0pt}{({L\hspace{0pt}R^{\prime}})}} = b}.}                  
     \end{aligned}$$                                                                                
  -- ------------------------------------------------------------------------------------------- -- -------

Even though the cost function is convex, the constraint is not. Such a problem is a nonconvex quadratic program, and it is not evidently easy to optimize. We show below that the minimization of the nuclear norm subject to equality constraints is in fact equivalent to this rather natural heuristic optimization, as long as $r$ is chosen to be sufficiently larger than the rank of the optimum of the nuclear norm problem.

###### Lemma 5.1 

Assume $r \geq {{rank}{(X_{0})}}$. The nonconvex quadratic optimization problem (5.1) is equivalent to the minimum nuclear norm relaxation (3.1).

Proof    Consider any feasible solution $(L,R)$ of (5.1). Then, defining $W_{1}:={L\hspace{0pt}L^{\prime}}$, $W_{2}:={R\hspace{0pt}R^{\prime}}$, and $X:={L\hspace{0pt}R^{\prime}}$ yields a feasible solution of the primal SDP problem (2.8) that achieves the same cost. Since the SDP formulation is equivalent to the nuclear norm problem, we have that the optimal value of (5.1) is always greater than or equal to the nuclear norm heuristic.

For the converse, we can use an argument similar to the proof of Proposition 2.1. From the SVD decomposition $X^{\ast} = {U\hspace{0pt}\Sigma\hspace{0pt}V^{\prime}}$ of the optimal solution of the nuclear norm relaxation (3.1), we can explicitly construct matrices $L:={U\hspace{0pt}\Sigma^{\frac{1}{2}}}$ and $R:={V\hspace{0pt}\Sigma^{\frac{1}{2}}}$ for (5.1) that yield exactly the same value of the objective.  

The main advantage of this reformulation is to substantially decrease the number of primal decision variables from $n\hspace{0pt}m$ to ${({n + m})}\hspace{0pt}r$. For large problems, this is quite a significant reduction that allows us to search for matrices of rank smaller than the order of $100$, and $n + m$ in the hundreds of thousands on a desktop computer. However, this problem is nonconvex and potentially subject to local minima. This is not as much of a problem as it could be, for two reasons. First recall from Theorem 3.2 that if ${\delta_{2\hspace{0pt}r}\hspace{0pt}{(\mathcal{A})}} < 1$, there is a unique $X^{\ast}$ with rank at most $r$ such that ${\mathcal{A}\hspace{0pt}{(X^{\ast})}} = b$. Since any local minima $(L^{\ast},R^{\ast})$ of (5.1) is feasible, we would have $X^{\ast} = {L^{\ast}\hspace{0pt}{}_{}^{}}$ and we would have found the minimum rank solution. Second, we now present an algorithm that is guaranteed to converge to a local minima for a judiciously selected $r$. We will also provide a sufficient condition for when we can construct an optimal solution of (2.8) from the solution computed by the method of multipliers.

#### SDPLR and the method of multipliers 

For general semidefinite programming problems, Burer and Monteiro have developed in \[8, 9\] a nonlinear programming approach that relies on a low-rank factorization of the matrix decision variable. We will adapt this idea to our problem, to provide a first-order Lagrangian minimization algorithm that efficiently finds a local minima of (5.1). As a consequence of the work in \[9\], it will follow that for values of $r$ larger than the rank of the true optimal solution, the local minima of (5.1) can be transformed into global minima of (2.8) under the identification $W_{1} = {L\hspace{0pt}L^{\prime}}$, $W_{2} = {R\hspace{0pt}R^{\prime}}$ and $Y = {L\hspace{0pt}R^{\prime}}$. We summarize below the details of this approach.

The algorithm employed is called the *method of multipliers*, a standard approach for solving equality constrained optimization problems \[6\]. The method of multipliers works with an augmented Lagrangian for (5.1)

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------
     $${{\mathcal{L}_{a}\hspace{0pt}{(L,R;y,\sigma)}}:={{{\frac{1}{2}\hspace{0pt}{({{\| L\|}_{F}^{2} + {\| R\|}_{F}^{2}})}} - {y^{\prime}\hspace{0pt}{({{\mathcal{A}\hspace{0pt}{({L\hspace{0pt}R^{\prime}})}} - b})}}} + {\frac{\sigma}{2}\hspace{0pt}{\|{{\mathcal{A}\hspace{0pt}{({L\hspace{0pt}R^{\prime}})}} - b}\|}^{2}}}},$$      (5.2)
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -- -------

where the $y_{i}$ are arbitrarily signed Lagrange multipliers and $\sigma$ is a positive constant. A somewhat similar algorithm was proposed by Rennie et al in \[42\] in the collaborative filtering. In this work, the authors minimize $\mathcal{L}_{a}$ with $\sigma$ fixed and $y = 0$ to serve as a regularized algorithm for matrix completion. Remarkably, by deterministically varying $\sigma$ and $y$, this method can be adapted into an algorithm for solving linearly constrained nuclear-norm minimization.

In the method of multipliers, one alternately minimizes the augmented Lagrangian with respect to the decision variables $L$ and $R$, and then increases the value of the penalty coefficient $\sigma$ and updates $y$. The augmented Lagrangian can be minimized using any local search technique, and the partial derivatives are particularly simple to compute. Let $\hat{y}:={y - {\sigma\hspace{0pt}{({{\mathcal{A}\hspace{0pt}{({L\hspace{0pt}R^{\prime}})}} - b})}}}$. Then we have

  -- -------------------------------------------------------------------------------------------------------------- --
     $$\begin{aligned}                                                                                              
     {\nabla_{L}\mathcal{L}_{a}} & {= {L - {\mathcal{A}^{\ast}\hspace{0pt}{(\hat{y})}\hspace{0pt}R}}} \\            
     {\nabla_{R}\mathcal{L}_{a}} & {{= {R - {\mathcal{A}^{\ast}\hspace{0pt}{(\hat{y})}^{\prime}\hspace{0pt}L}}}.}   
     \end{aligned}$$                                                                                                
  -- -------------------------------------------------------------------------------------------------------------- --

To calculate the gradients, we first compute the constraint violations ${\mathcal{A}\hspace{0pt}{({L\hspace{0pt}R^{\prime}})}} - b$, then form $\hat{y}$, and finally use the above equations to compute the gradients.

As the number of iterations tends to infinity, only feasible points will have finite values of $\mathcal{L}_{a}$, and for any feasible point, $\mathcal{L}_{a}\hspace{0pt}{(L,R)}$ is equal to the original cost function ${({{\| L\|}_{F}^{2} + {\| R\|}_{F}^{2}})}/2$. The method terminates when $L$ and $R$ are feasible, as in this case the Lagrangian is stationary and we are at a local minima of (5.1). Including the $y$ multipliers improves the conditioning of each subproblem where $\mathcal{L}_{a}$ is minimized and enhances the rate of convergence. The following theorem shows that when the method of multipliers converges, it converges to a local minimum of (5.1).

###### Theorem 5.2 

Suppose we have a sequence $(L^{(k)},R^{(k)},y^{(k)})$ of local minima of the augmented Lagrangian at each step of the method of multipliers. Assume that our sequence of $\sigma^{(k)}\rightarrow\infty$ and that the sequence of $y^{(k)}$ is bounded. If $(L^{(k)},R^{(k)})$ converges to $(L^{\ast},R^{\ast})$ and the linear map

  -- ------------------------------------------------------------------- -- -------
     $${\Lambda^{(k)}\hspace{0pt}{(y)}}:=\begin{bmatrix}                    (5.3)
     {\mathcal{A}^{\ast}\hspace{0pt}{(y)}\hspace{0pt}R^{(k)}} \\            
     {\mathcal{A}^{\ast}\hspace{0pt}{(y)}^{\prime}\hspace{0pt}L^{(k)}}      
     \end{bmatrix}$$                                                        
  -- ------------------------------------------------------------------- -- -------

has kernel equal to the zero vector for all $k$, then there exists a vector $y^{\ast}$ such that

1.  [(i)]

    ${{\nabla\mathcal{L}_{a}}\hspace{0pt}{(L^{\ast},R^{\ast};y^{\ast})}} = 0$

2.  [(ii)]

    ${\mathcal{A}\hspace{0pt}{({L^{\ast}\hspace{0pt}{}_{}^{}})}} = b$

Proof    This proof is standard and follows the approach in \[6\]. As above, we define ${\hat{y}}^{(k)}:={y^{(k)} - {\sigma^{(k)}\hspace{0pt}{({{\mathcal{A}\hspace{0pt}{({L^{(k)}\hspace{0pt}{}_{}^{(k)}})}} - b})}}}$ for all $k$. Since $(L^{(k)},R^{(k)})$ minimize the augmented Lagrangian at iteration $k$, we have

  -- -------------------------------------------------------------------------------------------------------- -- -------
     $$\begin{aligned}                                                                                           (5.4)
     0 & {= {L^{(k)} - {\mathcal{A}^{\ast}\hspace{0pt}{({\hat{y}}^{(k)})}\hspace{0pt}R^{(k)}}}} \\               
     0 & {{= {R^{(k)} - {\mathcal{A}^{\ast}\hspace{0pt}{({\hat{y}}^{(k)})}^{\prime}\hspace{0pt}L^{(k)}}}},}      
     \end{aligned}$$                                                                                             
  -- -------------------------------------------------------------------------------------------------------- -- -------

which we may rewrite as

  -- --------------------------------------------------------------------- -- -------
     $${{\Lambda^{(k)}\hspace{0pt}{({\hat{y}}^{(k)})}} = \begin{bmatrix}      (5.5)
     L^{(k)} \\                                                               
     R^{(k)}                                                                  
     \end{bmatrix}}.$$                                                        
  -- --------------------------------------------------------------------- -- -------

Since we have assumed that there is no non-zero $y$ with ${\Lambda^{(k)}\hspace{0pt}{(y)}} = 0$, there exists a left-inverse and we can solve for ${\hat{y}}^{(k)}$.

  -- --------------------------------------------------------------------- -- -------
     $${{\hat{y}}^{(k)} = {{}_{}^{(k)}\hspace{0pt}\left( \begin{bmatrix}      (5.6)
     L^{(k)} \\                                                               
     R^{(k)}                                                                  
     \end{bmatrix} \right)}}.$$                                               
  -- --------------------------------------------------------------------- -- -------

Everything on the right-hand side is bounded, and $L^{(k)}$ and $R^{(k)}$ converge. Therefore, we must have that ${\hat{y}}^{(k)}$ converges to some ${\hat{y}}^{\ast}$. Taking the limit of (5.4) proves (i). To prove (ii), note that we must have ${\hat{y}}^{(k)}$ is bounded. Since $y^{(k)}$ is also bounded, we find that $\sigma^{(k)}\hspace{0pt}{({{\mathcal{A}\hspace{0pt}{({L^{(k)}\hspace{0pt}{}_{}^{(k)}})}} - b})}$ is also bounded. But $\sigma^{(k)}\rightarrow\infty$ implies that ${\mathcal{A}\hspace{0pt}{({L^{\ast}\hspace{0pt}{}_{}^{}})}} = b$, completing the proof.  

Suppose the decision variables are chosen to be of size $m \times r_{d}$ and $n \times r_{d}$. A necessary condition for $\Lambda^{k}\hspace{0pt}{(y)}$ to be full rank is for the number of decision variables $r_{d}\hspace{0pt}{({m + n})}$ to be greater than the number of equalities $p$. In particular, this means that we must choose $r_{d} \geq {p/{({m + n})}}$ in order to have any hopes of satisfying the conditions of Theorem 5.2.

We close this section by relating the solution found by the method of multipliers to the optimal solution of the nuclear norm minimization problem. We have already shown that when the low-rank algorithm converges, it converges to a low-rank solution of ${\mathcal{A}\hspace{0pt}{(X)}} = b$. If we additionally find that $\mathcal{A}^{\ast}\hspace{0pt}{(y^{\ast})}$ has norm less than or equal to one, then it is dual feasible. One can check using straightforward algebra that $({L^{\ast}\hspace{0pt}{}_{}^{}},{L^{\ast}\hspace{0pt}{}_{}^{}},{R^{\ast}\hspace{0pt}{}_{}^{}})$ and $y^{\ast}$ form an optimal primal-dual pair for (2.8). This analysis proves the following theorem.

###### Theorem 5.3 

Let $(L^{\ast},R^{\ast},y^{\ast})$ satisfy (i)-(ii) in Theorem 5.2 and suppose ${\|{\mathcal{A}^{\ast}\hspace{0pt}{(y^{\ast})}}\|} \leq 1$. Then $({L^{\ast}\hspace{0pt}{}_{}^{}},{L^{\ast}\hspace{0pt}{}_{}^{}},{R^{\ast}\hspace{0pt}{}_{}^{}})$ is an optimal primal solution and $y^{\ast}$ is an optimal dual solution of (2.8).

## 6 Numerical Experiments 

To illustrate the scaling of low-rank recovery for a particular matrix $M$, consider the MIT logo presented in Figure 1. The image has a total of $46$ rows and $81$ columns (total 3726 elements), and 3 distinct non-zero numerical values corresponding to the colors white, red, and grey. Since the logo only has $5$ distinct rows, it has rank $5$. For each of the ensembles discussed in Section 4, we sampled measurement matrices with $p$ ranging between $700$ and $1500$, and solved the semidefinite program (2.6) using the freely available software SeDuMi \[48\]. On a 2.0 GHz Laptop, each semidefinite program could be solved in less than four minutes. We chose to use this interior point method because it yielded the highest accuracy in the shortest amount of time, and we were interested in characterizing precisely when the nuclear norm heuristic succeeded and failed.

Figure 2 plots the Frobenius norm of the difference between the optimal point of the semidefinite program and the true image in Figure 2. We observe a sharp transition to perfect recovery near 1200 measurements which is approximately equal to $2\hspace{0pt}r\hspace{0pt}{({{m + n} - r})}$. In Figure 3, we graphically plot the recovered solutions for various values of $p$ under the Gaussian ensemble.

Figure 1: The MIT logo image. The associated matrix has dimensions 46 × 81 and has rank 5.

(a)

(b)

Figure 2: (a) Error, as measured by the Frobenius norm, between the recovered image and the ground truth. Observe that there is a sharp transition to near zero error at around 1200 measurements. (b) Zooming in on this transition, we see fluctuation between high and low error when between 1125 and 1225 measurements are available.

(a)
(b)
(c)

Figure 3: Example recovered images using the Gaussian ensemble. (a) 700 measurements. (b) 1100 measurements (c) 1250 measurements. The total number of pixels is 46 × 81 = 3726. Note that the error is plotted on a logarithmic scale.

To demonstrate the average behavior of low-rank recovery, we conducted a series of experiments for a variety of the matrix sizes $n$, ranks $r$, and numbers of measurements $p$. For a fixed $n$, we constructed random recovery scenarios for low-rank $n \times n$ matrices. For each $n$, we varied $p$ between $0$ and $n^{2}$ where the matrix is completely discovered. For a fixed $n$ and $p$, we generated all possible ranks such that ${r\hspace{0pt}{({{2\hspace{0pt}n} - r})}} \leq p$. This cutoff was chosen because beyond that point there would be an infinite set of matrices of rank $r$ satisfying the $p$ equations.

For each $(n,p,r)$ triple, we repeated the following procedure $10$ times. A matrix of rank $r$ was generated by choosing two random $n \times r$ factors $Y_{L}$ and $Y_{R}$ with i.i.d. random entries and setting $Y_{0} = {Y_{L}\hspace{0pt}Y_{R}^{\prime}}$. A matrix $\mathbf{A}$ was sampled from the Gaussian ensemble with $p$ rows and $n^{2}$ columns. Then the nuclear norm minimization

  -- ------------------------------------------------------------------------------------------------- -- -------
     $$\begin{aligned}                                                                                    (6.1)
     \min\limits_{X} & {\| X\|}_{\ast} \\                                                                 
     \text{s.t.} & {{\mathbf{A}\hspace{0pt}{{vec}{(X)}}} = {\mathbf{A}\hspace{0pt}{{vec}{(Y_{0})}}}}      
     \end{aligned}$$                                                                                      
  -- ------------------------------------------------------------------------------------------------- -- -------

was solved using the SDP solver SeDuMi on the formulation (2.6). Again, we chose to use SeDuMi because we wanted to precisely distinguish between success and failure of the heuristic. We declared $Y_{0}$ to be recovered if ${{\|{X - Y_{0}}\|}_{F}/{\| Y_{0}\|}_{F}} < 10^{- 3}$. Figure 4 shows the results of these experiments for $n = 30$ and $40$. The color of the cell in the figures reflects the empirical recovery rate of the $10$ runs (scaled between $0$ and $1$). White denotes perfect recovery in all experiments, and black denotes failure for all experiments.

These experiments demonstrate that the logarithmic factors and constants present in our scaling results are somewhat conservative. For example, as one might expect, low-rank matrices are perfectly recovered by nuclear norm minimization when $p = n^{2}$ as the matrix is uniquely determined. Moreover, as $p$ is reduced slightly away from this value, low-rank matrices are still recovered $100$ percent of the time for most values of $r$. Finally, we note that despite the asymptotic nature of our analysis, our experiments demonstrate excellent performance with low-rank matrices of size $30 \times 30$ and $40 \times 40$ matrices, showing that the heuristic is practical even in low-dimensional settings.

Intriguingly, Figure 4 also demonstrates a "phase transition" between perfect recovery and failure. As observed in several recent papers by Donoho and his collaborators (See e.g. \[18, 19\]), the random sparsity recovery problem has two distinct connected regions of parameter space: one where the sparsity pattern is perfectly recovered, and one where no sparse solution is found. Not surprisingly, Figure 4 illustrates an analogous phenomenon in rank recovery. Computing explicit formulas for the transition between perfect recovery and failure is left for future work.

(a)

(b)

Figure 4: For each (n,p,r) triple, we repeated the following procedure ten times. A matrix of rank r was generated by choosing two random n × r factors YL and YR with i.i.d. random entries and set Y0 = YL YR′. We select a matrix A from the Gaussian ensemble with p rows and n2 columns. Then we solve the nuclear norm minimization subject to A vec(X) = A vec(Y0) We declare Y0 to be recovered if ∥X − Y0∥F/∥Y0∥F &lt; 10−3. The results are shown for (a) n = 30 and (b) n = 40. The color of each cell reflects the empirical recovery rate (scaled between 0 and 1). White denotes perfect recovery in all experiments, and black denotes failure for all experiments.

## 7 Discussion and future developments 

Having illustrated the natural connections between affine rank minimization and affine cardinality minimization, we were able to draw on these parallels to determine scenarios where the nuclear norm heuristic was able to exactly solve the rank minimization problem. These scenarios directly generalized conditions for which the $\ell_{1}$ heuristic succeeded and ensembles of linear maps for which these conditions hold. Furthermore, our experimental results display similar recovery properties to those demonstrated in the empirical studies of $\ell_{1}$ minimization. Inspired by the success of this program, we close this report by briefly discussing several exciting directions that are natural continuations of this work building on more analogies from the compressed sensing literature. We also describe possible extensions to more general notions of parsimony.

#### Factored measurements and alternative ensembles 

All of the measurement ensembles require the storage of $O\hspace{0pt}{({m\hspace{0pt}n\hspace{0pt}p})}$ numbers. For large problems this is wholly impractical. There are many promising alternative measurement ensembles that seem to obey the same scaling laws as those presented in Section 4. For example, "factored" measurements, of the form $A_{i}:{X\mapsto{u_{i}^{T}\hspace{0pt}X\hspace{0pt}v_{i}}}$, where $u_{i},v_{i}$ are Gaussian random vectors empirically yield the same performance as the Gaussian ensemble. This factored ensemble only requires storage of $O\hspace{0pt}{({{({m + n})}\hspace{0pt}p})}$ numbers, which is a rather significant savings for very large problems. The proof in Section 4 does not seem to extend to this ensemble, thus new machinery must be developed to guarantee properties about such low-rank measurements.

#### Noisy Measurements and Low-rank approximation 

Our results in this paper address only the case of exact (noiseless) measurements. It is of natural interest to understand the behavior of the nuclear norm heuristic in the case of noisy data. Based on the existing results for the sparse case (e.g., \[12\]), it would be natural to expect similar stability properties of the recovered solution, for instance in terms of the $\ell_{2}$ norm of the computed solution. Such an analysis could also be used to study the nuclear norm heuristic as an approximation technique where a matrix has rapidly decaying singular values and a low-rank approximation is desired.

#### Incoherent Ensembles and Partially Observed Transforms 

Again, taking our lead from the compressed sensing literature, it would be of great interest to extend the results of \[11\] to low-rank recovery. In this work, the authors show that partially observed unitary transformations of sparse vectors can be used to recover the sparse vector using $\ell_{1}$ minimization. There are many practical applications where low-rank processes are partially observed. For instance, the matrix completion problem can be thought of as partial observations under the identity transformations. As another example, there are many examples in two-dimensional Fourier spectroscopy where only partial information can be observed due to experimental constraints.

#### Alternative numerical methods 

Besides the techniques described in Section 5, there are a number of interesting additional possibilities to solve the nuclear norm minimization problem. An appealing suggestion is to combine the strength of second-order methods (as in the SDP approach) with the known geometry of the nuclear norm (as in the subgradient approach), and develop a customized interior point method, possibly yielding faster convergence rates, while still being relatively memory-efficient.

It is also of much interest to investigate the possible adaptation of some of the successful path-following approaches in traditional $\ell_{1}$/cardinality minimization, such as the Homotopy \[40\] or LARS (least angle regression) \[21\]. This may be not be completely straightforward, since the efficiency of many of these methods often relies explicitly on the polyhedral structure of the feasible set of the $\ell_{1}$ norm problem.

#### Geometric interpretations 

For the case of cardinality/$\ell_{1}$ minimization, a beautiful geometric interpretation has been set forth by Donoho and Tanner \[18, 19\]. Key to their results is the notion of *central $k$-neighborliness* of a centrosymmetric polytope, namely the property that every subset of $k + 1$ vertices not including an antipodal pair spans a $k$-face. In particular, they show that the $\ell_{1}$ heuristic always succeeds whenever the image of the $\ell_{1}$ unit ball (the cross-polytope) under the linear mapping $\mathcal{A}$ is a centrally $k$-neighborly polytope.

In the case of rank minimization, the direct application of these concepts fails, since the unit ball of the nuclear norm is not a polyhedral set. Nevertheless, it seems likely that a similar explanation could be developed, where the key feature would be the preservation under a linear map of the extremality of the components of the boundary of the nuclear norm unit ball defined by low-rank conditions.

#### Jordan algebras 

As we have seen, our results for the rank minimization problem closely parallel the earlier developments in cardinality minimization. A convenient mathematical framework that allows the simultaneous consideration of these cases as well as a few new ones, is that of *Jordan algebras* and the related symmetric cones \[24\]. In the Jordan-algebraic setting, there is an intrinsic notion of rank that agrees with the cardinality of the support in the case of the nonnegative orthant or the rank of a matrix in the case of the positive semidefinite cone. Besides mathematical elegance, a direct Jordan-algebraic approach would transparently yield similar results for the case of second-order (or Lorentz) cone constraints.

As specific examples of the power and elegance of this approach, we mention the work of Faybusovich \[25\] and Schmieta and Alizadeh \[43\] that provide a unified development of interior point methods for symmetric cones, as well as Faybusovich's work on convexity theorems for quadratic mappings \[26\].

#### Parsimonious models and optimization 

Sparsity and low-rank are two specific classes of parsimonious (or low-complexity) descriptions. Are there other kinds of easy-to-describe parametric models that are amenable to exact solutions via convex optimizations techniques? Given the intimate connections between linear and semidefinite programming and the Jordan algebraic approaches described earlier, it is likely that this will require alternative tractable convex optimization formulations.

## 8 Acknowledgements 

We thank Stephen Boyd, Emmanuel Candès, José Costa, John Doyle, Ali Jadbabaie, Ali Rahimi, and Michael Wakin for their useful comments and suggestions. We also thank the IMA in Minneapolis for hosting us during the initial stages of our collaboration.

## References 

-   [\[1\] P.-A. Absil, A. Edelman, and P. Koev. On the largest principal angle between random subspaces. Linear Algebra Appl., 414(1):288--294, 2006.]
-   [\[2\] D. Achlioptas. Database-friendly random projections: Johnson-Lindenstrauss with binary coins. Journal of Computer and Systems Science, 66(4):671--687, 2003. Special issue of invited papers from PODS'01.]
-   [\[3\] H. C. Andrews and C. L. Patterson, III. Singular value decomposition (SVD) image coding. IEEE Transactions on Communications, 24(4):425--432, 1976.]
-   [\[4\] R. Baraniuk, M. Davenport, R. DeVore, and M. Wakin. A simple proof of the restricted isometry property for random matrices. Preprint, 2007. http://dsp.rice.edu/cs/jlcs-v03.pdf.]
-   [\[5\] C. Beck and R. D'Andrea. Computational study and comparisons of LFT reducibility methods. In Proceedings of the American Control Conference, 1998.]
-   [\[6\] D. P. Bertsekas. Constrained Optimization and Lagrange Multiplier Methods. Athena Scientific, Belmont, Massachusetts, 1996.]
-   [\[7\] D. P. Bertsekas. Nonlinear Programming. Athena Scientific, Belmont, MA, 2nd edition, 1999.]
-   [\[8\] S. Burer and R. D. C. Monteiro. A nonlinear programming algorithm for solving semidefinite programs via low-rank factorization. Mathematical Programming (Series B), 95:329--357, 2003.]
-   [\[9\] S. Burer and R. D. C. Monteiro. Local minima and convergence in low-rank semidefinite programming. Mathematical Programming, 103(3):427--444, 2005.]
-   [\[10\] E. J. Candès. Compressive sampling. In International Congress of Mathematicians. Vol. III, pages 1433--1452. Eur. Math. Soc., Zürich, 2006.]
-   [\[11\] E. J. Candès and J. Romberg. Sparsity and incoherence in compressive sampling. Inverse Problems, 23(3):969--985, 2007.]
-   [\[12\] E. J. Candès, J. Romberg, and T. Tao. Stable signal recovery from incomplete and inaccurate measurements. Communications of Pure and Applied Mathematics, 59:1207--1223, 2005.]
-   [\[13\] E. J. Candès, J. Romberg, and T. Tao. Robust uncertainty principles: exact signal reconstruction from highly incomplete frequency information. IEEE Trans. Inform. Theory, 52(2):489--509, 2006.]
-   [\[14\] E. J. Candès and T. Tao. Decoding by linear programming. IEEE Transactions on Information Theory, 51(12):4203--4215, 2005.]
-   [\[15\] S. Dasgupta and A. Gupta. An elementary proof of a theorem of Johnson and Lindenstrauss. Random Structures and Algorithms, 22(1):60--65, 2003.]
-   [\[16\] K. R. Davidson and S. J. Szarek. Local operator theory, random matrices and Banach spaces. In W. B. Johnson and J. Lindenstrauss, editors, Handbook on the Geometry of Banach spaces, pages 317--366. Elsevier Scientific, 2001.]
-   [\[17\] D. L. Donoho. Compressed sensing. IEEE Trans. Inform. Theory, 52(4):1289--1306, 2006.]
-   [\[18\] D. L. Donoho and J. Tanner. Neighborliness of randomly projected simplices in high dimensions. Proc. Natl. Acad. Sci. USA, 102(27):9452--9457, 2005.]
-   [\[19\] D. L. Donoho and J. Tanner. Sparse nonnegative solution of underdetermined linear equations by linear programming. Proc. Natl. Acad. Sci. USA, 102(27):9446--9451, 2005.]
-   [\[20\] C. Eckart and G. Young. The approximation of one matrix by another of lower rank. Psychometrika, 1(3):211--218, 1936.]
-   [\[21\] B. Efron, T. Hastie, I. M. Johnstone, and R. Tibshirani. Least angle regression. Annals of Statistics, 32(2):407--499, 2004.]
-   [\[22\] L. El Ghaoui and P. Gahinet. Rank minimization under LMI constraints: A framework for output feedback problems. In Proceedings of the European Control Conference, 1993.]
-   [\[23\] N. El Karoui. New results about random covariance matrices and statistical applications. PhD thesis, Stanford University, 2004.]
-   [\[24\] J. Faraut and A. Korányi. Analysis on symmetric cones. Oxford Mathematical Monographs. The Clarendon Press Oxford University Press, New York, 1994.]
-   [\[25\] L. Faybusovich. Euclidean Jordan algebras and interior-point algorithms. Positivity, 1(4):331--357, 1997.]
-   [\[26\] L. Faybusovich. Jordan-algebraic approach to convexity theorem for quadratic mappings. http://www.optimization-online.org/DB_HTML/2005/06/1159.html, 2005.]
-   [\[27\] M. Fazel. Matrix Rank Minimization with Applications. PhD thesis, Stanford University, 2002.]
-   [\[28\] M. Fazel, H. Hindi, and S. Boyd. A rank minimization heuristic with application to minimum order system approximation. In Proceedings of the American Control Conference, 2001.]
-   [\[29\] M. Fazel, H. Hindi, and S. Boyd. Log-det heuristic for matrix rank minimization with applications to Hankel and Euclidean distance matrices. In Proceedings of the American Control Conference, 2003.]
-   [\[30\] W. Gander. Algorithms for the polar decomposition. SIAM J. Sci. Statist. Comput., 11(6):1102--1115, 1990.]
-   [\[31\] K. M. Grigoriadis and E. B. Beran. Alternating projection algorithms for linear matrix inequalities problems with rank constraints. In L. El Ghaoui and S. Niculescu, editors, Advances in Linear Matrix Inequality Methods in Control, chapter 13, pages 251--267. SIAM, 2000.]
-   [\[32\] J.-B. Hiriart-Urruty and C. Lemaréchal. Convex Analysis and Minimization Algorithms II: Advanced Theory and Bundle Methods. Springer-Verlag, New York, 1993.]
-   [\[33\] R. A. Horn and C. R. Johnson. Topics in Matrix Analysis. Cambridge University Press, New York, 1991.]
-   [\[34\] N. Linial, E. London, and Y. Rabinovich. The geometry of graphs and some of its algorithmic applications. Combinatorica, 15:215--245, 1995.]
-   [\[35\] G. G. Lorentz, M. von Golitschek, and Y. Makovoz. Constructive Approximation: Advanced problems, volume 304 of Grundlehren der Mathematischen Wissenschaften. Springer, 1996.]
-   [\[36\] G. Marsaglia and G. P. H. Styan. When does ${{rank}\hspace{0pt}\left( {A + B} \right)} = {{{rank}\hspace{0pt}(A)} + {{rank}\hspace{0pt}(B)}}$? Canad. Math. Bull., 15:451--452, 1972.]
-   [\[37\] M. Mesbahi and G. P. Papavassilopoulos. On the rank minimization problem over a positive semidefinite linear matrix inequality. IEEE Transactions on Automatic Control, 42(2):239--243, 1997.]
-   [\[38\] L. Mirsky. Symmetric gauge functions and unitarily invariant norms. Quart. J. Math. Oxford Ser. (2), 11:50--59, 1960.]
-   [\[39\] B. K. Natarajan. Sparse approximate solutions to linear systems. SIAM Journal of Computing, 24(2):227--234, 1995.]
-   [\[40\] M. R. Osborne, B. Presnell, and B. A. Turlach. A new approach to variable selection in least squares problems. IMA Journal of Numerical Analysis, 20:389--403, 2000.]
-   [\[41\] P. A. Parrilo and S. Khatri. On cone-invariant linear matrix inequalities. IEEE Trans. Automat. Control, 45(8):1558--1563, 2000.]
-   [\[42\] J. D. M. Rennie and N. Srebro. Fast maximum margin matrix factorization for collaborative prediction. In Proceedings of the International Conference of Machine Learning, 2005.]
-   [\[43\] S. H. Schmieta and F. Alizadeh. Associative and Jordan algebras, and polynomial time interior-point algorithms for symmetric cones. Math. Oper. Res., 26(3):543--564, 2001.]
-   [\[44\] I. J. Schoenberg. Remarks to Maurice Fréchet's article "Sur la définition axiomatique d'une classe d'espace distanciés vectoriellement applicable sur l'espace de Hilbert". Annals of Mathematics, 36(3):724--732, July 1935.]
-   [\[45\] R. E. Skelton, T. Iwasaki, and K. Grigoriadis. A Unified Algebraic Approach to Linear Control Design. Taylor and Francis, 1998.]
-   [\[46\] E. Sontag. Mathematical Control Theory. Springer-Verlag, New York, 1998.]
-   [\[47\] N. Srebro. Learning with Matrix Factorizations. PhD thesis, Massachusetts Institute of Technology, 2004.]
-   [\[48\] J. F. Sturm. Using SeDuMi 1.02, a MATLAB toolbox for optimization over symmetric cones. Optimization Methods and Software, 11-12:625--653, 1999.]
-   [\[49\] S. J. Szarek. The finite dimensional basis problem with an appendix on nets of the Grassmann manifold. Acta Mathematica, 151:153--179, 1983.]
-   [\[50\] S. J. Szarek. Metric entropy of homogeneous spaces. In Quantum probability (Gdańsk, 1997), volume 43 of Banach Center Publ., pages 395--410. Polish Acad. Sci., Warsaw, 1998. Preprint available at arXiv:math/9701213v1.]
-   [\[51\] K. C. Toh, M. Todd, and R. H. Tütüncü. SDPT3 - a MATLAB software package for semidefinite-quadratic-linear programming. Available from http://www.math.nus.edu.sg/\~mattohkc/sdpt3.html.]
-   [\[52\] M. W. Trosset. Distance matrix completion by numerical optimization. Computational Optimization and Applications, 17(1):11--22, October 2000.]
-   [\[53\] L. Vandenberghe and S. Boyd. Semidefinite programming. SIAM Review, 38(1):49--95, 1996.]
-   [\[54\] M. Wakin, J. Laska, M. Duarte, D. Baron, S. Sarvotham, D. Takhar, K. Kelly, and R. Baraniuk. An architecture for compressive imaging. In Proc. International Conference on Image Processing -- ICIP 2006, oct 2006.]
-   [\[55\] G. A. Watson. Characterization of the subdifferential of some matrix norms. Linear Algebra and Applications, 170:1039--1053, 1992.]
-   [\[56\] Y. Q. Yin, Z. D. Bai, and P. R. Krishnaiah. On the limit of the largest eigenvalue of the large dimensional sample covariance matrix. Probability Theory and Related Fields, 78:509--512, 1988.]
