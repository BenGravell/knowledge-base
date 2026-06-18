System Identification under Bounded Noise: Optimal Rates beyond Least Squares

Topics include System identification, Bounded noise, Least squares, Sample complexity, Linear systems, Optimality, Robustness.

Studies system identification when disturbances are bounded rather than stochastic in the usual least-squares-friendly way. The paper gives optimal-rate results beyond classical least squares, clarifying what estimators can exploit under adversarial or deterministic noise bounds.

System identification is a fundamental problem in control and learning, particularly in high-stakes applications where data efficiency is critical. Classical approaches, such as the ordinary least squares estimator (OLS), achieve an O(1/sqrt(T)) convergence rate under Gaussian noise assumptions, where T is the number of samples. This rate has been shown to match the lower bound. However, in many practical scenarios, noise is known to be bounded, opening the possibility of improving sample complexity. In this work, we establish the minimax lower bound for system identification under bounded noise, proving that the O(1/T) convergence rate is indeed optimal. We further demonstrate that OLS remains limited to an (1/sqrt(T)) convergence rate, making it fundamentally suboptimal in the presence of bounded noise. Finally, we instantiate two natural variations of OLS that obtain the optimal sample complexity.

## Introduction

System identification plays a crucial role in modern control design, especially in applications where accurate models of unknown dynamical systems must be learned from data. In high-stakes and safety-critical systems, where data collection can be costly or risky, sample efficiency is of particular importance. While classical results in system identification provide asymptotic convergence guarantees, they often fail to capture the finite-sample behavior. As a result, recent efforts have focused on analyzing the sample complexity of common system identification methods.

A

On the other hand, in many applications, system designers have prior knowledge on the noise characteristics. Therefore, alternative system identification approaches seek to harness this information to improve sample efficiency. Among these, set membership estimation (SME) algorithms leverage noise boundedness for estimation. One of the key advantages of SME is its ability to provide consistent uncertainty set estimation with convergence guarantees, whereas OLS fails to do so for irregular explosive systems.

Motivated, in this paper, we derive a minimax convergence rate lower bound for system identification when $\mathbf{w}_{t}$ is i.i.d. zero-mean with bounded support. We prove that indeed $\Omega{({1/T})}$ is the minimax lower bound for stable linear dynamical systems with bounded noise (Theorem 1. ‣ 3.1 Minimax Sample Complexity Lower Bound ‣ 3 Main results ‣ System Identification Under Bounded Noise: Optimal Rates Beyond Least Squares")), establishing that the rate achieved by SME is indeed optimal.

## Conclusion

This work establishes the minimax sample complexity lower bound for system identification under bounded i.i.d. noise, showing that SME-based methods achieve the optimal $\Omega{({1/T})}$ convergence rate while the ordinary least squares estimator remains limited to $\Omega{({1/\sqrt{T}})}$. Future work includes improving the dimension and $\delta$ dependence of the lower bound, which is admittedly loose in our current analysis. It will also be interesting to extend the analysis to more general bounded noise models beyond the infinity norm bound.
