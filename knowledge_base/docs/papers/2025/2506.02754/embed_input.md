Safely Learning Controlled Stochastic Dynamics

We address the problem of safely learning controlled stochastic dynamics from discrete-time trajectory observations, ensuring system trajectories remain within predefined safe regions during both training and deployment. Safety-critical constraints of this kind are crucial in applications such as autonomous robotics, finance, and biomedicine. We introduce a method that ensures safe exploration and efficient estimation of system dynamics by iteratively expanding an initial known safe control set using kernel-based confidence bounds. After training, the learned model enables predictions of the system's dynamics and permits safety verification of any given control. Our approach requires only mild smoothness assumptions and access to an initial safe control set, enabling broad applicability to complex real-world systems. We provide theoretical guarantees for safety and derive adaptive learning rates that improve with increasing Sobolev regularity of the true dynamics. Experimental evaluations demonstrate the practical effectiveness of our method in terms of safety, estimation accuracy, and computational efficiency.

## Introduction

We consider the problem of safely learning the dynamics of controlled continuous-time stochastic systems from discrete-time observations of trajectory data. This setting is common in applications such as robotics, finance, and healthcare, where system dynamics are only partially known and must be estimated from data. A key challenge in these applications is ensuring safety during both the learning phase and subsequent deployment \[Bonalli et al. Lew et al., \]. As an example, consider an autonomous robot navigating a partially known and turbulent environment, as illustrated in Figure....

### Outline of contributions

## Conclusion

We introduced a provably safe and efficient method for learning controlled stochastic dynamics from trajectory data. By leveraging kernel-based confidence bounds and smoothness assumptions, our method incrementally expands an initial safe control set, ensuring that all trajectories remain within predefined safety regions throughout the learning process. Theoretical guarantees were established for both safety and estimation accuracy, with learning rates that adapt to the Sobolev regularity of the true dynamics. Numerical experiments corroborate our theoretical findings regarding safety and estimation accuracy....

We fit kernel ridge regressors for the density, safety, and reset functions using a Matérn kernel $k$ (with Sobolev smoothness $\nu$) and regularization $\lambda > 0$

For $\xi \in {\lbrack 0,1\rbrack}$, a non-empty set $R_{0} \subset {D \times {\lbrack 0,T_{\max}\rbrack}}$ is provided such that

Safety and exploration guarantees for safe kernelized UCB methods have been developed in prior work \[Sui et al. Bottero et al., \], grounded in kernelized bandit theory \[Srinivas et al. Valko et al. Janz et al., \], which in turn builds on linear bandit results \[Dani et al. Auer, \]. Building on this foundation, we establish novel theoretical guarantees for safe exploration and dynamics estimation under Sobolev regularity. Complete proofs are deferred to Appendix A.

The contributions of this work are as follows.

Safe learning method. We derive a method that safely learns controlled stochastic dynamics, where safety is defined as the requirement that system trajectories remain within a designated set of safe states with high probability....
