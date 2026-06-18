HOGWILD! : A Lock-Free Approach to Parallelizing Stochastic Gradient Descent

Topics include Stochastic gradient descent, Parallel optimization, Lock-free algorithms, Sparse updates, Shared memory, Machine learning systems, Asynchronous optimization.

Shows that SGD can be parallelized without locks when gradient updates are sparse enough that write conflicts are limited. The paper combines convergence analysis with a simple shared-memory implementation, making HOGWILD! an influential baseline for asynchronous optimization on multicore hardware.

Stochastic Gradient Descent (SGD) is a popular algorithm that can achieve state-of-the-art performance on a variety of machine learning tasks. Several researchers have recently proposed schemes to parallelize SGD, but all require performance-destroying memory locking and synchronization. This work aims to show using novel theoretical analysis, algorithms, and implementation that SGD can be implemented without any locking. We present an update scheme called HOGWILD! which allows processors access to shared memory with the possibility of overwriting each other's work. We show that when the associated optimization problem is sparse, meaning most gradient updates only modify small parts of the decision variable, then HOGWILD! achieves a nearly optimal rate of convergence. We demonstrate experimentally that HOGWILD! outperforms alternative schemes that use locking by an order of magnitude.

## Introduction

With its small memory footprint, robustness against noise, and rapid learning rates, Stochastic Gradient Descent (SGD) has proved to be well suited to data-intensive machine learning tasks. However, SGD's scalability is limited by its inherently sequential nature; it is difficult to parallelize. Nevertheless, the recent emergence of inexpensive multicore processors and mammoth, web-scale data sets has motivated researchers to develop several clever parallelization schemes for SGD....

For some data sets, the sheer size of the data dictates that one use a cluster of machines. However, there are a host of problems in which, after appropriate preprocessing, the data necessary for statistical analysis may consist of a few terabytes or less. For such problems, one can use a single inexpensive work station as opposed to a hundred thousand dollar cluster....

Our Hogwild! schemes can be generalized to problems where some of the variables occur quite frequently as well. We could choose to not update certain variables that would be in particularly high contention. For instance, we might want to add a bias term to our Support Vector Machine, and we could still run a Hogwild! scheme, updating the bias only every thousand iterations or so.

For future work, it would be of interest to enumerate structures that allow for parallel gradient computations with no collisions at all. That is, it may be possible to bias the SGD iterations to completely avoid memory contention between processors. For example, recent work proposed a biased ordering of the stochastic gradients in matrix completion problems that completely avoids memory contention between processors. An investigation into how to generalize this approach to other structures and problems would enable even faster computation of machine learning problems.

and $c_{r}$ and $B$ are constants. This recursion underlies many convergence proofs for SGD where $a_{k}$ denotes the distance to the optimal solution after $k$ iterations. We will derive appropriate constants for Hogwild! in the Appendix. We will also discuss below what these constants are for standard stochastic gradient descent algorithms.

We now turn to our theoretical analysis of Hogwild! protocols. To make the analysis tractable, we assume that we update with the following "with replacement" procedure: each processor samples an edge $e$...
