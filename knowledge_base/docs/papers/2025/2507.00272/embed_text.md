### Introduction

The Kalman filter is the prevalent tool for state estimation, prized for its simplicity, low computational cost, and optimality for linear-Gaussian systems. It has found extensive use in many fields, including control, signal processing, robotics, navigation, neural interface systems, and econometrics \[Kalman1960, MalikTBH2010, SmetsW2007, Huber2022\]. Despite its popularity, the KF is notoriously vulnerable to outliers in the measurements and process noise in the dynamics \[MasreliezM1977\]. Measurement outliers may arise from occasional sensor malfunctions, while process noise outliers can result from sudden shocks to the system or unmodeled dynamics.

In this work, we propose the iteratively saturated Kalman filter, which is a modification of the standard KF's update (or correction) step. It iterates a modified KF update step, in which a saturating nonlinearity is applied to compensate for both measurement and process noise outliers. The method is derived as a scaled gradient method \[Davidon1959, FletcherR1963\] for solving a particular convex robust estimation problem involving the Huber function. Since the ISKF typically requires only one or two iterations to achieve good performance, it retains the standard KF's ease of implementation and per-step cost.

A key advantage of the ISKF is its steady-state variant, which matches the computational efficiency of the steady-state KF. Whereas the full KF must update its covariance estimate at each step, incurring matrix-matrix multiplications and linear solves, the steady-state KF uses precomputable gain matrices and requires only matrix-vector multiplications and vector additions. Our steady-state ISKF inherits this low per-step cost while compensating for both measurement and process-noise outliers. In contrast, existing robust KF extensions either lack robustness to process-noise outliers or rely on full covariance estimates in each step.

The rest of the paper is organized as follows. We review prior work in §[1.2](https://arxiv.org/html/2507.00272v1#Chx1.S2 "1.2 Prior work ‣ Iteratively Saturated Kalman Filtering"). The system model is given in §[1.3](https://arxiv.org/html/2507.00272v1#Chx1.S3 "1.3 System model ‣ Iteratively Saturated Kalman Filtering"), and the iteratively saturated Kalman filter is introduced in §[1.4](https://arxiv.org/html/2507.00272v1#Chx1.S4 "1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering"). We derive the filter as a scaled gradient method in §[1.5](https://arxiv.org/html/2507.00272v1#Chx1.S5 "1.5 Derivation as a scaled gradient method ‣ Iteratively Saturated Kalman Filtering"). Finally, we present numerical experiments in §[1.8](https://arxiv.org/html/2507.00272v1#Chx1.S8 "1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") and conclude in §[1.9](https://arxiv.org/html/2507.00272v1#Chx1.S9 "1.9 Conclusion ‣ Iteratively Saturated Kalman Filtering").

### Prior work

There is a large body of work on modifying the KF to be robust to outliers without sacrificing its computational efficiency. Many of these heuristics involve modifying the covariance estimate in each KF step, by scaling the measurement noise covariance matrix or the process and prior covariance matrices when outliers are detected \[DurovicK1999, Chang2014, DuranMartinAS2024\]. The idea is that if an outlier is detected, the corresponding covariance should be scaled up to account for the increased uncertainty. Some variations of this idea were derived by replacing the Gaussian distribution used by the KF with heavy-tailed distributions \[TingTS2007, AgamennoniNN2011\]. Others are derived by Huberizing the quadratic costs used by the KF \[Huber1964, MasreliezM1977, CipraR1991, KovacevicD1992, DurovicK1999, MattingleyB2012\].

Yet others have proposed combining the KF with inlier detection methods such as RANSAC \[Cantzler1981, VedaldiJFS2005\]. Several of the robust KF methods have also been extended to nonlinear systems \[PicheSH2012, Karlgaard2015\].

Our method generalizes the saturated KF \[FangHHW2018\] by compensating for process noise outliers in addition to measurement outliers. In the single-step case, our method is almost equivalent to the saturated KF, but uses a different saturation function.

Besides modified KF methods, we also mention particle filtering methods, which have been applied to handle outliers \[BoustatiADJ2020\], although they tend to be computationally expensive.

### System model

We consider a linear time-invariant dynamical system that evolves according to

where $t$ denotes time or epoch, $x_{t} \in \text{R}^{n}$ is the state, and $y_{t} \in \text{R}^{p}$ is the output measurement. The matrix $A \in \text{R}^{n \times n}$ is the state dynamics matrix, and $C \in \text{R}^{p \times n}$ is the output matrix. We assume that the dynamics matrix $A$ and the output matrix $C$ are known. The dynamics are driven by the process noise $w_{t} \in \text{R}^{n}$, and the outputs are influenced by the measurement noise $v_{t} \in \text{R}^{p}$. We assume that the initial state $x_{0}$ is Gaussian, with $x_{0} \sim {\mathcal{N}{(0,X_{0})}}$.

### Linear Gaussian model

In the classical model, the process noise $w_{t} \in \text{R}^{n}$ and the measurement noise $v_{t} \in \text{R}^{p}$ are Gaussian with

where $W$ is the known positive semidefinite (PSD) process noise covariance (which can be degenerate, i.e., singular) and $V$ is the known positive definite (PD) measurement noise covariance. We assume that the initial state $x_{0}$, the process noise $w_{t}$, and the measurement noise $v_{t}$ are independent and identically distributed (IID). In this case, the state and measurements are jointly Gaussian, and the Kalman filter \[Kalman1960\] gives the optimal estimate of the state, both in the minimum mean squared error (MMSE) and maximum a posteriori (MAP) sense.

### Outlier model

In this work, we consider a model where the process and measurement noises are typically Gaussian, but may occasionally be corrupted by outliers. We consider the model

where $F \in \text{R}^{n \times m}$ and $G \in \text{R}^{p \times p}$ are known matrices, and ${\overset{\sim}{w}}_{t} \in \text{R}^{m}$ and ${\overset{\sim}{v}}_{t} \in \text{R}^{p}$ are zero-mean whitened Gaussian noises with ${\overset{\sim}{w}}_{t} \sim {\mathcal{N}{(0,I)}}$ and ${\overset{\sim}{v}}_{t} \sim {\mathcal{N}{(0,I)}}$. The additional terms $s_{t} \in \text{R}^{n}$ and $o_{t} \in \text{R}^{p}$ are sparse outlier terms which are zero for most times $t$.

The process noise outliers $s_{t}$ can result from system shocks or unmodeled dynamics, while measurement outliers $o_{t}$ can arise from sensor malfunctions or environmental disturbances. In the absence of outliers, i.e., when $s_{t} = 0$ and $o_{t} = 0$ for all $t$, the system reduces to the linear Gaussian model, with $W = {FF^{T}}$ and $V = {GG^{T}}$.

### Extensions

Several extensions of the system model are readily handled. The model can be modified to handle known control inputs, process and measurement noises $w_{t}$ and $v_{t}$ with nonzero mean, and correlation between $w_{t}$ and $v_{t}$. We may also consider the time-varying case, where $A$, $C$, $W$, and $V$ are allowed to vary with $t$.

### Iteratively saturated Kalman filtering

Given a sequence of measurements $y_{1},\ldots,y_{t}$, our goal is to recursively estimate both the state $x_{t}$ and its covariance $P_{t}$. At each time step $t$, we update our previous estimates ${\hat{x}}_{t - {1 \mid {t - 1}}}$ and $P_{t - {1 \mid {t - 1}}}$ to obtain new estimates ${\hat{x}}_{t \mid t}$ and $P_{t \mid t}$. We assume in the following that $(A,C)$ is detectable and $(A,W^{1/2})$ is stabilizable \[Simon2006\]. Here, $W^{1/2}$ denotes any matrix such that ${{(W^{1/2})}^{T}W^{1/2}} = W$. Such a matrix can be found from the eigenvalue decomposition of $W$, or when $W$ is PD, via Cholesky factorization.

Our estimator starts with the standard Kalman filter prediction step

The update step is then given by the iteration

for $k = {1,\ldots,\overset{\sim}{k}}$, where $\overset{\sim}{k}$ denotes the number of iterations. We then take ${\hat{x}}_{t \mid t} = {\hat{x}}^{\overset{\sim}{k}}$. The nonlinear functions

saturate their inputs at threshold values $\lambda_{x}$ and $\lambda_{y}$, respectively, and $K_{t}$ is the Kalman gain matrix satisfying the standard Kalman filter covariance update equations

### Comments

Our filter compensates for outliers in the measurements by reducing the effect of outliers in the measurement noise on the state estimate by attenuating the magnitude of the *innovation* $y_{t} - {C{\hat{x}}_{t \mid {t - 1}}}$ when

is large, i.e., unlikely under the Gaussian noise model. Similarly, our filter compensates for outliers in the process noise by attenuating the magnitude of the proximity to the predicted state ${\hat{x}}_{t \mid {t - 1}}$.

### Single-step case

When $\overset{\sim}{k} = 1$, the update step ([1.6](https://arxiv.org/html/2507.00272v1#Chx1.E6 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")) is simply

In this case, the ISKF does not compensate for outliers in the process noise, only in the measurements. It closely resembles the standard KF, except that the innovation $y_{t} - {C{\hat{x}}_{t \mid {t - 1}}}$ is attenuated by the function $\sigma$. The single-step ISKF is very similar to the saturated KF \[FangHHW2018\], but uses a different saturation function.

### Outlier-free case

In the absence of detected outliers, our state estimate ${\hat{x}}_{t \mid t}$ satisfies

and the saturation functions $\rho_{t}$ and $\sigma$ reduce to the identity function. In this case, the ISKF is equivalent to the standard KF

with ${\hat{x}}^{k} = {\hat{x}}_{t \mid t}^{\text{kf}}$ for all $k$.

### Computational cost

At each time step, the ISKF costs $O{({\overset{\sim}{k}{({n^{3} + p^{3} + {np}})}})}$ floating-point operations (FLOPS) online, dominated by matrix-matrix products and solving a linear system. For $\overset{\sim}{k}$ fixed and small, this is comparable to the cost of the KF. In our experiments, we found that values between 1 and 5 were effective.

### Steady-state case

A key property of the Kalman filter recursion is that the covariance update steps ([1.4](https://arxiv.org/html/2507.00272v1#Chx1.E4 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")) and ([1.8](https://arxiv.org/html/2507.00272v1#Chx1.E8 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")) are independent of the measurements. This means we can compute $P_{t \mid t}$ offline, before processing any measurements. Furthermore, as $t\rightarrow\infty$, the covariance matrices $P_{t \mid t}$, $P_{t \mid {t - 1}}$, and gain matrix $K_{t}$ converge to steady-state values given by:

respectively. In steady-state, we may dispense with the covariance and gain update steps ([1.4](https://arxiv.org/html/2507.00272v1#Chx1.E4 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")), ([1.7](https://arxiv.org/html/2507.00272v1#Chx1.E7 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")), and ([1.8](https://arxiv.org/html/2507.00272v1#Chx1.E8 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")).

This leads to the *steady-state ISKF*

for $k = {1,\ldots,\overset{\sim}{k}}$. Like before, we take ${\hat{x}}_{t \mid t} = {\hat{x}}^{\overset{\sim}{k}}$. Here, we drop the subscript $t$ on the function $\rho$, since it is now time-invariant.

Since $K$ can be precomputed offline, the steady-state ISKF only requires matrix-vector multiplications and vector additions online, with has cost $O{({\overset{\sim}{k}{({n^{2} + {np}})}})}$ FLOPS online. Since the convergence of $P_{t}$ to $P$ is in practice often quick, the ISKF estimate ([1.10](https://arxiv.org/html/2507.00272v1#Chx1.E10 "In Steady-state case. ‣ 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")) gives an excellent approximation to the ISKF ([1.6](https://arxiv.org/html/2507.00272v1#Chx1.E6 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")).

### Derivation as a scaled gradient method

In this section, we show that the ISKF can be interpreted as a scaled gradient method for solving a convex regularized maximum a posteriori (MAP) estimation problem in which we estimate $x_{t}$, $s_{t}$, and $o_{t}$ jointly. We focus on the steady-state case for simplicity, but the discussion applies to the general case by replacing $P$ with $P_{t \mid t}$ and $\Sigma$ with $P_{t \mid {t - 1}}$, and adding the subscript $t$ on $K$ and $\rho$.

### Model

At each time step $t$, we consider the optimization problem

with variables $x$, $s$, and $o$. This is a convex optimization problem, and it has the following interpretation. When the outlier terms $s$ and $o$ are known and fixed, the first term corresponds to the negative log likelihood of the prior distribution over $x_{t}$ and the measurement noise. The second and third terms are sparse regularization terms on $s$ and $o$. When the thresholds $\lambda_{x}$ and $\lambda_{y}$ are infinite, the optimal values of $s$ and $o$ are zero, and the optimal value of $x$ is simply given by the (steady-state) KF estimate ${\hat{x}}_{t \mid t}^{\text{kf}}$.

### Comments

Our optimization problem is only an approximate MAP estimate, since in general we do not have a statistical model of the outliers $s_{t}$ and $o_{t}$. Moreover, in the presence of process noise outliers, the prior distribution over $x_{t}$ is no longer necessarily Gaussian with mean ${\hat{x}}_{t \mid {t - 1}}$ and covariance $P$. The goal is to reduce the influence of outliers on the state estimate by regularization, where the regularization terms are chosen such that the partial minimizations over $s$ and $o$ have closed-form solutions which can be written in terms of the Huber function.

### Circular Huber function

Let the function $\varphi$ denote the partial minimization

The function $\varphi$ has a closed-form solution given by

We refer to this function as the *circular Huber function* with threshold $\lambda$. It is a smooth convex function that is quadratic for ${\| a\|}_{2} \leq \lambda$, and grows only linearly with the norm of $a$ for ${\| a\|}_{2} > \lambda$. It is equivalent to the standard Huber function, composed with the Euclidean norm.

The estimation problem may then be written as

For future reference, we observe that the Hessian satisfies ${{\nabla^{2}\varphi}{(a;\delta)}} \leq I$, which implies that its gradient ${\nabla\varphi}{(a;\delta)}$ has Lipschitz constant one.

### Scaled gradient method

We propose a scaled gradient method for minimizing ([1.11](https://arxiv.org/html/2507.00272v1#Chx1.E11 "In Circular Huber function. ‣ 1.5.1 Model ‣ 1.5 Derivation as a scaled gradient method ‣ Iteratively Saturated Kalman Filtering")) over $x \in \text{R}^{n}$. The method has iterates

where $\eta \in {}$ is a constant step size,

is the scaling matrix, and the initial iterate $x^{0} = {\hat{x}}_{t|{t - 1}}$ is the predict step given by ([1.3](https://arxiv.org/html/2507.00272v1#Chx1.E3 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")).

The gradient of $f$ is given by

To simplify the scaled gradient $M^{- 1}{\nabla f}{(x)}$, we can use the fact that the Kalman gain can be written as

by applying the Woodbury matrix identity. Then, since ${\nabla\varphi}{(a;\lambda)}$ is a scalar multiple of $a$, the scaled gradient becomes

By setting the step size $\eta = 1$, we arrive at the ISKF update ([1.6](https://arxiv.org/html/2507.00272v1#Chx1.E6 "In 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")). Note that in practice, it may be numerically advantageous to implement the saturation functions as

where $\nabla\varphi$ has the form in ([1.13](https://arxiv.org/html/2507.00272v1#Chx1.E13 "In 1.5.2 Scaled gradient method ‣ 1.5 Derivation as a scaled gradient method ‣ Iteratively Saturated Kalman Filtering")), since the division by ${\| a\|}_{2}$ only occurs when ${\| a\|}_{2} > \lambda$.

### Choice of gradient method

In general a gradient method would be a very poor choice for a problem that must be solved in real-time, since its practical convergence can vary considerably depending on the input data. An interior-point method, which typically takes around 20 or so steps independent of the data, would seem like a better choice. We propose the use of a gradient method in this specific case only because an excellent estimate of the curvature of the function $f$ is available, which eliminates the need for a line search, and gives very good estimates in just a few iterations, independent of the data.

### Convergence

We now show that the scaled gradient method converges to a solution, and is a strict descent method, when the iterations are not terminated. Let $L$ be a matrix that satisfies ${LL^{T}} = M^{- 1}$, e.g., the Cholesky factorization of $M^{- 1}$. Let ${g{(z)}} = {f{({Lz})}}$. The scaled gradient method is then equivalent to the iteration

where $x^{k} = {Lz^{k}}$ for all $k$. To establish convergence and the descent property, it is sufficient to show that the gradient $\nabla g$ is Lipschitz continuous with constant one \[Polyak1987\]. Note that an upper bound on the Lipschitz constant of $\nabla g$ can be found by taking $\lambda_{x}$ and $\lambda_{y}$ to infinity, in which case $g$ is a quadratic function. In that case, $g{(z)}$ is given by

it follows that $\nabla g$ has Lipschitz constant one.

### Parameter selection

The performance of the ISKF depends on the number of iterations $\overset{\sim}{k}$ and the choice of parameters $\lambda_{x}$ and $\lambda_{y}$.

### Number of iterations

In our experiments, we found that the ISKF can compensate for outliers in the measurement noise even with $\overset{\sim}{k} = 1$, and outliers in both the measurement noise and process noise even with $\overset{\sim}{k} = 2$. While small improvements can be achieved for larger $\overset{\sim}{k}$, we found $\overset{\sim}{k} = 2$ to be a good default choice, with more iterations giving diminishing returns.

### Threshold parameters

The parameters $\lambda_{x}$ and $\lambda_{y}$ balance robustness against outliers and estimate bias. Larger values of $\lambda_{x}$ and $\lambda_{y}$ are ideal when there are no outliers (with $\lambda_{x} = \lambda_{y} = \infty$ reducing to the standard KF), while tuned values improve performance when outliers are present.

### Step size

The discussion in §[1.5.2](https://arxiv.org/html/2507.00272v1#Chx1.S5.SS2 "1.5.2 Scaled gradient method ‣ 1.5 Derivation as a scaled gradient method ‣ Iteratively Saturated Kalman Filtering") suggests that the step size $\eta$ in the scaled gradient method could be made a tunable parameter. The (steady-state) ISKF ([1.10](https://arxiv.org/html/2507.00272v1#Chx1.E10 "In Steady-state case. ‣ 1.4 Iteratively saturated Kalman filtering ‣ Iteratively Saturated Kalman Filtering")) can be modified as

However, we suggest fixing $\eta = 1$ in practice. In our experiments, we found that increasing $\eta$ to be greater than one could give marginal improvements, but at the cost of reducing the performance of the filter when there are no outliers present. This is because $\eta$ effectively acts as a type of gain parameter for the filter. This is most clearly seen in the single-step case. When $\overset{\sim}{k} = 1$ and there are no detected outliers (the saturation function $\sigma$ is identity), the ISKF reduces to the standard KF with gain matrix $\eta K$. Choosing $\eta = 1$ leads to a natural interpretation, since the filter is then equivalent to the standard KF when there are no detected outliers.

### Grid search

The parameters may be chosen via a simple grid search, given a sequence of measurements $y_{1},\ldots,y_{N}$ collected in the past. For each combination of parameters, the ISKF can be run on the past data containing outliers, and the parameter combination that best predicts the observed measurements is chosen. For each parameter combination, we compute the RMSE of the predicted measurements

although other metrics could be used. Note that we consider the RMSE of the residuals $y_{t} - {CA{\hat{x}}_{t - {1 \mid {t - 1}}}}$, rather than the innovations $y_{t} - {C{\hat{x}}_{t \mid t}}$, since the estimate ${\hat{x}}_{t \mid t}$ is computed as a function of $y_{t}$.

In practice, a strategy for choosing the parameters is to first fix the number of iterations $\overset{\sim}{k}$ based on the computational budget, and then search over $\lambda_{x}$ and $\lambda_{y}$ to minimize the RMSE.

### Extensions and variations

### Time-varying and non-linear systems

When the system model ([1.1](https://arxiv.org/html/2507.00272v1#Chx1.E1 "In 1.3 System model ‣ Iteratively Saturated Kalman Filtering")) is time-varying, we introduce subscripts $t$ to the matrices $A$, $C$, $W$, and $V$. The ISKF naturally extends to this scenario, though a steady-state version typically does not exist. For nonlinear systems, we approximate the model by linearizing around the current state estimate, resulting in time-varying matrices $A_{t}$, $C_{t}$, $W_{t}$, and $V_{t}$. Similar to how the EKF and UKF generalize the KF to nonlinear cases, analogous modifications enable the ISKF to handle nonlinear systems by iteratively updating the linearization.

### Missing measurements

We have assumed thus far that the measurements $y_{t}$ are fully available at each time $t$. When this is not the case, the update step is replaced with conditioning on only the *known entries* of $y_{t}$. The most general way to handle this is to allow for any subset of the entries of $y_{t}$ to be known or unknown. This is equivalent to the case where the measurement matrix $C$ and measurement covariance $V$ are time-varying, where only the rows of $C$ and $V$ corresponding to the available measurements are included. In the case where no measurements are available, the update step is skipped.

However, this approach leads to a time-varying system, so cannot be applied to the steady-state case without increasing the online computational cost from $O{({n^{2} + {np}})}$ to $O{({n^{3} + p^{3} + {np}})}$. Alternatively, there are only $2^{p}$ possible patterns of missing measurements. If $2^{p}$ isn't too large, we could precompute a different steady-state Kalman gain matrix $K$ for each pattern of known measurements.

### Numerical experiments

In this section, we present numerical experiments evaluating the performance of the ISKF, in comparison with the KF and other outlier-robust filters. In our experiments, we use the steady-state form of the ISKF and the KF.

### Competing methods

We compare the steady-state ISKF against the steady-state KF, and two outlier-robust Kalman filter variants: the weighted observation likelihood filter (WoLF) \[DuranMartinAS2024\] and the Huberized KF \[Huber1964, MasreliezM1977, CipraR1991, KovacevicD1992, DurovicK1999\]. WoLF is a covariance scaling method, and is only designed to reject measurement outliers. Our implementation of the Huberized KF solves the Huber regression problem ([1.11](https://arxiv.org/html/2507.00272v1#Chx1.E11 "In Circular Huber function. ‣ 1.5.1 Model ‣ 1.5 Derivation as a scaled gradient method ‣ Iteratively Saturated Kalman Filtering")) using the interior-point method Clarabel \[GoulartC2024\]. Both WoLF and the Huberized KF have online computational cost approximately $O{({n^{3} + p^{3} + {np}})}$, comparable to the full KF. In contrast, the steady-state ISKF and steady-state KF have online cost $O{({n^{2} + {np}})}$.

### Evaluation

We evaluate the performance of each filter on a simulated test trajectory of, using the state estimate RMSE

where $x_{t}$ is the true state and ${\hat{x}}_{t \mid t}$ is the state estimate produced by a filter. For the purposes of evaluation, we assume that the true state trajectory is available. Test trajectories had lengths of $1000$ time steps.

### Parameter selection

We tuned the parameters of each filter using a separate simulated trajectory than the test trajectory used for evaluation. Unlike the test trajectory, we assumed that the true state trajectory was not available for the tuning trajectory data. Instead, we minimized the predicted measurement RMSE ([1.16](https://arxiv.org/html/2507.00272v1#Chx1.E16 "In Grid search. ‣ 1.6 Parameter selection ‣ Iteratively Saturated Kalman Filtering")) in our grid search. For all parameters, we considered 20 values between $0.1$ and $10$, logarithmically spaced. Like the test trajectory, the tuning trajectory had length $1000$ time steps. The ISKF (for $\overset{\sim}{k} > 1$) and the Huberized KF have two tunable parameters, and WoLF has one.

### Vehicle tracking

### System model

The position and velocity of a vehicle in two dimensions are denoted $\xi_{t} \in \text{R}^{2}$ and $\nu_{t} \in \text{R}^{2}$. At time $t$, we observe a noisy measurement of the position $\xi_{t}$, and aim to estimate the state $x_{t} = {(\xi_{t},\nu_{t})}$. The vehicle has unit mass, and is subject to a drag force $- {\gamma\nu_{t}}$ with coefficient of friction $\gamma = 0.05$. The discrete-time system with time step $h = 0.05$ is

The vehicle is driven by a random applied force $u_{t} \in \text{R}^{2}$, which is distributed according to

The measurement noise $v_{t} \in \text{R}^{2}$ is distributed according to

such that $10\%$ of the samples are large outliers. This fits the system model ([1.2](https://arxiv.org/html/2507.00272v1#Chx1.E2 "In Outlier model. ‣ 1.3 System model ‣ Iteratively Saturated Kalman Filtering")) with $F = {\sqrt{10}B}$ and $G = {\sqrt{5}I}$.

Figure 1.1: True vehicle position over time, along with measurements and position estimates produced by the (steady-state) ISKF and KF.

Figure 1.2: Vehicle tracking state estimate errors (absolute values) for the KF and the two-iteration ISKF.

### Performance comparison

With the number of iterations fixed at $\overset{\sim}{k} = 2$, we selected the parameters to be

using the grid search procedure described in §[1.6](https://arxiv.org/html/2507.00272v1#Chx1.S6 "1.6 Parameter selection ‣ Iteratively Saturated Kalman Filtering"). The grid search was carried out over the predicted measurement RMSE ([1.16](https://arxiv.org/html/2507.00272v1#Chx1.E16 "In Grid search. ‣ 1.6 Parameter selection ‣ Iteratively Saturated Kalman Filtering")) on a separate simulated trajectory of measurements. Figure [1.1](https://arxiv.org/html/2507.00272v1#Chx1.F1 "Figure 1.1 ‣ System model. ‣ 1.8.1 Vehicle tracking ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") shows the true vehicle position over time, along with measurements and position estimates produced by the (steady-state) ISKF and KF. Figure [1.2](https://arxiv.org/html/2507.00272v1#Chx1.F2 "Figure 1.2 ‣ System model. ‣ 1.8.1 Vehicle tracking ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") shows the state estimate errors (absolute values) for the KF and the two-iteration ISKF.

Table [1.1](https://arxiv.org/html/2507.00272v1#Chx1.T1 "Table 1.1 ‣ Performance comparison. ‣ 1.8.1 Vehicle tracking ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") shows the state estimate RMSE ([1.17](https://arxiv.org/html/2507.00272v1#Chx1.E17 "In Evaluation. ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering")) evaluated for several filters on the same test trajectory. The ISKF with $\overset{\sim}{k} = 1$ achieves comparable performance to WoLF, as both are only designed to reject measurement outliers. The (steady-state) ISKF with $\overset{\sim}{k} = 2$ and $\overset{\sim}{k} = 3$ achieves better performance than WoLF, and performs comparably to the Huberized KF, at lower computational cost.

ISKF ($\overset{\sim}{k} = 1$)

ISKF ($\overset{\sim}{k} = 2$)

ISKF ($\overset{\sim}{k} = 3$)

Table 1.1: State estimate RMSE comparison of several filtering methods for the vehicle tracking example. All filters were tuned using the same data, and evaluated on the same test data.

Figure 1.3: Parameter tuning for vehicle tracking example. Left: state estimate RMSE vs. number of iterations $\overset{\sim}{k}$. A grid search was performed to choose λx and λy for each value of $\overset{\sim}{k}$. Right: contour plot of state estimate RMSE (1.17) for different values of λx and λy.

### Effect of parameters

Figure [1.3](https://arxiv.org/html/2507.00272v1#Chx1.F3 "Figure 1.3 ‣ Performance comparison. ‣ 1.8.1 Vehicle tracking ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") illustrates the effect of the parameters $\overset{\sim}{k}$, $\lambda_{x}$, and $\lambda_{y}$ on the performance of the ISKF on the test data. The left plot shows the best-achieved state estimate RMSE (by grid search) for each value of $\overset{\sim}{k}$. The ISKF achieves a $30\%$ improvement over the KF after two iterations, and does not improve after three iterations. The contour plot on the right shows the state estimate RMSE for different values of $\lambda_{x}$ and $\lambda_{y}$.

### Cascaded continuously-stirred tank reactor

### CSTR model

The adiabetic continuous stirred-tank reactor (CSTR) is a commonly-appearing system in the chemical process industry \[Bequette1998, SeborgEMD2016\]. We consider an ideal model of a single, first-order exothermic and irreversible reaction taking place in a reactor tank, which is assumed to be perfectly-mixed. The reagent enters the tank through the inlet at a constant rate, and the output product leaves the reactor at the same constant rate. The state consists of the concentration of the reagent $c$ and the temperature $\tau$ in the reactor, and the dynamics are controlled by the inlet concentration $c^{\text{in}}$ and the tank's jacket coolant temperature $\tau^{\text{c}}$.

The continuous-time dynamics are linearized around an operating point $(c_{0},\tau_{0},c_{0}^{\text{in}},\tau_{0}^{\text{c}})$. In the linearized model, the state is $\xi = {({c - c_{0}},{\tau - \tau_{0}})}$, and the process is driven by $u = {({c^{\text{in}} - c_{0}^{\text{in}}},{\tau^{\text{c}} - \tau_{0}^{\text{c}}})}$. We observe measurements of the reactor's temperature, but not of the reagent concentration. The discrete-time dynamics with step size of $h$ are

where $\nu_{t} \in \text{R}$ is the measurement noise and the matrices are \[MathWorksCSTRModel2025\]

Note that here, $y_{t}$ represents a measurement of the temperature offset from the operating point $\tau_{0}$, rather than the temperature itself.

### System model

In this example, we consider a cascade of three such reactors, with the state of each reactor being the input to the next. Let $c_{i}$ and $\tau_{i}$ be the reagent concentration and temperature of the $i$-th reactor, respectively. Then, the cascaded system has state $x \in \text{R}^{6}$ given by $x = {(\xi_{1},\xi_{2},\xi_{3})}$, where $\xi_{i} = {({c_{i} - c_{0}},{\tau_{i} - \tau_{0}})}$ is the state of the $i$-th reactor. The cascaded system has discrete-time model

and $w \in \text{R}^{6}$ and $v \in \text{R}^{3}$ are the process and measurement noises, with $F$ and $G$ matrices given by

The process noise $w_{t}$ and measurement noise $v_{t}$ are distributed according to

We discretized the continuous-time dynamics with a step size of $h = {50\text{ms}}$. The operating point is $c_{0} = {2\text{kmol/m}^{3}}$, $\tau_{0} = {373\text{K}}$, $c^{\text{in}} = {10\text{kmol/m}^{3}}$, and $\tau^{\text{c}} = {299\text{K}}$.

Figure 1.4: True reagent concentration and temperature values over time, along with measurements and state estimates produced by the (steady-state) ISKF and KF.

Figure 1.5: State estimate errors (absolute values) for the KF and the two-iteration ISKF.

### Performance comparison

With the number of iterations fixed at $\overset{\sim}{k} = 2$, we selected the parameters to be

using the grid search procedure described in §[1.6](https://arxiv.org/html/2507.00272v1#Chx1.S6 "1.6 Parameter selection ‣ Iteratively Saturated Kalman Filtering"). Like in the vehicle tracking example, the grid search was carried out over the predicted measurement RMSE ([1.16](https://arxiv.org/html/2507.00272v1#Chx1.E16 "In Grid search. ‣ 1.6 Parameter selection ‣ Iteratively Saturated Kalman Filtering")) on a separate simulated trajectory of measurements. Figure [1.4](https://arxiv.org/html/2507.00272v1#Chx1.F4 "Figure 1.4 ‣ System model. ‣ 1.8.2 Cascaded continuously-stirred tank reactor ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") shows the true reagent concentration and temperature values over time, along with measurements and estimates produced by the (steady-state) ISKF and KF. Figure [1.5](https://arxiv.org/html/2507.00272v1#Chx1.F5 "Figure 1.5 ‣ System model. ‣ 1.8.2 Cascaded continuously-stirred tank reactor ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") shows the state estimate errors (absolute values) for the KF and the two-iteration ISKF.

Table [1.2](https://arxiv.org/html/2507.00272v1#Chx1.T2 "Table 1.2 ‣ Performance comparison. ‣ 1.8.2 Cascaded continuously-stirred tank reactor ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") shows the state estimate RMSE ([1.17](https://arxiv.org/html/2507.00272v1#Chx1.E17 "In Evaluation. ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering")) evaluated for several filters on the same test trajectory. The ISKF with $\overset{\sim}{k} = 1$ achieves comparable performance to WoLF, as both are only designed to reject measurement outliers.

Figure 1.6: Parameter tuning for CSTR example. Left: state estimate RMSE vs. number of iterations $\overset{\sim}{k}$. A grid search was performed to choose λx and λy for each value of $\overset{\sim}{k}$. Right: contour plot of state estimate RMSE (1.17) for different values of λx and λy.

ISKF ($\overset{\sim}{k} = 1$)

ISKF ($\overset{\sim}{k} = 2$)

ISKF ($\overset{\sim}{k} = 3$)

Table 1.2: State estimate RMSE comparison of several filtering methods for the cascaded CSTR example. All filters were tuned using the same data, and evaluated on the same test data.

ISKF ($\overset{\sim}{k} = 2$)

ISKF ($\overset{\sim}{k} = 2$)

ISKF ($\overset{\sim}{k} = 2$)

ISKF ($\overset{\sim}{k} = 2$)

Table 1.3: Results of tuning the step size η jointly with λx and λy. RMSE is evaluated on the same test data as in §1.8.1 and §1.8.2. The RMSE with no outliers is computed by removing the outliers from the test data, so that the process and measurement noises are Gaussian with fixed covariance.
(a) Vehicle tracking example

### Effect of parameters

Figure [1.6](https://arxiv.org/html/2507.00272v1#Chx1.F6 "Figure 1.6 ‣ Performance comparison. ‣ 1.8.2 Cascaded continuously-stirred tank reactor ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering") illustrates the effect of the parameters $\overset{\sim}{k}$, $\lambda_{x}$, and $\lambda_{y}$ on the performance of the ISKF on the test data. The left plot shows the best-achieved state estimate RMSE (by grid search) for each value of $\overset{\sim}{k}$. The ISKF achieves a $49\%$ improvement over the KF after two iterations, and, like in the vehicle tracking example, does not improve after three iterations. The contour plot on the right shows the state estimate RMSE for different values of $\lambda_{x}$ and $\lambda_{y}$.

### Tuning step size

As discussed in §[1.6](https://arxiv.org/html/2507.00272v1#Chx1.S6 "1.6 Parameter selection ‣ Iteratively Saturated Kalman Filtering"), the step size $\eta$ may be tuned jointly with $\lambda_{x}$ and $\lambda_{y}$ as part of the same grid search procedure. For both the vehicle tracking and CSTR examples, we found that while increasing $\eta$ can provide marginal improvements in performance, the resulting filter underperforms when there are no outliers in the simulation, i.e., the process noise and measurement noises are Gaussian with fixed covariance. In the following, we consider a grid search over $20$ values of $\eta$ between 0.1 and 100, logarithmically-spaced. The results are shown in Table [1.3(b)](https://arxiv.org/html/2507.00272v1#Chx1.T3.st2 "In Performance comparison. ‣ 1.8.2 Cascaded continuously-stirred tank reactor ‣ 1.8 Numerical experiments ‣ Iteratively Saturated Kalman Filtering"). In the vehicle tracking example, the (two-step) ISKF with a tuned value of $\eta = 2.64$ achieves a $1\%$ improvement over the ISKF with $\eta = 1$ on the test data, but underperforms by $10\%$ when the outliers are removed from the test data. In the CSTR example, the ISKF with tuned value $\eta = 1.83$ achieves a $3\%$ improvement over the ISKF with $\eta = 1$ on the test data, but underperforms by $15\%$ when the outliers are removed from the test data.

### Conclusion

We have introduced the iteratively saturated Kalman filter, a modification of the standard KF's update step that makes it robust to outliers. The method is derived as a scaled gradient method for solving a particular convex maximum a posteriori estimation problem. The steady-state variant of the ISKF matches the computational efficiency of the steady-state KF, and is well-suited for real-time applications.

## Index

## Chapter 2 About the Authors

Alan Yang is a Ph.D candidate in Electrical Engineering at Stanford University. He received the B.S. degree in Electrical Engineering from the University of Illinois at Urbana-Champaign in 2018. His research interests include convex optimization and machine learning, control systems, and signal processing.

Stephen Boyd is the Samsung Professor of Engineering, and Professor of Electrical Engineering at Stanford University. He received the A.B. degree in Mathematics from Harvard University in 1980, and the Ph.D. in Electrical Engineering and Computer Science from the University of California, Berkeley, in 1985, before joining the faculty at Stanford. His current research focus is on convex optimization applications in control, signal processing, machine learning, and finance. He is a member of the US National Academy of Engineering, a foreign member of the Chinese Academy of Engineering, and a foreign member of the National Academy of Korea.
