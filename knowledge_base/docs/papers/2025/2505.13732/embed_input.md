Backward Conformal Prediction

Topics include Control, Backward conformal prediction.

We introduce Backward Conformal Prediction, a method that guarantees conformal coverage while providing flexible control over the size of prediction sets. Unlike standard conformal prediction, which fixes the coverage level and allows the conformal set size to vary, our approach defines a rule that constrains how prediction set sizes behave based on the observed data, and adapts the coverage level accordingly. Our method builds on two key foundations: (i) recent results by Gauthier et al. on post-hoc validity using e-values, which ensure marginal coverage of the form P(Y_rm test in hat C_n^{tildealpha}(X_rm test)) >= 1 - E[tildealpha] up to a first-order Taylor approximation for any data-dependent miscoverage tildealpha, and (ii) a novel leave-one-out estimator hatalpha^(rm) LOO of the marginal miscoverage E[tildealpha] based on the calibration set, ensuring that the theoretical guarantees remain computable in practice. This approach is particularly useful in applications where large prediction sets are impractical such as medical diagnosis....

## Introduction

Conformal prediction is a widely used framework for uncertainty quantification in machine learning. It produces set-valued predictions that are guaranteed to contain the true label with high probability, regardless of the underlying data distribution.

Given a calibration set of $n$ labeled examples ${\{{(X_{i},Y_{i})}\}}_{i = 1}^{n}$ and a test point $(X_{test},Y_{test})$, all assumed to be drawn from the same unknown distribution over $\mathcal{X} \times \mathcal{Y}$, conformal prediction constructs a prediction set ${\hat{C}}_{n}^{\alpha}{(X_{test})}$ such that

The size constraint rule also affects the marginal miscoverage ${\mathbb{E}}{\lbrack\overset{\sim}{\alpha}\rbrack}$, and dynamic, anytime adjustments to this rule based on the test sample could be explored, leveraging the leave-one-out estimator for real-time miscoverage estimation.

Finally, although our analysis focuses on classification, the method can also be applied to regression, which could be a valuable direction to explore.

## Theoretical analysis

E-values offer advantages that p-values alone cannot, including post-hoc validity, which enables more flexible and adaptive inference. The connections between e-variables and post-hoc validity have been explored, either explicitly or implicitly, in the following works: Wang and Ramdas; Xu et al.; Grünwald; Ramdas and Wang; Koning, and leveraged in conformal prediction by Gauthier et al.. For completeness, we briefly review the main application of post-hoc validity with e-variables in the context of conformal prediction.

The explicit bound established in the proof of Theorem 3.1 shows that for any $\delta > 0$, we have

where the target miscoverage $\alpha \in {}$ is fixed by the practitioner. The probability is taken over both the calibration data and the test point, and the guarantee holds under the assumption that all $n + 1$ points are exchangeable,^11^1Exchangeable random variables are a sequence of random variables whose joint distribution is invariant under any permutation of their indices. a generalization of the independent and identically distributed (i.i.d.) setting.

The method uses a score function $S:{{\mathcal{X} \times \mathcal{Y}}\rightarrow{\mathbb{R}}_{+}}$,^22^2In the conformal prediction literature, scores can also be negative....
