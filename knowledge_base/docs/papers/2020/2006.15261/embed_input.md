<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Picasso: A Sparse Learning Library for High Dimensional Data Analysis in R and Python

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a new library named picasso, which implements a unified framework of pathwise coordinate optimization for a variety of sparse learning problems (e.g., sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression) combined with efficient active set selection strategies. Besides, the library allows users to choose different sparsity-inducing regularizers, including the convex l_1, nonconvex MCP and SCAD regularizers. The library is coded in C++ and has user-friendly R and Python wrappers. Numerical experiments demonstrate that picasso can scale up to large problems efficiently.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

We describe a new library named picasso ^11^1More details can be found in our Github page: which implements a unified framework of pathwise coordinate optimization for a variety of sparse learning problems (e.g., sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression) combined with efficient active set selection strategies. Besides, the library allows users to choose different sparsity-inducing regularizers, including the convex $\ell_{1}$, nonvoncex MCP and SCAD regularizers. The library is coded in C++ and has user-friendly R and Python wrappers. Numerical experiments demonstrate that picasso can scale up to large problems efficiently.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Overview", "weight": 1.0} -->

Sparse Learning arises due to the demand of analyzing high-dimensional data such as high-throughput genomic data and functional Magnetic Resonance Imaging. The pathwise coordinate optimization is undoubtedly one the of the most popular solvers for a large variety of sparse learning problems. By leveraging the solution sparsity through a simple but elegant algorithmic structure, it significantly boosts the computational performance in practice. Some recent progresses in establish theoretical guarantees to further justify its computational and statistical superiority for both convex and nonvoncex sparse learning, which makes it even more attractive to practitioners.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Overview", "weight": 1.0} -->

We recently developed a new library named picasso, which implements a unified toolkit of pathwise coordinate optimization for solving a large class of convex and nonconvex regularized sparse learning problems. Efficient active set selection strategies are provided to guarantee superior statistical and computational preference. Specifically, we implement sparse linear regression, sparse logistic regression, sparse Poisson regression and scaled sparse linear regression. The options of regularizers include the $\ell_{1}$, MCP, and SCAD regularizers. Unlike existing libraries implementing heuristic optimization algorithms such as ncvreg or glmnet, our implemented algorithm picasso have strong theoretical guarantees that it attains a global linear convergence to a unique sparse local optimum with optimal statistical properties (e.g. minimax optimality and oracle properties). See more details in Zhao et al.; Li et al..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Algorithm Design and Implementation", "weight": 1.0} -->

The algorithm implemented in picasso is mostly based on the generic pathwise coordinate optimization framework proposed by Zhao et al.; Li et al., which integrates the warm start initialization, active set selection strategy, and strong rule for coordinate preselection into the classical coordinate optimization. The algorithm contains three structurally nested loops as shown in Figure 1: \(1\) Outer loop: The warm start initialization, also referred to as the pathwise optimization scheme, is applied to minimize the objective function in a multistage manner using a sequence of decreasing regularization parameters, which yields a sequence of solutions from sparse to dense. At each stage, the algorithm uses the solution from the previous stage as initialization.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Algorithm Design and Implementation", "weight": 1.0} -->

\(2\) Middle loop: The algorithm first divides all coordinates into active ones (active set) and inactive ones (inactive set) by a so-called strong rule based on coordinate gradient thresholding. Then the algorithm calls an inner loop to optimize the objective, and update the active set based on efficient active set selection strategies. Such a routine is repeated until the active set no longer changes \(3\) Inner loop: The algorithm conducts coordinate optimization (for sparse linear regression) or proximal Newton optimization combined with coordinate optimization (for sparse logistic regression, Possion regression, scaled sparse linear regression, sparse undirected graph estimation) only over active coordinates until convergence, with all inactive coordinates staying zero values. The active coordinates are updated efficiently using an efficient "naive update" rule that only operates on the non-zero coefficients. Better efficiency is achieved by the "covariance update" rule. See more details. The inner loop terminates when the successive descent is within a predefined numerical precision.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Algorithm Design and Implementation", "weight": 1.0} -->

The warm start initialization, active set selection strategies, and strong rule for coordinate preselection significantly boost the computational performance, making pathwise coordinate optimization one of the most important computational frameworks for sparse learning. The numerical evaluations show that picasso is highly scalable and efficient.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Algorithm Design and Implementation", "weight": 1.0} -->

The library is implemented in C++ with the memory optimized using sparse matrix output, and called from R and Python by user-friendly interfaces. Linear algebra is supported by the Eigen3 library for portable high performance computation. The implementation is modularized so that the algorithm in src/solver/actnewton.cpp works with popular sparsity-inducing regularizer functions and any convex objective function that exhibits restricted strong convexity property. Users can easily extend the package by writing customized objective function subclass and regularizer function subclass following the virtual function interfaces of class ObjFunction and class RegFunction in include/picasso/objective.hpp.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Example of R User Interface", "weight": 1.0} -->

We illustrate the user interface by analyzing the eye disease data set in picasso.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Example of R User Interface", "weight": 1.0} -->

> library(picasso); data(eyedata) # Load the data set > out1 = picasso(x,y,method="l1",type.gaussian="naive",nlambda=20, + lambda.min.ratio=0.2) # Lasso > out2 = picasso(x,y,method="mcp", gamma = 1.25, prec=1e-4) # MCP regularizer > plot(out1); plot(out2) # Plot solution paths The program automatically generates a sequence of regularization parameters and estimate the corresponding solution paths based on the $\ell_{1}$ and MCP regularizers respectively. For the $\ell_{1}$ regularizer, we set the number of regularization parameters as 20, and the minimum regularization parameter as 0.2\*lambda.max. For the MCP regularizer, we set the concavity parameter as $\gamma = 1.25$, and the pre-defined accuracy as $10^{- 4}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example of R User Interface", "weight": 1.0} -->

Here nlambda and lambda.min.ratio are omitted, and therefore set by the default values (nlambda=100 and lambda.min.ratio=0.05). We further plot two solution paths in Figure 2.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

To demonstrate the superior efficiency of our library, we compare picasso with a popular R library ncvreg (version 3.9.1) for nonconvex regularized sparse regression, the most popular R library glmnet (version 2.0-13) for convex regularized sparse regression, and two R libraries scalreg-v1.0 and flare-v1.5.0 for scaled sparse linear regression. All experiments are evaluated on an Intel Core CPU i7-7700k 4.20GHz and under R version 3.4.3. Timings of the CPU execution are recored in seconds and averaged over 10 replications on a sequence of 100 regularization parameters. All algorithms are compared on the same regularization path and the convergence threshold are adjusted so that similar objective gaps are achieved.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

We compare the timing performance and the optimization performance in Table 4. We choose the problem size to be $({{n = 3000},{d = 30000}})$, where $n$ is the number of observation and $d$ is the dimension of the parameter vector. We tests the algorithms for both well-conditioned cases and ill-conditioned cases. The details of data generation can be found in the R library vignette. Here is our summary: \(1\) For sparse linear regression using any regularizer and sparse logistic regression using the $\ell_{1}$ regularizer, all libraries achieve almost identical optimization objective values, and picasso slightly outperforms glmnet and ncvreg in the timing performance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

\(2\) For sparse logistic regression using nonconvex regularizers, picasso achieves comparable objective value with ncvreg, and significantly outperforms ncvreg in timing performance. We also remark that picasso performs stably for various settings and tuning parameters. However, ncvreg may converge very slow or fail to converge for sparse logistic regression using nonconvex regularizers, especially when the tuning parameters are relatively small (corresponding to denser estimators), as the ill-conditioned SCAD case shows.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

\(3\) For scaled Lasso, in order to make other competitors (flare and scalreg) converges in resonable time, we swtich to a smaller problem size $({{n = 1000},{d = 10000}})$. We see that picasso much more time saving than flare and scalreg.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

Sparse Linear Regression Sparse Logistic Regression Figure 2: The solution paths of ℓ1 (up) and MCP (down) regularizers.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The picasso library demonstrates significantly improved computational and statistical performance over existing libraries for nonconvex regularized sparse learning such as ncvreg. Besides, picasso also shows improvement over the popular libraries for convex regularized sparse learning such as glmnet. Overall, the picasso library has the potential to serve as a powerful toolbox for high dimensional sparse learning. We will continue to maintain and support this library.
