Asymptotically Optimal Sampling-Based Motion Planning Methods

Topics include Survey, Robotics, Motion planning, Robot motion planning, Sampling-based planning, Optimal motion planning, Asymptotically optimal.

Motion planning is a fundamental problem in autonomous robotics that requires finding a path to a specified goal that avoids obstacles and takes into account a robot's limitations and constraints. It is often desirable for this path to also optimize a cost function, such as path length. Formal path-quality guarantees for continuously valued search spaces are an active area of research interest. Recent results have proven that some sampling-based planning methods probabilistically converge toward the optimal solution as computational effort approaches infinity. This article summarizes the assumptions behind these popular asymptotically optimal techniques and provides an introduction to the significant ongoing research on this topic.

## INTRODUCTION

Planning is an important task in a number of fields, including computer science and robotics. It consists of finding a sequence of valid states (i.e., a path) between specified positions (i.e., a start and goal) in a search space. Many problems have multiple *feasible* solutions and applications often seek the feasible path that optimizes a cost function (i.e., the *optimal* solution). A feasible solution in robot motion planning is a path that avoids hazards in the environment (i.e., obstacles) and can be followed by the robot (e.g., is kinodynamically feasible)....

Optimal planning is difficult because there are often a large number of states to consider and it can be computationally expensive to evaluate them. Graph-search algorithms, such as A\*, can search discrete spaces (e.g., graphs) efficiently with strong formal guarantees. These techniques are guaranteed to find the optimal solution, if one exists, and otherwise return failure (i.e., they are *complete* and *optimal*). A\* is also guaranteed to expand no more states than any other optimal algorithm given the same information \i.e., it is *optimally efficient*;.

## DISCLOSURE STATEMENT

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review.

Formally analyzing the asymptotic optimality of kinodynamic motion planning algorithms requires additional assumptions that are not summarized here. These include statements about the controllability of the dynamical system, the nature of the cost function, and other properties of the problem, including whether the dynamical equation can be solved analytically for arbitrary end conditions (i.e., the existence of a 'steering' function). Kinodynamic motion planning is often considered in the presence of kinodynamic constraints (Section 3.3.3).

Karaman and Frazzoli note that all planning algorithms are provably either asymptotically optimal with probability one or zero \i.e., almost surely or almost never; Lemma 25 {extract}a sampling-based algorithm either converges to the optimal solution in almost all runs, or the convergence does not occur in almost all runs....
