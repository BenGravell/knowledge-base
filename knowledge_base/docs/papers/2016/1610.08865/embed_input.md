Hit-and-Run for Sampling and Planning in Non-Convex Spaces

We propose the Hit-and-Run algorithm for planning and sampling problems in non-convex spaces. For sampling, we show the first analysis of the Hit-and-Run algorithm in non-convex spaces and show that it mixes fast as long as certain smoothness conditions are satisfied. In particular, our analysis reveals an intriguing connection between fast mixing and the existence of smooth measure-preserving mappings from a convex space to the non-convex space. For planning, we show advantages of Hit-and-Run compared to state-of-the-art planning methods such as Rapidly-Exploring Random Trees.

## Introduction

Rapidly-Exploring Random Trees (RRT) is one of the most popular planning algorithms, especially when the search space is high-dimensional and finding the optimal path is computationally expensive. RRT performs well on many problems where classical dynamic programming based algorithms, such as A\*, perform poorly. RRT is essentially an exploration algorithm, and in the most basic implementation, the algorithm even ignores the goal information, which seems to be a major reason for its success....

Although many attempts have been made to improve the basic algorithm, RRT has proven difficult to improve upon. In fact, given extra computation, repeatedly running RRT often produces competitive solutions. In this paper, we show that a simple alternative greatly improves upon RRT. We propose using the Hit-and-Run algorithm for feasible path search. Arguably simpler than RRT, the Hit-and-Run is a rapidly mixing MCMC sampling algorithm for producing a point uniformly at random from a convex space. color=blue!20!white,\]Victor: not that clear, you mean hnr is simpler that RRT?...

This paper has two main contributions. First, we use a measure-preserving bilipschitz map to extend the analysis of the Hit-and-Run random walk to non-convex sets. Mixing time bounds for non-convex sets open up many applications, for example non-convex optimization via simulated annealing and similar methods. The second contribution of this paper has been to study one such application: the planning problem.

In contrast to RRT, using Hit-and-Run for planning has stronger guarantees on the number of samples needed and faster convergence in some cases. It also avoids the need for a sampling oracle for $\Sigma$, since it combines the search with an approximate sampling oracle. One drawback is that the sample paths for Hit-and-Run have no pruning and are therefore longer than the RRT paths. Hybrid approaches that yield short paths but also explore quickly are a promising future direction.

### Theorem 7 (Theorem 4.5 of Vempala )

## Analysis

### Lemma 10

Before giving more details, we define the planning and sampling problems that we consider. Let $\Sigma$ be a bounded connected subset of ${\mathbb{R}}^{n}$. For points ${a,b} \in \Sigma$, we use $\lbrack a,b\rbrack$ to denote their (one-dimensional) convex hull....
