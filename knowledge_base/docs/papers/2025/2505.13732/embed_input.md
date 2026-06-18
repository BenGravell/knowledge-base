Backward Conformal Prediction

Topics include Control, Backward conformal prediction.

We introduce Backward Conformal Prediction, a method that guarantees conformal coverage while providing flexible control over the size of prediction sets. Unlike standard conformal prediction, which fixes the coverage level and allows the conformal set size to vary, our approach defines a rule that constrains how prediction set sizes behave based on the observed data, and adapts the coverage level accordingly. Our method builds on two key foundations: (i) recent results by Gauthier et al. on post-hoc validity using e-values, which ensure marginal coverage of the form P(Y_rm test in hat C_n^{tildealpha}(X_rm test)) >= 1 - E[tildealpha] up to a first-order Taylor approximation for any data-dependent miscoverage tildealpha, and (ii) a novel leave-one-out estimator hatalpha^(rm) LOO of the marginal miscoverage E[tildealpha] based on the calibration set, ensuring that the theoretical guarantees remain computable in practice. This approach is particularly useful in applications where large prediction sets are impractical such as medical diagnosis.

## Introduction

Conformal prediction is a widely used framework for uncertainty quantification in machine learning. It produces set-valued predictions that are guaranteed to contain the true label with high probability, regardless of the underlying data distribution.

where the target miscoverage $\alpha \in {}$ is fixed by the practitioner. The probability is taken over both the calibration data and the test point, and the guarantee holds under the assumption that all $n + 1$ points are exchangeable,^11^1Exchangeable random variables are a sequence of random variables whose joint distribution is invariant under any permutation of their indices. a generalization of the independent and identically distributed (i.i.d.) setting.

The method uses a score function $S:{{\mathcal{X} \times \mathcal{Y}}\rightarrow{\mathbb{R}}_{+}}$,^22^2In the conformal prediction literature, scores can also be negative. In this work, we explicitly assume nonnegativity to simplify the construction of e-variables like. typically derived from a pre-trained model $f$, to evaluate how well the model's prediction $f{(x)}$ at input $x$ aligns with a candidate label $y$. In this paper, we assume that the scores are negatively oriented, meaning that a lower score indicates a better fit.

## Conclusion

We introduced Backward Conformal Prediction, a novel framework that prioritizes controlling the prediction set size over guarantees of fixed coverage levels. Built on e-value-based inference, our method enables data-dependent miscoverage and uses a leave-one-out estimator to approximate marginal miscoverage. This approach offers a flexible, principled alternative in settings where interpretability and set size control are critical, such as medical diagnosis. Our theoretical and empirical results show valid coverage guarantees while enforcing a user-specified size constraint.

Backward Conformal Prediction differs from standard conformal prediction in a fundamental way: it allows practitioners to control the size of prediction sets while simultaneously estimating coverage. In standard conformal prediction, coverage is guaranteed, but the size of each prediction set is uncontrolled and can vary widely. Our approach provides more actionable information, enabling practitioners to adjust the size constraint if the resulting coverage is too low.
