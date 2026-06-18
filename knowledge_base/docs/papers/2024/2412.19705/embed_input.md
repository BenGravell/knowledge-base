<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR

Topics include Data-driven control, Linear quadratic regulator, Semidefinite programming, Noise analysis, Robustness, Linear systems, Control theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Examines how semidefinite-programming formulations for direct data-driven LQR behave under noisy data. The paper highlights sensitivity mechanisms that matter when replacing model identification with data-dependent convex control synthesis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we study the noise sensitivity of the semidefinite program (SDP) proposed for direct data-driven infinite-horizon linear quadratic regulator (LQR) problem for discrete-time linear time-invariant systems. While this SDP is shown to find the true LQR controller in the noise-free setting, we show that it leads to a trivial solution with zero gain matrices when data is corrupted by noise, even when the noise is arbitrarily small. We then study a variant of the SDP that includes a robustness promoting regularization term and prove that regularization does not fully eliminate the sensitivity issue. In particular, the solution of the regularized SDP converges in probability also to a trivial solution.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Certainty equivalence approach and robust control approach are two alternative paradigms in learning-based control. Roughly speaking, in certainty equivalence, we *pretend* that our data is not corrupted by noise, the estimated model is the true system model, or the estimated control policy is designed based on the true system and clean data. Whereas, in robust control approach, we try to bound the effect of the noise in the data and aim to find a controller that achieves the desired properties for all possible noise values within this bound.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These two different paradigms can be applied both in the model-based setting, where system identification is followed by control design, or in direct data-driven control, where data is used directly to synthesize a controller utilizing ideas from the behavioral system theory (see, e.g.,). In the context of model-based LQR, Mania et al. show that certainty equivalence is statistically consistent and is more sample-efficient than the robust approach given. The success of certainty equivalent control, in this case, lies in the fact that there is some inherent robustness in the solutions of the Riccati equations with respect to perturbations in system matrices. That is, small perturbations in system matrices result in small changes in the corresponding optimal controller.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural question is how the certainty equivalence approach and a robust control approach compare in terms of statistical properties for direct data-driven LQR. Several works consider a robust approach for direct data-driven control for different control objectives or noise settings (e.g., ). On the other hand, De Persis and Tesi analyze a certainty equivalent approach to direct data-driven LQR, where they provide a sufficient condition for stabilizability and regularization techniques for improving noise robustness. Here, the certainty equivalence approach amounts to using the noisy data directly in the semidefinite programs developed for the noise-free case. It is observed that even small noise can lead to a violation of their proposed sufficient condition for stabilizability and the semidefinite program may favor low gain solutions. However, a thorough understanding of the noise sensitivity and statistical properties of these semidefinite programs for direct data-driven LQR is missing. In this paper, we show that the semidefinite program for direct data-driven LQR is very sensitive to noise and yields, with probability one, *trivial control gains* independent of the data even when there is an arbitrarily small amount of noise.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the robustified version also suffers from a similar issue as the length of the data trajectory used in the program goes to infinity. Therefore, neither of these approaches is statistically consistent.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is worth noting that there are recent works that propose alternative optimization formulations for direct data-driven control, solutions of which mimic the solution of the model-based certainty equivalent control. Since the controllers synthesized by these alternative formulations are equivalent to model-based certainty equivalent control, they inherit the nice statistical consistency properties of the former. Our analysis does not pertain to these alternative formulations. Similarly, our results are not directly related to the finite-horizon data-driven control problems for which some connections with model-based approaches are established since we focus on approximation of the infinite-horizon LQR gain.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A preliminary version of this paper has been submitted to. Compared with the conference version, we extend the results of certainty equivalent DDD LQR from scalar systems to multivariate systems and we also show that when the length of the data trajectory approaches infinity, the robustness promoting DDD LQR will also yield a zero state feedback gain estimate.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. In Section, we review some basic definitions from probability and data-driven control. Section LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR") reviews two formulations of the direct data-driven LQR problem from the literature. Section DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR") and Section DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR") introduces the main results of the paper together with their proofs. We provide some numerical examples in Section before concluding the paper in Section.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Results from Data-Driven Control", "weight": 1.0} -->

The following notion will be relevant in establishing our results.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Direct Data-Driven (DDD) LQR", "weight": 1.0} -->

where $\mathbf{Q} \succ 0$, $\mathbf{R} \succ 0$, and $\mathbb{E}$ denotes the expectation over the randomness from the initial state $\mathbf{x}_{0}$ and the process noise $\mathbf{w}_{t}$. We assume $(\mathbf{A},\mathbf{B})$ is controllable throughout the paper.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Direct Data-Driven (DDD) LQR", "weight": 1.0} -->

Then, the solution of ) is $\mathbf{u}_{t} = {- {\mathbf{K}_{\operatorname{lqr}}\mathbf{x}_{t}}}$ with the optimal state feedback gain given by

<!-- chunk {"id": "body-0014", "role": "body", "section": "Direct Data-Driven (DDD) LQR", "weight": 1.0} -->

In direct data-driven control, the parameters $\mathbf{A}$ and $\mathbf{B}$ are unknown and the goal is to directly estimate $\mathbf{K}_{\operatorname{lqr}}$ from data without explicitly estimating $\mathbf{A}$ and $\mathbf{B}$. We assume the data is collected offline by driving the system with a random input such that $\mathbf{u}_{t}\overset{i.i.d.}{\sim}\mathcal{N}{(0,{\sigma_{u}^{2}\mathbf{I}_{m}})}$ with $\sigma_{u} > 0$, and this input is independent of the noise process and the initial condition.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Direct Data-Driven (DDD) LQR", "weight": 1.0} -->

The following result shows that when the system does not have any noise (i.e., $\mathbf{w}_{t} = 0$ for all $t$) and a persistency of excitation condition holds (which can be shown to hold with probability $1$ when the input is Gaussian as assumed), we have $\mathbf{K}_{ce} = \mathbf{K}_{\operatorname{lqr}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Inconsistency of CE DDD LQR", "weight": 1.0} -->

Our first main result shows that in the presence of noise, with probability $1$, the solution of the certainty equivalence DDD LQR problem in ) is independent of the data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1", "weight": 1.0} -->

where $\delta_{t}\overset{i.i.d.}{\sim}\mathcal{N}{(0,{\sigma_{\delta}^{2}\mathbf{I}_{n}})}$ is the measurement noise. Now, if we form the data matrices in ) using the measurements $\mathbf{x}_{t}^{m}$ in place of $\mathbf{x}_{t}$ and solve ), the resulting gain will again be zero with probability one.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Next, we present a corollary that provides an alternative interpretation of Lemma. ‣ 3 Direct Data-Driven (DDD) LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR").

<!-- chunk {"id": "body-0019", "role": "body", "section": "Proofs of Theorem 2 DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR\") and Corollary 1 DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR\")", "weight": 1.0} -->

We start by defining a change of variables to obtain a noise-free LTI system by treating the noise as an additional input. To this end, consider

<!-- chunk {"id": "body-0020", "role": "body", "section": "Proofs of Theorem 2 DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR\") and Corollary 1 DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR\")", "weight": 1.0} -->

We denote the input trajectory matrix as $\mathbf{V}_{0} = \begin{bmatrix}
\mathbf{U}_{0}^{\top} & \mathbf{W}_{0}^{\top}
\end{bmatrix}^{\top}$. We use the fundamental lemma, which first appeared in Corollary 2 of, in our proof. Its detailed proof can be found.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Inconsistency of RP DDD LQR", "weight": 1.0} -->

Next, we analyze the solution of RP DDD LQR problem in ) as the data trajectory length $T$ goes to infinity.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present three numerical experiments to validate our main theoretical results. The experiments include CE, RP with a fixed regularization parameter, and RP with an increasing regularization parameter.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

where the spectral radius of $\mathbf{A}$ is $1.01$, indicating that this LTI system is open-loop unstable. The initial state $\mathbf{x}_{0} = \mathbf{0}_{2 \times 1}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "CE DDD LQR", "weight": 1.0} -->

In this part, we validate the theoretical results of CE DDD LQR in Theorem DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR") and compare it with the noiseless case in Theorem. ‣ 3 Direct Data-Driven (DDD) LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR"). We consider the specific system. The data matrices are collected offline by exciting the system with random inputs, sampled as $\mathbf{u}_{t}\overset{i.i.d.}{\sim}\mathcal{N}{(0,\sigma_{u}^{2})}$, with $\sigma_{u}^{2} = 1$. The trajectory length is set to $T = 50$. The implementation of CE DDD LQR in ) is performed using YALMIP with MOSEK in MATLAB.

<!-- chunk {"id": "body-0025", "role": "body", "section": "CE DDD LQR", "weight": 1.0} -->

As expected, for the noiseless case ($\sigma_{w}^{2} = 0$), the LQR gain estimate computed by CE DDD LQR is ${\mathbf{K}_{ce} = \begin{bmatrix}
\end{bmatrix}},$ which matches the true LQR gain. In contrast, for a small noise level ($\sigma_{w}^{2} = 0.00001$), the LQR gain estimate obtained from DDD LQR is ${\mathbf{K}_{ce} = \begin{bmatrix}
\end{bmatrix}}.$ This estimate results in an unstable closed-loop system for the system, highlighting that CE DDD LQR is highly sensitive to noise, even at very low levels. This observation corroborates the validity of Theorem DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR").

<!-- chunk {"id": "body-0026", "role": "body", "section": "RP DDD LQR with a Fixed Regularization Parameter", "weight": 1.0} -->

In this section, we verify Theorem DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR") for RP DDD LQR in ) with a fixed regularization parameter $\eta = 1$. Similar to the previous section for CE DDD LQR, we consider the same specific system dynamics as described, with the inputs in the data matrices unchanged. The spectral norm of the noise covariance matrix is set to $\sigma_{w}^{2} = 1$. The results are illustrated in Fig. and Fig.. For each horizon $T$, we run $10$ independent experiments to compute the mean and the variance of each respective data point. From Fig., we have that when horizon $T$ increases, $\|\mathbf{K}_{rp}\|$ with $\sigma_{w} > 0$ approaches zero, by which Theorem DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR") is verified.

<!-- chunk {"id": "body-0027", "role": "body", "section": "RP DDD LQR with a Fixed Regularization Parameter", "weight": 1.0} -->

Interestingly, when the data is generated from a system not subject to noise, with a fixed regularization parameter ($\eta = 1$), $\|\mathbf{K}_{rp}\|$ converges to $\|\mathbf{K}_{\operatorname{lqr}}\|$ as the trajectory length $T$ increases as shown in Fig. (indeed, $\mathbf{K}_{rp}$ converges to $\mathbf{K}_{\operatorname{lqr}}$).

<!-- chunk {"id": "body-0028", "role": "body", "section": "RP DDD LQR with a Fixed Regularization Parameter", "weight": 1.0} -->

Additionally, based on Fig., we see that as $T$ increases, $\|{\mathbf{X}_{0}\mathbf{Y}_{rp}^{\ast}}\|$ approaches $1$, $\|{\mathbf{U}_{0}\mathbf{Y}_{rp}^{\ast}}\|$ approaches $0$, and $\|\mathbf{K}_{rp}\|$ with $\sigma_{w} = 0$ approaches $0$. In fact, it is possible to show that as $T$ approaches infinity, any optimal solution of RP DDD LQR converges in probability to a solution of equation ).

<!-- chunk {"id": "body-0029", "role": "body", "section": "RP DDD LQR with an Increasing Regularization Parameter", "weight": 1.0} -->

This section investigates what happens if the regularization parameter $\eta$ is increased with increasing horizon length $T$. The bound in ) suggests that if $\eta$ increases with the data trajectory length $T$, the optimal objective value of ) may not converge to ${trace}{(\mathbf{Q})}$, thereby resulting in a nontrivial feedback gain. Motivated by this intuition, we set $\eta = {10T}$. As shown in Fig., as the data trajectory length $T$ increases, $\|\mathbf{K}_{rp}\|$ with $\sigma_{w} > 0$ does not approach zero. This observation highlights the potential of increasing $\eta$ systematically to obtain more reliable solutions, a direction that might be worthwhile to theoretically investigate.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we provide statistical analysis for two direct data-driven LQR methods in the presence of noise. Our results indicate that these methods are not statistically consistent. Therefore a "certainty equivalence" approach that uses the original SDPs with noisy data is not appropriate. This is in contrast to model-based techniques, where certainty equivalence is known to be statistically consistent and sample-efficient. The identified limitations of the "certainty equivalence" approach in direct data-driven control underscores the necessity of robust direct data-driven control methods. Our future work will focus on understanding the statistical properties of such methods.
