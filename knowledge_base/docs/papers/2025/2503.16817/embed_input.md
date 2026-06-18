System Identification under Bounded Noise: Optimal Rates beyond Least Squares

Topics include System identification, Bounded noise, Least squares, Sample complexity, Linear systems, Optimality, Robustness.

Studies system identification when disturbances are bounded rather than stochastic in the usual least-squares-friendly way. The paper gives optimal-rate results beyond classical least squares, clarifying what estimators can exploit under adversarial or deterministic noise bounds.

System identification is a fundamental problem in control and learning, particularly in high-stakes applications where data efficiency is critical. Classical approaches, such as the ordinary least squares estimator (OLS), achieve an O(1/sqrt(T)) convergence rate under Gaussian noise assumptions, where T is the number of samples. This rate has been shown to match the lower bound. However, in many practical scenarios, noise is known to be bounded, opening the possibility of improving sample complexity. In this work, we establish the minimax lower bound for system identification under bounded noise, proving that the O(1/T) convergence rate is indeed optimal. We further demonstrate that OLS remains limited to an (1/sqrt(T)) convergence rate, making it fundamentally suboptimal in the presence of bounded noise. Finally, we instantiate two natural variations of OLS that obtain the optimal sample complexity.

## Introduction

System identification plays a crucial role in modern control design, especially in applications where accurate models of unknown dynamical systems must be learned from data. In high-stakes and safety-critical systems, where data collection can be costly or risky, sample efficiency is of particular importance. While classical results in system identification provide asymptotic convergence guarantees, they often fail to capture the finite-sample behavior. As a result, recent efforts have focused on analyzing the sample complexity of common system identification methods.

A fundamental system identification problem is to estimate the unknown system parameter $\mathbf{A} \in {\mathbb{R}}^{n \times n}$ for an autonomous linear time-invariant (LTI) system:

## Conclusion

This work establishes the minimax sample complexity lower bound for system identification under bounded i.i.d. noise, showing that SME-based methods achieve the optimal $\Omega{({1/T})}$ convergence rate while the ordinary least squares estimator remains limited to $\Omega{({1/\sqrt{T}})}$. Future work includes improving the dimension and $\delta$ dependence of the lower bound, which is admittedly loose in our current analysis. It will also be interesting to extend the analysis to more general bounded noise models beyond the infinity norm bound.

### Theorem 1 (Minimax Lower Bound)

There exists $C_{\overline{w}} > 0$ such that for all $\epsilon \in {\lbrack 0,\overline{w}\rbrack}$ and for all $1 \leq j \leq n$, we have

In what follows, we will show that OLS does not achieve the optimal rate for systems under bounded noise. For simplicity of analysis, we will focus on scalar systems.

where $\mathbf{x}_{t} \in {\mathbb{R}}^{n}$ and $\mathbf{w}_{t} \in {\mathbb{R}}^{n}$ are the state and the noise at time $t$. When the noise $\mathbf{w}_{t}$ are independent and identically distributed (i.i.d.) Gaussian random variables, it has been shown that the ordinary least squares estimator (OLS) achieves the optimal convergence rate of $O{({1/\sqrt{T}})}$. Consequently, many learning-based control methods have leveraged OLS as a core system identification subroutine, enabling stability, safety, and performance guarantees.

On the other hand, in many applications, system designers have prior knowledge on the noise characteristics....
