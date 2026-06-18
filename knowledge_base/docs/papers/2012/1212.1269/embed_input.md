Approximate Dynamic Programming via Sum of Squares Programming

Topics include Approximate dynamic programming, Sum-of-squares programming, Stochastic control, Polynomial value functions, Semidefinite programming, Bellman inequalities, Helicopter control.

Extends linear-programming approaches to approximate dynamic programming from quadratic value approximations to higher-order polynomial bases through sum-of-squares relaxations. The useful insight is that the infinite Bellman inequality can be enforced offline as an SDP, while the online policy step becomes a polynomial optimization problem, making the method plausible for continuous stochastic-control systems such as the helicopter testbed.

We describe an approximate dynamic programming method for stochastic control problems on infinite state and input spaces. The optimal value function is approximated by a linear combination of basis functions with coefficients as decision variables. By relaxing the Bellman equation to an inequality, one obtains a linear program in the basis coefficients with an infinite set of constraints. We show that a recently introduced method, which obtains convex quadratic value function approximations, can be extended to higher order polynomial approximations via sum of squares programming techniques. An approximate value function can then be computed offline by solving a semidefinite program, without having to sample the infinite constraint. The policy is evaluated online by solving a polynomial optimization problem, which also turns out to be convex in some cases. We experimentally validate the method on an autonomous helicopter testbed using a 10-dimensional helicopter model.

## Introduction

Many problems in engineering and finance can be modeled as stochastic control problems on infinite state and input spaces, in which a control policy is sought to optimize the behavior of a stochastic dynamical system over a finite or infinite time horizon. While such models are quite general and expressive, the resulting optimization problems are extremely difficult because the decision variable (the control policy) is a *function*, which is generally infinite-dimensional and thus not amenable to computation or even storage on a computer....

Approximate dynamic programming (ADP) is a collection of heuristic methods for solving stochastic control problems for cases that are intractable with standard dynamic programming methods \[2, Ch. 6\],. The methods can be classified into three broad categories, all of which involve some kind of function approximation: lookahead/rollout/receding horizon/model predictive control policies, direct policy function approximation, policies based on value function approximation. Here, we will focus on an approach in the last category in which the value function is approximated by a linear combination of pre-specified basis functions.

## Concluding Remarks

We have described an approximate dynamic programming method on infinite state and control spaces. We showed how sum of squares techniques can be used to compute polynomial value function approximations offline via semidefinite programming. The policy is computed online by solving a polynomial optimization problem, which can be made convex in certain cases. Future work will include exploring various application domains, focusing in particular on what can be gained by using higher-order polynomial approximations....

and forms a cone in $\mathbf{R}{\lbrack x\rbrack}$.

One method to obtain a value function approximation is to relax the Bellman equation into an inequality. The set of functions that satisfy the Bellman inequality are underestimators of the optimal value function. To see this, suppose a function $\hat{V}$ satisfies $\hat{V} \leq {T\hat{V}}$. Then by monotonicity of $T$ and value iteration convergence we have

### III-C Numerical Example

A method recently introduced by Wang and Boyd in involves computing an approximate value function by relaxing the Bellman equation to an inequality....
