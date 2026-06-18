Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty

Topics include Robustness, Uncertainty, Sample complexity.

This paper studies the sample complexity of the stochastic Linear Quadratic Regulator when applied to systems with multiplicative noise. We assume that the covariance of the noise is unknown and estimate it using the sample covariance, which results in suboptimal behaviour. The main contribution of this paper is then to bound the suboptimality of the methodology and prove that it decreases with 1/N, where N denotes the amount of samples. The methodology easily generalizes to the case where the mean is unknown and to the distributionally robust case studied in a previous work of the authors. The analysis is mostly based on results from matrix function perturbation analysis.

## INTRODUCTION

The field of learning control has recently seen explosive growth, which can be attributed to the availability of large amounts of data, creating an incentive for controllers that use the available information optimally. A significant amount of this research effort is being directed towards the familiar Linear Quadratic Regulation (LQR) problem where the transition matrices are unknown. Most of these developments however are related to deterministic systems.

Instead this paper takes a different approach, considering systems that intrinsically include the uncertainty in the dynamics through stochastic disturbances. More specifically we study systems with a time-varying multiplicative disturbance. These may cover a wide range of system classes like Linear Parameter Varying (LPV) systems and Linear Difference Inclusions (LDI) or in our case, when the disturbance varies stochastically, systems with multiplicative noise. Such systems have already been studied in the context of learning control by using policy iteration and intrinsically introduce robustness in the controller design.

The final sample-complexity is then related to performance. It is given in Corollary 3.4. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty") and states that the suboptimality decreases with $1/N$. This is the same rate as was derived for determinstic certainty equivalent LQR in.

In future work, we aim to extend the results to partially observed systems and to the distributionally robust approach, where the stability complexity is absent, since it is satisfied automatically.

### Proof

where $\overline{n} = {\min{(n_{x},n_{u})}}$ and $\mathbf{\epsilon}_{\mathbf{K}}$ the right-side of (7. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")). The bound in (8. ‣ 3 MAIN RESULT ‣ Sample Complexity of Data-Driven Stochastic LQR with Multiplicative Uncertainty")) is valid as long as:

the matrix $\Phi{({\DeltaP})}$ is symmetric.

The authors previously developed a control synthesis procedure using the *distributionally robust approach* that guarantees stability with high probability, when the true distribution of the system is not known....
