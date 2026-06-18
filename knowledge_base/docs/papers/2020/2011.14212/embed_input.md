Approximate Midpoint Policy Iteration for Linear Quadratic Control

Topics include Policy iteration, Dynamic programming, Approximate dynamic programming, Reinforcement learning, Newton's method, Midpoint method, Linear systems, Linear quadratic regulator, Control, Least squares, Temporal difference learning.

By viewing policy iteration as Newton's method for solving MDPs and extending the analogy to the midpoint method, the work shows that policies can be solved for more efficiently, both in the model-known and model-unknown settings.

We present a midpoint policy iteration algorithm to solve linear quadratic optimal control problems in both model-based and model-free settings. The algorithm is a variation of Newton's method, and we show that in the model-based setting it achieves cubic convergence, which is superior to standard policy iteration and policy gradient algorithms that achieve quadratic and linear convergence, respectively. We also demonstrate that the algorithm can be approximately implemented without knowledge of the dynamics model by using least-squares estimates of the state-action value function from trajectory data, from which policy improvements can be obtained. With sufficient trajectory data, the policy iterates converge cubically to approximately optimal policies, and this occurs with the same available sample budget as the approximate standard policy iteration. Numerical experiments demonstrate effectiveness of the proposed algorithms.

## Introduction

With the recent confluence of reinforcement learning and data-driven optimal control, there is renewed interest in fully understanding convergence, sample complexity, and robustness in both "model-based" and "model-free" algorithms. Linear quadratic problems in continuous spaces provide benchmarks where strong theoretical statements can be made. In practice, it is often difficult or impossible to develop a model of a system from first-principles....

As an alternative, so-called "model-free" methods may also be used, which do not attempt to learn a model of the dynamics. The category of policy optimization methods which directly attempt to optimize the control policy, including policy gradient, has received significant attention recently for standard LQR \[Fazel et al.Fazel, Ge, Kakade, and Mesbahi, Bu et al.Bu, Mesbahi, and Mesbahi\], multiplicative-noise LQR \[Gravell et al.Gravell, Esfahani, and Summers\], Markov jump LQR \[Jansch-Porto et al.Jansch-Porto, Hu, and Dullerud\], and LQ games related to $\mathcal{H}_{\infty}$ robust control \[Zhang et al.Zhang, Yang, and Basar, Bu et...

This algorithm is perhaps most useful in the regime of practical problems in the online setting where it is relatively expensive to collect data and relatively cheap to perform the computations required to execute the updates. In such scenarios, the goal is to converge in as few iterations as possible, and MPI shows a clear advantage. Both the exact and approximate midpoint PI incur a computation cost *double* that of their standard PI counterparts. Theoretically, the faster *cubic* convergence rate of MPI over the *quadratic* convergence rate of PI should dominate this order constant (2$\times$) cost with sufficiently many iterations....

The current methodology is certainty-equivalent in the sense that we treat the estimated value functions as correct. Future work will explore ways to estimate and account for uncertainty in the value function estimate explicitly to minimize regret risk in the initial transient stage of learning when the amount of information is low and uncertainty is high.

Using the expression, this can be rewritten as

The midpoint Newton method, due originally to \[Traub\], begins with an initial guess $x_{0}$ then proceeds with iterations
