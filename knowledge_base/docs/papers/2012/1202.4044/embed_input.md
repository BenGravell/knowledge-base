Robust Computation of Linear Models by Convex Relaxation

Topics include Robust subspace recovery, Convex relaxation, REAPER, Outlier robustness, Orthogonal projectors, High-dimensional statistics.

Introduces REAPER, a convex relaxation for fitting a low-dimensional linear subspace in the presence of many outliers by optimizing over a convex hull of orthogonal projectors. The paper matters because it couples a practical solver with recovery theory for noisy inliers, making robust PCA-style model fitting less dependent on brittle combinatorial inlier selection.

Consider a dataset of vector-valued observations that consists of noisy inliers, which are explained well by a low-dimensional subspace, along with some number of outliers. This work describes a convex optimization problem, called REAPER, that can reliably fit a low-dimensional model to this type of data. This approach parameterizes linear subspaces using orthogonal projectors, and it uses a relaxation of the set of orthogonal projectors to reach the convex formulation. The paper provides an efficient algorithm for solving the REAPER problem, and it documents numerical experiments which confirm that REAPER can dependably find linear structure in synthetic and natural data. In addition, when the inliers lie near a low-dimensional subspace, there is a rigorous theory that describes when REAPER can approximate this subspace.

## Introduction

Low-dimensional linear models have applications in a huge array of data analysis problems. Let us highlight some examples from computer vision, machine learning, and bioinformatics.

: Images of a face---or any Lambertian object---viewed under different illumination conditions lie near a nine-dimensional subspace:5pm2; HYL+03:Clustering-Appearances;:Lambertian-Reflectance.

Our analysis of reaper builds on the ideas first presented in:lp-Recovery;:Novel-M-Estimator, but it incorporates a number of refinements that simplify and improve the theoretical guarantees. In particular, the present results do not require an oracle condition like (:Novel-M-Estimator Eqs. ), and our stability statistic $\mathcal{S}{(L)}$ supersedes the earlier exact recovery and stability requirements (:Novel-M-Estimator Eqs. & ). The exact recovery guarantees under the Haystack Model are somewhat stronger for reaper than the analogous guarantees for (6.3) (:Novel-M-Estimator Sec. 2.6.1)....

From a broad perspective, the idea of relaxing a difficult nonconvex program like (1.3) to obtain a convex problem is well established in the literature on combinatorial optimization. Research on linear programming relaxations is summarized in:Approximation-Algorithms. Some significant works on semidefinite relaxation include:Cones-Matrices;:Improved-Approximation.

Fix a number $\beta > 0$, and assume that $1 \leq d \leq {{({D - 1})}/2}$. Let $L$ be an arbitrary $d$-dimensional subspace of ${\mathbb{R}}^{D}$, and draw the dataset $\mathcal{X}$ at random according to the Haystack Model on page 3.1. The stability statistic satisfies the bound

Imagine that we knew in advance which points were inliers. Then we could pose the oracle $\ell_{1}$ orthogonal regression problem:

Algorithm 4.2 IRLS algorithm for solving the reaper problem (1.4)

: Feature points on a moving rigid body lie on an affine space of dimension three, assuming the affine camera model:Multibody-Factorization. More generally, estimating structure from motion involves estimating low-rank matrices (:Efficient-Computation Sec. 5.2).

: We can describe a large corpus of documents that concern a small number of topics using a low-dimensional linear model DDL+88:Improving-Information.

: Low-dimensional models of single nucleotide polymorphism (SNP) data have been used to show that the genotype of an individual is...
