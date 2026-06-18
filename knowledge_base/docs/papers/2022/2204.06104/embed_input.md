A Tutorial on Solution Properties of State Space Models of Dynamical Systems

Topics include Matrix exponential, Neumann series.

The starting point of analysis of state space models is investigating existence, uniqueness and solution properties such as the semigroup property, and various formulas for the solutions. Several concepts such as the state transition matrix, the matrix exponential, the variations of constants formula (the Cauchy formula), the Peano-Baker series, and the Picard iteration are used to characterize solutions. In this note, a tutorial treatment is given where all of these concepts are shown to be various manifestations of a single abstract method, namely solving equations using an operator Neumann series involving the Volterra operator of forward integration. The matrix exponential, the Peano-Baker series, the Picard iteration, and the Cauchy formula can be "discovered" naturally from this Neumann series. The convergence of the series and iterations is a consequence of the key property of asymptotic nilpotence of the Volterra operator. This property is an asymptotic version of the nilpotence property of a strictly-lower-triangular matrix.

## Introduction

State space models are the starting point in analysis of dynamical systems. They come in various forms of generality as follows

The state at each time ${x{(t)}} \in {\mathbb{R}}^{n}$ is an $n$-vector, while the input ${u{(t)}} \in {\mathbb{R}}^{q}$ is also a vector at each $t$, with typically a different dimension than the state. For control problems, for example, the signal $u$ is the control input, and most interesting problems have the dimension of $u$ being much less than that of $x$ (controlling many states with a single or few inputs). If the signal $u$ is a disturbance or a noise signal, it typically has dimensions comparable to those of the state $x$.

Both of the examples above highlight an important issue in mathematical modeling of physical systems. We generally believe that given enough information about a physical system, we can construct a mathematical model (e.g. a differential equation) that predicts the future behavior of the system given a fully accurate (infinite precision) description of initial conditions^99^9The discussion here is unrelated to the phenomenon of "chaos", which involves sensitive dependence on initial conditions. There are many chaotic systems with solutions that are guaranteed to exists from all initial conditions and are unique.....

The theme of the above remarks is that non-uniquness or lack of existence of solutions is not a mathematical difficulty, but rather a mathematical modeling difficulty. One can come up with equations and mathematical constructs that do all kinds of fantastical things. The question is whether these are good mathematical models of the physical world. It seems like a natural minimal requirement that a mathematical model should posses the property of existence and uniqueness of solutions.

Now compute the kernel representation of the operator $\left( {I - {\mathcal{V}\mathcal{A}}} \right)^{- 1}$. Using, and noting that the operator $\mathcal{A}^{k}$ is simply multiplication by the matrix $A^{k}$, we see that

It turns out that the Volterra integration operator $\mathcal{V}$ has a special property that guarantees the convergence of the Neumann series under very mild conditions. In addition, this formula will lead naturally to the matrix exponential when $A$ is constant, and to the so-called Peano-Baker series in the time-varying case....
