Learning to Control Linear Systems Can Be Hard

In this paper, we study the statistical difficulty of learning to control linear systems. We focus on two standard benchmarks, the sample complexity of stabilization, and the regret of the online learning of the Linear Quadratic Regulator (LQR). Prior results state that the statistical difficulty for both benchmarks scales polynomially with the system state dimension up to system-theoretic quantities. However, this does not reveal the whole picture. By utilizing minimax lower bounds for both benchmarks, we prove that there exist non-trivial classes of systems for which learning complexity scales dramatically, i.e. exponentially, with the system dimension. This situation arises in the case of underactuated systems, i.e. systems with fewer inputs than states. Such systems are structurally difficult to control and their system theoretic quantities can scale exponentially with the system dimension dominating learning complexity. Under some additional structural assumptions (bounding systems away from uncontrollability), we provide qualitatively matching upper bounds....

## Introduction

In stochastic linear control, the goal is to design a controller for a system of the form

where $x_{k} \in {\mathbb{R}}^{n}$ is the system internal state, $u_{k} \in {\mathbb{R}}^{p}$ is some exogenous input, and $w_{k} \in {\mathbb{R}}^{r}$ is some random disturbance sequence. Matrices $A,B,H$ determine the evolution of the state, based on the previous state, control input, and disturbance respectively. Control theory has a long history of studying how to design controllers for system when its model is *known*. However, in reality system might be *unknown* and we might not have access to its model. In this case, we have to learn how to control based on data.

We prove that learning to control linear systems can be hard for non-trivial system classes. The problem of stabilization might require sample complexity which scales exponentially with the system dimension $n$. Similarly, online LQR might exhibit regret which scales exponentially with $n$. This difficulty arises in the case of underactuated systems. Such systems are structurally difficult to control; they can be very sensitive to inputs/noise or very hard to excite. If the system is robustly coupled and has a mild degree of underactuation (small controllability index), then we can guarantee that learning will be easy.

We stress that system theoretic quantities might not be dimensionless. On the contrary, they might grow very large with the dimension and dominate any poly$(n)$ terms. Hence, going forward, an important direction of future work is to find policies with optimal dependence on such system theoretic quantities. Although the optimal dependence is known for the problem of system identification, it is still not clear what is the optimal dependence in the case of control. For example, an interesting open problem is to find the optimal dependence of the regret $R_{T}$ on the Riccati equation solution $P$....

### Proposition 1 (Staircase form)

### Difficulty of Online LQR

### Sample complexity upper bounds

Controlling unknown dynamical systems has also been studied from the perspective of Reinforcement Learning (RL). Although the setting of tabular RL is relatively well-understood, it has been challenging to analyze the continuous setting, where the state and/or action spaces are infinite. Recently, there has been renewed interest in learning to control linear systems....
