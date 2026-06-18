Minimum Volume Conformal Sets for Multivariate Regression

Topics include Conformal prediction, Multivariate regression, Prediction sets, Minimum-volume sets, Nonconformity scores, Norm balls, Distribution-free inference, Uncertainty quantification.

Proposes an optimization-driven way to learn conformal prediction sets for multivariate regression while directly targeting small set volume. The method turns minimum-volume coverage into a learned nonconformity score over norm-ball prediction sets, making conformal multivariate uncertainty more adaptive than fixed-shape constructions.

Conformal prediction provides a principled framework for constructing predictive sets with finite-sample validity. While much of the focus has been on univariate response variables, existing multivariate methods either impose rigid geometric assumptions or rely on flexible but computationally expensive approaches that do not explicitly optimize prediction set volume. We propose an optimization-driven framework based on a novel loss function that directly learns minimum-volume covering sets while ensuring valid coverage. This formulation naturally induces a new nonconformity score for conformal prediction, which adapts to the residual distribution and covariates. Our approach optimizes over prediction sets defined by arbitrary norm balls, including single and multi-norm formulations. Additionally, by jointly optimizing both the predictive model and predictive uncertainty, we obtain prediction sets that are tight, informative, and computationally efficient, as demonstrated in our experiments on real-world datasets.

## Introduction

In predictive modeling, quantifying uncertainty is often as crucial as making accurate predictions. Traditional point estimates provide limited insight into predictive accuracy, whereas prediction sets offer a more robust alternative by identifying regions that contain the true outcome with high probability. Conformal prediction Vovk et al.; Shafer and Vovk; Angelopoulos et al. provides a model-agnostic framework for constructing such sets with finite-sample validity, ensuring that the true response is captured at least $1 - \alpha$ fraction of the time without requiring strong distributional assumptions.

To address these limitations, we introduce a framework for constructing multivariate conformal prediction sets that minimize volume while maintaining valid coverage. Rather than imposing a fixed structure, our approach learns the optimal shape of the prediction set by optimizing over flexible geometric representations, including adaptive norm-based formulations. This optimization extends beyond the prediction set itself, as we jointly learn the predictive model together with the prediction set, ensuring that the predictor is aligned with the minimum-volume criterion.

## Discussion

While our approach provides a principled framework for learning minimum-volume prediction sets with finite-sample validity, several challenges remain. First, our reliance on first-order optimization methods does not guarantee avoidance of poor local minima, particularly given the inherent nonconvexity of our loss function. While our empirical results demonstrate stable performance, exploring alternative optimization strategies---such as second-order methods or tailored regularization techniques---could enhance robustness to nonconvexity.

Second, hyperparameter selection remains a critical factor. The learning rate of the matrix model, for instance, strongly influences convergence behavior, and we observed that optimal settings vary across datasets. Developing more adaptive or automated tuning strategies could improve generalization and reduce the need for manual adjustment.
