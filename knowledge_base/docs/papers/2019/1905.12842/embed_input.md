Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator

Topics include Reinforcement learning, Policy iteration, Regret bounds, Sample complexity, Control, Learning, PI, Linear quadratic regulator.

We study the sample complexity of approximate policy iteration (PI) for the Linear Quadratic Regulator (LQR), building on a recent line of work using LQR as a testbed to understand the limits of reinforcement learning (RL) algorithms on continuous control tasks. Our analysis quantifies the tension between policy improvement and policy evaluation, and suggests that policy evaluation is the dominant factor in terms of sample complexity. Specifically, we show that to obtain a controller that is within epsilon of the optimal LQR controller, each step of policy evaluation requires at most (n+d)^/epsilon^ samples, where n is the dimension of the state vector and d is the dimension of the input vector. On the other hand, only log(1/epsilon) policy improvement steps suffice, resulting in an overall sample complexity of (n+d)^ epsilon^(-2) log(1/epsilon). We furthermore build on our analysis and construct a simple adaptive procedure based on epsilon-greedy exploration which relies on approximate PI as a sub-routine and obtains T^(2/3) regret, improving upon a recent result of Abbasi-Yadkori et al.

## Introduction

With the recent successes of reinforcement learning (RL) on continuous control tasks, there has been a renewed interest in understanding the sample complexity of RL methods. A recent line of work has focused on the Linear Quadratic Regulator (LQR) as a testbed to understand the behavior and trade-offs of various RL algorithms in the continuous state and action space setting....

In this paper, we extend our understanding of model-free algorithms for LQR by studying the performance of approximate PI on LQR, which is a classic approximate dynamic programming algorithm. Approximate PI is a model-free algorithm which iteratively uses trajectory data to estimate the state-value function associated to the current policy (via e.g. temporal difference learning), and then uses this estimate to greedily improve the policy. A key issue in analyzing approximate PI is to understand the trade-off between the number of policy improvement iterations, and the amount of data to collect for each policy evaluation phase....

## Conclusion

We studied the sample complexity of approximate PI on LQR, showing that order ${({n + d})}^{3}\varepsilon^{- 2}{\log{({1/\varepsilon})}}$ samples are sufficient to estimate a controller that is within $\varepsilon$ of the optimal. We also show how to turn this offline method into an adaptive LQR method with $T^{2/3}$ regret. Several questions remain open with our work. The first is if policy iteration is able to achieve $T^{1/2}$ regret, which is possible with other model-based methods. The second is whether or not model-free methods provide advantages in situations of partial observability for LQ control....

Once again as we did for $Q$-functions, we slightly abuse notation and let $V$ denote the value function and the matrix that parameterizes the value function. Our main result for Algorithm 2 ‣ 2 Main Results ‣ Finite-time Analysis of Approximate Policy Iteration for the Linear Quadratic Regulator") appears in the following theorem. For simplicity, we will assume that ${\parallel S\parallel} \geq 1$ and ${\parallel R\parallel} \geq 1$.

Then we have with probability at least $1 - \delta$,

### LSPI for Adaptive LQR

We also extend our analysis of approximate PI to the online, adaptive LQR setting popularized by Abbasi-Yadkori and Szepesvári. By using a greedy exploration scheme similar to Dean et al....
