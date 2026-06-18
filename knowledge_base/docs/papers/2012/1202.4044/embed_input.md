Robust Computation of Linear Models by Convex Relaxation

Topics include Robust subspace recovery, Convex relaxation, REAPER, Outlier robustness, Orthogonal projectors, High-dimensional statistics.

Introduces REAPER, a convex relaxation for fitting a low-dimensional linear subspace in the presence of many outliers by optimizing over a convex hull of orthogonal projectors. The paper matters because it couples a practical solver with recovery theory for noisy inliers, making robust PCA-style model fitting less dependent on brittle combinatorial inlier selection.

Consider a dataset of vector-valued observations that consists of noisy inliers, which are explained well by a low-dimensional subspace, along with some number of outliers. This work describes a convex optimization problem, called REAPER, that can reliably fit a low-dimensional model to this type of data. This approach parameterizes linear subspaces using orthogonal projectors, and it uses a relaxation of the set of orthogonal projectors to reach the convex formulation. The paper provides an efficient algorithm for solving the REAPER problem, and it documents numerical experiments which confirm that REAPER can dependably find linear structure in synthetic and natural data. In addition, when the inliers lie near a low-dimensional subspace, there is a rigorous theory that describes when REAPER can approximate this subspace.

## Introduction

Low-dimensional linear models have applications in a huge array of data analysis problems. Let us highlight some examples from computer vision, machine learning, and bioinformatics.

: Images of a face---or any Lambertian object---viewed under different illumination conditions lie near a nine-dimensional subspace:5pm2; HYL+03:Clustering-Appearances;:Lambertian-Reflectance.

: Feature points on a moving rigid body lie on an affine space of dimension three, assuming the affine camera model:Multibody-Factorization. More generally, estimating structure from motion involves estimating low-rank matrices (:Efficient-Computation Sec. 5.2).

: We can describe a large corpus of documents that concern a small number of topics using a low-dimensional linear model DDL+88:Improving-Information.

This paper describes a new technique for fitting a low-dimensional linear model to data. Our formulation is based on convex optimization, but it has a different flavor from the earlier techniques. We use a new set of ideas to develop a rigorous analysis of the performance of our method. This theory demonstrates that the approach is robust against noise in the inliers, and it can cope with a large number of adversarial outliers. We describe an efficient numerical algorithm that is guaranteed to solve the optimization problem after a modest number of spectral calculations.
