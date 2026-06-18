From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs

In this paper we present a review of the connections between classical algorithms for solving Markov Decision Processes (MDPs) and classical gradient-based algorithms in convex optimization. Some of these connections date as far back as the 1980s, but they have gained momentum in recent years and have lead to faster algorithms for solving MDPs. In particular, two of the most popular methods for solving MDPs, Value Iteration and Policy Iteration, can be linked to first-order and second-order methods in convex optimization. In addition, recent results in quasi-Newton methods lead to novel algorithms for MDPs, such as Anderson acceleration. By explicitly classifying algorithms for MDPs as first-order, second-order, and quasi-Newton methods, we hope to provide a better understanding of these algorithms, and, further expanding this analogy, to help to develop novel algorithms for MDPs, based on recent advances in convex optimization.

## Introduction

Markov Decision Process (MDP) is a common framework modeling dynamic optimization problems, with applications ranging from reinforcement learning to healthcare and wireless sensor networks. Most of the algorithms for computing an optimal control policy are variants of two algorithms: Value Iteration (VI) and Policy Iteration (PI). Over the last 40 years, a number of works have highlighted the strong connections between these algorithms and methods from convex optimization, even though computing an optimal policy is a non-convex problem.

## Outline

We introduce the MDP framework as well as the classical Value Iteration and Policy Iteration algorithms in Section 2 ‣ From Convex Optimization to MDPs: A Review of First-Order, Second-Order and Quasi-Newton Methods for MDPs"). We highlight the recent connections between Value Iteration and first-order methods (Gradient Descent) in Section 3. The relations between Policy Iteration and second-order methods (Newton's method) are presented in Section 4. We review Anderson Value Iteration, a quasi-Newton methods for MDPs, in Section 5.

## Notations

In this paper, $n$ and $A$ denote integers in $\mathbb{N}$. The notation $\Delta{(A)}$ refers to the simplex of size $A$. We write $\lbrack n\rbrack$ for the set $\{ 1,\ldots,n\}$.

## Setting and notations

A (stationary) policy $\pi \in \left( {\Delta{(A)}} \right)^{n}$ maps each state to a probability distribution over the set of actions $\mathbb{A}$. For each policy $\pi$, the value vector ${\mathbf{v}}^{\pi} \in {\mathbb{R}}^{n}$ is defined as
