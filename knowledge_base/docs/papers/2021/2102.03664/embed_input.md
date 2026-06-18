Efficient Learning of a Linear Dynamical System with Stability Guarantees

Topics include Stability analysis, Learning, Linear dynamical system.

We propose a principled method for projecting an arbitrary square matrix to the non-convex set of asymptotically stable matrices. Leveraging ideas from large deviations theory, we show that this projection is optimal in an information-theoretic sense and that it simply amounts to shifting the initial matrix by an optimal linear quadratic feedback gain, which can be computed exactly and highly efficiently by solving a standard linear quadratic regulator problem. The proposed approach allows us to learn the system matrix of a stable linear dynamical system from a single trajectory of correlated state observations. The resulting estimator is guaranteed to be stable and offers explicit statistical bounds on the estimation error.

## Introduction

We study the problem of learning a stable linear dynamical system from a single trajectory of correlated state observations. This problem is of fundamental importance in various disciplines such as adaptive control, system identification, reinforcement learning and approximate dynamic programming. Specifically, we consider a discrete-time linear time-invariant system of the form

where $x_{t} \in {\mathbb{R}}^{n}$ and $w_{t} \in {\mathbb{R}}^{n}$ denote the state and the exogenous noise at time $t \in {\mathbb{N}}$, respectively, while $\theta$ represents a fixed system matrix, and $\nu$ stands for the marginal distribution of the initial state $x_{0}$. We assume that $\theta$ is asymptotically stable, that is, it belongs to $\Theta = {\{{\theta \in {\mathbb{R}}^{n \times n}}:{{\rho{(\theta)}} < 1}\}}$, where $\rho{(\theta)}$ denotes the largest absolute eigenvalue of $\theta$....

### Example 4.3 (Statistical guarantees)

The second experiment is designed to validate the statistical guarantees of Proposition 3.12. ‣ 3.2 Statistics of the reverse 𝐼-projection ‣ 3 Reverse 𝐼-projection ‣ Efficient Learning of a Linear Dynamical System with Stability Guarantees"). To this end, choose $n \in {\{ 1,10,100\}}$, and sample 100 stable matrices from a standard normal distribution on ${\mathbb{R}}^{n \times n}$ restricted to $\Theta$....

### Example 3.5 (System identification)

## Reverse $I$-projection

Note that the finite sample bound (3.3a. ‣ 3.2 Statistics of the reverse 𝐼-projection ‣ 3 Reverse 𝐼-projection ‣ Efficient Learning of a Linear Dynamical System with Stability Guarantees")), which leverages sophisticated results from \[55, § 6\], and the bound (3.3b. ‣ 3.2 Statistics of the reverse 𝐼-projection ‣ 3 Reverse 𝐼-projection ‣ Efficient Learning of a Linear Dynamical System with Stability Guarantees")), which follows almost immediately from the moderate deviations principle of Section 3.1, are qualitatively similar....

which may take any value in $\Theta^{\prime} = {\mathbb{R}}^{n \times n}$ under standard assumptions on the noise distribution. It is therefore possible that ${\hat{\theta}}_{T} \notin \Theta$ even though $\theta \in \Theta$. This is troubling because stability is important in many applications, for example, when the estimated model is used for prediction, filtering or control, e.g., see the discussions in \[67, pp....
