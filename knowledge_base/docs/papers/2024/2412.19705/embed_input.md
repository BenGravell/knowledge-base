Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR

Topics include Data-driven control, Linear quadratic regulator, Semidefinite programming, Noise analysis, Robustness, Linear systems, Control theory.

Examines how semidefinite-programming formulations for direct data-driven LQR behave under noisy data. The paper highlights sensitivity mechanisms that matter when replacing model identification with data-dependent convex control synthesis.

In this paper, we study the noise sensitivity of the semidefinite program (SDP) proposed for direct data-driven infinite-horizon linear quadratic regulator (LQR) problem for discrete-time linear time-invariant systems. While this SDP is shown to find the true LQR controller in the noise-free setting, we show that it leads to a trivial solution with zero gain matrices when data is corrupted by noise, even when the noise is arbitrarily small. We then study a variant of the SDP that includes a robustness promoting regularization term and prove that regularization does not fully eliminate the sensitivity issue. In particular, the solution of the regularized SDP converges in probability also to a trivial solution.

## Introduction

Certainty equivalence approach and robust control approach are two alternative paradigms in learning-based control. Roughly speaking, in certainty equivalence, we *pretend* that our data is not corrupted by noise, the estimated model is the true system model, or the estimated control policy is designed based on the true system and clean data. Whereas, in robust control approach, we try to bound the effect of the noise in the data and aim to find a controller that achieves the desired properties for all possible noise values within this bound.

These two different paradigms can be applied both in the model-based setting, where system identification is followed by control design, or in direct data-driven control, where data is used directly to synthesize a controller utilizing ideas from the behavioral system theory (see, e.g.,). In the context of model-based LQR, Mania et al. \[\] show that certainty equivalence is statistically consistent and is more sample-efficient than the robust approach given in \[\]....

## Conclusion and Future Work

In this paper, we provide statistical analysis for two direct data-driven LQR methods in the presence of noise. Our results indicate that these methods are not statistically consistent. Therefore a "certainty equivalence" approach that uses the original SDPs with noisy data is not appropriate. This is in contrast to model-based techniques, where certainty equivalence is known to be statistically consistent and sample-efficient. The identified limitations of the "certainty equivalence" approach in direct data-driven control underscores the necessity of robust direct data-driven control methods \[\]....

### Lemma 4

Based on Theorem DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR"), we have that when $T \geq {{{({m + n})}{({n + 1})}} + n}$, the data-driven feedback gain based on certainty equivalence DDD LQR in ) is equal to $\mathbf{0}_{m \times n}$ with probability one. Hence, $\mathbf{K}_{ce}$ will not converge to $\mathbf{K}_{\operatorname{lqr}}$ no matter how large $T$ is, i.e., $\mathbf{K}_{ce}$ is an inconsistent estimator of $\mathbf{K}_{\operatorname{lqr}}$. The proof of this theorem is given in Section DDD LQR ‣ Noise Sensitivity of the Semidefinite Programs for Direct Data-Driven LQR").

### Theorem 3
