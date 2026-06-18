Inside Madupite: Technical Design and Performance

Topics include Benchmarks, Scalability, Distributed systems, Optimization, Control, Inside madupite, Markov decision process.

In this work, we introduce and benchmark madupite, a newly proposed high-performance solver designed for large-scale discounted infinite-horizon Markov decision processes with finite state and action spaces. After a brief overview of the class of mathematical optimization methods on which madupite relies, we provide details on implementation choices, technical design and deployment. We then demonstrate its scalability and efficiency by showcasing its performance on the solution of Markov decision processes arising from different application areas, including epidemiology and classical control. Madupite sets a new standard as, to the best of our knowledge, it is the only solver capable of efficiently computing exact solutions for large-scale Markov decision processes, even when these exceed the memory capacity of modern laptops and operate in near-undiscounted settings. This is possible as madupite can work in a fully distributed manner and therefore leverage the memory storage and computation capabilities of modern high-performance computing clusters....

## INTRODUCTION

Markov Decision Processes (MDPs) offer a powerful and general mathematical framework for modeling sequential decision-making problems across a wide range of fields, including epidemiology \[\], finance \[\], robotics \[\] and agriculture \[\]. Dynamic programming, introduced by Bellman in the 1950s, remains a foundational method for solving MDPs \[\]. However, practical applications of dynamic programming algorithms face significant challenges, as they typically suffer from slow convergence in high discount factor regimes or limited scalability in large-scale settings \[\]....

Recent advances in algorithmic design have introduced inexact policy iteration (iPI) methods, a new class of dynamic programming techniques that overcome some of the traditional limitations by achieving rapid convergence, even in scenarios with discount factors approaching one. Nevertheless, solving large-scale MDPs requires more than algorithmic advances, it demands leveraging high-performance computing (HPC) platforms. Distributed and parallel implementations are crucial for harnessing the full computational power of modern HPC clusters....

We presented the technical details and implementation choices behind madupite, and clarified the connection between its user-selectable parameters and the underlying mathematical algorithmic framework. We also thoroughly demonstrated its performance, comparing it against existing SOTA solvers to highlight its superior efficiency. Our evaluation includes standard metrics such as strong scaling, as well as case studies, both inherently discrete and obtained by discretizing a continuous MDP....

A promising future direction is extending the codebase to support risk-averse MDPs, as the solution methods proposed in \[\] are highly parallelizable and well-suited to madupite's framework.

-ksp_max_it 1 -ksp_richardson_scale β

Matrix is distributed such that all $P{(s, \cdot, \cdot )}$ associated to the same state $s$ are stored in the same rank. Therefore in each rank we store a coherent chunk of consecutive rows from. To compute the precise number of rows, we first compute the local number of states stored on each rank by keeping a balanced load over the ranks. Assuming that we distribute the $n$ states across $R$ ranks, then the local number of states for rank $\rho$ is computed as follow
