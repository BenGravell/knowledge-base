Coordinate Descent Algorithms

Topics include Attention mechanisms, Optimization, Learning, Coordinate descent.

Coordinate descent algorithms solve optimization problems by successively performing approximate minimization along coordinate directions or coordinate hyperplanes. They have been used in applications for many years, and their popularity continues to grow because of their usefulness in data analysis, machine learning, and other areas of current interest. This paper describes the fundamentals of the coordinate descent approach, together with variants and extensions and their convergence properties, mostly with reference to convex objectives. We pay particular attention to a certain problem structure that arises frequently in machine learning applications, showing that efficient implementations of accelerated coordinate descent algorithms are possible for problems of this type. We also present some parallel variants and discuss their convergence properties under several models of parallel execution.

## Introduction

Coordinate descent (CD) algorithms for optimization have a history that dates to the foundation of the discipline. They are iterative methods in which each iterate is obtained by fixing most components of the variable vector $x$ at their values from the current iteration, and approximately minimizing the objective with respect to the remaining components. Each such subproblem is a lower-dimensional (even scalar) minimization problem, and thus can typically be solved more easily than the full problem.

Our approach throughout is to describe the CD methods in their simplest forms, to illustrate the fundamentals of the applications, implementations, and analysis. We focus almost exclusively on methods that adjust just one coordinate on each iteration. Most applications use block coordinate descent methods, which adjust groups of blocks of indices at each iteration, thus searching along a coordinate hyperplane rather than a single coordinate direction. Most derivation and analysis of single-coordinate descent methods can be extended without great difficulty to the block-CD setting; the concepts do not change fundamentally.

## Conclusion

We have surveyed the state of the art in convergence of coordinate descent methods, with a focus on the most elementary settings and the most fundamental algorithms. The recent literature contains many extensions, enhancements, and elaborations; we refer interested readers to the bibliography of this paper, and note that new works are appearing at a rapid pace.

Coordinate descent method have become an important tool in the optimization toolbox that is used to solve problems that arise in machine learning and data analysis, particularly in "big data" settings. We expect to see further developments and extensions, further customization of the approach to specific problem structures, further adaptation to various computer platforms, and novel combinations with other optimization tools to produce effective "solutions" for key application areas.
