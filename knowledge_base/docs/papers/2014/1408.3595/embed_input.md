Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints

Topics include Semidefinite programming, Stability analysis, Robustness, Optimization, Control, IQC.

This manuscript develops a new framework to analyze and design iterative optimization algorithms built on the notion of Integral Quadratic Constraints (IQC) from robust control theory. IQCs provide sufficient conditions for the stability of complicated interconnected systems, and these conditions can be checked by semidefinite programming. We discuss how to adapt IQC theory to study optimization algorithms, proving new inequalities about convex functions and providing a version of IQC theory adapted for use by optimization researchers. Using these inequalities, we derive numerical upper bounds on convergence rates for the gradient method, the heavy-ball method, Nesterov's accelerated method, and related variants by solving small, simple semidefinite programming problems. We also briefly show how these techniques can be used to search for optimization algorithms with desired performance characteristics, establishing a new methodology for algorithm design.

## Introduction

Convex optimization algorithms provide a powerful toolkit for robust, efficient, large-scale optimization algorithms. They provide not only effective tools for solving optimization problems, but are guaranteed to converge to accurate solutions in provided time budgets, are robust to errors and time delays, and are amendable to declarative modeling that decouples the algorithm design from the problem formulation.

This paper marks an attempt at providing a systematized approach to the design and analysis optimization algorithms using techniques from control theory. Our strategy is to adapt the notion of an *integral quadratic constraint* from robust control theory. These constraints link sequences of inputs and outputs of operators, and are ideally suited to proving algorithmic convergence.

Our methods are inspired by the recent work of Drori and Teboulle. In their manuscript, the authors propose writing down the first-order convexity inequality for all steps of an algorithmic procedure. They then derive a semidefinite program that analytically verifies very tight bounds for the convergence rate for the Gradient method, and numerically precise bounds for convergence of Nesterov's method and other first-order methods. The main drawback of the Drori and Teboulle approach is that the size of the semidefinite program scales with the number of time steps desired.

We are able to analyze a variety of methods in our framework. We show that our framework recovers the standard rates of convergence for the Gradient method applied to strongly convex functions. We show that we can numerically estimate the performance of Nesterov's method. Indeed, our analysis provides slightly sharper bounds than Nesterov's proof. We show how our system fails to certify the stability of the popular Heavy-ball method of Polyak for strongly convex functions whose condition ratio is larger than 18.

## Future work

We are only beginning to get a sense of what IQCs can tell us about optimization schemes, and there are many more control theory tools and techniques left to adapt to the context of optimization and machine learning. We conclude this paper with several interesting directions for future work.
