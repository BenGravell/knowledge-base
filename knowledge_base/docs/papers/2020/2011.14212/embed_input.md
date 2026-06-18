Approximate Midpoint Policy Iteration for Linear Quadratic Control

Topics include Policy iteration, Dynamic programming, Approximate dynamic programming, Reinforcement learning, Newton's method, Midpoint method, Linear systems, Linear quadratic regulator, Control, Least squares, Temporal difference learning.

By viewing policy iteration as Newton's method for solving MDPs and extending the analogy to the midpoint method, the work shows that policies can be solved for more efficiently, both in the model-known and model-unknown settings.

We present a midpoint policy iteration algorithm to solve linear quadratic optimal control problems in both model-based and model-free settings. The algorithm is a variation of Newton's method, and we show that in the model-based setting it achieves cubic convergence, which is superior to standard policy iteration and policy gradient algorithms that achieve quadratic and linear convergence, respectively. We also demonstrate that the algorithm can be approximately implemented without knowledge of the dynamics model by using least-squares estimates of the state-action value function from trajectory data, from which policy improvements can be obtained. With sufficient trajectory data, the policy iterates converge cubically to approximately optimal policies, and this occurs with the same available sample budget as the approximate standard policy iteration. Numerical experiments demonstrate effectiveness of the proposed algorithms.

## Introduction

With the recent confluence of reinforcement learning and data-driven optimal control, there is renewed interest in fully understanding convergence, sample complexity, and robustness in both "model-based" and "model-free" algorithms. Linear quadratic problems in continuous spaces provide benchmarks where strong theoretical statements can be made. In practice, it is often difficult or impossible to develop a model of a system from first-principles.

As an alternative, so-called "model-free" methods may also be used, which do not attempt to learn a model of the dynamics.

Between the fully model-based system identification approaches and the fully model-free policy optimization approaches lies another category of methods, which we denote as value function approximation methods. These methods attempt to estimate value functions then compute policies which are optimal with respect to these value functions. This class of methods includes approximate dynamic programming, exemplified by approximate value iteration, which estimates state-value functions, and approximate policy iteration, which estimates state-action value functions.

We present a midpoint policy iteration algorithm to solve linear quadratic optimal control problems when the dynamics are both known (Algorithm 1) and unknown (Algorithm 4).

We demonstrate that the method converges, and does so at a faster *cubic* rate than standard policy iteration or policy gradient, which converge at quadratic and linear rates, respectively.

We show that approximate midpoint policy iteration converges faster in the model-free setting even with the same available sample budget as the approximate standard policy iteration.

We present numerical experiments that illustrate and demonstrate the effectiveness of the algorithms and provide an open-source implementation to facilitate their wider use.
