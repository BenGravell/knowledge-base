From Optimization to Control: Quasi Policy Iteration

Topics include Convex optimization, Policy iteration, Value iteration, Computational complexity, Optimization, Control, QPI, Adopt the quasi-Newton method, QNM, Markov decision process, Hessian matrix.

Recent control algorithms for Markov decision processes (MDPs) have been designed using an implicit analogy with well-established optimization algorithms. In this paper, we adopt the quasi-Newton method (QNM) from convex optimization to introduce a novel control algorithm coined as quasi-policy iteration (QPI). In particular, QPI is based on a novel approximation of the ``Hessian'' matrix in the policy iteration algorithm, which exploits two linear structural constraints specific to MDPs and allows for the incorporation of prior information on the transition probability kernel. While the proposed algorithm has the same computational complexity as value iteration, it exhibits an empirical convergence behavior similar to that of QNM with a low sensitivity to the discount factor.

## Introduction

The problem of control, or the decision-making problem as it is also known within the operations research community, has been the subject of much research since the introduction of the Bellman principle of optimality in the late 1950s \[bellman1957markovian\]. In particular, the connection between control algorithms for Markov decision processes (MDPs) and optimization algorithms has been noticed since the late 1970s \[puterman1979convergence\]: Value iteration (VI) \[bellman1957markovian\] can be seen as an instance of gradient descent (GD) algorithm, and policy iteration (PI) \[howard1960dynamic\] is an instance of the Newton method (NM).

Main contribution.

Local superlinear convergence: We provide a modified implementation of QPI which also incorporates the secant-type constraints in approximation of the Hessian to guarantee the local superlinear convergence (Theorem 3.4. ‣ 3.2.3. Modified implementation with superlinear convergence ‣ 3.2. QPI Algorithm ‣ 3. Quasi-Policy Iteration (QPI) ‣ From Optimization to Control: Quasi Policy Iteration")).

The paper is organized as follows. In Section, we describe the optimal control problem of MDPs. In Section ‣ From Optimization to Control: Quasi Policy Iteration"), we introduce and analyze the model-based QPI algorithm and its model-free extension, the QPL algorithm. All the technical proofs are provided in Section. The performance of these algorithms is then compared with multiple control algorithms via extensive numerical experiments in Section. Section concludes the paper by providing some final remarks.

## Limitations and Future Research

In this paper, we proposed the model-based quasi-policy iteration (QPI) algorithm and its model-free counterpart, the quasi-policy learning (QPL) algorithm. The proposed algorithms were particularly inspired by the quasi-Newton methods and employed a novel approximation of the "Hessian" by using two new linear constraints specific to MDPs.
