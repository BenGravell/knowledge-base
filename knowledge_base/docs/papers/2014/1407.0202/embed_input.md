SAGA: A Fast Incremental Gradient Method with Support for Non-Strongly Convex Composite Objectives

Topics include SAGA, Variance reduction, Incremental gradient methods, Finite-sum optimization, Composite optimization, Proximal methods, Non-strongly convex optimization.

Introduces SAGA, an unbiased table-based variance-reduced incremental-gradient method that bridges ideas from SAG, SDCA, and SVRG. Its main contribution is a tighter and more flexible theory covering composite objectives, direct non-strongly-convex use, and automatic adaptation to inherent strong convexity.

In this work we introduce a new optimisation method called SAGA in the spirit of SAG, SDCA, MISO and SVRG, a set of recently proposed incremental gradient algorithms with fast linear convergence rates. SAGA improves on the theory behind SAG and SVRG, with better theoretical convergence rates, and has support for composite objectives where a proximal operator is used on the regulariser. Unlike SDCA, SAGA supports non-strongly convex problems directly, and is adaptive to any inherent strong convexity of the problem. We give experimental results showing the effectiveness of our method.

## Introduction

Remarkably, recent advances have shown that it is possible to minimise strongly convex finite sums provably faster in expectation than is possible without the finite sum structure. This is significant for machine learning problems as a finite sum structure is common in the empirical risk minimisation setting. The requirement of strong convexity is likewise satisfied in machine learning problems in the typical case where a quadratic regulariser is used.

In particular, we are interested in minimising functions of the form

where $x \in {\mathbb{R}}^{d}$, each $f_{i}$ is convex and has Lipschitz continuous derivatives with constant $L$.

where $h:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is convex but potentially non-differentiable, and where the proximal operation of $h$ is easy to compute --- few incremental gradient methods are applicable in this setting.

Our contributions are as follows. In Section 2 we describe the SAGA algorithm, a novel incremental gradient method. In Section 5 we prove theoretical convergence rates for SAGA in the strongly convex case better than those for SAG and SVRG, and a factor of 2 from the SDCA convergence rates. These rates also hold in the composite setting. Additionally, we show that like SAG but unlike SDCA, our method is applicable to non-strongly convex problems without modification. We establish theoretical convergence rates for this case also.
