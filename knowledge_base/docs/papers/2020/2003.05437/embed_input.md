Matrix Concentration for Products

This paper develops nonasymptotic growth and concentration bounds for a product of independent random matrices. These results sharpen and generalize recent work of Henriksen-Ward, and they are similar in spirit to the results of Ahlswede-Winter and of Tropp for a sum of independent random matrices. The argument relies on the uniform smoothness properties of the Schatten trace classes.

## Abstract

This paper develops nonasymptotic growth and concentration bounds for a product of independent random matrices. These results sharpen and generalize recent work of Henriksen--Ward, and they are similar in spirit to the results of Ahlswede--Winter and of Tropp for a sum of independent random matrices. The argument relies on the uniform smoothness properties of the Schatten trace classes.

The authors gratefully acknowledge the funding for this work. DH was supported under NSF grant DMS-1613861. JNW and RW were supported in part by the Institute for Advanced Study, where some of this research was conducted. JAT was supported under ONR Awards N00014-17-1-2146 and N00014-18-1-2363. RW also received support from AFOSR MURI Award N00014-17-S-F006.

## Motivation

Products of random matrices arise in many contemporary applications in the mathematics of data science. For instance, they describe the evolution of stochastic linear dynamical systems, which include popular stochastic algorithms for optimization such as Oja's algorithm for streaming principal component analysis and the randomized Kaczmarz method for solving linear systems. To understand the detailed behavior of these algorithms, such as the rate of convergence, we may seek out methods for studying a product of random matrices.

Unfortunately, the tools currently available in the literature are poorly adapted to these circumstances. Indeed, an instantiation of a stochastic optimization algorithm involves a finite product of finite-dimensional matrices, often with a particular structure (e.g., low-rank perturbations of the identity). But most existing theoretical results are limit laws that require the number of factors in the product or the dimension of the factors to tend to infinity. Furthermore, strong assumptions on the random matrices (e.g., independent and identically distributed entries) are usually required.
