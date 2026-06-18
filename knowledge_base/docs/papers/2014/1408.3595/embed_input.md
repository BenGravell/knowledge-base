Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints

Topics include Semidefinite programming, Stability analysis, Robustness, Optimization, Control, IQC.

This manuscript develops a new framework to analyze and design iterative optimization algorithms built on the notion of Integral Quadratic Constraints (IQC) from robust control theory. IQCs provide sufficient conditions for the stability of complicated interconnected systems, and these conditions can be checked by semidefinite programming. We discuss how to adapt IQC theory to study optimization algorithms, proving new inequalities about convex functions and providing a version of IQC theory adapted for use by optimization researchers. Using these inequalities, we derive numerical upper bounds on convergence rates for the gradient method, the heavy-ball method, Nesterov's accelerated method, and related variants by solving small, simple semidefinite programming problems. We also briefly show how these techniques can be used to search for optimization algorithms with desired performance characteristics, establishing a new methodology for algorithm design.

## Introduction

Convex optimization algorithms provide a powerful toolkit for robust, efficient, large-scale optimization algorithms. They provide not only effective tools for solving optimization problems, but are guaranteed to converge to accurate solutions in provided time budgets, are robust to errors and time delays, and are amendable to declarative modeling that decouples the algorithm design from the problem formulation....

This paper marks an attempt at providing a systematized approach to the design and analysis optimization algorithms using techniques from control theory. Our strategy is to adapt the notion of an *integral quadratic constraint* from robust control theory. These constraints link sequences of inputs and outputs of operators, and are ideally suited to proving algorithmic convergence....

### Large-scale composite system analysis

Perhaps the most ambitious goal of this program is to move beyond convex models and attempt to analyze complicated optimization systems used in science and industry. Powerful modeling languages like AMPL or GAMS allow for local analysis of large, complex systems, and certifying that the decisions about these systems are valid and safe would have impact in a variety of fields including process technology, web-scale analytics, and power management....

Now note that if we take a convex combination of the inequalities (3.19. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) corresponding to each off-by-$j$ IQC and let the associated coefficient be $h_{j}$, we have proven (3.19. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) for the case of a general sequence $h_{1},h_{2},\ldots$.

We now make several comments regarding Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints").

We computed the rate bounds using Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") using...
