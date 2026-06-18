Sharp Rates in Dependent Learning Theory: Avoiding Sample Size Deflation for the Square Loss

In this work, we study statistical learning with dependent (beta-mixing) data and square loss in a hypothesis class F subset L_Psi_p where Psi_p is the norm |f|_Psi_p defined as sup_m >= 1 m^(-1)/p |f|_L^(m) for some p in [2, infinity]. Our inquiry is motivated by the search for a sharp noise interaction term, or variance proxy, in learning with dependent data. Absent any realizability assumption, typical non-asymptotic results exhibit variance proxies that are deflated multiplicatively by the mixing time of the underlying covariates process. We show that whenever the topologies of L^ and Psi_p are comparable on our hypothesis class F - that is, F is a weakly sub-Gaussian class: |f|_Psi_p <~ |f|_L^^(eta) for some eta in (0, 1] - the empirical risk minimizer achieves a rate that only depends on the complexity of the class and second order statistics in its leading term. Our result holds whether the problem is realizable or not and we refer to this as a near mixing-free rate, since direct dependence on mixing is relegated to an additive higher order term. We arrive at our result by combining the above notion of a weakly sub-Gaussian class with mixed tail generic chaining....

## Introduction

While a significant portion the data used in modern learning algorithms exhibits temporal dependencies, we still lack a sharp theory of supervised learning from dependent data. Examples exhibiting such dependencies are far ranging and abundant, and include forecasting applications and data from controls/robotics systems. Over the last several decades, an order-wise rather sharp theory of learning with *independent* data has emerged....

In principle, one expects these results to be carried over to the dependent ($\beta$-mixing) setting through *blocking* (Bernstein Yu, ).^11^1See Section D.1 for a description of this technique. At a high level, the blocking technique involves splitting the original data (of length $n \in {\mathbb{N}}$) into consecutive blocks, each of length $k \in {\mathbb{N}}$, with the length chosen such that the starting points of each block are approximately independent. Indeed, several prior works pursue this route (Mohri & Rostamizadeh Kuznetsov & Mohri Roy et al., )....

## Summary

In this work, we obtain instance-optimal convergence rates for learning with the square loss function and dependent data. We overcome the typical deflation, by the mixing time, of the sample size. The main technical step to arrive at this result is a refined analysis of the multiplier process (1.8) via mixed tail generic chaining that is suitable for dependent, $\beta$-mixing, random variables. Indeed, the leading order term of our main result, Theorem 3.1, does not directly depend on any mixing-time type quantities....

where the variance term on the right is:

### Notation

we have that with probability $1 - {4\delta}$ that:

In the context of the square loss function, the typical approach to sidestep this sample size deflation relies on the "noise" (residual term) forming a martingale difference sequence. This approach has been carried out for parametric inference in (generalized) linear dynamical systems by Simchowitz et al. and Kowshik et al. and also for more general hypothesis classes and supervised learning with square loss by Ziemann & Tu....

In this paper, we instead show how the blocking approach can be salvaged for a wide range of hypotheses classes and the square loss function. In contrast to the just-mentioned references, our analysis does not require a realizability assumption....
