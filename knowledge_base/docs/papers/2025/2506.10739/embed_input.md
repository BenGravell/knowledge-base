Sampling-Based Planning under STL Specifications: A Forward Invariance Approach

We propose a variant of the Rapidly Exploring Random Tree Star (RRT^(star)) algorithm to synthesize trajectories satisfying a given spatio-temporal specification expressed in a fragment of Signal Temporal Logic (STL) for linear systems. Previous approaches for planning trajectories under STL specifications using sampling-based methods leverage either mixed-integer or non-smooth optimization techniques, with poor scalability in the horizon and complexity of the task. We adopt instead a control-theoretic perspective on the problem, based on the notion of set forward invariance. Specifically, from a given STL task defined over polyhedral predicates, we develop a novel algorithmic framework by which the task is efficiently encoded into a time-varying set via linear programming, such that trajectories evolving within the set also satisfy the task. Forward invariance properties of the resulting set with respect to the system dynamics and input limitations are then proved via non-smooth analysis....

## Introduction

Figure 1: A trajectory ζx (red) that satisfies an STL task ϕ is obtained by expanding a tree of trajectories, using an RRT, from a given initial state x0. The tree of trajectories is expanded within the time-varying set ℬϕ(t) such trajectory evolving into ℬϕ(t) also satisfy the STL task ϕ.

The application of sampling-based planners to plan kino-dynamically feasible trajectories in complex environments for systems subject to spatio-temporal constraints has been an active area of research during the past decades. Particularly, with the aim of deploying autonomous systems with verifiable performance guarantees, a growing body of literature has been devoted toward designing planning algorithms to synthesize trajectories satisfying tasks expressed as Linear Temporal Logic (LTL) formulas and, more recently, Signal Temporal Logic (STL) formulas.

### Proposition 9

### Proof

### Proof

Informally, Prop. not only guarantees viability of $\mathcal{B}^{\varphi}{(\left. t \middle| \mathbf{\vartheta} \right.)}$, but also that the set is monotonically shrinking toward the robust predicate level set $\mathcal{H}^{r}$. This is expected from the fact that $\gamma^{\varphi}$ is monotonically decreasing for any choice of the parameters $\mathbf{\vartheta}$ in the set $\Theta$, as per. We highlight that the parameter $r$, representing the robustness of satisfaction for the task $\varphi$, should be chosen to be positive and such that $\mathcal{H}^{r} \neq \varnothing$ as per....

### Proof

The focus of this work is on trajectory planning for linear systems under STL specification, leveraging Rapidly Exploring Random Trees (RRT) \[\] and, in particular, its asymptotically optimal variant RRT^⋆^ \[\], with applications to real-time robot motion planning in complex environments.

### Contributions

In this paper, we propose to adopt a novel approach to real-time sampling-based planning of trajectories for linear systems subject to STL constraints, leveraging the notion of forward invariance of time-varying sets. Namely, we formalize a simple, yet effective, approach to cast a STL specification, expressed over linear predicate functions, into a time-varying set, expressed as a time-varying polyhedron, which we design via linear programming....
