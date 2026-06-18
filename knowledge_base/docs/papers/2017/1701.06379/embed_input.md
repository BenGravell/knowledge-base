From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming

We consider linear programming (LP) problems in infinite dimensional spaces that are in general computationally intractable. Under suitable assumptions, we develop an approximation bridge from the infinite-dimensional LP to tractable finite convex programs in which the performance of the approximation is quantified explicitly. To this end, we adopt the recent developments in two areas of randomized optimization and first order methods, leading to a priori as well as a posterior performance guarantees. We illustrate the generality and implications of our theoretical results in the special case of the long-run average cost and discounted cost optimal control problems for Markov decision processes on Borel spaces. The applicability of the theoretical results is demonstrated through a constrained linear quadratic optimal control problem and a fisheries management problem.

## Introduction

Linear programming (LP) problems in infinite dimensional spaces appear in, among other areas, engineering, economics, operations research and probability theory. Infinite LPs offer remarkable modeling power, subsuming general finite dimensional optimization problems and the generalized moment problem as special cases. They are, however, often computationally formidable, motivating the study of approximations schemes.

A particularly rich class of problems that can be modeled as infinite LPs involves Markov decision processes (MDP) and their optimal control. More often than not, it is impossible to obtain explicit solutions to MDP problems, making it necessary to resort to approximation techniques. Such approximations are the core of a methodology known as *approximate dynamic programming*. Interestingly, a wide range of optimal control problems involving MDP can be equivalently expressed as *static* optimization problems over a closed convex set of measures, more specifically, as infinite LPs....

(b) Upper bound Jn, ηUB and lower bound Jn, ηLB

Figure 5. The results and error bounds are obtained by Algorithm 1 with n = 10 for Example 7.2. The red dotted line is the optimal solution computed as indicated in Figure 4.

Under Assumption 3.1. ‣ 3.2. Semi-infinite approximation ‣ 3. Infinite to Semi-infinite Programs ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming"), we then have ${J_{n} - {J_{n}{(\delta)}}} \leq \left\langle \delta,y_{n}^{\star} \right\rangle$, where $y_{n}^{\star}$ is an optimizer of 32.

which delivers the desired assertion when $\omega$ tends to 0. ∎

Suppose Assumption 5.1. ‣ 5.1. Structural convex optimization ‣ 5. Semi-infinite to Finite Program: Structural convex optimization ‣ From Infinite to Finite Programs: Explicit Error Bounds with Applications to Approximate Dynamic Programming") holds with constant $L$ and $\vartheta$ is the strong convexity parameter in the definition of the operator $\mathbb{T}$ in. Given the regularization term $\eta > 0$ and $k$ iterations of Algorithm 1, we define

Approximation schemes to tackle infinite LPs have historically been developed for special classes of problems, e.g., the general capacity problem, or the generalized moment problem....
