Matrix Concentration for Products

This paper develops nonasymptotic growth and concentration bounds for a product of independent random matrices. These results sharpen and generalize recent work of Henriksen-Ward, and they are similar in spirit to the results of Ahlswede-Winter and of Tropp for a sum of independent random matrices. The argument relies on the uniform smoothness properties of the Schatten trace classes.

## Abstract

This paper develops nonasymptotic growth and concentration bounds for a product of independent random matrices. These results sharpen and generalize recent work of Henriksen--Ward, and they are similar in spirit to the results of Ahlswede--Winter and of Tropp for a sum of independent random matrices. The argument relies on the uniform smoothness properties of the Schatten trace classes.

The authors gratefully acknowledge the funding for this work. DH was supported under NSF grant DMS-1613861. JNW and RW were supported in part by the Institute for Advanced Study, where some of this research was conducted. JAT was supported under ONR Awards N00014-17-1-2146 and N00014-18-1-2363. RW also received support from AFOSR MURI Award N00014-17-S-F006.

However, when the matrices ${\mathbf{X}}_{i}$ commute almost surely, it is easy to show the sharper bound

but the error term is not sharp. This type of bound would echo Tropp's improvements to the Ahlswede--Winter results for a sum of independent random matrices. At present, it is not clear whether this refinement is possible, nor what technical arguments would lead there.

In the final step, we use the assumption that ${\mathbf{Z}}_{0}$ is not random to see that ${\|\left| {\mathbf{Z}}_{0} \right|\|}_{p,q} = \left\| {\mathbf{Z}}_{0} \right\|_{p}$. For $i = n$, the formula (5.7. ‣ 5.2. Growth and Concentration ‣ 5. A Product of Independent Random Matrices ‣ Matrix Concentration for Products")) is the advertised result. ∎

### Subquadratic Averages for Random Matrices

To motivate this development, observe that random perturbations of the identity arise from the analysis of the iterative scheme

## Motivation

Products of random matrices arise in many contemporary applications in the mathematics of data science. For instance, they describe the evolution of stochastic linear dynamical systems, which include popular stochastic algorithms for optimization such as Oja's algorithm for streaming principal component analysis and the randomized Kaczmarz method for solving linear systems. To understand the detailed behavior of these algorithms, such as the rate of convergence, we may seek out methods for studying a product of random matrices.

Unfortunately, the tools currently available in the literature are poorly adapted to these circumstances....
