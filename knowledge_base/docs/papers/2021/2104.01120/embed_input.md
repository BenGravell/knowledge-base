Linear Systems Can Be Hard to Learn

In this paper, we investigate when system identification is statistically easy or hard, in the finite sample regime. Statistically easy to learn linear system classes have sample complexity that is polynomial with the system dimension. Most prior research in the finite sample regime falls in this category, focusing on systems that are directly excited by process noise. Statistically hard to learn linear system classes have worst-case sample complexity that is at least exponential with the system dimension, regardless of the identification algorithm. Using tools from minimax theory, we show that classes of linear systems can be hard to learn. Such classes include, for example, under-actuated or under-excited systems with weak coupling among the states. Having classified some systems as easy or hard to learn, a natural question arises as to what system properties fundamentally affect the hardness of system identifiability. Towards this direction, we characterize how the controllability index of linear systems affects the sample complexity of identification....

## Introduction

Linear system identification focuses on using input-output data samples for learning dynamical systems of form:

where $x_{k}$ represents the state, $u_{k}$ represents the control signal, and $w_{k}$ is the process noise. The statistical analysis of system identification algorithms has a long history. Until recently, the main focus was providing guarantees for the convergence of system identification in the *asymptotic regime*, when the number of collected samples $N$ tends to infinity. Under sufficient persistency of excitation, system identification algorithms converge and the asymptotic bounds capture very well how the identification error decays with $N$ qualitatively.

Figure 4: Sample complexity classes for linear systems. according to their controllability index.

Our results pose numerous future questions for exploiting other system properties (e.g. observability) for efficiently learning classes of partially-observed linear systems or nonlinear systems. It remains an open problem to prove whether or not the $n -$th order integrator is poly-learnable as discussed in Section 6. Similarly, it is an open problem to prove whether or not the Jordan block of size $n$ and eigenvalues all $0 < \lambda < 1$ has exponential complexity. Finally, the results of this paper might have ramifications for control, for example learning the linear quadratic regulator, as well as reinforcement learning.

In general, the noise might be ill-conditioned (zero across certain directions), while it might be physically impossible to actuate every state of the system. We call such systems underactuated or under-excited. It might still be possible to identify underactuated systems, e.g. if the pair $(A,\begin{bmatrix}
\end{bmatrix})$ is controllable. However, as we prove in the next section, the identification difficulty might increase dramatically.

In order to show that a class of systems $\mathcal{C}_{n}$ is $\exp$-hard, one must show that for any system identification algorithm the worst-case sample complexity is at least exponential in state dimension $n$. Contrary to $poly$-learnable problems, for exponential hardness we should establish sample complexity lower bounds.

Let ${(A,H)} \in {\mathbb{R}}^{n \times {({n + r})}}$ be controllable. Then, the distance from uncontrollability is given by:
