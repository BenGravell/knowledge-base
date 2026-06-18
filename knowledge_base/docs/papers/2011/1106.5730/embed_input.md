HOGWILD! : A Lock-Free Approach to Parallelizing Stochastic Gradient Descent

Topics include Stochastic gradient descent, Parallel optimization, Lock-free algorithms, Sparse updates, Shared memory, Machine learning systems, Asynchronous optimization.

Shows that SGD can be parallelized without locks when gradient updates are sparse enough that write conflicts are limited. The paper combines convergence analysis with a simple shared-memory implementation, making HOGWILD! an influential baseline for asynchronous optimization on multicore hardware.

Stochastic Gradient Descent (SGD) is a popular algorithm that can achieve state-of-the-art performance on a variety of machine learning tasks. Several researchers have recently proposed schemes to parallelize SGD, but all require performance-destroying memory locking and synchronization. This work aims to show using novel theoretical analysis, algorithms, and implementation that SGD can be implemented without any locking. We present an update scheme called HOGWILD! which allows processors access to shared memory with the possibility of overwriting each other's work. We show that when the associated optimization problem is sparse, meaning most gradient updates only modify small parts of the decision variable, then HOGWILD! achieves a nearly optimal rate of convergence. We demonstrate experimentally that HOGWILD! outperforms alternative schemes that use locking by an order of magnitude.

## Introduction

With its small memory footprint, robustness against noise, and rapid learning rates, Stochastic Gradient Descent (SGD) has proved to be well suited to data-intensive machine learning tasks. However, SGD's scalability is limited by its inherently sequential nature; it is difficult to parallelize. Nevertheless, the recent emergence of inexpensive multicore processors and mammoth, web-scale data sets has motivated researchers to develop several clever parallelization schemes for SGD.

For some data sets, the sheer size of the data dictates that one use a cluster of machines. However, there are a host of problems in which, after appropriate preprocessing, the data necessary for statistical analysis may consist of a few terabytes or less. For such problems, one can use a single inexpensive work station as opposed to a hundred thousand dollar cluster.

In this work, we propose a simple strategy for eliminating the overhead associated with locking: *run SGD in parallel without locks*, a strategy that we call Hogwild!. In Hogwild!, processors are allowed equal access to shared memory and are able to update individual components of memory at will. Such a lock-free scheme might appear doomed to fail as processors could overwrite each other's progress.

In Section 2, we formalize a notion of sparsity that is sufficient to guarantee such a speedup and provide canonical examples of sparse machine learning problems in classification, collaborative filtering, and graph cuts. Our notion of sparsity allows us to provide theoretical guarantees of linear speedups in Section 4. As a by-product of our analysis, we also derive rates of convergence for algorithms with constant stepsizes. We demonstrate that robust $1/k$ convergence rates are possible with constant stepsize schemes that implement an exponential back-off in the constant over time.

In practice, we find that computational performance of a lock-free procedure exceeds even our theoretical guarantees. We experimentally compare lock-free SGD to several recently proposed methods. We show that all methods that propose memory locking are significantly slower than their respective lock-free counterparts on a variety of machine learning applications.
