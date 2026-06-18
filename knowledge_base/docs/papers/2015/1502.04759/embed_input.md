Coordinate Descent Algorithms

Topics include Attention mechanisms, Optimization, Learning, Coordinate descent.

Coordinate descent algorithms solve optimization problems by successively performing approximate minimization along coordinate directions or coordinate hyperplanes. They have been used in applications for many years, and their popularity continues to grow because of their usefulness in data analysis, machine learning, and other areas of current interest. This paper describes the fundamentals of the coordinate descent approach, together with variants and extensions and their convergence properties, mostly with reference to convex objectives. We pay particular attention to a certain problem structure that arises frequently in machine learning applications, showing that efficient implementations of accelerated coordinate descent algorithms are possible for problems of this type. We also present some parallel variants and discuss their convergence properties under several models of parallel execution.

## Introduction

Coordinate descent (CD) algorithms for optimization have a history that dates to the foundation of the discipline. They are iterative methods in which each iterate is obtained by fixing most components of the variable vector $x$ at their values from the current iteration, and approximately minimizing the objective with respect to the remaining components. Each such subproblem is a lower-dimensional (even scalar) minimization problem, and thus can typically be solved more easily than the full problem.

CD methods are the archetype of an almost universal approach to algorithmic optimization: solving an optimization problem by solving a sequence of simpler optimization problems. The obviousness of the CD approach and its acceptable performance in many situations probably account for its long-standing appeal among practitioners. Paradoxically, the apparent lack of sophistication may also account for its unpopularity as a subject for investigation by optimization researchers, who have usually been quick to suggest alternative approaches in any given situation. There are some very notable exceptions....

We have surveyed the state of the art in convergence of coordinate descent methods, with a focus on the most elementary settings and the most fundamental algorithms. The recent literature contains many extensions, enhancements, and elaborations; we refer interested readers to the bibliography of this paper, and note that new works are appearing at a rapid pace.

Coordinate descent method have become an important tool in the optimization toolbox that is used to solve problems that arise in machine learning and data analysis, particularly in "big data" settings. We expect to see further developments and extensions, further customization of the approach to specific problem structures, further adaptation to various computer platforms, and novel combinations with other optimization tools to produce effective "solutions" for key application areas.

It is worth proving an expected linear convergence result for the Kaczmarz iteration for linear equations ${Aw} = b$ as a separate, more elementary analysis. In one sense, the result is a special case of Theorem 3.1 since, as we showed above, the iteration is obtained by applying Algorithm 3 to the dual formulation....
