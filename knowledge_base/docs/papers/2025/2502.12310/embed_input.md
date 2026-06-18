Domain Randomization Is Sample Efficient for Linear Quadratic Control

Topics include Robotics, Robustness, Benchmarks, Control, Learning, Sampling, Linear quadratic regulator.

We study the sample efficiency of domain randomization and robust control for the benchmark problem of learning the linear quadratic regulator (LQR). Domain randomization, which synthesizes controllers by minimizing average performance over a distribution of model parameters, has achieved empirical success in robotics, but its theoretical properties remain poorly understood. We establish that with an appropriately chosen sampling distribution, domain randomization achieves the optimal asymptotic rate of decay in the excess cost, matching certainty equivalence. We further demonstrate that robust control, while potentially overly conservative, exhibits superior performance in the low-data regime due to its ability to stabilize uncertain systems with coarse parameter estimates. We propose a gradient-based algorithm for domain randomization that performs well in numerical experiments, which enables us to validate the trends predicted by our analysis. These results provide insights into the use of domain randomization in learning-enabled control, and highlight several open questions about its application to broader classes of systems.

## Introduction

Figure 1: Illustration of the sample efficinecy of various synthesis methods.

The use of learned world models to synthesize controllers via policy optimization is becoming increasingly prevalent in reinforcement learning (Wu et al. Matsuo et al., ). The performance of the resulting controller depends heavily upon the synthesis procedure. Simple approaches that do not account for uncertainty, known as certainty equivalence, can overfit to errors in the learned model. Robust control approaches can tolerate some error in the learned model, but may be overly conservative and computationally demanding....

By analyzing the sample efficiency of learning the linear quadratic regulator via domain randomization and robust control, our work provides insights into the tradeoffs present for approaches to incorporate uncertainty quantification into learning-enabled control. Our analysis demonstrates that if one is strategic about the design of the sampling distribution, then the benefits of domain randomization over robust control may extend beyond computational considerations, and to the sample efficiency. This is particularly exciting due to the prominence of domain randomization in practice for robot learning....

We thank Manfred Morari, Anastasios Tsiamis, Ingvar Ziemann, and Thomas Zhang for several instructive conversations. TF is supported by JASSO Exchange Support program and UTokyo-TOYOTA Study Abroad Scholarship. TF and GP are supported in part by NSF Award SLES 2331880 and NSF TRIPODS EnCORE 2217033. BL and NM are supported by NSF Award SLES-2331880, NSF CAREER award ECCS-2045834 and AFOSR Award FA9550-24-1-0102.

A bound on least squares using this quantity is shown in Appendix C. Proofs for the remainder of the results in this section may be found in Appendix G.

We consider three approaches to control synthesis using the estimates $\hat{\theta}$ and $\hat{\mathsf{F}\mathsf{I}}$:

To illustrate the impact on control performance, suppose we have an estimate $\hat{a} = 1.01$. The certainty-equivalent controller derived from this estimate is $k = {- 0.0424}$, which fails to stabilize the true system. In contrast, if we apply robust control over any uncertainty set within the interval $\lbrack 0.3,1.8\rbrack$ that includes $a^{\star}$, we synthesize a controller that stabilizes the system....
