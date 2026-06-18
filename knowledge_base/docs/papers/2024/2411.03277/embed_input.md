Asymptotic Stability Equals Exponential Stability - While You Twist Your Eyes

Topics include Stability analysis, GAS, Exponential stability.

Suppose that two vector fields on a smooth manifold render some equilibrium point globally asymptotically stable (GAS). We show that there exists a homotopy between the corresponding semiflows such that this point remains GAS along this homotopy.

## Introduction

In the context of what we call today Conley index theory (see Section A), Conley posed the following "converse question" in the 1970s: "To what extent does the homotopy index *\[Conley index\]* itself determine the equivalence class of isolated invariant sets which are related by continuation?" \[ref:conley1978isolated, p. 83\].

This result provides a partial solution to Conley's converse question as it turns out that the asymptotically stable systems under consideration can be continuously transformed into the same exponentially stable system and hence, by transitivity, into each other. Concurrently, we discuss extensions to discontinuous vector fields throughout, plus we illustrate how to go about extensions to ISS. We also discuss intimate connections with optimization and optimal transport (e.g., see Example 3.4. ‣ 3 Stability preserving homotopies ‣ Asymptotic stability equals exponential stability—while you twist your eyes") and 5.1.

## Example 1.1 (Trivial convex combinations can fail)

Consider a linear differential equation $\overset{˙}{x} = {A{(s)}x}$ on ${\mathbb{R}}^{2}$ parametrized by the matrices

Both $A{}$ and $A{}$ correspond to global asymptotically stable systems, yet, for $s = \frac{1}{2}$, the system $\overset{˙}{x} = {A{(s)}x}$ is unstable. Hence, we cannot simply construct straight-line homotopies between stable vector fields and expect that stability is preserved. Instead, we know from \[ref:JongeneelSchwan2024TAC\] that for vector fields with convex Lyapunov functions we should homotope via the canonical ODE $\overset{˙}{x} = {- x}$. Explicitly, consider the following path of vector fields defined by

## Conclusion and future work

We have provided a step towards better understanding Conley's converse question in some generality, yet, many open problems remain. Although directly working with flows has benefits, e.g., see \[ref:aguiar2023universal\], the main open problem is the extension to vector fields and generic attractors. Several other questions are as follows.

Open problem 1: characterize stability of (2.1) throughout the homotopy.
