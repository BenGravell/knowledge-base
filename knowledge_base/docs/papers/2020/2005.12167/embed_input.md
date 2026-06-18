Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty

Topics include Robustness, Uncertainty, Sample complexity.

This paper studies the sample complexity of the stochastic Linear Quadratic Regulator when applied to systems with multiplicative noise. We assume that the covariance of the noise is unknown and estimate it using the sample covariance, which results in suboptimal behaviour. The main contribution of this paper is then to bound the suboptimality of the methodology and prove that it decreases with 1/N, where N denotes the amount of samples. The methodology easily generalizes to the case where the mean is unknown and to the distributionally robust case studied in a previous work of the authors. The analysis is mostly based on results from matrix function perturbation analysis.

## INTRODUCTION

The field of learning control has recently seen explosive growth, which can be attributed to the availability of large amounts of data, creating an incentive for controllers that use the available information optimally. A significant amount of this research effort is being directed towards the familiar Linear Quadratic Regulation (LQR) problem where the transition matrices are unknown. Most of these developments however are related to deterministic systems.

Instead this paper takes a different approach, considering systems that intrinsically include the uncertainty in the dynamics through stochastic disturbances. More specifically we study systems with a time-varying multiplicative disturbance. These may cover a wide range of system classes like Linear Parameter Varying (LPV) systems and Linear Difference Inclusions (LDI) or in our case, when the disturbance varies stochastically, systems with multiplicative noise. Such systems have already been studied in the context of learning control by using policy iteration and intrinsically introduce robustness in the controller design.

The authors previously developed a control synthesis procedure using the *distributionally robust approach* that guarantees stability with high probability, when the true distribution of the system is not known. This paper is related to that result and provides a methodology to evaluate the performance of the *empirical approach*, where the sample mean and covariance are used to produce a controller making it similar to the *certainty equivanlent approach* for deterministic LQR. Therefore the proofs are similar to the result of Mania et. al., where the sample complexity of this certainty equivalent approach is studied.

The main result is then a suboptimality guarantee for the empirical controller. To produce such a result we make use of Riccati perturbation analysis. This paper is, to the authors' knowledge, the first instance of such a perturbation analysis being applied to discrete time systems with multiplicative noise. A Riccati perturbation bound for continuous time systems was already produced .
