Inverse Quadratic Optimal Control for Discrete-Time Linear Systems

Topics include Optimal control, Optimization, Control, Linear quadratic regulator, Linear systems, Optimization problem.

In this paper, we consider the inverse optimal control problem for the discrete-time linear quadratic regulator, over finite-time horizons. Given observations of the optimal trajectories, and optimal control inputs, to a linear time-invariant system, the goal is to infer the parameters that define the quadratic cost function. The well-posedness of the inverse optimal control problem is first justified. In the noiseless case, when these observations are exact, we analyze the identifiability of the problem and provide sufficient conditions for uniqueness of the solution. In the noisy case, when the observations are corrupted by additive zero-mean noise, we formulate the problem as an optimization problem and prove the statistical consistency of the problem later. The performance of the proposed method is illustrated through numerical examples.

## Introduction

Proposed by Kalman, inverse optimal control has found a multitude of applications. The goal of a classical optimal control problem is to find the optimal control input as well as the optimal trajectory when the cost function, system dynamics, and initial conditions are given. In contrast, the objective of an inverse optimal control problem is to "reverse engineer" the cost function, given observations of optimal trajectories or control inputs, for known system dynamics.

This paper is concerned with inverse optimal control for the discrete-time linear quadratic regulator (LQR) over finite-time horizons, i.e., finding the parameters in the quadratic objective funtion given the discrete-time linear system dynamics and (possibly noisy) observations of the optimal trajectory or control input.

## Conclusion

In this paper, we analyse the inverse optimal control problem for discrete-time LQR in finite-time horizons. We consider both the noiseless case (in which observations of the optimal trajectories are exact) and the noisy case (in which such observations are corrupted by additive noise). The well-posedness of the problem is first justified. In the noiseless case, we discuss identifiability of the problem, and provide sufficient conditions on the uniqueness of the solution. In the noisy case, we formulate the search for $Q$ as an optimization problem, and prove that such formulation is statistically consistent....

are linearly independent, then matrix

Though the problem is easy in the noiseless case, however, we would like to have a closer look at the identifiability of $Q$. Namely, given a set of noiseless optimal trajectories $x_{1:N}^{({1:M})}$, is there a unique positive semidefinite matrix that corresponds to the given optimal trajectories? Now we give two sufficient conditions on the given trajectories $x_{1:N}^{({1:M})}$ that can be used to determine the uniqueness of $Q$.

Equipped with the stochastic set-up above and given that the initial value $x_{1}$ is actually a realization of the random vector $\overline{x}$, i.e., $x_{1} = {\overline{x}{(\omega)}}$, the LQR problem can actually be seen as

Inverse optimal control for LQR, particularly in the continuous infinite time-horizon case, has been studied by a number of authors....
