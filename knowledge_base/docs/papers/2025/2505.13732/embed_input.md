<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Backward Conformal Prediction

Topics include Control, Backward conformal prediction.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Backward Conformal Prediction, a method that guarantees conformal coverage while providing flexible control over the size of prediction sets. Unlike standard conformal prediction, which fixes the coverage level and allows the conformal set size to vary, our approach defines a rule that constrains how prediction set sizes behave based on the observed data, and adapts the coverage level accordingly. Our method builds on two key foundations: (i) recent results by Gauthier et al. on post-hoc validity using e-values, which ensure marginal coverage of the form P(Y_rm test in hat C_n^{tildealpha}(X_rm test)) >= 1 - E[tildealpha] up to a first-order Taylor approximation for any data-dependent miscoverage tildealpha, and (ii) a novel leave-one-out estimator hatalpha^(rm) LOO of the marginal miscoverage E[tildealpha] based on the calibration set, ensuring that the theoretical guarantees remain computable in practice. This approach is particularly useful in applications where large prediction sets are impractical such as medical diagnosis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide theoretical results and empirical evidence supporting the validity of our method, demonstrating that it maintains computable coverage guarantees while ensuring interpretable, well-controlled prediction set sizes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Conformal prediction is a widely used framework for uncertainty quantification in machine learning. It produces set-valued predictions that are guaranteed to contain the true label with high probability, regardless of the underlying data distribution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given a calibration set of $n$ labeled examples $\{(X_{i},Y_{i})\}_{i=1}^{n}$ and a test point $(X_{\rm test},Y_{\rm test})$, all assumed to be drawn from the same unknown distribution over $\mathcal{X}\times\mathcal{Y}$, conformal prediction constructs a prediction set $\hat{C}_{n}^{\alpha}(X_{\rm test})$ such that where the target miscoverage $\alpha\in$ is fixed by the practitioner. The probability is taken over both the calibration data and the test point, and the guarantee holds under the assumption that all $n+1$ points are exchangeable,^11^1Exchangeable random variables are a sequence of random variables whose joint distribution is invariant under any permutation of their indices. a generalization of the independent and identically distributed (i.i.d.) setting.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The method uses a score function $S:\mathcal{X}\times\mathcal{Y}\to\mathbb{R}_{+}$,^22^2In the conformal prediction literature, scores can also be negative. In this work, we explicitly assume nonnegativity to simplify the construction of e-variables like. typically derived from a pre-trained model $f$, to evaluate how well the model's prediction $f(x)$ at input $x$ aligns with a candidate label $y$. In this paper, we assume that the scores are negatively oriented, meaning that a lower score indicates a better fit. The basic idea of conformal prediction is that, under exchangeability, the test score should behave like a typical calibration score: it should not stand out as unusually large. For a new input $X_{\rm test}$, the conformal set includes all labels $y$ such that the test score $S(X_{\rm test},y)$ is not excessively large compared to the scores from the calibration set.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Standard methods rely on comparing score ranks, which can be interpreted in terms of p-values. We refer the reader to Angelopoulos and Bates; Angelopoulos et al. for a recent overview of conformal prediction. Our work focuses on classification with a finite set of labels $\mathcal{Y}$, a setting that has been the focus of extensive research in conformal prediction.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key limitation of conformal prediction is that the size of the conformal set is entirely data-driven and *cannot be controlled in advance*. In many applications, this lack of control can be problematic: overly large prediction sets may be *too ambiguous to be useful*, especially in high-stakes or resource-constrained settings. This has motivated a growing body of work aiming to reduce the size of conformal sets while maintaining valid coverage guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we take a different perspective. Rather than fixing a desired coverage level $1-\alpha$, we fix a *size constraint rule* $\mathcal{T}$ that flexibly determines, based on the observed calibration data $\{(X_{i},Y_{i})\}_{i=1}^{n}$ and the test feature $X_{\rm test}$, the maximum allowable size of the prediction set.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Healthcare", "weight": 1.0} -->

In medical diagnosis, doctors must often infer a patient's condition $Y$ from their profile $X$ (symptoms, history, etc.) under time constraints. Standard conformal prediction, applied to calibration data $\{(X_{i},Y_{i})\}_{i=1}^{n}$, may produce prediction sets that are too large to have a practical impact on the diagnosis. Backward Conformal Prediction addresses this by allowing a size constraint which can be fixed or adaptive and data-dependent; for example, expanding the prediction set in rare or unusual cases while keeping it small and actionable for common cases. Our method ensures marginal coverage guarantees and enables doctors to validate external reliability, via the guarantee that the coverage $1-\hat{\alpha}^{\text{LOO}}\approx 1-\mathbb{E}[\tilde{\alpha}]$ remains above a desired level (e.g., 99%), striking a balance between diagnostic efficiency and rigor.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Inventory demand forecasting", "weight": 1.0} -->

In commerce, demand forecasting models predict daily sales $Y$ from features $X$ such as day of the week, weather, seasonality, and promotions. To forecast demand for a new day $X_{\rm test}$, a seller may wish to define a size constraint rule $\mathcal{T}$ that adapts to past demand variability in similar conditions: larger prediction sets for volatile periods (e.g., holidays) and smaller ones for stable days. Backward Conformal Prediction ensures valid coverage, and the seller can verify if estimated coverage $1-\hat{\alpha}^{\rm LOO}$ meets reliability goals (e.g., 95%). This balances interpretability and reliability, supporting better stocking decisions under uncertainty.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Method", "weight": 1.0} -->

Backward Conformal Prediction builds on two core theoretical components. The first is the post hoc validity of the inverses of e-values, which provides marginal coverage guarantees while ensuring that the conformal sets have controlled size. The second is the estimation of these guarantees. While the first component has been established in conformal prediction by Gauthier et al., this paper establishes the second guarantee, which is essential for the method to be used in practice and not merely serve as a theoretical benchmark. Before explicating these two key steps, we first review the foundational principles of conformal prediction with e-values, or conformal e-prediction, which serves as the basis for Backward Conformal Prediction.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Conformal e-prediction", "weight": 1.0} -->

Most conformal prediction methods rely on the comparison of score ranks, which can be interpreted using p-values. However, it is also possible to construct conformal sets using e-values, a method known as conformal e-prediction.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Post-hoc validity", "weight": 1.0} -->

E-values offer advantages that p-values alone cannot, including post-hoc validity, which enables more flexible and adaptive inference. The connections between e-variables and post-hoc validity have been explored, either explicitly or implicitly, in the following works: Wang and Ramdas; Xu et al.; Grünwald; Ramdas and Wang; Koning, and leveraged in conformal prediction by Gauthier et al.. For completeness, we briefly review the main application of post-hoc validity with e-variables in the context of conformal prediction.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Leave-one-out estimator", "weight": 1.0} -->

In this section, we introduce the leave-one-out estimator $\hat{\alpha}^{\rm LOO}$ for the marginal miscoverage term $\mathbb{E}[\tilde{\alpha}]$. Because it depends only on calibration scores and not on the test label, this estimator provides a fully computable, real-world proxy for miscoverage, enabling practitioners to obtain empirical guarantees on coverage. The key intuition is that, for large $n$, the denominator of the e-value $E^{\rm test}$ in closely approximates the expected score $\mathbb{E}[S(X,Y)]$, so $E^{\rm test}$ effectively measures how far the test score deviates from the true average of the scores.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Leave-one-out estimator", "weight": 1.0} -->

To approximate the expectation of the marginal miscoverage, we emulate pseudo-ratios $\mathbf{E}^{j}$ based on the calibration set, where we compare $S(X_{j},y)$ to the average of the calibration scores for all $y\in\mathcal{Y}$: We compute the corresponding pseudo-miscoverages: This corresponds to averaging the $n$ pseudo-miscoverage terms obtained by artificially designating each calibration score $S(X_{j},Y_{j})$ as a pseudo-test score, with the remaining scores $\{S(X_{i},Y_{i})\}_{i=1,i\neq j}^{n}$ playing the role of the pseudo-calibration set. The construction of $\hat{\alpha}^{\rm LOO}$ is schematically detailed in Figure 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Leave-one-out estimator", "weight": 1.0} -->

We summarize the Backward Conformal Prediction procedure in Algorithm 1.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Leave-one-out estimator", "weight": 1.0} -->

Input: Calibration set {(Xi, Yi)}i = 1n, test feature $X_{\rm test}$, size constraint rule 𝒯, score function S Output: Conformal set $\hat{C}_{n}^{\tilde{\alpha}}(X_{\rm test})$ of size $\leq\mathcal{T}(\{(X_{i},Y_{i})\}_{i=1}^{n},X_{\rm test})$ and an approximate marginal coverage Compute calibration score S(Xi, Yi); Select α̃ adaptively using Eq. to build conformal set Ĉnα̃ of size $\leq\mathcal{T}(\{(X_{i},Y_{i})\}_{i=1}^{n},X_{\rm test})$, satisfying guarantee; Compute approximate miscoverage $\hat{\alpha}^{\rm LOO}$ using Eq.; return

<!-- chunk {"id": "body-0019", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

In this section, we present theoretical properties satisfied by the estimator $\hat{\alpha}^{\rm LOO}$ of the marginal miscoverage $\mathbb{E}[\tilde{\alpha}]$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Let $\mu:=\mathbb{E}[S(X,Y)]$ denote the expected value of $S(X,Y)$. For each calibration point $j~\in~\{1,\dots,n\}$, we define the normalized score vector: which consists of the normalized score values of $S(X_{j},y)$ for each $y\in\mathcal{Y}$. Similarly, for the test point, we define the vector: which represents the normalized score values $S(X_{\rm test},y)$ for each $y\in\mathcal{Y}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

We show that, under certain assumptions on the size constraint rule $\mathcal{T}$, the estimator $\hat{\alpha}^{\rm LOO}$ concentrates around its target $\mathbb{E}[\tilde{\alpha}]$, with an estimation error of order $O_{P}\left(\frac{1}{\sqrt{n}}\right)$ as the calibration size $n$ increases, using the $O_{P}$ notation from van der Vaart.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Constant size constraint rule", "weight": 1.0} -->

To build intuition, we begin with the simple case where the size constraint rule $\mathcal{T}$ is a constant, which we also denote by $\mathcal{T}$ for convenience. This simplified case provides a foundation for understanding the estimator's properties under more general conditions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

The explicit bound established in the proof of Theorem 3.1 shows that for any $\delta>0$, we have with probability at least $1-\delta$. While the constants $S_{\min}$ and $S_{\max}$ are typically known to the practitioner, $\mu$ is generally not observed. However, we may still upper bound the expression by which guarantees that, as long as $\mathbb{P}(Y_{\rm test}\in\hat{C}_{n}^{\tilde{\alpha}}(X_{\rm test}))\geq 1-\mathbb{E}[\tilde{\alpha}]$, we obtain with probability at least $1-\delta$. This provides a practical decision-making tool: given a target threshold $\tau$, the practitioner can trust the conformal set with probability at least $1-\delta$ if the inequality $1-\hat{\alpha}^{\rm LOO}-R_{\delta}(n)\geq\tau$ holds, and reject it otherwise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

In addition, the variance of $\hat{\alpha}^{\rm LOO}$ decreases at rate $O\left(\frac{1}{n}\right)$, further supporting its concentration around the marginal miscoverage $\mathbb{E}[\tilde{\alpha}]$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Note that when $\mathcal{T}$ is constant and the samples are i.i.d., coverage guarantees can be estimated in a straightforward way. For each calibration point $X_{i}$, let the corresponding prediction set consist of the top-$\mathcal{T}$ scores among $\{S(X_{i},y)\}_{y\in\mathcal{Y}}$. One then checks whether the associated label $Y_{i}$ lies within this top-$\mathcal{T}$ set. The empirical frequency of miscoverage directly estimates the true miscoverage probability, and standard concentration inequalities can be used to bound its deviation. In contrast, the general case where $\mathcal{T}$ may depend on the calibration data itself requires a more sophisticated treatment. The simplified constant-size case provides an instructive foundation: it clarifies the main ideas behind our estimator and motivates the proof techniques developed in the more general, data-adaptive setting presented next.

<!-- chunk {"id": "body-0026", "role": "body", "section": "General case", "weight": 1.0} -->

In the general case, we can also prove that the estimator $\hat{\alpha}^{\rm LOO}$ is consistent, provided that the size constraint rule preserves a form of stability for the miscoverages.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

We demonstrate through an image classification experiment how the estimator $\hat{\alpha}^{\rm LOO}$ effectively approximates the true miscoverage $\mathbb{E}[\tilde{\alpha}]$, showcasing the effectiveness of Backward Conformal Prediction. In this section, we conduct experiments using a constant size constraint rule $\mathcal{T}$. Additional details and experiments are provided in Appendix B, starting with a binary classification example to motivate the need for controlling prediction set sizes, followed by an image classification experiment using a more complex data-dependent size constraint rule.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our approach is evaluated on the CIFAR-10 dataset, which consists of 50,000 training images and 10,000 test images across 10 classes. For prediction, we use an EfficientNet-B0 model trained on the full training set. This model $f$ is treated as a black box that yields predictions. The model is trained to minimize the cross-entropy loss using stochastic gradient descent (SGD) with a learning rate of $0.1$, momentum $0.9$, weight decay $5\times 10^{-4}$, and cosine annealing over 100 epochs. We use a batch size of 512 and apply standard data augmentation during training. At the end of training, the model $f$ achieves a training accuracy of $98.6\%$ and a test accuracy of $91.1\%$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the estimation $\hat{\alpha}^{\rm LOO}\approx\mathbb{E}[\tilde{\alpha}]$ across various calibration sizes, $n\in\{100,1000,5000\}$, and prediction set sizes $\mathcal{T}\in\{1,2,3\}$. All the experiments are repeated $N=200$ times. In each run, we sample a calibration set $\{(X_{i},Y_{i})\}_{i=1}^{n}$ of size $n$ uniformly at random from the test set. We then compute scores using the cross-entropy loss, defined: where $p_{f}(y|x)$ is the predicted softmax probability by $f$ for class $y$ given feature $x$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

From the remaining test samples (i.e., not included in the calibration set), we draw one point $(X_{\rm test},Y_{\rm test})$ uniformly at random to serve as the test point.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

Based on the test features and the calibration set, we construct a conformal set $\hat{C}_{n}^{\tilde{\alpha}}(X_{\rm test})$ of size at most $\mathcal{T}$, along with an estimated coverage level $1-\hat{\alpha}^{\rm LOO}$, using the output of Algorithm 1. Both $\tilde{\alpha}$ and the intermediate $\tilde{\alpha}_{j}$ used to compute $\hat{\alpha}^{\rm LOO}$ are computed via binary search over $\alpha\in$: we seek the smallest $\alpha$ such that the number of labels $y$ with $\mathbf{E}^{\rm test}_{y}<1/\alpha$ (respectively, $\mathbf{E}^{j}_{y}<1/\alpha$) is at most $\mathcal{T}$. The search stops when the candidate value of $\alpha$ is within a tolerance of 0.005 from the optimal value.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We report the results averaged over the $N$ runs in Figure 3. We plot the histogram of the $N$ values of $1-\tilde{\alpha}$ obtained across runs in green, along with their expected value $1-\mathbb{E}[\tilde{\alpha}]$ shown as a green dashed line. Overlaid on this, we display the histogram of the corresponding $N$ leave-one-out estimators $1-\hat{\alpha}^{\rm LOO}$ in blue. A blue dashed vertical line indicates the average value of $1-\hat{\alpha}^{\rm LOO}$ for visualization. We also plot the empirical coverage rate $\mathbb{P}(Y_{\rm test}\in\hat{C}_{n}^{\tilde{\alpha}}(X_{\rm test}))$ as a red dashed line.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Recall that the true coverage probability $\mathbb{P}(Y_{\rm test}\in\hat{C}_{n}^{\tilde{\alpha}}(X_{\rm test}))$ satisfies up to a first-order Taylor approximation. In our experiments, we observe that the empirical coverage probability depicted by the red dashed line consistently exceeds the empirical coverage $1-\mathbb{E}[\tilde{\alpha}]$ depicted by the green dashed line. This behavior supports the validity of the first-order Taylor approximation used to derive in our method. Furthemore, while the values of $1-\tilde{\alpha}$ can exceed the coverage probability, especially for small $n$, the coverage always remain above $1-\mathbb{E}[\tilde{\alpha}]$, aligning with our theoretical marginal guarantees.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

We also observe that the leave-one-out estimators $\hat{\alpha}^{\rm LOO}$ closely approximate the marginal miscoverage $\mathbb{E}[\tilde{\alpha}]$, with the approximation improving as the calibration size $n$ increases, as suggested by Theorems 3.1 and 3.3. Note that the histograms of $\hat{\alpha}^{\rm LOO}$ and $\tilde{\alpha}$ may differ, but this is expected, as $\hat{\alpha}^{\rm LOO}$ targets $\mathbb{E}[\tilde{\alpha}]$ rather than higher-order properties. These results show that practitioners can effectively make use of available calibration data to approximate marginal coverage guarantees through the leave-one-out estimator.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced Backward Conformal Prediction, a novel framework that prioritizes controlling the prediction set size over guarantees of fixed coverage levels. Built on e-value-based inference, our method enables data-dependent miscoverage and uses a leave-one-out estimator to approximate marginal miscoverage. This approach offers a flexible, principled alternative in settings where interpretability and set size control are critical, such as medical diagnosis. Our theoretical and empirical results show valid coverage guarantees while enforcing a user-specified size constraint. These findings open new avenues for adaptive conformal prediction and data-driven control that go beyond mere coverage.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Backward Conformal Prediction differs from standard conformal prediction in a fundamental way: it allows practitioners to control the size of prediction sets while simultaneously estimating coverage. In standard conformal prediction, coverage is guaranteed, but the size of each prediction set is uncontrolled and can vary widely. Our approach provides more actionable information, enabling practitioners to adjust the size constraint if the resulting coverage is too low. While the coverage guarantee in Backward Conformal Prediction might be slightly conservative due to the use of Markov's inequality, this trade-off allows for principled decisions about the balance between set size and reliability, offering a more informative and flexible framework for practical applications.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

While we focused on miscoverage definitions with fixed set sizes, the method is applicable to any data-dependent miscoverage. Future work could explore alternative formulations and investigate real-world applications under different constraint rules. Additionally, the stability assumption in Theorem 3.5 could likely be relaxed under regularity conditions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The size constraint rule also affects the marginal miscoverage $\mathbb{E}[\tilde{\alpha}]$, and dynamic, anytime adjustments to this rule based on the test sample could be explored, leveraging the leave-one-out estimator for real-time miscoverage estimation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, although our analysis focuses on classification, the method can also be applied to regression, which could be a valuable direction to explore.
